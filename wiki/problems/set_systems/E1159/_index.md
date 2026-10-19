---
name: problems/set_systems/E1159
title: Problem 1159
desc: |
  Asks whether there is a constant $C>1$ such that every finite projective plane
  has a set of points meeting each line in at least $1$ and at most $C$ points.
tags:
- Combinatorics
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-17T22:11:11Z
---

# Problem 1159

[[problems/set_systems/_index|..]]

***

**Statement.** Determine whether there exists a constant $C>1$ such that the
following holds.

Let $P$ be a finite projective plane. Must there exist a set of points $S$ such
that $1\leq \lvert S\cap \ell\rvert \leq C$ for all lines $\ell$?

**Status.** Open.

**Source.** [erdosproblems.com/1159](https://www.erdosproblems.com/1159),
accessed 2026-09-04. Cite as: T. F. Bloom, Erdős Problem #1159,
https://www.erdosproblems.com/1159.

**References.**

- [ESS83] Erdős, P. and Silverman, R. and Stein, A., Intersection properties of
  families containing sets of nearly the same size. Ars Combin. (1983), 247-259.
- [Er81] Erdős, P., On the combinatorial problems which I would most like to see
  solved. Combinatorica (1981), 25-42.
- [Va99] Various, Some of Paul's favorite problems. Booklet produced for the
  conference "Paul Erdős and his mathematics", Budapest, July 1999 (1999).

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1159.lean).

## Current assessment

[[theory/combinatorics/L27_blocking_set_cap/_index|L27]] gives a complete
author-recorded incidence proof that a universal cap must be at least four:
no plane of order $q\ge5$ has a blocking set meeting every line at most
three times. At cap four the same argument gives only a necessary interval
for the set's size, not a construction. L27 is tier 0 and has no independent
review.

The held [[../library/set_systems/erdos_1983_intersection_properties_families_containing_sets_nearly/corollary_p255|Erdős–Silverman–Stein corollary]]
gives, for each $a>2e$ and all sufficiently large orders $q$, a set meeting
every line at least once and fewer than $a\log q$ times. This source
statement was inspected; its full proof was not independently audited here.
A logarithmic bound does not provide the absolute constant asked for.

[[../library/set_systems/szonyi_1992_blocking_sets_finite_planes_spaces/_index|Szőnyi's 1992 survey]]
reports on printed p. 102, from originals not read here, constant caps in
Desarguesian planes of fixed characteristic: at most $4$ points on a line
in PG$(2,3^r)$ (Bruen–Fisher), at most $p+1$ in PG$(2,p^r)$ for odd $p$
(Boros), and at most $5$ or $6$ in PG$(2,2^r)$ (Illés–Szőnyi–Wettl).
These give no absolute cap uniform over the prime-order planes PG$(2,p)$
or over non-Desarguesian planes. The applicable upper bounds read for
those families remain logarithmic. The research lead
[[research/leads/projective_plane_bounded_blocking/_index|on bounded line intersections in every plane]]
records an author proof of cap six in PG$(2,2^h)$ for $h\ge2$, an exact
obstruction to bounded-deletion moves that immediately advance coverage
from arbitrary states at a fixed power-of-two cap,
and a conditional negative argument requiring an unproved structural
premise. Its pencil count proves that, in PG$(2,q)$ with $q$ odd, a
bounded-cap blocking set has at least $q-O(\sqrt q)$ points off any bounded
union of lines and conics. An author-recorded proof using tame monodromy gives
the same bound off any curve of fixed degree in sufficiently large prime
planes. The negative answer then reduces to an unproved premise: for
each cap, a fixed proportion of every bounded-cap set of at least
$(1-\varepsilon)p$ points lies on a curve of fixed degree, for some
fixed $\varepsilon>0$.
The repair obstruction does not rule out more
selective greedy or absorbing constructions. The lead also retains exact
examples: cap four for $p=5,7,11$, cap five for $p=23,29$ and cap six for
$p=31,37,67,79$, and exhaustive nonexistence checks within specified
Singer-invariant families. These are finite facts, not a uniform mechanism
or a lower bound for arbitrary sets. The lead proves neither answer and
has no independent review. This assessment concerns these bounds and
source comparisons, not a complete literature survey.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/set_systems/asgarli_2025_blocking_sets_union_plane_curves/_index|asgarli_2025_blocking_sets_union_plane_curves]]
- [[../library/set_systems/asgarli_2025_blocking_sets_union_plane_curves/theorem_3_2|asgarli_2025_blocking_sets_union_plane_curves / theorem_3_2]]
- [[../library/set_systems/ball_1996_multiple_blocking_sets_arcs/_index|ball_1996_multiple_blocking_sets_arcs]]
- [[../library/set_systems/entin_2018_monodromy_hyperplane_sections_curves/_index|entin_2018_monodromy_hyperplane_sections_curves]]
- [[../library/set_systems/erdos_1981_combinatorial_problems_which_i_would_most/_index|erdos_1981_combinatorial_problems_which_i_would_most]]
- [[../library/set_systems/erdos_1983_intersection_properties_families_containing_sets_nearly/_index|erdos_1983_intersection_properties_families_containing_sets_nearly]]
- [[../library/set_systems/erdos_1983_intersection_properties_families_containing_sets_nearly/corollary_p255|erdos_1983_intersection_properties_families_containing_sets_nearly / corollary_p255]]
- [[../library/set_systems/erdos_1983_intersection_properties_families_containing_sets_nearly/theorem_1|erdos_1983_intersection_properties_families_containing_sets_nearly / theorem_1]]
- [[../library/set_systems/erdos_1983_intersection_properties_families_containing_sets_nearly/theorem_2|erdos_1983_intersection_properties_families_containing_sets_nearly / theorem_2]]
- [[../library/set_systems/hefez_1989_non_reflexive_curves/_index|hefez_1989_non_reflexive_curves]]
- [[../library/set_systems/kahn_1992_random_lines_projective_plane/_index|kahn_1992_random_lines_projective_plane]]
- [[../library/set_systems/szonyi_1992_blocking_sets_finite_planes_spaces/_index|szonyi_1992_blocking_sets_finite_planes_spaces]]

<!-- END problem library links -->
