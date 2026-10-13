---
name: research/erdos_809/proofs/c7_five_clique_construction
title: "A five-clique chain beating the longer-cycle formula for C7"
desc: "Plasma AI's construction showing that the Bucić–Chen–Ma coefficient fails for seven-cycles at every density strictly between 1/4 and 1/2; not independently reviewed."
tags: [research, graph-theory, erdos-809]
sources:
  - library/ramsey_theory/bucic_2026_maximal_anti_ramsey_conjecture_burr_erdos/theorem_1_2
created: 2026-10-13T02:29:30Z
updated: 2026-10-13T02:29:30Z
---

# A five-clique chain beating the longer-cycle formula for C7

***

This is Theorem 1.3 of Plasma AI's write-up *The seven-cycle case of the
maximal anti-Ramsey conjecture*, held as
[`c7_threshold.pdf`](../evidence/assets/publication/paper/c7_threshold.pdf)
with its TeX source in the [research evidence](../evidence/_index.md). It is
restated and proved here in this folder's notation. The result is the paper's,
credited to Plasma AI. It has not been independently reviewed here, is not
formalized and carries no tier.

## Statement

**Theorem.** Fix $1/4<q<1/2$, and let $s\in(0,1/2)$ be the unique solution of

$$
 q=\frac12-3s^2+4s^3.
$$

Then, as $n\to\infty$,

$$
 \chi_S(n,\lfloor qn^2\rfloor,C_7)\le(q-s^3)n^2+O(n),
 \qquad\text{and}\qquad
 q-s^3<\frac q2+\frac12\sqrt{q-\frac14}.
$$

The right side of the inequality is the coefficient that
[[../library/ramsey_theory/bucic_2026_maximal_anti_ramsey_conjecture_burr_erdos/theorem_1_2|Bucić, Chen and Ma's Theorem 1.2]]
proves for every odd cycle of length at least nine. So their formula fails
for $C_7$ at every fixed interior density, by a positive constant times $n^2$.
The [dense-curve obstruction](../archive/c7_dense_curve_obstruction.md) showed
the same failure at the single density $8869/20000$; this chain gives it at
every density in the open interval. Neither bears on the threshold
$e=\lfloor n^2/4\rfloor+1$, where the formulas agree at $n^2/8$. At $q=3/8$,
$s=1/4$, the upper coefficient is $23/64\approx0.359$ against the longer-cycle
$(3+2\sqrt2)/16\approx0.364$, and the
[density lower bound](c7_density_lower_bound.md) gives
$(4+\sqrt2)/16\approx0.338$.

## The construction

The map $s\mapsto\frac12-3s^2+4s^3$ has derivative $-6s(1-2s)<0$ on
$(0,1/2)$ and decreases from $1/2$ to $1/4$, so $s$ is well defined. Put

$$
 u=s^2,\qquad a=s(1-s),\qquad c=1-2s,
$$

so that $2u+2a+c=1$ and $u\le a$. Take five disjoint cliques
$U_1,A_1,C,A_2,U_2$, in this order along a chain, with $un$, $an$, $cn$,
$an$ and $un$ vertices. Join each clique completely to its neighbors in the
chain and add no other edges. Color as follows.

- The two complete bipartite graphs $U_1$–$A_1$ and $A_2$–$U_2$ are colored
  injectively with one common palette, so each color there is used once in
  each.
- Each edge inside $U_1$ is paired with a distinct edge inside $A_2$, and each
  edge inside $U_2$ with a distinct edge inside $A_1$, possible because
  $u\le a$; each pair gets its own new color.
- Every other edge gets its own new color.

## Every seven-cycle is rainbow

Number the cliques $1,\ldots,5$ along the chain. Every edge lies inside one
clique or joins two consecutive cliques, so a path from clique $i$ to clique
$j$ has at least $|i-j|$ edges. Each color is used at most twice, and only by
the three kinds of pairs above. If a cycle contains both edges of a pair,
removing them leaves two paths, each joining an endpoint of one edge to an
endpoint of the other.

- An edge inside $U_1$ (clique 1) and one inside $A_2$ (clique 4): both paths
  have at least three edges.
- An edge inside $U_2$ (clique 5) and one inside $A_1$ (clique 2): the same.
- An edge of $U_1$–$A_1$ (cliques 1 and 2) and one of $A_2$–$U_2$ (cliques 4
  and 5): according to how the endpoints are matched, the paths have at least
  $3+3$ or $4+2$ edges.

In every case the cycle has at least $2+6=8$ edges, so no seven-cycle carries
a repeated color.

## Counting

Up to $O(n)$,

$$
 \frac{e(G)}{n^2}=\frac{c^2}2+a^2+u^2+2ca+2au
 =\frac12-3s^2+4s^3=q,
$$

counting the inside of $C$, of $A_1,A_2$ and of $U_1,U_2$, then the joins
$C$–$A_i$ and $A_i$–$U_i$. The shared palette saves $au\,n^2$ colors and
the two pairings save $u^2n^2$, so

$$
 \frac{r(G)}{n^2}=q-(au+u^2)=q-s^3,
$$

since $au+u^2=s^3$. Rounding the part sizes symmetrically, with
$|U_1|=|U_2|$ and $|A_1|=|A_2|$, changes both counts by $O(n)$. Because the
edge density decreases in $s$, lowering $s$ by $O(1/n)$ and then deleting
surplus edges gives exactly $\lfloor qn^2\rfloor$ edges with
$(q-s^3)n^2+O(n)$ colors; deleting edges keeps every seven-cycle rainbow.

## Comparison with the longer-cycle coefficient

Direct expansion gives

$$
 q-\frac14-(q-2s^3)^2=s^3(1-2s)^2(2-s)>0.
$$

Since $q-2s^3=\frac12-3s^2+2s^3$ is positive on $[0,1/2)$, this gives
$q-2s^3<\sqrt{q-1/4}$, that is,
$q-s^3<\frac q2+\frac12\sqrt{q-\frac14}$.

## Standing

The construction and its counts are elementary and self-contained. No
independent review has been commissioned or filed, and no Lean statement
covers them. Whether the chain is optimal is the first of the
[open questions](../open_questions.md).
