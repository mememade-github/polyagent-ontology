# 사람 승인

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

사람 개입 지점의 기록이다. ~~승인 실행은 관찰되지 않았다.~~ → **results.md 갱신:** 스크립트가 바이너리에 직접 보낸 승인은 실행됐다. 사람과 Foundry 경로의 승인은 관찰되지 않았다. 관련: [뼈대](ontology-skeleton-source.md), [판정](second-verifier.md), [Auto-Ontology](../products/auto-ontology.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-06](../contradictions.md#C-06) (세분) Helix 사람 승인
- [C-09](../contradictions.md#C-09) (주장과 코드 불일치) README "certified definitions로 쿼리 검증"

## 시스템별

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="HA-01"></a>HA-01 | Auto-Ontology: 인증 플래그 | [실행/Stub] | F:197, F:80, AO:README.md:196,228-233, AO:auto_ontology/dal/terms.py:156 | 답변 프롬프트 영향 없음(기록만). `_certification`은 집계 표시 함수이다 | [AO-R5](../products/auto-ontology.md#AO-R5) |
| <a id="HA-02"></a>HA-02 | Helix: review 판정 | [실행/Stub] | F:197, E:helix/report3.raw | `written.reviews` 2, `low_confidence`, 키 있는 온톨로지의 `unresolved` | 검토 큐를 사람이 처리하는 경로는 실행되지 않았다 |
| <a id="HA-03"></a>HA-03 | Helix: 초안 승인 | ~~[코드]~~ → [코드] + [실행/Stub] ([HA-06](#HA-06)~[HA-11](#HA-11)) | F:108, F:197, I:85, HF:README.md:63,74, HF:backend/ontologyagent/contract.go:265,350, HF:backend/pb/proto/ontology_agent/v1/schema/turn_request.json (`approve`) | README는 사람이 검토·편집하고 버전을 current로 만든다고 쓴다. 계약에 `StatusApproved`와 `Bundle`, 입력 키 `approve`가 있다. 실행 관찰은 항목 `status: proposed`, `bundle` null(E:rea/draft/out2.ndjson)까지이다. [C-06](../contradictions.md#C-06) | ~~승인은 실행되지 않았다(I:85). 사람 승인이 필수 게이트인지 미입증이다~~ → 바이너리에 스크립트로 직접 보낸 승인이 실행됐고 미승인 항목은 거부됐다([HA-07](#HA-07), [HA-10](#HA-10)). 사람과 Foundry 경로의 승인은 미입증이다([HA-12](#HA-12)) |
| <a id="HA-04"></a>HA-04 | RAGFlow/논문: 사람 승인 | [미입증] | F:197 | findings.md가 미확인으로 기록했다 | 직접 근거 없음 |
| <a id="HA-05"></a>HA-05 | 초안 → 추출 연결 | ~~[미입증]~~ → [실행/Stub] ([HA-13](#HA-13)) | I:85, HF:backend/workers/foundry-graph-worker/task.go:3-5 | 주석: "a load's Ingest writes an approved version's tables ... then Extract adds the ontology's documents". ~~실행 전이다~~ → Stub 경로로 실행됐다([HA-13](#HA-13)) | ~~연결 전체 미실행~~ → Stub 경로 통과가 실행됐다. 번들 `mappings_toml` 미전달, Foundry 워커 미경유([C-20](../contradictions.md#C-20)) |

## results.md: 승인 게이트 실행

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="HA-06"></a>HA-06 | `approve` 잘못된 rev | [실행/Stub] | R:36, E:rea/approval/a0_wrongrev.out, E:rea/approval/appr.py | `stale_draft`, usage 0 | 호출 수 로그는 evidence/에 없고 usage 0으로 확인된다 |
| <a id="HA-07"></a>HA-07 | `approve` 항목 미승인 | [실행/Stub] | R:37, E:rea/approval/a1.out | `invalid_input`, 항목별 `policy`: "`type.Customer` is not approved", usage 0 | 없음(이 입력에 한함) |
| <a id="HA-08"></a>HA-08 | `feedback` 항목별 approve 5건 | [실행/Stub] | R:38, E:rea/approval/f1.out, E:rea/approval/appr2.py | `done`, rev 2, 항목 status `approved`, `decisions`가 `locked`, usage 0 | 승인 입력은 스크립트가 보냈다. 사람이 판단한 실행이 아니다 |
| <a id="HA-09"></a>HA-09 | `feedback` comment와 승인 항목 잠금 | [실행/Stub] | R:39, E:rea/approval/c1.out, E:rea/approval/sys.txt:83,532 | 모델 호출 usage 5단계. `put_items`가 `ok:false`, "error: rejected, the draft unchanged". 항목 status 유지. comment는 state의 `log`에 있다 | R:39가 인용한 "is locked by the user" 문장과 "코멘트가 모델 입력에 포함됨"은 raw에 없다(기록만). [C-17](../contradictions.md#C-17) |
| <a id="HA-10"></a>HA-10 | `approve` 전 항목 승인 후 | [실행/Stub] | R:40, E:rea/approval/a2.out, E:rea/approval/approved.json | `approved`, bundle 생성, usage 0, rev 3 | 없음(이 입력에 한함) |
| <a id="HA-11"></a>HA-11 | bundle 필드 | [실행/Stub] | R:42, E:rea/approval/a2.out, E:rea/approval/bundle_ontology.toml, E:rea/approval/bundle_mappings.toml | `version`, `parent`, `sha256`, `ontology_toml`, `mappings_toml`, `review_json`, `impact`, `agent_version`로 일치. `version`은 `2026-11-06.1` | `review_json`, `impact`의 의미는 읽히지 않았다 |
| <a id="HA-12"></a>HA-12 | 저장소 Go 계약은 `start`만, 바이너리 스키마는 `start`, `feedback`, `continue`, `approve` | [코드] | R:44, HF:backend/ontologyagent/contract.go:244-247, HF:backend/pb/proto/ontology_agent/v1/schema/turn_request.json | 주석 "Foundry sends only starts"와 `Input{Start}`를 확인했다. 스키마의 네 키도 확인했다. 위 실행은 바이너리에 직접 보냈다 | Foundry에서 승인이 실제로 어떤 경로로 일어나는지 미확인이다. [C-20](../contradictions.md#C-20) |

## results.md: 전 구간 연결

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="HA-13"></a>HA-13 | 문서 → 초안 → 항목 승인 → 초안 승인 → 번들 → `extract --ontology` → HelixDB 쓰기 | [실행/Stub] | R:48, R:50, R:52, E:rea/approval/e2e.out, E:rea/approval/e2e.sh, E:rea/approval/stub_e2e.py | `outcome ingested`, entities 2, evidence 1, facts_created 1, mentions 5, 판정 accept, span 26–71, `ontology_version 2026-11-06.1`로 일치. `e2e.sh`에 `--dry-run`이 없다 | Stub이 답을 정한 경로 통과뿐이다. 번들의 `mappings_toml`은 넘기지 않았다. 쓰인 그래프를 읽은 기록이 없다. [C-20](../contradictions.md#C-20) |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
- [C-17](../contradictions.md#C-17) (인용과 raw 불일치) R:39의 잠금 문장과 모델 입력 주장
- [C-20](../contradictions.md#C-20) (범위) "전 구간 연결"과 Foundry 경로
