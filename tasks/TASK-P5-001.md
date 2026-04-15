# TASK-P5-001: Plugin SDK Hardening + Internal Ecosystem Readiness

## Description

Stabilize plugin authoring workflows: SDK docs, templates, settings contributions, migration hooks, contract tests, and deterministic plugin validation pipeline.

## Acceptance Criteria

- [ ] Plugin SDK template for each extension type available
- [ ] Manifest semantic-version checks + migration hook contracts validated
- [ ] Contract test harness for plugins published in-repo
- [ ] Settings contribution validation and conflict detection implemented
- [ ] Documentation sufficient for internal team to build a plugin without core edits

## Scope

### In scope
- Internal ecosystem readiness and quality gates
- Backward-compatibility guarantees for public contracts

### Out of scope
- Public marketplace and signing infrastructure

## Dependencies

- TASK-P4-001 must be complete

## Validation Steps

1. `uv run pytest tests/plugin/`
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
  - Breaking public platform_api interfaces without migration path
  - Undocumented plugin behavior changes
- reclassification_required_after_diff: yes
- planner_rationale: Platform stability work with moderate ecosystem impact and low runtime side-effect risk.
