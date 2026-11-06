# 컨텍스트 크기와 토큰 측정

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

10k 대비 칸은 요청 크기 비교이다. 수행 능력 측정이 아니다. 측정 범위가 행마다 같다고 입증되지 않았다([C-07](../contradictions.md#C-07)). 관련: [엔티티 창](entity-windows.md), [심볼](binary-symbols.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-03](../contradictions.md#C-03) (세분) 엔티티 창과 `--max-section-bytes`
- [C-07](../contradictions.md#C-07) (측정 범위 불일치) 토큰 측정 범위
- [C-12](../contradictions.md#C-12) (재현 근거 공백) "evidence/에 스크립트와 입력이 있다"
- [C-14](../contradictions.md#C-14) (세분) `extract`의 프로바이더
- [C-15](../contradictions.md#C-15) (추가) `context_tokens` 동작

## 호출별 토큰

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="TK-01"></a>TK-01 | Helix 초안 첫 호출, 짧은 문서 1건 | [실행/Stub] | F:204, E:helix/stub4.py, E:helix/turn_a.json | 32,743(메시지 21,510 + 도구 11,233), 10k 초과(기록만) | 요청 캡처 원본 없음. 이후 호출의 크기는 기록되지 않았다 |
| <a id="TK-02"></a>TK-02 | Helix 엔티티 패스, 짧은 문서 | [실행/Stub] | F:205 | 739–833, 이내(기록만) | 측정 범위(스키마 포함 여부) 미기록. [C-07](../contradictions.md#C-07) |
| <a id="TK-03"></a>TK-03 | Helix 엔티티 패스, 138KB 헤딩 문서 3회 | [실행/Stub] | F:206, E:helix/mkdocs.py | 12,892–14,931, 초과(기록만). mkdocs.py 생성식 재계산 138,475바이트 | 측정 범위 미기록. [C-07](../contradictions.md#C-07) |
| <a id="TK-04"></a>TK-04 | Helix 엔티티 패스, 246KB 한국어 무헤딩 5회 | [실행/Stub] | F:207, E:helix/mkdocs.py | 18,756, 초과(기록만). 재계산 245,850바이트 | 측정 범위 미기록. [C-07](../contradictions.md#C-07) |
| <a id="TK-05"></a>TK-05 | Helix 엔티티 패스, 246KB 한국어 단일 문단 6회 | [실행/Stub] | F:208, E:helix/mkdocs.py | 4,403–18,040, 초과 포함(기록만). 재계산 245,830바이트 | 단일 문단의 분할 방식 미확인. [OP-H1](../open-items.md#OP-H1) |
| <a id="TK-06"></a>TK-06 | Helix 링크 패스, 긴 문서들 41–70회 | [실행/Stub] | F:209 | 819–2,266, 이내(기록만) | 측정 범위 미기록 |
| <a id="TK-07"></a>TK-07 | Helix 검증 패스, 긴 문서 40회 | [실행/Stub] | F:210 | 1,897–1,943, 이내(기록만) | 측정 범위 미기록 |
| <a id="TK-08"></a>TK-08 | AO SQL 생성, 4테이블 DB | [실행/Stub] | F:211, E:ao/seed.py | 3,318, 이내(기록만) | 다른 답변 노드의 토큰은 기록되지 않았다 |
| <a id="TK-09"></a>TK-09 | AO 문서 테이블 컬럼 설명, 본문 2건 | [실행/Stub] | F:212, [AO-D4](../products/auto-ontology.md#AO-D4) | 17,773, 초과(기록만) | [AO-D4](../products/auto-ontology.md#AO-D4) |
| <a id="TK-10"></a>TK-10 | RAGFlow claim 추출 | [미입증] | F:213 | 미측정 | 직접 근거 없음 |

## 프로바이더와 컨텍스트

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="TK-11"></a>TK-11 | `extract` CLI는 Anthropic 전용으로 표기, 계약 스키마는 Ollama와 OpenAI 호환 선언, ~~gRPC Extract 미실행~~ → gRPC Extract를 OpenAI 호환과 Ollama로 실행했다([C-24](../contradictions.md#C-24)) | [코드] | F:216, HF:backend/pb/proto/ontology_agent/v1/schema/turn_request.json:916,939, [SYM-05](binary-symbols.md#SYM-05) | 스키마의 `ollama`, `openai_compatible` 일치. `--help` 원본 없음(기록만). [C-14](../contradictions.md#C-14) | 비 Anthropic 경로로 추출을 실행한 기록이 없다 **results.md 갱신:** R:88에도 변화 없음([M-25](../method-and-limits.md#M-25)) |
| <a id="TK-12"></a>TK-12 | `context_tokens=8000`이어도 같은 크기 요청 전송 | [실행/Stub] | F:217, E:helix/turn_a.json, E:helix/turn_b.json | 두 turn 입력의 차이는 `context_tokens`이다. 요청 크기 비교 기록은 findings.md에만 있다(기록만). [C-15](../contradictions.md#C-15) | `context_tokens`의 코드 의미는 미확인이다 |
| <a id="TK-13"></a>TK-13 | Ollama 최소 컨텍스트 65,536 | [코드] | F:121, F:217, HF:backend/ai/validate.go:34,85, HF:backend/ai/deployment.go:18 | `MinContextTokens = 65536`, 미만 거부 분기, `DefaultContextTokens = 65536` | 실제 Ollama로 실행하지 않았다 |
| <a id="TK-14"></a>TK-14 | 보고된 사용량 7000/8000/9000과 턴 지속 | [실행/Stub] | I:41, E:rea/draft/t8k.json, E:rea/draft/stub5.py | `context_tokens=8000`에서 3회 모두 status `done`, 모델 호출 5회(기록만). 보존된 out2.ndjson은 `usage.input` 1–5인 별개 실행이다. [C-15](../contradictions.md#C-15) | ~~`Budget`의 동작은 디컴파일 전이라 미확인. 이 범위 밖에서 멈추는지도 미확인이다~~ → `Budget` 함수의 해석은 [TK-16](#TK-16), [TK-17](#TK-17). 서버 400에서 멈춤은 [TK-19](#TK-19). `context_tokens`의 의미는 미확인 |

## 품질

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="TK-15"></a>TK-15 | 저성능 모델의 추출·판정 품질 | [미입증] | F:218, F:26 | 측정하지 않았다 | 직접 근거 없음 |

## results.md: 컨텍스트 제한

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="TK-16"></a>TK-16 | `Budget::exhausted` | [디컴파일] | R:56, E:rea/decompiled/ontology-agent/b_exhausted.c | 정수 비교 1개, 스케일한 실수 비교 1개, `Instant::elapsed` 비교 1개가 있고 토큰 관련 호출은 이 함수에 없다. "스텝, 비용, 시간"은 필드 이름이 없는 오프셋의 해석이다 | 다른 함수의 토큰 처리까지 부정하지 않는다 |
| <a id="TK-17"></a>TK-17 | `Budget::prompt_bound` | [디컴파일] | R:57, E:rea/decompiled/ontology-agent/b_prompt_bound.c | `Request::body` 길이에서 값을 빼고 2로 나눈 올림을 계산한다. 뺄셈은 첫 필드의 하위 비트가 1일 때만 일어나며, R:57에는 이 조건이 없다 | 사용처 미확인(R:57) |
| <a id="TK-18"></a>TK-18 | `ModelSpec::settle`의 0x10000 | [디컴파일] | R:58, E:rea/decompiled/ontology-agent/m_settle.c, HF:backend/ai/validate.go:34,85 | `llm::wire::ollama` 타입을 쓰는 함수이다. 기존 값이 0일 때 0x10000을 쓰고, 모델 정보 값이 0이 아니고 더 작으면 그 값으로 줄인다 | Go 쪽 65,536 하한과의 관계 미확인. 기존 값이 `context_tokens`인지도 미확인이다. [C-21](../contradictions.md#C-21) |
| <a id="TK-19"></a>TK-19 | 서버 400 `context_length_exceeded` 처리 | [실행/Stub] | R:59, E:rea/approval/over.out, E:rea/approval/stub_over.py | 경고 "the model call failed: context_too_long (HTTP 400, context_length_exceeded)"와 "the conversation is too long for the model; `continue` resumes in a fresh one", status `budget_exhausted` | "호출 1회"는 기록만이다(로그 없음). 실제 서버의 오류 형식과 같은지 미확인이다 |
| <a id="TK-20"></a>TK-20 | 초안 시스템 메시지 크기 | [실행/Stub] | R:60, E:rea/approval/sys.txt | 73,350자로 일치(73,618바이트) | 토큰 수는 이 행에 없다. 전체 요청 크기는 [TK-01](#TK-01) |
| <a id="TK-21"></a>TK-21 | `continue`의 새 대화 크기 | [미입증] | R:60 | 측정하지 않았다고 기록됐다 | 직접 근거 없음 |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
- [C-21](../contradictions.md#C-21) (관계 미확인) 최소 컨텍스트와 `settle`
