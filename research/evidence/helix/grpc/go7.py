import json,sys,grpc,time,subprocess,uuid
from client import *
W=sys.argv[1]; s=chan()
BASE="http://ollama-t:11434"
def ep(t=280): return {"provider":{"ollama":{"base_url":BASE}},"call_timeout_secs":t,"max_calls_in_flight":1}
def run(load,db,name,doc,ctx,dry=True,mo=4000):
    spec={"name":"qwen3b-t8","price":"free","reasoning":False,"context_tokens":ctx,"max_output_tokens":mo}
    q={"request_id":"re-"+uuid.uuid4().hex,"database":db,"load":load,"ontology_toml":ONT,"ontology_version":VER,"mappings_toml":MAP,"helix":helix(),
       "documents":[{"doc_id":name,"set":"docs","uri":"file:///"+doc,"path":doc,"media_type":"markdown"}],
       "limits":{"max_usd":100.0,"documents_in_flight":1,"max_text_bytes":5000000},
       "models":{"endpoint":ep(),"extract":spec,"verify":spec},"dry_run":dry}
    t=time.time();evs=[];res=None
    for ev in s.Extract(pb.ExtractRequest(request_json=json.dumps(q))):
        if ev.WhichOneof("kind")=="result_json":res=json.loads(ev.result_json)
        else:evs.append(json.loads(ev.event_json))
    print("##",name,doc,"ctx",ctx,"sec=%.0f"%(time.time()-t),"status",res["status"])
    for d in evs:
        if d.get("event")=="document": print("  outcome",d["outcome"],"sections",d["sections"],"counts",{k:v for k,v in d["counts"].items() if v and k!="resolved"},"resolved",{k:v for k,v in d["counts"]["resolved"].items() if v},"usage",json.dumps(d.get("usage"))[:300])
    for d in evs:
        if d.get("event")=="artifact":
            open(W+f"/real_{name}.json","w").write(d["json"]); a=json.loads(d["json"])["extraction"]
            print("  calls",[ (c["kind"],c["usage"]["input_tokens"],c["usage"]["output_tokens"],round(c["usage"].get("seconds",0))) for c in a.get("calls",[])])
            for o in a.get("outcomes",[]):
                for v in o.get("verdicts",[]):
                    f=(v.get("fact") or {}); c=(f.get("candidate") or {}).get("fact") or f
                    print("  V",v.get("verdict"),v.get("reason"),v.get("confidence"),json.dumps(c,ensure_ascii=False)[:260])
                for u in o.get("unmatched",[]): print("  U",json.dumps(u,ensure_ascii=False)[:160])
                print("  section calls",[(c["kind"],c["usage"]["input_tokens"],c["usage"]["output_tokens"],round(c["usage"].get("seconds",0))) for c in o.get("calls",[])])
if __name__=="__main__":
    print(ingest(s,"LR","hxr")["status"])
    for a in sys.argv[2:]:
        name,doc,ctx=a.split(",")
        try: run("LR","hxr",name,doc,int(ctx))
        except grpc.RpcError as e: print("GRPC",name,e.code(),e.details()[:500])
