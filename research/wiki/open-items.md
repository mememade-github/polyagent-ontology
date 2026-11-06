# 미해결·미입증 항목

추론으로 메우지 않는다. 항목은 근거가 들어올 때까지 열어 둔다.

## 묶음

| ID | 항목 | 위치 | 상태 |
|---|---|---|---|
| <a id="OP-Q1"></a>OP-Q1 | Helix 인용 대조 판정 메커니즘. rapidfuzz 통지 포함 | [QV-P1](concepts/quote-validation.md#QV-P1), [QV-14](concepts/quote-validation.md#QV-14), [C-16](contradictions.md#C-16) | ~~임계값 시험 결과 raw 소스 대기~~ → results.md로 경로 해석 수집. 잔여는 OP-Q4 |
| <a id="OP-Q2"></a>OP-Q2 | `extract` 디컴파일 결과 | [SYM-14](concepts/binary-symbols.md#SYM-14) | ~~Ghidra 진행 중(I:83)~~ → 미완료 분석으로 일부 파일 생성([M-20](method-and-limits.md#M-20)). 잔여는 OP-H11 |
| <a id="OP-Q3"></a>OP-Q3 | `% 제거` 변형의 span이 인용보다 2바이트 긴 이유 | [QV-05](concepts/quote-validation.md#QV-05) | ~~미확인~~ → 퍼지 창의 쉼표 포함이라는 해석([QV-28](concepts/quote-validation.md#QV-28)). 직접 관찰 없음 |
| <a id="OP-H1"></a>OP-H1 | 엔티티 창 상한 상수, 상한을 넘는 단일 섹션의 처리 | [EW-06](concepts/entity-windows.md#EW-06), [TK-05](concepts/context-budget.md#TK-05) | ~~미확인~~ → 관측 최대 49,994, 50,000은 추정, 상수와 초과 섹션 처리 미확인([EW-10](concepts/entity-windows.md#EW-10)) |
| <a id="OP-H2"></a>OP-H2 | `Budget`과 `context_tokens`의 의미 | [TK-12](concepts/context-budget.md#TK-12), [TK-14](concepts/context-budget.md#TK-14), [SYM-08](concepts/binary-symbols.md#SYM-08) | ~~미확인~~ → `Budget` 일부 해석([TK-16](concepts/context-budget.md#TK-16)). 잔여는 OP-H10 |
| <a id="OP-H3"></a>OP-H3 | `glean_call`과 `--gleanings`의 연결, `adjudicate_call`의 호출 조건 | [EW-05](concepts/entity-windows.md#EW-05), [SV-09](concepts/second-verifier.md#SV-09) | ~~미확인~~ → `adjudicate` 호출 관찰. `glean_call` 연결은 미확인, 수용 조건은 OP-H8 |
| <a id="OP-H4"></a>OP-H4 | `--dry-run`의 의미. raw에 `written`이 0이 아닌 값으로 나오고, 1000-entry 한도 오류도 dry-run에서 났다 | [EW-03](concepts/entity-windows.md#EW-03), E:rea/quote/run.py, E:rea/quote/r_exact.raw | 미확인 |
| <a id="OP-H5"></a>OP-H5 | 초안 승인, 초안 → 추출 연결 | [HA-03](concepts/human-approval.md#HA-03), [HA-05](concepts/human-approval.md#HA-05) | ~~실행 전~~ → Stub 경로로 실행됨([HA-10](concepts/human-approval.md#HA-10), [HA-13](concepts/human-approval.md#HA-13)). 잔여는 OP-H9 |
| <a id="OP-H6"></a>OP-H6 | 비 Anthropic 경로의 추출, gRPC Extract | [TK-11](concepts/context-budget.md#TK-11), [SYM-05](concepts/binary-symbols.md#SYM-05) | ~~미실행~~ → 여전히 미실행(R:88) |
| <a id="OP-H7"></a>OP-H7 | `HelixDB/ontology-agent` 소스 접근 | [HX-02](products/helix-foundry.md#HX-02) | 이 세션에서 재확인하지 않음 |
| <a id="OP-A1"></a>OP-A1 | K1b에서 유령 컬럼 저장 0건, compiled_tables=0의 원인 | [AO-K1B](products/auto-ontology.md#AO-K1B) | 미확인 |
| <a id="OP-A2"></a>OP-A2 | A2 첫 실행의 줄 순서 차이 | [AO-X5](products/auto-ontology.md#AO-X5) | 원인 미확인 |
| <a id="OP-M1"></a>OP-M1 | 실제 저성능 로컬 모델의 추출·판정 품질, 실제 토크나이저 토큰 수 | [TK-15](concepts/context-budget.md#TK-15), [M-12](method-and-limits.md#M-12) | 미측정 |
| <a id="OP-M2"></a>OP-M2 | RAGFlow claim 추출 토큰, 파이프라인 실행 | [TK-10](concepts/context-budget.md#TK-10), [DO-04](concepts/document-only-input.md#DO-04) | 미측정 |
| <a id="OP-Q4"></a>OP-Q4 | `text::normalize`의 내용, 임계값 0.95의 raw | [QV-20](concepts/quote-validation.md#QV-20), [QV-23](concepts/quote-validation.md#QV-23), [C-18](contradictions.md#C-18) | 미확인 |
| <a id="OP-H8"></a>OP-H8 | adjudicate 응답을 수용시키는 조건, 호출 조건 | [SV-15](concepts/second-verifier.md#SV-15), [SV-13](concepts/second-verifier.md#SV-13) | **미확인** |
| <a id="OP-H9"></a>OP-H9 | Foundry 백엔드 경로의 승인, 번들 `mappings_toml`의 사용 | [HA-12](concepts/human-approval.md#HA-12), [C-20](contradictions.md#C-20) | 미확인 |
| <a id="OP-H10"></a>OP-H10 | `context_tokens`의 의미, `prompt_bound` 사용처, `continue`의 크기, Go 하한과 `settle`의 관계 | [TK-17](concepts/context-budget.md#TK-17), [TK-18](concepts/context-budget.md#TK-18), [TK-21](concepts/context-budget.md#TK-21), [C-21](contradictions.md#C-21) | 미확인 |
| <a id="OP-H11"></a>OP-H11 | results.md가 해석하지 않은 디컴파일 파일, 출력 없는 함수 | [SYM-19](concepts/binary-symbols.md#SYM-19), [SYM-20](concepts/binary-symbols.md#SYM-20) | 미해석 |
| <a id="OP-M3"></a>OP-M3 | Auto-Ontology 미실행 기능, RAGFlow 미측정 항목, 나머지 도구 | [M-26](method-and-limits.md#M-26), [M-27](method-and-limits.md#M-27), [M-28](method-and-limits.md#M-28) | 미실행 |

## 등급이 [미입증]인 요소 전체

| ID | 요소 | 인용 | 미입증 내용 |
|---|---|---|---|
| [M-01](method-and-limits.md#M-01) | 전수 나열 규칙: 프로젝트 자신의 선언(README 주장, 컴파일 단계, 답변 그래프 노드, 패스)을 나열하며 측정일은 2026-11-06이다 | F:3, F:9 | 선언 목록이 실제로 전수인지는 입증되지 않았다. 패스 목록은 이후 [SYM-02](concepts/binary-symbols.md#SYM-02)에서 늘어났다 |
| [M-02](method-and-limits.md#M-02) | 핵심 판정 규칙: 메커니즘 제거·오류 주입 시 출력이 달라지면 핵심으로 기록한다 | F:10 | 이 규칙은 Stub 입력에 대한 코드 동작 차이만 판정한다. 모델 품질은 판정하지 않는다 |
| [M-03](method-and-limits.md#M-03) | 근거 등급: [실행], [코드], [논문] | F:11 | 해당 없음(표기 규칙). 사실 주장이 아니다 |
| [AO-R3](products/auto-ontology.md#AO-R3) | 시스템 간 정의 조정 | F:78, AO:README.md:14 | findings.md가 미확인으로 기록했다. 직접 근거 없음 |
| [AO-R8](products/auto-ontology.md#AO-R8) | Learn: 인증 수정 환류 | F:83, AO:README.md:17, AO:auto_ontology/semantic/compile.py:99 | 환류 경로가 식별되지 않았다 |
| [AO-X1](products/auto-ontology.md#AO-X1) | 제외: Web UI, RBAC, Vault, PII, Kumo | F:85 | 이 기능들의 동작 전체 |
| [AO-X2](products/auto-ontology.md#AO-X2) | 거치지 않은 노드: `information_agent`, `refine_evidence`, `precheck_combined`, `validate_sql_values`, `kumo_predict` | F:85 | 이 노드들의 동작. `kumo_predict`는 F:55가 인용한 447-463행 범위에 없었다(범위 밖 위치 미확인) |
| [HX-02](products/helix-foundry.md#HX-02) | 이미지 라벨 Apache-2.0, `HelixDB/ontology-agent` 소스 미확인 | F:105, I:9 | 이 세션에서 재확인하지 않았다. 바이너리 소스는 읽히지 않았다 |
| [RF-03](products/paper-ragflow.md#RF-03) | 온톨로지 템플릿(§3.2, Fig.1) | F:170, P:§3.2 (p.txt:277), Fig.1 (p.txt:349), RF:internal/agentic_rag/tool_navigate_structure.go:801 | 템플릿이 공개 저장소 밖에 있는지 없는지는 미확인이다 |
| [QV-14](concepts/quote-validation.md#QV-14) | interim.md의 해석: "바이트 일치가 아니라 정규화 후 비교이며, 같은 섹션 안으로 제한된다" | I:62 | ~~정규화 방식, 유사도 사용 여부, 임계값 모두 미확정이다~~ → 유사도 사용은 [QV-22](concepts/quote-validation.md#QV-22), 임계값은 [QV-23](concepts/quote-validation.md#QV-23). 정규화 방식은 미입증 |
| ~~QV-P1~~ (results.md 갱신: [디컴파일], 잔여 [QV-23](concepts/quote-validation.md#QV-23)) [QV-P1](concepts/quote-validation.md#QV-P1) | ~~인용 대조가 rapidfuzz 유사도 함수를 호출한다는 코디네이터 통지(결과 대기)~~ → `locate_quote`의 rapidfuzz 호출 통지, results.md로 수집됨 | 코디네이터 메시지 2026-11-06. raw 소스 없음 | ~~호출 여부, 함수, 임계값, 대상 validator가 모두 미입증이다. 결과가 새 raw 소스로 들어오면 이 절을 갱신한다~~ → 호출과 함수는 [디컴파일]. 임계값 값은 [QV-23](concepts/quote-validation.md#QV-23), 정규화는 [QV-20](concepts/quote-validation.md#QV-20)이 미입증 |
| [HA-04](concepts/human-approval.md#HA-04) | RAGFlow/논문: 사람 승인 | F:197 | 직접 근거 없음 |
| ~~HA-05~~ (results.md 갱신: [실행/Stub], [HA-13](concepts/human-approval.md#HA-13)) [HA-05](concepts/human-approval.md#HA-05) | 초안 → 추출 연결 | I:85, HF:backend/workers/foundry-graph-worker/task.go:3-5 | ~~연결 전체 미실행~~ → Stub 경로 통과가 실행됐다. 번들 `mappings_toml` 미전달, Foundry 워커 미경유([C-20](contradictions.md#C-20)) |
| ~~SV-09~~ (results.md 갱신: [실행/Stub], 잔여 [SV-15](concepts/second-verifier.md#SV-15)) [SV-09](concepts/second-verifier.md#SV-09) | `adjudicate_call`의 실제 호출 | I:85, I:17 | ~~호출 조건과 역할 모두 미입증이다~~ → 호출은 관찰됐다. 호출 조건과 응답 수용 조건은 **미확인**이다([SV-15](concepts/second-verifier.md#SV-15)) |
| [EM-02](concepts/embedding-targets.md#EM-02) | Helix: 이 범위에서 미확인 | F:192 | 직접 근거 없음 |
| [TK-10](concepts/context-budget.md#TK-10) | RAGFlow claim 추출 | F:213 | 직접 근거 없음 |
| [TK-15](concepts/context-budget.md#TK-15) | 저성능 모델의 추출·판정 품질 | F:218, F:26 | 직접 근거 없음 |
| [SYM-14](concepts/binary-symbols.md#SYM-14) | `extract` Ghidra 분석 진행 중: `text::locate_quote`, `text::normalize`, `Document::sections`, `commit::constrain`, `adjudicate::bounded` 디컴파일 전 | I:83 | ~~이 다섯 함수의 동작 미입증~~ → `locate_quote`는 [QV-20](concepts/quote-validation.md#QV-20)~[QV-23](concepts/quote-validation.md#QV-23). 나머지는 [SYM-19](concepts/binary-symbols.md#SYM-19), [SYM-20](concepts/binary-symbols.md#SYM-20) |
| [SYM-15](concepts/binary-symbols.md#SYM-15) | `ontology-agent` 디컴파일 미착수 | I:84 | ~~동작 전체~~ → 나머지 함수의 동작([M-28](method-and-limits.md#M-28)) |
| [SYM-16](concepts/binary-symbols.md#SYM-16) | 초안 승인, `adjudicate_call` 호출, 초안 → 추출 연결이 실행 전 | I:85 | ~~[HA-03](concepts/human-approval.md#HA-03), [SV-09](concepts/second-verifier.md#SV-09), [HA-05](concepts/human-approval.md#HA-05)~~ → [HA-12](concepts/human-approval.md#HA-12), [SV-15](concepts/second-verifier.md#SV-15), [C-20](contradictions.md#C-20) |
| [CMP-3B](comparison.md#CMP-3B) | Helix: 이 범위에서 미확인 | [EM-02](concepts/embedding-targets.md#EM-02) | 직접 근거 없음 |
| [CMP-8C](comparison.md#CMP-8C) | 논문/RAGFlow: 미확인 | [HA-04](concepts/human-approval.md#HA-04) | 직접 근거 없음 |
| [M-17](method-and-limits.md#M-17) | results.md가 더한 등급 [디컴파일], [바이너리]와 "모델은 전부 Stub" 선언 | R:3, R:5, R:7, R:8 | 해당 없음(표기 규칙). 사실 주장이 아니다 |
| [M-24](method-and-limits.md#M-24) | 추출·판정 품질, 저성능 로컬 모델의 수행 능력 | R:85, R:87, [TK-15](concepts/context-budget.md#TK-15) | 직접 근거 없음 |
| [M-25](method-and-limits.md#M-25) | `extract`의 비-Anthropic 경로, gRPC Extract | R:88, [TK-11](concepts/context-budget.md#TK-11), [SYM-05](concepts/binary-symbols.md#SYM-05) | 다른 프로바이더 경로의 부재를 입증하지 않는다 |
| [M-26](method-and-limits.md#M-26) | Auto-Ontology 미실행 기능(Web UI, RBAC, Vault, PII, Kumo, Ossie, MCP 서버), Learn 경로 | R:89, [AO-X1](products/auto-ontology.md#AO-X1), [AO-R2](products/auto-ontology.md#AO-R2), [AO-R7](products/auto-ontology.md#AO-R7), [AO-R8](products/auto-ontology.md#AO-R8) | 환류 경로가 식별되지 않았다 |
| [M-27](method-and-limits.md#M-27) | RAGFlow 프롬프트 토큰, 온톨로지 템플릿, 사람 승인 | R:90, [TK-10](concepts/context-budget.md#TK-10), [RF-03](products/paper-ragflow.md#RF-03), [HA-04](concepts/human-approval.md#HA-04) | 직접 근거 없음 |
| [M-28](method-and-limits.md#M-28) | `ontology-agent`의 나머지 함수, 스크립트에 넣지 않은 도구 `evaluate`, `preview_extraction`, `dry_run` | R:91 | 동작 전체 |
| [QV-31](concepts/quote-validation.md#QV-31) | raw 29건 판정과 R:21-24 경로의 일치 점검 | E:rea/quote/r_*.raw, E:rea/quote/fuzzy.json, E:rea/quote/doc.md | 가정한 정규화는 입증되지 않았다. 일치는 경로와 값을 입증하지 않으며 모순이 없다는 점만 보여 준다 |
| [EW-10](concepts/entity-windows.md#EW-10) | 상한이 정확히 50,000이라는 추정 | R:66 | 상수 미확인. results.md도 "추정"이라고 쓴다. 창을 만드는 함수 자체가 evidence/에 식별돼 있지 않다 |
| [SV-15](concepts/second-verifier.md#SV-15) | adjudicate 응답을 수용시키는 조건 | R:81, E:rea/adjudicate/stub_adj.py, E:rea/adjudicate/t.py, E:rea/adjudicate/t2.py | **미확인.** 응답 형식 문제인지 다른 조건인지 구분되지 않았다. 추론으로 메우지 않는다 |
| [TK-21](concepts/context-budget.md#TK-21) | `continue`의 새 대화 크기 | R:60 | 직접 근거 없음 |
| [SYM-19](concepts/binary-symbols.md#SYM-19) | results.md에 해석이 없는 파일: `sections.c`, `fold.c`, `tokens.c`, `dec_entity.c`, `dec_fitting.c`, `adj_bounded.c`, `m_maxtokens.c`, `m_runtime.c` | E:rea/decompiled/ | 동작 미해석. 이 위키도 내용을 결론으로 쓰지 않았다 |
| [SYM-20](concepts/binary-symbols.md#SYM-20) | 출력 파일이 없는 함수: `normalize`, `adj_pairing`, `p_entity`, `commit::constrain` | E:rea/ghidra/addrs.txt, I:83 | 동작 미입증. [C-18](contradictions.md#C-18) |


**갱신(2026-11-06):** [OP-H6](#OP-H6)은 gRPC 실행으로 일부 해소([C-24](contradictions.md#C-24)). [OP-M1](#OP-M1)은 문서 2건의 실모델 관찰만 추가되어 미해소([LC-40](knowledge-lifecycle.md#LC-40)~[LC-44](knowledge-lifecycle.md#LC-44)). 새 미해결: 실제 파서를 포함한 RAGFlow 전체 경로, `agentic_rag` 실행(`office_oxide.h` 부재), Helix `Ask`의 실제 답변 완주.

---
[index](index.md) · [coverage](coverage.md)
