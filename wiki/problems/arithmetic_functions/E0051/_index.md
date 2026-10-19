---
name: problems/arithmetic_functions/E0051
title: Problem 51
desc: |
  Asks whether some infinite set $A$ of totient values has $n_a/a\to\infty$,
  where $n_a$ is the least $n$ with $\phi(n)=a$.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-19T04:19:00Z
---

# Problem 51

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0051/claims/_index|claims/]]: The 1 claim page of Problem 51, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Is there an infinite set $A\subset \mathbb{N}$ such that for
every $a\in A$ there is an integer $n$ such that $\phi(n)=a$, and yet if $n_a$
is the smallest such integer then $n_a/a\to \infty$ as $a\to\infty$?

**Status.** Open. Bloom's catalog labeled the problem OPEN (page last edited
2025-09-30), and its proof-claims tab carries no entry.

**Source.** [erdosproblems.com/51](https://www.erdosproblems.com/51), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #51,
https://www.erdosproblems.com/51.

**References.**

- [Gu04] Guy, Richard K., Unsolved problems in number theory, third
  edition, Problem Books in Mathematics, Springer (2004), xviii+437 pp.;
  B36 "Euler's totient function", printed p. 139: Erdős's question whether
  for every $\epsilon$ there
  is an $n$ with $\phi(n)=m$, $m<\epsilon n$, and $\phi(t)\ne m$ for all
  $t<n$, "perhaps there are many such $n$". Library home:
  [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]].

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/51.lean).

## Current assessment

The erdosproblems.com label was OPEN (erdosproblems.com record accessed
2026-09-04, problem page last edited 2025-09-30). No claim settles the question.
One claim page is recorded, and it is rejected: a one-page proof posted to the
erdosproblems.com discussion thread on 2026-01-11, produced by ChatGPT (free
version) for the user who posted it, asserted a yes answer through the products
$\prod_{i\le k}(p_i-1)$ and failed at its minimality step the same day, with
the curator's counterexamples $\phi(3)=\phi(6)$ and
$\phi(3\cdot5\cdot7)=\phi(5\cdot13)$
([[problems/arithmetic_functions/E0051/claims/2026_01_11_colossal_noob|the claim page]]).
The one outside result bearing on the question, the OpenAI release's
dichotomy for the counts of totients with least preimage between $kx$ and
$(k+1)x$ (manuscript of 2026-09-25), gets no claim page: it proves a
reformulation of the question, a dichotomy that decides neither answer and
settles no instance beyond the known cases $k=1,2$, so Known Results records
the theorem and its Lean declarations instead. The Progress notes below are
author-recorded, drawn from the research pages they link, and are not
independently reviewed; no further literature search is recorded.

## Progress

The question is equivalent to the unboundedness of the least-preimage ratio
$f_{\min}(v)/v$ over totients;
[[research/erdos_416/connections|the connections page of the Problem 416 folder]]
holds author-recorded research notes on totients all of whose preimages share
a divisor $k$, which Ford found only for prime-power $k\le11$ and $k=11$; the
notes are not a claim.
[[research/erdos_51/_index|The Problem 51 research home]] records the
substitution principle behind the collision $\varphi(105)=\varphi(65)$, small
values all of whose preimages are divisible by $2$ or by $3$, and a value
$54\cdot2^{32}$ showing that two forced divisors need not combine: a preimage
prime to $6$ uses primes $q$ with $q-1$ drawing on both factors.
It also proves an obstruction to one proposed repair: a fixed finite set of
covering primes, with only boundedly many designated divisors, cannot exclude
all unwanted shifted divisors across a family with unbounded least-preimage
ratio. This does not exclude covers that grow with the family.

## Known Results

The convenient-integer construction of Pollack, Pomerance and Treviño's
Lemma 4.1 transports a totient's least-preimage ratio, within a bounded factor,
to a positive proportion of totients but cannot create unbounded ratios;
[[research/erdos_49/connections|the Problem 49 connections page]] records this
failed transfer with its obstruction.

The OpenAI release's manuscript *An asymptotic formula for the number of
totients* (2026-09-25; the
[preprint at the pinned revision](https://github.com/openai/math/blob/adc7f1241/preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf),
digested on the intake card
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|openai_2026_asymptotic_formula_number_totients]])
proves, as a companion to its asymptotic formula for the number of totients
(whose fixed-scale limit answers the doubling question of
[[problems/arithmetic_functions/E0416/_index|Problem 416]], and which is a
pending claim on that problem's second question), a dichotomy for the
totients by least preimage. Write $\ell(v)$ for the least $n$ with
$\phi(n)=v$ (the $n_a$ of the Statement), $V(x)$ for the number of totients
up to $x$ and, for an integer $k\ge1$,
$N_k(x)=\#\{v\le x\ \text{totient}: kx<\ell(v)\le(k+1)x\}$. Its Theorem 2.2
states that $N_k(x)$ has an asymptotic formula on the counting scale of the
main theorem, with a coefficient built from finite arithmetic data, and that
for each $k$ exactly one of two alternatives holds: if some totient $d$ has
$\ell(d)>kd$, then $N_k(x)\asymp_k V(x)$, so a positive proportion of all
totients up to $x$ have least preimage in $(kx,(k+1)x]$; if no such $d$
exists, then $N_k(x)=0$ for every $x$. The first alternative holds for $k=1$
and $k=2$. The manuscript's own remark reads the theorem as this page does: a
positive answer to the question is equivalent to the first alternative holding
for every $k$, and neither the unboundedness of $\ell(d)/d$ over totients nor
the classification of the $k$ is established there. The result is therefore a
reformulation of the question, not progress on it, and no claim page records
it. The release's Lean tree proves the theorem as
`OAI.TotientAsymptotic.weighted_totient_asymptotic` (with
`weighted_totient_one_two` for the $k=1,2$ seeds) and its zero alternative as
`OAI.TotientAsymptotic.companion_zero_case`, in the folder
[`lean/OAI/NumberTheory/TotientAsymptotic`](https://github.com/openai/math/tree/adc7f1241/lean/OAI/NumberTheory/TotientAsymptotic)
at the pinned revision, pinned by the comparator challenges
[`TotientAsymptotic.lean`](https://github.com/openai/math/blob/adc7f1241/lean/ComparatorChallenges/TotientAsymptotic.lean)
and
[`TotientCompanionZero.lean`](https://github.com/openai/math/blob/adc7f1241/lean/ComparatorChallenges/TotientCompanionZero.lean).
These declarations state the manuscript's theorems faithfully, and no
declaration of the family asserts or refutes the seed condition for all $k$;
this corpus has not built them. The $k=1$ case of the same theorem bears on
[[problems/arithmetic_functions/E0417/_index|Problem 417]], whose page records
the item and why it is not a claim there.

## Exact scope of the arithmetic reduction

The multiplier argument in the existing research transports a fixed
minimum-preimage ratio into a bounded interval; it does not construct seed
ratios tending to infinity. A sufficient forcing condition is concrete: if
every preimage of a totient value $v$ is divisible by $k$, then

$$
\frac{\min\{n:\phi(n)=v\}}{v}\ge\frac{k}{\phi(k)},
$$

because $k\mid n$ implies $\phi(n)/n\le\phi(k)/k$. The missing input is
all-preimage divisibility with $k/\phi(k)$ unbounded. Exhibiting one divisible
preimage is insufficient: $\phi(105)=\phi(65)=48$ and $\phi(6)=\phi(3)=2$.
These exact elementary comparisons confer no new standing on the
source-dependent research. The next useful condition must control every smaller
alternative preimage.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|openai_2026_asymptotic_formula_number_totients]]
- [[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/theorem_2_2|openai_2026_asymptotic_formula_number_totients / theorem_2_2]]
- [[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|guy_2004_unsolved_problems_number_theory]]

<!-- END problem library links -->
