# 방법, 대상 버전, 실험 공통 한계

> 등급과 인용 표기는 [SCHEMA](SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

판정 규칙, 대상 버전, 모든 실험에 걸리는 한계를 모은다.

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](contradictions.md)에 있다.

- [C-12](contradictions.md#C-12) (재현 근거 공백) "evidence/에 스크립트와 입력이 있다"
- [C-13](contradictions.md#C-13) (버전 차이) compose 기본 이미지와 저장소 계약

## 판정 방법

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="M-01"></a>M-01 | 전수 나열 규칙: 프로젝트 자신의 선언(README 주장, 컴파일 단계, 답변 그래프 노드, 패스)을 나열하며 측정일은 2026-11-06이다 | [미입증] | F:3, F:9 | findings.md가 규칙으로 선언한다. 규칙 자체의 준수를 검사한 실행 기록은 없다 | 선언 목록이 실제로 전수인지는 입증되지 않았다. 패스 목록은 이후 [SYM-02](concepts/binary-symbols.md#SYM-02)에서 늘어났다 |
| <a id="M-02"></a>M-02 | 핵심 판정 규칙: 메커니즘 제거·오류 주입 시 출력이 달라지면 핵심으로 기록한다 | [미입증] | F:10 | 규칙 선언. 적용 사례는 [AO-K0](products/auto-ontology.md#AO-K0)~[AO-K6](products/auto-ontology.md#AO-K6), [SV-01](concepts/second-verifier.md#SV-01)~[SV-05](concepts/second-verifier.md#SV-05) | 이 규칙은 Stub 입력에 대한 코드 동작 차이만 판정한다. 모델 품질은 판정하지 않는다 |
| <a id="M-03"></a>M-03 | 근거 등급: [실행], [코드], [논문] | [미입증] | F:11 | 이 위키는 여기에 [심볼]과 [미입증] 표기를 더했다. 정의는 [SCHEMA.md](SCHEMA.md) | 해당 없음(표기 규칙). 사실 주장이 아니다 |

## 대상 버전

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="M-04"></a>M-04 | NVIDIA/auto-ontology `c4495670` | [실행] | F:17, 클론 `git rev-parse` 2026-11-06 | 클론 HEAD가 `c4495670`이다 | 클론은 휘발성 스크래치패드에 있다 |
| <a id="M-05"></a>M-05 | HelixDB/helix-foundry `c7de4051` | [실행] | F:18, 클론 `git rev-parse` 2026-11-06 | 클론 HEAD가 `c7de4051`이다 | 클론은 휘발성 스크래치패드에 있다 |
| <a id="M-06"></a>M-06 | ontology-agent 이미지 `latest`, revision `9e1b6284`, 계약 4.7.0 | [실행/Stub] | F:19, HF:backend/ontologyagent/contract.go:21, E:rea/draft/out2.ndjson 1행 | out2.ndjson의 `contract_version`이 4.7.0이고 저장소 상수도 4.7.0이다 | revision `9e1b6284`와 이미지 digest를 보여 주는 원시 기록은 evidence/에 없다(기록만) |
| <a id="M-07"></a>M-07 | 대조 이미지 `0.1.0`, revision `e1e5a083`, 계약 4.1.1 | [코드] | F:20, HF:local/compose.yaml:26 | compose 기본 이미지가 `ontology-agent:0.1.0`이다 | revision과 계약 4.1.1의 원시 기록이 없다. 이 이미지로 무엇을 대조 관찰했는지 findings.md에 없다. [C-13](contradictions.md#C-13) |
| <a id="M-08"></a>M-08 | infiniflow/ragflow `2096707f` | [실행] | F:21, 클론 `git rev-parse` 2026-11-06 | 클론 HEAD가 `2096707f`이다 | 클론은 휘발성 스크래치패드에 있다 |
| <a id="M-09"></a>M-09 | 논문 arXiv 2610.41172 (2026-10-30), Context as Infrastructure | [논문] | F:22, P:p.txt | 텍스트 사본이 있고 인용 문장을 대조했다. [PA-01](products/paper-ragflow.md#PA-01)~[PA-11](products/paper-ragflow.md#PA-11) | 게재일은 이 세션에서 대조하지 않았다 |

## 실험 공통 한계

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="M-10"></a>M-10 | ~~모든 모델은 Stub이다.~~ → 2026-11-06 이전 실험은 Stub이다. 실제 모델 소규모 실행은 [LC-40](knowledge-lifecycle.md#LC-40)~[LC-44](knowledge-lifecycle.md#LC-44). Stub 실험에서 코드가 무엇을 보내고 응답을 어떻게 처리하는지만 증명한다 | [실행/Stub] | F:26, I:3, I:29, E:ao/stub_llm.py, E:helix/stub2.py, E:rea/draft/stub5.py, E:rea/quote/stub.py, E:rea/window/stub.py | Stub 소스에 응답이 고정 또는 규칙으로 작성돼 있다 | 추출 품질, 저성능 로컬 모델의 수행 능력은 측정되지 않았다 |
| <a id="M-11"></a>M-11 | Stub의 SQL은 고정값이라 K3/K4에서 변한 것은 모델 입력이다 | [실행/Stub] | F:27, E:ao/stub_llm.py (`SQLGenerationModel` 분기) | Stub이 SQL을 조건 분기로 고정 반환한다 | K3/K4가 SQL 결과에 미치는 영향은 관찰할 수 없다 |
| <a id="M-12"></a>M-12 | 토큰 수는 `tiktoken cl100k_base` 기준이다 | [실행/Stub] | F:28, I:66, E:rea/window/run.py | window/run.py가 `cl100k_base`로 센다 | 실제 로컬 모델 토크나이저의 수는 측정되지 않았다 |

## 증거 재현

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="M-13"></a>M-13 | `evidence/`에 스크립트와 입력이 있고 업스트림 클론과 venv는 휘발성이다 | [실행] | F:222, E: 목록 대조 2026-11-06 | 일부 입력·원시 출력은 evidence/에 없다. [C-12](contradictions.md#C-12) **results.md 갱신:** 재확인 내용은 [C-12](contradictions.md#C-12) | evidence/의 스크립트만으로 전 실험이 재현되는지는 확인되지 않았다(이 위키는 실험을 돌리지 않았다) |

## REA 도구

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="M-14"></a>M-14 | REA `rea-agents` 6.8.0, `morluto/rea` `c467cf86`, CLI만 설치 | [실행] | I:7 | interim.md의 기록. 설치 로그는 evidence/에 없다(기록만) | 기록 외 검증 없음 |
| <a id="M-15"></a>M-15 | Ghidra 12.1.4(게시 SHA-256 일치), Temurin JDK 21.0.13, `rea doctor --provider ghidra` healthy | [실행] | I:8 | interim.md의 기록(기록만) | Ghidra가 이 환경에서 디컴파일을 끝낸다는 것은 아직 관찰되지 않았다. [OP-Q2](open-items.md#OP-Q2) **results.md 갱신:** [M-18](#M-18), [M-20](#M-20) |
| <a id="M-16"></a>M-16 | 대상 이미지 `ghcr.io/helixdb/ontology-agent:latest`(라벨 Apache-2.0)와 `inspect-rust-binary` 출력 3건, `auditable_metadata` null | [실행] | I:9, I:10, E:rea/rust-extract.json, E:rea/rust-ingest-mapped.json, E:rea/rust-ontology-agent.json | 세 JSON 모두 `auditable_metadata`와 `raw_result`가 null이다. `rustc_commit`은 `evidence_kind: inferred`이다 | JSON 스스로 "Functions, types, and runtime behavior are not recovered"라고 밝힌다. 의존성과 컴파일러는 이 출력으로 입증되지 않는다 |

## results.md: 등급과 도구 경로

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="M-17"></a>M-17 | results.md가 더한 등급 [디컴파일], [바이너리]와 "모델은 전부 Stub" 선언 | [미입증] | R:3, R:5, R:7, R:8 | [디컴파일]은 Ghidra 의사코드를 읽은 해석으로 [실행]보다 약하다. [바이너리]는 바이너리에서 값을 직접 읽은 것이다. 정의는 [SCHEMA.md](SCHEMA.md) | 해당 없음(표기 규칙). 사실 주장이 아니다 |
| <a id="M-18"></a>M-18 | REA `decompile` 사용 불가(300초 시작 제한, `provider_timeout`) | [실행] | R:12 | results.md의 기록(기록만). I:8의 `doctor` healthy와 나란히 둔다. [C-22](contradictions.md#C-22) | 실패 로그가 evidence/에 없다 |
| <a id="M-19"></a>M-19 | 디컴파일 경로: 같은 Ghidra, `DecAddrs.java`, 주소는 `nm` 값에 이미지 베이스를 더했다 | [실행] | R:13, E:rea/ghidra/DecAddrs.java, E:rea/ghidra/addrs.txt, E:rea/ghidra/addrs-oa.txt | 스크립트와 주소 목록이 있다. 목록의 일부 함수는 출력 파일이 없다. [SYM-20](concepts/binary-symbols.md#SYM-20) | Ghidra 프로젝트는 보존되지 않았다(R:95) |
| <a id="M-20"></a>M-20 | 분석 상태: `extract`는 1500초 제한으로 미완료 저장, `ontology-agent`는 분석 없이 함수 단위 디스어셈블 | [실행] | R:14, E:rea/decompiled/extract/adj_choices.c:43-44, E:rea/decompiled/extract/dec_entity.c:107 | results.md의 기록(기록만). 해당 c 파일에 점프 테이블 복원 실패 경고가 있다 | 이 조건은 모든 [디컴파일] 행에 걸린다. 경고 없는 파일이 온전히 복원됐다는 보장은 없다 |
| <a id="M-21"></a>M-21 | REA 내장 명령 중 기여한 것: `inspect-rust-binary`, `inspect-artifact`, `doctor` | [실행] | R:15, E:rea/rust-extract.json | `inspect-rust-binary` 출력만 evidence/에 있다 | `inspect-artifact`와 `doctor` 출력은 evidence/에 없다(기록만) |
| <a id="M-22"></a>M-22 | Ghidra 프로젝트, 클론, 일부 스크립트는 휘발성이고 실험 컨테이너는 제거됨 | [실행] | R:95 | results.md의 기록(기록만) | HelixDB에 실제로 쓰인 상태를 지금 다시 읽어 볼 수 없다 |

## results.md §7: 해결되지 않은 항목

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="M-24"></a>M-24 | 추출·판정 품질, 저성능 로컬 모델의 수행 능력 | [미입증] | R:85, R:87, [TK-15](concepts/context-budget.md#TK-15) | results.md도 달라지지 않았다고 기록한다 | 직접 근거 없음 |
| <a id="M-25"></a>M-25 | `extract`의 비-Anthropic 경로, gRPC Extract | [미입증] | R:88, [TK-11](concepts/context-budget.md#TK-11), [SYM-05](concepts/binary-symbols.md#SYM-05) | 심볼상 Anthropic 구체 타입만 보임. ~~gRPC Extract 미실행~~ → 실행했다([C-24](contradictions.md#C-24)) | 직접 근거 없음 |
| <a id="M-26"></a>M-26 | Auto-Ontology 미실행 기능(Web UI, RBAC, Vault, PII, Kumo, Ossie, MCP 서버), Learn 경로 | [미입증] | R:89, [AO-X1](products/auto-ontology.md#AO-X1), [AO-R2](products/auto-ontology.md#AO-R2), [AO-R7](products/auto-ontology.md#AO-R7), [AO-R8](products/auto-ontology.md#AO-R8) | results.md는 소스가 공개되어 있어 실행 문제라고 쓴다 | 직접 근거 없음 |
| <a id="M-27"></a>M-27 | RAGFlow 프롬프트 토큰, 온톨로지 템플릿, 사람 승인 | [미입증] | R:90, [TK-10](concepts/context-budget.md#TK-10), [RF-03](products/paper-ragflow.md#RF-03), [HA-04](concepts/human-approval.md#HA-04) | results.md도 미측정·미확인으로 기록한다 | 직접 근거 없음 |
| <a id="M-28"></a>M-28 | `ontology-agent`의 나머지 함수, 스크립트에 넣지 않은 도구 `evaluate`, `preview_extraction`, `dry_run` | [미입증] | R:91 | 미실행으로 기록됐다 | 동작 전체 |

---
[index](index.md) · [coverage](coverage.md) · [open items](open-items.md)
- [C-22](contradictions.md#C-22) (세분) REA 상태와 심볼 이름
