---
name: research/leads/distinct_totient_blocks_from_collision_bounds
title: Distinct totient blocks from the uniform collision bounds
desc: |
  An author-recorded deduction from the uniform shifted-collision bounds of
  Pollack, Pomerance and Treviño that almost every block of length below
  (log x)^2/(log log x)^50 carries pairwise distinct totients, answering
  Problem 1004 for every exponent below 2; the first-moment barrier at
  exponent 2 and the every-exponent question remain.
problems:
- 1004
research_state: candidate
review_status: reviewed
created: 2026-09-28T06:16:37Z
updated: 2026-10-19T04:19:07Z
---

# Distinct totient blocks from the uniform collision bounds

[[research/leads/_index|..]]

***

This lead's notes that cite no source are author-recorded research, not claims.

## Target and exact question

[[problems/arithmetic_functions/E1004/_index|Problem 1004]]: let $c>0$; if $x$ is
sufficiently large, is there $n\le x$ such that $\varphi(n+k)$,
$1\le k\le(\log x)^c$, are pairwise distinct? erdosproblems.com's non-strict
upper endpoint is the target, as the problem page's current assessment fixes it.
The question is asked for every fixed $c>0$, and the problem page records it as
open. That page records the anonymous note's claim of every fixed $c<2$ as a
pending partial claim, says that the cited sources state no growing-block
existence theorem, and records this lead's deduction for $c<2$ under Progress.

## Established inputs at their actual scope

Both inputs are published theorems of Pollack, Pomerance and Treviño, *Sets
of monotonicity for Euler's totient function* (Ramanujan J. 30 (2013)),
recorded on the cards
[[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/theorem_3_1|Theorem 3.1]]
and
[[../library/primes/pollack_et_al_2013_sets_monotonicity_euler_totient_function/theorem_3_3|Theorem 3.3]]
and reconstructed under the Problem 49 research folder:

- Theorem 3.1: $P_1(x;k)<x/\exp((\log x)^{1/3})$ for $x>x_0$, uniformly for
  $k\le\exp((\log x)^{1/3})$. In the source this is a proof sketch pointing
  to two other papers; the
  [[research/erdos_49/theorem_3_1_reconstruction|reconstruction]] records
  the sketch and its one written deduction only.
- Theorem 3.3: $P_0(x;k)\le(16C_2+o(1))c(k)x/(\log x)^2$ uniformly for even
  $k\le x^{\varepsilon(x)}$, together with the explicit bounds
  $1/(2k)\le c(k)\le3\cdot7^{3+2\omega(k)}\prod_{p\mid k,p>2}\frac{p-1}{p-2}\cdot\frac1k$.
  The [[research/erdos_49/theorem_3_3_reconstruction|reconstruction]] writes
  the proof out modulo Selberg's sieve as the source states it and
  Evertse's $S$-unit bound inside
  [[research/erdos_49/lemma_3_2_reconstruction|Lemma 3.2]].

Here $P(x;k)=\#\{n\le x:\varphi(n)=\varphi(n+k)\}=P_0(x;k)+P_1(x;k)$ is the
split of the source's §3 into the structured solutions of Theorem A and
the rest; $P_0(x;k)=0$ for odd $k$.

## The route and what is proved

The union bound over the $\binom L2$ shifts of a block of length $L$ costs
at most $L\sum_{h<L}P(x+L;h)$ bad starting points $n\le x$. The odd shifts
and the unstructured part of the even shifts are $o(x)$ by Theorem 3.1 for
every $L\le(\log x)^2$. The structured part is
$(16C_2+o(1))L\sum_{h<L}c(h)\,x/(\log x)^2$, and the upper bound on $c(k)$
gives $\sum_{h\le L}c(h)\ll(\log L)^{49}$ by a Mertens product. The result
is the following proposition, proved in full as Proposition 1 on the
[[research/erdos_49/connections|connections page]] of the Problem 49
reconstruction folder.

**Proposition 1** (author-recorded). If $L=L(x)$ is integer-valued with
$2\le L(x)\le(\log x)^2/(\log\log x)^{50}$, then all but $o(x)$ of the
integers $n\le x$ have $\varphi(n+1),\ldots,\varphi(n+L)$ pairwise
distinct. In particular Problem 1004 has an affirmative answer for every
fixed $c<2$, in the almost-all form.

The proposition has no provisional premise beyond the two published
theorems: it is unconditional relative to them. What it inherits is the proof
status of Theorem 3.1, a sketch in the source that the corpus has not
reconstructed, while the deduction itself was independently reviewed on
2026-09-28 (Current review).

## Relationship to the retained note

The lead
[[research/leads/totient_blocks_native_note/_index|totient_blocks_native_note]]
preserves an anonymous five-page note that claims the same $c<2$ corollary
by the same union bound, using an asserted average
$\sum_{h\le L}c(h)\ll\log L$. That lead is a preservation record of an
external source and its next step is a review of the note. This lead is
the corpus's own argument: it needs no average estimate beyond the crude
$(\log L)^{49}$ that follows from the bound on $c(k)$ stated in
Theorem 3.3, so the $c<2$ answer rests on the two published theorems
alone. The sharper average, if verified, would extend the range exactly to
the $L$ with $L\log L=o((\log x)^2)$, for instance
$L\le(\log x)^2/(\log\log x)^{1+\delta}$ for fixed $\delta>0$, and to no
$L\ge\kappa(\log x)^2/\log\log x$ with fixed $\kappa>0$. The erdosproblems.com
discussion thread for the problem, read on 2026-09-28, carries the note and
a reader's remark that the statement is implicit in the source paper; the
erdosproblems.com problem page, last edited 12 April 2026, records neither.

## The consequential gap

Exponents $c\ge2$. The union bound is fed with the termwise upper bound
$P_0(x;h)\ll c(h)x/(\log x)^2$, and Theorem 3.3 also proves $c(h)\ge1/(2h)$
for even $h$; so the bound is at least of order $L\log L\cdot x/(\log x)^2$
whatever average of $c(h)$ is used, and it stops being $o(x)$ once
$L\log L\gg(\log x)^2$. This is a limit of the first-moment method, not a
proved obstruction to the target: it would become one only with a matching
lower bound $P_0(x;h)\gg c(h)x/(\log x)^2$, a prime-pair statement (both
$ar+1$ and $br+1$ prime) that is not available. If that lower bound holds,
as the Hardy--Littlewood heuristic predicts, the expected number of
collisions in a block of length $L$ at a random start is at least of order
$L\log L/(\log x)^2$; a first moment does not decide how many blocks are
collision-free. Under a Poisson model for the positions of collisions, for
$c>2$ almost all blocks fail and only atypical starts can answer the
question, and the same model predicts a longest collision-free block below
$x$ of length $(\log x)^{3+o(1)}$, under which the every-$c$ form would
fail for $c>3$. Both are heuristics. The exploratory computation on the
connections page (longest distinct blocks of length $111$, $194$ and $321$
below $10^5$, $10^6$ and $10^7$, against $(\log N)^2=133$, $191$, $260$) is
far too short in range to separate the exponents.

## Next step

1. The independent review of Proposition 1 against the two theorem
   statements was done on 2026-09-28 (Current review). Proposition 1 and the
   corollary for every fixed $c<2$ are refutation-failed relative to
   Theorems 3.1 and 3.3. The $c<2$ answer still inherits the sketch status of
   Theorem 3.1 and the sieve constant and uniformity imported inside Theorem
   3.3.
2. For $c\ge2$, decide whether the collision set
   $\mathcal C_L=\{m:\varphi(m)=\varphi(m+h)\text{ for some }1\le h<L\}$ has
   gaps of length $L$ below $x$. A positive result for some $c\ge2$ needs a
   second-moment or sieve argument, or a construction of a start $n$ avoiding
   every structured shape $m=jq$, $m+h=(j+h)p$ with $q=br+1$ and $p=ar+1$ prime;
   it would extend the answer past the first-moment barrier. A negative result
   for some $c$ would refute the every-$c$ expectation and needs a lower bound
   for collisions, hence a prime-pair input. Either outcome would settle whether
   Erdős's expectation for every $c$ is right beyond the range the union bound
   reaches.

## Current review

Reviewed. The proposition, its inputs and the gap were written by the
author of the connections page from the reconstruction pages and the two
theorem cards. The route was then independently reviewed on 2026-09-28 in the
review record
[[research/erdos_49/evidence/verify/connections_problem_1004_distinct_totients_on_a_consecutive__review|the Problem 1004 review]],
whose subject is the Problem 1004 section of the connections page together
with this lead, and, for the inputs (T1) and (T3) as the connections page
transcribes them, in
[[research/erdos_49/evidence/verify/connections_notation_and_the_inputs_used_review|the notation review]];
both reports were graded in
[[research/erdos_49/evidence/verify/connections_grade|the grade]], which
records this lead as reviewed. The route rests on Proposition 1, on (T1)
and (T3) at the standing their reconstruction pages record, on Mertens'
bound and on the parity of Theorem A's shape, and the grade records every
one of these as refutation-failed after its corrections; in its numbering
of the Problem 1004 section, Proposition 1 (S1) and the corollary for
every fixed $c<2$ in the almost-all form (S2) are refutation-failed
relative to (T1) and (T3), Steps 1--4 of the proof (S3--S6) are
refutation-failed, and in the notation section the transcriptions of (T1)
(S3) and of (T3) with its bounds on $c(k)$ and its odd-$k$ clause (S4) are
refutation-failed, the latter with correction C1. The statements this
page carries but the route does not rest on are graded as follows: the
barrier at exponent $2$ (S7), refutation-failed with correction C3; the
reach of the sharper average (S8), refuted-as-stated in its "and no
further" clause by the witness
$L=\lfloor(\log x)^2/(\log\log x\cdot\log\log\log x)\rfloor$, corrected by
C4 on the connections page and C5 here; the deduction "so for $c>2$ almost
all blocks fail" from a lower bound for collisions (S10), proof defective
with the statement unresolved, corrected by C6 there and C7 here, which
withdraw the deduction and place the conclusion under the Poisson model;
and the Poisson prediction as a model statement (S11), the exploratory
computation (S12), the relation to the retained note (S13) and this lead's
route summary and provenance (S14), refutation-failed. Corrections C5 and
C7 were applied to the sections "Relationship to the retained note" and
"The consequential gap" above, so the current text differs from the
reviewed text at those two places; this section replaces the reviewed
text's closing "Current review state" section. The review does not discharge the
sketch status of
Theorem 3.1 or the sieve constant and uniformity imported inside Theorem
3.3, which the route inherits as stated above. No tier is assigned, and
the problem's status is unchanged.

Since the review, the sentence of "The route and what is proved" that called the
deduction unreviewed and the first item of "Next step" were rewritten to record
its outcome, and the account of the problem page's assessment under "Target and
exact question" was reworded to match that page; this touches no examined
statement, proof, code or input.
