#!/usr/bin/env python3
"""Build an ontology from mixed sources with a small local LLM.

Structure comes from code wherever the input states or implies it. The LLM gets
one small, memoryless, schema-constrained question at a time. Every call must
fit the context limit; anything that does not fit fails instead of truncating.
Usage: onto.py CORPUS_DIR OUT_DIR [--goal TEXT]
"""
import itertools
import argparse, collections, hashlib, json, os, re, sqlite3, sys, time, urllib.request, shutil
from pathlib import Path

OLLAMA = os.environ.get("OLLAMA", "http://ollama-t:11434")
MODEL = os.environ.get("MODEL", "qwen2.5:3b")
NUM_CTX = 8192
# Ollama silently keeps only about half of num_ctx (observed: limit=4098 at 8192).
MAX_PROMPT_TOKENS = 3800
OVERLAP_MIN = 0.95
GENRE_SAMPLE_BYTES = 768
GENRES = ["meeting_or_call", "contract", "pricing", "incident", "email", "report", "other"]
STOP_CONCEPTS = {"thing", "item", "other", "information", "detail", "statement", "fact", "entity", "person", "company", "organization", "date", "amount", "number"}


def validate(value, schema):
    """Validate the deliberately small JSON Schema subset used here; fail closed."""
    allowed = {"type", "properties", "required", "additionalProperties", "items", "maxItems", "enum"}
    if set(schema) - allowed:
        raise ValueError("unsupported schema keyword")
    kind = schema.get("type")
    types = {"object": dict, "array": list, "string": str, "boolean": bool}
    if kind not in types or type(value) is not types[kind]:
        raise ValueError("schema type mismatch")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError("schema enum mismatch")
    if kind == "object":
        if not set(schema.get("required", [])) <= value.keys():
            raise ValueError("missing required property")
        props = schema.get("properties", {})
        if set(value) - props.keys():
            raise ValueError("unexpected property")
        for key, item in value.items():
            validate(item, props[key])
    if kind == "array":
        if len(value) > schema.get("maxItems", float("inf")):
            raise ValueError("too many items")
        for item in value:
            validate(item, schema["items"])


def prompt_bound(system, user, schema):
    # One token per UTF-8 byte is a conservative byte-level tokenizer bound.
    # Include serialized schema/messages plus 512 tokens for chat/template framing.
    return len(json.dumps({"messages": [{"role": "system", "content": system},
        {"role": "user", "content": user}], "format": schema}, ensure_ascii=False).encode("utf8")) + 512


SAFE_ERRORS = frozenset(('declared FK target missing', 'disk below 2GB', 'documents yielded no grounded facts', 'duplicate source', 'empty ontology run', 'existing cache refused', 'existing measurements refused', 'incomplete generation', 'invalid corpus/output relationship', 'missing output token accounting', 'missing prompt token accounting', 'missing required property', 'model digest unavailable', 'private output must be outside repository under /tmp', 'prompt accounting violates bound', 'prompt byte bound exceeds limit', 'schema enum mismatch', 'schema type mismatch', 'too many items', 'unexpected property', 'unsupported declared foreign key', 'unsupported schema keyword'))

def safe_error(exc):
    message = str(exc)
    return message if type(exc) in (ValueError, RuntimeError) and message in SAFE_ERRORS else "operation failed; inspect private diagnostics"


class Llm:
    def __init__(self, cache):
        self.path, self.calls, self.seconds, self.maxp = cache, 0, 0.0, 0
        if os.path.exists(cache):
            raise ValueError("existing cache refused")
        self.records = []
        self.digest = None
        self.config = {"num_ctx": NUM_CTX, "temperature": 0, "seed": 7, "num_thread": 8}

    def ask(self, system, user, schema, predict=400):
        if shutil.disk_usage("/workspaces").free < 2_000_000_000:
            raise RuntimeError("disk below 2GB")
        size = prompt_bound(system, user, schema)
        if size >= MAX_PROMPT_TOKENS:
            raise ValueError("prompt byte bound exceeds limit")
        if self.digest is None:
            with urllib.request.urlopen(OLLAMA + "/api/tags", timeout=30) as response:
                tags = json.load(response)["models"]
            matches = [x for x in tags if x.get("name") == MODEL or x.get("model") == MODEL]
            if len(matches) != 1 or not matches[0].get("digest"):
                raise ValueError("model digest unavailable")
            self.digest = matches[0]["digest"]
        body = {"model": MODEL, "stream": False, "format": schema,
            "options": dict(self.config, num_predict=predict),
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}
        self.calls += 1
        meta = {"call": self.calls, "model": MODEL, "digest": self.digest,
            "prompt_byte_bound": size,
            "prompt_chars": sum(len(m["content"]) for m in body["messages"]),
            "prompt_utf8_bytes": sum(len(m["content"].encode("utf8")) for m in body["messages"]),
            "serialized_prompt_chars": len(json.dumps({"messages": body["messages"], "format": schema}, ensure_ascii=False)),
            "serialized_prompt_utf8_bytes": size - 512, "options": body["options"], "status": "started"}
        print(json.dumps(meta), flush=True)
        start = time.monotonic()
        cpu_start = time.process_time()
        try:
            req = urllib.request.Request(OLLAMA + "/api/chat", json.dumps(body).encode(), {"content-type": "application/json"})
            with urllib.request.urlopen(req, timeout=1800) as response:
                raw_response = response.read()
            with open(self.path, "a", encoding="utf8") as f:
                f.write(json.dumps({"call": self.calls, "request": body,
                    "raw_response": raw_response.decode("utf8", errors="backslashreplace")}, ensure_ascii=False) + "\n")
            r = json.loads(raw_response)
            for key in ("prompt_eval_count", "eval_count", "total_duration", "load_duration", "prompt_eval_duration", "eval_duration", "done_reason"):
                meta[key] = r.get(key)
            if r.get("done") is not True or r.get("done_reason") != "stop":
                raise ValueError("incomplete generation")
            if not isinstance(r.get("prompt_eval_count"), int) or r["prompt_eval_count"] <= 0:
                raise ValueError("missing prompt token accounting")
            if r["prompt_eval_count"] >= MAX_PROMPT_TOKENS or r["prompt_eval_count"] > size:
                raise ValueError("prompt accounting violates bound")
            if type(r.get("eval_count")) is not int or r["eval_count"] <= 0:
                raise ValueError("missing output token accounting")
            # Server counts cannot prove absence of truncation. The bound is below
            # the observed half-context threshold; record this residual limitation.
            result = json.loads(r["message"]["content"])
            validate(result, schema)
            meta["status"] = "ok"
            self.maxp = max(self.maxp, r["prompt_eval_count"])
            return result
        except Exception as exc:
            meta["status"] = "failed"
            meta["error_type"] = type(exc).__name__
            meta["error_message"] = safe_error(exc)
            raise
        finally:
            meta["seconds"] = round(time.monotonic() - start, 6)
            meta["cpu_seconds"] = round(time.process_time() - cpu_start, 6)
            self.seconds += meta["seconds"]
            self.records.append(meta)
            print(json.dumps(meta), flush=True)
            with open(os.path.join(os.path.dirname(self.path), "calls.json"), "w") as f:
                json.dump(self.records, f, indent=1)


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[*_`#|]", "", str(s))).strip().lower()


def type_name(s):
    w = [x for x in re.split(r"[^A-Za-z0-9가-힣]+", s) if x]
    w = [x[:-3] + "y" if x.endswith("ies") else x[:-1] if x.endswith("s") and not x.endswith("ss") else x for x in w]
    return "".join(x[:1].upper() + x[1:] for x in w)


# ---------- structured sources: code only ----------
def ident(value):
    return '"' + value.replace('"', '""') + '"'


def load_sqlite(path, tables):
    with sqlite3.connect(Path(path).resolve().as_uri() + "?mode=ro", uri=True) as c:
        c.row_factory = sqlite3.Row
        for (t,) in c.execute("select name from sqlite_master where type='table' and name not like 'sqlite_%'").fetchall():
            info = c.execute(f'pragma table_info({ident(t)})').fetchall()
            pk = [r["name"] for r in sorted(info, key=lambda r: r["pk"]) if r["pk"]]
            groups = collections.defaultdict(list)
            for r in c.execute(f'pragma foreign_key_list({ident(t)})'):
                groups[r["id"]].append(dict(r))
            fks = []
            for group in groups.values():
                group.sort(key=lambda r: r["seq"])
                fks.append({"columns": [r["from"] for r in group], "target": str(Path(path).resolve()) + "::" + group[0]["table"], "keys": [r["to"] for r in group]})
            key = str(Path(path).resolve()) + "::" + t
            if key in tables:
                raise ValueError("duplicate source")
            rows = [dict(r) for r in c.execute(f'select * from {ident(t)}')]
            tables[key] = {"rows": rows, "pk": pk, "fks": fks, "origin": "db", "label": t,
                "row_ids": [key + "::row:" + str(i) for i in range(len(rows))]}


def flatten(d, pre=""):
    # Preserve nested arrays/objects; dotted flattening can collide with literal keys.
    return dict(d)


def load_jsonl(path, tables):
    rows = []
    for line in open(path, encoding="utf8"):
        if line.strip():
            value = json.loads(line)
            rows.append(value if isinstance(value, dict) else {"value": value})
    key = str(Path(path).resolve())
    tables[key] = {"rows": rows, "pk": [], "fks": [], "origin": "jsonl", "label": Path(path).stem,
        "row_ids": [key + "::row:" + str(i) for i in range(len(rows))]}


def load_log(path, tables):
    """Keep every line, with parsed fields when available; retain original evidence."""
    groups = collections.defaultdict(list)
    decoder = json.JSONDecoder()
    for index, line in enumerate(open(path, encoding="utf8")):
        if not line.strip():
            continue
        kv, end = {}, 0
        for match in re.finditer(r"(\w+)=", line):
            if match.start() < end:
                continue
            try:
                value, consumed = decoder.raw_decode(line[match.end():])
                end = match.end() + consumed
            except json.JSONDecodeError:
                value = line[match.end():].split()[0]
                end = match.end() + len(value)
            kv[match.group(1)] = value
        prefix = line.split("=", 1)[0].rsplit(" ", 1)[0] if kv else "unparsed"
        tmpl = " ".join(re.findall(r"[A-Za-z_]+", prefix)[:3]).lower() or "unparsed"
        groups[tmpl].append({"fields": kv, "raw": line.rstrip("\n"), "line": index + 1})
    for tmpl, entries in groups.items():
        key = str(Path(path).resolve()) + "::" + tmpl
        tables[key] = {"rows": [dict(e["fields"]) for e in entries], "pk": [], "fks": [],
            "origin": "log", "template": tmpl, "label": tmpl, "evidence": entries,
            "row_ids": [str(Path(path).resolve()) + "::line:" + str(e["line"]) for e in entries]}


def values(t, col):
    return [r.get(col) for r in t["rows"] if r.get(col) not in (None, "")]


def key_candidates(t):
    """Declared primary key or minimal observed non-DB keys; never a guarantee."""
    if t["pk"]:
        return [{"columns": t["pk"], "declared": True, "inferred": False,
                 "basis": "declared_primary_key"}]
    if t["origin"] == "db" or len(t["rows"]) < 2:
        return []
    columns = sorted({c for r in t["rows"] for c in r})
    def identifier(c):
        parts = re.sub(r"([a-z])([A-Z])", r"\1_\2", c).lower()
        return bool(re.search(r"(?:^|[^a-z0-9])(id|key|code)(?:$|[^a-z0-9])", parts))
    eligible = [c for c in columns if identifier(c)]
    found = []
    # Minimal composites include at least one identifier-like column. All cells
    # must be present scalars; physical row identities are never replaced.
    for width in range(1, len(columns) + 1):
        for cols in itertools.combinations(columns, width):
            if not set(cols) & set(eligible) or any(set(k["columns"]) <= set(cols) for k in found):
                continue
            if len(tuple_values(t["rows"], cols)) == len(t["rows"]):
                found.append({"columns": list(cols), "declared": False, "inferred": True,
                    "basis": "observed_non_null_uniqueness_not_guaranteed", "rows": len(t["rows"])})
    return found


def find_key(t):
    candidates = key_candidates(t)
    return candidates[0]["columns"] if candidates else []


def tuple_values(rows, columns):
    return {tuple(r.get(c) for c in columns) for r in rows
            if all(isinstance(r.get(c), (str, int, float)) and not isinstance(r.get(c), bool)
                   and r.get(c) != "" for c in columns)}


def find_links(tables):
    links = []
    candidates = {n: key_candidates(t) for n, t in tables.items()}
    def evidence(a, columns, b, keys):
        vals, target = tuple_values(a["rows"], columns), tuple_values(b["rows"], keys)
        shared = vals & target
        return {"overlap": len(shared) / len(vals) if vals else None,
            "support_distinct": len(shared), "source_distinct": len(vals),
            "target_distinct": len(target), "source_rows": len(a["rows"]),
            "source_non_null_rows": sum(all(r.get(c) not in (None, "") for c in columns) for r in a["rows"])}
    def kinds(rows, cols):
        return {tuple("number" if isinstance(r.get(c), (int, float)) and not isinstance(r.get(c), bool)
                      else type(r.get(c)).__name__ for c in cols)
                for r in rows if all(r.get(c) not in (None, "") for c in cols)}
    for an, a in tables.items():
        for fk in a["fks"]:
            bn = fk["target"]
            if bn not in tables:
                raise ValueError("declared FK target missing")
            keys = fk["keys"]
            if all(k is None for k in keys):
                keys = tables[bn]["pk"]
            if not keys or any(k is None for k in keys) or len(keys) != len(fk["columns"]):
                raise ValueError("unsupported declared foreign key")
            links.append({"from": an, "to": bn, "column": fk["columns"], "key": keys,
                "declared": True, "inferred": False, "basis": "declared_foreign_key",
                **evidence(a, fk["columns"], tables[bn], keys)})
        columns = sorted({c for r in a["rows"] for c in r})
        for bn, b in tables.items():
            if an == bn:
                continue
            for candidate in candidates[bn]:
                keys = candidate["columns"]
                for cols in itertools.permutations(columns, len(keys)):
                    # Do not infer key-to-key identity from coincidental values.
                    if any(set(k["columns"]) <= set(cols) for k in candidates[an]):
                        continue
                    if any(l["from"] == an and l["to"] == bn and l["column"] == list(cols) for l in links):
                        continue
                    if kinds(a["rows"], cols) != kinds(b["rows"], keys):
                        continue
                    ev = evidence(a, cols, b, keys)
                    if ev["source_distinct"] >= 2 and ev["overlap"] >= OVERLAP_MIN:
                        links.append({"from": an, "to": bn, "column": list(cols), "key": keys,
                            "declared": False, "inferred": True,
                            "basis": "type_compatible_observed_overlap_not_semantic_guarantee",
                            "target_key_basis": candidate["basis"], **ev})
    return links


def categorical_entities(tables, doc_text, llm):
    """A low-cardinality text column may name a thing of its own. Ask one question per column."""
    found = []
    for tn, t in tables.items():
        n = len(t["rows"])
        for col in (t["rows"][0] if n else {}):
            vals = [v for v in values(t, col) if isinstance(v, str)]
            d = sorted(set(vals))
            if n < 5 or not 2 <= len(d) <= 12 or len(vals) < n * 0.5 or re.search(r"(^|_)(id|ts|date|on|at)$", col):
                continue
            if any(re.fullmatch(r"\d{4}-\d\d.*", v) for v in d):
                continue
            in_docs = sum(1 for v in d if re.search(r"\b" + re.escape(v.lower()) + r"\b", doc_text))
            if in_docs < 2:
                continue
            system = "Decide whether a column names a separate thing with its own details, rather than a status, category, frequency or level."
            user = f"Table: {t.get('label', tn)}\nColumn: {col}\nValues: {json.dumps(d, ensure_ascii=False)}"
            schema = {"type": "object", "properties": {"separate_thing": {"type": "boolean"}, "reason": {"type": "string"}}, "required": ["separate_thing", "reason"]}
            if prompt_bound(system, user, schema) >= MAX_PROMPT_TOKENS:
                llm.exclusions.append({"kind": "column", "table": tn, "column": col, "reason": "prompt_budget"})
                continue
            r = llm.ask(system, user, schema, 180)
            if r.get("separate_thing") and in_docs >= 2:
                found.append({"table": tn, "column": col, "values": d, "in_docs": in_docs, "reason": r.get("reason")})
    return found


# ---------- documents ----------
def sections(text):
    out, head, buf = [], "", []
    for line in text.splitlines():
        m = re.match(r"#{1,6}\s+(.*)", line)
        if m:
            if buf:
                out.append((head, "\n".join(buf)))
            head, buf = m.group(1), []
        elif line.strip():
            buf.append(line)
    if buf:
        out.append((head, "\n".join(buf)))
    return out


def units(body):
    """Bullets and sentences: the smallest piece one question can cover."""
    us = []
    for line in body.splitlines():
        line = re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", line).strip()
        for s in re.split(r"(?<=[.!?。])\s+(?=[A-Z가-힣])", line):
            if s:
                us.append(s)
    return us


def gazetteer(tables):
    """Row names and ids become anchors, so a mention gets its type without the LLM."""
    gaz = {}
    for tn, t in tables.items():
        key = find_key(t)
        if not key or len(key) != 1:
            continue
        cols = [c for c in (t["rows"][0] if t["rows"] else {}) if re.search(r"name|title$", c) or c == key[0]]
        for r in t["rows"]:
            for c in cols:
                v = r.get(c)
                if isinstance(v, str) and len(v) >= 3 and len({json.dumps(x.get(c), sort_keys=True) for x in t["rows"]}) > len(t["rows"]) * 0.8:
                    gaz.setdefault(norm(v), []).append((tn, r.get(key[0])))
    return gaz


def anchors_in(text, gaz, rx):
    t = norm(text)
    return {m.group(0): gaz[m.group(0)] for m in rx.finditer(t) if m.group(0) in gaz}


ITEM = {'type': 'object', 'properties': {'items': {'type': 'array', 'maxItems': 1, 'items': {'type': 'object', 'properties': {'subject': {'type': 'string'}, 'relation': {'type': 'string'}, 'object': {'type': 'string'}, 'concept': {'type': 'string'}}, 'required': ['subject', 'relation', 'object', 'concept']}}}, 'required': ['items']}
EXTRACT = 'Return JSON only. Extract at most one explicit proposition. Copy subject, relation, and object as exact spans of the sentence. Preserve negation and uncertainty. concept is one short general noun. If none, return {"items":[]}. Example sentence: A storm damaged the bridge. Output: {"items":[{"subject":"A storm","relation":"damaged","object":"the bridge","concept":"Damage"}]}.'
VERIFY = """Check whether all claim fields are supported by the sentence. Check subject and object roles,
negation, uncertainty, conditionality, speaker attribution and modality. A denied event must stay denied,
a request must stay a request. Return false for any altered meaning or omitted qualifier."""
BOOL = {"type": "object", "properties": {"stated": {"type": "boolean"}}, "required": ["stated"]}


def document_paths(root):
    return sorted(p for p in Path(root).rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".txt", ".rst"})


def read_docs(root, tables, llm, log):
    gaz = gazetteer(tables)
    rx = re.compile(r"(?<![\w-])(" + "|".join(sorted(map(re.escape, gaz), key=len, reverse=True)) + r")(?![\w-])") if gaz else None
    docs, facts, uncovered, total_units = [], [], [], 0
    for p in document_paths(root):
        text = p.read_text(encoding="utf8")
        rel = str(p.relative_to(root))
        encoded = text.encode("utf8")
        opening = encoded[:GENRE_SAMPLE_BYTES].decode("utf8", errors="ignore")
        sampled = len(opening.encode("utf8"))
        heading = next((h for h, _ in sections(text) if h), "")
        schema = {"type": "object", "properties": {"genre": {"type": "string", "enum": GENRES}}, "required": ["genre"]}
        genre = llm.ask("Classify the document genre using only the supplied path, first heading and bounded opening sample. Use other if unclear.",
            json.dumps({"path": rel, "first_heading": heading, "opening_sample": opening}, ensure_ascii=False), schema, 60)["genre"]
        docs.append({"path": rel, "genre": genre, "provenance": "hybrid", "inferred": True,
            "sampled_bytes": sampled, "omitted_bytes": len(encoded) - sampled,
            "anchors": anchors_in(text, gaz, rx) if rx else {}})
        for head, body in sections(text):
            for u in units(body):
                total_units += 1
                uid = f"{rel}::{total_units}"
                user = u
                if prompt_bound(EXTRACT, user, ITEM) >= MAX_PROMPT_TOKENS:
                    uncovered.append({"unit": uid, "sentence": u, "reason": "prompt_budget"})
                    continue
                r = llm.ask(EXTRACT, user, ITEM, 600)
                kept, rejected = 0, []
                for it in r["items"]:
                    it = {**it, "quote": u}
                    if any(not it[k].strip() or it[k] not in u for k in ("subject", "relation", "object")):
                        rejected.append({"claim": it, "reason": "span_grounding"})
                        continue
                    user_verify = json.dumps({"sentence": u, "claim": it}, ensure_ascii=False)
                    if prompt_bound(VERIFY, user_verify, BOOL) >= MAX_PROMPT_TOKENS:
                        rejected.append({"claim": it, "reason": "verification_budget"})
                        continue
                    if not llm.ask(VERIFY, user_verify, BOOL, 30)["stated"]:
                        rejected.append({"claim": it, "reason": "semantic_grounding"})
                        continue
                    kept += 1
                    facts.append({"unit": uid, "doc": rel, "section": head, "sentence": u, **it,
                        "provenance": "hybrid", "anchors": anchors_in(u, gaz, rx) if rx else {},
                        "dates": re.findall(r"\d{4}-\d\d-\d\d", u), "amounts": re.findall(r"\$[\d,.]+|\d+%", u)})
                if not kept or rejected or len(r["items"]) == 1:
                    uncovered.append({"unit": uid, "sentence": u, "reason": "rejected_or_partial" if kept else "no_grounded_fact", "rejected": rejected,
                        "capacity_reached": len(r["items"]) == 1})
    return docs, facts, uncovered, total_units


def concept_key(c):
    w = re.findall(r"[A-Za-z가-힣]+", str(c))
    return type_name(w[-1]) if w else ""


def type_id(kind, source, label):
    return kind + ":" + (type_name(label) or "Unnamed") + ":" + hashlib.sha256(source.encode()).hexdigest()[:16]


def induce(tables, links, cats, docs, facts):
    types, out_links = {}, []
    for n, t in tables.items():
        types[type_id("table", n, t.get("label", n))] = {"from": n, "origin": t["origin"], "provenance": "code", "key": find_key(t), "key_candidates": key_candidates(t), "props": sorted({c for r in t["rows"] for c in r})}
    name = {n: type_id("table", n, t.get("label", n)) for n, t in tables.items()}
    for l in links:
        out_links.append({**l, "from": name[l["from"]], "to": name[l["to"]],
            "via": f'{l["from"]}.{l["column"]}', "columns": l["column"], "keys": l["key"],
            "origin": "code", "provenance": "code"})
    for c in cats:
        tn = type_id("category", c["table"] + "::" + c["column"], c["column"])
        types[tn] = {"from": f'{c["table"]}.{c["column"]}', "origin": "column values", "provenance": "hybrid", "key": [c["column"]], "props": []}
        out_links.append({"from": name[c["table"]], "to": tn, "via": f'{c["table"]}.{c["column"]}', "origin": "hybrid", "provenance": "hybrid"})
    # A document genre seen more than once, with anchored mentions, becomes a type.
    genres = collections.Counter(d["genre"] for d in docs if d["genre"] != "other")
    for g, cnt in genres.items():
        members = [d for d in docs if d["genre"] == g]
        anchored = collections.Counter(a[0] for d in members for v in d["anchors"].values() for a in v)
        if cnt >= 2 and anchored:
            tn = type_id("genre", g, g)
            types[tn] = {"from": "documents", "provenance": "hybrid", "origin": f"{cnt} documents", "key": [], "props": []}
            for tb, k in anchored.items():
                in_docs = sum(1 for d in members if any(a[0] == tb for v in d["anchors"].values() for a in v))
                if in_docs >= 2:
                    out_links.append({"from": tn, "to": name[tb], "via": "mentions", "docs": in_docs, "origin": "hybrid", "provenance": "hybrid"})
    # A concept used across documents becomes a type; its anchored rows give its links.
    per = collections.defaultdict(list)
    for x in facts:
        k = concept_key(x.get("concept"))
        if k and k.lower() not in STOP_CONCEPTS:
            per[k].append(x)
    existing = {k.lower() for k in types}
    for k, xs in sorted(per.items(), key=lambda kv: -len(kv[1])):
        ndocs = len({x["doc"] for x in xs})
        if len(xs) < 3 or ndocs < 2 or k.lower() in existing:
            continue
        props = [p for p, f in (("date", "dates"), ("amount", "amounts")) if sum(1 for x in xs if x[f]) >= 2]
        k = type_id("concept", k, k)
        types[k] = {"from": "documents", "provenance": "hybrid", "origin": f"{len(xs)} statements in {ndocs} documents", "key": [], "props": props}
        anc = collections.Counter(a[0] for x in xs for v in x["anchors"].values() for a in v)
        for tb, c in anc.items():
            if c >= 2:
                out_links.append({"from": k, "to": name[tb], "via": "same sentence", "statements": c, "origin": "hybrid", "provenance": "hybrid"})
    return types, out_links


def main():
    wall_start, cpu_start = time.monotonic(), time.process_time()
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus")
    ap.add_argument("out", help="new private directory under /tmp")
    ap.add_argument("--measurements", help="optional NEW publishable JSON file")
    a = ap.parse_args()
    root, out = Path(a.corpus).resolve(), Path(a.out).resolve()
    if shutil.disk_usage("/workspaces").free < 2_000_000_000:
        raise RuntimeError("disk below 2GB")
    if not root.is_dir() or out == root or root in out.parents:
        raise ValueError("invalid corpus/output relationship")
    if Path("/tmp") not in out.parents or Path.cwd().resolve() == out or Path.cwd().resolve() in out.parents:
        raise ValueError("private output must be outside repository under /tmp")
    if a.measurements and Path(a.measurements).exists():
        raise ValueError("existing measurements refused")
    out.mkdir(parents=True, exist_ok=False, mode=0o700)
    llm = Llm(str(out / "raw_calls.jsonl"))
    llm.exclusions = []
    report = {"implementation_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "input_sha256": sorted(hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob("*") if p.is_file()),
        "status": "failed", "model": MODEL, "num_ctx": NUM_CTX,
        "prompt_limit_exclusive": MAX_PROMPT_TOKENS, "prompt_guard": "UTF8 bytes including schema/messages + 512 framing tokens",
        "truncation_detection": "server exposes no independent untruncated count; byte bound prevents known context overflow",
        "cache_reuse": False}
    try:
        tables = {}
        for p in sorted(root.rglob("*")):
            if p.is_file():
                if p.suffix in {".sqlite", ".db"}: load_sqlite(str(p), tables)
                elif p.suffix == ".jsonl": load_jsonl(str(p), tables)
                elif p.suffix == ".log": load_log(str(p), tables)
        links = find_links(tables)
        doc_text = "\n".join(p.read_text(encoding="utf8").lower() for p in document_paths(root))
        cats = categorical_entities(tables, doc_text, llm)
        docs, facts, uncovered, n = read_docs(root, tables, llm, lambda m: None)
        types, out_links = induce(tables, links, cats, docs, facts)
        for filename, value in (("ontology.json", {"types": types, "links": out_links}), ("facts.json", facts), ("documents.json", docs),
                ("uncovered.json", uncovered), ("tables.json", tables), ("exclusions.json", llm.exclusions)):
            (out / filename).write_text(json.dumps(value, ensure_ascii=False, indent=1), encoding="utf8")
        report.update(units=n, facts=len(facts), uncovered_units=len(uncovered), documents=len(docs), tables=len(tables),
            types=len(types), links=len(out_links), exclusions=len(llm.exclusions),
            genre_sampled_bytes=sum(d["sampled_bytes"] for d in docs),
            genre_omitted_bytes=sum(d["omitted_bytes"] for d in docs),
            type_provenance=dict(collections.Counter(v["provenance"] for v in types.values())),
            link_provenance=dict(collections.Counter(v["provenance"] for v in out_links)))
        if not types or not any(t["rows"] for t in tables.values()) and not facts:
            raise ValueError("empty ontology run")
        if docs and not facts:
            raise ValueError("documents yielded no grounded facts")
        report["status"] = "built"
    except Exception as exc:
        report["error_type"] = type(exc).__name__
        report["error_message"] = safe_error(exc)
        raise
    finally:
        report.update(wall_seconds=round(time.monotonic() - wall_start, 6),
            cpu_seconds=round(time.process_time() - cpu_start, 6), llm_calls=llm.calls, llm_seconds=round(llm.seconds, 6), max_prompt_eval=llm.maxp,
            model_digest=llm.digest, config=llm.config, calls=llm.records)
        (out / "report.json").write_text(json.dumps(report, indent=1))
        if a.measurements:
            with open(a.measurements, "x") as f:
                json.dump(report, f, indent=1)
        print(json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
