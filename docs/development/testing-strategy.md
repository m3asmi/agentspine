# Testing Strategy

## Test layers

### Unit tests

Cover:

- manifest validation
- dependency resolution
- registry logic
- permission parsing
- settings validation
- compatibility checks

### Contract tests

Cover:

- extension interface compliance
- contribution schema compliance
- capability contract compliance
- lifecycle hook behavior

### Integration tests

Cover:

- plugin load sequence
- registry activation
- settings merge behavior
- permission enforcement
- provider gateway routing
- execution dispatcher behavior

### Plugin tests

Each plugin should include:

- manifest sanity test
- registration test
- healthcheck test
- capability invocation test
- permission boundary test

### End-to-end tests

Cover:

- Telegram request to final response
- patch generation flow
- compare mode flow
- approval flow
- Odoo read flow

## Required CI checks

- manifest lint
- schema validation
- type checks
- unit tests
- contract tests
- plugin load smoke test

