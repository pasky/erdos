---
name: theory/number_theory/L44_finite_prime_totient_phase
title: Finite-prime reduction of the totient phase quotient
desc: |
  Conditional on the unrefereed totients manuscript, least-preimage
  divisibility counts have continuous phase profiles, and finite-prime
  weighted sums approximate the Problem 417 quotient uniformly in phase.
id: L44
statement: |
  Assume the premises and conclusions of L65 and L43, conditional on the
  unrefereed September 2026 OpenAI manuscript An asymptotic formula for the number of
  totients. Write q(s)=A(1/r;s)/A(1;s), and let mu_H,s(d) be proportional
  to p_H,s(d)/d over distinct tail totients, with p_H,s the union probability
  of all admissible witnesses. For every fixed squarefree positive integer
  k, put C_k(x)=#{v<=x: v is a positive totient and k divides ell(v)} and
  b_H,k(s)=sum_d mu_H,s(d) 1_{k divides ell(d)}, where ell is the minimum
  over all positive preimages. There is a continuous function b_k on R/Z
  such that b_H,k converges to b_k uniformly on 0<=s<1 and
  C_k(x)/V(x)=b_k(theta(x))+o(1). Here b_1=1, 0<=b_k<=1,
  b_2<=1/2, and b_p<=p/(p-1)^2 for every odd prime p. For an integer
  Y>=2, put P_Y=product_{p<=Y} p and
  Q_Y(s)=sum_{k divides P_Y} mobius(k)b_k(s)/k and
  T_Y=sum_{p>Y} 1/(p-1)^2. Then
  0<=Q_Y(s)-q(s)<=T_Y<=1/(Y-1), uniformly in s.
  Also, with w_Y(d)=product_{p<=Y, p divides ell(d)}(1-1/p),
  limsup_{H->infinity} sup_s sum_d mu_H,s(d)(w_Y(d)-d/ell(d))
  <=T_Y. Consequently V(x)/V'(x) has a limit if and
  only if lim_{Y->infinity}(max_s Q_Y(s)-min_s Q_Y(s))=0.
  V counts positive totients at most x and V' counts distinct phi(n) for
  1<=n<=x. No independence of the profiles b_k from s is asserted.
status: proved
tier: 0
depends_on:
- L65
- L43
created: 2026-10-14T10:49:15Z
updated: 2026-10-14T10:49:15Z
---

# Finite-prime reduction of the totient phase quotient

[[theory/number_theory/_index|..]]

[[theory/number_theory/L44_finite_prime_totient_phase/_proof|_proof]]: Encode fixed prime divisibility as a least-preimage-ratio weight, count it
using the common prefix, and transfer prime-deletion bounds to all phases
and to the finite coefficient.

***

This conditional deduction is recorded by Plasma AI. It constructs phase
profiles for fixed finite-prime observables and transfers a large-prime
bound to the finite arithmetic coefficient. It leaves the constancy question
open: the profiles may depend on the phase, and only their indicated weighted
combination needs to become constant.

The [proof](_proof.md) uses the structural and counting premises of
[[theory/number_theory/L65_conditional_totient_ratio_coefficient/_index|L65]]
to count divisibility of the least preimage, with every witness union and
global minimum retained. The finite-coefficient regularity from
[[theory/number_theory/L43_continuous_totient_phase_ratio/_index|L43]]
and the unit jumps of these counts give continuous profiles on the circle.
Both inputs stand at tier 0 and remain conditional on the
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|unrefereed totients manuscript]].

The prime-deletion estimate and the comparison of the mean of $v/\ell(v)$
with $V'/V$ occur in the unrefereed, non-arXiv two-page note
[*An explicit bound for Erdős problem 417*](https://github.com/LeanMeanBean/417/blob/3620821345595c5e2b60de4f86561e1872c81840/417.pdf),
posted by the account LeanMeanBean on 10 October 2026. The proof here spells
out the needed estimates and combines them with the manuscript's coefficient
construction. The new conclusion is the phase-uniform truncation and the
finite-prime criterion, not a new source for the note's numerical bound.
Neither the note's numerical sum nor the manuscript's underlying proofs are
certified by this deduction.

**Standing.** Tier 0, author-recorded, with no independent review or
formalization. This is a conditional reduction, not a solution of
[[problems/arithmetic_functions/E0417/_index|Problem 417]]. Its
[[research/leads/distinct_totient_preimage_ratio/_index|research route]]
records the unresolved cancellation among the phase profiles. There is no
computational evidence entry point: the evidence is the displayed argument.

The reduction is complete under its premises. The prime truncation error has
the explicit upper bound $1/(Y-1)$; evaluating the profiles still requires
the manuscript's cut limit. A proof of phase independence, or a phase gap
exceeding the truncation and cut errors, remains a separate mathematical
obligation.
