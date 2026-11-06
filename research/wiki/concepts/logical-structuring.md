# 논리 구조화

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/실모델]`은 한 모델, 소수 입력의 관찰이며 품질 수치가 아니다.

관리자 판단(2026-11-06): 본질은 실제 정보를 어떻게 논리적으로 구조화하느냐이다. 이 페이지는 그 기준으로 세 시스템을 코드와 실행으로 대조한다. 관련: [뼈대](ontology-skeleton-source.md), [문서만 입력](document-only-input.md), [컨텍스트](context-budget.md).

## 시스템별 논리 구조와 결정 주체

| ID | 시스템 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="LS-01"></a>LS-01 | Auto-Ontology | [코드] | AO:auto_ontology/dal/schema.py:456, AO:auto_ontology/semantic/deterministic.py:218, AO:auto_ontology/semantic/term_extractor.py:33 | 구조는 Term, ColumnAttribute, SemanticFK, SqlAttribute이다. 뼈대는 입력 DB 스키마이다. LLM은 이름, 설명, 열 배정을 정하고 프롬프트는 테이블당 Term 하나를 강하게 선호하며 `IS_A`, `PART_OF`, `ROLE` 제안을 금지한다 | 없음(선언 위치 확인) |
| <a id="LS-02"></a>LS-02 | Helix | [코드] | HF:backend/sample/acme.json, HF:backend/ontologyagent/contract.go:250 | 구조는 타입(props, key, names, identifiers), 링크(방향, cardinality, required), Datalog 제약, 매핑, 추출 경로이다. 입력은 사람의 workflow와 goals이고 뼈대는 에이전트가 제안한다 | 파서와 검증 구현은 비공개 바이너리이다 |
| <a id="LS-03"></a>LS-03 | Helix 초안 방법 | [실행/Stub] | E:rea/approval/sys.txt | 캡처 프롬프트의 절차: 목표를 역량 질문으로 바꾸고, 도구로 열, 키, 조인을 측정하고, 타입과 링크를 정의하고, dry_run과 규칙 평가를 거친다. 질문, 키, 조인에 쓰이지 않는 항목은 뺀다 | 프롬프트의 진술이다. 도구의 구현은 읽지 않았다 |
| <a id="LS-04"></a>LS-04 | RAGFlow | [코드] | RF:internal/ingestion/knowledge_compile/templates/knowledge_graph.yaml:11, RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:161 | 구조는 템플릿별 엔티티와 관계, claim과 인용, 요약 트리이다. 타입은 템플릿이 고정하고(엔티티 6, 관계 6) LLM은 그 안에서 이름과 관계를 뽑는다 | 사용자 정의 템플릿으로 대체되는지 |
| <a id="LS-05"></a>LS-05 | 차이 | [코드] | [LS-01](#LS-01), [LS-02](#LS-02), [LS-04](#LS-04) | 입력에 구조가 없을 때 뼈대를 정하는 쪽: Auto-Ontology는 해당 경로 없음, RAGFlow는 템플릿 작성자, Helix는 LLM 에이전트와 사람 승인이다 | 없음 |

## 실제 모델의 뼈대 생성

| ID | 조건 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="LS-10"></a>LS-10 | Helix, Ollama 프로바이더, `context_tokens` 8192, 65536, 131072 | [실행/실모델] | E:skeleton/d1_ctx8k_doc.out, E:skeleton/d2_ctx64k_doc.out, E:skeleton/s1.out, E:skeleton/s2.out | 모델 채팅 호출 0회, `budget_exhausted`, 경고 "the conversation filled the context window" | 원인. 모델이 보고한 컨텍스트 길이 32768과의 관계는 확인하지 않았다 |
| <a id="LS-11"></a>LS-11 | Helix, 호환 프로바이더, 실제 8192, 표기 8192 | [실행/실모델] | E:skeleton/t1_ctx8k_doc.out, E:skeleton/t1_ctx8k_doc.calls, E:skeleton/t1_ctx8k_doc.ollama | 30회 호출, 1,868초, `budget_exhausted`, 항목 0. 요청 약 119KB이고 Ollama 로그 `truncating input prompt limit=4098 prompt=28987`. `read_text`를 `source` 없이 반복 호출 | 다른 모델 |
| <a id="LS-12"></a>LS-12 | Helix, 실제 8192, 표기 65536 | [실행/실모델] | E:skeleton/t1b_ctxclaim64k_real8k.out, E:skeleton/t1b_ctxclaim64k_real8k.ollama | 30회 호출, 336초, `budget_exhausted`, 항목 0. 잘림은 같다 | 다른 모델 |
| <a id="LS-13"></a>LS-13 | Helix, 실제 32768, doc.md | [실행/실모델] | E:skeleton/t2_ctx64k_doc.out, E:skeleton/t2_ctx64k_doc.calls, E:skeleton/t2_ctx64k_doc.ollama | 6회 호출, 1,844초, status `done`인데 항목 0. 첫 호출 입력 29,131토큰, 1,180초. `num_ctx` 65536이어도 `n_ctx_slot` 32768. 문서를 읽지 않았고 `type.PromisedTo`, `type.PromisedToDate`를 없는 필드 `customer_id`, `promise_id`로 제안했다. 형식 오류로 거부됐고 고치지 못했다 | 다른 모델, 다른 문서 |
| <a id="LS-14"></a>LS-14 | Helix, 실제 32768, gold.md + 표 | [실행/실모델] | E:skeleton/t3_ctx64k_gold_table.out, E:skeleton/t3_ctx64k_gold_table.calls | 6회 호출, 1,077초, status `done`인데 항목 0. `describe`와 `check_draft`만 호출했다. 모델 문장은 빈 초안을 "clean"이라 하고 타입과 링크를 정의했다고 썼다 | 다른 모델, 다른 문서 |
| <a id="LS-15"></a>LS-15 | Auto-Ontology, 실제 8192, 4개 테이블 DB | [실행/실모델] | E:skeleton/ao.out, E:skeleton/ao_shop.calls | 호출 9회, 호출당 입력 146~794토큰, 잘림 없음. Term 4개, 속성 12개, 의미 FK 2개. 이름은 그럴듯하나 `Customers`, `Product Details`로 일관되지 않다. `order_items.product_id`는 선언 FK가 없어 관계가 아닌 속성으로 남았다 | 이후 단계의 품질, 다른 스키마 |
| <a id="LS-16"></a>LS-16 | Auto-Ontology, 실제 8192, 문서 테이블 | [실행/실모델] | E:skeleton/ao_docs.calls, E:skeleton/ao.out | Term `Documents`, 속성 3개, 의미 FK 0개. 열 설명 호출은 프롬프트 15,117토큰이 4,098로 잘렸고 본문 일부를 열 이름으로 낸 응답이 나왔다. 설명은 대체 문구가 저장됐다. 본문 구조는 나오지 않았다 | 실행을 도중에 중단했다. 이후 단계는 관찰하지 않았다 |

Auto-Ontology 실행의 임베딩은 해시값이다. 스레드는 14이고 이전 실모델 기록의 8과 다르다.

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
