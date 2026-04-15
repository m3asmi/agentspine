# TASK-P1-001: Personal Pack MVP (Telegram + Local Knowledge)

## Description

Deliver the first usable personal-assistant flow on top of the Phase 0 kernel: Telegram channel adapter, local knowledge ingestion/retrieval, and policy-gated side effects with audit traces.

## Acceptance Criteria

- [ ] Telegram inbound/outbound adapter integrated through `ChannelRegistry`
- [ ] Local knowledge ingestion path implemented via typed `IngestionExtension`
- [ ] Session + persistent memory paths available through memory provider abstraction
- [ ] All write/edit operations route through policy + approval checks
- [ ] End-to-end test: Telegram message → retrieval/context injection → response + audit events

## Scope

### In scope
- Single-user local-first operation
- Obsidian/local document read workflows
- Approval-gated note edits

### Out of scope
- WhatsApp integration
- Multi-user support
- Cloud-only dependencies

## Dependencies

- TASK-P0-012 must be complete

## Validation Steps

1. `uv run pytest tests/integration/test_phase1_personal_pack.py`
2. `uv run pytest --cov`
3. `uv run ruff check .`
4. `uv run mypy .`

## Estimated Size

L

## Governance Classification

- risk_level: medium
- council_required: no
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - File edits through assistant without policy gate
  - Channel actions bypassing dispatcher
- reclassification_required_after_diff: yes
- planner_rationale: Introduces user-facing channel and write-capable flows; requires enforced approval boundaries.
