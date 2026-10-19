---
name: research/erdos_699/archive/previous_bounds/interpolation_extensions
title: "Erdős 699: effective bounds at indices 15 and 20"
desc: "Monotone weighted interpolation, asymmetric prime-pair bounds, and exact modular jet ranks make both indices 15 and 20 effective."
created: 2026-09-22T04:07:31Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: effective bounds at indices 15 and 20

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/methods/details/jet_nonvanishing|Nonvanishing from surjective interpolation]]

**Complete exclusions.** Indices $15,20$ are fully excluded by the
[cutoff-15 proof](cutoff_15.md); the bounds and constructions below are retained
as earlier stages and inputs.

**There is an effectively computable last bad row at each of $i=15,20$.**
These are bounds for the entire index, including every possible assignment
and collision of the small-prime maximum positions. No binomial rows or
columns are enumerated.

Let $X_i$ be the maximum of the effective symmetric BFT thresholds, with
gap bound $100$, for the prime-pair weights used below. Then every bad
triple satisfies

$$
\begin{array}{c|c}
i&\text{effective last-row bound}\\\hline
15&n<\max\{X_{15}+15,\;10^{1100000000}\},\\
20&n<\max\{X_{20}+20,\;10^{4000000}\}.
\end{array}
$$

The powers of ten are deliberately crude. The additional symmetric
thresholds comprising $X_i$ are effectively computable but not all
numerically instantiated here. The two asymmetric thresholds are numerical
and are already below the displayed algebraic bounds.

## Cofactor inequalities

For each prime $p<i$, choose a position $r_p\in\{0,\ldots,i-1\}$
maximizing $v_p(n-r_p)$, and write

$$
n-r_p=P_pu_p,\qquad P_p=p^{v_p(n-r_p)}.
$$

Use the symmetric weights in BFT Corollary 2.3 together with the twelve
[additional pair estimates](../other_approaches/more_prime_pairs.md).
Include only pairs whose primes are less than $i$. Add these two
[asymmetric inequalities](../../methods/details/asymmetric_cofactors.md),
written for normalized cofactor exponents $e_p$:

$$
e_5\ge .3613\quad\text{or}\quad e_7\ge .2277,
\qquad
e_7\ge .0987\quad\text{or}\quad e_{13}\ge .2080.
$$

Here $e_p=\log u_p/\log(n-i+1)$. The exact asymmetric threshold evaluator
gives:

| Pair | Targets | Seed and $c/d$ | $L_1,m_0$ | Threshold for the smaller input |
| --- | --- | --- | --- | --- |
| $5,7$ | $(.3613,.2277)$ | $2\cdot25-49=1$, $8/5$ | $1.5407,53$ | $10^{2405782}$ |
| $7,13$ | $(.0987,.2080)$ | $343-2\cdot169=5$, $7/5$ | $1.4135,74$ | $10^{484367}$ |

Both use gap bound $100$. Their limiting exponents exceed, respectively,
$(.3613046269,.2277777234)$ and $(.0987539406,.2080310930)$.
The coefficient-gcd bounds $L_1,m_0$ are the retained BFT
Proposition 5.1 entries; no new asymptotic gcd assumption is made.

For each symmetric or asymmetric disjunction, choose an endpoint
witnessing it. Keeping the largest chosen weight at each prime, and
discarding componentwise dominated vectors, gives a finite list of
rational vectors $v$ such that some $v$ satisfies $v_p\le e_p$.
The list has 39 vectors at $i=15$ and 112 at $i=20$.

When $n\ge2(i-1)$, each singleton maximum satisfies

$$
P_p\le2^{v_p}n^{1-v_p}.
$$

At a position occupied by at least two primes, their selected prime
powers have product at most $n-r\le n$. Such a position therefore has
exponent capacity $1$. A singleton has capacity $1-v_p$.

For a fixed singleton subset, the other primes occupy at most
$\lfloor\#\text{other primes}/2\rfloor$ positions. Assign capacity $1$
to that many positions and sort all capacities decreasingly. These
vectors cover all collisions. For nonincreasing row multiplicities $m_t$,
rearrangement puts the largest capacities at the earliest positions,
giving the uniform upper exponent

$$
\sum_a m_a c_a.
$$

All entries $v_p$ used here are less than $1/2$, as checked exactly. The
capacity construction and its proof are also retained in the
[weighted-ramp calculation](../../computations/erdos_699_weighted_ramps.py).

## Integer interpolation data

For $i=15$, use

$$
\begin{aligned}
h={}&(69,63,57,51,43,34,24,11,0,0,0,0,0,0,0),\\
m={}&(139,139,138,137,127,127,127,119,106,95,87,79,73,68,63),\\
D={}&257.
\end{aligned}
$$

For $i=20$, use

$$
\begin{aligned}
h={}&(34,32,30,27,25,22,19,16,13,9,5,1,0,0,0,0,0,0,0,0),\\
m={}&(67,65,65,65,62,60,58,57,57,54,50,46,42,39,37,34,32,30,28,26),\\
D={}&96.
\end{aligned}
$$

Both $m$ vectors are nonincreasing. At each grid point $x,y\ge0$,
$x+y<i$, prescribe residual multiplicity

$$
R_{xy}=\max\{0,m_{x+y}-h_x-h_y\}.
$$

The exact symmetric jet calculations give:

| $i$ | Symmetric equations | Symmetric monomials through degree $D$ | Modulus | Rank |
| --- | ---: | ---: | ---: | ---: |
| 15 | 16768 | 16770 | 251 | 16768 |
| 20 | 2399 | 2401 | 65521 | 2399 |

Both moduli are prime. The matrix entries are the integer Hasse Taylor
coefficients of the symmetric monomials. At off-diagonal support points,
one point from each exchanged pair suffices; at diagonal points the
Taylor coefficients with exchanged derivative indices coincide. These
are exact identities, not numerical reductions.

Full row rank modulo the displayed prime implies surjectivity of the
rational symmetric interpolation map. The
[multiplication-by-$X+Y$ lemma](../../methods/details/jet_nonvanishing.md)
therefore supplies a finite family of integer polynomials of degree at
most $D+1$ with the prescribed residual multiplicities, having no common
zero when $X+Y>i-1$. This uses the symmetric local jet algebra. In
particular, independence of all nonsymmetric jet conditions is neither
claimed nor needed.

Multiply these polynomials by

$$
H(X,Y)=\prod_{a=0}^{i-1}((X-a)(Y-a))^{h_a}.
$$

The resulting family has row multiplicities at least $m_t$, degree at
most $2\sum h_a+D+1$, and no common zero in the physical range
$i<j\le c$. Exact capacity enumeration gives:

| $i$ | Capacity configurations checked | Total degree | Minimum exponent gain |
| --- | ---: | ---: | ---: |
| 15 | 1840 | 962 | $43/5000$ |
| 20 | 18479 | 563 | $713/5000$ |

Here the gain is

$$
\sum_t m_t-\sum_a m_a c_a-\left(2\sum_a h_a+D+1\right).
$$

Thus some nonzero polynomial evaluation gives a positive power bound
uniformly for every bad pair. There is no remaining curve or finite
base-locus exception.

## Explicit algebraic constants

The following generous bounds make the effectivity assertion concrete
without writing out a rational interpolation inverse.
Let $r$ be the symmetric rank, $N=\binom{D+2}{2}$, and put

$$
C=r!(2i^D)^r,\qquad
U=1+\left(\frac{i(i+1)}2+i+4\right)N.
$$

A full-rank minor and its cofactors give integer interpolation sections
$q_j$, with a common denominator-clearing factor $\Delta\ne0$, such that
$\|q_j\|_1\le NC$ and $|\Delta|\le C$. Every symmetric jet matrix entry
has magnitude at most $2i^D$.

In the standard local Taylor basis, multiplication by $X+Y$ has column
coefficient norm at most $t+3\le i+2$ on row $t$. At a diagonal point,
the extra $1$ allows the coincident derivative terms. The nonvanishing
generators are

$$
(X+Y)q_j-\sum_kT_{kj}q_k,
\qquad
\Delta-\sum_j u_jq_j,
$$

where $T$ represents that multiplication and $u$ is the jet of the
constant $1$. At most $i(i+1)/2$ entries of $u$ are nonzero, and they
equal $1$. Consequently every generator has coefficient norm at most
$UC$.

Let $s$ be the number of primes less than $i$, and let $g$ be the gain
in the preceding table. The off-maximum small-prime contribution is
at most $((i-1)!)^{m_0}$. For $n\ge2\sum t m_t$, the product of the
factors $(1-t/n)^{m_t}$ is at least $1/2$. Combining the weighted Kummer
divisibility with a nonzero generator gives

$$
n^g\le
2^{1+s m_0}((i-1)!)^{m_0}
\left(\prod_{a=0}^{i-1}(a+1)^{2h_a}\right)UC.
$$

Both indices are composite, so no rough denominator factor from $i!$
needs to be added. These estimates are applied only after the source
thresholds have been reached.

Use $i<10^2$, $r<10^5$, and $U<10^7$. The right-hand side is strictly
less than $10^E$, where

$$
E=r(6+2D)+1+s m_0+2(i-1)m_0+4\sum h_a+7.
$$

The two exact values are $E=8725502$ and $E=479024$. Finally,

$$
1100000000\cdot\frac{43}{5000}>8725502,
\qquad
4000000\cdot\frac{713}{5000}>479024.
$$

The powers of ten also exceed the elementary row thresholds and both
numerical asymmetric thresholds. This proves the bounds stated at the
start.

## Reproduction

The [checker](../../computations/erdos_699_interpolation_extensions.py)
and [recorded certificate](../../computations/erdos_699_interpolation_extensions.json)
retain the integer data, all source parameters used for the asymmetric
thresholds, finite-vector counts, worst capacities, exact gains, and ranks.
The floating-point optimization that suggested the integer data is not
used to certify any assertion.

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_interpolation_extensions.py
```

Dependencies are pinned in the [interpolation requirements](../../evidence/assets/erdos_699_interpolation_requirements.txt).
Install them in the chosen Python environment before running the checker.

The exact rank check for $i=15$ takes about three minutes on the machine
used here. The `--arithmetic-only` option checks the finite cofactor and
capacity calculations without repeating the rank calculation.
