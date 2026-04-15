---
contract_version: v2
artifact_type: research
task_id: TASK-101
timestamp: "2026-04-15"
---

## Summary
- Research for foundation pattern: `MemoryCapabilityExtension` with pluggable adapters.
- Goal: choose a safe decomposition that keeps adapter implementations isolated.

## Evidence
- Codebase patterns: `src/agent_framework/memory/`, `src/agent_framework/adapters/`, `src/agent_framework/platform_api/extensions/`, and `src/agent_framework/registries/` are mostly skeletons.
- No existing `MemoryCapabilityExtension` found in repository search.
- Specs reviewed: `docs/specs/tech-stack-lock-v1.md`, `plugin-manifest-v1.md`, `contribution-points-v1.md`, `capability-contract-v1.md`.
- Registry check: PyPI packages available (`cognee`, `pgvector`, `psycopg`).
- Existing implementation check via `gh search code`: unavailable in this environment (`gh` not installed).

## Decisions
### Recommended Approach
**Approach A — Direct dual-adapter coupling inside extension**
- Pros: fast initial delivery, fewer files.
- Cons: high coupling, harder testing, harder fallback evolution.

**Approach B — Adapter protocol + extension orchestrator (selected)**
- Pros: clean runtime boundaries, adapter-level tests, easier fallback policy changes.
- Cons: extra abstraction and boilerplate.

**Selected:** Approach B, because plugin-ready extension boundaries are a core architecture constraint and reduce lock-in risk.

## Metadata
- graphify report: N/A (no `graphify-out/GRAPH_REPORT.md` present)
- scope class: non-trivial, multi-step
- output artifact: planning only (no implementation)
