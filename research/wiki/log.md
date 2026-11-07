# Log

시간순 기록이다. `grep "^## \[" log.md`로 조회한다. 소스는 아래 순서로 하나씩 읽었고, 요소 행을 소스별로 대조한 뒤 페이지 파일은 한 번의 생성 작업으로 썼다.

## [2026-11-06] ingest | findings.md

sha256 앞 16자 `4712d35e1e9e2be5`. 요소 165개. 인용 행은 뒤 클론 대조에서 확인. [요약](sources/findings.md)

## [2026-11-06] ingest | evidence/ao

스크립트 8개. 원시 출력 없음. 요소 18개가 인용. [요약](sources/evidence-ao.md)

## [2026-11-06] ingest | evidence/helix

`report3.raw`로 F:131-138 대조 일치. 요소 26개가 인용. [요약](sources/evidence-helix.md)

## [2026-11-06] ingest | evidence/ragflow

복사본 세 함수와 업스트림 동일 확인. 요소 4개가 인용. [요약](sources/evidence-ragflow.md)

## [2026-11-06] ingest | evidence/rea (draft, quote, window, rust-*.json)

인용 raw 12개 파싱, I:49-60과 대조 일치. `out2.ndjson`과 I:28 대조 일치. 요소 26개가 인용. [요약](sources/evidence-rea.md)

## [2026-11-06] ingest | evidence/rea/interim.md

sha256 앞 16자 `8c11e6e54bae6cad`. findings.md보다 새 기록. 요소 55개. 변경은 [대조 기록](contradictions.md)에 기록. 인용 대조 절은 개정 예정 통지가 있어 미확정으로 수집. [요약](sources/interim.md)

## [2026-11-06] ingest | 업스트림 클론과 논문 텍스트(휘발성)

세 클론의 HEAD가 F:17, F:18, F:21과 일치. 인용 행 내용 출력 대조, 논문 인용 문장 대조. [요약](sources/upstream-and-paper.md)

## [2026-11-06] lint | 전체 점검 1회차

생성 후 스크립트로 검사했다. 페이지 29개, 요소 219개. 깨진 링크 0, 고아 페이지 0, 미해결 내부 ID 0, 인용 없는 요소 0, findings.md 대응 없는 내용 행 0, interim.md 대응 없는 내용 행 0.

interim.md가 findings.md를 바꾸거나 세분한 곳(양쪽 유지):

- [C-01](contradictions.md#C-01) 인용 대조 범위: F:134 → I:49-62
- [C-02](contradictions.md#C-02) 초안 완주와 원인: F:145, F:198 → I:26, I:28
- [C-03](contradictions.md#C-03) 창 옵션: F:215 → I:76
- [C-04](contradictions.md#C-04) 패스 구성: F:109 → I:17, I:73, I:85
- [C-06](contradictions.md#C-06) 사람 승인: F:108, F:197 → I:19, I:28, I:85
- [C-14](contradictions.md#C-14) 프로바이더: F:216 → I:18
- [C-15](contradictions.md#C-15) context_tokens: F:217 → I:41
- [C-16](contradictions.md#C-16) 인용 대조 메커니즘: 미확정, 새 raw 소스 대기

그 밖의 불일치: [C-05](contradictions.md#C-05), [C-07](contradictions.md#C-07), [C-08](contradictions.md#C-08), [C-09](contradictions.md#C-09), [C-10](contradictions.md#C-10), [C-11](contradictions.md#C-11), [C-12](contradictions.md#C-12), [C-13](contradictions.md#C-13).

위키 안에서 고친 것: 실험 번호와 어긋나던 knockout 요소 ID를 K0, K1, K1B, K2~K6, A3로 맞췄다. 제목과 코드 펜스 행을 요소 출처에서 뺐다. SV-08의 논문 행을 p.txt:432로 고쳤다. 페이지 머리말에 관련 링크를 두어 고아 페이지와 누락 교차 참조를 없앴다. raw 파일은 수정하지 않았다.

수집 시점 해시 재확인: findings.md `4712d35e1e9e2be5`, interim.md `8c11e6e54bae6cad`.

## [2026-11-06] ingest | evidence/rea/results.md와 그 파일들

sha256 앞 16자 `5bd0b7f2fc9e08d6`. [요약](sources/results.md). 새 등급 [디컴파일], [바이너리]를 SCHEMA에 추가했다. 새 요소 51개. 앞선 행은 지우지 않고 `~~원문~~ →` 표기로 대체했다. 각 주장을 raw와 대조했다. 바이너리 실행과 컨테이너 시작은 없었다. 다만 인용 판정 raw에 대한 메모리 내 산술 점검([QV-31](concepts/quote-validation.md#QV-31))을 했고, 미입증으로 표기했다.

## [2026-11-06] lint | 전체 점검 2회차

페이지 30개, 요소 270개. 깨진 링크 0, 고아 페이지 0, 미해결 내부 ID 0, 형식 불량 행 0, results.md 대응 없는 내용 행 0, 수집 후 바뀐 raw 0.

results.md에 따른 갱신: [C-01](contradictions.md#C-01), [C-02](contradictions.md#C-02), [C-03](contradictions.md#C-03), [C-04](contradictions.md#C-04), [C-06](contradictions.md#C-06), [C-07](contradictions.md#C-07), [C-12](contradictions.md#C-12), [C-14](contradictions.md#C-14), [C-15](contradictions.md#C-15), [C-16](contradictions.md#C-16).

results.md가 관련된 새 항목: [C-17](contradictions.md#C-17) 잠금 문장이 raw에 없음, [C-18](contradictions.md#C-18) `normalize` 파일 없음, [C-19](contradictions.md#C-19) 일반화 표현, [C-20](contradictions.md#C-20) 전 구간과 Foundry 경로, [C-21](contradictions.md#C-21) 하한과 `settle`, [C-22](contradictions.md#C-22) REA 상태와 심볼 이름.

수집 시점 해시: findings.md `4712d35e1e9e2be5`, interim.md `8c11e6e54bae6cad`.

## [2026-11-06] ingest | 누락 원본 보존과 C-12, C-17, C-18 갱신

조정자가 스크래치패드의 원본을 evidence/로 복사하고 위 세 항목에 갱신 줄을 추가했다. 나머지 페이지는 변경하지 않았다. human-approval 페이지의 해당 행은 아직 "기록만" 표기일 수 있으며 contradictions.md의 C-17 갱신이 우선한다.

## [2026-11-06] query | 지식 추출 기법 비교와 구현 수준

답을 [extraction-techniques](extraction-techniques.md)에 남겼다. RAGFlow 추출 경로 누락을 [C-23](contradictions.md#C-23)에 기록하고, E:ragflow/compile/과 `extract`, `ingest-mapped`의 `--help` 출력(E:helix/)을 새 raw로 추가했다. 기존 페이지의 행은 고치지 않았다.

## [2026-11-06] query | 추출·저장·사용과 품질 보장, 구현 가능 여부

답을 [knowledge-lifecycle](knowledge-lifecycle.md)에 남겼다. 새 raw: E:helix/grpc/, E:real-model/, E:ragflow/compile/rf_fault.out. [C-24](contradictions.md#C-24)~[C-26](contradictions.md#C-26) 추가. 실제 모델 실행이 처음 들어갔다. 기존 페이지 행은 고치지 않았다.

## [2026-11-06] lint | 등록 전 점검

고아 0, 소스 해시 변경 0(104행), 금지 표현 0. 수정: 축약 인용 4건 전체 경로화, `[실행/실모델]` 등급 정의, M-10·TK-11·XT-16 대체 표기, real-model 소스 페이지 추가, rf_use.out을 빌드 실패로 표기. `E:rea/quote/r_`는 접두 표기라 유지. 비밀 패턴: 실제 자격증명 없음(실험용 더미 값뿐이다). 디컴파일 출력과 캡처 프롬프트는 저장소에 넣지 않았다. 디컴파일을 읽어 풀어 쓴 설명은 연구 결과로 유지한다.

## [2026-11-06] lint | 독립 검수 반영

독립 검수 지적을 반영해 LC-02, 03, 07, 12, 21, 22, 24, 25, 29, 31, 32, 33, 41, 44, 45와 C-26을 고쳤다. 이전 보고의 "정답 1건"과 속도 9–13 t/s 단정은 근거와 맞지 않아 정정했다. 해시 행 없는 raw에 행을 추가하고, 토큰 수치를 E:helix/grpc/token_summary.json으로 보존했다.

## [2026-11-06] ingest | 논리 구조화와 실모델 뼈대 생성

관리자 판단에 따라 [논리 구조화](concepts/logical-structuring.md)와 [evidence/skeleton](sources/evidence-skeleton.md)을 추가했다. Helix 초안은 네 조건 모두 항목 0이었다. Auto-Ontology는 테이블 DB에서 Term을 만들었고 문서 테이블에서는 `Documents`만 만들었다. 이전 문제 정의는 철회했고 새 문제 정의는 기록하지 않았다.

## [2026-11-06] ingest | 새 접근 범위·논문·동결 규약

사용자가 새 설계·구현·실측을 승인해 이전 as-is 범위 제외를 대체했다. 역사 표는 보존했다. [논문](sources/papers-20261106.md) 13건은 조정자의 선택 독해 메모를 근거로 정리했고 다운로드 파일의 전체 SHA256을 대조했다. 전문 독해·재현은 주장하지 않는다. [설계](concepts/paper-informed-design.md)는 출처·한계를 연결한 새 통합 선택이며 효과와 신규성은 미입증이다. 동결 규약을 바이트 그대로 보존했다. 결과는 대기 중이다. WIP는 권위 원본으로 유지한다. 공개 빌더의 추가 누출 제외·코드/측정 허용 범위를 갱신했으며 재빌드는 아직 실행하지 않았다.

## [2026-11-06] ingest | 동결 프로토타입 실측·공개 metadata

[실측 결과](concepts/prototype-results.md)와 [소스 해시 원장](sources/evidence-prototype.md)을 추가했다. 준비 신호 이후 measurements/evaluation/stability/hashes 네 payload를 그대로 수집했다. [설계](concepts/paper-informed-design.md)의 pending 상태와 gold 공개 범위 오류를 정정했다. STRICT 사전 열 이름 가정 오류를 공개하고 주 점수·프로토콜을 보존했다. Acme 문서 의미 유도 부진, gold 두 실패, 이전 length실패·튜닝 이력도 포함했다. 새 추론·공개 재빌드·독립 검수·commit/push는 이 문서 역할에서 하지 않았다.

## [2026-11-06] lint | 관측 키와 결과 상태 기술 정정

실행 원본 ontology.json을 대조해 ProductUsage의 관측 복합 키 후보 `(account_id, month)`를 [결과](concepts/prototype-results.md)에 정정했다. 선언 키 부재와 후보 키 부재는 다르다. SCHEMA의 대기 문구를 결과 링크로 갱신했으며 코드·동결 규약·수치는 유지했다.

## [2026-11-06] ingest | QD-Rec 코드·논문과 실험 agent 관계

관리자 지시에 따라 [QD-Rec](products/qd-rec.md) 27개 홈 행과 [소스 원장](sources/qd-rec.md)을 추가했다. 지정 경로에 depth 1·부분 클론을 받아 커밋 `3a04ed170583e14ca08e689e8bff8fddf267dc8e`를 고정했다. shared 루프·bandit·archive와 도메인 코드를 읽고, arXiv 2610.23470v2의 선택 수치와 2610.40589v1의 역할·판정 구조를 대조했다. 기본 모델과 논문 조건 차이는 [C-27](contradictions.md#C-27)에 기록했다. 수집 metadata는 `E:qd-rec/`에 두었다. PDF 추출 도구 부재 후 HTML로 읽었다. 제품 실행·데이터/모델 다운로드·의존성 설치는 하지 않았으며 적용 가능성은 추론으로 표시했다. 기존 연구 원문·SCHEMA·스킬·research/는 수정하지 않았고 commit/push·컨테이너 생성도 하지 않았다.

## [2026-11-06] lint | QD-Rec 인용·해시·독립 검수

변경 페이지의 로컬 링크·앵커 206개, 코드 해시 31개, 논문/파생 파일 해시 5개, QD 홈 행 27개의 열·고유 ID와 로그 append-only를 검사해 통과했다. 독립 Codex 평가에서 문서 검수는 4/5였고, 남은 1개는 검수 읽기 범위가 Git ref/shallow 파일을 제외한 탓이었다. 별도 fresh 평가에서 실제 HEAD·shallow=true·깨끗한 upstream 상태와 31개 해시를 확인해 해당 공백을 해소했다(보충 검사 1/1). 첫 평가의 tomllib 부재는 표준 텍스트 검사로 우회 재검증했다. 두 평가는 저장소 밖 ephemeral 문맥에서 수행했으며 임시 runner는 기존 독립 실행·보고 검증 로직을 유지하고 빈 임시 디렉터리 정리만 rmdir로 바꿨다. 검사 보고서는 수집 스크래치패드의 `qd-rec-review/`에 있다. 이는 문서 검수이며 QD-Rec 실행·성능 재현이 아니다.

## [2026-11-06] ingest | QD 적응 A1/A2/A3 초안

[QDA 초안](concepts/qd-rec-adaptation.md)과 [소스 원장](sources/qd-rec-adaptation.md)을 추가했다. protocol SHA256 `ace4e402d240df3b18b58f69cf66b074a33e4af86d88fa12fbc3a003246db06f`를 실행 전에 lock했다. run-001은 scripted synthetic Stub 11검사 통과, callback39·실모델0이다. 독립 proposal/challenge는 관리자 요약임을 표시하고 입력 digest·접근 문맥을 procedure.json에 기록했다. fresh Modify는 독립 평가를 수행하지 않았다. 실제 tokenizer·총 token/서버 시간 driver·독립 heldout gold·품질 비교는 미실행이다. 초기 python 명령 부재는 python3로 재시도했으며 테스트 실패 run은 없었다. B 빌드·commit/push 없음. 기존 raw/onto.py/skills는 유지하고 WIP를 보존한다.

## [2026-11-06] ingest | QDA manuscript 수정

독립 계산 보고의 11+32 case/268 assertions, must-fix0을 보존했다. fresh manuscript 검토 5건을 미래 addendum으로 반영하고 현재 시각·해시를 잠갔다. 과거 raw와 mechanical verdict는 보존했다. 실제 모델 미검증, corpus/gold/driver 부재, 부모 최종 Evaluate 대기.

## [2026-11-06] lint | QDA 공개본 검증

지정 빌더 221파일 생성 후 check_wiki 통과: 링크1644/broken0, canonical16 해시170/mismatch0. 별도 linked64 메타 해시2, code/protocol/lock5 및 원 procedure/results/run 불변 대조 통과. 전체 Unicode40/byte40 sliding private-prompt 검사(73311/73579 source offsets), secret/IP/session scan은 hits0. 원 전문·upstream 복사본은 strict allowlist로 제외했다. 최초 검사는 외부 README URL을 local로 오인해 실패했고 공개 빌더 URL query 수정 후 통과했다. 이 기록 추가 후 최종 재빌드·재검사를 수행한다. 부모 최종 독립 Evaluate·commit/push는 아직 수행하지 않았다.

## [2026-11-06] lint | 외부 Markdown URL 검사 오류 수정

최초 공개 lint는 GitHub README.md의 HTTP URL을 로컬 경로로 오인해 1건 실패했다. 지정 check_wiki.py에서 URL scheme을 구분하도록 수정했고 원래 URL을 유지했다. 별도 작은 fixture에서 외부 URL 제외와 실제 누락 로컬 파일 검출을 모두 확인했다. 재빌드 결과 로컬 링크 1,644건·깨짐 0, 16자리 해시 170건·불일치 0. 공개 221파일에서 private sys.txt의 모든 40자 슬라이딩 위치(문자 73,311/바이트 73,579)와 비밀값·내부 IP·세션 경로를 검사해 검출 0건이었다. 이는 해당 검사 범위의 결과다.

## [2026-11-07] ingest | QD 실제 자료·실행 전 절차

[자료](concepts/qd-real-data.md)와 [절차](concepts/qd-real-procedure.md)에 QDR-D/QDR-P 고유 홈 행을 추가했다. 허용된 metadata/plan/Stub 및 두 scratch gate 보고만으로 정리했다. frozen analyzer/acquire와 두 보고를 exclusive-create로 bytes 그대로 보존했다. 6문서·12단위·7 eligible·5 deferred·gold85·미해결6·complete=false는 획득 전 metadata이며 diagnostic-only다. 실제 결과 수치는 아직 기록하지 않았다. 기존 raw/개념/source 원장·builder·research·동결 실행 코드는 변경하지 않았다. 모델·Docker·commit·재귀 refine 없음.

## [2026-11-07] ingest | QD 실제 결과 metadata 보고

[결과](concepts/qd-real-results.md) QDR-R 홈과 [전체 보고서](../evidence/qd-real/results.md), [해시 원장](sources/qd-real.md)을 추가했다. 공개 metadata만 사용했다. 15 arms+pre/post 완료, 세 가설 INCONCLUSIVE, Fact precision N/A 및 T0/F0/U1, confirmed cells0/4와 미확립 recall을 분리했다. 과거 raw를 보존했다. 소스 해시·표 수치 대조는 문서 범위에서 수행하며 부모 최종 build/privacy/독립평가/등록은 대기한다. 모델·Docker·재귀 refine·commit 없음.

## [2026-11-07] review | QDR 미해결 의미 표현 명확화

원고만 받은 독립 검토의 필수 수정1건을 반영했다. [결과](concepts/qd-real-results.md)의 T/F/U와 INCONCLUSIVE는 불변이다. 원고 수정 전 hash와 private 사본을 보존했다.

## [2026-11-07] lint | QDR 공개 검사와 원고 종결

[검증 기록](../evidence/qd-real/verification.json)에 링크/해시·69,986 sliding windows·비밀값/IP/세션 scan·mirror dry·completion checker 통과와 원고 수정종결을 기록했다. 긴 공백2곳만 공개 생성 단계에서 정규화했고 실행 코드는 불변, AST 동일이다. 최종 격리 평가는 별도 gate다.

## [2026-11-07] lint | 저장소 수록본 정제

[SCHEMA](SCHEMA.md)의 "저장소에 없는 Raw" 기준으로 파일을 제외하고 식별자를 치환했다. 그래서 `sources/`의 해시 값이 수집 당시와 달라졌다.
