---
name: problems/extremal_graph_theory/E0993
title: Problem 993
desc: |
  Asks whether the sequence counting the independent sets of each size in a tree
  or forest is unimodal.
tags:
- Graph theory
status: solved
claim: proved
created: 2026-09-04T09:17:27Z
updated: 2026-10-08T17:47:46Z
---

# Problem 993

[[problems/extremal_graph_theory/_index|..]]

[[problems/extremal_graph_theory/E0993/claims/_index|claims/]]: The 2 claim pages of Problem 993, one per claimant's result; the problem's standing derives from them.

***

**Statement.** The independent set sequence of any tree or forest is unimodal.

In other words, if $i_k(G)$ counts the number of independent sets of vertices of
size $k$ in a graph $G$, and $T$ is any tree or forest, then for some $m\geq 0$

$$
i_{0}(T)\leq i_{1}(T)\leq\cdots\leq i_{m}(T)\geq i_{m+1}(T)\geq
i_{m+2}(T)\geq\cdots.
$$

**Status.** Solved in the affirmative, on the accepted
[[problems/extremal_graph_theory/E0993/claims/2026_09_27_zhang_li|Li–Vallier–Zhang claim]]:
the independence sequence of every finite forest is unimodal. Acceptance rests
on the public Palomar formalization of their second proof, local
inspection of its statement and verification records, a successful local
build and comparator replay, and the project
reviewer's sign-off recorded on the claim page. Bloom's catalog labeled the
problem FALSIFIABLE on 6 October 2026; that label described finite
checkability of a counterexample and supplied no verdict on the later
formalization. Fang, Lu, Nevo, Yao and Zheng's
[[problems/extremal_graph_theory/E0993/claims/2026_09_17_fang_lu_nevo_yao_zheng|partial claim]]
concerns all forests above an unspecified absolute threshold and remains
recorded separately.

**Source.** [erdosproblems.com/993](https://www.erdosproblems.com/993), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #993,
https://www.erdosproblems.com/993.

**References.**

- [AMSE87] Alavi, Yousef and Malde, Paresh J. and Schwenk, Allen J. and Erdős,
  Paul, The vertex independence sequence of a graph is not constrained. Congr.
  Numer. (1987), 15-23.
- [Sc81] Schwenk, Allen J., On unimodal sequences of graphical invariants. J.
  Combin. Theory Ser. B (1981), 247-250.

**Formalization.** The current public formalization of the Li–Vallier–Zhang claim
follows version 2.15 of their second proof and supersedes the
version accompanying arXiv:2610.07943v1. Palomar's mechanical report records
acceptance of `Erdos993.erdos_993_forest` and its tree specialization by Lean's
default kernel, nanoda and con-ron, with only `propext`, `Classical.choice`
and `Quot.sound`. Plasma AI's source inspection found no statement mismatch
and matched the challenge, solution and comparator to the exact files checked
by Palomar; the scope and public records are on the
[[problems/extremal_graph_theory/E0993/claims/2026_09_27_zhang_li|claim page]].
A local build and comparator replay of that source also passed all three
kernels on 2026-10-16 UTC, with the execution details on the claim page.
The restricted manuscript is unnecessary for checking the public Lean theorem.

## Current assessment

The full forest statement is accepted on the public formalization registered
as PALOMAR-2026-10-11-000012. Plasma AI inspected the definitions and theorem
statements, found no mismatch with Problem 993, and confirmed that the
challenge, solution and comparator were the exact files in Palomar's
successful verification. Jacob Parish at Plasma AI signed off on acceptance
on 2026-10-16 UTC; the
[[problems/extremal_graph_theory/E0993/claims/2026_09_27_zhang_li|claim page]]
records the scope, source revision and verification report.

The acceptance is supported by Palomar's kernel verification and a successful
local build and comparator replay. The restricted manuscript is unreviewed, and
the local statement inspection has not been independently graded. No native
claim tier or manuscript proof-coverage verdict is asserted. The partial
[[problems/extremal_graph_theory/E0993/claims/2026_09_17_fang_lu_nevo_yao_zheng|Fang–Lu–Nevo–Yao–Zheng claim]]
addresses sufficiently large forests and does not by itself cover every size.
The earlier literature linked below is not compiled into a full proof here;
the compiled Alavi–Malde–Schwenk–Erdős result concerns arbitrary graphs and
gives no tree or forest counterexample.

## Known Results

[[../library/extremal_graph_theory/alavi_1987_vertex_independence_sequence_graph_is_not/_index|Alavi, Malde, Schwenk and Erdős]]
prove that arbitrary graphs can realize every strict ordering of their
independent-set counts (1987, printed p. 16). This does not provide a tree or
forest counterexample. Their Problem 3 on p. 21 poses that restricted question
separately.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/extremal_graph_theory/alavi_1987_vertex_independence_sequence_graph_is_not/_index|alavi_1987_vertex_independence_sequence_graph_is_not]]
- [[../library/extremal_graph_theory/alavi_1987_vertex_independence_sequence_graph_is_not/example_p21|alavi_1987_vertex_independence_sequence_graph_is_not / example_p21]]
- [[../library/extremal_graph_theory/alavi_1987_vertex_independence_sequence_graph_is_not/problem_3|alavi_1987_vertex_independence_sequence_graph_is_not / problem_3]]
- [[../library/extremal_graph_theory/alavi_1987_vertex_independence_sequence_graph_is_not/theorem_p16|alavi_1987_vertex_independence_sequence_graph_is_not / theorem_p16]]
- [[../library/extremal_graph_theory/basit_galvin_2020_independent_set_sequence_tree/_index|basit_galvin_2020_independent_set_sequence_tree]]
- [[../library/extremal_graph_theory/basit_galvin_2020_independent_set_sequence_tree/claim_1_10|basit_galvin_2020_independent_set_sequence_tree / claim_1_10]]
- [[../library/extremal_graph_theory/basit_galvin_2020_independent_set_sequence_tree/theorem_1_3|basit_galvin_2020_independent_set_sequence_tree / theorem_1_3]]
- [[../library/extremal_graph_theory/basit_galvin_2020_independent_set_sequence_tree/theorem_1_4|basit_galvin_2020_independent_set_sequence_tree / theorem_1_4]]
- [[../library/extremal_graph_theory/basit_galvin_2020_independent_set_sequence_tree/theorem_1_5|basit_galvin_2020_independent_set_sequence_tree / theorem_1_5]]
- [[../library/extremal_graph_theory/basit_galvin_2020_independent_set_sequence_tree/theorem_1_6|basit_galvin_2020_independent_set_sequence_tree / theorem_1_6]]
- [[../library/extremal_graph_theory/basit_galvin_2020_independent_set_sequence_tree/theorem_1_7|basit_galvin_2020_independent_set_sequence_tree / theorem_1_7]]
- [[../library/extremal_graph_theory/bencs_2017_trees_real_rooted_independence_polynomial/_index|bencs_2017_trees_real_rooted_independence_polynomial]]
- [[../library/extremal_graph_theory/bencs_2017_trees_real_rooted_independence_polynomial/corollary_3_1|bencs_2017_trees_real_rooted_independence_polynomial / corollary_3_1]]
- [[../library/extremal_graph_theory/bencs_2017_trees_real_rooted_independence_polynomial/proposition_2_7|bencs_2017_trees_real_rooted_independence_polynomial / proposition_2_7]]
- [[../library/extremal_graph_theory/bencs_2017_trees_real_rooted_independence_polynomial/proposition_3_3|bencs_2017_trees_real_rooted_independence_polynomial / proposition_3_3]]
- [[../library/extremal_graph_theory/bencs_2017_trees_real_rooted_independence_polynomial/proposition_3_4|bencs_2017_trees_real_rooted_independence_polynomial / proposition_3_4]]
- [[../library/extremal_graph_theory/bencs_2017_trees_real_rooted_independence_polynomial/proposition_3_5|bencs_2017_trees_real_rooted_independence_polynomial / proposition_3_5]]
- [[../library/extremal_graph_theory/bencs_2017_trees_real_rooted_independence_polynomial/theorem_2_3|bencs_2017_trees_real_rooted_independence_polynomial / theorem_2_3]]
- [[../library/extremal_graph_theory/galvin_2025_trees_non_log_concave_independent_set_sequences/_index|galvin_2025_trees_non_log_concave_independent_set_sequences]]
- [[../library/extremal_graph_theory/heilman_2020_independent_sets_random_trees_sparse_random_graphs/_index|heilman_2020_independent_sets_random_trees_sparse_random_graphs]]
- [[../library/extremal_graph_theory/heilman_2020_independent_sets_random_trees_sparse_random_graphs/lemma_5_1|heilman_2020_independent_sets_random_trees_sparse_random_graphs / lemma_5_1]]
- [[../library/extremal_graph_theory/heilman_2020_independent_sets_random_trees_sparse_random_graphs/theorem_1_17|heilman_2020_independent_sets_random_trees_sparse_random_graphs / theorem_1_17]]
- [[../library/extremal_graph_theory/heilman_2020_independent_sets_random_trees_sparse_random_graphs/theorem_1_18|heilman_2020_independent_sets_random_trees_sparse_random_graphs / theorem_1_18]]
- [[../library/extremal_graph_theory/heilman_2020_independent_sets_random_trees_sparse_random_graphs/theorem_1_19|heilman_2020_independent_sets_random_trees_sparse_random_graphs / theorem_1_19]]
- [[../library/extremal_graph_theory/heilman_2020_independent_sets_random_trees_sparse_random_graphs/theorem_1_20|heilman_2020_independent_sets_random_trees_sparse_random_graphs / theorem_1_20]]
- [[../library/extremal_graph_theory/kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26/_index|kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26]]
- [[../library/extremal_graph_theory/kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26/examples_p4|kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26 / examples_p4]]
- [[../library/extremal_graph_theory/kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26/lemma_4_2|kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26 / lemma_4_2]]
- [[../library/extremal_graph_theory/kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26/lemma_4_3|kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26 / lemma_4_3]]
- [[../library/extremal_graph_theory/kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26/lemma_4_4|kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26 / lemma_4_4]]
- [[../library/extremal_graph_theory/kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26/theorem_3_2|kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26 / theorem_3_2]]
- [[../library/extremal_graph_theory/kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26/theorem_3_3|kadrawi_levit_2023_independence_polynomial_trees_is_not_always_log_concave_starting_from_order_26 / theorem_3_3]]
- [[../library/extremal_graph_theory/levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees/_index|levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees]]
- [[../library/extremal_graph_theory/levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees/conjecture_1_2|levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees / conjecture_1_2]]
- [[../library/extremal_graph_theory/levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees/lemma_2_1|levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees / lemma_2_1]]
- [[../library/extremal_graph_theory/levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees/lemma_2_5|levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees / lemma_2_5]]
- [[../library/extremal_graph_theory/levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees/proposition_4_4|levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees / proposition_4_4]]
- [[../library/extremal_graph_theory/levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees/theorem_3_1|levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees / theorem_3_1]]
- [[../library/extremal_graph_theory/levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees/theorem_4_2|levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees / theorem_4_2]]
- [[../library/extremal_graph_theory/levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees/theorem_4_5|levit_mandrescu_2002_unimodality_independence_polynomials_some_well_covered_trees / theorem_4_5]]
- [[../library/extremal_graph_theory/levit_mandrescu_2004_very_well_covered_graphs_unimodality_conjecture/_index|levit_mandrescu_2004_very_well_covered_graphs_unimodality_conjecture]]
- [[../library/extremal_graph_theory/levit_mandrescu_2004_very_well_covered_graphs_unimodality_conjecture/corollary_2_7|levit_mandrescu_2004_very_well_covered_graphs_unimodality_conjecture / corollary_2_7]]
- [[../library/extremal_graph_theory/levit_mandrescu_2004_very_well_covered_graphs_unimodality_conjecture/corollary_2_8|levit_mandrescu_2004_very_well_covered_graphs_unimodality_conjecture / corollary_2_8]]
- [[../library/extremal_graph_theory/levit_mandrescu_2004_very_well_covered_graphs_unimodality_conjecture/theorem_2_5|levit_mandrescu_2004_very_well_covered_graphs_unimodality_conjecture / theorem_2_5]]
- [[../library/extremal_graph_theory/li_2026_unimodality_independence_polynomials_two_family_trees/_index|li_2026_unimodality_independence_polynomials_two_family_trees]]
- [[../library/extremal_graph_theory/li_2026_unimodality_independence_polynomials_two_family_trees/theorem_1_4|li_2026_unimodality_independence_polynomials_two_family_trees / theorem_1_4]]
- [[../library/extremal_graph_theory/li_2026_unimodality_independence_polynomials_two_family_trees/theorem_1_5|li_2026_unimodality_independence_polynomials_two_family_trees / theorem_1_5]]
- [[../library/extremal_graph_theory/ramos_sun_2025_ai_enhanced_approach_tree_unimodality_conjecture/_index|ramos_sun_2025_ai_enhanced_approach_tree_unimodality_conjecture]]
- [[../library/extremal_graph_theory/ramos_sun_2025_ai_enhanced_approach_tree_unimodality_conjecture/conjecture_2_2|ramos_sun_2025_ai_enhanced_approach_tree_unimodality_conjecture / conjecture_2_2]]
- [[../library/extremal_graph_theory/ramos_sun_2025_ai_enhanced_approach_tree_unimodality_conjecture/conjecture_4_2|ramos_sun_2025_ai_enhanced_approach_tree_unimodality_conjecture / conjecture_4_2]]
- [[../library/extremal_graph_theory/ramos_sun_2025_ai_enhanced_approach_tree_unimodality_conjecture/main_result|ramos_sun_2025_ai_enhanced_approach_tree_unimodality_conjecture / main_result]]
- [[../library/extremal_graph_theory/wang_zhu_2010_unimodality_independence_polynomials_some_graphs/_index|wang_zhu_2010_unimodality_independence_polynomials_some_graphs]]
- [[../library/extremal_graph_theory/wang_zhu_2010_unimodality_independence_polynomials_some_graphs/proposition_3_1|wang_zhu_2010_unimodality_independence_polynomials_some_graphs / proposition_3_1]]
- [[../library/extremal_graph_theory/wang_zhu_2010_unimodality_independence_polynomials_some_graphs/proposition_3_2|wang_zhu_2010_unimodality_independence_polynomials_some_graphs / proposition_3_2]]
- [[../library/extremal_graph_theory/wang_zhu_2010_unimodality_independence_polynomials_some_graphs/theorem_3_1|wang_zhu_2010_unimodality_independence_polynomials_some_graphs / theorem_3_1]]
- [[../library/extremal_graph_theory/yosef_et_al_2021_unimodality_independence_polynomials_trees/_index|yosef_et_al_2021_unimodality_independence_polynomials_trees]]
- [[../library/extremal_graph_theory/yosef_et_al_2021_unimodality_independence_polynomials_trees/theorem_5_3|yosef_et_al_2021_unimodality_independence_polynomials_trees / theorem_5_3]]
- [[../library/extremal_graph_theory/yosef_et_al_2021_unimodality_independence_polynomials_trees/verification_p15|yosef_et_al_2021_unimodality_independence_polynomials_trees / verification_p15]]

<!-- END problem library links -->
