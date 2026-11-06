# 커버리지

누락이 보이도록 원문 행 순서로 나열한다. 한 행은 한 원문 행과 한 요소의 대응이다. 표의 등급은 위키의 근거 등급이며, "근거 있음"은 해당 범위의 기록이 있다는 뜻이고 품질이나 일반성의 입증이 아니다.

## 요약

- 요소 270개 (findings, interim, results 원문에 대응하는 범위. XT, LC 페이지는 세지 않는다)
- 등급별(갱신 후 현재 표기): [논문] 14, [디컴파일] 11, [미입증] 31, [바이너리] 1, [실행/Stub] 132, [실행] 22, [심볼] 12, [코드] 46, [코드] + [실행/Stub] 1
- findings.md 대응 없는 내용 행: 0개
- interim.md 대응 없는 내용 행: 0개
- results.md 대응 없는 내용 행: 0개
- 전체 미입증 목록: [open-items](open-items.md)
- 검사 한계: 대응은 사람이 아닌 LLM이 행 단위로 작성했고, 스크립트는 행 대응만 검사한다. 한 행 안의 절 단위 누락은 스크립트로 검출되지 않는다.

## findings.md 전 요소

내용 행 121개 모두 아래 요소에 대응한다. 대응 없는 내용 행: 0개. 구조 행(제목, 표 구분선과 머리글, 코드 펜스) 51개는 제외했다.

| 원문 행 | 요소 | 내용 | 등급 | 상태 |
|---|---|---|---|---|
| F:3 | [M-01](method-and-limits.md#M-01) | 전수 나열 규칙: 프로젝트 자신의 선언(README 주장, 컴파일 단계, 답변 그래프 노드, 패스)을 나열하며 측정일은 2026-11-06이다 | [미입증] | 미입증 |
| F:9 | [M-01](method-and-limits.md#M-01) | 전수 나열 규칙: 프로젝트 자신의 선언(README 주장, 컴파일 단계, 답변 그래프 노드, 패스)을 나열하며 측정일은 2026-11-06이다 | [미입증] | 미입증 |
| F:10 | [M-02](method-and-limits.md#M-02) | 핵심 판정 규칙: 메커니즘 제거·오류 주입 시 출력이 달라지면 핵심으로 기록한다 | [미입증] | 미입증 |
| F:11 | [M-03](method-and-limits.md#M-03) | 근거 등급: [실행], [코드], [논문] | [미입증] | 미입증 |
| F:17 | [M-04](method-and-limits.md#M-04) | NVIDIA/auto-ontology `c4495670` | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:18 | [M-05](method-and-limits.md#M-05) | HelixDB/helix-foundry `c7de4051` | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:19 | [M-06](method-and-limits.md#M-06) | ontology-agent 이미지 `latest`, revision `9e1b6284`, 계약 4.7.0 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:20 | [M-07](method-and-limits.md#M-07) | 대조 이미지 `0.1.0`, revision `e1e5a083`, 계약 4.1.1 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:21 | [M-08](method-and-limits.md#M-08) | infiniflow/ragflow `2096707f` | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:22 | [M-09](method-and-limits.md#M-09) | 논문 arXiv 2610.41172 (2026-10-30), Context as Infrastructure | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:26 | [M-10](method-and-limits.md#M-10) | 모든 모델은 Stub이다. 코드가 무엇을 보내고 응답을 어떻게 처리하는지만 증명한다 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:27 | [M-11](method-and-limits.md#M-11) | Stub의 SQL은 고정값이라 K3/K4에서 변한 것은 모델 입력이다 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:28 | [M-12](method-and-limits.md#M-12) | 토큰 수는 `tiktoken cl100k_base` 기준이다 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:34 | [AO-01](products/auto-ontology.md#AO-01) | 뼈대는 DB 카탈로그, LLM은 이름·설명 부착, 임베딩 대상은 구조 노드 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:37 | [AO-02](products/auto-ontology.md#AO-02) | 컴파일 흐름: SQL 커넥터 → 카탈로그 → Term + ColumnAttribute → 의미 FK → SqlAttribute → 브리지 테이블 → pgvector | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:38 | [AO-02](products/auto-ontology.md#AO-02) | 컴파일 흐름: SQL 커넥터 → 카탈로그 → Term + ColumnAttribute → 의미 FK → SqlAttribute → 브리지 테이블 → pgvector | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:39 | [AO-03](products/auto-ontology.md#AO-03) | 답변 흐름: 질문 → 의도 → 엔티티 추출 → 후보 검색 → SQL 생성 → 카탈로그 검증 → DB 실행 → 응답 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:46 | [AO-04](products/auto-ontology.md#AO-04) | 카탈로그 추출 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:47 | [AO-05](products/auto-ontology.md#AO-05) | 컴파일 4단계 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:48 | [AO-06](products/auto-ontology.md#AO-06) | 컬럼 없는 테이블 건너뜀 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:49 | [AO-07](products/auto-ontology.md#AO-07) | Term 추출과 허용 목록, 폴백 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:50 | [AO-08](products/auto-ontology.md#AO-08) | 2차 컬럼 필터 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:51 | [AO-09](products/auto-ontology.md#AO-09) | 스키마 `term`, `column_attribute`, `column__semantic_fk`, `sql_attribute` | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:52 | [AO-10](products/auto-ontology.md#AO-10) | 임베딩 텍스트 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:53 | [AO-11](products/auto-ontology.md#AO-11) | 커버리지와 거리 임계값 0.75 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:54 | [AO-12](products/auto-ontology.md#AO-12) | SQL 카탈로그 검증 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:55 | [AO-13](products/auto-ontology.md#AO-13) | 답변 그래프 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:56 | [AO-14](products/auto-ontology.md#AO-14) | MCP 허용 목록과 읽기 전용 선언 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:60 | [AO-K0](products/auto-ontology.md#AO-K0) | 기준 실행 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:62 | [AO-K0](products/auto-ontology.md#AO-K0) | 기준 실행 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:63 | [AO-K2](products/auto-ontology.md#AO-K2) | K2 카탈로그 제거 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:64 | [AO-K1](products/auto-ontology.md#AO-K1) | K1 sanitizer 제거 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:65 | [AO-K1B](products/auto-ontology.md#AO-K1B) | K1b 1·2차 필터 모두 제거 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:66 | [AO-K3](products/auto-ontology.md#AO-K3) | K3 의미 FK 제거 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:67 | [AO-K4](products/auto-ontology.md#AO-K4) | K4 Term 임베딩 제거 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:68 | [AO-K5](products/auto-ontology.md#AO-K5) | K5 Term LLM 응답 없음 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:69 | [AO-K6](products/auto-ontology.md#AO-K6) | K6 SQL 카탈로그 검증 제거 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:70 | [AO-A3](products/auto-ontology.md#AO-A3) | A3 검증 유지 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:74 | [AO-R1](products/auto-ontology.md#AO-R1) | 메타데이터에서 온톨로지 생성 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:76 | [AO-R1](products/auto-ontology.md#AO-R1) | 메타데이터에서 온톨로지 생성 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:77 | [AO-R2](products/auto-ontology.md#AO-R2) | 기존 온톨로지·시맨틱 모델 연결(Ossie) | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:78 | [AO-R3](products/auto-ontology.md#AO-R3) | 시스템 간 정의 조정 | [미입증] | 미입증 |
| F:79 | [AO-R4](products/auto-ontology.md#AO-R4) | Agent에 의미 제공 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:80 | [AO-R5](products/auto-ontology.md#AO-R5) | 인증 정의로 쿼리 검증 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:81 | [AO-R6](products/auto-ontology.md#AO-R6) | 답변에 출처 반환 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:82 | [AO-R7](products/auto-ontology.md#AO-R7) | MCP/CLI/API 노출 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:83 | [AO-R8](products/auto-ontology.md#AO-R8) | Learn: 인증 수정 환류 | [미입증] | 미입증 |
| F:85 | [AO-X1](products/auto-ontology.md#AO-X1) | 제외: Web UI, RBAC, Vault, PII, Kumo | [미입증] | 미입증 |
| F:85 | [AO-X2](products/auto-ontology.md#AO-X2) | 거치지 않은 노드: `information_agent`, `refine_evidence`, `precheck_combined`, `validate_sql_values`, `kumo_predict` | [미입증] | 미입증 |
| F:85 | [AO-X3](products/auto-ontology.md#AO-X3) | `QuestionIntentModel` 6회 호출은 Stub 응답에 따른 재시도 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:85 | [AO-X4](products/auto-ontology.md#AO-X4) | upstream 테스트(semantic, catalog) 164 passed, 36 skipped | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:87 | [AO-X5](products/auto-ontology.md#AO-X5) | A2 첫 실행에서 줄 순서만 다른 프롬프트 1회 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:93 | [AO-D1](products/auto-ontology.md#AO-D1) | 입력이 빈 DB | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:94 | [AO-D2](products/auto-ontology.md#AO-D2) | `documents(doc_id,title,body)` 테이블, 본문 10,583자 × 2건 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:96 | [AO-D3](products/auto-ontology.md#AO-D3) | 본문이 조항으로 구조화되지 않았다 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:97 | [AO-D4](products/auto-ontology.md#AO-D4) | 본문이 컬럼 설명 프롬프트 1회에 분할 없이 투입 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:98 | [AO-D5](products/auto-ontology.md#AO-D5) | 저장 샘플 30자 제한 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:99 | [AO-D6](products/auto-ontology.md#AO-D6) | 문서 파서·청커 없음, 'chunk'는 임베딩 배치 단위 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:105 | [HX-01](products/helix-foundry.md#HX-01) | 저장소 Go 백엔드는 오케스트레이션과 계약만 담고, 초안·추출은 Rust 바이너리 `ontology-agent`, `extract`, `ingest-mapped`가 수행 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:105 | [HX-02](products/helix-foundry.md#HX-02) | 이미지 라벨 Apache-2.0, `HelixDB/ontology-agent` 소스 미확인 | [미입증] | 미입증 |
| F:105 | [HX-03](products/helix-foundry.md#HX-03) | 프롬프트는 실제 요청 캡처로 확인 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:105 | [HX-04](products/helix-foundry.md#HX-04) | `backend/enrichment/`는 문서 처리가 아니라 People 프로필 조회 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:108 | [HX-05](products/helix-foundry.md#HX-05) | 초안 흐름: 문서 집합 최신 5건 + 도구 17개 → ontology.toml + mappings.toml → 사람 검토 → 승인 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:108 | [HA-03](concepts/human-approval.md#HA-03) | Helix: 초안 승인 | [코드] + [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:109 | [HX-06](products/helix-foundry.md#HX-06) | 추출 흐름: 문서 → 엔티티 패스 → 섹션별 링크 패스 → 코드 검증 → 검증 모델 → 판정 → Helix | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:116 | [HX-07](products/helix-foundry.md#HX-07) | 문서 경로 `extraction` | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:117 | [HX-08](products/helix-foundry.md#HX-08) | 초안에 보여주는 문서 수 5건 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:118 | [HX-09](products/helix-foundry.md#HX-09) | 문서만으로 초안 허용 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:119 | [ES-03](concepts/evidence-spans.md#ES-03) | 인용 범위 타입(section, byte offset) | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:120 | [HX-10](products/helix-foundry.md#HX-10) | 저장 레이아웃 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:121 | [TK-13](concepts/context-budget.md#TK-13) | Ollama 최소 컨텍스트 65,536 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:122 | [HX-11](products/helix-foundry.md#HX-11) | 샘플 온톨로지 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:123 | [HX-12](products/helix-foundry.md#HX-12) | 테이블 필수 Definition(별도 경로) | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:127 | [HX-13](products/helix-foundry.md#HX-13) | 검증 확률 0.95/0.7/0.2 주입, 임계값 accept 0.9, review 0.6 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:129 | [SV-01](concepts/second-verifier.md#SV-01) | 실제 인용, 0.95 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:131 | [SV-01](concepts/second-verifier.md#SV-01) | 실제 인용, 0.95 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:132 | [SV-02](concepts/second-verifier.md#SV-02) | 실제 인용, 0.7 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:133 | [SV-03](concepts/second-verifier.md#SV-03) | 실제 인용, 0.2 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:134 | [QV-01](concepts/quote-validation.md#QV-01) | 문서에 없는 인용 주입 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:134 | [SV-04](concepts/second-verifier.md#SV-04) | 문서에 없는 인용의 검증 모델 전달 차단 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:135 | [SV-05](concepts/second-verifier.md#SV-05) | 도메인 위반(Contact → promised_to) 차단 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:137 | [HX-14](products/helix-foundry.md#HX-14) | 쓰기 결과 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:138 | [ES-02](concepts/evidence-spans.md#ES-02) | Helix: 수락된 사실의 `span {section:1, start:26, end:71}` | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:139 | [SK-08](concepts/ontology-skeleton-source.md#SK-08) | Helix 추출 뼈대: 온톨로지 TOML | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:139 | [OC-02](concepts/output-constraints.md#OC-02) | Helix: 스키마 enum이 링크 이름과 엔티티 ID를 제한 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:140 | [HX-15](products/helix-foundry.md#HX-15) | 키가 있는 온톨로지에서 0.95 사실이 `review`(`unresolved`), 쓰기 reviews 4건 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:144 | [HX-16](products/helix-foundry.md#HX-16) | 추출은 문서와 온톨로지만으로 그래프에 쓴다 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:144 | [DO-02](concepts/document-only-input.md#DO-02) | Helix: 추출 가능 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:145 | [SK-02](concepts/ontology-skeleton-source.md#SK-02) | 초안 경로 완주 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:145 | [DO-03](concepts/document-only-input.md#DO-03) | Helix: 초안 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:153 | [PA-01](products/paper-ragflow.md#PA-01) | 지식 컴파일 정의 κ: D→A, span으로의 lineage | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:154 | [PA-02](products/paper-ragflow.md#PA-02) | Parse·Chunk·Enrich·Validate·Assemble·Register 6단계 | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:155 | [PA-03](products/paper-ragflow.md#PA-03) | "청크는 recall 단위이지 의미 단위가 아니다" | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:156 | [PA-04](products/paper-ragflow.md#PA-04) | claim-evidence 단위 ⟨c,e,s,τ⟩ | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:157 | [PA-05](products/paper-ragflow.md#PA-05) | "model may propose, but the source disposes", 작은 추출기 glm-4-flash | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:158 | [PA-06](products/paper-ragflow.md#PA-06) | 원본/파생 채널 분리 | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:159 | [PA-07](products/paper-ragflow.md#PA-07) | 토큰 −91%/+1.9%/평균 −38%, 손익분기 2%(유한 배치에서는 식 9) | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:160 | [PA-08](products/paper-ragflow.md#PA-08) | 온톨로지: 타입 지정·추출 제약·소스 간 연결, FRAMES 미측정 | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:161 | [PA-09](products/paper-ragflow.md#PA-09) | 배포 장부 관측치 없음 | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:162 | [PA-10](products/paper-ragflow.md#PA-10) | 구조 산출물의 정확도 이득 미검출 | [논문] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:168 | [RF-01](products/paper-ragflow.md#RF-01) | claim과 verbatim span | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:169 | [RF-02](products/paper-ragflow.md#RF-02) | "locatable span 없는 claim은 저장 안 함"(§4.1)과 코드 기본값 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:170 | [RF-03](products/paper-ragflow.md#RF-03) | 온톨로지 템플릿(§3.2, Fig.1) | [미입증] | 미입증 |
| F:172 | [RF-01](products/paper-ragflow.md#RF-01) | claim과 verbatim span | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:174 | [RF-04](products/paper-ragflow.md#RF-04) | 4청크 배치, 초과 청크 미분할 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:176 | [RF-05](products/paper-ragflow.md#RF-05) | 검증기 함수를 복사해 실행, 저장소 테스트는 빌드 실패 | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:178 | [QV-R1](concepts/quote-validation.md#QV-R1) | verbatim | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:180 | [QV-R1](concepts/quote-validation.md#QV-R1) | verbatim | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:181 | [QV-R2](concepts/quote-validation.md#QV-R2) | 공백·줄바꿈 다른 인용 | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:182 | [QV-R3](concepts/quote-validation.md#QV-R3) | 한국어 인용 | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:183 | [QV-R4](concepts/quote-validation.md#QV-R4) | 의역 인용 | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:184 | [QV-R5](concepts/quote-validation.md#QV-R5) | 근거 없는 claim | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:188 | [CMP-1A](comparison.md#CMP-1A) | Auto-Ontology: DB 카탈로그 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:190 | [SK-07](concepts/ontology-skeleton-source.md#SK-07) | Auto-Ontology 뼈대: DB 카탈로그 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:190 | [SK-08](concepts/ontology-skeleton-source.md#SK-08) | Helix 추출 뼈대: 온톨로지 TOML | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:190 | [SK-09](concepts/ontology-skeleton-source.md#SK-09) | RAGFlow 뼈대: 프롬프트 템플릿 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:190 | [CMP-1A](comparison.md#CMP-1A) | Auto-Ontology: DB 카탈로그 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:190 | [CMP-1B](comparison.md#CMP-1B) | Helix: 승인된 온톨로지 TOML | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:190 | [CMP-1C](comparison.md#CMP-1C) | 논문/RAGFlow: 프롬프트 템플릿 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:191 | [CMP-2A](comparison.md#CMP-2A) | Auto-Ontology: 해당 경로 없음 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:191 | [CMP-2B](comparison.md#CMP-2B) | Helix: 엔티티 창 분할, 섹션 분할 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:191 | [CMP-2C](comparison.md#CMP-2C) | 논문/RAGFlow: 청크 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:192 | [EM-01](concepts/embedding-targets.md#EM-01) | Auto-Ontology: 구조 노드 텍스트 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:192 | [EM-02](concepts/embedding-targets.md#EM-02) | Helix: 이 범위에서 미확인 | [미입증] | 미입증 |
| F:192 | [EM-03](concepts/embedding-targets.md#EM-03) | RAGFlow: claim 벡터 경로 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:192 | [CMP-3A](comparison.md#CMP-3A) | Auto-Ontology: 구조 노드 텍스트 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:192 | [CMP-3B](comparison.md#CMP-3B) | Helix: 이 범위에서 미확인 | [미입증] | 미입증 |
| F:192 | [CMP-3C](comparison.md#CMP-3C) | 논문/RAGFlow: claim 벡터 경로 존재 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:193 | [OC-01](concepts/output-constraints.md#OC-01) | Auto-Ontology: 컬럼 허용 목록 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:193 | [OC-03](concepts/output-constraints.md#OC-03) | Helix: 타입 도메인 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:193 | [OC-04](concepts/output-constraints.md#OC-04) | RAGFlow: JSON 형식 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:193 | [CMP-4A](comparison.md#CMP-4A) | Auto-Ontology: 컬럼 허용 목록 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:193 | [CMP-4B](comparison.md#CMP-4B) | Helix: 스키마 enum + 타입 도메인 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:193 | [CMP-4C](comparison.md#CMP-4C) | 논문/RAGFlow: JSON 형식 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:194 | [CMP-5A](comparison.md#CMP-5A) | Auto-Ontology: SQL을 카탈로그와 대조 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:194 | [CMP-5B](comparison.md#CMP-5B) | Helix: 인용 원문 대조, 불일치 시 거부 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:194 | [CMP-5C](comparison.md#CMP-5C) | 논문/RAGFlow: 인용 원문 대조, 기본값은 claim 유지 | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:195 | [ES-01](concepts/evidence-spans.md#ES-01) | Auto-Ontology의 근거 위치: SQL·컬럼 ID·행 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:195 | [ES-04](concepts/evidence-spans.md#ES-04) | RAGFlow: chunk ID + offset | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:195 | [CMP-6A](comparison.md#CMP-6A) | Auto-Ontology: SQL·컬럼 ID·행 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:195 | [CMP-6B](comparison.md#CMP-6B) | Helix: 섹션 + byte offset | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:195 | [CMP-6C](comparison.md#CMP-6C) | 논문/RAGFlow: chunk ID + offset | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:196 | [SV-06](concepts/second-verifier.md#SV-06) | Auto-Ontology: SQL 의도 검증 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:196 | [SV-07](concepts/second-verifier.md#SV-07) | Helix: 사실별 확률 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:196 | [SV-08](concepts/second-verifier.md#SV-08) | RAGFlow: 충분성 게이트 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:196 | [CMP-7A](comparison.md#CMP-7A) | Auto-Ontology: SQL 의도 검증 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:196 | [CMP-7B](comparison.md#CMP-7B) | Helix: 사실별 확률 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:196 | [CMP-7C](comparison.md#CMP-7C) | 논문/RAGFlow: 충분성 게이트 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:197 | [HA-01](concepts/human-approval.md#HA-01) | Auto-Ontology: 인증 플래그 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:197 | [HA-02](concepts/human-approval.md#HA-02) | Helix: review 판정 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:197 | [HA-03](concepts/human-approval.md#HA-03) | Helix: 초안 승인 | [코드] + [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:197 | [HA-04](concepts/human-approval.md#HA-04) | RAGFlow/논문: 사람 승인 | [미입증] | 미입증 |
| F:197 | [CMP-8A](comparison.md#CMP-8A) | Auto-Ontology: 인증 플래그(답변 프롬프트 영향 없음) | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:197 | [CMP-8B](comparison.md#CMP-8B) | Helix: 초안 검토, review 판정 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:197 | [CMP-8C](comparison.md#CMP-8C) | 논문/RAGFlow: 미확인 | [미입증] | 미입증 |
| F:198 | [DO-01](concepts/document-only-input.md#DO-01) | Auto-Ontology: 불가 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:198 | [DO-02](concepts/document-only-input.md#DO-02) | Helix: 추출 가능 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:198 | [DO-03](concepts/document-only-input.md#DO-03) | Helix: 초안 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:198 | [DO-04](concepts/document-only-input.md#DO-04) | RAGFlow: claim 생성 가능, 온톨로지 템플릿 미확인 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:198 | [CMP-9A](comparison.md#CMP-9A) | Auto-Ontology: 불가 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:198 | [CMP-9B](comparison.md#CMP-9B) | Helix: 추출 가능, 초안은 진입까지 확인 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:198 | [CMP-9C](comparison.md#CMP-9C) | 논문/RAGFlow: claim 생성 가능, 온톨로지 템플릿 미확인 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:202 | [TK-01](concepts/context-budget.md#TK-01) | Helix 초안 첫 호출, 짧은 문서 1건 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:204 | [TK-01](concepts/context-budget.md#TK-01) | Helix 초안 첫 호출, 짧은 문서 1건 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:205 | [TK-02](concepts/context-budget.md#TK-02) | Helix 엔티티 패스, 짧은 문서 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:206 | [TK-03](concepts/context-budget.md#TK-03) | Helix 엔티티 패스, 138KB 헤딩 문서 3회 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:207 | [TK-04](concepts/context-budget.md#TK-04) | Helix 엔티티 패스, 246KB 한국어 무헤딩 5회 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:208 | [TK-05](concepts/context-budget.md#TK-05) | Helix 엔티티 패스, 246KB 한국어 단일 문단 6회 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:209 | [TK-06](concepts/context-budget.md#TK-06) | Helix 링크 패스, 긴 문서들 41–70회 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:210 | [TK-07](concepts/context-budget.md#TK-07) | Helix 검증 패스, 긴 문서 40회 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:211 | [TK-08](concepts/context-budget.md#TK-08) | AO SQL 생성, 4테이블 DB | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:212 | [TK-09](concepts/context-budget.md#TK-09) | AO 문서 테이블 컬럼 설명, 본문 2건 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:213 | [TK-10](concepts/context-budget.md#TK-10) | RAGFlow claim 추출 | [미입증] | 미입증 |
| F:215 | [EW-07](concepts/entity-windows.md#EW-07) | 창 조절과 `--max-section-bytes`의 관계 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:216 | [TK-11](concepts/context-budget.md#TK-11) | `extract` CLI는 Anthropic 전용으로 표기, 계약 스키마는 Ollama와 OpenAI 호환 선언, gRPC Extract 미실행 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:217 | [TK-12](concepts/context-budget.md#TK-12) | `context_tokens=8000`이어도 같은 크기 요청 전송 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:217 | [TK-13](concepts/context-budget.md#TK-13) | Ollama 최소 컨텍스트 65,536 | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| F:218 | [TK-15](concepts/context-budget.md#TK-15) | 저성능 모델의 추출·판정 품질 | [미입증] | 미입증 |
| F:222 | [M-13](method-and-limits.md#M-13) | `evidence/`에 스크립트와 입력이 있고 업스트림 클론과 venv는 휘발성이다 | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |

## evidence/rea/interim.md 전 요소

내용 행 47개 모두 아래 요소에 대응한다. 대응 없는 내용 행: 0개. 구조 행(제목, 표 구분선과 머리글, 코드 펜스) 14개는 제외했다.

| 원문 행 | 요소 | 내용 | 등급 | 상태 |
|---|---|---|---|---|
| I:3 | [M-10](method-and-limits.md#M-10) | 모든 모델은 Stub이다. 코드가 무엇을 보내고 응답을 어떻게 처리하는지만 증명한다 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:7 | [M-14](method-and-limits.md#M-14) | REA `rea-agents` 6.8.0, `morluto/rea` `c467cf86`, CLI만 설치 | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:8 | [M-15](method-and-limits.md#M-15) | Ghidra 12.1.4(게시 SHA-256 일치), Temurin JDK 21.0.13, `rea doctor --provider ghidra` healthy | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:9 | [M-16](method-and-limits.md#M-16) | 대상 이미지 `ghcr.io/helixdb/ontology-agent:latest`(라벨 Apache-2.0)와 `inspect-rust-binary` 출력 3건, `auditable_metadata` null | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:9 | [HX-02](products/helix-foundry.md#HX-02) | 이미지 라벨 Apache-2.0, `HelixDB/ontology-agent` 소스 미확인 | [미입증] | 미입증 |
| I:10 | [M-16](method-and-limits.md#M-16) | 대상 이미지 `ghcr.io/helixdb/ontology-agent:latest`(라벨 Apache-2.0)와 `inspect-rust-binary` 출력 3건, `auditable_metadata` null | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:14 | [SYM-01](concepts/binary-symbols.md#SYM-01) | `extract`가 스트립되지 않음, `.symtab` 37,626개 심볼, 디컴파일 전 | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:16 | [SYM-02](concepts/binary-symbols.md#SYM-02) | `extraction` 크레이트 모듈 14개: `adjudicate`, `attribute`, `commit`, `decision`, `document`, `fact`, `pipeline`, `prompt`, `query`, `roster`, `scope`, `store`, `text`, `verify` | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:17 | [SYM-03](concepts/binary-symbols.md#SYM-03) | `prompt::{entity_call, link_call, verify_call, glean_call}` | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:17 | [SYM-04](concepts/binary-symbols.md#SYM-04) | `prompt::adjudicate_call` | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:18 | [SYM-05](concepts/binary-symbols.md#SYM-05) | LLM 구체 타입 `Cached<Limited<Anthropic>>`, `extract::ingest_all`, `llm::anthropic::*` | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:19 | [SYM-06](concepts/binary-symbols.md#SYM-06) | `llm::provider`, `llm::wire` | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:19 | [SYM-07](concepts/binary-symbols.md#SYM-07) | `agent::guard::LeakGuard` | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:19 | [SYM-08](concepts/binary-symbols.md#SYM-08) | `agent::driver::Budget::{prompt_bound, room, near, exhausted}` | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:19 | [SYM-09](concepts/binary-symbols.md#SYM-09) | `agent::lint::lint`, `agent::policy::check` | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:19 | [SYM-10](concepts/binary-symbols.md#SYM-10) | `agent::bundle::approve` | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:20 | [SYM-11](concepts/binary-symbols.md#SYM-11) | 문자열 "the conversation filled the context window; `continue` resumes in a fresh one" | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:20 | [SYM-12](concepts/binary-symbols.md#SYM-12) | 문자열 "the conversation is too long for the model" | ~~[심볼]~~ → [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:22 | [SYM-13](concepts/binary-symbols.md#SYM-13) | 프로바이더 문자열 `anthropic, openai, azure_openai, bedrock, ollama, openai_compatible` | [심볼] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:26 | [SK-01](concepts/ontology-skeleton-source.md#SK-01) | Stub 스크립트로 문서 소스 초안 경로 실행 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:26 | [SK-03](concepts/ontology-skeleton-source.md#SK-03) | out2.ndjson에 나타난 항목 구조 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:28 | [SK-02](concepts/ontology-skeleton-source.md#SK-02) | 초안 경로 완주 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:29 | [M-10](method-and-limits.md#M-10) | 모든 모델은 Stub이다. 코드가 무엇을 보내고 응답을 어떻게 처리하는지만 증명한다 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:31 | [SK-06](concepts/ontology-skeleton-source.md#SK-06) | 잔여 호출 2회에서 예산 임박 안내 주입 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:33 | [SK-04](concepts/ontology-skeleton-source.md#SK-04) | 소스 이름을 포함한 항목 이름 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:35 | [SK-04](concepts/ontology-skeleton-source.md#SK-04) | 소스 이름을 포함한 항목 이름 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:35 | [OC-05](concepts/output-constraints.md#OC-05) | 초안 단계의 코드 거부 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:36 | [SK-05](concepts/ontology-skeleton-source.md#SK-05) | 문서 라우트 없이 `finish` | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:37 | [SK-06](concepts/ontology-skeleton-source.md#SK-06) | 잔여 호출 2회에서 예산 임박 안내 주입 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:41 | [TK-14](concepts/context-budget.md#TK-14) | 보고된 사용량 7000/8000/9000과 턴 지속 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:45 | [QV-02](concepts/quote-validation.md#QV-02) | 원문 그대로 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:47 | [QV-02](concepts/quote-validation.md#QV-02) | 원문 그대로 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:49 | [QV-02](concepts/quote-validation.md#QV-02) | 원문 그대로 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:50 | [QV-03](concepts/quote-validation.md#QV-03) | 대문자 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:51 | [QV-04](concepts/quote-validation.md#QV-04) | 공백·줄바꿈 다름 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:52 | [QV-05](concepts/quote-validation.md#QV-05) | `%` 제거 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:53 | [QV-06](concepts/quote-validation.md#QV-06) | 전각 `％` | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:54 | [QV-07](concepts/quote-validation.md#QV-07) | 단어 중간에서 시작·끝 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:55 | [QV-08](concepts/quote-validation.md#QV-08) | 한국어 NFC | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:56 | [QV-09](concepts/quote-validation.md#QV-09) | 한국어 NFD | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:57 | [QV-10](concepts/quote-validation.md#QV-10) | `...`로 생략 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:58 | [QV-11](concepts/quote-validation.md#QV-11) | 의역 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:59 | [QV-12](concepts/quote-validation.md#QV-12) | 다른 섹션의 문장 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:60 | [QV-13](concepts/quote-validation.md#QV-13) | 한국어 띄어쓰기 제거 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:62 | [QV-01](concepts/quote-validation.md#QV-01) | 문서에 없는 인용 주입 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:62 | [QV-14](concepts/quote-validation.md#QV-14) | interim.md의 해석: "바이트 일치가 아니라 정규화 후 비교이며, 같은 섹션 안으로 제한된다" | [미입증] | 미입증, results.md로 대체된 해석 |
| I:66 | [M-12](method-and-limits.md#M-12) | 토큰 수는 `tiktoken cl100k_base` 기준이다 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:66 | [EW-01](concepts/entity-windows.md#EW-01) | 입력과 측정 방식 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:68 | [EW-02](concepts/entity-windows.md#EW-02) | 기본(`--max-section-bytes 4000`) | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:70 | [EW-02](concepts/entity-windows.md#EW-02) | 기본(`--max-section-bytes 4000`) | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:71 | [EW-03](concepts/entity-windows.md#EW-03) | `--max-section-bytes 1000` | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:72 | [EW-04](concepts/entity-windows.md#EW-04) | `--max-section-bytes 20000` | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:73 | [EW-05](concepts/entity-windows.md#EW-05) | `--gleanings 1` | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:75 | [EW-06](concepts/entity-windows.md#EW-06) | 엔티티 창은 약 50KB 이내, 섹션 단위로 묶임 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:76 | [EW-07](concepts/entity-windows.md#EW-07) | 창 조절과 `--max-section-bytes`의 관계 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:77 | [EW-08](concepts/entity-windows.md#EW-08) | 언어별 토큰 차이 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:78 | [EW-05](concepts/entity-windows.md#EW-05) | `--gleanings 1` | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:79 | [EW-03](concepts/entity-windows.md#EW-03) | `--max-section-bytes 1000` | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:83 | [SYM-14](concepts/binary-symbols.md#SYM-14) | `extract` Ghidra 분석 진행 중: `text::locate_quote`, `text::normalize`, `Document::sections`, `commit::constrain`, `adjudicate::bounded` 디컴파일 전 | [미입증] | 미입증 |
| I:84 | [SYM-15](concepts/binary-symbols.md#SYM-15) | `ontology-agent` 디컴파일 미착수 | [미입증] | 미입증 |
| I:85 | [HA-03](concepts/human-approval.md#HA-03) | Helix: 초안 승인 | [코드] + [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| I:85 | [HA-05](concepts/human-approval.md#HA-05) | 초안 → 추출 연결 | ~~[미입증]~~ → [실행/Stub] | 근거 있음, results.md로 갱신 |
| I:85 | [SV-09](concepts/second-verifier.md#SV-09) | `adjudicate_call`의 실제 호출 | ~~[미입증]~~ → [실행/Stub] | 근거 있음, results.md로 갱신 |
| I:85 | [SYM-16](concepts/binary-symbols.md#SYM-16) | 초안 승인, `adjudicate_call` 호출, 초안 → 추출 연결이 실행 전 | [미입증] | 미입증 |

## evidence/rea/results.md 전 요소

내용 행 48개 모두 아래 요소에 대응한다. 대응 없는 내용 행: 0개. 구조 행 14개는 제외했다.

| 원문 행 | 요소 | 내용 | 등급 | 상태 |
|---|---|---|---|---|
| R:3 | [M-17](method-and-limits.md#M-17) | results.md가 더한 등급 [디컴파일], [바이너리]와 "모델은 전부 Stub" 선언 | [미입증] | 미입증 |
| R:5 | [M-17](method-and-limits.md#M-17) | results.md가 더한 등급 [디컴파일], [바이너리]와 "모델은 전부 Stub" 선언 | [미입증] | 미입증 |
| R:7 | [M-17](method-and-limits.md#M-17) | results.md가 더한 등급 [디컴파일], [바이너리]와 "모델은 전부 Stub" 선언 | [미입증] | 미입증 |
| R:8 | [M-17](method-and-limits.md#M-17) | results.md가 더한 등급 [디컴파일], [바이너리]와 "모델은 전부 Stub" 선언 | [미입증] | 미입증 |
| R:12 | [M-18](method-and-limits.md#M-18) | REA `decompile` 사용 불가(300초 시작 제한, `provider_timeout`) | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:13 | [M-19](method-and-limits.md#M-19) | 디컴파일 경로: 같은 Ghidra, `DecAddrs.java`, 주소는 `nm` 값에 이미지 베이스를 더했다 | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:14 | [M-20](method-and-limits.md#M-20) | 분석 상태: `extract`는 1500초 제한으로 미완료 저장, `ontology-agent`는 분석 없이 함수 단위 디스어셈블 | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:15 | [M-21](method-and-limits.md#M-21) | REA 내장 명령 중 기여한 것: `inspect-rust-binary`, `inspect-artifact`, `doctor` | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:19 | [QV-20](concepts/quote-validation.md#QV-20) | 1단계: 인용을 `text::normalize`로 정규화, 3글자 미만이면 찾지 못함 | [디컴파일] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:19 | [QV-23](concepts/quote-validation.md#QV-23) | 4단계: 최댓값이 0.95 이상이면 창의 원본 바이트 범위를 span으로 돌려줌 | [바이너리] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:21 | [QV-20](concepts/quote-validation.md#QV-20) | 1단계: 인용을 `text::normalize`로 정규화, 3글자 미만이면 찾지 못함 | [디컴파일] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:22 | [QV-21](concepts/quote-validation.md#QV-21) | 2단계: 섹션 본문을 정규화하고 정규화 문자열에서 정확 검색 | [디컴파일] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:23 | [QV-22](concepts/quote-validation.md#QV-22) | 3단계: 정확 검색 결과가 없으면 어절 수 n−1..n+1 창에서 `rapidfuzz` indel `normalized_similarity` 최댓값을 구함 | [디컴파일] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:24 | [QV-23](concepts/quote-validation.md#QV-23) | 4단계: 최댓값이 0.95 이상이면 창의 원본 바이트 범위를 span으로 돌려줌 | [바이너리] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:26 | [QV-24](concepts/quote-validation.md#QV-24) | 앞 단어를 `zzzz`로 바꾼 변형 7건(`sub1`~`sub7`) | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:26 | [QV-25](concepts/quote-validation.md#QV-25) | 끝에서 두 번째 글자부터 앞으로 X로 바꾼 변형 8건(`char1`~`char14`) | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:26 | [QV-26](concepts/quote-validation.md#QV-26) | 오타 2개 인용(`typo_mid`) | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:26 | [QV-27](concepts/quote-validation.md#QV-27) | 단어 하나 인용 `Globex` | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:28 | [QV-28](concepts/quote-validation.md#QV-28) | span 26–72가 퍼지 창이 뒤 쉼표까지 포함한 결과라는 해석 | [디컴파일] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:29 | [QV-29](concepts/quote-validation.md#QV-29) | 대조 범위가 인용이 나온 섹션 하나인지 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:30 | [QV-30](concepts/quote-validation.md#QV-30) | results.md의 진술: 임의의 짧은 단어 인용도 섹션에 있으면 통과, 사실 여부는 검증 모델 몫 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:34 | [HA-06](concepts/human-approval.md#HA-06) | `approve` 잘못된 rev | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:36 | [HA-06](concepts/human-approval.md#HA-06) | `approve` 잘못된 rev | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:37 | [HA-07](concepts/human-approval.md#HA-07) | `approve` 항목 미승인 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:38 | [HA-08](concepts/human-approval.md#HA-08) | `feedback` 항목별 approve 5건 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:39 | [HA-09](concepts/human-approval.md#HA-09) | `feedback` comment와 승인 항목 잠금 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:40 | [HA-10](concepts/human-approval.md#HA-10) | `approve` 전 항목 승인 후 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:42 | [HA-11](concepts/human-approval.md#HA-11) | bundle 필드 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:44 | [HA-12](concepts/human-approval.md#HA-12) | 저장소 Go 계약은 `start`만, 바이너리 스키마는 `start`, `feedback`, `continue`, `approve` | [코드] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:48 | [HA-13](concepts/human-approval.md#HA-13) | 문서 → 초안 → 항목 승인 → 초안 승인 → 번들 → `extract --ontology` → HelixDB 쓰기 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:50 | [HA-13](concepts/human-approval.md#HA-13) | 문서 → 초안 → 항목 승인 → 초안 승인 → 번들 → `extract --ontology` → HelixDB 쓰기 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:52 | [HA-13](concepts/human-approval.md#HA-13) | 문서 → 초안 → 항목 승인 → 초안 승인 → 번들 → `extract --ontology` → HelixDB 쓰기 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:56 | [TK-16](concepts/context-budget.md#TK-16) | `Budget::exhausted` | [디컴파일] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:57 | [TK-17](concepts/context-budget.md#TK-17) | `Budget::prompt_bound` | [디컴파일] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:58 | [TK-18](concepts/context-budget.md#TK-18) | `ModelSpec::settle`의 0x10000 | [디컴파일] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:59 | [TK-19](concepts/context-budget.md#TK-19) | 서버 400 `context_length_exceeded` 처리 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:60 | [TK-20](concepts/context-budget.md#TK-20) | 초안 시스템 메시지 크기 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:60 | [TK-21](concepts/context-budget.md#TK-21) | `continue`의 새 대화 크기 | [미입증] | 미입증 |
| R:64 | [EW-09](concepts/entity-windows.md#EW-09) | 99바이트 문단 3,000개 입력의 창 최대값 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:66 | [EW-10](concepts/entity-windows.md#EW-10) | 상한이 정확히 50,000이라는 추정 | [미입증] | 미입증 |
| R:68 | [EW-11](concepts/entity-windows.md#EW-11) | `--max-section-bytes 500`의 rc=1 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:72 | [SV-10](concepts/second-verifier.md#SV-10) | `ingest-mapped`로 `Account{A-100, Globex}` 적재, `sources` 형식 | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:76 | [SV-11](concepts/second-verifier.md#SV-11) | 문서 엔티티 `Globex`(이름 일치) | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:77 | [SV-12](concepts/second-verifier.md#SV-12) | 문서 엔티티 `Initech`(무관) | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:78 | [SV-13](concepts/second-verifier.md#SV-13) | 문서 엔티티 `Globex Inc`(부분 일치) | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:79 | [SV-14](concepts/second-verifier.md#SV-14) | 문서 엔티티 `Globex renewal`(부분 일치) | [실행/Stub] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:81 | [SV-15](concepts/second-verifier.md#SV-15) | adjudicate 응답을 수용시키는 조건 | [미입증] | 미입증 |
| R:81 | [SV-16](concepts/second-verifier.md#SV-16) | `adj_choices.c` | [디컴파일] | 근거 있음, 잔여는 해당 행의 미입증 칸 |
| R:85 | [M-24](method-and-limits.md#M-24) | 추출·판정 품질, 저성능 로컬 모델의 수행 능력 | [미입증] | 미입증 |
| R:87 | [M-24](method-and-limits.md#M-24) | 추출·판정 품질, 저성능 로컬 모델의 수행 능력 | [미입증] | 미입증 |
| R:88 | [M-25](method-and-limits.md#M-25) | `extract`의 비-Anthropic 경로, gRPC Extract | [미입증] | 미입증 |
| R:89 | [M-26](method-and-limits.md#M-26) | Auto-Ontology 미실행 기능(Web UI, RBAC, Vault, PII, Kumo, Ossie, MCP 서버), Learn 경로 | [미입증] | 미입증 |
| R:90 | [M-27](method-and-limits.md#M-27) | RAGFlow 프롬프트 토큰, 온톨로지 템플릿, 사람 승인 | [미입증] | 미입증 |
| R:91 | [M-28](method-and-limits.md#M-28) | `ontology-agent`의 나머지 함수, 스크립트에 넣지 않은 도구 `evaluate`, `preview_extraction`, `dry_run` | [미입증] | 미입증 |
| R:95 | [M-22](method-and-limits.md#M-22) | Ghidra 프로젝트, 클론, 일부 스크립트는 휘발성이고 실험 컨테이너는 제거됨 | [실행] | 근거 있음, 잔여는 해당 행의 미입증 칸 |

## 세 파일 밖에서 추가한 요소

evidence, 논문, 코디네이터 통지에서 직접 온 요소이다.

| 요소 | 내용 | 등급 | 인용 |
|---|---|---|---|
| [HX-17](products/helix-foundry.md#HX-17) | `unmatched`, `origin`, 모델 표기 | [실행/Stub] | E:helix/report3.raw |
| [PA-11](products/paper-ragflow.md#PA-11) | Validate 단계의 처리: "Invalid units are dropped, not repaired by the model" | [논문] | P:§3.2 (p.txt:264-266) |
| [QV-15](concepts/quote-validation.md#QV-15) | accept 8건, reject 4건의 검증 모델 전달 | [실행/Stub] | E:rea/quote/r_*.raw (`calls`) |
| [QV-P1](concepts/quote-validation.md#QV-P1) | ~~인용 대조가 rapidfuzz 유사도 함수를 호출한다는 코디네이터 통지(결과 대기)~~ → `locate_quote`의 rapidfuzz 호출 통지, results.md로 수집됨 | ~~[미입증]~~ → [디컴파일] | 코디네이터 메시지 2026-11-06. raw 소스 없음 |
| [ES-05](concepts/evidence-spans.md#ES-05) | 논문의 단위와 offset 기록 | [논문] | P:§4.2 (p.txt:445), §3.2 (p.txt:271-273) |
| [SK-10](concepts/ontology-skeleton-source.md#SK-10) | "an Ontology template adds classes, properties, and constraints" | [논문] | P:§3.2 (p.txt:277) |
| [QV-31](concepts/quote-validation.md#QV-31) | raw 29건 판정과 R:21-24 경로의 일치 점검 | [미입증] | E:rea/quote/r_*.raw, E:rea/quote/fuzzy.json, E:rea/quote/doc.md |
| [SYM-17](concepts/binary-symbols.md#SYM-17) | `Budget::near` | [디컴파일] | E:rea/decompiled/ontology-agent/b_near.c |
| [SYM-18](concepts/binary-symbols.md#SYM-18) | `b_room.c` | [디컴파일] | E:rea/decompiled/ontology-agent/b_room.c:4, E:rea/ghidra/addrs-oa.txt |
| [SYM-19](concepts/binary-symbols.md#SYM-19) | results.md에 해석이 없는 파일: `sections.c`, `fold.c`, `tokens.c`, `dec_entity.c`, `dec_fitting.c`, `adj_bounded.c`, `m_maxtokens.c`, `m_runtime.c` | [미입증] | E:rea/decompiled/ |
| [SYM-20](concepts/binary-symbols.md#SYM-20) | 출력 파일이 없는 함수: `normalize`, `adj_pairing`, `p_entity`, `commit::constrain` | [미입증] | E:rea/ghidra/addrs.txt, I:83 |

---
[index](index.md)
