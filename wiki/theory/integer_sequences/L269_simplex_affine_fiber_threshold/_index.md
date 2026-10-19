---
name: theory/integer_sequences/L269_simplex_affine_fiber_threshold
title: The exact affine-fiber threshold in a simplex tensor
desc: In the k-fold tensor of a q-point simplex over a prime-power index field, every affine fiber with nonzero coefficients is rationally independent for k<q and contains an explicit ternary relation for k>=q.
tags: [E0774, tensor, finite-field]
sources:
- problems/integer_sequences/E0774
id: L269
statement: |
  Let q>=3 be a prime power, k>=1, and index the columns of
  [I_(q-1) | -1] by the elements of F_q in any order. Index the
  columns of its k-fold tensor power by x in F_q^k. For nonzero
  ell_1,...,ell_k in F_q and any a in F_q, the columns indexed by
  H_a={x: sum_i ell_i x_i=a} are dissociated if and only if k<q.
  For k<q they are linearly independent over Q. For k>=q there is
  a nonzero relation on H_a with coefficients in {-1,0,1} whose
  support has exactly 2 q^(q-2) elements. The relations and linear
  independence are over the characteristic-zero vector space;
  F_q indexes columns and defines the fiber only.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T23:24:37Z
updated: 2026-10-15T23:24:37Z
---

# The exact affine-fiber threshold in a simplex tensor

[[theory/integer_sequences/_index|..]]

[[theory/integer_sequences/L269_simplex_affine_fiber_threshold/_proof|_proof]]: Translation of the additive Fourier transform proves independence below q factors, and a difference of two codimension-two fibers constructs a ternary relation at and above q factors.

[[theory/integer_sequences/L269_simplex_affine_fiber_threshold/evidence/_index|evidence/]]: Exact small tensors certify rational independence below the threshold and check the displayed ternary trades at and above it over both a prime field and a non-prime finite field.

***

The [Fourier proof](_proof.md), recorded by Plasma AI, gives an exact
boundary for scalar linear fiber colorings. Below the boundary, one
frequency translate avoids every zero coordinate. At the boundary,
a difference of two affine codimension-two fibers supplies a flat
relation, and fixing the extra coordinates gives the same support above
it. The characteristic-zero relation convention is essential.

## Standing

Proved at tier 0 by the displayed finite-field Fourier argument.
[Local exact evidence](evidence/_index.md) checks the boundary at $q=3$
and $q=4$, including a non-prime field and direct integer tensor images.
The evidence is diagnostic; the proof covers all prime powers and all
numbers of factors. No independent verification or formal proof is claimed.
No other native L-claim is consumed.

## Roadmap

The statement has no remaining mathematical gap. Its obstruction applies
to scalar linear fibers and their coarsenings or coordinatewise symbol
permutations. Arbitrary palettes remain open in the
[[research/dissociated_covering_attack/repeated_simplex|repeated-simplex route]];
failure of these algebraic colorings alone does not imply unbounded
covering number.
