# Execution and Safety Model

## Goal

Support shell, filesystem, and engineering workflows without giving uncontrolled power to the LLM runtime.

## Core rule

All shell access and host-side file work must go through the execution worker.

The control plane must not execute arbitrary commands directly.

## Execution modes

### Mode A — Read / Index

Used for:

- notes
- documents
- repositories
- spreadsheets
- PDFs
- images
- voice media

### Mode B — Isolated Workspace Execution

Default for engineering workflows.

Used for:

- shell commands
- tests
- file edits
- patch generation
- artifact generation

### Mode C — Live Bounded Write

Used only with policy grants.

Used for:

- append to notes
- save generated outputs
- approved edits within allowed scopes

## Repo policy

Stage 1 is patch-only.

Allowed:

- read repo
- copy or mount into workspace
- edit in workspace
- run tests
- output patch bundle

Not allowed:

- auto-commit
- auto-push

## File operation rules

- append allowed where policy permits
- edit existing content requires approval where configured
- delete is disabled in Stage 1

## Service account rule

Execution worker must run under a dedicated Linux service account.

