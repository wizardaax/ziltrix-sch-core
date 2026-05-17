---
agent: agent_07 Field Weaver (Snell-Vern)
topic: coupling_k_extraction
params: {"sample_idx": 3}
generated_at: 2026-05-17T11:59:08.715105+00:00
library: aeon_engine (AEON-M v2.1)
---

# Coupling k extraction from PhaseII sample #3

## Claim

Faraday-induction propulsion predicts `F = k · dΦ/dt` with a single coupling constant `k`. Extracting k from each documented PhaseII sample should yield the same value to within numerical precision.

## Sample #3

- t       = **`3.030e-08` s**
- Φ       = **`1.790e-04` Wb**
- dΦ/dt   = **`-1.732e+02` V**
- F       = **`-4.620e-07` N**

- k_extracted = F / (dΦ/dt) = **`2.666975e-09` N·s/V**
- k_documented (COUPLING_K) = **`2.670000e-09` N·s/V**
- |diff|  = **`3.025e-12`**
- rel_err = **`0.1133%`**

## Notes

COUPLING_K = 2.67e-9 N·s/V is the brane-lensing geometric factor in Faraday-induction units, derived from the multi-layer Snell's-law cascade through `[φ, χ, n₃]`. Internal consistency across all 5 PhaseII samples is the strongest empirical claim of the AEON-M v2.1 paper: one k, five thrust/flux pairs, no per-sample re-tuning.
