docker rm -f hx-x >/dev/null 2>&1
docker create --name hx-x --network polyagent-ontology_default --entrypoint extract -e ANTHROPIC_API_KEY=stub -w /tmp ghcr.io/helixdb/ontology-agent:latest --ontology /tmp/ontology.toml --helix-url http://hx-db:8080 --load L1 --verifier-model stub-v --extractor-model stub-e --anthropic-base-url http://__INTERNAL_IP__:18081 --responses /tmp/r.redb "$@" /tmp/doc.md >/dev/null
docker cp __SCRATCH__/hx/ontology_nokey.toml hx-x:/tmp/ontology.toml; docker cp __SCRATCH__/hx/doc.md hx-x:/tmp/doc.md
timeout 90 docker start -a hx-x 2>&1
