import json,subprocess,time
W='__SCRATCH__/d2/'
base=json.load(open('t0.json'))
res=[json.loads(l) for l in open('out2.ndjson')][-1]
state=res['state']
def turn(name,inp,st=state):
    t=dict(base);t['input']=inp;t['state']=st;t['request_id']=name
    json.dump(t,open(f'{name}.json','w'))
    log=f'{name}.log.jsonl';open(log,'w').close()
    p=subprocess.Popen(['python3','stub5.py',W+log,'1']);time.sleep(.3)
    subprocess.run('docker rm -f oa-t',shell=True,capture_output=True)
    subprocess.run('docker create --name oa-t --network polyagent-ontology_default -i --entrypoint ontology-agent -w /data ghcr.io/helixdb/ontology-agent:latest turn --allow-private-model-hosts',shell=True,capture_output=True)
    subprocess.run('docker cp doc.md oa-t:/data/doc.md',shell=True,capture_output=True)
    r=subprocess.run(f'timeout 60 docker start -ai oa-t < {name}.json',shell=True,capture_output=True,text=True)
    p.kill();p.wait();subprocess.run('docker rm -f oa-t',shell=True,capture_output=True)
    open(f'{name}.out','w').write(r.stdout+r.stderr)
    calls=sum(1 for _ in open(log))
    last=None
    for l in r.stdout.splitlines():
        try:last=json.loads(l)
        except:pass
    print('##',name,'rc',r.returncode,'model_calls',calls,'status',(last or {}).get('status'),'bundle',bool((last or {}).get('bundle')),'| stderr',r.stderr[:200])
    for l in r.stdout.splitlines():
        try:o=json.loads(l)
        except:continue
        if o.get('event') in('warning','tool_result','turn_finished') and name!='a1': print('  ',json.dumps(o,ensure_ascii=False)[:260])
    return last
rev=res['draft']['draft']['rev'];print('rev',rev)
turn('a0_wrongrev',{"approve":{"draft_rev":99}})
b=turn('a1',{"approve":{"draft_rev":rev}})
json.dump(b,open('approved.json','w'),ensure_ascii=False)
print(json.dumps(b.get('bundle'),ensure_ascii=False)[:1800] if b else None)
