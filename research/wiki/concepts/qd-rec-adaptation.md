# QD-Rec 적응 초안: 제한된 추출 탐색

[index](../index.md) · [소스·해시](../sources/qd-rec-adaptation.md) · [원 시스템](../products/qd-rec.md) · [기존 실측](prototype-results.md)

추천 이유 탐색에서 **고정 후보 선택과 이력 보존이라는 개념만 재사용**했다. upstream 코드를 복사하지 않은 작은 stdlib controller다. 온톨로지 사실 자동 삽입, 실제 모델 실행, 품질 개선은 이번 결과가 아니다. `QD:파일:행`은 [기존 소스 원장](../sources/qd-rec.md)의 고정 커밋을 가리킨다.

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QDA-01"></a>QDA-01 | 적응 경계 | [코드] | ../../prototype/qd/controller.py; QD:shared/qd_loop.py:187-227 | 고정 unit×lens pool, pending·outcome·history와 provisional archive를 새로 작성한 코드로 구현 | QD-Rec 재현 아님 |
| <a id="QDA-02"></a>QDA-02 | 품질·다양성 | [설계] | E:qd-adaptation/protocol.md | schema·exact span·VERIFY는 온라인 품질 proxy. 독립 의미 품질은 완전한 gold와 blind labels 필요. 다양성은 입력 tag tuple+anchor bool cell의 UNIQUE active 수 | 점유·VERIFY true는 사실성이나 의미 다양성 보장 아님 |
| <a id="QDA-03"></a>QDA-03 | 기계 검증 | [실행/Stub] | E:qd-adaptation/run-001.json | 11검사 통과,39 callback 시도, 실모델0. positive/duplicate/동일 cell 복수 claim/거부/예산/예외/defer/대조군/전부 거부 검사 | Stub 응답은 사전 스크립트이며 의미 oracle 아님 |
| <a id="QDA-04"></a>QDA-04 | 경쟁 가설·판정 | [설계] | E:qd-adaptation/protocol.md | Hmechanical 기계 불변식; Hquality coverage가 같은 random보다 고유 정답을 늘리는가. 미래 2×2 고정 | 실제 효과 미측정, scientific trial ready=false |
| <a id="QDA-05"></a>QDA-05 | 역할·문맥 | [기록] | E:qd-adaptation/procedure.json | 전달받은 독립 proposal/challenge 요약의 digest와 Modify 실제 절차 기록 | 원 세션 직접 관찰 아님; 독립 계산 통과; manuscript 수정은 아래 새 기록 참조 |

## 유지·변환·제거

| 결정 | 원본 file:line | 적응과 이유 |
|---|---|---|
| 유지(개념) | shared/qd_loop.py:187-205,224-227 | pool 선택·archive snapshot·저장 사고방식; 여기서는 순차 bounded task와 반환 기록 |
| 변환 | shared/bandit.py:101-135 | Thompson/cosine 보너스 대신 UNIQUE active가 적은 입력 cell 선택. 동률은 seed RNG, random은 동일 pending pool 무작위 선택 |
| 유지·변환 | shared/archive_records.py:179-225 | active와 discarded 이력 구분은 유지. 교체는 제거하고 독립 명제는 같은 cell에도 모두 보존 |
| 변환 | apps/papers/qd_rec.py:44-95 | novelty/duel 수용 대신 schema→span→VERIFY 통과만 provisional 수용. 점수 경쟁 없음 |
| 제거 | apps/papers/proposer.py:56-120 | 부모 예시·진화·문자 잘라내기 제거. parent=null; general/qualifier 두 고정 lens, 절대 truncation 없음 |
| 제거 | shared/embeddings.py:7-23,37-48 | 외부 embedding/API·최근접 의미 신규성 제거; 입력 descriptor만 사용 |
| 변환 | shared/llm.py:98-118 | upstream 점수 범위 검사 대신 기존 onto.validate 사용; 호출 실패도 cap 소비. 외부 client/retry는 사용 안 함 |

## 결정적 descriptor와 archive

unit의 외부 입력 `tags`를 중복 제거·정렬한 tuple과 `anchor` bool이 하나의 cell이다. condition+negation이 겹치면 두 cell이 아니라 결합 tuple 한 cell이다. 빈 tag도 유효하다. 자동 논리/의존성 탐지는 없다. `context_dependent=true`라고 **외부에서 표시한** unit은 두 selector 모두 호출 없이 deferred로 남긴다. 실제 문맥 의존 문장을 자동으로 찾아냈다고 주장하지 않는다.

선택 때 cell별 UNIQUE active provisional 명제 수를 센다. identity는 subject/relation/object 정확한 문자열 tuple이며 concept는 제외한다. 이는 의미 동치 판정이 아니므로 다른 표현의 중복은 남을 수 있다. qualifier를 해당 문자열에서 보존해야 한다. 같은 명제의 반복 evidence는 duplicate history에 source/hash/unit/lens/claim으로 남고 active는 한 번만 센다. 서로 다른 명제는 같은 cell에서도 보존한다. cap 소진 후 미시도 task는 pending이며, verify 못 한 claim은 rejected다. 미해결 의미 판단은 자동 승격하지 않는다.

## 기존 코드 연결 seam과 자원

[onto.py](../../prototype/onto.py)의 `read_docs` 418–438행: unit 추출 후 `facts.append`(436행) **이전**이 실험 후보 경계다. 미래 adapter가 unit/source SHA256/section/anchors를 구성하고 `run(..., ask=llm.ask, onto=onto)`에 전달할 수 있다. 이번에는 Stub만 전달했으며 onto.py 자체는 변경하지 않았다. 반환 active를 바로 append하면 안 된다. 독립 검수와 원 문서·section·sentence·quote·anchors·dates·amounts·provenance를 포함한 완전한 변환 계약이 먼저 필요하다. `induce` 454행 이후는 doc/anchors와 문서 간 반복을 사용하므로 명제만 넘기면 연결을 잃는다. `STOP_CONCEPTS` 21행의 Fact는 downstream concept 유도에서 제외된다.

각 extraction 600, verify 30 출력 토큰을 미리 예약하고 기존 `onto.prompt_bound`(50–55행)+predict <3800을 **각 호출 전** 검사한다. 관측 4098 문제보다 엄격한 총량 guard다. serialized schema/messages의 UTF8 byte와 512 framing allowance를 쓰지만 512는 가정이고 실제 tokenizer 검증은 없다. 초과는 callback 0, truncation 없음. callback 예외와 실패도 cap에 포함하고 verify 완료 없이는 active가 없다. 실제 총 토큰·서버 시간 측정 driver는 미구현이며 이 controller는 미래 scientific hard budget을 보장하지 않는다.

## 실행 전 기계 규칙과 미래 판정

[protocol](../../evidence/qd-adaptation/protocol.md)은 코드 실행 전에 [lock](../../evidence/qd-adaptation/lock.json)으로 SHA256·시각을 보존했다. random/coverage × original/fixed Fact의 2×2, 같은 pool/gate/budget, 독립 heldout·완전한 gold는 아직 없으며 미래 실행 전에 고정해야 한다. Acme/기존 gold는 알려진 개발 자료다. seed7/11/19는 paired이며 독립 corpus 표본이 아니다.

매 seed에서 precision≥.90이고 matched random 이상, unique correct≥random+max(1,ceil(.10×random)), supported gold cell recall≥random을 모두 요구한다. random=0도 최소1 증가 필요. gold 동치는 주체·관계·객체·극성·양태·조건·귀속까지 일치해야 한다. 통제/전수 label/accounting 무효면 inconclusive, 유효하지만 문턱 미달이면 해당 표본의 operational claim 기각이다. 일반 통계나 효과 주장은 하지 않는다. 전부 거부 fixture의 active=0은 성공 품질이 아니다.

미래 arm당 hard limit: 총64시도 호출, 호출별 conservative prompt+output<3800, 실제 input+output≤64,000 tokens, CPU-server-wall≤900초. 위반은 abort/inconclusive. 실제 token/time driver와 독립 정답 판정이 준비되기 전 실행하면 이 과학 판정을 낼 수 없다.

## 실제 역할·절차와 생략

| 역할/절차 | 실제 전달 문맥·상태 | 이번 포함/생략 |
|---|---|---|
| 독립 제안2 | 관리자 요약: QD 제품/onto.py/qd_loop만, 서로의 제안·부모 대화 없음 | P1 mechanics 채택, P2 fixed Fact 설명 유지; 직접 원 세션 미관찰 |
| 독립 반론 | 관리자 요약: 후보 명세·장치 한계만, PI 대화·파일·실행 없음 | descriptor/문맥 defer/호출 예산/gold 규칙4건 반영 |
| Modify | fresh 역할에서 계약·감사·위 요약·지정 소스 읽기 | 재귀 refine 없음, scripted Stub 실행1회 |
| 독립 Evaluate·manuscript review | 관리자 전달: 독립 계산 및 fresh manuscript 검토 수행 | 계산 11+32 cases/268 assertions, must-fix0; manuscript 5건 수정. 최종 Evaluate 대기 |
| 실모델·수치 예측·HPC·물리 안전 | 실행 안 함 | 실모델 의미 효과·예측 calibration·HPC·물리 실험 적용 미검증 |
| 관리 gate | 공간 검사11,947→11,946MB, 외부 호출0, 새 evidence exclusive write | B 공개 빌드·commit/push 미수행; WIP 유지; skills 등록 안 함 |

절차 요약과 전달 입력 digest는 [procedure](../../evidence/qd-adaptation/procedure.json)에 있다. 전체 skill/논문을 복제하지 않는다. 기존 QD-Rec upstream 선언·논문 출처는 [원장](../sources/qd-rec.md)에 보존한다.

## 검토 후 새 정의 (과거 동결과 구별)

[future addendum](../../evidence/qd-adaptation/future-analysis-addendum.md)은 Stub 이후 새로 작성한 미래 정의다. [시각·해시 lock](../../evidence/qd-adaptation/addendum-lock.json)은 현재 작성 시점을 보존하며 과거 preregistration이 아니다. [review summary](../../evidence/qd-adaptation/review-summary.json)는 원 procedure의 pending review를 역사 기록으로 대체한다. 원 raw는 수정하지 않았다.

Hq-Fact: fixed Fact 안에서 coverage 대 random의 추가 가치가 주 질문이다. Hq-original은 original concept 안에서 별도로 판정한다. 각 seed별 같은 extractor 내부 비교만 허용하며 pooled/cross-factor winner는 없다. 두 extractor는 Fact 추가 지시만 다르고 lens·schema는 공유한다.

미래 gold 작성자는 gold 완료까지 arm/selector/seed/model output을 보지 않는다. 이후 prediction judge는 arm/selector에 blinded이며 보존 source/proposition을 받는다. 독립 전수 의미 adjudication으로 동치 명제를 분자·분모 모두 dedup: precision=T/(T+F), empty=0. gold-cell recall 분모는 gold fact≥1인 입력 descriptor cell 집합, 분자는 correct ACTIVE first-origin record가 지지하는 cell이다. 분모0, gold 누락, 미해결 ambiguity는 inconclusive. descriptor/context flags는 실행 전 고정한다. Exact duplicate는 최초 active source cell만 지지하고 후속 provenance는 history다. Qualifier 보존은 요구·proxy이지 기계적 의미 증명이 아니다.

같은 budget caps와 실제 소비를 구별해 보고한다. 호출 전 예약으로 총 token cap 초과를 방지해야 한다. Wall time은 첫 요청 시작부터 최종 응답/종료까지 monotonic elapsed이며 queue/load/controller를 포함한다. 원 thresholds/hard limits는 그대로다. Corpus/gold/driver 부재로 과학 실행은 불가하며 실제 모델 미검증이다.

`onto.py:436`의 정확한 연결 행: `facts.append({"unit": uid, "doc": rel, "section": head, "sentence": u, **it,`

[독립 계산 보고](../../evidence/qd-adaptation/independent-calculation.json)는 11+32 case/268 assertions, must-fix0을 전달한다. Adversarial script는 scratch에 남아 public report만으로 full script-independent rerun을 주장할 수 없다. 현재 mechanical verdict는 그대로이며 부모의 최종 독립 평가는 아직 대기다.

**results.md 갱신:** 후속 [QD 실제 결과](qd-real-results.md)는 세 가설 모두 INCONCLUSIVE다. 이전 raw·역사 결과는 보존한다.
