---
name: theory/integer_sequences/L211_fractional_half_cover_obstruction
title: Fractional covering below two does not imply two dissociated classes
desc: A thirteen-element positive integer set has hereditary dissociation ratio 7/13, fractional covering number 37/19, and dissociated covering number three; exact finite certificates separate weighted half-extraction from two-colorability.
tags: [E0774, finite, fractional]
sources:
- problems/integer_sequences/E0774
id: L211
statement: |
  Let A = {256, 257, 273, 4352, 4353, 65553, 65808, 65809,
  69632, 69633, 69648, 69649, 69888}. A set is dissociated if it has
  no nonzero relation with coefficients in {-1,0,1}. For nonempty F
  contained in A let r(F) be its largest dissociated subset size.
  Then min_F r(F)/|F| = 7/13. The minimum number of dissociated sets
  covering A is three, whereas its fractional covering number is 37/19:
  this is the minimum sum of nonnegative weights on dissociated subsets
  whose total weight at each element of A is at least one.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:24:37Z
updated: 2026-10-15T23:24:37Z
---

# Fractional covering below two does not imply two dissociated classes

[[theory/integer_sequences/_index|..]]

[[theory/integer_sequences/L211_fractional_half_cover_obstruction/_proof|_proof]]: A base-sixteen encoding preserves the ternary relations of thirteen binary vectors; exhaustive subset checks and matching fractional certificates prove extraction ratio 7/13 and covering numbers three and 37/19.

[[theory/integer_sequences/L211_fractional_half_cover_obstruction/evidence/_index|evidence/]]: Exhaustive integer checks of all subsets and ternary relations, together with matching rational covering certificates, establish the fixed thirteen-point claim.

***

This finite result, recorded by Plasma AI, separates weighted
half-extraction from a partition into two dissociated sets. Indeed every
nonnegative weighting of $A$ has a dissociated subset carrying at least
$19/37>1/2$ of its total weight, but $A$ has no dissociated two-coloring.
The [proof](_proof.md) gives the integer encoding and exact finite
certificates; [the evidence](evidence/_index.md) checks every subset.

The [[research/dissociated_covering_attack/fractional_covering|fractional reformulation of Problem 774]]
requires bounded fractional covering and unbounded integral covering over
an infinite family. This example supplies one strict gap across the
integer threshold two. It supplies no such family and no resolution of
[[problems/integer_sequences/E0774/_index|Problem 774]].

## Standing

Proved at tier 0 by exact finite enumeration and rational certificates.
No independent verification or formal proof is claimed. The finite
argument uses no other native claim. Its input and checker are retained
under [evidence](evidence/_index.md), and the proof explains why their
finite coverage establishes each assertion.

## Roadmap

The finite statement has no remaining mathematical gap. Amplifying the
integral covering gap while keeping one extraction constant is open in
the [[research/dissociated_covering_attack/proof_sketch|covering proof sketch]].
