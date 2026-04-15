# Phase 1 — Personal Pack and Local Knowledge Workflows

## Goal

Deliver a usable personal assistant pack on top of the kernel.

## Deliverables

- personal domain pack
- filesystem read capabilities
- Obsidian ingestion and retrieval
- append-only note workflow
- edit-after-approval workflow
- file/image/voice ingestion pipeline
- Telegram channel baseline

## Non-goals

- Odoo business actions
- finance writes
- public plugin ecosystem

## Tasks

### P1-001 Telegram channel plugin
- [ ] Implement Telegram channel extension
- [ ] Normalize inbound text, file, image, and voice events
- [ ] Support basic outbound replies and approval prompts
- [ ] Acceptance:
  - [ ] text and file messages reach orchestration layer
  - [ ] outbound messages are templated through renderer path

### P1-002 Personal domain pack
- [ ] Register personal subgraph
- [ ] Add domain commands and retrieval namespace bindings
- [ ] Acceptance:
  - [ ] domain pack loads through manifest only
  - [ ] graph entrypoints are visible in registry

### P1-003 Filesystem capability plugin
- [ ] Add safe filesystem read capabilities
- [ ] Support directory listing, file read, metadata read
- [ ] Enforce approved path scopes
- [ ] Acceptance:
  - [ ] reads outside allowed scope are blocked
  - [ ] audit event includes resolved path and plugin id

### P1-004 Obsidian ingestion plugin
- [ ] Add markdown vault ingestion
- [ ] Extract metadata, backlinks, tags, and headings
- [ ] Store chunk metadata for retrieval
- [ ] Acceptance:
  - [ ] vault index can be rebuilt
  - [ ] namespaces separate notes from general docs

### P1-005 Retrieval service for personal namespaces
- [ ] Build retrieval flow using pgvector + metadata filters
- [ ] Add lexical fallback if vector search is empty
- [ ] Acceptance:
  - [ ] top-k results include source metadata
  - [ ] citations are reconstructable from stored metadata

### P1-006 Append-only note capability
- [ ] Create append-to-note capability for approved folders only
- [ ] Add idempotency rule for duplicate append attempts
- [ ] Acceptance:
  - [ ] existing content is not deleted or replaced
  - [ ] note append is policy-controlled and audited

### P1-007 Edit-after-approval note workflow
- [ ] Create proposed-edit workflow
- [ ] Generate diff and require explicit approval before applying
- [ ] Acceptance:
  - [ ] no edit occurs before approval
  - [ ] approval record links to file diff artifact

### P1-008 Media ingestion plugins
- [ ] Add file, image, and voice ingestion contribution points
- [ ] Store normalized artifact metadata
- [ ] Acceptance:
  - [ ] Telegram uploads are converted into framework artifacts
  - [ ] unsupported MIME types fail cleanly

### P1-009 Personal memory scopes
- [ ] Implement thread memory, user preference memory, workspace memory for personal pack
- [ ] Acceptance:
  - [ ] memories are namespaced and retrievable
  - [ ] source-of-truth rule is documented and enforced

### P1-010 Personal pack tests
- [ ] Add integration tests for note append, approval edit, retrieval, and path scope denial
- [ ] Acceptance:
  - [ ] green integration suite for personal pack core workflows

## Exit gate

- Telegram ingress works
- Obsidian retrieval works
- append-only notes work
- approval edit flow works
- path boundaries are enforced
