import json,sys
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
LOG=sys.argv[1];MSG=sys.argv[2];CODE=sys.argv[3]
class H(BaseHTTPRequestHandler):
    def log_message(self,*a):pass
    def do_POST(self):
        b=json.loads(self.rfile.read(int(self.headers['content-length'])))
        open(LOG,'a').write(json.dumps({"n":len(b['messages'])})+"\n")
        d=json.dumps({"error":{"message":MSG,"type":"invalid_request_error","code":CODE}}).encode()
        self.send_response(400);self.send_header('content-type','application/json');self.send_header('content-length',str(len(d)));self.end_headers();self.wfile.write(d)
ThreadingHTTPServer(("0.0.0.0",18081),H).serve_forever()
