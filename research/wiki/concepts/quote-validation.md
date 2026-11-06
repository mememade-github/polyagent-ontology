# 인용 대조 (quote validation)

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

~~**이 페이지의 Helix 인용 대조 메커니즘은 확정되지 않았다.** [QV-P1](#QV-P1)의 결과가 새 raw 소스로 들어오면 갱신한다. 아래 Helix 표는 입력별 판정 관찰이며, 판정 원리의 설명이 아니다.~~ → **results.md 갱신:** 판정 경로의 해석은 [`locate_quote` 경로](#QV-20)에 있다. 이는 [디컴파일]이며 [실행]보다 약하다. `normalize` 내용과 임계값의 raw는 미입증이다. 12변형 표는 입력별 판정 관찰로 그대로 둔다. 관련: [판정](second-verifier.md), [근거 위치](evidence-spans.md), [Helix](../products/helix-foundry.md), [논문/RAGFlow](../products/paper-ragflow.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-01](../contradictions.md#C-01) (세분) Helix 인용 대조 범위
- [C-10](../contradictions.md#C-10) (논문과 코드 불일치) RAGFlow: 저장 규칙, exact, 온톨로지 템플릿
- [C-16](../contradictions.md#C-16) (미확정) Helix 인용 대조 메커니즘

## Helix: 주입 실험

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QV-01"></a>QV-01 | 문서에 없는 인용 주입 | [실행/Stub] | F:134, I:62, E:helix/report3.raw, E:helix/stub2.py | `Jane Doe guaranteed a full refund`가 reject `quote_not_in_source`이다. 판정 항목에 `confidence`가 없다 | findings.md의 "문서에 없는 인용" 범위는 [QV-02](#QV-02)~[QV-13](#QV-13)으로 세분됐다. [C-01](../contradictions.md#C-01) |

## Helix: 인용 12변형

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QV-02"></a>QV-02 | 원문 그대로 | [실행/Stub] | I:49, E:rea/quote/r_exact.raw, E:rea/quote/run.py | accept, span 26–71, section 1 | ~~판정 메커니즘 미확정. [QV-P1](#QV-P1)~~ → 판정 경로 [QV-21](#QV-21). 정규화 내용은 미입증([QV-20](#QV-20)) |
| <a id="QV-03"></a>QV-03 | 대문자 | [실행/Stub] | I:50, E:rea/quote/r_case.raw | accept, span 26–71 | ~~메커니즘 미확정. [QV-P1](#QV-P1)~~ → 판정 경로 [QV-21](#QV-21). 정규화 내용은 미입증([QV-20](#QV-20)) |
| <a id="QV-04"></a>QV-04 | 공백·줄바꿈 다름 | [실행/Stub] | I:51, E:rea/quote/r_space.raw | accept, span 26–71 | ~~메커니즘 미확정. [QV-P1](#QV-P1)~~ → 판정 경로 [QV-21](#QV-21). 정규화 내용은 미입증([QV-20](#QV-20)) |
| <a id="QV-05"></a>QV-05 | `%` 제거 | [실행/Stub] | I:52, E:rea/quote/r_punct_dropped.raw, E:rea/quote/doc.md | accept, span 26–72. 원문을 그 범위로 자르면 뒤의 콤마까지 포함한 `...service credit,`이다(이 세션의 바이트 슬라이스 계산). 인용은 44바이트, span은 46바이트이다 | ~~span이 인용보다 2바이트 긴 이유는 미확인이다. interim.md에 언급 없음. [C-16](../contradictions.md#C-16)~~ → 퍼지 창이 쉼표까지 포함했다는 해석이 있다([QV-28](#QV-28)). 직접 관찰은 아니다 |
| <a id="QV-06"></a>QV-06 | 전각 `％` | [실행/Stub] | I:53, E:rea/quote/r_fullwidth.raw | accept, span 26–71 | ~~메커니즘 미확정. [QV-P1](#QV-P1)~~ → 판정 경로 [QV-21](#QV-21). 정규화 내용은 미입증([QV-20](#QV-20)) |
| <a id="QV-07"></a>QV-07 | 단어 중간에서 시작·끝 | [실행/Stub] | I:54, E:rea/quote/r_midword.raw | accept, span 27–69. 잘린 범위가 `ane Doe ... cred`이다 | ~~메커니즘 미확정. [QV-P1](#QV-P1)~~ → 판정 경로 [QV-21](#QV-21). 정규화 내용은 미입증([QV-20](#QV-20)) |
| <a id="QV-08"></a>QV-08 | 한국어 NFC | [실행/Stub] | I:55, E:rea/quote/r_ko_nfc.raw | accept, span 102–150 | ~~메커니즘 미확정. [QV-P1](#QV-P1)~~ → 판정 경로 [QV-21](#QV-21). 정규화 내용은 미입증([QV-20](#QV-20)) |
| <a id="QV-09"></a>QV-09 | 한국어 NFD | [실행/Stub] | I:56, E:rea/quote/r_ko_nfd.raw | accept, span 102–150 | ~~메커니즘 미확정. [QV-P1](#QV-P1)~~ → 판정 경로 [QV-21](#QV-21). 정규화 내용은 미입증([QV-20](#QV-20)) |
| <a id="QV-10"></a>QV-10 | `...`로 생략 | [실행/Stub] | I:57, E:rea/quote/r_ellipsis.raw | reject `quote_not_in_source`. `calls`에 `judgements`가 없다 | ~~거부 경계는 이 한 입력만 보여 준다. [QV-P1](#QV-P1)~~ → 퍼지 경계 관찰은 [QV-24](#QV-24), [QV-25](#QV-25) |
| <a id="QV-11"></a>QV-11 | 의역 | [실행/Stub] | I:58, E:rea/quote/r_paraphrase.raw | reject `quote_not_in_source`. `calls`에 `judgements`가 없다 | ~~거부 경계는 이 한 입력만 보여 준다. [QV-P1](#QV-P1)~~ → 퍼지 경계 관찰은 [QV-24](#QV-24), [QV-25](#QV-25) |
| <a id="QV-12"></a>QV-12 | 다른 섹션의 문장 | [실행/Stub] | I:59, E:rea/quote/r_other_section.raw, E:rea/quote/stub.py | reject `quote_not_in_source`. Stub이 section 1 호출에 section 2 문장을 인용으로 돌려줬다. `calls`에 `judgements`가 없다 **results.md 갱신:** [QV-29](#QV-29) | 섹션 제한은 이 한 입력의 관찰이다 |
| <a id="QV-13"></a>QV-13 | 한국어 띄어쓰기 제거 | [실행/Stub] | I:60, E:rea/quote/r_ko_space.raw | reject `quote_not_in_source`. `calls`에 `judgements`가 없다 | 공백 변형([QV-04](#QV-04))과의 처리 차이가 어디서 오는지 미확인이다 **results.md 갱신:** 점검은 [QV-31](#QV-31). 경로 표시는 raw에 없다 |

## Helix: 해석

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QV-14"></a>QV-14 | interim.md의 해석: "바이트 일치가 아니라 정규화 후 비교이며, 같은 섹션 안으로 제한된다" | [미입증] | I:62 | 관찰된 것은 입력별 판정뿐이다. 함수 내부는 읽히지 않았다([SYM-14](binary-symbols.md#SYM-14)). 코디네이터 메시지가 이 절의 개정을 예고했다([QV-P1](#QV-P1)). [C-16](../contradictions.md#C-16) **results.md 갱신:** I:62의 "정규화 후 비교"는 정확 검색 다음의 퍼지 경로가 빠진 해석으로 대체됐다([QV-21](#QV-21), [QV-22](#QV-22)) | ~~정규화 방식, 유사도 사용 여부, 임계값 모두 미확정이다~~ → 유사도 사용은 [QV-22](#QV-22), 임계값은 [QV-23](#QV-23). 정규화 방식은 미입증 |
| <a id="QV-15"></a>QV-15 | accept 8건, reject 4건의 검증 모델 전달 | [실행/Stub] | E:rea/quote/r_*.raw (`calls`) | 이 세션에서 raw 12개를 파싱했다. accept 8건에는 `judgements` 호출이 있고 reject 4건에는 없다 | 검증 확률은 0.95로 고정된 Stub 값이다(I:45) |

## ~~대기 중~~ → results.md로 수집된 통지
| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QV-P1"></a>QV-P1 | ~~인용 대조가 rapidfuzz 유사도 함수를 호출한다는 코디네이터 통지(결과 대기)~~ → `extraction::text::locate_quote`가 rapidfuzz indel 유사도를 호출한다는 통지, results.md로 수집됨 | ~~[미입증]~~ → [디컴파일] ([QV-22](#QV-22)) | ~~코디네이터 메시지 2026-11-06. raw 소스 없음~~ → R:19, R:23, E:rea/decompiled/extract/locate_quote.c, 코디네이터 메시지 2026-11-06 | 통지 내용은 "validator가 rapidfuzz 유사도 함수를 호출하며 임계값 시험이 진행 중"이다. grep `rapidfuzz` 결과: evidence/ 0건, auto-ontology·helix-foundry·ragflow 클론 0건(lock 파일 제외). 통지는 어느 validator인지 명시하지 않았다 **results.md 갱신:** 통지의 validator는 `extract` 바이너리의 `extraction::text::locate_quote`이다. c 파일에 `rapidfuzz` 심볼 호출이 있다. 세 클론 grep 0건은 이와 충돌하지 않는다 | ~~호출 여부, 함수, 임계값, 대상 validator가 모두 미입증이다. 결과가 새 raw 소스로 들어오면 이 절을 갱신한다~~ → 호출과 함수는 [디컴파일]. 임계값 값은 [QV-23](#QV-23), 정규화는 [QV-20](#QV-20)이 미입증 |

## RAGFlow: 검증기 복사 실행

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QV-R1"></a>QV-R1 | verbatim | [실행] | F:180, E:ragflow/validator_copy.go, RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:452 | soft와 hard 모두 유지, offset 기록(기록만). 모델 없음 | 출력 원본 없음 |
| <a id="QV-R2"></a>QV-R2 | 공백·줄바꿈 다른 인용 | [실행] | F:181, RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:549 | 유지, offset 기록(기록만). `normalizeForMatch`는 공백류를 한 칸으로 접는 코드이다. [C-10](../contradictions.md#C-10) | 대소문자 변형은 이 입력 집합에 없다 |
| <a id="QV-R3"></a>QV-R3 | 한국어 인용 | [실행] | F:182, E:ragflow/validator_copy.go | 유지, offset 기록(기록만) | NFD, 띄어쓰기 제거 변형은 시험되지 않았다 |
| <a id="QV-R4"></a>QV-R4 | 의역 인용 | [실행] | F:183, RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:445-448 | soft는 claim 유지·근거 제거, hard는 claim 제거(기록만) | 출력 원본 없음 |
| <a id="QV-R5"></a>QV-R5 | 근거 없는 claim | [실행] | F:184, RF:internal/ingestion/component/knowledge_compiler/tree/claims.go:463 | soft와 hard 모두 유지(기록만) | 출력 원본 없음 |

## results.md: `locate_quote` 경로

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QV-20"></a>QV-20 | 1단계: 인용을 `text::normalize`로 정규화, 3글자 미만이면 찾지 못함 | [디컴파일] | R:19, R:21, E:rea/decompiled/extract/locate_quote.c | `normalize` 호출, 글자 수 `< 3` 분기를 해당 c 파일에서 확인했다 | `normalize`의 내용은 미입증이다. `normalize.c`가 evidence/에 없다. 대문자, NFD, 전각 처리의 이유도 그래서 미입증이다. [C-18](../contradictions.md#C-18) |
| <a id="QV-21"></a>QV-21 | 2단계: 섹션 본문을 정규화하고 정규화 문자열에서 정확 검색 | [디컴파일] | R:22, E:rea/decompiled/extract/locate_quote.c | `StrSearcher`, `MatchIndices` 수집을 확인했다. 수집 결과가 비어 있지 않으면 그 목록을 돌려주는 분기로 읽힌다 | 여러 위치에 일치할 때 어떤 span이 판정에 쓰이는지 관찰되지 않았다 |
| <a id="QV-22"></a>QV-22 | 3단계: 정확 검색 결과가 없으면 어절 수 n−1..n+1 창에서 `rapidfuzz` indel `normalized_similarity` 최댓값을 구함 | [디컴파일] | R:23, E:rea/decompiled/extract/locate_quote.c | `rapidfuzz` indel 유사도 심볼 호출과 창 반복을 확인했다 | 변수 이름이 없는 의사코드의 해석이다. Rust 크레이트의 유사도 정의를 이 위키가 직접 읽지는 않았다 |
| <a id="QV-23"></a>QV-23 | 4단계: 최댓값이 0.95 이상이면 창의 원본 바이트 범위를 span으로 돌려줌 | [바이너리] | R:19, R:24, E:rea/decompiled/extract/locate_quote.c | 의사코드에 상수와 유사도의 비교가 있고, 상수 위치는 R:19의 `.rodata` 값과 맞는다(기록만) | 0.95라는 값은 results.md의 기록만 있다. `.rodata` 덤프가 evidence/에 없다. 간접 점검은 [QV-31](#QV-31) |

## results.md: 퍼지 변형 실행

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QV-24"></a>QV-24 | 앞 단어를 `zzzz`로 바꾼 변형 7건(`sub1`~`sub7`) | [실행/Stub] | R:26, E:rea/quote/fuzzy.json, E:rea/quote/run2.py | 전부 reject `quote_not_in_source` | 입력별 관찰이다 |
| <a id="QV-25"></a>QV-25 | 끝에서 두 번째 글자부터 앞으로 X로 바꾼 변형 8건(`char1`~`char14`) | [실행/Stub] | R:26, E:rea/quote/fuzzy.json, E:rea/quote/run2.py | `char1`만 accept, span 26–72. `char2` 이상 reject. run2.py는 마지막 글자 `t`를 남긴다(R:26의 "끝의 글자"는 이 뜻이다) | 문장 길이가 다르면 경계가 어디로 가는지 관찰되지 않았다 |
| <a id="QV-26"></a>QV-26 | 오타 2개 인용(`typo_mid`) | [실행/Stub] | R:26, E:rea/quote/fuzzy.json | accept, span 26–72 | 입력별 관찰이다 |
| <a id="QV-27"></a>QV-27 | 단어 하나 인용 `Globex` | [실행/Stub] | R:26, E:rea/quote/fuzzy.json | accept, span 44–50 | 다른 짧은 인용은 시험되지 않았다. [QV-30](#QV-30) |

## results.md: 해석

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QV-28"></a>QV-28 | span 26–72가 퍼지 창이 뒤 쉼표까지 포함한 결과라는 해석 | [디컴파일] | R:28, E:rea/quote/r_punct_dropped.raw, E:rea/quote/fuzzy.json | `% 제거`, `char1`, `typo_mid` 세 입력의 span이 모두 26–72임을 raw로 확인했다. R:28 스스로 "해석"이라고 쓴다 | 퍼지 경로가 원인이라는 직접 관찰은 없다. 경로를 표시하는 출력이 raw에 없다 |
| <a id="QV-29"></a>QV-29 | 대조 범위가 인용이 나온 섹션 하나인지 | [실행/Stub] | R:29, [QV-12](#QV-12), E:rea/decompiled/extract/locate_quote.c | `other_section` reject 1건의 관찰이다. 함수는 본문 하나를 인자로 받는 형태로 읽힌다 | 호출자가 어떤 본문을 넘기는지는 읽히지 않았다 |
| <a id="QV-30"></a>QV-30 | results.md의 진술: 임의의 짧은 단어 인용도 섹션에 있으면 통과, 사실 여부는 검증 모델 몫 | [실행/Stub] | R:30, [QV-27](#QV-27), [QV-20](#QV-20) | 관찰은 `Globex` 1건이다. "낮은 품질", "임의의", "검증 모델 몫"은 results.md의 서술이며 이 위키는 관찰로 올리지 않는다. [C-19](../contradictions.md#C-19) | "임의의"의 범위, 검증 모델의 실제 판별 능력 |

## 이 위키의 산술 점검
| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QV-31"></a>QV-31 | raw 29건 판정과 R:21-24 경로의 일치 점검 | [미입증] | E:rea/quote/r_*.raw, E:rea/quote/fuzzy.json, E:rea/quote/doc.md | 바이너리를 돌리지 않고 메모리 안에서 계산했다. 가정: NFKC + 소문자, 공백 분리 어절, 구두점 유지, 임계값 0.95. 12변형과 17변형 모두 판정이 일치했고(29/29), 퍼지 accept 3건의 span도 26–72로 일치했다. 유사도는 accept 최저 0.9663, reject 최고 0.9451(`char2`)이었다 | 가정한 정규화는 입증되지 않았다. 일치는 경로와 값을 입증하지 않으며 모순이 없다는 점만 보여 준다 |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
- [C-18](../contradictions.md#C-18) (근거 공백) `normalize` 내용과 I:83의 디컴파일 목록
- [C-19](../contradictions.md#C-19) (서술 범위) R:30의 일반화
