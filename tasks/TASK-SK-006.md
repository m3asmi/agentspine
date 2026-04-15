# TASK-SK-006: Obsidian Connector + Docs Automation Adapters

## Description

Implement first-class Obsidian memory adapter and documentation automation adapter as modular tools, not core-coupled logic.

## Acceptance Criteria

- [ ] Add `memory/obsidian/` adapter interfaces for vault search + note create/update
- [ ] Enforce wikilink-aware write behavior and provenance metadata
- [ ] Add docs adapter primitives for OpenAPI/ADR/module-doc generation workflows
- [ ] Controlled write policies apply to both adapters
- [ ] Adapter actions are auditable

## Scope

### In scope
- Obsidian adapter contracts + minimal implementation
- Docs automation contracts + minimal implementation

### Out of scope
- Complete end-user UI for docs/knowledge management

## Dependencies

- TASK-SK-005 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_obsidian_docs_adapters.py`
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
  - Uncontrolled writes to vault/docs paths
  - Missing provenance for generated artifacts
- reclassification_required_after_diff: yes
- planner_rationale: Introduces write-capable adapters with policy-sensitive behavior.
