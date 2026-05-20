---
agent: agent_07 Field Weaver (Snell-Vern)
topic: gate_activation
params: {"case": "\u03c4 above, d\u03c8 below", "case_id": 2}
generated_at: 2026-05-20T00:59:08.222307+00:00
library: aeon_engine (AEON-M v2.1)
---

# Dynamic-gate activation: τ above, dψ below

## Claim

AEON-M v2.1 dynamic gate: `(τ > 0.007) AND (|dψ/dt| > 1.5·σ)`. Activates only when BOTH thresholds are crossed simultaneously.

## Case: τ above, dψ below

| param | value | threshold | crosses? |
|---|---|---|---|
| τ      | `0.01`   | `> 0.007`     | **True** |
| |dψ/dt|| `0.5`  | `> 1.5·σ = 1.5` | **False** |

- expected gate state: **False**
- computed gate state: **False**
- agrees? **True**

## Notes

Both conditions must hold. The AND prevents activation from a single loud-but-slow ψ excursion (τ-only crossing) or a fast-but-quiet jitter (dψ-only crossing). Real propulsion events leave both signatures.
