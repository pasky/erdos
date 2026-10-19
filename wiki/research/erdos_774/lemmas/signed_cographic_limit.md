---
name: research/erdos_774/lemmas/signed_cographic_limit
title: Signed-cographic relation spaces have at most three colors
desc: A genuine vector configuration whose full rational relation space is a signed graph cut space has rational rank at least one third on every subset and hence at most three dissociated colors.
tags: [E0774, proved, obstruction, coloring]
sources: []
created: 2026-09-18T20:47:00Z
updated: 2026-09-18T20:53:07Z
---


# Signed-cographic relation spaces have at most three colors

***

## Exact hypothesis

Let G be a finite loopless signed multigraph, with vertex set U, edge
set E, and signs sigma_e in {+1,-1}. Orient its edges arbitrarily and
define the signed gradient map T by

$$
(T\phi)_e=\phi(u)-\sigma_e\phi(v)\qquad(e:u\longrightarrow v).
$$

Let A be a rational matrix with columns indexed by E and full real relation
space ker A=im T. Assume A has no nonzero ternary relation supported on one or
two columns. In particular this holds when its columns are nonzero, pairwise
distinct, and not antipodal, as required before the positive integer encoding.

**Theorem.** For every F subset E,

$$
\operatorname{rank} A_F\geq |F|/3,
\qquad \chi_1(A)\leq\chi_{\mathbb Q}(A)\leq3.
\tag{1}
$$

Thus signed-cographic two-parameter gluing does not yield an unbounded
coloring family. The assumption is equality with the **full** relation
space, not merely that some planted relations have this form. No result
for arbitrary higher-arity sharing is asserted.

## 1. Rank in terms of balanced components

A connected signed graph is balanced if vertex signs tau_u in {+1,-1}
can be chosen with sigma_e=tau_u tau_v on every edge. Let b(H) count
the balanced connected components of H, including isolated vertices.
The equations T phi=0 have one free scalar on each balanced component
and only the zero solution on an unbalanced component: propagate phi
along paths; a cycle with negative sign product forces its value to zero.
Hence dim ker T=b(G).

Requiring T phi to vanish outside F leaves one scalar for each balanced
component of G minus F. Quotienting by ker T gives

$$
\dim(\operatorname{im}T\cap\mathbb R^F)
=b(G\setminus F)-b(G).
$$

Since the relation space of A_F is precisely this intersection,

$$
\operatorname{rank} A_F
=|F|-b(G\setminus F)+b(G).
\tag{2}
$$

## 2. Every active balanced component uses three weighted incidences

For a balanced component C of G minus F choose its gauge tau, and let
phi_C equal tau on C and zero elsewhere. Put y_C=T phi_C. It is supported
on F. Its nonzero entries are:

- plus or minus one on an F-edge with exactly one endpoint in C;
- plus or minus two on an F-edge internal to C whose sign conflicts
  with the chosen gauge.

Let w_C be the number of the first kind plus twice the number of the
second kind. If y_C is nonzero, then w_C>=3. For w_C=1 there would be a
one-column ternary relation. For w_C=2 there would be either a two-column
ternary relation, or a vector plus or minus 2e in im T; dividing the
latter by two also gives a forbidden one-column ternary relation.

If y_C=0, C is already an entire balanced component of G: it has no
boundary F-edge and every internal F-edge respects the gauge. There
are at most b(G) such inactive components. Moreover

$$
\sum_C w_C\leq2|F|.
$$

Indeed a crossing edge can be counted at most once at each endpoint,
and an internal frustrated edge is counted twice in only one component.
Consequently

$$
3\bigl(b(G\setminus F)-b(G)\bigr)\leq2|F|.
$$

Insert this into (2) to obtain the rank inequality in (1).

## 3. Coloring conclusion and scope

[Edmonds' matroid partition theorem](../../../../library/additive_combinatorics/edmonds_1965_minimum_partition_matroid_into_independent_subsets/_index.md)
says that rank(F)>=|F|/k for every subset is equivalent to a partition into k
independent sets. Its statement was checked in the supplied full source after
reading the digest. Apply it to the rational column matroid with k=3. Rationally
independent classes are dissociated, proving the remaining assertions in (1).

This argument is author-recorded and was checked by a separate reviewer.
It is an obstruction to this specified gluing model,
not to arbitrary signed matching configurations or to the cover theorem
still needed for E0774. No computation is used.
