cd __SCRATCH__/sk
docker exec ollama-t sh -c 'printf "FROM qwen2.5:3b\nPARAMETER num_thread 14\nPARAMETER num_ctx 65536\n" > /tmp/M; ollama create qwen3b-c64 -f /tmp/M' >/dev/null 2>&1
cat > mk2.py <<'P'
import json,sys
name,prov,model,ctx,mo,doc,table,wall=sys.argv[1:9]
spec=lambda:{"name":model,"price":"free","reasoning":False,"context_tokens":int(ctx),"max_output_tokens":int(mo)}
src=[{"id":"docs1","display_name":"call notes","description":"Notes from customer calls","route":"extraction","access":{"documents":{"files":[{"doc_id":"d1","path":doc,"media_type":"markdown","title":"call notes"}]}},"fingerprint":"fp1"}]
if table=="table": src.append({"id":"accounts","display_name":"accounts","description":"Customer accounts table","route":{"mapping":{"trust":1.0}},"access":{"file":{"path":"accounts.jsonl","format":"jsonl"}},"fingerprint":"fp2"})
p={"ollama":{"ollama":{"base_url":"http://ollama-t:11434"}},"oai":{"openai_compatible":{"base_url":"http://ollama-t:11434/v1","api":"chat_completions"}}}[prov]
t={"session_id":name,"request_id":"r-"+name,"state":None,"sources":src,"input":{"start":{"workflow":"Track promises made to customers","goals":["What was promised to each customer?","When is each promise due?"]}},
"limits":{"max_usd":100.0,"max_steps":30,"max_wall_secs":int(wall)},
"models":{"endpoint":{"provider":p,"call_timeout_secs":3000},"draft":spec(),"extract":spec(),"verify":spec()}}
json.dump(t,open(name+".json","w"))
P
turn(){ n=$1; shift; python3 mk2.py $n "$@"; doc=$5
 docker rm -f oa-t >/dev/null 2>&1
 docker create --name oa-t --network polyagent-ontology_default -i --entrypoint ontology-agent -w /data ghcr.io/helixdb/ontology-agent:latest turn --allow-private-model-hosts >/dev/null
 docker cp $doc oa-t:/data/$doc; docker cp accounts.jsonl oa-t:/data/accounts.jsonl
 s=$(date +%s); since=$(date -u +%FT%TZ)
 timeout 100 docker start -ai oa-t < $n.json > $n.out 2> $n.err; rc=$?
 echo "## $n rc=$rc sec=$(( $(date +%s)-s )) :: $(grep -o '"status":"[a-z_]*"' $n.out | tail -1) calls=$(docker logs --since $since ollama-t 2>&1 | grep -c -E 'POST +"/(api/chat|v1/chat)') $(grep -o '"text":"[^"]*"' $n.out | cut -c1-110 | tr '\n' ' ')"
 docker rm -f oa-t >/dev/null
}
turn s1 ollama qwen3b-t14 65536 256 doc.md no 60
turn s2 ollama qwen3b-t14 131072 256 doc.md no 60
turn s3 ollama qwen3b-t14 65536 0 doc.md no 60
turn s4 oai qwen3b-c64 65536 2000 doc.md no 60
turn s5 oai qwen3b-c64 200000 2000 doc.md no 60
