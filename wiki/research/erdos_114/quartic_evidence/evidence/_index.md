---
name: research/erdos_114/quartic_evidence/evidence
desc: |
  Ball-arithmetic bounds proving the rotated deficit integral below -1 on every
  circle and line of both quartic collision pencils, with certified roots,
  Crofton windows, singular weights and an explicit far-field constant.
created: 2026-10-15T16:22:11Z
updated: 2026-10-15T16:22:11Z
---

# research/erdos_114/quartic_evidence/evidence

[[research/erdos_114/quartic_evidence/_index|..]]

***

The [entry point](main.py) checks the statement of the
[[research/erdos_114/quartic_evidence/_index|owning account]]: the rotated
deficit integral is below $-1$ on every circle and line of the pencils of
$z^4-\tfrac32z^2-z$ and $z^4-2z^2$. From the repository root run:

```sh
uv run --no-sync python wiki/research/erdos_114/quartic_evidence/evidence/main.py
```

It uses the repository's `tools.Checker`, python-flint arb and acb balls at
80 bits, and numpy only for approximate roots that Rouché tests then certify.
It reads no input files and writes no output. The full check covers the
tangent-chord angle range $[0,\pi/2]$ of both pencils. It takes about
forty-five minutes of one thread for each stratum, with a peak resident memory
near 51 MB. `--only double` or `--only equal` restricts the check to one
stratum, so the two strata can run as separate processes. `--quick` checks
four boxes of each pencil and the controls in a few seconds.

The program prints, for each stratum, the number of boxes and pieces and the
largest upper bound over its boxes. Every box must have an upper bound below
$-1$; a box that fails is bisected, at most six times, and the boxes must tile
the range. Controls on the box $[0,10^{-4}]$, which contains the line, check
that the upper and lower bounds are ordered and less than $1/2$ apart, and
that they enclose the value of the integral on the line computed separately
by floating-point quadrature, $-1.7075$ for the double critical point and
$-2.3963$ for equal values. The second is a negative control: no target
below that value can pass on that box. Tolerances affect only how many pieces
are used. A failed certificate, a nonfinite enclosure or an inverted piece
makes the box fail rather than pass.

The [landscape probe](landscape.py), enrolled as an entry point, recomputes
in floating point the exploratory observations of the sketch in a few
seconds, including the identities (14) and (15) at sample shapes, the
critical equilateral shape, the cubic analogue and the convexity of the length
in the gaps between the critical values, also in degrees five and six.
It also compares the full second-variation formulas of
[[theory/polynomials/L178_quartic_length_variation/_index|L178]] with finite
differences at two shapes. For the angular-gap Hessian the step is at most
one fiftieth of the smallest gap and the error is scaled by the Hessian's
largest entry; derivatives in these coordinates can be large near a vertex.
Further checks reproduce the failed sharp moment comparison, the unequal
petal lengths and variances at the equilateral shape, and the negative
deficits observed after replacing the density by twice the Euclidean norm
of the inverse derivatives, at six regular shapes and sixty angles on
each collision pencil. None of these samples covers a parameter region.
Run it with:

```sh
uv run --no-sync python wiki/research/erdos_114/quartic_evidence/evidence/landscape.py
```

Its checks only confirm that the recorded observations still come out of the
stated double-precision computation; they bound nothing.

The program does not check identity (10), the parametrization of the strata
by the pencils, or the estimates (a) to (d) of the
[[research/erdos_114/quartic_critical_values|quartic sketch]], which proves
them. This is author evidence, not an independent examination.
