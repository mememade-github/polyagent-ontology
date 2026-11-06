import json,subprocess,os,time
W=os.getcwd()+'/'
for nm,ename,reply in (('match_.95','Globex Inc',{"value":[{"entity":"E1","choice":"K1","confidence":0.95}]}),('match_.90','Globex Inc',{"value":[{"entity":"E1","choice":"K1","confidence":0.90}]}),('match_.89','Globex Inc',{"value":[{"entity":"E1","choice":"K1","confidence":0.89}]}),('null_choice','Globex Inc',{"value":[{"entity":"E1","choice":None,"confidence":0.95}]}),('exact_name','Globex',{"value":[]}),('unrelated','Initech',{"value":[]})):
    for f in('a.log','a.log.adj'):
        if os.path.exists(f):os.remove(f)
    json.dump(reply,open('a.log.reply','w'))
    p=subprocess.Popen(['python3','stub_adj.py',W+'a.log'],env={**os.environ,'ENAME':ename},stderr=subprocess.DEVNULL);time.sleep(.3)
    r=subprocess.run('bash ex.sh',shell=True,capture_output=True,text=True);p.kill();p.wait()
    t=r.stdout;i=t.find('{"attributes');
    if i<0: print(nm,'ERR',t[:300]);continue
    d=json.JSONDecoder().raw_decode(t[i:])[0]
    v=d['verdicts'][0] if d.get('verdicts') else {}
    print(nm,'| res',json.dumps(d['resolutions'][0],ensure_ascii=False)[:150],'| verdict',v.get('verdict'),v.get('reason'),'| calls',[c['kind'] for c in d['calls'] if c['kind'] not in('facts','entities','judgements')],'adj_called',os.path.exists('a.log.adj'))
    open(f'r_{nm}.json','w').write(json.dumps(d,ensure_ascii=False))
