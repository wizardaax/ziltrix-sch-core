from __future__ import annotations

from ziltrix_sch_core.entropy import deterministic_kdf, entropy_bytes, entropy_int


def test_entropy_lengths():
    assert len(entropy_bytes(16)) == 16
    assert entropy_int(8) >= 0


def test_deterministic_kdf():
    k1 = deterministic_kdf("seed", "ctx", out_len=32)
    k2 = deterministic_kdf("seed", "ctx", out_len=32)
    assert k1 == k2
    k3 = deterministic_kdf("seed", "other", out_len=32)
    assert k1 != k3
