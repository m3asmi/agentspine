from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel, Field

RiskTier = Literal["R0", "R1", "R2", "R3"]
ApprovalMode = Literal["always_auto", "always_ask", "ask_on_policy", "disabled"]


class EquityProfileInput(BaseModel):
    ticker: str = Field(min_length=1)


class EquityProfileOutput(BaseModel):
    ticker: str
    company_name: str
    sector: str | None = None
    industry: str | None = None
    description: str | None = None
    source_provider: str


class CompanyFundamentalsInput(BaseModel):
    ticker: str = Field(min_length=1)


class CompanyFundamentalsOutput(BaseModel):
    ticker: str
    market_cap: float | None = None
    pe_ratio: float | None = None
    revenue_ttm: float | None = None
    net_income_ttm: float | None = None
    source_provider: str


class MacroSeriesInput(BaseModel):
    series_id: str = Field(min_length=1)
    start_date: date | None = None
    end_date: date | None = None


class MacroSeriesPoint(BaseModel):
    date: date
    value: float


class MacroSeriesOutput(BaseModel):
    series_id: str
    points: list[MacroSeriesPoint]
    source_provider: str


class ScreenAssetsInput(BaseModel):
    market: str = Field(default="us")
    min_market_cap: float | None = None
    sector: str | None = None
    limit: int = Field(default=25, ge=1, le=200)


class ScreenedAsset(BaseModel):
    ticker: str
    company_name: str | None = None
    market_cap: float | None = None
    sector: str | None = None


class ScreenAssetsOutput(BaseModel):
    assets: list[ScreenedAsset]
    source_provider: str


class CompareTickersInput(BaseModel):
    tickers: list[str] = Field(min_length=2, max_length=10)


class CompareTickerRow(BaseModel):
    ticker: str
    market_cap: float | None = None
    pe_ratio: float | None = None
    revenue_ttm: float | None = None


class CompareTickersOutput(BaseModel):
    rows: list[CompareTickerRow]
    source_provider: str


class BuildMarketBriefInput(BaseModel):
    focus: str = Field(default="equities")
    region: str = Field(default="global")


class BuildMarketBriefOutput(BaseModel):
    title: str
    highlights: list[str]
    risks: list[str]
    source_provider: str


class GenerateInvestmentResearchDraftInput(BaseModel):
    ticker: str = Field(min_length=1)
    thesis: str | None = None


class GenerateInvestmentResearchDraftOutput(BaseModel):
    ticker: str
    draft_markdown: str
    disclaimers: list[str]
    source_provider: str
