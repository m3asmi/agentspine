# Stage 1 Kernel Overview

## Goal

Provide a stable extensibility kernel for internal plugins.

## Main layers

- platform API
- registries
- lifecycle manager
- compatibility validator
- permission enforcer
- orchestration runtime
- execution worker
- LLM gateway
- audit service

## Runtime topology

```text
Telegram -> FastAPI -> Policy Engine -> LangGraph -> Capability Registry -> Execution Worker
                                                                 -> LLM Gateway -> Ollama / OpenAI-compatible

PostgreSQL <- state / memory / audit / metadata
Langfuse   <- traces / prompts / eval hooks
```

## Stage 1 success condition

A new plugin can be added, enabled, disabled, upgraded, and audited without editing kernel internals.
