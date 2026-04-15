# TASK-P0-003: Manifest Schema and Loader

## Description

Define the plugin manifest model with Pydantic and implement manifest discovery from a local plugins directory. Validate required fields and contribution payload structure. Invalid manifests must fail with actionable errors.

## Acceptance Criteria

- [ ] Pydantic manifest model covering: plugin metadata, api_version, framework_range, dependencies, contributions, permissions, settings_schema
- [ ] Manifest loader discovers YAML files from a configurable plugins directory
- [ ] Validation rejects missing/malformed fields with clear error messages
- [ ] Valid manifest normalizes into a typed object usable by registries
- [ ] Tests with valid, invalid, and edge-case manifests
- [ ] 80%+ coverage on new code

## Scope

### In scope
- `plugins/manifest.py` — Pydantic models
- `plugins/loader.py` — discovery and parsing
- `plugins/errors.py` — manifest-specific exceptions
- Test fixtures with example manifests (valid + invalid)

### Out of scope
- Registry registration (P0-006)
- Compatibility checking (P0-004)
- Dependency resolution (P0-005)

## Dependencies

- TASK-P0-002 — extension types referenced in contribution declarations

## Validation Steps

1. `uv run pytest tests/test_plugins/` — unit tests pass
2. `uv run ruff check src/agent_framework/plugins/` — lint clean
3. `uv run mypy src/agent_framework/plugins/` — type check clean

## Estimated Size

M

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Schema changes after manifests exist in the wild (not applicable yet)
- reclassification_required_after_diff: yes
- planner_rationale: Internal validation logic with no external calls. Schema-first design with Pydantic. No auth, no data boundaries, no external side effects.
