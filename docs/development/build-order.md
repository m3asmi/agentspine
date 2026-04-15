# Build Order

## Phase 0 — Kernel foundations

Build first:

- manifest schema
- extension base interfaces
- contribution point schemas
- manifest loader
- compatibility validator
- dependency resolver
- registry manager
- lifecycle manager
- permission enforcer
- audit emitter

## Phase 1 — Runtime integration

Build next:

- LangGraph integration
- execution dispatcher
- LLM gateway
- settings manager
- health manager
- migration runner

## Phase 2 — First-party core plugins

Build next:

- core.filesystem
- core.git
- core.telegram
- core.ollama
- core.openai_compat
- core.patch_builder
- core.pdf
- core.image
- core.voice

## Phase 3 — Domain packs

Build next:

- personal.pack
- odoo.engineering
- odoo.business
- finance.pack

## Phase 4 — Admin and operator surfaces

Build next:

- plugin management UI
- approval center
- provider profile management
- health dashboard
- audit views

