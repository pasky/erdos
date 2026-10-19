---
name: research/erdos_132/rich_degree_profiles
title: Rich-distance degree profiles and concentric circles
desc: |
  Under bounded rarity, a positive-sized common rich-degree profile forces
  a positive circular fraction; no such profile is forced in general.
sources: []
research_state: closed
created: 2026-09-23T05:12:01Z
updated: 2026-09-24T22:12:56Z
---


# Rich-distance degree profiles and concentric circles

***

This records the checked part of the partial-permutation and equitable-partition
approach. It does not resolve either unrestricted assertion of
[Problem 132](../../problems/distance_problems/E0132/_index.md).

For $p\in A$ and an occurring distance $r$, put

$$d_r(p)=|\{q\in A:|p-q|=r\}|.$$

The **rich-degree profile** of $p$ is the vector of these degrees indexed
only by distances having more than $n=|A|$ unordered pairs. No assumption
of a group action or of an equitable partition is made below.

## Profile lemma

Suppose $R(A)\le K$ and $S\subseteq A$ has size $\delta n>0$, with
all its points having the same rich-degree profile. Put

$$L=\lfloor4K/\delta\rfloor,\qquad B=\binom{L+K}{K}.$$

There is a subset $T\subseteq S$ of size at least $\delta n/(2B)$
on which the distance to the centroid of $A$ is constant. If $|T|\ge2$,
it lies on a positive-radius circle centered at that centroid. In all
cases some positive-radius circle contains at least $\delta n/(2B)$
points of $S$, allowing an arbitrary circle through a singleton when
necessary.

**Proof.** The total degree in the rare classes satisfies

$$\sum_{p\in A}\sum_{r\text{ rare}}d_r(p)
=2\sum_{r\text{ rare}}m_A(r)\le2Kn.$$

At least half the points of $S$ therefore have total rare degree at
most $4K/\delta$, and hence at most $L$. Their rare-degree vectors,
padded with zeros to $K$ coordinates if necessary, have at most
$\binom{L+K}{K}$ possibilities. On a subset $T$ of the asserted
size, all rare degrees agree. The rich degrees already agree by
hypothesis, so

$$\sum_{q\in A}|p-q|^2=\sum_r r^2d_r(p)$$

is constant for $p\in T$. If $c=n^{-1}\sum_{q\in A}q$, then

$$\sum_{q\in A}|p-q|^2
=n|p-c|^2+\sum_{q\in A}|q-c|^2.$$

Thus $|p-c|$ is constant on $T$. Distinct points rule out radius
zero when $|T|\ge2$. This proves the lemma.

## Consequences and limitation

Together with the checked [positive-circle theorem](circle_incidence.md),
the lemma implies that in any hypothetical bounded-rarity sequence
$|A|\to\infty$, every rich-degree-profile fiber has size $o(n)$,
uniformly over the fibers. Otherwise a subsequence would have fixed
$K,\delta>0$ and hence a positive circular fraction, forcing linearly
many rare distances.

In particular, boundedly many equitable cells for the rich distance
graphs would suffice to prove rarity divergence: within each cell,
the total degree in each such graph is constant. If full distance
profiles agree on a cell, the centroid identity puts that entire cell
on one concentric circle without the rare-degree pigeonhole step.

The missing implication is substantial. The inequalities
$m_A(r)>n$ control the column sums $\sum_p d_r(p)>2n$, not equality
of the row profiles. No positive-sized profile fiber, bounded equitable
partition, or extension of partial isometries was deduced from bounded
rarity. Standard distance-energy counts do not supply such an extension;
their separate limitation remains in [motion_incidence](motion_incidence.md).

The profile lemma and its integer counting factors were checked by the
author and are author-recorded. No further extension criterion has been
developed, and the missing implication is not treated as a theorem.
