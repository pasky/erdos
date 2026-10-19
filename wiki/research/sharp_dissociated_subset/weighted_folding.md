---
name: research/sharp_dissociated_subset/weighted_folding
title: Weighted folding and the limit of a generic Kraft estimate
desc: Folding elements near multiples of a common modulus resolves repeated-source choices under a strict total budget. A dyadic interval construction refutes a generic weighted Kraft packing inequality, leaving the arithmetic structure of the virtual points essential.
created: 2026-10-15T22:09:18Z
updated: 2026-10-15T22:09:18Z
---

***

The lattice lemma in
[[research/sharp_dissociated_subset/pivot_certificates|the certificate note]]
can combine elements at very different scales: write $z=q_zg+\rho_z$
and require distinct 2-adic valuations of the nonzero residues, at most
one zero residue, and $\sum_z|\rho_z|<g$. The following observations,
by Plasma AI and author-recorded, delimit a proposed averaging proof of
this condition. They do not prove its existence for an arbitrary set.

## Virtual points and repeated sources

Let $g=z_0/q_0>0$, with $q_0$ odd, and use odd positive multipliers
$q_z$ for other elements. The virtual point $v_z=z/q_z$ satisfies

$$
\rho_z=z-q_zg=q_z(v_z-g),
\qquad
v_2(\rho_z)=v_2(v_z-g).
$$

Here $v_2$ is extended to nonzero rationals by subtracting the valuations
of numerator and denominator. The lattice proof still works for rational
$g$: multiplying all residues and $g$ by a common denominator preserves
the distinctness of their valuations and the strict budget. A companion's
cost is $q_z|v_z-g|$, so different sources carry different weights.

Under the strict total budget, a selected collection cannot use two
different representations of the same element $z$. Indeed, if the
multipliers are $p\ne q$, then

$$
|z-pg|+|z-qg|\ge |p-q|g\ge g.
$$

For two odd multipliers the lower bound is $2g$. Thus repeated-source
exclusion is automatic for this strict-budget construction. The statement
does not cover relaxed graded budgets whose total may exceed $g$.

The real center can also be chosen independently of the virtual pivot.
Let $v_i=z_i/q_i$ for positive odd integers $q_i$, and suppose the
nonzero differences $v_i-v_0$, $1\le i\le k$, have distinct 2-adic
valuations. If some real $c>0$ satisfies

$$
\sum_{i=0}^k |z_i-q_ic|<c,
\tag{F}
$$

then $\{z_0,\ldots,z_k\}$ is dissociated. Repeated sources are excluded
by the same strict-budget argument. In a ternary relation write
$Q=\sum_i\varepsilon_iq_i$. If $Q\ne0$, rewriting around $c$
contradicts (F). If $Q=0$, rewriting around $v_0$ gives
$\sum_{i\ge1}\varepsilon_iq_i(v_i-v_0)=0$; the least valuation is
unique since every $q_i$ is odd. All these coefficients vanish, and
$Q=0$ then forces the remaining coefficient to vanish. This is a
weighted version of the free-center lemma. Its averaging problem is
still open, but the center need not be constrained to one of the
virtual points.

## A generic weighted packing inequality is false

Let $T$ be a full binary tree whose leaves are labeled by a finite set
of intervals $I_i=[x_i-r_i,x_i+r_i]$ in $[0,1]$. Set
$S_i=\{j:x_i\in I_j\}$, which contains $i$. Let $m_i$ be the depth of
leaf $i$ in the tree induced on $S_i$, after vertices with just one child
are suppressed. There is no absolute constant $K$ such that

$$
\sum_i r_i2^{-m_i}\le K
\tag{W}
$$

for every such interval family and binary tree.

Here is an explicit family with linear growth in the number of scales.
For an integer $H\ge0$ and each $s=0,\ldots,H$, take the $2^s$ dyadic
cell centers and radii

$$
x_{s,j}=\frac{2j+1}{2^{s+1}},\qquad
r_{s,j}=2^{-s-2},\qquad 0\le j<2^s.
$$

The centers are pairwise distinct and each interval lies strictly
inside its cell. At a center of level $s$, no interval of a finer
level can contain that center: it is a cell boundary at every finer
level. No other interval of level $s$ contains it either. Thus
$S_{s,j}$ consists of $(s,j)$ itself and labels of coarser levels.

Let $B_s$ be any full binary tree on the level-$s$ labels. Put $T_0=B_0$
and recursively make $T_s$ the tree with children $T_{s-1}$ and $B_s$.
Use $T_H$ as the tree on all labels. In its restriction to $S_{s,j}$,
all finer levels disappear, and $(s,j)$ is the sole surviving leaf of
$B_s$. Every other surviving leaf is in $T_{s-1}$. Therefore its induced
depth $m_{s,j}$ is either zero or one, and

$$
\sum_i r_i2^{-m_i}
\ge \frac12\sum_{s=0}^H2^s2^{-s-2}
=\frac{H+1}{8}.
$$

This is unbounded, proving the failure of (W). The construction is
explicit for every $H$ and has no computational premise.

## What remains for folding

The virtual points of a fixed source $z$ are not arbitrary interval
centers: as the odd multiplier varies, they form the specific family
$z/q$, and a threshold on weighted distance gives intervals of radius
proportional to $1/q$. The obstruction above does not assert that its
interval family has this form with the required arithmetic relations.
Consequently it refutes a proof using arbitrary weighted intervals and
only the Kraft equality, not the folding route itself.

A successful averaging argument must use the compatibility of the
different multipliers of each source, or another arithmetic property
absent from (W), to produce a modulus with sufficiently many cheap
residues at distinct levels. This is the unresolved interface in the
[[research/sharp_dissociated_subset/proof_sketch|constant-loss route]].
