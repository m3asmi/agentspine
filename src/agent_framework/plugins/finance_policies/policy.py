from __future__ import annotations

from pydantic import BaseModel


class FinancePolicyDecision(BaseModel):
    capability_id: str
    allow: bool
    reason: str
    approval_mode: str


class FinanceReadOnlyPolicy:
    _allowed_read_only: frozenset[str] = frozenset(
        {
            "get_equity_profile",
            "get_company_fundamentals",
            "get_macro_series",
            "screen_assets",
            "compare_tickers",
            "build_market_brief",
            "generate_investment_research_draft",
        }
    )

    def evaluate(self, capability_id: str) -> FinancePolicyDecision:
        if capability_id in self._allowed_read_only:
            return FinancePolicyDecision(
                capability_id=capability_id,
                allow=True,
                reason="stage1_finance_read_only_allowed",
                approval_mode="always_auto",
            )
        return FinancePolicyDecision(
            capability_id=capability_id,
            allow=False,
            reason="finance_write_or_unknown_action_blocked_in_v1",
            approval_mode="disabled",
        )
