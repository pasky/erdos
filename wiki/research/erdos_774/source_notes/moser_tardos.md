---
name: research/erdos_774/source_notes/moser_tardos
title: "A constructive proof of the general Lovasz Local Lemma"
desc: "Source notes for Problem 774: A constructive proof of the general Lovasz Local Lemma."
tags: []
sources: []
created: 2026-09-24T22:18:19Z
updated: 2026-10-13T04:56:43Z
---

# A constructive proof of the general Lovasz Local Lemma

[Library card and held copy](../../../../library/set_systems/moser_tardos_2009_constructive_proof_general_lovasz_local_lemma/_index.md).

***

Robin A. Moser and Gábor Tardos, "A constructive proof of the general
Lovász Local Lemma," arXiv:0903.0544 (2009).

## What the research consumes

The card carries the digest of Algorithm 1.1, Theorem 1.2, the parallel and
derandomized variants, and the lopsidependency extension. The research
uses **Theorem 1.1**, the asymmetric local lemma in the independent-variable
setting, in three places: the
[decomposable-cycle coloring](../lemmas/decomposable_cycle_colors.md), the
[joined-boundary coloring](../lemmas/joined_boundary_colors.md), and the
elementary-boundary avoidance in the
[simplicial checks](../routes/shift_simplicial_gain_checks.md), where the
symmetric condition follows by choosing $x=1/(D+1)$. In each case the
events are the monochromaticity of selected relation supports under an
independent uniform coloring, with $\Pr[B_F]=q^{1-|F|}$ and dependency
neighborhoods the supports meeting $F$. Reading depth is claims checked
for Theorem 1.1 in the held copy.

## Exact limits

A color class is dissociated only when it avoids every relation support,
so a local-lemma coloring of a selected subfamily colors those templates
only; proportional dissociation supplies neither the overlap bounds nor the
weights needed for all relations of unbounded length. That is why the two
coloring theorems above are upper results for template families and not
obstructions to unbounded actual coloring.
