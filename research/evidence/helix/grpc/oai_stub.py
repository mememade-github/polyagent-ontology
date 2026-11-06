import json,sys,os,re,time
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
W=sys.argv[1]; PORT=int(sys.argv[2])
def mode(): return open(W+"/mode").read().strip()
Q="Jane Doe promised Globex a 10% service credit"
def schema(b):
    rf=b.get("response_format") or {}
    return ((rf.get("json_schema") or {}).get("schema")) or {}
def good(b):
    s=schema(b); p=s.get("properties",{})
    txt=json.dumps(b["messages"],ensure_ascii=False)
    if "entities" in p:
        return {"entities":[{"name":"Globex","type":"Customer","aliases":[],"descriptions":[],"identifiers":[]},
                            {"name":"10% service credit","type":"Promise","aliases":[],"descriptions":[],"identifiers":[]}]}
    if "facts" in p:
        if "Jane Doe promised" in txt:
            return {"facts":[{"link":"promised_to","subject":"E2","object":"E1","quote":Q}],"unmatched":[]}
        return {"facts":[],"unmatched":[]}
    if "judgements" in p:
        ids=p["judgements"]["items"]["properties"]["claim"]["enum"]
        return {"judgements":[{"claim":c,"probability":0.95} for c in ids]}
    return None
def kind(b):
    p=schema(b).get("properties",{})
    return "entity" if "entities" in p else "link" if "facts" in p else "verify" if "judgements" in p else "other"
class H(BaseHTTPRequestHandler):
    def log_message(self,*a):pass
    def do_GET(self):
        self.send_response(404);self.end_headers()
    def do_POST(self):
        b=json.loads(self.rfile.read(int(self.headers["content-length"])))
        m=mode();k=kind(b);code=200;finish="stop"
        r=good(b);text=None;err=None
        if m=="prose" : text="Sure! Globex is a customer."
        elif m=="prose_link" and k=="link": text="I found one fact."
        elif m=="prose_verify" and k=="verify": text="It looks right."
        elif m=="wrongkeys" and k=="entity": r={"items":[{"name":"Globex"}]}
        elif m=="trunc" and k=="link": text=json.dumps(r)[:40];finish="length"
        elif m=="trunc_nofinish" and k=="link": text=json.dumps(r)[:40]
        elif m=="ctx400": code=400;err={"error":{"code":"context_length_exceeded","message":"This model maximum context length is 8192 tokens","type":"invalid_request_error"}}
        elif m=="ctx400_llama": code=400;err={"error":{"code":400,"message":"the request exceeds the available context size. try increasing the context size or enable context shift","type":"exceed_context_size_error","n_prompt_tokens":14000,"n_ctx":8192}}
        elif m=="e500": code=500;err={"error":{"message":"boom"}}
        elif m=="link500" and k=="link": code=500;err={"error":{"message":"boom"}}
        elif m=="badenum" and k=="link": r={"facts":[{"link":"invented_link","subject":"E2","object":"E1","quote":Q}],"unmatched":[]}
        elif m=="badid" and k=="link": r={"facts":[{"link":"promised_to","subject":"E99","object":"E1","quote":Q}],"unmatched":[]}
        elif m=="falsefact" and k=="link": r={"facts":[{"link":"promised_to","subject":"E2","object":"E1","quote":"Globex is a customer"}],"unmatched":[]}
        elif m=="empty_entities" and k=="entity": r={"entities":[]}
        elif m=="empty_facts" and k=="link": r={"facts":[],"unmatched":[]}
        elif m=="missclaim" and k=="verify": r={"judgements":[]}
        elif m=="verify_low" and k=="verify":
            ids=schema(b)["properties"]["judgements"]["items"]["properties"]["claim"]["enum"]; r={"judgements":[{"claim":c,"probability":0.3} for c in ids]}
        elif m=="verify_oob" and k=="verify":
            ids=schema(b)["properties"]["judgements"]["items"]["properties"]["claim"]["enum"]; r={"judgements":[{"claim":c,"probability":7} for c in ids]}
        open(W+"/log.jsonl","a").write(json.dumps({"t":time.time(),"mode":m,"kind":k,"code":code,"req":b,"reply":text if text is not None else r},ensure_ascii=False)+"\n")
        if err is not None:
            d=json.dumps(err).encode();self.send_response(code);self.send_header("content-type","application/json");self.send_header("content-length",str(len(d)));self.end_headers();self.wfile.write(d);return
        if text is None:text=json.dumps(r,ensure_ascii=False)
        if b.get("stream"):
            self.send_response(200);self.send_header("content-type","text/event-stream");self.end_headers()
            c={"id":"x","object":"chat.completion.chunk","model":b["model"],"choices":[{"index":0,"delta":{"role":"assistant","content":text},"finish_reason":None}]}
            self.wfile.write(("data: "+json.dumps(c)+"\n\n").encode())
            c["choices"][0]={"index":0,"delta":{},"finish_reason":finish}; c["usage"]={"prompt_tokens":1,"completion_tokens":1,"total_tokens":2}
            self.wfile.write(("data: "+json.dumps(c)+"\n\ndata: [DONE]\n\n").encode());return
        d=json.dumps({"id":"x","object":"chat.completion","created":1,"model":b["model"],"choices":[{"index":0,"message":{"role":"assistant","content":text},"finish_reason":finish}],"usage":{"prompt_tokens":1,"completion_tokens":1,"total_tokens":2}}).encode()
        self.send_response(200);self.send_header("content-type","application/json");self.send_header("content-length",str(len(d)));self.end_headers();self.wfile.write(d)
ThreadingHTTPServer(("0.0.0.0",PORT),H).serve_forever()
