# TASK-P0-006: Registry Manager

## Description

Implement registries for all 10 contribution points. Each registry validates unique IDs, tracks source plugin, and provides lookup. Build a base registry class and concrete implementations.

## Acceptance Criteria

- [ ] `registries/base.py` — generic `Registry[T]` base class
- [ ] Concrete registries: Plugin, Capability, DomainPack, Channel, Policy, GraphNode, GraphTemplate, Renderer, Ingestion, Settings
- [ ] Unique ID validation — duplicate contribution IDs fail loudly
- [ ] Source-plugin tracking — every contribution knows its origin plugin
- [ ] Lookup by ID and by plugin source
- [ ] Deregistration support (for plugin disable/uninstall)
- [ ] Tests for register, lookup, duplicate rejection, deregistration
- [ ] 80%+ coverage on new code

## Scope

### In scope
- `registries/base.py` — generic typed registry
- `registries/*.py` — one file per registry or grouped logically
- `registries/__init__.py` — re-exports all registries

### Out of scope
- Lifecycle integration (P0-007)
- Manifest-driven auto-registration (P0-012)

## Dependencies

- TASK-P0-002 — extension types that registries hold

## Validation Steps

1. `uv run pytest tests/test_registries/` — unit tests pass
2. `uv run ruff check src/agent_framework/registries/` — lint clean
3. `uv run mypy src/agent_framework/registries/` — type check clean

## Estimated Size

M

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Registry corruption could affect all plugin operations (mitigated by immutable patterns and tests)
- reclassification_required_after_diff: yes
- planner_rationale: In-memory data structures with typed interfaces. No persistence, no external calls, no auth boundaries. Pure data management.
