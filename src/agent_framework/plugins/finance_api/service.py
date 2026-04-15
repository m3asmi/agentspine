from __future__ import annotations

from agent_framework.platform_api.contracts.finance import EquityProfileInput, EquityProfileOutput
from agent_framework.plugins.finance_api.registry import FinanceProviderRegistry
from agent_framework.plugins.finance_policies.policy import FinanceReadOnlyPolicy


class FinanceService:
    def __init__(
        self,
        *,
        provider_registry: FinanceProviderRegistry,
        policy: FinanceReadOnlyPolicy,
        default_provider_id: str,
    ) -> None:
        self._provider_registry = provider_registry
        self._policy = policy
        self._default_provider_id = default_provider_id

    async def get_equity_profile(
        self, payload: EquityProfileInput, provider_id: str | None = None
    ) -> EquityProfileOutput:
        decision = self._policy.evaluate("get_equity_profile")
        if not decision.allow:
            raise PermissionError(decision.reason)

        provider = self._provider_registry.get(provider_id or self._default_provider_id)
        return await provider.get_equity_profile(payload)
