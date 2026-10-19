---
name: theory/additive_bases/L33_dyadic_root_floor_completeness
title: Strong completeness at roots of the dyadic base
desc: Two residue classes of exponents turn a single geometric floor sequence into the two rays of the accepted dyadic completeness theorem.
id: L33
statement: |
  For every integer m>=2, real t>0, integer L>=0 and finite set F of
  integers, put gamma=2^(1/m). Every sufficiently large integer is a sum
  of distinct positive values in {floor(t gamma^n): n>=L} outside F.
  In particular this value set remains complete after any finite deletion.
status: proved
tier: 1
depends_on: []
created: 2026-10-14T18:42:37Z
updated: 2026-10-16T06:44:50Z
---

# Strong completeness at roots of the dyadic base

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L33_dyadic_root_floor_completeness/_proof|_proof]]: A sufficiently late tail has distinct positive values and contains two disjoint indexed rays to which the accepted theorem applies.

***

The [proof](_proof.md) is a short deduction by Plasma AI from the
[[../library/additive_bases/jenw1n_2026_erdos_354_part_i_lean_proof/target|accepted dyadic two-ray completeness theorem]].
The input is consumed at its recorded acceptance standing. Its statement
and indexed-sum convention have been inspected; its long proof is not
reconstructed here. The independent examination and separate grade below
accept the deduction at this external-source boundary. No Lean proof of
L33 or novelty assertion is recorded.

Taking $m=2$ supplies the existential-base reading of
[[problems/additive_bases/E0354/_index|Problem 354(ii)]] using either one
of its two rays. It also supplies all coefficients $t>0$ at the bases
$2^{1/m}$ for [[problems/additive_bases/E0349/_index|Problem 349]].
It gives neither the universal-base reading nor the whole classification
of Problem 349, and gives no threshold uniform in $t,m,L,F$.

The
[[research/leads/dyadic_root_floor_completeness/_index|research account]]
separates these formulations and explains why indexed multiplicity does
not obstruct this deduction. Verification is the exponent regrouping,
irrationality of the coefficient ratio, and eventual strict increase.

## Current standing and verification

Tier 1 records the independent
[[research/erdos_354/evidence/verify/dyadic_roots/report|whole-conclusion examination]]
and its
[[research/erdos_354/evidence/verify/dyadic_roots/grade|separate passing grade]],
both dated 2026-10-14. The reviewer and distinct grader each worked in a
fresh, isolated context and disclosed GPT-6 Astra. The accepted verdict
is **refutation-failed** for the whole single-ray theorem, arbitrary
finite deletion and the existential-base consequence at $\sqrt2$. The
canonical statement and proof have the same mathematical scope and
argument as the
[[research/erdos_354/evidence/verify/dyadic_roots/_index|preserved examination subject]].

The reviewer received excess source-proof and acceptance prose during a
dependency read. The grader ruled this exposure immaterial to both
conclusions by a content comparison, without treating its disclosure or
a corrected read as restoring independence. The record preserves the
exposure, the ruling and the historical-record limits.

The external indexed dyadic theorem was inspected at claims-checked
depth: its statement, convention and recorded acceptance were checked;
its full proof was not inspected and its kernel replay was not rerun.
No native L-claim is a premise. Neither the universal-base reading of
Problem 354(ii), the full classification in Problem 349 nor an effective
uniform threshold is covered by this grade.
