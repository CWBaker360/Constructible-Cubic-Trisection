# Reproducibility

The principal mathematical statements are proved in the manuscript by exact formal series composition. The scripts supplied here are independent reproducibility aids; they are not substitutes for the proofs.

## Environment

Reference outputs were generated with:

```text
Python 3
SymPy 1.14.0
mpmath 1.3.0
```

Install the pinned dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

## Exact symbolic verification

Run:

```bash
python scripts/verify_series.py
```

The script checks the expansions

```tex
D(\theta)
=
2\arcsin\!\left(\frac43\sin\frac{\theta}{8}\right)
=
\frac{\theta}{3}
+\frac{7}{10368}\theta^3
+\frac{7}{884736}\theta^5
+\frac{4969}{45864714240}\theta^7
+O(\theta^9),
```

and

```tex
\mathscr R(e)
=
e-2\arcsin\!\left(\frac43\sin\frac{3e}{8}\right)
=
-\frac{7}{384}e^3
-\frac{63}{32768}e^5
-\frac{4969}{20971520}e^7
+O(e^9).
```

The committed reference output is:

```text
outputs/symbolic_verification.txt
```

## Numerical consistency table

Run:

```bash
python scripts/numerical_consistency_check.py --output-dir outputs
```

The script uses 100 decimal digits of working precision and evaluates the seed and first two residual corrections at \(1^\circ\), \(60^\circ\), \(120^\circ\), and \(210^\circ\). It writes:

```text
outputs/numerical_consistency_report.txt
outputs/numerical_consistency_summary.csv
```

The table is a consistency check only. The theorems do not depend on floating-point evidence.

## LaTeX build

From the repository root:

```bash
cd paper
pdflatex constructible_cubic_trisection.tex
pdflatex constructible_cubic_trisection.tex
```

The two passes settle internal references and citations.
