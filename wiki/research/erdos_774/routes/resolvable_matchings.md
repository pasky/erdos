---
name: research/erdos_774/routes/resolvable_matchings
title: Uniform extraction for direction matchings beyond box covers
desc: The phase induction works for arbitrary signed linear direction matchings of sizes i+2; resolvable supports have explicit common covers with boxes, but coloring growth remains unproved.
tags: [E0774, proved, extraction, construction, incomplete]
sources: []
created: 2026-09-18T20:00:00Z
updated: 2026-09-18T20:53:07Z
---


# Uniform extraction for direction matchings beyond box covers

***

## 1. Global phase theorem

Let P_1,...,P_t be matchings of subsets of a finite set X: sets within
each P_i are disjoint. Every member of P_i has size d_i>=3, and
members of different directions intersect in at most one point. They
need not cover X. Identify each set with its zero-one indicator column.

For arbitrary complex coefficients c_E,

$$
\max_{z\in\mathbb T^X}\Re\sum_Ec_E\prod_{x\in E}z_x
\geq\sum_{i=1}^t r_{i,t}\sum_{E\in P_i}|c_E|,
\qquad
r_{i,t}=\prod_{j=i+1}^t\cos(\pi/d_j)^{d_i}.
\tag{1}
$$

**Proof.** The case t=1 follows by disjointness. In the last step let
a=cos(pi/d_t). The polygon of the d_t-th roots of any prescribed unit
number contains the disk of radius a, so it supports a random Y with
Y^{d_t} equal to that number and EY=a.

For an old set E let k(E) count the new sets it meets. Disjointness and
the intersection hypothesis give k(E)<=|E|=d_i. First apply induction
to the old polynomial with its **individual** coefficients multiplied
by a^{k(E)}, and fix the resulting phases. For each new F prescribe the
root target that aligns its coefficient, independently choose Y_F with
that target and expectation a, and multiply every row phase on F by Y_F.
Rows outside the new matching are unchanged.

Each new term is exactly aligned. An old term has expected multiplier
a^{k(E)}, since it meets each new set at most once. Hence expectation
equals the old prescaled polynomial plus the absolute values of the new
coefficients. Induction and a^{k(E)}>=a^{d_i} give (1). Some finite
random outcome attains at least this expectation. No row layers, coordinate
labels, or covering hypothesis were used.

For d_i=i+2, the checked inequality

$$
-\log\cos(\pi/n)\leq\frac{\pi^2}{2n(n-1)}\quad(n\geq4)
$$

telescopes to r_{i,t}>=exp(-pi^2/2). Thus all finite systems above with d_i=i+2
have one uniform positive-real Sidon lower bound. Put one copy of every finite
isomorphism type in this schedule in independent free-abelian summands. Their
union is Sidon with the same bound, because phase choices on different summands
are independent.
[Pisier, Theorem 2](../../../../library/analysis/pisier_1983_arithmetic_characterizations_sidon_sets/_index.md)
applied once gives **one positive full-dissociation extraction constant** for
all finite systems and all their subsets. Its hypotheses and full statement were
checked in the supplied source; no quantitative constant is inferred from the
announcement.

### 1.1 Signed extension of (1)

Replace the indicator on each support E by an arbitrary vector with entries
s_E(x) in {+1,-1} on E and zero elsewhere. Equation (1), with the same
constants, is unchanged. In its induction step, multiply the phase at a
point x of a new support F by Y_F^{s_F(x)}. The new character is multiplied
by Y_F^{d_t}, while an old character meeting F once is multiplied by
Y_F or its inverse. Both have expectation a, because EY_F=a is real and
Y_F lies on the unit circle. Thus the same individual prescaling and
expectation proof applies. One direct-sum Pisier application to all finite
signed systems again gives a single extraction constant.

This allows signed incidence constructions but supplies no chromatic
growth. In particular, making a family regular as a rational matroid
cannot itself complete the construction: if rational dependence always
contains a ternary dependence, uniform extraction implies proportional
rational rank on every subset, and the matroid partition theorem gives
a uniformly bounded coloring.

More specifically,
[signed-cographic relation spaces](../lemmas/signed_cographic_limit.md) give at
most three rationally independent colors under the necessary
nonzero/distinct-up-to-sign column condition. A two-parameter signed graph
gluing cannot supply the required unbounded coloring.

## 2. Which resolvable systems are themselves box covers?

The geometric statements in Sections 2--3 concern the unsigned supports.

Now assume X is nonempty and every P_i partitions X. The system is a
direction-preserving incidence cover of L(d_1,...,d_t) exactly when maps
f_i:X->[d_i] exist such that f_i is constant on every j-block for j!=i and
bijective on every i-block.

Necessity is immediate from projection to box coordinates. Conversely
f=(f_i) maps each block to a full line and is locally bijective at every
row and block vertex. Since the box incidence graph is connected, any
nonempty such finite local cover is surjective, with a common fiber
size (propagate fiber cardinalities across incidences). This is the
required incidence cover.

Equivalently, f_i is constant on connected components generated by all
other directions and rainbow on every i-block. The maps need not exist.
For example, take a bipartite graph whose eight left neighborhoods in
right vertices 1,...,6 are

$$
123,\ 124,\ 134,\ 234,\ 156,\ 256,\ 356,\ 456.
$$

Use its 24 incidences as rows. Left stars partition them into triples,
and right stars partition them into four-sets, with cross intersections
at most one. Coordinate f_1 would give three labels to the right stars,
rainbow on all listed triples. The first four triples require four
pairwise distinct labels on vertices 1,2,3,4. Thus this system is not
a direction-preserving cover of L(3,4).

## 3. Nevertheless an explicit common finite cover always exists

Let Y=product_i[d_i]. Use rows X times Y. For each i-block
E={x_0,...,x_{d_i-1}} and each box i-line
ell={y_0,...,y_{d_i-1}}, partition E times ell into the d_i sets

$$
F_{E,\ell,r}=\{(x_k,y_{k+r\bmod d_i}):0\leq k<d_i\},
\qquad 0\leq r<d_i.
\tag{2}
$$

For each i these form a partition of X times Y. Projection to X is
locally bijective on rows and blocks, hence gives a degree-|Y| cover
of the original system. Projection to Y similarly gives a degree-|X|
cover of the box. The cyclic matchings in (2) verify these claims
directly; no common-cover theorem is imported.

## 4. Exact remaining obligation

The global theorem enlarges the uniformly extracting family at the level
of actual configurations. An unbounded dissociated coloring theorem for
these direction matchings would suffice for the required construction,
using the existing exact integer encoding and separated blocks.

The common-cover construction does **not** transfer a chromatic lower
bound from a resolvable system to its lift: arbitrary colors on lifted
columns need not descend. No chromatic monotonicity under incidence
covering is asserted. Neither this theorem nor the new family proves the
missing actual-color statement. This route remains secondary to seeking
jointly unavoidable relation templates in ordinary line covers.
