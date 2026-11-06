"""Runs upstream's real run_ingest + run_semantic_compilation, unmodified."""
import logging,sys
logging.basicConfig(level=logging.WARNING)
from auto_ontology.connectors.sqlite import SQLiteDatabase
from auto_ontology.ingestion_service.ingest import run_ingest
from auto_ontology.semantic.compile import run_semantic_compilation
for p in sys.argv[1:]:
    c=SQLiteDatabase(f"sqlite:///{p}")
    from auto_ontology.connectors import registry
    registry.get_connectors=(lambda c=c: lambda *a,**k:[c])()
    import auto_ontology.semantic.visit_enter as ve
    ve._resolve_connector=(lambda c=c: lambda name: c)()
    run_ingest(c)
    print(c.database_name,"compiled_tables=",run_semantic_compilation(c.database_name),flush=True)
