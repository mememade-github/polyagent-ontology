"""Original bounded QD-inspired mechanics; no ontology mutation or model invocation."""
import collections
import hashlib
import json
import random


def run(units, ask, onto, *, selector='coverage', seed=7, cap=64, fixed_fact=False, state=None):
    """ask has onto.Llm.ask signature. Units supply source, unit, text, tags,
    anchor, context_dependent; source_sha256 is the full source digest.
    Tags are declared descriptors, never inferred ontology truth.
    """
    if selector not in {'random', 'coverage'} or cap < 0:
        raise ValueError('invalid control')
    if len({u['unit'] for u in units}) != len(units):
        raise ValueError('duplicate unit')
    rng = random.Random(seed)
    pending = [(u, lens) for u in units for lens in ('general', 'qualifier')]
    pool = [(u['unit'], lens) for u, lens in pending]
    history, calls, active, order = [], [], {}, []

    if state is not None:
        state.update(history=history, calls=calls, active=[], pending=[])

    def cell(u):
        return (tuple(sorted(set(u['tags']))), bool(u['anchor']))

    def call(system, user, schema, predict):
        bound = onto.prompt_bound(system, user, schema)
        if bound + predict >= 3800:
            raise ValueError('oversized')
        if len(calls) >= cap:
            raise ValueError('call_cap')
        record = {'bound': bound, 'predict': predict, 'status': 'attempted'}
        calls.append(record)  # exceptions and schema failures consume cap
        try:
            value = ask(system, user, schema, predict)
            onto.validate(value, schema)
            record['status'] = 'returned_valid_schema'
            return value
        except BaseException as exc:
            record['status'] = 'failed'
            record['error_type'] = type(exc).__name__
            raise

    while pending and len(calls) < cap:
        counts = collections.Counter(r['cell'] for r in active.values())
        candidates = pending
        if selector == 'coverage':
            low = min(counts[cell(u)] for u, _ in pending)
            candidates = [t for t in pending if counts[cell(t[0])] == low]
        task = rng.choice(candidates)
        pending.remove(task)
        u, lens = task
        if state is not None:
            state.update(active=list(active.values()), pending=[{'unit': x['unit'], 'lens': l, 'reason': 'unfinished'} for x, l in [task] + pending])
        order.append((u['unit'], lens))
        record = {'source': u['source'], 'source_sha256': u['source_sha256'],
                  'unit': u['unit'], 'unit_sha256': hashlib.sha256(u['text'].encode()).hexdigest(),
                  'lens': lens, 'parent': None, 'cell': cell(u), 'outcome': 'started'}
        history.append(record)
        if u.get('context_dependent', False):
            record['outcome'] = 'deferred_context'
            continue
        system = onto.EXTRACT
        if lens == 'qualifier':
            system += ' Focus on preserving condition, attribution, modality and negation.'
        if fixed_fact:
            system += ' Set concept to Fact.'
        try:
            result = call(system, u['text'], onto.ITEM, 600)
            record['extraction'] = result
            if not result['items']:
                record['outcome'] = 'empty'
                continue
            claim = dict(result['items'][0], quote=u['text'])
            record['claim'] = claim
            if fixed_fact and claim['concept'] != 'Fact':
                raise ValueError('fixed_fact_mismatch')
            if any(not claim[k].strip() or claim[k] not in u['text']
                   for k in ('subject', 'relation', 'object')):
                raise ValueError('span_grounding')
            user = json.dumps({'sentence': u['text'], 'claim': claim}, ensure_ascii=False)
            verdict = call(onto.VERIFY, user, onto.BOOL, 30)
            if not verdict['stated']:
                raise ValueError('false_verifier')
            key = tuple(claim[k] for k in ('subject', 'relation', 'object'))
            if key in active:
                record['outcome'] = 'duplicate'
                record['duplicate_of'] = active[key]['unit']
            else:
                record['outcome'] = 'active_provisional'
                active[key] = record
                if state is not None:
                    state['active'] = list(active.values())
        except Exception as exc:
            record['outcome'] = 'rejected'
            record['reason'] = str(exc) if type(exc) is ValueError else type(exc).__name__
    return {'pool': pool, 'selector': selector, 'seed': seed, 'cap': cap,
            'calls': calls, 'order': order, 'history': history,
            'active': list(active.values()),
            'pending': [{'unit': u['unit'], 'lens': lens, 'reason': 'call_cap'} for u, lens in pending],
            'quality': 'unmeasured; gate is a proxy', 'scientific_trial_ready': False}
