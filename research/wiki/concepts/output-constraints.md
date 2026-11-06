# LLM 출력 제약

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

모델 출력을 코드가 어디서 제한하는지의 기록이다. 관련: [판정](second-verifier.md), [Auto-Ontology](../products/auto-ontology.md), [Helix](../products/helix-foundry.md).

## 출력 제약

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="OC-01"></a>OC-01 | Auto-Ontology: 컬럼 허용 목록 | [실행/Stub] | F:193, [AO-07](../products/auto-ontology.md#AO-07), [AO-K1](../products/auto-ontology.md#AO-K1) | 허용 목록 제거 비교(기록만) | 실제 모델 출력에서의 위반 빈도는 측정되지 않았다 |
| <a id="OC-02"></a>OC-02 | Helix: 스키마 enum이 링크 이름과 엔티티 ID를 제한 | [실행/Stub] | F:139, E:helix/stub2.py | 캡처한 `output_config.format.schema`가 근거로 기록됐다. 보존 stub은 `claim`의 enum을 읽는다 | 링크 이름·엔티티 ID enum을 보여 주는 캡처 원본은 없다(기록만). enum을 지키지 않는 응답의 처리는 시험되지 않았다 |
| <a id="OC-03"></a>OC-03 | Helix: 타입 도메인 | [실행/Stub] | F:193, [SV-05](second-verifier.md#SV-05) | `domain_range_mismatch` 거부 | [SV-05](second-verifier.md#SV-05) |
| <a id="OC-04"></a>OC-04 | RAGFlow: JSON 형식 | [코드] | F:193, RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:75-76 | "Reply with a single JSON object" | 실제 모델의 준수와 파싱 실패 처리는 실행되지 않았다 |

## 초안 단계 게이트

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="OC-05"></a>OC-05 | 초안 단계의 코드 거부 | [실행/Stub] | I:35, I:36, [SK-04](ontology-skeleton-source.md#SK-04), [SK-05](ontology-skeleton-source.md#SK-05) | 두 사례가 기록됐다 | 전체 정책 목록은 미확인이다. [SYM-09](binary-symbols.md#SYM-09) |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
