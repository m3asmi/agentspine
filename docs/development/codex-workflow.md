# Codex Workflow

## Working model

- implement one task at a time
- update task checkbox state in the current phase file
- open one PR per task cluster
- do not mix architecture changes with feature tasks

## Task execution order

1. read current phase file
2. read linked spec files
3. implement minimum slice
4. add tests
5. update docs
6. mark acceptance criteria

## Commit style

- `phase0: add manifest loader`
- `phase1: add obsidian append capability`
- `phase2: add odoo json2 adapter`
