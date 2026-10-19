---
name: research/erdos_132/deletion_criticality
title: Exact obstructions to deletion-criticality arguments
desc: |
  A single spanning bicyclic minimum graph can account for every deletion;
  this persists with nonstar diameter and a sublinear distance palette.
sources: []
research_state: closed
created: 2026-09-23T07:45:00Z
updated: 2026-09-24T22:12:56Z
---


# Exact obstructions to deletion-criticality arguments

***

Suppose a hypothetical $R=1$ configuration is minimal by cardinality.
Write a nondiametral rich multiplicity as $m_A(r)=n+e_r$, $e_r\ge1$.
If deleting $v$ retains the diameter and leaves at least five points,
minimality requires some nondiametral class to become rare. No rich
class disappears on deleting one vertex. Its new multiplicity is at
most $n-1$ precisely when

$$d_r(v)\ge e_r+1.$$

Thus the critical vertex sets $\{v:d_r(v)\ge e_r+1\}$ cover $A$ when
the diameter survives every deletion. The constructions below show
that this condition, even its induced-subset strengthening and a small
total palette, does not itself supply a contradiction. They are not
counterexamples to [Problem 132](../../problems/distance_problems/E0132/_index.md).

## A simple nonstar-diameter example

For an integer $q\ge1$, let $L=q+\sqrt3$ and

$$A_q=\{(0,\pm1/2),(L,\pm1/2)\}
\cup\{(\sqrt3/2+j,0):0\le j\le q\}.$$

There are $n=q+5$ points. A left corner's squared distance to the
$j$-th path point is $1+j^2+\sqrt3j$, equal to one only for $j=0$;
the right-corner formula is the reversed one. Distances along the path
are positive integers. All remaining corner-to-corner distances exceed
one except the two vertical sides. Thus the minimum-distance graph is
exactly two unit equilateral triangles joined by a $q$-edge path, with

$$m_A(1)=q+6=n+1.$$

Every vertex has degree two except the two path endpoints, which have
degree three. The only diameter pairs are the two rectangle diagonals,
which are disjoint. Consequently every single-vertex deletion retains
the diameter but makes the unit class rare with the correct new threshold
$n-1$.

More generally every proper induced subgraph of this unit graph is a
pseudoforest. To retain both cycles in one component requires every
vertex of both triangles and their entire joining path, hence all
vertices. Thus every deletion for which unit pairs remain makes that
class rare relative to the retained order. The other distance classes
prevent this family from being an Erdős counterexample.

## The same obstruction with a sublinear palette

The following integer-coordinate family additionally has $q(A)=o(|A|)$.
Let $K\ge3$ be odd. Include all row points $(x,4j)$ for
$0\le x,j\le K$. For $0\le j<K$, join row $j$ to row $j+1$ by the
three intermediate lattice points at $x=K$ for even $j$, and $x=0$
for odd $j$. Close this path by adding $(-1,0)$, $(-1,4K)$, and
all $(-2,y)$ for $0\le y\le4K$. Finally attach a unit square at
$p=(K,4)$, adding

$$(K+1,4),\quad(K+1,5),\quad(K,5).$$

The rows are four units apart. A connector touches its two endpoint
rows only at the indicated endpoints; successive connectors alternate
between columns separated by at least three. The return column is two
units left of column zero, so it touches only its two horizontal closing
segments. The added square meets only $p$: the connector above row four
is at $x=0$, while the connector below is at $x=K$. These observations
exhaust horizontal and vertical unit pairs in the integer lattice.
Thus the unit graph is exactly a cycle with an attached square sharing
one vertex. Its order and edge count are

$$n=(K+1)^2+3K+(4K+1)+2+3=K^2+9K+7,
\qquad m_A(1)=n+1.$$

All vertices have degree two except $p$, whose degree is four. Every
proper induced subgraph is a pseudoforest, by the same two-cycle argument.

The original cycle lies in $[-2,K]\times[0,4K]$ and contains its four
corners. Its only diameters are the two rectangle diagonals, with

$$D^2=(K+2)^2+16K^2.$$

The added point $(K,5)$ is strictly inside this rectangle. Each of the
other two added points has squared distance to any original point at
most

$$(K+3)^2+(4K-4)^2
=D^2-(30K-21)<D^2.$$

Their mutual and square-edge distances are also smaller. The only
full-set diameter pairs therefore remain the two disjoint diagonals.
Every single deletion retains the diameter and makes the unit class rare.

All squared distances are sums of two integer squares bounded by $D^2=O(K^2)$.
The set of sums of two squares has density zero, so $q(A)=o(K^2)=o(n)$.
Here is the needed classical density argument. For every prime
$p\equiv3\pmod4$, representability forces an even $p$-adic valuation.
For any finite set of these primes, the proportion of admissible integers
has limit $\prod_p p/(p+1)$, by the Chinese remainder theorem and a
geometric-series tail estimate. These products tend to zero because
$\sum_{p\equiv3(4)}1/p=\infty$. One standard short verification of the
last fact uses, for $s>1$,

$$\frac{\zeta(s)}{L(s,\chi_4)}
=(1-2^{-s})^{-1}\prod_{p\equiv3(4)}
\frac{1+p^{-s}}{1-p^{-s}}.$$

Convergence of the reciprocal-prime sum would bound the right side as
$s\downarrow1$, while $\zeta(s)\to\infty$ and
$L(s,\chi_4)\to1-1/3+1/5-\cdots=\pi/4$. This proves the asserted
density-zero consequence without a quantitative counting theorem.

The [finite certificate](evidence/util/continuation_checks.py) checks the
coordinate construction, degrees, order, and two diameters at $K=3,5,9$;
the preceding argument treats every odd $K\ge3$.

## Scope

A spanning critical rich class, proper-induced-subset rarity of that
class, nonstar diameter, and even $q=o(n)$ are jointly compatible with
planar geometry. These examples do not make the remaining classes all rich.
In particular,
the integer-coordinate meanders satisfy the proved
[dyadic bound](dyadic_distances.md), $R(A)\ge\lceil\log_2 n\rceil$.
Any successful deletion induction must use joint multiplicity constraints
on the rest of the distance palette, rather than the critical cover alone.
The author checked the constructions and all stated implications; the
argument is author-recorded, and no claim of bounded total rarity is
made.
