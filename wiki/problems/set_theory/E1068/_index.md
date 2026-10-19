---
name: problems/set_theory/E1068
title: Problem 1068
desc: |
  Asks whether every graph of chromatic number $\aleph_1$ contains a countable
  subgraph that is infinitely vertex-connected.
tags:
- Graph theory
- Set theory
- Chromatic number
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1068

[[problems/set_theory/_index|..]]

***

**Statement.** Does every graph with chromatic number $\aleph_1$ contain a
countable subgraph which is infinitely vertex-connected?

**Formulation.** Under the erdosproblems.com definition of infinite connectivity
(any two vertices joined by infinitely many pairwise vertex-disjoint paths), a
subgraph with a single vertex qualifies vacuously, which would make the question
trivial. The question is read as its sources read it, as asking for a countably
infinite, infinitely connected subgraph. Bowler and Pitz pose it so in Remark
(3) of their note [BoPi24], for every uncountably chromatic graph. The
[formal-conjectures statement](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/1068.lean)
requires at least two vertices in its definition of infinite connectivity, and
two vertices joined by infinitely many disjoint paths need infinitely many
vertices, so the formal statement is not trivial. The open status concerns that
reading.

**Status.** Open.

**Source.** [erdosproblems.com/1068](https://www.erdosproblems.com/1068),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1068,
https://www.erdosproblems.com/1068.

**References.**

- [BoPi24] N. Bowler and M. Pitz, A note on uncountably chromatic graphs.
  arXiv:2402.05984 (2024).
- [ErHa66] Erdős, P. and Hajnal, A., On chromatic number of graphs and
  set-systems. Acta Math. Acad. Sci. Hungar. (1966), 61-99.
- [So15] Soukup, Dániel T., Trees, ladders and graphs. J. Combin. Theory Ser. B
  (2015), 96-116.
- [Va99] Various, Some of Paul's favorite problems. Booklet produced for the
  conference "Paul Erdős and his mathematics", Budapest, July 1999 (1999).

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1068.lean).

## Current assessment

The countably infinite formulation remains open in the held accounts. The
[[../library/set_theory/bowler_2024_note_uncountably_chromatic_graphs/remark_3|Bowler–Pitz question]]
asks exactly for that size. Their obstruction concerns uncountable infinitely
connected subgraphs; it does not supply a negative answer here. The following
author-recorded check of their explicit construction makes the distinction
concrete. This is a scoped source-fit check, not a current literature survey or
an independent review of the whole paper.

## A countable clique in the Bowler–Pitz graph

Use the tree and edge definition in Section 2 of
[[../library/set_theory/bowler_2024_note_uncountably_chromatic_graphs/_index|Bowler and Pitz's note]].
A vertex is an injective sequence of countable ordinal length in the positive
integers, with infinite complement. For a successor-length sequence $s$, write
$s^\star$ for its predecessor and $\operatorname{last}(s)$ for its last value.
An edge joins $t$ to $s^\star$ when $s\le t$ and
$\operatorname{last}(s)=\min(\operatorname{im}(t)\setminus
\operatorname{im}(s^\star))$.

For $n\ge0$, let $t_n=(2,4,\ldots,2n)$, including the empty sequence.
Each $t_n$ is a vertex. If $m<n$, choose $s=t_{m+1}$. Then $s\le t_n$,
$s^\star=t_m$, and the required minimum is $2m+2$, exactly the last
value of $s$. Thus every two distinct $t_n$ are adjacent. Their induced
$K_\omega$ is infinitely vertex-connected: any two vertices have infinitely
many internally disjoint two-edge paths through the other clique vertices.
This particular graph therefore has the subgraph sought in the question.

Conversely, obtaining an $n$-connected subgraph separately for every finite
$n$ does not by itself give an infinite one. The disjoint union of finite
cliques of unbounded orders has the former property and no infinite connected
subgraph. Its chromatic number is only $\aleph_0$, so it is an obstruction
to that quantifier exchange, not a counterexample to this problem. A route
using finite connectivity still needs compatible subgraphs or another
argument producing a single infinite object.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/set_theory/bowler_2024_note_uncountably_chromatic_graphs/_index|bowler_2024_note_uncountably_chromatic_graphs]]
- [[../library/set_theory/bowler_2024_note_uncountably_chromatic_graphs/remark_3|bowler_2024_note_uncountably_chromatic_graphs / remark_3]]
- [[../library/set_theory/bowler_2024_note_uncountably_chromatic_graphs/theorem_p1|bowler_2024_note_uncountably_chromatic_graphs / theorem_p1]]
- [[../library/set_theory/erdos_1966_chromatic_number_graphs_set_systems/_index|erdos_1966_chromatic_number_graphs_set_systems]]
- [[../library/set_theory/erdos_1966_chromatic_number_graphs_set_systems/assertion_p77|erdos_1966_chromatic_number_graphs_set_systems / assertion_p77]]
- [[../library/set_theory/soukup_2015_open_problems_around_uncountable_graphs/_index|soukup_2015_open_problems_around_uncountable_graphs]]
- [[../library/set_theory/soukup_2015_open_problems_around_uncountable_graphs/conjecture_1_1|soukup_2015_open_problems_around_uncountable_graphs / conjecture_1_1]]
- [[../library/set_theory/soukup_2015_trees_ladders_graphs/_index|soukup_2015_trees_ladders_graphs]]
- [[../library/set_theory/soukup_2015_trees_ladders_graphs/problem_6_4|soukup_2015_trees_ladders_graphs / problem_6_4]]
- [[../library/set_theory/soukup_2015_trees_ladders_graphs/theorem_3_5|soukup_2015_trees_ladders_graphs / theorem_3_5]]

<!-- END problem library links -->
