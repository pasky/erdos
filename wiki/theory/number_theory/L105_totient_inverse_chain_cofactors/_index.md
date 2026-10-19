---
name: theory/number_theory/L105_totient_inverse_chain_cofactors
title: Cofactor restrictions on infinite totient-plus-one inverse chains
desc: |
  An infinite increasing odd inverse chain for phi(n)+1 cannot have an
  eventually periodic largest-prime cofactor sequence, or have that
  cofactor eventually at most 9. A repeated block has an explicit 2-adic
  length bound; nonperiodic sequences remain uncontrolled.
id: L105
statement: |
  Let m_0,m_1,... be a strictly increasing infinite sequence of odd positive
  integers with phi(m_(i+1))+1=m_i for every i>=0. Let P+(n) denote the
  largest prime divisor of n, and put a_i=m_i/P+(m_i) for i>=1. Then the
  sequence (a_i) is not eventually periodic, and a_i>=11 for infinitely
  many i. More quantitatively, fix an integer r>=1 and odd integers
  a_1,...,a_r>=3, set
  d_j=phi(a_j), and write the composition of f_j(t)=a_j(t+d_j-1)/d_j
  in the order f_r after ... after f_1 as F(t)=(A t+B)/D, where
  A=product a_j and D=product d_j and B is the positive integer numerator
  obtained without canceling factors. For any integer k>=0, if t>0 is an
  integer and F^k(t) is an integer, then
  k v_2(D)<=v_2((A-D)t+B), where v_2 is the exponent
  of 2 in a positive integer. This bounds the number of consecutive
  repetitions of that cofactor block on any chain segment whose largest
  prime divides each term exactly once and is coprime to its cofactor.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T05:54:00Z
updated: 2026-10-15T06:01:00Z
---

# Cofactor restrictions on infinite totient-plus-one inverse chains

[[theory/number_theory/_index|..]]

[[theory/number_theory/L105_totient_inverse_chain_cofactors/_proof|_proof]]: Compose the exact inverse maps for fixed cofactors, linearize one block
at its negative fixed point, and compare 2-adic valuations. Necessary
prime-residue conditions force a cofactor sequence bounded by 9 to
become constant.

***

This elementary deduction is recorded by Plasma AI for
[[problems/arithmetic_functions/E0409/_index|Problem 409]]. An infinite
basin would contain an infinite increasing odd inverse chain. The claim
excludes an eventually repeated cofactor pattern, including the fixed
cofactor $3$ used by finite prime-tuple constructions. It also excludes
all chains that eventually have largest-prime cofactor at most $9$.

These exclusions do not prove any exceptional prime's basin finite.
Arbitrary nonperiodic sequences of bounded cofactors, and sequences of
unbounded cofactors, remain uncontrolled. The
[[research/erdos_409/_index|research sketch]] identifies this missing
comparison and explains why finite chains from varying roots do not
provide one infinite chain from a fixed root.

The proof uses exact affine identities and divisibility, with a four-row
necessary-transition table for cofactors $3,5,7,9$. It uses no conjecture
about primes and no computational enumeration. The bound applies to each
fixed starting integer and cofactor block; it is not a bound uniform over
all starting integers or all blocks.

**Standing.** Tier 0, author-recorded and unconditional, without
independent review or formalization. No solution of Problem 409 is
claimed. The evidence is the displayed proof, with no executable evidence
entry point needed.
