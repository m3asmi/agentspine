# TASK-P0-009: Audit Emitter

## Description

Define the audit event model and implement emission hooks for plugin load, lifecycle transitions, capability registration, and LLM calls. Every side-effecting action must produce a structured audit payload.

## Acceptance Criteria

- [ ] Audit event model: timestamp, event_type, source_plugin, actor, payload, risk_tier
- [ ] Audit emitter interface (abstract — concrete backends come later)
- [ ] In-memory audit backend for testing
- [ ] Events emitted for: plugin_loaded, plugin_enabled, plugin_disabled, capability_registered, llm_call_started, llm_call_completed
- [ ] No PII in audit payloads (use references, not raw data)
- [ ] Tests verify every lifecycle action emits correct audit payload
- [ ] 80%+ coverage on new code

## Scope

### In scope
- `audit/models.py` — event model
- `audit/emitter.py` — emitter interface + in-memory backend
- `audit/events.py` — event type constants

### Out of scope
- Persistent audit storage (database)
- Audit query API
- Langfuse integration

## Dependencies

- None (standalone — other tasks integrate with it)

## Validation Steps

1. `uv run pytest tests/test_audit/` — unit tests pass
2. `uv run ruff check src/agent_framework/audit/` — lint clean
3. `uv run mypy src/agent_framework/audit/` — type check clean

## Estimated Size

S

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Missing audit events could create compliance gaps (mitigated by explicit test for each event type)
- reclassification_required_after_diff: yes
- planner_rationale: Internal structured logging with no external side effects. In-memory only in Phase 0. No auth, no data persistence, no external calls.
