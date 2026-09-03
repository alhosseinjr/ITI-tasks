from pathlib import Path

from tinycalc.calculator import Calculator
from tinycalc.exceptions import CannotDivideByZeroError
from tinycalc.storage import save_history


def main() -> None:
    calculator = Calculator()

    print(calculator.add(10, 5))
    print(calculator.subtract(10, 5))
    print(calculator.multiply(10, 5))

    try:
        print(calculator.divide(10, 0))
    except CannotDivideByZeroError as error:
        print(f"Could not calculate: {error}")

    save_history(calculator.history, Path("history.json"))


if __name__ == "__main__":
    main()
