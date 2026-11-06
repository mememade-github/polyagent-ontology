"""Compile under a knockout, then run the real answer graph; report compile counts, nodes, SQL, result."""
import sys,json,hashlib
exec(open('knockout.py').read().split('run("baseline")')[0])
from auto_ontology.utils import get_embed_params
from auto_ontology.utils.retriever import Retriever
from auto_ontology.vdb import get_data_vdb,get_semantic_vdb
from auto_ontology.retrieval.text_to_sql.main import stream_agent_response
import auto_ontology.retrieval.text_to_sql.agents.sql_parse_validation as spv
SRC=sys.argv[1]
def answer(q):
    c=SQLiteDatabase(f"sqlite:///{SRC}/shop.sqlite"); registry.get_connectors=lambda *a,**k:[c]
    ep=get_embed_params()
    p=dict(question=q,connectors=[c],target_db="shop",data_retriever=Retriever(get_data_vdb(database_name="shop",reset=False),ep),semantic_retriever=Retriever(get_semantic_vdb(database_name="shop",reset=False),ep))
    nodes=[];sql=[];res=None
    for e in stream_agent_response(p):
        t=e.get('type')
        if t=='step' and e.get('phase')=='end': nodes.append(e['node'])
        elif t=='sql': sql.append(e['sql'])
        elif t=='result': res=e['answer']
        elif t=='error': res={'error':e.get('message','')[:120]}
    return nodes,sql,res
def case(label,patch=None,q="How many customers per region",answer_patch=None):
    run(label,patch)
    open('llm2.jsonl','w').close()
    r=answer_patch() if answer_patch else None
    n,s,a=answer(q)
    if r: r()
    gen=[json.loads(l) for l in open('llm2.jsonl') if '"schema": "SQLGenerationModel"' in l]
    pr=gen[0]['messages'][-1]['content'] if gen else ''
    print(json.dumps(dict(label=label,nodes=n,sql=s,db=(a or {}).get('sql_response_from_db'),err=(a or {}).get('error'),gen_prompt_chars=len(pr),prompt_md5=hashlib.md5(pr.encode()).hexdigest()[:8],semantic_match_lines=pr.count('Semantic match'),fk_col_refs=pr.count('main.customers.customer_id')),ensure_ascii=False),flush=True)
def k_validator():
    o=spv.parse_query_single
    class Fake:
        def get_tables_ids(self): return []
        def get_column_ids(self): return []
    spv.parse_query_single=lambda **k:Fake()
    def r(): spv.parse_query_single=o
    return r
case("A_baseline")
case("K3_no_semantic_fk",k_fk)
case("K4_no_semantic_embedding",k_embed)
case("K5_term_llm_none",k_llm_down)
case("A3_ghost_sql_with_validator",None,"Total ad spend per region")
case("K6_ghost_sql_no_catalog_parse_check",None,"Total ad spend per region",k_validator)
