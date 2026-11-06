# REA 도입 중간 결과 (2026-11-06)

`findings.md` 이후 수행한 실험의 원본 기록이다. 모델은 전부 Stub이므로 코드 동작만 증명하고, 모델 품질은 증명하지 않는다.

## 도구

- REA: `rea-agents` 6.8.0, `morluto/rea` `c467cf86`. 스크래치패드에 CLI만 설치했고 에이전트 설정은 변경하지 않았다.
- Ghidra 12.1.4 (게시된 SHA-256과 일치), Temurin JDK 21.0.13. `rea doctor --provider ghidra` healthy.
- 대상 이미지: `ghcr.io/helixdb/ontology-agent:latest`, 라벨 Apache-2.0.
- `rust-*.json`은 REA `inspect-rust-binary` 출력이다. `auditable_metadata`는 null이다.

## 정적 관찰 [심볼 표, `nm -C`]

`extract`는 스트립되지 않았다 (`.symtab` 있음, 37,626개 심볼). 디컴파일은 아직 수행하지 못했다. 아래는 함수 이름 근거이며 함수 내부 동작의 근거가 아니다.

- `extraction` 크레이트 모듈: `adjudicate`, `attribute`, `commit`, `decision`, `document`, `fact`, `pipeline`, `prompt`, `query`, `roster`, `scope`, `store`, `text`, `verify`.
- 프롬프트 함수: `prompt::{entity_call, link_call, verify_call, glean_call, adjudicate_call}`. `findings.md`에 없던 `glean_call`, `adjudicate_call`이 있다.
- `extract`의 LLM 구체 타입은 `Cached<Limited<Anthropic>>`만 보인다 (`extract::ingest_all`, `llm::anthropic::*`). 심볼 중 ollama/openai 일치는 1건이고 내용은 확인하지 않았다.
- `ontology-agent`에는 `llm::provider`, `llm::wire`, `agent::driver::Budget::{prompt_bound, room, near, exhausted}`, `agent::guard::LeakGuard`, `agent::lint::lint`, `agent::policy::check`, `agent::bundle::approve`가 있다.
- `ontology-agent` 문자열: "the conversation filled the context window; `continue` resumes in a fresh one", "the conversation is too long for the model".

프로바이더 문자열: `anthropic, openai, azure_openai, bedrock, ollama, openai_compatible`.

## 실행 1: 문서만으로 초안 완성 [실행, `draft/`]

스크립트 Stub이 정해진 도구 호출을 보냈다: `list_sources → read_text → put_items → check_draft → finish`. 실패 원인이던 스트리밍 미지원을 SSE로 해결했다.

- 결과 status `done`, 도구 5회. `ontology_toml`에 Customer, Promise, promised_to가 있고 `mappings_toml`에 `[extractions.calls]`가 있다. `bundle`은 null이다.
- 이 초안의 내용은 Stub 스크립트가 작성했다. 증명된 것은 "문서 소스만으로 초안 경로가 끝까지 통과한다"는 것뿐이며, 모델이 이런 초안을 만들 수 있다는 것이 아니다.

코드가 모델 출력을 막은 사례:

| 입력 | 결과 |
|---|---|
| 항목 이름 `extraction.docs` (소스 이름과 같음) | `put_items` 거부, `leak`: "the name contains the source name `docs`", 초안 불변 |
| 문서 라우트 없이 `finish` | 거부: "document sets have no route or draft item to explain why" |
| 잔여 호출 2회 | 사용자 메시지로 예산 임박 안내가 주입됨 |

## 실행 2: context_tokens와 보고된 사용량 [실행]

`context_tokens=8000`, Stub이 `prompt_tokens`를 7000/8000/9000으로 보고한 3회 모두 status `done`, 모델 호출 5회. 이 범위에서는 초과가 턴을 멈추지 않았다. `Budget`의 동작은 디컴파일 전이라 미확인이다.

## 실행 3: 인용 대조 12변형 [실행, `quote/`]

같은 사실에 인용만 바꿔 `extract --dry-run`을 돌렸다. 검증 확률은 0.95로 고정했다.

| 변형 | 판정 | span |
|---|---|---|
| 원문 그대로 | accept | 26–71 |
| 대문자 | accept | 26–71 |
| 공백·줄바꿈 다름 | accept | 26–71 |
| `%` 제거 | accept | 26–72 |
| 전각 `％` | accept | 26–71 |
| 단어 중간에서 시작·끝 | accept | 27–69 |
| 한국어 NFC | accept | 102–150 |
| 한국어 NFD | accept | 102–150 |
| `...`로 생략 | reject `quote_not_in_source` | |
| 의역 | reject `quote_not_in_source` | |
| 다른 섹션의 문장 | reject `quote_not_in_source` | |
| 한국어 띄어쓰기 제거 | reject `quote_not_in_source` | |

즉 대조는 바이트 일치가 아니라 정규화 후 비교이며, 같은 섹션 안으로 제한된다. `findings.md`의 "문서에 없는 인용" 행은 이 범위로 세분된다.

## 실행 4: 엔티티 창 [실행, `window/`]

550,798바이트 ASCII 문서(600문단), `cl100k` 토큰. 호출 순서는 동시 실행 때문에 뒤섞여 있다.

| 옵션 | 창당 본문 바이트 | 창당 토큰 | 엔티티 호출 | 링크 호출 |
|---|---:|---:|---:|---:|
| 기본 (`--max-section-bytes 4000`) | 47,735 (마지막 25,703) | 8,519–8,525 | 12 | 150 |
| `--max-section-bytes 1000` | 49,571 (마지막 5,507) | 8,827–8,837 | 12 | 600 |
| `--max-section-bytes 20000` | 38,555 (한 창 49,571) | 6,967–6,975 (한 창 8,835) | 14 | 29 |
| `--gleanings 1` | 47,735 (마지막 25,703) | 8,519–8,525 | 12 | 300 |

- 엔티티 창은 바이트 단위로 약 50KB 이내이고 섹션 단위로 묶인다. 정확한 상한 상수는 미확인이다.
- `--max-section-bytes`는 섹션을 바꾸므로 엔티티 창 크기에도 영향을 주지만, 창 상한을 직접 조절하지는 못한다. 작게 해도 창은 오히려 49,571로 커졌다.
- 같은 바이트 상한이라도 언어에 따라 토큰이 다르다: ASCII 약 8,500, `findings.md`의 한국어 문서는 최대 18,756.
- `--gleanings 1`은 링크 호출을 150에서 300으로 두 배로 늘렸다.
- `--max-section-bytes 1000`은 rc=1: "the write has 1202 entries, over the 1000-entry batch limit".

## 미완료

- `extract` Ghidra 분석 진행 중. `text::locate_quote`, `text::normalize`, `Document::sections`, `commit::constrain`, `adjudicate::bounded` 디컴파일 전.
- `ontology-agent` 디컴파일 미착수.
- 초안 승인(`agent::bundle::approve`), `adjudicate_call` 실제 호출, 초안 → 추출 연결 실행 전.
