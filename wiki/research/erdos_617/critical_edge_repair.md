---
name: research/erdos_617/critical_edge_repair
desc: Critical witnesses give individual edge-repair costs; an explicit matching-deletion family defeats additive charging without full hereditary caps.
tags: [graph-theory, proved, critical-graphs, obstruction]
sources: []
created: 2026-09-22T08:59:28Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/critical_edge_repair

***

**Proved exchange constraints and an obstruction to their aggregation,
not a resolution.** This investigates recoloring through independent
sets exposed by a deleted edge, rather than completing private cliques.
The individual bound applies to the
[least-budget minimal-ratio core](minimal_ratio_potential.md).

## Witness transversals control repair cost

Let $H$ satisfy

$$
|H|=ar+1,\quad \alpha(H)=a\ge2,\quad
|W|\le r\alpha(H[W])\quad(W\subsetneq V(H)).
$$

Suppose $e=uv$ is independence-critical. Write

$$
d_H(x)=r+s_x,\quad c_e=|N_H(u)\cap N_H(v)|,\quad
L_e=1+c_e-s_u-s_v,
$$

and put $Q_e=V(H)\setminus(N_H[u]\cup N_H[v])$.
Then

$$
\alpha(H[Q_e])=a-1,\qquad
|Q_e|=r(a-2)+L_e. \tag{1}
$$

A critical-edge witness supplies the lower independence bound;
an independent $a$-set there could be augmented by $u$.
The order formula follows from
$|N[u]\cup N[v]|=d(u)+d(v)-c_e$.

Every independent $(a+1)$-set of $H-e$ has the form
$\{u,v\}\cup S$, where $S$ is a maximum independent set
of $H[Q_e]$. Let $\tau_e$ be the minimum order of a vertex
set meeting all such $S$. Deleting a transversal $T$ gives
$\alpha(H[Q_e-T])\le a-2$, and proper-set minimality gives

$$
\boxed{\tau_e\ge |Q_e|-r(a-2)=L_e.} \tag{2}
$$

The bound is useful when $L_e>0$.

Let $D\subseteq E(H)$ contain $e$, and let $F$ be a set of
new edges, originally nonedges of $H$. If
$\alpha(H-D+F)\le a$, then

$$
\boxed{|F|\ge\tau_e\ge L_e.} \tag{3}
$$

Every original witness must contain an edge of $F$.
A relevant new edge is of type $uQ_e$, $vQ_e$, or $Q_eQ_e$.
Choose its endpoint in $Q_e$ in the first two cases and
either endpoint in the third. These at most $|F|$ vertices
meet every maximum independent set in $H[Q_e]$, proving (3).
Deleting further old edges does not invalidate this necessity.

In particular a trade removing and adding $k$ target edges cannot
remove any critical edge with $L_e>k$.

For a single-edge replacement there is an exact criterion. Put

$$
B_e=\{u,v\}\cup\bigcap_{S\in\mathcal I_{\max}(H[Q_e])}S.
$$

For a nonedge $f$ of $H$,

$$
\alpha(H-e+f)\le a\quad\Longleftrightarrow\quad f\subseteq B_e.
$$

If $L_e\ge2$, (2) forbids a vertex common to all the maximum
sets, so $B_e=\{u,v\}$ and no such replacement exists.
Every triangle edge whose endpoints have degree $r$ has
$L_e\ge2$.

## Why even matching deletions do not give additive costs

The following family shows that summing the individual bounds
requires additional information, even when the deleted edges form
a matching. Fix $a\ge3$, $s\ge1$, and put

$$
t=as+1,\qquad r=(2a+1)s+2,\qquad
H=C_{2a+1}[K_t].
$$

Write its cyclic clique bags as $B_0,\ldots,B_{2a}$.
Then

$$
|H|=ar+1,\qquad \alpha(H)=a,\qquad
\omega(H)=2t=r-s<r.
$$

Every proper induced set satisfies $|W|\le r\alpha(H[W])$.
If every bag meets $W$, its independence is $a$ and
$|W|\le ar$. Otherwise its bag support is a union of paths.
Pair consecutive bags along each path, retaining one singleton
when necessary. This partitions its vertices into
$\alpha(H[W])$ cliques of order at most $2t\le r$.

Every edge is independence-critical. After deleting an internal
bag edge, its endpoints can be joined by $a-1$ independent
vertices from the remaining $2a-2$-bag path. For a deleted
consecutive-bag edge, use the remaining $2a-3$-bag path.
All degrees are $3t-1$, with surplus $(a-1)s$.
A consecutive-bag edge has $2t-2$ common neighbors, so

$$
L_e=2s+1. \tag{4}
$$


Partition the bags into the $a$ groups

$$
\{B_0,B_1,B_2\},\quad \{B_3,B_4\},\quad\ldots,\quad
\{B_{2a-1},B_{2a}\}.
$$

Across each cut $(B_2,B_3),(B_4,B_5),\ldots,(B_{2a},B_0)$,
delete a perfect matching. Their union $D$ is a matching
of size $at$. Add the $t^2$ formerly missing edges between
$B_0,B_2$, calling this set $F$. The displayed groups
are now $a$ cliques, so $\alpha(H-D+F)\le a$.
Choosing one vertex from each of $B_1,B_3,\ldots,B_{2a-1}$
gives equality.

Nevertheless

$$
\frac{\sum_{e\in D}L_e}{|F|}
=\frac{a(2s+1)}{as+1}.
$$

At $s=1$ this is $3a/(a+1)>2$. Thus even the inequality
$\sum_{e\in D}L_e\le2|F|$ is false under proper-set
minimality, criticality, and $K_r$-freeness. The same repair
edges can serve many independent-set witness families.

For $a=3$ and $s\ge2$ the example also meets the
least-budget core allowance, since

$$
r(r-a)-\sum_v(d(v)-r)=7s^2-7s-2\ge0.
$$

It does not satisfy the full hereditary caps. Three consecutive
bags have $3t$ vertices and $(7t^2-3t)/2$ edges, giving

$$
e-D_r(3t)=(a^2-a-1)s^2+as>0.
$$

For $a=3$ the violation is $5s^2+3s$.

Thus the counterfamily rules out the attempted additive repair
charge without the full caps, not an argument that uses those
caps or actual cross-color constraints. No adequate aggregate
repair inequality has been established.
