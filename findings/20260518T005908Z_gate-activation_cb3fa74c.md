---
agent: agent_07 Field Weaver (Snell-Vern)
topic: gate_activation
params: {"case": "\u03c4 below, d\u03c8 below", "case_id": 0}
generated_at: 2026-05-18T00:59:08.764817+00:00
library: aeon_engine (AEON-M v2.1)
---

# Dynamic-gate activation: τ below, dψ below

## Claim

AEON-M v2.1 dynamic gate: `(τ > 0.007) AND (|dψ/dt| > 1.5·σ)`. Activates only when BOTH thresholds are crossed simultaneously.

## Case: τ below, dψ below

| param | value | threshold | crosses? |
|---|---|---|---|
| τ      | `0.005`   | `> 0.007`     | **False** |
| |dψ/dt|| `0.5`  | `> 1.5·σ = 1.5` | **False** |

- expected gate state: **False**
- computed gate state: **False**
- agrees? **True**

## Notes

Both conditions must hold. The AND prevents activation from a single loud-but-slow ψ excursion (τ-only crossing) or a fast-but-quiet jitter (dψ-only crossing). Real propulsion events leave both signatures.
