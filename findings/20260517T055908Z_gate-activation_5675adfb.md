---
agent: agent_07 Field Weaver (Snell-Vern)
topic: gate_activation
params: {"case": "\u03c4 above, d\u03c8 above", "case_id": 3}
generated_at: 2026-05-17T05:59:08.774326+00:00
library: aeon_engine (AEON-M v2.1)
---

# Dynamic-gate activation: τ above, dψ above

## Claim

AEON-M v2.1 dynamic gate: `(τ > 0.007) AND (|dψ/dt| > 1.5·σ)`. Activates only when BOTH thresholds are crossed simultaneously.

## Case: τ above, dψ above

| param | value | threshold | crosses? |
|---|---|---|---|
| τ      | `0.01`   | `> 0.007`     | **True** |
| |dψ/dt|| `3.0`  | `> 1.5·σ = 1.5` | **True** |

- expected gate state: **True**
- computed gate state: **True**
- agrees? **True**

## Notes

Both conditions must hold. The AND prevents activation from a single loud-but-slow ψ excursion (τ-only crossing) or a fast-but-quiet jitter (dψ-only crossing). Real propulsion events leave both signatures.
