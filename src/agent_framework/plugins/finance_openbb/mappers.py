from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from agent_framework.platform_api.contracts.finance import EquityProfileOutput


def map_equity_profile(
    raw: Mapping[str, Any], *, ticker: str, provider_id: str
) -> EquityProfileOutput:
    return EquityProfileOutput(
        ticker=ticker.upper(),
        company_name=str(raw.get("company_name") or raw.get("name") or ticker.upper()),
        sector=_to_opt_str(raw.get("sector")),
        industry=_to_opt_str(raw.get("industry")),
        description=_to_opt_str(raw.get("description") or raw.get("long_description")),
        source_provider=provider_id,
    )


def _to_opt_str(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
