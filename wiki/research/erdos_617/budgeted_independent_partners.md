---
name: research/erdos_617/budgeted_independent_partners
desc: The common least-color budget forces a disjoint partner for every maximum independent set and gives an exact, but incomplete, parameter descent.
tags: [graph-theory, proved, reductions, independent-sets]
sources: []
created: 2026-09-22T10:35:00Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/budgeted_independent_partners

***

**Proved consequences of the least-color budget, not a solution.**
These apply to both the [minimal-ratio core](minimal_ratio_potential.md)
and the [budgeted two-supported residue](critical_component_reduction.md).
They do not identify the two reductions or transfer their other hypotheses.

## Every maximum independent set has a disjoint partner

Suppose

$$
|H|=ar+1,\qquad \alpha(H)=a,\qquad 2\le a\le r,
\qquad 2e(H)\le ar(r-1)+r(r+1). \tag{1}
$$

Then, for every independent $a$-set $I$,

$$
\boxed{\alpha(H-I)=a.} \tag{2}
$$


Put $m=|H-I|=a(r-1)+1$. Every vertex outside $I$ has a neighbor
in $I$. If $\alpha(H-I)\le a-1$, the continuous complementary Turán
bound gives

$$
2e(H)\ge 2m+\frac{m^2}{a-1}-m
=m+\frac{m^2}{a-1}.
$$

But the difference between the budget in (1) and this lower bound is

$$
ar(r-1)+r(r+1)-m-\frac{m^2}{a-1}
=\frac{r(a-r-1)}{a-1}<0.
$$

This proves (2). Neither criticality nor hereditary caps were needed.

If $I$ is two-supported, represent private vertices by loops at their
anchor and exceptions by their two-element supports. A disjoint maximum
set $J$ supplied by (2) gives a spanning disjoint union of unicyclic
components in this support multigraph. Indeed every subfamily of its
supports satisfies Hall's condition: otherwise it and the unused anchors
augment $I$. Thus each connected component has at most as many edges as
vertices. There are exactly $a$ edges and $a$ available vertices, so every
component has equality and every anchor is covered.

This is a constraint on the supports of an independent partner, not a
claim that the full exception support graph is unicyclic.

## Criticality and two-support alone do not imply (2)

Here is a self-contained counterexample to that weaker claim. Start
with a triangle on $1,2,3$, replace its cyclically oriented edges
$12,23,31$ by paths $i,p_{ij},q_{ij},j$, and add a hub $0$ adjacent
to $1,2,3$. This ten-vertex graph has independence number four.
An independent set using the hub uses no original triangle vertex and
at most one internal vertex on each path. Without the hub, if it uses
$k$ original triangle vertices, it has size at most
$k+3-\binom k2\le4$.

Every edge is critical. Deleting a spoke allows the hub, its endpoint,
and one internal vertex from each of the three paths. Deleting an end
edge on the path from $i$ to $j$ allows $i,j$, the newly available
internal vertex on that path, and one internal vertex on each other
path. Deleting a middle edge allows its two internal endpoints, the
opposite original triangle vertex, and one internal vertex on each
other path. Each witness has size five.

The maximum set

$$
I=\{0,p_{12},p_{23},p_{31}\}
$$

is two-supported: each original triangle vertex has two neighbors in
$I$, and each $q_{ij}$ has one. Its deletion leaves precisely three
disjoint edges $q_{ij}j$, of independence three. Thus the budget in
(1) supplies an additional property, not a generic critical-graph fact.

## Exact anchor deletion and its missing induction hypothesis

Now assume $I$ is a maximum two-supported anchor set and $b$ outsiders
have two anchor neighbors. Then

$$
e(I,H-I)=a(r-1)+1+b.
$$

For $R=H-I$, equations (1)--(2) give

$$
|R|=a(r-1)+1,\qquad \alpha(R)=a,
$$


$$
\boxed{2e(R)\le
a(r-1)(r-2)+r(r-1)+2(r-b-1).} \tag{3}
$$

In particular $b\ge r-1$ supplies the formal least-color budget with
parameter $r-1$.

This is **not** an induction on $r$. Neither the parameter-$(r-1)$
hereditary caps nor two-support nor exclusion of $K_{r-1}$ has been
established for $R$.

When $I$ comes from a full component of a foreign color, there is a
valid asymmetric improvement. Deleting that whole foreign component
lowers its independence number to $r-1$, and $R$ lies in its complement.
Consequently, for every $W\subseteq R$,

$$
e(H[W])\le \binom{|W|}{2}
-(r-2)p_r(|W|)-p_{r-1}(|W|). \tag{4}
$$

The other $r-2$ foreign colors still have only their original independence
bound $r$. Replacing their terms in (4) by $p_{r-1}$ would be unjustified.

No light-anchor degree bound, bounded-exception conclusion for the
least color, or universal contradiction follows yet from (2)--(4).
