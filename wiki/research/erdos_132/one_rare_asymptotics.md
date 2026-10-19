---
name: research/erdos_132/one_rare_asymptotics
title: Necessary asymptotic shape of a one-rare-distance family
desc: |
  A hypothetical unbounded R=1 family has a two-thirds outer-layer split,
  an exact triangular-lattice spectrum at every fixed short scale,
  and lattice minimum-distance components.
sources: []
research_state: closed
created: 2026-09-23T03:11:32Z
updated: 2026-09-24T22:12:56Z
---


# Necessary asymptotic shape of a one-rare-distance family

***

**New long-scale restriction.** The
[angular matching argument](long_rank_gaps.md) shows that every fixed $k$
satisfies $(\Delta-r_k)/\Delta=O_k(n^{-2})$ in such a sequence. This sharpens
the long-scale description but does not control the intermediate palette or
contradict the short lattice structure below.

**Subsequent strengthening.** The
[translated-triangle argument](translated_triangles.md) now shows that each
lattice orientation has only $O(n^{5/7})$ good centers, so there are
$\Omega(n^{2/7})$ orientations and no macroscopic minimum-distance component. It
also gives $\Omega(n^{9/14})$ exceptional interior vertices and minimum pairs
touching the outer two layers. These conclusions do not contradict the $o(n)$
errors below. A common lattice of mesh $\delta$ is excluded, and any common
finer triangular lattice must have superpolynomial refinement. Arbitrarily fine
lattices remain unexcluded. The
[quantitative short-incidence bound](quantitative_short_incidence.md) also
supplies complete patches of radius $c n^{1/112}(\log(2n))^{-1/14}$ at linearly
many centers.

This is a conditional consequence of the
[short-edge incidence inverse](short_incident_inverse.md), not a
contradiction or an answer to either unrestricted question.

Suppose $|A|=n\to\infty$ along a sequence with $R(A)=1$. Let $L_i$ be
its convex layers, $h=|L_1|$, $s=|L_2|$, $\delta$ its minimum distance,
and $r_2$ its second-largest distance. Then


$$
h+s=(2/3+o(1))n,\qquad
m_A(r_2)=m_A(\delta)+o(n)=(1+o(1))n, \tag{1}
$$


$$
(1/3-o(1))n\le h\le(1/2+o(1))n, \tag{2}
$$

and every subsequent fixed layer has $o(n)$ points. Furthermore, all
but $o(n)$ points of $I=A\setminus(L_1\cup L_2)$ have exactly six
minimum-distance neighbors in $I$.

## Proof of the layer proportions

Since the diameter is the unique rare distance, both $\delta$ and $r_2$
are rich for sufficiently large $n$. The distance count is at most $n/2$.
The inverse theorem and circle theorem imply that the number of
minimum-distance pairs touching any strictly convex subset is $o(n)$,
uniformly over that subset. In particular, for every fixed $j$,


$$
e_\delta(L_1\cup\cdots\cup L_j,A)=o(n). \tag{3}
$$


Here the expression counts unordered pairs with at least one endpoint
in the displayed union. Degenerate layers of size at most two cause no
problem, since minimum-distance degree is at most six.

Put $I_j=A\setminus(L_1\cup\cdots\cup L_j)$. The same degree bound gives


$$
n<m_A(\delta)\le 3|I_j|+o(n).
$$


Thus $|L_1\cup\cdots\cup L_j|\le(2/3+o(1))n$ for each fixed $j$.
On the other hand, the checked second-distance bound gives


$$
n<m_A(r_2)\le
\min\{\tfrac32(h+s),\ \tfrac43h+2s,\ 2h+s\}. \tag{4}
$$


The first term proves (1); the other two, after substituting $s=2n/3-h+o(n)$,
prove (2). Combining the $j=2$ equality with the upper bound for each larger
fixed $j$ proves the assertion about later layers. Bound (4) is Theorem 1.3 and
its proof in Section 2.2 of the [supplied Clemen--Dumitrescu--Liu
paper](../../../library/distance_problems/clemen_2025_multiplicities_interpoint_distances/_index.md),
whose full passage was checked. The $3/2$ bound also follows by applying
Vesztergombi's theorem to $L_1\cup L_2$.

## Exact local triangular-lattice structure

Set $I=I_2$, so $|I|=n/3+o(n)$. By (3),


$$
e_\delta(I)=m_A(\delta)-o(n)\ge n-o(n)=3|I|-o(n).
$$


Every vertex of this graph has degree at most six. Hence


$$
\sum_{p\in I}(6-\deg_{I,\delta}(p))=o(n).
$$


Only $o(n)$ vertices have degree less than six. At a degree-six vertex,
the six neighbors lie on its radius-$\delta$ circle, with consecutive
angular gaps at least $\pi/3$, because $\delta$ is the global minimum.
The gaps sum to $2\pi$, so they are all exactly $\pi/3$. The neighbors
therefore form a regular hexagon.

Call these vertices good. Each connected component of the graph induced
by the good vertices lies in one translated and rotated triangular
lattice of mesh $\delta$: along an edge joining two good vertices, the
two regular hexagonal direction sets agree, and this propagates along
paths. The lattices of different components need not agree.

There are only $o(n)$ such components. A finite component has a vertex
missing at least one of its six lattice neighbors inside the component
(maximize a generic linear functional). That neighbor exists in $I$,
because the vertex is good, and must be bad. Each bad vertex has at most
six neighbors. Charging a component to one such incidence bounds the
number of components by six times the number of bad vertices.
Consequently, for every fixed $M$, only $o(n)$ good vertices belong to
components of size at most $M$.

## Exact spectrum at every fixed short scale

Let $Q(a,b)=a^2+ab+b^2$ be the triangular-lattice norm. For every
fixed $L>0$, eventually along the hypothetical sequence,

$$D(A)\cap(0,L\delta]
=\delta\{\sqrt{Q(a,b)}:a,b\in\mathbb Z,\ 0<Q(a,b)\le L^2\}. \tag{5}$$

Thus this is exact equality of finite sets of lengths, not convergence
of their normalized numerical values. Moreover, for each fixed
represented $r>0$, put
$t(r)=|\{(a,b)\in\mathbb Z^2:Q(a,b)=r^2\}|$. Then

$$m_A(\delta r)=\left(\frac{t(r)}6+o(1)\right)n. \tag{6}$$

### Complete patches at most interior vertices

Let $B\subset I$ be the bad vertices, $b=|B|=o(n)$. In the internal
minimum-distance graph on $I$, remove the vertices at graph distance
at most $k$ from $B$. For fixed $k$, there are at most
$(1+6+\cdots+6^k)b=o(n)$ removed vertices. Denote the remaining set
by $H_k$.

At each $v\in H_k$, propagation of the six lattice directions along
good vertices gives a complete triangular-lattice graph ball of radius
$k$, contained in $I$. Choose $k\ge\lceil2L+2\rceil$. A nearest
point $z$ of that lattice to any $x\in\overline B(v,L\delta)$
is within $\delta/\sqrt3$ of $x$: the lattice's equilateral triangles
have circumradius $\delta/\sqrt3$. Moreover,
$|z-v|\le(L+1/\sqrt3)\delta$. In axial coordinates, the path
length $|a|+|b|$ is at most $2\sqrt{Q(a,b)}$, so $z$ lies in the
complete graph ball and belongs to $I$.

If $x\in A$, minimum separation forces $x=z$, since otherwise
$0<|x-z|\le\delta/\sqrt3<\delta$. Consequently
$A\cap\overline B(v,L\delta)$ is exactly the corresponding complete
lattice patch, and all its points lie in $I$.

### Excluding a first nonlattice length

Suppose a distance $d\le L\delta$ not on the right of (5) occurs,
and choose the least such distance. Its global smallest-distance rank
is at most $N_L+1$, where
$N_L=|\{Q(a,b):0<Q(a,b)\le L^2\}|$ is fixed. No $d$-edge can touch
$H_k$. The [short-edge inverse](short_incident_inverse.md) says that
the $d$-edges touching $L_1\cup L_2$ number $o(n)$, uniformly over
these bounded ranks. All other edges are among the $o(n)$ exceptional
interior vertices, whose $d$-degrees are at most $6(N_L+1)$.
Thus $m_A(d)=o(n)$.

Packing the disjoint radius-$\delta/2$ disks gives
$n\le(2\Delta/\delta+1)^2$, so $\Delta/\delta\to\infty$.
For large $n$ the distance $d$ is not the diameter and must be rich
under $R(A)=1$, a contradiction. Every lattice length on the right
of (5) occurs in the complete patches, since $H_k$ is nonempty.
This proves (5).

For a fixed represented $r$, each deep vertex has exactly $t(r)$
neighbors at distance $\delta r$, all in $I$. Exceptional interior
vertices have bounded degree, and the outer-layer incidences are
$o(n)$ by (5) and the fixed-short-rank inverse. Therefore
$2e_{\delta r}(I)=t(r)|I|+o(n)$; use $|I|=n/3+o(n)$ to obtain (6).
In particular, the classes at $\delta,\sqrt3\delta,2\delta$ each
have $n+o(n)$ pairs, and the class at $\sqrt7\delta$ has $2n+o(n)$.

## Entire minimum-distance components lie in lattices

Equation (5) with $L=2$ strengthens the earlier good-component statement.
Eventually **each connected component of the entire minimum-distance
graph on $A$** lies in one translated, rotated triangular lattice of
mesh $\delta$, including its bad vertices.

Indeed, on a two-edge path $x-y-z$ with $x\ne z$, (5) gives
$|x-z|^2/\delta^2\in\{1,3,4\}$. The two directed edges consequently
differ in direction by $0$, $\pm\pi/3$, or $\pm2\pi/3$.
Directions and lattice coordinates propagate along paths from a first
edge. Isolated points can be placed in any lattice of this mesh.
Separate components need not have the same lattice.

## Total diameter of good components

For a good component $S$, take its own axial lattice coordinates $a,b$.
Connectivity makes the occupied $a$- and $b$-values integer intervals.
The boundary incidences in directions $\pm e_1$ number at least
$2(\operatorname{span}b+1)$; those in directions $\pm e_2$ number
at least $2(\operatorname{span}a+1)$. Hence

$$|\partial S|\ge2(\operatorname{span}a+\operatorname{span}b+2)
\ge 2\operatorname{diam}(S)/\delta+4.$$

Every external lattice neighbor of a good vertex exists in $I$ and
is bad, since otherwise it belongs to the same good component.
Each bad vertex has at most six minimum-distance neighbors, so
$\sum_S|\partial S|\le6b$. It follows that

$$\sum_S\operatorname{diam}(S)\le3b\delta=o(n\delta). \tag{7}$$

The [linear-aspect-ratio theorem](layers_and_obstructions.md) further
gives $\Delta/(n\delta)\to\infty$. Thus these component diameters
also have sum $o(\Delta)$. This does not bound the separation of their
centers or force their lattices to agree.

The [long-core surplus argument](diameter_activity.md) additionally
forces $m_A(\Delta)\ge(1/6-o(1))n$. In particular, the remaining
asymptotic obstruction does not have only a bounded number of diameter
pairs.

## What is still missing

This does not prove that the triangular-lattice components share a
common lattice, that one component contains a positive fraction of all
points, or that their distance palette is incompatible with the two
outer layers. The $o(n)$ minimum-distance incidences on those layers
can still exceed the boundary deficit of a large lattice patch.
Replacing $o(n)$ by zero, or silently deducing a common lattice, would
invalidate the argument.

In (6), a six-vector shell has multiplicity $n+o(n)$, not necessarily
at most $n$. The error can still make every such shell rich. The
exact short spectrum and the diameter estimate (7) do not control
overlaps of the long pinned-distance spectra between the distributed
lattice components and the outer layers. That is the remaining palette
compatibility question, not a consequence of local lattice structure.

Nor does the first distance joining two minimum-graph components have
to create a new palette value. For a concrete example, take the two
triangular-lattice patches
$T_m=\{a+b\omega:a,b\in\mathbb Z_{\ge0},\ a+b\le m\}$ and $T_m+(m+2)$,
where $\omega=e^{i\pi/3}$ and $m\ge2$. Their minimum-distance
components are separate, their shortest cross-distance is two, and
distance two already occurs inside each patch. Bounding only the
cross-pairs therefore does not bound the full multiplicity of that class.
This example tests that inference, not the $R=1$ hypotheses.

Nor does near-extremality of $r_2$ on $L_1\cup L_2$ alone force a circular
fraction. The
[even-order deformation construction](second_distance_extremality.md) attains
exact $3N/2$ second-distance multiplicity with no five points concyclic. The
additional global bound $q(A)\le n/2$ has not been combined with extremality to
obtain the missing rigidity.

The reduction only applies to an unbounded sequence with $R=1$.
It neither excludes a single finite counterexample nor treats general
bounded $R>1$. The author checked the pair factors, degree-six
rigidity, component count, and full source bound against these precise
hypotheses; the argument is author-recorded. The exact bounded-window spectrum,
nearest-lattice exclusion, fixed-shell factors, eventual whole-component
propagation, and component-diameter bound were also checked by the author
and are author-recorded.
