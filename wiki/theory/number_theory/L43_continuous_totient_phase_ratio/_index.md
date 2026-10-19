---
name: theory/number_theory/L43_continuous_totient_phase_ratio
title: Continuity of the totient phase coefficients
desc: |
  Under the unrefereed totients manuscript and L65, the phase coefficients of
  V and V' are continuous with the same jump factor at the period boundary,
  so the Problem 417 quotient is a continuous function on the circle.
id: L43
statement: |
  Assume the premises and conclusions of L65, with the definitions of A_H,
  alpha_s, G_m, gamma, lambda, rho and theta in the unrefereed September 2026 OpenAI
  manuscript An asymptotic formula for the number of totients, and put
  f0(r)=1/r. For every sufficiently large H and every f:[1,infinity)->[0,1],
  the function s->A_H(f;s) on 0<=s<1 is continuous outside finitely many
  points and has a right limit at every s in [0,1) and a left limit at every
  s in (0,1]; every uniform limit of such functions also has these one-sided
  limits. The functions A(1;s) and A(f0;s) are continuous on 0<=s<1, and for
  f=1 and f=f0 the left limit of A(f;s) at s=1 equals (lambda/gamma)A(f;0).
  Hence q(s)=A(f0;s)/A(1;s) is continuous on 0<=s<1 and its left limit at
  s=1 equals q(0), so q is a continuous function on R/Z. The set of
  subsequential limits of V(x)/V'(x) as x->infinity is exactly
  {1/q(s): 0<=s<1}, a compact interval. The ratio V(x)/V'(x) converges if
  and only if the integral of q(s)exp(-2 pi i n s) over 0<=s<1 vanishes for
  every nonzero integer n, and each such integral is the limit as
  H->infinity of the same integral with q replaced by
  A_H(f0;s)/A_H(1;s). Finally lambda>gamma, so A(1;s) is not constant.
  Here V(x) counts the distinct positive totients at most x, and V'(x)
  counts the distinct values phi(n) with 1<=n<=x.
status: proved
tier: 0
depends_on:
- L65
created: 2026-10-14T10:19:33Z
updated: 2026-10-14T10:24:24Z
---

# Continuity of the totient phase coefficients

[[theory/number_theory/_index|..]]

[[theory/number_theory/L43_continuous_totient_phase_ratio/_proof|_proof]]: Piecewise continuity of the finite coefficients, removal of interior jumps
by unit increments of the two counts, and the common jump factor of G_m at
the end of a phase period.

***

This conditional deduction is recorded by Plasma AI. It takes as premises the
results of the
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|unrefereed totients manuscript]]
that
[[theory/number_theory/L65_conditional_totient_ratio_coefficient/_index|L65]]
assumes, and it uses L65's conclusions: the uniform limit $A(f_0;s)$, its
positive lower bound, the asymptotic
$V'(x)=Z(x)(A(f_0;\theta(x))+o(1))$ with $Z(x)=xG_m/\log x$, and the
equivalence between convergence of $V/V'$ and constancy of
$q(s)=A(f_0;s)/A(1;s)$. The manuscript states that no regularity of its
phase coefficient is asserted or needed; this card supplies that regularity
from the same premises.

The [proof](_proof.md) has three parts. For a fixed cut the witness sets are
constant between finitely many phases, so each finite coefficient is piecewise
continuous and uniform limits keep one-sided limits. The counts $V$ and $V'$
change by at most one between consecutive integers while the phase moves by
$o(1)$, which removes every interior jump. At the end of a period the scale
factor $G_m$ jumps by the factor $\lambda/\gamma$, and both coefficients jump
back by the same factor, so their quotient joins up.

**Significance for Problem 417.** Constancy of $q$ cannot come from separate
constancy of the two coefficients: $A(1;\cdot)$ is provably nonconstant, and
the two coefficients carry the same boundary factor. A limit for $V/V'$ is
therefore an exact cancellation between two nonconstant functions. If $q$ is
nonconstant, the ratio oscillates continuously with the phase between
$\min 1/q$ and $\max 1/q$, and every intermediate value is a limit along an
exact-phase sequence. Since $q$ is continuous, the exact missing identity is
the vanishing of its nonzero Fourier coefficients, each a limit of an explicit
finite-cut integral. Continuity also means that constancy on a dense set of
phases would suffice. Because $q$ returns to $q(0)$ at the end of the period,
a one-sided comparison is enough as well: if $q(s)\le q(s')$ whenever
$0\le s\le s'<1$, then $q(0)\le q(s)\le\lim_{t\to1}q(t)=q(0)$ for every
$s$, so $q$ is constant. The same holds if the finite quotients satisfy
$q_H(s)\le q_H(s')+o(1)$ uniformly, since they converge uniformly to $q$.

**Standing.** Tier 0, author-recorded; no independent review or formalization.
It remains conditional on the unrefereed manuscript through L65, whose own
standing is tier 0. No constancy or nonconstancy of $q$ is established, so
[[problems/arithmetic_functions/E0417/_index|Problem 417]] remains open. The
[[research/leads/distinct_totient_preimage_ratio/_index|research route]]
records the remaining phase test. The strict inequality $\lambda>\gamma$
follows from the increase of the coefficients $a_j$, without a numerical
calculation. There is no computational evidence entry point.
