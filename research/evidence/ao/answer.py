import logging,sys,json; logging.disable(logging.CRITICAL)
from auto_ontology.connectors.sqlite import SQLiteDatabase
from auto_ontology.connectors import registry
from auto_ontology.utils import get_embed_params
from auto_ontology.utils.retriever import Retriever
from auto_ontology.vdb import get_data_vdb,get_semantic_vdb
from auto_ontology.retrieval.text_to_sql.main import stream_agent_response
c=SQLiteDatabase(f"sqlite:///{sys.argv[1]}/shop.sqlite"); registry.get_connectors=lambda *a,**k:[c]
ep=get_embed_params()
p=dict(question=sys.argv[2],connectors=[c],target_db="shop",
  data_retriever=Retriever(get_data_vdb(database_name="shop",reset=False),ep),
  semantic_retriever=Retriever(get_semantic_vdb(database_name="shop",reset=False),ep))
seen=[]
for e in stream_agent_response(p):
    if e.get('type')=='step' and e.get('phase')=='end': seen.append(e['node'])
    elif e.get('type')=='sql': print('SQL:',e['sql'])
    elif e.get('type')=='result': print('RESULT:',json.dumps(e['answer'],ensure_ascii=False,default=str)[:500])
    elif e.get('type')=='error': print('ERROR:',e.get('message','')[:300])
print('NODES:',seen)
