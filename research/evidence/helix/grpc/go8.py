import json,sys,grpc,time,uuid,subprocess
from client import *
W=sys.argv[1]; s=chan(); BASE="http://ollama-t:11434"
ep=lambda t:{"provider":{"ollama":{"base_url":BASE}},"call_timeout_secs":t,"max_calls_in_flight":1}
ingest(s,"LR","hxr")
def one(doc,ctx,mo):
    spec={"name":"qwen3b-t8","price":"free","reasoning":False,"context_tokens":ctx,"max_output_tokens":mo}
    q={"request_id":"sw-"+uuid.uuid4().hex,"database":"hxr","load":"LR","ontology_toml":ONT,"ontology_version":VER,"mappings_toml":MAP,"helix":helix(),
       "documents":[{"doc_id":doc+str(ctx)+str(mo),"set":"docs","uri":"file:///"+doc,"path":doc,"media_type":"markdown"}],"limits":{"max_usd":100.0,"documents_in_flight":1,"max_text_bytes":5000000},
       "models":{"endpoint":ep(1),"extract":spec,"verify":spec},"dry_run":True}
    t=time.time()
    for ev in s.Extract(pb.ExtractRequest(request_json=json.dumps(q))):
        if ev.WhichOneof("kind")=="event_json":
            e=json.loads(ev.event_json)
            if e.get("event")=="document": print(doc,"ctx",ctx,"maxout",mo,"=>",e["outcome"].get("model_failure") or e["outcome"]["kind"],"sec=%.1f"%(time.time()-t),flush=True)
for kb in (5,15,25,35,45):
    for lang in ("en","ko"):
        d=f"{lang}{kb}.md"
        subprocess.run(f"docker cp {W}/{d} oa-s:/tmp/{d}; docker exec -u 0 oa-s cp /tmp/{d} /data/{d}",shell=True)
        for ctx,mo in ((8192,1000),(8192,4000),(4096,1000),(16384,4000),(65536,4000)):
            one(d,ctx,mo)
