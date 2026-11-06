# 판정과 2차 검증

> 등급과 인용 표기는 [SCHEMA](../SCHEMA.md). `[실행/Stub]`은 코드 동작의 증거이고 모델 품질의 증거가 아니다. "기록만"은 원시 출력이 evidence/에 없고 findings.md 또는 interim.md의 서술만 있다는 뜻이다.

확률은 모두 Stub이 준 값이다. 코드의 분기를 보여 줄 뿐 모델의 판정 능력을 보여 주지 않는다. adjudicate 응답의 수용 조건은 미확인이다([SV-15](#SV-15)). 관련: [인용 대조](quote-validation.md), [출력 제약](output-constraints.md).

## 소스 간 변경과 불일치

한쪽을 조용히 고르지 않는다. 내용은 [대조 기록](../contradictions.md)에 있다.

- [C-01](../contradictions.md#C-01) (세분) Helix 인용 대조 범위
- [C-04](../contradictions.md#C-04) (추가) 추출 패스 구성

## Helix 판정

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SV-01"></a>SV-01 | 실제 인용, 0.95 | [실행/Stub] | F:131, E:helix/report3.raw | accept, `confidence: 0.95` | 확률은 Stub 값이다. 모델의 보정 여부와 무관하다 |
| <a id="SV-02"></a>SV-02 | 실제 인용, 0.7 | [실행/Stub] | F:132, E:helix/report3.raw | review, `low_confidence` | 확률은 Stub 값이다 |
| <a id="SV-03"></a>SV-03 | 실제 인용, 0.2 | [실행/Stub] | F:133, E:helix/report3.raw | refuted | 확률은 Stub 값이다 |
| <a id="SV-04"></a>SV-04 | 문서에 없는 인용의 검증 모델 전달 차단 | [실행/Stub] | F:134, E:helix/report3.raw, E:rea/quote/r_ellipsis.raw | reject 항목에 `confidence`가 없다. 인용 변형 실험의 reject에는 `judgements` 호출 자체가 없다. [QV-15](quote-validation.md#QV-15) | 인용 판정 메커니즘 자체는 [QV-P1](quote-validation.md#QV-P1) |
| <a id="SV-05"></a>SV-05 | 도메인 위반(Contact → promised_to) 차단 | [실행/Stub] | F:135, E:helix/report3.raw, E:helix/ontology_nokey.toml | reject `domain_range_mismatch`, `confidence` 없음. 온톨로지가 `promised_to`의 `from`을 Commitment로 둔다 | 캡처 로그가 없어 검증 프롬프트 제외를 직접 보여 주는 raw는 없다(기록만) |

## 시스템별 2차 검증

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SV-06"></a>SV-06 | Auto-Ontology: SQL 의도 검증 | [코드] | F:196, AO:auto_ontology/retrieval/text_to_sql/agents/sql_parse_validation.py:788, AO:auto_ontology/retrieval/text_to_sql/text_to_sql_graph.py:90 | "before checking its intent with the LLM" | findings.md §4 행에 등급과 인용이 없어 이 위키가 코드 위치를 찾아 붙였다. 의도 검증의 효과 실험은 기록되지 않았다 |
| <a id="SV-07"></a>SV-07 | Helix: 사실별 확률 | [실행/Stub] | F:196, E:helix/stub2.py | 스키마의 `judgements.items.properties.claim.enum`에서 ID를 읽어 확률을 돌려준다 | 실제 모델의 판정 품질은 측정되지 않았다(F:218) |
| <a id="SV-08"></a>SV-08 | RAGFlow: 충분성 게이트 | [코드] | F:196, RF:internal/agentic_rag/compiled_evidence.go:936, RF:internal/agentic_rag/decision_judge.go:98, P:§4.1 Listing 1 (p.txt:432) | `compiledEvidenceGate`, `defaultDecisionModel = "decision-model-preview"`가 있다 | 함수 이름과 상수 수준이다. 내부를 읽거나 실행하지 않았다. 논문의 `qwen-decision-model-preview`와 같은 모델인지 미확인이다 |

## 심볼 수준

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SV-09"></a>SV-09 | `adjudicate_call`의 실제 호출 | ~~[미입증]~~ → [실행/Stub] ([SV-13](#SV-13)) | I:85, I:17 | ~~실행 전이다.~~ → `calls`의 `adjudicate`로 호출이 관찰됐다([SV-13](#SV-13)). 이 호출이 `prompt::adjudicate_call`인지는 이름 수준의 대응이다. [SYM-04](binary-symbols.md#SYM-04) | ~~호출 조건과 역할 모두 미입증이다~~ → 호출은 관찰됐다. 호출 조건과 응답 수용 조건은 **미확인**이다([SV-15](#SV-15)) |

## results.md: 엔티티 해소

| ID | 요소 | 등급 | 인용 | 관찰 | 미입증 |
|---|---|---|---|---|---|
| <a id="SV-10"></a>SV-10 | `ingest-mapped`로 `Account{A-100, Globex}` 적재, `sources` 형식 | [실행/Stub] | R:72, E:rea/adjudicate/src.json, E:rea/adjudicate/try.sh | `src.json` 형식이 R:72와 일치한다 | ~~`rows.jsonl`, `mappings.toml`, 적재 출력이 evidence/에 없다~~ → `rows.jsonl`은 있다. `mappings.toml`은 저장소 수록본에 없고, 적재 출력은 보존되지 않았다(기록만) |
| <a id="SV-11"></a>SV-11 | 문서 엔티티 `Globex`(이름 일치) | [실행/Stub] | R:76, E:rea/adjudicate/r_exact_name.json | adjudicate 호출 없음, resolved, by `name`, key `sA-100`, 판정 accept | 이름 일치 규칙의 내용은 읽히지 않았다 |
| <a id="SV-12"></a>SV-12 | 문서 엔티티 `Initech`(무관) | [실행/Stub] | R:77, E:rea/adjudicate/r_unrelated.json | adjudicate 호출 없음, unresolved, 판정 review(`unresolved`) | 없음(이 입력에 한함) |
| <a id="SV-13"></a>SV-13 | 문서 엔티티 `Globex Inc`(부분 일치) | [실행/Stub] | R:78, E:rea/adjudicate/r_match_.89.json, E:rea/adjudicate/r_match_.90.json, E:rea/adjudicate/r_match_.95.json, E:rea/adjudicate/r_null_choice.json, E:rea/adjudicate/ex1.out | `calls`에 `adjudicate`가 있고 unresolved, 판정 review | 어떤 조건이 adjudicate 호출을 부르는지 미확인이다 |
| <a id="SV-14"></a>SV-14 | 문서 엔티티 `Globex renewal`(부분 일치) | [실행/Stub] | R:79, E:rea/adjudicate/t3.py | adjudicate 호출, unresolved(기록만). 스크립트만 있고 출력이 없다 | 원시 출력 없음 |
| <a id="SV-15"></a>SV-15 | adjudicate 응답을 수용시키는 조건 | [미입증] | R:81, E:rea/adjudicate/stub_adj.py, E:rea/adjudicate/t.py, E:rea/adjudicate/t2.py | raw 4건(0.89, 0.90, 0.95, choice null)은 모두 unresolved이다. 1.0과 배열 형식은 t2.py만 있고 출력이 없다(기록만). Stub 응답 형식 `{"value":[...]}`을 스키마와 대조할 캡처 `a.log.adj`가 evidence/에 없다 | **미확인.** 응답 형식 문제인지 다른 조건인지 구분되지 않았다. 추론으로 메우지 않는다 |
| <a id="SV-16"></a>SV-16 | `adj_choices.c` | [디컴파일] | R:81, E:rea/decompiled/extract/adj_choices.c:43-44 | 점프 테이블 복원 경고가 있고, results.md는 판단 근거로 쓰지 못했다고 기록한다 | 이 파일로 수용 조건을 읽을 수 없다. `adj_bounded.c`는 results.md가 해석하지 않았고 이 위키도 해석하지 않았다 |

---
[index](../index.md) · [coverage](../coverage.md) · [open items](../open-items.md)
