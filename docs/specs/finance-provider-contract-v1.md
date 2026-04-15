# Finance Provider Contract v1

## Scope

Defines provider-agnostic finance capability contracts for AgentSpine plugins.

## Required capabilities

- `get_equity_profile`
- `get_company_fundamentals`
- `get_macro_series`
- `screen_assets`
- `compare_tickers`
- `build_market_brief`
- `generate_investment_research_draft`

## Rules

- Finance provider implementations must be behind `FinanceProvider` interface.
- Agent-facing actions must use typed Pydantic input/output schemas.
- Stage 1 defaults to read-only behavior (`R0`/`R1` only).
- Unknown or write-like finance actions are blocked by policy.
