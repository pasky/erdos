---
name: research/sharp_dissociated_subset
title: Sharp dissociated-subset bound
desc: An attack on f(n) >= floor(log_2 n) for Problem 963. Multiscale pivot estimates prove the sharp bound for absolute values of ratio at most 4/3, a constant loss at ratio two, and a triple-logarithmic loss in general.
created: 2026-10-15T18:14:21Z
updated: 2026-10-15T22:50:16Z
---

# Sharp dissociated-subset bound

[[research/_index|..]]

[[research/sharp_dissociated_subset/evidence/_index|evidence/]]: Exact checks of odd-progression dissociation numbers, limits of fixed-pivot and freely centered certificates, and explicit certificates separating these models, run by one entry point.

[[research/sharp_dissociated_subset/pivot_certificates|pivot_certificates]]: Graded and recentered pivot lemmas, a lattice form, and exact limits of their certificates. A split-leaf family obstructs the stronger odd extraction at every fixed aspect ratio above one.

[[research/sharp_dissociated_subset/proof_sketch|proof_sketch]]: Multiscale averaging proves the sharp bound when nonzero absolute values lie within a factor 4/3, a constant loss at ratio two, and a triple-logarithmic loss in general. The remaining gaps are combining scales and removing the bounded-ratio constant.

[[research/sharp_dissociated_subset/weighted_folding|weighted_folding]]: Folding elements near multiples of a common modulus resolves repeated-source choices under a strict total budget. A dyadic interval construction refutes a generic weighted Kraft packing inequality, leaving the arithmetic structure of the virtual points essential.

***

This folder holds an attack, by Plasma AI, on the bound
$f(n)\ge\lfloor\log_2n\rfloor$ asked by
[[problems/number_theory/E0963/_index|Problem 963]]: every set of $n$ reals
should contain a dissociated subset of size $\lfloor\log_2n\rfloor$. The
[[research/sharp_dissociated_subset/proof_sketch|editable proof sketch]]
states the target, the established links, the two remaining gaps and the
next moves. The
[[research/sharp_dissociated_subset/pivot_certificates|certificate note]]
proves the graded pivot lemma that underlies the route and records exact
examples of what single-pivot certificates cannot prove.

The route has produced two author-recorded lower bounds:
[[theory/number_theory/L212_bounded_ratio_dissociated_subset/_index|L212, the sharp positive bound at ratio 4/3 and the bound |P| < 3 times 2^d(P) at ratio two]],
and
[[theory/number_theory/L213_triple_log_dissociated_subset/_index|L213, the bound f(n) >= log_2 n - log_2 log_2 log_2 n - O(1) for all real sets]].
The structural obstruction
[[theory/number_theory/L270_recentered_pivot_obstruction/_index|L270]]
shows that a single recentered graded certificate cannot always supply
the stronger odd extraction, even at an arbitrarily small fixed ratio
above one. Its explicit example still has the required dissociated
subset. All three claims are tier 0.
The earlier work on the problem, including the tier-2 bound L22 and the
odd-slice reduction, is in
[[research/erdos_963/_index|the Problem 963 research folder]]. The problem
remains open.
