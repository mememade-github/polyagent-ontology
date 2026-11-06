# 온톨로지 뼈대의 출처

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

온톨로지의 구조가 어디서 오는지에 대한 기록이다. 초안 관찰의 내용은 Stub 스크립트가 쓴 것이다. 관련: [사람 승인](human-approval.md), [문서만 입력](document-only-input.md), [출력 제약](output-constraints.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-02](../contradictions.md#C-02) (대체 및 원인 불일치) 초안 완주 여부와 이전 실패 원인

## 초안 경로

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SK-01"></a>SK-01 | Stub 스크립트로 문서 소스 초안 경로 실행 | [실행/Stub] | I:26, E:rea/draft/stub5.py, E:rea/draft/out2.ndjson | `list_sources → read_text → put_items → check_draft → finish`를 SSE로 보냈다 | [C-02](../contradictions.md#C-02) |
| <a id="SK-02"></a>SK-02 | 초안 경로 완주 | [실행/Stub] | F:145, I:28, E:rea/draft/out2.ndjson | status `done`, 도구 5회, `ontology_toml`에 Customer·Promise·promised_to, `mappings_toml`에 `[extractions.calls]`, `bundle` null. findings.md의 "진입까지만"을 넘어선 기록이다. [C-02](../contradictions.md#C-02) **results.md 갱신:** 이후 승인과 번들까지 실행됐다([HA-10](human-approval.md#HA-10)) | 초안 내용은 Stub이 썼다. 모델이 이런 초안을 만들 수 있다는 근거가 아니다(I:29) |
| <a id="SK-03"></a>SK-03 | out2.ndjson에 나타난 항목 구조 | [실행/Stub] | E:rea/draft/out2.ndjson | 항목별 `status: proposed`, `rationale`, `serves`, `evidence_ids`, `basis`, `pending`이 있다. `evidence`는 `e1`, `e2`를 도구 요약으로 기록한다. `cq.CQ1`은 `draft.items`에만 있고 `ontology_toml`에는 없다 | 이 필드들의 의미와 강제 여부는 읽히지 않았다 |

## 코드가 막은 사례

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SK-04"></a>SK-04 | 소스 이름을 포함한 항목 이름 | [실행/Stub] | I:35 | `extraction.docs`가 `put_items` 거부, `leak`: "the name contains the source name `docs`", 초안 불변(기록만) | 보존된 out2.ndjson에 이 호출이 없다. [SYM-07](binary-symbols.md#SYM-07)과의 연결은 함수 이름 수준이다 |
| <a id="SK-05"></a>SK-05 | 문서 라우트 없이 `finish` | [실행/Stub] | I:36 | 거부 "document sets have no route or draft item to explain why"(기록만) | 보존된 out2.ndjson에 이 호출이 없다 |
| <a id="SK-06"></a>SK-06 | 잔여 호출 2회에서 예산 임박 안내 주입 | [실행/Stub] | I:37 | 사용자 메시지로 예산 임박 안내(기록만) | 보존 원시 기록 없음. 어느 임계에서 주입되는지 미확인이다 |

## 뼈대 출처

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SK-07"></a>SK-07 | Auto-Ontology 뼈대: DB 카탈로그 | [실행/Stub] | F:190, [AO-K2](../products/auto-ontology.md#AO-K2) | 제거 시 0(기록만) | 없음(이 입력에 한함) |
| <a id="SK-08"></a>SK-08 | Helix 추출 뼈대: 온톨로지 TOML | [실행/Stub] | F:190, E:helix/ontology_nokey.toml, E:helix/run_nokey.sh | `extract --ontology`로 파일을 준다. 실험에 쓴 파일은 acme에서 키를 제거한 것으로 기록됐다 | ~~"승인된" TOML로 실행한 기록이 없다. 초안에서 추출로 이어 실행한 기록도 없다. [HA-05](human-approval.md#HA-05)~~ → 번들 온톨로지로 Stub 실행이 있다([HA-13](human-approval.md#HA-13)). 사람이 승인한 TOML은 아니다 |
| <a id="SK-09"></a>SK-09 | RAGFlow 뼈대: 프롬프트 템플릿 | [코드] | F:190, RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:75-84 | JSON 형식과 인용 규칙을 지시하는 프롬프트 | 온톨로지 템플릿 미확인. [RF-03](../products/paper-ragflow.md#RF-03) |

## 논문의 Ontology 템플릿
| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SK-10"></a>SK-10 | "an Ontology template adds classes, properties, and constraints" | [논문] | P:§3.2 (p.txt:277) | 저자의 진술이다 | [RF-03](../products/paper-ragflow.md#RF-03) |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
- [C-20](../contradictions.md#C-20) (범위) "전 구간 연결"과 Foundry 경로
