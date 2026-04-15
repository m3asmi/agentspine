# TASK-P0-007: Lifecycle Manager

## Description

Implement plugin lifecycle state machine: install -> enable -> disable -> upgrade -> uninstall. Each transition runs hooks with timeout handling and emits audit events. Failed transitions leave the plugin in a safe state.

## Acceptance Criteria

- [ ] Lifecycle states: `discovered`, `installed`, `enabled`, `disabled`, `error`
- [ ] State transitions with pre/post hooks
- [ ] Hook timeout handling (configurable, default 30s)
- [ ] Failed `enable` leaves plugin in `installed` (not `enabled`)
- [ ] Failed `install` leaves plugin in `discovered`
- [ ] Upgrade flow: disable -> update -> re-enable
- [ ] Audit event emitted for every state transition
- [ ] Tests for happy path and failure scenarios per transition
- [ ] 80%+ coverage on new code

## Scope

### In scope
- `lifecycle/manager.py` — state machine and transition logic
- `lifecycle/hooks.py` — hook runner with timeout
- `lifecycle/states.py` — state enum and transition rules
- Integration with audit emitter (P0-009)

### Out of scope
- Actual plugin code execution
- Registry population (handled by startup sequence P0-012)

## Dependencies

- TASK-P0-006 — registries for registration/deregistration during transitions
- TASK-P0-009 — audit emitter for event emission

## Validation Steps

1. `uv run pytest tests/test_lifecycle/` — unit tests pass
2. `uv run ruff check src/agent_framework/lifecycle/` — lint clean
3. `uv run mypy src/agent_framework/lifecycle/` — type check clean

## Estimated Size

M

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - State machine bugs could leave plugins in inconsistent state (mitigated by explicit state transitions and failure tests)
  - Hook execution could have side effects (mitigated by timeout and audit)
- reclassification_required_after_diff: yes
- planner_rationale: Internal state machine with no external side effects in Phase 0. Hooks are abstract — concrete implementations come later. Audit integration is structured logging only.
