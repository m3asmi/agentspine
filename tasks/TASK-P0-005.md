# TASK-P0-005: Dependency Resolver

## Description

Implement plugin dependency resolution with topological sort. Handle required and optional dependencies. Detect and reject circular dependencies. Produce a sorted activation plan.

## Acceptance Criteria

- [ ] Dependency graph builder from manifest dependency declarations
- [ ] Topological sort produces activation order
- [ ] Circular dependencies detected and rejected with clear error (names the cycle)
- [ ] Missing required dependencies block activation
- [ ] Missing optional dependencies log warning but proceed
- [ ] Tests cover: linear chain, diamond, cycle, missing required, missing optional
- [ ] 80%+ coverage on new code

## Scope

### In scope
- `plugins/dependency_resolver.py` — graph + toposort
- `plugins/errors.py` — dependency-specific exceptions (extend from P0-003)

### Out of scope
- Actual plugin activation (P0-007)
- Version compatibility (P0-004)

## Dependencies

- TASK-P0-003 — manifest model provides dependency declarations

## Validation Steps

1. `uv run pytest tests/test_plugins/test_dependency_resolver.py` — unit tests pass
2. `uv run ruff check src/agent_framework/plugins/` — lint clean
3. `uv run mypy src/agent_framework/plugins/` — type check clean

## Estimated Size

S

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Incorrect resolution could activate plugins in wrong order (mitigated by tests)
- reclassification_required_after_diff: yes
- planner_rationale: Pure algorithm with no side effects. Graph traversal and sorting — well-understood computer science. No auth, no external calls, no data access.
