---
name: theory/discrete_geometry/L143_split_class_rarity
title: Rare distances when one quadratic form splits few classes
desc: If some traceless quadratic form takes unequal values on equal-length pairs in only kappa distance classes, at least (n-1-2 kappa (M+2))/4 distances occur at most n times.
id: L143
statement: |
  Let A be a set of n>=2 points in the Euclidean plane. A class is the set of
  unordered pairs of A at one occurring distance, and R(A) is the number of
  classes with at most n pairs. For a nonzero real traceless symmetric 2x2
  matrix S, a class is S-split if it contains two pairs with difference
  vectors d,e such that d^T S d differs from e^T S e. Let kappa(A) be the
  least number of S-split classes over all such S, and M(A) the largest
  number of points of A on one circle of positive radius. Then
  R(A) >= (n-1-2 kappa(A) (M(A)+2))/4.
status: proved
tier: 0
depends_on: []
created: 2026-10-15T11:12:05Z
updated: 2026-10-15T11:12:50Z
---

# Rare distances when one quadratic form splits few classes

[[theory/discrete_geometry/_index|..]]

[[theory/discrete_geometry/L143_split_class_rarity/_proof|_proof]]: Unsplit classes have fixed absolute displacements, so long ones have maximum degree two; anchor distances outside split circles give the rare classes.

***

The [proof](_proof.md) is a complete author-recorded argument by Plasma AI,
without independent review or Lean proof. It uses no external theorem.

The case $\kappa(A)=0$ is the deformable case of the
[[research/erdos_132/affine_deformations|affine-deformation criterion]] for
[[problems/distance_problems/E0132/_index|Problem 132]]: some nonsimilarity
affine map preserves every distance equality. The bound reaches further,
to configurations in which the equal-length tensors span both dimensions but
one form splits few classes. The
[[research/erdos_132/split_class_deformations|research account]] gives such a
configuration and, conditional on the retained author-recorded weighted-circle
bound, the consequence that every form must split polynomially many classes
of a bounded-rarity configuration. It also describes the rotation-rich
classes that every form splits, which leave the general question open.
No gap remains in this inequality.
