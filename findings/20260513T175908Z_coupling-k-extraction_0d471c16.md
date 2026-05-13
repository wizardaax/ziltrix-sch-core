---
agent: agent_07 Field Weaver (Snell-Vern)
topic: coupling_k_extraction
params: {"sample_idx": 0}
generated_at: 2026-05-13T17:59:08.574855+00:00
library: aeon_engine (AEON-M v2.1)
---

# Coupling k extraction from PhaseII sample #0

## Claim

Faraday-induction propulsion predicts `F = k · dΦ/dt` with a single coupling constant `k`. Extracting k from each documented PhaseII sample should yield the same value to within numerical precision.

## Sample #0

- t       = **`0.000e+00` s**
- Φ       = **`1.810e-04` Wb**
- dΦ/dt   = **`-2.870e+01` V**
- F       = **`-7.650e-08` N**

- k_extracted = F / (dΦ/dt) = **`2.665505e-09` N·s/V**
- k_documented (COUPLING_K) = **`2.670000e-09` N·s/V**
- |diff|  = **`4.495e-12`**
- rel_err = **`0.1683%`**

## Notes

COUPLING_K = 2.67e-9 N·s/V is the brane-lensing geometric factor in Faraday-induction units, derived from the multi-layer Snell's-law cascade through `[φ, χ, n₃]`. Internal consistency across all 5 PhaseII samples is the strongest empirical claim of the AEON-M v2.1 paper: one k, five thrust/flux pairs, no per-sample re-tuning.
