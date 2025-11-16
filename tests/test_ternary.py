from __future__ import annotations

from hypothesis import given
from hypothesis import strategies as st

from ziltrix_sch_core.ternary import from_balanced_ternary, to_balanced_ternary


@given(st.integers(min_value=-10_000, max_value=10_000))
def test_balanced_ternary_roundtrip(n: int):
    s = to_balanced_ternary(n)
    assert from_balanced_ternary(s) == n
