# usage: run.sh <turnjson> <log> <usage> <out>
python3 stub5.py $PWD/$2 $3 & P=$!
docker rm -f oa-t >/dev/null 2>&1
docker create --name oa-t --network polyagent-ontology_default -i --entrypoint ontology-agent -w /data ghcr.io/helixdb/ontology-agent:latest turn --allow-private-model-hosts >/dev/null
docker cp doc.md oa-t:/data/doc.md
timeout 80 docker start -ai oa-t < $1 > $4 2>$4.err; echo rc=$?
kill $P; docker rm -f oa-t >/dev/null
