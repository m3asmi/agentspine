from agent_framework.plugins.finance_policies.policy import FinanceReadOnlyPolicy


def test_read_only_capability_allowed() -> None:
    policy = FinanceReadOnlyPolicy()
    decision = policy.evaluate("get_equity_profile")
    assert decision.allow is True
    assert decision.approval_mode == "always_auto"


def test_unknown_or_write_like_capability_blocked() -> None:
    policy = FinanceReadOnlyPolicy()
    decision = policy.evaluate("execute_trade")
    assert decision.allow is False
    assert decision.approval_mode == "disabled"
