# Plugin System Architecture

## Goal

Create a framework that is plugin-ready in Stage 1 and can evolve later into a stronger ecosystem model.

## Plugin categories

### Capability plugins

Provide executable units.

Examples:

- filesystem.search
- git.diff
- odoo.read_record
- pdf.extract_text

### Domain pack plugins

Provide domain-level bundles.

Examples:

- personal.pack
- finance.pack
- odoo.engineering
- odoo.business

### Channel plugins

Provide communication channels.

Examples:

- telegram
- whatsapp
- cli
- webui

### Policy plugins

Provide policy hooks.

Examples:

- default_risk_scoring
- path_grants
- approvals_default
- model_routing

### Ingestion plugins

Provide input processors.

Examples:

- pdf
- image
- voice
- spreadsheet

### Renderer plugins

Provide structured output rendering.

Examples:

- markdown_report
- patch_bundle
- telegram_card
- approval_card

## Plugin load model

1. load manifest
2. validate schema
3. validate compatibility
4. resolve dependencies
5. register settings schema
6. run install/upgrade hooks if needed
7. activate plugin
8. register contributions
9. run health checks
10. expose enabled contributions to runtime

## Design constraints

- no implicit plugin activation
- no monkey-patching internal runtime modules
- no silent dependency fallback
- no contribution registration without schema validation

## Critical rule

A plugin may contribute behavior only through declared contribution points.

