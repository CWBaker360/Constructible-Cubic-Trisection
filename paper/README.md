# Paper Source

This folder contains the source and compiled preprint for:

> **A Constructible Cubic Error Cascade for Approximate Angle Trisection**

Files:

```text
constructible_cubic_trisection.tex
constructible_cubic_trisection.pdf
```

Compile with:

```bash
pdflatex constructible_cubic_trisection.tex
pdflatex constructible_cubic_trisection.tex
```

The manuscript source was revised on November 16, 2026 to integrate a scoped Lean 4/Mathlib verification section. The compiled PDF in this folder remains the earlier edition until replaced; compile the current source twice to obtain the revised manuscript. The Lean evidence supports the local cubic residual coefficient only; a combined-root clean build and fresh axiom audit are not included in the current release.

The manuscript includes exact derivations, a numerical consistency table, and compact reproducibility code. Standalone versions of the verification programs are supplied in the repository-level `scripts/` folder.
