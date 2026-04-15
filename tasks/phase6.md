# Phase 6 — Cloud Portability and SaaS-Prep Boundaries

## Goal

Prepare the framework for future cloud deployment without implementing full multi-tenancy yet.

## Deliverables

- deployment profiles
- config layering cleanup
- externalized secrets strategy
- worker/app split validation
- storage abstraction review
- future tenant boundary plan

## Non-goals

- full SaaS rollout
- marketplace
- public plugin execution service

## Tasks

### P6-001 Deployment profile review
- [ ] Define laptop, on-prem host, and cloud-ready deployment profiles
- [ ] Acceptance:
  - [ ] deployment assumptions are documented and testable

### P6-002 Config layering cleanup
- [ ] Separate framework defaults, plugin defaults, env overrides, and runtime overrides
- [ ] Acceptance:
  - [ ] config precedence is deterministic

### P6-003 Secret management abstraction
- [ ] Replace direct env access with secrets interface where needed
- [ ] Acceptance:
  - [ ] provider and Odoo secrets are not hardcoded in business logic

### P6-004 Worker/app boundary validation
- [ ] Ensure API app can remain stateless relative to workspace execution
- [ ] Acceptance:
  - [ ] execution contract is transport-agnostic

### P6-005 Storage abstraction review
- [ ] Review checkpoint, memory, audit, and vector dependencies for future portability
- [ ] Acceptance:
  - [ ] assumptions about local-only storage are documented

### P6-006 Future tenant boundary ADR
- [ ] Draft tenant boundary plan for users, workspaces, plugins, and audit scopes
- [ ] Acceptance:
  - [ ] no implementation required, but future cut points are explicit

### P6-007 Portability test set
- [ ] Add smoke tests for local vs containerized deployment profiles
- [ ] Acceptance:
  - [ ] core flows run in more than one deployment shape

## Exit gate

- framework is still single-tenant by implementation
- future cloud cut points are documented
- deployment model is portable enough for next stage
