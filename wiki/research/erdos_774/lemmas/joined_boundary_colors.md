---
name: research/erdos_774/lemmas/joined_boundary_colors
title: Two colors split joined boundaries and small-vertex-excess cycles
desc: When log n=o(k), one two-coloring avoids all joined simplex boundaries and all flat cycles with vertex excess at most floor(sqrt(k/(16 log(2n)))); other flat cycles remain uncontrolled.
tags: [E0774, simplicial, coloring, proved, scoped-obstruction]
sources: []
created: 2026-09-19T01:38:00Z
updated: 2026-10-14T00:26:52Z
---


# Two colors split joined boundaries and small-vertex-excess cycles

***

## Statement and scope

Suppose $k\to\infty$ and $\log n=o(k)$, with $k<n$. For all
sufficiently large stages there is a two-coloring of $\binom{[n]}k$
splitting **every** support which is a join of boundaries of disjoint
simplices. The number and sizes of the joined factors are unrestricted.

This settles the joined-template local-lemma check.
It applies, in particular, at the uniformly extracting
[simplicial scale](../routes/simplicial_extraction.md)

$$
n/k\sim C\log n\qquad(0<C<\infty\text{ fixed}).
$$

It is **not** a dissociated two-coloring: arbitrary flat cycles need not
be such joins. It neither bounds the actual coloring number nor proves
that the simplicial candidate fails.

Section 4 strengthens the same two-coloring to avoid every flat cycle
whose vertex excess is at most the stated growing threshold. Separately,
[three colors avoid all decomposable cycles](decomposable_cycle_colors.md),
including simple wedges not of joined-boundary form.

## 1. All the templates and their sizes

Take pairwise disjoint sets $B_1,\ldots,B_a\subseteq[n]$, where

$$
|B_i|\geq2,\qquad \sum_{i=1}^a(|B_i|-1)=k.
$$

Their joined support is

$$
T=\left\{\bigcup_{i=1}^a(B_i\setminus\{b_i\}):b_i\in B_i\right\}.
\tag{1}
$$

In exterior notation the product of the oriented chains

$$
\partial e_{B_1}\wedge\cdots\wedge\partial e_{B_a}
$$

is a nonzero integral $k$-chain with coefficients in $\{0,\pm1\}$,
support $T$, and zero boundary. Disjointness makes all its monomials
distinct; the derivation rule and $\partial^2=0$ make it a cycle.
Thus (1) really is a ternary relation support for the boundary columns.

Put $s_T=|T|=\prod_i|B_i|$. If integers $b_i\geq2$ have
sum $k+a$, the product is minimized by moving all excess above two
to one factor: for $2<u\leq v$,

$$
uv-(u-1)(v+1)=v-u+1>0.
$$

Consequently

$$
s_T\geq2^{a-1}(k-a+2)\geq k+1.                 \tag{2}
$$

For the last inequality, the left side equals $k+1$ at $a=1$
and its consecutive ratio is $2(k-a+1)/(k-a+2)\geq1$.

Fix a face $I\in\binom{[n]}k$. There are at most

$$
a^k n^a                                             \tag{3}
$$

templates with $a$ blocks and $I\in T$. Indeed, label the blocks,
partition $I$ into their nonempty remnants $B_i\setminus\{b_i\}$,
and choose the omitted $b_i\notin I$. There are at most $a^k$
partitions and $n^a$ choices. This overcounts unordered templates and
invalid choices; both are harmless for an upper bound. Identical supports
can be retained just once.

## 2. A uniform weighted incidence bound

Assign each template the weight $x_T=e^{-s_T/2}$, and set

$$
L=\max_I\sum_{T\ni I}x_T.
$$

Equations (2)--(3) give

$$
L\leq n e^{-(k+1)/2}
 +\sum_{a=2}^k
   \exp\bigl(a\log n+k\log a-2^{a-2}(k-a+2)\bigr). \tag{4}
$$

For $2\leq a\leq k$,

$$
k-a+2\geq2k/a,
\qquad 2^{a-1}\geq4a^2/9.
$$

The first inequality is equivalent to $(a-2)(k-a)\geq0$.
For the second, check $a=2,3$; the ratio $2^{a-1}/a^2$ increases
for $a\geq3$, since $2a^2>(a+1)^2$. Since

$$
\frac{\log a}{a}\leq\frac1e<\frac49-\frac1{16},
$$

the negative term in (4) is at least

$$
2^{a-2}(k-a+2)\geq\frac49ak\geq k\log a+ak/16.
$$

Writing $b=k/16-\log n\to\infty$, we obtain the explicit bound

$$
L\leq n e^{-(k+1)/2}+\frac{e^{-2b}}{1-e^{-b}}=o(1). \tag{5}
$$

## 3. One coloring for the entire joined family

Color the $k$-faces independently with two equiprobable colors. The
bad event $A_T$ that $T$ is monochromatic has probability

$$
\Pr(A_T)=2^{1-s_T}.
$$

Two events are adjacent when their supports share a $k$-face. This
is a valid dependency graph for independent face-color variables.
Since $x_U\leq1/2$, the inequality
$\log(1-x_U)\geq-2x_U$ and (5) imply

$$
\prod_{U\in\Gamma(T)}(1-x_U)
\geq\exp\left(-2\sum_{U\in\Gamma(T)}x_U\right)
\geq e^{-2s_T L}.
$$

Therefore the asymmetric local-lemma condition follows from

$$
2^{1-s_T}\leq e^{-s_T(1/2+2L)}.
\tag{6}
$$

For every sufficiently large $k$, (6) holds simultaneously for all
templates: it is equivalent to

$$
\log2\leq s_T(\log2-1/2-2L),
$$

whose right side tends to infinity uniformly by $s_T\geq k+1$
and $L=o(1)$. The local lemma yields the asserted coloring.

The exact asymmetric statement and dependency requirement were checked after the
digest in
[Moser--Tardos, Theorem 1.1](../../../../library/set_systems/moser_tardos_2009_constructive_proof_general_lovasz_local_lemma/_index.md).
No computation or numerical search is used. The counting and inequalities are
author-recorded; a separate reviewer derived them independently, and another
checked the support formula, incidence count, uniform inequalities, dependency
graph, final factor of two, and source statement, finding no gap. This is
internal review, not external verification.

## 4. The same coloring can avoid small-vertex-excess cycles

Put

$$
T_0=\min\left(n-k,
 \left\lfloor\sqrt{\frac{k}{16\log(2n)}}\right\rfloor\right).
\tag{7}
$$

The two-coloring can simultaneously avoid every ternary cycle whose
union of vertices has size at most $k+T_0$, as well as all the joins
above. Here is a count covering **all** such cycles, not just manifolds
or decomposable cycles.

Fix a nonzero ternary cycle $z$ with exact vertex set $V$,
$v=k+t$, and support size $s$. Summing over vertices the number of
supported facets omitting each vertex gives $ts$. Some vertex $a$
is therefore omitted by at most $ts/v$ supported facets.

A cycle is uniquely determined by its coefficients on facets not
containing $a$. Indeed the boundary columns containing a fixed vertex
are independent: their rows obtained by deleting that vertex are private.
The difference of two cycles with the same coefficients off this star
must therefore be zero.

There are $M=\binom{v-1}k=\binom{v-1}{t-1}$ possible facets omitting
the anchor. For fixed $V,s$, the number of ternary cycles is at most

$$
v\sum_{h=1}^{\min(M,\lfloor ts/v\rfloor)}\binom Mh2^h
\leq2v(2M)^{ts/v}.                               \tag{8}
$$

This intentionally overcounts anchors and coefficient patterns. The
geometric-sum bound proves the last inequality, including the empty-sum
case. For $t\leq T_0$,

$$
\frac tv\log(2M)\leq\frac{t^2\log(2n)}k\leq1/16.
\tag{9}
$$

Every nonzero cycle has at least $k+1$ facets. Each of the $k$
ridges of one supported facet needs another supported facet to cancel
its boundary coefficient. These other facets are distinct: a different
$k$-set cannot contain two distinct ridges of the original one.

For a fixed face $I$, at most $n^t$ vertex sets of size $k+t$
contain it. Apply (8)--(9) and sum weights $e^{-s/2}$, first over
$s\geq k+1$, then $1\leq t\leq T_0$. The added local load is at
most

$$
B=\frac{2nT_0}{1-e^{-7/16}}
 \exp\bigl(T_0\log n-7(k+1)/16\bigr),            \tag{10}
$$

with $B=0$ if $T_0=0$. Because $\log n=o(k)$,
$T_0\log n=O(\sqrt{k\log n})=o(k)$ and
$\log(2nT_0)=o(k)$, so $B=o(1)$.

Deduplicate supports in the union of both families. If $J$ denotes
the right side of (5), their total local load is at most $J+B=o(1)$.
The proof in Section 3 applies unchanged. An explicit sufficient finite
condition, when $b=k/16-\log n>0$, is

$$
\tfrac12+2(J+B)\leq\log2-\frac{\log2}{k+1}.      \tag{11}
$$

It holds eventually in the stated regime. This extension is
author-recorded, including the anchor injectivity, floors, support
deduplication, and geometric sum; the separate reviewer described above
reviewed Sections 1--3 only.

## Consequence for the proof search

Any unbounded actual coloring theorem for the critical simplicial family
must use flat cycles outside this entire joined family, jointly with
whatever other supports are needed. Elementary boundaries, cross-polytope
boundaries, and all their disjoint joins alone cannot prove the required
lower bound. In the specific coloring furnished here, any remaining
monochromatic flat cycle is nonjoined and has vertex excess greater
than $T_0$. This is an existence statement about that coloring, not a
claim about every coloring. No arbitrary-color lower bound follows.
