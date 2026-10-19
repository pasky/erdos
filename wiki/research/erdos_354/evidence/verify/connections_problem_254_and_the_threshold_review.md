---
name: research/erdos_354/evidence/verify/connections_problem_254_and_the_threshold_review
title: "Independent review of the connections section: Problem 254 and the threshold $M_2^*$"
desc: |
  Refutation-failed for the section's mathematics: the sharpness example,
  the two-per-interval family and the Burr--Erdős correspondence survive
  re-derivation. One required correction (a universal clause about known
  incomplete two-ray sets, refuted-as-stated by a pair of dyadic rationals),
  two suggested corrections and three notes.
created: 2026-09-28T18:32:15Z
updated: 2026-09-28T20:40:46Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation and given only the assignment; the reviewer took no part in
writing the page, the folder's reconstructions or their reviews, and read
no existing review or grade body.

**Subject.** Page `wiki/research/erdos_354/connections.md` as it stood at
2026-09-28T13:50:48Z, section "## Problem 254 and the threshold $M_2^*$", lines
518--579 (the H2 at line 518 to the line before the next H2 at line 580), read
in the committed bytes. No separate lead page was named; the section is the
lead. The section contains no new proof: it composes reconstructed results and
source statements, so the review checks each composition, each quantifier and
each characterization of a source.

**Reading and depth.** The section clause by clause. The page's preamble
(lines 1--58: purpose and standing, notation, the definition of (1.5) and
of dyadic rationals) in full. As inputs whose proofs another reviewer
checks: the first section's Lemma 354.1, Proposition 354.2, Corollary 354.3
and the statement of Lemma 354.4 (lines 59--200), for the interface of
Corollary 354.3; the second section's Target, Proposition 354.5 and
conditional deduction 354.6 (lines 292--360), for the premise (P1); the
Problem 124 section and the closing section (lines 580--632), for the
shared description of the descent's inputs. Reconstruction pages, treated
as established at their reviewed standing:
[[research/erdos_354/fan_remark_4_1_reconstruction|Remark 4.1 at base two]]
and
[[research/erdos_354/fan_remark_4_2_reconstruction|Remark 4.2]] in full;
[[research/erdos_354/yu_chen_normalization_reconstruction|the normalization page]]
in full, for item 6;
[[research/erdos_354/yu_chen_theorem_reconstruction|the theorem page]]
through its four proof steps, the dependency map not read. Problem pages:
the statements of [[problems/integer_sequences/E0254/_index|Problem 254]] and
[[problems/additive_bases/E0354/_index|Problem 354]]. Library:
[[../library/additive_bases/fan_2026_strongly_complete_sets_conjecture_erdos/_index|the Fan card]]
and its
[[../library/additive_bases/fan_2026_strongly_complete_sets_conjecture_erdos/remark_4_2|Remark 4.2 page]];
[[../library/additive_bases/yu_chen_2026_erdos_problem_354_i_strong_completeness_two_dyadic_floor_sequences/theorem|the Yu--Chen theorem page]].
Held PDFs, read in their text layers: Fan v5, pp. 3--4 (Theorem 1.1,
Corollary 1.2, (1.8), (1.9), the paragraph on Hegyvári's results), the
opening of Section 2 (syndetic and thick sets, $\Delta(S)$, Lemma 2.1,
Theorem 2.2), the opening of Section 3 and Lemma 3.3, the opening of
Section 4 with the lemma citations inside the proof of Theorem 1.1,
Remarks 4.1 and 4.2, Propositions 4.2 and 4.3 with the paragraph between
them, the statement of Corollary 6.3 and the reference list; the Yu--Chen
manuscript, p. 1 (the theorem and the history paragraph) and its reference
list. Guidance: the named sections of `docs/verification.md`,
`docs/approach_vetting.md`, `docs/evidence.md` "Source fidelity" and
`docs/math_authoring.md`.

**Exposures.** Five, none used for a verdict.

1. The Problem 254 page's Current assessment, Progress and Known Results
   sections were displayed together with its statement in a single read of
   the page's first eighty lines; the Progress section summarizes the
   section under review.
2. The Problem 354 page's whole block before its Current assessment was
   displayed: Formulation, Status (acceptance text about the site-accepted
   Lean proof and the other 2026 sources), provenance of the proof file,
   Source, References and Formalization. Only the statement and the three
   reference entries [He89], [JiMa24] and [FaHe25], marked not held and
   site-attested, were used.
3. The Fan card, its Remark 4.2 page and the Yu--Chen theorem page were
   read whole, including their Bears-on standing paragraphs.
4. A listing of the folder's `evidence/verify/` directory (file names) and
   the twelve frontmatter lines of the normalization reconstruction's
   review, read to learn the record format; that frontmatter's description
   states the summary verdict of that other review.
5. Corpus-wide searches, file names only, for the word "syndetic" and for
   citations of Burr and Erdős, made to test statement S4's claim about
   what the corpus holds.

## Restatement

Throughout, $\mathbb N=\{1,2,\ldots\}$ for sets $A\subseteq\mathbb N$ as in
Fan, while the rays are indexed from exponent $0$ in every convention used:
$A_{\alpha,\beta}=\{\lfloor2^n\alpha\rfloor,\lfloor2^n\beta\rfloor:n\ge0\}\setminus\{0\}$.
A set is complete if every sufficiently large integer is a sum of distinct
elements, strongly complete if every finite deletion leaves it complete;
(1.5) is $\sum_{a\in A}\|a\theta\|=\infty$ for every
$\theta\in\mathbb R\setminus\mathbb Z$; $M_2^*$ is the least positive
integer $M$ such that every $A\subseteq\mathbb N$ with (1.5) and
$|A\cap(2^k,2^{k+1}]|\ge M$ for all sufficiently large $k$ is strongly
complete; a dyadic rational is a nonzero integer times a power of $2$.

- **S1 (Target; descriptive).** Problem 254 asks whether every
  $A\subseteq\mathbb N$ with $|A\cap(x,2x]|\to\infty$ as $x\to\infty$ and
  $\sum_{n\in A}\|\theta n\|=\infty$ for every $\theta\in(0,1)$ is
  complete. The Fan card records Corollary 1.2 (every $A$ with (1.5) and
  at least five elements in $(2^k,2^{k+1}]$ for all large $k$ is strongly
  complete) as the preprint's confirmation in strong form, the proof of
  Theorem 1.1 unread; the folder reconstructs Remarks 4.1 and 4.2, which
  consume Corollary 1.2 as a statement.
- **S2 (Sharpness).** (a) The set $A=\{2^k+1:k\ge1\}$ satisfies (1.5),
  has exactly one element in $(2^k,2^{k+1}]$ for every $k\ge1$, and is not
  complete (premise: Remark 4.1 page). (b) Hence the statement obtained
  from Problem 254 by replacing $|A\cap(x,2x]|\to\infty$ with "at least
  one element in $(2^k,2^{k+1}]$ for all large $k$", keeping the
  divergence hypothesis and the conclusion, is false; Corollary 1.2 asserts
  the version with "at least five" and the conclusion strengthened to
  strong completeness. (c) $M_2^*\in\{2,3,4,5\}$, and its exact value is
  open in the source.
- **S3 (Two-per-interval family).** (a) For all $\alpha,\beta>0$ with
  $\alpha/\beta$ not a power of $2$ and at least one of $\alpha,\beta$ not
  a dyadic rational, $A_{\alpha,\beta}$ satisfies (1.5) and has at least
  two elements in $(2^k,2^{k+1}]$ for all large $k$ (premise: Remark 4.2
  page, Steps 2--3). (b) When $\alpha/\beta$ is irrational these sets are
  strongly complete on the Yu--Chen theorem, if it stands; when
  $\alpha/\beta$ is rational and not a power of $2$, on each such line
  $A_{\alpha,\beta}$ is strongly complete for Lebesgue-almost every
  coefficient (Corollary 354.3, author-recorded). (c) The family lies
  outside the hypothesis of Corollary 1.2 and is consistent with
  $M_2^*=2$, the value that Remark 4.2 shows would imply Hegyvári's
  conjecture. (d) Fan's Proposition 4.3 says that Theorem 2.2 cannot yield
  $M_2^*\le4$ and that a different mechanism may be needed; the descent is
  a different mechanism but consumes the digit recurrence of two rays, not
  a per-interval count, so it says nothing about a general set with two
  elements per dyadic interval.
- **S4 (Burr--Erdős instance).** Item 6 of the normalization page, the
  bound $\operatorname{gap}(P_n)\le N$ derived from
  $c_{j+1}-\sum_{i\le j}c_i\le c_0$, is the two-ray instance of the
  Burr--Erdős lemma that Fan records as Lemma 2.1 (for infinite
  $S\subseteq\mathbb N$, $\Delta(S)<\infty$ makes $\operatorname{FS}(S)$
  syndetic); the corpus holds neither the Burr--Erdős paper nor a general
  proof.
- **S5 (What it does not give; obstruction).** The folder holds no
  reconstruction of Theorem 1.1 or of Theorem 2.2, and the descent does
  not extend to sets without the digit structure.
- **S6 (Next investigation).** (a) The compilation task for Problem 254 is
  a reconstruction of Fan's Theorem 2.2 and Section 4, which would also fix
  the standing of premise (P1). (b) The corpus holds no candidate for an
  incomplete set with (1.5) and two elements in every large dyadic
  interval. (c) Every incomplete two-ray set known (Hegyvári 1989,
  Jiang--Ma, Fang--He, site-attested) has a ratio that is a power of $2$
  and is therefore a single ray as a set.
- **S7 (Outcome; standing).** The section transfers the sharpness example
  and the family as author-recorded context for $M_2^*$ and fails as a
  route to Problem 254.

## Checklist

- **Quantifiers and scope.** One failure: S6(c) quantifies over "every
  incomplete two-ray set known" without the hypothesis that one
  coefficient is not a dyadic rational, and the pair $(2,6)$ refutes the
  literal clause (F3). S3(b)'s "each rational-ratio line" is read within
  the family (ratio not a power of $2$), which the sentence's "these sets"
  supplies; outside it the phrase would be false (F5). S2(b)'s weakening
  is a genuine weakening: $|A\cap(x,2x]|\to\infty$ at $x=2^k$ gives any
  fixed count for large $k$. The problem's $\theta\in(0,1)$ and Fan's
  $\theta\in\mathbb R\setminus\mathbb Z$ agree by periodicity.
- **Circularity.** None. The family's strong completeness in S3 comes from
  the Yu--Chen theorem and Corollary 354.3, not from $M_2^*=2$; the lower
  bound $M_2^*\ge2$ comes from a witness, not from Corollary 1.2.
- **Model and convention changes.** None found. Ray indices start at $0$
  in the preamble, in Fan's (1.9) and in the normalization page; strong
  completeness (deletion of a finite $B\subseteq A$ in Fan, of a finite
  $F\subseteq\mathbb Z$ on the Yu--Chen pages) is the same property;
  Problem 354's multiset reading is not used by the section, which speaks
  of sets throughout, and "a single ray as a set" in S6(c) names the
  convention it uses.
- **Finite and statistical overreach.** None. The almost-every statement
  of Corollary 354.3 is used as almost-every; no finite check is cited as
  coverage.
- **Uniformity.** Not at issue. No constant in the section is claimed
  uniform over a family; the exceptional null set in S3(b) may depend on
  the line, and the section claims nothing across lines.
- **Extremal conclusions.** S2(c) is checked in the claim's own unit, the
  count per half-open dyadic interval: the witness has count exactly $1$
  for every $k\ge1$, so $M=1$ fails and $M_2^*\ge2$. The upper bound and
  the existence of $M_2^*$ rest on the preprint's Corollary 1.2, which
  the sentence does not mark (F1).
- **Consequences and composition.** Each "so" and "hence" was attacked
  separately: S2(b) from S2(a) holds; S2(c)'s lower half holds; S3(c)
  holds since the family has exactly two elements per large interval;
  S6(c)'s "hence a single ray as a set" holds. S6(a) composes wrongly: the
  proof of Theorem 1.1 consumes Lemmas 3.1--3.3 of Section 3, so a
  reconstruction of Theorem 2.2 and Section 4 alone would not fix (P1)'s
  standing (F2).
- **Computation.** Inapplicable: the section computes nothing; the
  constants $u_2=2$, $v_2=3$, $M_2=5$ used on the Remark 4.2 page were
  recomputed from (1.6) and agree.
- **Reproduction.** Inapplicable: the section states no rerun command and
  claims no evidence coverage.
- **Source and verdict fidelity.** Fan's Lemma 2.1, Proposition 4.3 and
  the paragraph before it, Remark 4.1's openness sentence and the card's
  read-status sentence are characterized faithfully. The attribution of
  non-completeness results to Hegyvári 1989 cannot be checked from held
  sources, and the held Yu--Chen manuscript attributes them to Jiang--Ma
  and Fang--He only (F4). S6(a)'s scope of Fan's proof is misstated (F2).

## Weakest steps

**W1: from the witness to the threshold (S2).** Let $A=\{2^k+1:k\ge1\}$.
Membership: $2^k<2^k+1\le2^{k+1}$ for $k\ge1$, and $2^j+1$ with $j\ne k$
lies in a different interval, so the count in $(2^k,2^{k+1}]$ is exactly
$1$. Divergence: if $\sum_{a\in A}\|a\theta\|<\infty$ then
$\|(2^k+1)\theta\|\to0$, and
$\|\theta\|=\|2(2^k+1)\theta-(2^{k+1}+1)\theta\|\le2\|(2^k+1)\theta\|+\|(2^{k+1}+1)\theta\|\to0$,
so $\theta\in\mathbb Z$. Incompleteness: the elements at most $2^{k+1}$
are $2^j+1$ for $1\le j\le k$, whose nonempty subset sums number at most
$2^k-1$, leaving at least $2^k+1$ integers of $[1,2^{k+1}]$ outside
$\operatorname{FS}(A)$, unboundedly many. So the threshold definition
fails at $M=1$: $A$ has (1.5) and one element in every large interval but
is not even complete, hence $M_2^*\ne1$, and since larger $M$ only shrink
the set of $A$ considered, $M_2^*\ge2$ whenever $M_2^*$ exists. Existence
and the bound $5$ are exactly Corollary 1.2. Problem 254's growth
hypothesis implies any fixed count in every large dyadic interval, so
replacing it by "at least one" is a weakening, and the witness refutes the
weakened statement: S2(b) holds.

**W2: the family and its two covering results (S3).** Rescale to
$\alpha'=2^{-s}\alpha$, $\beta'=2^{-t}\beta$ in $(1/2,1]$. For $m\ge1$,
$2^m\alpha'\in(2^{m-1},2^m]$, so $\lfloor2^m\alpha'\rfloor\in[2^{m-1},2^m]$,
and it lies in $(2^k,2^{k+1}]$ only for $m=k+1$ (value $>2^k$ once
$\alpha'\ge1/2+2^{-k-1}$, true for large $k$ as $\alpha'>1/2$) or for
$m=k+2$ with value exactly $2^{k+1}$, excluded for large $k$ by the same
inequality. So each ray contributes exactly one element to every large
interval, and the two differ for large $k$ because
$2^{k+1}|\alpha'-\beta'|\ge2$: the count is exactly $2$, which is why the
family is outside Corollary 1.2's hypothesis (S3(c)). Divergence follows
from the digit argument of the Remark 4.2 page, which needs only that one
coefficient is not a dyadic rational. Coverage: an irrational ratio is not
a power of $2$, and two dyadic rationals have a rational ratio, so every
irrational-ratio pair is in the family and the Yu--Chen theorem's
hypothesis is exactly "irrational ratio"; on a line with rational ratio
not a power of $2$, Corollary 354.3's hypotheses (the parameter $\gamma$
not dyadic and its expansion containing $0^{L(p,q)}$ infinitely often)
hold for almost every $\gamma$, and both coefficients $p\gamma,q\gamma$
are then non-dyadic, so the covered sets are in the family. "Consistent
with $M_2^*=2$" claims only that no covered member is a counterexample.

**W3: the Burr--Erdős correspondence (S4) and the single-ray count
(S6(c)).** Fan defines $\Delta(S)=\sup_{s\in S}(s-\sum_{t\in S,t<s}t)$.
For a normalized pair the merged list $c_0<c_1<\cdots$ has
$c_{j+1}\le2c_j$ (item 4), so
$c_{j+1}-\sum_{i\le j}c_i=(c_{j+1}-2c_j)+(c_j-\sum_{i<j}c_i)\le c_j-\sum_{i<j}c_i\le\cdots\le c_0=N$,
and the term at $c_0$ is $N$ itself: $\Delta(S)=N<\infty$ with $S$
infinite, so Lemma 2.1 applies and item 6 is its quantitative two-ray
instance. For a single ray $c_n=\lfloor2^n\alpha'\rfloor$ with
$\alpha'\in(1/2,1]$ and $d_n=c_{n+1}-2c_n\in\{0,1\}$, induction gives
$c_{n+1}-\sum_{i\le n}c_i=c_0+\sum_{i\le n}d_i$, which is unbounded when
$\alpha'$ is not a dyadic rational; the integers strictly between
$\sum_{i\le n}c_i$ and $c_{n+1}$ are then never subset sums, so such a ray
is incomplete with unbounded gaps, while it satisfies (1.5) by the same
digit argument and has one element per large interval. A two-ray set with
ratio $2^j$ ($j\ge0$) equals $\{\lfloor2^n\beta\rfloor:n\ge0\}\setminus\{0\}$
for the smaller coefficient $\beta$, since
$\lfloor2^n\alpha\rfloor=\lfloor2^{n+j}\beta\rfloor$: a single ray as a
set, hence one element per large interval and no candidate for S6(b).

## Strongest attack

- **S1.** Compared clause by clause with the problem statement (the
  displayed growth condition is $|A\cap(x,2x]|\to\infty$, the distance
  function is the nearest-integer distance) and with the card's read
  status ("Theorem 1.1 and the rest of the paper were read at statement
  level only"). No discrepancy.
- **S2.** Attempted to break the witness (a wrong count at the interval's
  endpoints, a convergent distance sum, or completeness after all): each
  property re-derived in W1. Attempted to show the weakening is not a
  weakening: it is. Attempted to obtain $M_2^*\le5$ from anything in the
  corpus other than the preprint's statement: nothing exists, so the
  unconditional sentence overstates what is author-recorded (F1); the
  mathematics of S2(a)--(b) and the lower bound stand.
- **S3.** Attempted to find a family member with five elements per
  interval (inside Corollary 1.2's reach): impossible, the count is
  exactly two. Attempted to find a covered member outside the family: the
  Yu--Chen hypothesis and Corollary 354.3's almost-every set both lie
  inside it (W2). Attempted to read "each rational-ratio line" as covering
  ratios that are powers of $2$: there the set is a single ray, incomplete
  for almost every coefficient, so the phrase is true only within the
  family, which the sentence names (F5). Checked Fan's own words for
  S3(d): "there is no hope of deducing $M_2^*\le4$ from Theorem 2.2,
  suggesting that a genuinely different mechanism for strong completeness
  may be required", and Proposition 4.3 exhibits a strongly complete set
  with exactly four elements per interval for $k\ge3$ admitting no
  partition of the Theorem 2.2 shape; the section's paraphrase does not
  strengthen this.
- **S4.** Attempted a mismatch between Fan's $\Delta$ and the display: the
  sup is attained at $c_0$ and equals $N$ (W3). Attempted to find the
  lemma proved in the corpus: Fan records it with citations only, no
  corpus page proves it, and no card for the 1981 paper exists (F6 for the
  limit of this check).
- **S5.** The folder listing contains no reconstruction of Theorem 1.1 or
  Theorem 2.2. The obstruction is stated at its actual scope: the descent's
  inputs (interlacing, digit recurrence, reduced ratio at a block) are
  absent for a general set, and the section claims silence, not
  impossibility.
- **S6.** S6(a): the proof of Theorem 1.1 in Section 4 cites Lemma 3.1
  (countable spectra), Lemma 3.2 (the selection lemma) and Lemma 3.3 (the
  bound on $\Delta$), so the named reconstruction would leave (P1) resting
  on unreconstructed lemmas (F2). S6(b): the only sets in the read set
  with (1.5) and few elements per interval are the witness of S2, the
  single rays and Fan's Proposition 4.3 set (strongly complete): no
  candidate. S6(c): the pair $(\alpha,\beta)=(2,6)$ gives
  $A_{2,6}=\{2^{n+1}\}\cup\{3\cdot2^{n+1}\}$, a two-ray set whose ratio
  $1/3$ is not a power of $2$ and whose elements are all even, so it is
  incomplete; the literal universal clause is refuted. The witness fails
  (1.5) at $\theta=1/2$, so S6(b) is untouched (F3).
- **S7.** The standing sentence claims author-recorded context only, which
  is what the section provides.

## Premises

- Remark 4.1 at base two (reconstruction page; reviewed at its stated
  standing). Interface used: the three properties of $\{2^k+1:k\ge1\}$ and
  $M_2^*\ge2$; its $M_2^*\le5$ is explicitly attributed there to
  Corollary 1.2. Read in full.
- Remark 4.2 (reconstruction page; reviewed). Interface used: Steps 2--3
  (two elements per large interval and (1.5)) for every pair with ratio
  not a power of $2$ and one non-dyadic coefficient; the implication
  $M_2^*=2$ implies Hegyvári's conjecture; the statements of Theorem 1.1
  and Corollary 1.2 with $u_2=2$, $v_2=3$, $M_2=5$. Read in full.
- Normalization page (reconstruction; reviewed). Interface used: items 4
  and 6 and their proofs, valid for every normalized pair. Read in full.
- Yu--Chen theorem (reconstruction page and library theorem page).
  Interface: $\alpha,\beta>0$, $\alpha/\beta$ irrational, then strongly
  complete; an unrefereed manuscript claim, author-recorded reconstruction.
  Statement and proof steps read; the section's "if it stands" matches.
- Corollary 354.3 (first section of the page; author-recorded; its proof
  is another reviewer's subject). Interface: rational ratio not a power of
  $2$, $\gamma=\beta/q$ not dyadic with infinitely many runs of $L(p,q)$
  zeros, then strongly complete; in particular almost every $\gamma$ on
  each such line. Statement and proof read for the interface only.
- Premise (P1) (second section): Fan's Theorem 1.1 as a preprint claim
  whose proof, Sections 2--4, is not reconstructed. Read at statement.
- Fan (2026), arXiv:2607.14071v5, held; text layer read at the pages
  listed above. Used: (1.5), (1.8), (1.9), Theorem 1.1, Corollary 1.2,
  the definition of $\Delta(S)$, Lemma 2.1 (recorded without proof, with
  citations to Burr--Erdős [8, Lemma 3.2] and Bergelson--Simmons
  [1, Lemma 2.11]), Theorem 2.2, Lemma 3.3, the lemma citations in the
  proof of Theorem 1.1, Remark 4.1, Remark 4.2, Propositions 4.2 and 4.3.
- Yu and Chen (2026), manuscript, held; text layer read at p. 1 and the
  references. Used: the theorem's statement and the history sentence
  attributing non-completeness results for ratios that are powers of two
  to Jiang--Ma and Fang--He.
- Burr and Erdős (1981), Hegyvári (1989), Jiang and Ma (2024), Fang and He
  (2025): not held; the last three are site-attested through the Problem
  354 page's reference list. Nothing about their contents was verified.
- Problem 254 and Problem 354: statements read.

## Findings

- **F1 (suggested).** Location: "the exact threshold $M_2^*$ lies in
  $\{2,3,4,5\}$ and is open in the source" (lines 538--539), and the Outcome's
  "context for $M_2^*$". Defect: the upper bound and the existence of
  $M_2^*$ rest on the preprint's Corollary 1.2, whose proof no corpus page
  has read, while the sentence reads unconditionally; the page's second
  section labels the same theorem premise (P1). Witness: the Target
  paragraph itself ("the proof of Theorem 1.1 unread"). Replacement: "on
  the preprint's Corollary 1.2 the exact threshold $M_2^*$ lies in
  $\{2,3,4,5\}$; only $M_2^*\ge2$ is reconstructed, and the value is open
  in the source".
- **F2 (suggested).** Location: "a reconstruction of Fan's Theorem 2.2 and
  Section 4, which would also fix the standing of premise (P1) above"
  (lines 569--570). Defect: the proof of Theorem 1.1 in Section 4 consumes
  Lemmas 3.1, 3.2 and 3.3 of Section 3, so the named reconstruction would
  not fix (P1)'s standing. Witness: the citations of Lemma 3.1, Lemma 3.2
  and Lemma 3.3 inside the proof of Theorem 1.1 (v5, pp. 17--19), and the
  Remark 4.2 page's own scope, "Sections 2--4". Replacement: "a
  reconstruction of Fan's Theorem 2.2 with Sections 3--4".
- **F3 (required).** Location: "every incomplete two-ray set known
  (Hegyvári 1989, Jiang--Ma, Fang--He, all site-attested) having a ratio
  that is a power of $2$ and hence a single ray as a set" (lines
  572--574). Defect: the universal clause omits the hypothesis that one
  coefficient is not a dyadic rational. Witness: $A_{2,6}$, whose elements
  are all even, is an incomplete two-ray set with ratio $1/3$; any pair
  of even integers with ratio not a power of $2$ gives such a set. The
  conclusion of the sentence survives because these sets fail (1.5) at
  $\theta=1/2$.
  Replacement: "every incomplete two-ray set known with one coefficient
  not a dyadic rational (...) having a ratio that is a power of $2$ and
  hence a single ray as a set, while a pair of dyadic rationals fails
  (1.5)".
- **F4 (note).** Location: the same clause's attribution to Hegyvári 1989.
  The held Yu--Chen manuscript credits Hegyvári 1989 with the completeness
  case (one coefficient dyadic, the other not) and the non-completeness
  results for ratios that are powers of two to Jiang--Ma and Fang--He; the
  1989 paper is not held, so the attribution is unverified here. No
  replacement proposed; a reader should not take the parenthesis as a
  verified census.
- **F5 (note).** Location: "for almost every coefficient on each
  rational-ratio line" (lines 546--547). The phrase is true within the
  family the sentence names (ratio not a power of $2$) and false for the
  lines with ratio a power of $2$, where the set is a single ray. Optional
  replacement: "on each rational-ratio line of the family".
- **F6 (note).** Location: "the corpus holds neither Burr--Erdős nor a
  general proof" (line 561). Checked against the corpus's own pages
  (no page proves the lemma) and Fan's text (the lemma is recorded with
  citations only); held PDFs outside this review's read set were not
  examined for a proof. The claim stands as far as checked.

## Verdict

- S1: not a claim; its description of the problem and of the card is
  faithful.
- S2: refutation-failed for (a) and (b) and for the lower bound in (c);
  the upper bound in (c) is the preprint's Corollary 1.2 and should be
  marked as such (F1).
- S3: refutation-failed (F5 is a reading note).
- S4: refutation-failed (F6 states the limit of the corpus check).
- S5: refutation-failed; the obstruction is stated at its actual scope.
- S6: (b) refutation-failed; (c) refuted-as-stated in its literal
  universal reading, with the witness $A_{2,6}$, its conclusion surviving
  under the missing hypothesis (F3); (a) refuted-as-stated as a
  description of what would fix (P1), since Section 3 is also consumed
  (F2).
- S7: refutation-failed; the standing sentence claims exactly
  author-recorded context.

Limitations: the reconstructions and Corollary 354.3 were consumed at
their stated standing and not re-derived beyond their interfaces; the
three site-attested papers of S6(c) are not held, so nothing about their
contents was verified; no computation was run; the corpus check behind S4
covered corpus pages and Fan's text, not every held PDF. This focused
review assigns no tier and changes no status.
