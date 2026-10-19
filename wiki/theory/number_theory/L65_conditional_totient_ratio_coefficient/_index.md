---
name: theory/number_theory/L65_conditional_totient_ratio_coefficient
title: A conditional phase coefficient for the distinct-preimage ratio
desc: |
  Assuming the unrefereed totients manuscript's structural estimates, the
  weight 1/r gives the coefficient for distinct totients with a preimage at
  most x, reducing Problem 417 exactly to constancy in the phase.
id: L65
statement: |
  Assume Theorem 2.1, Proposition 5.3, the mass and prime-band estimates of
  Sections 6.1 and 7.1, Proposition 6.5, and Lemmas 6.6 and 7.3 of the
  September 2026 OpenAI manuscript An asymptotic formula for the number of
  totients, with its definitions of A_H, G_m, and theta. Put f0(r)=1/r for
  r>=1. Then A_H(f0;s) converges uniformly on 0<=s<1 to A(f0;s), which is
  bounded above and bounded away from zero, and
  V'(x)=(x G_m/log x)(A(f0;theta(x))+o(1)). Consequently V(x)/V'(x)
  converges if and only if A(f0;s)/A(1;s) is constant on 0<=s<1. If this
  quotient is nonconstant, the ratio has a nondegenerate closed interval
  of subsequential limits. Assuming also Theorem 2.2 of that manuscript,
  A(f0;s)=A(1;s)-sum_{k>=1} A(f_k;s), with uniform convergence in s.
  Here V(x) counts the distinct positive totients at most x, and V'(x)
  counts the distinct values phi(n) with 1<=n<=x.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T08:41:00Z
updated: 2026-10-14T08:41:00Z
---

# A conditional phase coefficient for the distinct-preimage ratio

[[theory/number_theory/_index|..]]

[[theory/number_theory/L65_conditional_totient_ratio_coefficient/_proof|_proof]]: A conditional extension of the manuscript's prime count, followed by a
uniform tail argument and an exact-phase criterion for convergence.

***

This conditional deduction is recorded by Plasma AI. Here $V(x)$ counts
distinct totients at most $x$, and $V'(x)$ counts distinct values of
$\varphi(n)$ with $n\le x$. The functions $f_k$ and the phase are those of
the [[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|unrefereed totients manuscript]].
The manuscript is an explicit premise, including its assertions about all
preimages of almost every totient. The checked fixed-dilation result held with
that source does not certify these stronger premises.

The [proof](_proof.md) extends the manuscript's largest-prime count to
$f_0(r)=1/r$. It controls the lower prime cutoff, obtains uniform convergence
without assuming continuity, and supplies the uniform tail bound needed for
the infinite sum. The expression $A(f_0;s)/A(1;s)$ is a limiting weighted
average of $d/\ell(d)$ over tail totients, with witnesses deduplicated by their
totient value.

**Standing.** Tier 0, author-recorded; no independent review or formalization
of this deduction. It remains conditional on an unrefereed manuscript. No
constancy or nonconstancy is established, so
[[problems/arithmetic_functions/E0417/_index|Problem 417]] remains open. The
[[research/leads/distinct_totient_preimage_ratio/_index|research route]] names
the remaining structural test. There is no computational evidence entry
point: the evidence is the displayed deduction from the specified source
premises.
