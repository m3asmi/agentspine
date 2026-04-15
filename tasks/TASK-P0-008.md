# TASK-P0-008: Permission Model and Executor Profiles

## Description

Define the permission schema and deny-by-default enforcement. Plugins declare required permissions in their manifest; the kernel grants or denies at activation. Define executor profiles that bound what a capability invocation can do at runtime.

## Acceptance Criteria

- [ ] Permission schema: resource, action, scope (Pydantic model)
- [ ] Deny-by-default: undeclared permissions are rejected at runtime
- [ ] Permission validator: checks requested permissions against granted set
- [ ] Four executor profiles defined: `read_only`, `workspace_safe`, `workspace_dev`, `bounded_live_write`
- [ ] Profile resolution: capability -> manifest permissions -> executor profile
- [ ] Plugin cannot request permissions not declared in its manifest
- [ ] Tests: grant/deny scenarios, profile resolution, undeclared access rejection
- [ ] 80%+ coverage on new code

## Scope

### In scope
- `policy/permissions.py` — permission models and schema
- `policy/profiles.py` — executor profile definitions
- `policy/enforcer.py` — runtime permission check
- `execution/profiles.py` — profile resolution logic

### Out of scope
- Policy engine rules (Phase 4)
- Admin UI for permission management
- Runtime sandbox enforcement

## Dependencies

- TASK-P0-003 — manifest model declares permissions

## Validation Steps

1. `uv run pytest tests/test_policy/` — unit tests pass
2. `uv run ruff check src/agent_framework/policy/` — lint clean
3. `uv run mypy src/agent_framework/policy/` — type check clean

## Estimated Size

M

## Governance Classification

- risk_level: medium
- council_required: no
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - Establishes the security boundary for the entire plugin system
  - Incorrect deny-by-default could silently allow unauthorized access
  - Executor profile definitions constrain all future capability execution
- reclassification_required_after_diff: yes
- planner_rationale: This task defines the permission model that all subsequent phases depend on for security. While the code is internal with no external calls, getting deny-by-default wrong would propagate as a security flaw through the entire system. Human review of the permission schema design is warranted.
