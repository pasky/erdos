---
name: theory/combinatorics/L238_normalized_core_near_clique_bound
title: Near-clique density in a minimum-anchor core
desc: An r-set with h missing edges in a normalized two-supported core satisfies r at most a(h+1), excluding the one-hole fold pattern when r exceeds 2a.
id: L238
statement: |
  Let r>=12 and 4<=a<r be integers. For n=rq+c with 0<=c<r, put
  D_r(n)=binom(n,2)-(r-1)(r binom(q,2)+qc). Let H be a finite simple
  graph with ar+1 vertices and independence number a, and let
  Q={q_1,...,q_a} be an independent anchor set. Every nonanchor has
  exactly one or two neighbors in Q. Let P_i consist of q_i and the
  vertices whose only anchor neighbor is q_i; assume P_i is a clique
  of order r-d_i with d_i>=1. Let B be the two-supported vertices,
  with b=|B|<=r and sum_i d_i=b-1, and let B_ij have anchor support
  {q_i,q_j}. Assume |B_ij|<=d_i+d_j-1 and e(H[U])<=D_r(|U|) for
  every U. Assume no induced subgraph H' has order kr+1, independence
  number k, an independent k-element anchor set relative to which
  every nonanchor has one or two anchor neighbors, and at most r
  two-supported vertices, for any integer 1<=k<a. Then every r-element
  set T with h=binom(r,2)-e(H[T])<=a-2 satisfies r<=a(h+1).
  In particular K_r minus one edge is impossible when r>2a.
  If also r<=4a-4, every r-element set has at least ceil(r/a)-1
  missing edges. Any r-element set with h<=a-2 has at most one anchor.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T17:09:48Z
updated: 2026-10-15T17:09:48Z
---

# Near-clique density in a minimum-anchor core

[[theory/combinatorics/_index|..]]

[[theory/combinatorics/L238_normalized_core_near_clique_bound/_proof|_proof]]: Hereditary caps bound outsider degrees; anchor incidence and a safe induced deletion force the near-clique inequality.

***

The [proof](_proof.md) is author-recorded Plasma AI work. Its hypotheses
are explicit; no independent review or Lean proof is attached.
The [bounded-exception normalization](../../../research/erdos_617/two_support_normalization.md)
supplies these hypotheses in the corresponding route to
[[problems/extremal_graph_theory/E0617/_index|Problem 617]], including its
pair capacity. The claim does not prove that reduction or assert a
least-color edge budget. It consumes no other native L-claim.

The [parallel unit-row fold](../../../research/erdos_617/parallel_unit_row_fold/_index.md)
uses the bound to exclude a possible first-cap obstruction when $r>2a$.
The remaining range $r\le2a$, other violating sets and preservation of all
folded caps remain open. This is not a resolution of Problem 617.

**Verification.** Read the proof's outsider bound, anchor incidence count
and induced-deletion argument against the stated minimality class. These
are noncomputational deductions. The separate local finite fold example
does not satisfy this claim's hypotheses and is not its evidence.
No gap remains in the recorded proposition at author standing.
