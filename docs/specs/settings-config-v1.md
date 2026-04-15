# Settings and Configuration v1

## Goal

Allow extensions to expose configuration safely and predictably.

## Rules

- every plugin setting must have a JSON Schema
- settings are namespaced by plugin id
- framework validates before saving
- plugin defaults come from manifest
- secrets are stored separately from normal config

## Settings layers

1. framework defaults
2. plugin defaults
3. environment overrides
4. user overrides
5. runtime overrides where allowed

## Recommended categories

- model routing
- default provider
- path grants
- Odoo environment aliases
- channel behavior
- compare mode flags
- timeout tuning
- feature flags

## Secret handling

Secrets must not be stored in general settings payloads.

Use a secret provider or dedicated secure store abstraction.

