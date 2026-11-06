# 소스: evidence/helix

위치: `evidence/helix/`. 불변 원본이다.

Helix 실험 스크립트, Stub, turn 입력, 판정 원시 출력 `report3.raw`이다. ~~`ontology.toml`과 캡처 로그는 없다~~ → results.md 수집 후 `ontology.toml`, `ontology_nokey.toml`, `mappings.toml`을 보존했다. 이 셋은 저장소 수록본에 없다([SCHEMA](../SCHEMA.md)). 캡처 로그의 상태는 [C-12](../contradictions.md#C-12)이다.

## 수집 시점 파일

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/helix/doc.md` | 230 | `8892e898c37a8670` |
| `evidence/helix/mkdocs.py` | 577 | `cc64f7dbfd764b4d` |
| `evidence/helix/ontology_nokey.toml` | (저장소 미포함) | - |
| `evidence/helix/report3.raw` | 4,074 | `faa53261105ecc79` |
| `evidence/helix/run.sh` | 561 | `3c2ff88be8a66214` |
| `evidence/helix/run2.sh` | 586 | `ba6a280d15a527c6` |
| `evidence/helix/run_nokey.sh` | 567 | `510859cde0f1643f` |
| `evidence/helix/stub2.py` | 2,552 | `c7d842ed97965d93` |
| `evidence/helix/stub4.py` | 981 | `32636a368871703d` |
| `evidence/helix/turn.json` | 688 | `2b78e6c516b20bbe` |
| `evidence/helix/turn_a.json` | 812 | `4cad76b0e8e0703d` |
| `evidence/helix/turn_b.json` | 884 | `e67e9e3e3df762f7` |

## results.md 수집 때 추가된 파일

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/helix/ontology.toml` | (저장소 미포함) | - |

## 이 소스를 인용하는 요소

[M-10](../method-and-limits.md#M-10), [HX-01](../products/helix-foundry.md#HX-01), [HX-03](../products/helix-foundry.md#HX-03), [HX-06](../products/helix-foundry.md#HX-06), [HX-13](../products/helix-foundry.md#HX-13), [HX-14](../products/helix-foundry.md#HX-14), [HX-15](../products/helix-foundry.md#HX-15), [HX-16](../products/helix-foundry.md#HX-16), [HX-17](../products/helix-foundry.md#HX-17), [QV-01](../concepts/quote-validation.md#QV-01), [ES-02](../concepts/evidence-spans.md#ES-02), [SK-08](../concepts/ontology-skeleton-source.md#SK-08), [HA-02](../concepts/human-approval.md#HA-02), [SV-01](../concepts/second-verifier.md#SV-01), [SV-02](../concepts/second-verifier.md#SV-02), [SV-03](../concepts/second-verifier.md#SV-03), [SV-04](../concepts/second-verifier.md#SV-04), [SV-05](../concepts/second-verifier.md#SV-05), [SV-07](../concepts/second-verifier.md#SV-07), [OC-02](../concepts/output-constraints.md#OC-02), [TK-01](../concepts/context-budget.md#TK-01), [TK-03](../concepts/context-budget.md#TK-03), [TK-04](../concepts/context-budget.md#TK-04), [TK-05](../concepts/context-budget.md#TK-05), [TK-12](../concepts/context-budget.md#TK-12), [SYM-13](../concepts/binary-symbols.md#SYM-13)


## grpc/ (2026-11-06 추가)

`ontology-agent serve`에 직접 보낸 Extract, Ask 실험. 스크립트 `client.py`, `go*.py`, `oai_stub.py`, 출력 `faults.out`, `ctx_sweep.out`, `ask_ctx.out`, `ollama_bound.out`. 실제 모델 출력은 `../real-model/`.


## 추가 수집 파일 (2026-11-06 등록 전 점검)

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/helix/extract.help.txt` | 2,544 | `c3965e90d4d8e7b5` |
| `evidence/helix/grpc/ask_ctx.out` | 912 | `fd7f99f71a3206ee` |
| `evidence/helix/grpc/client.py` | 2,401 | `2b59312f9701f7db` |
| `evidence/helix/grpc/ctx_sweep.out` | 1,947 | `cc7346fcf03d9047` |
| `evidence/helix/grpc/faults.out` | 13,622 | `47c399b09ff3eb4a` |
| `evidence/helix/grpc/go1.py` | 1,235 | `e0919524e77acba2` |
| `evidence/helix/grpc/go2.py` | 1,592 | `b9fdb1ab10b57bef` |
| `evidence/helix/grpc/go4.py` | 1,359 | `58af90bfa910b1fe` |
| `evidence/helix/grpc/go5.py` | 1,213 | `a34c44d6e040c151` |
| `evidence/helix/grpc/go6.py` | 1,453 | `10b89e00d7fe0a7e` |
| `evidence/helix/grpc/go7.py` | 2,562 | `d272322d906d20cb` |
| `evidence/helix/grpc/go8.py` | 1,463 | `aadd1becc27fdd67` |
| `evidence/helix/grpc/go9.py` | 1,953 | `476421233b633193` |
| `evidence/helix/grpc/oai_stub.py` | 5,213 | `a59b3e51f55b85af` |
| `evidence/helix/grpc/ollama_bound.out` | 2,608 | `0b9a2b18138087e9` |
| `evidence/helix/grpc/start.sh` | 656 | `cb4be3a6f77a7f47` |
| `evidence/helix/grpc/token_summary.json` | 291 | `46d807eee7437773` |
| `evidence/helix/ingest-mapped.help.txt` | 853 | `b4ae580a337198b0` |
| `evidence/helix/mappings.toml` | (저장소 미포함) | - |

---
[index](../index.md) · [coverage](../coverage.md)
