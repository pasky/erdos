---
name: research/erdos_617/minimal_ratio_potential
desc: A least-color potential retains its edge budget on a connected minimal-ratio core, with full neighborhood expansion and optional independence-critical pruning.
tags: [graph-theory, proved, reductions, potential]
sources: []
created: 2026-09-22T02:30:00Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_617/minimal_ratio_potential

***

**Proved reduction, not a resolution.** A hypothetical counterexample
with $r\ge12$ yields an $r$-coloring of a complete graph on $ar+1$
vertices, with a distinguished color graph $H$, such that

$$
4\le a\le\min\{r-5,\lfloor3r/4\rfloor\},\qquad \alpha(H)=a,\qquad
\delta(H)\ge r,\qquad \omega(H)\le r-1,
\tag{1}
$$


$$
2e(H)\le ar(r-1)+r(r+1),
\tag{2}
$$

and every proper induced subgraph satisfies

$$
|W|\le r\alpha(H[W]). \tag{3}
$$

Every other color has independence at most $r$. In particular all
inherited density bounds remain available. One may also make $H$
connected and independence-critical, in the sense that deleting any
edge increases its independence number. This last step changes the
coloring on the core and is not asserted to extend to the original
vertex set.

The point of the reduction is that (2) and the strong minimality (3)
hold **simultaneously**. The earlier two-supported selected color need
not have the least-color budget; no identification of those two colors
is being made here.

The later [greedy block charge](greedy_block_charge.md) proves the uniform bound
$a\le\lfloor3r/4\rfloor$. The
[core-structure results](minimal_core_structure.md) strengthen the range to
$a\le r-5$ and $r<8(r-a)^2$ and show that the degree-$r$ vertices induce a
Gallai forest. They also exclude a specific maximal-low-clique decomposition,
but do not force such a decomposition or resolve the core.

## 1. Normalizing a least color

For a graph $J$ with an independence upper bound $b$, define

$$
\Phi(J,b)=2e(J)-(2r-1)|J|+r^2b.
$$

Initially take a least color on $N=r^2+1$ vertices and $b=r$.
Its edge budget gives

$$
\Phi(J,r)\le r^2-r+1. \tag{4}
$$

Maintain $|J|=rb+t$, $t\ge1$, and $\alpha(J)\le b$.

If a minimum-degree vertex $v$ has degree $d\le r-1$, delete its
closed neighborhood and replace $b$ by $b-1$. At least
$\binom{d+1}{2}$ edges are removed: writing $A=N(v)$, minimum-degree
accounting gives

$$
e(A,V\setminus(A\cup\{v\}))+2e(A)\ge d(d-1),
$$

and $e(A)\le\binom d2$. Thus the potential changes by at most

$$
-d(d+1)+(2r-1)(d+1)-r^2
=-(r-d-1)^2\le0. \tag{5}
$$

The new surplus is $t+r-d-1\ge1$, and the independence bound drops
because any independent set outside $N[v]$ can be augmented by $v$.

If instead $\delta(J)\ge r$ and $t>1$, delete one arbitrary vertex,
keeping $b$ unchanged. Its degree is at least $r$, so the potential
changes by at most $-2r+(2r-1)=-1$, and the surplus remains positive.

Repeat until $t=1$ and $\delta(J)\ge r$. Each step deletes vertices.
Reaching $b=0$ with positive order would already be a contradiction,
so a counterexample permits termination with $b\ge1$.
The original least color has a vertex of degree at most $r-1$, by
the Brooks argument in [Reductions](reductions.md). Thus the first
operation occurs and the terminal bound satisfies $b<r$.

At termination $|J|=rb+1$, and (4) is precisely

$$
2e(J)\le br(r-1)+r(r+1). \tag{6}
$$


## 2. Extracting an arbitrary minimal-ratio subgraph is safe

Choose an inclusion-minimal induced subgraph $H\subseteq J$ with
$|H|>r\alpha(H)$, and put $a=\alpha(H)$. Such a subgraph exists
because $|J|=rb+1>r\alpha(J)$.
Minimality implies (3), and deleting one vertex shows
$|H|=ra+1$. Also $a\le b$.

Put $k=b-a$ and $D=V(J)\setminus V(H)$, so $|D|=rk$.
Let $E_{\mathrm{inc}}$ count edges of $J$ with at least one endpoint
in $D$. The elementary identity

$$
2E_{\mathrm{inc}}
=\sum_{v\in D}d_J(v)+e_J(D,V(H))\ge r^2k
\tag{7}
$$

uses only $\delta(J)\ge r$. Therefore

$$
\Phi(H,a)-\Phi(J,b)
=-2E_{\mathrm{inc}}+r(r-1)k\le-rk\le0.
$$

This proves (2). In fact extraction gains $rk$ in the doubled edge
budget whenever $k>0$. It is unnecessary to bound the internal edge
count of the deleted set or restrict this operation to small $k$.

The graph $H$ is connected: otherwise a component would itself have
order greater than $r$ times its independence number. It has minimum
degree at least $r$, as also follows from the expansion below.

## 3. Expansion, stability, and the absence of full cliques

For every nonempty independent set $S\subseteq V(H)$,

$$
\boxed{|N_H[S]|\ge r|S|+1.} \tag{8}
$$

If the remaining induced graph is nonempty, use (3) and
$\alpha(H-N[S])\le a-|S|$; if it is empty, the bound follows from
$|S|\le a$ and $|H|=ra+1$.

Likewise, for every $D\subseteq V(H)$ with $|D|\le r$,

$$
\alpha(H-D)=a. \tag{9}
$$

For nonempty $D$, its remaining order is at least $r(a-1)+1$,
so (3) forces independence at least $a$.

A $K_r$ cannot occur in $H$. Its deletion would leave an independent
$a$-set by (9). Since $a<r$, that set excludes fewer than $r$
vertices of the clique, using the outside-neighbor bound for a target
$K_r$, and could be augmented. Thus $\omega(H)\le r-1$.

The localized independence inequality then yields

$$
2e(H)\ge\frac{2(ar+1)^2}{a}-r(ar+1)
=ar^2+3r+\frac2a.
$$

Comparing with (2) gives $r(r-a-2)\ge2/a$, hence $a\le r-3$. The
[cross-color core inequality](cross_color_cores.md) excludes $a=2,3$, while
$a=1$ is excluded by the local clique cap. This proves the earlier $a\le r-3$
range; the neighborhood matching and balanced-surplus argument in
[Core structure](minimal_core_structure.md) strengthens it to $a\le r-5$ as
recorded in (1).

## 4. Degree cost of overlapping neighborhoods

Set $s(v)=d_H(v)-r\ge0$. Equation (2) gives

$$
\sum_v s(v)\le r(r-a). \tag{10}
$$

For nonadjacent $x,z$ with $c$ common neighbors, (8) gives

$$
2+d_H(x)+d_H(z)-c\ge2r+1,
\qquad s(x)+s(z)\ge c-1. \tag{11}
$$

In particular, the nonadjacent pair in an induced $K_r-e$ costs at
least $r-3$ total degree surplus. If $M$ is any matching of nonedges
whose endpoint pairs each have at least $c_0>1$ common neighbors,
then

$$
|M|\le\frac{r(r-a)}{c_0-1}. \tag{12}
$$

The endpoints of a maximal such matching meet every such nonedge.
This gives a controlled deletion set for highly overlapping
nonadjacent pairs, but has not completed the near-full clique packing.

There is also an exact local-clique deficit budget. Writing
$D_c=\sum_v(r-c_H(v))$, the uniform localized inequality and (2) give

$$
D_c\le r^2-2r+1-\frac2a,
\qquad
D_c-|H|\le r(r-a-2)-\frac2a. \tag{13}
$$

Put $F=r-a-1\ge2$. If the clustering hypotheses in
[Large-clique clusters](large_clique_clusters.md) hold with $k=F$,
then fewer than $r$ vertices are outside all cliques of order at least
$r-F$: an uncovered vertex contributes at least $F$ above the baseline
deficit one, whereas (13) allows less than $(F-1)r$ total excess.
Since each cluster has at most $r$ vertices, there are at least $a$
clusters. If there are exactly $a$, the cluster-deficit summation from
that note gives $T\le r-3$; as all anchor deficits are positive,

$$
\sum_j(t_j-1)=T-a\le F-2. \tag{14}
$$


For the case $F=2$ (that is, $a=r-3$, which the neighborhood charge below also
excludes), the sharper
threshold $k=1$ already leaves at most $r-1$ uncovered vertices.
Every cluster of $K_{r-1}$'s is either a $K_{r-1}$ or a $K_r-e$:
two distinct anchors in a cluster have union of order $r$ and cover
all edges except their two omitted vertices' edge; that edge cannot
be present because $H$ is $K_r$-free.

Distinct such clusters intersect in at most one vertex. Otherwise
their intersection contains an edge, which merges their anchor
components, or both are $K_r-e$'s sharing their missing pair. The
latter union has $2r-2$ vertices and at least $r(r-1)-2$ edges,
exceeding $D_r(2r-2)=(r-1)^2$ for $r>3$. Finally any external vertex
has at most two neighbors in a $K_r-e$ cluster, directly from the
$(r+1)$-set cap. These exact types do not yet exclude the core; pure
$K_{r-1}$ clusters can still have highly concentrated outside
adjacencies.

## 5. Optional independence-critical pruning

Delete edges of $H$ as long as its independence number stays $a$.
Property (3) persists, because edge deletion only increases independence
numbers of induced subgraphs. The edge budget improves. Connectedness,
minimum degree, and (8)--(9) follow again from (3).

For retaining actual color coupling on these $ar+1$ vertices, assign
each deleted edge to any fixed other color. Its independence number
cannot increase; the distinguished color still has independence $a$.
Thus the resulting local complete-graph coloring has all the stated
independence bounds and inherited caps. No claim is made that this
recoloring is safe on the original $r^2+1$ vertices.

The final distinguished graph is connected and independence-critical.
This does **not** establish that it is $(r+1)$-chromatic-critical.
Applying Kostochka--Yancey directly to this entire graph is therefore
not justified. A chromatic-critical subgraph may be substantially
smaller, and no sufficient lower bound on its order has been proved.

## Remaining gap

No contradiction has been derived from (1)--(3), (8), and (10).
They provide a least-budget minimal-ratio core, not a universal
exclusion theorem or an infinite family of solved parameters.
Combining its pair-surplus charges with the near-full clique structure
is a provisional direction; no completion statement is asserted.

The normalization, arbitrary minimal-ratio extraction, expansion, and
optional local pruning were checked by the author and are
author-recorded. The distinction
between independence-critical and chromatic-critical is essential.

## Comparison with the independent minimal-core warning

Appendix E of the
[independent input](independent/small_independence_and_packing_obstructions.md)
correctly warns that the original least-color average-degree bound cannot simply
be inherited by an arbitrary minimal-ratio core. This does not contradict the
potential reduction above. What is transferred is $\Phi$, yielding

$$
2e(H)\le r|H|+r(r-a),
$$

not $2e(H)\le r|H|$. The positive degree-surplus allowance is
precisely why $\delta(H)\ge r$ does not imply regularity.

The failed sparse gadget already recorded in
[Construction attempts](construction_attempts.md) isolates this issue.
For $r\ge3$, take two disjoint $K_r$'s $A,B$, vertices $a\in A,b\in B$, add
$v$ adjacent to $(A\setminus\{a\})\cup(B\setminus\{b\})$, and
add the edge $ab$. The graph $H$ has order $2r+1$, independence
number two, and clique number $r$. It is a minimal-ratio core:
a proper induced set has order at most $2r$, and any such set
of order greater than $r$ is not a clique.
Every vertex except $v$ has degree $r$, while $d(v)=2r-2$.
Thus $2e(H)=r|H|+r-2>r|H|$.

Yet $G=H\sqcup(r-2)K_r$ has order $r^2+1$, independence number
$r$, and

$$
e(G)=\frac{r^3-r^2+4r-2}{2}\le\frac{r(r^2+1)}2.
$$

It fails the local cap, since $v$ has $r-1$ neighbors in the full
clique $A$. This is a counterexample only to the naïve budget
inheritance argument, not to the full hereditary system or the
coloring problem.
