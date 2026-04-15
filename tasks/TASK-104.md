---
contract_version: v2
artifact_type: task
task_id: TASK-104
risk_level: medium
council_required: no
human_approval_stages:
  - before_merge
dependencies:
  - TASK-102
  - TASK-103
parallelizable: false
parallel_group: ""
conflict_scope:
  - src/agent_framework/memory/
  - src/agent_framework/plugins/
  - src/agent_framework/platform_api/contracts/
  - tests/
integration_blockers:
  - "Requires contract-compatible behavior from both adapters"
  - "Requires manifest and capability declarations aligned with specs"
merge_strategy: sequential_only
risk_triggers:
  - "Capability-level workflow routing affects memory behavior across packs"
  - "Incorrect manifest or permission declaration can bypass intended plugin governance"
planner_rationale: "Medium risk due business workflow impact and governance-critical contract and manifest integration."
model_overrides: {}
---

## Summary
Compose `MemoryCapabilityExtension` using `native_pgvector_adapter` and `cognee_adapter`, add strategy-based routing and fallback, and finalize plugin and capability declarations with integration tests.

## Evidence
- Manifest and capability specs define required declaration fields and deny-by-default permissions.
- Architecture requires auditable side effects and no provider-specific calls in orchestration nodes.

## Decisions
- Implement explicit routing strategy inside the extension only.
- Declare capability and plugin contributions in schema-first form.
- Add integration tests validating success, fallback, and both-adapters-unavailable behavior.

## Acceptance Criteria
- [ ] Extension routes through primary and fallback adapters using explicit strategy policy
- [ ] Capability declaration schema is added and plugin manifest contribution is valid
- [ ] Deny-by-default permissions are respected and no direct provider calls occur in orchestration nodes
- [ ] Audit events are emitted for read and write side effects across both adapter paths
- [ ] Integration tests cover success, fallback, and both-adapters-unavailable scenarios

## Metadata
- target_files:
  - src/agent_framework/memory/memory_capability_extension.py
  - src/agent_framework/plugins/memory_capability/manifest.yaml
  - src/agent_framework/platform_api/contracts/capabilities/memory_query.yaml
  - tests/integration/test_memory_capability_extension_dual_adapter.py
- exclusions:
  - "No Telegram/Odoo channel features"
  - "No unrelated plugin ecosystem changes"

## Impact Checklist
- database: none
- backend: extension routing policy and adapter orchestration
- frontend: none
- api_contracts: add new capability contract (non-breaking additive)
- infra_ci: none
- security: enforce deny-by-default permissions and side-effect audit mapping
- business_workflow: memory capability uses dual-adapter strategy with deterministic fallback

## Validation Steps
1. `uv run pytest tests/integration/test_memory_capability_extension_dual_adapter.py` - dual-adapter integration behavior passes
2. `uv run ruff check .` - lint clean
3. `uv run ruff format --check .` - formatting clean
4. `uv run mypy .` - typing clean

## Test Requirements
- required_behavior_to_test: "primary adapter success path, fallback on primary failure, and audit event emission for both read and write side effects."
- expected_regressions_to_prevent: "silent fallback loops, undeclared capability invocation, inconsistent response schema across adapter paths."
- edge_cases_to_cover: "both adapters unavailable, mismatched adapter payload schema, idempotent repeated requests, empty result with lexical fallback."
