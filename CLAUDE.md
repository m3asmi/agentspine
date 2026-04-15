# CLAUDE.md — Agent Framework

> **Single source of truth for working rules:** [AGENTS.md](./AGENTS.md)
> Read AGENTS.md before starting any work.

## What is this project?

A plugin-ready AI agent framework with strict runtime boundaries, local-first execution, and auditable side effects. The system uses a two-layer architecture:

- **Layer A (Platform API):** Stable public extension surface for plugins (`src/agent_framework/platform_api/`)
- **Layer B (Internal Runtime):** LangGraph orchestration, registries, execution dispatcher, audit, LLM gateway

## Tech stack (locked)

| Component | Choice |
|-----------|--------|
| Python | 3.12.13 |
| Package manager | `uv` |
| API framework | FastAPI |
| Orchestration | LangGraph |
| Database | PostgreSQL + pgvector |
| Observability | Langfuse |
| Local models | Ollama |
| Remote models | OpenAI-compatible gateway |
| Channel (v1) | Telegram |
| ERP integration | Odoo 19 via JSON-2 |

## Repository layout

```
src/agent_framework/
  main.py                  # FastAPI app, health endpoint
  platform_api/            # PUBLIC extension boundary (only stable API)
    contracts/             # Extension base interfaces
    extensions/            # Extension type definitions
  registries/              # 10 registries (Plugin, Capability, DomainPack, etc.)
  lifecycle/               # Plugin install/enable/disable/upgrade/uninstall
  compatibility/           # API version and framework range validation
  plugins/                 # Plugin discovery and loading
  audit/                   # Audit event emission
  execution/               # Safe capability invocation dispatcher
  llm_gateway/             # Provider routing (Ollama / OpenAI-compatible)
  orchestration/           # LangGraph runtime integration
  memory/                  # Thread, user, workspace memory
  knowledge/               # Knowledge base + retrieval (pgvector)
  policy/                  # Policy engine and enforcement
  adapters/                # Provider adapters (Telegram, Odoo)

docs/
  architecture/            # Design docs (overview, runtime, plugin system, etc.)
  specs/                   # Formal specs (tech stack, manifests, contracts, permissions)
  development/             # Setup, build order, testing strategy, codex workflow
  adr/                     # Architecture Decision Records
  templates/               # Plugin examples

tasks/                     # Phased roadmap (Phase 0-6 + backlog)
tests/                     # pytest suite (pytest-asyncio, pytest-cov)
```

## Current state (Phase 0 — in progress)

**Completed:** Project bootstrap, FastAPI health endpoint, test skeleton.

**Remaining Phase 0 tasks:** Platform API interfaces, manifest schema/loader, compatibility validator, dependency resolver, registry manager, lifecycle manager, permission model, audit emitter, LLM gateway skeleton, execution dispatcher, startup sequence.

**Exit gate:** Plugin discovery works, manifest validation enforced, registries live, lifecycle hooks tested, audit events emitted, deterministic app boot.

## Before coding — read in this order

1. `docs/specs/tech-stack-lock-v1.md`
2. `docs/specs/plugin-manifest-v1.md`
3. `docs/specs/contribution-points-v1.md`
4. `docs/specs/capability-contract-v1.md`
5. `tasks/README.md`
6. Current phase file (e.g., `tasks/phase-0-kernel.md`)

## Critical rules

- **Do not bypass the plugin system.** All contributions go through registries.
- **Do not hardcode provider-specific calls** inside orchestration nodes.
- **Do not write directly to live repos** — patch artifacts only in v1.
- **Finance actions are read/analyze/draft only** in v1.
- **Personal note edits require approval.** Append-only can be auto-approved by policy.
- **All side effects must emit audit events.**
- **All plugin contributions must be declared in the manifest.**
- **Do not import internal modules from plugin code** — only `platform_api` is allowed.
- **Deny-by-default permissions** — plugins request profiles, kernel grants, runtime enforces.

## Extension types (public in Stage 1)

`ExtensionBase`, `CapabilityExtension`, `DomainPackExtension`, `ChannelExtension`, `PolicyExtension`, `IngestionExtension`, `RendererExtension`

## Registries

`PluginRegistry`, `CapabilityRegistry`, `DomainPackRegistry`, `ChannelRegistry`, `PolicyRegistry`, `GraphNodeRegistry`, `GraphTemplateRegistry`, `RendererRegistry`, `IngestionRegistry`, `SettingsRegistry`

## Risk tiers for capabilities

| Tier | Scope | Example |
|------|-------|---------|
| R0 | Read-only | Fetch Odoo data |
| R1 | Workspace generation | Generate patch file |
| R2 | Bounded local write | Edit workspace file |
| R3 | Live external | Send Telegram message |

## Development commands

```bash
uv sync                    # Install dependencies
uv run pytest              # Run tests
uv run pytest --cov        # Run tests with coverage
uv run ruff check .        # Lint
uv run mypy .              # Type check
uv run uvicorn agent_framework.main:app --reload  # Run dev server
```

## Environment setup

Copy `.env.example` to `.env` and fill in values. Key services:
- PostgreSQL (with pgvector extension)
- Langfuse (localhost:3010)
- Ollama (localhost:11434)
- Telegram bot token + chat ID
- Odoo connection details

## Testing strategy

| Layer | What | Tool |
|-------|------|------|
| Unit | Functions, validators, registries | pytest |
| Contract | Extension compliance, capability schemas | pytest |
| Integration | Plugin load, settings merge, gateway routing | pytest + testcontainers |
| Plugin | Manifest sanity, registration, healthchecks | pytest |
| E2E | Telegram flow, patch generation, approvals | pytest + Playwright |

**Target coverage: 80%+. TDD is mandatory** (RED → GREEN → REFACTOR).

## Phased roadmap

| Phase | Focus |
|-------|-------|
| 0 | Kernel and extensibility primitives |
| 1 | Personal pack + local knowledge (Telegram, Obsidian, filesystem) |
| 2 | Odoo 19 integration + engineering pack |
| 3 | Finance pack + source-linked analysis |
| 4 | Approvals, admin UI, hardening |
| 5 | Plugin SDK hardening + internal ecosystem |
| 6 | Cloud portability + SaaS-prep |

Phases must complete in order unless explicitly marked parallel-safe.

# context-mode — MANDATORY routing rules

You have context-mode MCP tools available. These rules are NOT optional — they protect your context window from flooding. A single unrouted command can dump 56 KB into context and waste the entire session.

## BLOCKED commands — do NOT attempt these

### curl / wget — BLOCKED
Any Bash command containing `curl` or `wget` is intercepted and replaced with an error message. Do NOT retry.
Instead use:
- `ctx_fetch_and_index(url, source)` to fetch and index web pages
- `ctx_execute(language: "javascript", code: "const r = await fetch(...)")` to run HTTP calls in sandbox

### Inline HTTP — BLOCKED
Any Bash command containing `fetch('http`, `requests.get(`, `requests.post(`, `http.get(`, or `http.request(` is intercepted and replaced with an error message. Do NOT retry with Bash.
Instead use:
- `ctx_execute(language, code)` to run HTTP calls in sandbox — only stdout enters context

### WebFetch — BLOCKED
WebFetch calls are denied entirely. The URL is extracted and you are told to use `ctx_fetch_and_index` instead.
Instead use:
- `ctx_fetch_and_index(url, source)` then `ctx_search(queries)` to query the indexed content

## REDIRECTED tools — use sandbox equivalents

### Bash (>20 lines output)
Bash is ONLY for: `git`, `mkdir`, `rm`, `mv`, `cd`, `ls`, `npm install`, `pip install`, and other short-output commands.
For everything else, use:
- `ctx_batch_execute(commands, queries)` — run multiple commands + search in ONE call
- `ctx_execute(language: "shell", code: "...")` — run in sandbox, only stdout enters context

### Read (for analysis)
If you are reading a file to **Edit** it → Read is correct (Edit needs content in context).
If you are reading to **analyze, explore, or summarize** → use `ctx_execute_file(path, language, code)` instead. Only your printed summary enters context. The raw file content stays in the sandbox.

### Grep (large results)
Grep results can flood context. Use `ctx_execute(language: "shell", code: "grep ...")` to run searches in sandbox. Only your printed summary enters context.

## Tool selection hierarchy

1. **GATHER**: `ctx_batch_execute(commands, queries)` — Primary tool. Runs all commands, auto-indexes output, returns search results. ONE call replaces 30+ individual calls.
2. **FOLLOW-UP**: `ctx_search(queries: ["q1", "q2", ...])` — Query indexed content. Pass ALL questions as array in ONE call.
3. **PROCESSING**: `ctx_execute(language, code)` | `ctx_execute_file(path, language, code)` — Sandbox execution. Only stdout enters context.
4. **WEB**: `ctx_fetch_and_index(url, source)` then `ctx_search(queries)` — Fetch, chunk, index, query. Raw HTML never enters context.
5. **INDEX**: `ctx_index(content, source)` — Store content in FTS5 knowledge base for later search.

## Subagent routing

When spawning subagents (Agent/Task tool), the routing block is automatically injected into their prompt. Bash-type subagents are upgraded to general-purpose so they have access to MCP tools. You do NOT need to manually instruct subagents about context-mode.

## Output constraints

- Keep responses under 500 words.
- Write artifacts (code, configs, PRDs) to FILES — never return them as inline text. Return only: file path + 1-line description.
- When indexing content, use descriptive source labels so others can `ctx_search(source: "label")` later.

## ctx commands

| Command | Action |
|---------|--------|
| `ctx stats` | Call the `ctx_stats` MCP tool and display the full output verbatim |
| `ctx doctor` | Call the `ctx_doctor` MCP tool, run the returned shell command, display as checklist |
| `ctx upgrade` | Call the `ctx_upgrade` MCP tool, run the returned shell command, display as checklist |
