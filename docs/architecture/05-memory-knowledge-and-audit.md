# Memory, Knowledge, and Audit

## Memory scopes

### Thread memory

Conversation and run-local state.

### User preference memory

Stable personal preferences.

### Workspace memory

Project or repository summaries, vault maps, module hints.

### Domain memory

Stable domain context for personal, finance, or Odoo workflows.

## Memory rule

Memory is support context.

It never overrides source systems.

## Knowledge namespaces

Suggested initial namespaces:

- obsidian_notes
- home_docs
- odoo_custom_addons
- odoo_oca_addons
- finance_docs
- run_artifacts
- policy_docs

## Audit goals

Every extension action must be attributable.

## Minimum audit fields

- event_id
- timestamp
- plugin_id
- plugin_version
- contribution_type
- action
- run_id
- user_id
- result
- risk_tier
- approval_context
- resource_scope

## Audit categories

- plugin lifecycle events
- graph execution events
- capability execution events
- shell execution events
- file write events
- patch generation events
- Odoo interaction events
- LLM provider events
- approval events

