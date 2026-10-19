---
name: research/leads/rational_ratio_dyadic_floor_descent
title: Rational-ratio dyadic floors by permanent descent
desc: |
  Transports the Yu--Chen permanent descent to two dyadic floor sequences
  with rational ratio: strong completeness for every coefficient with long
  zero runs, hence almost every coefficient on each rational-ratio line,
  finite certificates for specific pairs, and the coefficients with only
  short common zero runs as the remaining gap in Hegyvári's conjecture.
problems:
- 354
research_state: ready
review_status: reviewed
created: 2026-09-28T06:40:00Z
updated: 2026-10-19T04:19:07Z
---

# Rational-ratio dyadic floors by permanent descent

[[research/leads/_index|..]]

[[research/leads/rational_ratio_dyadic_floor_descent/evidence/_index|evidence/]]: Exact finite completeness certificates for specific two-ray dyadic floor
sets with rational ratio, recomputed by one entry point: the pinned
pairs, a sweep over thirty-two rational coefficients, and an incomplete
control pair.

***

This lead's notes that cite no source are author-recorded research, not claims.

## Target and status evidence

For $\alpha,\beta>0$ let

$$
A_{\alpha,\beta}=\{\lfloor2^n\alpha\rfloor,\lfloor2^n\beta\rfloor:n\ge0\}
\setminus\{0\}.
$$

Hegyvári's conjecture, as recorded on
[[problems/additive_bases/E0354/_index|Problem 354]] and in Fan's preprint, says
that $A_{\alpha,\beta}$ is complete (every sufficiently large integer a sum
of distinct elements) whenever $\alpha/\beta$ is not a power of $2$ and at
least one of $\alpha,\beta$ is not a dyadic rational, a nonzero integer
times a power of $2$. The problem's Current assessment records the
irrational-ratio case as answered yes on a Conjectures.io-accepted Lean proof,
the case of exactly one dyadic rational as Hegyvári's
(erdosproblems.com-attested, paper not held; Fan's preprint, held, records it as
Hegyvári's on p. 4), and the remaining rational-ratio cases as untouched by
every 2026 source. The target here is exactly those cases: $\alpha/\beta$
rational, not a power of $2$, neither coefficient a dyadic rational. After
multiplying one coefficient by a power of $2$ the ratio is $p/q\in(1,2)$ in
lowest terms, and $\alpha=p\gamma$, $\beta=q\gamma$ with $\gamma=\beta/q$ not a
dyadic rational.

## Route and established inputs

The route is the permanent descent of the Yu--Chen manuscript,
reconstructed on the
[[research/erdos_354/yu_chen_theorem_5_1_reconstruction|Theorem 5.1 page]]
of the Problem 354 folder with the
[[research/erdos_354/yu_chen_normalization_reconstruction|normalization]]
and the three finite lemmas
([[research/erdos_354/yu_chen_lemma_2_1_reconstruction|2.1]],
[[research/erdos_354/yu_chen_lemma_2_2_reconstruction|2.2]],
[[research/erdos_354/yu_chen_lemma_2_3_reconstruction|2.3]]), whose
inputs are the interlacing of the two rays and the base-$2$ digit
recurrence, not the ratio. The
[[research/erdos_354/connections|connections page]] proves, as
author-recorded statements:

- Lemma 354.1: for every normalized pair not consisting of two dyadic
  rationals, incompleteness forces bounded event spacing (an event in
  $(n,4n]$ for every large $n$).
- Proposition 354.2: at a rational ratio $p/q$ the descent constant
  $K_*(p,q)=2q(p-1)+4(p+q)+64$ is fixed at every exact layer, so a zero
  run of the fixed length $L(p,q)=\lceil\log_2K_*\rceil-1+\lceil\log_2p\rceil$
  in the binary expansion of $\gamma$ produces one descent of the modular
  run invariant; infinitely many such runs give completeness.
- Corollary 354.3: $A_{\alpha,\beta}$ is strongly complete whenever
  $\gamma$ is not a dyadic rational and has infinitely many runs of
  $L(p,q)$ zeros, hence for Lebesgue-almost every $\gamma$ on each
  rational-ratio line ($L(3,2)=8$, $L(5,4)=10$, $L(5,3)=9$).
- Lemma 354.4: if the subset sums of the first $n$ layers of a normalized
  pair contain $b_n=\lfloor2^n\beta\rfloor$ consecutive integers, the
  pair is complete; the
  [[research/leads/rational_ratio_dyadic_floor_descent/evidence/_index|evidence]]
  certifies $(48/5,32/5)$, $(48/7,32/7)$, $(80/9,64/9)$,
  $(6\sqrt2,4\sqrt2)$, $(5\sqrt2,3\sqrt2)$ and thirty-two further pairs
  $(3\gamma,2\gamma)$ with $\gamma=2^T/d$, all outside every held source,
  and none of them known to be covered by Corollary 354.3: the rational
  coefficients have no zero run of the required length, and $\sqrt2$ is
  not known to have infinitely many.

## Provisional premises

The descent is consumed through the author-recorded reconstruction of
Theorem 5.1 and its finite certificate (rechecked by the folder's
evidence); the manuscript is unrefereed; the reconstruction of that page
has a filed focused review in the folder's evidence, graded faithful and
sound with one correction and assigning no tier. The transport imports
items 1--6 and the reduction of the normalization page, Lemmas 2.1--2.3,
Theorem 5.1 with the Appendix A certificate (finite data rechecked by the
folder's evidence) and Step 2 of the theorem page, each at the standing
its own page records; Lemma 354.4 and the certificates rest on the
normalization page alone. The a.e. statement imports Borel's normal number
theorem. Everything here is author-recorded; its review standing is stated
under Current review.

## The consequential gap

Coefficients $\gamma$ with only finitely many maximal common zero runs of
length at least $\lceil\log_2K_*\rceil-1$ at exact layers: every rational
$\gamma$ whose denominator has odd part at most $2^{\lceil\log_2K_*\rceil}$
($128$ at ratio $3/2$), in particular every rational pair certified by the
evidence, and uncountably many irrationals, while $\gamma=1/511$ at ratio
$3/2$, with infinitely many runs of eight zeros, is covered by Corollary
354.3. For them exact layers occur only at the $s$ with
$\{2^s\gamma\}<1/p$, possibly nowhere, and the common zero runs after them
are too short for Theorem 5.1, and the irrational-case continuation of the
Yu--Chen argument does not apply for two reasons recorded on the
connections page:
a rational ratio has finitely many good rational approximants, so the
digit budget and the sparse windows are empty, and a rational ratio lies
in the compact set $\mathcal C_k$ of ratios of sparse binary sums, so
returns between exact layers can cost two events (the witness at ratio
$3/2$: $\{2^s\gamma\}\in[1/4,1/3)$). Hegyvári's conjecture therefore stays
open for these coefficients, pair by pair certifiable but not uniformly
proved.

## Next step

Two bounded investigations. First, a descent for periodic conversions: for
rational $\gamma=m/v$ with $v$ odd, a block of layers satisfies
$a_{n+i}=2^ia_n+r_i$ with the correction
$r_i=\lfloor2^i\{2^n\alpha\}\rfloor$, the integer whose binary digits are
the eventually periodic conversions; decide whether the coefficient
interval of Step 1 and the node connection of Step 4 of the Theorem 5.1
page have analogs for such blocks. A positive outcome proves the
conjecture for every pair of rational coefficients with rational ratio; a
negative outcome locates the obstruction and leaves the search below as
the only tool. Second, extend the certificate search over families of
rational and quadratic coefficients; each positive case is a proved
instance, and a pair without a certificate to a large depth is the first
candidate for an incompleteness argument through Folkman-type gaps, which
would refute the conjecture.

## Current review

Reviewed. The route was first independently reviewed on 2026-09-28 in the review
records
[[research/erdos_354/evidence/verify/connections_problem_354_hegyv_ri_s_conjecture_at_a_rational__review|the
rational-ratio review]] (the section of the connections page that proves the
route's statements, with this lead) and
[[research/erdos_354/evidence/verify/connections_no_further_consumer_review|the
no-further-consumer review]] (the scope of the mechanism, with both leads), and
graded in [[research/erdos_354/evidence/verify/connections_grade|the grade]],
whose outcome for this lead was needs_update; its corrections C2, C3 and C4 were
applied to this page, the connections page and the evidence entry point before
the re-review below.

The route was then re-reviewed blind as it stood on 2026-10-02. The subject was
an extraction of this page and the connections page on that date, with the
review-status fields and this section removed, kept outside the repository; a
first attempt at the re-review, whose extraction carried the earlier verdicts,
was stopped before completion and its output discarded. The re-review is the
record
[[research/erdos_354/evidence/verify/lead_rational_ratio_dyadic_floor_descent_rereview|the
blind re-review]], graded in
[[research/erdos_354/evidence/verify/lead_rational_ratio_dyadic_floor_descent_rereview_grade|the
re-review grade]], which records pass. The graded verdicts of the statements the
route rests on: Lemma 354.1, Proposition 354.2, Corollary 354.3 with Borel's
theorem as its imported premise, and Lemma 354.4 are each refutation-failed, as
are the constants $L(3,2)=8$, $L(5,4)=10$ and $L(5,3)=9$, the two obstructions
with the two-event witness, and the certificate figures of all thirty-nine
pairs, under the reviewer's and the grader's independent exact recomputations;
the clause of "Route and established inputs" placing the certified pairs outside
Corollary 354.3 was proof defective; statement unresolved for the two
square-root pairs, since whether $\sqrt2$ has infinitely many zero runs of the
required length is open; and the first sentence of "The consequential gap" was
refuted-as-stated as wording only, since without "at least" it placed
$\gamma=1/511$ at ratio $3/2$, which the paragraph itself calls covered, in the
gap set. The grade's outcome for this lead is reviewed once its corrections
land, and they were applied, so the current text differs from the reviewed text
at these places: the fourth bullet of "Route and established inputs" (R1: none
of the certified pairs is known to be covered by Corollary 354.3), the first
sentence of "The consequential gap" (R2: runs of length at least
$\lceil\log_2K_*\rceil-1$), the sentence added to "Provisional premises" naming
the imported reconstruction inputs (S1), the correction $r_i$ of "Next step"
(S3), the Fan locator in "Target and status evidence" (S4), and, on the
connections page, the coverage clause after Lemma 354.4 (R1), the mesh-lemma
sentence after Lemma 354.4 (S2) and the correction $r_i$ of "Next investigation"
(S3). No tier is assigned and no status changes.
