# 엔티티 창 (entity windows)

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

Helix `extract`의 엔티티 패스 입력 분할 관찰이다. 토큰 수는 [컨텍스트 크기](context-budget.md)에도 있다. 모든 수치는 Stub 실행의 요청 크기이며 모델의 처리 능력과 무관하다.

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-03](../contradictions.md#C-03) (세분) 엔티티 창과 `--max-section-bytes`
- [C-04](../contradictions.md#C-04) (추가) 추출 패스 구성
- [C-07](../contradictions.md#C-07) (측정 범위 불일치) 토큰 측정 범위
- [C-12](../contradictions.md#C-12) (재현 근거 공백) "evidence/에 스크립트와 입력이 있다"

## 측정 조건

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="EW-01"></a>EW-01 | 입력과 측정 방식 | [실행/Stub] | I:66, E:rea/window/run.py, E:rea/window/stub.py | 550,798바이트 ASCII(600문단). 호출 순서는 동시 실행으로 뒤섞인다. 창당 토큰은 user 메시지와 system만 센 값이다(run.py의 `len(enc.encode(c))+len(enc.encode(str(b.get('system'))))`), 출력 스키마는 제외다. [C-07](../contradictions.md#C-07) | 입력 `ascii.txt`와 호출 로그는 evidence/에 없다(기록만) |

## 옵션별 관찰

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="EW-02"></a>EW-02 | 기본(`--max-section-bytes 4000`) | [실행/Stub] | I:70 | 창 본문 47,735바이트(마지막 25,703), 8,519–8,525토큰, 엔티티 12회, 링크 150회(기록만) | 없음(이 입력에 한함) |
| <a id="EW-03"></a>EW-03 | `--max-section-bytes 1000` | [실행/Stub] | I:71, I:79 | 49,571바이트(마지막 5,507), 8,827–8,837토큰, 엔티티 12회, 링크 600회, rc=1 "the write has 1202 entries, over the 1000-entry batch limit"(기록만) **results.md 갱신:** 같은 메시지가 다른 입력에서도 나왔다([EW-11](#EW-11)) | `--dry-run` 중 이 한도가 적용되는 조건은 미확인이다. [OP-H4](../open-items.md#OP-H4) |
| <a id="EW-04"></a>EW-04 | `--max-section-bytes 20000` | [실행/Stub] | I:72 | 38,555바이트(한 창 49,571), 6,967–6,975토큰(한 창 8,835), 엔티티 14회, 링크 29회(기록만) | 없음(이 입력에 한함) |
| <a id="EW-05"></a>EW-05 | `--gleanings 1` | [실행/Stub] | I:73, I:78 | 창은 기본과 같고 링크 호출 150→300회(기록만) | 증가분이 `glean_call`([SYM-03](binary-symbols.md#SYM-03))인지 이 기록으로 입증되지 않는다 |

## 해석

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="EW-06"></a>EW-06 | 엔티티 창은 약 50KB 이내, 섹션 단위로 묶임 | [실행/Stub] | I:75 | 관찰 최대는 49,571바이트이다(기록만) | 정확한 상한 상수 미확인. 한 섹션이 상한을 넘을 때의 처리도 미확인이다. [OP-H1](../open-items.md#OP-H1) **results.md 갱신:** 관측은 모두 50,000 미만이며 상수는 여전히 미확인이다([EW-09](#EW-09), [EW-10](#EW-10)) |
| <a id="EW-07"></a>EW-07 | 창 조절과 `--max-section-bytes`의 관계 | [실행/Stub] | F:215, I:76 | findings.md: 링크 패스 상한 옵션, 기본 4000, 창 조절 옵션은 `--help`에 없음. interim.md: 섹션을 바꾸므로 창 크기에도 영향을 주나 직접 조절은 아니며, 작게 해도 49,571로 커졌다. [C-03](../contradictions.md#C-03) | `--help` 출력 원본 없음. gRPC 경로의 옵션은 미확인이다 |
| <a id="EW-08"></a>EW-08 | 언어별 토큰 차이 | [실행/Stub] | I:77, F:207 | ASCII 약 8,500, 한국어 최대 18,756 | "같은 바이트 상한"은 상수가 미확인이라 전제이다. 두 수치의 측정 범위가 같은지도 미확인이다. [C-07](../contradictions.md#C-07) |

## results.md: 상한

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="EW-09"></a>EW-09 | 99바이트 문단 3,000개 입력의 창 최대값 | [실행/Stub] | R:64, E:rea/window/run3.py | `--max-section-bytes 500`에서 49,994바이트, 기본값에서 47,519바이트(기록만). 스크립트는 있고 입력 `small.txt`와 출력은 없다 | 없음(이 입력에 한함) |
| <a id="EW-10"></a>EW-10 | 상한이 정확히 50,000이라는 추정 | [미입증] | R:66 | 관측은 모두 50,000 미만이다. `objdump` 즉치값에서 0xc350과 0xc34f를 찾지 못했다고 기록됐다(기록만). evidence/의 디컴파일 파일에서도 `c350`, `c34f`, `50000`은 검색되지 않았다 | 상수 미확인. results.md도 "추정"이라고 쓴다. 창을 만드는 함수 자체가 evidence/에 식별돼 있지 않다 |
| <a id="EW-11"></a>EW-11 | `--max-section-bytes 500`의 rc=1 | [실행/Stub] | R:68, [EW-03](#EW-03) | "the write has 1202 entries, over the 1000-entry batch limit"(기록만). I:79와 입력·옵션이 다른데 수치가 같다 | 수치가 같은 이유는 미확인이다. `--dry-run` 의미는 [OP-H4](../open-items.md#OP-H4) |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
