# SakanaAI/QD-Rec

QD-Rec은 고정된 후보 목록에서 **항목 + 자연어 추천 이유(hypothesis)** 쌍을 탐색하는 추천 연구 코드다.
품질·다양성을 함께 고려하는 bandit이 항목을 선택하고, LLM이 기존 이유를 참고해 새 이유를 만든다.
신규성 판정과 이웃 간 경쟁으로 후보를 보존하며, 책·기업·고객·논문 도메인이 구현돼 있다.

> [SCHEMA](../SCHEMA.md)의 행 형식을 따른다. 제품 코드는 **실행하지 않았다**. `[코드]`는 정적 독해, `[논문]`은 저자 보고, `[미입증]`의 적용 제안은 **추론**이다. Git·해시 수집을 제품 실행으로 간주하지 않는다.

버전: [`3a04ed170583e14ca08e689e8bff8fddf267dc8e`](https://github.com/SakanaAI/QD-Rec/tree/3a04ed170583e14ca08e689e8bff8fddf267dc8e), 수집일 2026-11-06. `QD:파일:행`, `QDP:행`, `CAP:행`의 위치·해시는 [소스 원장](../sources/qd-rec.md)에 있다. 논문은 [QD-Rec, arXiv 2610.23470v2](https://arxiv.org/html/2610.23470v2), 비교 대상은 [실험 agent, arXiv 2610.40589v1](https://arxiv.org/html/2610.40589v1)이다.

## 입력·출력과 핵심 알고리즘

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QD-01"></a>QD-01 | 탐색 단위 | [코드] | QD:shared/qd_loop.py:45-64,75-103; QD:apps/papers/qd_rec.py:24-64 | 도메인별 항목 목록·profile·사전 임베딩·완료된 seed archive를 받아 항목과 생성한 이유를 평가한다. item_id와 평가 쌍의 entry_id를 구분한다 | 추천 이유는 검증된 과학 가설이나 온톨로지 사실을 뜻하지 않는다 |
| <a id="QD-02"></a>QD-02 | 네 도메인의 입력 | [코드] | QD:apps/papers/items.py:13-52; QD:apps/books/items.py:13-53; QD:apps/customers/items.py:14-40; QD:apps/companies/items.py:11-24 | 논문: id·제목·초록 JSONL와 연구자 profile. 책: 독자별 book_id·제목·설명·rating JSONL. 고객: uuid가 있는 persona Parquet와 제품 profile. 기업: Instrument가 있는 CSV와 인수 기업 profile. 각 도메인은 별도 임베딩 저장소를 읽는다 | 일반 문서의 타입·관계·제약을 추출하는 입력 계약은 이 경로에 없다 |
| <a id="QD-03"></a>QD-03 | JSON archive와 조회 화면 | [코드] | QD:shared/archive_format.py:106-167; QD:shared/qd_loop.py:141-177; QD:shared/view_archive.py:162-174 | archives/&lt;app&gt;/에 metadata와 entries를 기록하고 배치마다 저장한다. active/replaced/discarded를 모두 보존한다. 완료 예산을 채워야 completed_at을 설정한다. JSON을 HTML 조회 화면으로 변환하는 CLI가 있다 | 총 entries 수를 최종 추천 수로 쓰면 안 된다. active만 최종 집합이다. UI 미실행 |
| <a id="QD-04"></a>QD-04 | 두 임베딩의 역할 | [코드] | QD:apps/papers/items.py:29-46; QD:shared/qd_loop.py:79-81; QD:shared/embeddings.py:7-23,37-48 | 항목 임베딩은 제목+초록으로 bandit 선택에 사용한다. archive 임베딩은 제목+초록+추천 이유로 이웃 검색에 사용한다. 기본 모델은 openai/text-embedding-3-small, 512차원이다 | 벡터 유사도가 사실성이나 온톨로지 일관성을 입증하지 않는다 |
| <a id="QD-05"></a>QD-05 | 다양성 보너스를 더한 Thompson sampling | [코드] | QD:shared/bandit.py:27-87,101-135; QD:shared/qd_loop.py:134-138,224-226 | 선형 Bayesian posterior에서 θ를 뽑아 xᵀθ + β(1−최대 cosine 유사도)를 최대화한다. 참조 집합은 active 항목과 같은 배치에서 이미 고른 항목이다. λ=1, σ=0.1, β=1. seed로 초기화하고 폐기된 평가의 보상도 갱신에 사용한다 | 전역 최적성·탐색 효율을 재현하지 않았다 |
| <a id="QD-06"></a>QD-06 | 이유의 진화와 계보 | [코드] | QD:shared/archive_records.py:192-197; QD:apps/papers/proposer.py:56-120; QD:apps/papers/prompts.py:65-90; QD:shared/lineage.py:46-77 | active 예시를 무작위 표본화해 mutate/crossover/explore를 요청한다. 제시된 parent_entry_ids와 모델이 사용했다고 보고한 evo_parent_entry_ids를 구별한다. 잘못된 계보 표기는 정규화한다 | 연산자·부모 사용은 모델의 자기 보고이며 인과적 기여 증명이 아니다 |
| <a id="QD-07"></a>QD-07 | 신규성 우선 수용·국소 경쟁 | [코드] | QD:apps/papers/qd_rec.py:44-95; QD:apps/papers/evaluation.py:66-156 | 먼저 점수와 임베딩을 구하고 가까운 3개와의 신규성을 LLM에 묻는다. novel이면 추가한다. 아니면 가장 가까운 1개와 점수·신규 여부를 숨긴 무작위 A/B 비교를 하고 승자만 대체한다 | novel 수용에는 최소 품질 점수 문턱이 없다. LLM 판정을 사실 검증이나 실험 승인으로 해석할 수 없다 |
| <a id="QD-08"></a>QD-08 | 도서의 인간 평점 예외 | [코드] | QD:apps/books/qd_rec.py:27-75; QD:apps/books/evaluation.py:92-94 | 책은 1–5 평점을 보상·대체 기준으로 쓰고, 동점이면 기존 항목을 유지한다. 성공적으로 평가한 책은 다시 선택하지 않는다. 신규성은 여전히 LLM 판정이다 | 평점은 생성 메모의 품질을 측정하지 않는다 |
| <a id="QD-09"></a>QD-09 | 비교군 | [코드] | QD:shared/qd_loop.py:70-71,187-205,249-252 | novelty는 무작위 항목+zero-shot, novelty_evo는 무작위 항목+예시, qd_rec은 bandit+예시다. archive 수용 경로는 공유한다 | 이 코드 존재만으로 비교 실험 결과가 재현되지는 않는다 |
| <a id="QD-10"></a>QD-10 | 병렬 배치 조정 | [코드] | QD:shared/qd_loop.py:187-228; QD:shared/batch_dedup.py:31-59; QD:shared/archive_records.py:110-143,200-225 | 같은 archive snapshot으로 평가한 추가 후보끼리 cosine >0.9이면 하나를 무작위 폐기한다. 같은 entry_id 대체 충돌도 무작위 승자를 정한다. 폐기 항목은 이력에 남긴다 | 배치 조정은 최고 점수 우선 선택이 아니다. 병렬 수·순서의 품질 영향은 미측정 |
| <a id="QD-11"></a>QD-11 | 실패·예산과 저장 검증 | [코드] | QD:shared/evaluation_budget.py:6-25; QD:shared/qd_loop.py:209-235; QD:shared/archive_records.py:35-99; QD:shared/llm.py:21-46,98-118,170-184 | 평가 예산은 seed 이후 완료된 평가 수이며 폐기도 센다. 실패는 한 배치 또는 예산의 5% 중 큰 수만큼 추가 시도하고 미완료면 저장 후 예외를 낸다. 점수 범위·ID 참조·대체 상호 링크를 검사한다. API 재시도와 빈 payload 재시도는 별도다 | 평가 횟수가 API 호출·토큰·비용의 상한은 아니다. 전체 실패 경로 미실행 |
| <a id="QD-12"></a>QD-12 | 감사 가능한 범위 | [코드] | QD:apps/papers/qd_rec.py:44-95; QD:apps/papers/evaluation.py:99-107,149-154; QD:shared/archive_records.py:179-184 | 점수 판단, 추천 이유, 계보, 수용 경로와 교체·패배 ID를 보존한다. 논문 앱은 신규성·duel 응답의 reasoning을 반환받지만 new_entry에는 넣지 않는다 | 모든 판정 원문이나 문서 evidence span을 보존하는 감사 원장은 아니다. 이력 보존과 근거 검증은 별개다 |

## 의존성·자원·라이선스

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QD-13"></a>QD-13 | Python 의존성 | [코드] | QD:pyproject.toml:1-18 | Python ≥3.10. openai≥2.9.0, pandas≥2.3.3, python-dotenv≥1.2.1, datasets≥4.4.1, json-repair≥0.60.1, numpy≥2.2.6, requests≥2.33.1, httpx≥0.28.1, pyarrow≥24.0.0. uv.lock도 있다 | 설치·Python 버전별 호환성은 시험하지 않았다 |
| <a id="QD-14"></a>QD-14 | 모델·API·기본 예산 | [코드] | QD:shared/llm.py:203-249; QD:apps/papers/config.py:22-49; QD:shared/bandit.py:53-71,93-98,125-129 | OpenRouter URL과 OPENROUTER_API_KEY를 사용한다. 논문 앱 기본값은 proposer/judge 모두 openai/gpt-6-luna, reasoning high, seed 10개, 이후 1,000평가, worker 20개, 예시/이웃 각 3개, 임베딩 동시 요청 50개다. 로컬에서 NumPy 행렬 연산을 수행한다 | 최소 RAM·CPU·시간·총 비용은 미측정. 로컬 모델 서버 연결은 이 클라이언트의 기본 경로가 아니다. 논문 설정과의 차이는 [C-27](../contradictions.md#C-27) |
| <a id="QD-15"></a>QD-15 | 데이터 준비 부담 | [코드] | QD:apps/books/download.sh:13-14; QD:apps/customers/download_personas.py:23-25,40-44; QD:apps/papers/download_corpus.py:29-39; QD:README.md:74-110 | 책은 Goodreads 압축 파일 3개, 고객은 Hugging Face load_dataset(train), 논문은 Paper Copilot 목록을 가져오는 코드다. README 문서 진술: M&A 실험 데이터는 유료 LSEG이고 저장소에는 합성 기업 3개 예제만 제공한다 | 데이터 다운로드·크기·이용 조건의 개별 검증은 하지 않았다. 10,000명 표본이라는 설명이 그만큼만 내려받는다는 보장은 아니다 |
| <a id="QD-16"></a>QD-16 | 10k 미만 로컬 LLM 적합성 | [코드] | QD:apps/papers/proposer.py:56-107; QD:apps/papers/evaluation.py:49-96; QD:shared/llm.py:59-62 | 예시 초록은 2,000자, 메모는 2,500자로 자른다. 새 초록과 novelty/duel 입력은 해당 함수에서 토큰 예산을 재지 않는다. 여기서 확인한 길이 제한은 문자 기준이다 | 전체 입력이 10k 토큰 미만이라는 보장, 약한 로컬 모델에서의 품질·형식 준수는 미입증 |
| <a id="QD-17"></a>QD-17 | 라이선스 | [코드] | QD:LICENSE:2-4,190-202; QD:pyproject.toml:6; QD:README.md:76-78 | 코드의 선언은 Apache-2.0, Copyright 2026 Sakana AI다. README는 데이터별 라이선스·이용 조건을 별도로 확인하라고 한다 | 코드 라이선스를 외부 데이터·모델에 확대 적용하지 않는다 |

## 논문 보고 수치와 재현 한계

아래는 직접 실행 수치가 아니다. 원문 표의 선택 행만 기록하며 전체 조건의 우열로 일반화하지 않는다.

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QD-18"></a>QD-18 | 보고 실험 조건 | [논문] | [§5.1](https://arxiv.org/html/2610.23470v2#S5.SS1), QDP:182-184,213-225 | proposer Sonnet 5/Haiku 4.5, judge gpt-5.6-terra(도서는 인간 평점). 각 1,000평가, 5 seeds. 논문 후보 17,511개. Quality는 탐색 중 점수를 재사용하며 Diversity는 평균 cosine의 여집합, Coverage는 PCA 25×25 점유율이다 | 독립 사후 평가가 아니며 [기본 코드 설정](#QD-14)과 다르다 |
| <a id="QD-19"></a>QD-19 | 논문 추천 수치 | [논문] | [Table 2](https://arxiv.org/html/2610.23470v2#S5.T2), QDP:379-410,507 | OpenEndedness/Sonnet 5: Novelty → Novelty+Evo → QD-Rec 순으로 Quality 4.96±0.02 → 5.26±0.02 → 5.32±0.02, Diversity .469 → .479 → .501, active 578±5 → 690±8 → 730±8. ±는 5 seeds의 표준오차다 | Haiku 같은 profile의 Quality는 4.26 → 5.03 → 4.87로 순서가 다르다. 재현 안 함 |
| <a id="QD-20"></a>QD-20 | 도서 반례와 비교 조건 | [논문] | [Table 2](https://arxiv.org/html/2610.23470v2#S5.T2), [Appendix B](https://arxiv.org/html/2610.23470v2#A2), QDP:284-298,522 | picture-book/Sonnet 5의 평점: Novelty 4.19±0.01, QD-Rec 4.12±0.02; active는 297±6, 336±7. MMR/DPP 비교군은 평점 피드백을 받지 않는다 | 항상 품질이 오르거나 bandit 단독 효과를 증명한 비교라는 해석은 성립하지 않는다 |
| <a id="QD-21"></a>QD-21 | 비용 | [논문] | [§5.2 Cost](https://arxiv.org/html/2610.23470v2#S5.SS2), QDP:510-511 | 저자 추정: 실행당 약 $13–$62, QD-Rec/Novelty+Evo는 Novelty의 약 1.3배. 원 실행 토큰 로그가 없어 보존 호출 840개를 재전송해 호출별 비용을 추정했다 | 현재 가격 견적·청구 실측·이번 기본 모델 비용이 아니다 |

## 온톨로지 연구·실험 agent와의 관계

관리자 지시에 따라 위키에서 관리한다. 아래 추론은 구현 승인이나 기존 프로토타입 설계 변경을 뜻하지 않는다. 다른 세션의 `.claude/skills`는 변경하지 않는다.

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="QD-22"></a>QD-22 | 연구 문헌 선별에 직접 해당하는 구현 | [코드] | QD:apps/papers/prompts.py:24-37,65-90; [입력](#QD-02), [수용](#QD-07) | 연구자 profile과 논문 초록에서 관련 이유와 구체적인 후속 실험·ablation·확장 아이디어를 메모로 생성하도록 요청하는 앱이 있다 | 그 메모가 실행 가능한 연구 계획인지 검증하지 않았다 |
| <a id="QD-23"></a>QD-23 | 온톨로지 연구에 가져올 부분 | [미입증] | [항목 선택](#QD-05), [계보](#QD-06), [문헌 앱](#QD-22), [기존 설계](../concepts/paper-informed-design.md) | **추론:** 연구 논문·추출 방식·평가할 문서/후보 타입을 고정 목록으로 만들면, 무엇을 검토할지 선택하고 여러 해석 후보를 보존하는 외부 탐색 루프로 응용할 수 있다 | 온톨로지 추출·엔티티 해소·관계 일관성·원문 인용 검증은 별도 계약과 평가가 필요하다. 정확도 개선이나 로컬 LLM 적합성 근거 없음 |
| <a id="QD-24"></a>QD-24 | 실험 agent의 역할·독립 문맥 | [논문] | [2610.40589 §1](https://arxiv.org/html/2610.40589v1#S1), [§7.2](https://arxiv.org/html/2610.40589v1#S7.SS2), CAP:53-57,115-117 | proposer·PI·계산 연구자·실험자·manager·독립 reviewer와 별도 safety agent를 둔다. fresh proposer는 서로의 제안을 보지 않는다. 문서를 교환하고, 최종 reviewer는 새 대화에서 원고만 받는다 | 이번에는 해당 agent 코드·실험·다른 세션의 스킬 구현을 검증하지 않았다 |
| <a id="QD-25"></a>QD-25 | 실험 agent의 반복·판정 근거 | [논문] | [§2](https://arxiv.org/html/2610.40589v1#S2), [§4–5](https://arxiv.org/html/2610.40589v1#S4), CAP:59-61,82,94-96 | 약 30시간 동안 75제안을 거부했다. 반복 주제 제외 후 9제안이 새 방향 7개를 탐색했다. 정확도 기준을 충족해도 control 실패는 inconclusive로 남기고 기준을 완화하지 않았다 | QD-Rec을 사용한 결과라는 근거는 없다. 온톨로지 실험으로의 전이도 미입증 |
| <a id="QD-26"></a>QD-26 | 실험 agent에 결합할 부분과 경계 | [미입증] | [보존 이력](#QD-03), [탐색](#QD-05), [감사 한계](#QD-12), [실험 agent](#QD-24), [판정](#QD-25) | **추론:** manager 단계에 후보·거부·대체 이력과 다양성 기반 검토 순서 선택을 결합할 수 있다. 고정 pool을 무엇으로 정의할지 먼저 정해야 한다. 독립 fresh 제안과 QD의 부모 예시 기반 제안은 별도 경로로 구분해야 한다 | QD의 novel/duel 승리를 PI·독립 검증·사전 고정 수용 기준의 통과로 대체할 근거 없음. 통합·성능 개선 미실험 |
| <a id="QD-27"></a>QD-27 | 확인한 범위 | [실행] | [소스 원장](../sources/qd-rec.md), E:qd-rec/repository-snapshot.json, E:qd-rec/paper-access.json | 지정 경로의 얕은 클론·커밋·깨끗한 upstream 상태와 파일 해시, 논문 접근 상태를 수집했다. 모델 호출 0, 데이터 다운로드 0, 의존성 설치 0. 논문 HTML과 코드만 읽었다 | 추천 파이프라인·stub·실모델·품질·속도·메모리 실측은 하지 않았다 |

---
[index](../index.md) · [소스·해시](../sources/qd-rec.md) · [설정 대조 C-27](../contradictions.md#C-27)

**results.md 갱신:** 위의 미구현·미실행 진술은 QD-Rec 조사 당시 이력이다. 이후 승인된 별도 [QD 적응 초안](../concepts/qd-rec-adaptation.md)은 원본 stdlib controller와 Stub 기계 검사만 추가했다. upstream 제품·실모델 실행 및 품질 향상은 여전히 미입증이다.
