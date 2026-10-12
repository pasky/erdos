---
name: graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/corollary_1_2
title: "Corollary 1.2: graphs with a fixed forbidden subgraph F and large maximum degree Delta have correspondence chromatic number O_F(Delta/log Delta)"
desc: |
  The forbidden-subgraph form of the main claim, whose ordinary-coloring case
  is Conjecture 3.1 of Alon, Krivelevich and Sudakov (1999); deduced from
  Theorem 1.1 in three lines. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

The correspondence chromatic number $\chi_{\mathrm{DP}}$ is defined on
[[graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/theorem_1_1|the Theorem 1.1 page]];
it bounds the list and ordinary chromatic numbers from above. For a fixed
finite graph $F$, a graph $G$ is $F$-free if it has no subgraph isomorphic to
$F$; the subgraph need not be induced (p. 2).

**Corollary 1.2.** For every finite graph $F$ there are constants $C_F>0$
and $\Delta_F\ge3$ such that every $F$-free graph $G$ of maximum degree
$\Delta\ge\Delta_F$ satisfies

$$
\chi_{\mathrm{DP}}(G)\le\Bigl\lceil C_F\frac{\Delta}{\log\Delta}\Bigr\rceil,
$$

with the natural logarithm. The constants are those of Theorem 1.1 at
$r=\max\{4,|V(F)|\}$ and are not made explicit.

The manuscript identifies the ordinary-coloring version with Conjecture 3.1
of Alon, Krivelevich and Sudakov (J. Combin. Theory Ser. B 77 (1999)) and
says the corollary proves that conjecture "in the stronger
correspondence-coloring form" (p. 2). It adds that when $F$ contains a cycle
the order $\Delta/\log\Delta$ cannot be improved in general, since graphs of
girth greater than $|V(F)|$ and maximum degree at most $\Delta$ can have
chromatic number of that order, citing Bollobás (1978) and the proof of
Proposition 1.2 of Alon, Krivelevich and Sudakov.

**Source.** OpenAI, *Correspondence coloring graphs with a forbidden clique*,
release folder
`preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026`;
TeX file `build/sections/introduction.tex`, label `cor:forbidden` (lines
44--52), PDF p. 2; the proof follows at lines 53--56 (PDF p. 2), and the
remarks on the conjecture and on sharpness at lines 58--65. Read 2026-10-12.
Provenance and attestations are on
[[graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/_index|the card]].

**Read depth.** Claims checked: the statement and the definition of
$F$-freeness (lines 41--42) were read clause by clause in the TeX source, and
the three-line proof was followed; it rests entirely on Theorem 1.1, whose
proof was read for structure only. The cited conjecture and sharpness
results were not read. Nothing here is independently reviewed.

## Proof pointer

Put $r=\max\{4,|V(F)|\}$. Since $F$ has at most $r$ vertices, $K_r$ contains
$F$ as a subgraph, so an $F$-free graph is $K_r$-free, and
[[graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/theorem_1_1|Theorem 1.1]]
at this $r$ gives the bound with $C_F=C_r$ and $\Delta_F=\Delta_r$.

## Bears on

No problem page is identified for the corollary beyond Theorem 1.1's: with
$F=K_4$ it is Theorem 1.1 at $r=4$, whose row for Problem 620 is on
[[graph_coloring/openai_2026_correspondence_coloring_graphs_forbidden_clique/theorem_1_1|its page]].
