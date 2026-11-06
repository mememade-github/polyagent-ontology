# HelixDB/helix-foundry와 ontology-agent 이미지

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

문서 추출은 이미지 안의 바이너리가 수행한다. 관련 개념: [인용 대조](../concepts/quote-validation.md), [엔티티 창](../concepts/entity-windows.md), [근거 위치](../concepts/evidence-spans.md), [뼈대](../concepts/ontology-skeleton-source.md), [사람 승인](../concepts/human-approval.md), [판정](../concepts/second-verifier.md), [심볼](../concepts/binary-symbols.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-01](../contradictions.md#C-01) (세분) Helix 인용 대조 범위
- [C-02](../contradictions.md#C-02) (대체 및 원인 불일치) 초안 완주 여부와 이전 실패 원인
- [C-04](../contradictions.md#C-04) (추가) 추출 패스 구성
- [C-05](../contradictions.md#C-05) (근거 공백) 초안 입력 "최신 5건 + 도구 17개"
- [C-06](../contradictions.md#C-06) (세분) Helix 사람 승인
- [C-11](../contradictions.md#C-11) (인용 정밀도) findings.md의 `backend/api/ontology.go:19`
- [C-12](../contradictions.md#C-12) (재현 근거 공백) "evidence/에 스크립트와 입력이 있다"
- [C-13](../contradictions.md#C-13) (버전 차이) compose 기본 이미지와 저장소 계약
- [C-14](../contradictions.md#C-14) (세분) `extract`의 프로바이더
- [C-16](../contradictions.md#C-16) (미확정) Helix 인용 대조 메커니즘

## 실제 구조

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="HX-01"></a>HX-01 | 저장소 Go 백엔드는 오케스트레이션과 계약만 담고, 초안·추출은 Rust 바이너리 `ontology-agent`, `extract`, `ingest-mapped`가 수행 | [실행/Stub] | F:105, E:helix/run.sh, E:rea/rust-extract.json, HF:backend/workers/foundry-graph-worker/task.go:3-5 | 이미지 `/usr/local/bin` 바이너리가 실행됐다. 워커가 sidecar를 구동한다는 주석이 있다 | 저장소에 추출 로직이 전혀 없다는 부재 주장의 전수 검색 기록은 없다. Rust 여부는 REA가 `inferred`로 표기한 rustc 경로와 심볼 형태에 기댄다 |
| <a id="HX-02"></a>HX-02 | 이미지 라벨 Apache-2.0, `HelixDB/ontology-agent` 소스 미확인 | [미입증] | F:105, I:9 | "인증 없이 접근되지 않음"은 findings.md의 기록이다 | 이 세션에서 재확인하지 않았다. 바이너리 소스는 읽히지 않았다 |
| <a id="HX-03"></a>HX-03 | 프롬프트는 실제 요청 캡처로 확인 | [실행/Stub] | F:105, E:helix/stub2.py (요청을 로그에 기록) | Stub이 요청 본문을 로그에 쓴다 | 캡처 로그는 evidence/에 없다(기록만) |
| <a id="HX-04"></a>HX-04 | `backend/enrichment/`는 문서 처리가 아니라 People 프로필 조회 | [코드] | F:105, HF:backend/enrichment/plan.go, HF:backend/ontologyagent/contract.go:52 | contract.go 주석의 `SourceProfiles`가 People enrichment를 가리킨다 | plan.go는 이 세션에서 앞부분만 읽었다 |
| <a id="HX-05"></a>HX-05 | 초안 흐름: 문서 집합 최신 5건 + 도구 17개 → ontology.toml + mappings.toml → 사람 검토 → 승인 | [실행/Stub] | F:108, I:26, I:28, E:rea/draft/out2.ndjson | 5개 도구를 거친 산출은 [SK-02](../concepts/ontology-skeleton-source.md#SK-02). ~~승인은 [HA-03](../concepts/human-approval.md#HA-03)에서 미실행~~ → 승인 실행은 [HA-10](../concepts/human-approval.md#HA-10) **results.md 갱신:** 승인 실행은 [HA-10](../concepts/human-approval.md#HA-10), 연결은 [HA-13](../concepts/human-approval.md#HA-13) | "도구 17개"와 "최신"의 원시 근거가 evidence/에 없다. 이번 Stub 스크립트가 쓴 도구는 5개이다. [C-05](../contradictions.md#C-05) |
| <a id="HX-06"></a>HX-06 | 추출 흐름: 문서 → 엔티티 패스 → 섹션별 링크 패스 → 코드 검증 → 검증 모델 → 판정 → Helix | [실행/Stub] | F:109, E:helix/report3.raw (`calls`) | `calls`에 `entities` 1, `facts` 3, `judgements` 1이 있다. 섹션 3개에 facts 3회이다 | `glean_call`, `adjudicate_call`의 위치가 이 도식에 없다. [C-04](../contradictions.md#C-04) **results.md 갱신:** `adjudicate` 호출은 [SV-13](../concepts/second-verifier.md#SV-13) |

## 출처

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="HX-07"></a>HX-07 | 문서 경로 `extraction` | [코드] | F:116, HF:backend/ontologyagent/contract.go:49,218 | `SourceDocuments`, `route, access = "extraction"` | 없음(선언 위치 확인) |
| <a id="HX-08"></a>HX-08 | 초안에 보여주는 문서 수 5건 | [코드] | F:117, HF:backend/ontologyagent/generator.go:44-47 | `MaxSetDocuments = 5`. 주석은 Markdown, MDX, plain text, 텍스트가 읽힌 PDF를 든다 | 5건 선택 기준("최신")은 이 행에 없다. [C-05](../contradictions.md#C-05) |
| <a id="HX-09"></a>HX-09 | 문서만으로 초안 허용 | [코드] | F:118, HF:backend/ontologyagent/generator.go:559 | "empty for a version drafted from documents alone" 주석 | 실행 관찰은 [SK-02](../concepts/ontology-skeleton-source.md#SK-02) |
| <a id="HX-10"></a>HX-10 | 저장 레이아웃 | [코드] | F:120, HF:backend/document/document.go:1-16 | `original`, `read/rows.jsonl.gz`, `read/<mode>-<text sha256>.txt`, `extractions/<artifact key>.json.gz` | 이 레이아웃을 쓰는 워커는 실행되지 않았다 |
| <a id="HX-11"></a>HX-11 | 샘플 온톨로지 | [코드] | F:122, HF:backend/sample/acme.json | 키 `ontology_toml`, `mappings_toml` 존재, `[extractions.` 6회 | 샘플로 전체 Foundry 흐름을 실행하지 않았다. 추출 실험은 `ontology.toml`과 키 제거본을 썼다 |
| <a id="HX-12"></a>HX-12 | 테이블 필수 Definition(별도 경로) | [코드] | F:123, HF:backend/ontology/ontology.go:108,115,133, HF:backend/api/ontology.go:254 | `Validate`가 엔티티 필수와 synced table 참조를 검사한다. F:123의 `api/ontology.go:19`는 import 행이고 호출은 254행이다 | [C-11](../contradictions.md#C-11). 이 경로의 실행 관찰 없음 |

## 오류 주입 조건

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="HX-13"></a>HX-13 | 검증 확률 0.95/0.7/0.2 주입, 임계값 accept 0.9, review 0.6 | [실행/Stub] | F:127, E:helix/stub2.py, E:helix/report3.raw | Stub 소스의 `P=[0.95,0.7,0.2]`. 판정 결과는 [SV-01](../concepts/second-verifier.md#SV-01)~[SV-03](../concepts/second-verifier.md#SV-03) | `extract --help` 출력이 evidence/에 없어 기본값은 기록만이다. 경계값 동작은 시험되지 않았다 |

## 오류 주입 결과

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="HX-14"></a>HX-14 | 쓰기 결과 | [실행/Stub] | F:137, E:helix/report3.raw (`written`) | entities 2, evidence 1, facts_created 1, mentions 5, reviews 2로 일치 | `written`의 쓰기가 실제 그래프 상태와 맞는지 읽어 본 기록은 없다 |
| <a id="HX-15"></a>HX-15 | 키가 있는 온톨로지에서 0.95 사실이 `review`(`unresolved`), 쓰기 reviews 4건 | [실행/Stub] | F:140, E:helix/ontology_nokey.toml | 키 제거본의 네 엔티티 모두 created임은 E:helix/report3.raw로 일치. 키 있는 실행의 원시 출력과 `ontology.toml`은 없다(기록만) **results.md 갱신:** 행을 적재하면 이름 일치로 resolved 된 실행이 있다([SV-11](../concepts/second-verifier.md#SV-11)) | 키 있는 타입의 해소 규칙 자체는 읽히지 않았다 |

## 문서만으로

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="HX-16"></a>HX-16 | 추출은 문서와 온톨로지만으로 그래프에 쓴다 | [실행/Stub] | F:144, E:helix/run_nokey.sh, E:helix/report3.raw | `outcome: ingested`, 위 쓰기 수치 | 모델 품질은 측정되지 않았다. 키 있는 타입은 대응 행이 없으면 review로 간다([HX-15](#HX-15)) **results.md 갱신:** 번들 온톨로지로 실행한 기록은 [HA-13](../concepts/human-approval.md#HA-13) |

## report3.raw에만 있는 관찰

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="HX-17"></a>HX-17 | `unmatched`, `origin`, 모델 표기 | [실행/Stub] | E:helix/report3.raw | `unmatched`에 `{quote:"on the call", section:1, suggested_link:"mentioned_on"}`가 있다. `origin`은 `prompt_version:"8"`, `ontology_version:"draft"`이다. 모델 이름은 `anthropic/stub-e@high`이다 | `unmatched`가 이후 어떻게 쓰이는지 관찰되지 않았다. findings.md에 언급 없음 |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
- [C-20](../contradictions.md#C-20) (범위) "전 구간 연결"과 Foundry 경로
