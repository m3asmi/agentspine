# AGENTS.md

## Project objective

Build a plugin-ready AI agent framework with:

- stable extension primitives
- strict runtime boundaries
- local-first execution
- configurable LLM gateway
- auditable side effects

## Core architecture constraints

- Python: 3.12.13
- Package manager: `uv`
- API framework: FastAPI
- Orchestration: LangGraph
- Persistence: PostgreSQL + pgvector
- Observability: Langfuse
- Local models: Ollama
- Remote model path: OpenAI-compatible gateway
- First channel: Telegram
- Odoo integration: JSON-2 for Odoo 19

## Delivery governance

### Approval flow

```
Planner -> Executor -> Reviewer -> Security Gate -> Council (if required) -> Approval Brief -> Human
```

### Global rules

- One task at a time per executor
- No scope expansion beyond task acceptance criteria
- No unrelated file changes
- No self-approval (executor cannot review own work)
- Prefer smallest safe change
- TDD mandatory: RED -> GREEN -> REFACTOR

### Required inputs for execution

- Task file (tasks/TASK-XXX.md)
- AGENTS.md
- Relevant specs from docs/

### Required outputs from execution

- Implementation code + tests
- Execution report (reviews/EXEC-TASK-XXX.md)

### Validation baseline

```bash
uv run ruff check .        # lint
uv run ruff format --check . # format
uv run mypy .              # type check
uv run pytest              # tests
uv run pytest --cov        # coverage (80%+ required)
```

### Hard stop conditions

- Security vulnerability discovered -> fix before continuing
- Exposed secret -> rotate immediately
- Build broken on main -> fix before new work
- Task scope exceeded -> stop, re-plan

## Codex working rules

- Do not bypass the plugin system.
- Do not hardcode provider-specific calls inside orchestration nodes.
- Do not write directly to live repos.
- Repo outputs are patch artifacts only in v1.
- Finance actions are read/analyze/draft only in v1.
- Personal note edits require approval. Append-only can be auto-approved by policy.
- All side effects must emit audit events.
- All plugin contributions must be declared in the manifest.
- Do not import internal modules from plugin code unless the module is part of `platform_api`.

## Public extension surface

Only these extension types are public in Stage 1:

- `ExtensionBase`
- `CapabilityExtension`
- `DomainPackExtension`
- `ChannelExtension`
- `PolicyExtension`
- `IngestionExtension`
- `RendererExtension`

## Registries

Every contribution must be registered through a framework registry:

- PluginRegistry
- CapabilityRegistry
- DomainPackRegistry
- ChannelRegistry
- PolicyRegistry
- GraphNodeRegistry
- GraphTemplateRegistry
- RendererRegistry
- IngestionRegistry
- SettingsRegistry

## Required engineering quality

- typed interfaces
- schema-first IO
- semantic versioning for manifests
- migration hooks for breaking changes
- deny-by-default permissions
- deterministic startup sequence
- phase tasks must be completed in order unless explicitly marked parallel-safe

## Before coding

Read in this order:

1. `docs/specs/tech-stack-lock-v1.md`
2. `docs/specs/plugin-manifest-v1.md`
3. `docs/specs/contribution-points-v1.md`
4. `docs/specs/capability-contract-v1.md`
5. `tasks/README.md`
6. current phase file

## context-mode — MANDATORY routing rules

You have context-mode MCP tools available. These rules are NOT optional — they protect your context window from flooding. A single unrouted command can dump 56 KB into context and waste the entire session.

### BLOCKED commands — do NOT attempt these

#### curl / wget — BLOCKED
Any Bash command containing `curl` or `wget` is intercepted and replaced with an error message. Do NOT retry.
Instead use:
- `ctx_fetch_and_index(url, source)` to fetch and index web pages
- `ctx_execute(language: "javascript", code: "const r = await fetch(...)")` to run HTTP calls in sandbox

#### Inline HTTP — BLOCKED
Any Bash command containing `fetch('http`, `requests.get(`, `requests.post(`, `http.get(`, or `http.request(` is intercepted and replaced with an error message. Do NOT retry with Bash.
Instead use:
- `ctx_execute(language, code)` to run HTTP calls in sandbox — only stdout enters context

#### WebFetch — BLOCKED
WebFetch calls are denied entirely. The URL is extracted and you are told to use `ctx_fetch_and_index` instead.
Instead use:
- `ctx_fetch_and_index(url, source)` then `ctx_search(queries)` to query the indexed content

### REDIRECTED tools — use sandbox equivalents

#### Bash (>20 lines output)
Bash is ONLY for: `git`, `mkdir`, `rm`, `mv`, `cd`, `ls`, `npm install`, `pip install`, and other short-output commands.
For everything else, use:
- `ctx_batch_execute(commands, queries)` — run multiple commands + search in ONE call
- `ctx_execute(language: "shell", code: "...")` — run in sandbox, only stdout enters context

#### Read (for analysis)
If you are reading a file to **Edit** it → Read is correct (Edit needs content in context).
If you are reading to **analyze, explore, or summarize** → use `ctx_execute_file(path, language, code)` instead. Only your printed summary enters context. The raw file content stays in the sandbox.

#### Grep (large results)
Grep results can flood context. Use `ctx_execute(language: "shell", code: "grep ...")` to run searches in sandbox. Only your printed summary enters context.

### Tool selection hierarchy

1. **GATHER**: `ctx_batch_execute(commands, queries)` — Primary tool. Runs all commands, auto-indexes output, returns search results. ONE call replaces 30+ individual calls.
2. **FOLLOW-UP**: `ctx_search(queries: ["q1", "q2", ...])` — Query indexed content. Pass ALL questions as array in ONE call.
3. **PROCESSING**: `ctx_execute(language, code)` | `ctx_execute_file(path, language, code)` — Sandbox execution. Only stdout enters context.
4. **WEB**: `ctx_fetch_and_index(url, source)` then `ctx_search(queries)` — Fetch, chunk, index, query. Raw HTML never enters context.
5. **INDEX**: `ctx_index(content, source)` — Store content in FTS5 knowledge base for later search.

### Subagent routing

When spawning subagents (Agent/Task tool), the routing block is automatically injected into their prompt. Bash-type subagents are upgraded to general-purpose so they have access to MCP tools. You do NOT need to manually instruct subagents about context-mode.

### Output constraints

- Keep responses under 500 words.
- Write artifacts (code, configs, PRDs) to FILES — never return them as inline text. Return only: file path + 1-line description.
- When indexing content, use descriptive source labels so others can `ctx_search(source: "label")` later.

### ctx commands

| Command | Action |
|---------|--------|
| `ctx stats` | Call the `ctx_stats` MCP tool and display the full output verbatim |
| `ctx doctor` | Call the `ctx_doctor` MCP tool, run the returned shell command, display as checklist |
| `ctx upgrade` | Call the `ctx_upgrade` MCP tool, run the returned shell command, display as checklist |
