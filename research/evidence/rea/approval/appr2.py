import json
exec(open('appr.py').read().split("rev=res['draft']")[0])
items=list(res['draft']['draft']['items'].keys());print(items)
f=turn('f1',{"feedback":{"draft_rev":1,"actions":[{"approve":{"item":i}} for i in items]}})
rev=f['draft']['draft']['rev'];print('rev after',rev,{k:v.get('status') for k,v in f['draft']['draft']['items'].items()})
c=turn('c1',{'feedback':{'draft_rev':rev,'actions':[{'comment':{'text':'Please add the risk too.'}}]}},f['state'])
print('rev after comment',c['draft']['draft']['rev'])
rev=c['draft']['draft']['rev']
f=c
b=turn('a2',{"approve":{"draft_rev":rev}},f['state'])
json.dump(b,open('approved.json','w'),ensure_ascii=False)
bd=b.get('bundle');print(list(bd.keys()) if bd else None)
if bd:
    open('bundle_ontology.toml','w').write(bd.get('ontology_toml') or '');open('bundle_mappings.toml','w').write(bd.get('mappings_toml') or '')
    print(json.dumps({k:v for k,v in bd.items() if 'toml' not in k},ensure_ascii=False)[:600]);print(bd.get('ontology_toml'));print(bd.get('mappings_toml'))
