# TASK-SK-007: Browser + Sheets/Docs Artifact Tool Adapters

## Description

Implement controlled browser automation and spreadsheet/document/report adapters as isolated tool modules with strict policy gates.

## Acceptance Criteria

- [ ] Add browser adapter with allowlist domains, read-only default, screenshot/DOM extraction, audited interactions
- [ ] Add policy gate for mutating browser actions
- [ ] Add sheets/docs/report adapter contracts and emitters
- [ ] Ensure adapters are invoked via capability contracts, not direct orchestration calls
- [ ] Integration tests validate modularity + guardrail behavior

## Scope

### In scope
- Browser adapter + policy hooks
- Spreadsheet/doc/report adapter interfaces and base implementations

### Out of scope
- Full E2E web test framework or advanced BI/reporting suite

## Dependencies

- TASK-SK-006 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_browser_and_artifact_adapters.py`
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
  - Browser mutation allowed without approval gate
  - Network/domain access outside allowlist
- reclassification_required_after_diff: yes
- planner_rationale: Networked interaction tooling can create external side effects if not tightly controlled.
