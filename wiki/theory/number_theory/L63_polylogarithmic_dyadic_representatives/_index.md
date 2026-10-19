---
name: theory/number_theory/L63_polylogarithmic_dyadic_representatives
title: Polylogarithmic dyadic representatives imply short factorial sums
desc: |
  A conditional criterion for Problem 18(c): dyadic residue sums with a
  factorial index linear up to logarithms, polylogarithmic length, and a
  polylogarithmic height exponent imply a polylogarithmic bound for h(n!).
id: L63
statement: |
  Put L(t)=1+log_2(t+1). Fix real a,b,d>=0 and C>=1. Suppose that for every
  sufficiently large integer k there are integers F,u,D>=1 with
  F<=C k L(k)^a, u<=C L(k)^b, and D<=C L(k)^d, such that every residue
  modulo 2^k has a nonnegative representative S<=2^(kD) which is a sum of
  at most u positive divisors of F!, with repetition allowed. Then
  h(n!)=O((log n)^(a+b+d+3)) as n tends to infinity. Here h(N) is the
  least bound on the number of distinct positive divisors of N needed to
  represent each integer 1<=R<N; each R may use its own set of divisors.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T08:41:00Z
updated: 2026-10-14T08:41:00Z
---

# Polylogarithmic dyadic representatives imply short factorial sums

[[theory/number_theory/_index|..]]

[[theory/number_theory/L63_polylogarithmic_dyadic_representatives/_proof|_proof]]: Positive modular lifting, removal of repeated divisors, and a factorial
radix chain with every index, count, and height cost retained.

***

This conditional deduction is recorded by Plasma AI. It supplies the exact
local interface in the
[[research/erdos_18/dyadic_representative_route|dyadic route to Problem 18(c)]].
Its hypothesis is unproved for the required parameters. It therefore gives no
new unconditional bound for
[[problems/divisors/E0018/_index|Problem 18]].

The [proof](_proof.md) keeps three costs separate: the factorial index needed
for each residue, the number of terms, and the size of its nonnegative
representative. It permits repeated local summands, then removes repetitions
after lifting. Only dyadic moduli occur; no separate odd-prime covering is
needed for this criterion.

**Standing.** Tier 0, author-recorded. The proof is elementary and is not
independently reviewed or formalized here. It adapts the radix, lifting and
distinctness mechanisms in the
[[../library/divisors/jenw1n_2026_lean_proof_erdos_problem_18b/target|accepted proof of part (b)]],
but the quantitative implication stated here is a separate deduction. There is
no computational evidence entry point: verification consists of checking the
proof, in particular the accumulated factorial index and the two iteration
counts. The remaining mathematical obligation for part (c) is to construct the
representatives in the hypothesis.
