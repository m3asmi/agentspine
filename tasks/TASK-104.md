# TASK-104: Compose Dual-Adapter Memory Capability

## Description

Compose `MemoryCapabilityExtension` using `native_pgvector_adapter` and `cognee_adapter`, implement strategy-driven adapter selection/fallback, and finalize capability/plugin declaration artifacts with end-to-end integration tests.

## Acceptance Criteria

- [ ] Extension routes through primary/fallback adapters using explicit strategy policy
- [ ] Capability declaration schema is added and plugin manifest contribution is valid
- [ ] Deny-by-default permissions are respected and no direct provider calls occur in orchestration nodes
- [ ] Audit events are emitted for read/write side effects across both adapter paths
- [ ] Integration tests cover success, fallback, and both-adapters-unavailable scenarios

## Scope

### In scope
- `src/agent_framework/memory/memory_capability_extension.py`
- `src/agent_framework/plugins/memory_capability/manifest.yaml`
- `src/agent_framework/platform_api/contracts/capabilities/memory_query.yaml`
- `tests/integration/test_memory_capability_extension_dual_adapter.py`

### Out of scope
- Telegram/Odoo channel features
- Unrelated plugin ecosystem changes
- New external storage adapters beyond TASK-102/TASK-103

## Dependencies

- TASK-102 must be complete
- TASK-103 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_memory_capability_extension_dual_adapter.py` — dual-adapter integration behavior passes
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
  - Capability routing policy can change memory behavior across packs
  - Incorrect manifest/permission declarations can bypass intended governance boundaries
- reclassification_required_after_diff: yes
- planner_rationale: Medium risk integration task with workflow/governance impact; no finance actions and no uncontrolled external writes.
