# TASK-P0-012: Startup Sequence

## Description

Implement deterministic boot flow that ties together all Phase 0 components. On startup: load manifests -> validate compatibility -> resolve dependencies -> register contributions -> run lifecycle hooks -> health check -> expose runtime.

## Acceptance Criteria

- [ ] `main.py` startup event orchestrates the full boot sequence
- [ ] Manifests loaded from configured plugins directory
- [ ] Compatibility checked for each plugin
- [ ] Dependencies resolved and activation order determined
- [ ] Contributions registered in correct order
- [ ] Lifecycle `install` + `enable` hooks called per plugin
- [ ] Health check endpoint reflects plugin status
- [ ] Broken/incompatible plugin degrades cleanly (logged, skipped, does not crash boot)
- [ ] Startup logs show activation order and any skipped plugins
- [ ] Tests with healthy plugins, broken plugin, and empty plugins directory
- [ ] 80%+ coverage on new code

## Scope

### In scope
- `main.py` updates — startup event integration
- Bootstrap service that wires all components
- Health endpoint enhancement (show loaded plugins)
- Integration tests with test plugin fixtures

### Out of scope
- Production-grade error recovery
- Admin API for runtime plugin management
- Hot-reload

## Dependencies

- TASK-P0-002 through TASK-P0-011 (all prior Phase 0 tasks)

## Validation Steps

1. `uv run pytest` — full test suite passes
2. `uv run ruff check .` — lint clean
3. `uv run mypy .` — type check clean
4. `uv run pytest --cov` — 80%+ overall coverage
5. Manual: `uv run uvicorn agent_framework.main:app` boots cleanly with test plugins

## Estimated Size

L

## Governance Classification

- risk_level: low
- council_required: no
- human_approval_required: no
- human_approval_stage: none
- risk_triggers:
  - Integration of all components — bugs here surface as boot failures (mitigated by integration tests)
  - Changes to main.py affect the application entry point
- reclassification_required_after_diff: yes
- planner_rationale: Wiring existing components together. No new external calls, no new security boundaries. All component contracts are already defined and tested individually. Integration tests catch wiring bugs.
