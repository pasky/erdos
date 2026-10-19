---
name: research/erdos_774/routes/anchor_gluing
title: Small-loss anchor gluing and its iteration obstruction
desc: Small-loss gluing improves three-color obstructions, but the Grow source has a checked no-anchor obstruction at every simplex arity, including the boundary.
tags: [E0774, proved, construction, incomplete]
sources: []
created: 2026-09-18T00:04:10Z
updated: 2026-10-14T00:26:52Z
---


# Small-loss anchor gluing and its iteration obstruction

***

## The scalar gluing lemma — proved

Let $B\subset\mathbb Z\setminus\{0\}$ be finite, with hereditary
dissociation constant $\delta$ and coloring number $q\geq2$. Suppose
$w\ne0$, $w\notin B$, and $\chi(B\cup\{w\})=q+1$. In every
proper $q$-coloring of $B$, each color class signed-spans $w$:
otherwise adding $w$ to that class would give a proper coloring of the
extension.

Take the $m$-simplex directions $t_1,\ldots,t_m$, so
$\sum_it_i=0$ and any $m-1$ of them are rationally independent, and
put $G_m=\bigcup_i Bt_i$. For $m\geq q+1$,

$$
\eta(G_m)\geq\delta(1-1/m),\qquad\chi(G_m)=q+1. \tag{1}
$$

For extraction, omit a least-populated block of any given subset, and extract
within the other blocks. The independent directions make the union
dissociated. For the lower coloring bound, any proper $q$-coloring would
represent $w$ in each color in every block; summing those representations
against $\sum t_i=0$ gives a monochromatic relation. For the upper bound
use $q+1$ colors and a proper $q$-palette in every block, arranging
that each color is absent from at least one block. Each color then uses at
most $m-1$ independent directions.

## Exact finite input and improvement

For the [checked Grow–Whicher set](../evidence/grow_whicher/_index.md) of
[Grow–Whicher, *Finite unions of quasi-independent sets*](../../../../library/analysis/grow_whicher_1984_finite_unions_quasi_independent_sets/_index.md),
the finite input of this route, take
$B=E\setminus\{3\}$, $w=3$, $q=2$. The standard-library exact
certificate proves

$$
\eta(B)=7/13,\qquad\chi(B)=2.
$$

A proper partition is
$\{5,9,11,13,30,85,243\}$ and
$\{4,27,33,81,89,248,253\}$. Hence (1) gives explicit three-color
obstructions with

$$
\eta(G_m)\geq\frac7{13}(1-1/m)\longrightarrow\frac7{13}>\frac12.
$$

This is an improvement of a finite extraction/coloring gap, **not** unbounded
coloring. The finite positive-integer realization lemma applies to these
blocks without changing either parameter.

One explicit positive realization is

$$
\bigcup_{i=0}^{m-2}4525^i B
\ \cup\ (1+4525+\cdots+4525^{m-2})B.
$$

Here $\sum_{a\in B}a=1131$; every coefficient in a signed block sum has
absolute value at most $2262<4525-1$, so the leading-digit argument prevents
additional signed relations. The sign change of the last simplex direction
preserves relation supports. For every $m\geq15$, the guaranteed extraction
proportion is at least $98/195>1/2$, while the coloring number is exactly three.

## Universal anchors do not automatically propagate — proved

For $m\geq q+2$, $G_m$ has no nonzero vector signed-spanned by
every color class of every proper $(q+1)$-coloring. In fact the same is
true after **any linear scalar encoding that preserves the ternary relation
system exactly**, not just a generic encoding.

Fix a proper $q$-partition $B=P_1\sqcup\cdots\sqcup P_q$.
For each $q$-element set of blocks $S$, there is a proper palette
coloring in which the new color class is exactly
$C_S=\bigcup_{i\in S}P_1t_i$: assign its other $q-1$ old classes
to old colors in those blocks, omitting a different old color in each block
of $S$, and use only the old colors elsewhere. Every color is absent
from a block, so the coloring is proper.

Fix also a $q$-element set $T$ of blocks. Another proper palette
coloring has new color $D=\bigcup_{i\in T}P_2t_i$. This set is disjoint
from every $C_S$.

If a universal nonzero anchor existed after an exact scalar encoding $L$,
choose a signed representation $y$ of it on $D$, and for each $S$
a signed representation $x_S$ on $C_S$. The supports are disjoint, so
$L(x_S-y)=0$ is a ternary relation on $G_m$. Exact preservation
forces $x_S=y$ already in the vector configuration. This common vector
belongs to

$$
\bigcap_{|S|=q}\operatorname{span}\{t_i:i\in S\}=\{0\}.
$$

For the last equality, choose $q+1\leq m-1$ independent simplex rays
and intersect the spans of their $q$-subsets. This contradicts a nonzero
scalar anchor. Thus deliberately collapsing coefficient-two differences
cannot repair this gluing while preserving all ternary relations.

## Boundary case: the Grow source is excluded

For the Grow deletion above, $m=q+1=3$ is also excluded by
[an exact finite certificate](../evidence/boundary_anchor/_index.md). It proves
$U_3(B\otimes S_3)=\{0\}$, even after every exact ternary-preserving
scalar encoding. Thus no $m\geq3$ gives a reusable anchor from this source.

A different source is not ruled out. Two sharper tools are available but
neither implies anchor survival: the defect estimate below and
[quadratic-loss primitive-anchor gluing](anchored_phase_gluing.md).

Let $r_w^\perp(F)$ be the largest size of a subset of $F$ whose image
in the quotient by $\mathbb Qw$ is dissociated, and set
$\Delta_w(F)=r(F)-r_w^\perp(F)$. Glue $m$ copies of a vector source
by quotienting their direct sum by the single relation
$w_1+\cdots+w_m=0$. For layers $F_i$ the elementary bound is

$$
r_G\Bigl(\bigcup_i F_i\Bigr)
\geq\sum_i r(F_i)-\min_i\Delta_w(F_i). \tag{2}
$$

Choose an independent-modulo-$w$ subset in one block and ordinary
dissociated subsets in the others. Any cross-block relation would force
their block sums to be a common multiple of $w$; the special block rules
that out. For scalar sources the special quotient is zero and (2) reduces
to whole-block deletion. An invariant making these defects summably small
**while preserving anchors** in later gluings is not established.

Indeed, for $D=B^{\oplus r}$ and diagonal $w=(3,\ldots,3)$,
omitting a least-rank coordinate summand before quotienting by $\mathbb Qw$
gives $\Delta_w(F)\leq\min_j r(F_j)\leq r(F)/r$.
Its boundary three-copy gluing is $B\otimes S_{3r}$, whose universal
three-color anchor set is zero for every $r\geq1$, by the large-arity
proof and the new boundary certificate. Small relative defect alone is
therefore insufficient.
