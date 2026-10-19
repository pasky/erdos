---
name: research/erdos_774/lemmas/matching_profile_limits
title: Two scoped limits of sparse direction and full-profile focusing
desc: Bounded reciprocal direction mass gives bounded rational coloring, while sixteen plane labels defeat full-profile homogenization along every later multiscale line; neither result colors all mixed trades.
tags: [E0774, lines, coloring, proved, scoped-obstruction]
sources: []
created: 2026-09-19T01:30:00Z
updated: 2026-09-19T01:30:00Z
---


# Two scoped limits of sparse direction and full-profile focusing

***

These results constrain two proposed Ramsey implementations. They do
not exclude color-adaptive cancellation between several mixed trades,
and are not a coloring theorem for the whole line family.

## 1. Bounded reciprocal mass forces bounded actual colors

For signed linear direction matchings of sizes $d_i$, put
$S=\sum_i1/d_i$. Then
$$
\chi_1\leq\chi_{\mathbb Q}\leq\lceil1+S\rceil.       \tag{1}
$$
For any column subset $B$, normalize its columns to unit length and
let $G_B$ be their Gram matrix. A size-$d_i$ column meets at most
$d_i$ disjoint members of direction $j$; each squared correlation is
at most $1/(d_id_j)$. Hence
$$
\operatorname{tr}G_B=|B|,\qquad
\operatorname{tr}(G_B^2)\leq(1+S)|B|.
$$
Cauchy--Schwarz on its nonzero eigenvalues gives
$\operatorname{rank}_{\mathbb Q}B\geq|B|/(1+S)$.
[Edmonds, Theorem 1](../../../../library/additive_combinatorics/edmonds_1965_minimum_partition_matroid_into_independent_subsets/_index.md)
now proves (1). Both the digest and exact source statement were checked.

Thus assigning domains so large that $S$ remains bounded cannot
produce an unbounded-color direction family. The established extraction
phase condition permits divergent $S$; (1) does not rule out that regime.

## 2. Initial-plane profiles need not homogenize on a later column

In each [field, flag, or polynomial line model](../routes/field_tower_lines.md),
partition rows into initial affine $p$-planes. Every later column meets
each such plane at most once. Later sizes are $p^k$, $k\geq2$, with
at most $p^k$ directions at each size.

**Claim.** The initial planes can be labeled with sixteen labels so
that no later column meets planes all bearing the same label.

For a finite stage, color planes independently and uniformly with sixteen
labels. The event for a column of size $D$ has probability $16^{1-D}$.
Assign it local-lemma weight $x_D=2^{-D}$. A plane contains $p^2$
points and so meets at most $p^2M_E$ columns among $M_E$ directions
of size $E$. Thus the sum of neighboring event weights for a
$D$-column is at most
$$
Dp^2\sum_{k\geq2}p^k2^{-p^k}\leq(8/7)D.           \tag{2}
$$
Successive summands have ratio
$p\,2^{-(p-1)p^k}\leq1/8$. The first summand, after multiplication by
$p^2$, is at most one since $p^4\leq2^{p^2}$. This proves (2).
Since all $x_D\leq1/16$, the dependency product is at least
$$
\exp(-(16/15)(8/7)D)=\exp(-128D/105).
$$
For $D\geq4$,
$$
\frac{D-1}{D}\log16-\log2\geq2\log2>4/3>128/105.
$$
Therefore
$$
16^{1-D}\leq2^{-D}\exp(-128D/105),
$$
which verifies the asymmetric local-lemma hypothesis. The relevant
independent-variable statement was checked after its digest in
[Moser--Tardos, Theorems 1.1--1.2](../../../../library/set_systems/moser_tardos_2009_constructive_proof_general_lovasz_local_lemma/_index.md).
Compactness gives the same labeling on a nested infinite model.

### Realization by proper colors on the initial columns

In each initial $p$-plane, split every parallel class into two nonempty
parts. Each binary part is rationally independent: a relation in the
full affine plane is constant within each parallel class, whereas the
part omits a column from every class. Pair this binary color with the
plane's sixteen-valued label. Across the disjoint initial planes, this
gives thirty-two proper initial-column colors.

Any later column encounters distinct plane labels and hence distinct
complete initial-plane color profiles. Consequently a Ramsey argument
that requires identical full old-plane profiles along one entire later
column cannot be universal.

This coloring is only on the initial columns. It does not color the later
ones or split their mixed relations; several later columns can cancel
outside a chosen profile class. No general color-adaptive lifting theorem
is refuted. The finite dependency estimates and scope are author-recorded.
No computational search was run.
