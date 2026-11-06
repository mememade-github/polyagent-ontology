# research

프로젝트와 독립된 연구 공간이다. [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 패턴을 따르며 규약은 [wiki/SCHEMA.md](wiki/SCHEMA.md)이다. 시작은 [wiki/index.md](wiki/index.md).

`evidence/`의 스크립트는 기록용이다. 그대로 실행하지 않는다. 일부는 DB를 비우거나(`knockout.py`), 고정 이름 컨테이너를 강제 삭제하거나, 인증 없는 Stub 서버를 모든 인터페이스에 연다.

모델 대부분은 Stub이고 실제 모델 관찰은 소규모이다. 제품 평가나 권고가 아니다.
