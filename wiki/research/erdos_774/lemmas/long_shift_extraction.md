---
name: research/erdos_774/lemmas/long_shift_extraction
title: Uniform extraction bounds long-shift prescribed coloring
desc: Full k-edge increasing-path relations on pair labels force a signed-cube subset, bounding n by O_delta(k log k) under uniform full extraction; an elementary binary rank theorem also constrains their realizations.
tags: [E0774, shift, extraction, coloring, proved, scoped-obstruction]
sources: []
created: 2026-09-19T01:55:00Z
updated: 2026-09-19T01:55:00Z
---


# Uniform extraction bounds long-shift prescribed coloring

***

This closes a varying-relation-length possibility outside the earlier
[high-fractional full-shift regime](../routes/shift_simplicial_gain_checks.md).
The conclusion concerns the **prescribed** supports. It is not a coloring
of every additional ternary relation in a realization.

## 1. Statement

Let $k\geq2$, and label the pairs $1\leq i<j\leq n$ by distinct
nonzero rational vectors $a_{ij}$. Suppose that, for every increasing

$$
b_1<b_2<\cdots<b_{k+1},
$$

the $k$ consecutive pair labels support a relation whose every
coefficient is $+1$ or $-1$. The signs may vary with the path.
If the whole vector family has hereditary full-dissociation extraction
constant at least $\delta>0$, then

$$
\boxed{n\leq k+
\frac{2(k-1)\log_2(2(k-1))}{\delta}.}            \tag{1}
$$

Its prescribed long-shift hypergraph $H(n,2,k)$ consequently satisfies

$$
\boxed{\chi(H(n,2,k))\leq
 2+\left\lceil\log_2(1+2/\delta)\right\rceil.}   \tag{2}
$$

For each fixed $\delta$, this prescribed chromatic number is at most
two for all sufficiently large $k$.

## 2. The signed-cube argument

There is nothing to prove in (1) if $n\leq k$. Otherwise fix the
last $k$ indices $b_2=n-k+1<\cdots<b_{k+1}=n$. Every one of the
$m=n-k$ distinct labels

$$
F=\{a_{i,b_2}:i<b_2\}
$$

is a signed sum of the $d=k-1$ fixed suffix labels. Normalize the
coefficient of the first label in its path relation to $+1$.

Choose a dissociated $B\subseteq F$ of size $t\geq\delta m$, and
fix one signed-cube representation of each of its members. Its $2^t$
subset sums are distinct. In any one of the $d$ representation
coordinates, the subset-sum coefficients occupy an integer interval
of length $t$, hence at most $t+1$ values. Thus

$$
2^t\leq(t+1)^d.                                 \tag{3}
$$

For $d=1$, (3) gives $t\leq1$. For $d\geq2$, it implies
$t\leq2d\log_2(2d)$: otherwise $x=t/d>2\log_2(2d)\geq4$ would give

$$
x\leq\log_2(dx+1)\leq\log_2(2d)+\log_2x
\leq\log_2(2d)+x/2<x,
$$

a contradiction. Combining with $t\geq\delta m$ proves (1).
Only full dissociation of $B$, not a fixed-order substitute, was used.

## 3. Exact coloring of the prescribed hypergraph

For $n\geq2$,

$$
\chi(H(n,2,k))=\lceil\log_k n\rceil.             \tag{4}
$$

For the upper bound, encode the $n$ indices by distinct increasing
lexicographic words in $[k]^r$, and color the pair $(i,j)$ by its
first differing coordinate. Along a monochromatic increasing path that
coordinate strictly increases at every edge, so there are fewer than
$k$ edges.

Conversely, an $r$-coloring without a monochromatic $k$-edge path
assigns to every index the vector of the longest monochromatic path
lengths ending there. Each coordinate is in $\{0,\ldots,k-1\}$.
For $i<j$, the color of $(i,j)$ has a strictly larger coordinate
at $j$, so the $n$ vectors are distinct. Hence $n\leq k^r$.

Since $\log_2(2(k-1))\leq k-1$, (1) gives
$n\leq(1+2/\delta)k^2$, and (2) follows from (4).
The sharper $n=O_\delta(k\log k)$ gives $n\leq k^2$ eventually.

The abstract long-shift supports themselves have a uniform hereditary
independence fraction of at least $1/4$: independently label each
underlying index source or sink, and retain pairs directed from a source
to a sink. These contain no two consecutive edges, and every pair is
retained with probability $1/4$. The new obstruction is precisely that
this abstract fact does not transfer to **full dissociation** of vector
labels satisfying all the path relations.

## 4. An elementary binary-rank constraint on realizations

Call $(i,j)$ active if it occurs in some increasing $k$-edge path;
equivalently $j-i\leq n-k$. For $n\geq2k+1$, the binary matrix
of path supports, restricted to active columns, has zero nullspace if
$k$ is odd, and the constant vectors as its one-dimensional nullspace
if $k$ is even.

**Proof.** Let $x_{ij}\in\mathbb F_2$ sum to zero along every path.
For $j\leq n-k+1$, fix a suffix of $k-1$ edges after $j$ and
vary the first vertex. This shows $x_{ij}=y_j$, independent of $i<j$.
Precede any $k$-subset of $\{2,\ldots,n-k+1\}$ by vertex (1).
Its $y$-sum is zero. This ground set has at least $k+1$ elements;
comparing subsets gives $y_j=c$ for all $j$, with $kc=0$.

The symmetric last-vertex argument gives one constant $c'$ on all
edges with $i\geq k$, also with $kc'=0$. Edge $(k,k+1)$ belongs
to both regions, so $c=c'$. Any remaining active edge has $i<k$
and $j>n-k+1$. In a path containing it, all other edges are in the
previous two regions. Its equation gives $x_{ij}+(k-1)c=0$, whence
$x_{ij}=c$. This proves the assertion. $\square$

Every signing of the path rows reduces to this same binary matrix.
Its rational rank is at least its binary rank. Thus odd $k$ in this
range permits no nonzero rational realization at all on active edges.
For even $k$, a nonzero realization has all active labels collinear.
Its primitive integer coefficient vector reduces to a nonzero binary
constant vector, so all its entries are odd. This is not by itself a
full dissociated coloring theorem.

## Checks and finite evidence

The extraction argument, constants, prescribed coloring, and binary proof
are author-recorded; a separate reviewer derived them independently. A
single finite GF(2) rank diagnostic preceded the general proof. Its exact
range, outputs, and checker are retained in the
[binary rank probe](../evidence/long_shift_gf2/_index.md). No numerical
result is needed for the proofs.
