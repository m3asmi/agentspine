# TASK-SK-005: Engineering Review / Debug / QA Loop

## Description

Implement optional but structured engineering review loops: TDD-first checks, bug repro/assumption requirements, QA gates, and concern-specific reviews.

## Acceptance Criteria

- [ ] Add review models and loop coordinator
- [ ] Enforce no bug-fix run without repro case or explicit assumption record
- [ ] Enforce no apply/merge decision without review pass record
- [ ] Add concern-specific review stage hooks (code/security/perf)
- [ ] Review outcomes are attached to task audit trail

## Scope

### In scope
- Review loop orchestration and policy checks
- QA gate metadata contract

### Out of scope
- Always-on multi-agent review mode

## Dependencies

- TASK-SK-004 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_review_qa_loop.py`
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
  - Missing review artifact on high-risk changes
  - QA gate bypass
- reclassification_required_after_diff: yes
- planner_rationale: Control-plane quality feature with moderate execution impact.
