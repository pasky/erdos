---
name: research/bipartite_four_list_search
title: Order-26 bad four-list assignments on bipartite graphs
desc: |
  Search for non-4-choosable bipartite graphs: the order-26 domain, solver and
  local-search coverage, the weighted count that excludes order 26 (L78), its
  order-27 limit, and probes below the order-40 construction.
tags: []
sources: []
created: 2026-10-14T18:24:25Z
updated: 2026-10-14T19:22:44Z
---

# Order-26 bad four-list assignments on bipartite graphs

[[research/_index|..]]

[[research/bipartite_four_list_search/evidence/_index|evidence/]]: Exact checks of the order-40 construction and every exchange deleting up to five lists and adding fewer, with the incomplete global-search instruments.

***

## Target and outcome

[[problems/graph_coloring/E0629/_index|Problem 629]] asks for the least
number $n(k)$ of vertices of a bipartite graph that is not $k$-choosable;
for $k=4$ the held literature gives $23\le n(4)\le40$. This attack asked
whether a bipartite graph on 26 vertices carries a bad assignment of
four-element lists, one with no proper colouring from the lists.

The outcome is negative, with a proof by Plasma AI supported by an
independent whole-claim examination and separate passing grade:
[[theory/combinatorics/L78_bipartite_order_26_four_choosable/_index|L78 proves that every bipartite graph with at most 26 vertices is 4-choosable]],
so $n(4)\ge27$, recorded at tier 1 with an explicit counting table and an
exact evidence program. The claim page retains the review's qualifications.
Its argument is self-contained; this page records the
domain that was searched, the
searches that found nothing, how the weighted count of L78 was found, and
where it stops.

## The reduced domain

A non-4-choosable bipartite graph on 26 vertices may be completed to
$K_{a,b}$ with $a+b=26$, and a list assignment on $K_{a,b}$ is bad exactly
when every palette subset $T$ misses a left list or contains a right list
([[theory/combinatorics/L78_bipartite_order_26_four_choosable/_proof|the proof of L78 derives this criterion and the reduction below]]).
For a bad assignment with the fewest colours, every pair of colours lies in
a list, the palette has exactly 17 colours and the 26 lists are distinct.
Two further consequences defined the search domain but are not used by L78.
Each colour lies in at least six lists and the lists hold 104 colour
incidences, so the colour degrees are $6^{16}8$ or $6^{15}7^2$, and
$\sum_{x<y}(r(xy)-1)=26\cdot6-\binom{17}{2}=20$, where $r(xy)$ counts the
lists containing the pair. Counting 8-subsets gives $1287a+715b\ge24310$,
so $a\ge10$, and equality at $a=10$ is impossible because two left lists
avoid a common 8-subset; counting 9-subsets gives $b\ge11$ in the same way.
After a side swap, $(a,b)\in\{(11,15),(12,14),(13,13)\}$. Moreover every
left list is disjoint from another left list and every right list from
another right list, since lists are distinct; this is the step L78 uses.

Both-side colour incidence is not imposed in the searches. The proof of
L78 uses no at-most-25 lower bound: padding reduces every smaller order to
the same order-26 contradiction.

Badness also forces the 26 lists, read as one 4-uniform hypergraph, to have
no proper 2-colouring: a 2-colouring with no monochromatic list is a palette
subset that meets every list and contains none. This side-free condition is
weaker than badness and was searched separately.

## Searches and their coverage

All runs below ended without a witness, and none is an exclusion. They are
recorded as search observations; L78 does not depend on them.

- **Signed Boolean formulation.** One variable per side and four-subset of
  the 17 colours, one clause per colour pair, sequential-counter
  cardinality constraints, the lists $\{0,1,2,3\}$ and $\{4,5,6,7\}$ fixed
  on the left, and one clause for each of the 115200 palette subsets meeting
  both fixed lists (about 0.3 million variables and 0.7 million clauses).
  The kissat solver ran for 12 minutes on the domain $a\in\{12,13\}$ and for
  12 minutes on the same domain with exact degrees, colour 8 of degree 8 and
  the others of degree 6; both returned UNKNOWN.
- **Side-free formulation.** One variable per four-subset, pair coverage,
  degrees at least six, the same two fixed lists, at most 26 lists, and one
  clause for each of the 50176 relevant complementary pairs of palette
  subsets requiring a monochromatic list. Kissat ran 5 minutes and returned
  UNKNOWN. The same generator returns the Fano plane for 3-lists on seven
  colours with seven lists, and UNSAT with six.
- **Simulated annealing.** The state is a fixed number of signed
  four-subsets, scored by the number of uncovered palette subsets (subsets
  meeting every left list and containing no right list). On 17 colours the
  lowest scores reached were 13083 at order 26 (two million steps), and
  5638, 3028 and 2076 at orders 30, 36 and 40, with a list allowed once on
  each side when replacing a list; side flips may introduce within-side
  repetitions. On 11 colours at order 46 it reached 8. For 3-lists it finds
  the Fano plane on both sides of $K_{7,7}$ when a list may repeat across
  sides, and bad assignments of 18 distinct 3-lists on nine colours, but in
  short runs on seven to nine colours none with distinct lists at orders 14
  to 16. These scores measure the search, not the space: the annealer also
  fails at order 40, where the construction of
  [[../library/graph_coloring/hanson_1996_choosability_bipartite_graphs/_index|Hanson, MacGillivray and Toft, which gives $n(4)\le40$]]
  exists on 12 colours (see below).

The annealer's permissive side window $[1,100]$ initializes an inaccurate
internal left-list counter when the order is below 50; the uncovered-subset
score is still computed from the actual lists. Its scores give no exclusion
and its side-count restriction is not trusted in those probes. The exact
exchange checker below has neither restriction.

The three instruments are retained in the
[[research/bipartite_four_list_search/evidence/_index|evidence folder]] with
their commands. They write only to ignored output, and their runs are
observations, not certificates.

## The weighted count

Averaging over a whole layer of palette subsets cannot exclude order 26.
For the split $(13,13)$ the 8-subsets carry on average
$13(1287+715)/24310\approx1.07$ events, and a linear program that adds the
second moments of every layer reports feasible solutions in floating point
for the splits $(12,14)$ and $(13,13)$. This relaxed model supplies no
exclusion. The count that succeeds weights only the palette subsets
meeting two disjoint left lists $A_1,A_2$. There the events of $A_1$ and
$A_2$ vanish, so the remaining 24 lists must cover these subsets alone. A
weighting that is uniform on each profile
$(|T\cap A_1|,|T\cap A_2|,|T\cap W|)$ gives each other list an event weight
that depends only on its intersection type. The best such weighting is a
linear program in 160 profile weights. Its optimum lies below 1 for every
side split $2\le a\le24$ at order 26, so the 24 lists cannot carry enough
weight. The largest reported objective, $0.99627$, is at $(14,12)$. The retained
integer weights and their exact check are retained with
[[theory/combinatorics/L78_bipartite_order_26_four_choosable/_index|L78]].

The proof needs only one small weighting. Name the smaller side left, so
$a\le13$, and round the $(13,13)$ weighting after scaling its largest
entry to 8. The six nonzero profiles, up to interchanging the fixed lists,
are $(1,1,6)$, $(1,2,5)$, $(1,2,6)$, $(1,3,4)$, $(2,3,3)$ and
$(3,3,2)$, with weights $7,3,1,8,4,6$. Their total weight is 83424;
the maximum left and right event weights are 4374 and 2664. Therefore
the other lists cover at most
$1710a+60516\le82746<83424$. The proof displays all eight possible list
types and their event weights. This is a complete exclusion through a
uniform inequality, not an exhaustion of pair coverings or a conclusion
drawn from the incomplete searches.

## Where the count stops

At order 27 the same reduction leaves palettes of 15 to 18 colours: the
midpoint bound $26$ no longer excludes 15 and 16 colours, and the equality
arguments used at order 26 no longer apply. On 18 colours every colour has
degree exactly six and the 27 lists are distinct; on 17 colours one list may
occur twice, and on 15 or 16 colours more may. The same linear program,
evaluated in floating point for 17 and 18 colours with distinct lists, no
longer excludes every split. On 17 colours the largest optimum is about
$1.036$, at $(14,13)$, and four splits exceed 1. On 18 colours it is about
$1.042$, at $(13,14)$, and seven splits exceed 1. An exclusion of order 27,
which would give $n(4)\ge28$, needs a sharper weighting and an argument for
the smaller palettes and repeated lists. Two refinements are natural. One
fixes the two disjoint right lists as well and splits into cases by their
position relative to $A_1$, $A_2$ and $W$. The other adds second-moment
terms restricted to the same profile family. Neither has been tried.

## Below the upper bound 40

The bound $n(4)\le40$ comes from the construction in the proof of Theorem 3
of [[../library/graph_coloring/hanson_1996_choosability_bipartite_graphs/_index|Hanson, MacGillivray and Toft]].
For $k=4$ it uses 12 colours: four disjoint pairs, each united with the two
left and the four right 2-lists of the bad $K_{2,4}$ assignment on four
further colours, together with the 16 transversals of the four pairs, split
between the sides by the parity of the number of first elements of the pairs
they contain. This gives 16 left and 24 right lists. The
[[research/bipartite_four_list_search/evidence/_index|evidence entry point]]
rebuilds it and checks it bad over all 4096 palette subsets. It also checks
that the construction is rigid under small exchanges. Every list is
essential, and after deleting one list the deleted list is its only single
repair. No bad assignment arises from deleting $r$ lists and adding at most
$r-1$ four-subsets on either side for any $2\le r\le5$. The added lists
range over all 990 signed four-subsets of these 12 colours, including lists
already in the construction and repeated sets on opposite sides. There
are no imposed pair-coverage or degree restrictions.

The exact search uses the colour permutations that permute the four pairs,
flip an even number of them, and preserve the two left 2-lists on the last
four colours. The checker verifies that each generator preserves all 40
signed lists, enumerates every deletion set, and takes one representative
of each generated orbit. For a representative it computes the uncovered
palette subsets. A repair must cover any chosen uncovered subset, so
branching over every signed four-subset covering it is complete. With one
list left to add, intersecting their candidate sets decides whether a
single list covers all the remaining subsets. Memoization identifies only
states with the same uncovered subsets and remaining number of additions.

| Deleted lists $r$ | All deletion sets | Checked orbit representatives | Added lists allowed |
| --- | --- | --- | --- |
| 2 | 780 | 20 | at most 1 |
| 3 | 9880 | 84 | at most 2 |
| 4 | 91390 | 381 | at most 3 |
| 5 | 658008 | 1566 | at most 4 |

Every case has no repair of the indicated size. Thus any bad assignment
of at most 39 lists on this palette shares at most 34 signed lists with
this particular construction. Indeed, if it shared at least 35, removing
the unshared base lists would delete at most five, and adding its other
lists would contradict one of these checks (or essentiality for a single
deletion). This is a finite local obstruction, not a global lower bound
on $n(4)$.

The other probes toward order 39 were inconclusive:

- Kissat, on the signed formulation with 11 to 14 colours, pair coverage,
  and a list allowed on both sides, returned UNKNOWN after 2 minutes at
  order 39 for each palette size. It also returned UNKNOWN after 3 minutes
  at order 40 on 12 colours, where the construction above exists, so these
  short runs carry no information.
- The annealer on 12 colours reached 4 uncovered subsets at order 40 and 30
  at order 39.
- The weighted count of L78, adapted to 11 to 14 colours and distinct
  lists, excludes no order from 36 to 40: at each of these orders and
  palette sizes some side splits keep a linear-programming optimum above 1.
- Putting the 13 lines of the projective plane of order 3 on both sides
  leaves 234 complementary pairs of uncovered subsets. They are the proper
  2-colourings of the plane, and extra lists must cover them. A
  time-limited integer programming run reported 34 extras suffice and a
  lower bound of 27. Neither a witness nor a certified exclusion from that
  run is retained; these are solver observations only.

Whether a bad assignment exists on fewer than 40 vertices therefore
remains open. The 12-colour palette of the known construction is the
natural place for an exact search. A complete 12-colour search at order 39
needs symmetry breaking beyond what the short solver runs had. The local
exchange obstruction makes the next construction question precise: can
one find a bad assignment on these colours with at most 39 lists and at
most 34 lists in common with the construction above? No search of that
remaining domain is complete here.
