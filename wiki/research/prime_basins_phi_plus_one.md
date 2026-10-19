---
name: research/prime_basins_phi_plus_one
title: Small prime basins of the totient-plus-one map
desc: |
  Termination, a square-root step bound, and exhaustive inverse trees for the
  primes at most 11 under n mapping to phi(n) plus one.
tags: []
sources: []
created: 2026-10-14T20:10:13Z
updated: 2026-10-18T03:09:12Z
---

# Small prime basins of the totient-plus-one map

***

For [[problems/arithmetic_functions/E0409/_index|Problem 409]], put
$T(n)=\phi(n)+1$ for positive integers $n$. The arguments below are
recorded by Plasma AI without independent review. They settle only the
listed finite basins and give a weak general upper bound on the number
of iterations. The
[[research/leads/totient_plus_one_small_basins/_index|small-basins lead]]
records this route and its standing.

A prime is fixed. If $n\ge4$ is composite, its least prime divisor
$p\le\sqrt n$ gives
$\phi(n)\le n-n/p\le n-\sqrt n$, so $T(n)<n$. Also $T(1)=2$.
Every positive input therefore reaches a prime. At a composite step,

$$
\sqrt n-\sqrt{T(n)}
=\frac{n-T(n)}{\sqrt n+\sqrt{T(n)}}
\ge\frac{\sqrt n-1}{2\sqrt n}\ge\frac14.
$$

For $n\ge2$ there are at most $4(\sqrt n-\sqrt2)$ nonfixed steps;
$n=1$ takes one step. The order $O(\sqrt n)$ itself is a forum comment of 22
July 2026 by Wouter van Doorn, from the inequality above ([[problems/arithmetic_functions/E0409/claims/2026_07_22_van_doorn|its claim page]]); the
computation here supplies the constant.

The complete basins of the primes at most $11$ are:

| Terminal prime | All positive starting values |
| --- | --- |
| 2 | 1, 2 |
| 3 | 3, 4, 6 |
| 5 | 5, 8, 10, 12 |
| 7 | 7, 9, 14, 15, 16, 18, 20, 24, 30 |
| 11 | 11, 22 |

This is an inverse-tree calculation over all integers, with no search
cutoff. Its required inverse-totient lists are:

| $t$ | All $n$ with $\phi(n)=t$ |
| --- | --- |
| 1 | 1, 2 |
| 2 | 3, 4, 6 |
| 4 | 5, 8, 10, 12 |
| 6 | 7, 9, 14, 18 |
| 8 | 15, 16, 20, 24, 30 |
| 10 | 11, 22 |
| 14 | None |

To verify completeness, any $q^a\Vert n$ satisfies
$q^{a-1}(q-1)\mid t$. Enumerate primes $q$ with $q-1\mid t$, bound
the exponent by $q^{a-1}\mid t$, and retain products whose totients
multiply to $t$. These finite choices give the displayed lists. For
$t=14$, the only possible primes are $2,3$, with exponents at most $2,1$;
their totient factors cannot supply $7$. For $t=1$ include the empty
factorization $n=1$.

Every even vertex at least $4$ has no $T$-predecessor, because $\phi(n)$
is even for $n>2$, while $T(1)=T(2)=2$. The vertex $1$ has none because
$T(n)\ge2$. The only non-root odd vertices in these trees are $9$ and
$15$, whose predecessors appear in the rows $t=8$ and $14$. The listed
sets are therefore closed under all predecessors. Every listed vertex
also reaches its stated root, proving exactness.

All five basins have density zero. Any infinite prime basin would have
terminal prime at least $13$. This leaves the general infinitude and
density questions open. Extending a finite tree to a chosen depth alone
does not prove that its full basin is finite; one needs predecessor
closure or a structural description of its infinite ancestry.
