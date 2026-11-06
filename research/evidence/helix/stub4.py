import json,sys
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
LOG=sys.argv[1]
class H(BaseHTTPRequestHandler):
    def log_message(self,*a):pass
    def _s(self,d,code=200):
        d=json.dumps(d).encode();self.send_response(code);self.send_header('content-type','application/json');self.send_header('content-length',str(len(d)));self.end_headers();self.wfile.write(d)
    def do_GET(self): self._s({"object":"list","data":[{"id":"stub-d","object":"model"}]})
    def do_POST(self):
        b=json.loads(self.rfile.read(int(self.headers['content-length'])))
        open(LOG,'a').write(json.dumps({"path":self.path,"req":b},ensure_ascii=False)+"\n")
        self._s({"id":"x","object":"chat.completion","created":1,"model":b.get('model'),"usage":{"prompt_tokens":1,"completion_tokens":1,"total_tokens":2},"choices":[{"index":0,"finish_reason":"stop","message":{"role":"assistant","content":"stub"}}]})
ThreadingHTTPServer(("0.0.0.0",18081),H).serve_forever()
