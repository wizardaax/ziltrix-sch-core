---
agent: agent_07 Field Weaver (Snell-Vern)
topic: constant_consistency
params: {"name": "GOLDEN_ANGLE_DEG = 360 / \u03c6\u00b2", "variant": 0}
generated_at: 2026-05-13T14:59:08.487396+00:00
library: aeon_engine (AEON-M v2.1)
---

# Constant consistency: GOLDEN_ANGLE_DEG = 360 / φ²

## Claim

`GOLDEN_ANGLE_DEG = 360 / φ²` — derived identity must hold to floating-point precision.

## Computed

- LHS = **`137.507764050037849`**
- RHS = **`137.507764050037849`**
- |LHS − RHS| = **`0.000e+00`**
- Holds within 1e-12? **True**

## Notes

Golden angle in degrees derived from φ. The AEON constants are NOT free parameters — they are derived from the golden ratio, the fine-structure inverse, and the documented scale-field map. This check guards against accidental drift in `aeon_engine.py`.
