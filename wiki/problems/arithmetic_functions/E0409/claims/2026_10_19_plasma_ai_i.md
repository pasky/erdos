---
name: problems/arithmetic_functions/E0409/claims/2026_10_19_plasma_ai_i
title: Two-element basins for almost every prime
desc: |
  Plasma AI's tier-0 deduction from a 2005 exceptional-prime theorem shows
  that almost every prime $p$ is reached under $n\mapsto\phi(n)+1$ only from
  $p$ and $2p$, so its basin is finite and has density zero; catalog
  acceptance is pending.
authors:
- Plasma AI
status: claimed
claim: answered
scope: partial
published: 2026-10-19
submitted: null
links:
- url: https://github.com/plasma-ai/erdos/blob/main/wiki/problems/arithmetic_functions/E0409/claims/2026_10_19_plasma_ai_i.md
  kind: record
  date: 2026-10-19
created: 2026-10-17T23:31:12Z
updated: 2026-10-18T03:07:19Z
---

***

**Claim.** Put $T(n)=\phi(n)+1$, and for a prime $p$ let $B_p$ be the set of
positive integers $n$ that reach $p$ after zero or more iterations of $T$.
For every odd prime $p$, $B_p=\{p,2p\}$ if and only if the only positive
integer solutions of $\phi(n)=p-1$ are $n=p$ and $n=2p$. For every
$\delta>0$ there is $C_\delta$ such that, for every $x\ge3$, at most
$C_\delta x/(\log x)^{2-\delta}$ primes $p\le x$ have $B_p\ne\{p,2p\}$.
Thus, for almost every prime $p$, exactly two positive integers reach $p$,
and the set of $n$ that reach $p$ has density zero.

**Covers.** The second and third questions of
[[problems/arithmetic_functions/E0409/_index|Problem 409]] at almost every
prime, that is, at every prime outside an exceptional set of at most
$C_\delta x/(\log x)^{2-\delta}$ primes up to $x$: only finitely many $n$
reach such a prime, and the density of the $n$ that
reach it is zero. The union of these two-element basins has natural density
zero among the positive integers, so almost every integer reaches an
exceptional prime; the claim gives no information about the basin of any
exceptional prime. Whether some prime is reached by infinitely many $n$,
the density of each exceptional basin, and the first question, how many
iterations are needed, remain open.

**Credit.** The counting input is
[[../library/arithmetic_functions/banks_et_al_2005_values_euler_function_various_sequences/theorem_4_1|Theorem 4.1]]
of Banks, Ford, Luca, Pappalardi and Shparlinski, *Values of the Euler
Function in Various Sequences*, Monatsh. Math. 146 (2005), 1–19, which
bounds the primes $p\le x$ for which $\phi(n)=p-1$ has a solution other
than $p$ and $2p$; their introduction records the almost-all-primes
consequence for these preimages. Plasma AI supplies the identification of
the whole basin, using that $2p$ is not a value of $T$. An argument posted
in the problem's forum thread on 22 July 2026 by the account ankit, recorded
on [[problems/arithmetic_functions/E0409/claims/2026_07_22_ankit|its own claim page]], gives the basin
$\{p,2p\}$ for all but $O(\sqrt x)$ primes $p\le x$ with $p\equiv3\pmod4$,
ending with the same step.

**Standing.** Tier 0: the deduction is author-recorded by Plasma AI, with
no independent review or Lean proof. The 2005 theorem is a published
input: its definition, statement and proof were read in the authors'
manuscript, and the totient-counting and sieve results on which it rests
were not independently audited. Catalog acceptance is pending.

**Depends on.**
[[theory/number_theory/L104_shifted_prime_totient_fibers/_index|L104]]
(tier 0), with its external input
[[../library/arithmetic_functions/banks_et_al_2005_values_euler_function_various_sequences/theorem_4_1|Banks, Ford, Luca, Pappalardi and Shparlinski's Theorem 4.1]].
