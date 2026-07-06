# Reproducibility Notes

This repository is intended to make the paper source and supporting material easy to inspect, compile, and cite.

## Mathematical reproducibility

The paper records the following checkable components:

1. The Euclidean seed construction for an approximate trisection angle \(D(\theta)\).
2. The seed asymptotic law

   ```tex
   D(\theta)-\frac{\theta}{3}
   =
   \frac{7}{10368}\theta^3+O(\theta^5).
   ```

3. The residual correction operator

   ```tex
   \mathscr{R}(e)
   =
   e
   -
   2\arcsin\!\left(\frac43\sin\frac{3e}{8}\right).
   ```

4. The cubic residual expansion

   ```tex
   \mathscr{R}(e)
   =
   -\frac{7}{384}e^3+O(e^5).
   ```

5. The resulting cascade of local error orders

   ```text
   3, 9, 27, ...
   ```

## Numerical consistency checks

The current paper includes a numerical consistency section and reproducibility code appendix. If scripts are later separated from the paper source, place them in the `scripts/` folder and record:

- script name,
- Python version,
- command used,
- precision settings,
- input angle range,
- expected output summary.

## Recommended future archive contents

For a stronger public release, add:

```text
scripts/
  verify_seed_series.py
  verify_residual_series.py
  numerical_consistency_check.py

outputs/
  numerical_consistency_summary.csv
  numerical_consistency_report.txt
```

The first GitHub release can still be valid without these separated scripts if the reproducibility code remains included in the LaTeX appendix.
