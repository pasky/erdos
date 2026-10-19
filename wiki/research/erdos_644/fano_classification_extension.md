---
name: research/erdos_644/fano_classification_extension
desc: A fractional matching theorem extends the exact Fano classification of bad seven-tuples to ground size below 9k/5.
tags: [proved, structural-lemma, restricted-regime]
sources: []
created: 2026-09-23T06:00:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/fano_classification_extension

***

This improves the $n<30k/17$ classification in
[Coding refinement](coding_refinement.md), but does not improve the
unrestricted upper bound for Problem 644. It classifies the degree-four
points in a hypothetical bad seven-tuple, not an arbitrary ambient family.

## The fractional matching input

We use the following case of Füredi's fractional matching theorem:
an intersecting 3-uniform hypergraph containing no Fano plane has
fractional transversal number at most two. More generally, a
$q$-uniform hypergraph containing no projective plane of uniformity
$q$ has $\tau^*\le(q-1)\nu$.

The latter statement was checked in the proof of Proposition 2.4, p. 8, of
[Aharoni--Zerbib, *A generalization of Tuza's conjecture*,
arXiv:1611.07497v7](https://arxiv.org/pdf/1611.07497), where it is attributed to
[Füredi, *Maximum degree and fractional matchings in uniform hypergraphs*,
Combinatorica 1 (1981), 155--162](https://doi.org/10.1007/BF02579271). Only the
intersecting, 3-uniform specialization is needed below.

## Exact classification below nine fifths

**Theorem.** Let $A_1,\ldots,A_7$ be $k$-subsets of an $n$-point set,
with no transversal of size at most two. If

$$
n<\frac95k,
\tag{1}
$$

then the degree-four spectra of the tuple are exactly the seven caps
of a Fano plane on its row indices, and every cap occurs.

**Proof.** Since $n<2k$, any two rows intersect. A point occurring in
at least five rows could therefore be supplemented by one point
meeting the remaining at-most-two rows. Thus every point has degree
at most four. Put

$$
D=4n-7k,\qquad N=\{v:\deg(v)<4\}.
$$

The incidence count gives

$$
D=\sum_v(4-\deg(v)),\qquad |N|\le D.
\tag{2}
$$


For each degree-four point, take the triple of row indices it misses.
The collection $J$ of these triples is intersecting: two disjoint
missing triples would give a two-point transversal. It is nonempty,
since otherwise $7k\le3n$, contrary to (1).

Suppose $J$ has no Fano plane. The fractional matching theorem gives
nonnegative weights $y_1,\ldots,y_7$ with total at most two, and with
$\sum_{i\in L}y_i\ge1$ for each $L\in J$. Summing over the
degree-four points, and noting that row $i$ misses precisely $n-k$
ground points, gives

$$
n-|N|
\le\sum_{i=1}^7 y_i\,|\{v:\deg(v)=4,\ v\notin A_i\}|
\le2(n-k).
\tag{3}
$$

But (2) implies $n-|N|\ge7k-3n$. Together with (3), this yields
$9k\le5n$, contradicting (1).

Hence $J$ contains all lines of a Fano plane. No additional triple can
intersect all seven lines. Indeed, represent a nonline triple by
linearly independent nonzero vectors $a,b,c\in\mathbb F_2^3$; the
line $\{a+b,a+c,b+c\}$ is disjoint from it. Since $J$ is intersecting,
it consists of exactly the seven Fano lines. Taking complements proves
the theorem. $\square$

## Consequence for threefold symmetric differences

The spectrum count in
[Coding refinement](coding_refinement.md#a-threefold-xor-criterion)
now applies throughout (1). A degree-three spectrum cannot be a Fano
line, since its complementary cap occurs. For each Fano line $L$, put
$X_L=\mathop{\triangle}_{i\in L}A_i$. The numbers of lines meeting
a spectrum oddly, for degrees $0,1,2,3,4$, are respectively
$0,3,4,3,0$, where the degree-three case is a nonline and the
degree-four case a cap. Each count is at most three times the
corresponding deficiency $4-\deg(v)$. Therefore

$$
\sum_{L}|X_L|\le3D,
\qquad \min_L|X_L|\le\frac37(4n-7k).
\tag{4}
$$

In particular, for an arbitrary $k$-uniform family on $n<9k/5$
points, the sufficient condition

$$
\min_{A,B,C\in\mathcal H}|A\triangle B\triangle C|
>\frac37(4n-7k)
\tag{5}
$$

implies $P_7$. Repetitions are allowed in the minimum.

This extends the validity range of the sufficient criterion, not the
range of the polynomial obstruction or narrow-ground upper bound in
[Forbidden distances](forbidden_distances.md): their separate entropy
estimate still has its stated hypotheses. Neither (1) nor (5)
establishes either unrestricted asymptotic assertion.
