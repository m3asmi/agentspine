# TASK-SK-003: First-Class Planning Pipeline

## Description

Implement structured planning pipeline stages (`clarify`, `spec`, `plan`, `task_breakdown`, `design_options`, `approval_gate`) with auditable artifacts.

## Acceptance Criteria

- [ ] Add `planning/` models and pipeline executor
- [ ] Each stage emits typed stage output with trace metadata
- [ ] Pipeline supports PRD/spec input and outputs executable task artifacts
- [ ] Approval gate stage is mandatory for non-trivial tasks
- [ ] Integration with `plan_feature` skill works end-to-end

## Scope

### In scope
- Planning stage orchestrator
- Structured output + audit hooks

### Out of scope
- Autonomous execution/apply stages

## Dependencies

- TASK-SK-002 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_plan_feature_pipeline.py`
2. `uv run ruff check .`
3. `uv run mypy .`

## Estimated Size

L

## Governance Classification

- risk_level: medium
- council_required: no
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - Missing approval gate for non-trivial plans
  - Unstructured planning outputs reduce auditability
- reclassification_required_after_diff: yes
- planner_rationale: Planning becomes framework-level control path and must remain deterministic/auditable.
