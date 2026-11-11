# REA 시작 제한 300초의 출처 (정제 발췌)

2026-11-06 REA `decompile` 실행의 명령, 결과, 설치본 기본값에서 뽑은 발췌다. 세션 ID는 지웠고 작업 경로는 `__SCRATCH__`로 바꿨다.

출처: rea-kit 커밋 `8e739a2`의 `raw/g2-startup-300s-20261111/` (저장소 미포함)

| 원본 | sha256 앞 16자 |
|---|---|
| `command.txt` | `f817140fdbdf7cf5` |
| `result-excerpt.txt` | `0ba1debf71d6f17b` |
| `rea-install-version.txt` | `a05b5138404334e5` |

## 명령의 환경 변수 지정 (command.txt)

```
export ... REA_GHIDRA_STARTUP_TIMEOUT_MS=300000 GHIDRA_HEADLESS_MAXMEM=6G; ... time (timeout 400 $REA decompile $T --procedure=0x755d20 --provider ghidra --json > ...)
```

`$S`는 `__SCRATCH__`, `$T`는 `__SCRATCH__/agentimg/usr/local/bin/extract`다.

## 결과 (result-excerpt.txt)

```
( timeout 400 $REA decompile $T --procedure=0x755d20 --provider ghidra --json)  1182.78s user 105.47s system 387% cpu 5:32.16 total
rc=1
```

오류 JSON의 `code`는 `provider_timeout`, 문구 첫 문장:

```
Ghidra did not finish importing and analyzing the target within its configured 300000 ms startup deadline (REA_GHIDRA_STARTUP_TIMEOUT_MS).
```

## 같은 설치본의 기본값 (rea-install-version.txt)

```
node_modules/rea-agents/package.json:4:  "version": "6.8.0",
node_modules/rea-agents/dist/domain/analysisResourceLimits.js:16:export const DEFAULT_GHIDRA_STARTUP_TIMEOUT_MS = 330_000;
```

## 읽는 법

300,000ms는 REA 기본값이 아니라 호출자가 명령에서 지정한 값이다. 기본값은 330,000ms다. 바깥 `timeout 400`보다 먼저(wall 332초) REA가 rc 1로 끝났다. 기본값이나 더 긴 제한에서의 결과는 실행하지 않았다.
