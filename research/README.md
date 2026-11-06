# Research knowledge space

Independent research space following the [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern. Rules are in [wiki/SCHEMA.md](wiki/SCHEMA.md); start at [wiki/index.md](wiki/index.md).

> **Warning:** Scripts in `evidence/` are archival and must NOT be run as-is. Some empty a database (`knockout.py`), forcibly remove fixed-name containers, or expose unauthenticated Stub servers on all interfaces.

Most historical models are Stub; real-model observations are small-scale. This is not a product evaluation or recommendation.

The new prototype has a [paper-informed design](wiki/concepts/paper-informed-design.md) and [usage instructions](prototype/README.md). Its measurements follow a [frozen protocol](evidence/prototype/protocol.md); they describe the measured development samples, not general performance. Raw inputs, sample document texts, private prompts, facts/output dumps and caches are excluded. The authoritative WIP is retained separately.
