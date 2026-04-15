# TASK-101: Memory Capability Contract and Adapter Protocol Baseline

## Description

Define the memory capability contract foundation: `MemoryCapabilityExtension` orchestration interface, shared memory adapter protocol, and adapter registry hooks. This task is contract-first and intentionally excludes concrete storage/runtime implementations.

## Acceptance Criteria

- [ ] Typed `MemoryCapabilityExtension` contract exists under `platform_api/extensions/`
- [ ] Shared adapter protocol exists under `adapters/` with explicit request/response schemas
- [ ] Adapter registry enforces unique adapter IDs and deterministic lookup behavior
- [ ] Unit tests cover duplicate registration, unknown adapter key, and empty-registry behavior
- [ ] No provider-specific or storage-specific logic is implemented in this task

## Scope

### In scope
- `src/agent_framework/platform_api/extensions/memory_capability.py`
- `src/agent_framework/adapters/memory_adapter.py`
- `src/agent_framework/registries/memory_adapter_registry.py`
- `tests/unit/test_memory_adapter_registry.py`

### Out of scope
- Database migrations
- Concrete adapter implementations (`native_pgvector_adapter`, `cognee_adapter`)
- Memory routing/fallback workflow logic

## Dependencies

- TASK-P0-012 must be complete

## Validation Steps

1. `uv run pytest tests/unit/test_memory_adapter_registry.py` — contract/registry behavior passes
2. `uv run ruff check .` — lint clean
3. `uv run ruff format --check .` — formatting clean
4. `uv run mypy .` — typing clean

## Estimated Size

M

## Governance Classification

- risk_level: medium
- council_required: no
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - Foundational interfaces are consumed by all downstream memory adapters
  - Contract drift here causes cross-adapter incompatibility
- reclassification_required_after_diff: yes
- planner_rationale: Contract-first task with no external writes, but medium impact because it defines shared interfaces for subsequent memory branch work.
