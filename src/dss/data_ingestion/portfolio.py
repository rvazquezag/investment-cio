import json
from pathlib import Path
from typing import Any


def load_portfolio(portfolio_path: Path) -> dict[str, Any]:
    """
    Load the portfolio from a JSON file.

    Args:
        portfolio_path (Path): Path to the portfolio JSON file.

    Returns:
        dict: Portfolio data loaded from JSON.
    """
    with portfolio_path.open("r", encoding="utf-8") as f:
        return json.load(f)
