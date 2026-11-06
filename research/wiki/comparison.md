# 세 시스템 항목별 현황

> 등급과 인용 표기는 [SCHEMA](SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

findings.md §4의 표를 칸 단위로 펼쳤다. 칸마다 입증 행으로 연결한다. 칸 사이 우열은 기록하지 않는다.

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](contradictions.md)에 있다.

- [C-02](contradictions.md#C-02) (대체 및 원인 불일치) 초안 완주 여부와 이전 실패 원인
- [C-08](contradictions.md#C-08) (표현 범위) Auto-Ontology "문서만으로 불가"

## 뼈대의 출처

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="CMP-1A"></a>CMP-1A | Auto-Ontology: DB 카탈로그 | [실행/Stub] | F:190, [SK-07](concepts/ontology-skeleton-source.md#SK-07) | [SK-07](concepts/ontology-skeleton-source.md#SK-07) | [SK-07](concepts/ontology-skeleton-source.md#SK-07) |
| <a id="CMP-1B"></a>CMP-1B | Helix: 승인된 온톨로지 TOML | [실행/Stub] | F:190, [SK-08](concepts/ontology-skeleton-source.md#SK-08) | [SK-08](concepts/ontology-skeleton-source.md#SK-08) | [SK-08](concepts/ontology-skeleton-source.md#SK-08) |
| <a id="CMP-1C"></a>CMP-1C | 논문/RAGFlow: 프롬프트 템플릿 | [코드] | F:190, [SK-09](concepts/ontology-skeleton-source.md#SK-09) | [SK-09](concepts/ontology-skeleton-source.md#SK-09) | [SK-09](concepts/ontology-skeleton-source.md#SK-09) |

## 긴 문서 처리

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="CMP-2A"></a>CMP-2A | Auto-Ontology: 해당 경로 없음 | [코드] | F:191, [AO-D4](products/auto-ontology.md#AO-D4), [AO-D6](products/auto-ontology.md#AO-D6) | [AO-D6](products/auto-ontology.md#AO-D6) | [AO-D6](products/auto-ontology.md#AO-D6) |
| <a id="CMP-2B"></a>CMP-2B | Helix: 엔티티 창 분할, 섹션 분할 | [실행/Stub] | F:191, [EW-02](concepts/entity-windows.md#EW-02), [EW-06](concepts/entity-windows.md#EW-06) | [EW-02](concepts/entity-windows.md#EW-02) | [EW-06](concepts/entity-windows.md#EW-06) |
| <a id="CMP-2C"></a>CMP-2C | 논문/RAGFlow: 청크 | [코드] | F:191, [RF-04](products/paper-ragflow.md#RF-04) | [RF-04](products/paper-ragflow.md#RF-04) | [RF-04](products/paper-ragflow.md#RF-04) |

## 임베딩 대상

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="CMP-3A"></a>CMP-3A | Auto-Ontology: 구조 노드 텍스트 | [코드] | [EM-01](concepts/embedding-targets.md#EM-01) | [EM-01](concepts/embedding-targets.md#EM-01) | [EM-01](concepts/embedding-targets.md#EM-01) |
| <a id="CMP-3B"></a>CMP-3B | Helix: 이 범위에서 미확인 | [미입증] | [EM-02](concepts/embedding-targets.md#EM-02) | [EM-02](concepts/embedding-targets.md#EM-02) | [EM-02](concepts/embedding-targets.md#EM-02) |
| <a id="CMP-3C"></a>CMP-3C | 논문/RAGFlow: claim 벡터 경로 존재 | [코드] | [EM-03](concepts/embedding-targets.md#EM-03) | [EM-03](concepts/embedding-targets.md#EM-03) | [EM-03](concepts/embedding-targets.md#EM-03) |

## LLM 출력 제약

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="CMP-4A"></a>CMP-4A | Auto-Ontology: 컬럼 허용 목록 | [실행/Stub] | [OC-01](concepts/output-constraints.md#OC-01) | [OC-01](concepts/output-constraints.md#OC-01) | [OC-01](concepts/output-constraints.md#OC-01) |
| <a id="CMP-4B"></a>CMP-4B | Helix: 스키마 enum + 타입 도메인 | [실행/Stub] | [OC-02](concepts/output-constraints.md#OC-02), [OC-03](concepts/output-constraints.md#OC-03) | [OC-02](concepts/output-constraints.md#OC-02), [OC-03](concepts/output-constraints.md#OC-03) | [OC-02](concepts/output-constraints.md#OC-02) |
| <a id="CMP-4C"></a>CMP-4C | 논문/RAGFlow: JSON 형식 | [코드] | [OC-04](concepts/output-constraints.md#OC-04) | [OC-04](concepts/output-constraints.md#OC-04) | [OC-04](concepts/output-constraints.md#OC-04) |

## 원문 대조

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="CMP-5A"></a>CMP-5A | Auto-Ontology: SQL을 카탈로그와 대조 | [실행/Stub] | F:194, [AO-12](products/auto-ontology.md#AO-12), [AO-A3](products/auto-ontology.md#AO-A3) | 문서 원문 대조가 아니라 카탈로그 대조이다 | [AO-K6](products/auto-ontology.md#AO-K6) |
| <a id="CMP-5B"></a>CMP-5B | Helix: 인용 원문 대조, 불일치 시 거부 | [실행/Stub] | F:194, [QV-01](concepts/quote-validation.md#QV-01)~[QV-13](concepts/quote-validation.md#QV-13) | [QV-14](concepts/quote-validation.md#QV-14) **results.md 갱신:** [QV-20](concepts/quote-validation.md#QV-20)~[QV-23](concepts/quote-validation.md#QV-23) | ~~[QV-P1](concepts/quote-validation.md#QV-P1)~~ → [QV-23](concepts/quote-validation.md#QV-23), [QV-20](concepts/quote-validation.md#QV-20) |
| <a id="CMP-5C"></a>CMP-5C | 논문/RAGFlow: 인용 원문 대조, 기본값은 claim 유지 | [실행] | F:194, [QV-R1](concepts/quote-validation.md#QV-R1)~[QV-R5](concepts/quote-validation.md#QV-R5) | [RF-02](products/paper-ragflow.md#RF-02) | [RF-02](products/paper-ragflow.md#RF-02) |

## 근거 위치

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="CMP-6A"></a>CMP-6A | Auto-Ontology: SQL·컬럼 ID·행 | [실행/Stub] | [ES-01](concepts/evidence-spans.md#ES-01) | [ES-01](concepts/evidence-spans.md#ES-01) | [ES-01](concepts/evidence-spans.md#ES-01) |
| <a id="CMP-6B"></a>CMP-6B | Helix: 섹션 + byte offset | [실행/Stub] | [ES-02](concepts/evidence-spans.md#ES-02), [ES-03](concepts/evidence-spans.md#ES-03) | [ES-02](concepts/evidence-spans.md#ES-02) | [ES-02](concepts/evidence-spans.md#ES-02) |
| <a id="CMP-6C"></a>CMP-6C | 논문/RAGFlow: chunk ID + offset | [실행] | [ES-04](concepts/evidence-spans.md#ES-04) | [ES-04](concepts/evidence-spans.md#ES-04) | [ES-04](concepts/evidence-spans.md#ES-04) |

## 2차 검증 모델

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="CMP-7A"></a>CMP-7A | Auto-Ontology: SQL 의도 검증 | [코드] | [SV-06](concepts/second-verifier.md#SV-06) | [SV-06](concepts/second-verifier.md#SV-06) | [SV-06](concepts/second-verifier.md#SV-06) |
| <a id="CMP-7B"></a>CMP-7B | Helix: 사실별 확률 | [실행/Stub] | [SV-07](concepts/second-verifier.md#SV-07) | [SV-07](concepts/second-verifier.md#SV-07) | [SV-07](concepts/second-verifier.md#SV-07) |
| <a id="CMP-7C"></a>CMP-7C | 논문/RAGFlow: 충분성 게이트 | [코드] | [SV-08](concepts/second-verifier.md#SV-08) | [SV-08](concepts/second-verifier.md#SV-08) | [SV-08](concepts/second-verifier.md#SV-08) |

## 사람 승인

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="CMP-8A"></a>CMP-8A | Auto-Ontology: 인증 플래그(답변 프롬프트 영향 없음) | [실행/Stub] | [HA-01](concepts/human-approval.md#HA-01) | [HA-01](concepts/human-approval.md#HA-01) | [HA-01](concepts/human-approval.md#HA-01) |
| <a id="CMP-8B"></a>CMP-8B | Helix: 초안 검토, review 판정 | [코드] | [HA-02](concepts/human-approval.md#HA-02), [HA-03](concepts/human-approval.md#HA-03) | [HA-03](concepts/human-approval.md#HA-03) **results.md 갱신:** [HA-10](concepts/human-approval.md#HA-10), [C-20](contradictions.md#C-20) | [HA-03](concepts/human-approval.md#HA-03) |
| <a id="CMP-8C"></a>CMP-8C | 논문/RAGFlow: 미확인 | [미입증] | [HA-04](concepts/human-approval.md#HA-04) | [HA-04](concepts/human-approval.md#HA-04) | [HA-04](concepts/human-approval.md#HA-04) |

## 문서만으로

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="CMP-9A"></a>CMP-9A | Auto-Ontology: 불가 | [실행/Stub] | [DO-01](concepts/document-only-input.md#DO-01) | [DO-01](concepts/document-only-input.md#DO-01) | [C-08](contradictions.md#C-08) |
| <a id="CMP-9B"></a>CMP-9B | Helix: 추출 가능, 초안은 진입까지 확인 | [실행/Stub] | [DO-02](concepts/document-only-input.md#DO-02), [DO-03](concepts/document-only-input.md#DO-03) | [DO-03](concepts/document-only-input.md#DO-03) **results.md 갱신:** [HA-13](concepts/human-approval.md#HA-13) | [C-02](contradictions.md#C-02) |
| <a id="CMP-9C"></a>CMP-9C | 논문/RAGFlow: claim 생성 가능, 온톨로지 템플릿 미확인 | [코드] | [DO-04](concepts/document-only-input.md#DO-04) | [DO-04](concepts/document-only-input.md#DO-04) | [DO-04](concepts/document-only-input.md#DO-04) |

---
[index](index.md) · [coverage](coverage.md) · [open items](open-items.md)
