from tinycalc.exceptions import CannotDivideByZeroError
from tinycalc.models import CalculationRecord


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def subtract(left: float, right: float) -> float:
    """Return the difference between two numbers."""
    return left - right


def multiply(left: float, right: float) -> float:
    """Return the product of two numbers."""
    return left * right


def divide(left: float, right: float) -> float:
    """Return left divided by right."""
    if right == 0:
        raise CannotDivideByZeroError("Cannot divide by zero.")

    return left / right


class Calculator:
    """Calculator that stores calculation history."""

    def __init__(self) -> None:
        self.history: list[CalculationRecord] = []

    def add(self, left: float, right: float) -> float:
        result = add(left, right)
        self._record("add", left, right, result)
        return result

    def subtract(self, left: float, right: float) -> float:
        result = subtract(left, right)
        self._record("subtract", left, right, result)
        return result

    def multiply(self, left: float, right: float) -> float:
        result = multiply(left, right)
        self._record("multiply", left, right, result)
        return result

    def divide(self, left: float, right: float) -> float:
        result = divide(left, right)
        self._record("divide", left, right, result)
        return result

    def _record(
        self,
        operation: str,
        left: float,
        right: float,
        result: float,
    ) -> None:
        record = CalculationRecord(
            operation=operation, left=left, right=right, result=result
        )
        self.history.append(record)
