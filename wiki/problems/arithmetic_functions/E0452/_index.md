---
name: problems/arithmetic_functions/E0452
title: Problem 452
desc: |
  Asks for the size of the largest interval $I\subseteq[x,2x]$ on which every
  $n$ has more than $\log\log n$ distinct prime factors.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 452

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0452/claims/_index|claims/]]: The 1 claim page of Problem 452, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $\omega(n)$ count the number of distinct prime factors of
$n$. What is the size of the largest interval $I\subseteq [x,2x]$ such that
$\omega(n)>\log\log n$ for all $n\in I$?

**Status.** Open, the erdosproblems.com label (page last edited 28 October
2025). One pending partial claim,
[[problems/arithmetic_functions/E0452/claims/2026_07_26_white|White's weighted-sieve upper bound]],
bounds the longest run from above but does not determine its size. So the
derived standing is `open` with no full claim.

**Source.** [erdosproblems.com/452](https://www.erdosproblems.com/452), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #452,
https://www.erdosproblems.com/452.

**References.**

- [Er37] Erdős, Paul, Note on the number of prime divisors of integers. J.
  London Math. Soc. (1937), 308-314.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/452.lean).

## Current assessment

**The question (erdosproblems.com formulation).** With $\omega(n)$ the number of
distinct prime factors of $n$, the size $L(x)$ of the largest interval
$I\subseteq[x,2x]$ on which $\omega(n)>\log\log n$ throughout. Bloom's catalog
labeled the problem OPEN (page last edited 28 October 2025).

**Standing.** Open. One pending partial claim, White's report of 2026-07-26
([[problems/arithmetic_functions/E0452/claims/2026_07_26_white|claim page]]),
bounds $L(x)$ by $\exp((1+o(1))\log x/\log\log x)$; it is not refereed and
names no reviewer, and it does not determine $L(x)$, so the derived standing
stays `open`.

**What is known.** Erdős [Er37] proved that the integers with
$\omega(n)>\log\log n$ have density $1/2$. The Chinese remainder theorem
gives an interval with $|I|\ge(1+o(1))\log x/(\log\log x)^2$, and the
erdosproblems.com commentary suggests that intervals of length $(\log x)^k$
might exist for every $k$. From above, a [thread post of 4 July
2026](https://www.erdosproblems.com/forum/thread/452#post-7347) gives
$L(x)\le x^{O(1/\sqrt{\log\log x})}$ by comparing the mean, variance and
skewness of the count of prime factors below a power of the interval's length,
and reports that Erdős and Graham knew no upper bound; White's report of 26 July
2026 improves this to $\exp((1+o(1))\log x/\log\log x)$ by a weighted sieve,
crediting the argument to GPT-5.6 Sol; a [thread post of 28 September
2026](https://www.erdosproblems.com/forum/thread/452#post-9221) proves
$L(x)\le x^{(1+\varepsilon)/\log\log x}$ for every $\varepsilon>0$ by a Brun
sieve, cites the report, tabulates $L(x)$ for $x$ from $10^6$ to $5.3\times10^8$
and conjectures $L(x)\asymp\log x$. Between $\log x/(\log\log x)^2$ and
$x^{o(1)}$ the size is undetermined, and neither thread post is a dated
manuscript, so neither has a claim page.

**Search scope.** The erdosproblems.com page, its two comments and its empty
proof-claims tab, the report, the formal-conjectures statement file and the
community database; no other literature search was made.

## Prime-factor and interval interface

The standard disjoint-prime construction explains the recorded lower scale. Set
$r=\lfloor\log\log(2x)\rfloor+1$, assign $r$ distinct primes to each of $h$
offsets, with all $hr$ primes distinct, and force their products to divide the
corresponding shifted integers by the Chinese remainder theorem. Using the
first $hr$ primes gives modulus $M$ with $\log M\sim hr\log(hr)$ by the prime
number theorem. At

$$
h=\left\lfloor(1-\epsilon)\frac{\log x}{(\log\log x)^2}\right\rfloor
$$

for fixed $0<\epsilon<1$, this gives $M=x^{1-\epsilon+o(1)}=o(x)$. A
representative of the resulting progression places the whole block inside
$[x,2x]$. Each term has at least $r>\log\log n$ distinct factors. This author
reconstruction imports the prime number theorem; it makes no new record claim
beyond the
[[../library/arithmetic_functions/erdos_1937_note_number_prime_divisors_integers/main_theorem|held
lower-bound account]]. Its modulus cost is specific to disjoint prime
allocation, not an impossibility theorem for other constructions. A proposed
improvement must compute its actual modulus and guarantee every offset.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/erdos_1937_note_number_prime_divisors_integers/_index|erdos_1937_note_number_prime_divisors_integers]]
- [[../library/arithmetic_functions/erdos_1937_note_number_prime_divisors_integers/main_theorem|erdos_1937_note_number_prime_divisors_integers / main_theorem]]

<!-- END problem library links -->
