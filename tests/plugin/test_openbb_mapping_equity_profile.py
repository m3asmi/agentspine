from agent_framework.plugins.finance_openbb.mappers import map_equity_profile


def test_map_equity_profile_normalizes_payload() -> None:
    payload = {
        "name": "Microsoft Corporation",
        "sector": "Technology",
        "industry": "Software",
        "long_description": "A software company",
    }

    result = map_equity_profile(payload, ticker="msft", provider_id="openbb")
    assert result.ticker == "MSFT"
    assert result.company_name == "Microsoft Corporation"
    assert result.source_provider == "openbb"
