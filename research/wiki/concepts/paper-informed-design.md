# 논문 근거를 연결한 새 접근

[index](../index.md) · [논문 원장](../sources/papers-20261106.md) · [as-is 실행](logical-structuring.md)

사용자 승인 이후 설계 선택이다. 기존 as-is 관찰과 구분한다. 여러 기법을 작은 컨텍스트에서 결합하는 새 통합이며, 입증된 연구 신규성이나 성능 개선이 아니다. 아래는 설계 근거이며, 실제 구현·실측의 한계는 [결과](prototype-results.md)에 구분해 기록한다.

| ID | 요소 | 등급 | 인용 | 관찰·선택 | 미입증·한계 |
|---|---|---|---|---|---|
| <a id="PD-01"></a>PD-01 | 작은 문장·질문 단위 추출 | [설계] | [PR-01](../sources/papers-20261106.md#PR-01), [LS-11](logical-structuring.md#LS-11), [LS-16](logical-structuring.md#LS-16) | 원문 전체를 반복 투입하지 않고 입력 상한·실제 토큰·잘림을 기록 | 문맥 분할로 관계가 누락될 수 있고 3B 품질 미입증 |
| <a id="PD-02"></a>PD-02 | DB 뼈대와 문서 사실 분리 | [설계] | [PR-08](../sources/papers-20261106.md#PR-08), [LS-15](logical-structuring.md#LS-15) | 선언 FK는 보존하고 문서는 근거 있는 사실에서 개념 후보로 집계 | OWL·외부 온톨로지 RAG가 아니며 문서 관계 품질 미입증 |
| <a id="PD-03"></a>PD-03 | 표면 정규화와 암시적 DB 연결 | [설계] | [PR-02](../sources/papers-20261106.md#PR-02), [PR-04](../sources/papers-20261106.md#PR-04) | 표면형 묶기와 값 중복 휴리스틱을 명시적 출처와 함께 적용하는 선택 | 동명이인·우연 중복·세분성 오류, 학습 기반 의미 해소 미구현 |
| <a id="PD-04"></a>PD-04 | 사실→개념 집계 | [설계] | [PR-03](../sources/papers-20261106.md#PR-03) | 근거 위치가 있는 사실과 타입·관계 후보를 분리 | 집계 빈도는 진실성·계층 정확도가 아니다 |
| <a id="PD-05"></a>PD-05 | 형식 검증과 의미 평가 분리 | [설계] | [PR-10](../sources/papers-20261106.md#PR-10), [PR-13](../sources/papers-20261106.md#PR-13) | JSON 준수 외에 행위자·부정·양태·대상 전체 명제를 점검 | OWL/SHACL 검증이나 일반 의미 보증이 아니다 |
| <a id="PD-06"></a>PD-06 | 동결 독립 평가 | [설계] | [PR-05](../sources/papers-20261106.md#PR-05), [PR-09](../sources/papers-20261106.md#PR-09) | STRICT 의미 링크와 ENDPOINT 투영을 분리하고 두 uncached 실행을 비교 | Acme는 이미 본 개발 자료, 작은 표본은 일반 성능이 아니다 |
| <a id="PD-07"></a>PD-07 | 역할·규모 근거의 제한 | [설계] | [PR-06](../sources/papers-20261106.md#PR-06), [PR-07](../sources/papers-20261106.md#PR-07), [PR-11](../sources/papers-20261106.md#PR-11), [PR-12](../sources/papers-20261106.md#PR-12) | 큰 모델·사전 스키마·불충분한 재현 보고의 효과를 우리 결과로 옮기지 않는다 | 저성능 3B 성공, 다중 에이전트 개선, 연구 신규성은 미입증 |

## 평가와 공개 상태

**results.md 갱신:** 앞선 결과 대기 상태는 [실측 결과](prototype-results.md)로 대체한다. 작은 독립 질문은 문맥 부담을 줄이고, DB 구조와 문서 사실을 분리하면 구조적 출처를 보존할 수 있어 선택했다. 그러나 실행 결과는 문서 의미 유도가 빈약한 혼합 소스 스키마 초안이며, 완성된 온톨로지나 일반적 우월성의 증거가 아니다. 문장 간 문맥 추론도 구현하지 않았다.

[동결 규약](../../evidence/prototype/protocol.md)은 변경하지 않는다. STRICT 열 이름의 사전 가정 오류와 사후 재채점 금지는 [결과](prototype-results.md)에 명시한다. 코드 결정 비율은 추론 노력 비율이 아니다. 논문 효과의 재현·연구 신규성은 주장하지 않는다.

~~공개본에는 원문 입력·gold·fact/output dump·캐시를 넣지 않는다~~ → 기존 `evidence/real-model/gold.md`와 `gold.txt`는 이미 공개된 합성 회귀 fixture로 유지한다. 새 원문 입력·raw 모델 출력·fact/output dump·캐시는 공개하지 않고 코드와 선별 측정 메타데이터만 싣는다. PDF 3건은 미사용이며 JSONL은 live NoSQL connector가 아니다. 중첩 배열은 보존만 하고 정규화하지 않는다. 자유 형식 로그는 의미 파싱하지 않으며 폴더 경로는 분류 문맥일 뿐 폴더 온톨로지·계층이 아니다. OWL·SHACL·규칙은 없다.
