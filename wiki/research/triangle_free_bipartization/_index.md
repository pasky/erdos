---
name: research/triangle_free_bipartization
title: Middle-density triangle-free bipartization
desc: The open middle-density case of Problem 23, with its editable proof sketch, exact obstructions to profile-envelope relaxations, and their evidence.
created: 2026-10-15T23:29:23Z
updated: 2026-10-17T10:42:43Z
---

# Middle-density triangle-free bipartization

[[research/_index|..]]

[[research/triangle_free_bipartization/evidence/_index|evidence/]]: Exact profile bounds, two-root switching traps and controls for hereditary and recursive comparisons, with bounded numerical discovery for the whole-band argument kept separate from evidence.

[[research/triangle_free_bipartization/profile_envelope_obstructions|profile_envelope_obstructions]]: Exact root-count and linear-band envelope obstructions, a rooted repair for the Higman–Sims mixture, and an in-band mixture defeating constant-weight contradiction rows on at most four roots.

[[research/triangle_free_bipartization/proof_sketch|proof_sketch]]: Editable sketch of the attack on the open middle-density band of Problem 23, separating the held tail results, author-recorded partial results, tested routes with their exact obstructions, and the remaining gap.

[[research/triangle_free_bipartization/two_root_switching_traps|two_root_switching_traps]]: A probabilistic construction with an exact finite gain table refutes the two-root stability implication for the middle band; an exhibited three-root move escapes, and the original bipartization bound holds throughout the construction.

***

This folder holds the sustained attack on the case of
[[problems/extremal_graph_theory/E0023/_index|Problem 23]] that the known
density tails leave open: the conjecture that every triangle-free graph on
$N$ vertices whose edge density $p=2e/N^2$ satisfies
$1243/5000<p<3197/10000$ can be made bipartite by deleting at most
$N^2/25$ edges.

[[research/triangle_free_bipartization/proof_sketch|The proof sketch]]
states the target, the held tail results, three author-recorded partial
results, the routes tried and the gap that remains.
[[research/triangle_free_bipartization/profile_envelope_obstructions|The obstruction record]]
records the exact Clebsch obstruction for at most five roots and the
[[theory/extremal_graph_theory/L240_seven_root_linear_band_obstruction/_index|seven-root
linear-band obstruction of L240]]. The latter uses a mixture of the
Higman–Sims and balanced pentagon density vectors at interior density
$1/4$, forcing slack at least $1/1200$ at every convex relaxation order.
Its lower bound is checked by exact integer-Gram branching; stronger
numerical optimum reports are kept separate. An explicit order-five rooted
degree inequality removes this mixture in the contradiction formulation.
Inside the band, a mixture of the $C_{13}(1,5)$ and Clebsch graphons
defeats every certificate whose cut rows on at most four roots carry
constant weights. The sketch records the localized rooted route, its
floating-point linear-programming tests, and the unresolved full-positivity
and exact cut-pricing test;
[[research/leads/triangle_free_middle_band/_index|the middle-band lead]]
tracks that route.

The work here is by Plasma AI. It is author-recorded and has not been
independently reviewed. The full problem remains open.
