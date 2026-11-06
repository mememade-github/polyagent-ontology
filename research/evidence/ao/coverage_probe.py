"""Real PostgresVDB + real upstream coverage functions; stub embedding (hash BoW, lexical only)."""
import logging,sys,importlib.util; logging.disable(logging.WARNING)
spec=importlib.util.spec_from_loader("x",None)
import hashlib,math,re
def embed(t):
    v=[0.0]*2048
    for w in re.findall(r"[a-z0-9가-힣]+", t.lower()):
        v[int(hashlib.md5(w.encode()).hexdigest(),16)%2048]+=1.0
    n=math.sqrt(sum(x*x for x in v)) or 1.0
    return [x/n for x in v]
from auto_ontology.retrieval.entity_coverage.agents.coverage import _compute_coverage,_uncovered_entities,_filter_by_distance
from auto_ontology.retrieval.entity_coverage.state import DEFAULT_MAX_DISTANCE as D
from auto_ontology.vdb import get_semantic_vdb
v=get_semantic_vdb(database_name="shop",reset=False)
hits=[]
for e in ["region of customers","ad spend"]:
    h=v.retrieval([embed(e)],top_k=2)[0]
    print(repr(e),[(round(float(x['_distance']),3),x.get('metadata',{}).get('name') if isinstance(x.get('metadata'),dict) else x.get('name')) for x in h])
    hits+= [{**x,"query_entity":e,"score":x['_distance']} for x in h]
ents=["region of customers","ad spend"]
kept=_filter_by_distance(hits,D)
print("max_distance",D,"kept",len(kept),"of",len(hits))
print("coverage",_compute_coverage(ents,kept),"uncovered",_uncovered_entities(ents,kept))
print("hit keys",list(hits[0].keys())[:12])
