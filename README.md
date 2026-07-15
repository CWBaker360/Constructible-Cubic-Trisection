# A Constructible Cubic Error Cascade for Approximate Angle Trisection

**Author:** Wayne Baker  
**Repository:** `constructible-cubic-trisection`  
**Version:** 1.0.0  
**Date:** July 2026  
**Status:** Preprint / Research Source Archive

---

## Overview

This repository contains the complete research source for the paper

> **A Constructible Cubic Error Cascade for Approximate Angle Trisection**

including the LaTeX manuscript, compiled PDF, and supporting documentation.

The paper develops a straightedge-and-compass construction that produces a constructible approximation \(D(\theta)\) to one third of an arbitrary angle \(\theta\), together with a constructible residual refinement whose local convergence is cubic.

Rather than claiming an exact Euclidean trisection, the work establishes an arbitrarily refinable constructible approximation and proves the local cubic error law governing the refinement process.

---

# Paper

### Compiled manuscript

- [`paper/constructible_cubic_trisection.pdf`](paper/constructible_cubic_trisection.pdf)

### LaTeX source

- [`paper/constructible_cubic_trisection.tex`](paper/constructible_cubic_trisection.tex)

---

# Principal Results

The principal local asymptotic results are

\[
D(\theta)-\frac{\theta}{3}
=
\frac{7}{10368}\theta^3
+
O(\theta^5),
\]

where angles are measured in radians throughout the asymptotic analysis.

The constructible residual correction operator is

\[
\mathscr{R}(e)
=
e
-
2\arcsin\!\left(
\frac43\sin\frac{3e}{8}
\right),
\]

whose local expansion is

\[
\mathscr{R}(e)
=
-\frac{7}{384}e^3
+
O(e^5).
\]

Consequently,

- **Seed approximation:** \(O(\theta^3)\)
- **First refinement:** \(O(\theta^9)\)
- **Second refinement:** \(O(\theta^{27})\)

demonstrating cubic error propagation under repeated refinement.

---

# Scope

This work **does not** claim an exact straightedge-and-compass trisection of an arbitrary angle.

The classical impossibility theorem remains unchanged.

Instead, it develops an arbitrarily refinable constructible approximation together with a rigorously derived local cubic refinement law.

The trigonometric expressions appearing in the analysis provide an analytic model of Euclidean constructions involving

- angle copying,
- angle bisection,
- projection lengths,
- similar triangles,
- and right-triangle constructions.

---

# Analytic Domain

The residual operator

\[
\mathscr{R}(e)
=
e
-
2\arcsin\!\left(
\frac43\sin\frac{3e}{8}
\right)
\]

is defined whenever

\[
\left|
\frac43
\sin\frac{3e}{8}
\right|
\le
1.
\]

This domain contains the local convergence region analyzed throughout the paper.

---

# Repository Layout

## Top-level files

- `README.md`
- `LICENSE`
- `LICENSE-PAPER.md`
- `LICENSE-NOTICE.md`
- `CITATION.cff`
- `CHANGELOG.md`
- `REPRODUCIBILITY.md`
- `.gitignore`

## Paper

- `paper/constructible_cubic_trisection.pdf`
- `paper/constructible_cubic_trisection.tex`
- `paper/README.md`

## Documentation

- `docs/abstract.md`
- `docs/github_upload_checklist.md`
- `docs/repository_description.md`

## Supplementary directories

- `figures/`
- `scripts/`

---

# Building the Paper

Compile from inside the `paper` directory.

```bash
pdflatex constructible_cubic_trisection.tex
pdflatex constructible_cubic_trisection.tex
```

Running LaTeX twice ensures that references, labels, and cross-references are fully resolved.

---

# Citation

Repository citation metadata is provided in

```text
CITATION.cff
```

GitHub automatically uses this file to generate the **Cite this repository** feature.

---

# Licensing

This repository contains both research documents and software.

## Research documents

The paper, figures, documentation, and supplementary written material are licensed under the

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

## Source code

All source code contained in this repository is licensed under the

**MIT License**

See

- `LICENSE`
- `LICENSE-PAPER.md`
- `LICENSE-NOTICE.md`

for the complete licensing terms.

---

# Related Work

The broader proportional-subtended refinement theory developed within the **Geometric Approximation Theory** framework is presented in

> **A Local Cubic Refinement Law for Proportional-Subtended Angle Division**

Repository:

<https://github.com/CWBaker360/proportional-subtended-cubic-refinement>

---

# Independent Analysis

An independent mathematical analysis of the construction is available from **Rouben Rostamian** (University of Maryland, Baltimore County).

- *An Angle Trisection — Wayne Baker's Construction*
- *Interactive Modular Trisection App*

<https://userpages.umbc.edu/~rostamia/Geometry/trisect-baker.html>

<https://userpages.umbc.edu/~rostamia/Geometry/trisect-baker-javascript.html>

---

# Copyright

© 2026 Wayne Baker

Part of the **Geometric Approximation Theory** research series.
