---
name: problems/graph_coloring/E1091
title: Problem 1091
desc: |
  Asks whether every $K_4$-free graph with chromatic number $4$ contains an odd
  cycle with at least two diagonals. Erdős first asked for one diagonal, which
  Larson proved in 1979.
tags:
- Graph theory
- Chromatic number
parts:
- two_diagonals
- unbounded_diagonals
status: solved
claim: answered
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T17:47:46Z
---

# Problem 1091

[[problems/graph_coloring/_index|..]]

[[problems/graph_coloring/E1091/claims/_index|claims/]]: The 2 claim pages of Problem 1091, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $G$ be a $K_4$-free graph with chromatic number $4$. Must $G$
contain an odd cycle with at least two diagonals?

More generally, is there some $f(r)\to \infty$ such that every graph with
chromatic number $4$, in which every subgraph on $\leq r$ vertices has chromatic
number $\leq 3$, contains an odd cycle with at least $f(r)$ diagonals?

**Formulation.** Erdős first asked for one diagonal: must every $K_4$-free graph
of chromatic number $4$ contain an odd cycle with a diagonal? The
erdosproblems.com commentary records that question as his original one, without
a source (the erdosproblems.com source key for the problem is [Er76c], a text
not read here), and credits Larson [La79] with the answer yes, through a proof
of the stronger conjecture of Bollobás and Erdős that a $K_4$-free graph with no
odd cycle carrying a diagonal is bipartite, has a cut vertex, or has a vertex of
degree at most $2$; a $4$-critical subgraph of the graph is $2$-connected with
minimum degree at least $3$, so it has such a cycle. erdosproblems.com states
the problem with at least two diagonals, together with the more general question
about $f(r)$ diagonals, and that Statement sets the standing; the pentagonal
wheel shows that three diagonals are not forced.

**Status.** Bloom's catalog labeled the problem solved, with the two questions
answered in opposite directions. The first question asks whether a $K_4$-free
graph of chromatic number $4$ has an odd cycle with at least two diagonals. The
accepted partial claim
[[problems/graph_coloring/E1091/claims/1982_06_01_voss|Voss's two-chord theorem]]
answers it yes. The second asks whether local $3$-colorability forces some
$f(r)\to\infty$ diagonals. The accepted partial claim
[[problems/graph_coloring/E1091/claims/2026_04_08_alexeev_putterman_sawhney_sellke_valiant|the ten-chord construction of Alexeev, Putterman, Sawhney, Sellke and Valiant]]
answers it no. Together the two claims settle both parts of the problem, one yes
and one no. So the problem is solved with the mixed value answered.

**Source.** [erdosproblems.com/1091](https://www.erdosproblems.com/1091),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1091,
https://www.erdosproblems.com/1091.

**References.**

- [APSSV26b] B. Alexeev, M. Putterman, M. Sawhney, M. Sellke, and G. Valiant,
  Short proofs in combinatorics, probability, and number theory II.
  arXiv:2604.06609 (2026).
- [La79] Larson, Jean A., Some graphs with chromatic number three. J. Combin.
  Theory Ser. B (1979), 317-322.
- [Vo82] Voss, Heinz-Jürgen, Graphs having circuits with at least two chords. J.
  Combin. Theory Ser. B (1982), 264-285.

**Formalization.** erdosproblems.com records no formal-conjectures statement,
and the formal-conjectures catalog had no statement file for the problem on
2026-10-07. Boris Alexeev's lean-proofs collection holds a Lean file for it,
authored by OpenAI Codex, whose docstring credits the two results it proves to
Voss and to Alexeev, Putterman, Sawhney, Sellke and Valiant and proves both for
finite graphs; it is linked from both claim pages at its pinned commit, and the
corpus has not built it.

## Current assessment

The erdosproblems.com formulation (accessed 2026-09-04; page last edited 9
April 2026) asks two questions about a graph $G$ of chromatic number $4$:
whether every $K_4$-free such $G$ has an odd cycle with at least two diagonals,
and whether some $f(r)\to\infty$ exists such that every such $G$ whose subgraphs
on at most $r$ vertices are $3$-colorable has an odd cycle with at least $f(r)$
diagonals. The first question is answered yes by Voss's theorem of 1982
[Vo82], refereed in J. Combin. Theory Ser. B and credited by erdosproblems.com
([[problems/graph_coloring/E1091/claims/1982_06_01_voss|claim page]]); the
pentagonal wheel shows that two diagonals cannot be raised to three. Erdős's
original question, one diagonal, settled by Larson [La79], is recorded in the
Formulation. The second question is answered no by Theorem 4.1 of Alexeev,
Putterman, Sawhney, Sellke and Valiant [APSSV26b], a preprint of April 2026
whose proof the paper attributes to an internal OpenAI model: for every
$m\ge1$ an explicit $K_4$-free graph on $20m+31$ vertices with chromatic
number $4$, every proper subgraph $3$-colorable and every cycle carrying at
most ten chords
([[problems/graph_coloring/E1091/claims/2026_04_08_alexeev_putterman_sawhney_sellke_valiant|claim page]]).
The erdosproblems.com label SOLVED credits both results, so each claim page
lists `reviewed`, and the problem's parts, the two questions, are both settled
by accepted partial claims, one yes and one no, which derives the standing
solved with the claim answered. Neither result has been built in Lean by the
corpus; the lean-proofs file linked from both pages is third-party Lean.

Search scope: the erdosproblems.com page and discussion thread (two comments, of
3 and 23 November 2025, which report Voss's paper and link its publisher's
record and claim nothing), the community database (teorth/erdosproblems), the
formal-conjectures catalog and the lean-proofs catalog; on 2026-10-07 none of
them showed another claim on the problem.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/discrete_geometry/alexeev_2026_short_proofs_combinatorics_probability_number_theory/_index|alexeev_2026_short_proofs_combinatorics_probability_number_theory]]
- [[../library/discrete_geometry/alexeev_2026_short_proofs_combinatorics_probability_number_theory/theorem_4_1|alexeev_2026_short_proofs_combinatorics_probability_number_theory / theorem_4_1]]

<!-- END problem library links -->
