from dataclasses import dataclass


@dataclass
class CalculationRecord:
    """One calculation stored in history."""

    operation: str
    left: float
    right: float
    result: float
