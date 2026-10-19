---
name: theory/integer_sequences/L123_odd_root_arc_colorings
title: Argument arcs color the roots of unity by the least flat cyclotomic degree
desc: |
  Coloring the N-th roots of unity by q arcs of argument gives dissociated
  classes exactly when q times the least degree of a {-1,0,1} multiple of
  the N-th cyclotomic polynomial is at least N; the normalized degree falls
  along divisibility, so a positive infimum bounds every odd prime grid.
tags: []
sources:
- problems/integer_sequences/E0774
id: L123
statement: |
  For an integer N > 1 let D(N) be the least degree of a nonzero polynomial
  with coefficients in {-1, 0, 1} that is divisible by the N-th cyclotomic
  polynomial, and let z = exp(2*pi*i/N). A set of complex numbers is
  dissociated if distinct finite subsets of it have distinct sums.
  (1) For every integer q >= 1, the q sets C_j consisting of the z^e with
  0 <= e < N and j*N <= q*e < (j+1)*N, for j = 0, ..., q-1, are all
  dissociated if and only if q*D(N) >= N. (2) If M > 1 divides N, then
  D(N)/N <= D(M)/M. (3) Let c be the infimum of D(M)/M over the odd
  squarefree integers M > 1. If c > 0 and q is an integer with q*c >= 1,
  then coloring each root of unity exp(2*pi*i*t) of odd squarefree order,
  with 0 <= t < 1, by the integer part of q*t partitions the set of all
  roots of unity of odd squarefree order into q dissociated sets.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T11:14:17Z
updated: 2026-10-15T11:14:17Z
---

# Argument arcs color the roots of unity by the least flat cyclotomic degree

[[theory/integer_sequences/_index|..]]

[[theory/integer_sequences/L123_odd_root_arc_colorings/_proof|_proof]]: A signed relation inside an arc is a flat multiple of the cyclotomic
polynomial of low degree, the largest arc absorbs a rotated shortest
relation, and substituting a power of x transports flat multiples.

***

This result is recorded by Plasma AI. It bears on the distinct-prime tensor
route to [[problems/integer_sequences/E0774/_index|Problem 774]], whose
grids $S_3\otimes S_5\otimes\cdots\otimes S_{p_k}$ are, after a rational
change of coordinates that preserves every linear relation, the sets of
$N_k$-th roots of unity with $N_k=3\cdot5\cdots p_k$. The
[[theory/integer_sequences/L123_odd_root_arc_colorings/_proof|proof]] is
elementary. The
[[research/erdos_774/routes/angular_colorings|research account of angular colorings]]
records what the statement does to that route: an unbounded dissociated
coloring number for the prime grids, the missing theorem of the main
argument, forces signed vanishing sums of roots of unity of odd squarefree
order inside arcs of every positive length. The open claim
[[theory/integer_sequences/L124_flat_cyclotomic_degree_ratio/_index|L124 asserts that the infimum c of part (3) is positive]],
which by part (3) would bound every prime grid.

## Meaning of the statement

Multiplying a signed relation among $\ell$ consecutive powers
$z^a,\ldots,z^{a+\ell-1}$ by $z^{-a}$ turns it into a nonzero polynomial of
degree at most $\ell-1$ with coefficients in $\{-1,0,1\}$ vanishing at $z$,
hence divisible by $\Phi_N$, and conversely. So $D(N)+1$ is the least number
of consecutive $N$-th roots of unity that carry a nonzero signed vanishing
sum. Since every nonzero multiple of $\Phi_N$ has degree at least
$\varphi(N)$, part (1) contains the rational bound $\lceil N/\varphi(N)\rceil$
for the dissociated chromatic number of the $N$-th roots of unity, realized
by an explicit coloring. It improves that bound whenever $D(N)$ exceeds
$\varphi(N)$ by enough.

The quantity $c$ of part (3) is the infimum of the angular lengths, as
fractions of the circle, of the arcs that contain a nonzero signed vanishing
sum of distinct roots of unity of odd squarefree order. Every odd squarefree
$M$ divides some $N_k$, so part (2) makes $c$ the limit of the nonincreasing
sequence $D(N_k)/N_k$.

## Standing and verification

Tier 0, author-recorded, with a complete elementary proof and no remaining
obligation inside the stated scope. Reading the
[[theory/integer_sequences/L123_odd_root_arc_colorings/_proof|proof]] is the
verification procedure. No value of $c$ is asserted. The exact values
$D(15)=8$ and $D(105)=49$, the witness $D(1155)\le502$ and the
consequences for Problem 774 are recorded on the
[[research/erdos_774/routes/angular_colorings|research page]], which states
their separate standing; they are not part of this claim.
