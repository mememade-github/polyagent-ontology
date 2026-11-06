# 소스: QD 적응 실행·절차

[index](../index.md) · [QDA 홈](../concepts/qd-rec-adaptation.md) · [보존한 upstream 선언·논문 해시](qd-rec.md)

새로 작성한 코드는 upstream 개념만 재사용했다. upstream 고정 HEAD와 인용한 7파일의 전체 해시는 procedure.json에 다시 대조·기록했다. 기존 raw는 바꾸지 않았다. proposal-inputs/challenge는 관리자의 **요약**이며 원 skill/논문/세션 전문이 아니다. 실제 전달 입력 SHA256과 문맥 접근 조건은 procedure.json에 있다. 원 procedure의 검토 대기는 역사 기록이며 새 review-summary가 대체한다. 부모 최종 독립 평가는 대기다.

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/qd-adaptation/lock.json` | 200 | `af3daa4a1dda19e1` |
| `evidence/qd-adaptation/procedure.json` | 2,864 | `543220b4bc567481` |
| `evidence/qd-adaptation/protocol.md` | 3,379 | `ace4e402d240df3b` |
| `evidence/qd-adaptation/results.json` | 2,403 | `3c5ae7f53b295684` |
| `evidence/qd-adaptation/run-001.json` | 38,505 | `0f8230644d85736f` |
| `prototype/qd/controller.py` | 4,499 | `a46aefba779744bf` |
| `prototype/qd/demo.py` | 4,184 | `eb6a3a4313573532` |
| `prototype/onto.py` | 31,227 | `400e86746580509e` |

인용: E:qd-adaptation/protocol.md, E:qd-adaptation/lock.json, E:qd-adaptation/procedure.json, E:qd-adaptation/run-001.json, E:qd-adaptation/results.json. 결과 파일은 자기 해시를 포함하지 않는다. run은 controller/demo/onto/protocol 전체 SHA256을 포함하고 results는 run의 전체 해시를 포함한다. 이 원장의 해시는 원장 자체를 대상으로 하지 않는다.

실행: `PYTHONDONTWRITEBYTECODE=1 python3 prototype/qd/demo.py evidence/qd-adaptation/새-run-ID.json` (WIP 루트에서). 기존 결과를 덮어쓰면 exclusive create 실패한다. Stub는 고정 응답 iterator이며 자연어 정답을 계산하지 않는다. 11검사/39호출 통과는 mechanical 결과만이다. 원 시스템이나 실모델의 품질 수치를 새로 측정하지 않았다.

## 검토 후 추가 불변 근거

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/qd-adaptation/review-summary.json` | 1,339 | `9c83a284cda8098d` |
| `evidence/qd-adaptation/independent-calculation.json` | 11,473 | `6af01358041348fe` |
| `evidence/qd-adaptation/future-analysis-addendum.md` | 4,403 | `65fabd2ade1dbfb8` |
| `evidence/qd-adaptation/addendum-lock.json` | 353 | `175257a1d2a59d76` |
| `evidence/qd-adaptation/publication-policy.json` | 1,321 | `28e0e356cd78634f` |

공개 정책: QD 논문 stored HTML 255행 CC BY 4.0, LICENSE Apache 2.0을 대조했다. 허용되어도 전문·파생 텍스트·클론 코드는 공개하지 않는다. 위 publication-policy의 strict allowlist만 추가하며 기존 제외·정제를 보존한다.
