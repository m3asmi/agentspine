# Finance OpenBB Integration v1

## Intent

OpenBB is an optional finance backend adapter. It is not part of AgentSpine core runtime.

## Boundary

- `agent_framework.plugins.finance_api` provides contracts and capability declarations.
- `agent_framework.plugins.finance_openbb` implements provider adapter.
- `agent_framework.plugins.finance_policies` enforces read-only defaults.
- Core orchestration must never call OpenBB APIs directly.

## Configuration

- Optional dependency group: `finance_openbb`.
- Plugin setting `enabled=false` by default.
- Secrets referenced by `api_key_secret_ref`; do not store raw keys in regular settings payloads.

## Failure behavior

- Missing optional dependency or unconfigured adapter fails explicitly.
- Provider errors are surfaced as typed `FinanceProviderError` and should be audited by runtime.
