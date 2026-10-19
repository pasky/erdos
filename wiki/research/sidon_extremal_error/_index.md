---
name: research/sidon_extremal_error
title: "Finite Sidon extremal error"
desc: "Problem 30's upper and lower error gaps, a linear-capacity barrier, parity and quartic obstructions to specified moment rules, a global signed linear completion, and the remaining positivity and construction problems."
created: 2026-10-15T18:04:27Z
updated: 2026-10-16T00:29:25Z
---

# Finite Sidon extremal error

[[research/_index|..]]

[[research/sidon_extremal_error/degree_four_extension|degree_four_extension]]: The degree-four Sidon relaxation, a rigorous obstruction to zeroing and uniformly renormalizing the block law, the need to break cyclic symmetry, and the remaining nonuniform-correction problem.

[[research/sidon_extremal_error/evidence/_index|evidence/]]: Exact finite checks of degree-two moments, lattice capacities, Singer arc discrepancy, and the genuine block law's short-count covariance, with separately scoped exploratory computations.

[[research/sidon_extremal_error/linear_capacity_barrier|linear_capacity_barrier]]: A genuine fixed-size block-sampling law satisfies every Sidon capacity in expectation up to sqrt(N)+N^(1/4)/2-O(1), obstructing single linear-capacity certificates below exponent 1/4; adaptive and nonlinear arguments remain outside this conclusion.

[[research/sidon_extremal_error/local_repair_gap|local_repair_gap]]: A progression family defeats the proposed small off-centre error estimate, and forbidden triples force singularity of the square repair matrix; a compatible global linear completion exists, while local and matrix-positive repairs remain open.

[[research/sidon_extremal_error/parity_obstruction|parity_obstruction]]: The parity identity obstructs zeroing block/uniform moments and sets a necessary budget for repairs; a global signed extension can restore this square, while full matrix positivity remains open.

[[research/sidon_extremal_error/perfect_difference_cuts|perfect_difference_cuts]]: Every arc count of a perfect difference set modulo q^2+q+1 lies within sqrt(q)(1+ln(M/2)) of its mean, so cuts of moderate order reach sqrt(N)-O(N^eps) only from an order within O(N^(1/4) log N) of sqrt(N).

[[research/sidon_extremal_error/proof_sketch|proof_sketch]]: Editable argument for Problem 30: separate upper and lower obligations, an explicit probability-measure obstruction to linear capacities, an exact failed quartic extension, sufficient variance inputs, and the remaining nonuniform moment and construction gaps.

[[research/sidon_extremal_error/short_count_covariance|short_count_covariance]]: A direct edge-intersection calculation gives the short-count covariance as a low-rank polynomial plus two absolute-value kernels, exposing a negative cumulative-sum form relevant to local moment repairs.

[[research/sidon_extremal_error/signed_linear_completion|signed_linear_completion]]: The complete author-recorded linear extension theorem separates Sidon zero and cardinality consistency from matrix positivity; global right inverses and a parity trade leave local and spectral control open.

***

This folder holds the sustained attack on
[[problems/additive_bases/E0030/_index|Problem 30]], whether the largest Sidon
set in an interval of length $N$ has size $\sqrt N+O_\epsilon(N^\epsilon)$. The
[[research/sidon_extremal_error/proof_sketch|proof sketch is the entry point and records the two obligations, the held links and the gaps]].
Its results not drawn from a cited source are Plasma AI's, author-recorded and
not independently reviewed; they settle neither half of the problem. The
earlier scope comparison is in
[[research/sidon_extension_interfaces/finite_extremality|the finite extremality account, which separates the error exponent from coefficient improvements]].

The precise original results are
[[theory/additive_bases/L216_sidon_linear_capacity_barrier/_index|L216, the probability-measure barrier]],
[[theory/additive_bases/L217_sidon_block_quartic_obstruction/_index|L217, the failure of zeroing followed by uniform moment renormalization]],
[[theory/additive_bases/L273_sidon_parity_obstruction/_index|L273, the parity obstruction for even block lengths and arbitrary block/uniform mixtures]],
and
[[theory/additive_combinatorics/L274_signed_sidon_moment_extension/_index|L274, signed linear completion with a parity-square refinement]].
Each has a complete author-recorded proof at tier 0. L217 has an exact finite
negative-square witness; L273 has exhaustive rational controls for its
identity and moment calculation. The
[[research/sidon_extremal_error/parity_obstruction|parity account]] gives a
necessary budget for further repairs. The
[[research/sidon_extremal_error/local_repair_gap|local-repair analysis]]
identifies the exact compatibility constraints and failures of the proposed
local kernel construction. L274 gives a global signed solution of the linear
constraints; full matrix positivity remains open. The
[[research/sidon_extremal_error/short_count_covariance|exact short-count covariance]]
provides a separate calculation for that spectral question.
