# Extensible Agent Framework

Local-first, extensible AI agent framework.

## Current target

- Stage 1: extensibility-first kernel
- Development mode: Codex-driven implementation
- Runtime: FastAPI + LangGraph + PostgreSQL + pgvector + Langfuse
- Local model lane: Ollama
- Remote comparison lane: OpenAI-compatible providers
- First channel: Telegram
- Primary business integration: Odoo 19 JSON-2

## Start here

- `AGENTS.md`
- `docs/specs/tech-stack-lock-v1.md`
- `docs/architecture/stage1-kernel-overview.md`
- `tasks/README.md`

## Delivery model

Implementation is organized by phases.
Each phase has:

- scope
- deliverables
- task breakdown
- dependencies
- acceptance criteria
- exit gate

## Commands

```bash
uv sync
uv run pytest
uv run uvicorn agent_framework.main:app --reload
```
