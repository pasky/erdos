---
name: research/methods/finite_set_thresholds
title: Threshold and parameter tests for finite set systems
desc: Product-family, cube, coloring and packing tests distinguish exact finite deductions from the uniform bounds asked for in several set-system problems.
created: 2026-10-14T12:38:34Z
updated: 2026-10-14T12:38:34Z
---

***

These elementary author-recorded deductions by Plasma AI test specific
routes. Source results retain the qualifications stated below; no full
catalog resolution or independent verification is claimed.

## Spread does not remove the random-hitting logarithm

For [[problems/set_systems/E0020/_index|Problem 20]], a constant base in a
sunflower bound cannot be obtained just by deleting the logarithm in the
spread hypothesis of
[[../library/set_systems/bell_2021_note_sunflowers/theorem_3|Bell–Chueluecha–Warnke's Theorem 3]].
Their
[[../library/set_systems/bell_2021_note_sunflowers/lemma_4|Lemma 4]]
uses the following product family, credited there to Alweiss, Lovett, Wu and
Zhang. Partition a universe into $n$ classes of $s$ points and take every
transversal. There are $s^n$ members. Every fixed $t$-set belongs to zero or
$s^{n-t}$ members, so the family is $s$-spread. A random subset containing
each point independently with probability $\delta$ contains a transversal
exactly when it meets every class. The probability is

$$
\bigl(1-(1-\delta)^s\bigr)^n\longrightarrow0
\quad(n\longrightarrow\infty,\ s,\delta\text{ fixed},\ 0<\delta<1).
$$

This is an obstruction to a constant-spread random-hitting lemma. It is not
an obstruction to a constant-base sunflower bound: the family itself has
$s$ disjoint transversals. A successful route must change that intermediate
lemma or use a different way to obtain disjoint petals.

## A strict cube-counting threshold

Use the unrestricted map in
[[problems/set_systems/E0624/_index|Problem 624]], without imposing that
the image of a subset lie outside it. Suppose $n=2^h$, $h\ge2$, and the
map works at threshold $h$. On the subsets of every $h$-set it is a
surjection between sets of size $n$, hence injective. The empty set and
every pair of distinct singletons lie in some such cube. Their $n+1$
images must therefore all differ, a contradiction. Thus
$H(2^h)\ge h+1$. At nonpowers, $2^{H(n)}\ge n$ and integrality give
$H(n)>\log_2 n$, so the strict inequality holds for every $n\ge3$.

This proves only a unit gap at powers of two. The requested divergent gap
would require control when each cube has a fixed multiplicative surplus
of inputs over colors, where surjectivity no longer implies injectivity.
It also does not identify the extremal function for every extension of the
outside-the-input convention in the original Erdős–Hajnal source.

## Exactly three colors and failure of two colors

For uniformity $n\ge2$, the minimum number of edges of an exactly
3-chromatic hypergraph equals the minimum number of edges of a
non-2-colorable one, as used in
[[problems/set_systems/E0901/_index|Problem 901]].
To see this, choose an edge-minimal non-2-colorable hypergraph. Deleting an
edge $E$ gives a proper 2-coloring. The removed edge must be monochromatic;
give one of its vertices a new third color. Every other edge either keeps
its proper coloring or contains the unique third-colored vertex and at
least one other vertex, so remains nonmonochromatic. The resulting
hypergraph is exactly 3-chromatic. The opposite inequality is immediate.
This reconciles the extremal definitions; it improves no asymptotic bound.

## What maximal clique packing misses

For [[problems/set_systems/E0719/_index|Problem 719]], let $G$ have $e$
edges, and let $p$ edge-disjoint copies of $K_{r+1}^r$ be maximal. Deleting
their $(r+1)p$ edges leaves no such clique, whence

$$
p\ge\frac{e-\operatorname{ex}_r(n;K_{r+1}^r)}{r+1}.
$$

But the decomposition into those cliques and leftover single edges has
$e-rp$ pieces. The conjectured number of pieces requires the stronger
$p\ge(e-\operatorname{ex}_r(n;K_{r+1}^r))/r$. Maximality alone loses the
necessary factor. A new packing improvement is needed; the maximal-packing
argument is not a proof of the conjecture.

## A Latin-rectangle normalization boundary

Let $A_{k,n}$ denote the Godsil–McKay expression recorded on
[[problems/set_systems/E0725/_index|Problem 725]], for labeled rows,
columns and symbols. Taking logarithms gives

$$
\log\frac{A_{k,n}}{(n!)^k}
=n\sum_{i=0}^{k-1}\log(1-i/n)-\frac n2\log(1-k/n)-\frac k2.
$$

Taylor expansion, uniformly when $k/n\to0$, yields

$$
\log\frac{A_{k,n}}{(n!)^k}
=-\frac{k(k-1)}2
 +\frac{-2k^3+6k^2-k}{12n}
 +O\!\left(\frac{k^4+k^3}{n^2}\right).
$$

Indeed the sum of the cubic remainders is $O(k^4/n^2)$ after multiplication
by $n$, and the second logarithm contributes $O(k^3/n^2)$. Thus, for
$k\sim cn^{1/3}$ with fixed $c>0$,

$$
\frac{A_{k,n}}{(n!)^k e^{-\binom k2}}\longrightarrow e^{-c^3/6}.
$$

This compares formulas. Identifying $A_{k,n}$ with the actual count at
that boundary imports Godsil–McKay's theorem; its primary proof is not
inspected here. Even the pending extension recorded on the problem page
has $k=o(n)$ and leaves $k$ proportional to $n$ outside its scope.

## Uniformity reduction keeps the unbounded edge parameter

In [[problems/set_systems/E1178/_index|Problem 1178]], put $k=2,d=1$ in
[[../library/set_systems/conlon_2023_new_bound_brown_erdos_sos_problem/proposition_1_2|Conlon–Gishboliner–Levanzov–Shapira's Proposition 1.2]].
Writing $f_r(n,v,e)$ for the largest number of edges of an $r$-graph
without $e$ edges on at most $v$ vertices, it gives

$$
f_r(n,(r-2)e+3,e)
\le\left(\binom r3(e-1)+1\right)f_3(n,e+3,e),\qquad r,e\ge3.
$$

For each fixed $r,e$ the factor is constant. Hence the 3-uniform conjectured
upper bound implies the upper bound in every uniformity; the converse is
the case $r=3$. Isolated vertices reconcile “at most” with “exactly” the
forbidden vertex count in a sufficiently large host. The separately
recorded Brown–Erdős–Sós lower bound is still needed for equality of the
threshold. This is a specialization of the inspected source statement,
not an independent audit of its proof or the lower bound.

The reduction leaves all $e$ unbounded. The held upper theorem permits
$e+\lceil26\log e/\log\log e\rceil$ vertices, an excess that cannot be
rounded down to three. Neither a fixed-$e$ computation nor this uniformity
transfer settles the remaining universal parameter.
