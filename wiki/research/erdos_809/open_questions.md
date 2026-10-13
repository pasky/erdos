---
name: research/erdos_809/open_questions
title: "Open questions beyond the seven-cycle threshold"
desc: "The five further questions of Plasma AI's seven-cycle write-up: the interior coefficient, stability, compatible edge families, the error term and a proof without regularity."
tags: [research, graph-theory, erdos-809]
sources: []
created: 2026-10-13T02:29:30Z
updated: 2026-10-13T02:29:30Z
---

# Open questions beyond the seven-cycle threshold

***

These are the further questions of Section 8 of Plasma AI's write-up *The
seven-cycle case of the maximal anti-Ramsey conjecture*, held as
[`c7_threshold.pdf`](evidence/assets/publication/paper/c7_threshold.pdf)
in the [research evidence](evidence/_index.md). None is needed for
[[problems/ramsey_theory/E0809/_index|Problem 809]], which the threshold theorem
answers. Here $\chi_S(n,e,C_7)$ is the least number of colors in an edge
coloring of some $n$-vertex graph with $e$ edges in which every seven-cycle is
rainbow, and a family of edges is *$C_7$-compatible* when every two of its edges
lie on a common seven-cycle.

1. **The interior coefficient.** For fixed $1/4<q<1/2$ and $s$ as in the
   [five-clique construction](proofs/c7_five_clique_construction.md), is
   $\chi_S(n,\lfloor qn^2\rfloor,C_7)=(q-s^3)n^2+o(n^2)$? The
   [density lower bound](proofs/c7_density_lower_bound.md) is strictly smaller
   at every interior density, so the coefficient is open between the two.
2. **Stability at the threshold.** If $G_n$ has $\lfloor n^2/4\rfloor+1$
   edges and a coloring with $n^2/8+o(n^2)$ colors in which every $C_7$ is
   rainbow, must $G_n$ be within $o(n^2)$ edge additions and deletions of two
   disjoint cliques of orders $n/2+o(n)$? The write-up gives a partial answer:
   the reweighting step of Section 4 of the [solution note](proofs/c7_solution.md),
   run with cleaning parameter $\eta=v^2/128$ and weight shift $v/16$ when the
   normalized degree variance is at least $v>0$, raises the weighted density to
   at least $1/4+v^2/64$, and the finite inequality then forces more than
   $(1/8+v/70)n^2$ colors for large $n$. So the variance of such graphs tends to
   zero. That consequence is the write-up's and has not been checked here.
3. **Compatible edge families.** Does every $n$-vertex graph with more than
   $\lfloor n^2/4\rfloor$ edges contain a $C_7$-compatible family of at least
   $n^2/8-o(n^2)$ edges? A positive answer would strengthen the threshold
   theorem, since such a family needs that many colors. The
   [near-regular](proofs/c7_near_regular.md) and
   [near-bipartite](proofs/c7_near_bipartite.md) notes build such families
   under their hypotheses; the fractional coloring argument of
   [palette savings](proofs/c7_palette_savings.md) does not produce one.
4. **The error term.** Is
   $\chi_S(n,\lfloor n^2/4\rfloor+1,C_7)=n^2/8+O(n)$? The write-up's upper
   bound, from two cliques sharing one vertex, already has this error term;
   the two disjoint cliques of Section 5 of the solution note give
   $n^2/8+O(n^{3/2})$.
5. **A proof without regularity.** Can the threshold theorem be proved without
   the Szemerédi regularity lemma, in particular by a direct structural
   argument in place of the passage from closed walks to cycles in
   [seven-walk cleaning](proofs/c7_homomorphic_cleaning.md)? Such an argument
   could improve the quantitative bounds. Bucić, Chen and Ma prove the
   longer-cycle cases by induction and short-path arguments
   ([[../library/ramsey_theory/bucic_2026_maximal_anti_ramsey_conjecture_burr_erdos/theorem_1_2|their Theorem 1.2]]).
