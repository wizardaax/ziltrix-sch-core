"""Fibonacci and Lucas sequences with fast-doubling algorithms.

- fib(n): returns the nth Fibonacci number (F_0 = 0, F_1 = 1)
- lucas(n): returns the nth Lucas number (L_0 = 2, L_1 = 1)

Notes
-----
We use the fast-doubling method for O(log n) time with exact integers.
For Lucas we use the relation L_n = 2*F_{n+1} - F_n for n >= 1 and L_0 = 2.
"""

from __future__ import annotations


def _fib_doubling(n: int) -> tuple[int, int]:
    """Return (F_n, F_{n+1}) using fast-doubling.

    Raises ValueError on negative n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0, 1
    a, b = _fib_doubling(n >> 1)
    c = a * (2 * b - a)  # F_{2k}
    d = a * a + b * b  # F_{2k+1}
    if n & 1:
        return d, c + d
    else:
        return c, d


def fib(n: int) -> int:
    """Compute the nth Fibonacci number for n >= 0."""
    return _fib_doubling(n)[0]


def lucas(n: int) -> int:
    """Compute the nth Lucas number.

    Uses L_n = 2*F_{n+1} - F_n for n >= 1 and L_0 = 2.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 2
    fn, fn1 = _fib_doubling(n)  # F_n, F_{n+1}
    return 2 * fn1 - fn
