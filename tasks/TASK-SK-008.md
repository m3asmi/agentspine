# TASK-SK-008: Optional Multi-Agent Review Mode (Opt-In)

## Description

Add optional expert/decision review mode for high-stakes evaluations while preserving single-agent default execution.

## Acceptance Criteria

- [ ] Add configuration flags: `expert_mode`, `decision_review_mode`
- [ ] Multi-agent review path is off by default
- [ ] Allowed use cases constrained to architecture/risk/option evaluation
- [ ] Cost/latency metadata attached to review outcomes
- [ ] Tests verify no default path regression to agent swarms

## Scope

### In scope
- Optional review orchestration contract
- Guardrails for opt-in only behavior

### Out of scope
- General multi-agent default runtime

## Dependencies

- TASK-SK-007 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_optional_ensemble_review_mode.py`
2. `uv run ruff check .`
3. `uv run mypy .`

## Estimated Size

M

## Governance Classification

- risk_level: medium
- council_required: no
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - Multi-agent mode activated by default
  - Unbounded duplicate execution/cost loops
- reclassification_required_after_diff: yes
- planner_rationale: Optional orchestration feature with governance and cost implications.
