---
name: problems/divisors/E0893
title: Problem 893
desc: |
  Asks whether $f(2n)/f(n)$ tends to a limit, where
  $f(n)=\sum_{k\le n}\tau(2^k-1)$ sums the divisor counts of $2^k-1$.
tags:
- Number theory
- Divisors
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 893

[[problems/divisors/_index|..]]

[[problems/divisors/E0893/claims/_index|claims/]]: The 1 claim page of Problem 893, one per claimant's result; the problem's standing derives from them.

***

**Statement.** If $\tau(n)$ counts the divisors of $n$ then let

$$
f(n)=\sum_{1\leq k\leq n}\tau(2^k-1).
$$

Does $f(2n)/f(n)$ tend to a limit?

**Formulation.** The question whether $f(2n)/f(n)$ tends to a limit is read, as
erdosproblems.com and Kovač and Luca read it, as allowing the limit $+\infty$.
After Kovač and Luca proved the ratios unbounded, erdosproblems.com kept the
problem OPEN, and they describe what remains as deciding whether
$f(2n)/f(n)\to\infty$ or the ratio has no limit. The [formal-conjectures
statement](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/893.lean),
as last changed on 18 September 2026, likewise asks whether the ratio tends to
infinity. Read as asking for a finite limit, a variant this page sets aside,
the question is answered no by their Theorem 1.

**Status.** Bloom's catalog labeled the problem OPEN. Kovač and Luca's
unboundedness theorem rules out every finite limit, which answers the
finite-limit variant that the Formulation sets aside and leaves the question
open. Divergence to infinity is proved only under unproven conjectures. That
result is on
[[problems/divisors/E0893/claims/2025_06_05_kovac_luca_conditional|their conditional page]].

**Source.** [erdosproblems.com/893](https://www.erdosproblems.com/893), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #893,
https://www.erdosproblems.com/893.

**References.**

- [Er98] Erdős, Paul, Some of my new and almost new problems and results in
  combinatorial number theory. Number theory (Eger, 1996) (1998), 169-180.
- [KoLu25] V. Kovač and F. Luca, On the number of divisors of Mersenne numbers.
  arXiv:2506.04883 (2025); published in Experimental Mathematics (online 20 May
  2026), doi:10.1080/10586458.2026.2636060.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/893.lean).

## Current assessment

Bloom's catalog labeled the problem OPEN. Under the formulation above, the open
question is whether $f(2n)/f(n)\to\infty$. Kovač and Luca
([[../library/divisors/kovac_2025_number_divisors_mersenne_numbers/_index|card]])
prove the ratios unbounded
([[../library/divisors/kovac_2025_number_divisors_mersenne_numbers/theorem_1|Theorem 1]],
refereed in Experimental Mathematics), which rules out every finite limit. That
answers no to the finite-limit variant, which the Formulation sets aside, and
does not settle the question as read here: unboundedness leaves both
$f(2n)/f(n)\to\infty$, a yes, and no limit at all, a no. The theorem was not
submitted to erdosproblems.com as a claim, so it has no claim page. They also
derive $f(2n)/f(n)\to\infty$ from either of two unproven conjectures
([[problems/divisors/E0893/claims/2025_06_05_kovac_luca_conditional|conditional claim page]]),
and their computations support divergence. Erdős [Er98] expected no simple
asymptotic formula for $f(n)$, since it grows too fast.

## Finite reductions and uniformity requirements

Let $N$ be the earliest index maximizing $\tau(2^k-1)$ for $k\le n$. Then $N$
is a strict record and $N>n/2$: otherwise the coprime factorization
$(2^N-1)(2^N+1)$ would give a larger value at $2N\le n$. Therefore

$$
\frac{f(2n)-f(n)}{f(n)}
 \ge\frac{\tau(2^{2N}-1)}{n\tau(2^N-1)}
 =\frac{\tau(2^N+1)}n
 \ge\frac{\tau(2^N+1)}{2N}.
$$

This reproduces the inspected reduction in
[[../library/divisors/kovac_2025_number_divisors_mersenne_numbers/_index|Kovač–Luca,
Section 3.1]]. It would prove the desired limit from $\tau(2^N+1)/N\to\infty$
along all strict records, which is their unproved Conjecture 1. A lower
comparison with their auxiliary function proves unbounded limsup by excluding
polynomial growth; it cannot compare ratios without an upper bound on the
denominator. The all-large-$n$ record estimate remains missing. This account
adds no independent verification of the source.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/divisors/kovac_2025_number_divisors_mersenne_numbers/_index|kovac_2025_number_divisors_mersenne_numbers]]
- [[../library/divisors/kovac_2025_number_divisors_mersenne_numbers/proposition_2|kovac_2025_number_divisors_mersenne_numbers / proposition_2]]
- [[../library/divisors/kovac_2025_number_divisors_mersenne_numbers/theorem_1|kovac_2025_number_divisors_mersenne_numbers / theorem_1]]
- [[../library/divisors/kovac_2025_number_divisors_mersenne_numbers/theorem_3|kovac_2025_number_divisors_mersenne_numbers / theorem_3]]

<!-- END problem library links -->
