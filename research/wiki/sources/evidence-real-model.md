# 소스: evidence/real-model

위치: `evidence/real-model/`. 불변 원본이다.

`qwen2.5:3b`(스레드 8 파생 모델 `qwen3b-t8`), Ollama 0.40.10, CPU 실행 기록이다. Helix는 gRPC `Extract`와 `Ask`, RAGFlow는 패키지 내부 하니스로 호출했다. 정답지 `gold.txt`와 문서 `gold.md`는 이 조사에서 작성한 합성 자료이다. 이 환경은 조사 중 임시로 구성했고 실행 후 제거했다.

## 수집 시점 파일

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/real-model/ask.out` | 2,277 | `c5bd652175671ca4` |
| `evidence/real-model/default_ctx.out` | 372 | `c8516d7a9e69ce39` |
| `evidence/real-model/gold.md` | 845 | `d4301b300b8e4a6c` |
| `evidence/real-model/gold.txt` | 294 | `1c07cc10aa847e5b` |
| `evidence/real-model/h_real_structure_test.go.txt` | 3,033 | `42ad870122a574c8` |
| `evidence/real-model/h_real_tree_test.go.txt` | 2,198 | `12d6ccb6b65d4c77` |
| `evidence/real-model/helix.out` | 620 | `350cdebbaceb9dc3` |
| `evidence/real-model/helix_docmd.out` | 1,188 | `1c088914310b0fc2` |
| `evidence/real-model/ov_direct.out` | 2,423 | `d43141a6ad688427` |
| `evidence/real-model/real_gold.json` | 2,126 | `50afc09280786256` |
| `evidence/real-model/real_s8k.json` | 7,233 | `8af7e9c4d54e4f92` |
| `evidence/real-model/rf_claims.out` | 14,762 | `7611b7e50cbe41ab` |
| `evidence/real-model/rf_graph.out` | 1,461 | `9e878c8b71c0d3c0` |
| `evidence/real-model/run.sh` | 702 | `b2a825981be52de7` |

## 이 소스를 인용하는 요소

[LC-01](../knowledge-lifecycle.md#LC-01)~[LC-04](../knowledge-lifecycle.md#LC-04), [LC-11](../knowledge-lifecycle.md#LC-11), [LC-14](../knowledge-lifecycle.md#LC-14), [LC-32](../knowledge-lifecycle.md#LC-32), [LC-33](../knowledge-lifecycle.md#LC-33), [LC-40](../knowledge-lifecycle.md#LC-40)~[LC-44](../knowledge-lifecycle.md#LC-44)

---
[index](../index.md) · [coverage](../coverage.md)
