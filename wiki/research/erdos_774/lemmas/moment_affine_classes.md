---
name: research/erdos_774/lemmas/moment_affine_classes
title: Exact dissociation criterion for affine Boolean classes
desc: An affine cube class is dissociated for degree-k moments exactly when its restricted moment columns are rationally independent; a missing Fourier coset gives an explicit ternary relation.
tags: [E0774, Boolean-moments, coloring, proved, incomplete]
sources: []
created: 2026-09-18T23:43:00Z
updated: 2026-09-19T00:48:35Z
---


# Exact dissociation criterion for affine Boolean classes

***

This is an actual ternary-relation theorem, but for a restricted class of
colorings. It does not establish unbounded coloring under arbitrary
partitions of the [moment configuration](../routes/boolean_moments.md).

## 1. Fourier-support certificate

Identify the physical cube and its Walsh frequency group with
G=F_2^d. Write B_k={a in G:|a|<=k}, r=|B_k|, and n=2^d.
For a nonempty physical subset C, let F be the Fourier support of 1_C.
If B_k+F is not all of G, choose w outside that sumset. Then

$$
 f(x)=\chi_w(x)1_C(x)
 \tag{1}
$$

is a nonzero ternary relation among the degree-at-most-k moment columns
indexed by C. Indeed its Fourier support is w+F, disjoint from B_k;
this is exactly the vanishing of every Walsh moment through degree k.
Walsh and monomial rows have the same rational row space. The coefficients
in (1) are explicitly zero or plus/minus one, not merely rational.

In particular, every nonempty dissociated C must satisfy

$$
 |\operatorname{supp}\widehat{1_C}|\,r\ge n.
 \tag{2}
$$

This follows from |B_k+F|<=r|F|. No claim that a finite palette bounds
the Fourier support of its color indicators is made.

## 2. Exact affine-coset theorem

Let H<=G be a frequency subspace and let C=a+H^perp be any one of its
physical syndrome classes. The following are equivalent:

1. The moment columns on C are dissociated.
2. Those columns are rationally independent.
3. Every H-coset in G meets B_k, or equivalently B_k+H=G.

More precisely,

$$
 \operatorname{rank}_{\mathbb Q}E_{d,k}|_C
 =|\{b+H:b\in B_k\}|.
 \tag{3}
$$

To prove (3), restrict Walsh characters to C. Two frequencies restrict
to the same character of H^perp, up to a nonzero sign from a, exactly
when they differ by H. The distinct restricted characters are orthogonal
and form the full character basis of C. Thus the restricted rows span
exactly the number of frequency cosets displayed in (3). The rank is
the same over the rationals because the row matrices are rational.

If every frequency coset is met, this rank is |C| and gives (2), hence
(1). If w+H misses B_k, the Fourier support of 1_C is precisely H,
with coefficients |H|^(-1)chi_h(a). Formula (1) therefore supplies a
nonzero ternary relation, disproving (1). This proves all implications.

Equivalently, the binary linear code H must have covering radius at most
k: every frequency must be within Hamming distance k of H. This is just
a reformulation of (3), not an imported coding-theoretic assertion.

## 3. Consequences for parity palettes

A coloring by all h independent linear parity bits has |H|=2^h colors,
each an affine coset of H^perp. It is proper exactly when B_k+H=G.
Consequently it needs at least

$$
 2^h\ge n/r.
 \tag{4}
$$

At the surviving critical boundary r/n tends to zero. Thus every fixed
linear-parity palette eventually has an explicit monochromatic ternary
relation. In fact each of its nonempty classes has one whenever
2^h r<n. The same rank formula says that any dissociated affine subspace
has at most r points. Affine subspaces cannot supply positive-density
extraction in this window.

## 4. Explicit trades for every fixed finite-abelian checksum palette

There is a separate extension beyond linear parity colors. Let Q be a
finite abelian group, let g_1,...,g_d lie in Q, and suppose the color is
any function of the checksum sum_i g_i x_i. Let z count the zero g_i.
Partition the remaining indices by the inversion-orbits {g,-g}, pair
indices within each orbit, and leave u indices unpaired. Thus u is the
number of orbits with odd multiplicity.

For a pair i,j with g_j=g_i, use the factor x_i-x_j. Its nonzero inputs
10 and 01 have the same checksum g_i. For a pair with g_j=-g_i, use
1-x_i-x_j. Its nonzero inputs 00 and 11 have checksum zero. If g_i=-g_i,
either construction works. For each unpaired index h use 1-x_h, and
leave zero-increment coordinates unrestricted. The product p of all
these factors is nonzero, takes only values zero and plus/minus one,
and has a constant checksum on its support. Its degree is

$$
 t=(d-z+u)/2.
$$

Multiplication by full parity gives f=chi_[d]p, whose Fourier frequencies
all have weight at least d-t. Hence f is an explicit monochromatic
ternary moment relation whenever

$$
 \boxed{(d-z+u)/2\leq d-k-1.}
 \tag{5}
$$

Let tau be the number of inversion-orbits in Q minus {0}. Then u<=tau,
so the group-only condition tau<=d-2k-2 suffices. Explicitly,
tau=(|Q|+|Q[2]|-2)/2, where Q[2]={g:2g=0}; for a cyclic group of order
q, tau=floor(q/2). At the critical boundary d-2k-2 tends to infinity,
so every fixed finite-abelian checksum palette eventually fails,
regardless of its increments or the function assigning final colors.

This proof produces the required signs directly. It uses no identification
of rational or binary dependence with dissociation. It does not apply to
an arbitrary coloring merely because that coloring has finitely many
values: a fixed-size additive checksum representation is an additional
hypothesis.

## 5. Exact remaining scope

These statements neither bound arbitrary colorings nor rule out nonlinear
dissociated sets of positive density. General color indicators can have
full Fourier support even with only two colors. Passing from (4) to an
arbitrary-color lower bound would require an additional theorem, which is
not proved here. The affine criterion and checksum construction received
internal checks; no computation or external review enters the proofs.
