"""Golden ratio utilities, with high-precision Decimal support.

Provides:
- phi(): high-precision golden ratio φ
- binet(n): compute Fibonacci(n) via Binet's formula (rounded to nearest int)

Note: For large n, use `sequence.fib` for exact integer results. Binet is
useful for analytical work and small-to-medium n when using high precision.
"""

from __future__ import annotations

from decimal import Decimal, getcontext


def phi(precision: int = 80) -> Decimal:
    """Return the golden ratio φ with the given Decimal precision."""
    getcontext().prec = max(precision, 32)
    sqrt5 = Decimal(5).sqrt()
    return (Decimal(1) + sqrt5) / Decimal(2)


def binet(n: int, precision: int = 80) -> int:
    """Compute Fibonacci(n) using Binet's formula (rounded).

    For exact big integers, prefer sequence.fib. Raises ValueError for n < 0.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    getcontext().prec = max(precision, 50)
    sqrt5 = Decimal(5).sqrt()
    phi_val = (Decimal(1) + sqrt5) / Decimal(2)
    psi_val = (Decimal(1) - sqrt5) / Decimal(2)  # -1/phi
    val = (phi_val**n - psi_val**n) / sqrt5
    return int(val.to_integral_value(rounding="ROUND_HALF_UP"))
