---
name: theory/integer_sequences/L250_explicit_near_square_smooth_blocks
title: Every block of K integers below K^(5/2)/128 contains a product of three integers at most K
desc: |
  For K >= 64 and 0 <= m <= K^(5/2)/128 the block m+1, ..., m+K contains
  c(q-t)(q+t) with all three factors in [1, K], so k(n) in Problem 962 is
  below max(64, (128n)^(2/5)); an explicit form of Erdős and Sárközy's 1979
  exponent 2/5.
tags: []
sources:
- problems/integer_sequences/E0962
id: L250
statement: |
  For all integers K >= 64 and m with 0 <= m <= K^(5/2)/128, the interval
  (m, m+K] contains an integer c(q-t)(q+t) in which c, q-t and q+t are
  positive integers at most K; in particular it contains an integer all of
  whose prime factors are at most K. Consequently k(n) < max(64,
  (128n)^(2/5)) for every integer n >= 1, where k(n) is the largest integer
  k for which some integer m with 0 <= m <= n has each of m+1, ..., m+k
  divisible by a prime greater than k (the function of Problem 962; the
  bound holds equally when m is required to be positive).
status: proved
tier: 0
depends_on: []
created: 2026-10-15T22:27:51Z
updated: 2026-10-15T22:27:51Z
---

# Every block of K integers below K^(5/2)/128 contains a product of three integers at most K

[[theory/integer_sequences/_index|..]]

[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_proof|_proof]]: Scale m by c so that m/c is at most K^2/16, take the next square q^2 above
m/c, and subtract the largest admissible t^2; the three factors stay below
K and the overshoot c(2t+1) stays below 3K/4.

***

This result is recorded by Plasma AI as an explicit specialization of a
construction due to Erdős and Sárközy. It bears on the upper bound of
[[problems/integer_sequences/E0962/_index|Problem 962, whose function k(n) it bounds by an explicit multiple of n^(2/5)]].

## Meaning and source

A block $m+1,\ldots,m+K$ in which every term has a prime factor greater than
$K$ is exactly a block with no $K$-smooth member. The statement exhibits a
$K$-smooth member of every such block with $m\le K^{5/2}/128$, as a product
$c(q-t)(q+t)$ of three factors at most $K$: the multiplier $c$ brings
$m/c$ below $K^2/16$, the next square $q^2$ above $m/c$ lies within $2q$ of
it, and subtracting the largest $t^2$ that keeps $c(q^2-t^2)$ above $m$
leaves a gap of at most $c(2t+1)<K$.

The construction is that of
[[../library/integer_sequences/erdos_sarkozy_1979_prime_factors_consecutive_integers/theorem_2|Erdős and Sárközy's Theorem 2]], On the prime factors
of $\binom nk$ and of consecutive integers, Utilitas Math. 16 (1979),
197--215, section 3, the proof of their Theorem 2 (printed p. 198): "If
$k>k_0$, then $n_k>k^{5/2}/16$", where $n_k$ is the smallest $n$ with
$P(n+i)>k$ for $1\le i\le k$ and $P$ is the greatest prime factor (printed
p. 197). A public scan is at
[the Rényi Institute's Erdős archive](https://static.renyi.hu/~p_erdos/1979-15.pdf).
Friedlander and Lagarias (J. Number
Theory 25 (1987), 249--273, Theorems 3 and 4) give the same exponent, with
an $\varepsilon$ of slack, from the case $r=2$ of their construction, which
they credit independently to Balog and Sárközy. This card adds what the
asymptotic statements leave implicit: explicit constants valid for every
$K\ge64$, every $m\ge0$ with no exceptional small range, and the
translation to $k(n)$ with its endpoint convention.

## Standing and verification

Tier 0, author-recorded, with a complete elementary
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_proof|proof]];
reading it is the verification procedure. Nothing remains open within the
stated scope. The exponent $2/5$ is the known waypoint: it is the 1979
theorem with explicit constants, not a new exponent.

## Uses and context

The claim
[[theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_index|L251 consumes this statement for the blocks with m at most K^(5/2)/128]]
and covers the larger range up to $2^{-15}K^{28/11}$ by averaging the
multiplier $c$. The
[[research/smooth_integer_intervals/proof_sketch|research sketch on smooth integers in every short interval]]
places both exponents against the full question of Problem 962 and records
why this construction stops at $2/5$ when the multiplier is fixed.
