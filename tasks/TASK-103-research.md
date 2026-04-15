---
contract_version: v2
artifact_type: research
task_id: TASK-103
timestamp: "2026-04-15"
---

## Summary
- Research for `cognee_adapter` as secondary memory backend under the same adapter contract.

## Evidence
- PyPI registry confirms `cognee` package availability.
- No existing cognee integration in repository.
- Runtime boundary rule requires adapter encapsulation and auditability of side effects.

## Decisions
### Recommended Approach
**Approach A — Use cognee as primary adapter and pgvector as fallback**
- Pros: leverage richer semantic memory engine first.
- Cons: increases dependency on external behavior and startup complexity.

**Approach B — Keep cognee as optional/secondary adapter with strict contract parity (selected)**
- Pros: preserves local-first baseline via native pgvector, limits blast radius if cognee misbehaves.
- Cons: requires adapter-selection policy and consistency checks.

**Selected:** Approach B to maintain deterministic baseline while enabling richer memory features.

## Metadata
- external implementation discovery via `gh` could not run (`gh` missing)
- key risk theme: adapter parity + fallback determinism
