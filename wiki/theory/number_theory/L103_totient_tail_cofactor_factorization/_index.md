---
name: theory/number_theory/L103_totient_tail_cofactor_factorization
title: Tail uniqueness and cofactor factorization for the totient coefficient
desc: |
  Conditional on the unrefereed totients manuscript at two cuts, the tail
  totients of its coefficient factor through one prime tuple and a coprime
  cofactor outside vanishing mass, so the Problem 417 quotient is a limiting
  average of the cofactor's reciprocal least-preimage ratio.
id: L103
statement: |
  Use the definitions of the unrefereed September 2026 OpenAI manuscript An
  asymptotic formula for the number of totients: B, m, theta and G_m from its
  Equations (2.1)-(2.4); for a cut H, P=floor(log log H), R=m-H and L=m-P;
  the tail witnesses W_H,s(d) of its Equation (2.5), each a tuple of primes
  Q=(Q_h), P<=h<H, together with an integer a; and the data D_H(x) and the
  mass M_f(x;H) of its Section 6.1. Assume its Propositions 3.3 and 5.3 for
  every sufficiently large cut, and apply them at the cuts H and P with the
  same x. Write ell(n) for the least positive integer with phi(ell(n))=n.
  Call a tail totient d factorized at phase s if all witnesses in W_H,s(d)
  have one prime tuple Q, no witness (Q,a) has Q_P dividing a, and
  ell(d)=ell(e) Q_P Q_(P+1)...Q_(H-1), where
  e=d/((Q_P-1)(Q_(P+1)-1)...(Q_(H-1)-1)); then e=phi(a) for every witness
  (Q,a) of d. Let B_H(x) be the set of data (d,p_1,...,p_R) in D_H(x) for
  which d is not factorized at phase theta(x). Then for every sufficiently
  large H,
  limsup_{x->infinity} G_m^(-1) sum_{(d,p_1,...,p_R) in B_H(x)}
  1/(d (p_1-1)...(p_R-1)) <= eps_H + eps_P,
  where eps_K is the bound of Proposition 5.3 at the cut K; it does not
  depend on the phase and tends to zero as K tends to infinity. If in
  addition the premises of L65 hold, put q(s)=A(1/r;s)/A(1;s) and
  g(n)=n/ell(n), and let M*(x;H) be the sum of
  g(e)/(d (p_1-1)...(p_R-1)) over the data in D_H(x) outside B_H(x), with e
  defined from d as above. Then there are numbers c_H tending to zero,
  independent of the phase, such that for every sufficiently large H,
  limsup_{x->infinity} |q(theta(x)) - M*(x;H)/M_1(x;H)| <= c_H.
status: proved
tier: 0
depends_on:
- L65
created: 2026-10-15T04:35:23Z
updated: 2026-10-15T04:35:23Z
---

# Tail uniqueness and cofactor factorization for the totient coefficient

[[theory/number_theory/_index|..]]

[[theory/number_theory/L103_totient_tail_cofactor_factorization/_proof|_proof]]: Compare the common prefixes at the cuts H and P of one value, identify the
tail prime tuple of every witness and the least preimage, and transfer the
exceptional tuple count to the mass of the data and to the phase quotient.

***

This conditional deduction is recorded by Plasma AI. It applies the
common-prefix proposition of the
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|unrefereed totients manuscript]]
at two cuts at once: at the manuscript's cut $H$, whose tail totient $d$
enters the finite coefficient, and at the shorter cut $P=\lfloor\log\log
H\rfloor$, whose common prefix contains every retained tail prime of the
first. Outside the two exceptional sets the second prefix pins down the tail
prime tuple of every witness of $d$, forbids its smallest prime from
dividing the cofactor, and splits the least preimage. The manuscript is an
explicit premise, including its assertion that **every** preimage of a
non-exceptional value has the common prefix.

**Significance for Problem 417.** The finite coefficient of the manuscript
sums over distinct tail totients, each weighted by the probability of a
union over its witnesses and by its global least preimage. On factorized
tail totients the union has one member, the cofactor-to-value map is
replaced by distinct values $e=\varphi(a)$, and
$g(d)=g(e)\prod_h(1-1/Q_h)$ with the product within $2/Q_P$ of one. The
second part of the statement therefore expresses the phase quotient $q$ of
[[problems/arithmetic_functions/E0417/_index|Problem 417]] through the
reciprocal least-preimage ratio $g(e)$ of the cofactor totient alone. This
removes the union, the duplication of odd $a$ and $2a$, and the coprimality
question at $Q_P$ from the comparison of phases; it does not compare two
phases. The
[[research/leads/distinct_totient_preimage_ratio/_index|research route]]
uses it to locate the phase dependence in the cofactor fiber and records
why the manuscript's error rates leave constancy undecided.

**Dependency roles.** The second part consumes
[[theory/number_theory/L65_conditional_totient_ratio_coefficient/_index|L65]]
for the comparison of $V'(x)$ with the mass of the weight $1/r$ and for the
identification of $q(\theta(x))$ with $V'(x)/V(x)$ up to $o(1)$. The first
part uses only the manuscript.

The [proof](_proof.md) uses the statements of Propositions 3.3 and 5.3 at
the two cuts, the band conditions of Equation (2.5), and the prime count for
the largest prime from the proof of Proposition 6.1. It does not use
Lemma 6.4 or Proposition 6.5, so it says nothing directly about the finite
coefficient $A_H$; the passage to the coefficient's probability measure is
on the research route, with the extra reading of those proofs that it needs.

**Standing.** Tier 0, author-recorded, with no independent review or
formalization. It remains conditional on the unrefereed manuscript, and
through L65 on the same premises. No constancy or nonconstancy of $q$ is
established, and Problem 417 remains open. The exceptional mass is bounded
only through the manuscript's rates at the two cuts. At the cut $P$ the
coverage rate of Proposition 3.3 is $e^{-c\lfloor\log\log P\rfloor}$ up to
smaller terms, with an unspecified constant $c$, so the bound tends to zero
extremely slowly. There is no computational evidence entry point: the
evidence is the displayed deduction.
