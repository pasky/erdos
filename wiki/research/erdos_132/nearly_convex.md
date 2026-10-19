---
name: research/erdos_132/nearly_convex
title: Two rare distances in nearly convex sets
desc: |
  The first assertion holds with n minus one points strictly convex,
  and at even order with n minus two, using the circular extension theorem.
sources: []
research_state: closed
created: 2026-09-23T01:15:00Z
updated: 2026-09-24T22:12:56Z
---


# Two rare distances in nearly convex sets

***

**Proposition.** Let $n\ge5$. If $A$ contains an $(n-1)$-point subset
in strictly convex position, then $R(A)\ge2$.

The convex subset need not consist of all hull vertices of $A$.
This is a restricted result, not the unrestricted first assertion
of [Problem 132](../../problems/distance_problems/E0132/_index.md).

Use the checked [small-order theorem](small_orders.md) for $5\le n\le10$,
and assume $n\ge11$. If $R(A)=1$, its sole rare class is the diameter.
Writing $q=q(A)$ gives

$$\binom n2\ge1+(q-1)(n+1),\qquad q\le\lfloor n/2\rfloor. \tag{1}$$

For even $n$ and $q=n/2$, equality forces a unique diameter pair
and multiplicity exactly $n+1$ for every other class.

Let $H=A\setminus\{p\}$ be strictly convex. We use precisely Theorems 1--2 of
the supplied
[Fishburn paper](../../../library/distance_problems/fishburn_1995_convex_polygons_few_intervertex_distances/_index.md):
an odd convex $v$-gon with $(v-1)/2$ distances is regular; for even $v\ge8$, a
convex $v$-gon with $v/2$ distances is regular or a regular $(v+1)$-gon minus
one vertex. The digest and these full-source statements were checked; no
near-minimum classification is assumed.

If $n$ is odd, Altman's bound and (1) force $q(H)=(n-1)/2$.
The even-order classification makes $H$ concyclic. This contradicts
the [all-but-one-circle theorem](circular_configurations.md), which
gives two rare distances in the full set $A$.

If $n$ is even and $q\le n/2-1$, then $q(H)=(n-2)/2$ by Altman's
bound. Its odd equality case makes $H$ regular, giving the same
contradiction.

Finally suppose $n$ is even and $q=n/2$, with unique diameter pair
$ab$. If $p$ is one of $a,b$, deletion removes that distance, so
$q(H)\le q-1=(n-2)/2$ and the odd equality case again makes $H$
regular. Otherwise $a,b\in H$. Both convex sets $H\setminus\{a\}$
and $H\setminus\{b\}$ have $n-2$ points and at most $(n-2)/2$
distances. The even classification makes both concyclic. They share
$n-3\ge3$ noncollinear points, so their circles agree, and their
union $H$ is concyclic. Apply the all-but-one-circle theorem once
more. This proves the proposition.

The author checked the deletion counts, parity cases, common-circle
argument, and exact orders required by the source classification; the
argument is author-recorded.
This gives no bound when the number of points outside the chosen
convex subset is unbounded, nor an asymptotic rarity theorem even
for every convex set.

## Comparison with the second independent input

Section 5.2 of the
[second independent input](independent/large_distance_graph_and_convex_extension.md)
recovers the hull-vertex case of the proposition by the same two endpoint
deletions. The proposition above is stronger: its convex $(n-1)$-point subset
need not be the full hull. Section 5.1 is also covered by the stronger
all-but-one-circle theorem, which allows the extra point anywhere and supplies a
linear lower bound.

The input's two-nonvertex result is valid under its additional circular
hull hypothesis; a shorter proof and a modest extension are recorded in
[circular configurations](circular_configurations.md). It does not
establish the arbitrary two-nonvertex case. The lack of an asymptotic
conclusion from the classification argument itself is not a current gap
for this family: the later [short-edge inverse](short_incident_inverse.md)
proves divergence for fixed convex covers with $o(n)$ exceptions,
including all-but-one convex sets.

## Two points outside convex position at even order

**Corollary.** If $n\ge6$ is even and $A$ contains an $(n-2)$-point
subset $C$ in strictly convex position, then $R(A)\ge2$.

Orders through ten are already covered by [small orders](small_orders.md).
For even $n\ge12$, suppose $R(A)=1$. The
[unique-diameter theorem](unique_diameter_obstruction.md) excludes the
even counting boundary, so $q(A)\le n/2-1$. Altman's bound gives
$q(C)\ge(n-2)/2$, hence equality. Fishburn's even equality classification
quoted above applies to $|C|=n-2\ge10$ and makes $C$ cocircular.
The [all-but-two-circle theorem](two_off_circle.md) now contradicts
$R(A)=1$.

At odd order this argument leaves a convex $(n-2)$-gon with one more
than its minimum number of distances. No general classification of
that case is assumed, and the arbitrary odd-order two-exception case
remains untreated.

Sections 7.2--7.3 of the
[third independent report](independent/layer_bound_and_circular_majority.md)
were also checked. Its one-nonvertex classification argument and
its two-nonvertex reflection/affine-permutation argument are correct
under the stated hull hypotheses. They do not strengthen the results
above: the one-exception convex subset need not be the hull, and the
[two-off-circle theorem](two_off_circle.md) allows the two added
points anywhere. The report's unhandled two-nonvertex case is therefore
superseded at even order, but not at arbitrary odd order.
