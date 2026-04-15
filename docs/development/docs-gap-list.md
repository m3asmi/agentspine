# Documentation Gap List (Targeted Hardening)

## Goal

Reduce implementation ambiguity without expanding docs into heavy process overhead.

## Priority Gaps

### 1) Plugin Manifest Spec Is Too Thin

- File: `docs/specs/plugin-manifest-v1.md`
- Add:
  - One complete valid manifest example (all required fields + optional fields)
  - Two invalid examples with expected validation errors
  - Version migration policy with `breaking_change`, `migration_hook`, `deprecation_window`
- Acceptance criteria:
  - A contributor can copy the valid example and pass schema validation on first try
  - Invalid examples map to explicit error messages

### 2) Capability Contract Needs Operational Examples

- File: `docs/specs/capability-contract-v1.md`
- Add:
  - Risk-tiered capability examples (`low`, `medium`, `high`)
  - Side-effect declaration examples and matching audit events
  - Permission mismatch behavior (deny + error payload shape)
- Acceptance criteria:
  - Capability authors can determine tier and side effects with no reviewer clarification
  - Reviewers can validate policy compliance from docs alone

### 3) Contribution Points Need Boundary Rules

- File: `docs/specs/contribution-points-v1.md`
- Add:
  - "Allowed imports" section for plugin code (`platform_api` only)
  - Startup registration order and failure behavior
  - Duplicate registration conflict resolution rule
- Acceptance criteria:
  - Plugin startup behavior is deterministic and testable
  - Boundary violations have a single documented failure mode

### 4) Tasks Need Definition-of-Done and Traceability

- Files: `tasks/phase*.md`, `tasks/TASK-*.md`
- Add:
  - Per-task DoD checklist: code, tests, docs, audit events, security checks
  - Traceability fields: `spec_refs`, `test_refs`, `review_refs`
- Acceptance criteria:
  - Every task points to specific spec sections and tests
  - Execution reports can be verified against acceptance criteria quickly

### 5) New Contributor Onboarding Is Fragmented

- Files: `README.md`, `docs/README.md`
- Add:
  - 10-minute "first task" quickstart
  - Required reading sequence with exact paths
  - First safe command sequence and expected outputs
- Acceptance criteria:
  - New contributor can complete one low-risk task without verbal guidance

## Ready-to-Use Templates

### A) Spec Section Template

```md
## <Section Name>

### Intent
<What this section guarantees>

### Rules
- <Normative rule>
- <Normative rule>

### Valid Example
```yaml
<example>
```

### Invalid Example
```yaml
<example>
```
- Error: `<expected_error_code>`
- Reason: <why invalid>

### Verification
- Test: `<path/to/test>`
- Command: `<validation command>`
```

### B) Task Definition-of-Done Template

```md
## Definition of Done
- [ ] Implementation matches acceptance criteria
- [ ] Unit/integration tests added or updated
- [ ] Audit events emitted for side effects
- [ ] Security checks completed for risk tier
- [ ] Execution report added: `reviews/EXEC-TASK-XXX.md`
```

### C) Traceability Block Template

```md
## Traceability
- spec_refs:
  - `docs/specs/<spec>.md#<section>`
- test_refs:
  - `tests/<path>.py::<test_name>`
- review_refs:
  - `reviews/EXEC-TASK-XXX.md`
```

### D) Quickstart Template (README)

```md
## Quickstart (First Safe Task)

1. Read:
   - `docs/specs/tech-stack-lock-v1.md`
   - `docs/specs/plugin-manifest-v1.md`
   - `tasks/README.md`
2. Run:
   - `uv sync`
   - `uv run pytest -q`
3. Pick:
   - One low-risk task from `tasks/index.md`
4. Validate:
   - `uv run ruff check .`
   - `uv run mypy .`
```

## Suggested Rollout Sequence

1. Update `plugin-manifest-v1.md` and `capability-contract-v1.md`
2. Add DoD + traceability to active task files
3. Add quickstart section in `README.md`
4. Add ADR index page in `docs/adr/`
