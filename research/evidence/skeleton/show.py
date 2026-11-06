import json,sys
for f in sys.argv[1:]:
    print("=====",f)
    for i,l in enumerate(open(f)):
        r=json.loads(l); txt="";tc={}
        for ln in r["resp"].splitlines():
            if not ln.startswith("data: ") or ln=="data: [DONE]": continue
            try: d=json.loads(ln[6:])
            except: continue
            for c in d.get("choices",[]):
                de=c.get("delta",{}); txt+=de.get("content") or ""
                for t in de.get("tool_calls") or []:
                    k=t.get("index",0); e=tc.setdefault(k,{"n":"","a":""}); fn=t.get("function",{}); e["n"]+=fn.get("name") or ""; e["a"]+=fn.get("arguments") or ""
        print(f"--call {i} sec={r['sec']} text={txt[:600]!r}")
        for e in tc.values(): print("  TOOL",e["n"],e["a"][:1500])
