---
name: theory/additive_combinatorics/L31_finite_sidon_prefix_extension/_proof
title: Separating old and new sums
desc: A fixed number of deletions removes mixed collisions and a translate yields the claimed asymptotic extension coefficient.
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

Let $m=|A|$. By
[[../library/additive_bases/singer_1938_theorem_finite_projective_geometry_some_applications_number_theory/theorem_p380|Singer's theorem]],
for every prime power $q$ there is a set $T\subset[1,L]\cap\mathbb Z$,
where $L=q^2+q+1$ and $|T|=q+1$, with unique nonzero differences modulo
$L$. Its ordinary nonzero differences are therefore unique. This implies
strong Sidonicity: a nontrivial pair-sum equality would give two distinct
ordered pairs with the same nonzero difference, also when a summand is
repeated.

For each positive difference represented in $A$, delete one endpoint of
the pair of $T$ representing that difference, if it exists. The remaining
set $T'$ is strong Sidon, shares no positive difference with $A$, and has
size at least $q+1-\binom m2$.

Take $q$ large enough that $L>N$, and put

$$
B=(L+N)+T',\qquad M=2L+N.
$$

Old-old sums are at most $2N$. Old-new sums lie between $L+N+2$ and
$2L+2N$. New-new sums are at least $2L+2N+2$. These intervals are
disjoint. Each of the old-old and new-new types is separately Sidon.
An equality between two different old-new pairs would yield a common
nonzero difference of $A$ and $T'$, which the deletions excluded.
Thus $A\cup B$ is strong Sidon and

$$
|A\cup B|\ge q+1+m-\binom m2
=\left(\frac1{\sqrt2}+o(1)\right)\sqrt M.
$$

Here $A,N$ are fixed while $q$ tends to infinity through prime powers.
This gives arbitrarily large $M$ for every fixed positive $\varepsilon$.
