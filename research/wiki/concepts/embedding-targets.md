# 임베딩 대상

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

관련: [Auto-Ontology](../products/auto-ontology.md), [논문/RAGFlow](../products/paper-ragflow.md).

## 임베딩 대상

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="EM-01"></a>EM-01 | Auto-Ontology: 구조 노드 텍스트 | [코드] | F:192, AO:auto_ontology/semantic/embed.py:215,247, [AO-K4](../products/auto-ontology.md#AO-K4) | `Term: ...`, `ColumnAttribute: ...` 문자열 형식. K4에서 벡터 16→0 | 벡터 검색 품질은 측정되지 않았다. 임베딩은 해시 BoW Stub이다(E:ao/stub_llm.py) |
| <a id="EM-02"></a>EM-02 | Helix: 이 범위에서 미확인 | [미입증] | F:192 | findings.md가 미확인으로 기록했다 | 직접 근거 없음 |
| <a id="EM-03"></a>EM-03 | RAGFlow: claim 벡터 경로 | [코드] | F:192, RF:internal/agentic_rag/compiled_evidence.go:497-521 | `claimQueryVector`, `q_%d_vec` 컬럼 지정 | 실행 관찰 없음 |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
