---
name: research/erdos_644/clutter_amalgamation
desc: Standard clutter two-sums add transversal numbers but violate the local property for high-transversal inputs; bounded-interface amalgamations face a quantitative separator obstruction.
tags: [proved, limitations, convergence]
sources: []
created: 2026-09-23T02:58:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/clutter_amalgamation

***

This records an unsuccessful attempt to obtain the fixed-$r$ limit by a Hajós-
or Ore-type sum. The obstruction concerns operations retaining most input edges
on nearly disjoint supports. It does not exclude operations with a large
distributed interface or extensive replacement of input edges.

Write $P_r$ for the at-most-$r$ two-cover condition, with $r\ge3$.

## A separator obstruction

Suppose a $P_r$ family contains subfamilies

$$
\mathcal A\subseteq2^{X\cup S},\qquad
\mathcal B\subseteq2^{Y\cup S},
$$

where $X,Y,S$ are disjoint, $|S|=s$, and $\mathcal A$ has rank at most $k$. If
$\mathcal B$ has a nonempty edge disjoint from $S$, then

$$
\tau(\mathcal A)\le s+\left\lceil\frac{k}{r-2}\right\rceil.
\tag{1}
$$

Indeed, let $\mathcal A_0$ consist of the edges avoiding $S$. Any
at-most-$(r-1)$ of them have nonempty common intersection: otherwise they need
at least two points, and the disjoint edge of $\mathcal B$ requires another.
Partition an edge of $\mathcal A_0$ into $r-2$ parts of size at most
$\lceil k/(r-2)\rceil$. If no part is a transversal, choose an avoiding edge for
each part. Together with the partitioned edge these give at most $r-1$ edges
with empty intersection. Thus one part covers $\mathcal A_0$, and adding $S$
covers $\mathcal A$. The empty residual case is immediate.

In particular, suppose an amalgamation retains each rank-$k_i$,
transversal-$t_i$ input after deletion of at most $d_i$ edges, and the retained
supports intersect in at most $s$ vertices. If $t_j>d_j+s$, the other retained
side has an edge avoiding the interface, and (1) gives

$$
t_i\le d_i+s+\left\lceil\frac{k_i}{r-2}\right\rceil.
\tag{2}
$$

Here deleting $d_i$ nonempty edges lowers transversal number by at most $d_i$.
Additional edges in the amalgamation do not remove the local obstruction. For
$r=7$ and $t_i=(3/4+o(1))k_i$, inequality (2) requires
$d_i+s\ge(11/20-o(1))k_i$. Bounded-interface, bounded-edge-deletion sums
therefore cannot amplify near-extremal inputs.

A related direct bound concerns cross-padding. For any rank-$k$ subfamily
$\mathcal A$ of a $P_r$ family and any edge $E$ of that family,

$$
|E\cap V(\mathcal A)|\ge\tau(\mathcal A)-\left\lceil\frac{k}{r-2}\right\rceil.
\tag{3}
$$

To prove it, delete $S=E\cap V(\mathcal A)$ from consideration. The residual
$\mathcal A_S$ is disjoint from $E$, hence is $(r-1)$-wise intersecting by the
same argument. Cover this residual by the partition argument, then add $S$. Thus
one-sided cross-padding also needs linearly many points in the intended regime.

## The standard clutter two-sum

Take uniform inputs $\mathcal H_i$ of uniformities $k_i\ge2$ on disjoint
grounds, with $t_i=\tau(\mathcal H_i)\ge2$, and choose an incident vertex $v_i$
in each. Put

$$
\mathcal B_i=\{E\in\mathcal H_i:v_i\notin E\},\qquad
\mathcal A_i=\{E\setminus\{v_i\}:v_i\in E\in\mathcal H_i\}.
$$

All these edges are nonempty, and both $\mathcal B_i$ are nonempty. On the
remaining grounds define

$$
\mathcal K=\mathcal B_1\cup\mathcal B_2
\cup\{A_1\cup A_2:A_i\in\mathcal A_i\}.
$$

Write $b_i=\tau(\mathcal B_i)$ and $a_i=\tau(\mathcal A_i\cup\mathcal B_i)$. The
exact formulas are

$$
t_i=\min\{1+b_i,a_i\},\qquad
\tau(\mathcal K)=\min\{a_1+b_2,b_1+a_2\}\ge t_1+t_2-1.
\tag{4}
$$

A cover either uses $v_i$ or avoids it, giving the first formula. A cover of
$\mathcal K$ must cover each pure side $\mathcal B_i$ and must cover at least
one complete side $\mathcal A_i$ of the product. This gives the second formula.
Also

$$
\operatorname{rank}(\mathcal K)\le
\max\{k_1,k_2,k_1+k_2-2\}.
$$

These numerical parameters would be suitable for amplification. However, the
pure sides are disjoint, so (1) forces

$$
P_r(\mathcal K)\quad\Longrightarrow\quad
b_i\le\left\lceil\frac{k_i}{r-2}\right\rceil,
\qquad
t_i\le1+\left\lceil\frac{k_i}{r-2}\right\rceil.
$$

Thus the construction fails for the intended inputs. Removing nonminimal edges
to obtain a clutter cannot repair a failure of $P_r$: replace every edge of a
bad tuple by a contained minimal edge, and its lack of a two-cover persists.

No alternative additive construction was obtained. In particular, none of these
calculations proves or disproves the general convergence assertion.
