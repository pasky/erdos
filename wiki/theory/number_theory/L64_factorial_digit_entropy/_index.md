---
name: theory/number_theory/L64_factorial_digit_entropy
title: Subexponential support of short factorial divisor blocks
desc: |
  A counting obstruction to fixed positive dyadic nonconcentration for
  polylogarithmically many separated divisor digits with factorial index
  linear up to logarithms in the total bit length.
id: L64
statement: |
  Put L(K)=1+log_2(K+1). Fix B,C>=0. As the integer K tends to infinity,
  let F,u,b0 be integers with 1<=F<=K L(K)^C, 0<=u<=L(K)^B, b0>=0,
  and 2^b0<=F. For nonnegative integer widths w1,...,wu with
  b0+sum wi<=K, let S be the set
  of integers x0+sum_i 2^(b0+w1+...+w(i-1)) di, where 0<=x0<2^b0
  and each di is either zero or a positive divisor of F! less than 2^wi.
  Then log_2 |S|=o(K), uniformly over these choices. In particular no probability measure supported on S
  modulo 2^K has every atom at most 2^(-gamma K) for any fixed gamma>0
  and all sufficiently large K.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T08:41:00Z
updated: 2026-10-14T08:41:00Z
---

# Subexponential support of short factorial divisor blocks

[[theory/number_theory/_index|..]]

[[theory/number_theory/L64_factorial_digit_entropy/_proof|_proof]]: Small primes cost a sublinear number of bits, while the total bit budget
permits only O(K/log K) large prime factors across all the blocks.

***

This counting result is recorded by Plasma AI. Its
[proof](_proof.md) counts the prime factors across all blocks together and
requires no prime-counting estimate.

It identifies a limitation of the separated-digit construction in the
[[research/erdos_18/dyadic_representative_route|dyadic route to Problem 18(c)]]:
shrinking its factorial index to $K(\log K)^{O(1)}$ destroys any fixed
positive nonconcentration exponent. This does not exclude short sums of
arbitrary factorial divisors, a different construction, or an estimate with
parameters varying with $K$.

**Standing.** Tier 0, author-recorded; no independent review or formalization.
Verification consists of checking the prime-factor count and its uniform
asymptotics. No computation is used. The claim is closed as a counting
statement. Combined with the necessary factor count $rg\ge1$ in
[[theory/number_theory/L66_divisor_residue_spread/_index|L66]], it also
rules out a polylogarithmic value of the source's displayed block-expansion
bound with scale-dependent parameters. Different laws or a different
representation argument remain open.
