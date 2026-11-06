import json,subprocess,time,re
W='__SCRATCH__/w/'
for name,extra in (('small_d',''),('small_500','--max-section-bytes 500')):
    log=W+f'l3_{name}.jsonl';open(log,'w').close()
    p=subprocess.Popen(['python3',W+'stub.py',log]);time.sleep(.3)
    subprocess.run('docker rm -f hx-x',shell=True,capture_output=True)
    subprocess.run(f'docker create --name hx-x --network polyagent-ontology_default --entrypoint extract -e ANTHROPIC_API_KEY=stub -w /tmp ghcr.io/helixdb/ontology-agent:latest --ontology /tmp/o.toml --helix-url http://hx-db:8080 --load L1 --dry-run --verifier-model stub-v --extractor-model stub-e --anthropic-base-url http://__INTERNAL_IP__:18081 --responses /tmp/r.redb {extra} /tmp/small.txt',shell=True,capture_output=True)
    subprocess.run(f'docker cp {W}ontology_nokey.toml hx-x:/tmp/o.toml; docker cp {W}small.txt hx-x:/tmp/small.txt',shell=True,capture_output=True)
    r=subprocess.run('timeout 60 docker start -a hx-x',shell=True,capture_output=True,text=True);p.kill();p.wait()
    S=[]
    for l in open(log):
        b=json.loads(l)['req']
        if 'entities' in b['output_config']['format']['schema']['properties']:
            m=re.search(r'<document-[0-9a-f]+>(.*)</document-',b['messages'][-1]['content'],re.S);S.append(len(m.group(1).encode()))
    print(name,'rc',r.returncode,sorted(S)[-6:],'n',len(S),r.stderr[:80])
