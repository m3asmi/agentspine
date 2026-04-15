---
contract_version: v2
artifact_type: research
task_id: TASK-102
timestamp: "2026-04-15"
---

## Summary
- Research for `native_pgvector_adapter` implementation path.
- Focus: schema-safe persistence and retrieval behavior compatible with local-first runtime.

## Evidence
- Tech stack lock includes PostgreSQL + pgvector + Psycopg 3.
- Environment notes indicate pgvector extension is expected in local DB.
- Existing code has no concrete memory adapter implementation.

## Decisions
### Recommended Approach
**Approach A — SQLAlchemy ORM-first adapter**
- Pros: unified ORM patterns.
- Cons: higher setup overhead for vector operators; may obscure explicit SQL performance paths.

**Approach B — Psycopg + explicit SQL with pgvector operators (selected)**
- Pros: clear query control, easier debugging of vector distance and metadata filters.
- Cons: more manual SQL and mapping code.

**Selected:** Approach B for predictable pgvector behavior and tight control over retrieval semantics.

## Metadata
- existing implementation search: no in-repo candidate
- external registry signal: `pgvector`, `psycopg` packages available
- task risk driver: database schema/migration + retrieval correctness
