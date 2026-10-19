---
name: research/graph_ramsey_interfaces/homogeneous_triangle_deletion_bounds
title: Blow-ups and homogeneous triangle deletion bounds
desc: An exact maximum-cut identity transfers large-order triangle-free deletion bounds to every order, with the density boundary and unresolved range explicit.
created: 2026-10-14T22:20:00Z
updated: 2026-10-18T03:09:12Z
---

# Blow-ups and homogeneous triangle deletion bounds

[[research/graph_ramsey_interfaces/_index|..]]

***

Let $D_2(G)$ be the fewest edges whose deletion makes a finite simple graph
$G$ bipartite. For every positive integer $t$, let $G[t]$ replace each vertex
by an independent set of $t$ vertices and each edge by a complete bipartite
graph between the corresponding sets. Then

$$
D_2(G[t])=t^2D_2(G). \tag{1}
$$

This identity transfers the large-order bounds of
[[../library/extremal_graph_theory/balogh_2021_max_cuts_triangle_free_graphs/theorem_2|Balogh, Clemen and Lidický, Theorem 2]]
to homogeneous bounds at every order. It is useful for
[[problems/extremal_graph_theory/E0023/_index|Problem 23]], but does not
close the middle-density case. The same all-order tail conclusions are stated
in Corollary 4.2, p. 5, of
[[../library/extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/_index|Ferudun's unrefereed preprint]].
The elementary derivation below, including the sparse-density endpoint, is
recorded by Plasma AI and is not independently reviewed. It uses the imported
Balogh–Clemen–Lidický theorem at statement depth; its proof is not reverified
here. Ferudun's numerical middle-band certificate is not a premise of this
derivation. [[research/leads/triangle_free_density_tails/_index|The density-tail lead]]
records this route, and its tail and general bounds are Plasma AI's pending
partial claim on [[problems/extremal_graph_theory/E0023/claims/2026_10_19_plasma_ai|Problem 23]].

## The exact blow-up identity

For any graph, $D_2(G)=e(G)-\operatorname{maxcut}(G)$: retaining all edges
across a maximum cut gives a bipartite graph, and every bipartite retained
graph lies across some cut of the original graph.

Given a cut of $G[t]$, write $x_v$ for the proportion of the cluster of $v$
on its first side. Its number of crossing edges divided by $t^2$ is

$$
\sum_{uv\in E(G)} \bigl(x_u(1-x_v)+x_v(1-x_u)\bigr).
$$

This function is affine in each coordinate separately. Holding the other
coordinates fixed, replacing one coordinate by either $0$ or $1$ can never
decrease its value. Repeating for every coordinate produces a cut that
places each whole cluster on one side. Consequently its maximum on
$[0,1]^{V(G)}$ is the maximum cut of $G$; those endpoint choices are also
available among the discrete proportions of a cut of $G[t]$. Thus
$\operatorname{maxcut}(G[t])=t^2\operatorname{maxcut}(G)$, proving (1).
A triangle in $G[t]$ would project to a triangle of $G$, so a blow-up of a
triangle-free graph remains triangle-free. Adding isolated vertices changes
neither $D_2$ nor the edge count.

## Removing the large-order qualification

The cited theorem states that for all sufficiently large $N$, every
triangle-free graph on $N$ vertices satisfies $D_2\le N^2/23.5$, and
satisfies $D_2\le N^2/25$ if either

$$
e\ge0.3197\binom N2
\quad\hbox{or}\quad
e\le0.2486\binom N2. \tag{2}
$$

Let $G$ be triangle-free on $v\ge1$ vertices. Apply the first bound to
$G[t]$ for sufficiently large $t$ and divide by $t^2$. It gives

$$
D_2(G)\le\frac{2v^2}{47}. \tag{3}
$$

For the dense case, assume $e(G)\ge3197v^2/20000$. Then

$$
e(G[t])\ge0.3197\frac{(tv)^2}{2}
\ge0.3197\binom{tv}{2}.
$$

Apply (2) and (1) to get $D_2(G)\le v^2/25$.

For the sparse case, assume $e(G)\le1243v^2/10000$. Use $G[t]$ together
with one isolated vertex, of order $N=tv+1$. Its edge count satisfies

$$
t^2e(G)\le0.2486\frac{(tv)^2}{2}
\le0.2486\binom{tv+1}{2}.
$$

By (2), $t^2D_2(G)\le(tv+1)^2/25$ for arbitrarily large $t$.
Dividing by $t^2$ and letting $t\to\infty$ proves the same bound
$D_2(G)\le v^2/25$, including the boundary density. The isolated vertex
is what permits using the source's $\binom N2$ normalization at equality.

For a graph on $v=5n$ vertices, (3) says $D_2(G)\le50n^2/47$.
The desired $D_2(G)\le n^2$ follows in the two homogeneous density ranges
just proved. The interval

$$
\frac{1243}{10000}<\frac{e(G)}{v^2}<\frac{3197}{20000}
$$

is left unresolved. Blow-ups preserve this density, so repeating the
transfer cannot remove that gap. A finite census is not implied: a reduction
of every middle-density obstruction to a bounded order would be an additional
theorem. No such reduction is supplied.

## The finite-range certificate interface

The blow-up identity and integer-rounding transfer also appear as Lemma 2.1
and Proposition 2.2, p. 3, of
[[../library/extremal_graph_theory/ferudun_2026_erdos_max_cut_small_multiples/_index|Ferudun's unrefereed preprint]].
His notation $\beta$ is $D_2$ here. He uses graphon edge density
$p=2e/v^2$ and monochromatic density $d_{\rm mono}=2D_2/v^2$.
The asserted middle-band certificate has

$$
d_{\rm mono}\le\frac2{25}+\delta,
\qquad \delta\approx4.8557798\cdot10^{-5}.
$$

On $v=5n$ vertices this gives
$D_2(G)\le n^2+(25/2)n^2\delta$. Integrality yields $D_2(G)\le n^2$
when $\delta<2/(25n^2)$, which the stated value satisfies through $n=40$
and not at $n=41$. This mechanism is Ferudun's; the elementary deduction
has been checked here, but its numerical premise has not. The source card
records the missing modules and state files in the supplied replay package.
The finite-range claim remains pending.

For the full question this transfer needs a middle-band inequality with zero
error, or a family of valid errors tending to zero uniformly over that band.
A single smaller positive error extends the rounding range but still leaves
arbitrarily large orders untreated. The two tail inequalities above and the
exact density normalization must be retained when composing such a band bound.
The source's reported finite-order optimization plateau supplies neither a
counterexample to the band inequality nor a proof that other relaxations fail.
