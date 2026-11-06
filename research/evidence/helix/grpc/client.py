import json,sys,grpc,time,uuid
sys.path.insert(0,".")
from ontology_agent.v1 import agent_pb2 as pb, agent_pb2_grpc as gr
E="__RESEARCH__/evidence/rea/approval/"
ONT=open(E+"bundle_ontology.toml").read(); MAP=open(E+"bundle_mappings.toml").read()
VER="2026-11-06.1"
MAP=MAP.replace("[extractions.calls.types.Customer]","[extractions.calls.types.Customer]\ncreate = true").replace("[extractions.calls.types.Promise]","[extractions.calls.types.Promise]\ncreate = true")
def chan(addr=open("run/addr").read().strip()):
    return gr.AgentStub(grpc.insecure_channel(addr,options=[("grpc.max_receive_message_length",32<<20),("grpc.max_send_message_length",32<<20)]))
def helix(): return {"url":"http://hx-db:8080","token":"x","max_request_bytes":10000000,"timeout_secs":60}
def ingest(s,load,db="hxdb"):
    q={"request_id":"ing-"+load,"database":db,"load":load,"ontology_toml":ONT,"ontology_version":VER,"helix":helix(),"mappings_toml":MAP,"sources":[],"chunk_rows":100}
    res=None
    for ev in s.Ingest(pb.IngestRequest(request_json=json.dumps(q))):
        if ev.WhichOneof("kind")=="result_json":res=json.loads(ev.result_json)
    return res
def endpoint(base,timeout=60,inflight=2): return {"provider":{"openai_compatible":{"api":"chat_completions","base_url":base}},"call_timeout_secs":timeout,"max_calls_in_flight":inflight}
def extract(s,load,docs,base,db="hxdb",dry=True,ctx=None,maxout=None,timeout=60,model="stub",inflight=2,auto=False,maxusd=1.0):
    spec=lambda n:{k:v for k,v in {"name":n,"price":"free","reasoning":False,"context_tokens":ctx,"max_output_tokens":maxout}.items() if v is not None}
    q={"request_id":"ex-"+uuid.uuid4().hex,"database":db,"load":load,"ontology_toml":ONT,"ontology_version":VER,"mappings_toml":MAP,"helix":helix(),
       "documents":[{"doc_id":d,"set":"docs","uri":"file:///"+p,"path":p,"media_type":"markdown"} for d,p in docs],
       "limits":{"max_usd":maxusd,"documents_in_flight":1,"max_text_bytes":5000000},
       "models":{"endpoint":endpoint(base,timeout,inflight),"extract":spec(model),"verify":spec(model)},"dry_run":dry,"adjudication":{"auto":auto}}
    evs=[];res=None
    md=[("x-foundry-model-key","stub")]
    for ev in s.Extract(pb.ExtractRequest(request_json=json.dumps(q)),metadata=md):
        if ev.WhichOneof("kind")=="result_json":res=json.loads(ev.result_json)
        else:evs.append(json.loads(ev.event_json))
    return evs,res
