# QD 실제 자료: 발견·선택과 한계

**results.md 갱신:** 아래는 획득 전 역사적 준비 기록이다. 당시의 미실행·대기 표시는 현재 상태가 아니다. 실제 15 arms+pre/post 완료와 INCONCLUSIVE 판정은 [실제 결과](qd-real-results.md)에 기록했다.

[index](../index.md) · [절차](qd-real-procedure.md) · [기존 적응](qd-rec-adaptation.md) · [SCHEMA](../SCHEMA.md)

이번 페이지는 허용된 metadata/plan/Stub 기록의 관찰이다. 대상 원문·gold·모델 출력을 이 문서 역할에서 읽지 않았다. 실제 one-shot 결과는 아직 기록하지 않는다. 기존 raw와 역사 진술은 보존한다.

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QDR-D1"></a>QDR-D1 | 실제 발견 절차 | [실행] | [discovery](../../evidence/qd-real/discovery.json), [준비 이력](../../evidence/qd-real/preparation-events.json) | 먼저 metadata·라이선스 검색, 계획 동결 후 고정 파일 다운로드. 기록된 검색어는 `DocRED dataset github license annotated distant supervision human dev`, `KorQuAD 1.0 license CC BY ND dataset`, `SQuAD dataset license CC BY SA 4.0`. 공식 metadata·라이선스 응답 상태·바이트·해시·시각을 보존 | 검색 전체를 망라하지 않음 |
| <a id="QDR-D2"></a>QDR-D2 | 다섯 후보 결정 | [설계] | [동결 계획](../../evidence/qd-real/analysis-plan.md), 아래 후보 표 | 공개 문서, 독립 답/관계, 명시 라이선스, 다운로드 규모, 가능하면 영어·한국어 및 구조 companion을 기준으로 SQuAD2와 KLUE RE 채택 | 완전한 임의 사실 gold 발견 아님 |
| <a id="QDR-D3"></a>QDR-D3 | 계획·자료 잠금 | [실행] | [plan lock](../../evidence/qd-real/plan-lock.json), [downloads](../../evidence/qd-real/downloads.json), [material lock](../../evidence/qd-real/material-lock.json), [execution lock](../../evidence/qd-real/execution-lock.json) | 계획 SHA256 `a07d22b75d6947ca3efdc352052e7c83e5973ef60d3fb9865dc6efea6b012bbc`, 시각 `2026-11-07T00:46:32.199936+00:00`; target_content_accessed=false. 자료 잠금 `2026-11-07T00:57:59.860052+00:00`: 6문서·12단위·7 eligible·5 deferred, gold85·미해결6·4 cells·complete=false, model_outputs_accessed=false | 잠금 metadata 대조이며 원문 독립 감사 아님 |
| <a id="QDR-D4"></a>QDR-D4 | 독립 참조와 fallback | [설계] | [계획](../../evidence/qd-real/analysis-plan.md), [feasibility gate](../../evidence/qd-real/feasibility-gate.md) | 제한된 5후보 검색에서 완전한 arbitrary-fact gold를 확인하지 못해 출력 전 독립 atomic-fact annotation 및 별도 검토를 선택. QA/RE 원 참조는 독립 anchor이나 전수 gold가 아님. 획득 전에 complete=false이므로 diagnostic-only, 과학 판정 INCONCLUSIVE | 전세계에 적절한 dataset이 없다는 주장 아님. AI 작성 gold는 누락·해석 오류·참조 유도 편향이 가능하며 fresh context가 인간 gold나 완전성을 보장하지 않음 |
| <a id="QDR-D5"></a>QDR-D5 | 표본·공개 경계 | [설계] | [계획](../../evidence/qd-real/analysis-plan.md), [downloads](../../evidence/qd-real/downloads.json) | SQuAD 첫 두 paragraph의 unchanged onto.units 첫4개씩, KLUE 첫4행 문장 각1개. 값·결과 기반 교체 없음. QA/RE metadata는 extractor에서 분리. 원 다운로드는 private 보존, 공개는 URL·해시·metadata | business DB·table join 평가 없음; 공개 dev의 pretraining 오염 여부 미상 |

## 후보별 채택·제외

| 후보·공식 출처 | 결정·이유 | 경계 |
|---|---|---|
| [SQuAD2](https://rajpurkar.github.io/SQuAD-explorer/) / [dev-v2.0.json](https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json) | 채택: 영어 문서와 독립 crowd QA, CC BY-SA 4.0, 고정 dev 다운로드 | 질문에 대한 답은 문서의 모든 명제를 열거하지 않음 |
| [KLUE RE](https://github.com/KLUE-benchmark/KLUE) / [고정 라이선스](https://raw.githubusercontent.com/KLUE-benchmark/KLUE/3efd98708a40ff49251fddde35453f8fbb11f536/License.md) / [dev JSON](https://raw.githubusercontent.com/KLUE-benchmark/KLUE/3efd98708a40ff49251fddde35453f8fbb11f536/klue_benchmark/klue-re-v1.1/klue-re-v1.1_dev.json) | 채택: 한국어 문장·entity span·관계 JSON, CC BY-SA 4.0 | 고정 관계 annotation은 임의 사실의 전수 gold 아님 |
| [DocRED](https://github.com/thunlp/DocRED) / [누락 annotation 연구](https://arxiv.org/abs/2205.12696) | 미채택: annotation 누락 보고로 완전 gold 요건 미충족 | 이번 bounded-search 판단 |
| [Re-DocRED](https://github.com/tonytan48/Re-DocRED) | 미채택: 수정 annotation도 고정 관계 어휘이며 repository MIT만으로 모든 임의 명제의 완전성을 확립하지 못함 | 라이선스와 completeness는 별도 질문 |
| [KorQuAD1 역사 공식 URL](https://korquad.github.io/KorQuad%201.0/) | 미채택: 이번 metadata 접근404, QA-only | dataset 부재나 사용 불가의 일반 주장 아님 |

다운로드 기록: SQuAD `2026-11-07T00:46:58.063636+00:00`, SHA256 `80a5225e94905956a6446d296ca1093975c4d3b3260f1d6c8f68bc2ab77182d8`; KLUE `2026-11-07T00:46:59.125285+00:00`, SHA256 `d150873430e592a5c569d35b20d88fbbbfba751dae0ffa4d8cbfb6b7321dea14`. 로컬 불변 발견·다운로드 원장은 위 링크에 있고 원문은 재배포하지 않는다.
