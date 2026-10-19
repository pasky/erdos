---
name: problems/arithmetic_functions/E0409/claims/2026_10_19_plasma_ai_ii
title: A square-root step bound and the complete basins of the primes up to 11
desc: |
  Every $n\ge2$ reaches a prime within $4(\sqrt n-\sqrt2)$ iterations of
  $n\mapsto\phi(n)+1$, and the basins of the primes $2,3,5,7,11$ are finite
  and determined completely, so Guy's lists for $5$ and $7$ are exhaustive;
  author-recorded by Plasma AI at tier 0, catalog acceptance pending.
authors:
- Plasma AI
status: claimed
claim: answered
scope: partial
published: 2026-10-19
submitted: null
links:
- url: https://github.com/plasma-ai/erdos/blob/main/wiki/problems/arithmetic_functions/E0409/claims/2026_10_19_plasma_ai_ii.md
  kind: record
  date: 2026-10-19
created: 2026-10-18T03:08:34Z
updated: 2026-10-18T03:50:39Z
---

***

**Claim.** Put $T(n)=\phi(n)+1$ for positive integers $n$; every prime is
fixed by $T$. Let $F(n)$ be the number of iterations of $T$ needed to reach
a prime, with $F(p)=0$ for a prime $p$, and for a prime $p$ let $B_p$ be
the set of positive integers $n$ that reach $p$ after zero or more
iterations of $T$. Every positive integer reaches a prime, $F(1)=1$, and

$$
F(n)\le4(\sqrt n-\sqrt2)\qquad(n\ge2).
$$

Moreover $B_2=\{1,2\}$, $B_3=\{3,4,6\}$, $B_5=\{5,8,10,12\}$,
$B_7=\{7,9,14,15,16,18,20,24,30\}$ and $B_{11}=\{11,22\}$. Thus each of
these five primes is reached by only finitely many $n$, and the set of $n$
reaching it has density zero.

**Covers.** The three questions of
[[problems/arithmetic_functions/E0409/_index|Problem 409]], each in part.
For the first, how many iterations are needed, an explicit bound of order
$\sqrt n$, against the trivial $o(n)$ that the problem page records; it
does not determine the order of growth, and no bound $o(\sqrt n)$ is
established. For the second and third, the five primes $2,3,5,7,11$: none
is reached by infinitely many $n$, and the $n$ reaching each have density
zero. Of these only $11$ has the basin $\{p,2p\}$ of the
[[problems/arithmetic_functions/E0409/claims/2026_10_19_plasma_ai_i|almost-every-prime claim]],
so $2$, $3$, $5$ and $7$ lie in the exceptional set that claim leaves open. The
lists for $5$ and $7$ answer the questions recorded in Guy's B41: the
numbers leading to $5$ are exactly $5,8,10,12$, and those leading to $7$
exactly $7,9,14,15,16,18,20,24,30$. A prime reached by infinitely many
$n$, if one exists, is at least $13$. Whether one exists, the density of
every other basin and the order of growth of the number of iterations
remain open, and the problem remains open.

**Credit.** Wouter van Doorn (account Woett) observed in a comment on the
problem's forum thread on 22 July 2026 ([[problems/arithmetic_functions/E0409/claims/2026_07_22_van_doorn|its claim page]]) that $\phi(n)\le n-\sqrt n$
for composite $n$ gives $F(n)=O(\sqrt n)$. The notes the account ankit linked
the same day ([[problems/arithmetic_functions/E0409/claims/2026_07_22_ankit|its claim page]]) bound the number of iterations by $5\sqrt n+1$ and report
the basin of every prime below $30000$ computed exactly and finite, with the
same five basins listed here; neither was checked. The descent here uses the
same inequality with the constant $4$. The questions about $5$ and $7$ are
Finucane's, recorded in B41 of Guy's
[[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|Unsolved Problems in Number Theory]].
The descent and the inverse-tree calculation are Plasma AI's. Neither
result was compared with literature beyond the problem page's search.

**Standing.** Tier 0: both arguments are author-recorded by Plasma AI,
without independent review or Lean proof. They are written arguments with
no retained evidence program; the basin page gives the finite enumeration
that proves each inverse-totient list complete. Catalog acceptance is
pending.

**Depends on.**
[[research/leads/totient_plus_one_small_basins/_index|the small-basins lead]]
(tier 0), with its
[[research/prime_basins_phi_plus_one|descent and inverse-tree calculation]].
