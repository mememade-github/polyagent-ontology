import json,subprocess,time,re,tiktoken
W='__SCRATCH__/w/'
enc=tiktoken.get_encoding('cl100k_base')
for name,doc,extra in (('ascii_default','ascii.txt',''),('ascii_msb1000','ascii.txt','--max-section-bytes 1000'),('ascii_msb20000','ascii.txt','--max-section-bytes 20000'),('ascii_glean1','ascii.txt','--gleanings 1')):
    log=W+f'l_{name}.jsonl'
    open(log,'w').close()
    p=subprocess.Popen(['python3',W+'stub.py',log]);time.sleep(0.4)
    subprocess.run('docker rm -f hx-x',shell=True,capture_output=True)
    subprocess.run(f'docker create --name hx-x --network polyagent-ontology_default --entrypoint extract -e ANTHROPIC_API_KEY=stub -w /tmp ghcr.io/helixdb/ontology-agent:latest --ontology /tmp/o.toml --helix-url http://hx-db:8080 --load L1 --dry-run --verifier-model stub-v --extractor-model stub-e --anthropic-base-url http://__INTERNAL_IP__:18081 --responses /tmp/r.redb {extra} /tmp/{doc}',shell=True,capture_output=True)
    subprocess.run(f'docker cp {W}ontology_nokey.toml hx-x:/tmp/o.toml; docker cp {W}{doc} hx-x:/tmp/{doc}',shell=True,capture_output=True)
    r=subprocess.run('timeout 100 docker start -a hx-x',shell=True,capture_output=True,text=True)
    p.kill();p.wait()
    ents=[];links=0;rest=[]
    for l in open(log):
        b=json.loads(l)['req'];q=b['output_config']['format']['schema']['properties'];c=b['messages'][-1]['content']
        if 'entities' in q:
            m=re.search(r'<document-[0-9a-f]+>(.*)</document-',c,re.S)
            ents.append((len(m.group(1).encode()) if m else None,len(enc.encode(c))+len(enc.encode(str(b.get('system'))))))
        elif 'facts' in q: links+=1
        else: rest.append(list(q))
    print(name,'rc',r.returncode,'entity(bytes,tokens):',ents,'link calls',links,'other',len(rest),'| stderr',r.stderr[:100])
