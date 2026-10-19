---
name: research/erdos_774/lemmas/bounded_support
title: A bounded-support obstruction to interval constructions
desc: Proportional dissociation for bounded-support bounded-entry integer vectors forces a uniform rational-independent partition.
tags: [E0774, proved, obstruction]
sources: []
created: 2026-09-17T23:53:25Z
updated: 2026-09-17T23:53:25Z
---


# A bounded-support obstruction to interval constructions

***

## Theorem — proved

Let $(v_e)_{e\in E}$ be a finite indexed family of nonzero integer vectors.
Suppose every vector has at most an integer $K\geq1$ nonzero entries, of
absolute value at most an integer $M\geq1$. If every subfamily contains a
dissociated subfamily of relative size at least $\delta>0$, then the family has
a partition into at most

$$
q=\left\lceil\frac{2K\log_2(2MK)}{\delta}\right\rceil-1
\tag{1}
$$

rationally linearly independent classes. In particular its dissociated
coloring number is strictly less than $2K\log_2(2MK)/\delta$.

This is a signed-vector adaptation of the entropy/coordinate-degeneracy
mechanism of
[Nešetřil–Rödl–Sales](../../../../library/integer_sequences/nesetril_2024_pisier_type_theorems/_index.md),
Theorem 2.1 and Lemma 2.2 (Section 2, reading-copy pages 4–6). The proof below
is self-contained.

### Subset-sum entropy bound

If a dissociated $m$-element subfamily uses $n\geq1$ coordinates, let
$d_j$ count its nonzero entries in coordinate $j$. Then
$\sum_jd_j\leq Km$. The subset sums in that coordinate occupy an integer
interval of width at most $Md_j$: the lower endpoint sums negative entries
and the upper endpoint sums positive entries. Consequently

$$
2^m\leq\prod_{j=1}^n(Md_j+1)
\leq(1+MKm/n)^n.
$$

Writing $a=MK$ and $t=m/n$, this implies $2^t\leq1+at$, hence

$$
m<2n\log_2(2MK). \tag{2}
$$

To justify the last numerical step, put $t_0=2\log_2(2a)\geq2$.
For integer $a\geq1$, $\log_2(2a)\leq a$, so
$2^{t_0}=4a^2>1+2a^2\geq1+at_0$. Also
$\log_2(1+at)-t$ is strictly decreasing for $t\geq2$, since its
derivative is at most $1/(t\log2)-1<0$.

### Coordinate deletion

Let $X$ be the union of the supports. For nonempty $U\subseteq X$,
put $F_U=\{e:\operatorname{supp}v_e\subseteq U\}$. By extraction and
(2), when $F_U\ne\varnothing$,

$$
\delta|F_U|<2|U|\log_2(2MK).
$$

The sum over $x\in U$ of the degrees in $F_U$ is at most $K|F_U|$.
Hence some coordinate has degree strictly less than
$2K\log_2(2MK)/\delta$, and therefore at most $q$. If $F_U$ is
empty, this conclusion is immediate.

Delete coordinates repeatedly using this rule. Group each vector by its first
support coordinate in the deletion order; each group has size at most $q$.
Color each group injectively from $[q]$. A nonzero rational relation within
one color is impossible: at the earliest coordinate used by a participating
vector, exactly one participating vector of that color is nonzero. Its
coefficient cannot cancel. This proves (1).

## Fixed-width interval systems

### Sharper rank version (using Rado–Horn)

If every integer column has $\ell_1$-norm at most an integer $L\geq1$, the same
counting argument yields

$$
|D|<2\log_2(2L)\operatorname{rank}_{\mathbb Q}(D)
$$

for every nonempty dissociated subfamily $D$. Select a number of coordinate
rows equal to the rank so that projection is injective on the span. Projection
preserves dissociation and does not increase the column $\ell_1$-norms;
the subset-sum box then has total coordinate width at most $L|D|$.
Apply the numerical argument above with $n=\operatorname{rank}(D)$.

Under hereditary $\delta$-extraction this implies
$|F|\leq[2\log_2(2L)/\delta]\operatorname{rank}(F)$ for all subfamilies.
Rado–Horn (as stated in the
[Grow–Whicher source](../../../../library/analysis/grow_whicher_1984_finite_unions_quasi_independent_sets/_index.md)
and
[Lewko, Theorem 4.1](../../../../library/analysis/lewko_2026_sidon_decomposition_problem_abelian_groups_bounded_torsion/_index.md))
therefore partitions the columns into at most $\lceil2\log_2(2L)/\delta\rceil$
rationally independent classes. There is no justified minus-one improvement in
this last ceiling bound.

### Applying the elementary version

The NRS construction associates to an ordered even-sized edge
$e=\{x_1<\cdots<x_k\}$ the vector

$$
a_e=1_{A_e},\qquad
A_e=\bigcup_{i=1}^{k/2}[x_{2i-1},x_{2i})\times\{i\}.
$$

Discrete differentiation $(Df)(x,i)=f(x,i)-f(x-1,i)$ is injective on
finitely supported functions. It gives

$$
Da_e=\sum_{i=1}^{k/2}
\bigl(e_{(x_{2i-1},i)}-e_{(x_{2i},i)}\bigr),
$$

with exactly $k$ entries, all $\pm1$. Thus differentiation preserves
every rational and signed relation and places the family under the theorem
with $K=k,M=1$, regardless of interval lengths.

If the family contains a monochromatic signed relation under every
$r$-coloring, its hereditary dissociation constant $\eta$ satisfies

$$
\eta<\frac{2k\log_2(2k)}{r+1}. \tag{3}
$$

For affine scalar encodings $y_e=uL(a_e)+v$, use instead
$c_e=(Da_e,1)$, with $K=k+1,M=1$. Every relation of the $c_e$ is
balanced and maps to a relation among the $y_e$. A scalar-dissociated
subfamily must therefore be vector-dissociated. If the prescribed
monochromatic relations are balanced, they still occur among the $c_e$,
and (3) becomes

$$
\eta(\{y_e\})<
\frac{2(k+1)\log_2(2(k+1))}{r+1}. \tag{4}
$$

This transfer is one-way; it does not assume carry-freeness for arbitrary
length scalar relations. Distinct scalar labels are required, as holds in
the NRS encodings.

## Consequence for the supplied fixed-order construction

In NRS Section 3, Lemma 3.5 and the proof of Theorem 3.1 produce balanced
Ramsey relations with $h$ terms on each side in a fixed width $k=k(h)$.
Theorem 4.1 and the proof of Theorem 1.1 encode these by linear and affine
maps. Applying (4) to their finite high-chromatic witnesses proves that,
for each fixed $h\geq2$, their constructed integer set is **not
proportionately dissociated**. It is not just an unproved property of that
construction: the hereditary constants tend to zero along its witnesses.

Therefore increasing bases, interval lengths, or block dilations cannot repair
the fixed-width mechanism. A successful variant must leave this bounded-support,
bounded-entry class after any injective linear change of coordinates.
