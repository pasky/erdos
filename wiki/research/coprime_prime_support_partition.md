---
name: research/coprime_prime_support_partition
title: Coprime sums as partitions of prime support
desc: |
  An exact finite criterion for equality of the two functions in Problem 878,
  with a complete calculation of F(210) = 442 and its limited scope.
tags: []
sources: []
created: 2026-10-14T20:10:13Z
updated: 2026-10-14T20:10:13Z
---

# Coprime sums as partitions of prime support

***

Use the formulation of
[[problems/arithmetic_functions/E0878/_index|Problem 878]] with summands
$2\le a_i\le n$ and no prescribed number of summands. The following
arguments are recorded by Plasma AI without independent review.

For $n\ge2$, let $P$ be its set of prime divisors. For each nonempty
$S\subseteq P$, define

$$
w_n(S)=\max\{a\le n:\{p:p\mid a,\ p\text{ prime}\}=S\}.
$$

The set is nonempty because $\prod_{p\in S}p\mid n$. Pairwise coprime
summands have disjoint prime supports. A maximizing family uses every prime
in $P$: if $p$ is missing, the additional summand $p\le n$ strictly
increases its sum. Conversely, choosing the maximizing integer for each
block of a partition of $P$ gives a legal family. Thus

$$
F(n)=\max_{\mathcal P\text{ a partition of }P}
       \sum_{S\in\mathcal P}w_n(S),
\qquad
f(n)=\sum_{p\in P}w_n(\{p\}).
$$

In particular,

$$
F(n)=f(n)\quad\Longleftrightarrow\quad
w_n(S)\le\sum_{p\in S}w_n(\{p\})
\quad\text{for every nonempty }S\subseteq P.
$$

If one inequality fails, its block together with the remaining singleton
blocks improves on $f(n)$. If all hold, summing over any partition bounds
its value by $f(n)$. Bounded exponent enumeration computes every $w_n(S)$,
so this is an exhaustive finite criterion for a specified $n$.

For $n=210$, the singleton maxima for $2,3,5,7$ are respectively
$128,81,125,49$, with sum $383$. The pair maxima are:

| Support | Maximum | Maximum plus the other singletons |
| --- | ---: | ---: |
| $\{2,3\}$ | 192 | 366 |
| $\{2,5\}$ | 200 | 330 |
| $\{2,7\}$ | 196 | 402 |
| $\{3,5\}$ | 135 | 312 |
| $\{3,7\}$ | 189 | 442 |
| $\{5,7\}$ | 175 | 384 |

These values follow by enumerating the positive exponent of the larger
prime, then taking the largest admissible power of the smaller one. In the
row order above the possible larger-prime exponents are $1,\ldots,4$;
$1,2$; $1,2$; $1,2$; $1,2$; and $1$. The corresponding candidate maxima
are $(192,144,108,162)$, $(160,200)$, $(112,196)$, $(135,75)$,
$(189,147)$, and $(175)$.

Two pair blocks sum to at most $420$. A triple block and a singleton sum
to at most $210+128=338$, and the four-prime block is at most $210$.
Together with the all-singleton partition and the six rows, these cases
exhaust all partitions of four primes. The family $(128,189,125)$ attains
$442$, so

$$
F(210)=442>383=f(210).
$$

This calculation does not establish the separate reported assertion
$\max_{n\le210}f(n)=383$. Nor does it count the equality cases as $n$
varies. Such a count needs uniform information on the competition between
the block weights, not merely a finite test at each input. The source
[[../library/arithmetic_functions/erdos_1984_two_unconventional_number_theoretic_functions_related/_index|Erdős's 1984 paper]]
supplies density-one and limsup results and an upper bound for $H(x)$;
those have the scopes stated on the problem page. Its Theorem 8 is stated
without a proof in that paper and is not a proved premise of this argument.
