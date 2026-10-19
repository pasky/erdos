---
name: theory/irrationality/L219_dilation_design_prime_count
title: Signed dilation designs cancelling K levels need K+1 primes
desc: |
  A signed family of prime dilations, with admissible shifts and primes above
  K, that cancels levels 1 to K for every function uses at least K+1
  distinct primes, whose product therefore exceeds K^(K+1).
tags: []
sources:
- problems/irrationality/E0249
id: L219
statement: |
  Let K>=1 be an integer and V a nonempty finite set. For each v in V let
  p_v be a prime with p_v>K, s_v an integer and c_v a nonzero integer, the
  pairs (p_v,s_v) being distinct. Suppose that for every h in {1,...,K}
  and every integer m the sum of c_v over those v with p_v*h-s_v=m is
  zero, and that some integer n satisfies n congruent to s_v modulo p_v
  for every v in V. Then the set {p_v : v in V} has at least K+1 elements,
  and the product of its elements exceeds K^(K+1).
status: proved
tier: 0
depends_on: []
created: 2026-10-15T20:31:18Z
updated: 2026-10-15T20:31:18Z
---

# Signed dilation designs cancelling K levels need K+1 primes

[[theory/irrationality/_index|..]]

[[theory/irrationality/L219_dilation_design_prime_count/_proof|_proof]]: Each vertex needs a fiber-mate at every cancelled level; the mates are
distinct, and admissibility forces their primes to be distinct.

***

## Statement

Let $K\ge1$ and let $V$ be a nonempty finite set. For each $v\in V$ let
$p_v>K$ be a prime, $s_v$ an integer and $c_v$ a nonzero integer, the pairs
$(p_v,s_v)$ being distinct. Suppose that for every $h\in\{1,\dots,K\}$ and
every integer $m$,

$$
\sum_{v:\ p_vh-s_v=m}c_v=0,
$$

and that some integer $n$ satisfies $n\equiv s_v\pmod{p_v}$ for every
$v\in V$. Then the set $\{p_v:v\in V\}$ has at least $K+1$ elements, and
the product of its elements exceeds $K^{K+1}$.

## Significance

For admissible $n$ the numbers $n+p_vh-s_v=p_v(N_v+h)$, with
$N_v=(n-s_v)/p_v$, are the arguments at level $h$ of a signed combination of
prime dilations of shift tails, as in the alternating cube of the
[[research/leads/totient_binary_series/dilation_cube|prime dilation page]].
The hypothesis says that levels $1,\dots,K$ cancel for every function in
place of the totient. The cube does this with $2^K$ distinct primes; the
claim shows that every such design needs at least $K+1$. When the design is
averaged over a residue class with at least two representatives inside
$[x/2,x]$, the product is at most $x$, which forces
$K<(1+o(1))\ln x/\ln\ln x$, a vanishing fraction of the $\log_2x$ levels
that determine the phase of the binary tail. The
[[research/totient_binary_new_attack/dilation_designs|design bound page]]
draws this consequence for
[[problems/irrationality/E0249/_index|Problem 249]] and records its scope.
The claim neither proves nor disproves the irrationality of
$\sum_{n\ge1}\varphi(n)2^{-n}$. The cube is not the most economical design:
the design bound page exhibits a three-level design with six distinct
primes, and a four-level integer configuration with twelve points.
The latter has not been realized with prime first coordinates here. The
minimum number of primes for general $K$ is not determined.

## Current standing and verification

The complete [proof](_proof.md) is author-recorded at tier 0, with no
independent acceptance, formal verification, or novelty claim. No native
L-claim is consumed, and no computation is required. The proof uses only
that a prime dividing a product divides one of its factors and that distinct
primes do not divide one another.
