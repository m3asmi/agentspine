# TASK-P2-001: Odoo 19 Engineering Pack (JSON-2)

## Description

Implement Odoo 19 integration as a typed capability/domain pack using JSON-2 HTTP APIs, with strict read/analyze/draft boundaries and auditable execution.

## Acceptance Criteria

- [ ] Odoo client uses JSON-2 HTTP path (no XML-RPC/JSON-RPC as primary path)
- [ ] Typed capability contracts for Odoo read/analyze/draft actions
- [ ] Policy classifies Odoo mutations as high-risk and approval-gated
- [ ] Integration tests cover auth, pagination, error mapping, and audit events
- [ ] Engineering flows remain patch-artifact based (no direct live repo writes)

## Scope

### In scope
- Odoo model reads, diagnostics, and draft outputs
- Typed request/response schemas + retries/timeouts

### Out of scope
- Autonomous production writes to Odoo business data
- Cross-tenant Odoo orchestration

## Dependencies

- TASK-P1-001 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_phase2_odoo_json2.py`
2. `uv run ruff check .`
3. `uv run mypy .`

## Estimated Size

L

## Governance Classification

- risk_level: high
- council_required: yes
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - Odoo business write capability exposed without explicit approval policy
  - Untyped payload passthrough to external ERP
- reclassification_required_after_diff: yes
- planner_rationale: External enterprise-system integration with operational impact requires highest governance.
