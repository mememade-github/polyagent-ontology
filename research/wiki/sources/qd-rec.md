# 소스: QD-Rec 코드와 관련 논문

수집일: 2026-11-06. [제품 홈](../products/qd-rec.md)에 `QD-*` 요소 행을 둔다. 논문은 선택 독해이며 전문 독해·재현을 주장하지 않는다. 논문 전문은 휘발성 스크래치패드에만 두었다.

## 버전과 인용 규약

- 저장소: [SakanaAI/QD-Rec](https://github.com/SakanaAI/QD-Rec), 커밋 [`3a04ed170583e14ca08e689e8bff8fddf267dc8e`](https://github.com/SakanaAI/QD-Rec/tree/3a04ed170583e14ca08e689e8bff8fddf267dc8e).
- 클론: `__SCRATCH__/upstream/QD-Rec`. depth 1·부분 클론, `assets/` 제외 sparse checkout. 코드와 작은 예제 CSV는 포함, 별도 데이터·모델·의존성 설치 없음.
- `QD:경로:n`은 위 커밋 파일의 행 번호이다. 이 페이지와 제품 페이지에서만 쓰는 접두이며 기존 SCHEMA 접두의 뜻은 바꾸지 않는다.
- `QDP:n`, `CAP:n`은 각각 `__SCRATCH__/paper/qd-rec/2610.23470v2.txt`, `2610.40589v1.txt`의 행 번호. 공식 HTML의 절·표 링크를 함께 사용한다.
- 제품 실행 없음. `[실행]`은 Git 상태·파일 해시·HTTP 상태 수집에만 해당한다. 코드 동작은 `[코드]`, 논문 수치는 `[논문]`으로 기록한다.
- PDF 다운로드는 성공했으나 `pdftotext` 부재로 읽지 못했다. HTML을 Python 3 표준 HTMLParser로 텍스트화했다. 수식의 표현·주석 중복이 있으므로 수학 내용은 공식 HTML과 대조한다. `python` 명령 부재 후 `python3`를 사용했다.

## 보존한 수집 산출물

| 파일 | 바이트 | SHA256 |
|---|---:|---|
| [paper-access.json](../../evidence/qd-rec/paper-access.json) | 2503 | `d148c286f97534421dba205281264317cc9b093fb4a7c92d622a1563da5be917` |
| [repository-snapshot.json](../../evidence/qd-rec/repository-snapshot.json) | 5580 | `ce050c4d84371290df648e48b575a7b8c71769105ced168b6de756d6ccf23ae7` |

## 휘발성 원문의 해시

| 원문 / 파생 텍스트 | 읽은 범위·상태 | 바이트 | SHA256 |
|---|---|---:|---|
| [2610.23470v2.html](https://arxiv.org/html/2610.23470v2) | 선택 독해, HTTP HEAD 200 | 1946797 | `dc5028e0384400a4f1d6fe2184d6a6f213a8f76168bed688d0d8cc444979e625` |
| [2610.40589v1.html](https://arxiv.org/html/2610.40589v1) | 선택 독해, HTTP HEAD 200 | 148343 | `24fac1ee7f3811a9ea4831b000660b620201d73567d1b4a05215af5dd5063bd0` |
| [2610.23470v2.pdf](https://arxiv.org/pdf/2610.23470v2) | 미독해, HTTP HEAD 200 | 4691252 | `b5657f44ea0751b556700bc83fbc7354246457510b055ee6e0866d0e836796cb` |
| `2610.23470v2.txt` | HTML 파생 텍스트; QDP/CAP 행 인용 | 113772 | `f722d190241c3c50d6c036caab7e68f93cb2d04d574fb931f8ef507734c5e247` |
| `2610.40589v1.txt` | HTML 파생 텍스트; QDP/CAP 행 인용 | 61032 | `ce04c503aa0bf005c9d7331aa0dba6cb5c33d3dccab6a1e94f296e9240cf42df` |

QD 논문은 [2610.23470v2](https://arxiv.org/html/2610.23470v2), 실험 agent 비교 대상은 [2610.40589v1](https://arxiv.org/html/2610.40589v1)이다. 서로 다른 논문이며 결합 실험을 확인한 것은 아니다. 상세 독해 범위는 `paper-access.json`에 기록했다.

## 코드 인용 파일 해시

README는 문서 진술, `uv.lock`은 버전 원장 보존이다. 그 밖의 파일은 제품 페이지가 인용하는 함수·설정 중심으로 읽었으며 전수 검수를 뜻하지 않는다.

| 파일 | 바이트 | SHA256 |
|---|---:|---|
| [README.md](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/README.md) | 6494 | `daee2542a5d67246d202288654b411759400648b5ac60d45dd56308a30238025` |
| [LICENSE](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/LICENSE) | 11340 | `9ca36914e28c7be5ba427a67ddccbe60bd5c0129b5f23a28ed4bb7eadb9edbf9` |
| [pyproject.toml](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/pyproject.toml) | 421 | `ef7de5597c4fd2422af988d52d3c9ec5b1fc676e8c28934704319786e6943e29` |
| [uv.lock](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/uv.lock) | 496591 | `3d48dc8fd257126e4ec3cb51b9529e90709bc6491e19f764cd3db58b68630808` |
| [shared/qd_loop.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/shared/qd_loop.py) | 11658 | `a6d232117cc81abaac6e2e795e8231bdab506c8881da1fac491f3a858ec0684a` |
| [shared/bandit.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/shared/bandit.py) | 4770 | `b31111a5a1140ad7e2b974caa01c35fe5e45e6a5ada8dad74bb60563efd2d5cd` |
| [shared/archive_records.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/shared/archive_records.py) | 8776 | `8979ff5e2c396e0c55ccf7cd59fe95e5059a674fa463e60f5314533cfcc95e8f` |
| [shared/archive_format.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/shared/archive_format.py) | 5852 | `a215b559667c9c63b8e7b2b33ddd0af689d4a1aac086a5f41626cd6aabeb83f7` |
| [shared/batch_dedup.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/shared/batch_dedup.py) | 1980 | `d6ce79ab7eb7cc44dd1f3498c686e4615d2d3742f6ecd9d783b8311cf0d9e5ed` |
| [shared/embeddings.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/shared/embeddings.py) | 2501 | `9d8d3ba28c3ec984f79a6bd42dbe2ba66bcf338ccf614fc057791f76d691b847` |
| [shared/evaluation_budget.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/shared/evaluation_budget.py) | 958 | `def6ba0efa8b30d9dfb3a96948aff8d33d56ec7540ab66b2cd644e715017bd17` |
| [shared/llm.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/shared/llm.py) | 9666 | `ee02b16fe2dda5cf50880d7ab40566d9c3e736aeff1c2cc835de5c4e5f0e5f39` |
| [shared/lineage.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/shared/lineage.py) | 2725 | `1c3742c55a57498ea4f91f12555bfdc1f1eff3c4480feb84646892460f52f4b0` |
| [shared/view_archive.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/shared/view_archive.py) | 7639 | `a0d4eb14099e9408638bfb9404845ccfdc6a762d2474d7a7e128671edfac128e` |
| [apps/papers/config.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/papers/config.py) | 1755 | `c0c24a754db8c93ad0690c3e0e997ebd0da0087b0291dc303d4de08e7ca1d3a2` |
| [apps/papers/items.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/papers/items.py) | 1827 | `75946209a409d6302034592aa38bd005c4b33605ffbe40b61acf4111c19ee7eb` |
| [apps/papers/proposer.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/papers/proposer.py) | 4005 | `d684fb86450ca7f043195cb929c423c9a8674829ea9ea315f4538fb9f8096dba` |
| [apps/papers/evaluation.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/papers/evaluation.py) | 5208 | `09ee95121d7fd9e93074901c96f418d7b5447c598a4fa75eaba11e467785fd73` |
| [apps/papers/qd_rec.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/papers/qd_rec.py) | 3662 | `56cd43c6f25bfda360409e4b5ff39f8bd4a9c6af27c0e88e808f9b6273ad589a` |
| [apps/papers/prompts.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/papers/prompts.py) | 7072 | `0bee3b75ad9ca2a4703f83362634f2115a754a227328d73053558b4583699f7d` |
| [apps/papers/seed.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/papers/seed.py) | 5752 | `50080a6b5b2ea8e12fd6201233143cfbec78f407cbc812443ad8f4372b488179` |
| [apps/papers/create_embeddings.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/papers/create_embeddings.py) | 3816 | `445be1d40368dd6fe7ce7a6e167b2389b57e11389fc6913bc988356fa75c0bb5` |
| [apps/papers/download_corpus.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/papers/download_corpus.py) | 4756 | `ba71e9a56446726402931c4e1a876b1781660376d74ba271fbe24162eb89887f` |
| [apps/books/items.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/books/items.py) | 2464 | `bf622385db048ff7103f23ecf0853c176fe2e947262b903a6b6c3ad289495816` |
| [apps/books/qd_rec.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/books/qd_rec.py) | 2956 | `c96c6c2da7ad7c54a7141985737aa6aff8efa03704205a331bfd8b8b05819bd0` |
| [apps/books/evaluation.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/books/evaluation.py) | 3235 | `854bcd3c08394e02cb92b584ad3ca4d958d48275dd1e4d4326e1fdf491356c17` |
| [apps/books/download.sh](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/books/download.sh) | 1358 | `abb9127f6d3345e1dabc308ad1173f35015018b926afd0c91d9331bc57847010` |
| [apps/customers/config.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/customers/config.py) | 2321 | `b639194561a0d8c2b0d435f07376f2f3a62b13c444017f1c05ee33b6a9b42acd` |
| [apps/customers/items.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/customers/items.py) | 3581 | `b677debf80edc2ba9269d3413580c7838034084f4792bd498729700302846252` |
| [apps/customers/download_personas.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/customers/download_personas.py) | 3745 | `5c26bd0c9a3be36b75c4b4391d4d7257ef8db2fa38771e1507548b49a40caacd` |
| [apps/companies/items.py](https://github.com/SakanaAI/QD-Rec/blob/3a04ed170583e14ca08e689e8bff8fddf267dc8e/apps/companies/items.py) | 3818 | `4189a6009e0c2db3041f81ee78e7fbc9679e1043415c5f7a1faf35bdece2b87d` |

---
[index](../index.md) · [QD-Rec](../products/qd-rec.md)
