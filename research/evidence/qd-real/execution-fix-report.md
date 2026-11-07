# Execution fixes R1/R2

Implemented only WIP `prototype/qd/scientific.py` and scratch `acquire.py`; plan/scorer and criteria unchanged. No recursive refine or commit.

R1: Driver accepts optional absolute `global_deadline`. Each remaining check samples current monotonic once and returns min(arm expiry - now, global expiry - now), rejecting <= 0. Acquisition passes its original absolute deadline without regenerating a relative budget. Defaults remain 900 seconds, 24 calls, 64000 tokens; acquisition global limit remains 1800 seconds.

R2: targeted `docker stop --time 10 ollama-t` is attempted once in an outer finally around acquisition and result/manifest/summary writes, on success or failure. Subprocess timeout is 20 seconds. Cleanup exit/stderr, timeout, or launch exception is printed visibly to stderr. Cleanup failure produces nonzero exit; an existing acquisition abort remains the primary recorded error and produces exit 1 even if persistence fails. A write failure without an acquisition abort propagates after cleanup. No removal command exists in the wrapper; parent collects logs and removes the targeted container.

Elapsed description now ends at the sampled timestamp following postcontrol and arm I/O, excluding subsequent manifest/summary writes and cleanup.

Verification: full 25 historical Stub checks rerun successfully, including disk and arm-deadline checks, plus 7 new boundary checks. Synthetic creation delay beyond absolute deadline: zero metadata/model dispatch and zero attempts. Min-budget and unchanged defaults verified. Timeout + persistence failure with both cleanup timeout and nonzero cleanup exit: exactly one targeted stop attempt with timeout=20, acquisition TimeoutExpired retained. Normal completion, write failure after normal acquisition, and timeout without write failure also stop once. Historical reports were preserved by redirecting suite files/reports to a fresh scratch child. Test harness: `execution-fix-check.py`; detailed evidence: `execution-fix-stub.json`.

No target units/gold/raw/outputs read. No real model or Docker calls. Full-response slow-drip check uses only a synthetic loopback HTTP server. Git diff --check passed; WIP code is ignored by Git, so Git diff/status do not provide its change evidence. Code hashes below identify the tested implementation.

Gold review complete=false means diagnostic-only regardless of numeric results; criteria unchanged. Parent must lock these code/dependency hashes and remaining execution gates before the first real call. This report does not authorize or perform that call.

SHA-256:

- `__RESEARCH__/prototype/qd/scientific.py`: `7c1413b2dd041e1f03b54d3632386db6e6976e2b1eab7c706ced9b47e4ba7f59`

- `__SCRATCH__/qd-real-20261107/acquire.py`: `2f7eec0c3c5a3b6f50b3eb47d53530029d004cdffa2ec6b3f304962d7221b2d6`
