---
name: research/erdos_1221/evidence/verify/connections_grade
title: "Distinct grade of the Problem 1221 connections reviews"
desc: |
  Distinct grade of the four independent focused reviews of the Problem
  1221 connections page and its lead as they stood on 2026-09-28T13:50:48Z: all
  four reports pass, eight corrections are accepted, the remaining findings are
  downgraded to optional or rejected, and the lead's route is reviewed. No tier
  is assigned and no status changes.
created: 2026-09-28T19:37:42Z
updated: 2026-09-28T19:37:42Z
---

***

## Subject

**Frozen subject.** The repository as it stood on 2026-09-28T13:50:48Z. The page
[[research/erdos_1221/connections|research/erdos_1221/connections]], read whole
from the committed text of that state (587 lines; its four H2 sections open at
lines 45, 195, 333 and 519, as the reports state), and the lead
[[research/leads/consecutive_gap_bounds_coincident_points/_index|consecutive_gap_bounds_coincident_points]],
read whole in the same state. The worktree's copies of both equaled the frozen
text.

**Reports.** The four focused reviews of the page's sections, each read
whole:
[[research/erdos_1221/evidence/verify/connections_problem_255_the_1949_implication_toward_the_disc_review|connections_problem_255_the_1949_implication_toward_the_disc_review]]
(lines 45--194),
[[research/erdos_1221/evidence/verify/connections_problem_480_the_clustering_constant_and_the_sect_review|connections_problem_480_the_clustering_constant_and_the_sect_review]]
(lines 195--332),
[[research/erdos_1221/evidence/verify/connections_problem_1221_itself_the_site_s_family_against_se_review|connections_problem_1221_itself_the_site_s_family_against_se_review]]
(lines 333--518 and the lead) and
[[research/erdos_1221/evidence/verify/connections_the_span_to_count_transfer_has_no_second_consume_review|connections_the_span_to_count_transfer_has_no_second_consume_review]]
(lines 519--587).

**Rules read.** `docs/verification.md`, the sections "Independence and the
assignment", "Exact subjects and durable evidence", "Report contract",
"Grading and claim standing", "Whole-claim report" and "Audit checklist"
(the shared list of canonical failure modes and the ten Erdos items).

**Reading depth for adjudication.** In the same state:
[[research/erdos_1221/ko26b_lemma_4_2_reconstruction|the Lemma 4.2 page]]
whole (the statement of Theorem 4.1 as used, the role of $\delta$ and of
the translated $L$-span arc);
[[research/erdos_1221/ko26b_proposition_3_1_reconstruction|the Proposition 3.1 page]]
and
[[research/erdos_1221/ko26b_proposition_6_4_reconstruction|the Proposition 6.4 page]]
through their statements and the openings of their proofs (the ranges
$r\ge C_0A$ and $r\ge C_2A$);
[[research/erdos_1221/ko26b_theorem_1_1_reconstruction|the Theorem 1.1 page]],
statement and Section 5 proof (the comparison of
$\frac3{100}\log r+O(1)$ with $\frac1{32}\log r-O(\log\log r)$ and the
absolute threshold); the library page
[[../library/analysis/debruijn_erdos_1949_sequences_points_circle/section_2_r_equals_1|Section 2]]
whole; the contents list of
[[../library/number_theory/chung_1984_irregularities_distribution/_index|the chapter's card]];
[[problems/discrepancy/E0255/_index|Problem 255]] whole. Held sources: the 1949
note, image-only, PDF p. 2 (printed p. 14) rendered and read for Section
1, the remark naming the 1945 theorem and the opening of Section 2; the
1984 chapter, image-only, PDF p. 2 (printed p. 182) rendered and read for
the sentence on consecutive terms, the definition of $C$ and Theorem 1;
the Schmidt 1972 part VI PDF, text layer, p. 63, for the statement
attributed to van Aardenne-Ehrenfest. The two witnesses on which the
required findings rest were recomputed by the grader in a scratch script
(the first $n$ terms of $\{\log_2(2k-1)\}$ and their smallest gap for
$n\le100$; the span sums and the counting error of the Section 2 sequence
at $r=40$ and $n=2^{14}$, $2^{16}$); the derivations below are analytic
and the script is not retained.

**Independence.** The grader is a role distinct from the author of the
page and the lead and from each of the four reviewers: a fresh context
given only the grading assignment, taking no part in writing any page,
lead, reconstruction or report, with no contact with their authors and
with no other review of the page read. The worktree's status listing
names untracked review files of two other folders; none was opened. No
web search was made.

**Ruling on disclosed exposures.** Each report discloses over-wide reads:
the Problem 255 page's Current assessment and Progress paragraphs (the
latter summarizes the transfer under review); the Problem 480 page's
Formulation paragraph and a status fragment, one card line naming
Proposition 480.1, and the Standing, Read status and Read depth
paragraphs of the pages and cards read; the library cards' read-status
and relation paragraphs; the Problem 998 page's status paragraph and the
cards' standing sentences. Ruling by the content test: immaterial in
every case. Nothing in any report could only have come from that text:
every finding is a derivation from the frozen section or a comparison
with a held artifact; the attack directions (extreme configurations for
Proposition 255.1, the computation at $n=3$, the subtraction of $B$
inside the logarithm, the Section 2 sequence with $A=r-1$) follow from
the mathematics and not from any summary; no reviewer received a verdict
on its subject; and the Progress paragraph of Problem 255 repeats the
section's own claims and adds none. The reviews stand as independent.

## Reports graded

Each report is graded as a focused review record; none carries a tier. A
pass means the contract parts are present and real, not that every
finding is right; findings are adjudicated below.

- **connections_problem_255_the_1949_implication_toward_the_disc_review:
  pass.** Subject block resolving to lines 45--194; independence facts and
  one disclosed exposure; twelve restated statements with their
  quantifiers and the mean-normalized convention; ten explicit checklist
  verdicts; three weakest steps re-derived (the two counts inside a span
  with coincident entries and the zero-length and whole-circle cases, the
  ratio bound with the finite range $r<K$ closed by the Section 2
  sequence, the interval-circle passage); a real strongest attack per
  statement, including the check from the other side that each imported
  input of the 2026 route implies the 1945 theorem outright; premises with
  interfaces and reading depth; a per-statement verdict. F1 is accepted as
  C1 and F3 as C2.
- **connections_problem_480_the_clustering_constant_and_the_sect_review:
  pass.** Subject block resolving to lines 195--332 with sub-ranges; four
  disclosed exposures; twelve restated statements; ten checklist verdicts;
  three weakest steps re-derived, the first a successful attack with an
  exact witness at $n=3$ and a sandwich that saves the limit, the second
  the multiplicity identity, the third a scaled embedding that transfers
  the limit bound from (4.3); a strongest attack per statement; premises
  with page-image reading depth; a per-statement verdict. F1 is accepted
  as C4 and F3 as C3. One slip that changes nothing: the S8 attack writes
  the index shift for one prepended term as $x^*_{m+n-2}-x^*_{m-2}$ where
  $x^*_{m+n-1}-x^*_{m-1}$ is meant.
- **connections_problem_1221_itself_the_site_s_family_against_se_review:
  pass.** Subject block resolving to lines 333--518 and the whole lead;
  three disclosed exposures; nine restated statements with the multiset
  model and the convention $M/0=+\infty$; ten checklist verdicts; three
  weakest steps re-derived (the prefix identity and two-arc bound, the
  perturbation bridge, the note's chain and the two tie-break-sensitive
  identities with zero gaps); a strongest attack per statement, including
  the attempt to make the subtraction of $B$ inside the logarithm matter;
  premises with interfaces and depth; a per-statement verdict. F1 is
  accepted as C5 and C6 and F2 as C7.
- **connections_the_span_to_count_transfer_has_no_second_consume_review:
  pass.** Subject block resolving to lines 519--587; three disclosed
  exposures; fourteen restated statements; ten checklist verdicts; three
  weakest steps re-derived (the three range conditions inside the proof of
  Proposition 3.1, the single-set configuration that defeats one-time span
  control, the single-scale derivation of Theorem 2 from Theorem 3); a
  strongest attack that succeeded against S2 with an exact witness,
  recomputed here; premises with interfaces and depth; a per-statement
  verdict. F1 is accepted as C8.

## Corrections

Each correction is confined to the page named, outside any `statement:`
field (neither page carries one); the location is quoted from the frozen
text.

**C1.** [[research/erdos_1221/connections|connections]], section
"Problem 255", bullet "No rate, in either direction" (lines 136--143).
Verified: with $K(n)=\lceil\log n\rceil$ and $r=1$ the stage-$n$ upper
bound reads $nM_n^1(a)\le\log n+1$, a real constraint on the largest gap
at every stage, so the clause "which say nothing once $K(n)>r$" is false
for the upper bound (it is right for the lower bound, whose right side is
negative once $K(n)>r+1$); and the unqualified "nor feeds the conjecture"
contradicts the section's own reverse edge, where the claimed resolution
consumes a discrepancy lower bound that grows with the list length. Exact
change: replace "which say nothing once $K(n)>r$; the constants
$\Lambda_r,\lambda_r,\mu_r$ are limits in $n$ at fixed $r$, so a growth
rate of the discrepancy in $n$ neither follows from nor feeds the
conjecture." by "which bound nothing in the limit because $K(n)\to\infty$:
the constants $\Lambda_r,\lambda_r,\mu_r$ are limits in $n$ at fixed $r$,
so through Proposition 255.1 a growth rate of the discrepancy in $n$
neither follows from the conjecture nor feeds it."

**C2.** Same page, section "Problem 255", paragraph "The reverse edge",
first sentence (lines 161--162). Verified: the consumed Theorem 4.1 bounds
$H_L$, the largest anchored-prefix counting error of a finite list, below
by $\frac1{16}\log L$, and Halász's theorem bounds a planar $L^1$
discrepancy; both quantify the uniform statement, that no sequence has
$\sup_\alpha|D_n([0,\alpha))|$ bounded in $n$, and neither says anything
about one fixed interval, which is the conclusion of Problem 255 and which
the section's first bullet distinguishes from the uniform statement. Exact
change: replace "The quantitative form of the proved conclusion of Problem
255 is an input of the claimed resolution, not a consequence of it." by
"A quantitative form of the 1945 theorem, the uniform statement that the
conclusion of Problem 255 strengthens, is an input of the claimed
resolution, not a consequence of it."

**C3.** Same page, section "Problem 480", proof of Proposition 480.1
(lines 251--252). Verified: the proposition admits coincident values (its
own discussion uses $g_k=0$), and with coincident values $x_k$ equals
$y_j$ as a value for several $j$, so the written clause does not give
$\varepsilon_k\le2$; the positional statement does, because
$(k_1,\ldots,k_N)$ is a permutation and the position $j$ with $k_j=k$ lies
in the windows $j-1$ and $j$ only. Exact change: replace "the equality
$k_i^*=k$ forces $x_k\in\{y_i,y_{i+1}\}$, and $x_k$ is $y_j$ for exactly
one $j$" by "the equality $k_i^*=k$ forces $k\in\{k_i,k_{i+1}\}$, and
$k=k_j$ for exactly one $j$".

**C4.** Same page, section "Problem 480", the sharpness paragraph of the
proof (lines 271--276). Verified: the Section 2 page and the note (p. 14,
read on the image) state the cyclic order of $a_1,\ldots,a_n$ modulo $1$,
as the residues of $\log_2n,\ldots,\log_2(2n-1)$; the values in $[0,1)$
are $\log_2(k/2^j)$ with $2^j\le k<2^{j+1}$, which equal $\log_2(k/n)$
only when $n$ is a power of $2$. At $n=3$ the first three terms are $0$,
$\log_2(3/2)$ and $\log_2(5/4)$, the interior gaps are $\log_2(5/4)$ and
$\log_2(6/5)$, and $g_3=\log_2(6/5)$, not
$\log_2\frac{2n-1}{2n-2}=\log_2(5/4)$; the grader's recomputation for
$n\le100$ finds the frozen formula for $g_n$ wrong at every $n$ that is
not a power of $2$. The statement $\omega(\bar x)=1/\log4$ survives by the
sandwich below. Exact change: replace the paragraph from "For the
sharpness," to "$\square$" by:

"For the sharpness, the first $n$ terms of $x_k=\{\log_2(2k-1)\}$ are,
modulo $1$, the numbers $\log_2k$ for $n\le k\le2n-1$ (the
[[../library/analysis/debruijn_erdos_1949_sequences_points_circle/section_2_r_equals_1|Section 2 page]]),
so on the circle their $n$ gaps are $\log_2\frac{k+1}k$ for
$n\le k\le2n-1$, and the $n-1$ interior gaps of the interval are these
$n$ circle gaps with the wrap gap, from the largest term back to $x_1=0$,
removed. The smallest interior gap is therefore at least the smallest
circle gap and at most the second smallest:
$\log_2\frac{2n}{2n-1}\le g_n\le\log_2\frac{2n-1}{2n-2}$ for $n\ge2$, and
both bounds times $n$ tend to $1/(2\log2)=1/\log4$, so
$ng_n\to1/\log4$. $\square$"

**C5.** Same page, section "Problem 1221", conditional deduction 1221.3
(lines 480--481). Verified on the Theorem 1.1 page: the ratio part's
threshold is where $\frac3{100}\log r+O(1)<\frac1{16}\log\lfloor S\rfloor$
with $\lfloor S\rfloor\ge L_0$, and $r_0$ is an unspecified absolute
constant; the extended chain needs instead $\lfloor S\rfloor-B\ge L_0$ and
$\frac3{100}\log r+O(1)<\frac1{16}\log(\lfloor S\rfloor-B)$, where
$\log(\lfloor S\rfloor-B)=\log\lfloor S\rfloor+\log(1-B/\lfloor S\rfloor)$
and $B/\lfloor S\rfloor\to0$, so the comparison holds for all large $r$
with an absolute threshold, but nothing shows that the threshold of the
distinct-point theorem itself suffices. The same $c$ (Section 8 unchanged)
and the same coefficient $1/100$ (the margin $\frac3{100}<\frac1{32}$
unchanged) are established. Exact change: replace "with the same constants
$c$, $r_0$ and $1/100$" by "with the same $c$ and the same coefficient
$1/100$, and an absolute threshold in place of $r_0$".

**C6.**
[[research/leads/consecutive_gap_bounds_coincident_points/_index|consecutive_gap_bounds_coincident_points]],
section "Provisional premises", second bullet (line 104), which inherits
the clause of C5. Exact change: replace "with the same constants, for
every sequence," by "with the same constant $c$ and coefficient $1/100$
and an absolute threshold in $r$, for every sequence,".

**C7.** [[research/erdos_1221/connections|connections]], section
"Problem 1221", conditional deduction 1221.3, the parenthesis of premise
(P) (lines 477--478). Verified: the Lemma 4.2 page's "Statement as used"
states Theorem 4.1 for every list $z_1,\ldots,z_L\in[0,1)$ of length
$L\ge L_0$, as the source does (p. 7), so "for lists of distinct entries"
is not the statement there; the slip is harmless, a weaker premise, and
the bridge of Proposition 1221.1 restores the general case. Exact change:
replace "(Theorem 4.1 for lists of distinct entries and Halász's Theorem
7.1)" by "(Theorem 4.1, stated there for every list in $[0,1)$, of which
only the case of distinct entries is needed, and Halász's Theorem 7.1)".

**C8.** Same page, section "The span-to-count transfer has no second
consumer", the mechanism paragraph (line 529) and the Outcome (lines
583--585). Verified: Proposition 3.1 assumes $r\ge C_0A$ and Proposition
6.4 assumes $r\ge C_2A$, and the implication without a range is false.
Witness, recomputed: the Section 2 sequence $\log_2(2k-1)$ mod $1$ has
every gap at time $n$ in $[1/(2n\log2),1/(n\log2)]$, so every $r$-span
lies in $[0.72r/n,1.45r/n]$ and (2.1) holds with $A=r-1$ for $r\ge16$ (at
$r=40$ the span sums $a_t+b_t$ at $n=2^{14}$ and $n=2^{16}$ are $28.8$
against $A=39$); then $S\ge(r-1)^3$, while at $n=2^m$ the arc $(0,D/n]$
holds $\lfloor n2^{D/n}\rfloor-n\le0.694D+0.48D^2/n$ terms, so with
$D=(r-1)^3\le S$ and $n\ge D^2$ the counting error is at least
$0.3(r-1)^3-1$ (at $r=40$ and $D=n/4$ the errors are $997$ and $3985$),
against a claimed $O(r-1)$. Exact change: after "(only
$nM_n^{(r)}-r\le A$, or only $r-nm_n^{(r)}\le A$)" insert ", with $A\ge1$
and $r\ge C_0A$ for an absolute $C_0$, that is, a span error small
compared with $r$"; and in the Outcome replace "uniformly in the position,
and a conclusion" by "uniformly in the position to within an error small
compared with $r$, and a conclusion".

## Rejected and downgraded findings

Findings not listed under Corrections are recorded here with the reason.
"Optional" means a wording improvement the page may take without any
change to what it proves or attributes.

- **255 F2 (note):** downgraded to optional. The displays bound
  $r(\mu_r-1)$ for $r\ge K$ only, but "stay bounded" is true: the Section
  2 sequence has $M_n^1/m_n^1\to2$ and every $r$-span lies between $r$
  times its smallest and $r$ times its largest gap, so $\mu_r\le2$ for
  every $r$; and the contradiction with "tend to infinity" needs only the
  tail $r\ge K$. The short rewording "are bounded for all large $r$, so
  none tends to infinity" may be taken.
- **255 F4 (note):** downgraded to optional. "The only claimed proof" is
  a literature claim the section's reading cannot warrant, but the same
  bullet closes with "none is in the sources read", which supplies the
  scope; "in the sources held" may be added in both places.
- **255 F5 (note):** downgraded to optional. The content the section
  gives the 1945 theorem matches the held part VI, p. 63 (the supremum
  over anchors "cannot remain bounded"), read here in the text layer; the
  1949 note names the theorem without stating it (p. 14, read on the
  image); a citation of part VI for the statement may be added. The
  interval-circle identification is harmless: a sequence in $[0,1]$ with
  counting error at most $K$ on intervals has at most $K$ terms equal to
  $1$, so moving them to $0$ changes every count by at most $K$.
- **480 F2 (suggested):** downgraded to optional. The sentence is
  literally about the identity embedding, where the wrap gap is a genuine
  obstruction, and it stands. The review's scaled embedding is verified:
  with $a_i=x_i/(1+\delta)$ on the circle of circumference $1$ the wrap
  gap is at least $\delta/(1+\delta)$, the interior gaps are the
  interval's divided by $1+\delta$, and $g_n\le1/(n-1)$ by pigeonhole, so
  $m_n^1(a)=g_n/(1+\delta)$ for $n\ge1+1/\delta$ and (4.3) at $r=1$ gives
  $\omega(\bar x)\le(1+\delta)/\log4$ for every $\delta>0$. The page may
  record that the limit bound transfers this way while the interval count
  supplies the finite-$n$ bound $\tau'_n$.
- **480 F4 (note):** downgraded to optional. On p. 182 (read on the
  image) the chapter says that a sequence could have two consecutive
  terms very nearly equal infinitely often and still have $\omega$ large,
  provided that the pairs occur sufficiently far out, that this happens
  for the log sequence, and then introduces $C$ as the remedy; "remarks
  that $C$ can be small while $\omega$ stays large" is the section's
  inference, immediate from $C\le\liminf_m|x_{m+1}-x_m|$. The card of
  the chapter quotes the sentence as the chapter has it.
- **1221 F3 (note):** downgraded to optional. Under the section's
  tie-break a new coincident term comes last in its group and splits the
  gap after the group, which is positive (the wrap gap of length $1$ when
  all terms coincide), so a zero gap is never split; the clause "a zero
  gap may later be split into two zero pieces" describes a case that does
  not arise, and the accounting would absorb it. The proposed replacement
  may be taken.
- **1221 F4 (note):** downgraded to optional. On the Lemma 4.2 page
  $\delta$ serves only to keep at most one point of $P_{n_0}$ inside $J$,
  and the interval with exactly $L$ points comes from the $L$-span arc
  translated by a small $\varepsilon$, which uses distinct points; the
  inventory bullet attributes both to $\delta$. Both uses are replaced by
  Proposition 1221.1, so the inventory's conclusion stands.
- **1221 F5 (note):** rejected. When $B\ge L$ the list may be empty and
  the existence part is vacuous; the last sentence's condition
  $L-B\ge L_0$ excludes the case, and no consumer uses the proposition
  outside it.
- **1221 F6 (note):** downgraded to optional. "A proved replacement" in
  the lead's summary says that a proof is supplied; the body states
  "author-recorded, with proof" and the frontmatter carries
  `review_status: unreviewed`, so no standing is overstated; "with proof"
  may replace "proved".
- **span F2 (suggested):** downgraded to optional. The sentence names
  the direction, from counting control to span control, and attributes to
  Theorem 2 of the balanced-stick preprint what it takes from its Theorem
  3, which the review's W3 confirms is a single-scale passage (arcs of
  length about $R^\pm/n$ against $r$-spans); the reading as the strict
  converse of the descent from scale $r$ to scale $S$ is not the
  sentence's claim, though the review is right that that converse fails.
  The proposed replacement may be taken.
- **span F3 (suggested):** downgraded to optional. The two hypothesis
  forms and the two conclusion forms are paired by their parenthetical
  references, respectively; the review's witness that a one-sided
  hypothesis gives no pointwise conclusion (a sequence with small
  one-sided span error shrunk by the factor $1-A_0/r$, leaving an empty
  arc of length $S/n$) is correct and may be recorded.
- **span F4 (note):** downgraded to optional. "Arcs holding at most $S$
  terms" is the folder's shorthand for arcs of length at most $S/t$; under
  the hypothesis the two differ by $O(A)$ terms.
- **span F5 (note):** rejected. "Another setting" in the Outcome means
  another ambient space, the interval; Propositions 1221.1 and 1221.2 stay
  on the circle.
- **span F6:** not a finding; the status words and the corpus-inventory
  sentences are outside the review's read set and carry no verdict here
  either.

## Graded verdicts

No tier is assigned and no status changes. The page and the lead remain
author-recorded; the verdicts below are those of the graded focused
reviews, read with the corrections above and adjudicated by the grader.

**Problem 255: the 1949 implication toward the discrepancy theorem.**

- S1 (Proposition 255.1, displayed bounds): refutation-failed; the grader
  re-derived both counts with coincident entries, the zero-length and
  whole-circle spans and the stage $n=r+1$.
- S2 (consequences): refutation-failed; the finite range $r<K$ is covered
  by $\mu_r\le2$ (255 F2, optional).
- S3 (the implication and the factor $2$): refutation-failed.
- S4 (passage between arc types, $K\ge1$): refutation-failed.
- S5 (no fixed interval): refutation-failed.
- S6 (no rate): the clause "say nothing once $K(n)>r$" is
  refuted-as-stated for the upper bound (witness $K(n)=\lceil\log n\rceil$,
  $r=1$); the bullet's claim, that Proposition 255.1 transmits no rate
  into or out of the limits, is refutation-failed, with C1.
- S7 (circularity of the only route): refutation-failed; each imported
  input implies the 1945 theorem outright, as the review shows.
- S8 (scope): refutation-failed.
- S9 (reverse edge): refutation-failed for the interfaces; the sentence
  naming the quantified statement is corrected by C2.
- S10 (next investigation, conditional): refutation-failed as a
  conditional.
- S11 (target and source characterizations): refutation-failed; the
  p. 14 remark was read on the image by the grader.
- S12 (outcome): refutation-failed.

**Problem 480: the clustering constant and the Section 4 count.**

- S1 (target, imported): not a claim; faithful to the page image of
  p. 182.
- S2 (source characterization of display (1)): refutation-failed.
- S3 (Proposition 480.1, finite form): refutation-failed; the
  multiplicity identity re-derived by the grader, and its justification
  under coincident values repaired by C3.
- S4 (limit form): refutation-failed.
- S5 (sharpness): proof defective as frozen (the description of the first
  $n$ terms and of the smallest gap is false for every $n$ that is not a
  power of $2$); the statement $\omega(\bar x)=1/\log4$ is true and C4
  supplies a correct argument, so after C4 the statement is
  refutation-failed.
- S6 (obstruction): refutation-failed as stated, for the identity
  embedding; the scaled bridge is recorded under 480 F2.
- S7 (comparison of bounds): refutation-failed.
- S8 (incomparability): refutation-failed; both witnesses re-derived.
- S9 (descent): refutation-failed to the depth of a citation search of
  pp. 184--211.
- S10 (no reverse transfer): refutation-failed for the checkable clauses;
  "addressed by no held source" is unverified.
- S11 (next investigation): not a claim.
- S12 (outcome): refutation-failed.

**Problem 1221 itself: the site's family against sequences of distinct
points.**

- S1 (families): refutation-failed.
- S2 (multiset model): refutation-failed.
- S3 (inventory of distinctness): refutation-failed; 1221 F3 and F4 are
  wording notes on the inventory.
- S4 (Proposition 1221.1, existence part): refutation-failed.
- S5 (Proposition 1221.1, bridge and last sentence): refutation-failed.
- S6 (Proposition 1221.2): refutation-failed.
- S7 (conditional deduction 1221.3): the clause "the same $r_0$" is not
  established by the argument (proof defective for that clause; not
  refuted), and the description of the import in (P) misstates the Lemma
  4.2 page; with C5 and C7 the deduction is refutation-failed under its
  premise (P), which remains an explicit hypothesis, unrefereed and with
  two imports unchecked.
- S8 (limitations): refutation-failed.
- S9 (lead page): refutation-failed with C6; 1221 F6 optional.

**The span-to-count transfer has no second consumer.**

- S1 (hypothesis form): refutation-failed as a description of (2.1) and
  (6.1).
- S2 (conclusion form): refuted-as-stated as the unrestricted implication
  the sentence states (the witness of C8, recomputed by the grader);
  refutation-failed with the range $r\ge C_0A$ carried by C8.
- S3 (nesting): refutation-failed.
- S4 (converse passage): refutation-failed under the single-scale
  reading, which is the sentence's; span F2 optional.
- S5, S12: not claims (corpus inventory).
- S6 (Problem 255): refutation-failed.
- S7--S11: refutation-failed for the mathematical characterizations of
  the named problems; the status words and the theory-tree clause are
  unverified inventory.
- S13 (recognizer): refutation-failed with C8.
- S14 (only transfer): refutation-failed under the ambient-space reading.

**Lead outcomes.**

- [[research/leads/consecutive_gap_bounds_coincident_points/_index|consecutive_gap_bounds_coincident_points]]:
  **reviewed.** Its route rests on the inclusion inequalities (S1),
  Proposition 1221.1 (S4, S5), Proposition 1221.2 (S6) and the conditional
  deduction 1221.3 (S7) of the Problem 1221 section, each
  refutation-failed after C5 and C7, and on its own restatement (S9),
  refutation-failed after C6; the deduction remains conditional on (P),
  which the lead states as a provisional premise. The lead's frontmatter
  fields `research_state` and `review_status` are the integrator's to
  reconcile with this grade; no tier follows.

No tier is assigned and no status changes.
