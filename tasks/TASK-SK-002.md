# TASK-SK-002: Skill/Playbook Manifest System

## Description

Implement discoverable, registrable skill/playbook manifests with typed input/output schema references, required tools, and policy requirements.

## Acceptance Criteria

- [ ] Create `agent_framework/skills/` models, loader, and service
- [ ] Support filesystem discovery from `skills/<name>/manifest.yaml`
- [ ] Validate required fields: instructions, constraints, templates, examples, tools, policies, typed I/O refs
- [ ] Register skills through `SkillRegistry` only
- [ ] Skill execution requests fail if required policies/tools are not granted

## Scope

### In scope
- Skill manifest schema + loader + registry integration
- First skill skeleton: `skills/plan_feature/*`

### Out of scope
- Multi-agent orchestration
- Domain-specific implementation skills beyond `plan_feature`

## Dependencies

- TASK-SK-001 must be complete

## Validation Steps

1. `uv run pytest tests/plugin/test_skill_registry.py`
2. `uv run ruff check .`
3. `uv run mypy .`

## Estimated Size

L

## Governance Classification

- risk_level: medium
- council_required: no
- human_approval_required: yes
- human_approval_stage: before_merge
- risk_triggers:
  - Skill manifest accepts undeclared tool/policy requirements
  - Skill bypasses registry and policy layer
- reclassification_required_after_diff: yes
- planner_rationale: Introduces reusable execution primitives with potential policy bypass risk if incorrect.
