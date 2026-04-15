# TASK-P0-002: Platform API Interfaces

## Description

Define public base interfaces for all extension types in `platform_api/extensions/`. These are the stable contracts that plugins implement. No internal runtime details leak through these interfaces.

## Acceptance Criteria

- [ ] `platform_api/extensions/base.py` — `ExtensionBase` ABC with lifecycle hooks
- [ ] `platform_api/extensions/capability.py` — `CapabilityExtension` ABC
- [ ] `platform_api/extensions/domain_pack.py` — `DomainPackExtension` ABC
- [ ] `platform_api/extensions/channel.py` — `ChannelExtension` ABC
- [ ] `platform_api/extensions/policy.py` — `PolicyExtension` ABC
- [ ] `platform_api/extensions/ingestion.py` — `IngestionExtension` ABC
- [ ] `platform_api/extensions/renderer.py` — `RendererExtension` ABC
- [ ] All interfaces are typed (mypy strict passes)
- [ ] Docstrings on all public classes and methods
- [ ] No imports from internal runtime modules
- [ ] Tests verify interface contracts (instantiation, method signatures)
- [ ] 80%+ coverage on new code

## Scope

### In scope
- Abstract base classes for all 7 extension types
- Type-safe method signatures
- `platform_api/contracts/__init__.py` re-exports

### Out of scope
- Concrete implementations
- Registration logic
- Manifest integration

## Dependencies

- TASK-P0-001 (complete) — project skeleton exists

## Validation Steps

1. `uv run pytest tests/test_platform_api/` — unit tests pass
2. `uv run ruff check src/agent_framework/platform_api/` — lint clean
3. `uv run mypy src/agent_framework/platform_api/` — type check clean
4. Verify no imports from `agent_framework.registries`, `agent_framework.lifecycle`, etc.

## Estimated Size

M

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Interface change after plugins depend on it (not applicable yet — no plugins exist)
- reclassification_required_after_diff: yes
- planner_rationale: Pure interface definitions with no side effects, no external calls, no data access. Foundation for all later work but isolated to platform_api/ package.
