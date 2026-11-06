# polyagent-ontology

> **연구 중입니다.** 결론이 확정되지 않았고 내용은 바뀔 수 있습니다.

일반 문서를 구조화해 온톨로지를 자동 구축하는 방법을 연구하는 프로젝트입니다. 컨텍스트 10k 토큰 미만, 추론 능력이 낮은 로컬 LLM을 대상으로 합니다. 연구 지식은 독립 공간인 [`research/`](research/README.md)에 있습니다.

## 연관 프로젝트

이 프로젝트는 아래 프로젝트의 공식 자료가 아닙니다. 각 자료의 권리는 해당 권리자에게 있습니다.

| 프로젝트 | 관계 |
|---|---|
| [mememade-github/polyagent-devcontainer](https://github.com/mememade-github/polyagent-devcontainer) | 이 저장소의 기반 템플릿 |
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | 연구 대상 |
| [HelixDB/helix-foundry](https://github.com/HelixDB/helix-foundry), `ghcr.io/helixdb/ontology-agent` | 연구 대상 |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow), arXiv 2610.41172 | 연구 대상 |
| [morluto/rea](https://github.com/morluto/rea) | 분석 도구 |
| [Karpathy, LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | `research/`의 지식 패턴. 스킬 `.claude/skills/llm-wiki`의 원문 |
| [Ollama](https://github.com/ollama/ollama), `qwen2.5:3b` | 소규모 실험 실행 |

## 라이선스

[MIT](LICENSE). 인용·기록된 제3자 자료는 MIT로 재허락되지 않습니다.

## DevContainer

DevContainer base for running multiple AI coding agents (Claude Code · Codex CLI · Antigravity CLI) in parity on the same project. The container is workspace-scoped, not a security sandbox — see [REFERENCE.md § Privilege boundary](REFERENCE.md#privilege-boundary) for the docker.sock / docker-group implications.

Single ground truth (`.claude/`) + per-vendor mirror (`.agents/rules`, `.agents/skills`, `.codex/`). Antigravity reuses the same mirror plus a small native layer in `.agents/` (a hook adapter that runs the Claude hooks, and a rule-folder registration). Adding a new vendor reuses the mirror pattern instead of rewriting governance.

Behavioral foundation: [Karpathy 4-rule](https://github.com/forrestchang/andrej-karpathy-skills) (Think Before Coding · Simplicity First · Surgical Changes · Goal-Driven Execution) auto-loaded for Claude (`@import` in `CLAUDE.md`); for Codex, `AGENTS.md` instructs an explicit `Read` of the rule files under `.agents/rules/` at session start; Antigravity loads them automatically through their `trigger: always_on` frontmatter.

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or Docker Engine with Compose v2 (both paths)
- [VS Code](https://code.visualstudio.com/) + [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) (path A only)

## Quick start

```bash
git clone https://github.com/mememade-github/polyagent-ontology.git my-project
cd my-project
cp .devcontainer/.env.example .devcontainer/.env
```

In `.devcontainer/.env`, `COMPOSE_PROJECT_NAME` is the project and volume prefix
(for example, `my-project`), and `CONTAINER_NAME` is the container name used by
`docker exec` below (for example, `my-project-dev`). Both identifiers are unique
per instance; the other settings are listed in [Configuration](REFERENCE.md#configuration-devcontainerenv).

**A: VS Code.** Attach does not apply `devcontainer.json`.

```bash
code .
# VS Code: Ctrl+Shift+P → "Dev Containers: Reopen in Container"
# First build ~3-5 min.
```

**B: Docker Compose.** Run from the repository root:

```bash
docker compose --env-file .devcontainer/.env -f .devcontainer/docker-compose.yml build
docker compose --env-file .devcontainer/.env -f .devcontainer/docker-compose.yml up -d
docker exec -it my-project-dev bash
```

For settings, operations, and differences between A and B, see [DevContainer lifecycle](REFERENCE.md#devcontainer-lifecycle).

### Agents and first login

Run an agent inside the container:

```bash
claude --dangerously-skip-permissions
codex exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox "<prompt>"
agy
```

On first run, `claude` prompts interactive login and Codex needs
`codex login --device-auth` once. For `agy`, sign in at the printed Google URL
and follow the terminal prompts. Gemini 4 Argon requires a paid Google AI Pro
or Ultra plan, excluding free trials. All three credentials persist in named volumes.

Codex compatibility and project trust details are covered in [Codex sandbox bypass](REFERENCE.md#codex-sandbox-bypass-devcontainer-only).

## What's included

| Component | Count | Notes |
|-----------|------:|-------|
| AI agents | 3 | Claude Code · Codex CLI · Antigravity CLI (`agy`) |
| Governance roles | 2 | evaluator, wip-manager (Claude agents; Codex skill/subprocess mirrors; Antigravity built-in `self` subagents) |
| Hooks | 4 / 4 / 4 | session-start, pre-commit-gate, pre-push-gate, refinement-gate (Antigravity runs the Claude hooks through `.agents/hooks/claude-hooks-adapter.sh`) |
| Skills | 6 | /refine, /status, /verify, karpathy-guidelines, typesafe-ai, llm-wiki |
| Tools | 20+ | ripgrep, fd, fzf, jq, tmux, gh, docker CLI, uv |

For the optional TypeSafe API key, see [REFERENCE.md §TypeSafe (optional)](REFERENCE.md#typesafe-optional).

## Starting another project

Start a new project from the [base template](https://github.com/mememade-github/polyagent-devcontainer), not from this repository.

## Vendor parity sync

```bash
bash scripts/sync-agents-mirror.sh         # .claude/ → .agents/rules, .agents/skills (prunes deleted-source orphans)
bash scripts/sync-agents-mirror.sh --dry   # diff only
```

`.claude/` is the ground truth. `.agents/rules/` and `.agents/skills/` are
generated with matching content and file modes; do not edit them by hand. The
other `.agents/` files (`hooks.json`, `hooks/`, `rules.json`) are hand-maintained
Antigravity configuration that the sync never touches.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Build fails | `docker compose -f .devcontainer/docker-compose.yml build --no-cache` |
| Files invisible or container is unhealthy | A: use Reopen in Container. B: set `HOST_WORKSPACE_PATH` to a project path accessible to the Docker daemon. See [Configuration](REFERENCE.md#configuration-devcontainerenv). |
| Reopen menu missing | Install the Dev Containers extension |
| Claude re-auth needed | `docker volume ls \| grep claude-config` |
| Codex re-auth needed | `docker volume ls \| grep codex-config` |
| Antigravity re-auth needed or a rule is ignored | See [REFERENCE troubleshooting](REFERENCE.md#troubleshooting) |
| `.agents/` drift | `bash scripts/sync-agents-mirror.sh` |
