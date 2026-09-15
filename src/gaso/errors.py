class GasoError(Exception):
    """Base error with a stable machine-readable code."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message


class ConformanceError(GasoError):
    """The input is readable but violates a governance contract."""


class UsageError(GasoError):
    """The command, file, or local configuration cannot be used."""
