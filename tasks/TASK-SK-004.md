# TASK-SK-004: Execution Guardrails and Dangerous Action Policy

## Description

Implement explicit execution guardrails for risky actions: workspace sandboxing, path allowlists, dangerous git/filesystem action blocks, and controlled retries.

## Acceptance Criteria

- [ ] Add guardrail models and risk classifier
- [ ] Add policy gates for: `git push`, `reset --hard`, delete operations, migrations, mass edits, out-of-scope writes
- [ ] Enforce retry policy (failure classification before retry)
- [ ] Produce mandatory diff summary artifact before approval-required actions
- [ ] Guardrail decisions are auditable

## Scope

### In scope
- Policy engine + action gate implementation
- Testable risk and allow/deny decisions

### Out of scope
- Full worker isolation runtime (beyond interfaces/guards)

## Dependencies

- TASK-SK-003 must be complete

## Validation Steps

1. `uv run pytest tests/policy/test_execution_guardrails.py`
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
  - Destructive git/fs action allowed without policy decision
  - Writes outside approved paths
- reclassification_required_after_diff: yes
- planner_rationale: Directly controls autonomous safety boundaries and high-impact actions.
