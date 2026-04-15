# Phase 5 — Plugin SDK Hardening and Internal Ecosystem Readiness

## Goal

Turn the Stage 1 kernel into a reliable internal extension platform.

## Deliverables

- plugin SDK docs
- plugin template package
- migration runner
- health manager
- settings manager
- internal package install flow
- compatibility test kit

## Non-goals

- public extension registry
- untrusted third-party installs

## Tasks

### P5-001 Settings manager
- [ ] Implement namespaced plugin settings with JSON Schema validation
- [ ] Acceptance:
  - [ ] invalid settings cannot be stored

### P5-002 Migration runner
- [ ] Implement plugin migration execution with version tracking and idempotency
- [ ] Acceptance:
  - [ ] failed migration blocks upgrade and records audit event

### P5-003 Health manager
- [ ] Poll and aggregate plugin health checks
- [ ] Acceptance:
  - [ ] plugin health is visible in registry and UI

### P5-004 Plugin template generator
- [ ] Create a template for new plugins with manifest, interfaces, tests, and docs
- [ ] Acceptance:
  - [ ] new internal plugin can be scaffolded without copying random files

### P5-005 Compatibility test kit
- [ ] Add shared test helpers for manifest validation, lifecycle, permissions, and registry contributions
- [ ] Acceptance:
  - [ ] plugin authors can run a standard compliance suite

### P5-006 Internal install/update flow
- [ ] Define supported plugin package sources: local path, internal git repo, internal package index
- [ ] Acceptance:
  - [ ] plugin installation follows lifecycle manager and compatibility checks

### P5-007 SDK documentation
- [ ] Write developer docs for extension types, manifests, permissions, and testing
- [ ] Acceptance:
  - [ ] internal contributor can build a new plugin using docs only

### P5-008 Ecosystem regression tests
- [ ] Add tests for cross-plugin interactions and dependency upgrades
- [ ] Acceptance:
  - [ ] no broken dependency upgrade path in core first-party plugins

## Exit gate

- internal plugin authoring is repeatable
- migration flow is safe
- compatibility suite exists
