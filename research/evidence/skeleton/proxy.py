# Logging pass-through to Ollama: records request size and raw response for each call.
import http.client,json,sys,time
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
LOG=sys.argv[1]; UP=sys.argv[2]
class H(BaseHTTPRequestHandler):
    protocol_version="HTTP/1.1"
    def log_message(self,*a): pass
    def do_any(self):
        n=int(self.headers.get("content-length") or 0); b=self.rfile.read(n) if n else b""
        t=time.time(); c=http.client.HTTPConnection(UP,11434,timeout=3600)
        c.request(self.command,self.path,b,{"content-type":"application/json"}); r=c.getresponse()
        self.send_response(r.status)
        for k,v in r.getheaders():
            if k.lower() not in("transfer-encoding","connection","content-length"): self.send_header(k,v)
        self.send_header("transfer-encoding","chunked"); self.end_headers()
        out=b""
        while True:
            d=r.read1(65536)
            if not d: break
            out+=d; self.wfile.write(b"%x\r\n"%len(d)+d+b"\r\n"); self.wfile.flush()
        self.wfile.write(b"0\r\n\r\n"); self.wfile.flush()
        q={}
        try: q=json.loads(b or b"{}")
        except Exception: pass
        rec={"path":self.path,"status":r.status,"sec":round(time.time()-t,1),"req_bytes":len(b),"n_messages":len(q.get("messages",[])),"n_tools":len(q.get("tools",[])),"max_tokens":q.get("max_tokens") or q.get("max_completion_tokens"),"resp":out.decode("utf8","replace")}
        open(LOG,"a").write(json.dumps(rec,ensure_ascii=False)+"\n")
    do_POST=do_GET=do_any
ThreadingHTTPServer(("0.0.0.0",18090),H).serve_forever()
