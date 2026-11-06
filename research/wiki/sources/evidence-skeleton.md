# 소스: evidence/skeleton

위치: `evidence/skeleton/`. 불변 원본이다.

뼈대 생성을 실제 모델로 실행한 기록이다. `qwen2.5:3b`, Ollama 0.40.10, CPU, 스레드 14. 파생 모델은 `qwen3b-t14`(스레드만), `qwen3b-c8`(`num_ctx` 8192), `qwen3b-c64`(`num_ctx` 65536)이다. Helix는 `ontology-agent turn`을 직접 실행했고 `proxy.py`가 응답을 기록했다. Auto-Ontology는 `ao.sh`의 프록시로 채팅만 실제 모델에 보냈고 임베딩은 해시값이다. 문서는 `evidence/rea/quote/doc.md`, `evidence/real-model/gold.md`이다.

## 수집 시점 파일

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/skeleton/accounts.jsonl` | 222 | `8bd07a4a65343a1e` |
| `evidence/skeleton/ao.out` | 3,956 | `b533b6fc8f62756b` |
| `evidence/skeleton/ao.sh` | 3,504 | `07da649c13144609` |
| `evidence/skeleton/ao_docs.calls` | 17,114 | `bcbd4af8901749ff` |
| `evidence/skeleton/ao_shop.calls` | 18,071 | `93afd147d84b2c50` |
| `evidence/skeleton/d1_ctx8k_doc.out` | 1,139 | `e7afafba211a5880` |
| `evidence/skeleton/d2_ctx64k_doc.out` | 1,139 | `e7afafba211a5880` |
| `evidence/skeleton/mk2.py` | 1,248 | `a6eaeb8ee6c28ec8` |
| `evidence/skeleton/proxy.py` | 1,603 | `50a592a7dbc6a3f9` |
| `evidence/skeleton/run2.sh` | 1,542 | `6d50a4fe63680167` |
| `evidence/skeleton/s1.out` | 1,139 | `e7afafba211a5880` |
| `evidence/skeleton/s2.out` | 1,139 | `e7afafba211a5880` |
| `evidence/skeleton/s4.out` | 931 | `0b00a908631b95d2` |
| `evidence/skeleton/s5.out` | 931 | `0b00a908631b95d2` |
| `evidence/skeleton/show.py` | 774 | `63845beac21e0515` |
| `evidence/skeleton/summary.txt` | 248 | `036c1afe9bcfb1c6` |
| `evidence/skeleton/sweep.sh` | 2,442 | `d8fd526a764d0323` |
| `evidence/skeleton/t1_ctx8k_doc.calls` | 41,180 | `57630e0e8ba3a5f2` |
| `evidence/skeleton/t1_ctx8k_doc.ollama` | 10,193 | `249f7862284006a2` |
| `evidence/skeleton/t1_ctx8k_doc.out` | 9,674 | `9ecdb0c0aa7c5f72` |
| `evidence/skeleton/t1b_ctxclaim64k_real8k.calls` | 40,693 | `ae9bf17cac4df6b9` |
| `evidence/skeleton/t1b_ctxclaim64k_real8k.ollama` | 9,836 | `e8b1d0c8a7c06945` |
| `evidence/skeleton/t1b_ctxclaim64k_real8k.out` | 9,472 | `9393a5b0561a107e` |
| `evidence/skeleton/t2_ctx64k_doc.calls` | 181,271 | `5a3da59a91a09f24` |
| `evidence/skeleton/t2_ctx64k_doc.ollama` | 1,696 | `0a7e34b3cfb61b15` |
| `evidence/skeleton/t2_ctx64k_doc.out` | 2,242 | `27054b8d442bcabf` |
| `evidence/skeleton/t3_ctx64k_gold_table.calls` | 463,767 | `dd4997b4cdcf19bd` |
| `evidence/skeleton/t3_ctx64k_gold_table.ollama` | 1,158 | `595469699c23e41d` |
| `evidence/skeleton/t3_ctx64k_gold_table.out` | 2,156 | `62da681559f74008` |

---
[index](../index.md) · [logical structuring](../concepts/logical-structuring.md)
