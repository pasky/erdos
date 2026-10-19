---
name: theory/irrationality/L189_lcm_series_cone_no_product
title: Expanded running-lcm series has no lattice product decomposition
desc: |
  For three or more primes, the lattice-point set whose weighted count is the
  running-lcm reciprocal series is not a product of two lower-dimensional
  sets after any unimodular change of variables; for two primes it is.
tags: []
sources:
- problems/irrationality/E0269
id: L189
statement: |
  Let P be a finite set of primes with at least three elements, and put
  L_u = log u for u in P. Let Omega be the set of pairs (m, k) of vectors
  m = (m_u) and k = (k_u) in Z_{>=0}^P such that
  sum_{v in P} m_v L_v < (k_u + 1) L_u for every u in P. There are no
  integers d_1, d_2 >= 1, nonempty sets Omega_1 in Z^{d_1} and Omega_2 in
  Z^{d_2}, and group isomorphism T: Z^{d_1} x Z^{d_2} -> Z^P x Z^P with
  Omega = T(Omega_1 x Omega_2).
status: proved
tier: 0
depends_on: []
created: 2026-10-15T15:50:35Z
updated: 2026-10-15T15:50:35Z
---

# Expanded running-lcm series has no lattice product decomposition

[[theory/irrationality/_index|..]]

[[theory/irrationality/L189_lcm_series_cone_no_product/_proof|_proof]]: A product decomposition would split the recession cone along rational
subspaces; its irrational facets admit no such split for three primes.

***

## Statement

Let $P$ be a finite set of primes with $\lvert P\rvert\ge3$, and put
$L_u=\log u$ for $u\in P$. Let $\Omega$ be the set of pairs $(m,k)$ of vectors
$m=(m_u)_{u\in P}$ and $k=(k_u)_{u\in P}$ in $\mathbb Z_{\ge0}^P$ such that

$$
\sum_{v\in P}m_vL_v<(k_u+1)L_u\qquad\text{for every }u\in P.
$$

There are no integers $d_1,d_2\ge1$, nonempty sets
$\Omega_1\subset\mathbb Z^{d_1}$ and $\Omega_2\subset\mathbb Z^{d_2}$, and
group isomorphism
$T:\mathbb Z^{d_1}\times\mathbb Z^{d_2}\to\mathbb Z^P\times\mathbb Z^P$ with
$\Omega=T(\Omega_1\times\Omega_2)$.

## Significance and scope

Let $S_P=\sum_m 1/D(m)$ be the series of
[[problems/irrationality/E0269/_index|Problem 269]], summed over all positive
integers $m$ whose prime factors lie in $P$, where $D(m)$ is the running lcm at
the cutoff $m$. Since $D(m)=\prod_{u\in P}u^{\lfloor\log_u m\rfloor}$, and since
$u^{-\lfloor x\rfloor}=(1-u^{-1})\sum_{k\ge\lfloor x\rfloor}u^{-k}$ with
$k\ge\lfloor x\rfloor$ exactly when $k+1>x$, one has

$$
S_P=\prod_{u\in P}\bigl(1-u^{-1}\bigr)
    \sum_{(m,k)\in\Omega}\ \prod_{u\in P}u^{-k_u}.
$$

The weight is a character of the lattice. A decomposition
$\Omega=T(\Omega_1\times\Omega_2)$ would therefore factor the series into two
weighted lattice-point sums of lower dimension.

For two primes $P=\{p,q\}$ such a decomposition exists: the unimodular change
of variables $k'_p=k_p-m_p$, $k'_q=k_q-m_q$ turns the conditions into
$m_qL_q<(k'_p+1)L_p$ and $m_pL_p<(k'_q+1)L_q$, which involve disjoint sets of
variables. These strict inequalities force $k'_p,k'_q\ge0$, so the original
nonnegativity conditions introduce no further coupling. The two factors are
the one-slope sums of the
[[research/smooth_lcm_series/_index|two-prime factorization]], and their
product is the factorization recorded there. This claim shows that the mechanism
has no analogue for three or more primes in this representation. For three
primes, after the same change of variables, each $m_v$ occurs in two of the
three irrational conditions; the [proof](_proof.md) shows that no unimodular
change of variables separates them.

The claim concerns this lattice-point representation and product
decompositions of it. It does not exclude identities of other kinds, and it
says nothing about the irrationality or transcendence of $S_P$. The
[[research/smooth_lcm_three_prime/_index|three-prime research page]] uses it,
together with
[[research/smooth_lcm_three_prime/finite_separation|the known infinite-rank
obstruction to finite termwise separation]], to delimit the
separation route. The
[[theory/irrationality/L190_three_prime_no_finite_planar_partition/_index|finite
halfspace partition obstruction]] additionally excludes signed partitions
into one-slope polyhedral pieces in the same six coordinates.

## Current standing and verification

The complete [proof](_proof.md), by Plasma AI, is author-recorded at tier 0.
It has no identified gap and no independent review. It uses the linear
independence of $\log u$ ($u\in P$) over $\mathbb Q$, which follows from
unique factorization, and elementary facts about recession cones and faces of
polyhedral cones. No native claim is consumed and no source theorem is
imported. No computation is required; the expansion identity above is a
rearrangement of nonnegative terms.
