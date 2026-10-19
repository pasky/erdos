---
name: research/erdos_644/structural_reductions
desc: Linear-size trace cores, an exact graph relaxation, fractional restrictions, and obstructions to naive critical-kernel reductions.
tags: [proved, reductions, limitations]
sources: [tuza_1985_critical_hypergraphs_intersecting_set_pair_systems]
created: 2026-09-22T21:16:40Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/structural_reductions

***

These statements concern finite families and the at-most-$r$ local two-cover
condition. None proves the convergence asked for in Problem 644 or improves the
unrestricted $7k/8+O(1)$ upper bound. The later
[almost-core criteria](almost_cores.md) give sufficient reductions that do not
require retaining all original local covers.

## Passage to finite critical families

The compactness argument in §3.3 of
[first independent record](independent/fano_ground_set_and_coding_constructions.md)
is valid: if every finite subfamily of a family of finite sets has a transversal
of size at most an integer $t\ge0$, so does the entire family.

Induct on $t$, the case $t=0$ being immediate. For a nonempty family choose an
edge $A$. For $x\in A$, let $\mathcal H_x$ consist of edges missing $x$. If no
$\mathcal H_x$ has a $(t-1)$-point cover, induction supplies a finite
$\mathcal F_x\subseteq\mathcal H_x$ with no such cover. The finite family
$\{A\}\cup\bigcup_{x\in A}\mathcal F_x$ cannot have a $t$-point cover: choose
$x$ where a purported cover meets $A$ and remove it, obtaining a forbidden
$(t-1)$-point cover of $\mathcal F_x$. Otherwise a $(t-1)$-point cover of some
$\mathcal H_x$, together with $x$, covers the whole family.

Thus every positive finite transversal value $t$ is witnessed by a finite
subfamily, from which one may delete edges until it is $\tau$-critical. For a
$k$-uniform critical family, each edge $E_i$ has a $(t-1)$-point cover $T_i$ of
the other edges, disjoint from $E_i$. The checked set-pair inequality and
Theorem 17 in
[Tuza, §§2 and 4](../../../library/set_systems/tuza_1985_critical_hypergraphs_intersecting_set_pair_systems/_index.md)
give

$$
|\mathcal H|\le\binom{k+t-1}{k},\qquad
\left|\bigcup\mathcal H\right|<\binom{k+t}{k}.
$$

These are exponential bounds when $t=\Theta(k)$, not linear kernels or scaling
statements. The parameter must be the actual transversal number, not merely the
size of a supplied set-pair certificate; see
[Exterior transversal model](exterior_transversal_model.md).

The finite-witness proof and critical bounds in §§2.4 and 7.1 of
[second independent record](independent/fractional_reductions_and_good_triples.md)
agree with these arguments. Its statement that ISP completion was not shown to
preserve locality is superseded by the explicit failure in
[Exterior transversal model](exterior_transversal_model.md): Tuza's Construction
15 can complete a star to a complete graph containing a bad six-edge $K_4$,
while retaining uniformity. Formal certificate completion is therefore not a
general $P_7$ reduction.

## A linear-size trace core

Let $\mathcal H$ have rank at most $k$ and transversal number $t\ge2$. There are
at most

$$
q=1+\left\lceil\frac{k}{t-1}\right\rceil
$$

edges with empty common intersection. Indeed, partition one edge $A$ into at
most $q-1$ parts of size at most $t-1$, and choose an edge avoiding each part.

Remove repetitions from these references, obtaining $A_1,\ldots,A_{q'}$,
$q'\le q$. Suppose $q'<r$, and let $U=\bigcup_i A_i$. Then $|U|\le q'k$. Every
pair covering the references lies in $U$: an outside point covers none, and
their common intersection is empty.

Define a graph $G$ on $U$ whose edges are precisely those pairs covering all
references. Its incidence classes are

$$
V_I=\{x:\{i:x\in A_i\}=I\},\qquad
\varnothing\ne I\subsetneq[q'].
$$

The graph is a blow-up of a fixed graph with adjacency $I\sim J$ exactly when
$I\cup J=[q']$; there are no edges inside a class. Also

$$
\sum_{I\ni i}|V_I|=|A_i|\le k.
$$


Every at-most-$(r-q')$-tuple of traces $E\cap U$, $E\in\mathcal H$, is covered
by an edge of $G$, by adjoining the references and applying the original local
property. Moreover,

$$
\tau(\mathcal H|_U)\ge t.
$$

Thus a positive linear transversal number gives an $O(k)$-vertex, bounded-type
trace problem, but at the cost of weakening the local parameter. For $r=7$ and
$t>(k+1)/2$, three references suffice.

**Gap.** The trace family need not retain the original $(r,2)$ property.
Restoring it is not a routine consequence of this reduction.

## The unrestricted graph relaxation is exactly a static covering problem

For a nonempty graph $G$ on $n$ vertices, put

$$
b_s(G)=\min\left\{\max_i|S_i|:
E(G)\subseteq\bigcup_{i=1}^sE(G[S_i])\right\}.
$$

The largest possible transversal number of an arbitrary family $\mathcal F$ on
$V(G)$ such that every at-most-$s$ members are covered by an edge of $G$ is
exactly $b_s(G)$.

For the upper bound, if $\tau(\mathcal F)>b_s(G)$, choose $F_i\in\mathcal F$
disjoint from $S_i$. Each edge of $G$ is contained in some $S_i$ and therefore
misses $F_i$, contradiction.

For equality, take all $(n-b_s(G)+1)$-subsets. This family has transversal
number $b_s(G)$. A bad $s$-tuple would have complements of size $b_s(G)-1$ whose
induced subgraphs cover $E(G)$, contradicting the definition.

For blow-ups of a fixed finite graph, this parameter has a finite rational
linear-program description up to $O(1)$. Assign to each vertex the subset of
$[s]$ indexing the $S_i$ containing it. Support families assigned to adjacent
classes must cross-intersect. For each of finitely many choices of support
families, class-size and coordinate-load constraints form an LP. Rounding within
each class costs $O_{s,d}(1)$, where $d$ is the number of classes.

**Gap and useful distinction.** The equality construction has rank $n-b_s(G)+1$,
which can exceed the original allowed rank $k$. For example, a balanced good
reference triple with pair classes of size $.35k$ has union size $1.95k$. The
certificate in [the earlier notes](certificates_and_obstructions.md) gives
$b_4(G)\le.81k+O(1)$, so the unrestricted equality construction has rank at
least $1.14k-O(1)$. The static relaxation therefore discards potentially
essential rank information.

## Fractional restrictions

Write $z=\tau^*(\mathcal H)$ for the fractional transversal number. Universally,

$$
\tau(\mathcal H)\le k(z-1)+1.
\tag{1}
$$

To see this, choose the $t-1$ largest weights of an optimal fractional cover,
where $t=\tau(\mathcal H)$, and choose an edge avoiding those vertices. Its
weight is at least one, and each selected vertex has weight at least the largest
weight on that edge, hence at least $1/k$. The two disjoint contributions give
$z\ge1+(t-1)/k$.

For a $P_7$ family, the sparse-triple certificate gives a second bound.
Normalize an optimal fractional matching of total weight $z$ to a distribution
on edges. Its point probabilities satisfy $p_v\le1/z$ and $\sum_vp_v\le k$. For
three independent samples, let $S$ be the points occurring at least twice. If
$z\ge4/3$, then

$$
\mathbb E|S|=\sum_v(3p_v^2-2p_v^3)
\le k(3/z-2/z^2),
$$

because $3p-2p^2$ is increasing for $p\le3/4$. Applying the sparse-triple
certificate to a realization at most this expectation gives

$$
\tau(\mathcal H)\le k(3/z-2/z^2)+\lceil k/3\rceil.
\tag{2}
$$

Consequently an asymptotic counterexample with coefficient bounded above $3/4$
would require $z$ bounded away from both endpoints of

$$
\frac74\le z\le\frac{18+2\sqrt{51}}5.
$$

This is a bounded fractional-cover reduction, not a proof of the conjecture.

More generally, set $s=\lceil r/2\rceil$. Every rank-$k$ family with the local
property satisfies

$$
\tau^*(\mathcal H)\le W_r(k):=
\left(\binom rs k\right)^{1/(s-1)}.
\tag{3}
$$

For a fractional matching of total weight $W$, let $d_v\le1$ be the weighted
degree. Sample $r$ edges independently from its normalized distribution. A
two-cover forces some $s$ sample positions through one point. For a fixed
$s$-tuple of positions, this has probability at most

$$
\sum_v(d_v/W)^s\le k/W^{s-1}.
$$

A union bound proves (3).

The same argument with uniform sampling proves that each nonempty subfamily has
a vertex meeting at least a $1/W_r(k)$ proportion of its edges. Greedy covering
yields, for $M=|E(\mathcal H)|$,

$$
\tau(\mathcal H)\le\lceil W_r(k)\log M\rceil+1.
$$

In particular, at $r=7$, linear transversal number requires
$M\ge\exp(\Omega(k^{2/3}))$. A polynomial-size **edge** kernel cannot preserve a
positive normalized transversal number. This does not exclude the trace-core
**vertex** reduction above.

**Comparison with the second record.** Its §§3.1 and 3.3 reproduce (1) and (2),
since $\lfloor(k+2)/3\rfloor=\lceil k/3\rceil$; they do not tighten the
fractional interval. Its projective four-space example correctly rules out a
bound on $\tau^*$ **independent of $k$**, not the rank-dependent bound (3). The
later [moment deletion theorem](incidence_moment_rounding.md) finds a residual
with $\tau^*\le Z$ after deleting at most $\lfloor20k/Z^2\rfloor$ vertices. This
is different from retaining only high-weight vertices: neither it nor the valid
sufficient threshold $\tau^*<7/4$ in
[Complete families](complete_families.md#equivalent-fractional-formulations)
supplies the missing local-property-preserving small core. The
[indispensable-core examples](indispensable_local_cores.md) disprove such
retention in general even at the boundary ratio, while
[almost-cores](almost_cores.md) gives deletion-tolerant conditional
alternatives.

## Disconnected families

A $P_7$ family's edge-intersection graph has at most two components. If it has
two, every at-most-six edges of either component have a common point: adjoin an
edge from the other component, which is disjoint from all of them, and apply
$P_7$.

A rank-$k$ family whose every at-most-$u$ edges intersect has transversal number
at most $\lceil k/(u-1)\rceil$. Otherwise partition one edge into $u-1$ parts of
that size and choose one edge avoiding each part, contradicting the intersection
property. Hence disconnected $P_7$ families satisfy

$$
\tau(\mathcal H)\le2\lceil k/5\rceil.
$$

If the edges avoiding a set $T$ have disconnected intersection graph, the same
argument gives $\tau(\mathcal H)\le|T|+2\lceil k/5\rceil$.

### Why low-cost separators do not split near-extremal demand

A proposed new approach was to split a high-transversal family using balanced
separators in its edge-intersection graph, measuring the separator by its
transversal cost rather than its number of edges. The following obstruction
prevents such a split at sublinear cost.

Put $d=\lceil k/5\rceil$ and $t=\tau(\mathcal H)$. For an edge $E$, let
$\mathcal D_E$ be the subfamily disjoint from $E$. Every at-most-six members of
$\mathcal D_E$ intersect: adjoin $E$ and apply $P_7$; one point of the two-cover
must meet $E$, and the other covers all the disjoint edges. Consequently
$\tau(\mathcal D_E)\le d$ by the six-wise-intersection bound.

For any prescribed edges $E_1,\ldots,E_q$, let $\mathcal C$ consist of the edges
meeting every $E_i$. Its complement is contained in $\bigcup_i\mathcal D_{E_i}$,
giving

$$
\boxed{\tau(\mathcal C)\ge t-qd.}
\tag{S1}
$$

In particular, if $t>2d$, any two disjoint edges have a common neighbor in the
edge-intersection graph. Thus that graph has diameter at most two, strengthening
the earlier connectivity conclusion.

If deleting a subfamily $\mathcal Q$ separates this graph into two nonempty
components, choose edges $E,F$ in different components. Every edge meeting both
must belong to $\mathcal Q$. Formula (S1) therefore gives

$$
\tau(\mathcal Q)\ge t-2\lceil k/5\rceil.
\tag{S2}
$$

More generally, after deleting all edges hit by a vertex set $S$ and
additionally deleting a subfamily $\mathcal D$, the residual still has diameter
at most two whenever

$$
|S|+\tau(\mathcal D)<t-2\lceil k/5\rceil.
$$

Indeed its transversal number remains greater than $2d$, and it inherits $P_7$.

At $t=(3/4+o(1))k$, any such separating operation costs at least $(7/20-o(1))k$.
Thus even removing arbitrarily many edges of collective transversal number
$o(k)$ cannot supply the proposed separator. This rules out that decomposition
mechanism, not all decompositions or convergence arguments. It does not
establish a new upper coefficient.

## Criticality plus domination removal does not bound the ground set linearly

There are $\tau$-critical $P_7$ families of rank $K$, with no dominated
vertices, exponentially many vertices, and $\tau/K\to3/4$. Here a vertex is
dominated if all edges containing it also contain another fixed vertex.

Take $k=12s$, $n=21s-1$, and all $k$-subsets of an $n$-point base set. This is
$P_7$ and has transversal number $t=9s$. Partition $21s-3$ base points into
$7s-1$ triples, and rotate each triple cyclically at the same time. The $k$-sets
selecting two points from exactly $6s$ triples form

$$
3^{6s}\binom{7s-1}{6s}
$$

sets. They split into orbits of length three, each with empty triple
intersection.

For each orbit add one new vertex to exactly its three edges. Pad every other
edge with its own private vertex. This gives a $(k+1)$-uniform $P_7$ family,
since the original base-point covers still work.

Its transversal number remains $t$. A proposed cover with $r$ base points and
$q$ new points, $r+q\le t-1$, leaves at least

$$
\binom{n-r}{k}\ge\binom{k+q}{k}>3q
$$

base edges untouched by the base points; the new points cover at most $3q$ of
them. The inequality is immediate for $q=0$, and for $q\ge1$ follows already
from $k\ge3$. Conversely, any original $t$-point cover still works.

The family is $\tau$-critical: for an edge based on $E$, the original complement
of $E$ has size $t-1$, misses that edge, and meets every other edge.

Now delete the private padding vertices, but retain the orbit vertices. This
leaves rank at most $K=k+1$, preserves $P_7$ using the original covers, and
preserves $\tau=t$ and criticality. No orbit vertex is dominated by a base
vertex, because its three supporting edges have empty base intersection;
different orbit vertices support disjoint edge triples. No base vertex is
dominated by another base vertex or an orbit vertex, since its original
complete-family incidence set has more than three members and separates every
other base point.

Thus the remaining rank-$K$ family is domination-reduced and still has
exponentially many vertices. The ratio $t/K=9s/(12s+1)$ tends to $3/4$. This
rules out the proposed reduction by criticality and domination alone, not
subtler reductions: deleting all the new vertices in this example recovers its
small base ground set.

## Limits of the anchored rank-aware game

After fixing references, a query of a set $T$ of size at most $t$ produces an
edge avoiding it. On a ground set of size $n$, a rank-$k$ response must exclude
at least $n-k$ points. This extra exclusion can help beyond a static
certificate, but it can also be wasted on isolated vertices of the current
pair-cover graph.

More precisely, put $\delta=n-k-t\ge0$. If isolated ground mass is at least
$\delta$, an adversary can choose each future exclusion to have active mass at
most $t$: first use available isolated points outside $T$, and if these are
insufficient use all isolated points, leaving active mass at most
$n-k-\delta=t$. A successful continuation with $s$ such responses would then
give an ordinary static $s$-cover of the current graph. This only obstructs this
particular game strategy.

Maximizing the sum $S$ of the three pair-intersection sizes does give extra
information. With $P_i=A_j\cap A_l$ and $Q_i=A_i\setminus(A_j\cup A_l)$ for a
good triple, put $p_i=|P_i|$. If an edge $E$ avoids $P_i$ and $t-p_i$ points of
$Q_i$ (when that many points are available), then

$$
|E\cap(A_1\cup A_2\cup A_3)|\le k-t+p_i.
$$

Indeed, $(A_j,A_l,E)$ is good, so maximality bounds its intersection with
$A_j\triangle A_l$ by $S-p_i$; the remaining part in $Q_i$ has size at most
$k-S+2p_i-t$.

A simple lexicographic refinement does not force improvement after every
response. At $k=8$, take disjoint atom sizes

$$
(|P_1|,|P_2|,|P_3|)=(4,3,2),\qquad
(|Q_1|,|Q_2|,|Q_3|)=(3,2,1).
$$

Request avoidance of $P_1$ and two points of $Q_1$. Let $E$ consist of the
remaining point of $Q_1$, all of $P_2\cup Q_2$, and two fresh points. The new
good triples have sorted pair-size vectors $(4,3,2)$ and $(4,2,2)$; the third
new triple is not good. None improves the original key
$(S,\text{largest pair},\text{middle pair})=(9,4,3)$. This is not a
counterexample family to Problem 644, only an obstruction to that proposed
one-step potential argument.

## Uniform rank does not repair the anchored relaxation

The loss of three local edges in the trace-core reduction is essential even if
the traces remain uniform and contain the reference edges. Here is an explicit
asymptotic example of the relaxation, not of $P_7$.

Fix $m\ge1$. Take disjoint classes $P_1,P_2,P_3,Q_1,Q_2,Q_3$ with

$$
|P_i|=7m,\qquad |Q_i|=3m,
$$

and let $U$ be their union. Put $k=17m$ and

$$
A_i=P_j\cup P_l\cup Q_i\qquad(\{i,j,l\}=\{1,2,3\}).
$$

This is a good triple. Let $G$ be its pair-cover graph, with complete bipartite
pieces $P_i\times P_j$ for $i\ne j$ and $P_i\times Q_i$.

**Claim.** Four sets of size at most $13m$ cannot cover all edges of $G$ by
their induced subgraphs.

Suppose they could, and give each point the support in $[4]$ of the sets
containing it. Supports at adjacent vertices must intersect. Every support is
nonempty because every vertex has a neighbor. A $P_i$-point cannot have
singleton support: all its $17m$ neighbors would have to lie in one of the sets
of size at most $13m$. Thus the total incidence count has the form

$$
2(21m)+9m+h=51m+h,
$$

where $h\ge0$ counts the incidences beyond two at $P$-points and beyond one at
$Q$-points. The four capacity bounds give $h\le m$.

Each $P_i$ has a point of support size two, since otherwise it alone would
contribute $7m$ to $h$. Two disjoint two-element supports cannot occur within
one $P_i$: every $Q_i$-point would have to meet both supports, contributing at
least $3m$ to $h$. Two-element supports from different $P$-classes intersect by
adjacency. Therefore all two-element supports at $P$-points form a
pairwise-intersecting family of edges on $[4]$. Such a family is contained in a
star or a triangle.

In the star case its center occurs at every $P$-point except possibly those with
support size at least three. There are at most $h$ exceptions, giving center
load at least $21m-h\ge20m>13m$.

In the triangle case, let $a$ be the missing coordinate. A $P$-point whose
support contains $a$ has support size at least three, so its incidence at $a$
costs at least one unit of $h$. For a $Q_i$-point containing $a$, choose a
two-element support occurring in $P_i$. That support avoids $a$, so the
$Q_i$-point's support has another coordinate and likewise costs at least one
unit of $h$. Hence the load at $a$ is at most $h$. The other three loads have
sum at least $51m$, exceeding their combined capacity $39m$. This contradiction
proves the claim.

Now let $\mathcal F=\binom U{17m}$. It contains all three reference edges and
has

$$
\tau(\mathcal F)=13m+1>\frac34(17m).
$$

Nevertheless, every at-most-four members of $\mathcal F$ are jointly covered by
an edge of $G$. Otherwise their complements, each of size $13m$, would cover all
$G$-edges by induced subgraphs, contrary to the claim. Equivalently, adjoining
the three fixed references to any four members always gives a two-point
transversal.

Thus the rank constraint, the reference triple, and this anchored local-four
condition do not imply the desired three-quarter bound. Additional information
is necessary. The example does not exclude a method exploiting the full
unanchored $P_7$ condition or a choice of reference triple maximizing its total
pair-intersection: the displayed reference triple is not such a maximizer in
$\mathcal F$. To make the distinction explicit, when $m=4q$ the family
$\mathcal F$ contains the seven Fano-cap blowups with classes of size $17q$:
these are $68q$-sets on $119q$ of the $120q$ ground points and have no two-point
transversal. In particular, $\mathcal F$ is not a counterexample to Problem 644.

## A two-response inequality for a maximal good triple

Choose a good triple maximizing $S=p_1+p_2+p_3$ among ordered triples with empty
intersection, allowing repetitions. Let $U$ be its union. Suppose $E_i$ avoids
$P_i\cup Q_i$. For $j\ne i$, put

$$
d_{ij}=|P_j\setminus E_i|,\qquad
g_{ij}=|Q_j\cap E_i|,\qquad
r_i=\sum_{j\ne i}d_{ij},\qquad X_i=E_i\setminus U.
$$

The triple $(A_j,A_\ell,E_i)$ is good, where $\{i,j,\ell\}=[3]$. Its total pair
intersection is

$$
p_i+(p_j+p_\ell-r_i)+\sum_{j\ne i}g_{ij}
=S-r_i+\sum_{j\ne i}g_{ij}.
$$

Maximality and the row-size identity $k=p_j+p_\ell+q_i$ give

$$
\sum_{j\ne i}g_{ij}\le r_i,
\qquad |X_i|=q_i+r_i-\sum_{j\ne i}g_{ij}.
\tag{M1}
$$


Suppose in addition that $E_j$ avoids $P_j\cup Q_j$ and
$E_i\cap E_j\cap Q_\ell=\varnothing$. Then $(A_\ell,E_i,E_j)$ is good. With

$$
z_\ell=|(P_\ell\setminus E_i)\cap(P_\ell\setminus E_j)|,
$$

its pair intersections are

$$
\begin{aligned}
|A_\ell\cap E_i|&=p_j-d_{ij}+g_{i\ell},\\
|A_\ell\cap E_j|&=p_i-d_{ji}+g_{j\ell},\\
|E_i\cap E_j|&=p_\ell-d_{i\ell}-d_{j\ell}+z_\ell+|X_i\cap X_j|.
\end{aligned}
$$

The last equality holds because the common trace on $U$ lies entirely in
$P_\ell$. Summing and applying maximality proves

$$
|X_i\cap X_j|
\le r_i+r_j-g_{i\ell}-g_{j\ell}-z_\ell.
\tag{M2}
$$


These are exact constraints, not a closed seven-edge argument. The remaining
difficulty is that omissions from the $P$-classes can be offset by gains in the
$Q$-classes without decreasing $S$. Excluding those gains to make mixed triples
good consumes part of the same avoidance budget. No bound completing that
tradeoff at $\tau>3k/4+o(k)$ was obtained. The separate extremal-pair
certificate is recorded in
[Certificates and obstructions](certificates_and_obstructions.md).

## An adaptive obstruction for full-atom response queries

The following finite construction excludes one precise use of maximality. It is
**not** a $P_7$ counterexample: the seven constructed edges have a two-point
transversal. It shows that the four queried avoidance consequences alone do not
finish the argument.

Put $k=40m$ and $t=30m$. Take disjoint atoms

$$
|P_i|=16m,\qquad |Q_i|=8m,\qquad
A_i=P_j\cup P_\ell\cup Q_i.
$$

The reference triple is good and has pair-intersection sum $48m$. Suppose a
procedure successively chooses arbitrary, possibly adaptive queries

$$
T_i\supseteq P_i\cup Q_i,\qquad |T_i|\le30m
\quad(i=1,2,3),
$$

and receives a $40m$-set $E_i$ avoiding each query. It then makes one further
arbitrary query of size at most $30m$. There are responses preserving the
original triple's maximality, even under lexicographic refinement by its three
pair sizes, for which the final seven edges still have a two-cover.

For the first three responses, set

$$
D_i=T_i\cap(P_j\cup P_\ell),\qquad r_i=|D_i|\le6m.
$$

Choose a fresh set $X_i$ of size $8m+r_i$, disjoint from the query and every
preceding edge, and answer

$$
E_i=((P_j\cup P_\ell)\setminus D_i)\cup X_i.
$$

These choices work against adaptive queries. Among the first six edges, all
pairs intersect. A triple containing both $A_i,E_i$ has nonempty intersection
with any third distinct edge: the relevant $P$-atom retains at least
$16m-12m=4m$ points. Thus good triples use three different indices. Each pair
intersection in such a triple is contained in its corresponding $16m$-point
atom. The original triple maximizes their sum, and every maximizing triple has
pair-size vector $(16m,16m,16m)$.

Let $H_i=P_i\cap E_j\cap E_\ell$, which has size at least $4m$. The points
participating in two-covers of these six edges are exactly

$$
W=\bigcup_i\bigl(P_i\setminus(D_j\cap D_\ell)\bigr).
$$

Indeed, pairs of type $P_i\times Q_i$ fail on $E_i$. If a point $x\in P_i$
belongs to $E_j$, any point of $H_j$ completes it to a two-cover. A point of
$P_i$ belonging to neither other response cannot participate. Points outside the
$P$-atoms cannot participate either, by the original reference triple and the
exclusion of its $P_i\times Q_i$ pairs. Hence

$$
|W|\ge48m-\frac12\sum_i r_i\ge39m.
$$

The final $30m$-point query leaves some $v\in W$. Answer with $v$ and $40m-1$
fresh points. A two-cover through $v$ now covers all seven edges.

Maximality still holds. Any good triple of three distinct edges involving the
final response has pair sum at most $32m+1$: old pair intersections have size at
most $32m$, and goodness prevents $v$ from belonging to both other edges. A good
triple with a repeated edge has sum $40m$. Both are below $48m$.

Thus this fixed-reference strategy cannot prove the three-quarter bound.
Different query shapes, replacing references after further selections, and
additional consequences of global transversal number remain outside this
obstruction.

## A Fano-defect minimization formulation

This is an exact formulation and a limitation of one proposed inference, not an
upper-bound proof. Fix a Fano plane on the seven row indices, let its seven
complementary caps be $C$, and put

$$
d(S)=|S|-\max_C|S\cap C|\qquad(S\subseteq[7]).
$$

Thus $d(S)$ is the fewest incidences that must be removed from spectrum $S$ to
leave a subset of a cap. It is nonnegative and monotone, and adding one row
increases it by zero or one.

For a finite $k$-uniform family, choose an ordered seven-tuple of edges,
allowing repetitions, minimizing

$$
D=\sum_v d(S_v),\qquad S_v=\{i:v\in E_i\}.
$$

One has $D\le3k$ by repeating one edge seven times. If the family has $P_7$,
then $D\ge1$: when $D=0$, every point spectrum is contained in a Fano cap, and
two caps never cover all seven rows.

For row $i$, define

$$
W_i=\{v:d((S_v\setminus\{i\})\cup\{i\})-d(S_v\setminus\{i\})=1\},
\quad g_i=|E_i\cap W_i|,\quad h_i=|W_i\setminus E_i|.
$$

Points outside the tuple's union do not belong to $W_i$. Replacing row $i$ by an
edge $E$ changes the defect to $D-g_i+|E\cap W_i|$. Minimality therefore gives

$$
\min_{E\in\mathcal H}|E\cap W_i|=g_i.
$$

If $g_i>0$, every $(|W_i|-g_i+1)$-subset of $W_i$ is a transversal, so

$$
\tau(\mathcal H)\le h_i+1.
\tag{E1}
$$

No argument has forced an activated row with $h_i\le3k/4+o(k)$ under the
required high-transversal hypothesis.

An unconditional version of that assertion is false. Take two disjoint $k$-sets
$A,B$ as the entire family. A tuple assigns spectrum $S$ to all points of $A$
and $S^c$ to all points of $B$, so its defect is $k(d(S)+d(S^c))$. This has
minimum $k$, attained whenever $2\le|S|\le5$. To check this, complementary
spectra cannot both lie in caps, and every five-set contains a cap; for a
three-set, being a Fano line is equivalent to its complementary four-set being a
cap. At any minimizing tuple, an activated row has $g_i=k$. Replacing it by the
other edge cannot lower the defect, so all points of that other edge also lie in
$W_i$. Hence $h_i=k$ for every activated row, regardless of the choice of
minimizing tuple or Fano orientation. This example has $\tau=2$; it does not
refute an inference using $\tau>(3/4+\varepsilon)k$.

There is also an exact necessary finite-pattern relaxation. For a nonempty row
set $I$ contained in a Fano cap, define

$$
q_I(S)=d((S\setminus I)\cup I)-d(S\setminus I),
\qquad
G_I=\sum_v[d(S_v)-d(S_v\setminus I)].
$$

Here $q_I(S)\in\{0,1,2,3\}$ and $q_I(\varnothing)=0$. Replacing all rows in $I$
by the same edge shows

$$
G_I\le\min_{E\in\mathcal H}\sum_{v\in E}q_I(S_v).
$$

For an integer $0\le t<\tau(\mathcal H)$, choose an edge avoiding the $t$ points
with largest positive $q_I$ weights (or all positive-weight points if fewer
exist). Consequently

$$
G_I\le\max_{j=0,1,2,3}
\left\{\sum_v\min\{q_I(S_v),j\}-tj\right\}.
\tag{E2}
$$

The right side is precisely the total weight left after removing the $t$ largest
weights. Together with the seven row-size equations and $1\le D\le3k$, these are
necessary conditions on the 127 nonempty spectrum counts. Permuting rows
supplies further necessary comparisons with the other labeled Fano planes. The
following explicit feasible family shows that these conditions, even with the
indicated additional comparisons, do not prove the desired bound.

### An explicit feasible obstruction to the static relaxation

Identify the rows with the nonzero vectors of $\mathbb F_2^3$. Of their 35
triples, call the 28 non-lines triangles. Take $a$ points of spectrum $S$ for
every triangle $S$, and $u$ points of spectrum $[7]$, where $a,u$ are positive
integers and $u\le8a$. Every row has size

$$
k=12a+u,
\qquad D=3u.
$$

Here each row lies in twelve triangles, and every triangle is contained in a
cap.

This tuple minimizes the defect among **all** tuples obtained by replacing rows
with its existing rows, for every Fano orientation. Indeed, for any map
$f:[7]\to[7]$ and any Fano plane $F'$, the resulting defect is

$$
3u+a\sum_{S\text{ a triangle}}d_{F'}(f^{-1}(S))\ge3u.
$$

The universal class always contributes $3u$, and equality holds for the original
tuple and orientation.

For (E1), every row has $g_i=u$ and $h_i=12a$. Put $t=12a$. For cap-contained
$I$, the numbers of triangle spectra at the respective $q_I$ weights are as
follows; multiply the three count columns by $a$.

$$
\begin{array}{c|rrr|c|c}
|I|&q=0&q=1&q=2&q_I([7])&G_I\\ \hline
1&16&12&0&1&u\\
2&8&20&0&2&2u\\
3&4&21&3&2&2u\\
4&4&12&12&2&2u
\end{array}
$$

For triangles, $q_I(S)=d(S\cup I)$. A singleton belongs to twelve triangles, and
four other triangles complete it to a cap. A pair belongs to two caps, producing
eight zero-weight triangles. A triangle belongs to one cap, giving four zeros;
its complementary noncap four-set contains exactly three triangles, giving the
three weight-two cases. For a cap $I$, four triangles lie in $I$, twelve have
exactly one point outside $I$, and twelve have two points outside. These
observations verify the table.

After deleting the $t=12a$ largest weights, the remaining total weights are,
respectively,

$$
u,\qquad8a+u,\qquad12a+u,\qquad12a+2u.
$$

They are at least $G_I$ when $u\le8a$, so all (E2) inequalities hold. Their
remaining positive supports have sizes $u,8a+u,12a+u,12a+u$, respectively, all
at most $k$. Thus imposing the further rank-aware condition of retaining only
the $k$ largest remaining weights does not exclude this example either.

For instance, $a=19,u=72$ gives $k=300,t=228$, so the relaxation is feasible at
$t/k=0.76$. Taking $u=1$ and $a\to\infty$ makes its feasible ratio tend to one.

The actual seven-edge family has a common point and transversal number **one**.
This is only an obstruction to the static necessary inequalities, not a
counterexample to Problem 644 or to arguments using residual families after
deleting the universal class.
