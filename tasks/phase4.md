# Phase 4 — Approvals, Admin UI, and Hardening

## Goal

Make the framework operationally safe and inspectable.

## Deliverables

- approval service
- admin UI baseline
- path grant management
- provider profile management
- plugin management UI
- richer audit views
- failure recovery improvements

## Non-goals

- public marketplace
- multi-tenant SaaS deployment

## Tasks

### P4-001 Approval service
- [ ] Implement approval request model, status transitions, and resume hooks for LangGraph
- [ ] Acceptance:
  - [ ] paused runs can resume from approval outcome

### P4-002 Telegram approval UX
- [ ] Implement approval cards and actions in Telegram
- [ ] Acceptance:
  - [ ] user can approve or reject pending actions from chat

### P4-003 Admin UI baseline
- [ ] Build minimal internal UI for runs, approvals, plugins, and grants
- [ ] Acceptance:
  - [ ] view pending approvals and recent runs

### P4-004 Path grant management
- [ ] Implement CRUD for approved path scopes and executor profiles
- [ ] Acceptance:
  - [ ] grants are auditable and revocable

### P4-005 Provider profile management
- [ ] Add config management for local and remote providers
- [ ] Acceptance:
  - [ ] provider switch requires config change, not code change

### P4-006 Plugin management UI
- [ ] Show plugin status, version, dependencies, and health
- [ ] Acceptance:
  - [ ] plugin can be enabled or disabled through controlled lifecycle path

### P4-007 Audit explorer
- [ ] Add searchable audit views by run, plugin, capability, approval, provider
- [ ] Acceptance:
  - [ ] operator can trace a side effect back to source plugin and request

### P4-008 Failure recovery
- [ ] Improve degraded plugin handling, startup resilience, and recovery messaging
- [ ] Acceptance:
  - [ ] broken optional plugin does not crash the framework

### P4-009 Hardening tests
- [ ] Add end-to-end tests for approval, resume, plugin disable, and degraded mode startup
- [ ] Acceptance:
  - [ ] green hardening suite

## Exit gate

- approvals are live
- admin UI covers core operations
- audit views are usable
- degraded mode behavior is acceptable
