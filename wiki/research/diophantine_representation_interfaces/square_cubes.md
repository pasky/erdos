---
name: research/diophantine_representation_interfaces/square_cubes
title: "Uniform curve bounds and cubes of squares"
desc: "A uniform genus-two point bound would bound square cubes even with repeated subset sums, while curve-by-curve finiteness does not."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/diophantine_problems/E0782/_index|E0782]].

## E0782: the missing bound must be uniform in the curve

Brown--Erdős--Freedman define quasi-progressions as strictly increasing
sequences. Repeating a square is not an answer. The second target concerns cube
sets of unbounded cardinality; adding zero directions does not help. The
inspected Cilleruelo--Granville argument uses 2^d distinct squares.

The forward proof of Brown--Erdős--Freedman Theorem 1 gives QP=>CP=>proper cubes
of arbitrary dimension. Its block induction glues translates of the same proper
cube in two disjoint increasing blocks. Their union stays proper, starting from
two distinct points, so the distinctness needed below survives.

Fix two directions b_1,b_2 of a proper square cube. Each of the 2^(d-2) distinct
squares x^2 in the remaining subcube makes

$$
(x^2+b_1)(x^2+b_2)(x^2+b_1+b_2)
$$

a square. Properness makes b_1,b_2,b_1+b_2 nonzero and pairwise distinct, so the
degree-six polynomial has simple roots. The source uses Bombieri--Lang through a
uniform genus-two rational-point bound B, giving 2^(d-2)<=B. Curve-by-curve
finiteness gives a bound depending on the varying directions and does not bound
d.

The same uniform premise handles repeated vertices too, with a weaker bound.
Remove zero directions and flip negative directions, shifting the base so all
remaining d directions are positive. If two directions differ, use them for
b_1,b_2. If all directions are equal and d>=3, group two directions as b_1 and a
third as b_2. In either case these are disjoint groups using at most three
original directions, with b_1,b_2 positive and unequal. Among the remaining
directions the empty sum and successive partial sums give at least d-2 distinct
square vertices. Each makes the same degree-six polynomial a square. Thus
d-2<=B, and the entire cube has at most 2^(B+2) elements. Cubes with d<=2
already have at most four elements. This author argument removes the proper-cube
convention gap; it does not remove the uniformity premise.

This is the precise missing hypothesis; both negative conclusions remain
conditional. The next useful test is uniformity for this special three-shift
family or an unconditional cube bound. Individual-curve finiteness does not
provide the required uniformity.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/additive_combinatorics/brown_1990_quasi_progressions_descending_waves/_index|brown
  1990 quasi progressions descending waves]]: Definitions and Section 2 forward
  CP=>C block induction; reverse examples not used (proof reading). Definitions
  of QP, CP and C, pp.1-2 (statement reading). Section 5 square-sequence
  questions (statement reading).
- [[../library/diophantine_problems/cilleruelo_2007_lattice_points_circles_squares_arithmetic_progressions/_index|cilleruelo
  2007 lattice points circles squares arithmetic progressions]]: Distinctness
  convention and exact Bombieri-Lang dependence (account reading). Section 3
  Theorem 2 uniformity input and Conjecture 6 conditional cube argument (proof
  reading).
