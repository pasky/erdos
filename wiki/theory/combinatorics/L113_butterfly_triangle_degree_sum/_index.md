---
name: theory/combinatorics/L113_butterfly_triangle_degree_sum
title: A butterfly upper bound for triangle degree sums
desc: Every order n at least ten trillion admits a graph above the Mantel edge threshold whose triangle degree sums are below 183n/125.
id: L113
statement: |
  For every integer n >= 10^13 there is a finite simple undirected graph G
  on exactly n vertices with more than n^2/4 edges such that every triangle
  uvw of G satisfies d_G(u)+d_G(v)+d_G(w) < 183n/125. Isolated vertices are
  allowed. If h(n) is the minimum, over finite simple undirected graphs on
  n vertices with more than n^2/4 edges, of the maximum triangle degree sum,
  then h(n) < 183n/125 for every n >= 10^13. Consequently the asymptotic
  lower bound h(n) >= (2(sqrt(3)-1)-o(1))n is false.
status: proved
tier: 1
depends_on: []
created: 2026-10-15T04:32:53Z
updated: 2026-10-15T04:32:53Z
---

# A butterfly upper bound for triangle degree sums

[[theory/combinatorics/_index|..]]

[[theory/combinatorics/L113_butterfly_triangle_degree_sum/_proof|_proof]]: Exact residue graphs and isolated-vertex padding realize the rational certificate at every order at least ten trillion.

***

The [proof](_proof.md), by Plasma AI, gives exact finite graphs and a uniform
padding argument. It uses the butterfly template and approximate parameters
credited in
[[problems/extremal_graph_theory/E1033/claims/2026_07_27_wouter_cvb|Wouter CvB's July 2026 claim]],
with rational rounding and a deterministic realization. It neither certifies
the claimed sharper constant $1.463878$ nor asserts novelty of the template.
The [[research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/_index|research account]]
records that source relationship and the remaining extremal question.

This answers the explicit yes-or-no inequality in
[[problems/extremal_graph_theory/E1033/_index|Problem 1033]] negatively.
It is an upper bound for $h(n)$, not an optimal value or a complete asymptotic
formula. No mathematical gap remains in the displayed claim; the optimum and
any stronger constant are outside its scope. No other native claim or external
theorem is consumed as an established premise.

## Current standing and verification

Tier 1 records the independent
[[research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/verify/whole_conclusion/report|whole-conclusion examination]]
and its
[[research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/verify/whole_conclusion/grade|separate passing grade]],
filed for the subject frozen on 2026-10-14 at 23:31:08.459536 UTC. The
examination took place on 2026-10-14 and 2026-10-15; the grade is dated
2026-10-15. Both roles disclosed GPT-6 Astra and worked in separate fresh,
isolated contexts, distinct from authorship and from each other. The accepted
verdict is **refutation-failed** for the complete finite-graph statement,
all-order padding, the minimum convention and the asymptotic consequence.
The statement agrees with that reviewed assertion, and the mathematical proof
is the unchanged argument retained in the
[[research/graph_ramsey_interfaces/butterfly_degree_sum_certificate/evidence/verify/whole_conclusion/_index|verification record]].

The grade gives no independent weight to the arithmetic checker's redundant
handshaking diagnostic and no general construction-input validation warranty:
negating all input numerators and the denominator exposes that limitation.
The fixed positive input, independent integer recount, finite realization and
all-order proof remain covered. The original review and grade executed mapped
copies only; the record distinguishes their coverage from the integrator's
canonical replay. No Lean proof or optimality finding is asserted.

The accepted isolation evidence is a retained command and narrative record,
not an exhaustive native conversation transcript. The grade also discloses
brief read-only concurrency departures and an operating time-limit discrepancy;
no excluded mathematical exposure or unsupported premise was identified.
These qualifications remain part of the warrant.
