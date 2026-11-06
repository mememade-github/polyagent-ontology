# arXiv 2610.41172와 RAGFlow

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

논문 진술과 RAGFlow 코드를 나눠 적는다. `claims.go` 경로 접두어는 `internal/ingestion/component/knowledge_compiler/`이다(F:172). 관련 개념: [인용 대조](../concepts/quote-validation.md), [근거 위치](../concepts/evidence-spans.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-10](../contradictions.md#C-10) (논문과 코드 불일치) RAGFlow: 저장 규칙, exact, 온톨로지 템플릿

## 논문의 진술

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="PA-01"></a>PA-01 | 지식 컴파일 정의 κ: D→A, span으로의 lineage | [논문] | F:153, P:§3.1 식(1) (p.txt:227-230) | 문장 일치 | 저자의 정의이다 |
| <a id="PA-02"></a>PA-02 | Parse·Chunk·Enrich·Validate·Assemble·Register 6단계 | [논문] | F:154, P:§3.2 (p.txt:251-273) | 문장 일치 | 6단계 전체가 저장소의 한 경로로 이어지는지는 확인되지 않았다 |
| <a id="PA-03"></a>PA-03 | "청크는 recall 단위이지 의미 단위가 아니다" | [논문] | F:155, P:§3.2 (p.txt:248-249) | "The chunk is a unit of recall, not a unit of meaning" | 저자의 진술이다 |
| <a id="PA-04"></a>PA-04 | claim-evidence 단위 ⟨c,e,s,τ⟩ | [논문] | F:156, P:§4.1 식(2) (p.txt:326) | 문장 일치 | 코드 구조체와 필드 단위 대조는 없다 |
| <a id="PA-05"></a>PA-05 | "model may propose, but the source disposes", 작은 추출기 glm-4-flash | [논문] | F:157, P:§4.2 (p.txt:441-444) | 문장 일치. 같은 절이 "exact presence"라고 쓴다. [C-10](../contradictions.md#C-10) | 저자 실험의 재현 없음. 이 위키의 어느 실험도 glm-4-flash를 쓰지 않았다 |
| <a id="PA-06"></a>PA-06 | 원본/파생 채널 분리 | [논문] | F:158, P:§3.4 (p.txt:304-311) | 문장 일치 | 코드 대조 없음 |
| <a id="PA-07"></a>PA-07 | 토큰 −91%/+1.9%/평균 −38%, 손익분기 2%(유한 배치에서는 식 9) | [논문] | F:159, P:§4.4 (p.txt:486-492, 543-547) | 문장 일치 | 재현 없음. FRAMES 측정값이며 일반 문서나 로컬 모델 측정이 아니다 |
| <a id="PA-08"></a>PA-08 | 온톨로지: 타입 지정·추출 제약·소스 간 연결, FRAMES 미측정 | [논문] | F:160, P:§5.2 (p.txt:604-608), Table 1 (p.txt:391-393) | Table 1의 FRAMES 결과가 "not measured"이다 | 온톨로지 산출물의 효과는 논문 안에서도 측정되지 않았다 |
| <a id="PA-09"></a>PA-09 | 배포 장부 관측치 없음 | [논문] | F:161, P:§5.3 (p.txt:636-643) | "The ledger in Table 2 currently has no observations in it" | 저자가 명시한 공백이다 |
| <a id="PA-10"></a>PA-10 | 구조 산출물의 정확도 이득 미검출 | [논문] | F:162, P:§3.5 (p.txt:312-317), §8.2 (p.txt:909-916) | 문장 일치 | 단일 실행 기준 진술이다(§8.2) |

## 논문의 진술
| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="PA-11"></a>PA-11 | Validate 단계의 처리: "Invalid units are dropped, not repaired by the model" | [논문] | P:§3.2 (p.txt:264-266) | findings.md에 직접 언급되지 않은 §3.2 문장이다 | [RF-02](#RF-02)의 기본 동작과 대조 |

## 코드 대조

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="RF-01"></a>RF-01 | claim과 verbatim span | [코드] | F:168, F:172, RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:80,513 | 프롬프트 규칙 "CONTIGUOUS verbatim substring", `LocateEvidence`. 논문과 일치로 기록 | 실제 모델이 이 규칙을 지키는지는 측정되지 않았다 |
| <a id="RF-02"></a>RF-02 | "locatable span 없는 claim은 저장 안 함"(§4.1)과 코드 기본값 | [코드] | F:169, P:§4.1 (p.txt:406-407), RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:31,38,445-448,463 | 기본값 soft이고 근거 실패 claim을 유지한다. hard도 근거 필드 없는 claim을 유지한다. [C-10](../contradictions.md#C-10) | 실행 결과는 [QV-R1](../concepts/quote-validation.md#QV-R1)~[QV-R5](../concepts/quote-validation.md#QV-R5). 배포에서 어느 모드가 쓰이는지는 확인되지 않았다 |
| <a id="RF-03"></a>RF-03 | 온톨로지 템플릿(§3.2, Fig.1) | [미입증] | F:170, P:§3.2 (p.txt:277), Fig.1 (p.txt:349), RF:internal/agentic_rag/tool_navigate_structure.go:801 | 컴파일러 디렉터리는 `mindmap`, `structure`, `tree`, `wiki`와 `common`이다. grep 재실행: `ontolog` 일치 3개 파일(`tool_navigate_structure.go`, `tool_search_semantic_chunks.go`, `docs/basics/agent_native_database.md`). [C-10](../contradictions.md#C-10) | 템플릿이 공개 저장소 밖에 있는지 없는지는 미확인이다 |

## 배치

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="RF-04"></a>RF-04 | 4청크 배치, 초과 청크 미분할 | [코드] | F:174, RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:21, RF:internal/ingestion/component/knowledge_compiler/common/batch_packing.go:5,7 | `claimBatchSize = 4`, "a single chunk is NEVER split" | 실제 LLM 호출 토큰은 측정되지 않았다([TK-10](../concepts/context-budget.md#TK-10)) |
| <a id="RF-05"></a>RF-05 | 검증기 함수를 복사해 실행, 저장소 테스트는 빌드 실패 | [실행] | F:176, E:ragflow/validator_copy.go | 복사본 세 함수가 업스트림 `claims.go`와 공백 정규화 비교로 일치함을 이 세션에서 확인했다. 모델 없는 실행이다. 출력은 evidence/에 없다(기록만) | 빌드 실패 로그가 없다. 함수 단위 실행이라 파이프라인 동작을 뜻하지 않는다 |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
