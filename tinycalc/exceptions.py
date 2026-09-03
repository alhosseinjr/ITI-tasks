class TinyCalcError(Exception):
    """Base exception for TinyCalc."""


class CannotDivideByZeroError(TinyCalcError):
    """Raised when division by zero is requested."""
