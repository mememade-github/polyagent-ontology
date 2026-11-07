# 소스: QD 실제 진단 실행

[index](../index.md) · [결과 홈](../concepts/qd-real-results.md) · [전체 보고서](../../evidence/qd-real/results.md) · [자료·라이선스](../concepts/qd-real-data.md) · [절차](../concepts/qd-real-procedure.md)

기존 evidence/qd-real 파일 전체와 지정 scientific/controller/analyzer의 archival 원장이다. 아래 conventional backtick 경로·comma bytes·SHA256 first16은 현재 WIP bytes 기준이며 지정 공개 builder가 정제 후 공개 bytes로 재계산한다. 이 페이지는 자기 해시를 포함하지 않는다. 해시 취득은 코드 실행이나 private 본문 독해가 아니다.

| 경로 | bytes | SHA256 (앞16) |
|---|---:|---|
| `evidence/qd-real/acquire.py` | 3,866 | `8f67d7ffad25535b` |
| `evidence/qd-real/analysis-plan.md` | 9,555 | `a07d22b75d6947ca` |
| `evidence/qd-real/analysis-stub.json` | 3,066 | `c15efbd91cd76d03` |
| `evidence/qd-real/discovery.json` | 1,918 | `e7d795d26792c5e3` |
| `evidence/qd-real/docker-audit.json` | 473 | `690f5955efc2a90f` |
| `evidence/qd-real/downloads.json` | 718 | `8bdbfaec7f1785c9` |
| `evidence/qd-real/environment.json` | 1,101 | `3697fdfbf5c3f561` |
| `evidence/qd-real/execution-fix-report.md` | 2,823 | `bb2aa057c9495124` |
| `evidence/qd-real/execution-lock.json` | 1,699 | `b2efb0e2d9001a1c` |
| `evidence/qd-real/execution-stub-summary.json` | 7,490 | `538958424acacf38` |
| `evidence/qd-real/feasibility-gate.md` | 2,823 | `cdac66c458c09010` |
| `evidence/qd-real/gold-review-summary.json` | 1,126 | `882ba30ef34173cc` |
| `evidence/qd-real/judgment-summary.json` | 1,515 | `f872fd46e88feb68` |
| `evidence/qd-real/material-lock.json` | 4,455 | `391fbedf9fa0e21d` |
| `evidence/qd-real/measurements.json` | 154,956 | `8128679e5a6c3e46` |
| `evidence/qd-real/plan-lock.json` | 228 | `020e1ddda9ad4367` |
| `evidence/qd-real/preparation-events.json` | 2,418 | `5b326ad02e72efc9` |
| `evidence/qd-real/procedure-final.json` | 2,876 | `d0e3ef330101a7ab` |
| `evidence/qd-real/publication-policy.json` | 2,527 | `df118076c56e1842` |
| `evidence/qd-real/results.json` | 18,867 | `f54ac3aea045af31` |
| `evidence/qd-real/results.md` | 7,224 | `7f6644d3cd5cac7b` |
| `evidence/qd-real/stub-summary.json` | 2,196 | `22e58192c9c04df1` |
| `evidence/qd-real/review-summary.json` | 4,864 | `118163ed331717ea` |
| `evidence/qd-real/verification.json` | 2,532 | `4a5a59ffe7b7cf54` |
| `prototype/qd/scientific.py` | 16,230 | `4678d6aacd3bae87` |
| `prototype/qd/controller.py` | 4,894 | `4208b3a22d269e25` |
| `prototype/qd/analyze.py` | 32,177 | `63c8ee274c790531` |

실행 당시 original/code SHA는 [execution-lock.json](../../evidence/qd-real/execution-lock.json)과 WIP 실행 기록의 잠금 값이다. 공개 정제 후 archival code(특히 [acquire.py](../../evidence/qd-real/acquire.py))의 위 해시는 공개 보존물 식별자이며 실행 당시 private/WIP lock SHA와 구분한다. builder는 이미 설정되어 있으며 이번 역할은 수정하지 않는다.

full analysis-plan SHA256은 [plan-lock.json](../../evidence/qd-real/plan-lock.json)의 `a07d22b75d6947ca3efdc352052e7c83e5973ef60d3fb9865dc6efea6b012bbc`로 별도 잠금·불변이다. 위 16자리 공개 archival 해시는 이 실행 잠금을 대체하지 않는다.

URL/download SHA와 라이선스는 [downloads.json](../../evidence/qd-real/downloads.json), [discovery.json](../../evidence/qd-real/discovery.json), [자료 페이지](../concepts/qd-real-data.md)에 기록한다. private artifact hashes는 [material lock](../../evidence/qd-real/material-lock.json), [execution lock](../../evidence/qd-real/execution-lock.json), [measurements](../../evidence/qd-real/measurements.json), [judgment summary](../../evidence/qd-real/judgment-summary.json), [gold review](../../evidence/qd-real/gold-review-summary.json)의 metadata다. 원 dataset/gold/labels/predictions/responses는 공개되지 않는다. private 경로에 대한 위키 링크를 만들지 않는다.

공개 scientific.py는 긴 공백의40자 sliding 중복을 없애기 위해 두 continuation 들여쓰기만 정규화했다. 실행 WIP 원본은 잠금 그대로이며 Python AST 동일을 확인했다. 공개 hash와 실행 hash는 [검증 기록](../../evidence/qd-real/verification.json)에 구분한다.
