import json,sys,subprocess,time,grpc
from client import *
from collections import Counter
W=sys.argv[1]; s=chan(); base="http://__INTERNAL_IP__:18090/v1"
open(W+"/mode","w").write("ok")
EN="The supplier shall deliver the goods to the buyer within thirty days of the order date and Jane Doe promised Globex a 10% service credit. "
KO="공급자는 주문일로부터 삼십일 이내에 물품을 구매자에게 인도하여야 하며 제인 도우는 글로벡스에 십 퍼센트 서비스 크레딧을 약속하였다. "
def mk(name,unit,target):
    paras=[];n=0;i=0
    while n<target:
        p=("## Section %d\n\n"%i if i%8==0 else "")+unit*3+"\n\n"; paras.append(p); n+=len(p.encode()); i+=1
    open(W+"/"+name,"w").write("".join(paras))
    subprocess.run(f"docker cp {W}/{name} oa-s:/tmp/{name}; docker exec -u 0 oa-s cp /tmp/{name} /data/{name}",shell=True,check=True)
ingest(s,"L2","hx2")
for lang,unit in (("en",EN),("ko",KO)):
  for kb in (5,15,25,35,45,60,120):
    name=f"{lang}{kb}.md"; mk(name,unit,kb*1000)
    for ctx in (8000,):
        n0=sum(1 for _ in open(W+"/log.jsonl"))
        t=time.time()
        evs,res=extract(s,"L2",[("d"+name,name)],base,db="hx2",ctx=ctx,maxout=1000)
        d=[e for e in evs if e.get("event")=="document"][0]
        L=[json.loads(l) for l in open(W+"/log.jsonl")][n0:]
        print(lang,kb,"KB ctx",ctx,"outcome",d["outcome"],"sections",d["sections"],"calls",dict(Counter(x["kind"] for x in L)),"max_tokens_sent",sorted({x["req"].get("max_tokens") for x in L},key=str),"facts",d["counts"]["facts"],"rejected",d["counts"]["rejected"])
