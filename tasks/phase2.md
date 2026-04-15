# Phase 2 — Odoo 19 Integration and Engineering Pack

## Goal

Add Odoo 19 support with JSON-2 and deliver the engineering-focused Odoo pack.

## Deliverables

- Odoo JSON-2 adapter
- Odoo business read capabilities
- Odoo engineering domain pack
- addon analysis workflows
- OCA comparison workflow
- patch generation workflow

## Non-goals

- finance posting
- repo auto-commit
- RPC as primary integration path

## Tasks

### P2-001 Odoo JSON-2 adapter
- [ ] Implement Odoo 19 JSON-2 transport using `httpx`
- [ ] Add auth/session config and typed request wrappers
- [ ] Acceptance:
  - [ ] adapter reads basic model records from a configured test instance
  - [ ] transport errors are normalized

### P2-002 Odoo permission scopes
- [ ] Define Odoo permission schema by model and operation
- [ ] Enforce read-only default in v1
- [ ] Acceptance:
  - [ ] unauthorized model access is denied before network call

### P2-003 Odoo business read capabilities
- [ ] Add capabilities for record search, record read, field metadata read
- [ ] Acceptance:
  - [ ] each capability has typed input/output schema
  - [ ] each call is audited with model and method metadata

### P2-004 Odoo engineering domain pack
- [ ] Register domain pack for addon development tasks
- [ ] Bind graph templates for analysis and patch generation
- [ ] Acceptance:
  - [ ] engineering workflows are isolated from business read workflows

### P2-005 Repo inspection capabilities
- [ ] Add capabilities for addon manifest read, module tree scan, field usage scan, dependency map extraction
- [ ] Acceptance:
  - [ ] capabilities operate in approved repo paths only

### P2-006 OCA comparison workflow
- [ ] Compare custom addon structure against OCA counterpart
- [ ] Produce structured diff findings report
- [ ] Acceptance:
  - [ ] workflow emits artifact bundle with comparison summary and raw diff refs

### P2-007 Patch generation workflow
- [ ] Generate patch artifacts in workspace only
- [ ] Never commit or push
- [ ] Acceptance:
  - [ ] output is unified diff + changed file bundle + test report

### P2-008 Odoo test runner integration
- [ ] Add workspace execution profile for lint/test/dev commands
- [ ] Acceptance:
  - [ ] tests run only in workspace
  - [ ] command profile is audited

### P2-009 Odoo engineering retrieval namespaces
- [ ] Add separate namespaces for custom addons and OCA addons
- [ ] Acceptance:
  - [ ] retrieval does not mix sources silently

### P2-010 Odoo pack tests
- [ ] Add adapter tests, permission tests, workflow tests, patch generation tests
- [ ] Acceptance:
  - [ ] green suite for Odoo read and engineering flows

## Exit gate

- JSON-2 adapter works
- engineering pack can inspect addons
- patch generation works in workspace only
- no repo live mutations occur
