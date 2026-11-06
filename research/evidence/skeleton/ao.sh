S=__SCRATCH__; P=$S/proof; D=$S/sk; cd $P
docker rm -f ao-proof-pg >/dev/null 2>&1
PW=$(grep -o 'POSTGRES_PASSWORD=[^ ]*' env.sh | cut -d= -f2)
docker run -d --name ao-proof-pg --network polyagent-ontology_default -e POSTGRES_PASSWORD=$PW -e POSTGRES_DB=auto_ontology pgvector/pgvector:pg17 >/dev/null; sleep 8
PG=$(docker inspect ao-proof-pg --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'); OU=$(docker inspect ollama-t --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}')
cat > $D/aoproxy.py <<'PY'
# Chat goes to the real model; embeddings stay hashed (no embedding model in this run).
import hashlib,json,math,re,sys,time,http.client
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
LOG,UP=sys.argv[1],sys.argv[2]; DIM=2048
def emb(t):
    v=[0.0]*DIM
    for w in re.findall(r"[a-z0-9가-힣]+",t.lower()): v[int(hashlib.md5(w.encode()).hexdigest(),16)%DIM]+=1.0
    n=math.sqrt(sum(x*x for x in v)) or 1.0
    return [x/n for x in v]
class H(BaseHTTPRequestHandler):
    def log_message(self,*a): pass
    def do_POST(self):
        b=json.loads(self.rfile.read(int(self.headers["content-length"])))
        if self.path.endswith("/embeddings"):
            i=b["input"]; i=i if isinstance(i,list) else [i]
            out=json.dumps({"object":"list","model":b.get("model"),"data":[{"object":"embedding","index":k,"embedding":emb(str(x))} for k,x in enumerate(i)],"usage":{"prompt_tokens":1,"total_tokens":1}}).encode(); st=200
        else:
            b["model"]="qwen3b-c8"; b.pop("stream_options",None); t=time.time()
            c=http.client.HTTPConnection(UP,11434,timeout=1800); c.request("POST","/v1/chat/completions",json.dumps(b),{"content-type":"application/json"}); r=c.getresponse(); out=r.read(); st=r.status
            open(LOG,"a").write(json.dumps({"sec":round(time.time()-t,1),"status":st,"req_chars":sum(len(str(m.get("content"))) for m in b["messages"]),"sys":str(b["messages"][0].get("content"))[:80],"user":str(b["messages"][-1].get("content"))[:1500],"tools":[x["function"]["name"] for x in b.get("tools",[])],"rf":str(b.get("response_format"))[:120],"resp":out.decode("utf8","replace")[:4000]},ensure_ascii=False)+"\n")
        self.send_response(st); self.send_header("content-type","application/json"); self.send_header("content-length",str(len(out))); self.end_headers(); self.wfile.write(out)
ThreadingHTTPServer(("127.0.0.1",18080),H).serve_forever()
PY
: > $D/ao.log
python3 $D/aoproxy.py $D/ao.log $OU & PX=$!; sleep 1
sed "s/POSTGRES_HOST=[^ ]*/POSTGRES_HOST=$PG/" env.sh > $D/ao_env.sh; . $D/ao_env.sh
(cd $S/upstream/auto-ontology && $S/venv-ao/bin/alembic upgrade head 2>&1 | tail -1 | cut -c1-120)
psql(){ docker exec ao-proof-pg psql -U postgres -d auto_ontology "$@"; }
for db in shop docs; do
 echo "##### $db" ; s=$(date +%s)
 timeout 2400 $S/venv-ao/bin/python run_pipeline.py $P/src/$db.sqlite 2>&1 | grep -vE 'No connections' | tail -6 | cut -c1-240
 echo "sec=$(( $(date +%s)-s ))"
 psql -c "select name,left(description,120) d,source from term order by 1" 2>&1 | head -14
 psql -c "select term_name,name,source_column from column_attribute order by 1,3" 2>&1 | head -24
 psql -c "select count(*) semantic_fk from column__semantic_fk" 2>&1 | sed -n 3p
 cp $D/ao.log $D/ao_$db.calls; wc -l < $D/ao.log
 psql -qc "truncate term, column_attribute, catalog_database cascade" 2>&1 | head -2; psql -qc "truncate semantic_layer, data_objects_layer" 2>&1 | head -2; : > $D/ao.log
done
kill $PX; echo done
