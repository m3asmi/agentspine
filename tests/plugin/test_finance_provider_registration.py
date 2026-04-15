from agent_framework.plugins.finance_api.registry import FinanceProviderRegistry
from agent_framework.plugins.finance_openbb.adapter import OpenBBFinanceProvider


def test_finance_provider_registration_and_duplicate_rejection() -> None:
    registry = FinanceProviderRegistry()
    provider = OpenBBFinanceProvider(client=object())

    registry.register(provider)
    assert registry.list_provider_ids() == ["openbb"]

    try:
        registry.register(provider)
        assert False, "expected duplicate provider registration to fail"
    except ValueError as exc:
        assert "duplicate finance provider" in str(exc)
