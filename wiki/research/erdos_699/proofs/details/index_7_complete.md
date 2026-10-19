---
name: research/erdos_699/proofs/details/index_7_complete
title: "Erdős 699: complete exclusion at index seven"
desc: "Adjusted Padé blocks and complete numerical source covers meet the finite exclusion, proving the original common-prime assertion for every admissible triple at index seven."
created: 2026-09-22T18:08:22Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: complete exclusion at index seven

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[Complete cutoff ten](../../archive/previous_bounds/cutoff_10.md)

***

**Theorem.** For every $7<j\le n/2$, a prime $p\ge7$ divides both
$\binom n7$ and $\binom nj$.

There is no remaining exceptional set at seven. The
[combined checker](../../computations/erdos_699_index_7_complete.py)
and [proof record](../../computations/erdos_699_index_7_complete.json)
join the numerical infinite tail to the completed finite exclusion.
This is a computer-assisted proof using exact integer and rational
certificates and directed analytic bounds.

## The two ranges meet

Write $h=n-6$. The proof has the following numerical requirements:

| Component | Certified range |
| --- | --- |
| All five initial cofactor alternatives | $h\ge10^{100000000}$ |
| All 258 joint cofactor inequalities | $h\ge10^{100000000}$ |
| Complete polynomial coverage | $h\ge10^{99990923}$ |
| Finite exclusion | $n\le10^{100000001}$ |

The first three rows exclude every bad triple with
$n-6\ge10^{100000000}$. If $n>10^{100000001}$, this height condition
certainly holds. Every smaller row is covered by the fourth row.
Thus all admissible rows and columns are excluded.

The prime threshold is the original $p\ge i$. In particular, seven
is allowed as a common prime, and the selected smaller primes are
exactly $2,3,5$.

## Choosing the approximation index

The decisive numerical improvement is the
[block adjustment lemma](../../methods/details/pade_block_adjustment.md).
A source clause has the form

$$
\sum_p(g_p+b_pe_p)_+\ge R,
$$

with intercepts constructed using a nominal block parameter $t$.
For a smaller integer Padé index $m\le t x$, where $x=\log h$,
failure of the clause bounds the residual denominator cost by

$$
D_m(x)\le\bigl(Rx-\kappa(tx-m)\bigr)_+,
$$

where $\kappa$ is an explicit lower bound for the relevant seed-prime
coefficients. The decrease in denominator cost compensates for using
a smaller approximant. The retained cofactor clause and its polynomial
proof remain unchanged.

For a fixed $m$, the two logarithmic Padé error bounds become maxima
of finitely many affine functions of $x$. Strict endpoint inequalities
therefore certify a whole interval of heights. Complete chains of such
intervals reach the previously proved uniform analytic tails.

For an initial pair alternative, its negation gives an explicit box
of cofactor upper bounds. Evaluating the denominator cost directly on
that box also permits indices larger than the old nominal block.

## Every analytic source is covered

The [initial-source proof](index_7_initial_height_cover.md)
uses the three already sufficient numerical sources and two complete
boxed interval chains for the remaining $(2,5)$ alternatives. These
chains contain **122868 witnesses**, all retained. Their pointwise gcd
bounds and interval inequalities were independently replayed.

The [joint-source checker](../../computations/erdos_699_index_7_height_cover.py)
and [certificate](../../computations/erdos_699_index_7_height_cover.json)
cover all 258 joint clauses:

- **43** hold directly at the target height by adjusted uniform estimates.
- **215** are covered by **9811438** exact witnesses, in 187 direction groups.

The combined checker separately regenerates the target-height gcd
and numerical certificates for the 43 direct sources. It verifies that
the direct and interval-covered source identifiers partition all 258
clauses, with the exact thresholds used by the polynomial forest.

The joint interval calculation uses a compact directed prime-log prefix
through $10^{10}$ and proper prime powers through $10^{14}$. The
[prime-power lemma](../../methods/details/prime_power_gcd.md) supplies a common
divisor for both adjacent Padé rectangles. Larger prime intervals use
the [retained explicit Chebyshev bounds](../../methods/details/sharp_theta_gcd.md).
Only selected approximation indices are needed; each one certifies its
entire interval of real logarithmic heights.

Pair gaps are at most six. For an arithmetic progression of positions
in $\{0,\ldots,6\}$, the integer step has absolute value at most three,
so the product gap is at most nine. Actual gap zero is allowed by the
same nonzero-integer argument.

The joint generator checks every accepted interval with exact arithmetic
and retains the endpoints, counts, and a SHA-256 digest of each full
witness sequence. The combined checker regenerates every sequence by
default, through the generator's replay mode, and compares each count and
digest with the record; its `--quick` option checks only the source and
endpoint bindings and reports that reduced coverage.

## Polynomial and finite certificates

The [relaxed polynomial forest](../../computations/erdos_699_index_7_relaxed_sources.py)
covers all 540 distinct-position and minimal-cofactor cases, with 3388
exact rational Farkas leaves. Coincident positions and the central column
are covered by the reductions in the
[original effective proof](index_7_effective.md).

The [Newton-basis coefficient estimates](index_7_polynomial_bounds.md)
give the weighted bound

$$
\frac{40482625000000}{404863}<99990923.
$$

[Arithmetic nonvanishing](index_7_nonvanishing.md)
eliminates the previous common-zero height obstruction. Three modular
sections and local tangent calculations show that their integer lifts
have no simultaneous integral zero outside the interpolation grid.
The retained interpolation ranks remain in force.

The [finite proof](index_7_finite.md) first applies
prime-pair bounds of exponent $.44$, then $.47$, and then three-prime
CRT bounds. These reduce the cap successively to $10^{132427}$,
$10^{2057}$, and $10^{40}$. The final interval partition has
**18000 certified intervals** and **28 residual rows**, all at most 26250.
Exactly **41740 admissible columns** in those rows are excluded by integer
binomial gcd calculations. The extension to $10^{100000001}$ reuses
the earlier finite certificates and adds eight exponent anchors for
each of the three prime pairs.

## Reproduction and scope

With the [retained dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt)
available, run:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_7_complete.py
```

The combined checker verifies the exact relaxed forest, every retained
initial-source interval inequality, the direct joint-source constants,
the joint interval bindings, the overlap with the completed finite
range, and, unless `--quick` is given, the full joint witness replay. It
names its inputs by basename as its own run record and validates each by
its domain and coverage. The individual
source drivers provide the gcd replays. No interpolation rank is
recomputed by the combined checker.

Together with the [complete proof at nine](cutoff_9.md),
this settles $i=1,2,7$ and every $i\ge9$. The indices $4,5,6,8$
still lack effective row bounds here, and global finiteness at three
remains open.
