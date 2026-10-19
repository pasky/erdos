---
name: research/erdos_699/proofs/details/index_20_small_height
title: "Erdős 699: a smaller coefficient bound at index 20"
desc: "An explicit basis of 51 integer interpolation polynomials reduces the algebraic index-20 tail from 10^4000000 to 10^6396, after the cofactor source thresholds."
created: 2026-09-22T05:05:58Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: a smaller coefficient bound at index 20

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/archive/previous_bounds/interpolation_extensions|Effective bounds at 15 and 20]] ·
[[research/erdos_699/methods/details/jet_nonvanishing|The interpolation nonvanishing lemma]]

***

**Complete exclusions.** Indices $15,20$ are fully excluded by the
[cutoff-15 proof](../../archive/previous_bounds/cutoff_15.md); the bounds and
constructions below are retained as earlier stages and inputs.

The existing index-20 interpolation construction gives the much smaller
algebraic tail


$$
\boxed{n<10^{6396}}
$$


once its cofactor inequalities hold. This replaces the generic
coefficient estimate that gave $10^{4000000}$. It is **not** an assertion
that every source threshold is below $10^{6396}$: the original near-limit
asymmetric estimates still have larger numerical thresholds. The
polynomial bound below can also be combined with another certified
cofactor gain for the same row weights.

## An explicit complete kernel basis

Keep the index-20 vectors


$$
\begin{aligned}
h={}&(34,32,30,27,25,22,19,16,13,9,5,1,0,0,0,0,0,0,0,0),\\
m={}&(67,65,65,65,62,60,58,57,57,54,50,46,42,39,37,34,32,30,28,26),
\end{aligned}
$$


and residual multiplicities
$R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}$ at $x,y\ge0$, $x+y<20$.
The previously certified symmetric degree-96 jet map is surjective, of
rank 2399. There are 2450 symmetric monomials through degree 97, so its
degree-97 kernel has dimension 51.

The [compressed coefficient artifact](../../computations/erdos_699_index_20_small_height_basis.json.gz)
contains 51 integer polynomials in the basis
$X^aY^b+X^bY^a$ for $a<b$ and $X^aY^a$ for $a=b$.
The [direct verifier](../../computations/erdos_699_index_20_small_height.py)
checks:

* All 2399 required jets of every polynomial are exactly zero over the
  integers.
* The coefficient minor on the last 51 symmetric monomials has
  determinant $13345\pmod{65521}$, so the polynomials are independent.
* Their largest coefficient has 121 decimal digits, and their largest
  coefficient norm has 123 decimal digits.

Thus these polynomials form a rational basis of the **complete** symmetric
degree-97 kernel. The existing multiplication-by-$X+Y$ lemma guarantees
that they have no common zero when $X+Y>19$.

The basis was obtained by an exact Dixon solve for the 51 free columns,
followed by primitive normalization, saturation of the integer lattice,
and LLL reduction. The initial primitive basis had a 1696-digit maximum
coefficient norm. Saturation uses the row Hermite form of the transpose:
if $B$ has the basis vectors as rows and $H$ is a row basis of the
coordinate lattice of $B^{\mathsf T}$, then
$B^{\mathsf T}H^{-1}$ is integral and generates the saturated column
lattice. Exact identities verify this step and the unimodular LLL
transformation. Verification of the retained result does not depend on
any property of the search or reduction algorithm: integer jets and the
nonzero coefficient minor suffice.

## Evaluating the polynomials on a large row

For each retained polynomial $G$, write its degree-97 part as


$$
G_{97}(X,Y)=\sum_{a=0}^{97}c_aX^aY^{97-a}.
$$


The exact largest Bernstein coefficient, across the entire basis, is


$$
B:=\max_{G,a}\frac{|c_a|}{\binom{97}{a}}
=7848927543503780125160732509336560.
$$


For $X,Y\ge0$ and $X+Y=n$, the binomial theorem gives
$|G_{97}(X,Y)|\le Bn^{97}$.
All lower-degree terms together have magnitude less than $n^{97}$
when $n\ge10^{123}$, because the full coefficient norm of every $G$ is
less than $10^{123}$. Consequently


$$
|G(j,c)|<(B+1)n^{97}\qquad(n\ge10^{123}).
$$


This bound uses only the nonnegative physical coordinates, not a bound
for arbitrary complex evaluations.

## The weighted divisibility constant

Set


$$
H(X,Y)=\prod_{a=0}^{19}((X-a)(Y-a))^{h_a}.
$$


Here $2\sum h_a=466$. Pairing the factors gives the sharper direct bound


$$
0<H(j,c)\le\frac{n^{466}}{2^{466}}.
$$


The exact off-maximum small-prime constant is


$$
\begin{aligned}
C_{\rm off}
&=\prod_{p<20}p^{\max_r\sum_{t\ne r}m_t v_p(t-r)}\\
&=2^{885}3^{441}5^{177}7^{124}11^{67}13^{67}17^{67}19^{67}.
\end{aligned}
$$


For the normalized cofactor exponent $v_p$, retain


$$
P_p\le n^{1-v_p}(1-19/n)^{-v_p}
$$


at singleton positions instead of replacing the last factor by $2^{v_p}$.
At a collision position the selected prime powers have product at most
$n$. Write $L=\sum t m_t=7692$. The numerator factors and all singleton
normalization factors together are at least


$$
1-\frac{L+8m_0\cdot19}{n}
\ge\frac{999}{1000}
\qquad(n\ge17876000).
$$


This follows by expanding products of factors in $[0,1]$ and bounding
the total singleton exponent by $8m_0$.

For every bad pair beyond the cofactor thresholds, select a retained
$G$ with $G(j,c)\ne0$, which is possible by nonvanishing. Apply weighted
Kummer divisibility to $HG$. The already certified uniform gain is
$713/5000$, so


$$
n^{713/5000}
<\frac{1000\,C_{\rm off}(B+1)}{999\,2^{466}}
<10^{912}.
$$


The second inequality is checked by an integer comparison. Finally,
$6396\cdot713/5000>912$. Since $10^{6396}$ also exceeds the elementary
and evaluation thresholds, the claimed algebraic tail follows.

## Retained verification

The [small JSON report](../../computations/erdos_699_index_20_small_height.json)
contains the coefficient norm, Bernstein bound, coefficient-artifact
checksum, independence minor, exact off-maximum factors, and the
resulting exponent comparison. Run the checker with the
[pinned dependencies](../../evidence/assets/erdos_699_interpolation_requirements.txt)
installed in the repository's `.venv/`:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_20_small_height.py
```

Ordinary verification checks the retained integer polynomials directly.
The optional `--regenerate` flag repeats the exact solve, saturation, and
LLL construction. No binomial rows are enumerated.
