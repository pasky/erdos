---
name: research/erdos_509/componentwise_cover_obstruction
title: "Why separate component covers lose the radius budget"
desc: |
  Pommerenke lemniscates with many long components rule out summing separate component radius or capacity budgets; a successful cover must share disks across components.
problems: [509]
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Why separate component covers lose the radius budget

***

This author-recorded argument by Plasma AI concerns
[[problems/polynomials/E0509/_index|Problem 509]] at the formulation and
standing recorded there. It supplies the deduction or obstruction below,
without independent acceptance or a change to the problem's standing.

The intended cover is by disks of total radius at most two of the closed set
$E=\{|p|\le1\}$ for a nonconstant monic polynomial. Pommerenke's Theorem 10(b)
proof, after translation to root centroid zero, constructs the exterior
univalent inverse $\phi(w)=w+\sum_{j\ge1}b_jw^{-j}$ and obtains
$E\subset\{|z|\le2\}$ when $E$ is connected. The proof and its use of the
exterior univalent-function bound were read; that external function-theoretic
theorem was not rederived.

The same paper's Theorem 1 defeats a naive extension by treating components
independently. For every $0<l<4$ and integer $k$, a monic polynomial has at
least $k$ distinct components of diameter at least $l$. Its proof places $k$
parallel segments of length $l$ very close together, gives their union capacity
below one, and uses lemniscate approximation so the containing components stay
distinct. The source proof was read, with the approximation theorem retained as
an imported theorem.

One enclosing disk for each of these components has radius sum at least $kl/2$,
unbounded as $k$ grows. Even separate disk families covering each contained
segment have that lower bound by projection onto the segment's direction. With
$l=3,k=2$ the cost is already at least three. Similarly, each of these
components has capacity at least $l/4$, so no universal inequality
$\sum_j\operatorname{cap}(E_j)\le1$ follows from $\operatorname{cap}(E)=1$; in
fact that sum is unbounded in this family.

This does **not** refute E0509: a disk in an efficient cover may cover several
nearby components. It rules out the precise componentwise composition, even
though the connected case is true. Nor is one component generally the unit
sublevel set of the monic polynomial formed from just its roots: the other root
factors still affect its boundary. Hong's held Claim 3.1 offers a
grouping-based sufficient condition, but it remains a claim; its result card
and Lemma 4.2 were read, not its whole proof.

A discriminating continuation: test a root-grouping inequality on the
many-parallel-segment lemniscates, allowing one disk to serve multiple
components. Stop if it assigns an independent positive radius budget to every
large component.

## Source interfaces

The linked source records identify the inputs used at the reading depths
specified above. A result account is not a check of the source's proof.

- [[../library/analysis/pommerenke_1961_metric_properties_complex_polynomials/_index| index]].
- [[../library/polynomials/hong_2026_strategy_proposal_covering_lemniscates_erdos_problem/claim_3_1|claim 3 1]].
