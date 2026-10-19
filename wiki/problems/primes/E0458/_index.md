---
name: problems/primes/E0458
title: Problem 458
desc: |
  Asks whether $[1,\ldots,p_{k+1}-1]<p_k[1,\ldots,p_k]$ for all $k\ge1$, where
  $[1,\ldots,n]$ is the least common multiple of $1,\ldots,n$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 458

[[problems/primes/_index|..]]

***

**Statement.** Let $[1,\ldots,n]$ denote the least common multiple of
$\{1,\ldots,n\}$. Is it true that, for all $k\geq 1$,

$$
[1,\ldots,p_{k+1}-1]< p_k[1,\ldots,p_k]?
$$

**Status.** Falsifiable.

**Source.** [erdosproblems.com/458](https://www.erdosproblems.com/458), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #458,
https://www.erdosproblems.com/458.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/458.lean).

## Current assessment

The erdosproblems.com label FALSIFIABLE, which erdosproblems.com explains as
open but disprovable by a finite counterexample, marked the problem open and
records the question's logical form: a counterexample is a single $k$ with
$[1,\ldots,p_{k+1}-1]\ge p_k[1,\ldots,p_k]$, checked by finite arithmetic,
while a proof must cover every $k$. The label is a body note, not a claim, and
the problem has no claim page. The erdosproblems.com commentary records that
Erdős and Graham expected the inequality to hold and saw two obstacles to a
proof: ruling out several primes $q$ with $p_k<q^2<p_{k+1}$, which a gap bound
of the strength of Legendre's conjecture would give, and the behavior of the
small primes.

The erdosproblems.com discussion stated on 19 August 2025 that the comparison
becomes a product over the prime powers strictly between two consecutive primes,
each prime-power event contributing one factor of its base. A post of 27 April
2026 stated it again, counting a base once for each of its powers in the gap,
and reported a check finding no counterexample with $p_{k+1}\le10^{12}$. A post
of 12 June 2026 extends the check to $p_{k+1}\le10^{20}$. Below $4\times10^{18}$
it rests on the exhaustive gap search of Oliveira e Silva, Herzog and Pardi,
Math. Comp. 83 (2014), and above that on the unrefereed distributed prime-gap
search. As thread posts these have no claim page.

Search scope: the erdosproblems.com page, its thread (three comments by
2026-10-07, of 2025-08-19, 2026-04-27 and 2026-06-12) and the formal-conjectures
statement file.

## Exact local reduction and remaining uniformity

For consecutive primes $p<q$, increasing the lcm endpoint across a proper prime
power $\ell^a$ multiplies it by $\ell$. Thus the exact ratio is

$$
\frac{\operatorname{lcm}(1,\ldots,q-1)}{\operatorname{lcm}(1,\ldots,p)}
 =\prod_{p<\ell^a<q,\ a\ge2}\ell.
$$

Bertrand's theorem gives $q<2p$, so two powers of one prime cannot both occur
in the gap. Two prime squares force the product above $p$, hence a
counterexample. With at most two events and at most one square, the product is
below $q^{5/6}<(2p)^{5/6}<p$ for $p>32$. For $p=2,3,5,7,11,13,17,19,23,29,31$,
the event products are respectively $1,2,1,6,1,2,1,1,15,1,2$, all below $p$.

Consequently only gaps containing two prime squares or at least three proper
prime-power events can fail. This is an author-recorded structural filter, with
the displayed small cases, not an extended numerical search. The held
[[../library/number_theory/erdos_1980_old_new_problems_results_combinatorial_number_theory/_index|Erdős–Graham
passage]] identifies the related obstacles; external verification ranges were
not replayed. A finite search would still need certified consecutive-prime
endpoints and would not cover all such patterns.
