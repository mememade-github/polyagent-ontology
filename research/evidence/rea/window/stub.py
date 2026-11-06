import json,sys
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
LOG=sys.argv[1]
class H(BaseHTTPRequestHandler):
    def log_message(self,*a):pass
    def do_POST(self):
        b=json.loads(self.rfile.read(int(self.headers['content-length'])));p=b['output_config']['format']['schema']['properties']
        r={"entities":[{"name":"Globex","type":"Account","aliases":[],"descriptions":[],"identifiers":[]},{"name":"Credit","type":"Commitment","aliases":[],"descriptions":[],"identifiers":[]}]} if 'entities' in p else {"facts":[],"unmatched":[]} if 'facts' in p else {"judgements":[]}
        open(LOG,'a').write(json.dumps({"req":b},ensure_ascii=False)+"\n")
        d=json.dumps({"id":"m","type":"message","role":"assistant","model":b['model'],"stop_reason":"end_turn","content":[{"type":"text","text":json.dumps(r)}],"usage":{"input_tokens":0,"output_tokens":0}}).encode()
        self.send_response(200);self.send_header('content-type','application/json');self.send_header('content-length',str(len(d)));self.end_headers();self.wfile.write(d)
ThreadingHTTPServer(("0.0.0.0",18081),H).serve_forever()
