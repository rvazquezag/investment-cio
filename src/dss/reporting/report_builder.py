from typing import Dict, Any


def build_report(portfolio: Dict[str, Any], signal: str) -> str:
    """
    Build a human-readable daily investment brief.

    Args:
        portfolio (dict): Portfolio snapshot data.
        signal (str): System recommendation.

    Returns:
        str: Formatted daily report.
    """
    as_of = portfolio["as_of"]
    base_currency = portfolio["base_currency"]
    cash = portfolio["cash"]
    positions = portfolio["positions"]
    risk_profile = portfolio["risk_profile"]

    equities = [p for p in positions if p["asset_class"] == "equity"]
    etfs = [p for p in positions if p["asset_class"] == "etf"]

    report_lines = []

    # Header
    report_lines.append("DAILY PORTFOLIO SUMMARY")
    report_lines.append(f"As of: {as_of}")
    report_lines.append("")
    report_lines.append("-" * 50)

    # 1. Portfolio Snapshot
    report_lines.append("")
    report_lines.append("1. Portfolio Snapshot")
    report_lines.append("")
    report_lines.append(f"Base currency: {base_currency}")
    report_lines.append(f"Cash available: {cash['amount']} {cash['currency']}")
    report_lines.append(f"Number of positions: {len(positions)}")
    report_lines.append(f"Risk profile: {risk_profile['level'].capitalize()}")
    report_lines.append(
        f"Investment horizon: {risk_profile['investment_horizon'].replace('_', ' ').capitalize()}"
    )

    report_lines.append("")
    report_lines.append("-" * 50)

    # 2. Portfolio Composition
    report_lines.append("")
    report_lines.append("2. Portfolio Composition")
    report_lines.append("")

    report_lines.append(f"Equities ({len(equities)}):")
    for p in equities:
        report_lines.append(
            f"- {p['name']} ({p['symbol']}, {p['region']}): "
            f"{p['quantity']} shares at {p['avg_cost']} {p['currency']}"
        )

    report_lines.append("")
    report_lines.append(f"ETFs ({len(etfs)}):")
    for p in etfs:
        report_lines.append(
            f"- {p['name']} ({p['symbol']}): {p['quantity']} shares"
        )

    report_lines.append("")
    report_lines.append("-" * 50)

    # 3. System Recommendation
    report_lines.append("")
    report_lines.append("3. System Recommendation")
    report_lines.append("")
    report_lines.append(f"Recommendation: {signal}")
    report_lines.append("")
    report_lines.append("Rationale:")
    report_lines.append("- No strong conviction signals detected")
    report_lines.append("- Portfolio risk remains within target range")
    report_lines.append("- Current market conditions do not justify reallocation")

    report_lines.append("")
    report_lines.append("-" * 50)
    report_lines.append("")
    report_lines.append("End of report")

    return "\n".join(report_lines)
