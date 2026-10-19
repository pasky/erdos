---
name: research/geometric_configuration_interfaces/circumradii
title: "Circle counts and distinct circumradii"
desc: "Pair counting gives a linear radius bound and a conditional superlinear link; finite algebraic selection tests require exact general position."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/discrete_geometry/E0104/_index|E0104]],
[[problems/discrete_geometry/E0831/_index|E0831]],
[[problems/discrete_geometry/E0827/_index|E0827]].

## Congruent circles and distinct circumradii: E0104, E0831, E0827

Let U(P) count unit circles containing at least three points of an n-point
planar set P. Each such circle contains at least three unordered pairs. For two
distinct points there are at most two unit-circle centers equidistant one from
both. Consequently
$$
 3U(P)\leq2\binom n2,\qquad U(P)\leq n(n-1)/3.
$$
Tangency and separation beyond two only decrease the pair multiplicity. This is
a complete quadratic bound, not the little-o asked by E0104. If M centers are
added to P, the resulting unit-distance graph has n+M vertices. An upper bound
$C(n+M)^\beta$ with $\beta>1$ gives only
$3M\le2C(n+M)^\beta$: an edge can be counted twice when both endpoints
belong to both the point set and the center set. This inequality is compatible
with arbitrarily large $M$ relative to $n$ and gives no improved bound on $M$.

For E0831 take n at least three, with no three collinear and no four cocircular.
Every triple defines a finite circle, and distinct triples give distinct
circles. For any fixed radius r, the preceding pair count after scaling gives at
most n(n-1)/3 circles of that radius. Therefore the number h of distinct radii
satisfies
$$
 h\geq\frac{\binom n3}{n(n-1)/3}=(n-2)/2,
$$
with the integer ceiling understood. Define U(n) as the maximum number of
three-rich unit circles on an arbitrary n-point set. If E0104 holds, every
radius class has size at most U(n), uniformly in its radius, so
$$
 h(n)\geq \binom n3/U(n)=\omega(n).
$$
This is a one-way conditional link, not an unconditional superlinear bound or a
converse to E0104.

E0827 has an exact finite algebraic test, but its hypotheses matter. Its
intended general position is no three collinear and no four cocircular;
Martínez--Roldán-Pensado allow the weaker no-four-collinear condition in their
source. Their upper bounds apply to the stronger class, but an exact value in
one class does not automatically transfer to the other.

For distinct points p_i=(x_i,y_i), write
$$
 \ell_{ij}=(x_i-x_j)^2+(y_i-y_j)^2,\quad
 D_{ijk}=\det(p_j-p_i,p_k-p_i),\quad
 A_{ijk}=\ell_{ij}\ell_{ik}\ell_{jk}.
$$
A noncollinear triple T has
$$
 R_T^2=A_T/(4D_T^2).
$$
Thus two triples have equal circumradius exactly when A_T D_U squared minus A_U
D_T squared is zero. Distinctness is ell_ij greater than zero, no three
collinear is D_T nonzero, and no four cocircular is nonvanishing of the
four-by-four determinant with rows (x_i,y_i,x_i squared+y_i squared,1). For
fixed N,k, impose those conditions and, for each k-subset, the disjunction that
two of its distinct triples have equal radius. This finite real polynomial
formula is exactly the existence of a counterexample of size N, not a relaxation
to abstract triple colors. Quantifier elimination decides it in principle. No
solver, coordinates or infeasibility certificate were produced here.

The source's Sections 2 and 4 were inspected for the equal-radius loci and the
additional collision type involving two triples that both use the new point. A
greedy extension that checks only collisions with old radii misses that type.
The next useful finite test is one exactly specified N for k=5, under the strong
convention. Floating near-equalities and infinite-radius collinear triples are
not certificates.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/discrete_geometry/martinez_2015_points_defining_triangles_distinct_circumradii/_index|martinez
  2015 points defining triangles distinct circumradii]]: Sections 1-2, Theorems
  1.1-1.2; Section 4, circumradius collision polynomial and Lemma 4.1 (proof
  reading).
