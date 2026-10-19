---
name: research/erdos_644/quotient_compression_obstruction
desc: Near-three-quarter P7 families whose every subquadratic vertex quotient has sublinear transversal number.
tags: [proved, constructions, method-obstruction]
sources: []
created: 2026-09-23T06:00:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/quotient_compression_obstruction

***

The polynomial-size quotients in [Random quotients](random_quotients.md)
cannot in general be replaced by linear-size quotients, even for families
whose transversal-to-rank ratio tends to three quarters. In fact the
obstruction below applies to every fixed subquadratic ground-set bound.
It does not resolve either assertion of Problem 644: its families are
near-boundary examples, not counterexamples, and their guards can be
removed by incidence projection.

## Intersecting families on a small ground set

**Lemma.** A nonempty pairwise-intersecting family of nonempty sets on
at most $N$ points, with at most $M$ members, satisfies

$$
\tau\le 1+\sqrt{1+N\log M}.
\tag{1}
$$

Here and below logarithms are natural.

Write $u=\tau$. Each edge is a transversal, so every edge has at least
$u$ points. Sample

$$
\ell=\left\lceil (N/u)\log M\right\rceil
$$

points independently and uniformly from an $N$-point ground set, with
replacement. The expected number of edges missed by the sample is at
most $M\exp(-\ell u/N)\le1$. Some sample therefore misses at most one
edge. Supplementing it by one point, if necessary, gives

$$
u\le\ell+1\le N\log M/u+2.
$$

Solving this quadratic inequality proves (1).

## The guarded construction

Let $s-1$ run through primes, and put

$$
m=\lceil\log s\rceil,
\qquad M=s^2-s+1.
$$

Let $\mathcal A$ be the complete $4ms$-uniform family on $7ms-1$
points. On a disjoint ground set, let $\mathcal G$ be the disjoint
union of the line families of $3m$ projective planes of order $s-1$.
Define

$$
\mathcal H=\{A\cup B:A\in\mathcal A,\ B\in\mathcal G\}.
\tag{2}
$$


The complete family has $\tau(\mathcal A)=3ms$ and $P_7$. Indeed,
seven rows have total incidence $28ms>4(7ms-1)$, so some point meets at
least five rows. Any two rows intersect, so one further point meets
the at-most-two remaining rows.

Each plane has $M$ lines, of size $s$, and transversal number $s$.
A line meets every line, whereas $s-1$ points meet at most
$s(s-1)=M-1$ lines. It follows that

$$
\tau(\mathcal G)=3ms.
$$

A transversal of the product (2) must cover at least one factor:
otherwise choose an edge missed in each factor and take their union.
Conversely, a cover of either factor covers the product. Therefore

$$
K=\operatorname{rank}(\mathcal H)=(4m+1)s,
\qquad \tau(\mathcal H)=3ms.
\tag{3}
$$

All edges have size $K$. The family inherits $P_7$ from $\mathcal A$,
and $\tau(\mathcal H)/K\to3/4$.

## Every small quotient collapses

Let $\phi:V(\mathcal H)\to[N]$ be any map. In particular, it may
identify points from different planes or factors. Each image plane
remains pairwise intersecting and has at most $M$ distinct edges.
A cover of all image planes covers every image edge of (2). Applying
(1) to each plane gives

$$
\boxed{\tau(\phi(\mathcal H))
\le3m\left(1+\sqrt{1+N\log(s^2-s+1)}\right).}
\tag{4}
$$


For each fixed $\varepsilon>0$, if $N=O(K^{2-\varepsilon})$, then
the right side of (4) is $o(K)$. Indeed, $m=O(\log K)$,
$\log M=O(\log K)$, and division by $K$ gives
$O(K^{-\varepsilon/2}(\log K)^{3/2})+o(1)$.

More quantitatively, preserving a fixed proportion $\delta>0$ of
$\tau(\mathcal H)$ requires

$$
N\ge\frac{\delta^2s^2-2\delta s}{\log(s^2-s+1)}
=\left(\frac{\delta^2}{32}+o(1)\right)
  \frac{K^2}{(\log K)^3}.
\tag{5}
$$

For sufficiently large $s$, this follows from (3)--(4) by subtracting
one and squaring; $K\sim4s\log s$ gives the asymptotic form.

The one-product-edge deletion lemma in
[Prime guard families](prime_guard_families.md#deleting-one-product-edge)
also makes these examples conjunction-prime without changing their
uniformity or transversal number. They still have $P_7$, and (4)
continues to hold for the resulting subfamily.

## What remains possible

The guard rank $s$ is $o(K)$. Erasing guard incidences recovers
$\mathcal A$, preserves the transversal number and $P_7$, and reduces
the ground set to linear size. Consequently the example does not
exclude a ground-set reduction preceded by an appropriate structural
normalization. It rules out vertex identification alone, even with
exact conjunction-primality. There is no asserted obstruction under
simultaneous edge and incidence criticality, and no conclusion about
the existence of $\lim_k f(k,r)/k$.
