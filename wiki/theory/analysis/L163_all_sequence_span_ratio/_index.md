---
name: theory/analysis/L163_all_sequence_span_ratio
title: Logarithmic growth of the consecutive-span ratio for every sequence
desc: For every circle sequence, repeated points allowed, the limiting upper ratio of largest to smallest r-spans is at least 1 + log(r)/(200r) for all sufficiently large r.
id: L163
statement: |
  On the circle R/Z, let X be any infinite sequence, repeated terms allowed.
  For n >= r, order the first n labels by position, breaking ties by arrival
  index, and extend their real lifts by y_(i+n) = y_i + 1. Let M_n^(r) and
  m_n^(r) be the maximum and minimum of y_(i+r)-y_i over 1 <= i <= n.
  Interpret M/0 as positive infinity and log as the natural logarithm.
  There is an absolute integer r0 such that for every integer r >= r0
  and every X, limsup_n M_n^(r)/m_n^(r) >= 1 + log(r)/(200r).
  If mu_r = inf_X limsup_n M_n^(r)/m_n^(r) over the same sequence family,
  then r(mu_r-1) >= log(r)/200 for r >= r0, and r(mu_r-1) tends to
  positive infinity as r tends to infinity through the positive integers.
status: proved
tier: 1
depends_on: []
created: 2026-10-15T20:39:29Z
updated: 2026-10-15T20:39:29Z
---

# Logarithmic growth of the consecutive-span ratio for every sequence

[[theory/analysis/_index|..]]

[[theory/analysis/L163_all_sequence_span_ratio/_proof|_proof]]: Converts a putative small ratio into uniformly small short-arc count errors, extracts a finite list, and contradicts its explicit prefix discrepancy lower bound.

[[theory/analysis/L163_all_sequence_span_ratio/evidence/_index|evidence/]]: Exact mathematical subjects and independently graded examination of the ratio theorem and its exact extremal consequences.

***

The [proof](_proof.md) combines the reconstructed span-to-count argument of
S. Korsky's unrefereed arXiv:2609.07196v2 with a complete finite-list
lower bound following Larcher's range splitting. The extension to coincident
terms, finite-list argument with its explicit constant, and local composition
are credited to Plasma AI. This gives the ratio part of the mean-normalized
[[problems/analysis/E1221/_index|Problem 1221]]. The coefficient $1/100$ in
Korsky's statement is outside this claim.

## Conventions and scope

Spans are forward lifted arcs, or sums of $r$ consecutive nonnegative gaps;
they are not shortest unoriented distances. Their sum is $r$, so
$nm_n^{(r)}\le r\le nM_n^{(r)}$ and $M_n^{(r)}>0$. Counts in the proof
retain label multiplicity in half-open arcs $(x,x+\ell]$, $\ell<1$.
All limits in $n$ use integers $n\ge r$. The constant $r_0$ is independent of
$X$, although intermediate time thresholds can depend on $X$ and $r$.
No optimal coefficient, attained infimum or conclusion for every small $r$
is asserted.

## Current standing and verification

Tier 1 records the
[[theory/analysis/L163_all_sequence_span_ratio/evidence/verify/whole_statement/report|whole-statement adversarial examination]]
and its
[[theory/analysis/L163_all_sequence_span_ratio/evidence/verify/whole_statement/grade|distinct passing grade]],
both dated 2026-10-15. The mathematical subject was frozen on that date at
09:49:19.072889 UTC. Both roles disclosed GPT-6 Astra and worked in separate
fresh, isolated contexts, distinct from authorship and from each other.
The accepted verdict is **refutation-failed** for the full sequence theorem,
its exact ratio infimum and the divergence. The statement above has exactly
that scope. The complete supplied proofs, including the finite-prefix lower
bound, were examined; no native claim or unprovided external theorem was
consumed as an established premise.

The original publications were unread by the reviewer and grader, so their
mathematical acceptance is of the supplied local deductions, not independent
source fidelity. The unavailable inbox was not established empty; the grader's
eligibility ruling rests on the complete available received-input and action
records. Opaque internal fields were retained but not decoded. The
[[theory/analysis/L163_all_sequence_span_ratio/evidence/verify/whole_statement/_index|verification record]]
retains these limits, the exact subject and the presentation correction in the
grading derivation. There is no Lean or computational warrant.

No mathematical gap remains in this claim. The
[[research/erdos_1221/all_sequence_composition|combined research argument]]
explains its composition with the separate one-sided bounds. Whole-conclusion
scrutiny of that combination and its match to the modified Statement are
separate from this claim's warrant.
