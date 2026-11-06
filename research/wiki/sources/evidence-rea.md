# 소스: evidence/rea (interim.md 제외)

위치: `evidence/rea/`. 불변 원본이다.

초안 스크립트와 출력 1건, 인용 12변형 원시 출력, 엔티티 창 스크립트, REA 출력이다. window 입력과 로그, `nm` 출력, 실행 2의 원시 출력은 없다. results.md 수집 후 재확인은 [C-12](../contradictions.md#C-12).

## 수집 시점 파일

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/rea/draft/doc.md` | 230 | `8892e898c37a8670` |
| `evidence/rea/draft/go.py` | 335 | `1a4a1c0a1025480e` |
| `evidence/rea/draft/out2.ndjson` | 6,086 | `b70563d7ede5cada` |
| `evidence/rea/draft/run.sh` | 438 | `039721c714775e35` |
| `evidence/rea/draft/show.py` | 458 | `ae8895978a816117` |
| `evidence/rea/draft/stub5.py` | 3,095 | `4368156aed570ba1` |
| `evidence/rea/draft/t0.json` | 813 | `744b7e3b1df41bcd` |
| `evidence/rea/draft/t8k.json` | 885 | `31c8ad507425bb9b` |

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/rea/quote/doc.md` | 263 | `5421895eedb0b8cd` |
| `evidence/rea/quote/r_case.raw` | 2,236 | `19693d3b1b91633d` |
| `evidence/rea/quote/r_ellipsis.raw` | 1,898 | `c4796b22db886b9d` |
| `evidence/rea/quote/r_exact.raw` | 2,236 | `d90c139fcb7f3ce8` |
| `evidence/rea/quote/r_fullwidth.raw` | 2,238 | `8df64c623909cdfa` |
| `evidence/rea/quote/r_ko_nfc.raw` | 2,242 | `124c009194d235b9` |
| `evidence/rea/quote/r_ko_nfd.raw` | 2,314 | `1f162c91d2417fe9` |
| `evidence/rea/quote/r_ko_space.raw` | 1,916 | `9fefb6919b5cf910` |
| `evidence/rea/quote/r_midword.raw` | 2,233 | `3a91ec159fe52611` |
| `evidence/rea/quote/r_other_section.raw` | 1,887 | `a378298670fa00cf` |
| `evidence/rea/quote/r_paraphrase.raw` | 1,913 | `15b43de7d6ba0f8f` |
| `evidence/rea/quote/r_punct_dropped.raw` | 2,234 | `00b36b02415af48b` |
| `evidence/rea/quote/r_space.raw` | 2,241 | `e7ce4f3ba1842f48` |
| `evidence/rea/quote/run.py` | 1,725 | `aba80ee88b897694` |
| `evidence/rea/quote/stub.py` | 1,654 | `026f9764992634c3` |

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/rea/window/run.py` | 1,786 | `5551e9c7b2658752` |
| `evidence/rea/window/stub.py` | 1,122 | `0d9964b23938511a` |

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/rea/rust-extract.json` | (저장소 미포함) | - |
| `evidence/rea/rust-ingest-mapped.json` | (저장소 미포함) | - |
| `evidence/rea/rust-ontology-agent.json` | (저장소 미포함) | - |

## results.md 수집 때 추가된 파일

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/rea/approval/a0_wrongrev.out` | 4,331 | `1ea5b41220bd8485` |
| `evidence/rea/approval/a1.out` | 5,937 | `b52ba0389263656d` |
| `evidence/rea/approval/a2.out` | 7,658 | `834afe8d782cf156` |
| `evidence/rea/approval/appr.py` | 1,870 | `47fd5b7286c563eb` |
| `evidence/rea/approval/appr2.py` | 1,029 | `f59ecf0d551d4045` |
| `evidence/rea/approval/approved.json` | (저장소 미포함) | - |
| `evidence/rea/approval/bundle_mappings.toml` | 204 | `84644e4a4b3273aa` |
| `evidence/rea/approval/bundle_ontology.toml` | 315 | `16a5911b2b412c62` |
| `evidence/rea/approval/c1.out` | 6,437 | `24e2b8dd3fba4bc4` |
| `evidence/rea/approval/e2e.out` | 2,238 | `2cce181220a8d549` |
| `evidence/rea/approval/e2e.sh` | 543 | `5b4e061c1aeeebd5` |
| `evidence/rea/approval/f1.out` | 4,869 | `59571ac2cb255d7a` |
| `evidence/rea/approval/over.out` | 1,018 | `2e990cb4fd9dca69` |
| `evidence/rea/approval/stub_e2e.py` | 1,553 | `2f7e2da5e2fb263b` |
| `evidence/rea/approval/stub_over.py` | 695 | `b455900c71899b17` |
| `evidence/rea/approval/sys.txt` | (저장소 미포함) | - |
| `evidence/rea/adjudicate/ex.sh` | 542 | `726b5b4b5b344176` |
| `evidence/rea/adjudicate/ex1.out` | 2,111 | `3308520b10ae2d93` |
| `evidence/rea/adjudicate/r_exact_name.json` | 2,425 | `a6afed08e568fe61` |
| `evidence/rea/adjudicate/r_match_.89.json` | 2,451 | `ac475320fa21451d` |
| `evidence/rea/adjudicate/r_match_.90.json` | 2,452 | `dab6971543d7386e` |
| `evidence/rea/adjudicate/r_match_.95.json` | 2,453 | `e6616f9047c21e7b` |
| `evidence/rea/adjudicate/r_null_choice.json` | 2,453 | `a2ff76367de3c981` |
| `evidence/rea/adjudicate/r_unrelated.json` | 2,297 | `d0575dacdc34bc80` |
| `evidence/rea/adjudicate/src.json` | 108 | `c59278855c3592b6` |
| `evidence/rea/adjudicate/stub_adj.py` | 2,054 | `9255a7b72b82b908` |
| `evidence/rea/adjudicate/t.py` | 1,361 | `6cf4f46a9e55f74b` |
| `evidence/rea/adjudicate/t2.py` | 713 | `a6825c2fb5596e64` |
| `evidence/rea/adjudicate/t3.py` | 665 | `4cbf36bf36c2bf65` |
| `evidence/rea/adjudicate/try.sh` | 524 | `837d773f6e1d3708` |
| `evidence/rea/decompiled/extract/adj_bounded.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/extract/adj_choices.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/extract/dec_entity.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/extract/dec_fitting.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/extract/fold.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/extract/locate_quote.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/extract/sections.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/extract/tokens.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/ontology-agent/b_exhausted.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/ontology-agent/b_near.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/ontology-agent/b_prompt_bound.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/ontology-agent/b_room.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/ontology-agent/m_maxtokens.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/ontology-agent/m_runtime.c` | (저장소 미포함) | - |
| `evidence/rea/decompiled/ontology-agent/m_settle.c` | (저장소 미포함) | - |
| `evidence/rea/ghidra/DecAddrs.java` | (저장소 미포함) | - |
| `evidence/rea/ghidra/addrs-oa.txt` | (저장소 미포함) | - |
| `evidence/rea/ghidra/addrs.txt` | (저장소 미포함) | - |
| `evidence/rea/quote/fuzzy.json` | 2,509 | `20de7a2492a40f1e` |
| `evidence/rea/quote/run2.py` | 1,705 | `5dad7b2e6ece4208` |
| `evidence/rea/window/run3.py` | 1,357 | `be1b6199719813cb` |

## 이 소스를 인용하는 요소

[M-06](../method-and-limits.md#M-06), [M-10](../method-and-limits.md#M-10), [M-12](../method-and-limits.md#M-12), [M-16](../method-and-limits.md#M-16), [HX-01](../products/helix-foundry.md#HX-01), [HX-05](../products/helix-foundry.md#HX-05), [QV-02](../concepts/quote-validation.md#QV-02), [QV-03](../concepts/quote-validation.md#QV-03), [QV-04](../concepts/quote-validation.md#QV-04), [QV-05](../concepts/quote-validation.md#QV-05), [QV-06](../concepts/quote-validation.md#QV-06), [QV-07](../concepts/quote-validation.md#QV-07), [QV-08](../concepts/quote-validation.md#QV-08), [QV-09](../concepts/quote-validation.md#QV-09), [QV-10](../concepts/quote-validation.md#QV-10), [QV-11](../concepts/quote-validation.md#QV-11), [QV-12](../concepts/quote-validation.md#QV-12), [QV-13](../concepts/quote-validation.md#QV-13), [QV-15](../concepts/quote-validation.md#QV-15), [EW-01](../concepts/entity-windows.md#EW-01), [SK-01](../concepts/ontology-skeleton-source.md#SK-01), [SK-02](../concepts/ontology-skeleton-source.md#SK-02), [SK-03](../concepts/ontology-skeleton-source.md#SK-03), [SV-04](../concepts/second-verifier.md#SV-04), [TK-14](../concepts/context-budget.md#TK-14), [SYM-13](../concepts/binary-symbols.md#SYM-13), [M-19](../method-and-limits.md#M-19), [M-20](../method-and-limits.md#M-20), [M-21](../method-and-limits.md#M-21), [QV-20](../concepts/quote-validation.md#QV-20), [QV-21](../concepts/quote-validation.md#QV-21), [QV-22](../concepts/quote-validation.md#QV-22), [QV-23](../concepts/quote-validation.md#QV-23), [QV-24](../concepts/quote-validation.md#QV-24), [QV-25](../concepts/quote-validation.md#QV-25), [QV-26](../concepts/quote-validation.md#QV-26), [QV-27](../concepts/quote-validation.md#QV-27), [QV-28](../concepts/quote-validation.md#QV-28), [QV-29](../concepts/quote-validation.md#QV-29), [QV-31](../concepts/quote-validation.md#QV-31), [EW-09](../concepts/entity-windows.md#EW-09), [HA-06](../concepts/human-approval.md#HA-06), [HA-07](../concepts/human-approval.md#HA-07), [HA-08](../concepts/human-approval.md#HA-08), [HA-09](../concepts/human-approval.md#HA-09), [HA-10](../concepts/human-approval.md#HA-10), [HA-11](../concepts/human-approval.md#HA-11), [HA-13](../concepts/human-approval.md#HA-13), [SV-10](../concepts/second-verifier.md#SV-10), [SV-11](../concepts/second-verifier.md#SV-11), [SV-12](../concepts/second-verifier.md#SV-12), [SV-13](../concepts/second-verifier.md#SV-13), [SV-14](../concepts/second-verifier.md#SV-14), [SV-15](../concepts/second-verifier.md#SV-15), [SV-16](../concepts/second-verifier.md#SV-16), [TK-16](../concepts/context-budget.md#TK-16), [TK-17](../concepts/context-budget.md#TK-17), [TK-18](../concepts/context-budget.md#TK-18), [TK-19](../concepts/context-budget.md#TK-19), [TK-20](../concepts/context-budget.md#TK-20), [SYM-17](../concepts/binary-symbols.md#SYM-17), [SYM-18](../concepts/binary-symbols.md#SYM-18), [SYM-19](../concepts/binary-symbols.md#SYM-19), [SYM-20](../concepts/binary-symbols.md#SYM-20)


## 추가 수집 파일 (2026-11-06 등록 전 점검)

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/rea/adjudicate/a.log.adj` | (저장소 미포함) | - |
| `evidence/rea/adjudicate/rows.jsonl` | 137 | `3fbcbf8f90004063` |
| `evidence/rea/approval/a0_wrongrev.log.jsonl` | 0 | `e3b0c44298fc1c14` |
| `evidence/rea/approval/a1.log.jsonl` | 0 | `e3b0c44298fc1c14` |
| `evidence/rea/approval/a2.log.jsonl` | 0 | `e3b0c44298fc1c14` |
| `evidence/rea/approval/c1.log.jsonl` | (저장소 미포함) | - |
| `evidence/rea/approval/f1.log.jsonl` | 0 | `e3b0c44298fc1c14` |
| `evidence/rea/decompiled/extract/normalize.c` | (저장소 미포함) | - |

---
[index](../index.md) · [coverage](../coverage.md)
