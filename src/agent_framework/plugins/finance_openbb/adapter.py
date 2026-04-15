from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from agent_framework.platform_api.contracts.finance import (
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
    ScreenAssetsInput,
    ScreenAssetsOutput,
)
from agent_framework.plugins.finance_api.provider import FinanceProvider, FinanceProviderError
from agent_framework.plugins.finance_openbb.mappers import map_equity_profile


class OpenBBFinanceProvider(FinanceProvider):
    def __init__(self, *, provider_id: str = "openbb", client: Any | None = None) -> None:
        self.provider_id = provider_id
        self._client = client

    async def get_equity_profile(self, payload: EquityProfileInput) -> EquityProfileOutput:
        raw = self._fetch_equity_profile(payload.ticker)
        return map_equity_profile(raw, ticker=payload.ticker, provider_id=self.provider_id)

    def _fetch_equity_profile(self, ticker: str) -> Mapping[str, Any]:
        if self._client is None:
            raise FinanceProviderError(
                "OpenBB client not configured. Install optional extra and wire adapter.",
                code="openbb_not_configured",
                retriable=False,
            )
        if hasattr(self._client, "get_equity_profile"):
            result = self._client.get_equity_profile(ticker)
            if isinstance(result, Mapping):
                return result
        raise FinanceProviderError(
            "OpenBB client does not expose supported equity profile method.",
            code="openbb_unsupported_client",
            retriable=False,
        )

    async def get_company_fundamentals(
        self, payload: CompanyFundamentalsInput
    ) -> CompanyFundamentalsOutput:
        raise FinanceProviderError("Not implemented in v1 slice", code="not_implemented")

    async def get_macro_series(self, payload: MacroSeriesInput) -> MacroSeriesOutput:
        raise FinanceProviderError("Not implemented in v1 slice", code="not_implemented")

    async def screen_assets(self, payload: ScreenAssetsInput) -> ScreenAssetsOutput:
        raise FinanceProviderError("Not implemented in v1 slice", code="not_implemented")

    async def compare_tickers(self, payload: CompareTickersInput) -> CompareTickersOutput:
        raise FinanceProviderError("Not implemented in v1 slice", code="not_implemented")

    async def build_market_brief(self, payload: BuildMarketBriefInput) -> BuildMarketBriefOutput:
        raise FinanceProviderError("Not implemented in v1 slice", code="not_implemented")

    async def generate_investment_research_draft(
        self, payload: GenerateInvestmentResearchDraftInput
    ) -> GenerateInvestmentResearchDraftOutput:
        raise FinanceProviderError("Not implemented in v1 slice", code="not_implemented")
