---
name: theory/number_theory/L34_exceptional_widths_for_omega
title: Exceptional widths prevent unbounded clustering for shifted omega
desc: A second-moment estimate permits widths to be enlarged on a density-zero set while keeping every normalized local count bounded.
id: L34
statement: |
  Let omega(n) count the distinct prime divisors of the positive integer n.
  There is F:[1,infinity)->(0,infinity) with F(x)->infinity as x->infinity,
  and a set G of positive integers of natural density one such that
  F(n)/omega(n)->0 as n->infinity through G, while for every sufficiently
  large real x the number of positive integers n satisfying
  x<n+omega(n)<x+F(x), divided by F(x), is at most 7.
status: proved
tier: 1
depends_on: []
created: 2026-10-14T18:42:37Z
updated: 2026-10-16T06:44:50Z
---

# Exceptional widths prevent unbounded clustering for shifted omega

[[theory/number_theory/_index|..]]

[[theory/number_theory/L34_exceptional_widths_for_omega/_proof|_proof]]: A dyadic second-moment argument bounds the count at ordinary locations and identifies a density-zero set where large widths are harmless.

***

The [proof](_proof.md) is an independently examined argument by Plasma AI using
[[../library/arithmetic_functions/erdos_1997_locally_repeated_values_arithmetic_functions_iv/lemma_1|Erdős–Pomerance–Sárközy Lemma 1]]
at modulus $1$. Its hypotheses and conclusion are inspected at statement
depth; the source proof is not independently verified here. This claim
has the independently graded review below and no Lean proof.

L34 gives a negative answer for $f=\omega$ under the literal
almost-all width condition in the modified statement of
[[problems/arithmetic_functions/E0122/_index|Problem 122]]. It does not
classify the other arithmetic functions. The
[[research/leads/exceptional_widths_shifted_omega/_index|research account]]
distinguishes density-one smallness from a uniform or monotone width
condition and from the historical unpublished affirmative report.

There is no computational premise. Verification consists of specializing
the source lemma, bounding the exceptional input and interval sets,
checking the real-location extension, and proving density-one smallness
of the constructed widths.

## Current standing and verification

Tier 1 records the independent
[[research/leads/exceptional_widths_shifted_omega/evidence/verify/width_counterexample/report|whole-conclusion examination]]
and its
[[research/leads/exceptional_widths_shifted_omega/evidence/verify/width_counterexample/grade|separate passing grade]],
both dated 2026-10-14. The reviewer and distinct grader each worked in a
fresh, isolated context and disclosed GPT-6 Astra. The accepted verdict
is **refutation-failed** for the complete density-one construction,
including the everywhere real width limit and eventual normalized-count
bound of seven. The canonical statement has exactly that scope, and its
proof preserves the examined core argument.

The canonical proof omits the literal stronger-width assertion at
lines 104–106 of the
[frozen argument](../../../research/leads/exceptional_widths_shifted_omega/evidence/assets/width_subject/argument.md).
Its separately accepted verdict is **proof defective; statement
unresolved**: that assertion requires infinitude of the exceptional set,
which was not established and is not consumed by L34. The grade also
accepts **refuted-as-stated** for the unused universal strict EPS97
wording at $x=2,m=1,h=0,f\equiv0$. This does not affect the consumed
$K=1$, $X\ge2$ specialization or certify its proof.

No native L-claim is a premise. The EPS97 statement was checked from the
supplied source interfaces; its proof was not independently verified,
and Euler's divergence remains an explicit classical premise. No result
for other $f$, everywhere-small or monotone widths, historical priority,
or the unpublished affirmative report is accepted by this grade.
