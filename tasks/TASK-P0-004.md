# TASK-P0-004: Compatibility Validator

## Description

Implement API version and framework range checks. Reject incompatible plugins before activation. Uses semantic versioning to compare manifest-declared ranges against the running framework version.

## Acceptance Criteria

- [ ] Semantic version parser and comparator (or use `packaging` library)
- [ ] `compatibility/validator.py` — checks api_version and framework_range from manifest
- [ ] Incompatible version blocks plugin load with clear error message
- [ ] Test matrix covers: exact match, range match, too old, too new, malformed versions
- [ ] 80%+ coverage on new code

## Scope

### In scope
- `compatibility/validator.py` — version checking service
- `compatibility/version.py` — semver helpers (if not using `packaging`)
- Tests covering supported and unsupported version combinations

### Out of scope
- Dependency resolution (P0-005)
- Manifest loading (P0-003 handles that)

## Dependencies

- TASK-P0-003 — manifest model provides version fields to validate

## Validation Steps

1. `uv run pytest tests/test_compatibility/` — unit tests pass
2. `uv run ruff check src/agent_framework/compatibility/` — lint clean
3. `uv run mypy src/agent_framework/compatibility/` — type check clean

## Estimated Size

S

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Incorrect version logic could silently allow incompatible plugins (mitigated by test matrix)
- reclassification_required_after_diff: yes
- planner_rationale: Pure validation logic, no side effects, no external calls. Deterministic input/output with comprehensive test coverage.
