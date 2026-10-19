---
name: research/erdos_699/proofs/details/index_9_complete
title: "Erdős 699: complete exclusion at index nine"
desc: "Complete Padé source covers meet the finite exclusion, proving the original common-prime assertion for every admissible triple at index nine."
created: 2026-09-22T18:41:46Z
updated: 2026-10-13T05:28:09Z
---

# Erdős 699: complete exclusion at index nine

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[Complete index seven](index_7_complete.md)

***

**Theorem.** For every $9<j\le n/2$, a prime $p\ge9$ divides both
$\binom n9$ and $\binom nj$.

There is no remaining exceptional set at nine. The
[combined checker](../../computations/erdos_699_index_9_complete.py)
and [proof record](../../computations/erdos_699_index_9_complete.json)
join the complete numerical infinite tail to the finite exclusion.
This is a computer-assisted proof using exact integer and rational
certificates and directed analytic bounds.

## The two ranges meet

Put $h=n-8$. Every ingredient of the infinite-tail proof now applies
at the same height:

| Component | Certified range |
| --- | --- |
| Nineteen initial pair alternatives and four ordinary AP sources | $h\ge10^{241547627}$ |
| All 790 joint cofactor clauses | $h\ge10^{241547627}$ |
| Complete polynomial coverage | $h\ge10^{241547627}$ |
| Finite exclusion | $n\le10^{241547629}$ |

The first three rows exclude every bad triple with
$n-8\ge10^{241547627}$. If $n>10^{241547629}$, this condition certainly
holds. The fourth row handles every smaller row, so the ranges leave
no gap.

The prime threshold is the original $p\ge i$. At index nine the
selected smaller primes are exactly $2,3,5,7$.

## Complete coverage of the analytic sources

The [initial-source proof](index_9_initial_height_cover.md)
establishes eleven pair sources implying all nineteen weakened baseline
alternatives, together with the four ordinary arithmetic-progression
sources. Its complete interval chains contain **299324 witnesses**.
Every interval inequality and endpoint is checked again by the combined
checker. The symmetric $(3,7)$ pair already has a sufficient uniform
tail and needs no additional interval.

For the joint clauses, the
[new height-cover driver](../../computations/erdos_699_index_9_height_cover.py)
and [certificate](../../computations/erdos_699_index_9_height_cover.json)
give the following partition:

- **440 clauses** hold directly at the target height by adjusted uniform
  estimates. They include all 224 clauses whose earlier uniform bounds
  were already sufficient.
- **350 clauses** are covered by **11599987 interval witnesses**, grouped
  into 321 direction triples. Every chain reaches a verified uniform
  tail: 19 use the earlier bound and 331 use the adjusted bound.

The combined checker independently regenerates every direct-target
numerical certificate and its analytic coefficient-gcd bound. It also
regenerates the uniform bound selected at the end of each interval chain.
It checks that the direct and interval-covered identifiers partition
all 790 clauses, with exactly the individual threshold weakenings used
by the polynomial forest.

The [block adjustment lemma](../../methods/details/pade_block_adjustment.md)
allows the source heights to be lowered without changing the cofactor
clauses. A clause has the form

$$
\sum_p(g_p+b_pe_p)_+\ge R,
$$

with nominal block parameter $t$. If $x=\log h$ and $m\le tx$, failure
of the clause bounds the residual denominator cost by

$$
D_m(x)\le\bigl(Rx-\kappa(tx-m)\bigr)_+.
$$

Here $\kappa$ is a directed lower bound for the relevant seed-prime
coefficients. At a fixed integer $m$, the logarithmic error estimates
are maxima of finitely many affine functions of $x$. Strict endpoint
inequalities therefore certify entire intervals of real heights.
For initial sources, evaluating the residual denominator cost directly
on the prescribed cofactor box also permits larger approximation indices.

The joint calculation uses a compact directed prime-log prefix through
$10^{10}$ and proper prime powers through $10^{14}$. The
[prime-power gcd lemma](../../methods/details/prime_power_gcd.md) supplies the
common coefficient divisor for both adjacent Padé rectangles. Larger
prime intervals use the
[retained explicit Chebyshev bounds](../../methods/details/sharp_theta_gcd.md).
The retained joint estimates allow pair gaps through eight and product
gaps through 64, with maximum shift eight. Actual gap zero is permitted
by the nonzero-integer argument.

Every accepted joint interval was checked with exact arithmetic during
construction. The joint certificate retains the first and last witnesses,
the count, and a SHA-256 digest of each complete witness sequence.
The combined checker regenerates every sequence by default, running the
generator to a separate output, and compares each count and digest with
the certificate; its `--quick` option checks only the source bindings and
endpoints and reports that reduced coverage. The initial-source certificate,
by contrast, retains every individual witness, so its complete interval
inequalities are checked by the combined verifier. Its optional gcd
replay separately reconstructs the pointwise prime sums.

## Polynomial coverage and the finite range

The [relaxed baseline](../../computations/erdos_699_index_9_relaxed_baseline.py)
uses all 128 retained polynomial certificates. It covers 104148 of the
$9^4\cdot16=104976$ labeled position and minimal-cofactor cases,
including collisions of selected prime-power positions. The
[relaxed forest](../../computations/erdos_699_nine_relaxed_forest.py)
closes the remaining **828 cases** with **24322 exact rational Farkas
leaves**. The reductions for the central column are those of the
[original effective proof](index_9_effective.md).

The [Newton-basis coefficient bounds](../../computations/erdos_699_nine_newton_farkas_bound.py)
give the weighted leaf threshold

$$
\frac{7465512500000}{30907}<241547627.
$$

[Arithmetic nonvanishing](index_9_nonvanishing.md)
removes the two largest common-zero thresholds. The remaining common-zero
bound has exponent 162400114, and the baseline coefficient bound is
$151670000/17$. Both lie below the stated polynomial height. The
interpolation ranks remain unchanged; the combined checker uses their
retained certificates.

The [finite proof](index_9_finite.md) excludes every
$n\le10^{241547629}$. Prime-pair estimates with cofactor exponents
$41/100$ and then $9/20$ reduce a hypothetical bad row to $n<10^{26}$.
The final partition contains **607975 certified intervals** and
**thirteen residual rows**, all at most 5832. Exact binomial gcd
calculations exclude all **6762 admissible columns** in those rows.
The terminal-prime lemma handles the earlier prefix.

## Reproduction and scope

With the [retained dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt)
available, run:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_9_complete.py
```

The checker verifies the full source partition, the numerical source
constants and selected uniform tails, every retained initial interval,
the joint endpoint bindings, all exact forest leaves, the finite-proof
bindings, the overlap of the two ranges, and, unless `--quick` is given,
the full joint witness replay. The proof record names its inputs by
basename as its own run record; the checker validates each input by its
domain and coverage. The
initial-source driver reconstructs the individual prime sums. No
interpolation rank is recomputed by the combined checker.

Together with the earlier cutoff-ten result, this proves the original
assertion for every $i\ge9$. The completed index-seven proof is separate.
This argument does not establish global finiteness at index three.
