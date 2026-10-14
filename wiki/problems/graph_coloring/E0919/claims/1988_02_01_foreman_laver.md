---
name: problems/graph_coloring/E0919/claims/1988_02_01_foreman_laver
title: Foreman and Laver's model with no such graph on omega two squared
desc: |
  Foreman and Laver (Adv. Math., 1988) build from a huge cardinal a model of ZFC
  and GCH in which every graph of size and chromatic number $\aleph_2$ has a
  subgraph of size and chromatic number $\aleph_1$, so no graph answers the
  first question positively there.
authors:
- Matthew Foreman
- Richard Laver
status: accepted
claim: not_provable
scope: partial
settles:
- q1
evidence:
- refereed
submitted: null
links:
- url: https://doi.org/10.1016/0001-8708(88)90041-2
  kind: paper
  date: 1988-02
created: 2026-10-13T13:17:12Z
updated: 2026-10-13T13:17:12Z
---

***

**Claim.** Assuming the consistency of ZFC with a huge cardinal, Foreman and
Laver force a model of ZFC + GCH in which every graph of size $\aleph_2$ and
chromatic number $\aleph_2$ has an induced subgraph of size $\aleph_1$ and
chromatic number $\aleph_1$, as the zbMATH review (Zbl 0659.03033) gives the
theorem. In that model no graph answers the first question of
[[problems/graph_coloring/E0919/_index|Problem 919]] positively. A graph on
the vertex set $\omega_2^2$ with chromatic number $\aleph_2$ has $\aleph_2$
vertices, so in that model it has a subgraph on $\aleph_1$ vertices with
chromatic number $\aleph_1$. The vertex set of that subgraph has an order type
of cardinality $\aleph_1$, which is below $\omega_2$ and so below
$\omega_2^2$; it is a subgraph of lesser type that is not countably chromatic.
So, relative to a huge cardinal, ZFC with GCH does not prove that such a graph
exists: the first question is not provable. The large-cardinal hypothesis is
part of the claim: the consistency is relative to ZFC with a huge cardinal,
not to ZF alone. The paper does not mention this problem; the step from its
theorem is the order-type count above. The same theorem settles the not
provable side of the first question of
[[problems/graph_coloring/E0918/_index|Problem 918]].

**Covers.** The first question of Problem 919 (the part `q1`), on its not
provable side, as a consistency statement relative to a huge cardinal. That
side alone leaves the question open. The models that answer the first
question of Problem 918 positively, Baumgartner's among them, do not answer
this one, because they make countably chromatic only the subgraphs on
$\aleph_1$ vertices, while a vertex set of smaller type than $\omega_2^2$,
such as $\omega_2\cdot\alpha$ for $1\le\alpha<\omega_2$, can have $\aleph_2$
elements. It does not cover the second question.

**Depends on.** No other wiki page; the claim rests on the paper above and on
the step from its theorem stated in the Claim.

**Acceptance.** Refereed: Matthew Foreman and Richard Laver, Some downwards
transfer properties for $\aleph_2$, Adv. in Math. 67 (1988), no. 2, 230--238,
DOI 10.1016/0001-8708(88)90041-2. The issue is dated February 1988 and
carries no day, so this page is dated the first of that month. Bloom's catalog
labeled the problem OPEN, so no curator acceptance is listed. Its proof is not
reviewed in this corpus.
