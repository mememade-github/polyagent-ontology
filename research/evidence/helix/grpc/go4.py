import json,sys,grpc
from client import *
W=sys.argv[1]; s=chan(); base="http://__INTERNAL_IP__:18090/v1"
open(W+"/mode","w").write("askprobe")
for ctx in (2000,8000,16000,32000,65536,None):
    n0=sum(1 for _ in open(W+"/log.jsonl"))
    spec={"name":"stub","price":"free","reasoning":False,"max_output_tokens":1000}
    if ctx: spec["context_tokens"]=ctx
    q={"request_id":"ask-%s"%ctx,"database":"hx3","load":"L3","ontology_version":VER,"ontology_toml":ONT,"mappings_toml":MAP,"draft_json":"{}","questions_json":"[]","goal":"Track promises","catalog":[],"question":"What was promised to Globex?","helix":helix(),"as_of":"2026-11-06",
     "limits":{"max_usd":100.0,"max_steps":30,"max_wall_secs":60,"read":{"wall_ms":5000,"scan_entities":20000}},
     "models":{"endpoint":endpoint(base),"ask":spec}}
    last=None
    for ev in s.Ask(pb.AskRequest(request_json=json.dumps(q)),metadata=[("x-foundry-model-key","stub")]):
        if ev.WhichOneof("kind")=="result_json": last=json.loads(ev.result_json)
    L=[json.loads(l) for l in open(W+"/log.jsonl")][n0:]
    print("ctx",ctx,"calls",len(L),"status",last["status"],json.dumps({k:v for k,v in last.items() if k in("reason","gap")},ensure_ascii=False)[:200])
    if L and not __import__("os").path.exists(W+"/ask_req.json"): open(W+"/ask_req.json","w").write(json.dumps(L[0]["req"],ensure_ascii=False))
