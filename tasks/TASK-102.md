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
Implement `native_pgvector_adapter` to store, index, and retrieve memory entries with metadata filters and deterministic fallback behavior for empty vector results.

## Evidence
- Architecture and phase roadmap explicitly require pgvector-backed retrieval flow.
- No current implementation exists; adapter must align with contract from TASK-101.

## Decisions
- Implement adapter behind protocol from TASK-101; no direct use from orchestration nodes.
- Keep SQL explicit and typed for vector operations.
- Require audit events on write/read side effects where framework hooks exist.

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
- database: migration + pgvector-backed memory table/index creation
- backend: add native pgvector adapter and repository implementation
- frontend: none
- api_contracts: none
- infra_ci: none
- security: none
- business_workflow: memory retrieval ranking + metadata filtering behavior

## Test Requirements
- required_behavior_to_test: "insert/query/update memory records, vector top-k retrieval, metadata filter intersection, lexical fallback when vector returns empty."
- expected_regressions_to_prevent: "duplicate writes from idempotent keys, incorrect namespace leakage, unstable ordering for equal scores."
- edge_cases_to_cover: "missing vector extension, empty namespace, malformed embedding dimensions, null metadata keys."
