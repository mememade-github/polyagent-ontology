# QD 실제 결과: INCONCLUSIVE

[index](../index.md) · [전체 보고서](../../evidence/qd-real/results.md) · [자료·라이선스](qd-real-data.md) · [동결 절차](qd-real-procedure.md) · [소스 원장](../sources/qd-real.md)

공개 집계 metadata만 읽어 작성했다. private corpus/gold/labels/response 원문은 읽지 않았다. 독립 manuscript 검토는 보고서만 받았으며 필수 표현 수정1건의 종결을 확인했다. 원자료·코드 감사가 아니다. 보고서 초고의 pending 표시는 당시 기록이며 [검증 기록](../../evidence/qd-real/verification.json)이 후속 상태를 남긴다. 최종 격리 평가·등록 결과는 별도 최종 보고와 Git 기록으로 확인한다.

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QDR-R1"></a>QDR-R1 | 과학 판정 | [실행/실모델] | [결과](../../evidence/qd-real/results.json), [보고서](../../evidence/qd-real/results.md) | Hq-Fact/Hq-original/Honto 모두 INCONCLUSIVE. 15 arms+pre/post 획득 완료와 과학 유효성은 별개 | 과학 PASS/FAIL 아님 |
| <a id="QDR-R2"></a>QDR-R2 | gold·통제 한계 | [실행/실모델] | [gold review](../../evidence/qd-real/gold-review-summary.json), [측정](../../evidence/qd-real/measurements.json) | 출력 전 gold85·미해결6·complete=false. pre/post 각4/12 통제 실패: 한국어 positive verify·두 extraction pipeline, 영어 role reversal negative | 원인 추가 추정 없음; 완전 gold 아님 |
| <a id="QDR-R3"></a>QDR-R3 | 미해결 예측 | [실행/실모델] | [judge](../../evidence/qd-real/judgment-summary.json), [15행 품질표](../../evidence/qd-real/results.md) | locked gold에 없는 unique1이 ambiguous, Fact 두 selector×3seed의6occurrences. 각 T0/F0/U1, precision N/A. JSON0은 empty-resolved-label sentinel | ambiguous는 참·거짓 미확정; 0% 품질 주장 금지 |
| <a id="QDR-R4"></a>QDR-R4 | 빈 arm·cell | [실행/실모델] | [결과](../../evidence/qd-real/results.json), [보고서](../../evidence/qd-real/results.md) | onto와 original 두 selector 모두 active0; 명시 empty rule precision0. 전 arm correct cells0/4는 confirmed only | 최종 recall 미확립 |
| <a id="QDR-R5"></a>QDR-R5 | selector 해석 | [실행/실모델] | [최종 절차](../../evidence/qd-real/procedure-final.json), [결과](../../evidence/qd-real/results.json) | 모든 pool exhausted, selector active output 동일; contrast uninformative | pooled winner·일반 QD 이익/무이익·ontology 결론 없음 |
| <a id="QDR-R6"></a>QDR-R6 | 자원 | [실행/실모델] | [측정](../../evidence/qd-real/measurements.json), [15행 자원표](../../evidence/qd-real/results.md) | controls 포함276calls, input47413/output6929/total54342; whole595.062946s, summed server561.10463739s | server duration은 CPU time 아님; 같은 cap은 같은 소비 아님 |
| <a id="QDR-R7"></a>QDR-R7 | accounting·cleanup | [실행] | [측정](../../evidence/qd-real/measurements.json), [audit](../../evidence/qd-real/docker-audit.json) | prompt max364, reserved max2406; 전체 stopped container log truncating0, chat276=측정276; container removed | 문서 역할의 raw log 재감사 아님 |
| <a id="QDR-R8"></a>QDR-R8 | 동결·one-shot | [기록] | [절차](../../evidence/qd-real/procedure-final.json), [계획](../../evidence/qd-real/analysis-plan.md) | synthetic-only tuning, model prompt tuning0; fixed public dev12/eligible7/deferred5; 단일 matrix, rerun0·response 재사용 없음. 14locks 검증 기록 | pretraining contamination 불명; private artifact 독립 감사 아님 |
| <a id="QDR-R9"></a>QDR-R9 | 불변 판정 기준 | [설계] | [계획](../../evidence/qd-real/analysis-plan.md), [기존 절차](qd-real-procedure.md#QDR-P4) | precision≥90% 및 nondecrease, gain≥max(1,ceil(.10×comparator T)), cell nondecrease 유지. hard64calls/64000tokens/900s, operational24, global1800s 이내 기록 | 데이터 기반 threshold 조정 없음; invalidity를 threshold로 복구 불가 |

judge 입력은 judgment-summary의 해시와 일치하는 `judge-units.json`이다. final procedure의 한 narrative 철자는 입력 변경을 뜻하지 않는다. 모든 15개 seed/arm의 active/T/F/U/P/cells 및 실제 calls/tokens/wall은 [전체 보고서](../../evidence/qd-real/results.md)에 있다. 고정 full plan SHA256·자료 URL/download SHA·private artifact hash의 기록 위치는 [원장](../sources/qd-real.md)을 따른다. 원문 dataset/gold/prediction은 공개하지 않는다.

**results.md 갱신:** 원고만 읽은 독립 검토가 미해결 예측을 “거짓이 아니다”로 단정한 영문 1곳을 지적했다. “참·거짓 어느 쪽도 확정되지 않았다”로 명확히 했으며 수치·정답·판정·실행은 바꾸지 않았다. [검토와 반영 기록](../../evidence/qd-real/review-summary.json). 이 검토는 원자료·코드 감사가 아니다.
