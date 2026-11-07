# 혼합 소스 프로토타입 결과

[index](../index.md) · [설계](paper-informed-design.md) · [해시 원장](../sources/evidence-prototype.md) · [전체 결과·대응표](../../evidence/prototype/results.md)

작은 질문과 구조/사실 분리로 출처를 남기려 했지만, 실행 결과는 문서 의미 유도가 빈약한 혼합 소스 스키마 초안이다. 완성 온톨로지나 일반 성능·신규성은 입증되지 않았다. Acme는 prompt 조정에 사용한 개발 자료이며 gold도 알려진 합성 회귀 입력이다.

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증·한계 |
|---|---|---|---|---|---|
| <a id="PX-01"></a>PX-01 | 두 Acme 실행 | [실행/실모델] | E:prototype/measurements.json | 각각 150단위, 타입10·링크13·사실3, 189호출. wall 269.967564/202.643924초, prompt 최대340 | built는 의미 품질 성공이 아니다 |
| <a id="PX-02"></a>PX-02 | 타입 대응 | [실행/실모델] | E:prototype/evaluation.json, E:prototype/results.md | frozen precision8/10, recall8/9. TicketOpened→Ticket은 티켓당 로그 행, ProductUsage→MonthlyUsage는 계정/월 행, MeetingOrCall→Conversation은 문서 교환 분류. Role/Category 추가, Commitment 누락 | MonthlyUsage는 선언 키가 없지만 관측 복합 키 후보 `(account_id, month)`가 있음; frozen alias를 결과 후 변경하지 않음 |
| <a id="PX-03"></a>PX-03 | STRICT 동결 점수·오류 | [실행/실모델] | E:prototype/protocol.md, E:prototype/evaluation.json | STRICT5/13·5/11. 사전 contact_id/account_ref 가정이 실제 requester_id/account_id와 달라 소스 기반 2연결 제외. 문서 mentions도 attended_by/conversation_with/discussed로 세지 않음 | 5/11은 편향 없는 의미 품질 추정치가 아니다. 유리한 사후 재채점 없음. ENDPOINT10/13·10/11은 구조 투영이며 의미 정확도 아님 |
| <a id="PX-04"></a>PX-04 | 결정 출처 | [실행/실모델] | E:prototype/measurements.json | 코드 타입6+링크7=13/23(56.52%), hybrid 타입4+링크6=10/23(43.48%) | 추론 노력 비율 아님 |
| <a id="PX-05"></a>PX-05 | 사실 전수 감사 | [실행/실모델] | E:prototype/evaluation.json, E:prototype/results.md | min(20,N), N=3 중2지지(66.67%). 금액을 인용 주체로 잘못 추출한 1건. 파일·행·해시는 전체 결과에 보존 | quote 존재는 의미 정답이 아님. 147단위 grounded fact 없음, 3단위 capacity1 partial. uncovered150은 전부 미독해라는 뜻 아님 |
| <a id="PX-06"></a>PX-06 | gold·안정성 | [실행/실모델] | E:prototype/evaluation.json, E:prototype/stability.json | 두 gold 모두 약속1/4, trap 거짓 약속0/2, 기한0/3, 타입0으로 failed. Acme 타입/링크/사실 Jaccard각1, full출력 동일, cache hit0 | 반복 안정성은 정답 보장 아님; blind test 아님 |
| <a id="PX-07"></a>PX-07 | 조정·이전 실패 | [실행/실모델] | E:prototype/measurements.json | Acme Summary3문장으로 one-item prompt 조정, 중립 정수 prompt threads1/4/8/16 뒤8선택. 2400예산 gold call4·Acme call10 length실패, default-thread2호출 후 중단 | 실패 원장 보존. 일반 최적값·개선 우월성 미입증 |
| <a id="PX-08"></a>PX-08 | 범위·공개 | [실행/실모델] | E:prototype/hashes.json, E:prototype/results.md | SQLite4테이블569행+JSONL225+로그327+Markdown6, PDF3제외. Python3.10.12/Ollama0.40.10 CPU, 3.1B Q4_K_M, ctx8192/temp0/seed7/threads8 | JSONL은 live connector아님; 배열 보존만, 자유로그 의미파싱·폴더계층·OWL/SHACL/규칙·문장간추론 없음. 코드·메타데이터만 새 공개 |

동결 프로토콜 및 코드·입력·참조 SHA256, 라이선스와 파일 크기는 [해시 원장](../sources/evidence-prototype.md)에서 시작한다. 전체 대응 근거와 실패 이력은 [results.md](../../evidence/prototype/results.md)에 있다. 기존 공개 `evidence/real-model/gold.md`/`gold.txt` 합성 fixture는 유지하고 새 raw 모델 출력·facts/cache/tables/ontology dump와 샘플 본문은 공개하지 않는다.

**results.md 갱신:** 후속 [QD 실제 결과](qd-real-results.md)는 세 가설 모두 INCONCLUSIVE다. 이전 raw·역사 결과는 보존한다.
