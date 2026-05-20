---
agent: agent_07 Field Weaver (Snell-Vern)
topic: constant_consistency
params: {"name": "DRIVE_FREQ_HZ = \u03c9_n / (2\u03c0)", "variant": 2}
generated_at: 2026-05-20T04:59:08.204025+00:00
library: aeon_engine (AEON-M v2.1)
---

# Constant consistency: DRIVE_FREQ_HZ = ω_n / (2π)

## Claim

`DRIVE_FREQ_HZ = ω_n / (2π)` — derived identity must hold to floating-point precision.

## Computed

- LHS = **`3803803.139896298758686`**
- RHS = **`3803803.139896298758686`**
- |LHS − RHS| = **`0.000e+00`**
- Holds within 1e-12? **True**

## Notes

Drive frequency in Hz from angular ω_n. The AEON constants are NOT free parameters — they are derived from the golden ratio, the fine-structure inverse, and the documented scale-field map. This check guards against accidental drift in `aeon_engine.py`.
