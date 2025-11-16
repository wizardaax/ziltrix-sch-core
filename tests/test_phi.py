from __future__ import annotations

from decimal import Decimal

from ziltrix_sch_core.phi import binet, phi
from ziltrix_sch_core.sequence import fib


def test_phi_approx():
    val = phi(precision=60)
    # φ ≈ 1.6180339887
    assert abs(val - Decimal("1.6180339887")) < Decimal("1e-10")


def test_binet_matches_fib_small():
    for n in range(0, 50):
        assert binet(n, precision=80) == fib(n)
