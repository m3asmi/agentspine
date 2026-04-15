---
contract_version: v2
artifact_type: task_index
execution_graph:
  - TASK-101
  - TASK-102
  - TASK-103
  - TASK-104
parallel_groups: []
---

## Summary
Task plan for recommended implementation pattern: `MemoryCapabilityExtension` with `native_pgvector_adapter` and `cognee_adapter`, delivered in dependency-safe sequence.

## Evidence
- Adapter and memory packages are currently skeletons; foundational contracts are required first.
- Risk routing constraints escalate database-impacting and workflow-impacting tasks to medium.
- Parallel safety check found overlapping write scopes (`adapters/`, `memory/`, `tests/`), so execution remains sequential.

## Decisions
- Wave 0: TASK-101 establishes interfaces/registry contracts.
- Wave 1: TASK-102 implements native pgvector adapter.
- Wave 2: TASK-103 implements cognee adapter with contract parity.
- Wave 3: TASK-104 composes extension + capability/manifest + integration tests.
- No parallel group declared due shared conflict scopes and integration blockers.

## Metadata
- wave_rationale: "Each task depends on artifacts from the previous wave; sequencing minimizes merge conflict risk and keeps validation incremental."
- governance_snapshot:
  - low: [TASK-101]
  - medium: [TASK-102, TASK-103, TASK-104]
  - high: []
- notes: "Legacy phase roadmap remains in `tasks/phase*.md`; this index is the canonical v2 execution graph for the scoped plan."
