# 소스: evidence/ragflow

위치: `evidence/ragflow/`. 불변 원본이다.

RAGFlow 실험 하니스와 `compile/`의 실행 출력이다. `claims.go`의 검증기 세 함수를 복사한 실행 파일 `validator_copy.go`는 저장소 수록본에 없다. 세 함수가 업스트림과 공백 정규화 비교로 같음을 확인했다(기록만).

## 수집 시점 파일

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/ragflow/validator_copy.go` | (저장소 미포함) | - |

## 이 소스를 인용하는 요소

[RF-05](../products/paper-ragflow.md#RF-05), [QV-R1](../concepts/quote-validation.md#QV-R1), [QV-R3](../concepts/quote-validation.md#QV-R3), [ES-04](../concepts/evidence-spans.md#ES-04)

## compile/ (2026-11-06 추가)

`harness.out`, `h_structure_test.go.txt`, `h_tree_test.go.txt`, `analyzer_link_stub.c`, `upstream_tests.txt`. 클론 `2096707f`, Go 1.27.3. 하니스를 패키지에 잠시 복사해 실행한 뒤 제거했다. 빌드에 쓴 스텁 라이브러리와 cl100k 테이블은 스크래치패드에만 있다. [XT-14](../extraction-techniques.md#XT-14)~[XT-23](../extraction-techniques.md#XT-23)


`rf_fault.out`, `h_fault_*_test.go.txt`: 오류 주입 하니스와 출력(2026-11-06 추가). `rf_use.out`, `h_use_test.go.txt`: `agentic_rag` 시험 시도로, **`office_oxide.h` 부재로 빌드 실패**하여 결과가 아니다.


## 추가 수집 파일 (2026-11-06 등록 전 점검)

| 파일 | 바이트 | sha256 앞 16자 |
|---|---:|---|
| `evidence/ragflow/compile/analyzer_link_stub.c` | 1,789 | `4ccfac29ef708bbc` |
| `evidence/ragflow/compile/h_fault_structure_test.go.txt` | 6,425 | `6d9c4d32b4f8f9d9` |
| `evidence/ragflow/compile/h_fault_tree_test.go.txt` | 3,392 | `ec713cf58afd9918` |
| `evidence/ragflow/compile/h_structure_test.go.txt` | 5,197 | `c91ff106a3e4be68` |
| `evidence/ragflow/compile/h_tree_test.go.txt` | 2,013 | `06e81ed0c4feef0d` |
| `evidence/ragflow/compile/h_use_test.go.txt` | 1,435 | `2cb90930529ec97d` |
| `evidence/ragflow/compile/harness.out` | 3,594 | `64efe99c37a13d14` |
| `evidence/ragflow/compile/rf_fault.out` | 4,303 | `24d14f2161f4a5f7` |
| `evidence/ragflow/compile/rf_use.out` | 662 | `41f80bfda96ee85e` |
| `evidence/ragflow/compile/upstream_tests.txt` | 502 | `45247724f2ed147b` |

---
[index](../index.md) · [coverage](../coverage.md)
