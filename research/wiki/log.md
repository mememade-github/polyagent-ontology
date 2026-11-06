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

## [2026-11-06] lint | 저장소 수록본 정제

[SCHEMA](SCHEMA.md)의 "저장소에 없는 Raw" 기준으로 파일을 제외하고 식별자를 치환했다. 그래서 `sources/`의 해시 값이 수집 당시와 달라졌다.
