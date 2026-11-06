# REA 도입 실증 결과 (2026-11-06)

`interim.md` 이후 결과이며 `interim.md`의 미완료 항목을 갱신한다. 모델은 전부 Stub이므로 코드 동작만 증명한다.

근거 등급에 다음을 더한다.

- **[디컴파일]** Ghidra 의사코드를 읽은 해석. 이름이 없는 변수를 해석했으므로 [실행]보다 약하다.
- **[바이너리]** 바이너리에서 값을 직접 읽음.

## 도구 경로

- REA `decompile`은 사용 불가했다: 저장 프로젝트를 지정해도 300초 시작 제한에 걸렸다 (`provider_timeout`).
- 디컴파일은 같은 Ghidra로 수행했다: `ghidra/DecAddrs.java`, 주소는 `nm` 값에 이미지 베이스를 더했다.
- `extract` 자동 분석은 1500초 제한에 걸려 **미완료 상태로 저장**됐다. `ontology-agent`는 분석 없이 가져와 함수 단위로 디스어셈블했다. 그래서 일부 점프 테이블 복원이 깨진다 (`adj_choices.c`).
- REA 내장 명령 중 `inspect-rust-binary`, `inspect-artifact`, `doctor`만 실제 결과에 기여했다.

## 1. 인용 대조: `extraction::text::locate_quote` (`extract`)

[디컴파일, `decompiled/extract/locate_quote.c`], [바이너리, `.rodata` 상수]

1. 인용을 `text::normalize`로 정규화한다. 3글자 미만이면 찾지 못한 것으로 처리한다.
2. 섹션 본문을 정규화하고 정규화 문자열에서 정확 검색한다.
3. 정확 검색 결과가 없으면 어절 수 n−1..n+1의 창을 밀며 `rapidfuzz` indel `normalized_similarity` 최댓값을 구한다.
4. 최댓값이 **0.95 이상**이면 그 창의 원본 바이트 범위를 span으로 돌려준다.

[실행, `quote/run2.py`, `quote/fuzzy.json`]: 끝의 글자를 X로 바꾼 변형은 1글자 accept, 2글자 이상 reject. 앞 단어를 `zzzz`로 바꾼 변형은 전부 reject. 오타 2개 인용 accept. 단어 하나 `Globex` accept, span 44–50.

- `interim.md`의 span 26–72 (`%` 제거)는 이 퍼지 경로로 찾은 창이 뒤의 쉼표까지 포함한 것과 일치한다. 같은 span이 `char1`, `typo_mid`에서도 나왔다. 퍼지 경로가 원인이라는 것은 해석이다.
- 대조 범위가 인용이 나온 섹션 하나인지는 `other_section` reject로 관찰했다.
- 낮은 품질 인용이 통과하는 경로: 임의의 짧은 단어 인용도 그 섹션에 있으면 통과한다. 사실이 맞는지는 검증 모델 몫이다.

## 2. 초안 승인 게이트 [실행, `approval/`]

| 입력 | 모델 호출 | 결과 |
|---|---:|---|
| `approve` 잘못된 rev | 0 | `stale_draft` |
| `approve` 항목 미승인 | 0 | `invalid_input`, 항목별 `policy`: "`type.Customer` is not approved" |
| `feedback` 항목별 approve 5건 | 0 | `done`, rev 1→2, 항목 status `approved` |
| `feedback` comment | 5 | 코멘트가 모델 입력에 포함됨. 승인 항목에 대한 `put_items`는 거부: `locked`, "`type.Customer` is locked by the user" |
| `approve` 전 항목 승인 후 | 0 | `approved`, bundle 생성 |

bundle 필드: `version`, `parent`, `sha256`, `ontology_toml`, `mappings_toml`, `review_json`, `impact`, `agent_version`.

- 저장소 Go 계약은 `start`만 표현한다 (`backend/ontologyagent/contract.go:244-247`). 바이너리 스키마는 `start`, `feedback`, `continue`, `approve`를 선언한다 (`backend/pb/proto/ontology_agent/v1/schema/turn_request.json`). 위 실행은 바이너리에 직접 보냈으며, Foundry 백엔드를 거치지 않았다.

## 3. 전 구간 연결 [실행, `approval/e2e.out`]

문서 → 초안(Stub 스크립트) → 항목 승인 → 초안 승인 → 번들 → `extract --ontology bundle_ontology.toml` → HelixDB 쓰기.

결과: `outcome ingested`, entities 2, evidence 1, facts_created 1, mentions 5. 검증 판정 accept, span 26–71, `ontology_version 2026-11-06.1`.

Stub이 답을 정해 준 실행이므로 경로의 통과만 증명한다. `extract`에는 ontology 파일만 넘겼고 번들의 `mappings_toml`은 넘기지 않았다.

## 4. 컨텍스트 제한 [실행+디컴파일]

- `Budget::exhausted`는 스텝 수, 비용, 경과 시간만 비교한다 [디컴파일, `b_exhausted.c`].
- `Budget::prompt_bound`는 요청 본문 바이트에서 어떤 값을 뺀 뒤 2로 나눈 올림을 계산한다 [디컴파일, `b_prompt_bound.c`]. 이 값의 사용처는 확인하지 않았다.
- `ModelSpec::settle`은 Ollama 경로에서 컨텍스트 기본값 **0x10000 (65,536)**을 쓰고 모델 정보 값과 비교해 줄인다 [디컴파일, `m_settle.c`]. `backend/ai/validate.go:34,85`의 65,536과 같은 값이다. 양쪽의 관계는 확인하지 않았다.
- 서버가 400 `context_length_exceeded`를 반환하면 호출 1회 후 경고 "the conversation is too long for the model; `continue` resumes in a fresh one"과 함께 `budget_exhausted`로 끝난다 [실행, `approval/over.out`].
- 초안의 시스템 메시지만 73,350자이다 [실행, `approval/sys.txt`]. `continue`의 새 대화 크기는 측정하지 않았다.

## 5. 엔티티 창 상한 [실행, `window/run3.py`]

99바이트 문단 3,000개, `--max-section-bytes 500`에서 창 본문 최대 **49,994**바이트. 기본값에서는 47,519. `interim.md`의 관측 최대 49,571을 포함해 모두 50,000 미만이다.

상한이 정확히 50,000이라는 것은 관측과 맞는 추정이다. `objdump` 즉치값에서 0xc350과 0xc34f를 찾지 못해 상수는 확인하지 못했다.

`--max-section-bytes 500`도 rc=1: "the write has 1202 entries, over the 1000-entry batch limit".

## 6. 엔티티 해소와 adjudicate [실행, `adjudicate/`]

`ingest-mapped`로 `Account{A-100, Globex}`를 적재했다. `sources` 형식은 `[{"id","trust","access":{"kind":"file","path","format":{"kind":"jsonl"}}}]`이다.

| 문서 엔티티 이름 | adjudicate 호출 | 결과 |
|---|---|---|
| `Globex` (이름 일치) | 없음 | resolved, by `name`, key `sA-100`, 판정 accept |
| `Initech` (무관) | 없음 | unresolved, 판정 review |
| `Globex Inc` (부분 일치) | 있음 | unresolved |
| `Globex renewal` (부분 일치) | 있음 | unresolved |

adjudicate 프롬프트와 스키마를 캡처했다. `Globex Inc`에 대해 confidence 0.89/0.90/0.95/1.0, choice null, 배열 형식 응답을 시도했으나 **모두 unresolved**였다. 응답을 수용시키는 조건은 **미확인**이다. 응답 형식 문제인지 다른 조건인지 구분하지 못했다. `adj_choices.c`는 점프 테이블 복원이 깨져 판단 근거로 쓰지 못했다.

## 7. REA로 해결되지 않는 항목

바이너리 분석 대상이 아니므로 이번 작업에서 달라지지 않았다.

- 추출·판정 품질, 저성능 로컬 모델의 수행 능력: 실제 모델 실행 필요.
- `extract`의 비-Anthropic 경로: 심볼상 Anthropic 구체 타입만 보였으나, gRPC Extract 경로는 실행하지 않았다.
- Auto-Ontology 미실행 기능 (Web UI, RBAC, Vault, PII, Kumo, Ossie, MCP 서버), Learn 경로: 소스가 공개되어 있어 실행 문제이다.
- RAGFlow: 프롬프트 토큰 미측정, 온톨로지 템플릿 미확인, 사람 승인 미확인: 소스가 공개되어 있다.
- `ontology-agent`의 나머지 함수, 스크립트에 넣지 않은 도구(`evaluate`, `preview_extraction`, `dry_run`)의 동작.

## 재현 시 주의

`Ghidra` 프로젝트, 업스트림 클론, 스크래치패드 스크립트 일부는 휘발성이다. HelixDB 컨테이너 등 실험 컨테이너는 제거했다.
