---
name: problems/arithmetic_functions/E0417
title: Problem 417
desc: |
  Asks whether the ratio of the number of totient values up to $x$ to the number
  of distinct values $\phi(m)$ with $m\le x$ has a limit, and whether that limit
  exceeds 1; phase reductions conditional on an unrefereed manuscript leave
  convergence open, and an unrefereed non-arXiv note claims a conditional upper bound.
tags:
- Number theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-19T06:04:51Z
---

# Problem 417

[[problems/arithmetic_functions/_index|..]]

[[problems/arithmetic_functions/E0417/claims/_index|claims/]]: The 0 claim pages of Problem 417, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let

$$
V'(x)=\#\{\phi(m) : 1\leq m\leq x\}
$$

and

$$
V(x)=\#\{\phi(m) \leq x : 1\leq m\}.
$$

Does $\lim V(x)/V'(x)$ exist? Is it $>1$?

**Formulation.** The second question, whether the limit is $>1$,
presupposes the first. It is read as the formal-conjectures statement linked
under Formalization states it (`erdos_417.parts.ii`): whether $V(x)/V'(x)$
tends to a limit $L>1$, possibly infinite, so a yes to it includes a yes to
the first.

**Status.** Open. Bloom's catalog labeled the problem OPEN, and the derived
standing is open. The erdosproblems.com proof-claims thread carried no claim on
2026-10-06. No resolution claim was identified in the search described below.
An unrefereed, non-arXiv October note claims the conditional upper bound
$\limsup V(x)/V'(x)<2.195202$ using the unrefereed OpenAI manuscript of 25
September 2026. The bound does not decide whether the limit exists, and it is
not recorded as a resolution claim.

**Source.** [erdosproblems.com/417](https://www.erdosproblems.com/417), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #417,
https://www.erdosproblems.com/417.

**References.**

- [Er98] Erdős, Paul, Some of my new and almost new problems and results in
  combinatorial number theory. Number theory (Eger, 1996) (1998), 169-180.

**Formalization.** Statement in the file
[`ErdosProblems/417.lean`](https://github.com/google-deepmind/formal-conjectures/blob/6fbb54f24ccc2e64dcfaffc28c58950e377110d2/FormalConjectures/ErdosProblems/417.lean)
of formal-conjectures, pinned at its last change of 18 September 2026:
`erdos_417.parts.i` (the existence of the limit) and `erdos_417.parts.ii` (a
limit exceeding $1$), each an `answer(sorry)` equivalence marked
`research open` with no `formal_proof` attribute.

## Current assessment

**The question (erdosproblems.com formulation, 2026-09-04).** Whether
$\lim V(x)/V'(x)$ exists and whether it exceeds $1$. OPEN. The erdosproblems.com
commentary records that $V'(x)\le V(x)$ trivially and that Erdős [Er98]
suggested the limit may be infinite.

**Standing.** No resolution claim page is recorded, and the derived standing
is open. The native coefficient deductions below are author-recorded at
tier 0.

**The OpenAI release item (family 024).** Theorem 2.2 of the release
manuscript of 25 September 2026, *An asymptotic formula for the number of
totients*
([[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|intake card]],
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/theorem_2_2|Theorem 2.2 page]]),
claims, for each fixed $k\ge1$, an asymptotic for
$N_k(x)=\#\{v\le x\text{ totient}:kx<\ell(v)\le(k+1)x\}$, with $\ell(v)$
the least preimage of $v$, and that $N_k(x)$ is of order $V(x)$ for $k=1$
and $2$; the manuscript is unrefereed, and this corpus has not built the
release's Lean for these counts (`weighted_totient_asymptotic`,
`weighted_totient_one_two`). The manuscript does not mention $V'$ or this
problem, and the release claims nothing about it. A totient
$v\le x$ is counted by $V'(x)$ exactly when $\ell(v)\le x$, so
$V(x)-V'(x)=\sum_{k\ge1}N_k(x)$, an identity the manuscript does not state.
The item settles neither question and is recorded here, not as a claim.

**The conditional coefficient reduction.**
[[theory/number_theory/L65_conditional_totient_ratio_coefficient/_index|L65]]
extends the manuscript's largest-prime count to the weight $f_0(r)=1/r$,
where $r$ is the least-preimage ratio of a tail totient. Assuming the
manuscript's structural and approximation estimates, it proves

$$
V'(x)=\frac{xG_m}{\log x}\bigl(A(f_0;\theta(x))+o(1)\bigr),
$$

with $A(f_0;s)$ defined by a uniform cut limit and bounded away from zero.
The manuscript's Lemma 7.3 also gives the uniform tail control in
$V-V'=\sum_kN_k$. Consequently the limit exists if and only if
$s\mapsto A(f_0;s)/A(1;s)$ is constant; if it is not, the ratio has a
nondegenerate interval of limit points. L65 is a tier-0 conditional
deduction by Plasma AI, outside the existing reviews and dependent on the
unrefereed manuscript. It does not decide constancy.

[[theory/number_theory/L43_continuous_totient_phase_ratio/_index|L43]]
deduces that the quotient is continuous on the phase circle; both numerator
and denominator have the same nontrivial boundary factor. The limit set is
exactly the image of that circle under the reciprocal quotient.
[[theory/number_theory/L44_finite_prime_totient_phase/_index|L44]]
constructs continuous phase profiles for
$\#\{v\le x:k\mid\ell(v)\}/V(x)$ for fixed squarefree $k$. A finite
weighted sum of these profiles, using primes at most $Y$, approximates the
quotient from above with error at most $1/(Y-1)$, uniformly in phase.
These are further tier-0 deductions conditional on the unrefereed manuscript.
They prove no phase independence.
[[theory/number_theory/L103_totient_tail_cofactor_factorization/_index|L103]],
also tier 0 and conditional, applies the manuscript's common-prefix
proposition at two cuts: outside vanishing mass each tail totient factors
through one prime tuple and a coprime cofactor, so the quotient becomes a
cofactor statistic averaged over a phase-dependent law. The
[[research/leads/distinct_totient_preimage_ratio/_index|distinct totient preimage ratio lead]]
records the unresolved cancellation, the missing fiber estimate in a
proposed renewal comparison, the scale obstruction to a direct rectangle
comparison, and precise sufficient estimates for reopening the test.

**The October ratio bound.** The unrefereed, non-arXiv two-page note
[*An explicit bound for Erdős problem 417*](https://github.com/LeanMeanBean/417/blob/3620821345595c5e2b60de4f86561e1872c81840/417.pdf),
posted by the account LeanMeanBean on 10 October 2026, claims

$$
\limsup_{x\to\infty}\frac{V(x)}{V'(x)}\le e^{M_*}<2.195202,
\qquad
M_*=\frac{\log2}{2}+
\sum_{p\ge3\text{ prime}}\frac{p}{(p-1)^2}\log\frac p{p-1}.
$$

It compares $V'(x)$ with the sum of $v/\ell(v)$ over totients at most $x$,
bounds prime divisibility of the least preimage by deleting a prime power,
and applies Jensen's inequality. Its inputs include Theorem 2.1 and
Proposition 5.3 of the unrefereed September manuscript, beyond the accepted
fixed-dilation result for Problem 416. Both pages, including the proof and
the stated numerical procedure, were read; the rational prime sum was not
rerun, and no independent acceptance of the note is recorded. It claims a
bound, not convergence or a resolution of either question.

**Search scope.** The historical erdosproblems.com page and its proof-claims
thread (empty on 2026-10-06), the OpenAI manuscript, and a search on
2026-10-14 of the
[live formal-conjectures statement](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/417.lean),
[Palomar's registry search](https://data.palomar-registry.org/api/v1/results?q=417),
Conjectures.io's visible problem listing and first ten recent results, and
targeted web and arXiv-index searches. The live statement still marks both
questions open. Palomar's text search returned no entry for 417 at registry
revision 265, and no newer primary resolution was found in the targeted
searches. Conjectures.io's results pagination was not exhausted. The October
announcement was traced to the actual two-page note cited above. These
searches do not establish openness, and no new independent proof review was
performed.

## Progress

Author-recorded research on the limit points of $V(x)/V'(x)$ is on
[[research/erdos_416/connections|the connections page of the Problem 416 folder]]
and in the lead
[[research/leads/distinct_totient_preimage_ratio/_index|distinct totient preimage ratio]];
it is not a claim, and the existence of the limit is open.
L65 supplies the conditional coefficient for $V'$ and controls the uniform
tail; L43 supplies continuity; L44 reduces the single expectation to
finite-prime weighted sums with an explicit uniform truncation error; L103
expresses the quotient through a smooth-cofactor statistic under a
phase-dependent law. All four are tier-0 deductions conditional on the
unrefereed manuscript and leave phase constancy open. The unrefereed,
non-arXiv October note claims the
conditional upper bound recorded in the assessment, with its numerical check
unverified here.

## Known Results

The ratio $V(x)/V'(x)$ is bounded: Pollack, Pomerance and Treviño quote
$V(x)\asymp V'(x)$ from Ford on p. 7 of their manuscript, which excludes the
infinite limit erdosproblems.com reports Erdős suggested.
[[research/erdos_49/connections|The Problem 49 connections page]] holds
author-recorded research notes on this ratio; they are not a claim.

## Method connection

[[research/methods/shifted_prime_moments|Moments over the prime factors of $p-1$]]
is background only here: it controls the joint divisibility of $p-1$ by prime
tuples, the kind of input that counts of totient values use, but no deduction
for $V(x)/V'(x)$ is recorded.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/arithmetic_functions/leanmeanbean_2026_explicit_bound_erdos_problem_417/_index|leanmeanbean_2026_explicit_bound_erdos_problem_417]]
- [[../library/arithmetic_functions/leanmeanbean_2026_explicit_bound_erdos_problem_417/theorem_1|leanmeanbean_2026_explicit_bound_erdos_problem_417 / theorem_1]]
- [[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|openai_2026_asymptotic_formula_number_totients]]
- [[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/theorem_2_2|openai_2026_asymptotic_formula_number_totients / theorem_2_2]]
- [[../library/arithmetic_functions/plasma_ai_2026_normal_order_number_iterations_euler_s_function/_index|plasma_ai_2026_normal_order_number_iterations_euler_s_function]]

<!-- END problem library links -->
