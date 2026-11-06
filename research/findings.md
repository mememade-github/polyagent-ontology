# 문서 → 온톨로지 자동화 참고 시스템: 실제 형상 (As-Is)

향후 계획과 권고는 포함하지 않는다. 측정일 2026-11-06.

## 0. 판정 방법

| 항목 | 규칙 |
|---|---|
| 누락 방지 | 프로젝트 자신의 선언을 전수 나열한다: README 주장, 컴파일 단계, 답변 그래프 노드, 패스 |
| 핵심 판정 | 해당 메커니즘만 제거하거나 오류를 주입했을 때 출력이 달라지면 핵심이다. 차이가 없으면 핵심이 아니라고 기록한다 |
| 근거 등급 | **[실행]** 실제 코드/바이너리를 돌려 관찰. **[코드]** 소스만 읽음. **[논문]** 저자의 진술 |

### 대상 버전

| 대상 | 버전 |
|---|---|
| NVIDIA/auto-ontology | `c4495670` |
| HelixDB/helix-foundry | `c7de4051` |
| ontology-agent 이미지 | `latest`, revision `9e1b6284`, 계약 4.7.0 (저장소 `contract.go:21`과 일치) |
| ontology-agent 이미지 (대조) | `0.1.0`, revision `e1e5a083`, 계약 4.1.1 (`local/compose.yaml:26`의 기본값) |
| infiniflow/ragflow | `2096707f` |
| 논문 | arXiv 2610.41172 (2026-10-30), Context as Infrastructure |

### 실험 공통 한계

- 모델은 전부 **Stub**이다. 코드가 프롬프트로 무엇을 보내고 응답을 어떻게 처리하는지만 증명한다. **추출 품질과 저성능 로컬 모델의 수행 능력은 측정하지 않았다.**
- Stub의 SQL은 고정값이다. 따라서 K3/K4에서 변한 것은 모델 입력이고, SQL 결과 변화는 관찰할 수 없다.
- 토큰 수는 `tiktoken cl100k_base` 기준이다. 실제 로컬 모델의 토크나이저와 다를 수 있다.

## 1. NVIDIA Auto-Ontology

### 실제 구조

DB 카탈로그가 뼈대이고, LLM은 이름과 설명을 붙이며, 임베딩 대상은 문서 청크가 아니라 구조 노드이다.

```
SQL 커넥터 → 카탈로그(Table/Column/PK/FK) → 테이블별 Term + ColumnAttribute
           → 의미 FK → SqlAttribute(쿼리 이력) → 브리지 테이블 → pgvector
질문 → 의도 → 엔티티 추출 → 후보 검색 → SQL 생성 → 카탈로그 검증 → DB 실행 → 응답
```

### 출처

| 개념 | 위치 |
|---|---|
| 카탈로그 추출 | `auto_ontology/catalog/extract.py:89-94`, `ingestion_service/ingest.py:110` |
| 컴파일 4단계 | `semantic/compile.py:64,91,99,105` |
| 컬럼 없는 테이블 건너뜀 | `semantic/pipeline.py:186` |
| Term 추출과 허용 목록 | `semantic/term_extractor.py:134,141,186`, 폴백 `:109` |
| 2차 컬럼 필터 | `semantic/visit_enter.py:129` |
| 스키마 | `dal/schema.py:456,487,576,599` |
| 임베딩 텍스트 | `semantic/embed.py:215,247` |
| 커버리지 | `retrieval/entity_coverage/agents/coverage.py:60`, 거리 임계값 `state.py:17` |
| SQL 카탈로그 검증 | `retrieval/text_to_sql/agents/sql_parse_validation.py:961,971` |
| 답변 그래프 | `retrieval/text_to_sql/text_to_sql_graph.py:447-463` |
| MCP 허용 목록 | `mcp/auto_ontology_mcp/tools.py:161`, 읽기 전용 선언 `AGENTS.md:60` |

### Knockout 결과 [실행]

| 실험 | terms | attrs | sem_fk | 의미 벡터 | 관찰 |
|---|---:|---:|---:|---:|---|
| 기준 | 4 | 12 | 2 | 16 | |
| K2 카탈로그 제거 | 0 | 0 | 0 | 0 | 전체 소멸 |
| K1 sanitizer 제거 | 4 | 8 | 0 | 12 | 유령 컬럼은 2차 필터가 막음. 누락 컬럼 손실 |
| K1b 1·2차 필터 모두 제거 | 4 | 8 | 0 | 0 | 유령 컬럼 저장 0건. compiled_tables=0 |
| K3 의미 FK 제거 | 4 | 12 | 0 | 16 | SQL 프롬프트 9,113→8,700자 |
| K4 Term 임베딩 제거 | 4 | 12 | 2 | 0 | "Semantic match" 3→0줄, 프롬프트 7,498자 |
| K5 Term LLM 응답 없음 | 4 | 12 | 2 | 16 | 폴백으로 동일 개수 생성, 프롬프트 10,113자 |
| K6 SQL 카탈로그 검증 제거 | - | - | - | - | 유령 SQL이 DB까지 도달한 뒤 실행 실패로 재생성 |
| A3 검증 유지 | - | - | - | - | 유령 SQL이 DB 실행 전 `reconstruct_sql`로 전환 |

### README 주장 전수 대조

| 주장 | 상태 |
|---|---|
| 메타데이터에서 온톨로지 생성 | [실행] 확인 |
| 기존 온톨로지/시맨틱 모델 연결 (Ossie) | [코드] 존재, 미실행 |
| 시스템 간 정의 조정 | 미확인 |
| Agent에 의미 제공 | [실행] 확인 |
| 인증 정의로 쿼리 검증 | [실행] **코드와 불일치.** 인증 값을 3회씩 교차 변경해도 SQL 프롬프트 해시 동일. `retrieval/`에서 `certif`는 `literal_check.py` 주석뿐. 인증은 집계 표시용(`dal/terms.py:156`) |
| 답변에 출처 반환 | [실행] SQL·컬럼 ID·행 반환 확인 |
| MCP/CLI/API 노출 | [코드] MCP 허용 목록 확인, 서버 미실행 |
| Learn: 인증 수정 환류 | 경로 미식별. 쿼리 이력 제안(`compile.py:99`)은 존재하나 시험 데이터 이력 0건으로 미수행 |

제외: Web UI, RBAC, Vault, PII, Kumo는 실행하지 않았다. 답변 그래프의 `information_agent`, `refine_evidence`, `precheck_combined`, `validate_sql_values`, `kumo_predict` 노드는 이번 실행에서 거치지 않았다. 답변 그래프의 `QuestionIntentModel` 6회 호출은 Stub 응답에 따른 재시도이다. upstream 테스트(semantic, catalog)는 164 passed, 36 skipped.

인증 비교 첫 실행(A2)에서 줄 순서만 다른 프롬프트가 1회 나왔다. 줄 집합은 같았고, 이후 교차 6회에서는 재현되지 않았으며 원인은 확인하지 못했다.

### 문서만 넣었을 때 [실행]

| 입력 | 결과 |
|---|---|
| 빈 DB | compiled_tables=0, LLM 호출 0회 |
| `documents(doc_id,title,body)` 테이블, 본문 10,583자 × 2건 | Term 1개 `Documents`, 속성 3개 (`Body`, `docId`, `Title`) |

- 본문은 조항으로 구조화되지 않았다.
- 본문이 컬럼 설명 프롬프트 1회에 **분할 없이** 들어갔다: 22,001자, 17,773토큰 (`deterministic.py:123,135`).
- 저장되는 샘플은 30자 제한으로 본문이 제외됐다 (`visit_enter.py:64`). 해당 컬럼의 저장 샘플은 비어 있다.
- 저장소에 문서 파서·청커가 없다 (`pdf|docx|docling|text_splitter|nemo.retriever` 검색 시 주석과 의존성 주석만). 'chunk'는 임베딩 배치 단위이다 (`utils/embedding.py:263`).

## 2. Helix Foundry

### 실제 구조

문서 추출 로직은 **이 저장소에 없다.** 저장소의 Go 백엔드는 오케스트레이션과 계약만 담고, 온톨로지 초안과 문서 추출은 Rust 바이너리 `ontology-agent`, `extract`, `ingest-mapped`(이미지 `/usr/local/bin`)가 수행한다. 이미지 라벨은 Apache-2.0이지만 `HelixDB/ontology-agent` 저장소는 인증 없이 접근되지 않아 소스를 확인하지 못했다. 그래서 프롬프트는 실제 요청을 캡처해 확인했다. `backend/enrichment/`는 문서 처리가 아니라 People 프로필 조회이다 (`enrichment/plan.go`).

```
[초안] 문서 집합 최신 5건 + 도구 17개 → ontology.toml + mappings.toml → 사람 검토 → 승인
[추출] 문서 → 엔티티 패스 → 섹션별 링크 패스 → 코드 검증 → 검증 모델 → 판정 → Helix
```

### 출처

| 개념 | 위치 |
|---|---|
| 문서 경로 `extraction` | `backend/ontologyagent/contract.go:49,218` |
| 초안에 보여주는 문서 수 5건 | `backend/ontologyagent/generator.go:47` |
| 문서만으로 초안 허용 | `backend/ontologyagent/generator.go:559` |
| 인용 범위(section, byte offset) | `backend/ontologyagent/ask.go:443` |
| 저장 레이아웃 | `backend/document/document.go:1-16` |
| Ollama 최소 컨텍스트 65,536 | `backend/ai/validate.go:34,85`, `backend/ai/deployment.go:18` |
| 샘플 온톨로지 | `backend/sample/acme.json` (`ontology_toml`, `mappings_toml`의 `[extractions.*]`) |
| 테이블 필수 Definition (별도 경로) | `backend/ontology/ontology.go:108,115,133`, 사용처 `backend/api/ontology.go:19` |

### 오류 주입 결과 [실행, latest 이미지, 실제 HelixDB]

Stub이 사실 5건을 반환하고 검증 확률을 0.95/0.7/0.2로 준 결과이다. 임계값은 기본값 accept 0.9, review 0.6 (`extract --help`).

| 주입한 사실 | 판정 | 사유 | 검증 모델 전달 |
|---|---|---|---|
| 실제 인용, 0.95 | accept | | O |
| 실제 인용, 0.7 | review | low_confidence | O |
| 실제 인용, 0.2 | refuted | | O |
| **문서에 없는 인용** | reject | `quote_not_in_source` | **X, 코드가 차단** |
| **도메인 위반** (Contact → promised_to) | reject | `domain_range_mismatch` | **X, 코드가 차단** |

- 쓰기 결과: entities 2, evidence 1, facts_created 1, mentions 5, reviews 2.
- 수락된 사실에 `span {section:1, start:26, end:71}`가 기록됐다.
- 스키마 enum이 링크 이름과 엔티티 ID를 제한한다 (캡처한 `output_config.format.schema`).
- 키가 있는 온톨로지(acme 원본)로 돌리면 같은 0.95 사실이 `review`(사유 `unresolved`)이고 쓰기는 reviews 4건이다. 키 없는 Commitment만 `resolved:created`였다. 키를 제거한 온톨로지에서는 네 엔티티 모두 created였다.

### 문서만으로 가능한가

- **추출: 가능 [실행].** 테이블 없이 문서와 온톨로지만으로 그래프에 썼다. 단, 위와 같이 키 있는 타입은 대응 행이 없으면 review로 간다.
- **온톨로지 초안: 진입까지만 확인 [실행 일부].** 문서 소스 하나로 `turn`이 시작되어 첫 호출이 나갔다. Stub은 도구 루프를 수행할 수 없어 초안 완성까지는 관찰하지 못했다.

## 3. 논문과 RAGFlow

### 논문의 진술 [논문]

| 개념 | 위치 |
|---|---|
| 지식 컴파일 정의 κ: D→A, span으로의 lineage | §3.1 식(1) |
| Parse·Chunk·Enrich·Validate·Assemble·Register 6단계 | §3.2 |
| "청크는 recall 단위이지 의미 단위가 아니다" | §3.2 |
| claim-evidence 단위 ⟨c,e,s,τ⟩ | §4.1 식(2) |
| "model may propose, but the source disposes", 작은 추출기 glm-4-flash | §4.2 |
| 원본/파생 채널 분리 | §3.4 |
| 토큰 −91%/+1.9%/평균 −38%, 손익분기 2% (유한 배치에서는 식 9) | §4.4 |
| 온톨로지: 타입 지정·추출 제약·소스 간 연결. **FRAMES 미측정** | §5.2, Table 1 |
| 배포 장부 관측치 없음 | §5.3 |
| 구조 산출물의 정확도 이득 미검출 | §3.5, §8.2 |

### 코드 대조

| 논문 | 코드 | 일치 |
|---|---|---|
| claim과 verbatim span | `tree/claims.go:80` 프롬프트, `:513` LocateEvidence | 일치 |
| "locatable span 없는 claim은 저장 안 함" (§4.1) | 기본값 soft (`claims.go:31,38`), 근거 실패 claim 유지. hard도 근거 필드 없는 claim 유지 (`:463`) | **불일치** |
| 온톨로지 템플릿 (§3.2, Fig.1) | 컴파일러 디렉터리는 `mindmap`, `structure`, `tree`, `wiki`. `ontolog` 등장은 3개 파일(도구 별칭 `tool_navigate_structure.go:801`, 프롬프트, 문서) | **코드에서 미확인** |

`claims.go` 경로 접두어: `internal/ingestion/component/knowledge_compiler/`.

배치: 4청크 단위 (`claims.go:21`). 토큰 패킹은 초과 청크를 분할하지 않는다 (`common/batch_packing.go:5,7`).

[실행] 검증기 함수를 그대로 복사해 실행했다(저장소 테스트는 C++ 토크나이저 라이브러리 부재로 빌드 실패).

| 입력 | soft | hard |
|---|---|---|
| verbatim | 유지, offset 기록 | 동일 |
| 공백·줄바꿈 다른 인용 | 유지, offset 기록 | 동일 |
| 한국어 인용 | 유지, offset 기록 | 동일 |
| 의역 인용 | claim 유지, 근거 제거 | claim 제거 |
| 근거 없는 claim | 유지 | **유지** |

## 4. 비교: 사용자가 말한 "청크를 구조화"의 위치

| 항목 | Auto-Ontology | Helix Foundry | 논문/RAGFlow |
|---|---|---|---|
| 뼈대의 출처 | DB 카탈로그 | 승인된 온톨로지 TOML | 프롬프트 템플릿 |
| 긴 문서 처리 | 해당 경로 없음 | 엔티티 창 분할, 섹션 분할 | 청크 |
| 임베딩 대상 | 구조 노드 텍스트 | 이 범위에서 미확인 | claim 벡터 경로 존재 (`compiled_evidence.go`) |
| LLM 출력 제약 | 컬럼 허용 목록 | 스키마 enum + 타입 도메인 | JSON 형식 |
| 원문 대조 | SQL을 카탈로그와 대조 | 인용 원문 대조, 불일치 시 거부 | 인용 원문 대조, 기본값은 claim 유지 |
| 근거 위치 | SQL·컬럼 ID·행 | 섹션 + byte offset | chunk ID + offset |
| 2차 검증 모델 | SQL 의도 검증 | 사실별 확률 | 충분성 게이트 |
| 사람 승인 | 인증 플래그 (답변 프롬프트 영향 없음) | 초안 검토, review 판정 | 미확인 |
| 문서만으로 | 불가 | 추출 가능, 초안은 진입까지 확인 | claim 생성 가능, 온톨로지 템플릿 미확인 |

## 5. 10k 토큰 미만 조건에서의 실측

| 호출 | 입력 | 토큰 (cl100k) | 10k 대비 |
|---|---|---:|---|
| Helix 초안 첫 호출 | 짧은 문서 1건 | **32,743** (메시지 21,510 + 도구 11,233) | 초과 |
| Helix 엔티티 패스 | 짧은 문서 | 739–833 | 이내 |
| Helix 엔티티 패스 | 138KB 헤딩 문서, 3회 | **12,892–14,931** | 초과 |
| Helix 엔티티 패스 | 246KB 한국어 무헤딩, 5회 | **18,756** | 초과 |
| Helix 엔티티 패스 | 246KB 한국어 단일 문단, 6회 | **4,403–18,040** | 초과 포함 |
| Helix 링크 패스 | 긴 문서들, 41–70회 | 819–2,266 | 이내 |
| Helix 검증 패스 | 긴 문서, 40회 | 1,897–1,943 | 이내 |
| AO SQL 생성 | 4테이블 DB | 3,318 | 이내 |
| AO 문서 테이블 컬럼 설명 | 본문 2건 | **17,773** | 초과 |
| RAGFlow claim 추출 | | 미측정 | |

- 링크 패스의 상한은 옵션이다: `--max-section-bytes` 기본 4000. 엔티티 패스 창을 조절하는 옵션은 `extract --help`에 없다.
- `extract` CLI의 모델 옵션은 Anthropic API 전용으로 표기된다. 계약 스키마(`turn_request.json`의 `Provider`)는 Ollama와 OpenAI 호환을 선언한다. gRPC Extract 경로는 실행하지 않았다.
- 초안 `turn`에 `context_tokens=8000`을 지정해도 OpenAI 호환 경로로 같은 크기의 요청이 전송됐다 [실행]. Ollama 설정은 65,536 미만을 거부한다 [코드, `validate.go:85`].
- 저성능 모델의 추출·판정 품질은 측정하지 않았다.

## 6. 증거 재현

`evidence/` 하위에 스크립트와 입력이 있다. 업스트림 클론과 venv는 세션 스크래치패드에 있어 사라질 수 있으므로, 위 커밋으로 다시 받아야 한다.
