# 혼합 소스 프로토타입 실측 — 2026-11-06

[위키 결과](../../wiki/concepts/prototype-results.md) · [동결 규약](protocol.md) · [측정](measurements.json) · [평가](evaluation.json) · [안정성](stability.json) · [해시](hashes.json)

## 판단과 설계 이유

작은 독립 질문으로 문맥 부담을 낮추고 DB 구조와 문서 사실을 분리해 출처를 남기는 방식을 선택했다. 실행 결과는 **혼합 소스 스키마 초안**이다. 문서 의미 유도는 빈약하며 완성된 온톨로지·일반 우월성·연구 신규성을 입증하지 않는다. Acme는 이전에 살펴본 개발 자료이고 합성 gold도 알려진 회귀 입력이다. blind/heldout 평가가 아니다. 이 문서는 조정자가 제공한 공개 측정 메타데이터를 정리한 것이며 문서 작성자가 새 추론을 실행하지 않았다.

## 환경·입력·실행

Python 3.10.12, Ollama 0.40.10 CPU, qwen2.5:3b (실제 3.1B, Q4_K_M). temperature=0, seed=7, num_ctx=8192, num_thread=8. 새 모델 pull은 하지 않았다. 모델 digest와 호출별 설정·입력 문자/UTF8 byte·토큰·종료 상태·시간은 measurements.json에 있다. client CPU는 모델 서버 CPU를 포함하지 않는다.

입력은 SQLite 4테이블 569행, JSONL 225레코드, key=value 로그 327레코드, calls/reference 아래 Markdown 6문서다. 내부 구조 단위는 JSONL·로그를 포함해 6개다. PDF 3건은 제외했다. HelixDB/helix-foundry의 Apache-2.0 샘플을 변환해 사용했으며 commit과 파일별 크기·해시는 hashes.json에 기록한다. 원본 SQL·acme.json·전체 샘플 문서를 재배포하지 않는다. acme.json은 추론 입력에 없고 참조 메타데이터의 이름·해시만 평가에 사용한다.

| 실행 | 상태 | 타입/링크/사실 | HTTP 호출 | wall 초 | LLM 합계 초 | client CPU 초 | 최대 prompt 토큰 |
|---|---|---|---:|---:|---:|---:|---:|
| measured-run1 | built | 10/13/3 | 189 | 269.967564 | 267.563437 | 2.563105 | 340 |
| measured-run2 | built | 10/13/3 | 189 | 202.643924 | 200.505817 | 2.284546 | 340 |
| measured-gold1 | failed | 0/0/1 | 11 | 16.467740 | 16.428839 | 0.027389 | 308 |
| measured-gold2 | failed | 0/0/1 | 11 | 17.893353 | 17.864431 | 0.030873 | 308 |

최종 4실행 합계 400회 실제 HTTP 호출, application cache hit 0. 새 출력 디렉터리로 반복했으며 서버 모델/KV warming은 허용했다. 직렬화된 messages+schema UTF8 byte와 framing 여유 512를 합해 3800 미만으로 제한했다. 관측 최대 prompt 340은 알려진 약 4098 한계 미만이다. 컨테이너 전체 수명(개발 포함) 로그의 `truncating` 출현은 0회다. 최종 호출의 길이 종료는 없지만 독립적인 서버 원본 토큰 수는 없어 카운터만으로 모든 잘림 부재를 증명하지 않는다.

## 동결 타입 대응과 분모

두 Acme 실행 모두 타입 precision 8/10=80.00%, recall 8/9=88.89%. 출력 전체를 분모로 유지하고 frozen alias를 바꾸지 않았다.

| 예측 | 참조 | 출처·세분성 근거 |
|---|---|---|
| Account | Account | accounts의 계정 행 |
| Contact | Contact | contacts의 연락처 행 |
| Subscription | Subscription | subscriptions의 구독 행 |
| Invoice | Invoice | invoices의 청구 행 |
| TicketOpened | Ticket | ticket opened 로그가 티켓당 한 행인 세분성 |
| ProductUsage | MonthlyUsage | product_usage.jsonl의 계정/월 행. 선언 키는 없지만 `(account_id, month)`가 225행에서 관측 유일한 복합 키 후보다. 이 표본 밖의 유일성은 보장하지 않는다 |
| Plan | Plan | subscriptions.plan의 범주 |
| MeetingOrCall | Conversation | 문서 교환을 장르로 분류한 hybrid 타입; 약속 관계를 입증하지 않는다 |
| Role | 없음 | contacts.role에서 나온 추가 범주 |
| Category | 없음 | 로그 category에서 나온 추가 범주 |

Commitment는 누락됐다. 참조와 불일치한 추가 타입이 현실에서 반드시 거짓이라는 뜻은 아니다. 전체 prediction ID와 대응은 evaluation.json에 보존했다.

## STRICT 링크와 프로토콜 결함

두 실행의 **STRICT FROZEN MAPPING** precision은 5/13=38.46%, recall은 5/11=45.45%다. 실행 전 열 목록을 추정하면서 `ticket.contact_id`와 `usage.account_ref`라고 잘못 적었다. 실제 소스 열은 각각 `requester_id`, `account_id`다. 따라서 소스에 근거한 두 연결도 동결 literal 규칙상 제외됐다. **5/11은 편향 없는 의미 관계 품질 추정치가 아니다.** 오류를 공개하되 프로토콜·주 점수를 수정하거나 유리한 사후 재채점을 하지 않았다.

| 예측 연결 | 실제 출처 열/관계 | 동결 STRICT 대응 |
|---|---|---|
| Contact → Account | `acme.sqlite::contacts.['account_id']` | contact_at |
| Subscription → Account | `acme.sqlite::subscriptions.['account_id']` | subscription_of |
| Invoice → Account | `acme.sqlite::invoices.['account_id']` | 불인정 |
| Invoice → Subscription | `acme.sqlite::invoices.['subscription_id']` | invoice_for |
| TicketOpened → Account | `support.log::ticket opened.['account_id']` | ticket_for |
| TicketOpened → Contact | `support.log::ticket opened.['requester_id']` | 불인정 |
| ProductUsage → Account | `product_usage.jsonl.['account_id']` | 불인정 |
| Contact → Role | `acme.sqlite::contacts.role` | 불인정 |
| Subscription → Plan | `acme.sqlite::subscriptions.plan` | on_plan |
| TicketOpened → Category | `support.log::ticket opened.category` | 불인정 |
| MeetingOrCall → Account | `mentions` | 불인정 |
| MeetingOrCall → Contact | `mentions` | 불인정 |
| MeetingOrCall → TicketOpened | `mentions` | 불인정 |

`mentions` 세 연결은 attended_by/conversation_with/discussed의 명시적 의미 관계가 아니므로 인정하지 않는다. promised_to도 누락됐다. Invoice→Account의 선언 FK는 전이 경로가 있어도 유지했으나 참조 링크 대응은 없다. ENDPOINT ordered-pair 구조 투영은 10/13=76.92%, 10/11=90.91%이며 **의미 정확도가 아니다**. 전체 13예측/11참조 분모를 축소하지 않는다.

코드 독립 결정은 타입 6+링크 7=13/23(56.52%), 모델 의존 hybrid는 타입 4+링크 6=10/23(43.48%)다. 이는 출력 요소의 출처 비율이며 추론 노력·시간 비율이 아니다.

## 사실 감사·누락

동결 선택은 canonical doc/section/sentence/subject/relation/object의 SHA256 순 min(20,N)이다. N=3이므로 전수 감사했으며 2/3=66.67%가 지지된다. 감사자는 코드 modifier와 다른 조정자이며 두 번째 사람의 독립 감사는 아니다. 인용 원문 존재 3/3은 의미 정답 3/3이 아니다. 원문 문장은 재인용하지 않는다.

| 파일 | 행 | 소스 SHA256 | 사실 SHA256 | 명제 지지 | 한국어 판정 |
|---|---:|---|---|---|---|
| `docs/calls/Pinecrest QBR 2026-09-15.md` | 23 | `7f90b63f9ad9653c9524938ae2eedff79541e8ae318ff6bc678693a50e641ff2` | `88cf72eb46546125b72884533763f44769549c69fc9543f161413b2fc0901a9e` | False | 금액을 인용 행위의 주체로 잘못 추출했다. 원문의 인용 주체와 일치하지 않는다. |
| `docs/reference/Acme Corp plans and pricing 2026.md` | 29 | `43de20f971d4dce47916aed7b58478928c7cdffa7d5f477e56588c5c2b57d665` | `b97a50065359d1b862cb69396170a083d23aa3da1324214f07de177ba7590b6c` | True | 승인이 필요하다는 대상과 관계가 원문 절에서 직접 확인된다. |
| `docs/calls/Brightmoor renewal call 2026-10-21.md` | 14 | `e62bf657fdf6b44042b3bb09b8ef6a89a69a3d6b07672dad5f3208c13a30edfb` | `c5cfb1b65f32e4254c1fc884f22231d86adfe866e805a842c8fe678fc918ab15` | True | 계정의 요금제 간 좌석 분할 금지라는 주체·부정·대상이 원문 설명과 일치한다. 원문 전체에 발화자도 보존되어 있다. |

150문장 단위 중 147개는 grounded fact가 없고 3개는 extractor capacity=1 때문에 partial이다. uncovered 150은 150개 모두 전혀 읽지 않았다는 뜻이 아니다. span 거절 5, 의미 거절 25가 기록됐다. 문장당 최대 한 명제라 채택된 사실이 있어도 전체 명제 커버리지는 보장하지 않는다.

## Gold 반복과 안정성

두 gold 실행을 각각 확인하면 모두 약속 1/4, 부정 약속 trap의 거짓 채택 0/2, 기한 있는 양성의 기한 보존 0/3이다. 수신자를 포함한 약속 기준으로 평가했고, 누락된 세 양성은 수신자·날짜도 회수되지 않았다. 1사실이 있어도 타입/링크 0/0으로 `empty ontology run`, status=failed다. 이를 성공한 문서 온톨로지로 세지 않는다. gold는 알려진 합성 회귀 자료이며 blind 검증이 아니다.

두 Acme 실행에서 타입 10/10, 링크 13/13, 사실 3/3의 교집합/합집합이 일치해 각 Jaccard=1.0이고 full ontology/facts도 같다. gold의 사실·온톨로지도 같다. 반복 안정성은 정확성을 뜻하지 않으며 같은 실패가 반복될 수 있다.

## 개발 이력과 이전 실패

Acme 혼합 fixture와 개발 자료를 사전에 봤다. 첫 문서 Summary의 처음 3문장을 문장당 한 항목 추출 prompt 재설계에 사용했다. 중립 정수 prompt의 스레드 1/4/8/16 및 8 재확인으로 8을 선택했다. 상세 시간은 measurements.json의 development 원장에 있으며 일반 최적값이라는 뜻은 아니다. default-thread 시도는 2호출 완료 후 중단됐다.

이전 2400-token 출력 예산 구현은 gold call 4(LLM 합계 167.259231초)와 Acme call 10(171.474016초)에서 done_reason=length로 실패했고 완성 온톨로지를 만들지 못했다. 실패 코드 해시와 마지막 호출 metadata를 development 원장에 보존했다. 이후 최종 코드 해시는 hashes.json과 일치하며 최종 반복 사이 조정은 없다. 이전 README의 pending/no-live-tuning 표현은 이 실행 이력으로 대체한다.

## 구현·공개 한계

JSONL export는 live NoSQL DB connector가 아니다. 중첩 배열은 보존하지만 정규화하지 않는다. 자유 형식 로그는 보존하며 의미 파싱하지 않는다. 폴더 경로는 분류 문맥에만 쓰며 폴더 온톨로지·계층이 없다. OWL/SHACL/규칙 및 문맥 의존 문장 간 추론은 없다. 같은 약한 모델의 검증은 독립 진실 판정기가 아니다.

공개 범위는 코드와 측정 metadata다. 새 raw facts/cache/tables/ontology dump, 원문 SQL·문서·참조 acme.json은 비공개다. 기존 공개 합성 `evidence/real-model/gold.md`/`gold.txt`는 유지한다. 과거 sys fragment 파일의 공개 제외도 유지한다. 선택적 portable evaluator는 추가하지 않았다. 계산은 고정 alias/source 대응, 실제 via 열과 동결 literal 열의 대조, 전체 출력 분모로 재현하며 대응표와 평가 스크립트 해시는 evaluation.json/hashes.json에 있다. 이 역할은 공개 재빌드·전체 scan·독립 검수·commit/push를 수행하지 않았다.

## 해시 연결

- protocol_sha256: `dbc2b8673b7b5afe247278954479f2cc3182e31672925968611757caa644d1dd`
- onto_sha256: `400e86746580509e8d79ac038769f2d990a29c7938f6e98267925e5178c7a575`
- builder_sha256: `8eb1476a6270f6af14b7858bbf66df1dd1c9ff20a1ad67dfb87234f5ef5994c7`
- reference_sha256: `c477ae87689f7d67bd00a4df2940450c29e46d935e739dcaaeeb91e504cdfb8c`
- upstream: HelixDB/helix-foundry `c7de40515f56a491d1b46af0bb1efa890f106700`, Apache-2.0. 입력별 bytes/SHA256과 비공개 출력 해시는 [hashes.json](hashes.json)에 있다.
