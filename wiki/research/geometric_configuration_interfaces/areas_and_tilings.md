---
name: research/geometric_configuration_interfaces/areas_and_tilings
title: "Area constraints and congruent tilings"
desc: "Uniform area thresholds, weighted triangle incidences and square-multiple tiling extensions expose distinct unresolved interfaces."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/discrete_geometry/E0352/_index|E0352]],
[[problems/discrete_geometry/E0507/_index|E0507]],
[[problems/distance_problems/E1086/_index|E1086]],
[[problems/discrete_geometry/E0634/_index|E0634]].

## Areas and tilings: E0352, E0507, E1086, E0634

Mauldin Section 5 reduces E0352 to unions of interiors of finitely many compact
convex sets, with one constant that must work for every number of components.
Its cases of at most three components do not provide an induction to arbitrary
component count. Bulj--Kovač Theorem 2 gives a bound O(R squared sqrt(log log
R/log R)) for sets in an R-by-R box avoiding a triangle of area one. This tends
to infinity, whereas E0352 requires an absolute area threshold. Scaling a set by
s also scales triangle areas by s squared, so normalizing the box does not
preserve the forbidden area. The source statement was inspected, not its proof.
See the primary theorem at https://arxiv.org/html/2605.30033v1. The
discriminating question is a bound uniform in the component count or box size;
neither inspected result supplies it.

For E0507, Cohen--Pohoata--Zakharov's point-tube result and its Heilbronn
application were inspected at statement level, including the n^(-7/6+epsilon)
upper-bound route. The comparison between unit-square and unit-disk versions
changes only fixed area constants: an inscribed unit square gives Delta(n) <=
alpha(n), and rescaling the disk's containing side-two square gives alpha(n) <=
4Delta(n). A finite rational-coordinate configuration can certify its minimum
area by checking every determinant, at that n only. Placing small copies of it
does not preserve a lower bound on areas of triangles meeting different copies.
No such computation or recursive construction was performed. The next test is a
proof controlling these cross-copy triangles before optimizing coordinates.

E1086 counts positive equal areas: Erdős--Purdy's opening convention explicitly
excludes zero area. Otherwise all collinear points would trivialize a different
question. For fixed A>0, scaling reduces to area one. Given a base p,q,
allowable third vertices lie on the two lines
$$
 \det(q-p,r-p)=\pm2A.
$$
These lines form a multiset indexed by bases. With points (i,0) for integer i
and points on y=2, all adjacent unit horizontal bases have the same area-one
offset line y=2. For m bases and m points on that line the triangle contribution
is of quadratic order, while the unweighted incidence contribution of that one
line is only m. Therefore an unweighted point-line bound cannot replace the
required weighted count. Raz--Sharir's O(n^(20/9)) bound was read through its
theorem card, not verified. A proposed improvement must state its line weights
and survive this example.

For E0634, any N-tiling of a triangle by congruent triangles yields an Nq
squared-tiling: subdivide every tile by the standard parallel grid into q
squared congruent triangles. All smaller triangles across all tiles remain
congruent, regardless of the original tile orientations. This is a complete
extension for square multiples. Two unrelated existence witnesses for N and M do
not give an NM-tiling unless their tile shapes allow the second subdivision.

An exact finite tiling certificate can consist of outer and tile coordinates,
equal side-length multisets, containment, disjoint interiors and total area
equality. For finitely many closed triangles these checks imply coverage: an
uncovered point of the outer triangle would, by closedness and density of its
interior, leave an uncovered open region of positive area. That contradicts area
equality. No such certificate was replayed here. The held Harries claim and its
qualifications were read; the already-disclosed withdrawal of an exclusion
dependency must not be silently ignored.

Zhang's Theorem 4 assumes integer sides a,b,c with a squared+ab+b squared=c
squared. Its printed page 5 sets M=3 ceil((c squared-a-b)/(ab)) and states
existence for every m at least M. In the proof, however, r,s,t are each taken at
least M, and their sum is then said to range over every integer at least M. The
stated choices only reach sums at least 3M. The printed page was inspected and
the transcription agrees with print. This is not a disproof of the theorem. A
possible intended
M/3 parameter choice requires checking the strict threshold and the geometric
assembly. Until then this account does not certify the exact displayed
threshold. The qualification concerns the printed argument, not the truth of the
theorem or a transcription error.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/discrete_geometry/cohen_2024_lower_bounds_incidences/_index|cohen
  2024 lower bounds incidences]]: Section 1, Theorem 1.1, Corollary 1.2; Section
  1.2 Heilbronn application (statement reading).
- [[../library/discrete_geometry/mauldin_2013_some_problems_ideas_erdos_analysis_geometry/_index|mauldin
  2013 some problems ideas erdos analysis geometry]]: Section 5, Problems
  5.1-5.2 and cases of at most three convex components (account reading).
- [[../library/discrete_geometry/zhang_2025_tiling_triangles_angles/_index|zhang
  2025 tiling triangles angles]]: Section 2.1 integer-side assumptions and
  Section 3.1 Theorem 4 and printed proof (proof reading).
- [[../library/distance_problems/erdos_1971_extremal_problems_geometry/_index|Erdős–Purdy:
  Some extremal problems in geometry]]: Opening paragraph on positive area;
  Section 4 context (statement reading).
- [[../library/distance_problems/raz_2017_number_unit_area_triangles_plane_theme/_index|raz
  2017 number unit area triangles plane theme]]: Theorem 1 statement and proof
  outline (account reading).
