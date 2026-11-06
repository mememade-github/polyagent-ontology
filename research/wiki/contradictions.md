# 소스 간 변경과 불일치

lint에서 찾은 항목이다. 양쪽을 원문 위치와 함께 남기고, 어느 쪽도 지우지 않는다. "처리"는 위키의 기록 방식이며 판단이 아니다.

## <a id="C-01"></a>C-01 Helix 인용 대조 범위

- 종류: 세분
- 앞선 기록 또는 주장: F:134 "문서에 없는 인용" reject 1행
- 대조 기록: I:49-62 12변형: 변형 8건 accept, 4건 reject
- 처리: 두 기록을 모두 유지한다. F:134 행은 그대로 관찰이고, 범위는 12변형으로 세분된다. 메커니즘은 C-16
- 영향 페이지: [인용 대조 (quote validation)](concepts/quote-validation.md), [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md), [판정과 2차 검증](concepts/second-verifier.md)

## <a id="C-02"></a>C-02 초안 완주 여부와 이전 실패 원인

- 종류: 대체 및 원인 불일치
- 앞선 기록 또는 주장: F:145 "진입까지만", 원인은 "Stub은 도구 루프를 수행할 수 없어", F:198 "진입까지 확인"
- 대조 기록: I:26, I:28 스크립트 Stub으로 `done` 완주, 원인은 "스트리밍 미지원"
- 처리: 완주 관찰은 interim.md가 새 기록이다. 초안 내용은 Stub이 작성(I:29). 원인 진술 두 개는 표현이 다르며, E:helix/stub4.py가 비스트리밍 JSON을 반환한다는 것만 확인된다
- 영향 페이지: [온톨로지 뼈대의 출처](concepts/ontology-skeleton-source.md), [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md), [문서만 입력한 경우](concepts/document-only-input.md), [세 시스템 항목별 현황](comparison.md)

## <a id="C-03"></a>C-03 엔티티 창과 `--max-section-bytes`

- 종류: 세분
- 앞선 기록 또는 주장: F:215 창 조절 옵션이 `--help`에 없음
- 대조 기록: I:76 섹션을 바꾸므로 창 크기에 영향, 직접 조절은 아님
- 처리: 두 진술은 양립한다. "직접 옵션 없음"과 "간접 영향 있음"을 함께 기록한다
- 영향 페이지: [엔티티 창 (entity windows)](concepts/entity-windows.md), [컨텍스트 크기와 토큰 측정](concepts/context-budget.md)

## <a id="C-04"></a>C-04 추출 패스 구성

- 종류: 추가
- 앞선 기록 또는 주장: F:109 엔티티 → 링크 → 코드 검증 → 검증 모델 → 판정
- 대조 기록: I:17 `glean_call`, `adjudicate_call` 심볼, I:73 `--gleanings 1` 링크 호출 2배, I:85 `adjudicate_call` 호출 전
- 처리: F:109 도식은 관찰된 기본 실행의 기록으로 유지한다. 추가 패스의 위치는 미입증이다
- 영향 페이지: [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md), [바이너리 심볼과 문자열](concepts/binary-symbols.md), [판정과 2차 검증](concepts/second-verifier.md), [엔티티 창 (entity windows)](concepts/entity-windows.md)

## <a id="C-05"></a>C-05 초안 입력 "최신 5건 + 도구 17개"

- 종류: 근거 공백
- 앞선 기록 또는 주장: F:108 "최신 5건", "도구 17개"
- 대조 기록: HF:backend/ontologyagent/generator.go:44-47은 수 5만 말하며 선택 기준은 없다. 스크립트 실행(E:rea/draft/stub5.py)은 도구 5개만 쓴다
- 처리: "최신"과 "17개"는 findings.md 기록으로만 남기고 입증으로 올리지 않는다
- 영향 페이지: [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md)

## <a id="C-06"></a>C-06 Helix 사람 승인

- 종류: 세분
- 앞선 기록 또는 주장: F:108, F:197 "사람 검토 → 승인", "초안 검토"
- 대조 기록: I:19 `bundle::approve` 심볼, I:28 `bundle` null, I:85 승인 실행 전
- 처리: 승인은 README와 계약 코드 수준으로만 기록하고 실행 관찰로 올리지 않는다
- 영향 페이지: [사람 승인](concepts/human-approval.md), [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md)

## <a id="C-07"></a>C-07 토큰 측정 범위

- 종류: 측정 범위 불일치
- 앞선 기록 또는 주장: F:204는 메시지와 도구를 합산한다. F:205-208은 범위 미기록
- 대조 기록: E:rea/window/run.py는 마지막 메시지와 system만 센다. I:77은 8,500과 18,756을 나란히 놓는다
- 처리: 수치는 원 기록대로 두고, 범위가 같다고 쓰지 않는다. I:77의 "같은 바이트 상한"은 I:75의 "상수 미확인"과 함께 전제로 표시한다
- 영향 페이지: [컨텍스트 크기와 토큰 측정](concepts/context-budget.md), [엔티티 창 (entity windows)](concepts/entity-windows.md)

## <a id="C-08"></a>C-08 Auto-Ontology "문서만으로 불가"

- 종류: 표현 범위
- 앞선 기록 또는 주장: F:198 "불가"
- 대조 기록: F:94 문서 테이블에서 Term 1개, 속성 3개 생성
- 처리: 입력이 다르다. 문서 파일 경로는 없고(F:99), 문서를 담은 DB 테이블은 컬럼 수준 Term이 된다. 두 관찰을 모두 유지한다
- 영향 페이지: [문서만 입력한 경우](concepts/document-only-input.md), [NVIDIA/auto-ontology](products/auto-ontology.md), [세 시스템 항목별 현황](comparison.md)

## <a id="C-09"></a>C-09 README "certified definitions로 쿼리 검증"

- 종류: 주장과 코드 불일치
- 앞선 기록 또는 주장: AO:README.md:15
- 대조 기록: F:80 프롬프트 해시 동일, `certif` 일치는 주석뿐
- 처리: findings.md의 기록을 유지한다. 범위는 `retrieval/`이다
- 영향 페이지: [NVIDIA/auto-ontology](products/auto-ontology.md), [사람 승인](concepts/human-approval.md)

## <a id="C-10"></a>C-10 RAGFlow: 저장 규칙, exact, 온톨로지 템플릿

- 종류: 논문과 코드 불일치
- 앞선 기록 또는 주장: P:§4.1 p.txt:406-407 미위치 claim 미저장, P:§4.2 p.txt:442-443 "exact presence", P:§3.2 Ontology 템플릿
- 대조 기록: F:169 기본 soft 유지, RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:549 공백 접기, F:170 템플릿 코드 미확인
- 처리: "exact"와 공백 접기의 차이는 이 위키가 lint에서 추가했다. 불일치의 원인은 미확인이다
- 영향 페이지: [arXiv 2610.41172와 RAGFlow](products/paper-ragflow.md), [인용 대조 (quote validation)](concepts/quote-validation.md), [문서만 입력한 경우](concepts/document-only-input.md)

## <a id="C-11"></a>C-11 findings.md의 `backend/api/ontology.go:19`

- 종류: 인용 정밀도
- 앞선 기록 또는 주장: F:123 "사용처 :19"
- 대조 기록: 19행은 import, `ontology.Validate` 호출은 254행
- 처리: 위키는 254행을 인용한다. findings.md는 수정하지 않았다
- 영향 페이지: [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md)

## <a id="C-12"></a>C-12 "evidence/에 스크립트와 입력이 있다"

- 갱신: 보존함: `helix/mappings.toml`, `adjudicate/rows.jsonl`, `adjudicate/a.log.adj`, `approval/*.log.jsonl`, `decompiled/extract/normalize.c`. 여전히 없음: `window/ascii.txt`, `window/small.txt`, `run3.py` 출력, `t2.py`와 `t3.py` 출력, `objdump`와 `.rodata` 출력, `inspect-artifact` 출력
- 종류: 재현 근거 공백
- 앞선 기록 또는 주장: F:222
- 대조 기록: 없는 것: K1 호출 줄, A2 스크립트, `helix/ontology.toml`, `window/ascii.txt`, 호출 캡처 로그, knockout·토큰·window·실행 2의 원시 출력, `--help`, `nm` 출력. knockout.py는 baseline 뒤 `sys.exit()`
- 처리: 해당 행에 "기록만"으로 표시한다. 스크래치패드의 다른 디렉터리는 범위 제한상 읽지 않았다
- 영향 페이지: [방법, 대상 버전, 실험 공통 한계](method-and-limits.md), [NVIDIA/auto-ontology](products/auto-ontology.md), [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md), [엔티티 창 (entity windows)](concepts/entity-windows.md), [컨텍스트 크기와 토큰 측정](concepts/context-budget.md)

## <a id="C-13"></a>C-13 compose 기본 이미지와 저장소 계약

- 종류: 버전 차이
- 앞선 기록 또는 주장: HF:local/compose.yaml:26 `0.1.0`, F:20 계약 4.1.1
- 대조 기록: HF:backend/ontologyagent/contract.go:21 4.7.0, 실험은 `latest`
- 처리: 실험 관찰은 `latest`에 한한다. `0.1.0` 대조 결과의 기록은 없다
- 영향 페이지: [방법, 대상 버전, 실험 공통 한계](method-and-limits.md), [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md)

## <a id="C-14"></a>C-14 `extract`의 프로바이더

- 종류: 세분
- 앞선 기록 또는 주장: F:216 CLI 옵션은 Anthropic 전용 표기, 계약은 Ollama·OpenAI 호환 선언
- 대조 기록: I:18 구체 타입 `Cached<Limited<Anthropic>>`만 보임, ollama/openai 일치 1건 내용 미확인
- 처리: 심볼 근거는 이름 수준이다. 비 Anthropic 추출 경로의 존재 여부는 미입증으로 둔다
- 영향 페이지: [컨텍스트 크기와 토큰 측정](concepts/context-budget.md), [바이너리 심볼과 문자열](concepts/binary-symbols.md), [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md)

## <a id="C-15"></a>C-15 `context_tokens` 동작

- 종류: 추가
- 앞선 기록 또는 주장: F:217 8000 지정에도 같은 크기 요청
- 대조 기록: I:41 보고 사용량 초과에도 3회 모두 `done`, `Budget` 미확인
- 처리: 두 관찰 모두 턴이 멈추지 않은 범위의 기록이다. 제한 메커니즘은 미입증이다
- 영향 페이지: [컨텍스트 크기와 토큰 측정](concepts/context-budget.md)

## <a id="C-16"></a>C-16 Helix 인용 대조 메커니즘

- 종류: 미확정
- 앞선 기록 또는 주장: I:62 "정규화 후 비교"
- 대조 기록: I:52 span 26–72가 인용보다 2바이트 길다. 코디네이터 통지: rapidfuzz 유사도 호출, 임계값 시험 중. evidence/와 세 클론에서 `rapidfuzz` 0건
- 처리: 어느 쪽도 채택하지 않는다. 새 raw 소스를 기다린다
- 영향 페이지: [인용 대조 (quote validation)](concepts/quote-validation.md), [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md), [근거 위치 (evidence spans)](concepts/evidence-spans.md)

## <a id="C-17"></a>C-17 R:39의 잠금 문장과 모델 입력 주장

- 종류: 인용과 raw 불일치
- 앞선 기록 또는 주장: R:39 "`type.Customer` is locked by the user", "코멘트가 모델 입력에 포함됨"
- 대조 기록: E:rea/approval/c1.out의 `put_items` 결과는 "error: rejected, the draft unchanged"이고 `decisions`는 `locked`이다. "is locked by"는 evidence/에서 results.md에만 있다. 호출 로그가 evidence/에 없다
- 처리: 거부와 `locked` 상태는 raw로 확인된 관찰로, 문장과 모델 입력 포함은 기록만으로 둔다
- 갱신: `evidence/rea/approval/c1.log.jsonl`을 보존해 확인했다. 네 번째 호출의 도구 결과에 "is locked by the user"가 있고, 첫 호출 메시지에 코멘트 원문이 있다. 두 관찰 모두 [실행/Stub]으로 올린다
- 영향 페이지: [ha](concepts/human-approval.md)

## <a id="C-18"></a>C-18 `normalize` 내용과 I:83의 디컴파일 목록

- 종류: 근거 공백
- 앞선 기록 또는 주장: R:21 "인용을 `text::normalize`로 정규화", I:83 다섯 함수
- 대조 기록: `normalize.c`가 없다(`addrs.txt`에는 있음). `commit::constrain`은 주소 목록에도 없다. 다섯 중 `locate_quote`, `sections`, `bounded`만 파일이 있다
- 처리: 호출 사실은 [디컴파일]로, 정규화 내용은 미입증으로 둔다
- 갱신: `normalize.c`를 보존했다. 파일에서 NFC/NFKC 또는 소문자 변환 함수 이름을 찾지 못했으므로(`nfk?[cd]`, `to_lowercase` 등 검색) 정규화 내용은 여전히 미입증이다. `commit::constrain`은 계속 없다
- 영향 페이지: [qv](concepts/quote-validation.md), [sym](concepts/binary-symbols.md)

## <a id="C-19"></a>C-19 R:30의 일반화

- 종류: 서술 범위
- 앞선 기록 또는 주장: R:30 "낮은 품질 인용", "임의의 짧은 단어 인용도"
- 대조 기록: R:26의 관찰은 `Globex` 1건, R:21은 3글자 미만을 거부한다
- 처리: 관찰 1건으로 기록하고 일반화와 평가 표현은 results.md의 서술로만 인용한다
- 영향 페이지: [qv](concepts/quote-validation.md)

## <a id="C-20"></a>C-20 "전 구간 연결"과 Foundry 경로

- 종류: 범위
- 앞선 기록 또는 주장: R:46-52 전 구간 연결, F:108, HF:README.md:63,74 사람 검토와 current 지정
- 대조 기록: R:44, HF:backend/ontologyagent/contract.go:244-247 "Foundry sends only starts". `e2e.sh`는 `mappings_toml`을 넘기지 않았다
- 처리: 바이너리 직접 실행의 통과로 기록한다. Foundry 백엔드 경로의 승인과 매핑 사용은 미입증으로 둔다
- 영향 페이지: [ha](concepts/human-approval.md), [hx](products/helix-foundry.md), [sk](concepts/ontology-skeleton-source.md)

## <a id="C-21"></a>C-21 최소 컨텍스트와 `settle`

- 종류: 관계 미확인
- 앞선 기록 또는 주장: F:121, HF:backend/ai/validate.go:34,85 65,536 미만 거부
- 대조 기록: R:58, m_settle.c: 기존 값이 0일 때 0x10000, 모델 정보 값이 더 작으면 줄임. R:58은 "양쪽의 관계는 확인하지 않았다"고 쓴다
- 처리: Go는 입력 거부, 바이너리는 값 축소로 각각 기록하고 관계는 미확인으로 둔다
- 영향 페이지: [tk](concepts/context-budget.md)

## <a id="C-22"></a>C-22 REA 상태와 심볼 이름

- 종류: 세분
- 앞선 기록 또는 주장: I:8 `rea doctor --provider ghidra` healthy, I:19 `Budget::{...room...}`
- 대조 기록: R:12 REA `decompile` 사용 불가, b_room.c:4 `room_before`
- 처리: 둘 다 유지한다. healthy는 doctor의 결과이고, decompile 실패는 별도 기록이다. `room`과 `room_before`의 관계는 미확인이다
- 영향 페이지: [method](method-and-limits.md), [sym](concepts/binary-symbols.md)

## <a id="C-23"></a>C-23 RAGFlow 추출 경로의 누락

- 종류: 범위 누락
- 앞선 기록 또는 주장: F:190 뼈대 "프롬프트 템플릿", F:198, F:170 온톨로지 템플릿 코드 미확인. 기존 비교는 RAGFlow를 claim 경로로만 다뤘다
- 대조 기록: `structure`, `wiki`, `mindmap` 경로와 `templates/*.yaml`이 코드에 있다([XT-15](extraction-techniques.md#XT-15)~[XT-22](extraction-techniques.md#XT-22)). `ontolog` 검색만으로는 `knowledge_graph.yaml`이 잡히지 않았다
- 처리: 앞선 기록을 지우지 않고 새 페이지에 수집했다. 논문의 Ontology 템플릿은 템플릿 목록과 kind 허용 목록에서도 찾지 못했다
- 영향 페이지: [추출 기법](extraction-techniques.md), [arXiv 2610.41172와 RAGFlow](products/paper-ragflow.md), [세 시스템 항목별 현황](comparison.md)

## <a id="C-24"></a>C-24 (범위 정정) Helix 추출의 로컬 모델 경로

- F:216, [OP-H6](open-items.md#OP-H6): `extract` CLI는 Anthropic 전용 표기, gRPC 미실행.
- 새 실행: `ontology-agent serve`의 gRPC `Extract`가 OpenAI 호환과 Ollama로 추출을 끝까지 수행했다(E:helix/grpc/faults.out, E:real-model/helix_docmd.out). 이전 비교표의 "모델 교체" 칸은 CLI에 한한 서술이다.
- 영향 페이지: [생애주기](knowledge-lifecycle.md), [추출 기법](extraction-techniques.md)

## <a id="C-25"></a>C-25 (세분) RAGFlow 미지 엔드포인트 관계의 저장

- [XT-16](extraction-techniques.md#XT-16): `Run` 출력에 유지.
- 새 근거: 데이터셋 병합 입구의 `FilterOrphanRelations`가 제거한다(RF:internal/ingestion/knowledge_compile/consumer.go:1622, E:ragflow/compile/rf_fault.out S10). 원문에 없는 엔티티 자체는 이 필터로 제거되지 않는다. 호출처는 이 한 곳이라 문서 단위 행은 이 필터를 거치지 않는다.

## <a id="C-26"></a>C-26 (세분) `context_tokens`의 효과

- F:217: 초안 `turn`은 8000을 줘도 같은 크기 전송(OpenAI 호환).
- 새 실행: `Extract`도 OpenAI 호환에서 21,727토큰을 전송했다([LC-31](knowledge-lifecycle.md#LC-31)). Ollama는 호출 전에 거부한다([LC-30](knowledge-lifecycle.md#LC-30)). `Ask`의 Ollama 8192는 호출 0회로 끝난다([LC-03](knowledge-lifecycle.md#LC-03)). 프로바이더와 경로마다 다르다.
- 첫 실모델 실행은 실험에서 CPU 제한을 건 상태에서 280초 `model_timeout`이었고, 제한을 푼 뒤 같은 문서가 204초에 끝났다(기록만, 원인 단정 없음).

## <a id="C-27"></a>C-27 QD-Rec 기본 모델과 논문 보고 조건

- 종류: 실행 기본값과 논문 실험 조건 차이. 코드 오류나 논문 수치 반박으로 단정하지 않는다.
- 코드·문서: QD:apps/papers/config.py:27-32와 QD:README.md:24-38,140은 proposer/judge 기본값을 `openai/gpt-6-luna`로 둔다.
- 논문: arXiv 2610.23470v2 §5.1(QDP:182)은 Sonnet 5/Haiku 4.5 proposer와 `gpt-5.6-terra` judge를 보고한다(도서 품질은 인간 평점).
- 처리·갱신: 두 조건을 모두 보존한다. 기본 명령 실행을 논문 결과 재현으로 간주하지 않는다. 이 세션은 어느 조건도 실행하지 않았다.
- 영향 페이지: [QD-14](products/qd-rec.md#QD-14), [QD-18](products/qd-rec.md#QD-18), [소스 원장](sources/qd-rec.md).

---
[index](index.md) · [coverage](coverage.md)
- 갱신(results.md 수집): I:62의 "정규화 후 비교"가 다루지 못한 퍼지 경로가 추가됐다(R:23-24, [QV-22](concepts/quote-validation.md#QV-22)). F:194의 "불일치 시 거부"는 정확히는 임계값 미만 거부로 읽히나, 임계값 값의 raw는 없다
- 갱신(results.md 수집): 승인까지 실행됐다([HA-10](concepts/human-approval.md#HA-10), [HA-13](concepts/human-approval.md#HA-13)). 내용은 여전히 Stub 작성이다. 이전 실패 원인 두 진술의 차이는 results.md로 달라지지 않았다
- 갱신(results.md 수집): 상한 관찰이 추가됐고 상수는 미확인이다([EW-09](concepts/entity-windows.md#EW-09), [EW-10](concepts/entity-windows.md#EW-10))
- 갱신(results.md 수집): `adjudicate`가 `calls`에 나타났다([SV-13](concepts/second-verifier.md#SV-13)). F:109의 도식은 raw `calls` 순서상 빠진 패스가 있음을 보여 준다. `glean_call`의 위치는 여전히 미입증이다
- 갱신(results.md 수집): 승인 게이트와 번들이 실행됐다([HA-06](concepts/human-approval.md#HA-06)~[HA-11](concepts/human-approval.md#HA-11)). 이는 스크립트가 바이너리에 직접 보낸 것이다. 사람이나 Foundry 경로의 승인은 관찰되지 않았다([C-20](#C-20))
- 갱신(results.md 수집): R:88이 같은 상태를 기록한다. 변화 없음
- 갱신(results.md 수집): `Budget::exhausted`에 토큰 비교가 없다는 해석이 추가됐고([TK-16](concepts/context-budget.md#TK-16)), 서버 400 경로가 실행됐다([TK-19](concepts/context-budget.md#TK-19)). `context_tokens`의 의미와 `prompt_bound` 사용처는 여전히 미확인이다
- 갱신(results.md 수집): **메커니즘 일부 해소, 임계값 값과 정규화 내용은 미입증.** 통지의 validator는 `extraction::text::locate_quote`이다. 클론 grep 0건은 이 함수가 `extract` 바이너리 안에 있어서라는 코디네이터 설명과, c 파일의 `rapidfuzz` 심볼이 맞는다. 판정 경로는 [QV-20](concepts/quote-validation.md#QV-20)~[QV-23](concepts/quote-validation.md#QV-23), 26–72는 해석으로 [QV-28](concepts/quote-validation.md#QV-28), 산술 점검은 [QV-31](concepts/quote-validation.md#QV-31)
- 갱신(results.md 수집): R:64의 창 크기는 바이트이다. 토큰 측정 범위 불일치는 달라지지 않았다
- 갱신(results.md 수집): 재확인 결과: ~~`helix/ontology.toml`~~은 이제 있다. `window/ascii.txt`는 저장돼 있지 않다(실행 이력의 한 줄로 재생성 가능하다는 것은 코디네이터 통지이며 이 위키가 확인하지 않았다). K1 호출 줄, A2 스크립트, knockout·토큰·window·실행 2의 원시 출력, `--help`, `nm` 출력은 여전히 없다. 새로 없는 것: `helix/mappings.toml`, `adjudicate/rows.jsonl`, `adjudicate/a.log.adj`(adjudicate 프롬프트·스키마 캡처), `t2.py`와 `t3.py` 출력, `window/small.txt`와 run3 출력, `approval/*.log.jsonl`, `objdump`와 `.rodata` 출력, `inspect-artifact` 출력
