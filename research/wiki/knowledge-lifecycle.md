# 지식의 추출·저장·사용과 품질 보장

> 등급과 인용 표기는 [SCHEMA](SCHEMA.md). 칸 사이 우열은 기록하지 않는다. `[실행/실모델]`은 `qwen2.5:3b`(Ollama 0.40.10, CPU) 실행이고 **문서 2건, 1~2회 관찰**이다. 평가 수치가 아니다. 스크립트에는 파생 모델 이름 `qwen3b-t8`만 있고(E:helix/grpc/go7.py), 원 모델과 Ollama 버전은 기록만이다. `num_ctx`는 행마다 적는다. RAGFlow 하니스는 `zap` 로그를 걸렀으므로 "오류 없음"은 반환값 수준의 관찰이다. 사용자가 구현 가능 여부를 물어 Query 결과로 남긴다.

관련: [C-24](contradictions.md#C-24), [C-25](contradictions.md#C-25), [C-26](contradictions.md#C-26), [추출 기법](extraction-techniques.md).

## 흐름

| ID | 시스템 | 단계 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|---|
| <a id="LC-01"></a>LC-01 | Helix | 추출 | [실행/실모델] | E:real-model/helix_docmd.out, E:helix/grpc/go7.py | gRPC `Extract`가 Ollama로 문서 → 엔티티 → 섹션별 링크 → 코드 검증 → 검증 모델을 수행 | 대량 문서 품질 |
| <a id="LC-02"></a>LC-02 | Helix | 저장 | [실행/실모델], [코드] | E:real-model/ask.out, E:helix/grpc/go9.py, HF:backend/pb/proto/ontology_agent/v1/agent.proto:96 | `Extract` 결과 집계 facts 1(`dry_run` false). 산출물 재전송 시 모델 호출 없이 replay한다는 것은 계약 설명이다 | DB를 다시 읽어 확인하지 않았다. 문서 단위 커밋은 계약 설명 수준. Foundry 저장소 경로 미실행 |
| <a id="LC-03"></a>LC-03 | Helix | 사용 | [실행/Stub], [실행/실모델] | E:helix/grpc/token_summary.json, E:helix/grpc/ask_ctx.out, E:real-model/ask.out | Stub: 도구 12개 루프, 첫 호출 메시지 4,772 + 도구 15,332토큰(cl100k), `context_tokens` 8000에서도 전송, `max_output_tokens` 1000이면 호출 0회로 `budget_exhausted`. 실모델(Ollama, 출력 4000): `context_tokens` 8192는 호출 0회로 `budget_exhausted`, 32768은 280초 `model_timeout`, 65536은 도구 호출까지 관찰하고 `ask.out`은 종료 줄 없이 끝난다(실험 명령의 `timeout 590`이 원인이라는 것은 기록만) | 실제 답변 품질, 인용 품질 |
| <a id="LC-04"></a>LC-04 | RAGFlow | 추출 | [실행/실모델] | E:real-model/rf_claims.out, E:real-model/rf_graph.out | `claim`, `structure` 함수를 Ollama로 실행. 청크는 하니스가 헤딩으로 나눔 | 실제 파서·청커, 전체 파이프라인 |
| <a id="LC-05"></a>LC-05 | RAGFlow | 저장 | [코드] | RF:internal/ingestion/component/knowledge_compiler/component.go:93, RF:internal/ingestion/knowledge_compile/consumer.go:1621, RF:internal/ingestion/knowledge_compile/writer.go:182 | 산출물을 청크 테이블 행으로 변환. 데이터셋 병합은 소문자 이름 버킷. Infinity, Elasticsearch만 dataset structure 지원. 배치 실패 시 Ack 안 함(consumer.go:289) | 실행 안 함 |
| <a id="LC-06"></a>LC-06 | RAGFlow | 사용 | [코드] | RF:internal/agentic_rag/agent.go:393, RF:internal/agentic_rag/compiled_evidence.go:596, RF:internal/agentic_rag/decision_filter.go:735 | 검색 → 앵커 10청크의 claim 페이지(판정 전 상한 기본 16) → 답변 → 검증 → 실패 시 도구 루프. 그래프 행은 `graph_explore` 도구로 읽힌다 | 패키지 빌드 실패(`office_oxide.h`)로 미실행 |
| <a id="LC-07"></a>LC-07 | Auto-Ontology | 전체 | [실행/Stub] 기록만, [코드] | [AO-02](products/auto-ontology.md#AO-02), [AO-03](products/auto-ontology.md#AO-03), AO:auto_ontology/retrieval/text_to_sql/text_to_sql_graph.py:82 | DB 카탈로그 기반. 문서 경로 없음. SQL 재구성 최대 7회는 [코드] | 원시 출력 없음. [DO-01](concepts/document-only-input.md#DO-01) |

## 코드가 보장하는 것과 하지 않는 것

| ID | 항목 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="LC-10"></a>LC-10 | Helix: 스키마 위반 | [실행/Stub] | E:helix/grpc/faults.out (`badenum`, `badid`) | 없는 링크, 없는 엔티티 ID는 rejected | 실제 모델의 스키마 준수율 |
| <a id="LC-11"></a>LC-11 | Helix: 속성값 형식 | [실행/실모델] | E:real-model/real_s8k.json | 날짜 속성에 `false`를 준 항목은 `invalid_value` reject | 값의 의미 |
| <a id="LC-12"></a>LC-12 | Helix: 인용은 실재하나 사실이 틀림 | [실행/Stub] | E:helix/grpc/faults.out (`falsefact`), E:helix/grpc/go1.py | 무관한 실제 문장 인용 + 검증 0.95면 dry-run 집계에 facts 1. 코드는 막지 않았다 | 실제 쓰기는 이 모드에서 하지 않았다. 실제 검증 모델의 판별력 |
| <a id="LC-13"></a>LC-13 | RAGFlow: 인용은 실재하나 claim이 틀림 | [실행/Stub] | E:ragflow/compile/rf_fault.out (T4, T5) | 거짓 claim + 실제 인용 유지. 1글자 인용 `a`도 통과. soft, hard 동일 | 실제 모델에서의 빈도 |
| <a id="LC-14"></a>LC-14 | 누락 탐지 | [실행/실모델] | E:real-model/helix.out, E:real-model/rf_claims.out | 두 시스템 모두 사실 누락을 오류로 처리하지 않았다 | 이 입력 밖의 동작 |

## 오류·성능 미달 시 동작

| ID | 상황 | 등급 | 인용 | Helix | RAGFlow structure | RAGFlow claim |
|---|---|---|---|---|---|---|
| <a id="LC-20"></a>LC-20 | JSON이 아닌 응답 | [실행/Stub] | E:helix/grpc/faults.out, E:ragflow/compile/rf_fault.out | 재시도 호출 없이 문서 `failed/malformed` | 6회 시도 후 문서 전체 오류 (S3, S6) | 6회 시도 후 배치만 건너뜀, 오류 없음 (T1) |
| <a id="LC-21"></a>LC-21 | 키 이름이 다른 JSON | [실행/Stub] | 위와 같음 | `failed/malformed` | 0행, 오류 없음 (S1). 최상위 배열은 원소 1개면 0행(S2a), 2개면 6회 후 오류(S2b) | 배치 건너뜀, 오류 없음 (T2) |
| <a id="LC-22"></a>LC-22 | 출력 한도로 잘린 JSON | [실행/Stub] | 위와 같음 | `failed/truncated`. `finish_reason`이 없으면 `failed/malformed` | 복구해 잘린 이름 `Jane Do` 저장 (S4) | 복구해 잘린 claim·인용 유지 (T3) |
| <a id="LC-23"></a>LC-23 | 컨텍스트 초과 오류 | [실행/Stub] | 위와 같음, RF:internal/common/retry.go:94 | `failed/context_too_long` | `status 400` 표기면 1회, 없으면 6회 후 문서 오류 (S7) | 배치 건너뜀 [코드] |
| <a id="LC-24"></a>LC-24 | 일부만 실패 | [실행/Stub] | 위와 같음 | 검증 호출 실패로 문서 전체 `failed`(`prose_verify`). 링크 일부 섹션만 실패하는 조건은 미시험 | 3배치 중 1개 실패에 0행 (S6) | 나머지 배치 유지 [코드, tree/claims.go:303] |
| <a id="LC-25"></a>LC-25 | 엔티티 성공 후 다음 단계 실패 | [실행/Stub] | E:helix/grpc/faults.out (`prose_link`, `link500`), E:ragflow/compile/rf_fault.out (S8) | 문서 `failed`, 엔티티 집계 0 | 성공한 엔티티까지 0행 | 해당 없음 |
| <a id="LC-26"></a>LC-26 | 서버 500 지속 | [실행/Stub] | E:helix/grpc/faults.out (`link500`) | 링크 호출 12회, 48.8초 후 `failed/unavailable` | 미실행 | 미실행 |
| <a id="LC-27"></a>LC-27 | 동명 다른 타입 | [실행/Stub] | E:ragflow/compile/rf_fault.out (S9), RF:internal/ingestion/component/knowledge_compiler/structure/merge.go:182 | 미실행 | `Mercury` 사람·회사가 1행, 첫 타입 유지 | 해당 없음 |
| <a id="LC-28"></a>LC-28 | 이름 변형 | [실행/Stub] | E:ragflow/compile/rf_fault.out (S9), [SV-13](concepts/second-verifier.md#SV-13) | 부분 일치는 unresolved | `Globex`, `Globex Inc`, `글로벡스` 3행 | 해당 없음 |
| <a id="LC-29"></a>LC-29 | 답변 검증 응답이 JSON 아님 | [코드] | RF:internal/agentic_rag/agent.go:1091,1231 | 해당 없음 | 해당 없음(claim 답변 경로) | `supported=true`로 답변 수락 |

## 컨텍스트 초과의 실제 동작

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="LC-30"></a>LC-30 | Helix + Ollama 사전 거부 | [실행] | E:helix/grpc/ollama_bound.out | `context_tokens` 8192: 15KB 호출, 25KB 이상 0초 `context_too_long`. 16384: 35KB 호출, 45KB 거부. 4096: 5KB 호출, 15KB 거부. 영어·한국어 같은 구간 | 정확한 임계값. 바이트 기준이라는 것은 관찰과 [R:57](sources/results.md)에 맞는 해석이다 |
| <a id="LC-31"></a>LC-31 | Helix + OpenAI 호환 | [실행/Stub] | E:helix/grpc/ctx_sweep.out, E:helix/grpc/token_summary.json | `context_tokens` 8000에서도 엔티티 호출 최대 21,727토큰 전송. 사전 거부 없음 | 실제 서버 동작 |
| <a id="LC-32"></a>LC-32 | Ollama 자체의 초과 처리 | [실행/실모델] | E:real-model/ov_direct.out | HTTP 200, 로그 `truncating input prompt limit=4098 prompt=11923 keep=4`. 응답이 시스템 지시(단어 하나로 답하라)를 따르지 않음. 오류 없음. `num_ctx` 8192 | 입력 원문은 기록만. 다른 버전 |
| <a id="LC-33"></a>LC-33 | RAGFlow + Ollama | [코드], [실행/실모델] | RF:conf/models/ollama.json, RF:internal/ingestion/component/knowledge_compiler/common/deps.go:16, E:real-model/default_ctx.out | `internal/`, `conf/`에 `num_ctx` 0건. 미지정 시 이 Ollama의 컨텍스트는 4096. RAGFlow는 모델 길이를 모를 때 8192를 쓴다 | RAGFlow 전체 경로 실행, 서버 환경 변수로 기본값을 바꾼 경우 |

## 실제 모델 관찰

정답지: E:real-model/gold.txt. 약속 4건, 함정 2건. RAGFlow 기본 템플릿에는 약속 타입이 없어 graph는 정답 4건과 직접 비교할 수 없다.

| ID | 경로 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="LC-40"></a>LC-40 | Helix, gold.md | [실행/실모델] | E:real-model/helix.out, E:real-model/real_gold.json | 엔티티 패스가 Customer 3개만 반환, Promise 0개. 링크 호출 0회, facts 0. 결과는 `done`, `ingested` | 다른 프롬프트·모델 |
| <a id="LC-41"></a>LC-41 | Helix, doc.md | [실행/실모델] | E:real-model/helix_docmd.out, E:real-model/real_s8k.json, E:real-model/ask.out, E:rea/quote/doc.md | 2회 모두 facts 1, rejected 2. reviews 1 → 3으로 실행마다 다름. 1회차 사실의 인용은 약속 문장과 일치하지만 주어 엔티티는 `Jane Doe`를 Promise 타입으로 둔 것이라 구조는 맞다고 볼 수 없다. 이 문서의 정답지는 없다 | 2회차 사실 내용 미기록 |
| <a id="LC-42"></a>LC-42 | RAGFlow claim, gold.md | [실행/실모델] | E:real-model/rf_claims.out | 4건 중 3건 존재, `10% 크레딧` 누락. 첫 배치가 출력 한도 1500(하니스 값)까지 반복 생성, 같은 인용의 유사 claim 12개, 잘린 JSON 수용. `Bob Lee` claim은 `재발급 기간`으로 변형되고 근거 제거 후 유지. 함정 2건은 부정문 그대로 | 다른 출력 한도 |
| <a id="LC-43"></a>LC-43 | RAGFlow graph, gold.md | [실행/실모델] | E:real-model/rf_graph.out | 4행. Globex, Initech 없음. `후리`를 person으로, 원문에 없는 `Bob Lee caused_by 후리` 저장. 오류 없음 | 다른 템플릿 |
| <a id="LC-44"></a>LC-44 | 속도 | [실행/실모델] | E:real-model/ov_direct.out, E:real-model/helix_docmd.out | 다른 프로세스와 CPU를 공유한 환경에서 3섹션 문서 204초. `ov_direct.out` 호출은 생성 2.05 t/s, 프롬프트 23.6 t/s. 다른 시점의 짧은 호출 9–13 t/s와 41 t/s는 기록만이다. 시점에 따라 크게 달랐다 | 다른 하드웨어. 부하 조건 미기록 |
| <a id="LC-45"></a>LC-45 | 시간 상한 | [코드], [실행] 기록만 | HF:backend/config/config.go:478,509, RF:internal/agentic_rag/agent.go:906 | Foundry 설정은 `Ask` 300초 이상을 거부. 에이전트가 600초 요청을 `more than 299`로 거부한 것은 기록만. RAGFlow claim 답변 경로 기본 90초 | 없음 |

---
[index](index.md) · [open items](open-items.md)
