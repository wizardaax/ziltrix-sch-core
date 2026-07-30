"""Balanced ternary conversions.

Digits are in {T, 0, 1} where T represents -1. Strings are big-endian.
"""

from __future__ import annotations

_DIGITS = {-1: "T", 0: "0", 1: "1"}
_INV = {v: k for k, v in _DIGITS.items()}


def to_balanced_ternary(n: int) -> str:
    """Convert integer n to balanced ternary string using digits T,0,1.
    Returns '0' for n == 0.
    """
    if n == 0:
        return "0"
    sign = -1 if n < 0 else 1
    n = abs(n)
    digits = []
    while n != 0:
        n, r = divmod(n, 3)
        if r == 2:
            r = -1
            n += 1
        digits.append(_DIGITS[r])
    s = "".join(reversed(digits))
    return s if sign > 0 else _negate_balanced_ternary(s)


def _negate_balanced_ternary(s: str) -> str:
    # Negation maps T<->1, 0->0
    trans = {"T": "1", "1": "T", "0": "0"}
    return "".join(trans[ch] for ch in s)


def from_balanced_ternary(s: str) -> int:
    """Parse a balanced ternary string (T,0,1) into an integer.
    Leading zeros are allowed. Empty string is invalid.
    """
    if not s:
        raise ValueError("empty balanced ternary string")
    val = 0
    for ch in s:
        if ch not in _INV:
            raise ValueError(f"invalid digit {ch!r}; expected one of T,0,1")
        val = 3 * val + _INV[ch]
    return val
