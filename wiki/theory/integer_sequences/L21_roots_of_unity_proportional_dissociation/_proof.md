---
name: theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_proof
title: Proof account for the proportional dissociation of the roots of unity
desc: |
  Finite interpolation, Khintchine moments and a Riesz-product average give
  a Pisier-type extraction from the analytic Sidon constant; this account
  maps the Lean modules.
tags: []
sources:
- theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_index
created: 2026-09-25T22:01:44Z
updated: 2026-10-13T13:08:56Z
---

***

This proves the entire statement of
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_index|L21]]
by machine-checked Lean, at tier 2 for the Lean sources of 2026-09-28 that
the card's standing names; the
[[research/erdos_774/lean_proof_map|Lean proof map]]
lists the modules stage by stage. The formal entry point is
`Erdos.Research.Problem774.rootsOfUnity_proportionalDissociation` in
`lean/Erdos/RootsOfUnitySidon/RootsOfUnitySidonComplete.lean`, which applies
`statement_of_analyticSidon_of_pisier` to the analytic Sidon theorem (the
subject of [[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_index|L20]]) and to the finite Pisier
implication `PisierForwardComplete.pisierForward`. That implication is proved
in the same folder: given a Sidon constant and a finite set of frequencies,
finite interpolation and Khintchine's inequality bound the even moments of
the real character sum (`FiniteSidonInterpolation.lean`,
`FiniteKhintchine.lean`), one finite character sample captures all moments
through the needed order (`FiniteOrthogonalCharacters.lean`,
`FiniteMomentOrthogonality.lean`), a Riesz-product average bounds the
weighted count of signed relations (`FiniteRieszMomentBound.lean`,
`PisierRelationCounting.lean`), and two counting lemmas select a
proportional relation-free subset (`PisierFixedSizeThinning.lean`,
`PisierThinningAssembly.lean`). The definitions `rootsOfUnity`,
`UniformExtraction` and `statement` live in `RootsOfUnitySidon.lean`.
