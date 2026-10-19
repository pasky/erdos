---
name: research/graph_ramsey_interfaces/finite_reduction_obstructions
title: When an asymptotic graph theorem leaves a finite task
desc: Exact rounding and amplification distinguish an unquantified finite tree-embedding remainder from parameter-dependent embedding and path-partition obstacles.
created: 2026-10-14T22:20:00Z
updated: 2026-10-14T22:20:00Z
---

# When an asymptotic graph theorem leaves a finite task

[[research/graph_ramsey_interfaces/_index|..]]

***

A theorem that holds for every host order above a fixed threshold leaves a
finite remainder. A theorem with an additional unbounded parameter need not.
The following interfaces concern
[[problems/extremal_graph_theory/E0580/_index|Problem 580]],
[[problems/extremal_graph_theory/E0583/_index|Problem 583]],
[[problems/extremal_graph_theory/E0065/_index|Problem 65]],
[[problems/extremal_graph_theory/E0743/_index|Problem 743]] and
[[problems/extremal_graph_theory/E1035/_index|Problem 1035]].
The deductions and reconstruction are author-recorded by Plasma AI; no
independent examination is recorded. The source theorems enter at the
statement depth specified below.

## Loebl's hypothesis and the finite remainder

[[../library/extremal_graph_theory/zhao_2011_proof_n_2_n_2_n_2_conjecture_large_n/theorem_1_6|Zhao's Theorem 1.6]]
states that for some $n_0$ and every $n\ge n_0$, a graph with at least
$\lceil n/2\rceil$ vertices of degree at least $\lceil n/2\rceil$ contains
every tree with at most $\lfloor n/2\rfloor$ edges. Its statement in the
held transcription, p. 2, was inspected; the proof in Sections 3--7 and
the appendix was not checked here.

Problem 580 asks only for trees with at most $\lfloor n/2\rfloor$
vertices. Such a nonempty tree has at most $\lfloor n/2\rfloor-1$ edges.
The integer-valued count and degree conditions in the problem are exactly
the rounded hypotheses of the theorem. Therefore the theorem applies,
and only orders $n<n_0$ remain. This is an existence-level finite
reduction. No numerical value of $n_0$ or effective extraction of one is
supplied here; the retained finite verification claim through $n=19$ is
unreviewed and was not replayed.

The vertex formulation also admits an exact odd-to-even reduction. For
$n=2m+1$, there are at least $m+1$ vertices of degree at least $m+1$.
Delete one such vertex. At least $m$ of the remaining $2m$ vertices then
have degree at least $m$. If the statement holds for order $2m$, the
remaining graph contains every tree on at most $m$ vertices, precisely
what order $2m+1$ asks for. Thus verifying the even orders suffices. This
does not turn an unstated $n_0$ into an executable census, and it does not
supply the extra vertex asked for by the edge formulation.

## Gallai's partition problem cannot lose a linear error

Let $p(H)$ denote the fewest simple paths in a partition of the edges of a
connected graph $H$ on $m$ vertices. Suppose that
$p(H)\ge\lceil m/2\rceil+1$, so $H$ is a counterexample to Problem 583.
Take $k$ disjoint copies of $H$, add one vertex $z$, and join $z$ by
exactly one edge to a chosen vertex of each copy. The resulting connected
graph $G_k$ has $km+1$ vertices and satisfies

$$
p(G_k)\ge k p(H)-\lfloor k/2\rfloor. \tag{1}
$$

Indeed, restrict a path partition of $G_k$ to the edges inside each copy.
Every nonempty restriction is a simple path. A global path meets edges in
at most two copies, since it can pass through $z$ at most once. A path
meeting two copies uses two distinct edges at $z$; edge-disjointness
therefore permits at most $\lfloor k/2\rfloor$ such paths. If the global
partition has $P$ members, the total number of nonempty restricted pieces
is at most $P+\lfloor k/2\rfloor$, whereas it is at least $kp(H)$.
This proves (1).

Consequently

$$
\liminf_{k\to\infty}\frac{p(G_k)}{km+1}
\ge\frac{p(H)-1/2}{m}>\frac12.
$$

Thus a bound $p(G)\le |V(G)|/2+o(|V(G)|)$ uniform over all connected
graphs would already imply the exact conjecture. This reconstructs the
hub example in
[[../library/extremal_graph_theory/pyber_1996_covering_edges_connected_graph_paths/theorem_i|Pyber's discussion after Theorem II]],
printed p. 153; that example and its counting argument were read. Pyber's
actual asymptotic theorem concerns covers whose paths may share edges.
For covers, the bound on the number of uses of edges at $z$ fails, so that
theorem cannot be substituted into the partition conclusion.

## Parameter dependence prevents a global census

The recorded degree-bounded packing theorem for Problem 743 has the form
$\forall\Delta\,\exists N(\Delta)\,\forall n\ge N(\Delta)$, and constrains
the degrees of the larger trees. It leaves out families with growing
maximum degree, at arbitrarily large host orders. Packing the smallest
fixed fraction and packing the largest fixed fraction into separate
copies of $K_n$ does not show their packings are edge-disjoint in one
host. Their total edge demand is exact, so this compatibility is essential.

Similarly, the separate fixed-parameter results recorded for Problem 65
do not bound the first unresolved order uniformly over its unbounded
parameter. For Problem 1035, a theorem about embedding a fixed $Q_d$ as
host order tends to infinity has different quantifiers from embedding
$Q_n$ spanning a host on $2^n$ vertices: there $d=n$ grows with the host,
and a permitted threshold depending on $d$ can exceed $2^d$.

The next useful test in each case is a quantitative statement that covers
all the varying parameters of the target. Without it, additional small
examples are not a finite reduction. These are failures of the stated
implications, not counterexamples to any of the three conjectures.
