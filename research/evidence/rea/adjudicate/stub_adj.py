import json,sys
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
LOG=sys.argv[1]
def reply(b):
    s=b['output_config']['format']['schema'];p=s['properties']
    if 'entities' in p: return {"entities":[{"name":__import__("os").environ.get("ENAME","Globex Inc"),"type":"Account","aliases":[],"descriptions":[],"identifiers":[]},{"name":"10% service credit","type":"Commitment","aliases":[],"descriptions":[],"identifiers":[]}]}
    if 'facts' in p:
        if 'Jane Doe promised' in str(b['messages'][-1]['content']): return {"facts":[{"link":"promised_to","subject":"E2","object":"E1","quote":"Jane Doe promised Globex a 10% service credit","props":[]}],"unmatched":[]}
        return {"facts":[],"unmatched":[]}
    if 'judgements' in p: return {"judgements":[{"claim":c,"probability":0.95} for c in p['judgements']['items']['properties']['claim']['enum']]}
    return None
class H(BaseHTTPRequestHandler):
    def log_message(self,*a):pass
    def do_POST(self):
        b=json.loads(self.rfile.read(int(self.headers['content-length'])));r=reply(b)
        if r is None:
            # adjudication call: answer from the schema, recording it verbatim
            print('OTHER',list(b['output_config']['format']['schema']['properties']),file=sys.stderr)
            it=b['output_config']['format']['schema']
            open(LOG+'.adj','a').write(json.dumps(b,ensure_ascii=False)+"\n")
            r=json.loads(open(LOG+'.reply').read()) if __import__('os').path.exists(LOG+'.reply') else {"assessments":[]}
        open(LOG,'a').write(json.dumps({"req":b,"reply":r},ensure_ascii=False)+"\n")
        d=json.dumps({"id":"m","type":"message","role":"assistant","model":b['model'],"stop_reason":"end_turn","content":[{"type":"text","text":json.dumps(r)}],"usage":{"input_tokens":0,"output_tokens":0}}).encode()
        self.send_response(200);self.send_header('content-type','application/json');self.send_header('content-length',str(len(d)));self.end_headers();self.wfile.write(d)
ThreadingHTTPServer(("0.0.0.0",18081),H).serve_forever()
