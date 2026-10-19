---
name: theory/analysis/L164_all_sequence_span_deviations
title: Unbounded one-sided consecutive-span deviations for every sequence
desc: Every circle sequence has upper-span excess and lower-span deficit with limsup at least a positive absolute constant times the square root of log r, for all sufficiently large r.
id: L164
statement: |
  On the circle R/Z, let X be any infinite sequence, repeated terms allowed.
  For n >= r, order the first n labels by position, breaking ties by arrival
  index, and extend their real lifts by y_(i+n) = y_i + 1. Let M_n^(r) and
  m_n^(r) be the maximum and minimum of y_(i+r)-y_i over 1 <= i <= n.
  There are absolute constants c > 0 and integer r0 such that, for every
  integer r >= r0 and every X, limsup_n(n M_n^(r)-r) >= c sqrt(log r)
  and limsup_n(r-n m_n^(r)) >= c sqrt(log r), with natural logarithms.
  Set Lambda_r = inf_X limsup_n n M_n^(r) and
  lambda_r = sup_X liminf_n n m_n^(r) over this same family.
  Then Lambda_r-r and r-lambda_r are each at least c sqrt(log r) for
  every integer r >= r0, and both tend to positive infinity as r tends
  to infinity through positive integers. The two deviations need not
  occur at the same times.
status: proved
tier: 1
depends_on: []
created: 2026-10-15T20:39:29Z
updated: 2026-10-15T20:39:29Z
---

# Unbounded one-sided consecutive-span deviations for every sequence

[[theory/analysis/_index|..]]

[[theory/analysis/L164_all_sequence_span_deviations/_proof|_proof]]: Each one-sided span hypothesis yields uniform short-arc L1 control, contradicted by the complete planar discrepancy bound after localization.

[[theory/analysis/L164_all_sequence_span_deviations/evidence/_index|evidence/]]: Exact mathematical subjects and independently graded examination of the two one-sided sequence bounds and their separate extremal consequences.

***

The [proof](_proof.md) uses the one-sided transport and localization mechanism
of S. Korsky's unrefereed arXiv:2609.07196v2. It includes the local complete
proof of Halász's planar $L^1$ bound, following Bilyk, with constant
$1/41000$. The extension to coincident terms, local constant calculations and
composition are credited to Plasma AI. It gives the first two parts of the
mean-normalized [[problems/analysis/E1221/_index|Problem 1221]].

## Conventions and scope

The $r$-spans are forward lifted arcs, each a sum of $r$ consecutive gaps,
including zero and full-turn spans. They are not shortest circle distances.
Their sum is $r$. Counting arcs are half-open $(x,x+\ell]$, $\ell<1$,
and counts retain multiplicity. Limits use integer $n\ge r$.
The constants $c,r_0$ are independent of the sequence, whereas intermediate
onset times may depend on it and on $r$. The two limsups are separate
assertions, with no common subsequence required. Small-$r$ bounds, optimal
constants and attained extrema are outside the statement.

## Current standing and verification

Tier 1 records the
[[theory/analysis/L164_all_sequence_span_deviations/evidence/verify/whole_statement/report|whole-statement adversarial examination]]
and its
[[theory/analysis/L164_all_sequence_span_deviations/evidence/verify/whole_statement/grade|distinct passing grade]],
both dated 2026-10-15, for the mathematical subject frozen at
09:49:19.072889 UTC. Both roles disclosed GPT-6 Astra in separate fresh,
isolated contexts, distinct from authorship and each other. The grade accepts
**refutation-failed** separately for both sequence bounds, the infimum
consequence and its divergence, and the supremum consequence and its
divergence. The statement above retains exactly that scope.

The complete supplied deductions were examined, including the whole planar
proof and both anchored conventions. Neither the ratio theorem nor a native
L-claim or unprovided external theorem is an established premise. The original
publications remained unread by the reviewer and grader; original-paper
fidelity and refereeing are not implied.

The grade rejects the report's blanket historical assertion that no messages
were read: the reviewer later read its own authorized sent receipt. The grader
ruled this own-output confirmation immaterial by the content test. No incoming
message or excluded communication was identified as consumed. The unavailable
inbox was not established empty, and opaque internal fields were not decoded.
The [[theory/analysis/L164_all_sequence_span_deviations/evidence/verify/whole_statement/_index|verification record]]
retains the unchanged report and this controlling qualification. No Lean or
computational warrant is asserted.

No mathematical gap remains in this claim. Its role in the full question and
the separate obligation to examine the combined conclusion are described by
[[research/erdos_1221/all_sequence_composition|the combined research argument]].
