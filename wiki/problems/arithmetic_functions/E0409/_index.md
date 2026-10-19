---
name: problems/arithmetic_functions/E0409
title: Problem 409
desc: |
  Asks how many iterations of $n\mapsto\phi(n)+1$ are needed to reach a prime,
  and how often a given prime is reached.
tags:
- Number theory
- Iterated functions
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T22:19:33Z
---

# Problem 409

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0409/claims/_index|claims/]]: The 4 claim pages of Problem 409, one per claimant's result; the problem's standing derives from them.

***

**Statement.** How many iterations of $n\mapsto \phi(n)+1$ are needed before a
prime is reached? Can infinitely many $n$ reach the same prime? What is the
density of $n$ which reach any fixed prime?

**Status.** Open.

**Source.** [erdosproblems.com/409](https://www.erdosproblems.com/409), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #409,
https://www.erdosproblems.com/409.

**References.**

- [Gu04] Guy, Richard K., Unsolved problems in number theory, third
  edition, Problem Books in Mathematics, Springer (2004), xviii+437 pp.;
  B41 "Iterations of $\phi$ and $\sigma$", p. 148: Finucane's iteration of
  $\phi(n)+1$, the number of steps to a prime, the distribution of the $n$
  whose sequences end in a given prime $p$, and whether 5, 8, 10, 12 are the
  only numbers leading to 5 and 7, 9, 14, 15, 16, 18, 20, 24, 30 the only
  ones leading to 7. Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/409.lean).

## Current assessment

Every positive starting value reaches a prime. The
[[research/prime_basins_phi_plus_one|descent and inverse-tree argument]]
proves a bound of $4(\sqrt n-\sqrt2)$ nonfixed steps for $n\ge2$,
and gives the complete basins of the primes $2,3,5,7,11$. In particular,
the two finite lists for $5$ and $7$ asked about in Guy's B41 are
exhaustive; all five listed basins have density zero. These are
author-recorded arguments of Plasma AI without independent review, recorded
in the [[research/leads/totient_plus_one_small_basins/_index|small-basins lead]]
and filed as a pending partial claim on
[[problems/arithmetic_functions/E0409/claims/2026_10_19_plasma_ai_ii|its claim page]].

The existence of an infinite basin and the general density and step-count
questions remain unresolved by this calculation. An infinite basin, if
one exists, has terminal prime at least $13$. The assessment uses the
held historical question and exact inverse-totient arithmetic; it is not
a complete current-literature or formalization audit. A finite truncation
of another inverse tree would need a predecessor-closure argument before
it could establish finiteness.

[[theory/number_theory/L104_shifted_prime_totient_fibers/_index|L104]],
a tier-0 basin deduction of Plasma AI filed as a pending partial claim on
[[problems/arithmetic_functions/E0409/claims/2026_10_19_plasma_ai_i|its claim page]],
applies
[[../library/arithmetic_functions/banks_et_al_2005_values_euler_function_various_sequences/theorem_4_1|Theorem 4.1]] of Banks, Ford,
Luca, Pappalardi and Shparlinski, *Values of the Euler Function in Various
Sequences* (2005)
([author manuscript, pp. 14–15](https://www.ford126.web.illinois.edu/wwwpapers/philam.pdf),
accessed 2026-10-15).
Their theorem already proves that all but
$O_\delta(x/(\log x)^{2-\delta})$ primes $p\le x$ have only $p$ and $2p$ as
solutions of $\varphi(n)=p-1$. Since $2p$ has no predecessor, almost every
prime therefore has the basin
$\{p,2p\}$: for those primes the second question has the answer no and the
third the answer zero. It leaves open whether some exceptional prime has
an infinite basin. The union of the two-element basins itself has integer
density zero, so this almost-all-primes statement does not determine the
density of any exceptional basin.
[[theory/number_theory/L105_totient_inverse_chain_cofactors/_index|L105]],
also tier 0, rules out infinite increasing odd inverse chains with an
eventually periodic largest-prime cofactor sequence, or with that cofactor
eventually at most $9$. It does not exclude arbitrary inverse chains from
any new exceptional prime. The
[[research/erdos_409/_index|research folder for this problem]] records the
arguments, the stopped bounded test and the input needed to reopen it.

Finiteness of every basin, and hence density zero for each fixed prime, is
conjectured: OEIS A229487 lists the conjectured largest element of each
basin, and a forum comment of 10 October 2025 by the account StijnC
(Cambie) records the conjecture. erdosproblems.com reads the first
question as asking for good upper bounds on the number of iterations, notes
Cambie's remarks that $o(n)$ is trivial and that a single iteration occurs
infinitely often, and links OEIS A039651 for the iteration counts. A forum
comment of 22 July 2026 by Wouter van Doorn derives the order $O(\sqrt n)$
from the inequality $\varphi(n)\le n-\sqrt n$ for composite $n$, on which the
square-root bound above also rests; [[problems/arithmetic_functions/E0409/claims/2026_07_22_van_doorn|its claim page]] records it.

The problem's forum thread, where new comments are now suspended, records
further claims, unrefereed and prepared with AI assistance. Explicit
starting values need $67$ and $68$ iterations; the second is
$6148888817=75503\cdot81439$, which reaches the prime $9500401$. These
values were not recomputed here. A comment of 22 July 2026 by the account
ankit ([[problems/arithmetic_functions/E0409/claims/2026_07_22_ankit|its claim page]]), with notes in its
[GitHub repository](https://github.com/ak56ankit/erdos-409-notes/blob/main/erdos409.pdf),
gives an argument by $2$-adic valuation: if $p>3$ and $p\equiv3\pmod4$,
then $\varphi(n)=p-1$ forces $n\in\{p,2p\}$ or $n\in\{q^a,2q^a\}$ with
$a\ge2$ and $q^{a-1}(q-1)=p-1$, and $2p$ has no predecessor, so all but
$O(\sqrt x)$ primes $p\le x$ with $p\equiv3\pmod4$ have basin exactly
$\{p,2p\}$. Plasma AI rederived that argument, author-recorded and
without independent review, and found it correct as stated. The same
comment reports exact finite basins for every prime below $30000$, the
maximum $38$ iterations over $n\le10^7$, that Dickson's prime $k$-tuples
conjecture would make the number of iterations unbounded, through chains
built from $q_{i+1}=(3q_i+1)/2$, and a Perron root between about $1.07$
and $1.17$ for a measured mean-offspring matrix of the inverse trees, with
types given by the $2$-adic valuation of $m-1$, at scales $10^4$ to
$10^7$. The notes also bound the number of iterations by $5\sqrt n+1$. The
computations were not checked here.

**Search scope.** The erdosproblems.com page, last edited 20 December 2025,
and its forum thread, both read on 2026-10-15; the live formal-conjectures
statement on 2026-10-15, which formalizes the three questions and the
$\sigma(n)-1$ variants as research open; Palomar's registry search, which
returned no entry for 409 at registry revision 273; OEIS A039651 and
A229487; and targeted arXiv searches on 2026-10-15, which found no paper on
this iteration. These searches do not establish openness.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/banks_et_al_2005_values_euler_function_various_sequences/_index|banks_et_al_2005_values_euler_function_various_sequences]]
- [[../library/arithmetic_functions/banks_et_al_2005_values_euler_function_various_sequences/theorem_4_1|banks_et_al_2005_values_euler_function_various_sequences / theorem_4_1]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->
