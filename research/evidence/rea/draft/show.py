import json,sys
for l in open(sys.argv[1]):
    try:o=json.loads(l)
    except: print(l[:300]);continue
    if 'event' in o:
        if o['event']!='usage': print(json.dumps(o,ensure_ascii=False)[:300])
    else:
        print('RESULT status',o.get('status'),'| summary',o.get('summary'));print(o['draft']['ontology_toml']);print(o['draft']['mappings_toml']);print('bundle',json.dumps(o.get('bundle'),ensure_ascii=False)[:400]);print('usage',o.get('usage'))
