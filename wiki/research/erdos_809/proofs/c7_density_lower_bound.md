---
name: research/erdos_809/proofs/c7_density_lower_bound
title: "A lower bound for rainbow seven-cycles at every edge density"
desc: "Plasma AI's lower bound on the seven-cycle maximal anti-Ramsey function above the Turán threshold, from the finite inequality and cleaning; not independently reviewed."
tags: [research, graph-theory, erdos-809]
sources: []
created: 2026-10-13T02:29:30Z
updated: 2026-10-13T02:29:30Z
---

# A lower bound for rainbow seven-cycles at every edge density

***

This is Theorem 1.2 of Plasma AI's write-up *The seven-cycle case of the
maximal anti-Ramsey conjecture*, held as
[`c7_threshold.pdf`](../evidence/assets/publication/paper/c7_threshold.pdf)
with its TeX source in the [research evidence](../evidence/_index.md). It is
restated and proved here from the notes of this folder. The result is the
paper's, credited to Plasma AI. It has not been independently reviewed here and
is not formalized: the Lean development covers only the threshold theorem. It
carries no tier.

## Statement

**Theorem.** For $\lfloor n^2/4\rfloor+1\le e\le\binom n2$ put $q=e/n^2$ and

$$
 f(q)=q-\frac18+\frac14\sqrt{q-\frac14}\qquad(1/4\le q\le1/2).
$$

Then, as $n\to\infty$,

$$
 \chi_S(n,e,C_7)\ge f(q)\,n^2-o(n^2),
$$

with the error term uniform in $e$.

At $q=1/4$ this is the threshold value $n^2/8$, and at $q=1/2$ it is
$n^2/2$, every edge of $K_n$ needing its own color. For odd cycles of length
at least nine,
[[../library/ramsey_theory/bucic_2026_maximal_anti_ramsey_conjecture_burr_erdos/theorem_1_2|Bucić, Chen and Ma's Theorem 1.2]]
gives the exact coefficient $q/2+\frac12\sqrt{q-1/4}$ on the same range.
Writing $t=\sqrt{q-1/4}$, that coefficient exceeds $f(q)$ by $t(1-2t)/4$,
which is positive for $1/4<q<1/2$. The bound here is therefore weaker in the
interior, and it does not determine the coefficient for $C_7$ there; the
[five-clique construction](c7_five_clique_construction.md) shows that the
longer-cycle coefficient is wrong for $C_7$ at every interior density. At
$q=3/8$ the lower coefficient is $(4+\sqrt2)/16\approx0.338$, the
construction's upper coefficient is $23/64\approx0.359$, and the longer-cycle
coefficient is $(3+2\sqrt2)/16\approx0.364$.

## Proof

Three results of this folder are used:

- the finite inequality (1) of the [solution note](c7_solution.md), proved in
  [palette savings](c7_palette_savings.md): for vertex weights summing to one
  with weighted edge density $Q>1/4$, the fractional cost $C$ of covering the
  active edge types by independent sets of the two-plus-three conflict graph
  $J_{23}$ satisfies $C\ge f(Q)$;
- the cleaning lemma of Section 2 of the solution note, proved in
  [seven-walk cleaning](c7_homomorphic_cleaning.md): for every $\eta>0$ and
  all large $n$, a graph whose seven-cycles are all rainbow loses at most
  $\eta n^2$ edges to a spanning subgraph $H$ in which no closed seven-walk
  contains two distinct edges of the same color;
- the threshold theorem of the solution note,
  $\chi_S(n,\lfloor n^2/4\rfloor+1,C_7)\ge n^2/8-o(n^2)$.

Choose $\eta_n\downarrow0$ slowly enough that the cleaning lemma applies with
$\eta=\eta_n$ for all large $n$. Let $G$ have $n$ vertices, $e$ edges and an
$r$-coloring under which every $C_7$ is rainbow. Let $H$ be its cleaned
subgraph, and put $Q=e(H)/n^2$, so that $0\le q-Q\le\eta_n$.

*Case $Q>1/4$.* Give every vertex weight $1/n$, so every edge of $H$ has
demand $1/n^2$ and the weighted edge density is $Q$. By the cleaning lemma,
each color class of $H$, restricted to active edge types, is independent in
$J_{23}(H)$, since a conflict between two of its edges would close into a
seven-walk with a repeated color. Giving each nonempty class weight $1/n^2$
covers every demand, so $C\le r/n^2$. The finite inequality gives

$$
 \frac r{n^2}\ \ge\ f(Q)\ \ge\ f(q)-\eta_n-\frac14\sqrt{\eta_n},
$$

using $q-Q\le\eta_n$ and $\sqrt a-\sqrt b\le\sqrt{a-b}$ for $a\ge b\ge0$.

*Case $Q\le1/4$.* Then $q\le1/4+\eta_n$. Delete edges of $G$ until exactly
$\lfloor n^2/4\rfloor+1$ remain; every remaining $C_7$ is still rainbow and
at most $r$ colors are used. The threshold theorem gives

$$
 \frac r{n^2}\ \ge\ \frac18-o(1)\ \ge\ f(q)-\eta_n-\frac14\sqrt{\eta_n}-o(1),
$$

since $f$ is increasing and $f(1/4+\eta_n)=1/8+\eta_n+\frac14\sqrt{\eta_n}$.

In both cases the error depends only on $n$, which proves the theorem
uniformly in $e$.

## Standing

The argument adds two cases to results recorded in this folder. Its only
external premise is the Szemerédi regularity lemma, used through the cleaning
lemma. The threshold theorem it uses is the $k=3$ branch of claim
[[theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/_index|L17]], formalized
in Lean, but this note's argument is not. No independent review of this note or
of the paper's proof has been commissioned or filed. The question whether the
bound or the construction gives the true coefficient is the first of the
[open questions](../open_questions.md).
