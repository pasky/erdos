---
name: research/erdos_809/proofs
title: A proof of the seven-cycle threshold
desc: Six notes for the C7 threshold, from finite palette savings through graph cleaning and the near-Turán cases, and two for Plasma AI's bounds above the threshold.
created: 2026-09-24T00:00:00Z
updated: 2026-10-13T02:31:05Z
---

# A proof of the seven-cycle threshold

[[research/erdos_809/_index|..]]

[[research/erdos_809/proofs/c7_density_lower_bound|c7_density_lower_bound]]: Plasma AI's lower bound on the seven-cycle maximal anti-Ramsey function above the Turán threshold, from the finite inequality and cleaning; not independently reviewed.

[[research/erdos_809/proofs/c7_five_clique_construction|c7_five_clique_construction]]: Plasma AI's construction showing that the Bucić–Chen–Ma coefficient fails for seven-cycles at every density strictly between 1/4 and 1/2; not independently reviewed.

[[research/erdos_809/proofs/c7_homomorphic_cleaning|c7_homomorphic_cleaning]]: Regularity cleaning separates repeated colors on closed seven-walks and transfers the threshold question to weighted templates.

[[research/erdos_809/proofs/c7_joint_clique_mass|c7_joint_clique_mass]]: A constrained maximization and weighted Hajnal argument for the clique-mass bound used in the seven-cycle threshold proof.

[[research/erdos_809/proofs/c7_near_bipartite|c7_near_bipartite]]: The rainbow-color lower bound at o(n squared) edit distance from bipartite, with no minimum-degree assumption.

[[research/erdos_809/proofs/c7_near_regular|c7_near_regular]]: The rainbow-color lower bound when minimum degree is n/2 up to a lower-order error.

[[research/erdos_809/proofs/c7_palette_savings|c7_palette_savings]]: The finite weighted-template inequality, using a functional palette lemma and the joint-clique mass bound.

[[research/erdos_809/proofs/c7_solution|c7_solution]]: The argument combines a joint-walk clique bound, palette savings, cleaning, and the near-Turán boundary cases.

***

The [solution note](c7_solution.md)
combines the finite and graph arguments. Its dependencies are, in reading order,
[joint clique mass](c7_joint_clique_mass.md), [palette savings](c7_palette_savings.md),
[near-bipartite graphs](c7_near_bipartite.md), [near-regular graphs](c7_near_regular.md),
and [seven-walk cleaning](c7_homomorphic_cleaning.md). The [Lean account](../formalization.md)
identifies the corresponding Lean modules and the successful targeted build in
this repository. The argument is the $k=3$ branch of native claim
[[theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/_index|L17]], accepted at
tier 2 on 2026-09-25 for the Lean sources and the statement as they stood on
2026-09-25T03:40:15Z (first carried by the default branch on 2026-09-28); the
solution note states the standing of
the prose proof, which remains author-recorded. [Earlier research notes](../archive/_index.md) give context
for routes considered before the proof.

Two further notes record results of Plasma AI's write-up above the threshold,
neither independently reviewed here nor formalized: the
[density lower bound](c7_density_lower_bound.md) for every edge density above
the Turán threshold, which uses the threshold proof, and the
[five-clique construction](c7_five_clique_construction.md), which shows that
the Bucić–Chen–Ma coefficient fails for $C_7$ at every interior density. The
write-up's further questions are on the
[open questions](../open_questions.md) page.
