from __future__ import annotations

from typing import Protocol, runtime_checkable

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


class FinanceProviderError(RuntimeError):
    def __init__(self, message: str, *, code: str, retriable: bool = False) -> None:
        super().__init__(message)
        self.code = code
        self.retriable = retriable


@runtime_checkable
class FinanceProvider(Protocol):
    provider_id: str

    async def get_equity_profile(self, payload: EquityProfileInput) -> EquityProfileOutput: ...

    async def get_company_fundamentals(
        self, payload: CompanyFundamentalsInput
    ) -> CompanyFundamentalsOutput: ...

    async def get_macro_series(self, payload: MacroSeriesInput) -> MacroSeriesOutput: ...

    async def screen_assets(self, payload: ScreenAssetsInput) -> ScreenAssetsOutput: ...

    async def compare_tickers(self, payload: CompareTickersInput) -> CompareTickersOutput: ...

    async def build_market_brief(
        self, payload: BuildMarketBriefInput
    ) -> BuildMarketBriefOutput: ...

    async def generate_investment_research_draft(
        self, payload: GenerateInvestmentResearchDraftInput
    ) -> GenerateInvestmentResearchDraftOutput: ...
