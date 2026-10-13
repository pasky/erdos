---
name: research/erdos_809
title: Proof of the rainbow odd-cycle threshold
desc: The seven-cycle argument and Lean formalization of the full k≥3 threshold, recorded as claim L17 and accepted at tier 2 on 2026-09-25 for its audited Lean sources and statement.
created: 2026-09-24T00:00:00Z
updated: 2026-10-13T02:31:05Z
---

# Proof of the rainbow odd-cycle threshold

[[research/_index|..]]

[[research/erdos_809/archive/_index|archive/]]: Earlier finite-template, spectral, geometric, and construction notes, preserved with their original local scope.

[[research/erdos_809/evidence/_index|evidence/]]: Retained publication files of the Erdős 809 formalization: the Mathlib-only
challenge statement, the solution module, the comparator configuration, the
registry entry (PALOMAR-2026-09-30-000004) and the write-up, kept as assets
beside the research folder.

[[research/erdos_809/formalization|formalization]]: The Lean theorem covers every k≥3 by combining the seven-cycle proof with the Bucić–Chen–Ma k≥4 theorem.

[[research/erdos_809/open_questions|open_questions]]: The five further questions of Plasma AI's seven-cycle write-up: the interior coefficient, stability, compatible edge families, the error term and a proof without regularity.

[[research/erdos_809/proofs/_index|proofs/]]: Six notes for the C7 threshold, from finite palette savings through graph cleaning and the near-Turán cases, and two for Plasma AI's bounds above the threshold.

***

The [seven-cycle proof](proofs/_index.md) supplies the $k=3$ branch of
[[problems/ramsey_theory/E0809/_index|Problem 809]]. The $k\ge4$ branch follows the
full-density theorem of Bucić, Chen and Ma
([[../library/ramsey_theory/bucic_2026_maximal_anti_ramsey_conjecture_burr_erdos/theorem_1_2|Theorem 1.2]]).
The [formalization account](formalization.md) identifies the complete Lean
statement and the modules for both branches. The final theorem's import chain
builds against this repository's pinned Lean and Mathlib versions. The result
is recorded as native claim [[theory/ramsey_theory/L17_rainbow_odd_cycle_threshold/_index|L17]]; the corpus build and native audit pass, and
the independent whole-statement fidelity audit, its grade and a non-author
clean gate are filed on the claim page, so the claim stands at tier 2
(accepted on 2026-09-25 for the Lean sources and the statement as they stood
on 2026-09-25T03:40:15Z)
and the problem page records the question as proved.

Priority. Asad Shahab's independent proof claim, a proof of the seven-cycle case
with a preprint (arXiv:2609.38286, 29 September 2026) and a Lean development
whose headline theorem covers every odd cycle $C_{2k+1}$ with $k\ge3$, was filed
on the site's proof-claims tab first, as proof claim 358, before the project's
claim 367 on the same day, 27 September 2026; this corpus built that development
at its pinned commit and audited its statement on 2026-10-08. The seven-cycle
argument here is the project's own in authorship and was not the first posted,
as [[problems/ramsey_theory/E0809/_index|the problem page]] records from the
site's page as it stood on 2026-10-05.

Read the [six C7 proof notes](proofs/_index.md) in their stated order, then
the [formalization account](formalization.md) for the Lean assembly. The
[research archive](archive/_index.md) preserves earlier finite-template
routes, counterexamples to stronger formulas, and bounded experiments. Its
local unresolved questions do not remain gaps in the threshold proof.

Plasma AI's write-up of the seven-cycle proof, held in the
[research evidence](evidence/_index.md), also proves a lower bound at every
edge density above the Turán threshold and a construction beating the
longer-cycle formula at every interior density. Both are recorded among the [proof notes](proofs/_index.md)
as the write-up's results, not independently reviewed here. Its further
questions are collected on the [open questions](open_questions.md) page.
