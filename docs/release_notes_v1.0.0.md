# A Constructible Cubic Error Cascade for Approximate Angle Trisection - v1.0.0

This release archives the first complete research-source version of Wayne Baker's preprint *A Constructible Cubic Error Cascade for Approximate Angle Trisection*.

## Principal result

The paper develops a finite straightedge-and-compass approximation to one third of an angle and proves the local laws

```tex
D(\theta)-\frac{\theta}{3}
=
\frac{7}{10368}\theta^3+O(\theta^5),
```

and

```tex
\mathscr R(e)
=
-\frac{7}{384}e^3+O(e^5).
```

The resulting finite-stage local error orders are

```text
3 -> 9 -> 27 -> 81 -> ...
```

The work does not claim exact trisection of an arbitrary angle.

## Included material

- compiled preprint PDF and LaTeX source;
- repository infographic;
- exact symbolic verification script;
- 100-decimal-digit numerical consistency script;
- committed text and CSV reference outputs;
- citation and reproducibility metadata;
- supporting publication documentation.

## Citation

Use the repository's **Cite this repository** control, generated from `CITATION.cff`. A DOI will be added to the citation metadata after archival.
