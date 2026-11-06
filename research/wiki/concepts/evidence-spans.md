# 근거 위치 (evidence spans)

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

시스템마다 "근거"가 가리키는 대상이 다르다. 관련: [인용 대조](quote-validation.md), [Helix](../products/helix-foundry.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-16](../contradictions.md#C-16) (미확정) Helix 인용 대조 메커니즘

## 시스템별 근거 위치

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="ES-01"></a>ES-01 | Auto-Ontology의 근거 위치: SQL·컬럼 ID·행 | [실행/Stub] | F:195, [AO-R6](../products/auto-ontology.md#AO-R6) | DB 값 근거이다(기록만) | 문서 범위의 span이 없다. [AO-D6](../products/auto-ontology.md#AO-D6) |
| <a id="ES-02"></a>ES-02 | Helix: 수락된 사실의 `span {section:1, start:26, end:71}` | [실행/Stub] | F:138, E:helix/report3.raw | 일치. `review`와 `refuted`에도 span이 있고 `reject`에는 없다 | ~~span이 원문에 항상 정확히 맞는지는 [QV-05](quote-validation.md#QV-05)가 반례 후보로 남긴다~~ → 퍼지 창 span은 인용보다 넓을 수 있다는 관찰과 해석이 있다([QV-05](quote-validation.md#QV-05), [QV-28](quote-validation.md#QV-28)) |
| <a id="ES-03"></a>ES-03 | 인용 범위 타입(section, byte offset) | [코드] | F:119, HF:backend/ontologyagent/ask.go:443 | `QuoteTarget{DocID, Section, Start, End}` | Foundry 질의 경로에서의 실행 관찰 없음 |
| <a id="ES-04"></a>ES-04 | RAGFlow: chunk ID + offset | [실행] | F:195, E:ragflow/validator_copy.go | `EvidenceRef{Quote, ChunkID, Start, End}` | 파이프라인 저장 경로의 실행 관찰 없음 |

## 시스템별 근거 위치
| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="ES-05"></a>ES-05 | 논문의 단위와 offset 기록 | [논문] | P:§4.2 (p.txt:445), §3.2 (p.txt:271-273) | 검증이 offset을 기록하고, Register가 source version, offsets 등을 저장한다고 쓴다 | Register 항목 전체와 코드의 대조는 없다 |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
