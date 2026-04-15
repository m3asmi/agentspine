# TASK-DOC-001: Harden Plugin Manifest Spec

## Description

Expand `docs/specs/plugin-manifest-v1.md` from a minimal contract into an execution-ready specification with valid/invalid examples, explicit validation behavior, and version migration semantics.

## Assumptions

- Runtime manifest validator behavior remains unchanged in this task (documentation-only scope).
- Existing v1 field names remain canonical unless explicitly marked deprecated.
- Migration hooks are described as policy, not implemented as executable code in this task.

## Acceptance Criteria

- [ ] Add one complete valid manifest example covering required and optional fields.
- [ ] Add at least two invalid examples with expected error code/message patterns.
- [ ] Add version migration policy covering `breaking_change`, `migration_hook`, and deprecation window.
- [ ] Add section-level verification guidance that maps spec rules to future tests.
- [ ] Ensure examples align with `docs/templates/plugin-manifest.example.yaml` conventions.

## Scope

### In scope
- `docs/specs/plugin-manifest-v1.md`
- Optional doc link alignment in `docs/README.md` if needed for discoverability

### Out of scope
- Runtime schema/model changes in `src/`
- Backward-compatibility enforcement implementation

## Dependencies

- None

## Validation Steps

1. Verify rendered markdown structure and links in updated spec.
2. `uv run ruff check .` — no regression from incidental edits.
3. `uv run mypy .` — no regression in repository baseline.
4. `uv run pytest -q` — baseline tests remain green.

## Estimated Size

S

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Misstated manifest rule could create implementation drift across plugins.
  - Ambiguous migration policy could cause incompatible extension behavior later.
- reclassification_required_after_diff: yes
- planner_rationale: Documentation-only change with no direct runtime/data/security impact; risk is limited to requirement clarity.
