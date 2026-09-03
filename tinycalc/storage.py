import json
from pathlib import Path

from tinycalc.models import CalculationRecord


def save_history(records: list[CalculationRecord], path: Path) -> None:
    """Save calculation history to a JSON file."""
    # Assuming CalculationRecord objects can be converted to dictionaries via vars()
    records_dict = [vars(record) for record in records]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(records_dict, f, indent=4)


def load_history(path: Path) -> list[CalculationRecord]:
    """Load calculation history from a JSON file."""
    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as f:
        records_dict = json.load(f)

    return [CalculationRecord(**record) for record in records_dict]
