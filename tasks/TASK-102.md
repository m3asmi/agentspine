---
contract_version: v2
artifact_type: task
task_id: TASK-102
risk_level: medium
council_required: no
human_approval_stages:
  - before_merge
dependencies:
  - TASK-101
parallelizable: false
parallel_group: ""
conflict_scope:
  - src/agent_framework/adapters/
  - src/agent_framework/memory/
  - tests/
integration_blockers:
  - "Depends on finalized adapter protocol from TASK-101"
merge_strategy: sequential_only
risk_triggers:
  - "Introduces database schema and pgvector query behavior"
  - "Incorrect retrieval ranking can degrade memory relevance"
planner_rationale: "Database-impacting task (migration/schema + vector retrieval), classified medium per impact routing."
model_overrides: {}
---

## Summary
Implement `native_pgvector_adapter` as the local-first memory backend, including repository wiring, schema migration, metadata filtering, and deterministic retrieval fallback behavior.

## Evidence
- Architecture and phase roadmap explicitly require pgvector-backed retrieval flow.
- No current implementation exists; adapter must align with the contract from TASK-101.

## Decisions
- Implement adapter behind the TASK-101 protocol; no direct use from orchestration nodes.
- Keep SQL explicit and typed for vector operations.
- Require audit events on write and read side effects where framework hooks exist.

## Acceptance Criteria
- [ ] `native_pgvector_adapter` conforms to adapter protocol from TASK-101
- [ ] Memory table plus pgvector index migration exists and is reversible and idempotent
- [ ] Top-k vector retrieval works with metadata filter intersection
- [ ] Deterministic lexical fallback behavior is defined for empty vector results
- [ ] Integration tests cover write, read, update, and query edge cases

## Metadata
- target_files:
  - src/agent_framework/adapters/native_pgvector_adapter.py
  - src/agent_framework/memory/repositories/pgvector_memory_store.py
  - src/agent_framework/memory/migrations/001_memory_pgvector.sql
  - tests/integration/test_native_pgvector_adapter.py
- exclusions:
  - "No cognee integration"
  - "No channel/plugin UX changes"

## Impact Checklist
- database: migration plus pgvector-backed memory table and index creation
- backend: add native pgvector adapter and repository implementation
- frontend: none
- api_contracts: none
- infra_ci: none
- security: none
- business_workflow: memory retrieval ranking and metadata filtering behavior

## Validation Steps
1. `uv run pytest tests/integration/test_native_pgvector_adapter.py` - adapter integration behavior passes
2. `uv run ruff check .` - lint clean
3. `uv run ruff format --check .` - formatting clean
4. `uv run mypy .` - typing clean

## Test Requirements
- required_behavior_to_test: "insert/query/update memory records, vector top-k retrieval, metadata filter intersection, lexical fallback when vector returns empty."
- expected_regressions_to_prevent: "duplicate writes from idempotent keys, incorrect namespace leakage, unstable ordering for equal scores."
- edge_cases_to_cover: "missing vector extension, empty namespace, malformed embedding dimensions, null metadata keys."
