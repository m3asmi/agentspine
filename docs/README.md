# Development Documentation Pack

This documentation pack defines the Stage 1 framework architecture for a local-first, extensible AI agent kernel.

## Purpose

These documents are intended to be added directly to the project repository as the baseline engineering documentation for implementation.

## Scope

The framework is designed for:

- personal assistant workflows
- finance analysis workflows
- Odoo engineering and business workflows
- local-first execution
- plugin-ready extensibility
- provider-agnostic LLM routing
- approval and auditability

## Core design goals

- modular kernel
- stable extension boundary
- typed contribution points
- lifecycle-managed plugins
- policy-driven execution
- auditable runtime behavior
- future migration toward a broader ecosystem model

## Suggested repository placement

```text
/docs
  /adr
  /architecture
  /specs
  /development
  /templates
```

## Reading order

1. `adr/ADR-001-stage1-extensibility-kernel.md`
2. `architecture/00-overview.md`
3. `architecture/01-runtime-topology.md`
4. `architecture/02-plugin-system.md`
5. `specs/plugin-manifest-v1.md`
6. `specs/contribution-points-v1.md`
7. `specs/capability-contract-v1.md`
8. `specs/permissions-and-executor-profiles-v1.md`
9. `specs/lifecycle-and-compatibility-v1.md`
10. `development/build-order.md`

## Document map

### ADR
- architecture decision record for the Stage 1 kernel

### Architecture
- system shape
- runtime topology
- plugin system
- provider gateway
- execution and safety model
- memory, knowledge, audit

### Specs
- manifest schema
- contribution points
- capability contract
- lifecycle and compatibility rules
- settings/config model
- approval/risk matrix
- permissions and executor profiles

### Development
- environment setup (install guide, service status, .env reference)
- repository structure
- build order
- testing strategy

### Templates
- plugin manifest example
- plugin implementation checklist

## Non-goals for this pack

- public marketplace design
- multi-tenant SaaS architecture
- production deployment runbooks
- low-level code implementation

