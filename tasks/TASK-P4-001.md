# TASK-P4-001: Approval Service + Admin Control Surface

## Description

Implement centralized approvals and operational control tooling: approval queue/state machine, policy overrides with audit trail, and minimal admin surface for traceability and intervention.

## Acceptance Criteria

- [ ] Approval request lifecycle implemented (pending/approved/rejected/expired)
- [ ] Resume-token flow supported for paused executions
- [ ] Admin endpoints/UI expose audit timeline, approval queue, and policy decisions
- [ ] All approval decisions emit immutable audit events
- [ ] Degraded mode behavior defined and tested

## Scope

### In scope
- Approval orchestration
- Operational visibility for single-user/local-first setup

### Out of scope
- Full multi-tenant RBAC UI
- Advanced analytics dashboards

## Dependencies

- TASK-P3-001 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_phase4_approvals.py`
2. `uv run ruff check .`
3. `uv run mypy .`

## Estimated Size

L

## Governance Classification

- risk_level: high
- council_required: no
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - Approval bypass or inconsistent resume state
  - Missing audit trail for approval decisions
- reclassification_required_after_diff: yes
- planner_rationale: Core safety-control plane; correctness is critical for bounded autonomy.
