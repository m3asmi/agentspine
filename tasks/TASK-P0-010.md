# TASK-P0-010: LLM Gateway Skeleton

## Description

Create the provider profile model and gateway interface for routing LLM calls to local (Ollama) or remote (OpenAI-compatible) providers. No actual API calls yet — this is the contract and routing logic.

## Acceptance Criteria

- [ ] Provider profile model: name, base_url, model_id, api_key_env, timeout, capabilities
- [ ] Gateway interface with `complete()` and `stream()` methods
- [ ] Routing modes: `local_only`, `remote_only`, `manual_compare`, `fallback_on_failure`, `fallback_on_low_confidence`
- [ ] Provider configuration validates at startup (schema + env var presence)
- [ ] No orchestration node calls provider SDK directly (gateway is the only path)
- [ ] Stub implementations that return typed responses
- [ ] Tests for routing mode selection and config validation
- [ ] 80%+ coverage on new code

## Scope

### In scope
- `llm_gateway/models.py` — provider profile, request/response models
- `llm_gateway/gateway.py` — gateway interface and routing logic
- `llm_gateway/providers/base.py` — provider ABC
- `llm_gateway/providers/ollama.py` — stub
- `llm_gateway/providers/openai_compat.py` — stub

### Out of scope
- Actual API calls to Ollama or OpenAI
- Token counting, cost tracking
- Langfuse integration

## Dependencies

- TASK-P0-009 — audit emitter for llm_call events

## Validation Steps

1. `uv run pytest tests/test_llm_gateway/` — unit tests pass
2. `uv run ruff check src/agent_framework/llm_gateway/` — lint clean
3. `uv run mypy src/agent_framework/llm_gateway/` — type check clean

## Estimated Size

M

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Gateway design constrains all future LLM integration (but skeleton only — no actual calls)
  - API key handling must use env vars, never hardcoded
- reclassification_required_after_diff: yes
- planner_rationale: Skeleton interfaces and stubs only — no actual external API calls in Phase 0. No secrets in code (env var references only). Design decisions are important but reversible at this stage.
