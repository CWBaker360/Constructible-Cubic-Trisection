# Abstract

We describe a straightedge-and-compass construction producing a constructible approximation \(D(\theta)\) to one third of a given angle \(\theta\). The seed approximation satisfies

```tex
D(\theta)-\frac{\theta}{3}
=
\frac{7}{10368}\theta^3+O(\theta^5),
```

where angles in asymptotic formulae are measured in radians. We then describe a Euclidean correction step, written analytically as the residual operator

```tex
\mathscr{R}(e)
=
e
-
2\arcsin\!\left(
\frac43\sin\frac{3e}{8}
\right).
```

Its local expansion is

```tex
\mathscr{R}(e)
=
-\frac{7}{384}e^3+O(e^5).
```

Thus repeated correction increases the local error order cubically. Starting from the seed error \(O(\theta^3)\), the first and second corrected angles have errors \(O(\theta^9)\) and \(O(\theta^{27})\), respectively. The trigonometric notation is an analytic model of the Euclidean construction, not a procedural call to transcendental functions. The correction step is realized by copying and bisecting angles, representing sine values as directed projection lengths on a reference circle, scaling lengths by similar triangles, and constructing the corresponding right-triangle angle. The method therefore constructs arbitrarily refinable approximants to \(\theta/3\), while the exact trisection of an arbitrary angle remains impossible in the classical straightedge-and-compass sense.
