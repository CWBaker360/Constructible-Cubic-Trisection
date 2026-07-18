#!/usr/bin/env python3
"""Reproduce the numerical consistency table with high precision."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import mpmath as mp


ANGLES_DEG = ("1", "60", "120", "210")


def compute_rows() -> list[dict[str, str]]:
    mp.mp.dps = 100
    rows: list[dict[str, str]] = []

    for angle_text in ANGLES_DEG:
        degrees = mp.mpf(angle_text)
        theta = mp.radians(degrees)

        d = 2 * mp.asin(mp.mpf(4) / 3 * mp.sin(theta / 8))
        i = d - 2 * mp.asin(mp.mpf(4) / 3 * mp.sin((3 * d - theta) / 8))
        m = i - 2 * mp.asin(mp.mpf(4) / 3 * mp.sin((3 * i - theta) / 8))

        errors = (
            abs((d - theta / 3) * 180 / mp.pi),
            abs((i - theta / 3) * 180 / mp.pi),
            abs((m - theta / 3) * 180 / mp.pi),
        )

        rows.append(
            {
                "theta_degrees": angle_text,
                "seed_error_degrees": mp.nstr(errors[0], 18),
                "first_correction_error_degrees": mp.nstr(errors[1], 18),
                "second_correction_error_degrees": mp.nstr(errors[2], 18),
            }
        )

    return rows


def write_outputs(rows: list[dict[str, str]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    report_path = output_dir / "numerical_consistency_report.txt"
    csv_path = output_dir / "numerical_consistency_summary.csv"

    lines = [
        "Numerical consistency check",
        "Working precision: 100 decimal digits",
        "Errors are absolute and expressed in degrees.",
        "",
        "theta_deg  seed_error_deg        first_error_deg       second_error_deg",
    ]
    for row in rows:
        lines.append(
            f"{row['theta_degrees']:>9}  "
            f"{row['seed_error_degrees']:<20}  "
            f"{row['first_correction_error_degrees']:<20}  "
            f"{row['second_correction_error_degrees']}"
        )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Directory for the text and CSV outputs (default: outputs).",
    )
    args = parser.parse_args()

    rows = compute_rows()
    write_outputs(rows, args.output_dir)

    for row in rows:
        print(
            row["theta_degrees"],
            row["seed_error_degrees"],
            row["first_correction_error_degrees"],
            row["second_correction_error_degrees"],
        )


if __name__ == "__main__":
    main()
