---
name: problems/graph_coloring/E0919
title: Problem 919
desc: |
  Asks whether some graph on the ordinal $\omega_2^2$ has chromatic number
  $\aleph_2$ while every subgraph of smaller type is countably colorable, and
  asks the same with chromatic number $\aleph_1$.
tags:
- Graph theory
- Chromatic number
status: open
claim: none
parts:
- q1
- q2
created: 2026-09-04T09:17:27Z
updated: 2026-10-13T13:29:21Z
---

# Problem 919

[[problems/graph_coloring/_index|..]]

[[problems/graph_coloring/E0919/claims/_index|claims/]]: The 1 claim page of Problem 919, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Is there a graph $G$ with vertex set $\omega_2^2$ and chromatic
number $\aleph_2$ such that every subgraph whose vertices have a lesser type has
chromatic number $\leq \aleph_0$?

What if instead we ask for $G$ to have chromatic number $\aleph_1$?

**Status.** Open. The site labeled the problem OPEN, with the note that it
cannot be resolved with a finite computation. The first question (the part
`q1`) is not provable relative to a huge cardinal, by Foreman and Laver 1988;
its positive side is open. The second question (the part `q2`) is open.

**Source.** [erdosproblems.com/919](https://www.erdosproblems.com/919), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #919,
https://www.erdosproblems.com/919.

**References.**

- [Er69b] Erdős, P., Problems and results in chromatic graph theory. Proof
  Techniques in Graph Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann
  Arbor, Mich., 1968) (1969), 27-35.

**Formalization.** None recorded.

## Current assessment

**Question.** Both questions ask for a graph on the ordinal $\omega_2^2$ whose
subgraphs on vertex sets of smaller order type are all countably chromatic,
with chromatic number $\aleph_2$ (the part `q1`) or $\aleph_1$ (the part
`q2`). Erdős [Er69b] (printed p. 29, recorded on the
[[../library/graph_coloring/erdos_1969_problems_results_chromatic_graph_theory/_index|source card]])
says that he and Hajnal cannot decide either question, while the version with
chromatic number $\aleph_2$ and subgraphs of chromatic number at most
$\aleph_1$ is easy. The site's commentary describes the Erdős--Hajnal graph
on $\omega_1^2$ with chromatic number $\aleph_1$ whose smaller subgraphs are
countably chromatic.

**First question.** A positive answer to it is a positive answer to the first
question of [[problems/graph_coloring/E0918/_index|Problem 918]]. A graph of
the kind asked for has $\aleph_2$ vertices and chromatic number $\aleph_2$,
and a set of $\aleph_1$ of its vertices has an order type of cardinality
$\aleph_1$, below $\omega_2$ and so below $\omega_2^2$, so the subgraph on
it is countably chromatic. In the model of Foreman and Laver, built from a
huge cardinal with GCH, every graph of size and chromatic number $\aleph_2$
has a subgraph of size and chromatic number $\aleph_1$, so no such graph
exists there, and relative to a huge cardinal ZFC + GCH does not prove that
one exists
([[problems/graph_coloring/E0919/claims/1988_02_01_foreman_laver|claim page]],
accepted on the refereed paper). The positive side is open. The models that
answer Problem 918's first question positively, Baumgartner's among them, do
not transfer: they make countably chromatic only the subgraphs on $\aleph_1$
vertices, while a vertex set of smaller type than $\omega_2^2$, such as
$\omega_2\cdot\alpha$ for $1\le\alpha<\omega_2$, can have $\aleph_2$
elements.

**Second question.** No result on it is recorded here. A graph with chromatic
number $\aleph_1$ answers neither question of Problem 918, so the models
recorded there do not bear on it.

**Standing.** The problem lists its two questions as the parts `q1` and `q2`,
and its standing derives from the claim pages. Foreman and Laver's page
settles only the not provable side of `q1`, and one side alone leaves that
question open; `q2` has no claim page. So the problem is open, and the site
labeled it OPEN.

**Search scope.** The site's problem page, discussion thread and proof-claim
tab as accessed 2026-09-05 (no comments, no proof claims); the held sources
[Er69b] and Shelah's 2012 paper on incompactness of the chromatic number
([[../library/graph_coloring/shelah_2012_incompactness_chromatic_number_graphs/_index|source card]]),
which does not treat order types and answers neither question; and the claim
pages of Problem 918. Not searched: the literature beyond these sources,
arXiv, MathSciNet, zbMATH, Google Scholar, X.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/graph_coloring/erdos_1969_problems_results_chromatic_graph_theory/_index|erdos_1969_problems_results_chromatic_graph_theory]]
- [[../library/graph_coloring/shelah_2012_incompactness_chromatic_number_graphs/_index|shelah_2012_incompactness_chromatic_number_graphs]]
- [[../library/graph_coloring/shelah_2012_incompactness_chromatic_number_graphs/claim_1_1|shelah_2012_incompactness_chromatic_number_graphs / claim_1_1]]
- [[../library/graph_coloring/shelah_2012_incompactness_chromatic_number_graphs/claim_1_2|shelah_2012_incompactness_chromatic_number_graphs / claim_1_2]]
- [[../library/graph_coloring/shelah_2012_incompactness_chromatic_number_graphs/claim_2_2|shelah_2012_incompactness_chromatic_number_graphs / claim_2_2]]
- [[../library/graph_coloring/shelah_2012_incompactness_chromatic_number_graphs/conclusion_2_4|shelah_2012_incompactness_chromatic_number_graphs / conclusion_2_4]]

<!-- END problem library links -->
