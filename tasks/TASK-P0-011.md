# TASK-P0-011: Execution Dispatcher Skeleton

## Description

Create execution request/response models and define worker boundary contracts. Capabilities request execution through the dispatcher — they never have direct shell access in the API process.

## Acceptance Criteria

- [ ] Execution request model: capability_id, input_payload, executor_profile, workspace_ref
- [ ] Execution response model: status, output_payload, artifacts, audit_ref
- [ ] Dispatcher interface with `dispatch()` method
- [ ] Worker boundary contract: defines what a worker can access based on executor profile
- [ ] Stub dispatcher for testing (returns mock responses)
- [ ] Tests for request validation and profile-based boundary checks
- [ ] 80%+ coverage on new code

## Scope

### In scope
- `execution/models.py` — request/response schemas
- `execution/dispatcher.py` — dispatcher interface + stub
- `execution/boundaries.py` — worker boundary definitions

### Out of scope
- Actual process isolation / sandboxing
- Docker/subprocess execution
- Workspace management

## Dependencies

- TASK-P0-008 — executor profiles used for boundary checks
- TASK-P0-009 — audit emitter for execution events

## Validation Steps

1. `uv run pytest tests/test_execution/` — unit tests pass
2. `uv run ruff check src/agent_framework/execution/` — lint clean
3. `uv run mypy src/agent_framework/execution/` — type check clean

## Estimated Size

S

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Execution boundary design affects safety of all future capability runs (skeleton only for now)
- reclassification_required_after_diff: yes
- planner_rationale: Interface and stub definitions only — no actual process execution. Boundary enforcement is modeled but not runtime-enforced yet. Low blast radius.
