import json,sys,grpc,os
from client import *
W=sys.argv[1]; s=chan(); base="http://__INTERNAL_IP__:18090/v1"
open(W+"/mode","w").write("askprobe")
for ctx,mo in ((None,None),(None,1000),(None,4000),(None,16000),(2000,None),(8000,None),(16000,None),(32000,None),(40000,None),(65536,None),(65536,4000),(8000,1000)):
    n0=sum(1 for _ in open(W+"/log.jsonl"))
    spec={"name":"stub","price":"free","reasoning":False}
    if ctx: spec["context_tokens"]=ctx
    if mo: spec["max_output_tokens"]=mo
    q={"request_id":"ask6-%s-%s"%(ctx,mo),"database":"hx3","load":"L3","ontology_version":VER,"ontology_toml":ONT,"mappings_toml":MAP,"draft_json":"{}","questions_json":"[]","goal":"Track promises","catalog":[],"question":"What was promised to Globex?","helix":helix(),"as_of":"2026-11-06",
     "limits":{"max_usd":100.0,"max_steps":30,"max_wall_secs":60,"read":{"wall_ms":5000,"scan_entities":20000}},
     "models":{"endpoint":endpoint(base),"ask":spec}}
    last=None
    for ev in s.Ask(pb.AskRequest(request_json=json.dumps(q)),metadata=[("x-foundry-model-key","stub")]):
        if ev.WhichOneof("kind")=="result_json": last=json.loads(ev.result_json)
    L=[json.loads(l) for l in open(W+"/log.jsonl")][n0:]
    print("ctx",ctx,"maxout",mo,"calls",len(L),"status",last["status"],last.get("reason"),"max_tokens_sent",L[0]["req"].get("max_tokens") if L else None)
    if L: open(W+"/ask_req.json","w").write(json.dumps(L[0]["req"],ensure_ascii=False))
