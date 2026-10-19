---
name: research/erdos_774/lemmas/difference_tower_color_limits
title: Valuation colorings and the limits of difference-tower flattening
desc: Small-loss towers on valuation-separated seeds are exactly two-colorable despite arbitrarily large rational coloring number; canonical height-halving witnesses contain whole coordinate cycles.
tags: [E0774, proved, coloring, obstruction]
sources: []
created: 2026-09-18T21:00:00Z
updated: 2026-09-18T21:59:00Z
---


# Valuation colorings and the limits of difference-tower flattening

***

The [difference-tower theorem](../routes/difference_towers.md) proves
near-lossless proportional dissociation. This page proves exact limitations
on proposed chromatic consequences. They do not color the line-seed towers
or the original ordinary line covers.

## 1. Hereditary rank transfer on an ancestral subfamily

Fix a field K. At a difference stage D_N(B), retain only descendants of a
specified subset S of the parent types. Suppose every subset T of S has
K-rank at least delta|T|. The global seam/maximal-vertex proof applies
without change to these selected types, giving rank density at least
(1-1/N)delta for their descendants. The sheet group may still have a
coordinate for every parent type, including types outside S: those extra
coordinates cause no problem for the common height or the incoming-type
argument.

It follows inductively that any ancestral seed subfamily of hereditary
K-rank density delta has normalized descendant rank density at least

$$
 \delta P_k,\qquad P_k=\prod_{j=1}^k(1-1/N_j).
 \tag{1}
$$

This statement can also be applied after dividing every seed column in
that subfamily, and all its descendants, by a common nonzero integer and
then reducing modulo a prime.

## 2. A valuation-layer coloring theorem

Fix a prime p and a finite nonzero integer seed A=(a_v). For each type let

$$
 t_v=\min_x\nu_p(a_v(x)),\qquad
 V_t=\{v:t_v=t\},\qquad
 \bar a_v=p^{-t_v}a_v\pmod p.
$$

The valuation of zero coordinates is infinity; since each column is nonzero,
t_v is finite and every normalized residue column is nonzero.
Assume, for one delta>0, that

$$
 \operatorname{rank}_{\mathbb F_p}\{\bar a_v:v\in S\}
 \geq\delta|S|
 \quad(S\subseteq V_t,\ \text{every }t).
 \tag{2}
$$

**Theorem.** Every k-stage difference tower on A has

$$
 \boxed{\chi_1(A^{(k)})\leq
                 \left\lceil\frac1{\delta P_k}\right\rceil.}
 \tag{3}
$$

**Proof.** Every descendant of a type v has the same minimum p-valuation
t_v: taking differences places positive and negative copies in distinct
row blocks and never adds their entries. Normalize and reduce each
ancestral layer modulo p. Section 1 gives hereditary rank density at least
delta P_k in that layer. Edmonds' matroid partition theorem partitions its
columns into K=ceil(1/(delta P_k)) residue-independent classes. Use the
same K color names independently in each layer.

If a nonzero monochromatic ternary integer relation existed, choose its
least occupied valuation t. Divide the entire relation by p^t and reduce
modulo p. All higher layers vanish. The surviving coefficients in layer t
are +1 or -1, which are nonzero also when p=2. This is a nontrivial linear
relation among the residue-independent columns of one color, a
contradiction. This proves (3). QED.

The source statement was checked in
[Edmonds, Section 1.3, Theorem 1](../../../../library/additive_combinatorics/edmonds_1965_minimum_partition_matroid_into_independent_subsets/_index.md),
including its applicability to matrices over arbitrary fields.

## 3. Arbitrarily dense rational seeds whose towers remain two-colorable

Take the scalar seed

$$
 A_n=(1,p,p^2,\ldots,p^{n-1}).
 \tag{4}
$$

It is fully dissociated: its largest occupied power exceeds the sum of all
smaller powers, for p>=2. It has rational coloring number n, since every
two nonzero scalars are rationally dependent. Nevertheless each valuation
layer consists of a singleton, so (2) holds with delta=1. Thus

$$
 P_k\geq\tfrac12\quad\Longrightarrow\quad
 \chi_1(A_n^{(k)})\leq2.
 \tag{5}
$$

At every positive depth there is a complete newest-coordinate cycle;
its distinct columns sum to zero. Hence for k>=1 equality holds in (5).
For example N_j=2^{j+3} gives P_k>=7/8 at every depth, so

$$
 \boxed{\chi_1(A_n^{(k)})=2\quad(n\geq1,\ k\geq1),}
 \tag{6}
$$

while the seed rational coloring number n is unbounded.
This disproves a **universal small-loss difference-tower/rational-coloring
comparison**, even with arbitrarily deep towers and arbitrarily small
positive total seam loss. A fixed-depth objection alone would be weaker.
The bounded-entry line seeds all lie in a single valuation layer, so this
example does not supply a uniform bound for those seeds.

## 4. Canonical coefficient-halving witnesses have a full-cycle obstruction

Consider the centered-cube lift from Section 5 of the difference-tower page.
If an input coefficient u_v has |u_v|>=2, fix the other coordinates so that
p_v=1. On this complete v-line its two coefficient values are
ceil(u_v/2) and -floor(u_v/2), both nonzero. Thus the lifted support
contains an entire coordinate-v cycle.

The coloring

$$
 c(v,g)=\mathbf1_{\{g_v=0\}}
 \tag{7}
$$

splits every coordinate cycle. Therefore it simultaneously splits every
centered-cube lift whose input has height at least two. The even-modulus
parity version has the same limitation. In particular the final genuine
height-two-to-ternary step of this canonical flattening can never be
monochromatic under (7).

This is a statement about those **particular templates**. A general
non-cycle ternary relation need not contain a complete coordinate cycle,
and (7) is not asserted to color all relations. The exact first-non-cycle
height theorem remains valid: an algebraically non-cyclewise-constant
relation may have support containing a full cycle. These are different
notions, and a chromatic argument cannot identify them.

## 5. A simple universal one-stage coloring upper bound

For every N>=4,

$$
 \chi_1(D_N(A))\leq2\chi_1(A).
 \tag{8}
$$

There is a more general and simpler proof. Let a finite loopless directed
graph have edges labeled by seed types v, with at most one incoming edge
of each type at every vertex. Associate a_v tensor(e_x-e_y) to an edge
x -> y of type v. For this indexed family B,

$$
 \eta(B)\geq\tfrac12\eta(A),\qquad
 \chi_1(B)\leq2\chi_1(A).
 \tag{9}
$$

For extraction, a uniform random strict total order retains each edge
with probability one half when only forward edges are kept. The retained
DAG has distinct incoming types at each head. Extract at each head and
use the maximal-vertex argument. This proves the first bound.

For coloring, fix a proper base coloring with q colors and any strict
vertex order. Split all edges into forward and backward arcs, **retaining
their original orientations**. Forward arcs form a DAG in the chosen
order; backward arcs form a DAG in the opposite order. Pair this bit
with the base color. Within each part, a maximal supported vertex in a
hypothetical relation has only incoming active arcs, of distinct types
in a dissociated base color. Their row equation forces all their
coefficients zero, a contradiction. This proves the second bound. No
outdegree restriction is used.

Difference tori and arbitrary loopless permutation differences are special
cases. Thus even the latter have the factor two, not a factor three from
cycle edge coloring. Permutation cycles of length at least three ensure
no repeated or antipodal same-type column labels. For a fully dissociated
seed, any such nonempty permutation family has coloring number exactly
two: a complete type cycle supplies the lower bound.

More generally, if a distribution of acyclic deletions removes each edge
with probability at most epsilon, the first bound improves to
eta(B)>=(1-epsilon)eta(A). The phase proof similarly gives
rho(B)>=(1-epsilon)rho(A)-epsilon. These extraction improvements do not
remove the displayed chromatic upper bound.

## 6. Scope of what survives

The uniform extraction theorem is unconditional. What remains sufficient
is a prechosen small-loss tower on suitable **varying, non-valuation-separated**
seeds with unbounded dissociated coloring under arbitrary actual colors.
The ordinary line-cover target also remains open. Neither rational seed
density nor canonical height flattening proves such a statement.
