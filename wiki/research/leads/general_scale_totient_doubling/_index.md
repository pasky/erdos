---
name: research/leads/general_scale_totient_doubling
title: General-Scale Doubling from the Accepted Totient Family
desc: |
  Closed (superseded): the general-scale law V(cx)/V(x) -> c for every fixed
  c > 0 is proved by the OpenAI release's Lean-checked theorem of September
  2026, accepted as a partial claim on Problem 416; the reduction of the law
  to one balance estimate for the Conjectures.io family is retained as a record,
  not as a route.
problems:
- 416
research_state: closed
review_status: reviewed
created: 2026-09-28T06:18:00Z
updated: 2026-10-19T04:19:07Z
---

# General-Scale Doubling from the Accepted Totient Family

[[research/leads/_index|..]]

***

This lead's notes that cite no source are author-recorded research, not claims.

## Closure

Closed, superseded. The target of this lead, $V(cx)/V(x)\to c$
as real $x\to\infty$ for every fixed $c>1$, is the last clause of Theorem 2.1
of the OpenAI release manuscript of 25 September 2026, proved for every fixed
real $c>0$ and recorded as the
[[problems/arithmetic_functions/E0416/claims/2026_09_25_openai|accepted partial claim]]
on [[problems/arithmetic_functions/E0416/_index|Problem 416]]: its Lean
declaration `OAI.TotientAsymptotic.totient_asymptotic_formula` was built by
this corpus's verification with the axioms `propext`, `Classical.choice` and
`Quot.sound` only, and its statement audited against the problem's count. The
release's method is not the balance estimate (5$_c$) of this lead: it counts
the largest prime factor of a typical preimage with common endpoint parameters
at $x$ and $cx$ and compares the two counts directly. The reduction below, from
the law to one balance estimate for the Conjectures.io family, keeps its
reviewed standing as a record of what the accepted $c=2$ file would have needed
for other scales; nothing in it is a route any longer, and the next step is
withdrawn. The cluster interval of
[[../library/arithmetic_functions/zeraoulia_2026_fixed_scale_limit_points_distinct_totients/_index|the Zeraoulia preprint]]
collapses to $\{c\}$ for every $c>1$ if the accepted claim stands. The second
question of Problem 416, an asymptotic formula, is not touched by this closure;
the release's equivalent is the problem's pending full claim.

## Target and exact question

The general-scale variant of
[[problems/arithmetic_functions/E0416/_index|Problem 416]]: with $V(x)$ the
number of totient values up to $x$, does $V(cx)/V(x)\to c$ as real
$x\to\infty$ for every fixed $c>1$? Erdős posed it alongside the
two erdosproblems.com questions; it is recorded in Guy's B36
([[../library/number_theory/guy_2004_unsolved_problems_number_theory/_index|card]])
and in §1.2 of Ford's paper
([[../library/arithmetic_functions/ford_1998_distribution_totients/_index|card]]),
which says the method of its Theorem 1 falls short of it. It is not a
clause of the erdosproblems.com statement: the first question there is the case
$c=2$, answered by the Lean proof the bounty site accepted (the problem
page's Current assessment, search, records the acceptance
and its limits), and the second is an asymptotic formula, open. For
$c\ne2$ the assessment finds only the preprint's cluster-interval claim,
reconstructed on
[[research/erdos_416/zeraoulia_theorem_1_1_reconstruction|the preprint's page]]:
$c$ is a limit point of $V(cn)/V(n)$ and the cluster set is a closed interval of
unknown width; the integer powers of $2$ are settled by the accepted law by
telescoping (Consequential gap). No further status search was made here.

## Route and established inputs at their actual scope

The route is the section "Problem 416 at a general scale" of
[[research/erdos_416/connections|the connections page of the Problem 416 folder]],
where the two lemmas and the proposition below are proved.

- Lemma 416.1 (author-recorded): the finite counting inequality of
  [[research/erdos_416/kruer_kohlmeyer_lemma_2_1_reconstruction|the Lemma 2.1 reconstruction]]
  holds at every scale $c\ge1$ with the constant $\max(1,c-1)$ on the
  missing-value and excess-representation terms; finite combinatorics,
  no import.
- Lemma 416.2 (author-recorded): $|w-cv|\le\delta w$ with
  $0\le\delta\le1/2$ and $v>0$ gives $|w/v-c|\le2c\delta$, the scale-$c$
  form of [[research/erdos_416/kruer_kohlmeyer_lemma_5_1_reconstruction|the Lemma 5.1 reconstruction]].
- Proposition 416.3 (author-recorded, conditional): for a fixed $c>1$,
  if for every $0<\varepsilon<1/2$ there are retained families
  $(P_y,f_y)$ satisfying the coverage estimate (3) and the collision
  estimate (4) of the write-up's Proposition 4.1 together with the
  balance estimate (5$_c$), $A_y-cB^{(c)}_y=o(A_y)$ with $B^{(c)}_y$ the
  number of pairs whose value is at most $y/c$, then $V(cx)/V(x)\to c$.
  The proof is Steps 1–5 of
  [[research/erdos_416/kruer_kohlmeyer_theorem_1_1_reconstruction|the Theorem 1.1 reconstruction]]
  with $T(y/c)$ in place of $T(y/2)$.
- Estimates (3) and (4) concern one family at one scale and do not
  mention $c$. The family of the accepted Lean file, whose (3) and (4)
  are the kernel-accepted declarations named on the Theorem 1.1 page,
  therefore serves for every $c$, at the standing the problem page
  records for that acceptance (the file is not held and was not built
  in the corpus).

## Provisional premises

- (5$_c$) for the accepted family, for the chosen $c$. Per the write-up's
  §4.3 as read on the Theorem 1.1 page, the case $c=2$ comes from a
  common mass $H(y)$ with $A_y/H(y)\to1$ and $B_y/H(y)\to1/2$ over cores
  $b$ with $\log b\le G(y)=o(\log y)$. If the pairs above a core $b$ are the
  primes $p$ in an interval whose upper end is $y/b$ for $p-1$, so that
  $b(p-1)\le y$, then the $c=2$ balance forces the lower ends to be negligible
  in aggregate, $B^{(c)}_y/H(y)\to1/c$ follows from the uniformity
  $\pi(u/c)/\pi(u)\to1/c$ for $u\ge y^{1-o(1)}$, and (5$_c$) holds for every
  $c>1$. Whether the accepted development counts in this way is not established:
  the mass is defined only in the file.
- The standing of (3) and (4) is Conjectures.io's kernel acceptance of the
  file, recorded with its limits on the problem page; no prose proof of
  either exists.

## Consequential gap

The balance estimate (5$_c$) itself. Without it the reconstructed cluster
interval $[\alpha_c,\beta_c]$ stands for every $c>1$ that is not an integer
power of $2$; the accepted $c=2$ law settles $c=2^m$ for every integer $m\ge1$
by telescoping, and for $c=2^{1/m}$ adds that the geometric mean of $V(cx)/V(x)$
over $m$ consecutive scales tends to $c$ (for $m=2$, $\alpha_c\beta_c=2$), which
gives near-hits and no width control. A positive (5$_c$) gives no asymptotic
formula and no rate, since the mass depends on $\varepsilon$.

## Next step

Obtain the accepted file (URL, size and hash on
[[../library/arithmetic_functions/kruer_kohlmeyer_2026_doubling_law_distinct_totient_values/_index|the write-up's card]]),
read the definition of the pair family, the mass $H(y)$ and the
declaration `power_corePairs_count_asymptotic` (line 63482 in the
write-up's map) with its dependencies, and determine whether the
top-prime ranges and the count are scale-free. A positive outcome gives
(5$_c$) for every $c>1$ by the same argument, hence $V(cx)\sim cV(x)$ for
all $c>1$ at the standing of the accepted file plus an author-checked
generalization, and collapses the reconstructed cluster interval to
$\{c\}$ for every $c$; a negative one closes this route: (5$_c$) for the
accepted family would then need an argument of its own, or a differently
balanced family with its own estimates (3)–(5). Neither outcome touches the
second question of Problem 416.

## Current review

Reviewed. The route was independently reviewed on 2026-09-28 in the review
record
[[research/erdos_416/evidence/verify/connections_problem_416_at_a_general_scale_the_accepted_fami_review|the general-scale review]],
whose subject is the general-scale section of the connections page together with
this lead, and graded in
[[research/erdos_416/evidence/verify/connections_grade|the grade]], which
records this lead as reviewed. The graded verdicts of the statements the route
rests on, in the review's numbering, are these. The target and its provenance
(S1): refutation-failed, the clause that Erdős posed the variant with the
problem supported by his 1979 paper. Lemma 416.1 (S2) and Lemma 416.2 (S3):
refutation-failed, both re-derived. Proposition 416.3 (S4): refutation-failed as
a conditional from (3), (4) and (5$_c$), with its Step 4 re-derived. The
scale-free remark, that (3) and (4) do not mention the scale (S5):
refutation-failed. The plausibility argument for (5$_c$) in the Provisional
premises (S6): refutation-failed under the interval reading of its hypothesis,
which correction C5 writes out. The geometric mean for $c=2^{1/m}$ (S7) and
$\alpha_c\beta_c=2$ (S8): refutation-failed, both re-derived. No formula, no
rate and no prose proof (S9), and the standing sentences (S13):
refutation-failed. The sentence that the cluster interval stands for every
$c\ne2$ (S10): refuted-as-stated, witness $c=4$, where
$V(4x)/V(x)=(V(4x)/V(2x))(V(2x)/V(x))\to4$ by the accepted $c=2$ law; it sat in
the Consequential gap as a description of what remains without (5$_c$), not as a
step of the route, and correction C4 replaces it. The positive outcome of the
next step (S11): refutation-failed; the negative outcome (S12) is not a claim,
and correction C6 rewords what it establishes. The corrections C4, C5 and C6
were applied to this page (the Target and Consequential gap sentences on the
integer powers of $2$; the hypothesis of the (5$_c$) premise, now an interval
for $p-1$ whose lower ends the $c=2$ balance makes negligible; and the negative
outcome of the Next step) and to the general-scale section of the connections
page, so the current text of both differs from the reviewed text at those
places. The premise (5$_c$) remains provisional, and (3) and (4) keep the
standing of the accepted file. No tier is assigned, and the problem's status is
unchanged.
