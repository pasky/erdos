---
name: research/leads/factorial_unit_fraction_transfer
title: Unit-Fraction Bounds from the Accepted Factorial Divisor Bound
desc: |
  Closed (superseded): Transfers the Conjectures.io-accepted h(n!) < n^epsilon
  of Problem 18 to N(b) at most 2 (log b)^epsilon (Problem 304) and v(k) at
  least exp(k^A) (Problem 293); reviewed 2026-09-28; superseded by the OpenAI
  release's bounds.
problems:
- 304
- 293
research_state: closed
review_status: reviewed
created: 2026-09-28T06:15:52Z
updated: 2026-10-19T04:19:07Z
---

# Unit-Fraction Bounds from the Accepted Factorial Divisor Bound

[[research/leads/_index|..]]

***

This lead's notes that cite no source are author-recorded research, not claims.

## Targets and status evidence

[[problems/unit_fractions/E0304/_index|Problem 304]] asks to estimate
$N(b)=\max_{1\le a<b}N(a,b)$, where $N(a,b)$ is the least number of distinct
unit fractions with denominators above $1$ summing to $a/b$, and whether
$N(b)\ll\log\log b$. The problem page records it as answered: Theorem 1.1 of the
OpenAI mathematics release's manuscript of 25 September 2026 gives
$N(b)\le c_2\log\log b$ for every $b\ge b_0$, accepted on its Lean evidence, so
with Erdős's 1950 lower bound $N(b)\asymp\log\log b$. The earlier bounds were
$\log\log b\ll N(b)\ll\sqrt{\log b}$ (Erdős 1950; Vose 1985), and the van Doorn
note's claimed $N(b)\le2c_0(\log\log b)^2$ is a pending claim.

[[problems/unit_fractions/E0293/_index|Problem 293]] asks for the growth of $v(k)$,
the least integer above $1$ that occurs in no decomposition
$1=1/n_1+\cdots+1/n_k$ with $1\le n_1<\cdots<n_k$. The problem page records it
as open: Corollary 1.3 of the same manuscript, accepted as a partial claim on
its Lean evidence, gives $e^{e^{k/600}}\le v(k)$ for all large $k$, so
$\log\log v(k)=\Theta(k)$, and the best upper bound remains
$v(k)\le c_0^{(2/5+o(1))2^k}$. Before the release the best lower bound was
$e^{ck^2}\le v(k)$ (van Doorn and Tang), and the note's claimed doubly
exponential bound is a pending claim.

Both questions are the exact erdosproblems.com questions; no variant is
substituted.

## Route

The route is the classical transfer from divisor representations of a
practical number to unit fractions, with the accepted factorial bound as its
input. Every link is proved on
[[research/erdos_18/connections|the Problem 18 connections page]] in its
sections on Problems 304 and 293 and its shared lemmas; this page states the
chain and its standing.

**Established inputs, at their actual scope.**

- *Part (b) of Problem 18.* For every $\varepsilon>0$, $h(n!)<n^{\varepsilon}$
  for all sufficiently large $n$, where $h(n!)$ is the least $k$ such that
  every $1\le m\le n!$ is a sum of at most $k$ distinct divisors of $n!$, a
  fresh set for each $m$. Standing: the Lean proof accepted by the bounty site
  and filed as
  [[../library/divisors/jenw1n_2026_lean_proof_erdos_problem_18b/_index|the JenW1N record]]
  (kernel check, review, certification and payment in September 2026; not
  refereed; a single kernel; not built here), whose
  [[../library/divisors/jenw1n_2026_lean_proof_erdos_problem_18b/target|target page]]
  confirms that the formal $h$ is this one. The thresholds $n_0(\varepsilon)$
  are not extracted, so every bound below is ineffective in $b$ and $k$.
- *Lemma C, the unit-fraction transfer* (the note's Lemma 5.1, reconstructed
  with proof on the connections page; author-recorded, elementary): for
  practical $n\ge b\ge2$ and $1\le a<b$, $a/b$ is a sum of at most $2h(n)$
  distinct unit fractions with denominators above $1$, none equal to $b$ when
  $b\nmid n$.
- *Lemma C′, avoiding a prescribed denominator* (connections page;
  author-recorded): for large $b$ with $n$ the least integer with $n!\ge b$,
  either $N=n!$ or $N=p^j(n-1)!$, with $p$ the least prime not dividing $n$
  and $p^j\ge n$, is practical with $N\ge b$, $b\nmid N$ and
  $h(N)\le\max(h(n!),h((n-1)!)+\lceil\log_2n\rceil)$. It uses the extension
  step [[research/erdos_18/doorn_lemma_3_1_reconstruction|Lemma 3.1]] of the
  van Doorn reconstruction with $A=p$ and $L=1$; that page carries the label
  *claimed* because the note is a claim, but the lemma's proof is complete on
  the page and is consumed here as an elementary argument, not on the note's
  authority.
- *Factorials are practical with the ratio-two property* (Lemma A of the
  connections page, or the compilation-supplied proof on
  [[research/erdos_18/hughes_lemma_4_reconstruction|the Lemma 4 page]]).
- *Nesting.* $D_k\subseteq D_{k+1}$ for $k\ge2$, and $v(k)\to\infty$:
  van Doorn–Tang, Lemma 2.1 and Theorem 1.1, refereed, on
  [[../library/unit_fractions/doorn_2025_smallest_denominator_not_contained_unit_fraction/theorem_1_1|the Theorem 1.1 page]].

**Conclusions (author-recorded; conditional on part (b) at its standing).**

- (304.1) For every $\varepsilon>0$ there is $b_0(\varepsilon)$ with
  $N(b)\le2(\log b)^{\varepsilon}$ for all $b\ge b_0(\varepsilon)$: with $n$
  the least integer with $n!\ge b$, $n<\log b$ and Lemma C gives
  $N(b)\le2h(n!)<2n^{\varepsilon}$. This is below Vose's bound for every
  $\varepsilon<\tfrac12$.
- (293.1) For every $\varepsilon>0$ there is $k_0(\varepsilon)$ with
  $v(k)\ge\exp((k/5)^{1/\varepsilon})$ for all $k\ge k_0(\varepsilon)$; hence
  $v(k)\ge\exp(k^{A})$ for every fixed $A>0$ and all large $k$: Lemma C′ and
  Lemma C write $(b-1)/b$ without $1/b$ in at most $2h(N)\le4n^{\varepsilon}$
  terms, adjoining $1/b$ gives a decomposition of $1$ containing $b$, and the
  nesting places $b$ in $D_k$ for every $k\ge5(\log b)^{\varepsilon}$.

The full proofs are the displayed items (304.1) and (293.1) of the
connections page.

## Provisional premises

The only nonelementary premise is part (b) at its recorded standing. Nothing
here depends on the claimed van Doorn chain: its Proposition 4.1 would give
the stronger (304.3) and (293.3) on the connections page, and this lead is
independent of it.

## Consequential gap

There is no gap inside the deduction. What separates the two bounds from the
problem pages is recording: the fresh-context check of the transfer that the
corpus's rule requires before a problem page records a consequence of an
accepted result was made on 2026-09-28 (Current review), and the problem pages
do not carry the bounds. The standing of part (b) itself (Conjectures.io
acceptance, not refereeing) is inherited and is stated wherever the bounds are
quoted.

## What the route cannot give

The exponent-one statements, $N(b)\ll\log\log b$ and $v(k)\ge e^{e^{ck}}$,
are out of reach of this route for exact reasons recorded on the connections
page: [[research/erdos_18/hughes_remark_6_reconstruction|Remark 6]] gives
$h(n!)\gg(\log n)^2\approx(\log\log b)^2$, so factorials can never give less
than $(\log\log b)^2$ through Lemma C, and the counting floor (Lemma D of the
connections page) shows that certificates built from Lemma 3.1 extensions
from a seed bounded independently of the scale are never below
$(1/(2\log2)-o(1))(\log\log N)^2$. Both mechanisms stop at exponent $2$; the
conjecture of Problem 304 needs a practical $N\in[b,\exp((\log b)^{O(1)})]$
with $h(N)\ll\log\log N$, which neither mechanism can supply; the greedy
count of Lemma B on another ratio-two family is not excluded by counting,
but no gap input of the required strength is known.

## Next step

The fresh-context refutation review of Lemma C, Lemma C′, (304.1) and (293.1)
was made on 2026-09-28 and passed (Current review). The remaining step is to add
to the Problem 304 and 293 pages the bounds $N(b)\ll_\varepsilon(\log
b)^{\varepsilon}$ and $v(k)\ge\exp(k^{A})$ with the standing of part (b) stated
in the same sentence. Either outcome leaves the exponent-one question open, and
that question, not a sharper exponent from the same inputs, is the mathematical
continuation.

## Current review

Reviewed. The route was independently reviewed on 2026-09-28 in the review
records
[[research/erdos_18/evidence/verify/connections_problem_304_the_number_of_unit_fractions_for_a_b_review|the Problem 304 review]]
(which covers this lead with the Problem 304 section of the connections
page and re-derives the Lemma 3.1 interface inside Lemma C′, the passage
from $(n-1)!<b$ to $n<\log b$ and the two obstructions) and
[[research/erdos_18/evidence/verify/connections_problem_293_the_least_denominator_missing_from_k_review|the Problem 293 review]]
(which covers this lead with the Problem 293 section and re-derives Lemma
C′, with an exact finite check of its construction for $3\le b\le5040$, and
the arithmetic of (293.1)), with Lemmas A, C, C′ and D re-derived in
[[research/erdos_18/evidence/verify/connections_shared_lemmas_review|the shared lemmas review]],
and graded in
[[research/erdos_18/evidence/verify/connections_grade|the grade]], which
records this lead as reviewed. The graded verdicts of the statements the
route rests on are these. Lemma A: refutation-failed. Lemma C:
refutation-failed. Lemma C′, with the Lemma 3.1 interface it consumes:
refutation-failed. The nesting $D_k\subseteq D_{k+1}$ for $k\ge2$ and
$v(k)\to\infty$, consumed at the refereed standing of van Doorn–Tang:
refutation-failed as consumed. (304.1): refutation-failed, as a deduction
conditional on the accepted part (b) at its recorded standing. (293.1):
refutation-failed, conditional on part (b). The corrections the grade
accepted were applied to the connections page, so its current text differs
from the reviewed text at the places the grade names; those near this route
are C1 (Lemma D's floor is stated for chains from a bounded seed, with
the witness $n_0=2^k$, $A_0=3$, $L_0=1$ showing that there is no floor
without a seed bound), C2(a), C4(a), C5 and C6 in the obstruction paragraphs
of the Problem 304 and 293 sections, on which the route does not rest, and
C3, which says that (304.1) is the first consequence of part (b) drawn
in this corpus and that no search for an earlier one was made. Corrections
C2(b) and C4(b) were applied to the section "What the route cannot give"
above, so the current text of this page differs from the reviewed text at
those two places; the Consequential gap and Next step sections record this
review as the fresh-context check. The problem pages do not carry the bounds. No
tier is assigned, the standing of
part (b) is inherited unchanged, and the status of neither problem changes.

Since the review, the summary (`desc`), "Consequential gap" and "Next step" of
this page were rewritten to record its outcome, and "Targets and status
evidence" was restated against the current problem pages, which record Problem
304 as answered; this touches no examined statement, proof, code or input.

## Closure

Closed as superseded. The OpenAI mathematics release's manuscript *Short
Egyptian fractions* (25 September 2026) proves both exponent-one statements
that this route cannot reach, $N(b)\ll\log\log b$ and $v(k)\ge e^{e^{ck}}$ for
large $k$, by a different method, a divisor-selected descent with no practical
numbers and no $h(N)$; the corpus's verification built and audited the Lean
declarations, and the results are recorded on
[[problems/unit_fractions/E0304/claims/2026_09_25_openai|the Problem 304 claim page]]
(accepted, full) and
[[problems/unit_fractions/E0293/claims/2026_09_25_openai|the Problem 293 claim page]]
(accepted, partial). Those bounds imply (304.1) and (293.1) without the
Problem 18 premise, since $\log\log b=o((\log b)^{\varepsilon})$ and
$e^{k/600}$ eventually exceeds every power of $k$, so the problem pages carry
the accepted bounds and not this route's conditional ones. The transfer itself
(Lemmas A, C, C′ and D with their reviews) stays recorded above as independent
mathematics, and nothing on this page is contradicted: the route's own limits,
stated under "What the route cannot give", stand.
