docker rm -f hx-i >/dev/null 2>&1
docker create --name hx-i --network polyagent-ontology_default --entrypoint ingest-mapped -w /tmp ghcr.io/helixdb/ontology-agent:latest --ontology /tmp/o.toml --mappings /tmp/m.toml --sources /tmp/src.json --helix-url http://hx-db:8080 --load ADJ >/dev/null
docker cp ../hx/ontology.toml hx-i:/tmp/o.toml; docker cp ../hx/mappings.toml hx-i:/tmp/m.toml; docker cp $1 hx-i:/tmp/src.json; docker cp rows.jsonl hx-i:/tmp/rows.jsonl
timeout 40 docker start -a hx-i 2>&1 | cut -c1-500 | tail -4
