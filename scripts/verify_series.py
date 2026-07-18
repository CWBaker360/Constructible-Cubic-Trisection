#!/usr/bin/env python3
"""Verify the exact seed and residual Maclaurin coefficients."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    x = sp.symbols("x")

    seed = 2 * sp.asin(sp.Rational(4, 3) * sp.sin(x / 8))
    residual = x - 2 * sp.asin(sp.Rational(4, 3) * sp.sin(3 * x / 8))

    seed_series = sp.series(seed, x, 0, 9)
    residual_series = sp.series(residual, x, 0, 9)

    expected_seed = (
        x / 3
        + sp.Rational(7, 10368) * x**3
        + sp.Rational(7, 884736) * x**5
        + sp.Rational(4969, 45864714240) * x**7
    )
    expected_residual = (
        -sp.Rational(7, 384) * x**3
        - sp.Rational(63, 32768) * x**5
        - sp.Rational(4969, 20971520) * x**7
    )

    assert sp.expand(seed_series.removeO() - expected_seed) == 0
    assert sp.expand(residual_series.removeO() - expected_residual) == 0

    print("Seed series:")
    print(seed_series)
    print()
    print("Residual series:")
    print(residual_series)
    print()
    print("All exact coefficient checks passed.")


if __name__ == "__main__":
    main()
