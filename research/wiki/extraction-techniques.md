# 지식 추출 기법별 비교와 구현 범위

> 등급과 인용 표기는 [SCHEMA](SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. 칸 사이 우열은 기록하지 않는다.

Query 결과를 남긴 페이지이다. RAGFlow 행은 이번에 새로 수집한 E:ragflow/compile/ 을 근거로 한다. 하니스는 업스트림 패키지 내부에서 Stub 채팅으로 함수를 호출했고, C++ 분석기는 호출 시 중단되는 링크용 스텁으로 대체했다. RAGFlow 전체 파이프라인과 저장은 실행하지 않았다. 관련: [대조 기록 C-23](contradictions.md#C-23).

## Auto-Ontology

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="XT-01"></a>XT-01 | 카탈로그 추출(LLM 없음) | [실행/Stub] | [AO-04](products/auto-ontology.md#AO-04), [AO-K2](products/auto-ontology.md#AO-K2) | 제거 시 산출 전체 소멸 | SQL 커넥터 입력 전용이다 |
| <a id="XT-02"></a>XT-02 | Term·컬럼 속성 라벨링 + 허용 목록 | [실행/Stub] | [AO-01](products/auto-ontology.md#AO-01), [OC-01](concepts/output-constraints.md#OC-01), AO:auto_ontology/semantic/term_extractor.py:134-186 | 응답이 없어도 폴백으로 같은 개수 생성(K5) | 라벨 품질 |
| <a id="XT-03"></a>XT-03 | 의미 FK(벡터 검색, 샘플값 대조, LLM 선택) | [실행/Stub] | AO:auto_ontology/semantic/semantic_fk.py:466,531,655, [AO-K3](products/auto-ontology.md#AO-K3) | 기준 실행 2건 | 후보 선택 품질 |
| <a id="XT-04"></a>XT-04 | 쿼리 이력 기반 SqlAttribute | [코드] | AO:auto_ontology/semantic/compile.py:99, [AO-R8](products/auto-ontology.md#AO-R8) | 시험 이력 0건으로 미수행 | 동작 전체 |
| <a id="XT-05"></a>XT-05 | 문서 입력 | [실행/Stub] | [DO-01](concepts/document-only-input.md#DO-01) | 파서·청커 없음. 본문이 컬럼 설명 프롬프트 1회에 분할 없이 들어가 17,773토큰 | 없음 |

## Helix

소스 비공개 바이너리이다. 프롬프트는 요청 캡처로 확인했다.

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="XT-06"></a>XT-06 | 온톨로지 초안(도구 루프) | [실행/Stub] | [SK-02](concepts/ontology-skeleton-source.md#SK-02), [HA-13](concepts/human-approval.md#HA-13), F:204 | 문서만으로 `done`, 승인, 번들까지 통과. 첫 호출 32,743토큰 | 초안 내용은 Stub 작성. Foundry 경유 없음 |
| <a id="XT-07"></a>XT-07 | 엔티티 패스 | [실행/Stub] | F:205-208, [EW-09](concepts/entity-windows.md#EW-09) | 긴 문서에서 12,892–18,756토큰. 창 크기 옵션 없음 | 상한 상수 |
| <a id="XT-08"></a>XT-08 | 링크 패스 | [실행/Stub] | F:209, [OC-02](concepts/output-constraints.md#OC-02) | 819–2,266토큰. 스키마 enum이 링크와 엔티티 ID 제한 | 실제 모델의 스키마 준수 |
| <a id="XT-09"></a>XT-09 | `--gleanings` | [실행/Stub] | I:78 | 링크 호출 150→300 | `glean_call`과의 연결, 추가 회수량 |
| <a id="XT-10"></a>XT-10 | 코드 검증(인용, 도메인·범위) | [실행/Stub] | [QV-20](concepts/quote-validation.md#QV-20), F:134-135 | 위반 시 reject, 검증 모델 미전달 | `normalize` 내용 |
| <a id="XT-11"></a>XT-11 | 검증 모델(확률 판정) | [실행/Stub] | [SV-07](concepts/second-verifier.md#SV-07), F:210 | accept 0.9, review 0.6. 1,897–1,943토큰 | 판정 품질 |
| <a id="XT-12"></a>XT-12 | 엔티티 해소와 adjudicate | [실행/Stub] | [SV-11](concepts/second-verifier.md#SV-11), [SV-13](concepts/second-verifier.md#SV-13), [SV-15](concepts/second-verifier.md#SV-15) | 이름 일치 resolved. 부분 일치는 호출되나 전부 unresolved | **수용 조건 미확인** |
| <a id="XT-13"></a>XT-13 | `ingest-mapped`(구조 데이터 매핑) | [실행] | R:72, E:helix/ingest-mapped.help.txt | 모델 옵션이 `--help`에 없다. JSONL 행 적재 | 문서 추출 경로가 아니다 |

## RAGFlow

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="XT-14"></a>XT-14 | claim 추출(tree) | [실행/Stub] | RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:21,378, E:ragflow/compile/harness.out | 프롬프트 578토큰. 2,551토큰 청크 8개에 `ModelContextLen` 8000을 줘도 4개씩 묶여 호출당 10,823토큰. 인용 실패 claim은 soft 유지, hard 제거. 근거 없는 claim은 둘 다 유지 | 실제 모델 품질 |
| <a id="XT-15"></a>XT-15 | graph(structure, 엔티티→관계 2단계) | [실행/Stub] | RF:internal/ingestion/component/knowledge_compiler/structure/compile.go:54, RF:internal/ingestion/knowledge_compile/templates/knowledge_graph.yaml, E:ragflow/compile/harness.out | 고정 타입: 엔티티 6, 관계 6. 시스템 프롬프트 486토큰 | 실제 모델 품질 |
| <a id="XT-16"></a>XT-16 | graph의 코드 차단 범위 | [실행/Stub] | E:ragflow/compile/harness.out, RF:internal/ingestion/component/knowledge_compiler/structure/compile.go:301 | 저장 유지: 템플릿 밖 타입, 원문에 없는 엔티티, 미지 엔드포인트 관계. `knowledge_graph.yaml`은 `evidence`를 요구하지 않는다. 제거: 자기 참조 관계, hard 모드의 인용 실패 항목. 없는 청크 ID는 배치 청크로 대체 | ~~다운스트림 저장 단계의 처리~~ → 데이터셋 병합이 미지 엔드포인트 관계를 제거한다([C-25](contradictions.md#C-25)). 나머지 저장 처리는 미실행 |
| <a id="XT-17"></a>XT-17 | graph의 입력 예산 | [실행/Stub] | RF:internal/ingestion/component/knowledge_compiler/structure/structure.go:57, RF:internal/ingestion/component/knowledge_compiler/common/batch_packing.go:5, E:ragflow/compile/harness.out | 예산 = max(컨텍스트×0.5 − 프롬프트, 1024). 컨텍스트 8000에서 최대 14,146토큰은 예산 초과 단일 청크이고 분할되지 않는다 | 실제 청커가 만드는 청크 크기 |
| <a id="XT-18"></a>XT-18 | 중복 병합(LLM 판정) | [코드] | RF:internal/ingestion/component/knowledge_compiler/structure/merge.go:136,182 | 패키지 테스트 통과 | 파이프라인 실행 없음 |
| <a id="XT-19"></a>XT-19 | wiki(MAP→REDUCE→PLAN→REFINE) | [코드] | RF:internal/ingestion/component/knowledge_compiler/wiki/wiki.go:1-7,65 | MAP 예산 상수 2048. 패키지 테스트 통과 | 호출 크기 미측정 |
| <a id="XT-20"></a>XT-20 | mindmap | [코드] | RF:internal/ingestion/component/knowledge_compiler/mindmap/prompt.go | 예산 상수(`mindmapMaxLength` 4096 기준). 근거는 `source_chunk_ids`뿐이다. 패키지 테스트 통과 | 호출 크기 미측정 |
| <a id="XT-21"></a>XT-21 | page_index, timeline, session 계열 | [코드] | RF:internal/ingestion/component/knowledge_compiler/common/types.go:332-334, RF:internal/ingestion/knowledge_compile/templates/ | structure 경로로 분기된다 | 동작 미실행 |
| <a id="XT-22"></a>XT-22 | 논문의 Ontology 템플릿 | [코드] | P:§3.2 (p.txt:277), RF:internal/ingestion/knowledge_compile/templates/, RF:internal/engine/types/compilation.go | 템플릿 파일과 kind 허용 목록에 `ontology`가 없다 | 공개 저장소 밖 존재 여부, 사용자 정의 템플릿으로 대체되는지 |
| <a id="XT-23"></a>XT-23 | 패키지 테스트 | [실행] | E:ragflow/compile/upstream_tests.txt, E:ragflow/compile/rf_use.out | `structure`, `tree`, `wiki`, `mindmap`, `common` ok. `golden`은 빌드 실패. 같은 의존성 `office_oxide`의 헤더 부재 오류가 `rf_use.out`에 있다 | 실패 패키지의 동작 |

---
[index](index.md) · [comparison](comparison.md) · [open items](open-items.md)
