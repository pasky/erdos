---
name: research/sidon_extremal_error/signed_linear_completion
title: "Signed linear completion of Sidon moments"
desc: "The complete author-recorded linear extension theorem separates Sidon zero and cardinality consistency from matrix positivity; global right inverses and a parity trade leave local and spectral control open."
created: 2026-10-16T00:29:25Z
updated: 2026-10-16T00:29:25Z
---

***

[[theory/additive_combinatorics/L274_signed_sidon_moment_extension/_index|L274]]
is Plasma AI's complete author-recorded theorem, at tier 0 without independent
review. For every $N\ge55$, the first and second moments of any genuine law
on $k$-subsets of $\{0,\ldots,N-1\}$ extend to real signed moments through
degree four satisfying every strong-Sidon zero and every local cardinality
identity. For $N\ge58$, the extension can also preserve exactly the genuine
variance of $A=\sum_{i<j}(-1)^{i+j}z_iz_j$. Positivity of the full moment
matrix is not part of the theorem.

The
[[theory/additive_combinatorics/L274_signed_sidon_moment_extension/_proof|proof]]
uses inclusion matrices $B_r$ between Sidon $r$- and $(r+1)$-sets. Elementary
Gram identities give $B_2B_2^{\mathsf T}\succeq(N-13)I$ and
$B_3B_3^{\mathsf T}\succeq(N-54)I$. Thus every required row datum has a
signed preimage. The proof also identifies the exact restriction of
zero-three-margin functions to forbidden four-sets: their sums must vanish
on the four-sets containing each forbidden triple. The putative square
inverse in the [[research/sidon_extremal_error/local_repair_gap|local-kernel
construction]] is singular because it ignores these relations. This does
not obstruct a compatible global repair.

If $f$ is prescribed on forbidden triples, its complementary correction on
Sidon triples can be chosen with Euclidean norm at most
$3\|f\|_2/\sqrt{N-13}$. If $f$ is prescribed on forbidden four-sets and
meets the compatibility equations, the corresponding bound is
$\sqrt{48/(N-54)}\|f\|_2$. These are bounds on moment vectors, with all
supports counted once. They do not bound the smallest eigenvalue of the
quadratic moment matrix after correction.

A signed trade supported on the sixteen four-sets selecting one element from
each pair in $(0,1),(4,9),(16,27),(40,57)$ changes the alternating square
while preserving every linear constraint. Its full eight-point support is
Sidon; the proof lists all positive differences. This explains why the
[[theory/additive_bases/L273_sidon_parity_obstruction/_index|negative parity square of the zeroing rule]]
is a defect of that rule rather than an obstruction to all signed linear
extensions. The trade may harm other squares.

The remaining task is a matrix-positive extension, with control suited to all
quadratic test polynomials. A localized version of the global inverse, or
another quantitatively controlled correction, could be useful for that task.
The [[research/sidon_extremal_error/proof_sketch|proof sketch]] keeps it
separate from the upper and all-$N$ lower estimates for Problem 30.
