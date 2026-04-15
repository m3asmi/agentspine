# TASK-103: Cognee Secondary Memory Adapter

## Description

Implement `cognee_adapter` as an optional/secondary memory backend that conforms to the shared adapter protocol, with deterministic initialization and error signaling to enable extension-level fallback routing.

## Acceptance Criteria

- [ ] `cognee_adapter` fully conforms to adapter protocol from TASK-101
- [ ] Initialization failure is explicit and does not crash orchestration flow
- [ ] Read/write responses maintain contract parity with native adapter shape
- [ ] Integration tests validate deterministic error-to-fallback signaling
- [ ] No provider-specific logic leaks outside adapter module

## Scope

### In scope
- `src/agent_framework/adapters/cognee_adapter.py`
- `src/agent_framework/adapters/cognee_client.py`
- `tests/integration/test_cognee_adapter_contract.py`

### Out of scope
- Direct changes to orchestration graph nodes
- Native pgvector schema/migration changes
- Channel-specific behavior changes

## Dependencies

- TASK-101 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_cognee_adapter_contract.py` — contract-parity behavior passes
2. `uv run ruff check .` — lint clean
3. `uv run ruff format --check .` — formatting clean
4. `uv run mypy .` — typing clean

## Estimated Size

M

## Governance Classification

- risk_level: medium
- council_required: no
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - Third-party dependency behavior can diverge from native adapter semantics
  - Fallback signaling bugs can break deterministic memory routing
- reclassification_required_after_diff: yes
- planner_rationale: Medium risk because external adapter integration affects reliability and fallback policy, though boundaries remain adapter-contained.
