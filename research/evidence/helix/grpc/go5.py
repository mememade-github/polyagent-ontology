import json,sys,grpc
from client import *
W=sys.argv[1]; s=chan(); base="http://__INTERNAL_IP__:18090/v1"
open(W+"/mode","w").write("askprobe")
for label,lim in (("usd100",dict(max_usd=100.0,max_steps=30,max_wall_secs=60)),("steps100_wall600",dict(max_usd=100.0,max_steps=100,max_wall_secs=600)),("maxsteps1000",dict(max_usd=1000.0,max_steps=1000,max_wall_secs=3600))):
    n0=sum(1 for _ in open(W+"/log.jsonl"))
    q={"request_id":"ask-"+label,"database":"hx3","load":"L3","ontology_version":VER,"ontology_toml":ONT,"mappings_toml":MAP,"draft_json":"{}","questions_json":"[]","goal":"Track promises","catalog":[],"question":"What was promised to Globex?","helix":helix(),"as_of":"2026-11-06",
     "limits":{**lim,"read":{"wall_ms":5000,"scan_entities":20000}},
     "models":{"endpoint":endpoint(base),"ask":{"name":"stub","price":"free","reasoning":False}}}
    for ev in s.Ask(pb.AskRequest(request_json=json.dumps(q)),metadata=[("x-foundry-model-key","stub")]):
        k=ev.WhichOneof("kind");print(label,k,getattr(ev,k)[:300])
    L=[json.loads(l) for l in open(W+"/log.jsonl")][n0:]
    print(label,"calls",len(L))
    if L: open(W+"/ask_req.json","w").write(json.dumps(L[0]["req"],ensure_ascii=False))
