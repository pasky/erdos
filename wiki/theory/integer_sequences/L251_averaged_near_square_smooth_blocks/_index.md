---
name: theory/integer_sequences/L251_averaged_near_square_smooth_blocks
title: Averaging the multiplier pushes the smooth-block exponent from 2/5 to 11/28
desc: |
  For K >= 64 and 0 <= m <= 2^(-15) K^(28/11) the block m+1, ..., m+K
  contains c(q-t)(q+t) with all three factors in [1, K]; so k(n) in Problem
  962 is below max(64, (2^15 n)^(11/28)), improving the exponent 2/5 of
  Erdős and Sárközy to 11/28.
tags: []
sources:
- problems/integer_sequences/E0962
id: L251
statement: |
  For all integers K >= 64 and m with 0 <= m <= 2^(-15) K^(28/11), the
  interval (m, m+K] contains an integer c(q-t)(q+t) in which c, q-t and q+t
  are positive integers at most K; in particular it contains an integer all
  of whose prime factors are at most K. Consequently k(n) < max(64,
  (2^15 n)^(11/28)) for every integer n >= 1, where k(n) is the largest
  integer k for which some integer m with 0 <= m <= n has each of m+1, ...,
  m+k divisible by a prime greater than k (the function of Problem 962; the
  bound holds equally when m is required to be positive). In Erdős's
  notation, the first sentence also gives n_k > 2^(-15) k^(28/11) for every
  integer k >= 64, where n_k is the least integer n >= 0 such that each of
  n+1, ..., n+k has a prime factor greater than k.
status: proved
tier: 0
depends_on:
- L250
created: 2026-10-15T22:27:51Z
updated: 2026-10-15T22:27:51Z
---

# Averaging the multiplier pushes the smooth-block exponent from 2/5 to 11/28

[[theory/integer_sequences/_index|..]]

[[theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_proof|_proof]]: Count pairs (c, q) with C < c <= 2C and cq^2 in a window of length about
K^2/C above m; Vaaler's inequality and the third-derivative test bound the
error by about C^(4/7) K^(1/7), below the main term K/C when C is at most
K^(6/11)/1024, and one adjustment lands within K of m.

***

This result is recorded by Plasma AI. It improves the exponent of the proved
upper bound for
[[problems/integer_sequences/E0962/_index|Problem 962, whose function k(n) it bounds by a constant times n^(11/28)]]:
$11/28\approx0.3929$, against $2/5$ from Erdős and Sárközy's 1979
construction and $1/2$ from the forum argument the problem page records.
It does not touch the displayed question of Problem 962, which asks for
$\log k(n)\le(\log n)^{1/2+o(1)}$.

## Meaning of the statement

Erdős and Sárközy write a $K$-smooth member of the block as $c(q-t)(q+t)$
with one multiplier $c$ chosen from $m$ alone; that choice forces
$m\ll K^{5/2}$, as
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_index|L250]]
records. Here the multiplier ranges over a whole interval $C<c\le2C$, and
one only needs some pair $(c,q)$ with $cq^2$ in a window
$(m,m+E]$ of length $E\asymp K^2/C$; the adjustment by $t$ then lands within
$K$ of $m$. The number of such pairs has main term of order $K/C$, and its
error term is a sum of the sawtooth function $\psi$ at $\sqrt{X/c}$ over the
multipliers. Vaaler's trigonometric approximation and the van der Corput
third-derivative test bound that sum by
$\ll C^{4/7}K^{1/7}+C^{3/4}(\log C)^{3/2}$, which stays below the main term
for $C\le K^{6/11}/1024$, that is, for $m$ up to about $K^{28/11}$.

## Standing and verification

Tier 0, author-recorded, with a complete
[[theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_proof|proof]];
no independent review has examined it. Reading the proof is the
verification procedure; every constant in it is explicit. The two analytic
inputs are source results consumed as stated, with their hypotheses checked
against the use in the proof: Vaaler's inequality and the explicit
third-derivative test, as Lemmas 7.1 and 8.6 of
[[../library/factorials_binomials/granville_1996_explicit_bounds_exponential_sums_scarcity_squarefree/_index|Granville and Ramaré (1996), whose held statements supply both inputs]]
print them. The proof records one misprint in the printed Lemma 7.1, the
place of a sign, and shows that the inequality it uses holds for the
corrected placement; only the moduli of the coefficients enter. Nothing
remains open within the stated scope.

**Dependency roles.**
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_index|L250 supplies the blocks with m at most K^(5/2)/128]],
where the averaging step is not needed; it is used at full strength, for
every $K\ge64$.

## Novelty and context

No every-interval result giving a diagonal exponent below $2/5$ was found in
the literature search that the
[[research/smooth_integer_intervals/literature|literature comparison for smooth integers in short intervals]]
records; that search is bounded and is not a novelty certificate. By its
abstract, Rivat and Shparlinski (2016) use the same toolkit, exponent pairs
with Vaaler polynomials, for multiples of squares in intervals of length
$x^{1/2}$, a different range; their full text was not read. The
[[research/smooth_integer_intervals/proof_sketch|research sketch]]
records the exponent this route gives from any exponent pair, the exact
limits of that calculation and of a three-factor output, and the next
tests toward Problem 962. The stronger asymptotic bound
[[theory/integer_sequences/L253_exponent_pair_smooth_blocks/_index|L253 uses Bourgain's exponent pair to obtain k(n) <<_epsilon n^(38/97+epsilon)]],
while this claim retains an explicit bound for every $n\ge1$.
