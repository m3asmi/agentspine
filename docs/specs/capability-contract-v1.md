# Capability Contract v1

## Required fields

- capability_id
- plugin_id
- description
- input_schema
- output_schema
- risk_tier
- approval_mode
- executor_profile
- idempotency_strategy
- audit_event_type
- handler_ref

## Risk tiers

- R0 read-only
- R1 workspace generation
- R2 bounded local write
- R3 live external side effect

## Rule

No capability is executable without a schema and declared audit event type.
