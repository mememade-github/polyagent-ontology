# NVIDIA/auto-ontology

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

[뼈대](../concepts/ontology-skeleton-source.md)는 DB 카탈로그이다. 관련 개념: [임베딩 대상](../concepts/embedding-targets.md), [문서만 입력](../concepts/document-only-input.md), [사람 승인](../concepts/human-approval.md), [토큰](../concepts/context-budget.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-08](../contradictions.md#C-08) (표현 범위) Auto-Ontology "문서만으로 불가"
- [C-09](../contradictions.md#C-09) (주장과 코드 불일치) README "certified definitions로 쿼리 검증"
- [C-12](../contradictions.md#C-12) (재현 근거 공백) "evidence/에 스크립트와 입력이 있다"

## 실제 구조

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="AO-01"></a>AO-01 | 뼈대는 DB 카탈로그, LLM은 이름·설명 부착, 임베딩 대상은 구조 노드 | [실행/Stub] | F:34, 근거 행 [AO-K2](#AO-K2), [EM-01](../concepts/embedding-targets.md#EM-01) | 카탈로그 제거 시 전체 소멸(K2) | 실제 LLM이 붙인 이름·설명의 품질은 측정되지 않았다 |
| <a id="AO-02"></a>AO-02 | 컴파일 흐름: SQL 커넥터 → 카탈로그 → Term + ColumnAttribute → 의미 FK → SqlAttribute → 브리지 테이블 → pgvector | [실행/Stub] | F:37, F:38, E:ao/run_pipeline.py | SQLite 커넥터로 실제 `run_ingest`와 `run_semantic_compilation`을 돌렸다(기록만, 원시 출력 없음) | SqlAttribute 단계는 시험 이력 0건으로 수행되지 않았다([AO-R8](#AO-R8)). 브리지 테이블 산출은 표에 기록이 없다 |
| <a id="AO-03"></a>AO-03 | 답변 흐름: 질문 → 의도 → 엔티티 추출 → 후보 검색 → SQL 생성 → 카탈로그 검증 → DB 실행 → 응답 | [실행/Stub] | F:39, E:ao/answer.py, E:ao/k_answer.py | 그래프를 실행하며 노드 목록을 기록했다(스크립트만, 출력 없음) | 거치지 않은 노드는 [AO-X2](#AO-X2) |

## 출처

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="AO-04"></a>AO-04 | 카탈로그 추출 | [코드] | F:46, AO:auto_ontology/catalog/extract.py:89-94, AO:auto_ontology/ingestion_service/ingest.py:110 | 행 내용 일치: `get_tables/columns/views/queries/pks/fks`, `ingest_catalog` | 제거 효과는 [AO-K2](#AO-K2) |
| <a id="AO-05"></a>AO-05 | 컴파일 4단계 | [코드] | F:47, AO:auto_ontology/semantic/compile.py:64,91,99,105 | 행 내용 일치: `compile_semantic_layer`, `resolve_semantic_fks`, `suggest_sql_attributes`, `build_bridge_tables_sql_attributes` | 브리지 단계 제거 효과는 실험되지 않았다 |
| <a id="AO-06"></a>AO-06 | 컬럼 없는 테이블 건너뜀 | [코드] | F:48, AO:auto_ontology/semantic/pipeline.py:186 | 행 내용 일치: `if not ctx.get("columns"):` | 실행 관찰은 [AO-D1](#AO-D1)의 빈 DB뿐이며 이 행을 지나는지는 기록되지 않았다 |
| <a id="AO-07"></a>AO-07 | Term 추출과 허용 목록, 폴백 | [코드] | F:49, AO:auto_ontology/semantic/term_extractor.py:109,134,141,186 | 행 내용 일치: `_fallback_result`, `_sanitize_result`, `allowed_columns`, 미할당 컬럼 폴백 주석 | 제거 효과는 [AO-K1](#AO-K1), [AO-K5](#AO-K5) |
| <a id="AO-08"></a>AO-08 | 2차 컬럼 필터 | [코드] | F:50, AO:auto_ontology/semantic/visit_enter.py:129 | `_terms_with_assignments`가 `spec_by_column`에 있는 컬럼만 남긴다 | 제거 효과는 [AO-K1B](#AO-K1B) |
| <a id="AO-09"></a>AO-09 | 스키마 `term`, `column_attribute`, `column__semantic_fk`, `sql_attribute` | [코드] | F:51, AO:auto_ontology/dal/schema.py:456,487,576,599 | 행 내용 일치 | 없음(선언 위치 확인) |
| <a id="AO-10"></a>AO-10 | 임베딩 텍스트 | [코드] | F:52, AO:auto_ontology/semantic/embed.py:215,247 | [EM-01](../concepts/embedding-targets.md#EM-01) 참조 | [EM-01](../concepts/embedding-targets.md#EM-01) 참조 |
| <a id="AO-11"></a>AO-11 | 커버리지와 거리 임계값 0.75 | [코드] | F:53, AO:auto_ontology/retrieval/entity_coverage/agents/coverage.py:60, AO:auto_ontology/retrieval/entity_coverage/state.py:17, E:ao/coverage_probe.py | 행 내용 일치: `_compute_coverage`, `DEFAULT_MAX_DISTANCE = 0.75`. 프로브 스크립트는 보존됐으나 출력과 결과 기록이 없다 | 임계값의 효과는 어떤 raw에도 기록되지 않았다. 프로브의 임베딩은 해시 BoW Stub이다 |
| <a id="AO-12"></a>AO-12 | SQL 카탈로그 검증 | [코드] | F:54, AO:auto_ontology/retrieval/text_to_sql/agents/sql_parse_validation.py:961,971 | 행 내용 일치: `_sql_parse_validation`, "SQL doesn't reference any table known to the catalog" | 실행 효과는 [AO-K6](#AO-K6), [AO-A3](#AO-A3) |
| <a id="AO-13"></a>AO-13 | 답변 그래프 | [코드] | F:55, AO:auto_ontology/retrieval/text_to_sql/text_to_sql_graph.py:447-463 | 16개 `add_node` 호출을 확인했다(`precheck_combined`는 조건부) | 일부 노드 미실행. [AO-X2](#AO-X2) |
| <a id="AO-14"></a>AO-14 | MCP 허용 목록과 읽기 전용 선언 | [코드] | F:56, AO:mcp/auto_ontology_mcp/tools.py:161, AO:AGENTS.md:60 | `RouteMap(mcp_type=MCPType.EXCLUDE)`, "MCP is read-only by design" | 서버를 실행하지 않았다. [AO-R7](#AO-R7) |

## Knockout

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="AO-K0"></a>AO-K0 | 기준 실행 | [실행/Stub] | F:62, E:ao/knockout.py, E:ao/seed.py, E:ao/stub_llm.py | terms 4, attrs 12, sem_fk 2, 의미 벡터 16(기록만, 원시 출력 없음) | Stub이 유령 컬럼 추가와 컬럼 누락을 일부러 주입한 입력에서의 값이다 |
| <a id="AO-K2"></a>AO-K2 | K2 카탈로그 제거 | [실행/Stub] | F:63, E:ao/knockout.py (`k_catalog`) | 0/0/0/0, 전체 소멸(기록만). 보존된 knockout.py는 `run("baseline")` 뒤 `sys.exit()`이라 그대로면 K2까지 가지 않는다 | [C-12](../contradictions.md#C-12) |
| <a id="AO-K1"></a>AO-K1 | K1 sanitizer 제거 | [실행/Stub] | F:64, E:ao/knockout.py (`k_sanitize`) | terms 4, attrs 8, sem_fk 0, 벡터 12. findings.md는 유령 컬럼을 2차 필터가 막았고 누락 컬럼이 손실됐다고 기록한다(기록만) | sem_fk가 0이 된 경로는 기록되지 않았다. K1을 호출하는 줄이 보존된 스크립트에 없다 |
| <a id="AO-K1B"></a>AO-K1B | K1b 1·2차 필터 모두 제거 | [실행/Stub] | F:65, E:ao/k1b.py | terms 4, attrs 8, sem_fk 0, 벡터 0, 유령 컬럼 저장 0건, compiled_tables=0(기록만) | 두 필터 없이 유령 컬럼이 저장되지 않은 이유와 compiled_tables=0의 원인이 기록되지 않았다. [OP-A1](../open-items.md#OP-A1) |
| <a id="AO-K3"></a>AO-K3 | K3 의미 FK 제거 | [실행/Stub] | F:66, E:ao/k_answer.py | sem_fk 0, SQL 프롬프트 9,113→8,700자(기록만) | SQL 결과 변화는 관찰 불가([M-11](../method-and-limits.md#M-11)) |
| <a id="AO-K4"></a>AO-K4 | K4 Term 임베딩 제거 | [실행/Stub] | F:67, E:ao/k_answer.py | 벡터 0, "Semantic match" 3→0줄, 프롬프트 7,498자(기록만) | SQL 결과 변화는 관찰 불가([M-11](../method-and-limits.md#M-11)) |
| <a id="AO-K5"></a>AO-K5 | K5 Term LLM 응답 없음 | [실행/Stub] | F:68, E:ao/k_answer.py | 폴백으로 동일 개수 생성, 프롬프트 10,113자(기록만) | 폴백 Term의 의미 품질은 측정되지 않았다 |
| <a id="AO-K6"></a>AO-K6 | K6 SQL 카탈로그 검증 제거 | [실행/Stub] | F:69, E:ao/k_answer.py (`k_validator`) | 유령 SQL이 DB까지 도달한 뒤 실행 실패로 재생성(기록만) | 유령 SQL은 Stub이 작성했다 |
| <a id="AO-A3"></a>AO-A3 | A3 검증 유지 | [실행/Stub] | F:70, E:ao/k_answer.py | 유령 SQL이 DB 실행 전 `reconstruct_sql`로 전환(기록만) | 유령 SQL은 Stub이 작성했다 |

## README 주장

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="AO-R1"></a>AO-R1 | 메타데이터에서 온톨로지 생성 | [실행/Stub] | F:76 | findings.md가 확인으로 기록(기록만). [AO-K0](#AO-K0) | 생성물의 의미 품질은 측정되지 않았다 |
| <a id="AO-R2"></a>AO-R2 | 기존 온톨로지·시맨틱 모델 연결(Ossie) | [코드] | F:77, AO:README.md:255-258, AO:auto_ontology/server/model_interchange/router.py | Ossie YAML 내보내기·가져오기 라우트가 있다 | 실행되지 않았다 |
| <a id="AO-R3"></a>AO-R3 | 시스템 간 정의 조정 | [미입증] | F:78, AO:README.md:14 | README 문구만 있다 | findings.md가 미확인으로 기록했다. 직접 근거 없음 |
| <a id="AO-R4"></a>AO-R4 | Agent에 의미 제공 | [실행/Stub] | F:79 | findings.md가 확인으로 기록(기록만). 프롬프트 변화는 [AO-K3](#AO-K3), [AO-K4](#AO-K4) | Stub은 의미를 사용하지 않는다. 실제 답변 품질 효과는 측정되지 않았다 |
| <a id="AO-R5"></a>AO-R5 | 인증 정의로 쿼리 검증 | [실행/Stub] | F:80, AO:README.md:15, AO:auto_ontology/dal/terms.py:156, AO:auto_ontology/retrieval/text_to_sql/db_probe/literal_check.py:765-766 | 인증 값 3회씩 교차 변경에도 SQL 프롬프트 해시 동일(기록만). `retrieval/`의 `certif` 일치는 literal_check.py 주석 2행뿐임을 재확인했다. [C-09](../contradictions.md#C-09) | A2 스크립트가 evidence/에 없다. 프롬프트 외 경로로 인증이 쓰이는지는 `retrieval/` 밖에서 전수 확인되지 않았다 |
| <a id="AO-R6"></a>AO-R6 | 답변에 출처 반환 | [실행/Stub] | F:81, E:ao/answer.py | SQL·컬럼 ID·행 반환(기록만). [ES-01](../concepts/evidence-spans.md#ES-01) | 원문 문서 근거가 아니다. 이 행은 DB 근거만 말한다 |
| <a id="AO-R7"></a>AO-R7 | MCP/CLI/API 노출 | [코드] | F:82, AO:mcp/auto_ontology_mcp/tools.py:161 | MCP 허용 목록 확인 | 서버 미실행. CLI·API는 이 행으로 입증되지 않는다 |
| <a id="AO-R8"></a>AO-R8 | Learn: 인증 수정 환류 | [미입증] | F:83, AO:README.md:17, AO:auto_ontology/semantic/compile.py:99 | 쿼리 이력 제안 호출은 있으나 시험 데이터 이력 0건으로 수행되지 않았다 | 환류 경로가 식별되지 않았다 |

## 실행 범위

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="AO-X1"></a>AO-X1 | 제외: Web UI, RBAC, Vault, PII, Kumo | [미입증] | F:85 | 실행하지 않았다고 findings.md가 기록한다 | 이 기능들의 동작 전체 |
| <a id="AO-X2"></a>AO-X2 | 거치지 않은 노드: `information_agent`, `refine_evidence`, `precheck_combined`, `validate_sql_values`, `kumo_predict` | [미입증] | F:85 | 이번 실행에서 거치지 않았다고 기록됐다 | 이 노드들의 동작. `kumo_predict`는 F:55가 인용한 447-463행 범위에 없었다(범위 밖 위치 미확인) |
| <a id="AO-X3"></a>AO-X3 | `QuestionIntentModel` 6회 호출은 Stub 응답에 따른 재시도 | [실행/Stub] | F:85 | findings.md의 기록(기록만) | 재시도 조건은 인용되지 않았다 |
| <a id="AO-X4"></a>AO-X4 | upstream 테스트(semantic, catalog) 164 passed, 36 skipped | [실행] | F:85 | findings.md의 기록(기록만). 모델과 무관한 저장소 테스트이다 | 다른 디렉터리의 테스트 결과와 skipped 사유는 기록되지 않았다 |
| <a id="AO-X5"></a>AO-X5 | A2 첫 실행에서 줄 순서만 다른 프롬프트 1회 | [실행/Stub] | F:87 | 줄 집합은 같았고 이후 교차 6회에서 재현되지 않았다(기록만) | 원인 미확인. 미확인 그대로 둔다 |

## 문서만 넣었을 때

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="AO-D1"></a>AO-D1 | 입력이 빈 DB | [실행/Stub] | F:93, E:ao/seed.py, E:ao/run_pipeline.py | compiled_tables=0, LLM 호출 0회(기록만) | 없음(이 입력에 한함) |
| <a id="AO-D2"></a>AO-D2 | `documents(doc_id,title,body)` 테이블, 본문 10,583자 × 2건 | [실행/Stub] | F:94, E:ao/seed.py | Term 1개 `Documents`, 속성 3개(기록만). seed.py 생성식으로 10,583자를 재계산해 일치 확인 | [C-08](../contradictions.md#C-08) |
| <a id="AO-D3"></a>AO-D3 | 본문이 조항으로 구조화되지 않았다 | [실행/Stub] | F:96 | findings.md의 기록(기록만) | 실제 모델을 썼을 때 달라지는지는 측정되지 않았다 |
| <a id="AO-D4"></a>AO-D4 | 본문이 컬럼 설명 프롬프트 1회에 분할 없이 투입 | [실행/Stub] | F:97, AO:auto_ontology/semantic/deterministic.py:123,135 | 22,001자, 17,773토큰(기록만). 행 내용 일치: `_describe_column_batch`, `_get_column_samples` | 토큰은 cl100k 기준([M-12](../method-and-limits.md#M-12)) |
| <a id="AO-D5"></a>AO-D5 | 저장 샘플 30자 제한 | [실행/Stub] | F:98, AO:auto_ontology/semantic/visit_enter.py:64 | `_MAX_SAMPLE_VALUE_LEN = 30`, 본문 컬럼의 저장 샘플이 비어 있다(기록만) | 없음(이 입력에 한함) |
| <a id="AO-D6"></a>AO-D6 | 문서 파서·청커 없음, 'chunk'는 임베딩 배치 단위 | [코드] | F:99, AO:auto_ontology/utils/embedding.py:263 | grep 재실행: `pdf\\|docx\\|docling\\|text_splitter\\|nemo.retriever`가 `pyproject.toml`, `auto_ontology/vdb/records.py`, `dev_tools/` 2개 파일에 걸린다 | 부재 주장은 이 패턴 범위의 grep 결과이다. `frontend/`와 다른 표기는 전수 확인되지 않았다 |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
