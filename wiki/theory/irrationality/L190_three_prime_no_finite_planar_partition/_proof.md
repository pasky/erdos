---
name: theory/irrationality/L190_three_prime_no_finite_planar_partition/_proof
title: Proof of the finite halfspace partition obstruction
desc: |
  A facet with three rationally independent logarithmic coefficients cannot
  be reproduced on the lattice by finitely many halfspace regions whose
  normal coefficients each have rational rank at most two.
tags: []
sources:
- theory/irrationality/L190_three_prime_no_finite_planar_partition/_index
created: 2026-10-15T16:35:43Z
updated: 2026-10-15T16:35:43Z
---

***

This proves the full statement of
[[theory/irrationality/L190_three_prime_no_finite_planar_partition/_index|L190]].
Write $V=\mathbb R^P\times\mathbb R^P$ and

$$
\ell_u(m,k)=\sum_{v\in P}m_vL_v-k_uL_u,
\qquad
C=\{(m,k):m_v\ge0,\ \ell_u(m,k)\le0\ (u,v\in P)\}.
$$

Unique factorization implies that $L_p,L_q,L_r$ are linearly independent
over $\mathbb Q$. The coefficient vector of each $\ell_u$ therefore has
rational rank three. Multiplying a vector by a nonzero real scalar
preserves this rank: scalar multiplication is a $\mathbb Q$-linear
isomorphism between the two coordinate spans. Consequently no nonzero
normal of rational rank at most two has the same kernel as $\ell_u$.

Fix $u\in P$. There is a relatively open, nonempty part $F^\circ$ of the
hyperplane $H=\ker\ell_u$ on which every $m_v$ is positive and all the
inequalities $\ell_v<0$ for $v\ne u$ are strict. For example, start at the
point with all $m_v=1$, with $k_u=\sum_vL_v/L_u$, and with
$k_v=2\sum_wL_w/L_v$ for $v\ne u$. A small neighbourhood within $H$ has
the required properties. All its $k_v$ are positive as well.

Suppose a proposed finite indicator identity uses the normals
$a_1,\ldots,a_M$, after listing every defining inequality of every region.
Each $H\cap\ker a_i$ is a proper linear subspace of $H$, by the rank
observation. Finitely many proper linear subspaces cannot cover a nonempty
open subset of $H$. Choose $x\in F^\circ$ outside their union.

There is a ball $U$ around $x$ in $V$ on which all coordinates $m_v,k_v$
are positive, all $\ell_v$ with $v\ne u$ are negative, and each $a_i$
has one fixed, nonzero sign. Both sides of $H$ meet $U$. Choose
$x_{\rm in},x_{\rm out}\in U$ with

$$
\ell_u(x_{\rm in})<0<\ell_u(x_{\rm out}).
$$

For each positive integer $N$, round the coordinates of $Nx_{\rm in}$ and
$Nx_{\rm out}$ to nearest integers, obtaining $z_{{\rm in},N}$ and
$z_{{\rm out},N}$. The rounding errors are bounded independently of $N$.
Thus, for any fixed linear form $a$,

$$
a\cdot z_{{\rm in},N}=N(a\cdot x_{\rm in})+O(1),
\qquad
a\cdot z_{{\rm out},N}=N(a\cdot x_{\rm out})+O(1).
$$

For all sufficiently large $N$, both rounded vectors have positive
coordinates. Every $\ell_v(z_{{\rm in},N})$ is negative, hence less than
$L_v$, so $z_{{\rm in},N}\in\Omega$. In contrast,
$\ell_u(z_{{\rm out},N})>L_u$, so $z_{{\rm out},N}\notin\Omega$.

For every defining inequality with normal $a_i$ and constant $b_i$, the
values at these two vectors tend to the same signed infinity. They
therefore either both satisfy that inequality or both fail it, whether
the comparison is strict or non-strict. Because there are only finitely
many inequalities, for all sufficiently large $N$ the two vectors have
identical membership in every region $E_j$. The proposed right-hand side
then takes equal values at them, whereas $\mathbf1_\Omega$ takes values
one and zero. This contradiction proves the indicator assertion.

Finally, the coordinate span of a normal is unchanged by an invertible
rational linear transformation: each transformed coefficient is a rational
linear combination of the old ones, and the inverse gives the reverse
inclusion. Translation changes only the constant term. A product of planar
polyhedra, each with only one irrational slope, and rational polyhedra has
defining normals of rational rank at most two, even when the slopes differ
between the planar factors. The indicator assertion therefore applies to
every finite signed partition into their invertible affine rational images.
