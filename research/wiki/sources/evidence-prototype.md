# 소스: evidence/prototype

[index](../index.md) · [실측 결과](../concepts/prototype-results.md) · [설계](../concepts/paper-informed-design.md)

조정자의 results-ready 신호 이후 공개 payload 4파일을 바이트 그대로 수집했다. raw 모델 출력·입력 본문은 포함하지 않는다. 아래 해시는 수집 시점이며 전체 source/code/reference/model 정보는 `E:prototype/hashes.json`, 실행 환경·개발 실패 원장은 `E:prototype/measurements.json`에 있다. `protocol.md`와 `paper-access.json`은 변경하지 않았다.

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/prototype/protocol.md` | 3,849 | `dbc2b8673b7b5afe` |
| `evidence/prototype/paper-access.json` | 6,215 | `53ef3ffbe96862b6` |
| `evidence/prototype/measurements.json` | 362,853 | `b771a2918c64fec0` |
| `evidence/prototype/evaluation.json` | 18,891 | `0d83e80462a9bd15` |
| `evidence/prototype/stability.json` | 644 | `bea33f7eab977652` |
| `evidence/prototype/hashes.json` | 4,301 | `2e9a3ee81c88ab01` |
| `evidence/prototype/results.md` | 11,569 | `9792543780fbfa5c` |

인용: E:prototype/protocol.md, E:prototype/paper-access.json, E:prototype/measurements.json, E:prototype/evaluation.json, E:prototype/stability.json, E:prototype/hashes.json, E:prototype/results.md.

이 소스의 홈 요소는 [PX-01~PX-08](../concepts/prototype-results.md#PX-01)이다. 기존 공개 합성 gold와 새 비공개 raw 출력은 구분한다. 샘플 출처는 HelixDB/helix-foundry, Apache-2.0, commit `c7de40515f56a491d1b46af0bb1efa890f106700`이다. 원본 샘플은 재배포하지 않는다.
