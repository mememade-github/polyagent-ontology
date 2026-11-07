#!/usr/bin/env python3
"""Frozen QDR numeric analysis; no model requests and no corpus text in score output.

CLI:
  analyze.py packet --manifest manifest.json --units judge-units.json --out packet.json --mapping private-map.json
  analyze.py score --manifest manifest.json --units judge-units.json --gold gold.json --judgments labels.json --validity validity.json --out score.json
  analyze.py self-test --out analysis-stub.json

Manifest: {"entries":[{"arm":...,"seed":7,"path":".../result.json"}, ...]}.
Relative result paths resolve against the manifest directory. Units is a list.
Gold: {"facts":[{"semantic_id":...,"unit":...,"id":optional}, ...]}.
Judgments: {"labels":[{"id":...,"status":"true|false|ambiguous",
  "semantic_id":...,"gold_ids":[...],"reason":...}],"missing_gold":[],"ambiguities":[]}.
Validity: controls_passed, gold_complete, gold_review_passed, blinding_intact,
rules_unchanged, locks_verified must be true; truncation_events must be zero;
acquisition_wall_seconds must be <=1800. Optional checks:[{id,passed}], model_digest,
and locks:{absolute_file_path:sha256} are independently checked when supplied.
External validity attestations are reported separately from numerical thresholds.
All packet/mapping/score files are created exclusively, mode 0600.
"""

import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import random
import sys


SEEDS = (7, 11, 19)
ARMS = ('onto', 'original-random', 'original-coverage', 'fact-random', 'fact-coverage')
COMPARISONS = {
    'Hq-Fact': ('fact-coverage', 'fact-random'),
    'Hq-original': ('original-coverage', 'original-random'),
    'Honto': ('fact-coverage', 'onto'),
}
SHUFFLE_SEED = 20261107001
BOOL_ATTESTATIONS = ('controls_passed', 'gold_complete', 'gold_review_passed',
                     'blinding_intact', 'rules_unchanged', 'locks_verified')
DURATION_FIELDS = ('total_duration', 'load_duration', 'prompt_eval_duration', 'eval_duration')


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def claim_id(unit, claim):
    """Concept, quote, arm, seed and lens cannot affect an opaque claim ID."""
    payload = {'unit': unit, **{k: claim[k] for k in ('subject', 'relation', 'object')}}
    return hashlib.sha256(canonical(payload).encode('utf8')).hexdigest()


def cell(unit):
    return (tuple(sorted(set(unit['tags']))), bool(unit['anchor']))


def encoded_cell(value):
    return [list(value[0]), value[1]]


def finite_number(value):
    return type(value) in (int, float) and math.isfinite(value) and value >= 0


def valid_int(value, minimum=0):
    return type(value) is int and value >= minimum


def build_packet(runs, units):
    """Pure builder. Runs use {arm, seed, result}; private mapping preserves order.

    All active occurrences map to a label. Equal unit/triple occurrences share
    one judge item, while occurrences and first-origin ordering are retained.
    """
    issues, by_unit, claims, mappings = [], {}, {}, []
    for u in units:
        if not isinstance(u, dict) or not isinstance(u.get('unit'), str):
            issues.append('invalid_unit')
            continue
        if u['unit'] in by_unit:
            issues.append('duplicate_unit')
        try:
            cell(u)
            if not isinstance(u['text'], str) or not u['text'].strip() or not isinstance(u.get('source_text', u['text']), str):
                raise ValueError()
        except (KeyError, TypeError, ValueError):
            issues.append('invalid_unit_schema')
            continue
        by_unit[u['unit']] = u
    for run in runs:
        mapped = {'arm': run.get('arm'), 'seed': run.get('seed'), 'claims': []}
        result = run.get('result', {})
        active = result.get('active')
        if not isinstance(active, list):
            issues.append('missing_active_list')
            active = []
        for index, record in enumerate(active):
            if not isinstance(record, dict):
                issues.append('invalid_active_record')
                continue
            u = by_unit.get(record.get('unit'))
            claim = record.get('claim')
            if u is None or not isinstance(claim, dict) or not all(
                    isinstance(claim.get(k), str) and claim[k].strip()
                    for k in ('subject', 'relation', 'object')):
                issues.append('invalid_active_claim')
                continue
            ident = claim_id(u['unit'], claim)
            claims.setdefault(ident, {'id': ident, 'unit': u['unit'],
                'source_text': u.get('source_text', u['text']),
                'claim': {k: claim[k] for k in ('subject', 'relation', 'object')}})
            mapped['claims'].append({'id': ident, 'unit': u['unit'],
                                    'cell': encoded_cell(cell(u)), 'active_index': index})
            if record.get('outcome') != 'active_provisional':
                issues.append('nonactive_record_in_active')
            if u.get('context_dependent'):
                issues.append('deferred_unit_active')
            if record.get('cell') is not None and record['cell'] != encoded_cell(cell(u)):
                # In-memory controller fixtures may contain tuples before JSON serialization.
                if canonical(record['cell']) != canonical(encoded_cell(cell(u))):
                    issues.append('active_cell_mismatch')
        mappings.append(mapped)
    ordered = [claims[k] for k in sorted(claims)]
    random.Random(SHUFFLE_SEED).shuffle(ordered)
    return {'claims': ordered}, {'runs': mappings, 'issues': sorted(set(issues)),
                               'active_occurrences': sum(len(r['claims']) for r in mappings)}


def accounting_summary(result, seed):
    """Validate driver accounting without trusting its status alone."""
    reasons, summary = [], {'valid': False}
    a = result.get('accounting')
    if not isinstance(a, dict):
        return summary, ['missing_accounting']
    calls = a.get('calls')
    if not isinstance(calls, list):
        return summary, ['missing_call_accounting']
    if a.get('seed') != seed:
        reasons.append('accounting_seed_mismatch')
    for name, expected in (('cap', 24), ('token_limit', 64000), ('deadline_seconds', 900)):
        if a.get(name) != expected or type(a.get(name)) not in (int, float):
            reasons.append('unequal_' + name)
    if not valid_int(a.get('attempts')) or a['attempts'] != len(calls) or len(calls) > 24:
        reasons.append('invalid_attempt_count')
    if not valid_int(a.get('actual_tokens')) or a['actual_tokens'] > 64000:
        reasons.append('invalid_actual_tokens')
    if not finite_number(a.get('wall_seconds')) or a['wall_seconds'] > 900:
        reasons.append('invalid_arm_wall')
    if not isinstance(a.get('digest'), str) or not a['digest']:
        reasons.append('missing_model_digest')
    prompt = output = running = 0
    server = {k: 0 for k in DURATION_FIELDS}
    for c in calls:
        if not isinstance(c, dict):
            reasons.append('invalid_call_record')
            continue
        needed = ('bound', 'reservation', 'prompt_eval_count', 'eval_count')
        if not all(valid_int(c.get(k), 1) for k in needed):
            reasons.append('missing_call_tokens')
            continue
        if c['bound'] + c['reservation'] >= 3800 or running + c['bound'] + c['reservation'] > 64000:
            reasons.append('invalid_reservation')
        prompt += c['prompt_eval_count']
        output += c['eval_count']
        running = prompt + output
        if c['prompt_eval_count'] > c['bound'] or c['eval_count'] > c['reservation']:
            reasons.append('exceeded_call_reservation')
        if not finite_number(c.get('seconds')):
            reasons.append('missing_call_wall')
        if c.get('status') != 'ok' or c.get('done_reason') != 'stop':
            reasons.append('incomplete_call')
        for k in DURATION_FIELDS:
            if not valid_int(c.get(k)):
                reasons.append('missing_server_duration')
            else:
                server[k] += c[k]
    if a.get('actual_tokens') != prompt + output:
        reasons.append('token_total_mismatch')
    summary.update(attempts=len(calls), prompt_tokens=prompt, output_tokens=output,
                   actual_tokens=a.get('actual_tokens') if valid_int(a.get('actual_tokens')) else None,
                   wall_seconds=a.get('wall_seconds') if finite_number(a.get('wall_seconds')) else None,
                   server_duration_ns=server, valid=not reasons)
    return summary, sorted(set(reasons))


def threshold_tests(treatment, comparator):
    p1 = Fraction(treatment['T'], treatment['T'] + treatment['F']) if treatment['T'] + treatment['F'] else Fraction(0)
    p0 = Fraction(comparator['T'], comparator['T'] + comparator['F']) if comparator['T'] + comparator['F'] else Fraction(0)
    margin = max(1, (comparator['T'] + 9) // 10)
    tests = {'precision_at_least_0_90': p1 >= Fraction(9, 10),
             'precision_nondecrease': p1 >= p0,
             'correct_gain': treatment['T'] >= comparator['T'] + margin,
             'gold_cell_recall_nondecrease': treatment['gold_cells_covered'] >= comparator['gold_cells_covered']}
    return {'tests': tests, 'required_correct_gain': margin, 'passed': all(tests.values())}


def score(runs, units, gold, judgments, validity):
    """Sanitized numeric diagnostics and globally gated verdicts; no pooled winner."""
    packet, mapping = build_packet(runs, units)
    reasons = list(mapping['issues'])
    unit_map = {u['unit']: u for u in units if isinstance(u, dict) and isinstance(u.get('unit'), str)}
    expected = {(arm, seed) for arm in ARMS for seed in SEEDS}
    observed = [(r.get('arm'), r.get('seed')) for r in runs]
    if set(observed) != expected or len(observed) != len(expected):
        reasons.append('incomplete_or_duplicate_run_matrix')
    if any(type(seed) is not int for _, seed in observed):
        reasons.append('invalid_seed_type')
    facts = gold.get('facts') if isinstance(gold, dict) else None
    if not isinstance(facts, list):
        facts = []
        reasons.append('invalid_gold_schema')
    semantic_ids, refs, gold_cells = set(), {}, set()
    for f in facts:
        if not isinstance(f, dict) or not isinstance(f.get('semantic_id'), str) or not f['semantic_id'] or f.get('unit') not in unit_map:
            reasons.append('invalid_gold_fact')
            continue
        semantic_ids.add(f['semantic_id'])
        refs.setdefault(f['semantic_id'], set()).add(f['semantic_id'])
        if isinstance(f.get('id'), str):
            refs.setdefault(f['id'], set()).add(f['semantic_id'])
        gold_cells.add(cell(unit_map[f['unit']]))
    if not gold_cells:
        reasons.append('empty_gold_cell_denominator')
    if isinstance(gold, dict) and gold.get('complete') is False:
        reasons.append('gold_declared_incomplete')
    if isinstance(gold, dict) and gold.get('ambiguities'):
        reasons.append('gold_ambiguity')

    wanted = {r['id'] for r in packet['claims']}
    labels = {}
    raw_labels = judgments.get('labels') if isinstance(judgments, dict) else None
    if not isinstance(raw_labels, list):
        raw_labels = []
        reasons.append('missing_judgment_labels')
    for label in raw_labels:
        if not isinstance(label, dict) or not isinstance(label.get('id'), str):
            reasons.append('invalid_judgment_label')
            continue
        ident = label['id']
        if ident in labels:
            reasons.append('duplicate_judgment_label')
        labels[ident] = label
        status, semantic = label.get('status'), label.get('semantic_id')
        if status not in ('true', 'false', 'ambiguous'):
            reasons.append('invalid_judgment_status')
        if status == 'ambiguous':
            reasons.append('ambiguous_judgment')
        if status in ('true', 'false') and (not isinstance(semantic, str) or not semantic):
            reasons.append('missing_semantic_equivalence_id')
        if status == 'true':
            gold_refs = label.get('gold_ids')
            if semantic not in semantic_ids:
                reasons.append('supported_claim_absent_from_gold')
            if not isinstance(gold_refs, list) or not gold_refs or not all(
                    isinstance(g, str) and g in refs and semantic in refs[g] for g in gold_refs):
                reasons.append('invalid_true_gold_reference')
    if wanted - set(labels):
        reasons.append('unlabeled_active_claim')
    if set(labels) - wanted:
        reasons.append('unknown_judgment_claim')
    for name in ('missing_gold', 'ambiguities'):
        if not isinstance(judgments, dict) or not isinstance(judgments.get(name), list):
            reasons.append('missing_judge_' + name + '_audit')
        elif judgments[name]:
            reasons.append('judge_' + name)

    attestations = {key: validity.get(key) is True for key in BOOL_ATTESTATIONS}
    for key, passed in attestations.items():
        if not passed:
            reasons.append('validity_' + key)
    if type(validity.get('truncation_events')) is not int or validity['truncation_events'] != 0:
        reasons.append('truncation_audit_failed')
    elapsed = validity.get('acquisition_wall_seconds')
    if not finite_number(elapsed) or elapsed > 1800:
        reasons.append('invalid_global_acquisition_wall')
    if 'checks' in validity:
        if not isinstance(validity['checks'], list) or not all(isinstance(c, dict) and c.get('passed') is True for c in validity['checks']):
            reasons.append('failed_validity_check')
    lock_count = 0
    if 'locks' in validity:
        if not isinstance(validity['locks'], dict) or not validity['locks']:
            reasons.append('invalid_lock_manifest')
        else:
            for path, digest in validity['locks'].items():
                try:
                    if not Path(path).is_absolute() or not isinstance(digest, str) or hashlib.sha256(Path(path).read_bytes()).hexdigest() != digest:
                        reasons.append('locked_file_modified')
                    else:
                        lock_count += 1
                except (OSError, TypeError, ValueError):
                    reasons.append('locked_file_unavailable')

    metrics, run_map, digests, accounting_reasons = {}, {}, set(), {}
    for run, mapped in zip(runs, mapping['runs']):
        arm, seed = run.get('arm'), run.get('seed')
        if (arm, seed) not in expected:
            continue
        result = run.get('result', {})
        account, account_issues = accounting_summary(result, seed)
        if result.get('status') != 'complete':
            account_issues.append('run_not_complete')
        if not isinstance(result.get('pending'), list):
            account_issues.append('missing_pending_ledger')
        ledger = result.get('ledger')
        if not isinstance(ledger, list) or Counter(x.get('unit') for x in ledger if isinstance(x, dict)) != Counter(unit_map.keys()):
            account_issues.append('incomplete_unit_ledger')
        else:
            excluded = {x['unit'] for x in ledger if x.get('reason')}
            if any(x['unit'] in excluded for x in mapped['claims']):
                account_issues.append('deferred_unit_active')
        digest = result.get('accounting', {}).get('digest')
        if isinstance(digest, str):
            digests.add(digest)
        correct, incorrect, correct_cells, seen_exact = set(), set(), set(), set()
        duplicates = {'exact': 0, 'semantic_correct': 0, 'semantic_incorrect': 0}
        ambiguous = unlabeled = 0
        for occurrence in mapped['claims']:
            ident = occurrence['id']
            if ident in seen_exact:
                duplicates['exact'] += 1
            seen_exact.add(ident)
            label = labels.get(ident)
            if label is None:
                unlabeled += 1
                continue
            status, semantic = label.get('status'), label.get('semantic_id')
            if status == 'ambiguous':
                ambiguous += 1
            if status not in ('true', 'false') or not isinstance(semantic, str) or not semantic:
                continue
            if status == 'true' and semantic not in semantic_ids:
                continue
            equivalences = correct if status == 'true' else incorrect
            if semantic in equivalences:
                duplicates['semantic_correct' if status == 'true' else 'semantic_incorrect'] += 1
                continue
            equivalences.add(semantic)
            if status == 'true':
                correct_cells.add(cell(unit_map[occurrence['unit']]))
        t, f = len(correct), len(incorrect)
        covered = correct_cells & gold_cells
        row = dict(T=t, F=f, precision=t/(t+f) if t+f else 0,
                   gold_cells_covered=len(covered), gold_cell_denominator=len(gold_cells),
                   gold_cell_recall=len(covered)/len(gold_cells) if gold_cells else None,
                   correct_first_origin_cells=[encoded_cell(c) for c in sorted(correct_cells)],
                   active_occurrences=len(mapped['claims']), exact_unique_claims=len(seen_exact),
                   duplicates=duplicates, ambiguous_occurrences=ambiguous,
                   unlabeled_occurrences=unlabeled, pool_exhausted=result.get('pending') == [],
                   accounting=account)
        key = str(seed) + ':' + arm
        metrics[key] = row
        run_map[(arm, seed)] = row
        if account_issues:
            accounting_reasons[key] = sorted(set(account_issues))
            reasons.append('run_accounting_or_status_invalid')
    if len(digests) != 1 or ('model_digest' in validity and digests != {validity['model_digest']}):
        reasons.append('model_digest_mismatch')
    if not units:
        reasons.append('empty_unit_set')
    arm_wall_sum = sum(r['accounting'].get('wall_seconds') or 0 for r in metrics.values())
    if finite_number(elapsed) and arm_wall_sum > elapsed + 1e-6:
        reasons.append('global_wall_accounting_inconsistent')
    valid = not reasons
    decisions = {}
    for name, (treatment, comparator) in COMPARISONS.items():
        rows = []
        for seed in SEEDS:
            a, b = run_map.get((treatment, seed)), run_map.get((comparator, seed))
            outcome = threshold_tests(a, b) if a is not None and b is not None and gold_cells else {'tests': {}, 'passed': False, 'not_evaluable': True}
            rows.append({'seed': seed, **outcome,
                         'selector_contrast_uninformative': name != 'Honto' and bool(a and b and a['pool_exhausted'] and b['pool_exhausted'])})
        numerical_pass = all(r['passed'] for r in rows)
        decisions[name] = {'treatment': treatment, 'comparator': comparator,
            'per_seed': rows, 'all_seeds_thresholds_passed': numerical_pass,
            'verdict': 'INCONCLUSIVE' if not valid else 'PASS' if numerical_pass else 'FAIL'}
    totals = {'attempts': sum(r['accounting'].get('attempts', 0) for r in metrics.values()),
              'actual_tokens': sum(r['accounting'].get('actual_tokens') or 0 for r in metrics.values()),
              'arm_wall_seconds_sum': arm_wall_sum,
              'acquisition_wall_seconds': elapsed if finite_number(elapsed) else None}
    return {'schema_version': 1, 'valid': valid, 'validity_reasons': sorted(set(reasons)),
            'validity_attestations': attestations, 'verified_lock_count': lock_count,
            'run_validity_reasons': accounting_reasons,
            'gold_fact_records': len(facts), 'gold_unique_semantic_ids': len(semantic_ids),
            'gold_cell_denominator': len(gold_cells), 'judge_unique_claims': len(wanted),
            'judge_label_count': len(labels), 'active_occurrences': mapping['active_occurrences'],
            'per_run': metrics, 'decisions': decisions, 'accounting_totals': totals,
            'deduplication': 'Opaque IDs include unit and exact triple, excluding concept. Correct and incorrect canonical semantic IDs deduplicate independently within each arm and seed, preserving first active origin. Exact duplicate counts overlap semantic duplicate counts; they must not be added.',
            'scope': 'Fixed sample, paired seeds; no pooled winner, significance, or general benefit claim.'}


def load_json(path):
    return json.loads(Path(path).read_text(encoding='utf8'))


def load_runs(manifest_path):
    manifest = load_json(manifest_path)
    entries = manifest['entries'] if isinstance(manifest, dict) else manifest
    base = Path(manifest_path).resolve().parent
    return [{'arm': e['arm'], 'seed': e['seed'],
             'result': load_json(base / e['path'])} for e in entries]


def write_json(path, value):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w', encoding='utf8') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def synthetic_fixture():
    units = [dict(unit='synthetic-en', text='A storm damaged the bridge.', tags=['en'], anchor=False),
             dict(unit='synthetic-ko', text='폭풍이 다리를 파괴했다.', tags=['ko'], anchor=False),
             dict(unit='synthetic-deferred', text='He built 2 bridges.', tags=['en'], anchor=True, context_dependent=True)]
    gold = {'facts': [dict(semantic_id='G1', unit='synthetic-en'),
                      dict(semantic_id='G2', unit='synthetic-ko'),
                      dict(semantic_id='G3', unit='synthetic-deferred')]}
    records = []
    for u in units[:2]:
        records.append(dict(unit=u['unit'], outcome='active_provisional', cell=encoded_cell(cell(u)),
            claim=dict(subject='A storm', relation='damaged', object='the bridge', concept='Fact')))
    call = dict(bound=100, reservation=30, prompt_eval_count=40, eval_count=10,
                status='ok', done_reason='stop', seconds=0.1, **{k: 1 for k in DURATION_FIELDS})
    runs = []
    for seed in SEEDS:
        for arm in ARMS:
            active = records if arm.endswith('coverage') else records[:1]
            runs.append({'arm': arm, 'seed': seed, 'result': dict(status='complete', active=deepcopy(active),
                pending=[{'unit': 'synthetic-ko'}], ledger=[{'unit': u['unit'], 'reason': 'context_dependent' if u.get('context_dependent') else None} for u in units],
                accounting=dict(seed=seed, digest='synthetic-digest', cap=24, token_limit=64000,
                    deadline_seconds=900, wall_seconds=1.0, attempts=1, actual_tokens=50, calls=[deepcopy(call)]))})
    labels = [{'id': claim_id(r['unit'], r['claim']), 'status': 'true', 'semantic_id': 'G'+str(i+1),
               'gold_ids': ['G'+str(i+1)], 'reason': 'Synthetic support.'} for i, r in enumerate(records)]
    judgments = {'labels': labels, 'missing_gold': [], 'ambiguities': []}
    validity = {k: True for k in BOOL_ATTESTATIONS}
    validity.update(truncation_events=0, acquisition_wall_seconds=15)
    return runs, units, gold, judgments, validity


def self_test():
    """Synthetic-only contract examples; never opens source, gold, or result files."""
    checks = []
    def check(name, condition):
        checks.append({'id': name, 'passed': bool(condition)})
    args = synthetic_fixture()
    baseline = score(*args)
    check('valid_baseline_all_three_claims_all_seeds_pass', baseline['valid'] and all(d['verdict'] == 'PASS' for d in baseline['decisions'].values()))
    check('deferred_gold_cell_remains_denominator', baseline['gold_cell_denominator'] == 3 and baseline['per_run']['7:fact-coverage']['gold_cell_recall'] == 2/3)
    packet, mapping = build_packet(args[0], args[1])
    check('packet_exhaustive_and_blind', mapping['active_occurrences'] == 21 and len(packet['claims']) == 2 and all(set(c) == {'id', 'unit', 'source_text', 'claim'} and set(c['claim']) == {'subject', 'relation', 'object'} for c in packet['claims']))
    check('shuffle_stable_under_run_order', build_packet(list(reversed(args[0])), args[1])[0] == packet)
    changed = deepcopy(args[0][0]['result']['active'][0]['claim'])
    changed['concept'] = 'Another concept'
    check('concept_excluded_from_id', claim_id('synthetic-en', changed) == packet['claims'][next(i for i,c in enumerate(packet['claims']) if c['unit']=='synthetic-en')]['id'])
    def variant(index, mutate):
        data = deepcopy(args)
        mutate(data[index])
        return score(*data)
    missing = variant(3, lambda j: j['labels'].pop())
    check('missing_label_inconclusive', not missing['valid'] and 'unlabeled_active_claim' in missing['validity_reasons'])
    check('empty_gold_invalid', not variant(2, lambda g: g.update(facts=[]))['valid'])
    data = deepcopy(args)
    for run in data[0]:
        run['result']['active'] = []
    data[3]['labels'] = []
    empty = score(*data)
    check('empty_outputs_precision_zero_valid_fail', empty['valid'] and all(r['precision'] == 0 for r in empty['per_run'].values()) and all(d['verdict']=='FAIL' for d in empty['decisions'].values()))
    data = deepcopy(args)
    data[3]['labels'][1].update(semantic_id='G1', gold_ids=['G1'])
    dedup = score(*data)['per_run']['7:fact-coverage']
    check('semantic_dedup_preserves_first_origin', dedup['T'] == 1 and dedup['gold_cells_covered'] == 1 and dedup['correct_first_origin_cells'] == [[['en'], False]] and dedup['duplicates']['semantic_correct'] == 1)
    data[0][4]['result']['active'].reverse()
    reversed_row = score(*data)['per_run']['7:fact-coverage']
    check('first_origin_follows_active_order', reversed_row['correct_first_origin_cells'] == [[['ko'], False]])
    data = deepcopy(args)
    for lab in data[3]['labels']:
        lab.update(status='false', semantic_id='F1', gold_ids=[])
    incorrect = score(*data)['per_run']['7:fact-coverage']
    check('incorrect_semantic_dedup', incorrect['T'] == 0 and incorrect['F'] == 1 and incorrect['duplicates']['semantic_incorrect'] == 1)
    data[3]['labels'][0].update(status='true', semantic_id='G1', gold_ids=['G1'])
    data[3]['labels'][1].update(semantic_id='G1')
    separate = score(*data)['per_run']['7:fact-coverage']
    check('correct_incorrect_dedup_independent', separate['T'] == 1 and separate['F'] == 1)
    data = deepcopy(args)
    data[0][4]['result']['active'].append(deepcopy(data[0][4]['result']['active'][0]))
    exact = score(*data)['per_run']['7:fact-coverage']
    check('exact_duplicates_share_label_and_keep_first', exact['T'] == 2 and exact['duplicates']['exact'] == 1 and exact['duplicates']['semantic_correct'] == 1)
    def row(t, f=0, c=1):
        return {'T': t, 'F': f, 'gold_cells_covered': c}
    check('precision_exact_90_percent_passes', threshold_tests(row(9, 1), row(8, 1))['passed'])
    check('precision_below_90_percent_fails', not threshold_tests(row(8, 1), row(7, 1))['tests']['precision_at_least_0_90'])
    check('precision_comparator_nondecrease', not threshold_tests(row(9, 1), row(8))['tests']['precision_nondecrease'])
    check('minimum_one_gain_zero', threshold_tests(row(1), row(0))['required_correct_gain'] == 1 and threshold_tests(row(1), row(0))['passed'])
    check('ceil_ten_percent_boundary', threshold_tests(row(11), row(10))['passed'] and not threshold_tests(row(12), row(11))['passed'] and threshold_tests(row(13), row(11))['passed'])
    check('cell_recall_nondecrease', not threshold_tests(row(13,c=1), row(11,c=2))['tests']['gold_cell_recall_nondecrease'])
    controls = variant(4, lambda v: v.update(controls_passed=False))
    check('control_failure_global_inconclusive', not controls['valid'] and all(d['verdict']=='INCONCLUSIVE' for d in controls['decisions'].values()))
    check('missing_seed_inconclusive', not variant(0, lambda r: r.__setitem__(slice(None), [x for x in r if x['seed'] != 19]))['valid'])
    check('malformed_accounting_inconclusive', not variant(0, lambda r: r[0]['result']['accounting']['calls'][0].pop('eval_count'))['valid'])
    check('over_limit_accounting_inconclusive', not variant(0, lambda r: r[0]['result']['accounting'].update(wall_seconds=901))['valid'])
    check('global_timeout_inconclusive', not variant(4, lambda v: v.update(acquisition_wall_seconds=1801))['valid'])
    check('global_wall_accounting_consistent', not variant(4, lambda v: v.update(acquisition_wall_seconds=1))['valid'])
    check('ambiguity_inconclusive', not variant(3, lambda j: j['labels'][0].update(status='ambiguous'))['valid'])
    check('missing_gold_inconclusive', not variant(3, lambda j: j.update(missing_gold=['synthetic']))['valid'])
    check('unknown_true_semantic_inconclusive', not variant(3, lambda j: j['labels'][0].update(semantic_id='NOT_LOCKED'))['valid'])
    check('changed_rules_inconclusive', not variant(4, lambda v: v.update(rules_unchanged=False))['valid'])
    check('incomplete_gold_diagnostic_only', not variant(4, lambda v: v.update(gold_complete=False))['valid'])
    check('hash_mismatch_inconclusive', not variant(4, lambda v: v.update(locks={str(Path(__file__).resolve()): '0'*64}))['valid'])
    locked = variant(4, lambda v: v.update(locks={str(Path(__file__).resolve()): hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}))
    check('matching_file_hash_valid', locked['valid'] and locked['verified_lock_count'] == 1)
    data = deepcopy(args)
    for run in data[0]:
        if run['arm'] == 'fact-coverage' and run['seed'] == 19:
            run['result']['active'] = run['result']['active'][:1]
    one_seed_fail = score(*data)
    check('all_three_seeds_required_no_pooling', one_seed_fail['valid'] and one_seed_fail['decisions']['Hq-Fact']['verdict'] == 'FAIL' and [r['passed'] for r in one_seed_fail['decisions']['Hq-Fact']['per_seed']] == [True, True, False])
    check('empty_source_record_invalid', not variant(1, lambda u: u[0].update(text=''))['valid'])
    check('gold_empty_output_no_exception', score([], [], {'facts': []}, {'labels': [], 'missing_gold': [], 'ambiguities': []}, args[4])['valid'] is False)
    check('score_contains_no_prediction_or_corpus_text', all(u['text'] not in canonical(baseline) for u in args[1]) and 'A storm' not in canonical(baseline))
    return {'scope': 'Synthetic fixtures only; no target corpus, gold, or model output opened.',
            'checks_total': len(checks), 'checks_passed': sum(c['passed'] for c in checks),
            'passed': all(c['passed'] for c in checks), 'checks': checks}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='mode', required=True)
    for mode in ('packet', 'score', 'self-test'):
        cmd = sub.add_parser(mode)
        cmd.add_argument('--out', required=True)
        if mode != 'self-test':
            cmd.add_argument('--manifest', required=True)
            cmd.add_argument('--units', required=True)
        if mode == 'packet':
            cmd.add_argument('--mapping', required=True)
        if mode == 'score':
            for name in ('gold', 'judgments', 'validity'):
                cmd.add_argument('--'+name, required=True)
    a = ap.parse_args()
    try:
        if a.mode == 'self-test':
            result = self_test()
        else:
            runs, units = load_runs(a.manifest), load_json(a.units)
            if a.mode == 'packet':
                result, mapping = build_packet(runs, units)
                write_json(a.mapping, mapping)
            else:
                result = score(runs, units, load_json(a.gold), load_json(a.judgments), load_json(a.validity))
        write_json(a.out, result)
        print(json.dumps({'mode': a.mode, 'written': True, 'valid': result.get('valid'),
                          'passed': result.get('passed'), 'checks_total': result.get('checks_total')}))
        return 1 if a.mode == 'self-test' and not result['passed'] else 0
    except Exception as exc:
        # Exception contents may contain corpus text or private paths.
        print(json.dumps({'mode': a.mode, 'written': False, 'error_type': type(exc).__name__}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
