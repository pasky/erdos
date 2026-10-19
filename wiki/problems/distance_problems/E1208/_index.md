---
name: problems/distance_problems/E1208
title: Problem 1208
desc: |
  Asks for an estimate of $F_d(n)$, the largest number of points with all
  distances distinct that every set of $n$ points in $\mathbb{R}^d$ must
  contain, for fixed $d\ge2$ as $n\to\infty$.
tags:
- Geometry
- Distances
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-15T01:58:15Z
---

# Problem 1208

[[problems/distance_problems/_index|..]]

[[problems/distance_problems/E1208/claims/_index|claims/]]: The 2 claim pages of Problem 1208, one per claimant's result; the problem's standing derives from them.

***

**Statement.** For $d\geq 2$ let $F_d(n)$ be minimal such that every set of $n$
points in $\mathbb{R}^d$ contains a set of $F_d(n)$ points with distinct
distances. Estimate $F_d(n)$ for fixed $d$ as $n\to \infty$.

**Status.** Open. The erdosproblems.com label was OPEN. Its remarks (page last
edited 7 September 2026) credit [LPZ26] with the upper bound
$F_2(n)\ll n^{1/2-c}$ for some $c>0$, which leaves the estimate open.

**Source.** [erdosproblems.com/1208](https://www.erdosproblems.com/1208),
accessed 2026-09-04 and 2026-10-13. Cite as: T. F. Bloom, Erdős Problem #1208,
https://www.erdosproblems.com/1208.

**References.**

- [CFGHUZ15] Conlon, David and Fox, Jacob and Gasarch, William and Harris, David
  G. and Ulrich, Douglas and Zbarsky, Samuel, Distinct volume subsets. SIAM J.
  Discrete Math. 29 (2015), 472-480.
- [Ch13] Charalambides, Marcos, A note on distinct distance subsets. J. Geom.
  (2013), 439-442.
- [ErGu70] Erdős, P. and Guy, R. K., Distinct distances between lattice points.
  Elem. Math. (1970), 121-123.
- [KSS75] Komlós, J. and Sulyok, M. and Szemeredi, E., Linear problems in
  combinatorial number theory. Acta Math. Acad. Sci. Hungar. (1975), 113-121.
- [LeTh95] Lefmann, Hanno and Thiele, Torsten, Point sets with distinct
  distances. Combinatorica (1995), 379-408.
- [LPZ26] S. Lee, C. Pohoata, and D. G. Zhu, The Minkowski grid has robustly
  many repeated distances. arXiv:2607.05374 (2026).
- [Th95] T. Thiele, Geometric selection problems and hypergraphs. PhD thesis,
  Freir Universitat Berlin (1995).

**Formalization.** None recorded.

## Current assessment

The erdosproblems.com formulation asks for the order of $F_d(n)$, the size of a
subset with all distances distinct that every set of $n$ points in
$\mathbb{R}^d$ is guaranteed to contain, for fixed $d\ge2$ as $n\to\infty$. The
erdosproblems.com label was OPEN, and the derived standing is open: two pending
partial claims lower the planar upper bound, and no result determines the order
of $F_d(n)$ for any $d\ge2$.

**The plane.** Before 2026 the bounds were
$n^{1/3}/(\log n)^{1/3}\ll F_2(n)\ll n^{1/2}/(\log n)^{1/4}$. The upper bound
is the square grid
([[../library/distance_problems/charalambides_2013_note_distinct_distance_subsets/proposition_1_2|[Ch13], Proposition 1.2]]).
The lower bound is credited to Charalambides
([[../library/distance_problems/charalambides_2013_note_distinct_distance_subsets/proposition_2_1|[Ch13], Proposition 2.1]],
which prints $N^{1/3}/\log N$; [CFGHUZ15] say that a careful reading of its
proof gives the erdosproblems.com form). Croot, Mao, Pohoata, Sheffer and Yip's
bound for distinct-distance subsets of the grid
([[../library/additive_bases/croot_2026_combinatorial_large_sieve_sidon_sets_distances/theorem_1_3|their Theorem 1.3]],
a preprint) gives $F_2(n)\ll n^{1/2}\exp(-c\log n/\log\log n)$. Two pending
partial claims lower the exponent below $1/2$. Sungchul Lee's manuscript of 14
June 2026
([[problems/distance_problems/E1208/claims/2026_06_14_lee|claim page]]) and
the joint preprint [LPZ26] of 6 July 2026
([[problems/distance_problems/E1208/claims/2026_07_06_lee_pohoata_zhu|claim page]])
each give $F_2(n)\ll n^{1/2-\delta}$ for an absolute $\delta>0$, by closely
related number-field constructions; the erdosproblems.com remarks credit
[LPZ26], which says that Lee's manuscript came first. Neither is refereed or
formalized, and their proofs were not checked here. A thread comment of 13 June
2026 reports that Clemen, Führer and Roche-Newton (arXiv:2606.05841) prove
$F_2(n)\gg n^{1/3}$; that preprint was not read here. So the exponent of
$F_2(n)$ lies between $1/3$ and $1/2$, and below $1/2$ if the pending claims
stand.

**Higher dimensions.** For $d\ge3$ the erdosproblems.com remarks record Thiele's
$F_d(n)\gg n^{1/(3d-2)}$ [Th95], improved by [CFGHUZ15] to
$F_d(n)\gg_d n^{1/(3d-3)}(\log n)^{1/3-2/(3d-3)}$
([[../library/distance_problems/conlon_2015_distinct_volume_subsets/proposition_1_1|their Proposition 1.1]]),
and $F_d(n)\ll n^{1/d}$ from the integer grid. These do not meet. The case
$d=1$ is [[problems/additive_bases/E0530/_index|Problem 530]], where
Komlós, Sulyok and Szemerédi [KSS75] proved $F_1(n)\asymp n^{1/2}$, and the
behavior for fixed $n$ as $d\to\infty$ is
[[problems/discrete_geometry/E1088/_index|Problem 1088]].

Search scope: the erdosproblems.com problem page and discussion thread, the
arXiv record and text of [LPZ26], Lee's repository, the community database
entry, and the library cards linked below. No wider literature search was made,
and nothing here is independently reviewed.

## Route analysis

The [[research/geometric_configuration_interfaces/distance_subsets|repeated
distances and geometric sidon subsets]] account records the following scope.
Optimizing the inspected deletion inequality qN-aq^3N^(7/3)-bq^4N^3 log N with
q=epsilon N^(-2/3)(log N)^(-1/3) gives Omega(N^(1/3)/(log N)^(1/3)).

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/additive_bases/croot_2026_combinatorial_large_sieve_sidon_sets_distances/_index|croot_2026_combinatorial_large_sieve_sidon_sets_distances]]
- [[../library/additive_bases/croot_2026_combinatorial_large_sieve_sidon_sets_distances/theorem_1_3|croot_2026_combinatorial_large_sieve_sidon_sets_distances / theorem_1_3]]
- [[../library/additive_bases/croot_2026_combinatorial_large_sieve_sidon_sets_distances/theorem_1_5|croot_2026_combinatorial_large_sieve_sidon_sets_distances / theorem_1_5]]
- [[../library/distance_problems/charalambides_2013_note_distinct_distance_subsets/_index|charalambides_2013_note_distinct_distance_subsets]]
- [[../library/distance_problems/charalambides_2013_note_distinct_distance_subsets/conjecture_2_3|charalambides_2013_note_distinct_distance_subsets / conjecture_2_3]]
- [[../library/distance_problems/charalambides_2013_note_distinct_distance_subsets/proposition_1_2|charalambides_2013_note_distinct_distance_subsets / proposition_1_2]]
- [[../library/distance_problems/charalambides_2013_note_distinct_distance_subsets/proposition_2_1|charalambides_2013_note_distinct_distance_subsets / proposition_2_1]]
- [[../library/distance_problems/charalambides_2013_note_distinct_distance_subsets/proposition_3_1|charalambides_2013_note_distinct_distance_subsets / proposition_3_1]]
- [[../library/distance_problems/conlon_2015_distinct_volume_subsets/_index|conlon_2015_distinct_volume_subsets]]
- [[../library/distance_problems/conlon_2015_distinct_volume_subsets/proposition_1_1|conlon_2015_distinct_volume_subsets / proposition_1_1]]
- [[../library/distance_problems/conlon_2015_distinct_volume_subsets/theorem_1_2|conlon_2015_distinct_volume_subsets / theorem_1_2]]
- [[../library/distance_problems/dumitrescu_2008_distinct_distances_points_general_position/_index|dumitrescu_2008_distinct_distances_points_general_position]]
- [[../library/distance_problems/dumitrescu_2008_distinct_distances_points_general_position/theorem_3|dumitrescu_2008_distinct_distances_points_general_position / theorem_3]]
- [[../library/distance_problems/erdos_1970_distinct_distances_between_lattice_points/_index|erdos_1970_distinct_distances_between_lattice_points]]
- [[../library/distance_problems/erdos_1970_distinct_distances_between_lattice_points/inequality_1|erdos_1970_distinct_distances_between_lattice_points / inequality_1]]
- [[../library/distance_problems/erdos_1970_distinct_distances_between_lattice_points/inequality_2|erdos_1970_distinct_distances_between_lattice_points / inequality_2]]
- [[../library/distance_problems/erdos_1970_distinct_distances_between_lattice_points/inequality_4|erdos_1970_distinct_distances_between_lattice_points / inequality_4]]
- [[../library/distance_problems/erdos_1970_distinct_distances_between_lattice_points/inequality_7|erdos_1970_distinct_distances_between_lattice_points / inequality_7]]
- [[../library/distance_problems/sheffer_2014_distinct_distances_open_problems_current_bounds/_index|sheffer_2014_distinct_distances_open_problems_current_bounds]]
- [[../library/distance_problems/sheffer_2014_distinct_distances_open_problems_current_bounds/problem_22|sheffer_2014_distinct_distances_open_problems_current_bounds / problem_22]]
- [[../library/distance_problems/sheffer_2014_distinct_distances_open_problems_current_bounds/problem_25|sheffer_2014_distinct_distances_open_problems_current_bounds / problem_25]]

<!-- END problem library links -->
