---
name: problems/primes/E1142
title: Problem 1142
desc: |
  Asks whether infinitely many $n$, or any $n>105$, have $n-2^k$ prime for every
  $k$ with $1<2^k<n$.
tags:
- Number theory
- Primes
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1142

[[problems/primes/_index|..]]

***

**Statement.** Are there infinitely many $n$ (or any $n>105$) such that $n-2^k$
is prime for all $1<2^k<n$?

**Status.** Open.

**Source.** [erdosproblems.com/1142](https://www.erdosproblems.com/1142),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1142,
https://www.erdosproblems.com/1142.

**References.**

- [Gu04] Guy, Richard K., Unsolved problems in number theory, third
  edition, Problem Books in Mathematics, Springer (2004), xviii+437 pp.;
  A19 "Values of $n$ making $n-2^k$ prime. Odd numbers not of the form
  $\pm p^a\pm2^b$.", printed p. 67: Erdős's conjecture that 4, 7, 15, 21,
  45, 75 and 105 are the only such $n$, the verifications to $2^{44}$
  ([MiWe69]) and $2^{77}$ (Uchiyama and Yorinaga), Vaughan's bound
  $x\exp(-(\ln x)^c)$ ([Va73]) and the conditional bounds $O(x^c)$, $c<1$,
  of Hooley and Narkiewicz. Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].
- [MiWe69] Mientka, Walter E. and Weitzenkamp, Roger C., On $f$-plentiful
  numbers. J. Combinatorial Theory (1969), 374-377.
- [Va73] Vaughan, R. C., Some applications of Montgomery's sieve. J. Number
  Theory (1973), 64-79.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1142.lean).

## Current assessment

For $n>4$, any solution is odd. For an odd prime $q$, let
$h=\operatorname{ord}_q(2)$ and $H_q=\{2^j\bmod q:1\le j\le h\}$. If $n>q+2^h$
and $n\bmod q\in H_q$, one of these exponents makes $n-2^j>q$ a multiple of
$q$, contradicting primality. The equality exceptions $n=q+2^j$ must be
retained.

Thus $3\mid n$ for solutions $n>7$ and $5\mid n$ for solutions $n>21$; modulo
seven the residues $1,2,4$ are excluded for $n>15$. But any fixed finite
collection $S$ of odd test primes leaves arbitrarily large odd multiples of
$\prod_{q\in S}q$ surviving all these tests, because zero belongs to no $H_q$.
A fixed-prime sieve cannot prove finiteness. These are exact author deductions
with no replay of the reported search range. A useful extension must grow the
moduli and control every prime-equality exception.

## Known Results

Not yet compiled.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]
- [[../library/primes/erdos_1950_integers_form_related_problems/_index|erdos_1950_integers_form_related_problems]]
- [[../library/primes/erdos_1950_integers_form_related_problems/conjecture_p115|erdos_1950_integers_form_related_problems / conjecture_p115]]

<!-- END problem library links -->
