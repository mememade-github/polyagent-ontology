import json,sys,subprocess,time,grpc
from client import *
W=sys.argv[1]
s=chan()
print("INGEST",ingest(s,"L1"))
MODES=sys.argv[2:]
base="http://__INTERNAL_IP__:18090/v1"
for m in MODES:
    name,_,opt=m.partition(":")
    open(W+"/mode","w").write(name)
    n0=sum(1 for _ in open(W+"/log.jsonl")) if __import__("os").path.exists(W+"/log.jsonl") else 0
    t=time.time()
    kw=json.loads(opt) if opt else {}
    try:
        evs,res=extract(s,"L1",[("d1","doc.md")],base,**kw)
        doc=[e for e in evs if e.get("event")=="document"]
        arts=[e for e in evs if e.get("event")=="artifact"]
        print("##",m,"sec=%.1f"%(time.time()-t))
        print("  result",json.dumps(res,ensure_ascii=False)[:300])
        for d in doc: print("  outcome",json.dumps(d["outcome"]),"counts",json.dumps(d["counts"],ensure_ascii=False))
        if arts:
            a=json.loads(arts[0]["json"]); open(W+"/art_"+name+".json","w").write(arts[0]["json"]); print("  artifact keys",list(a)[:12])
    except grpc.RpcError as e:
        print("##",m,"GRPC",e.code(),e.details()[:400])
    L=[json.loads(l) for l in open(W+"/log.jsonl")][n0:]
    from collections import Counter
    print("  calls",dict(Counter((x["kind"],x["code"]) for x in L)))
