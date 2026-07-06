# A Constructible Cubic Error Cascade for Approximate Angle Trisection

**Author:** Wayne Baker
**Date:** July 2, 2026
**Status:** Preprint / source archive

This repository contains the LaTeX source and supporting documentation for the paper **A Constructible Cubic Error Cascade for Approximate Angle Trisection**.

## Read the paper

The compiled preprint PDF is available here:

- [`paper/constructible_cubic_trisection.pdf`](paper/constructible_cubic_trisection.pdf)

The LaTeX source is available here:

- [`paper/constructible_cubic_trisection.tex`](paper/constructible_cubic_trisection.tex)

The paper describes a straightedge-and-compass construction that produces a constructible approximation $D(\theta)$ to one third of a given angle $\theta$, together with a constructible residual correction step whose local error law is cubic.

## Main result

The seed construction satisfies:

$D(\theta)-\theta/3=(7/10368)\theta^3+O(\theta^5)$.

Angles are measured in radians for the asymptotic formulae.

The residual correction operator is written analytically as:

$\mathscr{R}(e)=e-2\arcsin((4/3)\sin(3e/8))$.

Its local expansion is:

$\mathscr{R}(e)=-(7/384)e^3+O(e^5)$.

Consequently, repeated correction raises the local error order cubically. Starting from a seed error of order $O(\theta^3)$, the first and second corrected approximants have errors of order $O(\theta^9)$ and $O(\theta^{27})$, respectively.

## Important scope note

This work does **not** claim exact trisection of an arbitrary angle by straightedge and compass. The classical impossibility theorem remains unchanged.

The result is an arbitrarily refinable constructible approximation to $\theta/3$, with a proved local cubic residual law.

The trigonometric notation in the paper is an analytic model of Euclidean operations. The construction itself is described in terms of copying and bisecting angles, representing sine values as directed projection lengths on a reference circle, scaling by similar triangles, and constructing the corresponding right-triangle angle.

## Repository layout

Top-level files:

* `README.md`
* `CITATION.cff`
* `REPRODUCIBILITY.md`
* `LICENSE_NOTICE.md`
* `CHANGELOG.md`
* `.gitignore`

Paper source:

* `paper/constructible_cubic_trisection.pdf`
* `paper/constructible_cubic_trisection.tex`
* `paper/README.md`

Supporting documentation:

* `docs/abstract.md`
* `docs/github_upload_checklist.md`
* `docs/repository_description.md`

Reserved folders:

* `figures/`
* `scripts/`

## Build instructions

The main source file is `paper/constructible_cubic_trisection.tex`.

A standard LaTeX installation should compile the paper. From inside the `paper` folder, run:

`pdflatex constructible_cubic_trisection.tex`

Then run it a second time:

`pdflatex constructible_cubic_trisection.tex`

Run LaTeX twice so cross-references and bibliography labels settle correctly.

## Citation

A citation file is included at `CITATION.cff`. GitHub will use this file to show a **Cite this repository** button.

## License

This repository is currently distributed under the rights notice in `LICENSE_NOTICE.md`.

Copyright © 2026 Wayne Baker. All rights reserved unless otherwise stated.

No permission is granted to reproduce, redistribute, modify, sublicense, or republish the paper text, LaTeX source, figures, or supporting documentation without written permission from the author.

If verification scripts are added later, they may be released under a separate open-source software license.
