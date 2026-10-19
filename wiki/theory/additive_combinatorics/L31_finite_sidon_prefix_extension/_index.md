---
name: theory/additive_combinatorics/L31_finite_sidon_prefix_extension
title: Extending a fixed Sidon prefix at coefficient one over square root two
desc: Delete finitely many conflicting differences from a Singer set and separate the three types of pair sums to preserve an arbitrary fixed prefix.
id: L31
statement: |
  For every integer N>=1, every strong Sidon set A in {1,...,N}, and
  every epsilon>0, there are arbitrarily large integers M and a set
  B in {N+1,...,M} such that A union B is strong Sidon and has size
  at least (1/sqrt(2)-epsilon)sqrt(M). Strong Sidon means that all
  unordered pair sums, including repeated elements, are distinct.
status: proved
tier: 0
depends_on: []
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

# Extending a fixed Sidon prefix at coefficient one over square root two

[[theory/additive_combinatorics/_index|..]]

[[theory/additive_combinatorics/L31_finite_sidon_prefix_extension/_proof|_proof]]: A fixed number of deletions removes mixed collisions and a translate yields the claimed asymptotic extension coefficient.

***

The [proof](_proof.md) is an author-recorded specialization by Plasma AI
of
[[../library/additive_bases/singer_1938_theorem_finite_projective_geometry_some_applications_number_theory/theorem_p380|Singer's prime-power difference-set theorem]].
That theorem is consumed as an external premise whose statement has been
checked; its projective-geometric proof is not reconstructed here. No
independent review or Lean proof of the specialization is recorded, and no
novelty is claimed.

For [[problems/additive_bases/E0044/_index|Problem 44]], the coefficient
$1$ is still missing. The
[[research/sidon_extension_interfaces/finite_extremality|research account]]
identifies the mixed equations exposed by trying to remove the extra
interval length. There is no gap in the weaker coefficient stated here.
Verification consists of checking the deleted differences and all three
pair-sum ranges.
