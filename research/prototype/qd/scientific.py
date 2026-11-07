"""One-shot extraction trial boundary. No acquisition, gold, scoring or publication."""
import argparse
import hashlib
import importlib.util
import json
import os
import shutil
from pathlib import Path
import subprocess
import sys
import time

from controller import run as qd_run

spec = importlib.util.spec_from_file_location('onto', Path(__file__).parents[1] / 'onto.py')
onto = importlib.util.module_from_spec(spec)
spec.loader.exec_module(onto)


class BudgetAbort(BaseException):
    """Must escape the historical controller's task rejection handler."""


def transport(endpoint, path, body, remaining):
    # subprocess timeout bounds the entire response, including slow-drip bodies.
    code = ('import sys,urllib.request,shutil; b=sys.stdin.buffer.read(); '
            'r=urllib.request.Request(sys.argv[1],b or None,{"Content-Type":"application/json"}); '
            'shutil.copyfileobj(urllib.request.urlopen(r),sys.stdout.buffer)')
    return subprocess.run([sys.executable, '-u', '-c', code, endpoint.rstrip('/') + path],
                          input=json.dumps(body).encode() if body is not None else b'',
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          timeout=remaining, check=True).stdout


class Driver:
    def __init__(self, endpoint, digest, seed, private, *, dispatch=transport,
                 cap=24, tokens=64000, seconds=900, global_deadline=None):
        if not digest or not 0 <= cap <= 64 or not 0 <= tokens <= 64000 or not 0 < seconds <= 900:
            raise ValueError('invalid budget or digest')
        self.endpoint, self.digest, self.seed = endpoint, digest, seed
        self.cap, self.limit, self.seconds = cap, tokens, seconds
        self.start = time.monotonic()
        self.global_deadline = global_deadline
        self.first_dispatch = None
        self.records, self.total, self.dispatch = [], 0, dispatch
        self.private = Path(private).resolve()
        if Path('/tmp') not in self.private.parents:
            raise ValueError('explicit private scratch under /tmp required')
        self.private.mkdir(mode=0o700, parents=True, exist_ok=False)
        self.raw = open(self.private / 'raw.jsonl', 'x', encoding='utf8')
        os.chmod(self.private / 'raw.jsonl', 0o600)

    def remaining(self):
        now = time.monotonic()
        left = self.start + self.seconds - now
        if self.global_deadline is not None:
            left = min(left, self.global_deadline - now)
        if left <= 0:
            raise BudgetAbort('deadline')
        return left

    def request(self, path, body):
        if shutil.disk_usage('/workspaces').free < 2_000_000_000:
            raise BudgetAbort('disk_floor')
        remaining = self.remaining()
        if self.first_dispatch is None:
            self.first_dispatch = time.monotonic()
        return self.dispatch(self.endpoint, path, body, remaining)

    def ask(self, system, user, schema, predict=400):
        bound = onto.prompt_bound(system, user, schema)
        if bound + predict >= 3800 or self.total + bound + predict > self.limit:
            raise BudgetAbort('reservation')
        if len(self.records) >= self.cap:
            raise BudgetAbort('call_cap')
        self.remaining()
        # No acquisition/fallback: check the existing alias against the lock each time.
        try:
            tags = json.loads(self.request('/api/tags', None))['models']
            matches = [x for x in tags if x.get('name') == 'qwen2.5:3b' or x.get('model') == 'qwen2.5:3b']
            if len(matches) != 1 or matches[0].get('digest') != self.digest:
                raise BudgetAbort('digest_mismatch')
        except Exception as exc:
            raise BudgetAbort('digest_transport_' + type(exc).__name__) from exc
        body = dict(model='qwen2.5:3b', stream=False, format=schema,
                    options=dict(num_ctx=8192, temperature=0, num_thread=8, seed=self.seed, num_predict=predict),
                    messages=[dict(role='system', content=system), dict(role='user', content=user)])
        record = dict(bound=bound, reservation=predict, status='attempted')
        self.records.append(record)
        begin = time.monotonic()
        self.raw.write(json.dumps({'request': body}, ensure_ascii=False) + '\n')
        self.raw.flush()
        try:
            raw = self.request('/api/chat', body)
            self.raw.write(json.dumps({'response': raw.decode('utf8', errors='backslashreplace')}, ensure_ascii=False) + '\n')
            self.raw.flush()
            response = json.loads(raw)
            for k in ('prompt_eval_count', 'eval_count', 'total_duration', 'load_duration', 'prompt_eval_duration', 'eval_duration', 'done_reason'):
                record[k] = response.get(k)
            for k in ('prompt_eval_count', 'eval_count'):
                if type(response.get(k)) is not int or response[k] <= 0:
                    raise BudgetAbort('invalid_' + k)
            self.total += response['prompt_eval_count'] + response['eval_count']
            if response['prompt_eval_count'] > bound or response['eval_count'] > predict or self.total > self.limit:
                raise BudgetAbort('accounting_exceeded')
            for k in ('total_duration', 'load_duration', 'prompt_eval_duration', 'eval_duration'):
                if type(response.get(k)) is not int or response[k] < 0:
                    raise BudgetAbort('invalid_' + k)
            if response.get('done') is not True or response.get('done_reason') != 'stop':
                raise BudgetAbort('incomplete_generation')
            self.remaining()
            value = json.loads(response['message']['content'])
            onto.validate(value, schema)
            record['status'] = 'ok'
            return value
        except BaseException as exc:
            record.update(status='failed', error_type=type(exc).__name__)
            partial = getattr(exc, 'output', None)
            if partial:
                self.raw.write(json.dumps({'partial_response': partial.decode('utf8', errors='backslashreplace')}) + '\n')
                self.raw.flush()
            if isinstance(exc, BudgetAbort):
                raise
            raise BudgetAbort('response_' + type(exc).__name__) from exc
        finally:
            record['seconds'] = time.monotonic() - begin

    def accounting(self):
        now = time.monotonic()
        return dict(calls=self.records, attempts=len(self.records), actual_tokens=self.total,
                    wall_seconds=0 if self.first_dispatch is None else now-self.first_dispatch,
                    setup_seconds=(now if self.first_dispatch is None else self.first_dispatch)-self.start,
                    cap=self.cap, token_limit=self.limit,
                    deadline_seconds=self.seconds, digest=self.digest, seed=self.seed)


def cell(u):
    return [sorted(set(u['tags'])), bool(u['anchor'])]


def preflight(units):
    ledger = []
    for u in units:
        reason = 'context_dependent' if u.get('context_dependent') else None
        # Common guard covers both QD lenses and Fact suffix, before selection.
        system = onto.EXTRACT + ' Focus on preserving condition, attribution, modality and negation. Set concept to Fact.'
        if onto.prompt_bound(system, u['text'], onto.ITEM) + 600 >= 3800:
            reason = reason or 'oversize'
        ledger.append(dict(source=u['source'], source_sha256=u['source_sha256'], unit=u['unit'],
                           unit_sha256=hashlib.sha256(u['text'].encode()).hexdigest(), cell=cell(u), reason=reason))
    return ledger


def baseline(units, driver, state):
    """Copy of read_docs facts.append extraction seam, without genre/downstream."""
    for index, u in enumerate(units):
        state['pending'] = [dict(unit=x['unit'], reason='unfinished') for x in units[index:]]
        if len(driver.records) >= driver.cap:
            return
        record = dict(unit=u['unit'], source=u['source'], source_sha256=u['source_sha256'],
                      unit_sha256=hashlib.sha256(u['text'].encode()).hexdigest(), cell=cell(u), outcome='started')
        state['history'].append(record)
        r = driver.ask(onto.EXTRACT, u['text'], onto.ITEM, 600)
        record['extraction'] = r
        record['outcome'] = 'empty'
        for it in r['items']:
            it = dict(it, quote=u['text'])
            if any(not it[k].strip() or it[k] not in u['text'] for k in ('subject', 'relation', 'object')):
                record['outcome'] = 'span_grounding'
                continue
            user = json.dumps({'sentence': u['text'], 'claim': it}, ensure_ascii=False)
            if onto.prompt_bound(onto.VERIFY, user, onto.BOOL) + 30 >= 3800:
                record['outcome'] = 'verification_budget'
                continue
            if len(driver.records) >= driver.cap:
                record['outcome'] = 'call_cap'
                return
            if not driver.ask(onto.VERIFY, user, onto.BOOL, 30)['stated']:
                record['outcome'] = 'semantic_grounding'
                continue
            record.update(claim=it, outcome='active_provisional')
            state['active'].append(record)
    state['pending'] = []


def execute(units, driver, arm):
    ledger = preflight(units)
    deferred = [x for x in ledger if x['reason']]
    excluded = {x['unit'] for x in deferred}
    eligible = [u for u in units if u['unit'] not in excluded]
    state = dict(active=[], history=[], pending=[], status='complete')
    try:
        if len({u['unit'] for u in units}) != len(units):
            raise BudgetAbort('duplicate_unit')
        if arm == 'onto':
            baseline(eligible, driver, state)
        else:
            factor, selector = arm.split('-')
            if factor not in ('original', 'fact'):
                raise BudgetAbort('invalid_arm')
            state.update(qd_run(eligible, driver.ask, onto, selector=selector, seed=driver.seed,
                                cap=driver.cap, fixed_fact=factor == 'fact', state=state))
    except BaseException as exc:
        state.update(status='inconclusive', error_type=type(exc).__name__, error=str(exc) if isinstance(exc, BudgetAbort) else 'operation_failed')
    finally:
        if time.monotonic() - driver.start > driver.seconds:
            state.update(status='inconclusive', error='deadline')
        if state.get('status') == 'inconclusive' and state['history'] and state['history'][-1]['outcome']=='started':
            state['history'][-1]['outcome'] = 'aborted'
        visited = {x['unit'] for x in state['history']}
        for x in ledger:
            x['status'] = 'deferred' if x['reason'] else ('complete' if x['unit'] in visited and not any(p['unit']==x['unit'] for p in state['pending']) else 'partial')
        documents = []
        for source in dict.fromkeys(x['source'] for x in ledger):
            rows = [x for x in ledger if x['source']==source]
            statuses = {x['status'] for x in rows}
            documents.append(dict(source=source, source_sha256=rows[0]['source_sha256'], status='complete' if statuses=={'complete'} else 'deferred' if statuses=={'deferred'} else 'partial'))
        for row in deferred:
            row['text'] = next(u['text'] for u in units if u['unit']==row['unit'])
        state.update(ledger=ledger, deferred=deferred, documents=documents, accounting=driver.accounting())
    return state


# Inspectable synthetic fixtures; never populated from target materials.
CONTROLS = [
    dict(language='en', sentence='A storm damaged the bridge.', subject='A storm', relation='damaged', object='the bridge',
         spans=dict(subject=('A storm', 'storm'), relation=('damaged',), object=('the bridge', 'bridge'))),
    dict(language='ko', sentence='폭풍이 다리를 파괴했다.', subject='폭풍이', relation='파괴했다', object='다리를',
         spans=dict(subject=('폭풍이', '폭풍'), relation=('파괴했다', '파괴했다.', '파괴'), object=('다리를', '다리'))),
]
NEGATIVE_CONTROLS = [
    ('A storm did not damage the bridge.', 'A storm', 'damage', 'the bridge'),
    ('A storm damaged the bridge.', 'the bridge', 'damaged', 'A storm'),
    ('Mina said a storm damaged the bridge.', 'a storm', 'damaged', 'the bridge'),
    ('폭풍이 다리를 파괴하지 않았다.', '폭풍이', '파괴', '다리를'),
    ('폭풍이 다리를 파괴했다.', '다리를', '파괴했다', '폭풍이'),
    ('민수는 폭풍이 다리를 파괴했다고 말했다.', '폭풍이', '파괴', '다리를'),
]


def controls(driver):
    results = []
    try:
        for fixture in CONTROLS:
            claim = {k: fixture[k] for k in ('subject', 'relation', 'object')}
            claim.update(concept='Fact', quote=fixture['sentence'])
            verdict = driver.ask(onto.VERIFY, json.dumps(dict(sentence=fixture['sentence'], claim=claim), ensure_ascii=False), onto.BOOL, 30)
            results.append(dict(check='verify_positive_'+fixture['language'], passed=verdict['stated']))
            for fact in (False, True):
                r = driver.ask(onto.EXTRACT + (' Set concept to Fact.' if fact else ''), fixture['sentence'], onto.ITEM, 600)
                matched = bool(r['items']) and all(r['items'][0][k] in fixture['spans'][k]
                    and r['items'][0][k] in fixture['sentence']
                    for k in ('subject', 'relation', 'object'))
                if fact:
                    matched = matched and r['items'][0]['concept']=='Fact'
                if matched:
                    extracted = dict(r['items'][0], quote=fixture['sentence'])
                    verified = driver.ask(onto.VERIFY, json.dumps(dict(sentence=fixture['sentence'], claim=extracted), ensure_ascii=False), onto.BOOL, 30)
                    matched = verified['stated'] is True
                results.append(dict(check='extract_'+fixture['language']+'_'+str(fact), passed=matched))
        for i, (sentence, subject, relation, obj) in enumerate(NEGATIVE_CONTROLS):
            claim = dict(subject=subject, relation=relation, object=obj, concept='Fact', quote=sentence)
            r = driver.ask(onto.VERIFY, json.dumps(dict(sentence=sentence, claim=claim), ensure_ascii=False), onto.BOOL, 30)
            results.append(dict(check='verify_negative_'+str(i), passed=r['stated'] is False))
        return dict(status='valid' if all(x['passed'] for x in results) else 'inconclusive', checks=results, accounting=driver.accounting())
    except BaseException as exc:
        return dict(status='inconclusive', error_type=type(exc).__name__, checks=results, accounting=driver.accounting())


def main():
    ap = argparse.ArgumentParser(__doc__)
    ap.add_argument('--units')
    ap.add_argument('--out', required=True, help='new private /tmp directory')
    ap.add_argument('--summary', help='new sanitized summary file, separate from private output')
    ap.add_argument('--seed', type=int, required=True)
    ap.add_argument('--arm', choices=['onto','original-random','original-coverage','fact-random','fact-coverage'])
    ap.add_argument('--endpoint', required=True)
    ap.add_argument('--digest', required=True)
    ap.add_argument('--controls', action='store_true')
    a = ap.parse_args()
    if not a.controls and (not a.units or not a.arm):
        ap.error('--units and --arm required')
    driver = Driver(a.endpoint, a.digest, a.seed, a.out)
    try:
        result = controls(driver) if a.controls else execute(json.loads(Path(a.units).read_text()), driver, a.arm)
    except BaseException as exc:
        result = dict(status='inconclusive', error_type=type(exc).__name__, active=[], history=[],
                      pending=[], deferred=[], ledger=[], documents=[], accounting=driver.accounting())
    with open(driver.private / 'result.json', 'x') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    driver.raw.close()
    summary = dict(status=result['status'], accounting=result['accounting'])
    if a.summary:
        with open(a.summary, 'x') as f:
            json.dump(summary, f, indent=2)
    print(json.dumps(summary))
    return 0 if result['status'] in ('complete','valid') else 1


if __name__ == '__main__':
    sys.exit(main())
