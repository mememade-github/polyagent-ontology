# 바이너리 심볼과 문자열

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

**이 페이지의 [심볼] 행은 이름과 문자열 근거이다. 함수 내부 동작의 근거가 아니다(I:14).** `rust-*.json`은 함수와 런타임 동작을 복원하지 않는다고 스스로 밝힌다. 관련: [Helix](../products/helix-foundry.md), [미해결 항목](../open-items.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-04](../contradictions.md#C-04) (추가) 추출 패스 구성
- [C-14](../contradictions.md#C-14) (세분) `extract`의 프로바이더

## extract

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SYM-01"></a>SYM-01 | `extract`가 스트립되지 않음, `.symtab` 37,626개 심볼, 디컴파일 전 | [심볼] | I:14 | interim.md의 기록. `nm` 출력은 evidence/에 없다 | 함수 내부 동작의 근거가 아니다 |
| <a id="SYM-02"></a>SYM-02 | `extraction` 크레이트 모듈 14개: `adjudicate`, `attribute`, `commit`, `decision`, `document`, `fact`, `pipeline`, `prompt`, `query`, `roster`, `scope`, `store`, `text`, `verify` | [심볼] | I:16 | 이름 목록뿐이다 | 각 모듈의 동작 미확인 |
| <a id="SYM-03"></a>SYM-03 | `prompt::{entity_call, link_call, verify_call, glean_call}` | [심볼] | I:17 | 이름뿐이다. findings.md에 없던 `glean_call`이 있다. [C-04](../contradictions.md#C-04) | 동작 근거가 아니다. `--gleanings`와의 연결은 입증되지 않았다([EW-05](entity-windows.md#EW-05)) |
| <a id="SYM-04"></a>SYM-04 | `prompt::adjudicate_call` | [심볼] | I:17, I:85 | 이름뿐이다. ~~호출은 실행 전이다~~ → `calls`의 `adjudicate`가 관찰됐다([SV-13](second-verifier.md#SV-13)) | ~~[SV-09](second-verifier.md#SV-09)~~ → 호출 관찰 [SV-13](second-verifier.md#SV-13), 수용 조건은 [SV-15](second-verifier.md#SV-15) |
| <a id="SYM-05"></a>SYM-05 | LLM 구체 타입 `Cached<Limited<Anthropic>>`, `extract::ingest_all`, `llm::anthropic::*` | [심볼] | I:18 | 심볼 중 ollama/openai 일치 1건, 내용 미확인이다. [C-14](../contradictions.md#C-14) | 다른 프로바이더 경로의 부재를 입증하지 않는다 |

## ontology-agent

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SYM-06"></a>SYM-06 | `llm::provider`, `llm::wire` | [심볼] | I:19 | 이름뿐이다 | ~~동작 미확인. 디컴파일 미착수(I:84)~~ → 동작 미확인. 이 이름의 c 파일이 evidence/에 없다 |
| <a id="SYM-07"></a>SYM-07 | `agent::guard::LeakGuard` | [심볼] | I:19 | 이름뿐이다. [SK-04](ontology-skeleton-source.md#SK-04)의 `leak`과 이름이 비슷하다 | [SK-04](ontology-skeleton-source.md#SK-04)와 같은 코드인지 입증되지 않았다 |
| <a id="SYM-08"></a>SYM-08 | `agent::driver::Budget::{prompt_bound, room, near, exhausted}` | [심볼] | I:19 | 이름뿐이다 | [TK-14](context-budget.md#TK-14), [SK-06](ontology-skeleton-source.md#SK-06)와 같은 코드인지 입증되지 않았다 **results.md 갱신:** [TK-16](context-budget.md#TK-16), [TK-17](context-budget.md#TK-17), [SYM-17](#SYM-17), [SYM-18](#SYM-18) |
| <a id="SYM-09"></a>SYM-09 | `agent::lint::lint`, `agent::policy::check` | [심볼] | I:19 | 이름뿐이다. `lint: []`는 E:rea/draft/out2.ndjson에 있다 | 동작 미확인 |
| <a id="SYM-10"></a>SYM-10 | `agent::bundle::approve` | [심볼] | I:19, I:85 | 이름뿐이다. ~~실행 전이다~~ → `approve` 입력은 실행됐다([HA-10](human-approval.md#HA-10)) | [HA-03](human-approval.md#HA-03) **results.md 갱신:** `approve` 입력 실행은 [HA-10](human-approval.md#HA-10). 이 함수가 그 코드인지는 입증되지 않았다 |
| <a id="SYM-11"></a>SYM-11 | 문자열 "the conversation filled the context window; `continue` resumes in a fresh one" | [심볼] | I:20 | 바이너리 문자열이다 | 어떤 조건에서 나오는지 미관찰 **results.md 갱신:** [TK-19](context-budget.md#TK-19)의 경고가 비슷한 문장이나, "filled the context window" 문장은 관찰되지 않았다 |
| <a id="SYM-12"></a>SYM-12 | 문자열 "the conversation is too long for the model" | ~~[심볼]~~ → [실행/Stub] ([TK-19](context-budget.md#TK-19)) | I:20 | 바이너리 문자열이다 | ~~어떤 조건에서 나오는지 미관찰~~ → 서버 400에서 나왔다([TK-19](context-budget.md#TK-19)). 다른 조건은 미관찰 |
| <a id="SYM-13"></a>SYM-13 | 프로바이더 문자열 `anthropic, openai, azure_openai, bedrock, ollama, openai_compatible` | [심볼] | I:22, E:helix/turn_a.json, E:rea/draft/out2.ndjson | 문자열 목록. `openai_compatible` 초안 경로는 out2.ndjson에서 실행 관찰됐다 | 나머지 프로바이더는 미실행이다 |

## 미완료

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SYM-14"></a>SYM-14 | `extract` Ghidra 분석 진행 중: `text::locate_quote`, `text::normalize`, `Document::sections`, `commit::constrain`, `adjudicate::bounded` 디컴파일 전 | [미입증] | I:83 | 함수 이름만 알려져 있다 **results.md 갱신:** `locate_quote`, `sections`, `adjudicate::bounded`는 c 파일이 있다. 분석은 미완료 저장이다([M-20](../method-and-limits.md#M-20)) | ~~이 다섯 함수의 동작 미입증~~ → `locate_quote`는 [QV-20](quote-validation.md#QV-20)~[QV-23](quote-validation.md#QV-23). 나머지는 [SYM-19](#SYM-19), [SYM-20](#SYM-20) |
| <a id="SYM-15"></a>SYM-15 | `ontology-agent` 디컴파일 미착수 | [미입증] | I:84 | 미착수로 기록됐다 **results.md 갱신:** 함수 단위로 일부를 디컴파일했다([TK-16](context-budget.md#TK-16)~[TK-18](context-budget.md#TK-18)) | ~~동작 전체~~ → 나머지 함수의 동작([M-28](../method-and-limits.md#M-28)) |
| <a id="SYM-16"></a>SYM-16 | 초안 승인, `adjudicate_call` 호출, 초안 → 추출 연결이 실행 전 | [미입증] | I:85 | 실행 전으로 기록됐다 **results.md 갱신:** 세 항목 모두 실행 기록이 생겼다([HA-10](human-approval.md#HA-10), [SV-13](second-verifier.md#SV-13), [HA-13](human-approval.md#HA-13)) | ~~[HA-03](human-approval.md#HA-03), [SV-09](second-verifier.md#SV-09), [HA-05](human-approval.md#HA-05)~~ → [HA-12](human-approval.md#HA-12), [SV-15](second-verifier.md#SV-15), [C-20](../contradictions.md#C-20) |

## results.md 수집: 해석되지 않은 파일
| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SYM-17"></a>SYM-17 | `Budget::near` | [디컴파일] | E:rea/decompiled/ontology-agent/b_near.c | 스텝 값에 2를 더해 비교하는 분기가 있다. 이 위키의 읽기이며 results.md에는 해석이 없다 | [SK-06](ontology-skeleton-source.md#SK-06)의 "잔여 호출 2회"와 같은 코드인지 입증되지 않았다 |
| <a id="SYM-18"></a>SYM-18 | `b_room.c` | [디컴파일] | E:rea/decompiled/ontology-agent/b_room.c:4, E:rea/ghidra/addrs-oa.txt | 함수 이름은 `Budget::room_before`이다. 주소 목록은 `b_room_before`와 `b_room`을 같은 주소로 둔다. I:19는 `room`으로 적는다. [C-22](../contradictions.md#C-22) | 동작은 results.md도 이 위키도 해석하지 않았다 |
| <a id="SYM-19"></a>SYM-19 | results.md에 해석이 없는 파일: `sections.c`, `fold.c`, `tokens.c`, `dec_entity.c`, `dec_fitting.c`, `adj_bounded.c`, `m_maxtokens.c`, `m_runtime.c` | [미입증] | E:rea/decompiled/ | 파일은 있으나 해석 기록이 없다. `dec_entity.c`, `m_runtime.c`에 점프 테이블 경고가 있다 | 동작 미해석. 이 위키도 내용을 결론으로 쓰지 않았다 |
| <a id="SYM-20"></a>SYM-20 | 출력 파일이 없는 함수: `normalize`, `adj_pairing`, `p_entity`, `commit::constrain` | [미입증] | E:rea/ghidra/addrs.txt, I:83 | 앞의 세 함수는 주소 목록에 있으나 c 파일이 없다. `commit::constrain`은 I:83에 있으나 주소 목록과 c 파일에 없다 | 동작 미입증. [C-18](../contradictions.md#C-18) |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
- [C-18](../contradictions.md#C-18) (근거 공백) `normalize` 내용과 I:83의 디컴파일 목록
- [C-22](../contradictions.md#C-22) (세분) REA 상태와 심볼 이름
