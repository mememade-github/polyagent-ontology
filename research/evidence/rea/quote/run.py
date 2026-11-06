import json,subprocess,unicodedata,time,sys
V={"exact":"Jane Doe promised Globex a 10% service credit",
"case":"JANE DOE PROMISED GLOBEX A 10% SERVICE CREDIT",
"space":"Jane  Doe\npromised   Globex a 10% service credit",
"punct_dropped":"Jane Doe promised Globex a 10 service credit",
"midword":"ane Doe promised Globex a 10% service cred",
"ellipsis":"Jane Doe ... service credit",
"paraphrase":"Jane Doe guaranteed Globex a service credit",
"other_section":"Globex may not renew",
"fullwidth":"Jane Doe promised Globex a 10％ service credit",
"ko_nfc":"제인이 글로벡스에 환불을 약속했다",
"ko_nfd":unicodedata.normalize('NFD',"제인이 글로벡스에 환불을 약속했다"),
"ko_space":"제인이글로벡스에환불을약속했다"}
for k,q in V.items():
    p=subprocess.Popen(['python3','stub.py',f'__SCRATCH__/q/l_{k}.jsonl',json.dumps(q)]); time.sleep(0.4)
    subprocess.run('docker rm -f hx-x',shell=True,capture_output=True)
    subprocess.run('docker create --name hx-x --network polyagent-ontology_default --entrypoint extract -e ANTHROPIC_API_KEY=stub -w /tmp ghcr.io/helixdb/ontology-agent:latest --ontology /tmp/o.toml --helix-url http://hx-db:8080 --load L1 --dry-run --verifier-model stub-v --extractor-model stub-e --anthropic-base-url http://__INTERNAL_IP__:18081 --responses /tmp/r.redb /tmp/doc.md',shell=True,capture_output=True)
    subprocess.run('docker cp ontology_nokey.toml hx-x:/tmp/o.toml; docker cp doc.md hx-x:/tmp/doc.md',shell=True,capture_output=True)
    r=subprocess.run('timeout 60 docker start -a hx-x',shell=True,capture_output=True,text=True)
    p.kill(); p.wait()
    open(f'r_{k}.raw','w').write(r.stdout+r.stderr)
    print(k,'rc',r.returncode,len(r.stdout))
