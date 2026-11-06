S=__SCRATCH__; W=$S/hxg/run
NET=polyagent-ontology_default
docker rm -f hx-db oa-s >/dev/null 2>&1
docker run -d --name hx-db --network $NET -e HELIX_DATA_DIR=/var/lib/helix ghcr.io/helixdb/helixdb:v0.0.12 >/dev/null
docker create --name oa-s --network $NET -p 127.0.0.1:50061:50061 --entrypoint ontology-agent ghcr.io/helixdb/ontology-agent:latest serve --files-root /data --addr 0.0.0.0:50061 --allow-private-model-hosts >/dev/null
docker cp $W/doc.md oa-s:/tmp/doc.md 2>/dev/null
docker start oa-s >/dev/null; sleep 4
docker exec -u 0 oa-s sh -c "mkdir -p /data; cp /tmp/doc.md /data/doc.md" 2>&1 | head -2
docker logs oa-s 2>&1 | tail -3 | cut -c1-200
