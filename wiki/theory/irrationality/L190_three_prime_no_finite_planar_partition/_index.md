---
name: theory/irrationality/L190_three_prime_no_finite_planar_partition
title: Three-prime lcm lattice sets have no finite planar halfspace partition
desc: |
  The expanded lattice set for three distinct primes is not a finite real
  linear combination of indicators of polyhedra whose facet coefficients
  span at most two dimensions over the rationals.
tags: []
sources:
- problems/irrationality/E0269
id: L190
statement: |
  Let P={p,q,r} consist of three distinct primes, let L_u=log u, and let
  Omega be the set of (m,k) in Z_{>=0}^P times Z_{>=0}^P satisfying
  sum_{v in P} m_v L_v < (k_u+1)L_u for each u in P. There is no identity
  1_Omega = sum_{j=1}^J c_j 1_{E_j} on Z^6 with finitely many sets
  E_1,...,E_J in Z^6 and real constants c_1,...,c_J, where each E_j
  is defined by finitely many inequalities a dot z < b or a dot z <= b,
  with b real and a a nonzero real six-vector whose coordinates span a
  vector space of dimension at most two over Q. In particular this
  excludes finite signed partitions into lattice points in invertible
  affine rational images of Cartesian products of planar one-slope
  polyhedra and rational polyhedra, with total dimension six.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T16:35:43Z
updated: 2026-10-15T16:35:43Z
---

# Three-prime lcm lattice sets have no finite planar halfspace partition

[[theory/irrationality/_index|..]]

[[theory/irrationality/L190_three_prime_no_finite_planar_partition/_proof|_proof]]: A facet with three rationally independent logarithmic coefficients cannot
be reproduced on the lattice by finitely many halfspace regions whose
normal coefficients each have rational rank at most two.

***

Let $P=\{p,q,r\}$ consist of three distinct primes, put $L_u=\log u$, and
define

$$
\Omega=\left\{(m,k)\in\mathbb Z_{\ge0}^P\times\mathbb Z_{\ge0}^P:
 \sum_{v\in P}m_vL_v<(k_u+1)L_u\quad(u\in P)\right\}.
$$

For a nonzero real vector $a$, write
$\operatorname{rank}_{\mathbb Q}(a)=\dim_{\mathbb Q}
\operatorname{span}_{\mathbb Q}\{a_1,\ldots,a_6\}$. A set of lattice points
defined by finitely many inequalities $a\cdot z<b$ or $a\cdot z\le b$ is
called a halfspace region here; $b$ can be any real number.

There is no identity on $\mathbb Z^6$ of the form

$$
\mathbf1_\Omega=\sum_{j=1}^J c_j\mathbf1_{E_j},
$$

where $J$ is finite, $c_j\in\mathbb R$, and every defining normal of every
$E_j$ has rational rank at most two. Empty conjunctions are allowed and
describe the whole lattice. Equality constraints can be written as pairs of
inequalities.

The [proof](_proof.md) finds a facet of the limiting cone of $\Omega$ whose
normal has rational rank three. A finite collection of lower-rank boundary
hyperplanes misses a relatively open part of that facet. Integer points on
opposite sides of it then have identical membership in every $E_j$ but
different membership in $\Omega$.

A planar Hecke–Mahler region has inequalities such as
$y\le\theta x+\rho$, together with rational coordinate inequalities. Its
normals have rational rank at most two. Products retain this property, as do
invertible rational linear coordinate changes and translations. Taking the
lattice points in such real polyhedra therefore cannot give a finite signed
decomposition of $\Omega$ in the original six coordinates. The theorem
permits arbitrary slopes and intercepts; an
algebraicity assumption on the slopes is not used.

This strengthens the partition obstruction relevant to the
[[research/smooth_lcm_three_prime/_index|three-prime running-lcm expansion]].
The separate
[[theory/irrationality/L189_lcm_series_cone_no_product/_index|L189 obstruction]]
excludes a single product of arbitrary lower-dimensional lattice sets after
a unimodular change of variables. Neither result excludes an identity that
holds only after weighted summation, an infinite partition, or a
representation using additional summation coordinates. Neither proves
irrationality of the series.

The proof by Plasma AI is complete and author-recorded at tier 0, with no
independent review. It uses unique factorization, elementary linear algebra,
and rounding real vectors to integer vectors. It imports no native claim or
literature theorem. No computation is needed. There is no remaining
mathematical obligation for the stated obstruction; the value-theorem gap
remains on the research page.
