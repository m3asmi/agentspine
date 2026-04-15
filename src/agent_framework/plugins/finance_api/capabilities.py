from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from agent_framework.platform_api.contracts.finance import (
    ApprovalMode,
    BuildMarketBriefInput,
    BuildMarketBriefOutput,
    CompanyFundamentalsInput,
    CompanyFundamentalsOutput,
    CompareTickersInput,
    CompareTickersOutput,
    EquityProfileInput,
    EquityProfileOutput,
    GenerateInvestmentResearchDraftInput,
    GenerateInvestmentResearchDraftOutput,
    MacroSeriesInput,
    MacroSeriesOutput,
    RiskTier,
    ScreenAssetsInput,
    ScreenAssetsOutput,
)


@dataclass(frozen=True)
class CapabilitySpec:
    capability_id: str
    plugin_id: str
    description: str
    input_schema: type[BaseModel]
    output_schema: type[BaseModel]
    risk_tier: RiskTier
    approval_mode: ApprovalMode
    executor_profile: str
    idempotency_strategy: str
    audit_event_type: str
    handler_ref: str
    metadata: dict[str, Any]


def _spec(
    capability_id: str,
    input_schema: type[BaseModel],
    output_schema: type[BaseModel],
    handler_ref: str,
) -> CapabilitySpec:
    return CapabilitySpec(
        capability_id=capability_id,
        plugin_id="agentspine-finance-api",
        description=capability_id,
        input_schema=input_schema,
        output_schema=output_schema,
        risk_tier="R0",
        approval_mode="always_auto",
        executor_profile="read_only",
        idempotency_strategy="by_input_hash",
        audit_event_type=f"finance.{capability_id}.executed",
        handler_ref=handler_ref,
        metadata={"read_only": True},
    )


FINANCE_CAPABILITIES: tuple[CapabilitySpec, ...] = (
    _spec(
        "get_equity_profile",
        EquityProfileInput,
        EquityProfileOutput,
        "FinanceService.get_equity_profile",
    ),
    _spec(
        "get_company_fundamentals",
        CompanyFundamentalsInput,
        CompanyFundamentalsOutput,
        "FinanceService.get_company_fundamentals",
    ),
    _spec(
        "get_macro_series", MacroSeriesInput, MacroSeriesOutput, "FinanceService.get_macro_series"
    ),
    _spec("screen_assets", ScreenAssetsInput, ScreenAssetsOutput, "FinanceService.screen_assets"),
    _spec(
        "compare_tickers",
        CompareTickersInput,
        CompareTickersOutput,
        "FinanceService.compare_tickers",
    ),
    _spec(
        "build_market_brief",
        BuildMarketBriefInput,
        BuildMarketBriefOutput,
        "FinanceService.build_market_brief",
    ),
    _spec(
        "generate_investment_research_draft",
        GenerateInvestmentResearchDraftInput,
        GenerateInvestmentResearchDraftOutput,
        "FinanceService.generate_investment_research_draft",
    ),
)
