from pathlib import Path

from dss.data_ingestion.portfolio import load_portfolio
from dss.engine.signals import generate_signal
from dss.reporting.report_builder import build_report


def main() -> None:
    """
    Main pipeline: load portfolio -> generate signal -> build report -> write output.
    """
    portfolio_path = Path("data/portfolio_example.json")
    output_path = Path("reports/sample_daily_brief.md")

    portfolio = load_portfolio(portfolio_path)
    signal = generate_signal(portfolio)
    report = build_report(portfolio, signal)

    output_path.write_text(report, encoding="utf-8")
    print("Daily brief generated successfully.")


if __name__ == "__main__":
    main()
