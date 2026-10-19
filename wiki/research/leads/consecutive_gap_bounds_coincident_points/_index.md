---
name: research/leads/consecutive_gap_bounds_coincident_points
title: Consecutive-Gap Lower Bounds Without the Distinctness Hypothesis
desc: |
  Extends the 2026 lower bounds for the de Bruijn–Erdős consecutive-gap
  constants from sequences of distinct points to the erdosproblems.com family
  with coincident terms: a proved replacement for the short-interval list lemma,
  the fixed-r ratio bound over all sequences, and the claimed growth bounds
  conditionally on the claimed chain; independently reviewed on 2026-09-28.
problems:
- 1221
research_state: candidate
review_status: reviewed
created: 2026-09-28T05:44:00Z
updated: 2026-10-19T04:19:07Z
---

# Consecutive-Gap Lower Bounds Without the Distinctness Hypothesis

[[research/leads/_index|..]]

***

This lead's results that a claim covers are credited on its claim page; its
other notes that cite no source are author-recorded research, not claims.

## Target and exact question

[[problems/analysis/E1221/_index|Problem 1221]], under its
mean-normalized reading: with the 1949 constants
$\Lambda_r=\inf_a\limsup_nnM_n^r(a)$,
$\lambda_r=\sup_a\liminf_nnm_n^r(a)$ and
$\mu_r=\inf_a\limsup_nM_n^r(a)/m_n^r(a)$, where $M_n^r(a)$ and $m_n^r(a)$
are the largest and smallest sums of $r$ consecutive gaps cut by the first
$n$ terms of $a$ on the circle of circumference $1$, do $\Lambda_r-r$,
$r-\lambda_r$ and $r(\mu_r-1)$ tend to infinity? The erdosproblems.com wording
and Section 1 of the 1949 note take the infimum and supremum over all sequences,
coincident terms allowed (a gap has length $0$ between coincident terms), while
the two 2026 sources state their lower bounds over sequences of distinct points.
The problem page's Formulation asks whether the constants over the two
families agree. This lead's question is narrower and sufficient for the
conjecture: do the 2026 lower bounds hold over the erdosproblems.com family?

The dated problem assessment is the Current assessment of the problem
page (search); no different target is taken and no further
status search was made here.

## Route and established inputs at their actual scope

The route is the extension worked out in the section "Problem 1221
itself" of
[[research/erdos_1221/connections|the connections page of the Problem 1221 folder]],
which identifies every place where the reconstructed arguments use
distinctness and discharges each.

- The 1949 bounds $\Lambda_r-r\ge\tfrac12+o(1)$, $r-\lambda_r\ge\tfrac12+o(1)$
  and $r(\mu_r-1)\ge1$ hold over all sequences as stated
  ([[research/erdos_1221/dber49_inequality_3_3_reconstruction|Section 3]],
  [[research/erdos_1221/dber49_inequality_4_3_reconstruction|(4.3)]],
  [[research/erdos_1221/dber49_inequality_5_7_reconstruction|(5.7)]];
  refereed source, author-recorded reconstructions with filed
  reconstruction reviews).
- The upper bound $\mu_r\le1+c'\log r/r$ for large $r$
  ([[research/erdos_1221/clst25_theorem_2_reconstruction|Theorem 2 of the balanced-stick preprint]];
  unrefereed, its Theorem 3 imported) is proved by exhibiting a sequence
  of distinct points, so it passes to the larger family by inclusion.
- The fixed-$r$ bound $\mu_r\ge1+r/(r^2-1)$ for $r\ge2$ over all sequences
  is Proposition 1221.2 of the connections page (author-recorded): the
  three pages
  [[research/erdos_1221/ko26a_lemma_3_1_reconstruction|Lemma 3.1 with Lemma 2.1]],
  [[research/erdos_1221/ko26a_proposition_4_1_reconstruction|Proposition 4.1]]
  and [[research/erdos_1221/ko26a_theorem_1_1_reconstruction|Theorem 1.1]]
  of the 2026 note use only gaps $\ge0$ once the contradiction hypothesis
  makes every late $r$-block positive. The filed reviews of those pages
  cover the distinct-point argument, not this reading.
- The replacement of the one lemma that uses distinctness in the 2026
  preprint,
  [[research/erdos_1221/ko26b_lemma_4_2_reconstruction|Lemma 4.2]], is
  Proposition 1221.1 of the connections page (author-recorded, with
  proof): under the short-interval counting hypothesis (4.1) there is a
  short arc holding $L'$ terms, $|L'-\lfloor S\rfloor|\le B$, none of them
  early, whose terms listed by insertion time have every prefix counting
  error at most $B$; and the imported finite-list bound for distinct lists
  implies it for lists with repeated entries by a small perturbation, so
  $B\ge\frac1{16}\log(\lfloor S\rfloor-B)$ with the comparison of the
  preprint's Section 5 unchanged.

## Provisional premises

- (P) The chain reconstructed on the preprint's pages,
  [[research/erdos_1221/ko26b_lemma_2_1_reconstruction|Lemma 2.1]],
  [[research/erdos_1221/ko26b_proposition_3_1_reconstruction|Proposition 3.1]],
  Lemma 4.2 and Section 5 for the ratio part, and
  [[research/erdos_1221/ko26b_lemma_6_1_reconstruction|Lemma 6.1]],
  [[research/erdos_1221/ko26b_lemma_6_2_reconstruction|Lemma 6.2]],
  [[research/erdos_1221/ko26b_lemma_6_3_reconstruction|Lemma 6.3]],
  [[research/erdos_1221/ko26b_proposition_6_4_reconstruction|Proposition 6.4]],
  [[research/erdos_1221/ko26b_lemma_7_2_reconstruction|Lemma 7.2]] and
  Section 8 for the one-sided parts, proves
  [[research/erdos_1221/ko26b_theorem_1_1_reconstruction|Theorem 1.1]]
  for sequences of distinct points with its two imports as stated (the
  finite-list bound with constant $1/16$ derived from Larcher's proof, and
  Halász's planar $L^1$ theorem). This is exactly the standing of the
  source claim: unrefereed, with no accepted warrant for the exact
  coefficient $1/100$ and its optimized finite-list input. The complete local
  reproof with coefficient $1/200$ is a separate result, described below.
- Under (P), deduction 1221.3 of the connections page gives the three
  bounds of Theorem 1.1, with the same constant $c$ and coefficient
  $1/100$ and an absolute threshold in $r$, for every sequence, coincident
  terms allowed, hence all three parts of the conjecture for the
  erdosproblems.com family. Without (P) the lead delivers only the fixed-$r$
  bound above.

## Consequential gap

The reading of the reconstructed arguments with coincident terms is the corpus's
and was independently reviewed on 2026-09-28 in the record named under Current
review. The two places where the tie-break among coincident terms (by index)
interacts with positions are the displacement bookkeeping of Lemma 2.1 (the
moves by $kr$ places act on index sets and the displacement of a move is a sum
of spans, which may include zero gaps) and the covering identity of Lemma 6.3
(for $x$ at no term's position, a term $y_i$ is among the $r$ terms after $x$
exactly when $x$ lies in the open arc from $y_{i-r}$ to $y_i$, an empty arc when
the span vanishes). A fresh-context reader may find a step where a zero gap
breaks an inequality that the pages state for positive gaps; none was found
here. The sources define their objects for distinct points, and no source
asserts the extension. Equality of the constants over the two families remains
open and is not needed for the conjecture.

## Next step

The conditional extension with the coefficient $1/100$ still needs its premise
(P), in particular the optimized finite-list discrepancy input, discharged.
That stronger constant is unnecessary for the qualitative question. The
[[research/erdos_1221/all_sequence_composition|complete local composition]]
uses an elementary weaker finite-list bound. Its ratio conclusion is
[[theory/analysis/L163_all_sequence_span_ratio/_index|L163]] and its two
one-sided conclusions are
[[theory/analysis/L164_all_sequence_span_deviations/_index|L164]], each with
a separate whole-statement examination and passing grade. The independent
check still owed by that route is of their conjunction and its exact match to
the mean-normalized question,
[[theory/analysis/L165_consecutive_gap_growth_conjunction/_index|L165]].
Equality of the constants over the two sequence families is not needed by
either route.

## Current review

Reviewed. The route was independently reviewed on 2026-09-28 in the review
record
[[research/erdos_1221/evidence/verify/connections_problem_1221_itself_the_site_s_family_against_se_review|Problem 1221 itself: the site's family against sequences of distinct points]]
(the section of the connections page that carries the route, re-derived line
by line, and this page whole, with each named reconstruction page read in
full as a premise at its standing) and graded in
[[research/erdos_1221/evidence/verify/connections_grade|the grade]].
The graded verdicts of the statements the route rests on: the inclusion
inequalities between the constants over the two families, refutation-failed;
Proposition 1221.1, its existence part and its perturbation bridge with the
last sentence, refutation-failed; Proposition 1221.2, refutation-failed;
conditional deduction 1221.3, refutation-failed under its premise (P) after
two corrections, its clause "the same $r_0$" having been found not
established by the argument (the extended chain gives an absolute threshold
in $r$, not the threshold of the distinct-point theorem itself) and the
parenthesis of (P) having misdescribed the imported Theorem 4.1, which the
Lemma 4.2 page states for every list; and this page's restatement of the
deduction, refutation-failed after the matching correction. The premise (P)
remains an explicit hypothesis, unrefereed, with two imports unchecked. The
grade's corrections C5 and C7 were applied to the deduction on the
connections page and C6 to the second bullet of "Provisional premises"
above, so the current text differs from the reviewed text at those places.
This review warrants the conditional extension at its stated premise. It
assigns no tier and does not accept the problem as solved. The complete local
bounds and their distinct warrants described under "Next step" are outside
this earlier review's subject.

Since the review, the summary (`desc`), "Consequential gap" and "Next step" of
this page were rewritten to record its outcome; this touches no examined
statement, proof, code or input.
