---
agent: agent_07 Field Weaver (Snell-Vern)
topic: brane_refraction
params: {"theta_in_deg": 30.0}
generated_at: 2026-05-19T16:59:09.490801+00:00
library: aeon_engine (AEON-M v2.1)
---

# Brane refraction at θ_in=30.0°

## Claim

Cascading Snell's law through the documented AEON-M brane stack `[φ, χ, n₃]` deflects an incoming ray by a deterministic geometric factor.

## Computed (θ_in = 30.0°)

- input angle: **30.0°** (`0.523599` rad)
- base brane layers: `[φ, χ, n₃]` = **[1.618034, 6.000000, 0.951639]**
- output angle: **58.225838°** (`1.016233` rad)
- deflection: **-28.225838°**

## Notes

Layer identities:
- `φ` = golden ratio (1.6180339887…) — the outer brane index
- `χ` = 2π / (π/3) ≈ 6.2832 — modulation frequency from 60° aperture
- `n₃` = α⁻¹ / ψ_resonance = 137.036 / 144 ≈ 0.9516 — medium index

The cascade is element-wise `n₁·sin(θ₁) = n₂·sin(θ₂)`. Clipping to `[-1, 1]` handles total internal reflection where it would otherwise return NaN.
