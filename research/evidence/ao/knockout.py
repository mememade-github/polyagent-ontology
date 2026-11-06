"""Knockouts on real upstream compile: each run fresh DB rows; compares ontology output to baseline."""
import logging,sys,json,subprocess
logging.disable(logging.CRITICAL)
from auto_ontology.connectors.sqlite import SQLiteDatabase
from auto_ontology.connectors import registry
import auto_ontology.semantic.visit_enter as ve, auto_ontology.semantic.term_extractor as te, auto_ontology.semantic.compile as cp
from auto_ontology.ingestion_service.ingest import run_ingest
from auto_ontology.semantic.compile import run_semantic_compilation
from auto_ontology.dal.session import store
from sqlalchemy import text
def q(s):
    return store().query_read(text(s)) if False else None
import psycopg,os
conn=psycopg.connect(host=os.environ['POSTGRES_HOST'],user='postgres',password='<redacted>',dbname='auto_ontology',autocommit=True)
def scal(s): return conn.execute(s).fetchall()
def vc(t):
    try: return scal(f"select count(*) from {t}")[0][0]
    except Exception: return 0
def reset():
    conn.execute("truncate term, column_attribute, catalog_database, sql_attribute cascade"); 
    for t in ('vdb.semantic_layer','vdb.data_objects_layer'):
        conn.execute(f"create table if not exists {t}_probe_guard (x int); drop table {t}_probe_guard") if False else None
        try: conn.execute(f"delete from {t}")
        except Exception: pass
def run(name,patch=None,db='shop'):
    reset(); restore=patch() if patch else None
    c=SQLiteDatabase(f"sqlite:///{sys.argv[1]}/{db}.sqlite")
    registry.get_connectors=lambda *a,**k:[c]; ve._resolve_connector=lambda n:c
    err=None
    try: run_ingest(c); n=run_semantic_compilation(c.database_name)
    except Exception as e: n=None; err=f"{type(e).__name__}: {str(e)[:90]}"
    r=dict(name=name,tables=n,err=err,
      terms=scal("select count(*) from term")[0][0],
      attrs=scal("select count(*) from column_attribute")[0][0],
      ghost=scal("select count(*) from column_attribute where source_column='ghost_column'")[0][0],
      sem_fk=scal("select count(*) from column__semantic_fk")[0][0],
      vec_sem=vc('vdb.semantic_layer'),
      vec_cat=vc('vdb.data_objects_layer'))
    print(json.dumps(r,ensure_ascii=False),flush=True)
    if restore: restore()
def k_sanitize():
    o=te._sanitize_result
    from auto_ontology.semantic.models import TableTermsResult,TermProposal,TermAttributeAssignment
    def raw(result,*,table,specs):
        return TableTermsResult(terms=[TermProposal(name=t.name,description=t.description,attributes=[TermAttributeAssignment(source_column=a.source_column,display_name=a.display_name) for a in t.attributes]) for t in result.terms])
    te._sanitize_result=raw
    def r(): te._sanitize_result=o
    return r
def k_catalog():
    import auto_ontology.catalog.ingest as ci, auto_ontology.ingestion_service.ingest as ii
    o=ii.ingest_catalog; import pandas as pd
    ii.ingest_catalog=lambda c:(pd.DataFrame(),pd.DataFrame())
    def r(): ii.ingest_catalog=o
    return r
def k_fk():
    o=cp.resolve_semantic_fks; cp.resolve_semantic_fks=lambda d:0
    def r(): cp.resolve_semantic_fks=o
    return r
def k_embed():
    o=cp.build_semantic_embedder
    cp.build_semantic_embedder=lambda *a,**k:None
    def r(): cp.build_semantic_embedder=o
    return r
def k_llm_down():
    import auto_ontology.semantic.term_extractor as t
    o=t.invoke_with_structured_output
    t.invoke_with_structured_output=lambda *a,**k:None
    def r(): t.invoke_with_structured_output=o
    return r
run("baseline")
sys.exit()
run("K2_no_catalog",k_catalog)
run("K3_no_semantic_fk",k_fk)
run("K4_no_semantic_embedding",k_embed)
run("K5_term_llm_returns_none",k_llm_down)
