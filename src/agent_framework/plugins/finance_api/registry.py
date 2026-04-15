from __future__ import annotations

from agent_framework.plugins.finance_api.provider import FinanceProvider


class FinanceProviderRegistry:
    def __init__(self) -> None:
        self._providers: dict[str, FinanceProvider] = {}

    def register(self, provider: FinanceProvider) -> None:
        if provider.provider_id in self._providers:
            raise ValueError(f"duplicate finance provider: {provider.provider_id}")
        self._providers[provider.provider_id] = provider

    def get(self, provider_id: str) -> FinanceProvider:
        try:
            return self._providers[provider_id]
        except KeyError as exc:
            raise ValueError(f"unknown finance provider: {provider_id}") from exc

    def list_provider_ids(self) -> list[str]:
        return sorted(self._providers.keys())
