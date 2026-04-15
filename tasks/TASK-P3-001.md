# TASK-P3-001: Finance Pack (Read/Analyze/Draft Only)

## Description

Deliver finance analysis workflows with strict source-linking and non-execution constraints: ingest financial data, generate draft analyses, and block all autonomous financial transactions.

## Acceptance Criteria

- [ ] Finance ingestion adapters (CSV/XLSX/PDF) produce source-linked artifacts
- [ ] Every financial statement/metric in outputs is traceable to source references
- [ ] Transactional actions are blocked by policy in v1
- [ ] Draft reports include confidence + missing-data flags
- [ ] Tests verify no finance write path is executable

## Scope

### In scope
- Read, parse, normalize, and analyze financial inputs
- Draft-only investment/accounting summaries

### Out of scope
- Trade execution, payment execution, or account mutation

## Dependencies

- TASK-P2-001 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_phase3_finance_pack.py`
2. `uv run pytest --cov`
3. `uv run ruff check .`
4. `uv run mypy .`

## Estimated Size

M

## Governance Classification

- risk_level: high
- council_required: yes
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - Any path that can execute financial transactions
  - Output without source references for material claims
- reclassification_required_after_diff: yes
- planner_rationale: Financial domain requires strict safety and explainability guarantees.
