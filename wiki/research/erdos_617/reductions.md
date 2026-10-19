---
name: research/erdos_617/reductions
desc: Uniform consequences of a hypothetical balanced coloring and the limits of the fixed-case proof architecture.
tags: [graph-theory, reductions]
sources: []
created: 2026-09-21T23:52:12Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/reductions

***

All claims below are necessary conditions on a hypothetical counterexample;
they do not prove that one exists. Put $N=r^2+1$, and let $G_i$ be the graph
of color $i$. The exact counterexample condition is


$$
\alpha(G_i)\le r\qquad(i=1,\ldots,r),
$$


and the graphs $G_i$ partition $E(K_N)$.

## Inherited density

For $n=rq+b$, $0\le b<r$, define


$$
p_r(n)=r\binom q2+qb,
\qquad D_r(n)=\binom n2-(r-1)p_r(n).
$$


Complementary Turán gives, for every vertex set $W$ and every color $i$,


$$
p_r(|W|)\le e(G_i[W])\le D_r(|W|).
$$


The upper bound follows by applying the lower bound to the other $r-1$
colors and summing their disjoint edge sets. In particular,


$$
e(G_i[S])\le\binom r2+1\quad(|S|=r+1).
$$


The general inequality is strictly stronger than this last cap. Its use in the
supplied nine-color proof was checked in
[source, Lemma 2](../../../library/extremal_graph_theory/sneiderman_2026_nine_color_case_balanced_coloring/_index.md).

## Least color and neighborhood accounting

A least color $G$ satisfies


$$
e(G)\le \frac{r(r^2+1)}2.
$$


It has a vertex of degree at most $r-1$. Otherwise it is $r$-regular.
Brooks's theorem then makes it $r$-colorable, because a component
$K_{r+1}$ is forbidden and the odd-cycle exception has degree two, whereas
$r\ge3$. An $r$-coloring of $N>r^2$ vertices gives an independent
$r+1$-set, a contradiction.

For a minimum-degree vertex $v$, put $d=d_G(v)$, $A=N_G(v)$,
$U=V(G)\setminus(A\cup\{v\})$, $X=e_G(A,U)$, and $Y=e(G[A])$.
Summing the degree lower bound over $A$ gives


$$
X+2Y\ge d(d-1).
$$


Since $Y\le\binom d2$,


$$
e(G[U])\le e(G)-d-\binom d2,
\qquad |U|=r^2-d,
\qquad\alpha(G[U])\le r-1.
$$


## Monochromatic $K_r$'s

If $Q$ is a color-$i$ $K_r$ and $x\notin Q$, at most one of the
$r$ edges from $x$ to $Q$ has color $i$. Indeed, all the other
$r-1$ colors must occur on those edges. In particular, distinct such
cliques intersect in at most one vertex.

Given disjoint color-$i$ $K_r$'s $Q_1,\ldots,Q_k$ and a disjoint
color-$i$ independent set $I$, one can extend $I$ by one representative
from each $Q_j$, while preserving independence, provided
$|I|+k\le r$. At each step fewer than $r$ previously selected vertices
exclude at most one vertex each from the next block.

Consequently, after removing $j$ disjoint target $K_r$'s from the
nonneighborhood $U$ above, the residual $R_j$ has


$$
|R_j|=r^2-d-jr,\qquad
\alpha(G[R_j])\le r-1-j,
$$


and


$$
e(G[R_j])\le
\frac{r(r^2+1)}2-\binom{d+1}{2}-j\binom r2.
$$


To check the independence bound, an independent set of size $r-j$ in
$R_j$ could be extended to size $r$ within $U$, and then by $v$.
The edge estimate discards the internal edges of the removed cliques, and
does not count any cross edges twice.

This is the uniform content of [the nine-color proof, Lemmas 6--7 and Section
3](../../../library/extremal_graph_theory/sneiderman_2026_nine_color_case_balanced_coloring/_index.md).
What is missing is a uniform theorem forcing another $K_r$ in the residual, or
otherwise excluding it. Parameter-specific tables and finite Ramsey catalogs
cannot be substituted for such a theorem.
