---
name: research/erdos_132/long_rank_gaps
title: Quadratic gap collapse and odd girth at fixed long ranks
desc: |
  Bounded rarity forces every rich fixed long rank to lie within O(Delta/n^2)
  of its predecessor; fixed top-rank unions have odd girth Omega(n^(1/8)).
sources: []
research_state: closed
created: 2026-09-23T07:45:00Z
updated: 2026-09-24T22:12:56Z
---


# Quadratic gap collapse and odd girth at fixed long ranks

***

These are necessary conditions, not a resolution of either assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md). Write the distinct
lengths as $\Delta=r_1>r_2>\cdots>r_q$; all edge counts are unordered.

## An angular matching inequality

Suppose $0<r<\ell$, no occurring distance lies in $(r,\ell)$, and the
graph $J$ of pairs longer than $r$ has $E$ edges and a matching of
size $M>0$. If $M^2\ge4E$, then

$$\frac{\ell-r}{\ell}\le\frac{2\pi^2E^2}{M^4}. \tag{1}$$

Put $\alpha=2\arccos(r/\ell)$ and $B=\lceil\pi/\alpha\rceil$.
Partition unoriented directions $[0,\pi)$ into $B$ half-open intervals
of equal width at most $\alpha$. Consider two matched segments in one
interval, oriented consistently, with lengths $L_i,L_j\ge\ell$,
unit directions $u_i,u_j$, and midpoint difference $w$. Their angle
$\theta$ satisfies $\theta<\alpha$, including when the bin width equals
$\alpha$. Two cross-pair vectors are

$$w\pm v,\qquad v=(L_i u_i+L_j u_j)/2.$$

The parallelogram identity and projection onto the angular bisector give

$$\max\{|w+v|,|w-v|\}\ge |v|
\ge\frac{L_i+L_j}{2}\cos(\theta/2)>r.$$

Each pair of matching edges in one bin therefore supplies an edge of
$J$. These supplied edges are distinct for different pairs of matching
edges: their endpoints identify the two matched segments. None is an
edge of the matching itself. For bin occupancies $M_i$,

$$\sum_i\binom{M_i}{2}\le E-M,\qquad
\frac{M^2}{B}\le2E-M\le2E.$$

Since $B\le\pi/\alpha+1$ and $M^2\ge4E$,
$\pi/\alpha\ge M^2/(4E)$. Consequently

$$1-r/\ell=1-\cos(\alpha/2)
\le\alpha^2/8\le2\pi^2E^2/M^4.$$

The matched segments need not have equal lengths. The assumptions
$M>0$ and $r<\ell$ exclude the zero denominators.

## A gap estimate from core excess

Fix $k\ge2$. Let $H$ be the 2-core of $G_{r_k}(A)$, and put
$\sigma=e(H)-v(H)>0$, $a=4k-3$, $b=k-1$. The
[long-rank bounds](layers_and_obstructions.md) give

$$\Delta(H)\le4k-2=a+1,\qquad m_A(r_j)\le(2j-1)n.$$

If $\sigma\ge4ab\sqrt n$, then

$$\frac{r_{k-1}-r_k}{\Delta}
\le32\pi^2a^4b^4\frac{n^2}{\sigma^4}. \tag{2}$$

Indeed, consider the longer-pair graph on $V(H)$, and a maximum matching
of size $M$ in it. Its $2M$ endpoints $U$ cover all its edges. The
remaining vertices have diameter at most $r_k$, so the planar diameter
bound gives $e(H-U)\le v(H)-2M$. Counting edges touching $U$ by the
core maximum degree yields

$$\sigma\le2aM,\qquad M\ge\sigma/(2a).$$

The number $E$ of longer pairs on $V(H)$ satisfies

$$E\le n\sum_{j=1}^{k-1}(2j-1)=b^2n.$$

Thus $M^2\ge4E$ under the stated hypothesis. Apply (1) to the core
vertex set, with $r=r_k$ and $\ell=r_{k-1}$. This is valid even if
$r_{k-1}$ itself does not occur on that vertex set: every occurring
length greater than $r_k$ is at least $r_{k-1}$. Substitution and
$r_{k-1}\le\Delta$ prove (2).

Suppose now that $n\to\infty$ and $R(A)\le K$. The
[linear core-surplus argument](diameter_activity.md) gives, for every
rich fixed largest rank $k$,

$$\sigma\ge n/[3(K+1)]-o(n).$$

The finitely many choices of a rich smallest rank at most $K+1$ make
this uniform for fixed $K,k$. Hence eventually
$\sigma\ge n/[6(K+1)]$, and (2) gives

$$r_{k-1}-r_k=O_{K,k}(\Delta n^{-2}). \tag{3}$$

For a hypothetical unbounded $R=1$ sequence, every fixed rank $j\ge2$
is rich. Summing (3) gives

$$\frac{\Delta-r_k}{\Delta}=O_k(n^{-2})
\quad\text{for every fixed }k. \tag{4}$$

The ranks exist eventually by the elementary two-anchor distance bound.
For general bounded rarity, (3) does **not** control gaps whose lower
endpoint is rare, and does not imply (4).

## Odd-cycle contraction without a diameter assumption

Let $V$ contain an odd cycle all of whose edges have length at least
$r>0$. Then

$$Q=\bigcap_{v\in V}\overline B(v,r)$$

has diameter at most $r$ (with an empty or singleton intersection allowed).

Suppose instead $x,y\in Q$ with $d=|x-y|>r$. Every point of $V$ is in
the lens $L=\overline B(x,r)\cap\overline B(y,r)$. Normalize
$x=(0,0)$ and $y=(d,0)$. Every $(a,b)\in L$ has $0<a<d$.
Two points in the upper closed half-lens, say $(a,b),(c,e)$ with
$b\ge e\ge0$, are at distance strictly less than $r$. For $a\le c$,

$$(a-c)^2+(b-e)^2\le(a-c)^2+b^2
<(a-d)^2+b^2\le r^2;$$

for $a>c$, use instead
$(a-c)^2+b^2<a^2+b^2\le r^2$. Reflection treats the lower half-lens.
Thus every edge of length at least $r$ joins the two open half-planes;
a vertex on the axis has no such neighbor. This graph is bipartite,
contradicting the odd cycle.

## Quantitative odd girth

Let $H$ be the $r_k$-core with $\sigma>0$ as above, and write
$M(A)=\max_{\Gamma\text{ circle}}|A\cap\Gamma|$. If the union of
the $k$ largest-distance graphs contains an odd cycle of length $t$,
then

$$t\ge\frac{\sigma}{(4k-3)(k-1)M(A)}. \tag{5}$$

For its vertex set $V$, the points not in $Q$ lie on the at most
$t(k-1)$ circles centered at members of $V$ with radii greater than
$r_k$. Thus $|A\setminus Q|\le t(k-1)M(A)$. The core vertices in
$Q$ have diameter at most $r_k$. Counting edges after deleting the
other core vertices, as in the matching argument, gives
$\sigma\le(4k-3)|A\setminus Q|$, proving (5).

Under $R(A)\le K$, the [weighted-circle theorem](weighted_circle_energy.md)
gives $M(A)=O_K(n^{7/8})$. If $r_k$ is rich, linear core surplus
therefore gives odd girth $\Omega_{K,k}(n^{1/8})$ for the top-$k$ union.
For any fixed $h$, choose a rich rank among $h,\ldots,h+K$ and apply
this conclusion to that larger union. Hence

$$\text{odd girth of the top-}h\text{ union}
=\Omega_{K,h}(n^{1/8}). \tag{6}$$

An acyclic or bipartite graph has infinite odd girth and is allowed.

## Why even cycles do not replace odd cycles

Use the already checked regular initial construction in
[second-distance extremality](second_distance_extremality.md), with
$m=8$, $p_j=e^{ij\pi/4}$, $c=\cos(\pi/8)$,
$r=2c$, $\rho=\sqrt{5c^2-1}-c$, and
$u_j=-\rho e^{i(2j+1)\pi/8}$. Retain

$$A=\{p_1,p_2,p_3,p_5,p_6,p_7,u_1,u_2,u_5,u_6\}.$$

The three diameter pairs are $p_1p_5,p_2p_6,p_3p_7$, of length 2.
There are twelve second-distance pairs at $r$: the four outer edges
$p_1p_6,p_2p_5,p_2p_7,p_3p_6$, and the eight pairs joining each
retained $u_j$ to $p_j,p_{j+1}$. All other lengths are smaller by
the parent construction's exact formulas. Thus $m_A(r)=12>10$.
The top-two union is bipartite, with parts

$$\{p_1,p_2,p_3,u_5,u_6\},\qquad
\{p_5,p_6,p_7,u_1,u_2\}.$$

Both omitted points $p_0,p_4$ lie in
$\bigcap_{a\in A}\overline B(a,r)$, but are at distance $2>r$.
So the odd-cycle contraction is false for general even-cycle supports,
even when the second-distance class is rich.

The author checked the angular inequality and its core application,
including half-open bins and zero cases, and the contraction, odd-girth
deduction, and exact ten-point obstruction; the arguments are
author-recorded.
Neither gap collapse nor growing odd girth controls the remaining global
palette. The unrestricted questions stay open in this work.
