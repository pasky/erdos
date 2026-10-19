---
name: research/erdos_699/proofs/details/index_13_interpolation
title: "Erdős 699: an interpolation system for one index-13 case"
desc: "A fixed polynomial space of dimension at least 108 gives a positive exponent, leaving an explicit common-divisor computation as the nonvanishing gap."
created: 2026-09-22T03:36:52Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: an interpolation system for one index-13 case

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

***

**Complete exclusion.** Index $13$ is
[completely excluded](further_interval_certificates.md). The data below
record the initial one-pattern construction.

**Superseded.** The [complete index-13 proof](index_13_effective.md)
establishes the explicit bound $n<10^{56000}$. It uses improved
nonincreasing row multiplicities and a surjective jet map, covering every
position assignment and removing the nonvanishing gap described below.

This note records the initial exact algebraic reduction for one canonical
small-prime position assignment. No binomial rows or columns were enumerated.

## Input and exact data

Use the BFT lower vector, indexed by primes $(2,3,5,7,11)$,

$$
v=(2757,3453,2667,0,0)/10000,
$$

and the canonical positions

$$
(r_2,r_3,r_5,r_7,r_{11})=(3,4,2,0,1).
$$

Thus the weighted rough-part exponents of the rows $t=0,\ldots,12$ are

$$
\alpha=(0,0,2667/10000,2757/10000,3453/10000,1,1,1,1,1,1,1,1).
$$

Take coordinate-line exponents

$$
h=(57,51,45,39,32,24,13,3,0,0,0,0,0)
$$

and target row multiplicities

$$
m=(0,0,111,103,96,99,89,78,70,63,57,51,46).
$$

At each grid point $(x,y)$ with nonnegative integer coordinates and
$x+y\le12$, put

$$
R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}.
$$

The exact totals are

$$
\sum h_a=264,\qquad \sum R_{xy}=883,\qquad
\sum R_{xy}^2=11557.
$$

The residual multiplicities, by fixed $x$ and increasing $y$, are:

```
0:  0  0  9  7  7 18 19 18 13  6  0  0  0
1:  0  9  7  6 16 14 14 16 12  6  0  0
2:  9  7  6 15 12  9 12 15 12  6  1
3:  7  6 15 11  7  7 11 15 12  7
4:  7 16 12  7  6  7 12 16 14
5: 18 14  9  7  7  9 14 19
6: 19 14 12 11 12 14 20
7: 18 16 15 15 16 19
8: 13 12 12 12 14
9:  6  6  6  7
10: 0  0  1
11: 0  0
12: 0
```

## The fixed linear system

Let $V$ be the rational vector space of polynomials $G(X,Y)$ of total
degree at most 111 that vanish to multiplicity at least $R_{xy}$ at every
grid point. These are homogeneous rational linear conditions on
coefficients.

There are 6328 monomials of total degree at most 111. The multiplicity
conditions impose at most

$$
\sum_{x,y}\binom{R_{xy}+1}{2}
=\frac{11557+883}{2}=6220
$$

linear equations. Consequently

$$
\dim_{\mathbb Q}V\ge108.
$$

For any nonzero $G$ in this space, clear its coefficient denominators and
define

$$
H(X,Y)=\prod_{a=0}^{12}((X-a)(Y-a))^{h_a},\qquad F=HG.
$$

Then $\deg H=528$, $\deg F\le639$, and $F$ has multiplicity at least
$m_t$ at every Kummer point on row $x+y=t$.

The weighted row sum is

$$
\sum_{t=0}^{12}\alpha_t m_t=\frac{805187}{1250}=644.1496,
$$

so the degree gain is positive:

$$
\boxed{\sum_t\alpha_t m_t-639=\frac{6437}{1250}=5.1496.}
$$

All these statements are exact integer or rational arithmetic. They do not
depend on a floating-point optimization result.

## Consequence for bad pairs

Write $c=n-j$. The Kummer valuation argument in `adapted_certificates.md`
applies to every integer polynomial with these row multiplicities. Its
lower estimate, combined with the stated BFT vector at the stated
positions, gives

$$
|F(j,c)|\gg_F n^{805187/1250}
$$

whenever $F(j,c)$ is nonzero, beyond effective BFT and elementary
thresholds. On the other hand,

$$
|F(j,c)|\le \|F\|_1 n^{639}.
$$

Therefore every such nonzero evaluation gives an effective upper bound for
$n$.

Choose any rational basis of $V$ and clear denominators individually. There
are finitely many basis polynomials, and all their coefficient bounds are
effectively computable by exact linear algebra. Beyond the maximum of the
associated effective row bounds, every bad pair in this canonical position
case must lie in

$$
\{(j,c):G(j,c)=0\text{ for every }G\in V\}.
$$

Here $H(j,c)>0$ throughout the physical range $13<j\le c$, so
multiplication by $H$ introduces no physical zero.

## Precisely what remains

The missing step is to compute the common polynomial divisor of the
degree-111 space $V$, or equivalently enough basis elements to determine
its curve components.

* If the gcd is constant, the common zero set is finite. A resultant or a
  zero-dimensional Groebner basis gives an **effective** bound for all its
  integer coordinates. This would settle this canonical position case
  effectively.
* The same conclusion holds if all common curve factors have no points in
  the physical region $13<j\le c$ beyond an explicit bound; coordinate and
  bounded-sum grid lines would be harmless examples.
* A common curve component meeting the physical region remains an
  obstacle. A general finiteness statement for that component would not by
  itself supply an effective bound.

A single nonzero interpolating polynomial is insufficient: it may vanish at
the putative bad pair. Dimension at least 108 does not imply that the
common zero set is finite. No gcd or rank computation has been completed.
