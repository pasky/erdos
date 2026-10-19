---
name: research/smooth_integer_intervals
title: Smooth integers in every short block
desc: |
  Upper bounds for k(n) in Problem 962 through smooth integers in every
  block of K consecutive integers: the known exponent 2/5, the explicit
  bound 11/28 and the exponent 38/97+epsilon from multiplier averaging,
  with precise limits of that method and a least-nonresidue reduction.
tags: [E0962]
sources:
- problems/integer_sequences/E0962
created: 2026-10-15T22:27:51Z
updated: 2026-10-15T22:54:40Z
---

# Smooth integers in every short block

[[research/_index|..]]

[[research/smooth_integer_intervals/literature|literature]]: Each located theorem on smooth integers in every short interval, read at
its exact interval length and smoothness, with the diagonal exponent it
gives for k(n) in Problem 962, including the classical 2/5 exponent,
the parameter mismatch in recent results, and Bourgain's analytic
input for the project bound 38/97+epsilon.

[[research/smooth_integer_intervals/proof_sketch|proof_sketch]]: Proof sketch for upper bounds on k(n) in Problem 962: the near-square
construction gives 2/5 with one multiplier, 11/28 explicitly and
38/97+epsilon with Bourgain's exponent pair (L250, L251, L253); exact
limits of these estimates and the nonresidue reduction locate the gaps.

***

This folder's results that are not drawn from a cited source are Plasma
AI's, credited to Plasma AI.

The question is how long a block $m+1,\ldots,m+k$ with starting parameter
$m\le n$ can be when every term has a prime factor larger than the
block's length. This defines the function $k(n)$ of
[[problems/integer_sequences/E0962/_index|Problem 962, whose assessment records both of its questions as open; this research does not change that status]].
Equivalently, $k(n)+1$ is the least positive integer $K$ such that every
block $(m,m+K]$ with $0\le m\le n$ contains a $K$-smooth integer. The
quantifier is over every allowed block.

The
[[research/smooth_integer_intervals/proof_sketch|proof sketch]]
carries the argument and its standing. Erdős and Sárközy's 1979 theorem
gives $k(n)\ll n^{2/5}$, recorded with explicit constants as
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_index|L250]];
averaging their multiplier and bounding the resulting sawtooth sum by the
third-derivative test gives
[[theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_index|L251, the bound k(n) < max(64, (2^15 n)^(11/28))]].
Using Bourgain's exponent pair in the same construction gives
[[theory/integer_sequences/L253_exponent_pair_smooth_blocks/_index|L253, the bound k(n) <<_epsilon n^(38/97+epsilon) for every epsilon > 0]].
These project deductions are author-recorded at tier 0. The sketch also
records the $3/8$ limit of its exponent-pair estimate and the exact $1/3$
limit imposed by producing a product of three factors at most $K$, together
with the difficulty reduction of
[[theory/integer_sequences/L252_nonresidue_blocks_without_smooth_members/_index|L252]]:
an exponent below $1/(4\sqrt e)$ would improve the least-nonresidue bound
for primes $3\bmod4$. The
[[research/smooth_integer_intervals/literature|literature comparison]]
matches the located every-interval theorems at their exact parameters. The
displayed question of Problem 962, $\log k(n)\le(\log n)^{1/2+o(1)}$, is not
implied by any fixed power bound.
