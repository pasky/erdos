---
name: problems/primes/E1200
title: Problem 1200
desc: |
  Asks for a constant $C$ such that, for every large $x$, there are primes
  $p_1<\cdots<p_k<x$ with $\sum 1/p_i<C$ and congruences $a_i\pmod{p_i}$ that
  cover every integer $n<x$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-17T22:11:11Z
---

# Problem 1200

[[problems/primes/_index|..]]

***

**Statement.** There exists a constant $C$ such that for all large $x$ there is
a collection of primes $p_1<\ldots<p_k<x$ with $\sum\frac{1}{p_i}<C$ together
with a system of congruences $a_i\pmod{p_i}$ such that every integer $n<x$
satisfies at least one of these congruences.

**Status.** Open.

**Source.** [erdosproblems.com/1200](https://www.erdosproblems.com/1200),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1200,
https://www.erdosproblems.com/1200.

**References.**

- [Er80] Erdős, Paul, A survey of problems in combinatorial number theory. Ann.
  Discrete Math. (1980), 89-115.
- [ErRu80] Erdős, P. and Ruzsa, I. Z., On the small sieve. I. Sifting by primes.
  J. Number Theory (1980), 385-394.

**Formalization.** None recorded.

## Current assessment

The [[../library/primes/erdos_1980_small_sieve/problem_2|source's Problem 2]]
uses the positive initial interval. Put $N=\lceil x\rceil-1$. If one residue
for each of $s$ distinct primes $p_i<x$ covers $1,\ldots,N$, union counting
gives

$$
N\le N\sum_i\frac1{p_i}+s,\qquad
\sum_i\frac1{p_i}\ge1-\frac{\pi(x)}N=1-o(1).
$$

Thus no constant $C<1$ works, but this does not exclude $C=1$ or larger fixed
constants. It is a necessary bound for actual covers, not a construction.

The zero-residue theorem in
[[../library/primes/erdos_1980_small_sieve/_index|Erdős–Ruzsa]] supplies no
uniformity for an arbitrary translated interval after a CRT shift.
[[../library/primes/ruzsa_1982_small_sieve_ii_sifting_composite_numbers/theorem_iii|Ruzsa's
composite-modulus covers]] can have cost below one and therefore cannot
transfer unchanged to distinct prime moduli.
[[../library/primes/warlimont_1991_problem_posed_i_z_ruzsa/inequality_2|Warlimont's
inequality]] concerns a necessary counting relaxation, not an actual cover. The
source statements and interval convention were inspected; proofs of the latter
two inputs were not checked. The counting deduction is author-recorded, and the
bounded-cost prime construction remains missing.

The author-recorded
[[research/leads/bounded_cost_prime_covers/_index|attack on bounded-cost covers]]
gives an explicit cover of $1,\ldots,N$ for every large $N$ at reciprocal cost
$\log\log\log N+O(1)$: the class $1\bmod2$, residue $0$ for the primes in
$(N^{1/u},N/2]$ with $u=4\log\log N$, and one prime in $(N/2,N]$ for each
integer still uncovered. A midpoint variant omits the extra prime $2$ and
gives $\mu(N)\le\log\log\log N+\log4+o(1)$; its fixed-exponent windows
still leave a positive proportion of survivors. So $\mu(N)$ grows at most
triple-logarithmically. An argument from the published Erdős–Ruzsa sieve
theorem shows that this
zero-residue design cannot beat a constant multiple of that cost. By sieve
arguments the same page shows that every cover of bounded cost has almost one
unit of reciprocal mass on primes in a window $(N^{\theta},N^{1-\eta}]$ whose
endpoints depend on the cost bound and the allowed loss, and that a cover of
cost tending to one has
vanishing mass on primes up to $N^\tau$ for each fixed $\tau<1/3$.
None of this is independently reviewed. An exact finite survivor inequality
on the same page makes the
middle-mass obstruction explicit. In the window $(N^{1/3},N]$, a cover must
also have a prime at most $\sqrt N$ interacting through coincident short
triples with at least
$(\sqrt{2\rho(3)}-o(1))N^{1/4}\sqrt{\log N}$ other selected primes, where
$\rho$ is Dickman's function. Small groups of such coincidences therefore
cannot supply a cover. These are restricted obstructions; whether a bounded
cost suffices remains open. The same page records an exact identity that,
for each fixed $u\ge3$, reduces a cover of cost $\log u+o(1)$ with
reserved cleanup primes in $(N/2,N]$ to one net-gain inequality for the
classes of the primes in $(N^{1/u},N/2]$; no construction attaining it is
known. It also shows from the linear sieve that the selected primes up to
$N^{1/2-\delta}$, in any number and with any classes, leave at least a
fixed proportion of $[1,N]$ uncovered, depending only on $\delta$ and the
cost.

An [Erdős Problem a Day report](https://www.erdosproblemaday.com/report/1200)
dated 2026-07-27 defines $\mu(N)$ as the least reciprocal-prime cost
of covering $1,\ldots,N$ by one class for each selected prime at most
$N$, with value $+\infty$ if no cover exists. It reports exact values
for $1\le N\le40$ and an explicit cover at $N=40$. Its maximum finite
value in that range is claimed to be
$\mu(28)=24403493/17160990$; some smaller orders have no cover.
The report and its stated exhaustive-search method were read on
2026-10-16, but the companion checker was not inspected or replayed.
No independent acceptance is recorded. Neither the finite table nor
its necessary counting bounds establishes or refutes an eventually
bounded $\mu(N)$; the report explicitly leaves that question open.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/number_theory/erdos_1980_survey_problems_combinatorial_number_theory/_index|erdos_1980_survey_problems_combinatorial_number_theory]]
- [[../library/primes/erdos_1980_small_sieve/_index|erdos_1980_small_sieve]]
- [[../library/primes/erdos_1980_small_sieve/problem_2|erdos_1980_small_sieve / problem_2]]
- [[../library/primes/ruzsa_1982_small_sieve_ii_sifting_composite_numbers/_index|ruzsa_1982_small_sieve_ii_sifting_composite_numbers]]
- [[../library/primes/ruzsa_1982_small_sieve_ii_sifting_composite_numbers/theorem_iii|ruzsa_1982_small_sieve_ii_sifting_composite_numbers / theorem_iii]]
- [[../library/primes/warlimont_1991_problem_posed_i_z_ruzsa/_index|warlimont_1991_problem_posed_i_z_ruzsa]]
- [[../library/primes/warlimont_1991_problem_posed_i_z_ruzsa/equation_1|warlimont_1991_problem_posed_i_z_ruzsa / equation_1]]
- [[../library/primes/warlimont_1991_problem_posed_i_z_ruzsa/inequality_2|warlimont_1991_problem_posed_i_z_ruzsa / inequality_2]]

<!-- END problem library links -->
