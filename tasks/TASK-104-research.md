---
contract_version: v2
artifact_type: research
task_id: TASK-104
timestamp: "2026-04-15"
---

## Summary
- Research for final composition: `MemoryCapabilityExtension` orchestrating `native_pgvector_adapter` + `cognee_adapter` through policy-driven selection.

## Evidence
- Contribution points and manifest spec require declared capabilities and permissions.
- Capability contract requires explicit input/output schema, risk tier, idempotency, and audit event type.
- Prior tasks establish adapter protocol and concrete backends.

## Decisions
### Recommended Approach
**Approach A — Hardcoded adapter precedence in extension logic**
- Pros: minimal config, quick ship.
- Cons: rigid behavior, harder environment-specific tuning.

**Approach B — Strategy-driven adapter router in extension (selected)**
- Pros: configurable precedence/fallback, easier policy enforcement and testing.
- Cons: additional settings validation logic.

**Selected:** Approach B for maintainability and explicit governance over side effects.

## Metadata
- primary integration dependency: TASK-102 + TASK-103 outputs
- risk focus: capability declaration correctness + audit completeness
