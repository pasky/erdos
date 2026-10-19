---
name: theory/integer_sequences/L253_exponent_pair_smooth_blocks
title: An exponent-pair bound for smooth blocks
desc: |
  Bourgain's exponent pair applied to the averaged near-square construction
  gives a K-smooth integer in every block (m,m+K] with
  m <= K^(97/38-delta), for large K depending on delta, and hence
  k(n) <<_epsilon n^(38/97+epsilon) in Problem 962.
tags: []
sources:
- problems/integer_sequences/E0962
id: L253
statement: |
  For every real delta with 0 < delta < 1/20 there is an integer K_0(delta)
  >= 64 such that, for every integer K >= K_0(delta) and every integer m
  with 0 <= m <= K^(97/38-delta), the interval (m,m+K] contains an integer
  c(q-t)(q+t) whose three factors c, q-t and q+t are positive integers at
  most K. Consequently, for every epsilon > 0 there is a constant
  A_epsilon such that k(n) <= A_epsilon n^(38/97+epsilon) for every integer
  n >= 1. Here k(n) is the largest integer k for which some integer m with
  0 <= m <= n has each of m+1, ..., m+k divisible by a prime greater than
  k; the same conclusions hold when m is required to be positive.
status: proved
tier: 0
depends_on:
- L250
- L251
created: 2026-10-15T22:54:40Z
updated: 2026-10-15T22:54:40Z
---

# An exponent-pair bound for smooth blocks

[[theory/integer_sequences/_index|..]]

[[theory/integer_sequences/L253_exponent_pair_smooth_blocks/_proof|_proof]]: Match the reciprocal square-root phase to Bourgain's exponent pair,
use Vaaler's inequality to bound the multiplier discrepancy, and show
that its error is uniformly smaller than the pair-count main term for
m <= K^(97/38-delta).

***

This result is recorded by Plasma AI. It applies Bourgain's published
exponent-pair theorem to the multiplier sum in
[[theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_index|L251's averaged near-square construction]].
It gives a uniform upper bound for
[[problems/integer_sequences/E0962/_index|Problem 962's function k(n)]]
with any fixed exponent greater than $38/97\approx0.391753$. In
particular, choosing $0<\varepsilon<3/2716$ improves the exponent
$11/28$ of L251. It does not prove a bound with exponent exactly $38/97$
and a fixed constant, nor the subpower conjecture in Problem 962.

## Argument and dependencies

The analytic input is
[[../library/number_theory/bourgain_2017_decoupling_exponential_sums_riemann_zeta/theorem_6|Bourgain's Theorem 6]], *Decoupling, exponential
sums and the Riemann zeta function*, J. Amer. Math. Soc. 30 (2017),
205--224, in the version
[arXiv:1408.5794v2](https://arxiv.org/abs/1408.5794v2), Section 5:
$(13/84+\eta,55/84+\eta)$ is an exponent pair for every $\eta>0$.
For the exact monomial phase here it gives

$$
\left|\sum_{C<c\le2C}e\bigl(r\sqrt{X/c}\bigr)\right|
\ll_\eta C^{1/2}(rY_X)^{13/84+\eta},\qquad
Y_X=\sqrt{X/C},\quad rY_X\ge2C.
$$

The [[theory/integer_sequences/L253_exponent_pair_smooth_blocks/_proof|proof]]
checks that phase against the source's monomial class, then sums over the
Fourier frequencies and compares with the main term in the pair count.
The source theorem is consumed as a published analytic input; its full
decoupling argument is not reproduced here.

**Dependency roles.**
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_index|L250 covers every m at most K^(5/2)/128]].
The proof of
[[theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_proof|L251 supplies the elementary counting and adjustment lemmas and the Vaaler inequality, including its integer-endpoint convention]].
L253 does not consume L251's third-derivative estimate or the numerical
constant $2^{-15}$.

## Standing and remaining question

Tier 0, complete author-recorded proof, without independent examination.
Reading the proof and its stated source interface is the verification
procedure; no computational certificate or Lean result is used. Nothing
remains open within this statement's scope.

The
[[research/smooth_integer_intervals/literature|literature comparison]]
records the inspected uniform smooth-number results and the limits of the
novelty search. The
[[research/smooth_integer_intervals/proof_sketch|research sketch]]
keeps the stronger multiplier estimates and the full subpower question
separate from this completed power bound.
