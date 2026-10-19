---
name: research/leads/totient_plus_one_small_basins
title: Descent and complete small basins of the totient-plus-one map
desc: |
  Closed (resolved): An elementary descent bounds the number of iterations
  of n -> phi(n)+1 needed to reach a prime by 4(sqrt n - sqrt 2) for n >= 2,
  and exhaustive inverse trees give the complete finite basins of 2, 3, 5,
  7 and 11, answering Guy's lists for 5 and 7. Author-recorded at tier 0;
  the general questions of Problem 409 remain open.
problems:
- 409
research_state: closed
review_status: unreviewed
created: 2026-10-18T03:08:34Z
updated: 2026-10-18T03:50:39Z
---

# Descent and complete small basins of the totient-plus-one map

[[research/leads/_index|..]]

***

This lead's results that are not drawn from a cited source are Plasma AI's,
credited to Plasma AI. All of them are author-recorded at tier 0, and no
independent review has examined the lead.

## Target and route

[[problems/arithmetic_functions/E0409/_index|Problem 409]] asks, for
$T(n)=\phi(n)+1$, how many iterations of $T$ are needed before a prime is
reached, whether infinitely many $n$ can reach the same prime, and what the
density of the $n$ reaching a fixed prime is. Let $F(n)$ be the number of
iterations needed, with $F(p)=0$ for a prime $p$, and let the basin of a
prime $p$ be the set of positive integers that reach $p$ after zero or more
iterations. This lead targets two bounded parts of these questions: an
explicit upper bound on $F(n)$, and the complete basins of the primes at
most $11$. The problem page's current assessment records the problem as
open, and this lead does not change that.

The route has two elementary steps, both proved on
[[research/prime_basins_phi_plus_one|the basin page]]. A descent at
composite steps, through the least prime divisor, bounds the number of
iterations. An inverse-tree calculation over all integers, with no search
cutoff, walks each small prime's tree backwards through complete
inverse-totient lists until the tree is closed under all predecessors.

## Results

**Step bound.** Every positive integer reaches a prime, $F(1)=1$, and
$F(n)\le4(\sqrt n-\sqrt2)$ for $n\ge2$. A prime is fixed by $T$; a
composite $n\ge4$ has least prime divisor at most $\sqrt n$, so
$\phi(n)\le n-\sqrt n$, and each composite step lowers $\sqrt n$ by at
least $1/4$.

**Complete basins.** The basins of the primes at most $11$ are
$\{1,2\}$ for $2$, $\{3,4,6\}$ for $3$, $\{5,8,10,12\}$ for $5$,
$\{7,9,14,15,16,18,20,24,30\}$ for $7$ and $\{11,22\}$ for $11$. Even
numbers at least $4$ and the number $1$ are never values of $T$, the only
non-root odd vertices are $9$ and $15$, and the basin page's lists of all
solutions of $\phi(n)=t$ for $t=1,2,4,6,8,10,14$, each proved complete by
a finite enumeration, close every tree under all predecessors.

Each of these basins is finite and so has density zero. The lists for $5$
and $7$ are exactly those asked about in Guy's B41
([[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|card]]),
so both are exhaustive. Any prime reached by infinitely many $n$ is at
least $13$.

## Standing and earlier statements

Both results are author-recorded by Plasma AI at tier 0, without
independent review or Lean proof. They are written arguments, and no
evidence program is retained.

The square-root order also appears in a forum comment of 22 July 2026 by
Wouter van Doorn (account Woett), who derives $F(n)=O(\sqrt n)$ from the
same inequality $\phi(n)\le n-\sqrt n$ for composite $n$. Notes linked the
same day by the account ankit bound the number of iterations by
$5\sqrt n+1$ and report that the basin of every prime below $30000$ is
finite and computed exactly, with the same five basins as above; neither
was checked here. Both have claim pages on the problem. The problem page
records both comments with its search scope.

## Closure

Closed, resolved: the step bound and the five basins are proved at the
scope stated above, and the route settles nothing further. Extending an
inverse tree to a chosen depth does not prove that its basin is finite;
that needs predecessor closure or a structural description of the basin's
infinite ancestry. No bound $F(n)=o(\sqrt n)$ is established: a slow step
needs an integer with large least prime factor, prime squares and balanced
semiprimes are the limiting cases of the descent estimate, and no estimate
for the length of strings of balanced-semiprime steps has been obtained.

The [[research/erdos_409/_index|research folder for the problem]] records
the general questions: the almost-all-primes basin deduction
[[theory/number_theory/L104_shifted_prime_totient_fibers/_index|L104]], the
inverse-chain obstruction
[[theory/number_theory/L105_totient_inverse_chain_cofactors/_index|L105]],
and the open gaps that remain.
