---
agent: agent_07 Field Weaver (Snell-Vern)
topic: coupling_k_extraction
params: {"sample_idx": 4}
generated_at: 2026-05-18T08:59:08.803848+00:00
library: aeon_engine (AEON-M v2.1)
---

# Coupling k extraction from PhaseII sample #4

## Claim

Faraday-induction propulsion predicts `F = k · dΦ/dt` with a single coupling constant `k`. Extracting k from each documented PhaseII sample should yield the same value to within numerical precision.

## Sample #4

- t       = **`4.040e-08` s**
- Φ       = **`1.770e-04` Wb**
- dΦ/dt   = **`-2.320e+02` V**
- F       = **`-6.190e-07` N**

- k_extracted = F / (dΦ/dt) = **`2.668449e-09` N·s/V**
- k_documented (COUPLING_K) = **`2.670000e-09` N·s/V**
- |diff|  = **`1.551e-12`**
- rel_err = **`0.0581%`**

## Notes

COUPLING_K = 2.67e-9 N·s/V is the brane-lensing geometric factor in Faraday-induction units, derived from the multi-layer Snell's-law cascade through `[φ, χ, n₃]`. Internal consistency across all 5 PhaseII samples is the strongest empirical claim of the AEON-M v2.1 paper: one k, five thrust/flux pairs, no per-sample re-tuning.
