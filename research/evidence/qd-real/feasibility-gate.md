# 최초 획득 전 실행 gate

**판정: 진행 — 계획에 허용된 diagnostic one-shot에 한정한다. R1·R2는 해소되었으며, 이번 확인에서 추가 실행 차단 결함을 찾지 못했다.** 첫 요청 전에 부모가 최종 코드·의존성·자료·scorer 잠금을 완료해야 한다. 임계값·표본·자료 규칙·호출 cap 변경은 없다.

허용된 `scientific.py`, `acquire.py`, `execution-fix-report.md`, `execution-fix-stub.json`만 추가로 읽었다. 대상 원문·gold·모델 출력은 읽지 않았고 코드를 실행하지 않았다. JSON에서 기존 25개와 경계 7개 검사 모두 `passed: true`임을 직접 확인했다. 보고된 실모델 호출·Docker 호출·대상 읽기는 모두 0이다.

1. **R1 해소.** acquire가 원래의 절대 global deadline을 Driver에 전달한다. `remaining()`은 현재 monotonic을 한 번 읽고 arm 만료와 global 만료까지의 시간 중 작은 값을 반환하며, 0 이하에서 요청을 차단한다. 생성 지연으로 global deadline이 지난 Stub은 dispatch 0건이다. 기본 arm 900초·24회·64,000 tokens와 전체 1,800초는 유지된다.

2. **R2 해소.** 획득 및 결과/manifest/summary 쓰기를 감싼 바깥 `finally`가 정확히 `ollama-t`에 stop을 시도한다. subprocess timeout 20초, 종료 코드·timeout·시작 실패가 명시되며 cleanup 실패는 비정상 종료다. 획득 timeout과 저장 실패가 함께 발생한 경우, 정상 획득 후 저장 실패, 정상 완료를 포함한 경계 Stub에서 stop 시도 1회를 확인했다. 부모의 로그 수집과 최종 컨테이너 제거는 그대로 필요하다.

**과학 판정은 이미 INCONCLUSIVE다.** 부모가 전달한 최종 material 상태는 12 units/7 eligible/5 deferred/gold 85/4 cells이며 독립 gold review는 unresolved 6, complete=false다. 이 숫자와 gold 내용은 본 심사자가 독립 검증하지 않았다. gold 불완전은 이후 모델 통제 통과나 수치 임계값 충족으로 복구되지 않는다. Hq-Fact·Hq-original·Honto의 성공/실패를 과학적으로 판정하거나 coverage·Fact 단독·온톨로지 개선을 입증했다고 쓰지 않는다. 결과는 호출/시간/회계/통제·추출 행동의 진단 기록으로 남긴다. 누락 gold를 모델 출력으로 보충하거나 대상을 재실행하여 원 one-shot을 교체하지 않는다.

최종 잠금은 이번 Stub이 기록한 scientific 해시 `7c1413b2dd041e1f03b54d3632386db6e6976e2b1eab7c706ced9b47e4ba7f59`, acquire 해시 `2f7eec0c3c5a3b6f50b3eb47d53530029d004cdffa2ec6b3f304962d7221b2d6`와 현재 파일의 일치를 부모가 확인한다. scorer는 이번 범위에서 재심사하지 않았으며, 그 잠금과 INCONCLUSIVE 강제 처리는 부모 gate의 책임으로 남는다.
