import json,subprocess,os,time
W=os.getcwd()+'/'
for nm,reply in (('bare_array',[{"entity":"E1","choice":"K1","confidence":0.99}]),('value_1.0',{"value":[{"entity":"E1","choice":"K1","confidence":1.0}]})):
    for f in('a.log','a.log.adj'):
        if os.path.exists(f):os.remove(f)
    json.dump(reply,open('a.log.reply','w'))
    p=subprocess.Popen(['python3','stub_adj.py',W+'a.log'],env={**os.environ,'ENAME':'Globex Inc'},stderr=subprocess.DEVNULL);time.sleep(.3)
    r=subprocess.run('bash ex.sh',shell=True,capture_output=True,text=True);p.kill();p.wait()
    t=r.stdout;i=t.find('{"attributes')
    print(nm,'ERR '+(t+r.stderr)[:400] if i<0 else json.JSONDecoder().raw_decode(t[i:])[0]['resolutions'][0])
