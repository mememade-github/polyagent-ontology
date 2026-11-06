W=__SCRATCH__/d2
docker rm -f hx-x >/dev/null 2>&1
docker create --name hx-x --network polyagent-ontology_default --entrypoint extract -e ANTHROPIC_API_KEY=stub -w /tmp ghcr.io/helixdb/ontology-agent:latest --ontology /tmp/o.toml --helix-url http://hx-db:8080 --load E2E --verifier-model stub-v --extractor-model stub-e --anthropic-base-url http://__INTERNAL_IP__:18081 --responses /tmp/r.redb /tmp/doc.md >/dev/null
docker cp $W/bundle_ontology.toml hx-x:/tmp/o.toml; docker cp $W/doc.md hx-x:/tmp/doc.md
timeout 60 docker start -a hx-x 2>&1
