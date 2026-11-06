cd __SCRATCH__/sk; rm -f DONE summary.txt
OU=$(docker inspect ollama-t --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'); ME=$(hostname -i | awk '{print $1}')
python3 proxy.py proxy.log $OU & PX=$!
sleep 1
docker exec ollama-t sh -c 'printf "FROM qwen2.5:3b\nPARAMETER num_thread 14\nPARAMETER num_ctx 8192\n" > /tmp/M; ollama create qwen3b-c8 -f /tmp/M' >/dev/null 2>&1
sed -i "s#http://ollama-t:11434/v1#http://$ME:18090/v1#" mk2.py
turn(){ n=$1; shift; python3 mk2.py $n "$@"; doc=$5; wall=$7
 docker rm -f oa-t >/dev/null 2>&1
 docker create --name oa-t --network polyagent-ontology_default -i --entrypoint ontology-agent -w /data ghcr.io/helixdb/ontology-agent:latest turn --allow-private-model-hosts >/dev/null
 docker cp $doc oa-t:/data/$doc; docker cp accounts.jsonl oa-t:/data/accounts.jsonl
 s=$(date +%s); since=$(date -u +%FT%TZ); : > proxy.log
 timeout $((wall+300)) docker start -ai oa-t < $n.json > $n.out 2> $n.err; rc=$?
 echo "$n rc=$rc sec=$(( $(date +%s)-s )) $(grep -o '"status":"[a-z_]*"' $n.out | tail -1) calls=$(wc -l < proxy.log)" >> summary.txt
 cp proxy.log $n.calls; docker logs --since $since ollama-t 2>&1 | grep -E 'truncat|n_ctx|level=(WARN|ERROR)' | cut -c1-220 > $n.ollama
 docker rm -f oa-t >/dev/null
}
turn t1_ctx8k_doc oai qwen3b-c8 8192 2000 doc.md no 2400
turn t1b_ctxclaim64k_real8k oai qwen3b-c8 65536 2000 doc.md no 2400
turn t2_ctx64k_doc oai qwen3b-c64 65536 2000 doc.md no 7200
turn t3_ctx64k_gold_table oai qwen3b-c64 65536 2000 gold.md table 7200
kill $PX; echo done > DONE
