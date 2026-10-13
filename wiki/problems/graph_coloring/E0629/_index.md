---
name: problems/graph_coloring/E0629
title: Problem 629
desc: |
  Asks for the least number of vertices $n(k)$ of a bipartite graph whose list
  chromatic number exceeds $k$; open, with $n(2)=6$ and $n(3)=14$ known.
tags:
- Graph theory
- Chromatic number
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-07T14:38:26Z
---

# Problem 629

[[problems/graph_coloring/_index|..]]

[[problems/graph_coloring/E0629/claims/_index|claims/]]: The 2 claim pages of Problem 629, one per claimant's result; the problem's standing derives from them.

***

**Statement.** The list chromatic number $\chi_L(G)$ is defined to be the
minimal $k$ such that for any assignment of a list of $k$ colours to each vertex
of $G$ (perhaps different lists for different vertices) a colouring of each
vertex by a colour on its list can be chosen such that adjacent vertices receive
distinct colours.

Determine the minimal number of vertices $n(k)$ of a bipartite graph $G$ such
that $\chi_L(G)>k$.

**Status.** Open. The site labeled the problem OPEN (page last edited 28
October 2025), with the note that it cannot be resolved with a finite
computation.

**Source.** [erdosproblems.com/629](https://www.erdosproblems.com/629), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #629,
https://www.erdosproblems.com/629.

**References.**

- [ERT80] Erdős, Paul and Rubin, Arthur L. and Taylor, Herbert, Choosability in
  graphs. Congr. Numer. XXVI (1980), 125-157.
- [HMT96] Hanson, Denis and MacGillivray, Gary and Toft, Bjarne, [[../library/graph_coloring/hanson_1996_choosability_bipartite_graphs/_index|Choosability
  of bipartite graphs]]. Ars Combin. 44 (1996), 183-192.
- [RaSr00] Radhakrishnan, Jaikumar and Srinivasan, Aravind, Improved bounds and
  algorithms for hypergraph $2$-coloring. Random Structures Algorithms (2000),
  4-32.

**Formalization.** None recorded.

## Current assessment

**The question.** The statement asks for the exact value of $n(k)$ for every
$k$. Exact values are known only for $k\le3$, and the two partial claim pages
record the instances $k=2$ and $k=3$, so the derived standing is open.

**Small values.** $n(1)=2$ is the single edge. $n(2)=6$ is stated by Erdős,
Rubin and Taylor
([[problems/graph_coloring/E0629/claims/1980_01_01_erdos_rubin_taylor|claim page]],
claimed, since its conference proceedings have no record of refereeing).
$n(3)=14$ is Hanson, MacGillivray and Toft's
([[problems/graph_coloring/E0629/claims/1996_01_01_hanson_macgillivray_toft|claim page]],
accepted on the refereed paper), which closes Erdős, Rubin and Taylor's range
$12\le n(3)\le14$.

**The case $k=4$.** $23\le n(4)\le40$. Write $m(k)$ for the least number of
edges of a $k$-uniform hypergraph without property B, the subject of
[[problems/set_systems/E0901/_index|Problem 901]]. The lower bound combines
Erdős, Rubin and Taylor's inequality $m(k)\le n(k)$
([[../library/graph_coloring/erdos_1980_choosability_graphs/theorem_p129|Theorem, p. 129]],
whose short argument the result page follows, and which Hanson, MacGillivray
and Toft recall on pp. 183--184) with Östergård's $m(4)=23$, accepted on
[[problems/set_systems/E0901/claims/2014_01_01_ostergard|Problem 901's claim page]].
The upper bound is Corollary 3.1 of Hanson, MacGillivray and Toft
([[../library/graph_coloring/hanson_1996_choosability_bipartite_graphs/_index|source card]]),
their recursion $n(k)\le k\,n(k-2)+2^k$ (Theorem 3) applied to $n(2)=6$;
Erdős, Rubin and Taylor's $n(k)\le2m(k)$ gives only $46$. A footnote of
Erdős, Rubin and Taylor (p. 129) asserts $m(k)+1<n(k)$ for $k>1$, which would
give $n(4)\ge25$, but the paper states it without proof, so $25$ is not
recorded here as a bound.

**General bounds.** Erdős, Rubin and Taylor print
$2^{k-1}<m(k)\le n(k)\le2m(k)<k^22^{k+2}$ (in their notation $M_k$ and
$N(2,k)$). The site's remark writes the upper bound as $n(k)\le m(k+1)$,
while the paper prints $2M_k$. With Radhakrishnan and Srinivasan's lower bound
for $m(k)$, accepted on
[[problems/set_systems/E0901/claims/2000_01_01_radhakrishnan_srinivasan|Problem 901's claim page]],
this gives $n(k)\gg2^k\sqrt{k/\log k}$, as the site states. No bound
determines $n(k)$ for any $k\ge4$.

**Search scope.** The site's problem page, its four-comment discussion thread
(one comment, of 22 June 2026, reports computational work on $n(4)$ without a
new bound) and its empty proof-claim tab; the held sources [ERT80], [HMT96]
and [RaSr00]; and the claim pages of Problem 901. Not searched: the literature
beyond these sources, arXiv, MathSciNet, zbMATH, Google Scholar, X. Proofs are
compiled at statement level: those of Hanson, MacGillivray and Toft were not
checked, and Erdős, Rubin and Taylor state their values and footnote without
proof.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/graph_coloring/erdos_1980_choosability_graphs/_index|erdos_1980_choosability_graphs]]
- [[../library/graph_coloring/erdos_1980_choosability_graphs/theorem_p129|erdos_1980_choosability_graphs / theorem_p129]]
- [[../library/graph_coloring/erdos_1980_choosability_graphs/theorem_p132|erdos_1980_choosability_graphs / theorem_p132]]
- [[../library/graph_coloring/hanson_1996_choosability_bipartite_graphs/_index|hanson_1996_choosability_bipartite_graphs]]
- [[../library/graph_coloring/radhakrishnan_2000_improved_bounds_algorithms_hypergraph_coloring/_index|radhakrishnan_2000_improved_bounds_algorithms_hypergraph_coloring]]
- [[../library/graph_coloring/radhakrishnan_2000_improved_bounds_algorithms_hypergraph_coloring/theorem_2_1|radhakrishnan_2000_improved_bounds_algorithms_hypergraph_coloring / theorem_2_1]]

<!-- END problem library links -->
