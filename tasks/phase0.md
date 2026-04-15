# Phase 0 — Kernel and Extensibility Primitives

## Goal

Build the Stage 1 platform kernel.

## Deliverables

- package skeleton
- manifest loader
- compatibility validator
- dependency resolver
- lifecycle manager
- permission enforcer
- core registries
- audit emitter
- LLM gateway skeleton
- execution dispatcher skeleton
- startup sequence

## Non-goals

- business features
- Odoo live integration
- finance analysis
- full admin UI

## Tasks

### P0-001 Project bootstrap
- [x] Create project package tree under `src/agent_framework/`
- [x] Add `pyproject.toml`, `.python-version`, `.env.example`, `.gitignore`
- [x] Add `tests/` package and base CI commands
- [x] Outputs: runnable package skeleton
- [x] Acceptance:
  - [x] `uv sync` works
  - [x] `pytest` runs with zero test failures
  - [x] package imports resolve

### P0-002 Platform API interfaces
- [ ] Define public base interfaces for all extension types
- [ ] Keep the API minimal and typed
- [ ] Outputs:
  - [ ] `platform_api/extensions/base.py`
  - [ ] `capability.py`
  - [ ] `domain_pack.py`
  - [ ] `channel.py`
  - [ ] `policy.py`
  - [ ] `ingestion.py`
  - [ ] `renderer.py`
- [ ] Acceptance:
  - [ ] interfaces are documented
  - [ ] no plugin code imports internal runtime modules

### P0-003 Manifest schema and loader
- [ ] Define manifest model with Pydantic
- [ ] Implement manifest discovery from local plugins directory
- [ ] Validate required fields and contribution payload structure
- [ ] Outputs:
  - [ ] manifest schema models
  - [ ] loader service
  - [ ] manifest validation tests
- [ ] Acceptance:
  - [ ] invalid manifest fails with actionable error
  - [ ] valid manifest is normalized into registry input

### P0-004 Compatibility validator
- [ ] Implement API version and framework range checks
- [ ] Reject incompatible plugins before activation
- [ ] Outputs:
  - [ ] compatibility service
  - [ ] semantic version helpers
- [ ] Acceptance:
  - [ ] incompatible version blocks load
  - [ ] test matrix covers supported and unsupported cases

### P0-005 Dependency resolver
- [ ] Add required and optional dependency handling
- [ ] Implement topological sort
- [ ] Detect circular dependencies
- [ ] Outputs:
  - [ ] dependency graph service
  - [ ] sorted activation plan
- [ ] Acceptance:
  - [ ] cycles are rejected
  - [ ] missing required deps block plugin activation

### P0-006 Registry manager
- [ ] Implement registries for all contribution points
- [ ] Add unique ID validation and source-plugin tracking
- [ ] Outputs:
  - [ ] registry base class
  - [ ] concrete registries
- [ ] Acceptance:
  - [ ] duplicate contribution IDs fail loudly
  - [ ] registries expose lookup by id and plugin source

### P0-007 Lifecycle manager
- [ ] Implement install, enable, disable, upgrade, uninstall hooks
- [ ] Add hook timeout handling and audit integration
- [ ] Outputs:
  - [ ] lifecycle service
  - [ ] hook runner
- [ ] Acceptance:
  - [ ] failed enable leaves plugin disabled
  - [ ] lifecycle events are audited

### P0-008 Permission model and executor profiles
- [ ] Define permission schema and deny-by-default behavior
- [ ] Define executor profiles: `read_only`, `workspace_safe`, `workspace_dev`, `bounded_live_write`
- [ ] Outputs:
  - [ ] permission models
  - [ ] permission validator
- [ ] Acceptance:
  - [ ] plugin cannot request undeclared access at runtime
  - [ ] executor profile resolution works

### P0-009 Audit emitter
- [ ] Define audit event model
- [ ] Add event emission hooks for plugin load, lifecycle, capability registration, and LLM calls
- [ ] Outputs:
  - [ ] audit models
  - [ ] audit emitter interface
- [ ] Acceptance:
  - [ ] every lifecycle action emits structured audit payload

### P0-010 LLM gateway skeleton
- [ ] Create provider profile model
- [ ] Create gateway interface for local and OpenAI-compatible calls
- [ ] Support routing modes: `local_only`, `remote_only`, `manual_compare`, `fallback_on_failure`, `fallback_on_low_confidence`
- [ ] Outputs:
  - [ ] `llm_gateway/` contracts and stub implementation
- [ ] Acceptance:
  - [ ] provider configuration validates
  - [ ] no orchestration node calls provider SDK directly

### P0-011 Execution dispatcher skeleton
- [ ] Create execution request/response models
- [ ] Define worker boundary contracts
- [ ] Outputs:
  - [ ] dispatcher interface
  - [ ] workspace request schema
- [ ] Acceptance:
  - [ ] capability can request execution without direct shell access in API process

### P0-012 Startup sequence
- [ ] Implement deterministic boot flow
- [ ] Load manifests -> validate -> resolve deps -> register -> health check -> expose runtime
- [ ] Outputs:
  - [ ] application bootstrap service
- [ ] Acceptance:
  - [ ] broken plugin degrades cleanly
  - [ ] startup logs show activation order

## Exit gate

- plugin discovery works
- manifest validation is enforced
- registries are live
- lifecycle hooks are tested
- audit events are emitted
- app boot is deterministic
