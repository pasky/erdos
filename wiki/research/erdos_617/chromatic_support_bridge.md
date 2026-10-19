---
name: research/erdos_617/chromatic_support_bridge
desc: Neighborhood expansion controls the independence number of a vertex-critical chromatic support; non-Ore density strengthens its order bound.
tags: [graph-theory, proved, critical-graphs, reductions]
sources:
  - kostochka_yancey_2012_ores_conjecture_color_critical_graphs_is_almost_true
created: 2026-09-22T13:50:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/chromatic_support_bridge

***

**Proved bounds, not a contradiction.** Use the
[least-budget minimal-ratio core](minimal_ratio_potential.md), with

$$
|H|=ar+1,\quad \alpha(H)=a,\quad \delta(H)\ge r,
\quad S:=\sum_v(d_H(v)-r)\le rh,\quad h=r-a,
$$

where $r\ge12$ and $a\le r-5$. Every nonempty independent set obeys

$$
|N_H[I]|\ge r|I|+1. \tag{1}
$$


Choose an inclusion-minimal vertex set $U$ such that $J=H[U]$ is not
$r$-colorable, and put $m=|U|$, $b=\alpha(J)$. Such a set exists
because $|H|>r\alpha(H)$. Then

$$
\boxed{b\le\min\{a,h+1\},\qquad
(r-2)m\le r^2(h+1)-3r-2.} \tag{2}
$$

If $J=H$, the stronger conclusion is

$$
\boxed{a\le\lfloor(r+1)/2\rfloor.} \tag{3}
$$

The distinction between vertex-critical $J$ and an independence-critical
core is essential throughout.

## A bridge using the supplied density theorem

Let $c=e_H(U,V(H)\setminus U)$. Nonnegativity of degree surplus gives

$$
S\ge2e(J)+c-rm. \tag{4}
$$

For a maximum independent $b$-set $I$ of $J$, inducedness makes $I$
independent in $H$. By (1),

$$
c\ge |N_H[I]\setminus U|\ge rb+1-m. \tag{5}
$$


An edge-minimal non-$r$-colorable subgraph of $J$ must be spanning: otherwise
its vertex support contradicts the choice of $U$. It is therefore
$(r+1)$-critical in the usual subgraph sense. The supplied [Kostochka--Yancey
source, Theorem 3 and equation
(9)](../../../library/extremal_graph_theory/kostochka_yancey_2012_ores_conjecture_color_critical_graphs_is_almost_true/_index.md)
gives

$$
2e(J)-rm\ge(1-2/r)m-r+1+2/r. \tag{6}
$$

The digest was read before checking that passage. Combining (4)--(6)
with $S\le rh$ proves

$$
rb\le r(h+1)-2-2/r+2m/r, \tag{7}
$$

and hence $b\le h+2$. This already supplies independence control on
the chromatic support, rather than merely a scalar order estimate.
Here $b$ is the independence number of the **induced graph $J$**, not
of its edge-pruned critical subgraph.

## The non-Ore strengthening

The previously proved [Ore-cap exclusion](minimal_core_structure.md)
says that every $(r+1)$-Ore graph satisfying the $(r+1)$-set cap has
at least $r^2+1$ vertices. It applies to the spanning critical subgraph
just extracted, since edge deletion preserves the upper caps. That
subgraph has at most $ar+1<r^2+1$ vertices, so is non-Ore.

An additional primary source gives a useful strict improvement: Kostochka and
Yancey, *A Brooks-type result for sparse critical graphs*,
[Theorem 6, printed page 4](https://kostochk.web.illinois.edu/docs/submit/cca18y.pdf).
For a non-Ore $k$-critical graph, $k\ge6$, it states

$$
2e\ge\frac{(k+1)(k-2)m-(k^2-5k+2)}{k-1}.
$$

Its statement was checked in the primary text; its full proof was not
independently rederived. Substituting $k=r+1$ strengthens (6) to

$$
2e(J)-rm\ge(1-2/r)m-r+3+2/r. \tag{8}
$$

Using $c\ge0$ in (4) gives the order bound in (2). Using (5) instead
gives

$$
\boxed{rb\le r(h+1)-4-2/r+2m/r.} \tag{9}
$$


To obtain $b\le h+1$, first suppose $h+1<r/2$. The order bound in
(2) implies

$$
m<r^2/2+2r+1,
$$

because substituting this latter expression into its left side exceeds
$r^3/2-3r-2$ by $r^2$. Equation (9) and integrality then give the
claim. If $h+1\ge r/2$, the claim already follows from $b\le a$
unless $r$ is even and $a=r/2+1=h+2$. In that sole case
$m\le ar+1=r^2/2+r+1<r^2/2+2r+1$, so (9) again suffices.
This proves (2).

If $J=H$, substitute $b=a$, $m=ar+1$ into (9). It gives

$$
2a(r-1)\le r^2+r-4,
\qquad a\le(r+2)/2-1/(r-1),
$$

and hence (3).

## Actual color coupling strengthens the support cap

The core still carries an actual coloring in which every foreign color
has independence at most $r$. If a foreign color graph on $U$ could
partition into $r$ cliques, those same parts would be independent in
$J$, contradicting $\chi(J)>r$. Thus the elementary
[nonpartite Turan gap](packing_tools.md) applies to each foreign color.
For $m\ge2r+1$, it gives

$$
\boxed{e(J)\le D_r(m)-(r-1)(\lfloor m/r\rfloor-1).} \tag{10}
$$

Indeed every foreign color has at least
$p_r(m)+\lfloor m/r\rfloor-1$ edges, and their edge sets partition
the complement of $J$ on $U$. This is an upper bound for this
chromatic support, not an inherited bound on every induced subgraph.

## What remains missing

Even with (2), $J$ need not have $m>rb$. The
[hereditary span theorem](hereditary_span_bound.md) therefore cannot
be applied merely because $b\le h+1$ is smaller than $a$.
No theorem has been established saying that every capped graph of
small independence number is $r$-colorable below its capacity $rb$.
Likewise (3) applies only if the entire core is vertex-critical;
the core has not been proved to have that property.

The expansion/cut bridge, the substitution in the supplied density
theorem, and the non-Ore strengthening against the later primary theorem
were checked by the author; the argument is author-recorded. These
estimates
do not establish an unrestricted infinite family of positive cases.
