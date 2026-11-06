import json,subprocess,time
base="Jane Doe promised Globex a 10% service credit"
V={}
# progressive one-word substitutions against a known passage: fuzzy threshold probe
words=base.split()
for n in range(1,len(words)):
    w=list(words)
    for i in range(n): w[i]="zzzz"
    V[f'sub{n}']=' '.join(w)
for n in (1,2,3,4,6,8,10,14):
    V[f'char{n}']=base[:-n-1]+'X'*n+base[-1]
V['short_one_word']='Globex'
V['typo_mid']="Jane Doe promisd Globex a 10% servce credit"
W='__SCRATCH__/q/'
res={}
for k,q in V.items():
    p=subprocess.Popen(['python3',W+'stub.py',W+f'l2_{k}.jsonl',json.dumps(q)]);time.sleep(0.3)
    subprocess.run('docker rm -f hx-x',shell=True,capture_output=True)
    subprocess.run('docker create --name hx-x --network polyagent-ontology_default --entrypoint extract -e ANTHROPIC_API_KEY=stub -w /tmp ghcr.io/helixdb/ontology-agent:latest --ontology /tmp/o.toml --helix-url http://hx-db:8080 --load L1 --dry-run --verifier-model stub-v --extractor-model stub-e --anthropic-base-url http://__INTERNAL_IP__:18081 --responses /tmp/r.redb /tmp/doc.md',shell=True,capture_output=True)
    subprocess.run(f'docker cp {W}ontology_nokey.toml hx-x:/tmp/o.toml; docker cp {W}doc.md hx-x:/tmp/doc.md',shell=True,capture_output=True)
    r=subprocess.run('timeout 60 docker start -a hx-x',shell=True,capture_output=True,text=True)
    p.kill();p.wait()
    t=r.stdout;i=t.find('{"attributes"');d=json.JSONDecoder().raw_decode(t[i:])[0]
    v=d['verdicts'][0]
    res[k]={"q":q,"verdict":v['verdict'],"reason":v.get('reason'),"span":(v.get('fact') or {}).get('span')}
    print(k,repr(q),v['verdict'],v.get('reason'),res[k]['span'])
json.dump(res,open(W+'fuzzy.json','w'),ensure_ascii=False,indent=1)
