from agent_framework.plugins.finance_api.provider import FinanceProvider
from agent_framework.plugins.finance_openbb.adapter import OpenBBFinanceProvider


def test_openbb_adapter_matches_provider_protocol() -> None:
    provider = OpenBBFinanceProvider(client=object())
    assert isinstance(provider, FinanceProvider)
