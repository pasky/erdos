---
name: problems/extremal_graph_theory/E0081/claims
desc: The 5 claim pages of Problem 81, one per claimant's result; the problem's standing derives from them.
tags: []
sources: []
created: 2026-10-07T08:08:44Z
updated: 2026-10-11T22:24:14Z
---

# problems/extremal_graph_theory/E0081/claims

[[problems/extremal_graph_theory/E0081/_index|..]]

[[problems/extremal_graph_theory/E0081/claims/2026_06_17_agbanwa|2026_06_17_agbanwa]]: A Zenodo note by Agbanwa proves $\mathrm{cp}(G)\le(2n-1)^2/24+2$ for every
chordal graph on $n$ vertices with a maximum clique whose edge deletion lowers
the clique number by at most one. This class excludes the extremal split
graphs, and the note is unreviewed.

[[problems/extremal_graph_theory/E0081/claims/2026_08_23_traverso|2026_08_23_traverso]]: Paper III of Traverso's series asserts that every split graph on $n$ vertices
has a clique partition into $n^2/6+O(n)$ cliques, with the sharp coefficient.
It comes with a Lean 4 freeze that the author reports as unconditional, and
covers the split case only.

[[problems/extremal_graph_theory/E0081/claims/2026_09_08_morluto_luo_huang_lee|2026_09_08_morluto_luo_huang_lee]]: A manuscript and Lean 4 development in the N0zoM1z0/erdos-81 repository assert
that for all large $n$ the largest clique partition number of an $n$-vertex
chordal graph is $\lfloor n(n+1)/6\rfloor$, so $n^2/6+O(n)$. The Lean
development assumes three theorems.

[[problems/extremal_graph_theory/E0081/claims/2026_09_15_okechukwu|2026_09_15_okechukwu]]: Okechukwu's arXiv preprint, announced on the thread and unreviewed, determines
the eventual maximum clique partition number of graphs with rooted simplicial
defect $s$. The case $s=0$, the chordal graphs, gives
$\mathrm{cp}(G)\le n^2/6+n/6+O(1)$.

[[problems/extremal_graph_theory/E0081/claims/2026_09_22_traverso|2026_09_22_traverso]]: Paper IV of Traverso's series asserts that every chordal graph on $n$ vertices
has an edge partition into at most $\lfloor n(n+1)/6\rfloor+b$ cliques of
order at most four, hence $n^2/6+O(n)$. The author reports its Lean 4 proof as
unconditional.

***
