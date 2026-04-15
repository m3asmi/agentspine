# TASK-DOC-002: Harden Capability Contract Spec

## Description

Expand `docs/specs/capability-contract-v1.md` with operational examples for risk tiers, side effects, audit event expectations, and permission mismatch behavior.

## Assumptions

- Risk tier definitions in `docs/security-policy.md` are the source of truth.
- Capability contract remains schema-first and provider-agnostic.
- Error payload examples are normative documentation, not an API implementation commitment beyond v1 scope.

## Acceptance Criteria

- [ ] Add concrete examples for `low`, `medium`, and `high` capability declarations.
- [ ] Add side-effect declaration examples and required audit event mapping.
- [ ] Add permission mismatch behavior with standard deny response shape.
- [ ] Add explicit boundary note: capabilities cannot bypass policy registry checks.
- [ ] Add verification references to likely test surfaces for future implementation.

## Scope

### In scope
- `docs/specs/capability-contract-v1.md`
- Cross-reference alignment with `docs/security-policy.md`

### Out of scope
- Executor/policy engine code changes
- New risk tier model introduction

## Dependencies

- TASK-DOC-001 (recommended first for terminology consistency)

## Validation Steps

1. Confirm risk-tier language matches `docs/security-policy.md`.
2. Confirm audit expectations align with `AGENTS.md` side-effect rule.
3. `uv run ruff check .` — no regression from incidental edits.
4. `uv run pytest -q` — baseline tests remain green.

## Estimated Size

S

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Inconsistent risk-tier wording can cause incorrect downstream task classification.
  - Missing audit-event examples can weaken enforceability of side-effect controls.
- reclassification_required_after_diff: yes
- planner_rationale: Documentation-only spec hardening; no auth, money, schema, or production runtime changes in this task.
