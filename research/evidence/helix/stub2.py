import json,sys,re
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
LOG=sys.argv[1]
def reply(b):
    props=b['output_config']['format']['schema']['properties']
    if 'entities' in props:
        return {"entities":[
          {"name":"Globex","type":"Account","aliases":[],"descriptions":[],"identifiers":[]},
          {"name":"Jane Doe","type":"Contact","aliases":[],"descriptions":[],"identifiers":[]},
          {"name":"10% service credit","type":"Commitment","aliases":[],"descriptions":[],"identifiers":[]},
          {"name":"Initech","type":"Account","aliases":[],"descriptions":[],"identifiers":[]}]}
    if 'facts' in props:
        u=b['messages'][-1]['content']; u=u if isinstance(u,str) else json.dumps(u)
        if 'Jane Doe promised' in u:
            q="Jane Doe promised Globex a 10% service credit"
            return {"facts":[
              {"link":"promised_to","subject":"E3","object":"E1","quote":q},
              {"link":"promised_to","subject":"E3","object":"E4","quote":q},
              {"link":"contact_at","subject":"E2","object":"E1","quote":"Jane Doe promised Globex"},
              {"link":"promised_to","subject":"E3","object":"E1","quote":"Jane Doe guaranteed a full refund"},
              {"link":"promised_to","subject":"E2","object":"E1","quote":q}],
              "unmatched":[{"quote":"on the call","suggested_link":"mentioned_on"}]}
        return {"facts":[],"unmatched":[]}
    if 'judgements' in props:
        ids=props['judgements']['items']['properties']['claim']['enum']; P=[0.95,0.7,0.2]
        return {"judgements":[{"claim":c,"probability":P[i%3]} for i,c in enumerate(ids)]}
    return None
class H(BaseHTTPRequestHandler):
    def log_message(self,*a):pass
    def do_POST(self):
        b=json.loads(self.rfile.read(int(self.headers['content-length'])))
        r=reply(b)
        open(LOG,'a').write(json.dumps({"req":b,"reply":r},ensure_ascii=False)+"\n")
        if r is None:
            d=json.dumps({"type":"error","error":{"type":"invalid_request_error","message":"probe"}}).encode(); code=400
        else:
            d=json.dumps({"id":"m","type":"message","role":"assistant","model":b['model'],"stop_reason":"end_turn","content":[{"type":"text","text":json.dumps(r)}],"usage":{"input_tokens":0,"output_tokens":0}}).encode(); code=200
        self.send_response(code);self.send_header('content-type','application/json');self.send_header('content-length',str(len(d)));self.end_headers();self.wfile.write(d)
ThreadingHTTPServer(("0.0.0.0",18081),H).serve_forever()
