"""Scripted synthetic state-transition checks, not semantic evaluation."""
import hashlib
import importlib.util
import json
from pathlib import Path
from controller import run

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('onto', ROOT / 'onto.py')
onto = importlib.util.module_from_spec(spec)
spec.loader.exec_module(onto)


class Stub:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.calls = 0

    def __call__(self, *args):
        self.calls += 1
        value = next(self.responses)
        if isinstance(value, Exception):
            raise value
        return value


def unit(i, text='A holds B. C holds D.', tags=(), anchor=False, context=False):
    return dict(unit=str(i), source='synthetic.txt', text=text, tags=list(tags),
                anchor=anchor, context_dependent=context,
                source_sha256=hashlib.sha256(text.encode()).hexdigest())


def item(s='A', r='holds', o='B'):
    return {'items': [dict(subject=s, relation=r, object=o, concept='Holding')]}


def suite():
    runs, checks = {}, {}
    def execute(name, us, responses, **kw):
        stub = Stub(responses)
        result = run(us, stub, onto, **kw)
        assert stub.calls == len(result['calls'])
        runs[name] = result
        return result
    yes = {'stated': True}
    r = execute('positive_duplicate', [unit(1)], [item(), yes, item(), yes])
    checks['positive_duplicate'] = len(r['active']) == 1 and any(x['outcome']=='duplicate' for x in r['history'])
    r = execute('same_cell', [unit(1)], [item(), yes, item('C','holds','D'), yes])
    checks['same_cell'] = len(r['active']) == 2 and r['active'][0]['cell'] == r['active'][1]['cell']
    r = execute('invalid_and_false', [unit(1)], [item('X'), item(), {'stated': False}])
    checks['invalid_and_false'] = not r['active'] and {x.get('reason') for x in r['history']} == {'span_grounding','false_verifier'}
    r = execute('oversized', [unit(1, '한'*4000)], [])
    checks['oversized'] = not r['calls'] and all(x['reason']=='oversized' for x in r['history'])
    r = execute('exception', [unit(1)], [RuntimeError('scripted')], cap=1)
    checks['exception'] = len(r['calls'])==1 and not r['active'] and len(r['pending'])==1
    r = execute('verify_exhausted', [unit(1)], [item()], cap=1)
    checks['verify_exhausted'] = not r['active'] and r['history'][0]['reason']=='call_cap'
    for selector in ('random','coverage'):
        r = execute('deferred_'+selector, [unit(1, context=True)], [], selector=selector)
        checks['deferred_'+selector] = not r['calls'] and all(x['outcome']=='deferred_context' for x in r['history'])
    us = [unit(1), unit(2,tags=('condition','negation'),anchor=True), unit(3,tags=('condition',))]
    responses = [item(), yes]*6
    a = execute('control_random', us, responses, selector='random',cap=12)
    b = execute('control_coverage', us, responses, selector='coverage',cap=12)
    checks['controls'] = a['pool']==b['pool'] and a['cap']==b['cap'] and a['order']!=b['order']
    checks['overlap'] = any(x['cell']==(('condition','negation'),True) for x in b['history'])
    r = execute('all_reject', [unit(1,'가 는 나.')], [{'items':[]},{'items':[]}])
    checks['all_reject'] = not r['active'] and r['quality'].startswith('unmeasured')
    return {'checks': checks, 'passed': all(checks.values()), 'runs': runs,
            'actual_calls': sum(len(r['calls']) for r in runs.values()),
            'real_model_calls': 0, 'semantic_quality': 'not tested'}


if __name__ == '__main__':
    import sys
    result = suite()
    evidence = Path(sys.argv[1])
    result['hashes'] = {str(p.relative_to(ROOT.parent)): hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in (ROOT/'onto.py', Path(__file__), Path(__file__).with_name('controller.py'),
                                  ROOT.parent/'evidence/qd-adaptation/protocol.md')}
    with evidence.open('x') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(json.dumps({'passed':result['passed'],'checks':result['checks'],'actual_calls':result['actual_calls']}))
    sys.exit(0 if result['passed'] else 1)
