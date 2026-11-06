import json,sys
name,prov,model,ctx,mo,doc,table,wall=sys.argv[1:9]
spec=lambda:{"name":model,"price":"free","reasoning":False,"context_tokens":int(ctx),"max_output_tokens":int(mo)}
src=[{"id":"docs1","display_name":"call notes","description":"Notes from customer calls","route":"extraction","access":{"documents":{"files":[{"doc_id":"d1","path":doc,"media_type":"markdown","title":"call notes"}]}},"fingerprint":"fp1"}]
if table=="table": src.append({"id":"accounts","display_name":"accounts","description":"Customer accounts table","route":{"mapping":{"trust":1.0}},"access":{"file":{"path":"accounts.jsonl","format":"jsonl"}},"fingerprint":"fp2"})
p={"ollama":{"ollama":{"base_url":"http://ollama-t:11434"}},"oai":{"openai_compatible":{"base_url":"http://__INTERNAL_IP__:18090/v1","api":"chat_completions"}}}[prov]
t={"session_id":name,"request_id":"r-"+name,"state":None,"sources":src,"input":{"start":{"workflow":"Track promises made to customers","goals":["What was promised to each customer?","When is each promise due?"]}},
"limits":{"max_usd":100.0,"max_steps":30,"max_wall_secs":int(wall)},
"models":{"endpoint":{"provider":p,"call_timeout_secs":3000},"draft":spec(),"extract":spec(),"verify":spec()}}
json.dump(t,open(name+".json","w"))
