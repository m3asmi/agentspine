---
contract_version: v2
artifact_type: task
task_id: TASK-103
risk_level: medium
council_required: no
human_approval_stages:
  - before_merge
dependencies:
  - TASK-101
parallelizable: false
parallel_group: ""
conflict_scope:
  - src/agent_framework/adapters/
  - src/agent_framework/memory/
  - tests/
integration_blockers:
  - "Requires stable adapter protocol from TASK-101"
  - "Must preserve local-first behavior when cognee is unavailable"
merge_strategy: sequential_only
risk_triggers:
  - "Third-party adapter dependency and runtime fallback policy"
  - "Potential divergence in retrieval semantics vs native adapter"
planner_rationale: "Medium risk due external dependency integration and workflow impact on retrieval routing."
model_overrides: {}
---

## Summary
Implement `cognee_adapter` conforming to the shared memory adapter protocol, including initialization, write/read operations, and deterministic failure/fallback signaling.

## Evidence
- `cognee` package is available but not yet integrated.
- Existing codebase has no adapter abstraction implementation to reuse.

## Decisions
- Treat cognee as optional adapter; do not bypass native path.
- Enforce strict contract parity with native adapter for returned data shape.
- Fail closed with auditable error events; extension decides fallback.

## Metadata
- target_files:
  - src/agent_framework/adapters/cognee_adapter.py
  - src/agent_framework/adapters/cognee_client.py
  - tests/integration/test_cognee_adapter_contract.py
- exclusions:
  - "No direct changes to orchestration graph nodes"
  - "No provider-specific logic outside adapter module"

## Impact Checklist
- database: none
- backend: add cognee adapter/client and contract-parity mapping
- frontend: none
- api_contracts: none
- infra_ci: none
- security: dependency boundary + controlled error handling for external adapter failures
- business_workflow: adapter selection/fallback behavior for memory retrieval

## Test Requirements
- required_behavior_to_test: "contract parity with native adapter, graceful initialization failure, deterministic error-to-fallback signaling."
- expected_regressions_to_prevent: "adapter-specific payload divergence, uncaught exceptions propagating to orchestration layer."
- edge_cases_to_cover: "cognee unavailable at startup, partial write failures, empty retrieval response, timeout handling."
