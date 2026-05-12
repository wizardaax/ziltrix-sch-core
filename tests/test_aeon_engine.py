"""Tests for AEON Engine v2.1 distillation.

Validates that the runnable module reproduces the documented PhaseII
simulation data (June 4 2025) within 1% relative error, and that the
framework constants match their derivations.
"""

from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aeon_engine import (
    ALPHA_INV,
    CHEVRON_ANGLE_RAD,
    CHI,
    COUPLING_K,
    DRIVE_FREQ_HZ,
    GOLDEN_ANGLE_DEG,
    N3_MEDIUM,
    OMEGA_N,
    PHASEII_DATA,
    PHI,
    PSI_RESONANCE,
    aeon_brane_state,
    aeon_gate_from_coherence_history,
    aeon_gate_state,
    aeon_summary,
    aeon_thrust_series,
    base_brane_layers,
    dynamic_gate,
    dynamic_layers,
    snells_refraction,
    thrust_from_dphi_dt,
    validate_against_phaseii,
)


def test_phi_constant() -> None:
    assert math.isclose(PHI, (1 + math.sqrt(5)) / 2, rel_tol=1e-15)


def test_golden_angle_derivation() -> None:
    assert math.isclose(GOLDEN_ANGLE_DEG, 360.0 / (PHI ** 2), rel_tol=1e-15)
    # Documented: ≈ 137.508°
    assert 137.5 < GOLDEN_ANGLE_DEG < 137.51


def test_n3_medium_derivation() -> None:
    # n3 = α⁻¹ / ψ ≈ 0.952 (per AEON-M v2.1)
    assert math.isclose(N3_MEDIUM, ALPHA_INV / PSI_RESONANCE, rel_tol=1e-15)
    assert 0.95 < N3_MEDIUM < 0.96


def test_drive_freq_consistent_with_omega() -> None:
    # ωₙ = 2π · f
    assert math.isclose(DRIVE_FREQ_HZ * 2 * math.pi, OMEGA_N, rel_tol=1e-9)
    # ≈ 3.8 MHz
    assert 3.7e6 < DRIVE_FREQ_HZ < 3.9e6


def test_chevron_chi_derivation() -> None:
    assert math.isclose(CHI, 2 * math.pi / CHEVRON_ANGLE_RAD, rel_tol=1e-15)


def test_thrust_reproduces_phaseii_data() -> None:
    """The headline test: distillation matches documented June 4 2025 results."""
    samples = aeon_thrust_series()
    val = validate_against_phaseii(samples, rel_tol=0.01)  # 1% tolerance
    assert val["matched"] is True, f"Failed validation: {val}"
    assert val["max_rel_err"] < 0.01


def test_thrust_sign_convention() -> None:
    """Negative dΦ/dt produces negative thrust (matches documented PhaseII)."""
    f = thrust_from_dphi_dt(-100.0)
    assert f < 0


def test_thrust_proportional_to_dphi_dt() -> None:
    """F / (dΦ/dt) is constant — Faraday induction holds across the series."""
    samples = aeon_thrust_series()
    ratios = [s.thrust / s.dphi_dt for s in samples if s.dphi_dt != 0]
    # All ratios should equal COUPLING_K to high precision.
    for r in ratios:
        assert math.isclose(r, COUPLING_K, rel_tol=1e-12)


def test_snells_refraction_identity_for_uniform_medium() -> None:
    """Refraction through identical layers is the identity map."""
    theta_in = 0.5
    theta_out = snells_refraction(theta_in, [1.0, 1.0, 1.0])
    assert math.isclose(theta_out, theta_in, rel_tol=1e-12)


def test_snells_refraction_clipping() -> None:
    """Total-internal-reflection regime: clipped to ±π/2."""
    # Going from very dense (n1=10) to very rare (n2=1) at large angle
    theta = snells_refraction(1.5, [10.0, 1.0])
    assert -math.pi / 2 <= theta <= math.pi / 2


def test_base_brane_layers() -> None:
    layers = base_brane_layers()
    assert len(layers) == 3
    assert layers[0] == PHI
    assert math.isclose(layers[1], CHI, rel_tol=1e-12)
    assert math.isclose(layers[2], N3_MEDIUM, rel_tol=1e-12)


def test_dynamic_layers_modulation() -> None:
    """n_i(t) = n_base + 0.1 · ψ(t) per AEON-M v2.1."""
    layers0 = dynamic_layers(0.0)
    layers1 = dynamic_layers(1.0)
    base = base_brane_layers()
    for n0, b in zip(layers0, base):
        assert math.isclose(n0, b, rel_tol=1e-12)
    for n1, b in zip(layers1, base):
        assert math.isclose(n1, b + 0.1, rel_tol=1e-12)


def test_dynamic_gate_both_conditions_required() -> None:
    """Gate fires only when τ > 0.007 AND |dψ/dt| > 1.5σ."""
    # Both pass
    assert dynamic_gate(0.01, 1.0, 0.5) is True  # 1.0 > 1.5·0.5 = 0.75? Yes
    # τ fails
    assert dynamic_gate(0.005, 1.0, 0.5) is False
    # dpsi_dt fails
    assert dynamic_gate(0.01, 0.5, 0.5) is False  # 0.5 < 1.5·0.5 = 0.75


def test_aeon_summary_complete() -> None:
    """Public summary contains constants + series + validation + v2.1 fields."""
    s = aeon_summary()
    assert s["version"] == "v2.1"
    assert "constants" in s
    assert "thrust_series" in s
    assert "validation" in s
    assert "brane_geometry" in s
    assert "dynamic_gate" in s
    assert s["constants"]["phi"] == PHI
    assert len(s["thrust_series"]) == 5
    assert s["validation"]["matched"] is True


def test_aeon_brane_state_v21_shape() -> None:
    """v2.1 brane geometry snapshot exposes base + dynamic stacks and shift."""
    b = aeon_brane_state()
    assert b["base_layers"] == base_brane_layers()
    assert len(b["dynamic_layers"]) == 3
    # ψ_t=1.0 default → each dynamic layer = base + 0.1
    for d, base in zip(b["dynamic_layers"], b["base_layers"]):
        assert math.isclose(d, base + 0.1, rel_tol=1e-12)
    # Snell angle through identical-φ first-pair is identity → small for π/4 input
    assert -math.pi / 2 <= b["snell_angle_base_rad"] <= math.pi / 2
    assert -math.pi / 2 <= b["snell_angle_dynamic_rad"] <= math.pi / 2
    # Shift between base and dynamic should be finite and small
    assert abs(b["snell_shift_deg"]) < 90.0


def test_aeon_gate_state_v21_thresholds() -> None:
    """v2.1 dynamic-gate snapshot reports both activation conditions."""
    g = aeon_gate_state()  # defaults: tau=0.01, dpsi_dt=0.199, sigma=1.0
    assert g["tau_threshold"] == 0.007
    assert g["tau_above"] is True  # 0.01 > 0.007
    assert math.isclose(g["dpsi_dt_threshold"], 1.5, rel_tol=1e-12)
    assert g["dpsi_dt_above"] is False  # 0.199 < 1.5
    assert g["gated_active"] is False  # only one condition met
    # When both pass → gate active
    g2 = aeon_gate_state(tau=0.01, dpsi_dt=2.0, sigma_dpsi_dt=1.0)
    assert g2["gated_active"] is True


def test_aeon_gate_from_history_insufficient() -> None:
    """Live gate falls back to documented defaults when history < 3."""
    g = aeon_gate_from_coherence_history([0.5, 0.6])
    assert g["source"] == "insufficient_history"
    assert g["history_n"] == 2
    # Falls back to documented defaults
    assert g["tau"] == 0.01


def test_aeon_gate_from_history_constant_series() -> None:
    """Constant coherence → τ=0, σ tiny, gate τ-condition fails."""
    series = [0.7] * 10  # 10 cycles, all 0.7
    g = aeon_gate_from_coherence_history(series, dt=1.0, window=5)
    assert g["source"] == "live"
    assert math.isclose(g["tau"], 0.0, abs_tol=1e-12)
    assert g["tau_above"] is False  # 0.0 not > 0.007
    # dψ/dt is also 0 → not above 1.5σ either
    assert g["gated_active"] is False


def test_aeon_gate_from_history_realistic() -> None:
    """Realistic ramp produces meaningful τ and dψ/dt values."""
    # Coherence climbing from 0.5 → 0.9 over 12 cycles (real-looking ramp)
    series = [0.50, 0.52, 0.55, 0.58, 0.62, 0.66, 0.70, 0.74, 0.78, 0.82, 0.86, 0.90]
    g = aeon_gate_from_coherence_history(series, dt=60.0, window=5)
    assert g["source"] == "live"
    assert g["history_n"] == 12
    assert g["ma_window"] == 5
    assert g["last_coherence"] == 0.90
    assert g["prev_coherence"] == 0.86
    # τ = |0.90 - 0.86| = 0.04 — well above 0.007
    assert math.isclose(g["tau"], 0.04, rel_tol=1e-9)
    assert g["tau_above"] is True
    # Monotone increasing ramp → positive dψ/dt
    assert g["dpsi_dt"] > 0


def test_phaseii_reference_data_intact() -> None:
    """Sanity: documented data points stayed where we left them."""
    assert len(PHASEII_DATA) == 5
    # First row: t=0, Φ=1.81e-4, dΦ/dt=-28.7, F=-7.65e-8
    t, phi, dpd, F = PHASEII_DATA[0]
    assert t == 0.0
    assert math.isclose(phi, 1.81e-4, rel_tol=1e-9)
    assert math.isclose(dpd, -28.7, rel_tol=1e-9)
    assert math.isclose(F, -7.65e-8, rel_tol=1e-9)
