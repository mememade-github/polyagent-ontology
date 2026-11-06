import json,sys
t=json.load(open('__RESEARCH__/evidence/helix/turn_b.json'))
ctx=int(sys.argv[1]); t['limits']={"max_usd":1.0,"max_steps":12,"max_wall_secs":60}
for k in('draft','extract','verify'):
    if ctx: t['models'][k]['context_tokens']=ctx
    else: t['models'][k].pop('context_tokens',None)
json.dump(t,open(sys.argv[2],'w'))
