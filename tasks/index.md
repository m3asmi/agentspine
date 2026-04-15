---
contract_version: v2
artifact_type: task_index
execution_graph:
  - TASK-P0-001
  - TASK-DOC-001
  - TASK-DOC-002
  - TASK-P0-002
  - TASK-P0-003
  - TASK-P0-004
  - TASK-P0-005
  - TASK-P0-006
  - TASK-P0-008
  - TASK-P0-009
  - TASK-P0-007
  - TASK-P0-010
  - TASK-P0-011
  - TASK-P0-012
  - TASK-SK-001
  - TASK-SK-002
  - TASK-SK-003
  - TASK-SK-004
  - TASK-SK-005
  - TASK-SK-006
  - TASK-SK-007
  - TASK-SK-008
  - TASK-P1-001
  - TASK-P2-001
  - TASK-P3-001
  - TASK-P4-001
  - TASK-P5-001
  - TASK-P6-001
parallel_groups:
  - [TASK-102, TASK-103]
optional_branches:
  - branch_id: memory_adapters
    start_after: TASK-P0-012
    execution_graph:
      - TASK-101
      - TASK-102
      - TASK-103
      - TASK-104
---

## Summary
Canonical execution graph for AgentSpine v1 planning: Phase 0 contracts and docs hardening first, then skill-driven framework primitives, then phase-aligned vertical delivery. Memory-adapter tasks remain an optional branch that starts after P0.

## Evidence
- Existing repository is a stage-0 skeleton with strong architectural specs and phase documents.
- Phase 0 requires deterministic ordering due tight coupling between manifests, registries, lifecycle, policy, audit, and dispatcher.
- Memory adapter work is scoped enough to track as a separate optional branch once the platform baseline is complete.

## Decisions
- P0 remains dependency-ordered, including TASK-P0-009 before TASK-P0-007 due audit-emitter dependency.
- TASK-DOC-001 and TASK-DOC-002 stay in the canonical graph for spec and governance alignment.
- TASK-SK series executes sequentially after P0 to establish reusable skills, planning, and guardrails before domain expansion.
- P1 through P6 execute sequentially with phase exit gates.
- TASK-101 through TASK-104 remain an optional memory branch after P0; TASK-102 and TASK-103 are the only parallel-safe pair inside that branch.

## Metadata
- wave_rationale: "Dependency-ordered execution minimizes migration cost and enforces stable public contracts and specs before domain expansion."
- governance_snapshot:
  - low: [TASK-DOC-001, TASK-DOC-002, TASK-P0-001, TASK-P0-002, TASK-P0-003, TASK-P0-004, TASK-P0-005, TASK-P0-006, TASK-P0-007, TASK-P0-009, TASK-P0-010, TASK-P0-011, TASK-P0-012, TASK-SK-001, TASK-101]
  - medium: [TASK-P0-008, TASK-SK-002, TASK-SK-003, TASK-SK-005, TASK-SK-006, TASK-SK-008, TASK-P1-001, TASK-P5-001, TASK-P6-001, TASK-102, TASK-103, TASK-104]
  - high: [TASK-SK-004, TASK-SK-007, TASK-P2-001, TASK-P3-001, TASK-P4-001]
- notes: "Do not start a phase until the previous phase gate is green unless explicitly marked parallel-safe."
