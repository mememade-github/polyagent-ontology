import json,subprocess,os,time
W=os.getcwd()+'/'
for ename in ('Globex renewal',):
    for f in('a.log','a.log.adj'):
        if os.path.exists(f):os.remove(f)
    json.dump({"value":[{"entity":"E1","choice":"K1","confidence":0.99}]},open('a.log.reply','w'))
    p=subprocess.Popen(['python3','stub_adj.py',W+'a.log'],env={**os.environ,'ENAME':ename},stderr=subprocess.DEVNULL);time.sleep(.3)
    r=subprocess.run('bash ex.sh',shell=True,capture_output=True,text=True);p.kill();p.wait()
    t=r.stdout;i=t.find('{"attributes');d=json.JSONDecoder().raw_decode(t[i:])[0]
    print(ename,d['resolutions'][0],[c['kind'] for c in d['calls'] if c['kind']=='adjudicate'])
