---
name: theory/additive_bases/L4_random_modulus_exponent
title: A random-modulus two-representation exponent
desc: |
  One infinite positive-integer set has at most two representations of each
  sum and counting exponent root six minus two with an explicit loss.
tags: []
sources: []
id: L4
statement: |
  Put gamma=sqrt(6)-2. There exist one infinite set A of positive integers,
  a real constant C>0, and a real x0>e such that, writing
  A(x)=|A intersect [1,x]| for real x and
  r_A(n)=|{(a,b) in A^2 : a <= b and a+b=n}| for integer n,
  r_A(n) <= 2 for every integer n and
  A(x) >= x^gamma exp(-C sqrt(log x) log log x)
  for every real x >= x0, with natural logarithms in this bound.
  A diagonal representation a+a is counted once. Consequently this same
  A has liminf log A(x)/log x >= gamma as real x tends to infinity,
  and for each real alpha<gamma it satisfies A(x)>=x^alpha at every
  sufficiently large real x; only that threshold may depend on alpha.
status: proved
tier: 0
depends_on: []
created: 2026-09-09T01:21:03Z
updated: 2026-09-09T01:21:03Z
---

# A random-modulus two-representation exponent

[[theory/additive_bases/_index|..]]

[[theory/additive_bases/L4_random_modulus_exponent/_proof|_proof]]: Product probabilities and collision-plane counts give one auxiliary basis
and simultaneous shell selections with the original quantitative loss.

***

For $A\subseteq\mathbb Z_{>0}$, write

$$
A(x)=|A\cap[1,x]|,\qquad
r_A(n)=|\{(a,b)\in A^2:a\le b,\ a+b=n\}|.
$$

The representations are unordered, and a diagonal $a+a$ counts once.

## Statement

Put $\gamma=\sqrt6-2$. There exist one infinite set
$A\subseteq\mathbb Z_{>0}$ and constants $C>0$, $x_0>e$ such that

$$
r_A(n)\le2\quad(n\in\mathbb Z),\qquad
A(x)\ge x^\gamma
\exp\{-C\sqrt{\ln x}\,\ln\ln x\}\quad(x\ge x_0).
$$

The last inequality holds for every real cutoff. In particular,

$$
\liminf_{x\to\infty}\frac{\log A(x)}{\log x}\ge\gamma.
$$

For every real $\alpha<\gamma$, this same set satisfies
$A(x)\ge x^\alpha$ at all sufficiently large real cutoffs. The set is
chosen before $\alpha$; only the latter threshold may depend on $\alpha$.

The [proof](_proof.md) chooses each auxiliary prime $q_j$ independently
and uniformly in $(2^{2j-1},2^{2j}]$. The source-prime shells are the
fixed intervals $(2^{\gamma(k-1)^2},2^{\gamma k^2}]$. A localized
factorization count handles the lower part of the collision range. In the
upper part, a count of integer points on collision planes is averaged over
the lower auxiliary modulus. One favorable infinite auxiliary sequence and
one simultaneous selection across all shells give the stated set.

## Scope and relationships

The claim uses the fixed auxiliary-prime intervals and source shells stated
above, with the quantitative loss in the statement. It asserts no
optimized-schedule bound.

The construction develops the mixed-radix method and independent
auxiliary-prime choices in Javier Cilleruelo's
[*Infinite Sidon sequences*](../../../../library/additive_bases/cilleruelo_2014_infinite_sidon_sequences/_index.md).
The proof identifies the selected version and the exact method locators.
These are method attributions; no density theorem from that paper is a
premise of L4.

[L2](../L2_two_representation_exponent/_index.md) records the related
exponent-$3/7$ argument at tier 0. L4 reproduces its needed digital,
factorization, and finite-selection deductions with the new parameter
range checked explicitly. It does not consume L2's theorem or a local
component as an accepted premise, and its local claim dependency list is
empty.

The exponent satisfies $3/7<\gamma<1/2$. The result therefore bears on
[E0158](../../../problems/additive_bases/E0158/_index.md) without settling its
square-root lower-density question. There is no claim of a positive
constant times $x^\gamma$, optimality, priority, or a resolution of E0158.

## Current standing

The proof and all displayed consequences are author-recorded at tier 0.
No independent whole-claim acceptance or native Lean verification is
asserted. The elementary deductions are supplied in full; the standard
external inputs and their actual reading depth are stated in the proof.
No mathematical program, numerical certificate, or private input is needed
to use the argument.

The author check covers the product atom bound, localized factorization,
primitive plane and short-vector estimates, all conditional expectation
terms, uniform exponent balance, one infinite auxiliary realization,
simultaneous shell selections, and every real cutoff. Independent acceptance
would require scrutiny of this exact statement, proof, consequences, and
external interfaces. This record supplies no independently accepted
literature-proof coverage and makes no current literature-priority claim.

The reported bounded literature checking had partial
API coverage and outstanding MathSciNet review, with the additional search
limits stated in the proof. No fresh literature census or comparative record
assessment is supplied here.

## Remaining obligations

- [ ] Reconcile the result of
  [[research/leads/balanced_auxiliary_prime_density/_index|the balanced
  auxiliary-prime density lead]] (its whole-argument review and distinct grade
  of 2026-09-15 are retained under that lead's evidence/verify/) with this
  claim's statement and historical evidence without rewriting the old
  assessment, and decide the result's statement and tier as part of that
  integration, as the grade asks.
