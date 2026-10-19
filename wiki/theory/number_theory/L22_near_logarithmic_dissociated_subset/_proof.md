---
name: theory/number_theory/L22_near_logarithmic_dissociated_subset/_proof
title: Proof account for the near-logarithmic dissociation bound
desc: |
  A binary residue tree yields a pivot with companions whose differences have
  distinct 2-adic valuations, distinct valuations force dissociation after a
  short deletion, and an integer model transfers the bound to real sets; this
  account maps the Lean modules.
tags: []
sources:
- theory/number_theory/L22_near_logarithmic_dissociated_subset/_index
created: 2026-09-28T02:43:51Z
updated: 2026-10-13T13:08:56Z
---

***

This proves the entire statement of
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_index|L22]]
by machine-checked Lean, at tier 2 for the Lean sources of 2026-09-28 that
the card's standing names; the prose route it formalizes is the section "Proved
near-logarithmic bound via a binary tree" of
[[research/erdos_963/proof_sketch|the proof sketch]], together with that
page's reduction of a real configuration to an integer one. The formal entry
point is `Erdos.Problem963.exists_real_dissociated_large` in
`lean/Erdos/Problem963/CardBound.lean`: it takes a dissociated subset $B$ of
$A$ of maximum size (`Finset.exists_max_image`), applies
`real_card_bound_of_integer_card_bound` to `integer_card_bound` to get
$|A|\le(|B|+1)2^{|B|}$, and finishes with `log_bound_of_card_le`.

The modules, all in the namespace `Erdos.Problem963`, cover the argument as
follows. `BinaryWords.lean` encodes bounded natural numbers as binary words
(`encodeNat`, `codeSet`) and proves that a set of more than $2^h$ words
contains a word with $h+1$ companions at pairwise distinct first-difference
levels (`card_le_pow_of_branchRank_le`, `exists_large_levels`,
`exists_firstDiff_companions`); this is the prose count of branching vertices
on a root-to-leaf path, with words of length the largest element in place of
residues modulo $2^j$. `BitValuation.lean` identifies the first differing
bit of two bounded naturals with the 2-adic valuation of their integer
difference (`firstDiff_encodeNat_eq_padicValInt`). `ResidueTree.lean` turns
this into a pivot $a$ with more than $h$ companions whose differences from
$a$ have pairwise distinct 2-adic valuations, first for natural numbers and
then, after translation by the minimum, for integers
(`exists_nat_valuation_companions`, `exists_int_valuation_companions`).
`Valuation.lean` proves that nonzero integers with distinct valuations cannot
sum to zero (`sum_ne_zero_of_distinct_valuation`,
`signed_sum_ne_zero_of_distinct_valuation`), that the companions of the pivot
$0$ are dissociated (`zero_pivot_dissociated`), and that a nonzero pivot
together with companions whose valuations avoid the
$\lfloor\log_2(d+1)\rfloor+1$ values starting at the pivot's own valuation is
dissociated (`pivot_coefficient_valuation_bound`, `pivot_dissociated`); the
last converts two equal subset sums into a signed relation whose pivot
coefficient has magnitude at most $d+1$. `CardBound.lean` assembles the
integer estimate $|S|\le2^{d+\lfloor\log_2(d+1)\rfloor}\le(d+1)2^d$
(`integer_card_le_pow`, `integer_card_bound`). `IntegerModel.lean` builds
the integer model of a finite real set: a $\mathbb Q$-linear functional
that does not vanish on any of the finitely many nonzero differences of
subset sums (`Module.exists_dual_forall_apply_ne_zero`), with its
denominators cleared (`IsLocalization.exist_integer_multiples`), gives an
injective map to the integers preserving and reflecting every subset-sum
equality (`exists_rational_subset_sum_model`,
`exists_integer_subset_sum_model`); dissociation and the cardinal bound
transfer along it (`addDissociated_image_of_subset_sum_reflection`,
`real_card_bound_of_integer_card_bound`). Unlike the prose reduction, which
chooses a rational functional preserving the signs of all nonzero ternary
combinations, this model preserves subset-sum equalities only, which is all
the argument uses. `LogBound.lean` converts $n\le(d+1)2^d$ with $n\ge1$ into
$\log_2 n-\log_2(\log_2 n+1)\le d$ by the two cases $d\ge\log_2 n$ and
$d<\log_2 n$ (`log_bound_of_card_le`).
