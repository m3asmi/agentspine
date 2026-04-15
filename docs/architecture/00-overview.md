# Architecture Overview

## Objective

Provide a plugin-ready framework kernel for agent workflows with clear boundaries between:

- platform API
- orchestration runtime
- policy enforcement
- execution worker
- knowledge and memory
- audit and observability
- provider routing

## Design model

The framework is split into two layers.

### Layer A — Stable Platform API

This is the only supported extension boundary.

It includes:

- extension base contracts
- manifest schema
- contribution point contracts
- settings and permission contracts
- lifecycle hook contracts

### Layer B — Internal Runtime

This is the implementation layer.

It includes:

- LangGraph orchestration
- execution dispatcher
- registries
- audit emitter
- provider gateway
- adapters
- persistence
- policy engine

## Stage 1 extension types

- Capability Extension
- Domain Pack Extension
- Channel Extension
- Policy Extension
- Ingestion Extension
- Renderer Extension

## Main kernel services

- ManifestLoader
- CompatibilityValidator
- DependencyResolver
- LifecycleManager
- RegistryManager
- PermissionEnforcer
- SettingsManager
- MigrationRunner
- HealthManager
- AuditEmitter
- ExecutionDispatcher
- LLMGateway
- GraphRuntime

## Key rule

Plugins depend on platform contracts.

Plugins do not import internal runtime modules.

