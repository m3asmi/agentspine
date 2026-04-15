# TASK-P0-001: Phase 0 Contract Baseline

## Description

Establish the Phase 0 baseline for contract-first kernel development: testing harness, package boundaries, and canonical naming so all subsequent P0 tasks (002–012) can execute with deterministic dependencies.

## Acceptance Criteria

- [ ] `src/agent_framework/platform_api/` exists as the public extension surface root
- [ ] Contract-test folder structure exists (`tests/contract/`, `tests/unit/`, `tests/integration/`)
- [ ] Phase 0 task dependency chain is valid and non-cyclic
- [ ] `tasks/index.md` reflects canonical execution graph and governance routing
- [ ] Validation baseline commands are documented in this task and executable

## Scope

### In scope
- Establish naming, boundaries, and task-order baseline
- Define test folder conventions for Phase 0
- Ensure plan artifacts are internally consistent

### Out of scope
- Implementing runtime features
- Plugin implementations

## Dependencies

- None

## Validation Steps

1. `uv run ruff check .` — lint baseline valid
2. `uv run ruff format --check .` — formatting baseline valid
3. `uv run mypy .` — typing baseline valid
4. `uv run pytest` — test harness baseline valid

## Estimated Size

S

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Task graph contains circular dependencies or missing prerequisite tasks
- reclassification_required_after_diff: yes
- planner_rationale: Planning and structural consistency only; no side effects, no data writes.
