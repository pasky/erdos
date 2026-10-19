---
name: research/erdos_354/evidence/verify/connections_grade
title: Distinct grade of the Problem 354 connections reviews
desc: |
  Grades the seven focused reviews of the Problem 354 connections page and
  its two leads as of 2026-09-28T13:50:48Z: all seven pass; twelve corrections,
  C1--C12, are accepted after adjudication against the pages, the held
  sources and exact recomputation; both leads need an update; no tier is
  assigned.
created: 2026-09-28T19:30:42Z
updated: 2026-09-28T19:30:42Z
---

***

## Subject

**Date and paths.** The repository as it stood at 2026-09-28T13:50:48Z: the page
`wiki/research/erdos_354/connections.md` (652 lines; its seven H2 sections open
at lines 59, 292, 441, 490, 518, 580 and 611) and the two leads
`wiki/research/leads/rational_ratio_dyadic_floor_descent/_index.md` and
`wiki/research/leads/small_base_two_ray_distance_divergence/_index.md`. Every
path was present in the tree as of that time, and the working-tree copies were
byte-identical to that state at grading.

**Reports.** The seven independent focused reviews filed in this folder,
one per H2 section of the page, each naming the same subject date, the page's
path and its section's line range as its frozen subject, the first two and the
last also naming the leads:

- [[research/erdos_354/evidence/verify/connections_problem_354_hegyv_ri_s_conjecture_at_a_rational__review|the rational-ratio review]]
  (lines 59--291, with the first lead);
- [[research/erdos_354/evidence/verify/connections_problem_354_the_second_question_at_bases_up_to_t_review|the second-question review]]
  (lines 292--439, with the second lead);
- [[research/erdos_354/evidence/verify/connections_problem_349_single_rays_and_the_digit_recurrence_review|the Problem 349 review]]
  (lines 441--489);
- [[research/erdos_354/evidence/verify/connections_problem_348_deletion_thresholds_review|the Problem 348 review]]
  (lines 490--516);
- [[research/erdos_354/evidence/verify/connections_problem_254_and_the_threshold_review|the Problem 254 review]]
  (lines 518--579);
- [[research/erdos_354/evidence/verify/connections_problem_124_mixed_power_sets_review|the Problem 124 review]]
  (lines 580--609);
- [[research/erdos_354/evidence/verify/connections_no_further_consumer_review|the no-further-consumer review]]
  (lines 611--652, with both leads).

The line ranges were checked against the committed page and are right.

**What the grader read, and at what depth.** In `docs/verification.md`,
the sections "Independence and the assignment", "Exact subjects and
durable evidence", "Report contract", "Grading and claim standing", the
shared "Audit checklist" and the Erdos-specific "Whole-claim report" and
"Audit checklist". Each of the seven reports in full. The page and both
leads in full as of that time. Reconstruction pages as of that time, where a
finding needed them: the normalization page in full; the Theorem 5.1 page's
Definitions and Statement; the theorem page's Steps 2 and 4, dependency map and
Scope; the Remark 4.2 page in full; the Theorem 9 page's Statement and the proof
of Proposition 11; the Corollary 12 page in full; the bounded-spacing page's
definitions and Steps 1--2. The first lead's evidence index and its entry point
`evidence/main.py` in full, read and not run: the sweep finding turns on
the evidence's own selection rule. Problem pages as of that time: Problem 354
(Statement, Formulation, Status, References and the Current assessment's
"Remaining gaps"), Problems 346 and 347 in full, Problem 124's Statement and
Progress, Problem 254 through its Progress section, and Problems 348 and 349
(Statement and Progress). Library as of that time: the Geneson, Fan and van
Doorn cards in full, the three Geneson result pages searched for their task
wording, the card of the Problem 346 counterexample in full, and the van Doorn
canonical conversion at its Lemma 5. Held sources, in the text layer
(`pdftotext -layout`): Fan v5 at pp. 3--4 (Theorem 1.1, the observation, the
sentence placing $M_\rho=2$ on $(1,\rho_0]$, Corollary 1.2), p. 7 (Theorem 1.5,
Lemma 2.1), pp. 16--19 (the proof of Theorem 1.1 with its lemma citations,
Proposition 4.3); Geneson at pp. 11--13 (Proposition 11, Corollary 12);
van Doorn at Lemma 4, Lemma 5 and Proposition 2; Yu and Chen at p. 1
(the history paragraph) and the reference list. No page image was
needed: no accepted finding turns on a formula the text layer misreads.
No web source was consulted. Every finding accepted below was
adjudicated by the grader against the page, the source text or an exact
recomputation, and the reviewers' derivations were followed step by step
where a finding depends on them.

**Computation.** In exact integer arithmetic, with its own script in
ignored scratch, the grader recomputed every pinned certificate of the
rational-ratio section (depth, run start and $b_n$ all reproduce), the
control pair, the thirty-two-denominator sweep under two rules (the
page's "normalized by the least $T$" and the evidence's "least $T$ with
$\lfloor2\gamma\rfloor\ge2$"), the witnesses $\gamma=1/511$, $1/257$ and
$24/7$ at ratio $3/2$, the threshold witness $\gamma=5/4$,
$\alpha=(5/4)^{21}$, and the deletion witness $(3\sqrt2,3)$ (the subset
sums of its first three layers, the mesh propagation through index $29$,
and every integer in $[6,5000)$ represented from fourteen layers); the
two Pisot roots of the Problem 349 review were recomputed in floating
point with the margins that review states. Nothing below relies on the
output of the lead's evidence.

**Independence facts, by role.** The grader is a fresh context given only
the grading assignment, distinct from the author of the page and the
leads and from each of the seven reviewers; the grader took no part in
writing any page, any report, the reconstruction pages or the leads'
evidence, and had not seen the folder before. The grader is not blind,
as a grader need not be. Each report discloses its reviewer's incidental
exposures: directory listings of `evidence/verify/` by file name; status
and label lines of problem pages printed while locating statements;
cards and result pages printed whole with their Overview, Read status,
Proof pointer and Bears-on paragraphs; the Problem 254 page's Progress
paragraph, which summarizes the reviewed section; the frontmatter
description of the normalization reconstruction's review; one line of
the Theorem 5.1 reconstruction's review; the H2 headings and Outcome
lines of other sections; and the leads' paraphrase of the Current
assessment, which was allowed reading. Materiality ruling, by the
content test: immaterial for every report. None of the exposed text
states a verdict on any statement of the page or the leads; every
finding cites the page, a source or a computation; the direction of
every attack follows the section's own sentences; and nothing in any
report could only have come from the exposed text. No reviewer read
another review of this page, the grade of the reconstruction reviews,
the leads' evidence or any web source.

## Reports graded

A report passes when it has a subject block that resolves (subject date, path,
section lines and, where named, the lead), stated independence facts and
exposures, a restatement carrying the quantifiers, an explicit verdict on
all ten items of the Erdos-specific audit checklist, weakest steps
actually re-derived rather than paraphrased, a real strongest attack, the
premises with their interfaces and reading depth, and a per-statement
verdict; it is void otherwise. All seven reports pass. Each entry records
what was checked.

1. [[research/erdos_354/evidence/verify/connections_problem_354_hegyv_ri_s_conjecture_at_a_rational__review|the rational-ratio review]]:
   **pass.** Subject resolves (section and lead); ten reconstruction
   pages and three PDFs listed with depth; three exposures; restatement
   S1--S15 carrying every quantifier of Lemma 354.1, Proposition 354.2,
   Corollary 354.3 and Lemma 354.4; ten explicit checklist verdicts, four
   of them defects tied to findings; W1--W3 re-derived (the count from a
   run of $\gamma$ to the Section 3 hypotheses with $\ell=L'+1$ and
   $K\ge K_*$, the descent chain, the two transports); a real attack on
   every statement, which produced three witnesses ($\gamma=1/511$,
   $\gamma=24/7$, the three sweep denominators) that the grader
   reproduced to the digit; premises with interfaces and depth; verdicts
   per statement. Limitation: the recomputation's code is not retained;
   its figures follow from the page's own criterion and were reproduced
   here.
2. [[research/erdos_354/evidence/verify/connections_problem_354_the_second_question_at_bases_up_to_t_review|the second-question review]]:
   **pass.** Subject resolves (section, preamble, lead); reading listed
   with depth (four reconstruction pages, Fan pp. 1--5 and 19--21,
   Geneson pp. 11--13, two cards); exposure disclosed; restatement
   S1--S12 with the thresholds, the premises (P1) and (P2) and the
   quantifier over bases; ten verdicts; three weakest steps re-derived
   (the threshold of Proposition 354.5 with its dependence on $j$, the
   $q\ge5$ step with the automorphism, the bookkeeping of (P2) including
   the closure); a real attack on each statement, with the witness
   $\gamma=5/4$, $\alpha=(5/4)^{21}$ that the grader reproduced;
   premises with interfaces; verdicts per statement.
3. [[research/erdos_354/evidence/verify/connections_problem_349_single_rays_and_the_digit_recurrence_review|the Problem 349 review]]:
   **pass.** Subject resolves; reading with depth (the Geneson and van
   Doorn text layers, Graham's page images); four exposures; restatement
   S1--S6 with the two indexing conventions; ten verdicts, three marked
   inapplicable with their reasons; W1--W3 re-derived (the base-two
   identity by induction, the scope reading with two Pisot witnesses and
   an irreducibility argument, the van Doorn analogy); a real attack per
   statement; premises with depth (Dubickas not held); verdicts, all
   refutation-failed, with four suggestions and two notes.
4. [[research/erdos_354/evidence/verify/connections_problem_348_deletion_thresholds_review|the Problem 348 review]]:
   **pass.** Subject resolves; reading with depth (Geneson pp. 1--5 in
   full); three exposures with their lines named; restatement S1--S6
   separating the one mathematical statement from the record and
   judgment sentences; ten verdicts; W1--W3 re-derived (the bridge under
   both sequence conventions, the exclusion mechanism from the source's
   Section 2, the load-bearing scope phrase with the powers-of-two
   witness); a real attack per statement; premises; verdicts per
   statement.
5. [[research/erdos_354/evidence/verify/connections_problem_254_and_the_threshold_review|the Problem 254 review]]:
   **pass.** Subject resolves; reading with depth (Fan v5 at Theorem 1.1,
   Section 2, Lemma 3.3, the proof of Theorem 1.1, Remarks 4.1--4.2 and
   Propositions 4.2--4.3; Yu--Chen p. 1); five exposures; restatement
   S1--S7 with $M_2^*$ defined in the claim's own units; ten verdicts;
   W1--W3 re-derived (from the witness to the threshold, the family with
   its two covering results, the Burr--Erdős correspondence and the
   single-ray count); a real attack with the witness $A_{2,6}$; premises
   naming the papers not held; verdicts per statement.
6. [[research/erdos_354/evidence/verify/connections_problem_124_mixed_power_sets_review|the Problem 124 review]]:
   **pass.** Subject resolves; reading with depth (Fan v5 pp. 7 and 34 as
   page images, pp. 6--10 and 34--36 in text); four exposures;
   restatement S1--S10; ten verdicts; W1--W3 re-derived, W1 by a genuine
   derivation (no tail of a base-two ray lies in a mixed power set
   without the base $2$, in the dyadic and the non-dyadic case); a real
   attack; premises; verdicts per statement.
7. [[research/erdos_354/evidence/verify/connections_no_further_consumer_review|the no-further-consumer review]]:
   **pass.** Subject resolves (section and both leads); reading with
   depth (three reconstruction pages in full, ten problem statements);
   five exposures; restatement S1--S8; ten verdicts; W1--W3 re-derived
   (the ratio pattern with its two limit points, the single-ray count
   with the sharper bound, the interface inventory of Theorem 5.1); a
   real attack with the deletion witness $(3\sqrt2,3)$ and its mesh
   argument, which the grader reproduced; premises; verdicts per
   statement.

## Corrections

Each correction was adjudicated against the page as of that time and, where a
source or a computation decides it, against the held text layer or the grader's
exact recomputation. Locations quote the page text as of that time.

**C1.** Page [[research/erdos_354/connections|connections]], section
"Problem 354: Hegyvári's conjecture at a rational ratio", "What it does
not give", the first bullet, from "The bounded-run coefficients." to
"node connection (Step 4)." Replace the bullet with:

"The short-block coefficients. Proposition 354.2 acts through a maximal
common zero run of the conversions of length at least
$\lceil\log_2K_*\rceil-1$ at an exact layer, which a run of $L(p,q)$
zeros in $\gamma$ guarantees; a coefficient with only finitely many such
runs is outside the descent. Exact layers occur exactly at the $s$ with
$\{2^s\gamma\}<1/p$, possibly nowhere ($\gamma=24/7$ at ratio $3/2$ has
none: $\delta_s$ runs through $2,1,1$), and at an exact layer a common
zero run of that length forces $\{2^s\gamma\}<2^{-\lceil\log_2K_*\rceil}$.
For a rational $\gamma$ whose denominator in lowest terms has odd part
$v$, $\{2^s\gamma\}\ge1/v$ for all large $s$, so every rational $\gamma$
with $v\le2^{\lceil\log_2K_*\rceil}$ ($v\le128$ at ratio $3/2$), in
particular every rational pair certified below, and uncountably many
irrationals are outside the descent, while $\gamma=1/511$ at ratio $3/2$
has infinitely many runs of exactly eight zeros and is covered by
Corollary 354.3. For the coefficients outside, Hegyvári's conjecture
stays open except pair by pair through Lemma 354.4, since Theorem 5.1
needs $K\ge K_*$ for its coefficient interval (Step 1) and node
connection (Step 4)."

In the third bullet replace "the exceptional set contains every pair with
rational coefficients" with "the exceptional set contains every pair with
rational coefficients whose $\gamma$ has odd denominator part at most
$2^{L(p,q)}$"; in the Outcome replace "open for the bounded-run
coefficients" with "open for the short-block coefficients". Basis:
bounded runs are not short runs. $\gamma=1/511$ is rational and not
dyadic ($511=7\cdot73$), $2^9\equiv1$ modulo $511$, so its expansion is
the block of eight zeros and a one repeated, and $L(3,2)=8$; Corollary
354.3 with $k=0$, $p/q=3/2$ makes $A_{3/511,2/511}$ strongly complete, a
pair with rational coefficients in the class the bullet calls open. The
grader recomputed the normalized pair $(3072/511,2048/511)$ ($N=4$,
$M=6$): maximal common zero runs of length $7$ start at $s=8,17,26,\ldots$,
each with $\delta_s=0$, so $\ell=8$ and $K=256\ge92$, and a Lemma 354.4
certificate exists at depth $9$ from $516$ with $b_9=2052$; likewise
$\gamma=1/257$ (period $16$) certifies as $(1536/257,1024/257)$ at depth
$5$ from $41$ with $b_5=127$. The sentence "such coefficients still have
exact layers" is false: $\gamma=24/7$ at ratio $3/2$, normalized pair
$(72/7,48/7)$, has doubling orbit $\{3/7,6/7,5/7\}$ of its fractional
part, all at least $1/3$, and $\delta_s=2a_s-3b_s$ takes the values
$2,1,1$ periodically. The bounds in the replacement: at an exact layer
$\{2^s\alpha\}=p\{2^s\gamma\}$, so a common zero run of length
$\lceil\log_2K_*\rceil-1$ gives $p\{2^s\gamma\}<2^{1-\lceil\log_2K_*\rceil}$
and, as $p\ge3$, $\{2^s\gamma\}<2^{-\lceil\log_2K_*\rceil}$; for $s$ past
the $2$-adic part of the denominator $\{2^s\gamma\}$ is a nonzero
multiple of $1/v$; a run of $L$ zeros needs $v>2^L$, so odd part at most
$2^{L(p,q)}$ puts $\gamma$ in the corollary's exceptional set. The
certified rational pairs have odd parts $5$, $7$, $9$ and the sweep's
$d\le99$. From F1 and F2 of the rational-ratio review, required,
accepted.

**C2.** Lead
[[research/leads/rational_ratio_dyadic_floor_descent/_index|rational_ratio_dyadic_floor_descent]],
frontmatter `desc`, "and the bounded-run coefficients as the remaining
gap in Hegyvári's conjecture": replace with "and the coefficients with
only short common zero runs as the remaining gap in Hegyvári's
conjecture". Section "The consequential gap", the first two sentences
through "too short for Theorem 5.1, and": replace with "Coefficients
$\gamma$ with only finitely many maximal common zero runs of length
$\lceil\log_2K_*\rceil-1$ at exact layers: every rational $\gamma$ whose
denominator has odd part at most $2^{\lceil\log_2K_*\rceil}$ ($128$ at
ratio $3/2$), in particular every rational pair certified by the
evidence, and uncountably many irrationals, while $\gamma=1/511$ at ratio
$3/2$, with infinitely many runs of eight zeros, is covered by Corollary
354.3. For them exact layers occur only at the $s$ with
$\{2^s\gamma\}<1/p$, possibly nowhere, and the common zero runs after
them are too short for Theorem 5.1, and". Basis: as for C1; the lead
restates the refuted bullet. From F1 and F2 of the rational-ratio review,
required, accepted.

**C3.** Page [[research/erdos_354/connections|connections]], same
section, the sentence after Lemma 354.4 listing the certificates, its
last clause "and every pair $(3\gamma,2\gamma)$ with $\gamma=2^T/d$ for
the thirty-two odd denominators $5\le d\le99$ not divisible by $3$,
normalized by the least $T$, by depth $9$." Replace with "and every pair
$(3\gamma,2\gamma)$ with $\gamma=2^T/d$ for the thirty-two odd
denominators $5\le d\le99$ not divisible by $3$, normalized by the least
$T$, by depth $12$: twenty-nine of them by depth $9$, and $d=23$, $89$
and $91$, the pairs $(192/23,128/23)$, $(768/89,512/89)$ and
$(768/91,512/91)$, at depths $10$, $12$ and $11$, from $2139$, $11036$
and $4323$ with $b_{10}=5698$, $b_{12}=23563$ and $b_{11}=11522$." The
lead's evidence entry point,
`wiki/research/leads/rational_ratio_dyadic_floor_descent/evidence/main.py`,
function `check_sweep`, must then select the least $T$ for which the pair
is normalized,
$2\le\lfloor2\gamma\rfloor<\lfloor3\gamma\rfloor<2\lfloor2\gamma\rfloor$,
in place of the least $T$ with $\lfloor2\gamma\rfloor\ge2$, and its check
"greatest depth needed is 9" becomes "greatest depth needed is 12"; the
evidence index's clause "normalized by the least $T$" then describes the
run. Basis: under the page's own definition of a normalized pair
($N\ge2$, $N<M<2N$) the least $T$ is $6$ for $d=23$ ($T=5$ gives $N=2$,
$M=4=2N$) and $8$ for $d=89$ and $d=91$; the grader's recomputation,
independent of the reviewer's, finds at depth $9$ the longest runs
$2826$ from $2139$ against $b_9=2849$, $22$ against $b_9=2945$ and $22$
against $b_9=2880$, and the first certificates at the depths and starts
above; the other twenty-nine certify by depth $9$, the deepest ($d=11$
and $d=73$) at $9$. The evidence's rule differs from the normalized rule
for the seven denominators $d=11,23,43,47,89,91,95$, where it gives
$\lfloor2\gamma\rfloor=2$ and $\lfloor3\gamma\rfloor=4=2\lfloor2\gamma\rfloor$,
a pair outside the precondition its own docstring states; there its
certificate is found at depth $2$ for the set with the two extra
elements $2$ and $4$, a superset of the normalized pair's set, and its
check "greatest depth needed is 9" passes on $d=73$. The page's sentence
is false under the page's definition and does not describe what the
evidence computes; the reading that keeps the page's mathematics (Lemma
354.4 is stated for normalized pairs) is adopted, and the evidence must
follow it. From F3 of the rational-ratio review, required, accepted.

**C4.** Lead
[[research/leads/rational_ratio_dyadic_floor_descent/_index|rational_ratio_dyadic_floor_descent]],
"Provisional premises", "the manuscript is unrefereed and the
reconstruction of that page is not among the filed reviews." Replace with
"the manuscript is unrefereed; the reconstruction of that page has a
filed focused review in the folder's evidence, graded faithful and sound
with one correction and assigning no tier." Basis: as of that time the folder's
`evidence/verify/` holds
[[research/erdos_354/evidence/verify/yu_chen_theorem_5_1_reconstruction_review|the Theorem 5.1 reconstruction review]],
and [[research/erdos_354/evidence/verify/grade|the reconstruction grade]]
records it as pass with fidelity faithful and the argument sound with
its correction C6. A sentence characterizing the filed reviews is a
claim, and this one is false as of that time. From F4 of the rational-ratio
review, filed as suggested because the reviewer could not read the reviews;
accepted by the grader, who read the grade.

**C5.** Page [[research/erdos_354/connections|connections]], section
"Problem 354: the second question at bases up to the plastic number",
proof of Proposition 354.5, "so for $k\ge m_0$ the $\alpha$-ray has
exactly one term in $I_k$, namely $\lfloor\alpha^*\gamma^k\rfloor$".
Replace with "so for $k\ge\max(m_0,j)$ the $\alpha$-ray has exactly one
term in $I_k$, namely $\lfloor\alpha^*\gamma^k\rfloor$". Basis: the term
of index $k-j$ exists only for $k\ge j$, and $m_0$ is chosen without
reference to $j$. Witness, recomputed exactly by the grader: $\gamma=5/4$,
$\alpha=(5/4)^{21}$ give $j=20$, $\alpha^*=5/4$; the least admissible
$m_0$ is $6$ (the inequality fails at $m=5$, $3.81\ldots<4$, holds at
$m=6$, $4.76\ldots\ge4$, and for $m\ge7$ because $(1/4)(5/4)^m\ge1$);
the ray's least term is $108>\gamma^{20}=86.7\ldots$, so the ray has no
term in $I_k$ for $6\le k\le19$. The statement is unaffected: with the
threshold $\max(m_0,j)$ for each ray the proof closes as written. From
F1 of the second-question review, filed as suggested; accepted because
the displayed sentence is false at values inside its stated range.

**C6.** Same page, same section, "Next investigation", "gives an
incomplete single ray at a rational base below the golden ratio, which
is new for [[problems/additive_bases/E0349/_index|Problem 349]] and closes this
route at that base." Replace with "gives an incomplete single ray at a
rational base below the golden ratio (the ray of the coefficient
$t\gamma^{n_0}$, every term of which is divisible by $q$), which is new
for [[problems/additive_bases/E0349/_index|Problem 349]] and closes the
single-ray sufficient condition at that base; premise (P2) for the
irrational-ratio pairs then needs a direct argument, or a second bad
coefficient with irrational ratio to the first, which would give an
incomplete pair as Proposition 354.7 does." Lead
small_base_two_ray_distance_divergence,
"Next step", "gives an incomplete single ray at a rational base below
the golden ratio, new for [[problems/additive_bases/E0349/_index|Problem 349]],
and closes the route at that base." Replace with "gives an incomplete
single ray at a rational base below the golden ratio (the ray of the
coefficient $t\gamma^{n_0}$, every term of which is divisible by $q$),
new for [[problems/additive_bases/E0349/_index|Problem 349]], and closes the
single-ray sufficient condition at that base, leaving (P2) for the
irrational-ratio pairs to a direct argument or to a second bad
coefficient with irrational ratio to the first." Basis: (P2) concerns
the two-ray set, and a set of nonnegative terms fails (1.5) at $\theta$
exactly when both rays have convergent distance sums at $\theta$. A
coefficient $t$ with all late terms divisible by $q$ makes the sum of
$S(t)$ at $\theta=1/q$ finite, but the pair $(t,\beta)$ fails (1.5) at
$1/q$ only if $S(\beta)$ also has all but finitely many terms divisible
by $q$, and neither page produces such a $\beta$ with $\beta/t$
irrational: at a rational base the Corollary 12 device $\beta=t(1+\gamma)$
has rational ratio and $\gamma^{\mathbb Z}\subseteq\mathbb Q$. So the
negative outcome closes the sufficient condition "every single ray
satisfies (1.5)" and not deduction 354.6, and no argument either way is
available. The ray of the coefficient $t$ itself need not be incomplete,
since its early terms may supply the residues its late terms lack (base
$2$, $t=1$: every later term even, the ray complete); the ray of
$t\gamma^{n_0}$ is incomplete. From F2 (required) and F3 (suggested) of
the second-question review; accepted, F3 folded into the same sentence.

**C7.** Same page, same section, "What it does not give", second
bullet, "and the problem's multiset has every value twice". Replace with
"and the problem's multiset has every sufficiently large value twice".
Basis: for $\alpha=\beta\gamma^k$ with $k\ne0$ the $|k|$ initial values
of the longer ray occur once. From F7 of the second-question review,
filed as a note; accepted because the clause is false at a case inside
the bullet's range.

**C8.** Same page, section "Problem 348: deletion thresholds", "Next
investigation", "A reconstruction of Geneson's Sections 2--4 is the
separate compilation task the card records as pending." Replace with "A
reconstruction of Geneson's Sections 2--4 would be a separate compilation
task; the card records that this proof was read for structure only."
Basis: the Geneson card's read-status paragraph records that the proof of
Theorem 1 (Sections 2--4, pp. 3--11) "was read for structure only";
neither the card nor its three result pages record a reconstruction or
compilation task, and the word "pending" occurs there only in the result
pages' sentences that a separate triage of a problem page is pending
(grader's search of the four pages as of that time). From F1 of the Problem 348
review, required, accepted.

**C9.** Same page, section "Problem 254 and the threshold $M_2^*$", "Next
investigation", "every incomplete two-ray set known (Hegyvári 1989,
Jiang--Ma, Fang--He, all site-attested) having a ratio that is a power of
$2$ and hence a single ray as a set." Replace with "every incomplete
two-ray set known with one coefficient not a dyadic rational (Hegyvári
1989, Jiang--Ma, Fang--He, all site-attested) having a ratio that is a
power of $2$ and hence a single ray as a set, while a pair of dyadic
rationals fails (1.5)." Basis: $A_{2,6}=\{2^{n+1}\}\cup\{3\cdot2^{n+1}\}$
has ratio $1/3$, not a power of $2$, and every element even, so it is an
incomplete two-ray set, and trivially a known one; the universal clause
is false as written. Its purpose survives with the hypothesis: the
site-attested incomplete sets with a non-dyadic coefficient all have a
power-of-two ratio, and a pair of dyadic rationals has all but finitely
many elements divisible by a fixed power of $2$, so its distance sum at
$\theta=2^{-c}$ is finite for $c$ large and it is no candidate for the
question. From F3 of the Problem 254 review, required, accepted.

**C10.** Same page, same section, "Next investigation", "a
reconstruction of Fan's Theorem 2.2 and Section 4, which would also fix
the standing of premise (P1) above". Replace with "a reconstruction of
Fan's Theorem 2.2 with Sections 3--4, which would also fix the standing
of premise (P1) above". Basis: in Fan v5 the proof of Theorem 1.1
(Section 4, pp. 16--19) invokes Lemma 3.1 twice, Lemma 3.2 three times
and Lemma 3.3 once before "Invoking Theorem 2.2 and (1.2) completes the
proof of the base case"; the grader located each citation in the text
layer. The page's own deduction 354.6 describes the proof of (P1) as
Sections 2--4 of the source. From F2 of the Problem 254 review, filed as
suggested; accepted because the sentence, read as a description of what
would fix (P1), is false.

**C11.** Same page, section "Problem 124: mixed power sets", Target
paragraph, "the Fan card records Theorem 1.5 at statement level:
$\bigcup_{d\in D}\{d^n\}$ is strongly complete when $D=D_1\cup D_2\cup C$
with $\gcd(C)=1$ and $\sum_{d\in D_i}1/(d-1)\ge1$ for $i=1,2$, one
component fewer than Bergelson--Simmons." Replace with "the Fan card
records Theorem 1.5 (v5, p. 7) at statement level only; the theorem says
that for a nonempty finite $D\subseteq\mathbb N_{\ge2}$ with no two
elements powers of the same integer, $\bigcup_{d\in D}\{d^n\}$ is
strongly complete whenever $D=D_1\cup D_2\cup C$ is a partition into
nonempty parts with $\gcd(C)=1$ and $\sum_{d\in D_i}1/(d-1)\ge1$ for
$i=1,2$, one component fewer than the Bergelson--Simmons theorem as the
source states it." Basis: Fan v5 p. 7, text layer: "Let
$D\subseteq\mathbb N_{\ge2}$ be a nonempty finite subset with no two
elements being powers of the same integer. Suppose that
$D=D_1\cup D_2\cup C$ is a partition of $D$ into nonempty subsets such
that $\gcd(C)=1$ and (1.13) for every $i=1,2$. Then $P(D)$ is strongly
complete."; Section 7 (p. 34) uses finiteness in its bound on
$b-\sum_{b'<b}b'$ and the no-common-power hypothesis to make
$P_k(D)=\mathcal B_1\cup\mathcal B_2\cup\mathcal C$ a partition. The Fan
card's only mention is "Theorem 1.5, mixed power sets; all at statement
level only here". From F3 of the Problem 124 review, required, accepted.

**C12.** Same page, section "No further consumer", "and the two-ray sets
are not examples for Problem 346 or 347, since their sorted terms have
ratios alternating near $\alpha/\beta$ and $2\beta/\alpha$, while a
single ray,". Replace with "and the two-ray sets are not examples for
Problem 347, since their sorted terms have ratios alternating near
$\alpha/\beta$ and $2\beta/\alpha$ and so do not tend to $2$; for
Problem 346, refuted by a counterexample, the ratios decide nothing,
since its hypotheses ask that completeness be lost under every infinite
deletion, which the descent does not address and which fails for the
pair $(3\sqrt2,3)$ after the deletion of $\{3\cdot2^m:m\ge4,\ 4\mid m\}$;
a single ray,". Basis: Problem 346 asks whether its hypotheses (complete
after every finite deletion, incomplete after every infinite deletion,
ratios at least $1+\varepsilon$) force the ratio to tend to the golden
ratio; the ratio pattern of a two-ray set (limit points $\theta$ and
$2/\theta$, both in $(1,2)$) shows only that such a set would violate
the questioned conclusion, so it cannot exclude the set from the
hypotheses, and had a two-ray set satisfied them it would be a further
counterexample. The corpus records the problem as solved by the
counterexample of the held card (a sequence with ratio floor $6/5$ and
two subsequential ratio limits), so no consumer is needed. The witness,
re-derived by the grader: $(3\sqrt2,3)$ is normalized ($N=3$, $M=4$),
its ratio $\sqrt2$ is irrational, the subset sums of its first three
layers $\{3,4,6,8,12,16\}$ cover $[6,43]$, and adding the retained
weights of index at least $3$ in increasing order keeps a full interval
whose span exceeds the next retained weight at every step (the
reviewer's inequalities $s_m\ge b_m$ and $s_m\ge a_m$ hold as derived;
the propagation was checked through index $29$ and every integer in
$[6,5000)$ is represented from fourteen layers), so
$A_{3\sqrt2,3}\setminus B$ is complete and the pair fails the deletion
hypothesis for a reason unrelated to its ratios. From F1 of the
no-further-consumer review, required, accepted.

C1, C2, C7, C9, C12 and the closure clause of C6 repair sentences that
are false or unsupported as written; C3, C4, C8, C10 and C11 correct the
pages' account of the evidence, the filed reviews and the sources; C5
repairs a false intermediate sentence in a proof whose statement stands.
No correction changes a transported result: Lemma 354.1, Proposition
354.2, Corollary 354.3, Lemma 354.4, Proposition 354.5, deduction 354.6
and Proposition 354.7 keep their statements.

## Rejected and downgraded findings

Every finding not listed under Corrections is recorded here with its
disposition. "Downgraded" means the finding is right as an observation
but does not require a change; "rejected as a correction" means the
proposed change cannot be adopted.

**The rational-ratio review.** F5 (the wording "not contradictory by
itself"; the quantifier on membership in $\mathcal C_k$): downgraded; in
its paragraph the first sentence reads as a statement about the
reconstructed argument, and the quantifier is stated two sentences
earlier ("as soon as $k$ is at least the number of ones"). F6 ("every
non-dyadic normalized pair"; the period of the conversions): downgraded;
Lemma 354.1 states its hypothesis precisely and the Outcome's shorthand
is read against it; the order of $2$ modulo $v$ is a period and no
minimality is claimed. F7 (the multiset-to-set bridge in the Target
paragraph): downgraded, and resolved by the grader: the site-accepted
theorem applies to every pair with irrational ratio, hence to
$(2^K\alpha,2^K\beta)$ for every $K$; the two rays share only finitely
many values (Step 1 of the Remark 4.2 page), so for $K$ large the tail
multiset has distinct values and its completeness is completeness of a
subset of $A_{\alpha,\beta}$; the case split stands, and the problem
page's remaining gap (5) says what the paragraph attributes to it. F8
(the attribution and normalization of $(5/2,5)$): downgraded; the
multiset is incomplete for the reason the review gives, the problem
page's site commentary attributes the incompleteness of $\beta=2^k\alpha$
with $\alpha\ge2$ to Hegyvári 1989, and the page presents the pair as a
control that "must not" certify, which is all the evidence checks.

**The second-question review.** F4 (the lead's "any proof"): downgraded;
the sentence's "so" ties "any proof" to the strong completeness its
antecedent names, and the section states the precise form; the author
may add "of strong completeness". F5 (the object of the positive
outcome): downgraded; the sentence's object is (1.5), "beginning with
rational $\theta$" names a starting point, and the preceding bullet says
that (1.5) at irrational $\theta$ is a further condition. F6 (the Pisot
alternative is vacuous on $(1,2)$): downgraded; verified by the grader (a
reciprocal irreducible polynomial pairs each conjugate with its inverse,
so a Pisot number with one has degree $2$, minimal polynomial $x^2-ax+1$
with $a\ge3$ and value at least $(3+\sqrt5)/2$); a vacuous alternative in
a hypothesis is not an error. F8 (novelty for Problem 349; "no held
source"; the description of the Current assessment; "marks the bases
where (P2) fails"; "every set with two elements"): downgraded; the grader
read the Problem 354 page's Status paragraph, which records Corollary 12
for the every-base reading and the $\sqrt\varphi$ Lean candidate for the
some-base reading as both pages say; "marks the bases" reads as "marks
bases", and "every set with two elements" is Theorem 1.1's "at least
two" as the proof applies it.

**The Problem 349 review.** F1 (the range of $k$ in Proposition 2):
downgraded; the page states the necessary direction only ("only
$t=2^{-k}$ gives"), true for every range of $k$, and van Doorn's
Proposition 2 reads "if and only if $t=1/2^k$ for some $k\ge1$" in his
indexing from $n=1$ (text layer). F2 ("the certificate" among the objects
lost at a non-integer base): rejected as a correction; the list names
Theorem 5.1's objects (the exact doubling blocks, the coefficient
interval $d\{px+qy\}$, the finite node-connection certificate, the
modular invariant), which the digit recurrence supplies, not the mesh
certificate of Lemma 354.4, whose single-ray form the page names in its
next sentence. F3 ("which the corpus already records"): downgraded; no
card or result page records van Doorn's Lemma 5 (the card's list of
results to transcribe omits it), but the held preprint and its canonical
conversion beside the card carry it; the author may write "held in the
preprint, not transcribed on its card". F4 (the hedge "if any besides
Geneson's exists"): downgraded; the sentence is a true conditional and a
witness is an addition; the grader recomputed the two roots ($1.534158$
with the other roots of modulus at most $0.951$; $1.590005$ with at most
$0.977$). F5 (the coefficient shift): downgraded; carried by C6. F6
($a_0\ge1$): downgraded; the set convention discards zero terms.

**The Problem 348 review.** F2 (name the irrational-ratio hypothesis):
downgraded; "of its theorem" carries it, as the review's own W3 shows.
F3 (the card's read status): downgraded; the card records the statement
read clause by clause and the proof for structure only, and the page's
compression changes no standing. F4 (Theorem 2 named as part of the
incompleteness mechanism): downgraded; Lemma 4 is the engine and Theorem
2 its input, as the review derives, and the parenthetical names the
source's objects correctly.

**The Problem 254 review.** F1 (the unconditional "$M_2^*$ lies in
$\{2,3,4,5\}$"): downgraded; the same paragraph attributes the upper
bound to Corollary 1.2 and the Target says the proof of Theorem 1.1 is
unread; the author may add "on the preprint's Corollary 1.2". F4 (the
attribution to Hegyvári 1989): downgraded; the held Yu--Chen manuscript
credits the power-of-two incompleteness results to Jiang--Ma and
Fang--He, while the problem page's site commentary, which the parenthesis
paraphrases, credits the case $\alpha\ge2$, $\beta=2^k\alpha$ to Hegyvári
1989; the paper is not held and "site-attested" says so. F5 ("each
rational-ratio line"): downgraded; read within the family the sentence
names. F6 (no corpus proof of the Burr--Erdős lemma): downgraded; a
limit of the check, not a defect.

**The Problem 124 review.** F1 (the problem page's typed condition):
downgraded as a correction to the connections page, which states the
source's condition (1.12) correctly; the problem page
`wiki/problems/diophantine_problems/E0124/_index.md` types the denominator as
$d_r-1$, a condition no admissible tuple meets, and is flagged to its
owner for a check against the site's statement (outside this grade's
subject; not edited here). F2 ("coprime"; the quantifier over $k$):
downgraded; $\gcd(d_1,\ldots,d_r)=1$ is the reading of "coprime" for a
tuple, and the omitted quantifier belongs to the problem's second
question, which the section only names. F4 (a second shared step):
downgraded; the sentence's operative content, a resemblance of tools and
not a transfer, is right, and the second resemblance is of the same
kind. F5 (whose statement of Bergelson--Simmons): downgraded; C11 adds
"as the source states it".

**The no-further-consumer review.** F2 (the displayed single-ray bound):
downgraded; the inequality $a_n\ge\lfloor\alpha\rfloor2^n$ is true, the
exclusion of single rays is carried in the same sentence by the
resolution of both problems, and the sharper bound $a_n>2^n\alpha-1$ the
review derives is available to the author. F3 ("the reusable content of
the folder is a descent"): downgraded; the search terms cover the other
mechanisms, as the review says. F4 ("every later layer"): downgraded;
the Theorem 5.1 page's statement ($t\ge n+\ell+3$) is what the summary
compresses. F5 ("no research lead outside this folder"): downgraded;
"no lead other than the two named" is the only reading the sentence
supports.

**Observations outside the reports' read sets.** (a) The sentences
recording that the pages of Problems 349, 348, 254 and 124 carry
"progress not compiled" are stale as of that time: each of those pages' Progress
sections holds, since the same change, a note derived from this page and nothing
else; the author may write "with no progress recorded beyond this folder's
note". No correction is numbered for it, since no report found it. (b) The
Problem 124 page's typed condition, see F1 of the Problem 124 review above.

## Graded verdicts

Verdicts are per statement in the numbering of each review, grouped by
section. "Refutation-failed" and "refuted-as-stated" are written in full.

**Problem 354: Hegyvári's conjecture at a rational ratio.** S1 (target
and reduction): refutation-failed, the case split confirmed by the grader.
S2 (the inventory of irrationality): refutation-failed. S3 (Lemma 354.1):
refutation-failed. S4 (Proposition 354.2): refutation-failed. S5
(Corollary 354.3): refutation-failed. S6 (the constants):
refutation-failed. S7 (Lemma 354.4): refutation-failed. S8 (the pinned
certificates and controls): refutation-failed, reproduced by the grader.
S9 (the sweep sentence): refuted-as-stated (C3). S10 (obstruction 1):
refuted-as-stated (C1); the obstruction stands in its corrected form.
S11 (obstruction 2): refutation-failed. S12 (obstruction 3): the
rational-coefficients clause refuted-as-stated (C1); the uniformity and
dichotomy clauses refutation-failed. S13 (next investigation): not a
claim. S14 (outcome): refutation-failed for the transfer list, with the
wording of C1. S15 (the lead): the route summary refutation-failed; the
consequential-gap paragraph refuted-as-stated (C2); the premise sentence
refuted-as-stated as a record claim (C4).

**Problem 354: the second question at bases up to the plastic number.**
S1 (the index bridge): refutation-failed. S2 (the constants; $M_\rho=2$
on $(1,\rho_0]$): refutation-failed; the theorem it feeds is (P1), a
preprint statement. S3 (Proposition 354.5): refutation-failed, its proof
corrected by C5. S4 (deduction 354.6): refutation-failed as a conditional
on (P1) and (P2), which remain unproved. S5 (the addenda):
refutation-failed. S6 (Proposition 354.7): refutation-failed, resting on
Proposition 11 and through it on Dubickas's theorem as quoted. S7 (the
bases where (P2) fails; the every-base reading): refutation-failed. S8
(the first bullet): refutation-failed for its equivalences; the Mahler
comparison and the coverage remark are not adjudicated. S9 (the
exceptional pairs): refutation-failed with C7. S10 (redundancy):
refutation-failed. S11(a), S11(b): refutation-failed. S11(c): "gives an
incomplete single ray at that base" refutation-failed for the shifted
coefficient (C6); "closes this route at that base", on both pages: proof
defective; statement unresolved (C6). S12 (the lead): refutation-failed
for its restatements; its Next step carries C6.

**Problem 349: single rays and the digit recurrence.** S1--S6:
refutation-failed.

**Problem 348: deletion thresholds.** S1, S2(b), S3a, S3b, S3c, S4:
refutation-failed. S5(b): refuted-as-stated (C8). S5(a), S6: judgments,
consistent with what was read. S2(a), S2(c): not adjudicated by the
review; the status clause confirmed by the grader, the progress clause
stale (observation (a) above).

**Problem 254 and the threshold $M_2^*$.** S1: not a claim, faithful.
S2: refutation-failed, the upper bound being the preprint's Corollary
1.2. S3, S4, S5: refutation-failed. S6(b): refutation-failed. S6(c):
refuted-as-stated in its literal universal reading (C9). S6(a):
refuted-as-stated as a description of what would fix (P1) (C10). S7:
refutation-failed.

**Problem 124: mixed power sets.** S1: refutation-failed, with the flag
on the problem page. S2: refutation-failed for the status; the progress
clause stale (observation (a)). S3: refuted-as-stated (C11). S4: not
examined by the review. S5--S10: refutation-failed.

**No further consumer.** S1: refutation-failed. S2: not a claim. S3:
refutation-failed for the descriptors; the status words for Problems 346
(solved) and 347 (proved) confirmed by the grader. S4: refutation-failed.
S5 (two-ray sets and Problem 346): proof defective; statement unresolved
(C12). S6: refutation-failed. S7: refutation-failed. S8: not a claim.

**Lead outcomes.**

- [[research/leads/rational_ratio_dyadic_floor_descent/_index|rational_ratio_dyadic_floor_descent]]:
  **needs_update.** The four statements its route rests on, Lemma 354.1,
  Proposition 354.2, Corollary 354.3 and Lemma 354.4, are
  refutation-failed and the pinned certificates reproduce; but the lead's
  consequential-gap paragraph and its `desc` are refuted-as-stated (C2),
  its provisional-premise sentence is a false record claim (C4), and the
  sweep sentence it relies on and its evidence's sweep rule are wrong
  (C3). After C2, C3 and C4 the route rests only on refutation-failed
  statements.
- small_base_two_ray_distance_divergence:
  **needs_update.** Proposition 354.5, deduction 354.6 as a conditional
  on (P1) and (P2), and Proposition 354.7 are refutation-failed, the
  proof of 354.5 taking C5 on the connections page; the closure clause of
  the lead's Next step is proof defective; statement unresolved (C6), so
  the lead overstates what a negative outcome would establish. After C6
  the route rests only on refutation-failed statements.

No tier is assigned and no status changes.
