import json,sys,re
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
LOG,USAGE=sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 1
ONT_TYPES="[types.Customer]\ndescription = \"A company that buys from us, named in the documents.\"\nprops = { }\n"
ONT_PROM="[types.Promise]\ndescription = \"Something promised to a customer.\"\nprops = { due_on = \"date\" }\n"
LINK="[links.promised_to]\nfrom = \"Promise\"\nto = \"Customer\"\ndescription = \"The promise was made to the customer.\"\n"
CQ="cq.CQ1 = {question = \"What was promised to Globex?\", path = [\"Promise\", \"promised_to>\", \"Customer\"]}\n"
ROUTE="[extractions.calls]\ndocuments = \"all\"\nlinks = [\"promised_to\"]\n[extractions.calls.types.Customer]\n[extractions.calls.types.Promise]\nprops = [\"due_on\"]\n"
def items(ev):
    e=ev[:1]
    return {"items":[
     {"id":"type.Customer","toml":ONT_TYPES,"rationale":"Endpoint of CQ1.","serves":["cq.CQ1"],"evidence_ids":e},
     {"id":"type.Promise","toml":ONT_PROM,"rationale":"Endpoint of CQ1.","serves":["cq.CQ1"],"evidence_ids":e},
     {"id":"link.promised_to","toml":LINK,"rationale":"Path of CQ1.","serves":["cq.CQ1"],"evidence_ids":e},
     {"id":"cq.CQ1","toml":CQ,"rationale":"The user's goal.","serves":[],"evidence_ids":[]},
     {"id":"extraction.calls","toml":ROUTE,"rationale":"Documents fill the promises.","serves":["cq.CQ1"],"evidence_ids":e}]}
STEPS=[("list_sources",lambda ev:{}),("read_text",lambda ev:{"source":"docs1"}),("put_items",items),("check_draft",lambda ev:{}),
 ("finish",lambda ev:{"summary":"Drafted from documents only."})]
class H(BaseHTTPRequestHandler):
    def log_message(self,*a):pass
    def do_GET(self):
        d=json.dumps({"object":"list","data":[{"id":"stub-d","object":"model"}]}).encode();self.send_response(200);self.send_header('content-length',str(len(d)));self.end_headers();self.wfile.write(d)
    def do_POST(self):
        b=json.loads(self.rfile.read(int(self.headers['content-length'])))
        open(LOG,'a').write(json.dumps({"path":self.path,"req":b},ensure_ascii=False)+"\n")
        ms=b['messages'];n=sum(1 for m in ms if m['role']=='assistant')
        ev=re.findall(r'\be\d+\b',' '.join(str(m.get('content')) for m in ms if m['role']=='tool'))
        name,fn=STEPS[min(n,len(STEPS)-1)]
        args=json.dumps(fn(ev))
        self.send_response(200);self.send_header('content-type','text/event-stream');self.end_headers()
        def s(c,fin=None,u=None):
            o={"id":"x","object":"chat.completion.chunk","created":1,"model":b['model'],"choices":[{"index":0,"delta":c,"finish_reason":fin}] if c is not None else []}
            if u:o["usage"]=u
            self.wfile.write(("data: "+json.dumps(o)+"\n\n").encode())
        s({"role":"assistant","tool_calls":[{"index":0,"id":f"c{n}","type":"function","function":{"name":name,"arguments":args}}]})
        s({},"tool_calls")
        s(None,u={"prompt_tokens":USAGE,"completion_tokens":10,"total_tokens":USAGE+10})
        self.wfile.write(b"data: [DONE]\n\n");self.wfile.flush()
ThreadingHTTPServer(("0.0.0.0",18081),H).serve_forever()
