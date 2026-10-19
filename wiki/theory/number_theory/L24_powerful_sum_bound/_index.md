---
name: theory/number_theory/L24_powerful_sum_bound
title: A uniform bound for sums of two powerful integers
desc: A quadratic norm count and dyadic interpolation give at most N^(2/5+o(1)) ordered representations of N as a sum of two positive powerful integers.
id: L24
statement: |
  Let R(N) count ordered pairs of positive powerful integers u,v with u+v=N,
  where an integer is powerful if each of its prime divisors occurs to
  exponent at least two, and 1 is powerful. For every epsilon>0 there is
  C_epsilon such that R(N)<=C_epsilon N^(2/5+epsilon) for all integers N>=2.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

# A uniform bound for sums of two powerful integers

[[theory/number_theory/_index|..]]

[[theory/number_theory/L24_powerful_sum_bound/_proof|_proof]]: A field-uniform count for each pair of cube factors, followed by three complementary bounds on every dyadic box.

***

The [proof](_proof.md) gives a uniform subpower bound for each pair of
squarefree cube factors, then sums over the varying factors. It is a complete
author-recorded argument by Plasma AI, with no independent review or Lean
proof and no novelty claim. No other native claim is used. The standard
ideal-factorization and imaginary-quadratic-unit facts used in the proof are
stated there; the elementary divisor estimate is also proved there.

No mathematical gap remains in the stated bound. For
[[problems/diophantine_problems/E0943/_index|Problem 943]], the desired
bound is $N^{o(1)}$. This result leaves an exponent $2/5$ and does not
resolve that question. The
[[research/powerful_numbers_and_products/_index|research account]]
identifies the balanced range where all three estimates used in the proof
have the same loss. Verification is mathematical: check the norm injection,
its uniformity in the quadratic field, and the dyadic interpolation. No
computational certificate is needed.
