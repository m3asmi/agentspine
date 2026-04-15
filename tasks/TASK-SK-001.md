# TASK-SK-001: Extension Interfaces and Registries Baseline

## Description

Define and implement the public extension interfaces and minimal registries required to support skill-driven workflows without coupling tools into core runtime.

## Acceptance Criteria

- [ ] Add typed extension interfaces under `platform_api/extensions/` (base, capability, domain_pack, channel, policy, ingestion, renderer)
- [ ] Add minimal typed registry base + `SkillRegistry` and `PlanningRegistry`
- [ ] Duplicate registration is blocked with explicit errors
- [ ] Contract tests validate interface shape and registry behavior
- [ ] No plugin imports internal runtime modules beyond `platform_api`

## Scope

### In scope
- Public extension contracts
- Registry primitives for skills and planning artifacts

### Out of scope
- Concrete skill implementations
- Planning pipeline stage logic

## Dependencies

- TASK-P0-012 must be complete

## Validation Steps

1. `uv run pytest tests/contract/test_extension_interfaces.py`
2. `uv run ruff check .`
3. `uv run mypy .`

## Estimated Size

M

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Breaking public API contracts without migration notes
- reclassification_required_after_diff: yes
- planner_rationale: Contract-only foundation with no side effects.
