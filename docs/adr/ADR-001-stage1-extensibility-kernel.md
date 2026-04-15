# ADR-001 — Stage 1 Extensibility-First Framework Kernel

## Status

Accepted.

## Context

The project needs a local-first framework that starts as a personal system but can evolve into a broader extensible agent platform.

The architecture must support:

- plugin-ready modularity from day 1
- controlled shell and filesystem execution
- patch-only engineering workflows
- read-only finance workflows
- Telegram as the first channel
- Odoo 19 integration through a modern adapter path
- local LLM usage through Ollama
- optional fallback or comparison through OpenAI-compatible providers
- approval and auditability
- future internal and external extensibility

The main risk is not scale. It is uncontrolled coupling between orchestration, tools, permissions, runtime execution, and future extension logic.

## Decision

Build a Stage 1 framework kernel with:

- one stable platform API for extensions
- one internal runtime implementation
- a plugin manifest system as the source of truth
- typed contribution points
- lifecycle-managed extensions
- version and compatibility enforcement
- permission enforcement per extension
- executor profiles managed by the kernel
- audited runtime actions
- a provider-agnostic LLM gateway

The framework must expose only a small public extension surface. Plugins must not depend on internal runtime modules.

## Consequences

### Positive

- clean extension boundary
- lower refactor cost later
- easier isolation of domain logic
- internal ecosystem possible without rewriting the core
- future path toward VS Code/Odoo-style platform behavior

### Negative

- more up-front design work
- more boilerplate for plugins
- stricter loading and compatibility checks
- slower early prototyping than ad hoc modules

## Decision rules

- all extension behavior must be declarative first
- plugin manifests are mandatory
- contributions must go through registries
- permissions are deny-by-default
- shell and write access must be policy-controlled
- provider switching must be infra-level, not ad hoc
- public API changes require versioning and deprecation policy

## Out of scope for Stage 1

- public plugin marketplace
- plugin signing
- untrusted third-party code execution
- dynamic production hot-reload
- full multi-tenant extension cloud

