# A Constructible Cubic Error Cascade for Approximate Angle Trisection

**Author:** Wayne Baker  
**Date:** July 2, 2026  
**Status:** Preprint / source archive

This repository contains the LaTeX source and supporting documentation for the paper:

**A Constructible Cubic Error Cascade for Approximate Angle Trisection**

The paper describes a straightedge-and-compass construction that produces a constructible approximation $D(\theta)$ to one third of a given angle $\theta$, together with a constructible residual correction step whose local error law is cubic.

## Main result

The seed construction satisfies

$$D(\theta)-\frac{\theta}{3}=\frac{7}{10368}\theta^3+O(\theta^5),$$

with angles measured in radians for the asymptotic formulae.

The residual correction operator is written analytically as

$$\mathscr{R}(e)=e-2\arcsin\left(\frac43\sin\frac{3e}{8}\right),$$

and has local expansion

$$\mathscr{R}(e)=-\frac{7}{384}e^3+O(e^5).$$

Consequently, repeated correction raises the local error order cubically. Starting from a seed error of order $O(\theta^3)$, the first and second corrected approximants have errors of order $O(\theta^9)$ and $O(\theta^{27})$, respectively.

## Important scope note

This work does **not** claim exact trisection of an arbitrary angle by straightedge and compass. The classical impossibility theorem remains unchanged. The result is an arbitrarily refinable constructible approximation to $\theta/3$, with a proved local cubic residual law.

The trigonometric notation in the paper is an analytic model of Euclidean operations. The construction itself is described in terms of copying and bisecting angles, representing sine values as directed projection lengths on a reference circle, scaling by similar triangles, and constructing the corresponding right-triangle angle.

## Repository layout

```text
.
├── README.md
├── CITATION.cff
├── REPRODUCIBILITY.md
├── LICENSE_NOTICE.md
├── CHANGELOG.md
├── .gitignore
├── paper/
│   ├── constructible_cubic_trisection.tex
│   └── README.md
├── docs/
│   ├── abstract.md
│   ├── github_upload_checklist.md
│   └── repository_description.md
├── figures/
└── scripts/
