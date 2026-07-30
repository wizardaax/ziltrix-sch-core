from __future__ import annotations

import pytest
from hypothesis import given
from hypothesis import strategies as st

from ziltrix_sch_core.sequence import fib, lucas


def test_small_values():
    assert fib(0) == 0
    assert fib(1) == 1
    assert lucas(0) == 2
    assert lucas(1) == 1


@given(st.integers(min_value=0, max_value=2000))
def test_fib_recurrence(n: int):
    if n < 2:
        pytest.skip("recurrence needs n>=2")
    assert fib(n) + fib(n - 1) == fib(n + 1)


@given(st.integers(min_value=0, max_value=2000))
def test_lucas_relation(n: int):
    # For n >= 1, L_n = 2*F_{n+1} - F_n
    if n == 0:
        assert lucas(0) == 2
    else:
        assert lucas(n) == 2 * fib(n + 1) - fib(n)
