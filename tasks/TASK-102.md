# TASK-102: Native pgvector Memory Adapter

## Description

Implement `native_pgvector_adapter` as the local-first memory backend, including repository wiring, schema migration, metadata filtering, and deterministic retrieval behavior when vector search yields empty results.

## Acceptance Criteria

- [ ] `native_pgvector_adapter` conforms to adapter protocol from TASK-101
- [ ] Memory table + pgvector index migration exists and is reversible/idempotent
- [ ] Top-k vector retrieval works with metadata filter intersection
- [ ] Deterministic lexical fallback behavior is defined for empty vector results
- [ ] Integration tests cover write/read/update/query edge cases

## Scope

### In scope
- `src/agent_framework/adapters/native_pgvector_adapter.py`
- `src/agent_framework/memory/repositories/pgvector_memory_store.py`
- `src/agent_framework/memory/migrations/001_memory_pgvector.sql`
- `tests/integration/test_native_pgvector_adapter.py`

### Out of scope
- Cognee adapter integration
- Channel/plugin UX changes
- Orchestration-node direct SQL logic

## Dependencies

- TASK-101 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_native_pgvector_adapter.py` — adapter integration behavior passes
2. `uv run ruff check .` — lint clean
3. `uv run ruff format --check .` — formatting clean
4. `uv run mypy .` — typing clean

## Estimated Size

L

## Governance Classification

- risk_level: medium
- council_required: no
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - Introduces database migration and pgvector retrieval behavior
  - Retrieval ranking/filtering regressions can degrade memory quality
- reclassification_required_after_diff: yes
- planner_rationale: Medium risk due schema + retrieval semantics impact; still bounded to local-first backend and no external financial/auth boundary changes.
