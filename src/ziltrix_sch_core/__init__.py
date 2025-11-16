"""Ziltrix SCH Core — minimal math primitives scaffold.

Exports selected primitives for convenience.
"""

from .entropy import deterministic_kdf, entropy_bytes, entropy_int
from .phi import binet, phi
from .sequence import fib, lucas
from .ternary import from_balanced_ternary, to_balanced_ternary

__all__ = [
    "fib",
    "lucas",
    "phi",
    "binet",
    "to_balanced_ternary",
    "from_balanced_ternary",
    "entropy_bytes",
    "entropy_int",
    "deterministic_kdf",
]

__version__ = "0.0.1"
