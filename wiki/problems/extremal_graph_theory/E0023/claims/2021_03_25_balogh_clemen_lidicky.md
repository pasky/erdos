---
name: problems/extremal_graph_theory/E0023/claims/2021_03_25_balogh_clemen_lidicky
title: Balogh, Clemen and Lidický's bound in two density ranges
desc: |
  Theorem 2(b),(c) of Balogh, Clemen and Lidický: for every sufficiently large
  $n$, a triangle-free graph on $5n$ vertices with at least
  $0.3197\binom{5n}{2}$ or at most $0.2486\binom{5n}{2}$ edges can be made
  bipartite by deleting at most $n^2$ edges. The proof is a sketch in an
  extended abstract, not refereed.
authors:
- József Balogh
- Felix Christian Clemen
- Bernard Lidický
status: claimed
claim: proved
scope: partial
published: 2021-03-25
submitted: null
links:
- url: https://arxiv.org/abs/2103.14179v1
  kind: preprint
  date: 2021-03-25
- url: https://doi.org/10.1007/978-3-030-83823-2_82
  kind: paper
  date: 2021-08-24
created: 2026-10-18T03:08:34Z
updated: 2026-10-18T03:50:39Z
---

***

**Claim.** József Balogh, Felix Christian Clemen and Bernard Lidický, *Max
Cuts in Triangle-free Graphs*, arXiv:2103.14179v1, submitted 25 March 2021
(the claim's date), prove as Theorem 2(b),(c), p. 2, that there is an $N_0$
such that every triangle-free graph $G$ on $N\ge N_0$ vertices satisfies
$D_2(G)\le N^2/25$ when $|E(G)|\ge0.3197\binom{N}{2}$ or
$|E(G)|\le0.2486\binom{N}{2}$. Here $D_2(G)$ is the fewest edges whose
deletion makes $G$ bipartite; the paper writes $n$ for the order and gives no
value of $N_0$. With $N=5n$ this answers the question of
[[problems/extremal_graph_theory/E0023/_index|Problem 23]] yes, at most $n^2$
deletions, for every sufficiently large $n$ and every triangle-free graph on
$5n$ vertices with at least $0.3197\binom{5n}{2}$ or at most
$0.2486\binom{5n}{2}$ edges. The statement and this specialization are
recorded on the
[[../library/extremal_graph_theory/balogh_2021_max_cuts_triangle_free_graphs/theorem_2|Theorem 2 page]]
of the
[[../library/extremal_graph_theory/balogh_2021_max_cuts_triangle_free_graphs/_index|source card]].
The same six-page extended abstract appeared in *Extended Abstracts EuroComb
2021* (Trends in Mathematics 14, Birkhäuser), pp. 509--514, online 24 August
2021.

**Covers.** The question of Problem 23 for the triangle-free graphs on $5n$
vertices with at least $0.3197\binom{5n}{2}$ or at most $0.2486\binom{5n}{2}$
edges, for every $n$ above an unspecified threshold. The thresholds are
fractions of $\binom{5n}{2}$, not of $(5n)^2$. Not covered: the graphs whose
edge count lies strictly between the two thresholds, at every order, and
every order below the threshold, so neither a proof for all $n$ nor a
counterexample follows. The balanced blow-up of $C_5$ (five independent sets
of $n$ vertices, complete bipartite graphs between cyclically consecutive
sets) has $5n^2$ edges, in the dense range, and needs at least $n^2$
deletions (p. 1), so the bound cannot be lowered there. The theorem's clause
(a), $D_2(G)\le N^2/23.5$ for every triangle-free graph on $N\ge N_0$
vertices, is $(50/47)n^2$ on $5n$ vertices; it answers the question for no
graph, since $50/47>1$, and the problem page records it among the known
results.

**Relation to other claims.**
[[problems/extremal_graph_theory/E0023/claims/2026_06_26_ferudun|Ferudun's pending claim]]
uses clauses (b) and (c) for its two density tails: its Corollary 4.2 states
them at every order, and its Theorem 1.1 uses them up to order $200$, adding a
middle-band certificate of its own to assert the bound $n^2$ at every density
for $1\le n\le40$.
[[problems/extremal_graph_theory/E0023/claims/2026_10_19_plasma_ai|Plasma AI's pending claim]]
carries clauses (b) and (c) to every order by the blow-up identity
$D_2(G[t])=t^2D_2(G)$, with the densities measured as $2e(G)/N^2$ rather than
as fractions of $\binom{N}{2}$, and clause (a) as $D_2(G)\le2N^2/47$. Neither
page is a premise of this one.

**Depends on.** No page of this wiki; the result is the paper's own theorem,
recorded on
[[../library/extremal_graph_theory/balogh_2021_max_cuts_triangle_free_graphs/theorem_2|the Theorem 2 page]].

**Standing.** Claimed, not accepted. The result's only publication is the
six-page extended abstract: arXiv:2103.14179v1, the only version, which
carries no journal reference, and the EuroComb 2021 chapter, DOI
10.1007/978-3-030-83823-2_82. The volume's preface says its program committee
selected 135 of the 177 submitted contributions for presentation; it
describes no refereeing, and an extended abstract in a proceedings volume is
not refereed evidence. The abstract itself gives only a proof sketch. Its
flag-algebra argument, Section 2.1, pp. 3--4, rests on a semidefinite program
solved by computer, whose certificate the abstract does not supply. Section
2.2, pp. 4--5, treats densities slightly below $2/5$ through cited structural
theorems of Erdős, Győri and Simonovits and of Häggkvist, and omits its
detailed computations. No journal version or later full proof was found in a
search on 2026-10-18; the authors' 2022 paper *10 Problems for Partitions of
Triangle-free Graphs* (arXiv:2203.15764) still cites the EuroComb abstract
for this work. The erdosproblems.com commentary (read 2026-10-18) credits
[BCL21] only with the general bound of at most $1.064n^2$ deletions, clause
(a), on a problem Bloom's catalog labeled FALSIFIABLE; that is commentary on
an open problem, not reviewed evidence. The source card's reading checked the
statement against the PDF and read the sketch for structure; no
reconstruction, certificate replay or independent review is recorded here. A
refereed full proof, or an independent reviewer's acceptance of a
reconstructed proof, would move the claim to accepted. The claim is partial,
so the problem's standing is unchanged by it.
