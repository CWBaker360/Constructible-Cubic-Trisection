# GitHub Publication Checklist

Use this checklist when synchronizing the prepared files with the GitHub repository and creating release `v1.0.0`.

## Repository identity

- Repository name: `constructible-cubic-trisection`
- Description: `A constructible cubic error cascade for approximate angle trisection.`
- Default branch: `main`
- Release tag: `v1.0.0`
- Release title: `A Constructible Cubic Error Cascade for Approximate Angle Trisection - v1.0.0`

## Required files

Confirm that GitHub contains the current versions of:

```text
README.md
CITATION.cff
CHANGELOG.md
LICENSE
LICENSE-PAPER.md
LICENSE_NOTICE.MD
REPRODUCIBILITY.md
MANIFEST.txt
SHA256SUMS.txt
requirements.txt
assets/Repo01_constructible-cubic-trisection.png
paper/constructible_cubic_trisection.pdf
paper/constructible_cubic_trisection.tex
scripts/verify_series.py
scripts/numerical_consistency_check.py
outputs/symbolic_verification.txt
outputs/numerical_consistency_report.txt
outputs/numerical_consistency_summary.csv
docs/abstract.md
docs/release_notes_v1.0.0.md
docs/repository_description.md
docs/revision_report_2026-07-18.md
```

## Validation

- The PDF opens and matches the current LaTeX source.
- The README image renders.
- Every relative README link opens.
- `CITATION.cff` parses without an error banner.
- The profile name and repository author are spelled `Wayne Baker`.
- The repository description and topics are entered.
- The dual-license files are present and the README scope statement matches them.
- The GitHub release is created before DOI archiving.

## Suggested topics

```text
geometry
angle-trisection
straightedge-and-compass
constructible-geometry
asymptotic-analysis
cubic-convergence
error-cascade
mathematics
```

## Release notes

Copy the contents of:

```text
docs/release_notes_v1.0.0.md
```

into the GitHub release description.
