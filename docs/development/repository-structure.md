# Recommended Repository Structure

```text
project-root/
  app/
    api/
    orchestration/
    execution/
    llm_gateway/
    policy/
    audit/
    knowledge/
    memory/
    adapters/
    registries/
    lifecycle/
    compatibility/
    settings/
    platform_api/
  plugins/
    core.filesystem/
    core.git/
    core.telegram/
    core.ollama/
    core.openai_compat/
    core.pdf/
    core.image/
    core.voice/
    core.patch_builder/
    personal.pack/
    finance.pack/
    odoo.business/
    odoo.engineering/
    policy.risk_default/
    policy.path_grants/
    policy.approvals_default/
    policy.model_routing/
  docs/
    adr/
    architecture/
    specs/
    development/
    templates/
  tests/
    unit/
    integration/
    contract/
    plugin/
    e2e/
```

## Rules

- platform contracts stay separate from runtime code
- first-party plugins live in `/plugins`
- docs stay versioned with code
- contract tests are mandatory for registries and manifest validation

