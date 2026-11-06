# 문서만 입력한 경우

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

관련: [뼈대](ontology-skeleton-source.md), [Auto-Ontology](../products/auto-ontology.md), [Helix](../products/helix-foundry.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-02](../contradictions.md#C-02) (대체 및 원인 불일치) 초안 완주 여부와 이전 실패 원인
- [C-08](../contradictions.md#C-08) (표현 범위) Auto-Ontology "문서만으로 불가"
- [C-10](../contradictions.md#C-10) (논문과 코드 불일치) RAGFlow: 저장 규칙, exact, 온톨로지 템플릿

## 문서만

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="DO-01"></a>DO-01 | Auto-Ontology: 불가 | [실행/Stub] | F:198, [AO-D1](../products/auto-ontology.md#AO-D1), [AO-D2](../products/auto-ontology.md#AO-D2), [AO-D6](../products/auto-ontology.md#AO-D6) | 문서를 테이블에 넣으면 컬럼 수준 Term만 나왔다. [C-08](../contradictions.md#C-08) | 없음(이 입력에 한함) |
| <a id="DO-02"></a>DO-02 | Helix: 추출 가능 | [실행/Stub] | F:198, [HX-16](../products/helix-foundry.md#HX-16) | 그래프에 썼다 | 모델 품질 미측정. [HX-15](../products/helix-foundry.md#HX-15) |
| <a id="DO-03"></a>DO-03 | Helix: 초안 | [실행/Stub] | F:198, [SK-02](ontology-skeleton-source.md#SK-02) | findings.md의 "진입까지 확인"은 interim.md에서 Stub 스크립트 완주로 세분됐다. [C-02](../contradictions.md#C-02) **results.md 갱신:** 승인과 추출까지 Stub 경로로 이어졌다([HA-13](human-approval.md#HA-13)) | 모델이 초안을 만들 수 있는지 미측정이다 |
| <a id="DO-04"></a>DO-04 | RAGFlow: claim 생성 가능, 온톨로지 템플릿 미확인 | [코드] | F:198, [RF-01](../products/paper-ragflow.md#RF-01), [RF-03](../products/paper-ragflow.md#RF-03) | 프롬프트와 검증기 코드가 있다. 검증기 함수만 복사 실행했다 | claim 생성 파이프라인을 실행한 기록이 없다 |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
