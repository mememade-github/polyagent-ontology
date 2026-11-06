"""OpenAI-compatible stub. No intelligence: logs every prompt, answers by schema name.
Purpose: expose exactly what the pipeline sends to an LLM and how code treats the reply.
Deliberately injects a hallucinated column to exercise the sanitizer."""
import hashlib, json, math, re, sys, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
LOG = sys.argv[1]; DIM = 2048
def embed(t):
    v=[0.0]*DIM
    for w in re.findall(r"[a-z0-9가-힣]+", t.lower()):
        v[int(hashlib.md5(w.encode()).hexdigest(),16)%DIM]+=1.0
    n=math.sqrt(sum(x*x for x in v)) or 1.0
    return [x/n for x in v]
def cols(p):
    return re.findall(r"source_column=(\S+)", p)
def answer(name, msgs, schema):
    u = "\n".join(str(m.get("content")) for m in msgs if m["role"]!="system")
    if name=="RawTableTermsResult":
        t=re.search(r"Table: (\S+)",u).group(1)
        attrs=[{"source_column":c,"display_name":" ".join(w.capitalize() for w in c.split("_"))} for c in cols(u)]
        attrs.append({"source_column":"ghost_column","display_name":"Ghost Column"})   # hallucination
        if len(attrs)>2: attrs.pop(0)                                                    # omission
        return {"terms":[{"name":" ".join(w.capitalize() for w in t.split("_")),"description":f"Business entity from {t}","attributes":attrs}]}
    if name=="FkAndPkResult":
        s=[{"column_name":m,"rationale":"name ends with _id"} for m in re.findall(r"\b([a-z_]+_id)\b",u)]
        return {"fk_suggestions":[],"pk_column_names":[],"is_junction_table":False,"junction_table_rationale":""}
    if name=="ColumnDescriptionResult":
        return {"descriptions":[{"column_name":c,"description":f"Stub description of {c}."} for c in re.findall(r"^\s*- (\S+) \(",u,re.M)]}
    if name=="QuestionExtractionModel":
        q="Total ad spend per region" if "ad spend" in u else "How many customers per region"
        return {"sanitized_question":q,"required_entity_name":["region","customers"],"subject":"customers","used_glossary_names":[]}
    if name=="SQLGenerationModel":
        n=len([1 for l in open(LOG) if '"schema": "SQLGenerationModel"' in l])
        bad="ghost" in u.lower() or "ad spend" in u.lower()
        sql=("SELECT g.spend FROM ghost_ads g" if bad and n==0 else "SELECT region, COUNT(*) AS n FROM customers GROUP BY region")
        return {"thought":"stub","sql_code":sql,"response":"stub"}
    if name and re.search(r"(?i)sql",name) and "sql" in json.dumps(schema).lower():
        props=schema.get("properties",{})
        base=minimal(schema,schema.get("$defs",{}))
        for k in props:
            if k in("sql","sql_query","query"): base[k]="SELECT c.region, COUNT(*) AS n FROM customers c GROUP BY c.region"
        return base
    return None
def minimal(s, defs):
    if "$ref" in s: return minimal(defs[s["$ref"].split("/")[-1]],defs)
    if "anyOf" in s: return minimal(s["anyOf"][0],defs)
    if "enum" in s: return s["enum"][0]
    if "const" in s: return s["const"]
    if "default" in s: return s["default"]
    t=s.get("type")
    if t=="object": return {k:minimal(v,defs) for k,v in s.get("properties",{}).items()}
    if t=="array": return []
    return {"string":"","integer":0,"number":0,"boolean":False,"null":None}.get(t)
class H(BaseHTTPRequestHandler):
    def log_message(self,*a): pass
    def do_POST(self):
        b=json.loads(self.rfile.read(int(self.headers["content-length"])))
        if self.path.endswith("/embeddings"):
            i=b["input"]; i=[i] if isinstance(i,str) else i
            with open(LOG,"a") as f: f.write(json.dumps({"kind":"embed","input":i},ensure_ascii=False)+"\n")
            out={"object":"list","model":b["model"],"usage":{"prompt_tokens":0,"total_tokens":0},"data":[{"object":"embedding","index":n,"embedding":embed(t)} for n,t in enumerate(i)]}
        else:
            rf=b.get("response_format") or {}; js=rf.get("json_schema") or {}
            name=js.get("name"); schema=js.get("schema") or {}
            if not name and b.get("tools"):
                fn=b["tools"][0]["function"]; name=fn["name"]; schema=fn["parameters"]
            r=answer(name,b["messages"],schema)
            with open(LOG+".names","a") as f: f.write(str(name)+" "+",".join(schema.get("properties",{}).keys())+"\n")
            if r is None: r=minimal(schema,schema.get("$defs",{})) if schema else "stub"
            with open(LOG,"a") as f: f.write(json.dumps({"kind":"chat","schema":name,"messages":b["messages"],"reply":r},ensure_ascii=False)+"\n")
            content=r if isinstance(r,str) else json.dumps(r)
            out={"id":"x","object":"chat.completion","created":int(time.time()),"model":b["model"],"usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0},
                 "choices":[{"index":0,"finish_reason":"stop","message":{"role":"assistant","content":content}}]}
        d=json.dumps(out).encode(); self.send_response(200); self.send_header("content-type","application/json"); self.send_header("content-length",str(len(d))); self.end_headers(); self.wfile.write(d)
ThreadingHTTPServer(("127.0.0.1",18080),H).serve_forever()
