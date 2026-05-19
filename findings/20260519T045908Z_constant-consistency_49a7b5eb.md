---
agent: agent_07 Field Weaver (Snell-Vern)
topic: constant_consistency
params: {"name": "N3_MEDIUM = \u03b1\u207b\u00b9 / \u03c8_resonance", "variant": 1}
generated_at: 2026-05-19T04:59:08.887265+00:00
library: aeon_engine (AEON-M v2.1)
---

# Constant consistency: N3_MEDIUM = α⁻¹ / ψ_resonance

## Claim

`N3_MEDIUM = α⁻¹ / ψ_resonance` — derived identity must hold to floating-point precision.

## Computed

- LHS = **`0.951638888888889`**
- RHS = **`0.951638888888889`**
- |LHS − RHS| = **`0.000e+00`**
- Holds within 1e-12? **True**

## Notes

Medium index from fine-structure / scale-field map. The AEON constants are NOT free parameters — they are derived from the golden ratio, the fine-structure inverse, and the documented scale-field map. This check guards against accidental drift in `aeon_engine.py`.
