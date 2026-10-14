---
name: problems/set_theory/E0602
title: Problem 602
desc: |
  Asks whether every family of countably infinite sets, any two meeting in a
  finite set of size other than $1$, has a $2$-coloring of its union with no set
  monochromatic.
tags:
- Combinatorics
- Set theory
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-14T01:12:01Z
---

# Problem 602

[[problems/set_theory/_index|..]]

[[problems/set_theory/E0602/claims/_index|claims/]]: The 1 claim page of Problem 602, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $(A_i)$ be a family of sets with $\lvert A_i\rvert=\aleph_0$
for all $i$, such that for any $i\neq j$ we have $\lvert A_i\cap A_j\rvert$
finite and $\neq 1$. Is there a $2$-colouring of $\cup A_i$ such that no $A_i$
is monochromatic?

**Status.** Open. Bloom's catalog labeled the problem OPEN and shows no verdict.
Its proof-claims tab carries one partial proof claim, filed 2026-10-01. The
claim gives a finite criterion for Property B, and its author says it does not
resolve the problem. The filing is recorded below, and
[[problems/set_theory/E0602/claims/2026_07_22_gao|its claim page]] is rejected,
since it settles no instance of the question.

**Source.** [erdosproblems.com/602](https://www.erdosproblems.com/602), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #602,
https://www.erdosproblems.com/602.

**Formalization.** Statement in
[formal-conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/602.lean).

## Current assessment

**The question (erdosproblems.com formulation, accessed 2026-09-04).** The
statement above; OPEN. The erdosproblems.com commentary attributes the problem
to Komjáth and notes that the existence of such a $2$-coloring is called
Property B. No assessment of the mathematics is recorded here beyond the known
special cases below.

**Known special cases.** Countable families have Property B by Bernstein's
lemma, which the formal-conjectures file states as a solved variant, so the
question concerns uncountable families. Families whose pairwise
intersections all have fewer than $n$ points, for a fixed finite $n$, have
Property B by Miller's theorem (E. W. Miller, On a property of families of
sets, C. R. Soc. Sci. Lett. Varsovie Cl. III 30 (1937), 31--38). Komjáth
(Families close to disjoint ones, Acta Math. Hungar. 43 (1984), 199--207,
doi:10.1007/BF01958019) strengthens this for such families of countable
sets to essential disjointness: removing a finite set from each member
leaves the members pairwise disjoint. Pairwise finite intersections alone
do not suffice, since Miller's almost disjoint family on $\omega$ lacks
Property B; so the hypothesis that no intersection has exactly one point
does work. Countably many colors always suffice: Erdős reports in
[[../library/set_theory/erdos_1987_problems_finite_infinite_graphs/problem_12|Problem 12]]
of his 1987 problem paper (printed p. 227) that when only
$|A_i\cap A_j|\ne1$ is assumed, Komjáth easily showed the chromatic number
to be at most $\aleph_0$, and the erdosproblems.com commentary on
[[problems/set_theory/E0603/_index|Problem 603]] (page last edited 6 July
2026) repeats it. The families here satisfy that hypothesis. Erdős gives no
proof or reference, no paper of Komjáth's stating the bound was identified,
and it is not checked here. The case left open is that of uncountable
families whose pairwise intersections are finite but not uniformly bounded,
and for them the question is whether two colors suffice where countably many
do. These results have no claim pages: the erdosproblems.com commentary and the
community database credit none of the earlier ones, and Komjáth's countable
bound answers no instance of the two-color question.

**Claims.** The one claim page is rejected, and the frontmatter standing is open
with no claim. The one filing on the erdosproblems.com proof-claims page (claim
380, filed 2026-10-01 by Lezhe Gao under the forum name lezhe, with the systems
DeepSeek and GPT-5.5 named in its entry) is the manuscript "Peeling Hypergraphs:
A Structural Sufficient Condition for Property B", a Zenodo deposit of
2026-07-22 (doi:10.5281/zenodo.21475088). It calls a finite hypergraph peeling
if its edges can be ordered so that each edge brings at least two vertices not
in any earlier edge, or one such vertex together with a vertex of an earlier
edge, proves that every peeling hypergraph has Property B, and characterizes
peeling hypergraphs by acyclic assignments of vertices to edges; for graphs the
peeling ones are exactly the forests. It does not address the question, whose
sets are countably infinite: the claimant's notes say that it is neither a proof
of the infinite problem nor a partial solution to it, having no compactness
argument, transfinite construction or reduction from the infinite case, and that
it was filed as a related finite criterion in the hope that it prompts work on
the infinite version. As a claim erdosproblems.com shows, it has a claim page,
[[problems/set_theory/E0602/claims/2026_07_22_gao|rejected]] because it settles
no instance of the question.

**Search scope:** the erdosproblems.com problem page, commentary, discussion
thread (one comment by 2026-10-07, post 5648 of 2026-04-20) and proof-claims
page, with the Zenodo record of the claim. arXiv, Crossref, MathSciNet, zbMATH,
Google Scholar and X were not searched.

**Remaining gaps.** (1) The mathematics of the question has not been
assessed, and the literature on Property B for the stated families was not
searched beyond the classical results named above. (2) The finite criterion
filed on erdosproblems.com was not read beyond its record and the claim's
summary.
<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/set_theory/erdos_1987_problems_finite_infinite_graphs/_index|erdos_1987_problems_finite_infinite_graphs]]
- [[../library/set_theory/erdos_1987_problems_finite_infinite_graphs/problem_12|erdos_1987_problems_finite_infinite_graphs / problem_12]]

<!-- END problem library links -->
