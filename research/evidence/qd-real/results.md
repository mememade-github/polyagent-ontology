# QD real diagnostic results — qdr-20261107-001

Hq-Fact, Hq-original and Honto are all **INCONCLUSIVE**. Acquisition completed; this is neither a scientific PASS nor a scientific FAIL. This report uses public metadata only, without inspecting private corpus, gold, labels or response text. Final independent manuscript review receives this report only: review is pending and is not a raw-data audit. Parent publication build, privacy checks, independent evaluation and registration remain pending.

The pre-model gold review retained 85 facts and six unresolved ambiguities, complete=false. Both pre- and post-controls failed four of twelve checks: Korean positive verification, both Korean extraction-pipeline positives, and the English role-reversal negative. These failures invalidate scientific threshold decisions; no further cause is inferred here.

There was one unique active prediction, absent from locked gold and judged ambiguous, repeated across six Fact/random and Fact/coverage occurrences at seeds 7, 11 and 19. It is not confirmed true or false: confirmed T=0, F=0, unresolved U=1. The frozen score JSON's precision=0 for these arms is an empty-resolved-label sentinel, not a 0% quality estimate. Fact precision is N/A. Onto and original/random/coverage had zero active predictions; their precision=0 follows the explicit empty-arm rule. Correct cells are 0/4 confirmed only; final recall is not established.

All pools exhausted and paired selectors produced identical active outputs. Selector contrast is uninformative. There is no pooled winner, general QD benefit/nonbenefit conclusion, or ontology claim. This is extraction-only on a fixed public development sample, with unknown pretraining contamination.

## Per-seed quality

T/F are confirmed unique semantic labels within each arm; U counts unresolved active claims (one per Fact arm). P is precision, not a hypothesis verdict. Cell counts use confirmed correct first origins only.

| Seed | Arm | Active | T | F | U | P | Correct cells / fixed cells |
|---|---|---:|---:|---:|---:|---|---|
| 7 | onto | 0 | 0 | 0 | 0 | 0 (empty rule) | 0/4 confirmed only |
| 7 | original-random | 0 | 0 | 0 | 0 | 0 (empty rule) | 0/4 confirmed only |
| 7 | original-coverage | 0 | 0 | 0 | 0 | 0 (empty rule) | 0/4 confirmed only |
| 7 | fact-random | 1 | 0 | 0 | 1 | N/A | 0/4 confirmed only |
| 7 | fact-coverage | 1 | 0 | 0 | 1 | N/A | 0/4 confirmed only |
| 11 | onto | 0 | 0 | 0 | 0 | 0 (empty rule) | 0/4 confirmed only |
| 11 | original-random | 0 | 0 | 0 | 0 | 0 (empty rule) | 0/4 confirmed only |
| 11 | original-coverage | 0 | 0 | 0 | 0 | 0 (empty rule) | 0/4 confirmed only |
| 11 | fact-random | 1 | 0 | 0 | 1 | N/A | 0/4 confirmed only |
| 11 | fact-coverage | 1 | 0 | 0 | 1 | N/A | 0/4 confirmed only |
| 19 | onto | 0 | 0 | 0 | 0 | 0 (empty rule) | 0/4 confirmed only |
| 19 | original-random | 0 | 0 | 0 | 0 | 0 (empty rule) | 0/4 confirmed only |
| 19 | original-coverage | 0 | 0 | 0 | 0 | 0 (empty rule) | 0/4 confirmed only |
| 19 | fact-random | 1 | 0 | 0 | 1 | N/A | 0/4 confirmed only |
| 19 | fact-coverage | 1 | 0 | 0 | 1 | N/A | 0/4 confirmed only |

## Per-seed resources

Actual API tokens; wall seconds include queue/controller. Server total duration is reported separately and is not CPU time. Values below come directly from results.json accounting; wall seconds are rounded to six decimals.

| Seed | Arm | Calls | Input tokens | Output tokens | Total tokens | Wall seconds |
|---|---|---:|---:|---:|---:|---:|
| 7 | onto | 10 | 1850 | 236 | 2086 | 26.157385 |
| 7 | original-random | 20 | 3749 | 493 | 4242 | 45.553554 |
| 7 | original-coverage | 19 | 3539 | 457 | 3996 | 42.248881 |
| 7 | fact-random | 16 | 2651 | 470 | 3121 | 38.783142 |
| 7 | fact-coverage | 16 | 2651 | 470 | 3121 | 39.058194 |
| 11 | onto | 10 | 1850 | 238 | 2088 | 21.500360 |
| 11 | original-random | 20 | 3749 | 492 | 4241 | 43.392209 |
| 11 | original-coverage | 17 | 3102 | 415 | 3517 | 37.309498 |
| 11 | fact-random | 16 | 2651 | 474 | 3125 | 38.459931 |
| 11 | fact-coverage | 16 | 2651 | 485 | 3136 | 38.353314 |
| 19 | onto | 10 | 1850 | 237 | 2087 | 20.535528 |
| 19 | original-random | 21 | 3988 | 523 | 4511 | 42.680234 |
| 19 | original-coverage | 21 | 3988 | 526 | 4514 | 43.631573 |
| 19 | fact-random | 16 | 2651 | 467 | 3118 | 34.278589 |
| 19 | fact-coverage | 16 | 2651 | 458 | 3109 | 36.701835 |

Including both control batches: **276 calls, 47,413 input + 6,929 output = 54,342 actual tokens**, 595.062946 seconds whole acquisition, and 561.10463739 seconds summed server total duration (not CPU). Target arms alone used 244 calls, 50,012 tokens and 548.644230 seconds summed arm wall. Whole acquisition starts before precontrol driver initialization and ends after postcontrol and arm I/O; subsequent manifest/summary writes and cleanup are excluded. Per-arm and whole clocks are distinct.

Maximum actual prompt=364 tokens; maximum reserved prompt+output=2,406. The audit captured the entire stopped container lifetime: zero case-insensitive truncating events; 276 chat log events match 276 measured calls. Container removed; existing image/volume retained. These are metadata audit observations, not a fresh raw-log audit by this documentation role.

## Frozen interpretation and procedure

One evaluation matrix: 15 arms and pre/post controls, no target reruns and no reused responses. Tuning used authored synthetic controls and Stub fixtures only; model prompt tuning runs=0. Fixed public dev selection: 12 units, 7 eligible and 5 deferred. Gold never amended from predictions. The actual judging input is judge-units.json, whose hash is recorded in judgment-summary.json; an earlier narrative typo does not name a different input.

Hard per-arm caps remained 64 calls, 64,000 actual tokens and 900 seconds; operational cap=24 calls, global acquisition cap=1,800 seconds. Recorded consumption stayed within these bounds. Original criteria remain precision≥90% and nondecrease, unique correct gain≥max(1,ceil(10%×comparator T)), and confirmed gold-cell recall nondecrease, independently at every seed. No threshold adjustment from data. Frozen threshold booleans do not override invalid gold/controls: all three hypothesis verdicts remain INCONCLUSIVE.

The initial score CLI omitted --out and exited 2 before producing analysis; corrected arguments used the same frozen analyzer and single acquisition. This was not a model rerun. Fourteen locks were verified by the recorded analysis; blinding and unchanged rules were attested. This documentation role has not independently audited private artifacts.

Sources: [results.json](results.json), [measurements.json](measurements.json), [gold review](gold-review-summary.json), [judgment summary](judgment-summary.json), [final procedure](procedure-final.json), [container audit](docker-audit.json). Fixed [data/license provenance](../../wiki/concepts/qd-real-data.md), [procedure](../../wiki/concepts/qd-real-procedure.md), [analysis plan](analysis-plan.md), [plan lock](plan-lock.json), [source inventory](../../wiki/sources/qd-real.md). Locked analysis-plan SHA256: `a07d22b75d6947ca3efdc352052e7c83e5973ef60d3fb9865dc6efea6b012bbc` (full execution lock value, unchanged).
