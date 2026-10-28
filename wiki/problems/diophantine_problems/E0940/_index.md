---
name: problems/diophantine_problems/E0940
title: Problem 940
desc: |
  Asks, for $r\geq 3$, whether infinitely many integers are not a sum of at most
  $r$ numbers divisible by the $r$th power of each of their prime factors, and
  whether the integers that are such sums have density $0$.
tags:
- Number theory
- Powerful numbers
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-28T16:29:39Z
---

# Problem 940

[[problems/diophantine_problems/_index|..]]

[[problems/diophantine_problems/E0940/claims/_index|claims/]]: The 3 claim pages of Problem 940, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $r\geq 3$. A number $n$ is $r$-powerful if for every prime
$p$ which divides $n$ we have $p^r\mid n$.

Are there infinitely many integers which are not the sum of at most $r$ many
$r$-powerful numbers? Does the set of integers which are the sum of at most $r$
$r$-powerful numbers have density $0$?

**Status.** Open. The infinitude question is answered for $r=3$ and $r=4$ by
accepted partial claims, in both cases with positive lower density of the
complement; the higher exponents and the density-zero question remain open.
The erdosproblems.com label was OPEN, and the page was last edited on
2025-11-03. The erdosproblems.com remarks record that Baker and Brüdern
[BaBr94] first proved the density-zero statement at $r=2$. They also
record that at $r=3$ the statement is unknown even for sums of three cubes.
Finally, they record that Heath-Brown [He88] proves every large integer is a sum
of at most three $2$-powerful numbers
([[problems/diophantine_problems/E0941/_index|Problem 941]]). On 2026-10-06 the
erdosproblems.com proof-claims tab carried one partial claim, filed 2026-09-06.

**Source.** [erdosproblems.com/940](https://www.erdosproblems.com/940), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #940,
https://www.erdosproblems.com/940.

**References.**

- [BaBr94] Baker, R. C. and Brüdern, J., On sums of two squarefull numbers.
  Math. Proc. Cambridge Philos. Soc. 116 (1994), no. 1, 1-5.
- [Er76d] Erdős, P., Problems and results on number theoretic properties of
  consecutive integers and related questions. Proceedings of the Fifth Manitoba
  Conference on Numerical Mathematics (Univ. Manitoba, Winnipeg, Man., 1975)
  (1976), 25-44.
- [He88] Heath-Brown, D. R., Ternary quadratic forms and sums of three
  square-full numbers. Séminaire de Théorie des Nombres, Paris 1986–87, Progr.
  Math. 75, Birkhäuser Boston (1988), 137-163.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/940.lean).
The Lean development
[plasma-ai/erdos-940](https://github.com/plasma-ai/erdos-940)
proves the complement statements for $r=3$ and $r=4$, the formal basis of
[[problems/diophantine_problems/E0940/claims/2026_07_26_beyer_de_ryke|Beyer de Ryke's claim]]
and the
[[problems/diophantine_problems/E0940/claims/2026_10_28_plasma_ai|quartic claim]].

## Current assessment

The positive integers not expressible as sums of at most $r$ $r$-powerful
numbers have positive lower natural density for $r=3$ and $r=4$. The cubic
result is Beyer de Ryke's
[[problems/diophantine_problems/E0940/claims/2026_07_26_beyer_de_ryke|accepted partial claim]];
the quartic result is
[[problems/diophantine_problems/E0940/claims/2026_10_28_plasma_ai|Plasma AI's accepted partial claim]].
Both acceptances rest on the
[[../library/diophantine_problems/plasma_ai_2026_powerful_sum_complements/_index|separate Lean formalization]],
with a pinned build, Comparator, kernel replay and independently graded
statement review. No numerical tier is assigned.

The stronger progression theorem in
[[../library/diophantine_problems/beyer_de_ryke_2026_density_deficit_cube_full_sums/_index|Beyer de Ryke's manuscript]]
and the stronger statement in the
[[research/erdos_940/quartic_complement|quartic prose argument]]
remain outside those formal acceptance records. The prose proofs are not
independently reviewed. Positive lower density of the complement does not
imply that the representable set has density zero. That second question
remains open for every $r\ge3$, and no infinitude conclusion for $r\ge5$
is recorded here.

On the density question, Wang's Theorem 1.3 (arXiv:2108.03398, first posted
7 August 2021) shows, assuming three unproved conjectures on Hasse--Weil
$L$-functions (automorphy and a zero-free half-plane, a Ratios-type
second-moment bound, and a square-free sieve), that the sums of three
nonnegative cubes have positive lower density. Thus at $r=3$ the sums of at
most three $3$-powerful numbers would not have density zero; this is recorded
as a
[[problems/diophantine_problems/E0940/claims/2021_08_07_wang|conditional claim]]
and settles nothing unconditionally.

The erdosproblems.com proof-claims tab, read on 2026-10-06, carried Beyer de
Ryke's partial claim submitted on 2026-09-06, with no comments. That source
snapshot is separate from the corpus's formalization-based acceptance. Beyond
the erdosproblems.com record (accessed 2026-09-04), the erdosproblems.com
proof-claims tab (accessed 2026-10-06) and the sources cited, no status search
is recorded on this page.

## Known Results

- For $r=3$, the complement of sums of at most three cube-full numbers has
  positive lower natural density: Beyer de Ryke's
  [[problems/diophantine_problems/E0940/claims/2026_07_26_beyer_de_ryke|accepted partial claim]],
  supported here by the separate Lean formalization.
- For $r=4$, the complement of sums of at most four $4$-powerful numbers has
  positive lower natural density:
  [[problems/diophantine_problems/E0940/claims/2026_10_28_plasma_ai|Plasma AI's accepted partial claim]],
  supported by the same formalization project.
- For $r=3$, conditionally on three unproved $L$-function conjectures, the
  sums of at most three $3$-powerful numbers have positive lower density:
  Wang's
  [[problems/diophantine_problems/E0940/claims/2021_08_07_wang|conditional claim]].

## Research

The [[research/erdos_940/_index|research folder for Problem 940]] holds
reading notes and the repository's work on both questions, including the
quartic prose argument and the open density and higher-exponent cases.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/diophantine_problems/beyer_de_ryke_2026_density_deficit_cube_full_sums/_index|beyer_de_ryke_2026_density_deficit_cube_full_sums]]
- [[../library/diophantine_problems/browning_heath_brown_2018_counting_rational_points_quadric_surfaces/_index|browning_heath_brown_2018_counting_rational_points_quadric_surfaces]]
- [[../library/diophantine_problems/browning_munshi_wang_2026_beyond_square_root_barrier_cubic_forms_perazzo_type/_index|browning_munshi_wang_2026_beyond_square_root_barrier_cubic_forms_perazzo_type]]
- [[../library/diophantine_problems/browning_verzobio_2026_sums_three_powerful_numbers/_index|browning_verzobio_2026_sums_three_powerful_numbers]]
- [[../library/diophantine_problems/ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms/_index|ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms]]
- [[../library/diophantine_problems/ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms/lemma_5_4|ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms / lemma_5_4]]
- [[../library/diophantine_problems/ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms/proposition_5_2|ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms / proposition_5_2]]
- [[../library/diophantine_problems/ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms/proposition_8_5|ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms / proposition_8_5]]
- [[../library/diophantine_problems/ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms/theorem_1_1|ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms / theorem_1_1]]
- [[../library/diophantine_problems/ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms/theorem_1_2|ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms / theorem_1_2]]
- [[../library/diophantine_problems/ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms/theorem_6_2|ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms / theorem_6_2]]
- [[../library/diophantine_problems/ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms/theorem_8_8|ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms / theorem_8_8]]
- [[../library/diophantine_problems/heath_brown_1997_density_rational_points_cubic_surfaces/_index|heath_brown_1997_density_rational_points_cubic_surfaces]]
- [[../library/diophantine_problems/heath_brown_1997_density_rational_points_cubic_surfaces/corollary_p3|heath_brown_1997_density_rational_points_cubic_surfaces / corollary_p3]]
- [[../library/diophantine_problems/heath_brown_1997_density_rational_points_cubic_surfaces/theorem_1|heath_brown_1997_density_rational_points_cubic_surfaces / theorem_1]]
- [[../library/diophantine_problems/plasma_ai_2026_powerful_sum_complements/_index|plasma_ai_2026_powerful_sum_complements]]
- [[../library/diophantine_problems/plasma_ai_2026_powerful_sum_complements/complement_density|plasma_ai_2026_powerful_sum_complements / complement_density]]
- [[../library/diophantine_problems/salberger_2023_counting_rational_points_projective_varieties/_index|salberger_2023_counting_rational_points_projective_varieties]]
- [[../library/diophantine_problems/salberger_2023_counting_rational_points_projective_varieties/corollary_0_7|salberger_2023_counting_rational_points_projective_varieties / corollary_0_7]]
- [[../library/diophantine_problems/salberger_2023_counting_rational_points_projective_varieties/corollary_6_5|salberger_2023_counting_rational_points_projective_varieties / corollary_6_5]]
- [[../library/diophantine_problems/salberger_2023_counting_rational_points_projective_varieties/theorem_0_4|salberger_2023_counting_rational_points_projective_varieties / theorem_0_4]]
- [[../library/diophantine_problems/salberger_2023_counting_rational_points_projective_varieties/theorem_1_2|salberger_2023_counting_rational_points_projective_varieties / theorem_1_2]]
- [[../library/diophantine_problems/wang_2021_sums_cubes_ratios_conjectures/_index|wang_2021_sums_cubes_ratios_conjectures]]
- [[../library/diophantine_problems/wang_2021_sums_cubes_ratios_conjectures/corollary_1_7|wang_2021_sums_cubes_ratios_conjectures / corollary_1_7]]
- [[../library/diophantine_problems/wang_2021_sums_cubes_ratios_conjectures/theorem_1_3|wang_2021_sums_cubes_ratios_conjectures / theorem_1_3]]
- [[../library/diophantine_problems/wang_2021_sums_cubes_ratios_conjectures/theorem_1_6|wang_2021_sums_cubes_ratios_conjectures / theorem_1_6]]
- [[../library/diophantine_problems/wang_2021_sums_cubes_ratios_conjectures/theorem_1_9|wang_2021_sums_cubes_ratios_conjectures / theorem_1_9]]
- [[../library/number_theory/colliot_thelene_skorobogatov_2021_brauer_groups_schemes/_index|colliot_thelene_skorobogatov_2021_brauer_groups_schemes]]
- [[../library/number_theory/colliot_thelene_skorobogatov_2021_brauer_groups_schemes/theorem_3_5_4|colliot_thelene_skorobogatov_2021_brauer_groups_schemes / theorem_3_5_4]]
- [[../library/number_theory/colliot_thelene_skorobogatov_2021_brauer_groups_schemes/theorem_3_7_1|colliot_thelene_skorobogatov_2021_brauer_groups_schemes / theorem_3_7_1]]
- [[../library/number_theory/colliot_thelene_skorobogatov_2021_comparing_two_brauer_groups_ii/_index|colliot_thelene_skorobogatov_2021_comparing_two_brauer_groups_ii]]
- [[../library/number_theory/colliot_thelene_skorobogatov_2021_comparing_two_brauer_groups_ii/corollary_4_4_5|colliot_thelene_skorobogatov_2021_comparing_two_brauer_groups_ii / corollary_4_4_5]]
- [[../library/number_theory/colliot_thelene_skorobogatov_2021_comparing_two_brauer_groups_ii/theorem_4_3_10|colliot_thelene_skorobogatov_2021_comparing_two_brauer_groups_ii / theorem_4_3_10]]
- [[../library/number_theory/elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms/_index|elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms]]
- [[../library/number_theory/elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms/corollary_18_5|elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms / corollary_18_5]]
- [[../library/number_theory/elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms/theorem_17_12|elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms / theorem_17_12]]
- [[../library/number_theory/elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms/theorem_17_14|elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms / theorem_17_14]]
- [[../library/number_theory/elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms/theorem_17_3|elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms / theorem_17_3]]
- [[../library/number_theory/elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms/theorem_18_10|elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms / theorem_18_10]]
- [[../library/number_theory/elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms/theorem_18_3|elman_karpenko_merkurjev_2008_algebraic_geometric_theory_quadratic_forms / theorem_18_3]]
- [[../library/number_theory/voight_2021_quaternion_algebras_over_global_fields/_index|voight_2021_quaternion_algebras_over_global_fields]]
- [[../library/number_theory/voight_2021_quaternion_algebras_over_global_fields/corollary_14_2_3|voight_2021_quaternion_algebras_over_global_fields / corollary_14_2_3]]
- [[../library/number_theory/voight_2021_quaternion_algebras_over_global_fields/corollary_14_6_2|voight_2021_quaternion_algebras_over_global_fields / corollary_14_6_2]]
- [[../library/number_theory/voight_2021_quaternion_algebras_over_global_fields/main_theorem_14_1_3|voight_2021_quaternion_algebras_over_global_fields / main_theorem_14_1_3]]
- [[../library/number_theory/voight_2021_quaternion_algebras_over_global_fields/main_theorem_14_7_4|voight_2021_quaternion_algebras_over_global_fields / main_theorem_14_7_4]]
- [[../library/number_theory/voight_2021_quaternion_algebras_over_global_fields/proposition_14_2_1|voight_2021_quaternion_algebras_over_global_fields / proposition_14_2_1]]
- [[../library/number_theory/voight_2021_quaternion_algebras_over_global_fields/theorem_14_3_3|voight_2021_quaternion_algebras_over_global_fields / theorem_14_3_3]]
- [[../library/number_theory/voight_2021_quaternion_algebras_over_global_fields/theorem_14_3_8|voight_2021_quaternion_algebras_over_global_fields / theorem_14_3_8]]
- [[../library/number_theory/voight_2021_quaternion_algebras_over_global_fields/theorem_14_6_9|voight_2021_quaternion_algebras_over_global_fields / theorem_14_6_9]]

<!-- END problem library links -->
