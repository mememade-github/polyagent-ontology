import json,sys,grpc,time
from client import *
W=sys.argv[1]; s=chan(); BASE="http://ollama-t:11434"
print("ING",ingest(s,"LR2","hxr2")["status"])
spec={"name":"qwen3b-t8","price":"free","reasoning":False,"context_tokens":8192,"max_output_tokens":4000}
q={"request_id":"wr","database":"hxr2","load":"LR2","ontology_toml":ONT,"ontology_version":VER,"mappings_toml":MAP,"helix":helix(),"documents":[{"doc_id":"d1","set":"docs","uri":"file:///doc.md","path":"doc.md","media_type":"markdown"}],"limits":{"max_usd":100.0,"documents_in_flight":1,"max_text_bytes":5000000},"models":{"endpoint":{"provider":{"ollama":{"base_url":BASE}},"call_timeout_secs":280,"max_calls_in_flight":1},"extract":spec,"verify":spec},"dry_run":False}
for ev in s.Extract(pb.ExtractRequest(request_json=json.dumps(q))):
    if ev.WhichOneof("kind")=="result_json": r=json.loads(ev.result_json);print("EXTRACT",r["status"],json.dumps(r["totals"]["counts"])[:200])
for ctx,mo,w in ((8192,4000,120),(32768,4000,290),(65536,4000,290)):
    sp={"name":"qwen3b-t8","price":"free","reasoning":False,"context_tokens":ctx,"max_output_tokens":mo}
    a={"request_id":"ar-%d"%ctx,"database":"hxr2","load":"LR2","ontology_version":VER,"ontology_toml":ONT,"mappings_toml":MAP,"draft_json":"{}","questions_json":"[]","goal":"Track promises","catalog":[],"question":"What was promised to Globex?","helix":helix(),"as_of":"2026-11-06","limits":{"max_usd":100.0,"max_steps":12,"max_wall_secs":w,"read":{"wall_ms":5000,"scan_entities":20000}},"models":{"endpoint":{"provider":{"ollama":{"base_url":BASE}},"call_timeout_secs":280,"max_calls_in_flight":1},"ask":sp}}
    t=time.time()
    try:
        for ev in s.Ask(pb.AskRequest(request_json=json.dumps(a))):
            k=ev.WhichOneof("kind")
            print("ctx",ctx,k,getattr(ev,k)[:900],flush=True)
    except grpc.RpcError as e: print("ctx",ctx,"GRPC",e.code(),e.details()[:300])
    print("ctx",ctx,"sec=%.0f"%(time.time()-t),flush=True)
