import pytest

from agent_framework.platform_api.contracts.finance import EquityProfileInput
from agent_framework.plugins.finance_api.registry import FinanceProviderRegistry
from agent_framework.plugins.finance_api.service import FinanceService
from agent_framework.plugins.finance_openbb.adapter import OpenBBFinanceProvider
from agent_framework.plugins.finance_policies.policy import FinanceReadOnlyPolicy


class _FakeOpenBBClient:
    def get_equity_profile(self, ticker: str) -> dict[str, str]:
        return {
            "company_name": "Apple Inc.",
            "sector": "Technology",
            "industry": "Consumer Electronics",
            "description": f"{ticker.upper()} profile",
        }


@pytest.mark.asyncio
async def test_equity_profile_vertical_slice() -> None:
    registry = FinanceProviderRegistry()
    registry.register(OpenBBFinanceProvider(client=_FakeOpenBBClient()))

    service = FinanceService(
        provider_registry=registry,
        policy=FinanceReadOnlyPolicy(),
        default_provider_id="openbb",
    )

    output = await service.get_equity_profile(EquityProfileInput(ticker="aapl"))

    assert output.ticker == "AAPL"
    assert output.company_name == "Apple Inc."
    assert output.source_provider == "openbb"
