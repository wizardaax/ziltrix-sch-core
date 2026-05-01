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
    """Public summary contains constants + series + validation."""
    s = aeon_summary()
    assert "constants" in s
    assert "thrust_series" in s
    assert "validation" in s
    assert s["constants"]["phi"] == PHI
    assert len(s["thrust_series"]) == 5
    assert s["validation"]["matched"] is True


def test_phaseii_reference_data_intact() -> None:
    """Sanity: documented data points stayed where we left them."""
    assert len(PHASEII_DATA) == 5
    # First row: t=0, Φ=1.81e-4, dΦ/dt=-28.7, F=-7.65e-8
    t, phi, dpd, F = PHASEII_DATA[0]
    assert t == 0.0
    assert math.isclose(phi, 1.81e-4, rel_tol=1e-9)
    assert math.isclose(dpd, -28.7, rel_tol=1e-9)
    assert math.isclose(F, -7.65e-8, rel_tol=1e-9)
