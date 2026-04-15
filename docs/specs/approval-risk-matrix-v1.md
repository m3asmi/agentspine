# Approval and Risk Matrix v1

## Risk tiers

### R0 — Read-only
Auto.

Examples:
- read note
- inspect repo
- read Odoo record
- summarize PDF

### R1 — Workspace generation
Auto.

Examples:
- generate patch
- run tests
- build report
- extract spreadsheet data

### R2 — Bounded local write
Policy-controlled.

Examples:
- append note
- save output in approved folder
- edit existing note after approval

### R3 — Live external side effect
Ask by default.

Examples:
- create/update Odoo record
- future outbound email/calendar actions

## Approval modes

- `always_auto`
- `always_ask`
- `ask_on_policy`
- `disabled`

## Stage 1 defaults

- repo patch generation: `always_auto`
- repo live apply: `disabled`
- finance writes: `disabled`
- note append: `ask_on_policy`
- note edit: `always_ask`
- Odoo writes: `ask_on_policy` when enabled later

