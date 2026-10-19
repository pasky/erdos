---
name: theory/additive_bases/L3_square_complement_nine_halves
title: An annular square complement with upper limit 9/2
desc: |
  An explicit positive-integer square complement has exact lower and upper
  counting limits 3 sqrt(2) and 9/2, with uniform real-cutoff estimates.
tags: []
sources: []
id: L3
statement: |
  For each positive integer M let R_M be the set of positive integers
  congruent to 0, 1, or 2 modulo M, identifying repeated residue classes.
  Define A as the union, over q=3^k with integer k>=0, of
  (R_(2q) intersect [4q^2/9,4q^2]) and
  (R_q intersect [5q^2/9,q^2]). Intervals select positive integers.
  Every integer t>=1 equals m^2+a with an integer m>=0 and a in A.
  Write A(X)=|A intersect [1,X]| for real X. For every integer k>=1,
  q=3^k, and real X with 4q^2/9<=X<=4q^2, put x=X/q^2. Then
  |A(X)-q F(x)|<=18k+5, where F(x)=7/3+3x/2 on [4/9,5/9],
  F(x)=3/2+3x on [5/9,1], and F(x)=3+3x/2 on [1,4];
  the formulas agree at common endpoints. For this same A, as X tends
  to infinity through real values, liminf A(X)/sqrt(X)=3 sqrt(2) and
  limsup A(X)/sqrt(X)=9/2.
status: proved
tier: 0
depends_on: []
created: 2026-09-09T00:57:37Z
updated: 2026-09-09T01:21:03Z
---

# An annular square complement with upper limit 9/2

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L3_square_complement_nine_halves/_proof|_proof]]: Elementary root lifting proves positive-target coverage; disjoint cycles
give a uniform counting error and exact limits 3 sqrt(2) and 9/2.

***

For a positive integer $M$, put

$$
R_M=
\{a\in\mathbb Z_{>0}:a\equiv0,1,\text{ or }2\pmod M\}.
$$

Repeated residue classes are identified, so $R_1$ and $R_2$ both
contain every positive integer. Define the single explicit set

$$
A=\bigcup_{k\ge0}\left(
\left(R_{2q}\cap\left[\frac{4q^2}{9},4q^2\right]\right)
\cup
\left(R_q\cap\left[\frac{5q^2}{9},q^2\right]\right)
\right),\qquad q=3^k.
\tag{1}
$$

Each interval in (1) selects positive integers. Write
$A(X)=|A\cap[1,X]|$ for real $X$ and
$\mathcal S=\{m^2:m\in\mathbb Z_{\ge0}\}$.

## Statement

The set (1) represents every positive integer:

$$
\mathbb Z_{>0}\subseteq A+\mathcal S.
\tag{2}
$$

For every integer $k\ge1$, let $q=3^k$. For every real cutoff
$4q^2/9\le X\le4q^2$, put $x=X/q^2$ and define

$$
F(x)=
\begin{cases}
\dfrac73+\dfrac32x,&\dfrac49\le x\le\dfrac59,\\[2mm]
\dfrac32+3x,&\dfrac59\le x\le1,\\[2mm]
3+\dfrac32x,&1\le x\le4.
\end{cases}
\tag{3}
$$

The formulas agree at the two common endpoints, and

$$
|A(X)-qF(X/q^2)|\le18k+5.
\tag{4}
$$

Consequently this same set has the exact limits

$$
\liminf_{X\to\infty}\frac{A(X)}{\sqrt X}=3\sqrt2,
\qquad
\limsup_{X\to\infty}\frac{A(X)}{\sqrt X}=\frac92,
\tag{5}
$$

where both limits range over real cutoffs. The upper limit is witnessed
along $X=3^{2k}$ and the lower limit along $X=2\cdot3^{2k}$.

The [proof](_proof.md) establishes bounded modular roots, coverage across
successive scales, exact membership on disjoint cycles, and the uniform
counting estimate (4). The cases $q=1$, $q=3$, zero residuals, and shared
annular endpoints are included.

## Relation to the square-complement problem

This is a construction relevant to
[E0033](../../../problems/additive_bases/E0033/_index.md). It proves the exact
two limits of the displayed set; it does not determine the infimum over
all square complements or assert that this construction is optimal. The
result is asymptotic: no inequality $A(X)\le(9/2)\sqrt X$ at every
cutoff is asserted.

## Current standing

The complete argument, including (4) and (5), is author-recorded at tier 0.
It has not received independent whole-claim acceptance or native Lean
verification. There is no identified gap in the supplied proof. It consumes
no native L-claim or external theorem: the modular lifting and periodic
counts are proved directly. No mathematical program or computational input
is needed.

The author check covered the small scales, the first crossing, the zero
residual branch, every closed seam, the error uniform over real cutoffs,
and both sequences giving equality in (5). Independent acceptance would
require scrutiny of the exact statement, proof, and named consequences.
This record does not claim independently accepted literature-proof coverage.
