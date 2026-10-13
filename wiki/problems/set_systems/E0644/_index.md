---
name: problems/set_systems/E0644
title: Problem 644
desc: |
  Bounds the size of a set needed to meet every member of a family of
  $k$-element sets in which any $r$ members are all met by one pair. The
  question is whether this size is asymptotically a constant times $k$.
tags:
- Combinatorics
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-07T19:24:45Z
---

# Problem 644

[[problems/set_systems/_index|..]]

[[problems/set_systems/E0644/claims/_index|claims/]]: The 1 claim page of Problem 644, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $f(k,r)$ be minimal such that if $A_1,A_2,\ldots$ is a family
of sets, all of size $k$, such that for every collection of $r$ of the $A_is$
there is some pair $\{x,y\}$ which intersects all of the $A_j$, then there is
some set of size $f(k,r)$ which intersects all of the sets $A_i$. Is it true
that

$$
f(k,7)=(1+o(1))\frac{3}{4}k?
$$

Is it true that for any $r\geq 3$ there exists some constant $c_r$ such that

$$
f(k,r)=(1+o(1))c_rk?
$$

**Status.** Open.

**Source.** [erdosproblems.com/644](https://www.erdosproblems.com/644), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #644,
https://www.erdosproblems.com/644.

**References.**

- [EFKT92] Erdős, P. and Fon-Der-Flaass, D. and Kostochka, A. V. and Tuza, Zs.,
  Small transversals in uniform hypergraphs. Siberian Adv. Math. (1992), 82-88.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/644.lean).

## Current assessment

The status above is the site's label. One claim page,
[[problems/set_systems/E0644/claims/1992_01_01_erdos_fon_der_flaass_kostochka_tuza|the exact values of Erdős, Fon-Der-Flaass, Kostochka and Tuza]],
records the refereed values $f(k,3)=2k$, $f(k,4)=\lceil3k/2\rceil$,
$f(k,5)=\lceil5k/4\rceil$ and $f(k,6)=k$, an accepted partial claim that
answers the second question yes for $r=3,4,5,6$ and covers neither the
$r=7$ asymptotic nor the second question for $r\ge7$, so the derived standing
is open; the site's commentary prints the two middle values with floors,
which fail already for $k=3$.

For $r=7$ the bounds are those of Fon-Der-Flaass, Kostochka and Woodall,
*Transversals in uniform hypergraphs with property (7,2)*, Discrete Math. 207
(1999), 277--284, whose $f(k,7,2)$ is this page's $f(k,7)$ (the identification
is made on the
[[../library/set_systems/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2/_index|source card]]).
Their [[../library/set_systems/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2/theorem_1|Theorem 1]]
(p. 278) gives $f(4q,7)\ge3q+1$ for every $q\ge10$, and their
[[../library/set_systems/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2/theorem_2|Theorem 2]]
(p. 281) gives $f(k,7)\le\lceil7k/8\rceil$ for every $k\ge8$. Adding to each
set a new point of its own keeps the hypothesis and does not lower the least
size of a set meeting every member, so $f(k,7)$ is nondecreasing in $k$; hence
$3\lfloor k/4\rfloor+1\le f(k,7)\le\lceil7k/8\rceil$ for $k\ge40$, and
$f(k,7)\ge(3/4-o(1))k$. Whether $f(k,7)/k$ tends to $3/4$, the first
question, stays open, and so does the second question for every $r\ge7$.
For fixed $r\ge3$, Bucić, Korándi and Sudakov (arXiv:1902.05055) give
$f(k,r)\le2k$
([[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/observation_5_1|Observation 5.1]])
and, through a derivation on the result page of their
[[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/theorem_5_7|Theorem 5.7]],
$\liminf_{k\to\infty}f(k,r)/k\ge1/(\sqrt r-1)$, about $0.608$ for $r=7$;
neither shows that $f(k,r)/k$ converges. These bounds settle neither
question, so they have no claim pages. The project's notes on these sources
are in
[[research/erdos_644/_index|the Problem 644 research folder]].

The assessment covers the library sources linked here, whose proofs were read
for structure only; no wider literature search is recorded, and nothing here
is independently reviewed.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/ramsey_theory/erdos_1997_some_recent_problems_results_graph_theory/_index|erdos_1997_some_recent_problems_results_graph_theory]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/_index|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/corollary_2_9|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / corollary_2_9]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/lemma_5_10|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / lemma_5_10]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/lemma_5_8|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / lemma_5_8]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/observation_5_1|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / observation_5_1]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/proposition_5_6|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / proposition_5_6]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/proposition_a_1|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / proposition_a_1]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/theorem_1_7|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / theorem_1_7]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/theorem_5_2|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / theorem_5_2]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/theorem_5_3|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / theorem_5_3]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/theorem_5_7|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / theorem_5_7]]
- [[../library/set_systems/bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs/theorem_6_1|bucic_et_al_2019_covering_graphs_by_monochromatic_trees_helly_type_results_hypergraphs / theorem_6_1]]
- [[../library/set_systems/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2/_index|fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2]]
- [[../library/set_systems/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2/lemma_1|fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2 / lemma_1]]
- [[../library/set_systems/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2/theorem_1|fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2 / theorem_1]]
- [[../library/set_systems/fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2/theorem_2|fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2 / theorem_2]]
- [[../library/set_systems/tuza_1985_critical_hypergraphs_intersecting_set_pair_systems/_index|tuza_1985_critical_hypergraphs_intersecting_set_pair_systems]]
- [[../library/set_systems/tuza_1985_critical_hypergraphs_intersecting_set_pair_systems/lemma_4|tuza_1985_critical_hypergraphs_intersecting_set_pair_systems / lemma_4]]
- [[../library/set_systems/tuza_1985_critical_hypergraphs_intersecting_set_pair_systems/theorem_17|tuza_1985_critical_hypergraphs_intersecting_set_pair_systems / theorem_17]]
- [[../library/set_systems/tuza_1985_critical_hypergraphs_intersecting_set_pair_systems/theorem_20|tuza_1985_critical_hypergraphs_intersecting_set_pair_systems / theorem_20]]
- [[../library/set_systems/tuza_1985_critical_hypergraphs_intersecting_set_pair_systems/theorem_6|tuza_1985_critical_hypergraphs_intersecting_set_pair_systems / theorem_6]]

<!-- END problem library links -->
