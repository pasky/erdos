---
name: research/erdos_774/evidence/boundary_anchor
title: Exact boundary-anchor exclusion for the Grow source
desc: A checked finite certificate rules out universal three-color anchors at the remaining simplex boundary, including after all exact scalar encodings.
tags: [E0774, proved, computational, obstruction]
sources: []
created: 2026-09-18T00:32:00Z
updated: 2026-09-18T00:32:00Z
---

# Exact boundary-anchor exclusion for the Grow source

[[research/erdos_774/evidence/_index|..]]

***

## Theorem and scope

Let $A=\{4,5,9,11,13,27,30,33,81,85,89,243,248,253\}$ and
$G=A\otimes S_3$. Then $\chi(G)=3$ and $U_3(G)=\{0\}$.
Every linear scalar encoding preserving all ternary relations exactly also
has $U_3=\{0\}$. Here $U_q$ is the universal signed-span set in
[the tensor coloring page](../../routes/tensor_coloring.md).

Together with [the large-arity obstruction](../../routes/anchor_gluing.md),
this means that **no arity $m\geq3$** supplies a reusable three-color
anchor from this particular Grow deletion, even after exact scalar
realization. This retires the repeated gluing of this source, not every
anchored construction. The source is the deletion of the point $3$ from
the [Grow–Whicher example](../grow_whicher/_index.md).

## Exact finite verification

Run, from the repository root,

```sh
uv run --no-sync python wiki/research/erdos_774/evidence/boundary_anchor/main.py
```

The [checker](main.py) reads the fixed
[certificate](assets/boundary_anchor_certificate.json). It uses the
standard library and the shared root `tools` checker, performs no search,
and finishes in a few seconds. Its named checks verify:

- all $2^{14}=16384$ source subsets and exactly 56 proper two-color classes;
- the complete $U_2(A)$, of size 501 including zero;
- 12,730 canonical nonzero candidate orbits;
- 83 coloring templates, all six ray permutations of each, and their 498
  proper palette bridges;
- exclusion of every candidate, with an independent ordinary-integer-set
  recomputation of all colorings and one exclusion per candidate.

A failed clause exits nonzero. The author ran the checker on the retained
certificate; that run is author-recorded, not an independent review.

## Discovery of the certificate

The certificate was found by finite constructive sampling, which is not
part of the proof or of the normal run. With all $2^{14}$ source subsets
tabulated and the exact layer-intersection test, the searches were:
100,000 unstructured source assignments and 300,000 triples of retained
proper partitions (seed 42; 28,410 retained partitions; no proper tensor
coloring found); all 84 single-point recolorings of one palette (no valid
move); all 128 splits of one seven-point class and then all 7,168 splits
across the 56 source classes (the inherited anchor survived); all
$56\cdot128\cdot56=401408$ mixed-middle splits (a coloring omitting $3t_1$
was found); an initial elimination over 30,000 split-family and 30,000
refinement-family samples (seed 813743), reducing the 12,730 candidate
orbits to 87 and then 54; an expanded elimination of at most 200,000
outer-row proposals (seed 666013), each admitted pair tested against all
56 middle partitions, succeeding at proposal 42,927 after 4,087 admissions
and 228,872 proper-coloring checks; and a reverse compression scan of at
most 1,040 reducing witnesses, retaining the 83 templates.

The families were, for proper pairs $P\sqcup Q=R\sqcup T=V\sqcup W=A$:
splits $P=a\sqcup b$ with rows $(a,b,Q),(R,T,0),(b,a,Q)$; refinements
$(P\cap R,Q\cap R,T),(V,W,0),(P\cap T,Q\cap T,R)$; and expanded proposals
choosing proper outer pairs $P,Q$ and $P',Q'$, splitting their first
classes into $a,b$ and $a',b'$ oppositely on their intersection, admitting
only when $a\cup a'$ and $b\cup b'$ are dissociated, and testing
$(a,b,Q),(R,T,0),(a',b',Q')$ for every middle pair. A separate omission
check tested the three scalar possibilities $-3,30,-36$. The fixed
certificate and the checker replace all of these searches for verification.

## Candidate reduction

Use $t_1=(1,0),t_2=(0,1),t_3=(-1,-1)$. A color with layers
$C_1,C_2,C_3$ is dissociated exactly when the layers are dissociated
and their signed spans intersect only at zero. Also

$$
(x,y)\in\Sigma\Bigl(\bigcup_j C_jt_j\Bigr)
\iff \exists a\in\Sigma(C_3):
       a+x\in\Sigma(C_1),\quad a+y\in\Sigma(C_2). \tag{1}
$$

Palette colorings with any given source two-color class on any pair of rays
force a universal vector to satisfy $x,y,x-y\in U_2(A)$. Ray permutations
and overall sign reversal give a representative with $x>0$ and
$0\leq2y\leq x$, unless the vector is zero. This gives the 12,730
candidates. For each, (1) fails on a class of a symmetry-expanded witness.
The source anchor $3$ and the palette upper bound prove $\chi(G)=3$.

## Why arbitrary exact scalar encodings are covered

Join color classes by an edge when their supports are disjoint. If an exact
linear encoding $L$ had a universal nonzero scalar anchor $a$, choose
$v_C\in\Sigma(C)$ with $L(v_C)=a$ in each class. For disjoint
$C,D$, their representation difference is a ternary sum, so exactness
forces $v_C=v_D$. All representatives therefore coincide on each
connected component of this class graph.

All palettes with rows

$$
(P,0,Q),\qquad(R,T,0),\qquad(0,P',Q'), \tag{2}
$$

where the displayed pairs are proper two-partitions of $A$, lie in one
component: the three classes of each coloring are disjoint, and changing a
single layer leaves its absent color class unchanged. This family includes
all two-ray classes used to bound candidates.

Every certificate template shares its third class with a palette (2). Each
ray-permuted template shares a class with a permuted palette; global color
relabeling returns that palette to (2). All these bridges and relabelings
are explicitly checked. Thus all bounding classes and all symmetry-expanded
witnesses share one vector representative of $a$. The candidate exclusion
forces that vector to be zero, a contradiction. Neither overlapping-support
subtraction nor symmetry of $L$ is assumed.
