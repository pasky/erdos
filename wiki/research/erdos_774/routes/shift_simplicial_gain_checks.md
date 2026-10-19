---
name: research/erdos_774/routes/shift_simplicial_gain_checks
title: Scoped checks of shift, simplicial, and gain-graph mechanisms
desc: Full shift supports and gain-graph stars have bounded colorings under stated hypotheses; simplicial boundaries at n/k asymptotic to C log n have uniform extraction but an open actual-coloring gap.
tags: [E0774, proved, scoped-obstruction, incomplete]
sources: []
created: 2026-09-18T22:38:00Z
updated: 2026-09-18T22:38:00Z
---


# Scoped checks of shift, simplicial, and gain-graph mechanisms

***

This page records the exact scopes of three mechanisms examined beside the
[Boolean moment route](boolean_moments.md). None of these checks is a
solution or a general impossibility theorem for E0774. All three are
author-recorded.

## 1. Full shift hypergraphs cannot be freely prescribed as relation supports

Let H(n,ell,k), k>=2, have vertices the ell-subsets of [n]. Its edges
are the k consecutive ell-windows of each increasing (ell+k-1)-tuple.
Suppose its vertices have distinct labels a_v in a rational vector space,
and every edge supports a relation with all its coefficients in {+1,-1}.
The signs may vary arbitrarily between edges. Then

$$
 \boxed{n\leq\ell+k+2^{k-1}-2.}
 \tag{1}
$$

If there is no edge, (1) is immediate. Otherwise fix b_2,...,b_{ell+k-1}
to be the final ell+k-2 indices, and vary b_1<b_2. The final k-1 window
vertices remain fixed. Normalize the coefficient of the first window to
+1. Its label must be one of at most 2^{k-1} signed sums of the other
labels. The first-window labels are distinct, so
n-ell-k+2=b_2-1<=2^{k-1}, proving (1).

In particular, for fixed k these realizable full shifts have chromatic
number at most k+2^{k-1}-1: color each tuple by its first index.
This colors the prescribed shift hypergraph, **not every possible extra
relation among its labels**. It shows that these prescribed supports do
not themselves yield unbounded chromatic numbers.

### Uniform six-color bound in the supplied high-fractional shift regime

The checked NRS Theorem 5.1 proof uses
ell=ceil(2(k-1)^2/(epsilon k)), where
0<epsilon<(k-1)/k. In particular ell>=2k-1. In that regime (1) implies

$$
 n\leq2^{(\ell+3)/2}.
$$

At ell=2k-1 this follows from 3k-3+2^{k-1}<=2^{k+1}; increasing ell
preserves the inequality since the right side grows by a factor sqrt(2)
and the left side only by one.

Here is an explicit coloring, without an asymptotic Ramsey bound.
Suppose the ordinary two-shift graph on j-tuples is properly q-colored,
q>=2. A (j+1)-tuple has two consecutive j-windows of distinct colors.
Encode colors in ceil(log_2 q) bits, choose a differing bit of that ordered
pair, and record its position and the first color's bit. Adjacent new
windows cannot have equal records: their shared old color would have to
have both recorded bit values. Thus the new graph has at most
2 ceil(log_2 q) colors.

Start with n colors on singletons. After one step the displayed bound on
n gives at most ell+4 colors. Each subsequent step decreases the count
by at least one whenever it exceeds six, and counts at most six stay at
most six. The remaining ell-2 steps therefore give a six-coloring on
ell-tuples. Consecutive vertices of any k-shift edge receive different
colors, so it too is properly colored.

Thus these **full prescribed shift supports** cannot supply the desired
unbounded coloring even by varying k in the NRS regime. The conclusion
does not exclude thinned shift hypergraphs or color obstructions caused
by additional relation supports. No extraction claim for their linear
realizations follows just from the hypergraph's fractional property.

## 2. Oriented boundaries of simplices: extraction proved, coloring open

Let E_{n,k} consist of the oriented boundaries of all k-subsets of [n],
viewed as integer vectors on the (k-1)-subsets, with 2<=k<n. Put
N=binom(n,k), R=binom(n,k-1), and let alpha be its maximum dissociated size.
Signed permutation symmetry gives eta(E_{n,k})=alpha/N by the same averaging
argument as for Boolean moments.

Write delta=alpha/N. Independent fair subset choices on a maximum
subfamily give entropy delta N. A row has variance one quarter of its
incidence degree, and the average degree over all R rows is
k delta N/R=(n-k+1)delta. Subadditivity, the integer Gaussian entropy bound,
and concavity give

$$
 \delta\leq\frac{k}{2(n-k+1)}
 \log_2\left(2\pi e\left[\frac{(n-k+1)\delta}{4}
                                     +\frac1{12}\right]\right).
 \tag{2}
$$

In particular eta tends to zero if n/(k log n) tends to infinity. This
does not exclude n/k asymptotic to C log_2 k; (2) only gives the upper
limit 1/(2C) there.

The boundaries of all k-subsets containing one fixed vertex are rationally
independent: the row obtained by deleting that vertex from a column is private
among those columns. They span all columns, by taking the boundary of a
(k+1)-simplex including that vertex and using boundary-squared zero. Thus the
full rank is binom(n-1,k-1). Averaging these vertex stars gives
rank(F)>=(k/n)|F| for every F. The
[matroid partition theorem of Edmonds](../../../../library/additive_combinatorics/edmonds_1965_minimum_partition_matroid_into_independent_subsets/_index.md),
checked in the held copy, gives

$$
 \chi_1(E_{n,k})\leq\chi_{\mathbb Q}(E_{n,k})=\lceil n/k\rceil.
 \tag{3}
$$

Hence bounded n/k cannot yield unbounded chromatic numbers, while excessively
large n/k loses extraction. In the intermediate range n/k asymptotic to C log n
for one fixed C>0, uniform hereditary extraction is proved by
[exterior-root semistability and the weak stable-lattice Gaussian theorem](simplicial_extraction.md);
the arbitrary-color obligation there **remains open**.

Elementary simplex boundaries are not enough for its coloring lower bound.
In a random two-coloring of the k-subsets, a particular (k+1)-simplex
boundary is monochromatic with probability 2^{-k}. Its event shares a
variable with exactly (k+1)(n-k-1) other such events. The symmetric local
lemma therefore gives a coloring avoiding all these elementary boundaries if

$$
 e\,2^{-k}\bigl((k+1)(n-k-1)+1\bigr)\leq1.
 \tag{4}
$$

For completeness, the symmetric condition follows from
[Moser--Tardos, Theorem 1.1](../../../../library/set_systems/moser_tardos_2009_constructive_proof_general_lovasz_local_lemma/_index.md),
checked in the held copy, by choosing x=1/(D+1) when the dependency degree D>=1,
using (1-1/(D+1))^D>=e^{-1}. When D=0 the events are independent. Condition (4)
holds for n=O(k log k) at sufficiently large k. This is only avoidance of the
elementary boundary supports, **not all flat cycles**.

## 3. Gain graphs: local extraction shortcuts do not supply the color step

Consider nonzero columns a_e e_u-b_e e_v with distinct endpoints and
nonzero integer endpoint coefficients.

**One-sided star condition.** Designate a good endpoint for every edge.
If, at each vertex, the indexed list of coefficients on its good incidences
can be partitioned into K dissociated classes, then the entire edge family
has at most 2K dissociated colors. Orient edges toward their good endpoint,
split into forward/backward DAGs under one vertex order, and use the local
star color at the head. A sink of a nonzero monochromatic relation has only
good incoming incidences, contradicting its star dissociation. This proof
allows arbitrary integer weights and no outdegree bound. In particular
one-sided lacunarity gives at most two colors.

**Separated positive coefficient groups.** Suppose all a_e,b_e are positive.
At each vertex, group incidences by their equal coefficient magnitudes
lambda_{v,s}. Suppose these distinct magnitudes are independent for integer
coefficients of absolute value at most the vertex degree. Split the vertex
into one slot for each magnitude. A ternary relation in the gain columns
then exists exactly when it exists in the ordinary oriented incidence
matrix of this split graph: the row equation at v separates into its slot
coefficient sums. This equivalence concerns the indexed edge family.

Dissociation in that incidence matrix is forest independence. Therefore a
hereditary extraction constant delta implies rank(F)>=delta|F| in the split
graph. Edmonds supplies at most ceil(1/delta) forest colors, which are also
dissociated gain colors by the established ternary equivalence. This bound
uses the stated digit-separation hypothesis, not arbitrary gain coefficients.

**Rigid copy blocks.** The equation x+2y-3z=0 for ternary variables forces
x=y=z: for z=+1 or -1 the extreme sum is required, and for z=0 only
x=y=0 is possible. It can implement rigid copying in weighted checks.
But suppose the columns are partitioned into prescribed blocks, each of
size at least two, and every nonzero relation uses either all or none of
each block. The construction is then two-colorable: split each block
between the two colors. A nonzero relation must meet, and hence contain,
one entire block. This observation
concerns rigid all-or-nothing gadgets; it is not a theorem excluding
flexible routing constructions or arbitrary gain graphs.

No high-chromatic uniformly extracting gain family was obtained. No
conclusion about all signed gain configurations is asserted.
