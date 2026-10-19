---
name: research/erdos_354/evidence/verify/connections_problem_348_deletion_thresholds_review
title: "Independent review of the connections section: Problem 348: deletion thresholds"
desc: |
  Refutation review of the Problem 348 section of the connections page as of
  2026-09-28T13:50:48Z. The one mathematical statement, that the strongly
  complete Yu--Chen sets are examples for no deletion pair, survives
  (refutation-failed); one record sentence is refuted-as-stated. One
  required correction, one suggested, two notes.
created: 2026-09-28T18:23:04Z
updated: 2026-09-28T18:23:04Z
---

***

## Subject and independence

**Role.** The reviewer worked in a fresh context from the assignment alone
and took no part in writing the connections page, the reconstruction pages,
the library cards or the problem pages. The charge was refutation. This
review assigns no tier and changes no status.

**Subject.** Page `wiki/research/erdos_354/connections.md` as it stood at
2026-09-28T13:50:48Z, section "## Problem 348: deletion thresholds", lines
490--516 (the H2 heading at line 490 through the "**Outcome.**" paragraph at
line 516; the next H2 opens at line 518). The assignment named no separate lead
page; the [[research/erdos_354/connections|connections page]] is the only
subject page. Its shared preamble (lines 1--58: purpose and standing, the
notation for $A_{\alpha,\beta}$, complete and strongly complete sets, the
normalized pair, and the dyadic-rational and conjecture conventions) was read as
input. The bodies of the page's other sections were not read; only the
list of H2 headings was used to locate the section.

**Read set and depth.**

- The section, read in full and re-derived sentence by sentence; the
  preamble, read in full.
- Reconstruction pages, read in full as premises at their reviewed
  standing:
  [[research/erdos_354/yu_chen_theorem_reconstruction|Yu--Chen Theorem]]
  (statement, Steps 1--4, dependency map, scope),
  [[research/erdos_354/geneson_theorem_9_reconstruction|Geneson Theorem 9]]
  and
  [[research/erdos_354/geneson_corollary_12_reconstruction|Geneson Corollary 12]]
  (statements, proofs, scope). The folder's remaining reconstruction pages
  were identified by name only; the section uses nothing from them beyond
  the theorem's conclusion.
- Problem pages, Statement paragraphs only:
  [[problems/additive_bases/E0348/_index|Problem 348]] and
  [[problems/additive_bases/E0354/_index|Problem 354]].
- Library: the provenance and read-status paragraphs of the
  [[../library/additive_bases/geneson_2026_deletion_thresholds_exponential_examples_complete_sequences/_index|Geneson (2026)]]
  card and the provenance and Statement sections of its result pages
  [[../library/additive_bases/geneson_2026_deletion_thresholds_exponential_examples_complete_sequences/theorem_1|Theorem 1]],
  [[../library/additive_bases/geneson_2026_deletion_thresholds_exponential_examples_complete_sequences/theorem_9|Theorem 9]]
  and
  [[../library/additive_bases/geneson_2026_deletion_thresholds_exponential_examples_complete_sequences/corollary_12|Corollary 12]];
  the provenance and Statement sections of the
  [[../library/additive_bases/yu_chen_2026_erdos_problem_354_i_strong_completeness_two_dyadic_floor_sequences/theorem|Yu--Chen Theorem]]
  result page. The held Geneson PDF (arXiv:2609.25107v1, 14 pages) was
  read in its text layer, pp. 1--5 in full (Theorem 1; Section 2 with
  Theorem 2, Lemma 3, Lemma 4, Proposition 5 and the exclusion of
  $m\ge2$), together with the closing line of Section 4 (p. 11) and the
  roadmap paragraph of the introduction (p. 3). No page image was needed:
  the section quotes no formula from the source.
- Guidance: `docs/verification.md` sections "Grading and claim standing",
  "Audit checklist — the canonical failure modes", "Whole-claim report"
  and "Audit checklist"; `docs/approach_vetting.md`; `docs/evidence.md`
  section "Source fidelity"; `docs/math_authoring.md`.

**Exposures.** Three incidental exposures, none of review, grade or
assessment text, disclosed in full:

1. A grep for headings and bold labels over the two problem pages, run to
   locate their Statement sections, printed each bold label line of those
   pages. For E0348 this included the line "Status. Open. Tags. number
   theory, complete sequences." (line 21); for E0354 it included the
   label lines of its header block (lines 38, 52, 97, 128, 139, 150,
   215) and the opening words of the label lines of its Current
   assessment section (lines 243, 303, 351, 384, 404, 419), and nothing
   of their bodies. None of these lines concerns Problem 348's
   mathematics; the E0348 status word was not used except where the
   section itself reports it (S2).
2. A grep for the words "pending", "compilation task" and "reconstruct"
   over the four pages of the Geneson card folder, run to check the
   section's sentence about a pending task (S5b), printed one line of
   `theorem_1.md` (line 72), three lines of `theorem_9.md` (lines 57,
   59, 80) and two lines of `corollary_12.md` (lines 65, 67), all
   outside those pages' Statement sections. Their content is reported
   under F1 and nowhere else.
3. Directory listings by name only: the folder
   `wiki/research/erdos_354/` including the name of its `evidence/`
   subtree and the file names under `evidence/verify/`. No file under
   `evidence/` was opened.

The folder's `_index.md`, every existing review and grade, every Current
assessment, Progress, Known results and standing text, and the web were
not read.

## Restatement

The section makes the following statements. The page's preamble fixes
"complete" as: every sufficiently large integer is a sum of distinct
elements, and "strongly complete" as: complete after every finite
deletion.

- **S1 (target).** Problem 348 asks for which integer pairs $0\le m<n$
  there exists a complete nondecreasing sequence of integers that remains
  complete after the removal of any $m$ elements and is not complete after
  the removal of any $n$ elements. ("Any" is universal in both clauses:
  every $m$-element removal keeps completeness; every $n$-element removal
  destroys it.)
- **S2 (records).** (a) The problem page records the status open with
  progress not compiled. (b) The Geneson card records Theorem 1, the
  classification "exactly the pairs with $m\le1$", as a preprint claim
  read for structure only. (c) The folder index names Problem 348 only as
  a further target of the same preprint.
- **S3 (nothing transports).** Three supporting statements.
  - **S3a.** The folder's reconstructions of Geneson's paper concern
    Theorem 9 and Corollary 12 and not Theorem 1.
  - **S3b (the obstruction).** The Yu--Chen theorem gives completeness
    after every finite deletion. Hence for every pair $\alpha,\beta>0$
    satisfying the theorem's hypothesis ($\alpha/\beta$ irrational), the
    set $A_{\alpha,\beta}$ has Problem 348's first property for every
    $m\ge0$ and fails its second property for every $n\ge1$; so no such
    set is an example for any pair $(m,n)$.
  - **S3c.** The content of the problem beyond the two classical
    constructions is the exclusion of $m\ge2$; in Geneson's paper this is
    carried by an incompleteness mechanism, the central-interval Theorem 2
    and Lemma 4; the folder holds no reconstruction of it; and the
    Yu--Chen descent argument has no counterpart to it.
- **S4.** The folder gives no part of the classification, neither the
  existence side ($m\le1$) nor the exclusion side ($m\ge2$).
- **S5.** (a) No next investigation arises from the folder. (b) A
  reconstruction of Geneson's Sections 2--4 is a separate compilation task
  that the card records as pending.
- **S6.** The transfer fails; the only link between the folder and Problem
  348 is the shared source.

S3b is the section's one mathematical statement and its stated
obstruction; S3a, S3c (first three clauses) and S5b are record and
source-fidelity statements; the "no counterpart" clause of S3c, S5a and
the first clause of S6 are judgments.

## Checklist

- **Quantifiers and scope.** Pass. S3b needs the theorem's conclusion in
  its full universal form (every finite $F$), which the reconstruction
  states; the section's "for every $m$" and "for no $n$" follow from it
  without an almost-all step. The hypothesis $\alpha/\beta$ irrational is
  carried only by the phrase "of its theorem"; it is load-bearing (see
  Weakest steps, W3), so F2 suggests making it explicit. The pair
  constraint $n>m\ge0$ forces $n\ge1$, which the "for no $n$" clause needs.
- **Circularity.** Inapplicable. No statement assumes its own conclusion;
  S3b consumes the reconstructed theorem and the problem's definition.
- **Model and convention changes.** Pass. Problem 348 concerns a
  nondecreasing sequence with removals of elements; the theorem concerns
  the set $A_{\alpha,\beta}$ and sums of distinct elements. The bridge is
  checked under both readings (distinct values in increasing order; the
  interleaving with repeated occurrences) in W1 and holds under both. The
  completeness convention (eventual, distinct indices) is the same in the
  preamble, in the problem statement and in the source (its p. 1).
- **Finite and statistical overreach.** Inapplicable. No finite sample or
  heuristic is used.
- **Uniformity.** Inapplicable. The threshold $H$ of the theorem depends on
  $F$, and the section claims nothing uniform in $F$, $m$ or $n$.
- **Extremal conclusions.** Inapplicable. No infimum, supremum or sharpness
  sentence.
- **Consequences and composition.** Pass. The "so" of S3b is re-derived in
  W1. S3's conclusion "Nothing" composes S3a, S3b and S3c: the folder has
  no examples for any pair and no argument on the exclusion side; S4 and
  S6 restate this. The judgment clauses are recorded as judgments.
- **Computation.** Inapplicable. The section runs no computation.
- **Reproduction.** Inapplicable. No rerun command or coverage claim.
- **Source and verdict fidelity.** One failure and two imprecisions. The
  labels "central-interval Theorem 2", "Lemma 4", "the exclusion of
  $m\ge2$" and "Sections 2--4" match the held PDF (Theorem 2 is labeled
  "(central-interval)" on p. 3; Lemma 4 is the two-occurrence gap lemma on
  p. 4; "Exclusion of $m\ge2$ in Theorem 1" is on p. 5; the roadmap on
  p. 3 assigns Sections 2--4 to Theorem 1). S5b's clause "the card records
  as pending" is not supported by the card (F1, refuted-as-stated). S2b
  compresses the card's read status (F3, note). S3c's parenthetical names
  a representation theorem as part of the incompleteness mechanism (F4,
  note). S2a and S2c lie outside the read set and are unverified.

## Weakest steps

**W1: the bridge in S3b (the theorem's conclusion to Problem 348's two
properties).** Fix $\alpha,\beta>0$ with $\alpha/\beta$ irrational and
write $A=A_{\alpha,\beta}$, an infinite set of positive integers. The
reconstructed theorem says: for every finite $F\subseteq\mathbb Z$ there
is $H$ such that every integer $m\ge H$ is a sum of distinct elements of
$A\setminus F$.

*Reading 1: the sequence is $A$ in increasing order (distinct values).*
Removing any $m$ elements means passing to $A\setminus F$ with $|F|=m$;
the theorem gives completeness of $A\setminus F$; so the first property
holds for every $m\ge0$ (with $F=\emptyset$ giving completeness of $A$
itself). The second property for a given $n$ says that every removal of
$n$ elements leaves an incomplete set; the theorem says every such
removal leaves a complete set; since $A$ is infinite there is at least
one $n$-element removal, so the second property fails for every $n\ge1$.
Pairs have $n>m\ge0$, hence $n\ge1$: no pair $(m,n)$ is witnessed.

*Reading 2: the sequence is the interleaving of
$(\lfloor2^k\alpha\rfloor)_{k\ge0}$ and $(\lfloor2^k\beta\rfloor)_{k\ge0}$
with repeated values kept as separate occurrences and sorted.* Delete any
$n$ occurrences. Let $F$ be the set of nonzero values all of whose
occurrences were deleted; $|F|\le n$. Every element of $A\setminus F$
still has an occurrence in the remaining multiset, and distinct values
have distinct positions, so every sum of distinct elements of
$A\setminus F$ is a sum of remaining occurrences at distinct positions.
By the theorem the remaining multiset is complete. Zero occurrences (when
$\lfloor\alpha\rfloor=0$ or $\lfloor\beta\rfloor=0$) change no sum and
their deletion changes no sum. So both properties behave exactly as in
Reading 1. The bridge holds under either convention, and no zero, index
or multiplicity subtlety breaks it.

**W2: the characterization in S3c of the exclusion of $m\ge2$.** From the
held PDF, Section 2: Lemma 3 (single-deletion tolerance forces the prefix
slack $S_j-b_{j+1}$ to infinity, also after any fixed finite deletion);
Theorem 2 (a complete nondecreasing positive sequence with threshold $T$
and diverging slack represents all of $[T,S_N-T]$ from its first $N$
terms for large $N$); Lemma 4 (a deletion-minimal sequence with such
central intervals has, for every $C$, two occurrences whose deletion
leaves arbitrarily late runs of more than $C$ consecutive missing
integers); Proposition 5 (if every two-occurrence deletion keeps
completeness, every finite deletion $D$ that keeps completeness can be
enlarged by one occurrence keeping completeness: otherwise $A\setminus D$
is deletion-minimal, Lemma 3 and Theorem 2 supply its central intervals,
Lemma 4 with $C=\sum D$ supplies two occurrences $E$ whose deletion leaves
gaps that restoring $D$ cannot fill, so $A\setminus E$ is incomplete, a
contradiction). The exclusion then reads: an $m$-tolerant sequence with
$m\ge2$ is two-tolerant, so some $n$-deletion keeps completeness, against
the required universal failure; the nonpositive-term and bounded cases
are reduced separately (p. 5). The engine that produces the contradiction
is Lemma 4's construction of long gaps after two deletions, an
incompleteness statement; Theorem 2 is a representation statement that
supplies Lemma 4's hypothesis. The section's "incompleteness mechanism"
describes the engine correctly; its parenthetical folds the input theorem
into the mechanism (F4). The clause "the folder holds no reconstruction"
is confirmed by the folder's page names: the two Geneson reconstruction
pages treat Theorem 9 and Corollary 12 only, and no page treats
Theorem 2, Lemma 4 or Proposition 5.

**W3: the scope phrase "of its theorem" in S3b.** Without the restriction
to the theorem's hypothesis the sentence would be false. Witness:
$\alpha=1$, $\beta=2$ give $A_{1,2}=\{1,2,4,8,\dots\}$, the powers of two
(the two floor sequences coincide up to a shift, and $0$ is excluded by
definition). This set is complete (binary expansion) and, after the
removal of any $n\ge1$ elements, one of them $2^k$, every sum of distinct
remaining elements has binary digit $k$ equal to $0$, so the infinitely
many integers with that digit equal to $1$ are missed: it is an example
for every pair $(0,n)$. Here $\alpha/\beta=1/2$ is a power of $2$, outside
the theorem's hypothesis and outside the rational-ratio lines the page's
first section transports (its conjecture convention excludes power-of-two
ratios). So the phrase "of its theorem" carries the irrational-ratio
hypothesis and is load-bearing; the sentence is correct as written, and
F2 asks only that the hypothesis be named.

## Strongest attack

- **S1.** Compared clause by clause with the Statement paragraph of the
  problem page ("remains complete after removing any $m$ elements, but $A$
  is not complete after removing any $n$ elements", for $0\le m<n$ and a
  nondecreasing sequence of integers). The paraphrase drops "of integers"
  and the nondecreasing ordering, neither of which changes the question
  for the section's purpose. Failed.
- **S2.** (b) Attacked by comparison with the card's read-status
  paragraph and the Theorem 1 result page: both record that the statement
  of Theorem 1 was read clause by clause and that its proof was read for
  structure only. The section's "a preprint claim read for structure
  only" attaches the structural reading to the claim rather than to its
  proof; it understates the card and changes no standing. Failed, with
  F3. (a) and (c) could not be attacked within the read set.
- **S3a.** Attacked by listing the folder's pages: the Geneson
  reconstructions are the Theorem 9 and Corollary 12 pages, and the
  Corollary 12 page rests on Theorem 9 and Proposition 11 only. Failed.
- **S3b.** Four attacks. (i) Convention: set against multiset; W1 shows
  the bridge holds under both. (ii) Quantifier: "not complete after
  removing any $n$ elements" read existentially ("some $n$-removal leaves
  it incomplete") would still fail for the theorem's sets, since every
  removal leaves them complete; read universally it fails a fortiori. No
  reading rescues a pair. (iii) Zero and multiplicity: $0$ is excluded
  from $A_{\alpha,\beta}$ and zero occurrences change no sum. (iv)
  Hypothesis: the powers-of-two witness of W3 shows the sentence would be
  false without the restriction to the theorem's sets, and the sentence
  carries that restriction. Failed.
- **S3c.** Attacked by arguing that the exclusion is a completeness
  mechanism, since Proposition 5's conclusion is completeness after some
  larger deletion. The conclusion is of that form, but its proof is by
  contradiction and the step doing the work is Lemma 4's production of
  arbitrarily long gaps; the characterization of the engine stands, and
  the parenthetical is imprecise only in naming Theorem 2 as part of it
  (F4). The "no counterpart" clause is a judgment about the descent
  argument, whose conclusion (a decreasing modular-run invariant forcing
  representation) points the opposite way from a deletion that destroys
  completeness; no counterexample to a judgment is possible, and none is
  claimed. Failed.
- **S4.** Follows from S3; no separate attack surface. Failed.
- **S5.** (b) Attacked by reading the card's provenance and read-status
  paragraphs, which record the structural reading of Sections 2--4 and
  no task, and by a word search over the card folder (exposure 2), which
  found the word "pending" only in sentences on the Theorem 1 and Theorem
  9 result pages saying that a separate triage of a problem page is
  pending. The card records no pending reconstruction or compilation
  task. Succeeded: refuted-as-stated, F1. (a) is a judgment.
- **S6.** The clause "the only link is the shared source" was checked
  against S3a--S3c: both Theorem 1 and the reconstructed Theorem 9 and
  Corollary 12 come from the same preprint, and nothing else in the read
  set connects the folder to the problem. Consistent; the rest is a
  judgment.

## Premises

- **Yu--Chen Theorem reconstruction**
  ([[research/erdos_354/yu_chen_theorem_reconstruction|page]]), read in
  full. Interface used: for $\alpha,\beta>0$ with $\alpha/\beta$
  irrational and every finite $F\subseteq\mathbb Z$ there is $H$ such
  that every integer $m\ge H$ is a sum of distinct elements of
  $A_{\alpha,\beta}\setminus F$; in particular $A_{\alpha,\beta}$ is
  strongly complete. Standing: an author-recorded reconstruction of an
  unrefereed manuscript, independently reviewed at the standing the
  assignment states; used here as a premise at that standing. The section
  uses only this conclusion, within its hypothesis.
- **Geneson Theorem 9 and Corollary 12 reconstructions**
  ([[research/erdos_354/geneson_theorem_9_reconstruction|Theorem 9]],
  [[research/erdos_354/geneson_corollary_12_reconstruction|Corollary 12]]),
  read in full. Used only to confirm S3a: their subjects are Theorem 9,
  Proposition 11 and Corollary 12 of the source; neither touches
  Theorem 1, Theorem 2, Lemma 3, Lemma 4 or Proposition 5.
- **Geneson (2026)**, arXiv:2609.25107v1, held PDF
  ([[../library/additive_bases/geneson_2026_deletion_thresholds_exponential_examples_complete_sequences/_index|card]]),
  text layer, pp. 1--5 read in full and p. 11 (closing line) and p. 3
  (roadmap) located. Interfaces: Theorem 1 (p. 1); Theorem 2 (p. 3),
  Lemma 3 (p. 3), Lemma 4 (p. 4), Proposition 5 (p. 4), the exclusion of
  $m\ge2$ (p. 5), as restated in W2. Card read status: statement of
  Theorem 1 checked clause by clause; proof read for structure only. The
  result pages' Statement sections for Theorem 1, Theorem 9 and
  Corollary 12 were read. A preprint; nothing in it is used as
  established, only as the object the section characterizes.
- **Yu and Chen (2026)**, manuscript of 13 September 2026, result page
  ([[../library/additive_bases/yu_chen_2026_erdos_problem_354_i_strong_completeness_two_dyadic_floor_sequences/theorem|Theorem]]),
  provenance and Statement read; the PDF was not opened, since the section
  invokes the theorem through the reconstruction.
- **Problem statements.** E0348 and E0354 Statement paragraphs, read in
  full; the section's S1 is checked against E0348.
- **Explicit assumptions.** The preamble's definitions of complete and
  strongly complete; the source's convention that completeness is
  eventual and counts occurrences. No batch acceptance order.

## Findings

- **F1 (required).** Location: lines 512--514, "A reconstruction of
  Geneson's Sections 2--4 is the separate compilation task the card
  records as pending." Defect: source fidelity. The card records that the
  proof of Theorem 1 (Sections 2--4) "was read for structure only"; it
  records no reconstruction or compilation task and does not use the word
  "pending" for one. Witness: the card's read-status paragraph (lines
  50--61 of its `_index.md`); the word search of exposure 2, whose only
  hits for "pending" are the result pages' sentences that a separate
  triage of a problem page is pending. Proposed replacement: "A
  reconstruction of Geneson's Sections 2--4 would be a separate
  compilation task; the card records that this proof was read for
  structure only."
- **F2 (suggested).** Location: lines 501--504, "the Yu--Chen mechanism
  produces completeness after every finite deletion: the sets
  $A_{\alpha,\beta}$ of its theorem satisfy the first property for every
  $m$ and the second for no $n$". Defect: the irrational-ratio hypothesis
  is carried only by "of its theorem", and it is load-bearing: the
  powers-of-two witness $A_{1,2}$ of W3 is an example for every pair
  $(0,n)$. Proposed replacement: "the sets $A_{\alpha,\beta}$ of its
  theorem ($\alpha/\beta$ irrational) satisfy ...".
- **F3 (note).** Location: lines 495--496, "the Geneson card records
  Theorem 1, the classification $m\le1$, as a preprint claim read for
  structure only." Defect: the card records the statement as read clause
  by clause and the proof as read for structure only; the sentence
  attaches the structural reading to the claim. It understates and
  changes no standing. Proposed replacement: "as a preprint claim whose
  proof was read for structure only."
- **F4 (note).** Location: lines 505--506, "an incompleteness mechanism
  (Geneson's central-interval Theorem 2 and his Lemma 4)". Defect:
  Theorem 2 is a representation theorem (central intervals are
  represented); the incompleteness step is Lemma 4, reached through
  Proposition 5, with Lemma 3 and Theorem 2 as its inputs (W2). Proposed
  replacement: "an incompleteness mechanism (Geneson's Lemma 4, fed by
  Lemma 3 and the central-interval Theorem 2 through Proposition 5)".

## Verdict

- **S1:** refutation-failed. A faithful paraphrase of the problem
  statement.
- **S2:** refutation-failed for clause (b), with the imprecision of F3;
  clauses (a) and (c) lie outside the commissioned read set and are
  unverified.
- **S3a:** refutation-failed.
- **S3b:** refutation-failed. The bridge from the theorem's universal
  conclusion to both of Problem 348's properties holds under both
  sequence conventions; the restriction to the theorem's sets is
  necessary and present (F2).
- **S3c:** refutation-failed for the record clauses; the parenthetical is
  imprecise (F4); the "no counterpart" clause is a judgment, not a claim.
- **S4:** refutation-failed, as a consequence of S3.
- **S5:** clause (a) is a judgment, not a claim; clause (b)
  refuted-as-stated (F1): the card does not record the task the sentence
  attributes to it.
- **S6:** the "shared source" clause is consistent with S3a--S3c; the
  rest is a judgment, not a claim.

**Limitations.** The review covers the section's sentences and the
preamble's conventions; the proofs of the reconstruction pages were taken
as premises at their reviewed standing and not re-derived here. The
source PDF was read in its text layer only, which suffices because the
section quotes no formula from it. S2(a) and S2(c) refer to text outside
the read set and were not checked. No computation was run; the
powers-of-two witness of W3 is a two-line argument.

This focused review assigns no tier and changes no status.
