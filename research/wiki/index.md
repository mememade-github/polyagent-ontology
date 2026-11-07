# Index

세 참조 시스템의 as-is와 사용자 승인 이후 새 접근을 구분한 위키이다. 모든 `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. 규약은 [SCHEMA](SCHEMA.md), 이력은 [log](log.md).

## 시작 지점

- [coverage](coverage.md): 원문 행과 요소의 대응
- [open-items](open-items.md): 미해결과 미입증
- [contradictions](contradictions.md): 소스 간 변경과 불일치
- [comparison](comparison.md): findings.md §4의 칸별 현황 (27행)
- [extraction-techniques](extraction-techniques.md): 지식 추출 기법별 비교와 구현 범위 (23행)
- [knowledge-lifecycle](knowledge-lifecycle.md): 추출·저장·사용, 품질 보장 범위, 오류 동작, 실제 모델 관찰
- [method-and-limits](method-and-limits.md): 방법, 버전, 한계 (27행)

## 제품

- [NVIDIA/auto-ontology](products/auto-ontology.md): DB 카탈로그 기반 compile과 text-to-SQL, knockout, 문서 입력 (42행)
- [HelixDB/helix-foundry와 ontology-agent 이미지](products/helix-foundry.md): Go 오케스트레이션과 이미지 바이너리, 판정 주입 실험 (17행)
- [arXiv 2610.41172와 RAGFlow](products/paper-ragflow.md): 논문 진술, RAGFlow 코드 대조 (16행)
- [SakanaAI/QD-Rec](products/qd-rec.md): 품질·다양성 추천 코드, 논문 수치, 온톨로지·실험 agent 적용 추론과 한계 (27행; 제품 미실행)

## 개념

- [논리 구조화](concepts/logical-structuring.md): 시스템별 논리 구조와 결정 주체, 실제 모델의 뼈대 생성 (12행)
- [인용 대조 (quote validation)](concepts/quote-validation.md): Helix 변형 관찰, `locate_quote` 디컴파일 해석(정규화 내용 미입증), RAGFlow 복사 실행 (33행)
- [엔티티 창 (entity windows)](concepts/entity-windows.md): 옵션별 창 크기와 호출 수 (11행)
- [근거 위치 (evidence spans)](concepts/evidence-spans.md): 시스템별 근거 위치 (5행)
- [온톨로지 뼈대의 출처](concepts/ontology-skeleton-source.md): 뼈대 출처와 초안 경로 완주 (10행)
- [사람 승인](concepts/human-approval.md): 인증 플래그, review, 바이너리 직접 승인 실행(사람·Foundry 경로 미입증) (13행)
- [판정과 2차 검증](concepts/second-verifier.md): 판정 분기, 2차 모델, 엔티티 해소와 adjudicate(수용 조건 미확인) (16행)
- [LLM 출력 제약](concepts/output-constraints.md): 허용 목록, enum, 도메인, JSON (5행)
- [임베딩 대상](concepts/embedding-targets.md): 구조 노드, claim 벡터 (3행)
- [문서만 입력한 경우](concepts/document-only-input.md): 문서만 넣었을 때 시스템별 (4행)
- [컨텍스트 크기와 토큰 측정](concepts/context-budget.md): 호출별 토큰, 프로바이더, context_tokens (21행)
- [바이너리 심볼과 문자열](concepts/binary-symbols.md): 이름 수준 근거, 해석되지 않은 디컴파일 파일 (20행)

## 소스

- [소스: findings.md](sources/findings.md)
- [소스: interim.md](sources/interim.md)
- [소스: evidence/ao](sources/evidence-ao.md)
- [소스: evidence/helix](sources/evidence-helix.md)
- [소스: evidence/ragflow](sources/evidence-ragflow.md)
- [소스: evidence/rea (interim.md 제외)](sources/evidence-rea.md)
- [소스: results.md](sources/results.md)
- [소스: evidence/real-model](sources/evidence-real-model.md)
- [소스: evidence/skeleton](sources/evidence-skeleton.md)
- [소스: 업스트림 클론과 논문 텍스트](sources/upstream-and-paper.md)
- [소스: QD-Rec 코드와 관련 논문](sources/qd-rec.md): 고정 커밋, 파일·논문 해시, arXiv 2610.40589 비교 근거

## 새 접근 구축

- [논문 근거와 설계 선택](concepts/paper-informed-design.md): PD 홈 행, 선택 근거와 실측 한계
- [논문 13건 선택 독해·접근 원장](sources/papers-20261106.md): PR 홈 행, 읽은 절·URL·해시·재배포 제한
- [동결 측정 규약](../evidence/prototype/protocol.md): 두 독립 실행과 의미 평가 기준

- [프로토타입 실측 결과](concepts/prototype-results.md): 동결 점수·열 이름 가정 오류·실패·안정성
- [소스: evidence/prototype](sources/evidence-prototype.md): 공개 측정 metadata 크기·해시 원장

- [QD 적응 초안](concepts/qd-rec-adaptation.md): QDA-01~05, 제한 scheduler·provisional archive·Stub 기계 검증과 미래 반증 규칙
- [소스: QD 적응](sources/qd-rec-adaptation.md): 실행 전 lock·절차 입력 digest·코드/결과 해시

QD 적응 검토 후 정의: [적응 초안](concepts/qd-rec-adaptation.md), [검토·계산·addendum 원장](sources/qd-rec-adaptation.md). 실모델 미검증.

- [QD 실제 자료](concepts/qd-real-data.md): QDR-D 홈 행, bounded search·라이선스·자료 잠금·불완전 gold (2026-11-07)
- [QD 실제 절차](concepts/qd-real-procedure.md): QDR-P 홈 행, 역할 경계·고정 비교·실행 전 gate와 Stub (2026-11-07)

**results.md 갱신:** 위 실모델 미검증 표시는 과거 QDA 단계 기록이다.

- [QD 실제 결과](concepts/qd-real-results.md): QDR-R 홈 행, 세 가설 INCONCLUSIVE·15 seed/arm 행·통제/gold 한계
- [소스: QD 실제 실행](sources/qd-real.md): 공개 metadata와 scientific/controller/analyzer 해시 원장
