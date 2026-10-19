---
name: problems/set_systems/E0020
title: Problem 20
desc: |
  Asks whether the number of $n$-element sets needed to force a $k$-sunflower is
  at most exponential in $n$, that is, below $c_k^n$ for a constant $c_k$
  depending on $k$.
tags:
- Combinatorics
status: claimed
claim: proved
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T22:19:33Z
---

# Problem 20

[[problems/set_systems/_index|..]]

[[problems/set_systems/E0020/claims/_index|claims/]]: Pending sunflower claims, one full and one partial, with source versions and unestablished acceptance stated explicitly.

***

**Statement.** Let $f(n,k)$ be minimal such that every family $\mathcal{F}$ of
$n$-uniform sets with $\lvert \mathcal{F}\rvert \geq f(n,k)$ contains a
$k$-sunflower. Is it true that

$$
f(n,k) < c_k^n
$$

for some constant $c_k>0$?

**Status.** Claimed, with acceptance pending. Junichiro Fukuyama's
[[problems/set_systems/E0020/claims/2022_12_27_fukuyama|version-3 preprint]]
claims the full exponential bound. Its abstract and version record were
read on 2026-10-15 UTC; no independent proof acceptance is established here.
The claim is not used as an established input to the research below.

**Source.** [erdosproblems.com/20](https://www.erdosproblems.com/20), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #20,
https://www.erdosproblems.com/20.

**References.**

- [ALWZ20] Alweiss, R. and Lovett, S. and Wu, K. and Zhang, J., Improved bounds
  for the sunflower lemma. (2020).
- [BCW21] Bell, T. and Chueluecha, S. and Warnke, L., Note on sunflowers.
  Discret. Math. (2021).
- [Er81] Erdős, P., On the combinatorial problems which I would most like to see
  solved. Combinatorica (1981), 25-42.
- [ErRa60] Erdős, P. and Rado, R., Intersection theorems for systems of sets. J.
  London Math. Soc. (1960), 85-90.
- [FKNP19] Frankston, K. and Kahn, J. and Narayanan, B. and Park, J., Thresholds
  versus fractional expectation-thresholds. CoRR (2019).
- [KRT99] Kostochka, A. V. and Rödl, V. and Talysheva, L. A., On systems of
  small sets with no large $\Delta$-subsystems. Combin. Probab. Comput. (1999),
  265-268.
- [Ko97] Kostochka, A., A bound on the cardinality of families not containing
  $\Delta$-systems. (1997).
- [Ra20] Rao, A., Coding for sunflowers. Discrete Analysis (2020).

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/20.lean).

## Current assessment

The [[research/methods/finite_set_thresholds|spread-family obstruction]]
shows why a constant spread parameter cannot suffice in the same
random-subset hitting lemma: the family of all transversals of $n$ fixed
$s$-point classes is $s$-spread, but its hitting probability tends to zero
at fixed sampling density as $n$ grows. This is the product construction
in Bell–Chueluecha–Warnke's Lemma 4. The family has $s$ disjoint
transversals, so it does not obstruct the requested sunflower bound.
This checks one proposed implication and is not a wider standing survey.

The [[research/sunflower_exponential_bound/_index|spread-family research]]
gives author-recorded obstructions to constant-spread matching and
bounded-core replacements, alongside exponential bounds for affine word
families, recorded as Plasma AI's pending partial claim on
[[problems/set_systems/E0020/claims/2026_10_19_plasma_ai|its claim page]], and
for bounded-additive-growth subclasses. The missing step is a structural
restriction with controlled total loss for arbitrary families.
Its source test concerns particular intermediate assertions in the pending
preprint, and supplies no resolution of the full sunflower question.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_combinatorics/petridis_2012_new_proofs_plunnecke_type_estimates/_index|petridis_2012_new_proofs_plunnecke_type_estimates]]
- [[../library/set_systems/alon_2013_sunflowers_matrix_multiplication/_index|alon_2013_sunflowers_matrix_multiplication]]
- [[../library/set_systems/alon_2013_sunflowers_matrix_multiplication/theorem_2_3|alon_2013_sunflowers_matrix_multiplication / theorem_2_3]]
- [[../library/set_systems/alon_2013_sunflowers_matrix_multiplication/theorem_2_6|alon_2013_sunflowers_matrix_multiplication / theorem_2_6]]
- [[../library/set_systems/alweiss_2020_improved_bounds_sunflower_lemma/_index|alweiss_2020_improved_bounds_sunflower_lemma]]
- [[../library/set_systems/alweiss_2020_improved_bounds_sunflower_lemma/lemma_3_1|alweiss_2020_improved_bounds_sunflower_lemma / lemma_3_1]]
- [[../library/set_systems/alweiss_2020_improved_bounds_sunflower_lemma/theorem_1_4|alweiss_2020_improved_bounds_sunflower_lemma / theorem_1_4]]
- [[../library/set_systems/alweiss_2020_improved_bounds_sunflower_lemma/theorem_1_9|alweiss_2020_improved_bounds_sunflower_lemma / theorem_1_9]]
- [[../library/set_systems/alweiss_2020_improved_bounds_sunflower_lemma/theorem_2_5|alweiss_2020_improved_bounds_sunflower_lemma / theorem_2_5]]
- [[../library/set_systems/bell_2021_note_sunflowers/_index|bell_2021_note_sunflowers]]
- [[../library/set_systems/bell_2021_note_sunflowers/lemma_2|bell_2021_note_sunflowers / lemma_2]]
- [[../library/set_systems/bell_2021_note_sunflowers/lemma_4|bell_2021_note_sunflowers / lemma_4]]
- [[../library/set_systems/bell_2021_note_sunflowers/theorem_1|bell_2021_note_sunflowers / theorem_1]]
- [[../library/set_systems/bell_2021_note_sunflowers/theorem_3|bell_2021_note_sunflowers / theorem_3]]
- [[../library/set_systems/erdos_1960_intersection_theorems_systems_sets/_index|erdos_1960_intersection_theorems_systems_sets]]
- [[../library/set_systems/erdos_1960_intersection_theorems_systems_sets/conjecture_p86|erdos_1960_intersection_theorems_systems_sets / conjecture_p86]]
- [[../library/set_systems/erdos_1960_intersection_theorems_systems_sets/theorem_1|erdos_1960_intersection_theorems_systems_sets / theorem_1]]
- [[../library/set_systems/erdos_1960_intersection_theorems_systems_sets/theorem_2|erdos_1960_intersection_theorems_systems_sets / theorem_2]]
- [[../library/set_systems/erdos_1960_intersection_theorems_systems_sets/theorem_3|erdos_1960_intersection_theorems_systems_sets / theorem_3]]
- [[../library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/_index|erdos_1981_combinatorial_problems_which_i_would_most]]
- [[../library/set_systems/frankston_2019_thresholds_versus_fractional_expectation_thresholds/_index|frankston_2019_thresholds_versus_fractional_expectation_thresholds]]
- [[../library/set_systems/frankston_2019_thresholds_versus_fractional_expectation_thresholds/lemma_3_1|frankston_2019_thresholds_versus_fractional_expectation_thresholds / lemma_3_1]]
- [[../library/set_systems/frankston_2019_thresholds_versus_fractional_expectation_thresholds/theorem_1_1|frankston_2019_thresholds_versus_fractional_expectation_thresholds / theorem_1_1]]
- [[../library/set_systems/fukuyama_2022_sunflower_conjecture_proven/_index|fukuyama_2022_sunflower_conjecture_proven]]
- [[../library/set_systems/ge_2026_bounded_vc_dimension_implies_sunflower_conjecture/_index|ge_2026_bounded_vc_dimension_implies_sunflower_conjecture]]
- [[../library/set_systems/kostochka_1999_systems_small_sets_no_large_subsystems/_index|kostochka_1999_systems_small_sets_no_large_subsystems]]
- [[../library/set_systems/kostochka_1999_systems_small_sets_no_large_subsystems/theorem_1|kostochka_1999_systems_small_sets_no_large_subsystems / theorem_1]]
- [[../library/set_systems/kostochka_1999_systems_small_sets_no_large_subsystems/theorem_2|kostochka_1999_systems_small_sets_no_large_subsystems / theorem_2]]
- [[../library/set_systems/naslund_2017_upper_bounds_sunflower_free_sets/_index|naslund_2017_upper_bounds_sunflower_free_sets]]
- [[../library/set_systems/naslund_2017_upper_bounds_sunflower_free_sets/theorem_5|naslund_2017_upper_bounds_sunflower_free_sets / theorem_5]]
- [[../library/set_systems/rao_2020_coding_sunflowers/_index|rao_2020_coding_sunflowers]]
- [[../library/set_systems/rao_2020_coding_sunflowers/lemma_2|rao_2020_coding_sunflowers / lemma_2]]
- [[../library/set_systems/rao_2020_coding_sunflowers/lemma_4|rao_2020_coding_sunflowers / lemma_4]]
- [[../library/set_systems/rao_2020_coding_sunflowers/theorem_1|rao_2020_coding_sunflowers / theorem_1]]
- [[../library/set_systems/shangguan_2026_thresholds_spread_set_systems_bounded_vc_dimension/_index|shangguan_2026_thresholds_spread_set_systems_bounded_vc_dimension]]

<!-- END problem library links -->
