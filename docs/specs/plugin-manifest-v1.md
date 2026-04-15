# Plugin Manifest v1

## Required fields

- plugin_id
- name
- version
- type
- api_version
- framework_version_range
- entrypoint
- contributes
- permissions
- dependencies
- settings_schema
- executor_profiles
- healthcheck
- migrations

## Plugin types

- capability
- domain_pack
- channel
- policy
- ingestion
- renderer

## Rules

- manifest is the source of truth
- plugin load fails if manifest is invalid
- undeclared contributions are forbidden
- undeclared permissions are denied
