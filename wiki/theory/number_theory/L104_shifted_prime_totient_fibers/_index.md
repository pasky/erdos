---
name: theory/number_theory/L104_shifted_prime_totient_fibers
title: Almost every prime has the two-element totient-plus-one basin
desc: |
  The exceptional-prime theorem of Banks, Ford, Luca, Pappalardi and
  Shparlinski implies that all but x/(log x)^(2-delta) primes up to x
  have basin {p,2p} under phi(n)+1. Their union has integer density zero.
id: L104
statement: |
  Let phi be Euler's function, T(n)=phi(n)+1, and B_p the set of positive
  integers n for which T iterated zero or more times equals the prime p.
  For every odd prime p, B_p={p,2p} if and only if the only positive
  integer solutions of phi(n)=p-1 are p and 2p. For every delta>0 there is
  C_delta such that, for every x>=3, at most C_delta x/(log x)^(2-delta)
  primes p<=x have B_p different from {p,2p}. Thus almost every prime has
  a finite two-element basin, but the union of these basins has natural
  density zero among the positive integers.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T05:22:42Z
updated: 2026-10-18T03:07:19Z
---

# Almost every prime has the two-element totient-plus-one basin

[[theory/number_theory/_index|..]]

[[theory/number_theory/L104_shifted_prime_totient_fibers/_proof|_proof]]: Apply the 2005 exceptional-prime theorem and the absence of predecessors
of 2p to identify almost every prime basin. A supplementary reconstruction
of a weaker count uses the source's largest-prime splitting mechanism.

***

This basin deduction is recorded by Plasma AI. Its number-theoretic input
is the exceptional-prime theorem of Banks, Ford, Luca, Pappalardi and
Shparlinski, *Values of the Euler Function in Various Sequences*,
Monatshefte für Mathematik 146 (2005), 1–19, [[../library/arithmetic_functions/banks_et_al_2005_values_euler_function_various_sequences/theorem_4_1|Theorem 4.1]]
([author manuscript, pp. 14–15](https://www.ford126.web.illinois.edu/wwwpapers/philam.pdf),
accessed 2026-10-15).
That theorem already bounds the primes $p$ for which $p-1$ has a totient
preimage other than $p$ and $2p$ by

$$
\frac{x}{(\log x)^2}
\exp\bigl((\kappa+o(1))(\log\log\log x)^2\bigr),
\qquad \kappa=0.8178\ldots .
$$

The source's introduction explicitly records the almost-all-primes
consequence. The counting theorem is theirs; the present claim identifies
its consequence for the entire iteration basin, using the fact that $2p$
has no predecessor. It bears on
[[problems/arithmetic_functions/E0409/_index|Problem 409]], which asks about
the iteration $n\mapsto\varphi(n)+1$: how many steps are needed to reach a
prime, whether infinitely many $n$ can reach the same prime, and the
density of the $n$ that reach a fixed prime. The claim answers the second
and third questions for almost every prime: such a prime is reached only
from $p$ itself and from $2p$, so its basin is finite and has density zero.
It does not control the basin of any exceptional prime. Indeed the union
of the two-element basins is contained in the primes and twice the primes,
so it has density zero among integers. Almost every integer therefore
terminates at an exceptional prime, despite the exceptional primes having
relative density zero. This gives no positive density to any one of their
basins. Whether some prime has an infinite basin, and the step-count
question, remain open.

An argument posted on the problem's forum thread on
22 July 2026 by the account ankit, recorded on
[[problems/arithmetic_functions/E0409/claims/2026_07_22_ankit|its claim page]],
treats the primes $p\equiv3\pmod4$ by $2$-adic valuation and leaves
$O(\sqrt x)$ exceptions there. The earlier 2005 theorem covers all residue
classes with a weaker exception bound than this specialized argument.

The [proof](_proof.md) first gives the basin implication from that source
theorem. It also records a weaker-count reconstruction by the same
largest-prime split: smooth preimages, preimages divisible by the square
of a large prime, and a two-prime upper-bound sieve summed over distinct
totient values. That reconstruction is not a new counting result. It uses
the sparsity of totient values in Erdős's 1935 bound, held as
[[../library/arithmetic_functions/erdos_1935_normal_number_prime_factors_related_problems/_index|his paper's card]];
the sieve inequalities are classical and cited in the proof.

**Standing.** Tier 0, author-recorded, with no independent review or
formalization. It is unconditional. There is no computational evidence
entry point: the evidence is the displayed argument. It does not resolve
Problem 409, whose status is unchanged.
