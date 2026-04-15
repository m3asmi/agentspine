# Runtime Topology

## High-level topology

```text
Channel Adapter
   |
   v
Control Plane
   |
   +--> Policy Engine
   +--> Approval Service
   +--> Capability Registry
   +--> LLM Gateway
   +--> Graph Runtime
   +--> Audit Service
   +--> Execution Dispatcher
             |
             v
      Host Execution Worker
             |
             +--> Workspace Manager
             +--> Shell Runner
             +--> Filesystem Adapter
             +--> Git Adapter
             +--> Odoo Adapter
             +--> Obsidian Adapter
             +--> Media Processors
             +--> Patch Builder

PostgreSQL + pgvector
Langfuse
Ollama
Optional OpenAI-compatible remote endpoint
```

## Control plane responsibilities

- receive normalized user/system events
- load session state
- evaluate policies
- execute graph workflows
- interrupt for approvals
- dispatch work to the execution plane
- record audit and provider events
- return structured outputs

## Execution plane responsibilities

- run shell commands
- manage workspaces
- read/write files within policy grants
- run tests
- generate patches and artifacts
- process files, images, and voice

## Persistence responsibilities

- framework config and plugin metadata
- runtime state and checkpoints
- memory scopes
- audit events
- knowledge metadata
- embedding metadata

## Observability responsibilities

- request traces
- tool traces
- LLM provider traces
- latency metrics
- failure metrics
- prompt versions

