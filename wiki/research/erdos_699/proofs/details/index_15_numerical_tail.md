---
name: research/erdos_699/proofs/details/index_15_numerical_tail
title: "Erdős 699: a fully numerical tail at index 15"
desc: "Seven explicitly bounded asymmetric prime-pair estimates strengthen the existing interpolation gain to 7993/10000 and prove n<10^15170264."
created: 2026-09-22T05:00:00Z
updated: 2026-09-22T05:17:48Z
---

# Erdős 699: a fully numerical tail at index 15

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/interpolation_extensions|The interpolation map]]

***

Every bad triple with $i=15$ satisfies the fully numerical bound

$$
\boxed{n<10^{15\,170\,264}.}
$$

This replaces the unevaluated cofactor thresholds in the earlier
interpolation argument. No new interpolation matrix is needed: its
degree-257 symmetric jet map already has full row rank, and the
nonvanishing polynomial family has total degree 962.

## Explicit cofactor constraints

Use the original explicit BFT Theorem 2.1 table and the following seven
additional asymmetric constraints. An entry $(a,b)$ for the pair $(p,q)$
means

$$
u_p\ge(n-14)^a\quad\text{or}\quad u_q\ge(n-14)^b.
$$

| Pair | Endpoint exponents | Certified factor threshold |
| --- | --- | --- |
| $(2,7)$ | $(.2734,.3201)$ | $10^{768032}$ |
| $(2,11)$ | $(.1197,.1879)$ | $10^{785060}$ |
| $(5,7)$ | $(.3613,.2277)$ | $10^{2405782}$ |
| $(7,13)$ | $(.0987,.2080)$ | $10^{484367}$ |
| $(2,5)$ | $(.2638,.2674)$ | $10^{15170263}$ |
| $(3,11)$ | $(.3414,.4249)$ | $10^{12315735}$ |
| $(11,13)$ | $(.1260,.0652)$ | $10^{8222386}$ |

The first four are retained in the
[asymmetric prime-pair table](../../computations/erdos_699_bft_asymmetric_pair_table.json).
For the last three, the oriented seed parameters $(P,Q,a,b,c,d)$ are

$$
 (128,125,1,1,53,43),\quad
 (243,121,1,2,34,25),\quad
 (13,11,1,1,69,49).
$$

The seed differences $aP-bQ$ are respectively $3,1,2$.
The prime-interval GCD estimate is applied with
$m_0=100000$ and 4000 interval terms. It supplies an exact rational lower
bound $\ell$ with
$G(c,d,dm-\delta)\ge\exp(dm\ell)$ for every $m\ge m_0$ and
$\delta\in\{0,1\}$. This is a uniform analytic inequality; the parameter
$m$ is not enumerated.

The numerical asymmetric BFT formula then certifies the displayed
exponents and thresholds. For $(11,13)$ the oriented seed lists 13 first,
so its targets are exchanged before evaluating that formula. All source
differences are at most 100; the actual differences here are at most 14.
The [source derivation](../../methods/details/bft_numerical_thresholds.md) and
[asymmetric argument](../../methods/details/asymmetric_cofactors.md) give the
underlying inequalities.

## Applying the existing polynomial family

Keep the line exponents and row multiplicities from the
[index-15 interpolation certificate](../../archive/previous_bounds/interpolation_extensions.md).
Enumerate the minimal cofactor vectors for the preceding disjunctions and
the original explicit table. For each vector, consider every possible
subset of primes at singleton maximal positions; the remaining primes
are grouped as in the weighted-certificate argument. Rearrangement is
applicable because the row multiplicities are nonincreasing.

The exact minimum degree gain is now

$$
g=\frac{7993}{10000}>0.
$$

The same polynomial coefficient estimate as before gives, for every bad
row beyond the source thresholds,

$$
n^g<10^{8725502}.
$$

The row threshold $10^{15170264}$ exceeds every listed factor threshold
by at least a full power of ten, so subtracting any selected position
$0\le r_p\le14$ leaves each source estimate applicable. It also satisfies

$$
15170264\cdot\frac{7993}{10000}>8725502.
$$

This proves the stated complete numerical tail. The
[checker](../../computations/erdos_699_index_15_numerical_tail.py)
recomputes the three new GCD and asymmetric source bounds, performs the
exact finite cofactor optimization, and verifies the final rational
comparison. Its [output](../../computations/erdos_699_index_15_numerical_tail.json)
records all parameters and certified intervals. The previously completed
modular-rank calculation is an input and is not repeated.
