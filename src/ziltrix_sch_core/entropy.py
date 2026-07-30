"""Entropy utilities and a simple deterministic KDF wrapper.

Security notes
--------------
- `entropy_bytes` and `entropy_int` use `secrets` for cryptographic randomness.
- `deterministic_kdf` uses BLAKE2b keyed hashing as a compact KDF stand-in.
  For high-assurance contexts, consider HKDF (RFC 5869) via `cryptography`.
"""

from __future__ import annotations

from hashlib import blake2b
from secrets import randbits, token_bytes


def entropy_bytes(n: int) -> bytes:
    """Return n bytes of cryptographic-quality random data."""
    if n <= 0:
        raise ValueError("n must be positive")
    return token_bytes(n)


def entropy_int(bits: int) -> int:
    """Return a random integer with the specified number of bits (>=1)."""
    if bits <= 0:
        raise ValueError("bits must be positive")
    return randbits(bits)


def deterministic_kdf(seed: str | bytes, context: str | bytes, out_len: int = 32) -> bytes:
    """Derive a fixed-length key from (seed, context) using BLAKE2b.

    - seed: secret input (bytes or UTF-8 str)
    - context: domain separation / label (bytes or UTF-8 str)
    - out_len: number of bytes to output (1..64)
    """
    if not (1 <= out_len <= 64):
        raise ValueError("out_len must be in [1, 64]")
    if isinstance(seed, str):
        seed_b = seed.encode("utf-8")
    else:
        seed_b = seed
    if isinstance(context, str):
        ctx_b = context.encode("utf-8")
    else:
        ctx_b = context
    h = blake2b(key=seed_b, digest_size=out_len)
    h.update(ctx_b)
    return h.digest()
