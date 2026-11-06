#!/usr/bin/env python3
"""Convert the sample SQL/docs into mixed sources, without replacing any output.
Usage: build_acme.py HELIX_CLONE NEW_OUT_UNDER_TMP
This fixture adapter's table choices are not ontology inference rules.
"""
import argparse
import json
from pathlib import Path
import re
import shutil
import sqlite3


def quote(name):
    return '"' + name.replace('"', '""') + '"'


def statements(sql, skipped_admin=None):
    # sqlite's parser recognizes semicolons inside quoted strings.
    buf = ""
    for ch in sql:
        buf += ch
        if ch == ";" and sqlite3.complete_statement(buf):
            clean = re.sub(r"--[^\n]*", "", buf).strip()
            if clean:
                # Administrative fixture statements are counted, never executed.
                if re.match(r"\A(?:CREATE\s+ROLE\s|GRANT\s)", clean, re.I):
                    if skipped_admin is not None:
                        skipped_admin.append(clean)
                    buf = ""
                    continue
                if not re.match(r"\A(?:CREATE\s+TABLE\s|INSERT\s+INTO\s)", clean, re.I):
                    raise ValueError("SQL statement outside CREATE TABLE / INSERT allowlist")
                yield buf
            buf = ""
    if re.sub(r"--[^\n]*", "", buf).strip():
        raise ValueError("incomplete SQL statement")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("out")
    args = ap.parse_args()
    source, out = Path(args.source).resolve(), Path(args.out).resolve()
    if out.exists() or out.is_symlink():
        raise ValueError("existing output refused")
    if Path('/tmp') not in out.parents or Path.cwd().resolve() in out.parents:
        raise ValueError("fixture output must be outside repository under /tmp")
    if shutil.disk_usage('/workspaces').free < 2_000_000_000:
        raise RuntimeError("disk below 2GB")
    sql_path = source / 'local/acme/acme.sql'
    docs = source / 'public/samples/acme'
    sql = sql_path.read_text(encoding='utf8')
    files = sorted(docs.glob('*.md'))
    if not files:
        raise ValueError("missing source documents")
    # Validate the full script before creating output. No DROP, PRAGMA, ATTACH,
    # extension functions or external-file access are permitted in conversion.
    skipped_admin = []
    script = list(statements(sql, skipped_admin))
    c = sqlite3.connect(':memory:')
    c.enable_load_extension(False)
    allowed = {sqlite3.SQLITE_CREATE_TABLE, sqlite3.SQLITE_INSERT,
               sqlite3.SQLITE_READ, sqlite3.SQLITE_SELECT, sqlite3.SQLITE_UPDATE, sqlite3.SQLITE_TRANSACTION}
    def authorize(action, arg1, arg2, db, trigger):
        # SQLite creates these indexes for PRIMARY KEY / UNIQUE constraints.
        if action == sqlite3.SQLITE_CREATE_INDEX and arg1.startswith('sqlite_autoindex_'):
            return sqlite3.SQLITE_OK
        if action not in allowed or (action == sqlite3.SQLITE_UPDATE and arg1 != 'sqlite_master'):
            return sqlite3.SQLITE_DENY
        return sqlite3.SQLITE_OK
    c.set_authorizer(authorize)
    for statement in script:
        c.execute(statement)
    c.row_factory = sqlite3.Row
    tables = c.execute("select name, sql from sqlite_master where type='table'").fetchall()
    names = {r['name'] for r in tables}
    if not {'product_usage', 'support_tickets'} <= names:
        raise ValueError("fixture conversion tables missing")
    out.mkdir(parents=True, exist_ok=False, mode=0o700)
    for directory in ('db', 'nosql', 'logs', 'docs'):
        (out / directory).mkdir()
    for directory in ('calls', 'reference'):
        (out / 'docs' / directory).mkdir()
    with sqlite3.connect(out / 'db/acme.sqlite') as target:
        for table in tables:
            name = table['name']
            if name in {'product_usage', 'support_tickets'}:
                continue
            target.execute(table['sql'])
            rows = c.execute('select * from ' + quote(name)).fetchall()
            if rows:
                target.executemany('insert into ' + quote(name) + ' values (' + ','.join('?' for _ in rows[0]) + ')', [tuple(r) for r in rows])
    with (out / 'nosql/product_usage.jsonl').open('x') as f:
        for row in c.execute('select * from product_usage'):
            f.write(json.dumps(dict(row), ensure_ascii=False) + '\n')
    # JSON-encoded key/value values preserve quotes, newlines, nulls and numbers.
    with (out / 'logs/support.log').open('x') as f:
        for row in c.execute('select * from support_tickets'):
            f.write('ticket opened ' + ' '.join(k + '=' + json.dumps(v, ensure_ascii=False) for k, v in dict(row).items()) + '\n')
    for path in files:
        # Filename routing belongs only to this fixture adapter.
        folder = 'reference' if 'pricing' in path.name.lower() else 'calls'
        with (out / 'docs' / folder / path.name).open('xb') as f:
            f.write(path.read_bytes())
    print(json.dumps({'status': 'built', 'tables': len(tables), 'documents': len(files),
                      'skipped_administrative_statements': len(skipped_admin)}))


if __name__ == '__main__':
    main()
