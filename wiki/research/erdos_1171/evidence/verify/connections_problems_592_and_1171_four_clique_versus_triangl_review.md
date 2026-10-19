---
name: research/erdos_1171/evidence/verify/connections_problems_592_and_1171_four_clique_versus_triangl_review
title: "Independent review of the connections section: Problems 592 and 1171: four-clique versus triangle colors"
desc: |
  Refutation-failed for the conditional deduction, the exclusion of
  omega^{omega^2}, the necessary condition on answers, the shape dichotomy,
  the CH instance and the two ZFC instances at omega^{omega^2}; one outcome
  sentence is refuted at the boundary case beta = 0 and one is unresolved as
  stated, and one interface sentence of the lead is refuted as worded. Two
  required corrections, one suggested, three notes.
created: 2026-09-28T19:05:51Z
updated: 2026-09-28T20:42:19Z
---

***

## Subject and independence

The reviewer worked in a fresh context from the commissioned assignment
alone, took no part in writing the section, the lead, the reconstruction
pages or the library pages, and had no contact with their author.

The subject is the source as it stood on 2026-09-28T13:50:48Z (then the tip
of the default branch; called "the commit" below), file
`wiki/research/erdos_1171/connections.md`, section "Problems 592 and 1171:
four-clique versus triangle colors", lines 493--548 (the H2 at line 493 up
to the H2 at line 549), together with the lead page
`wiki/research/leads/four_clique_versus_triangle_colors/_index.md` at the
same commit, read in full.

Read as inputs, interfaces only: the page's frontmatter, Scope paragraph
and Tools section (lines 1--124), whose proofs another reviewer checks.
Read as premises, in full: the folder's two reconstruction pages,
`lemma_2_1_reconstruction.md` and `theorem_3_1_reconstruction.md`. Read at
statement depth: the statement blocks of `problems/set_theory/E0592/_index.md`
and `problems/set_theory/E1171/_index.md` (frontmatter and the text above
"Current assessment"); the provenance and read-status paragraphs of the
Schipperus 2010 card and the Statement sections of its `theorem_28` and
`theorem_29` pages; the provenance paragraph of the Komjáth 2025 card; the
Baumgartner and Hajnal 1987 card and the Statement and Specialization
sections of its `negative_relation` and `positive_relation` pages. Sources
read on the page images of the held PDFs: Schipperus, printed pp. 1195,
1197, 1209, 1211, 1212, 1213, 1214 and 1215 (the text layer for the
location of Theorems 19 and 21 only); Komjáth, printed pp. 425, 442
and 443. Guidance read: `docs/verification.md` ("Whole-claim report", "Audit
checklist", "Grading and claim standing"), `docs/approach_vetting.md`,
`docs/evidence.md` ("Source fidelity") and `docs/math_authoring.md`.

Exposures: the two problem pages' frontmatter `status` fields and the
one-word "**Status.**" entries inside their statement blocks (status words
only, no assessment text); the "Specialization to Problem 1171" sections of
the two Baumgartner and Hajnal result pages, which restate the statements
for $\kappa=\omega$; and the Komjáth card's provenance paragraph, which
summarizes what the survey records for Problem 1171. Not read: the folder
index, anything under `evidence/`, any Current assessment or Known results,
other sections' reviews, the arXiv report the section cites for its
outside status check (not held), and the web. Larson's paper and the
Baumgartner and Hajnal paper are not held; they enter only as reported by
Schipperus (p. 1197) and by Komjáth (pp. 425, 442--443) and the library's
review-based statements.

## Restatement

Conventions. $\alpha\to(\beta_0,\ldots,\beta_{n-1})^2_n$ is the relation of
the lemma page: every coloring of $[\alpha]^2$ with the colors
$0,\ldots,n-1$ has, for some $i<n$, a subset of order type $\beta_i$
homogeneous in color $i$; the subscript is omitted at two colors. A pair
of ordinals $(\alpha,\beta)$ is an *answer* when
$\alpha\not\to(\beta,4)^2$ and $\alpha\to(\beta,3,3,3)^2_4$ both hold. An
ordinal $\alpha$ is a *partition ordinal* when $\alpha\to(\alpha,3)^2$.
"Sum of $n$ indecomposables" counts the summands of the Cantor normal
form.

- **S1 (target).** Komjáth 2025, p. 443, records as unknown whether
  $\omega_1^2\to(\omega_1\omega,3,3,3)^2$ holds, "or at least" whether it
  is consistent that an answer exists, for some ordinals $\alpha,\beta$.
  The undecided case of Problem 592 is
  $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ for countable
  $\beta$ with exactly three summands.
- **S2 (core deduction).** For every ordinal $\alpha$: if
  $\alpha\to(\alpha,3)^2$ and $\alpha\not\to(\alpha,4)^2$, then
  $\alpha\to(\alpha,3,3,3)^2_4$, so $(\alpha,\alpha)$ is an answer, and
  the deduction is a theorem of ZFC.
- **S3 (instantiation).** For every countable $\beta$ that is a sum of
  exactly three indecomposables, $\alpha=\omega^{\omega^\beta}$ satisfies
  $\alpha\not\to(\alpha,4)^2$ (Theorem 29, part 2). Hence: if
  $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ for some such
  $\beta$, then $(\alpha,\alpha)$ is an answer in every model of ZFC in
  which the premise holds, and in ZFC if the premise is a theorem. The
  section states both sentences without "countable".
- **S4 (exclusion).** $(\omega^{\omega^2},\omega^{\omega^2})$ is not an
  answer, because $\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$ (Larson,
  as reported by Schipperus, p. 1197).
- **S5 (necessary condition).** Every answer $(\alpha,\beta)$ has
  $\beta\not\to(\beta,4)^2$.
- **S6 (shape dichotomy, lead).** If $(\alpha,\beta)$ is an answer and
  $\beta$ is a partition ordinal, then $(\beta,\beta)$ is an answer;
  otherwise $\beta\not\to(\beta,3)^2$, and then $\beta<\alpha$ (the
  section's "other shape").
- **S7 (CH instance).** In every model of CH,
  $(\omega_1^2,\omega_1\omega)$ is an answer exactly when
  $\omega_1^2\to(\omega_1\omega,3,3,3)^2$ holds there; this pair has
  $\beta<\alpha$.
- **S8 (ZFC instances at $\omega^{\omega^2}$, lead).** With
  $\alpha=\omega^{\omega^2}$: $\alpha\not\to(\alpha,6)^2$ and
  $\alpha\to(\alpha,3,3,3,3,3)^2_6$ hold in ZFC; and given Larson's
  $\alpha\not\to(\alpha,5)^2$, it holds together with
  $\alpha\to(\alpha,3,3,3,3)^2_5$.
- **S9 (interfaces).** Komjáth asks for some pair in some model, the
  deduction gives one pair in every model; Theorem 29's target $4$ is a
  four-element homogeneous set in the two-color convention of the lemma
  page; the lead adds "both relations are two-color relations in the
  convention of the lemma page".
- **S10 (structure of the source proof).** The proof of Theorem 28 runs
  through the dichotomy of Theorem 19, the homogeneous set of Theorem 21
  when every play of the Builder wins, and the triangle of Lemma 26 when
  the Architect has a winning strategy; only the triangle step is
  sensitive to the number of indecomposables (section: "Schipperus's proof
  of Theorem 28 says" this; lead: "the paper says" it, with the one-summand
  proof and the two-summand adaptation on p. 1211).
- **S11 (outcome sentences).** A positive outcome of the premise answers
  Komjáth's question in ZFC and extends the positive boundary of Problem 592.
  A negative outcome for every three-summand $\beta$ completes the
  classification of Problem 592 as "one or two indecomposables" and
  "leaves Komjáth's question to the other shape of answer"; the lead says
  the two side facts "fix the candidates" and that a negative outcome
  "returns Komjáth's question to the shape with $\beta<\alpha$".
- **S12 (provenance).** The section characterizes the arXiv report on the
  Isabelle formalization and refers to the Problem 1171 page's assessment.

## Checklist

- **Quantifiers and scope.** Fails in three places. S3's two sentences in
  the section range over all $\beta$ that are sums of three
  indecomposables, while Theorem 29 is a theorem about countable $\beta$
  (Schipperus, p. 1195, restricts the whole paper to countable ordinals,
  and the representation $W_\beta$ is built from ladders on countable
  intervals); the lead says "countable" (F1). S11's classification omits
  the boundary case $\beta=0$, where $\omega^{\omega^0}=\omega$ and
  $\omega\to(\omega,3)^2$ by Ramsey's theorem (F6). S11's "leaves ... to
  the other shape" excludes the shape $(\alpha,\alpha)$ at every other
  partition ordinal without an argument (F2). All other quantifiers match
  their sources: S1 was read on the page image; S2 is for every ordinal;
  S7 is for every model of CH.
- **Circularity.** None. The premise of S3 is open and labeled as such; the
  deduction consumes Lemma 2.1, whose hypothesis is the premise and not the
  conclusion, and nothing on the lead feeds the premise back.
- **Model and convention changes.** Pass, with one wording defect. The
  two-color relation of Schipperus's Definition 1 (p. 1195: color $0$
  carries the large order type, color $1$ the finite one) is the lemma
  page's relation at $n=2$; Komjáth's $\alpha\to(\beta,3,3,3)^2$ has four
  entries and is the four-color relation of the lemma's conclusion at
  $k=3$; Komjáth's negative relation is the same orientation (p. 443:
  "a $K_4$-free graph $X$ on $\omega_1^2$ with no independent set of type
  $\omega_1\omega$"). The lead's "both relations are two-color relations"
  misdescribes the four-color one (F3).
- **Finite and statistical overreach.** Not applicable: no finite
  computation or heuristic is used.
- **Uniformity.** Not applicable: $k$ is fixed at $3$, $4$ or $5$ in each
  use of Lemma 2.1 and no constant depends on a parameter.
- **Extremal conclusions.** Pass. "The smallest being $\beta=3$" is right:
  $0$, $1$ and $2$ have zero, one and two summands. The section makes no
  sharpness claim of its own beyond the sources' boundaries.
- **Consequences and composition.** Two consequence sentences fail (F2,
  F6). The compositions S2, S4, S5, S6, S7 and S8 were rederived below;
  S5 uses $\beta\le\alpha$, which the pages do not state but which follows
  from the positive relation (F4).
- **Computation.** Not applicable: no computation is claimed.
- **Reproduction.** Not applicable: no rerun instruction is claimed. The
  reading-depth statements ("statement depth", "read and not checked")
  agree with the library card's read-status paragraph.
- **Source and verdict fidelity.** Pass for the Komjáth quotation
  (p. 443, checked word for word on the page image), Theorem 29 (p. 1213),
  Theorem 28 (p. 1212), the Larson report (p. 1197, "improving the 6 in
  theorem 6.2 to a 5 and proving $\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$")
  and the Baumgartner and Hajnal relations (Komjáth p. 425 and p. 442).
  One misattribution: the sensitivity remark belongs to the opening of
  Section 10 (p. 1209), not to the proof of Theorem 28, and it also names
  the clique size (F5). The arXiv report's characterization and the
  reference to the Problem 1171 assessment are outside the read set and
  unverified here.

## Weakest steps

**W1: the core deduction (S2) and its composition with the question.**
Let $\alpha$ be an ordinal with $\alpha\to(\alpha,3)^2$ and
$\alpha\not\to(\alpha,4)^2$. Lemma 2.1 with $k=3$ (interface: $\alpha$ an
ordinal, hypothesis exactly $\alpha\to(\alpha,3)^2$) gives that every
$c:[\alpha]^2\to\{0,1,2,3\}$ has a subset of type $\alpha$ homogeneous in
color $0$ or a triangle in one of the colors $1,2,3$; that is
$\alpha\to(\alpha,3,3,3)^2_4$. Komjáth's second relation with
$\beta=\alpha$ is this relation read in his notation (four entries, four
colors). His first relation with $\beta=\alpha$ is the hypothesis. So
$(\alpha,\alpha)$ is an answer; the argument uses no axiom beyond ZFC, and
a ZFC theorem is in particular consistent. Komjáth's "for some ordinals
$\alpha,\beta$" admits $\alpha=\beta$; the reading is literal and the
section says so.

**W2: the necessary condition (S5).** Let $(\alpha,\beta)$ be an answer.
First $\beta\le\alpha$: under the constant coloring of $[\alpha]^2$ with
color $0$ there is no triangle in a color $\ge1$, so
$\alpha\to(\beta,3,3,3)^2_4$ yields a subset of $\alpha$ of order type
$\beta$, and a subset of an ordinal has order type at most that ordinal.
Now suppose $\beta\to(\beta,4)^2$. By (T2), whose hypothesis "$\gamma'$ has
a subset of type $\gamma$" is met with $\gamma=\beta$ and
$\gamma'=\alpha$, $\alpha\to(\beta,4)^2$, contradicting the answer. Hence
$\beta\not\to(\beta,4)^2$. The pages skip the step $\beta\le\alpha$ (F4).
The dichotomy S6 follows: if $\beta\to(\beta,3)^2$, Lemma 2.1 at $k=3$ and
$\beta\not\to(\beta,4)^2$ make $(\beta,\beta)$ an answer; otherwise
$\beta\ne\alpha$, since $\alpha\to(\alpha,3,3,3)^2_4$ gives
$\alpha\to(\alpha,3)^2$ by leaving three colors unused, so $\beta<\alpha$.

**W3: the negative-outcome consequence (S11).** Suppose
$\omega^{\omega^\beta}\not\to(\omega^{\omega^\beta},3)^2$ for every
countable $\beta$ with three summands. With Theorem 28 and Theorem 29,
part 3, the countable $\beta$ with the property of Problem 592 are then
exactly the sums of at most two indecomposables, the empty sum $\beta=0$
included ($\omega\to(\omega,3)^2$). What this does not do is confine
answers to the shape $\beta<\alpha$: a pair $(\alpha,\alpha)$ is an answer
whenever $\alpha$ is a partition ordinal with $\alpha\not\to(\alpha,4)^2$,
and for $\beta$ a single indecomposable other than $1$, or a sum of two
indecomposables other than $2$, Theorem 28 gives
$\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ while nothing cited
decides $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},4)^2$ either way:
Theorem 29 has no negative relation for one summand and only the $6$ for
two, Milner's all-$n$ result is for $\beta=1$ (p. 1196), and Schipperus
says the exact boundary is known only for $\beta=2$ (p. 1197). Uncountable
partition ordinals are not addressed at all.

## Strongest attack

- **S1.** Attempted: a different reading of Komjáth's sentence (the
  consistency question as tied to $\omega_1^2$ and $\omega_1\omega$). The
  page image reads "for some ordinals $\alpha,\beta$" with no further
  restriction; the attack fails. The identification of the undecided case
  rests on Theorem 28 (at most two summands) and Theorem 29, part 3 (four
  or more) at statement depth; no attack is possible without their proofs.
- **S2.** Attempted: a mismatch of color counts between Lemma 2.1's
  conclusion and Komjáth's four-entry relation, and a mismatch of
  orientation (which color carries the large set). Both conventions put
  the large order type in color $0$ and the finite targets in the other
  colors; the attack fails.
- **S3.** Attempted: an uncountable $\beta$ with three summands. For such
  $\beta$ Theorem 29 supplies nothing, so the section's unrestricted
  sentences are not proved; restricted to countable $\beta$, which is the
  reading the section's own identification with Problem 592 fixes and the
  lead states, the attack fails (F1).
- **S4.** Attempted: could $\omega^{\omega^2}$ serve with some other
  $\beta$? No: $\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$ gives, by
  (T2), $\omega^{\omega^2}\to(\beta,4)^2$ for every $\beta\le\omega^{\omega^2}$
  and $\alpha\to(\omega^{\omega^2},4)^2$ for every
  $\alpha\ge\omega^{\omega^2}$, so the ordinal serves in neither role. The
  claim is weaker than what holds; the attack fails. The input is
  Larson's theorem at report depth only.
- **S5, S6.** Attempted: an answer with $\beta>\alpha$, where (T2) would
  not apply. Such a pair is not an answer (W2); the attack fails once the
  omitted step is supplied (F4).
- **S7.** Attempted: an orientation mismatch in the CH relation. Komjáth's
  reformulation (p. 443) is a $K_4$-free graph with no independent set of
  type $\omega_1\omega$, the same orientation as Definition 1 and the
  lemma page; the "exactly when" is the definition of an answer given that
  relation; the attack fails.
- **S8.** Attempted: the summand count of $2$. It is $\omega^0+\omega^0$,
  two indecomposables, so Theorem 29, part 1, and Theorem 28 both apply;
  Lemma 2.1 at $k=5$ and $k=4$ gives the displayed relations. The $5$
  rests on Schipperus's report of Larson; the attack fails.
- **S9.** Attempted: read "both relations" as the two displayed relations.
  One of them has four colors, so the lead's sentence is false as worded;
  the intended check, that the premise and Theorem 29, part 2, are
  two-color relations in Definition 1's convention, holds (F3).
- **S10.** Attempted: check the attribution on the page images. The
  remark is the second sentence of Section 10 (p. 1209) and reads "It is
  only this last part of the proof that is sensitive to the number of
  indecomposables in $\beta$ and to the size of the finite clique"; the
  proof of Theorem 28 (p. 1212) does not contain it, and its own wording
  says "If the Builder has a winning strategy then ... there is a
  triangle", a slip against Lemma 26, which the lead reads correctly. The
  two-summand adaptation begins on p. 1211 as the lead says (F5).
- **S11.** Attempted and successful in two places: $\beta=0$ refutes the
  literal classification (F6), and W3 shows the exclusion of the shape
  $(\alpha,\alpha)$ is unsupported (F2). The positive-outcome half
  survives: it is S3 plus Theorem 28's boundary.
- **S12.** No attack possible inside the read set.

## Premises

- Lemma 2.1, `research/erdos_1171/lemma_2_1_reconstruction.md`, read in
  full, treated as established at its standing: for an ordinal $\alpha$
  with $\alpha\to(\alpha,3)^2$ and every finite $k\ge1$,
  $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$. Used at $k=3$ (S2, S6), $k=5$
  and $k=4$ (S8); every use has an ordinal and the exact hypothesis.
- Theorem 3.1 page, `research/erdos_1171/theorem_3_1_reconstruction.md`,
  read in full; nothing in the section consumes it. Its remark that CH
  gives $\omega_1\omega\not\to(\omega_1\omega,3)^2$ is consistent with S7's
  pair having $\beta\not\to(\beta,3)^2$ under CH but is not used.
- (T2) on the connections page: restriction and weakening, interface
  confirmed at each use ($\gamma'$ has a subset of type $\gamma$; unused
  colors). Its proof is another reviewer's subject.
- Schipperus 2010, held; Theorem 29, parts 1--3 (p. 1213), Theorem 28
  (p. 1212), Definition 1 (p. 1195), the Larson report and Theorem 4
  (p. 1197), the Section 10 remark (p. 1209), the two-summand discussion
  (p. 1211), Theorems 31--33 with the closing remark (pp. 1214--1215): read
  on the page images at statement depth; no proof checked. The library's
  `theorem_29` page notes that the printed proof of Theorem 33 treats
  exactly four summands; the section uses part 3 only in the outcome
  sentence and part 2 as its second half.
- Larson 2000, not held; enters only as Schipperus's report (p. 1197) of
  $\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$ and of the improvement of
  the $6$ to a $5$.
- Komjáth 2025, held; the Problem 54 discussion (pp. 442--443) and the
  Problem 13 commentary (p. 425) read on the page images.
- Baumgartner and Hajnal 1987, not held; the negative relation under CH,
  $\omega_1^2\not\to(\omega_1\omega,4)^2$, taken from the library's
  review-based `negative_relation` page and confirmed in Komjáth's
  restatements (pp. 425, 442--443).
- The arXiv report of Džamonja, Koutsoukou-Argyraki and Paulson, not held
  and not read; the section's characterization of it is unverified here.
- Problem statements: E0592 (countable $\beta$, red $K_\alpha$ or blue
  $K_3$ at $\alpha=\omega^{\omega^\beta}$) and E1171 (the relation for all
  finite $k$), statement blocks only.

## Findings

- **F1 (required).** Location: "Theorem 29(2) supplies the second half for
  every $\alpha=\omega^{\omega^\beta}$ with $\beta$ a sum of three
  indecomposables" and "if $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$
  for some $\beta$ that is a sum of three indecomposables, then Komjáth's
  question has a positive answer in ZFC". Defect: the quantifier ranges
  over all ordinals $\beta$, but Theorem 29 is a theorem about countable
  $\beta$ (the paper's standing restriction, p. 1195, and its
  representation of $\omega^{\omega^\beta}$ by trees built on countable
  ladders), so for uncountable $\beta$ the second half is not supplied.
  Witness: any uncountable $\beta$ with three summands, for which the
  cited theorem says nothing. Replacement: insert "countable" before
  $\beta$ in both sentences, as the lead already does.
- **F2 (required).** Location: section, "a negative outcome for every such
  $\beta$ ... leaves Komjáth's question to the other shape of answer";
  lead, "Two side facts fix the candidates" and "returns Komjáth's
  question to the shape with $\beta<\alpha$". Defect: a negative outcome
  removes only the three-summand ordinals from the shape
  $(\alpha,\alpha)$; every other partition ordinal whose four-clique
  relation is undecided remains a candidate through the other half, a
  proof of $\alpha\not\to(\alpha,4)^2$. Witness: $\beta=\omega$, where
  $\omega^{\omega^\omega}\to(\omega^{\omega^\omega},3)^2$ by Theorem 28
  and nothing cited decides
  $\omega^{\omega^\omega}\to(\omega^{\omega^\omega},4)^2$; likewise
  $\beta=\omega+1$, where Theorem 29, part 1, gives only the $6$ and
  Schipperus reports the exact boundary for $\beta=2$ alone (p. 1197).
  Replacement: "leaves the shape $(\alpha,\alpha)$ to the partition
  ordinals whose four-clique relation is undecided, $\omega^{\omega^\beta}$
  for $\beta$ a sum of one or two indecomposables other than $1$ and $2$
  and the uncountable partition ordinals, or to the other shape"; in the
  lead, "narrow the candidates" for "fix the candidates" and the same
  replacement for the return sentence. The desc's "are exactly the
  undecided case of Problem 592" is true as an identification and should
  not be read as a census of candidates.
- **F3 (suggested).** Location: lead, "The interfaces match: both
  relations are two-color relations in the convention of the lemma page".
  Defect: the nearest antecedent is the two displayed relations, and
  $\alpha\to(\beta,3,3,3)^2$ is a four-color relation. Witness: the
  displayed relation itself. Replacement: "the premise and Theorem 29,
  part 2, are two-color relations in Schipperus's Definition 1, which is
  the lemma page's relation at two colors, and Komjáth's
  $\alpha\to(\beta,3,3,3)^2$ is the four-color relation of the lemma's
  conclusion at $k=3$".
- **F4 (note).** Location: section, "any answer $(\alpha,\beta)$ has
  $\beta\not\to(\beta,4)^2$, because $\beta\to(\beta,4)^2$ would give
  $\alpha\to(\beta,4)^2$ by (T2)"; lead, the same "by restriction".
  Defect: (T2) needs a subset of $\alpha$ of type $\beta$, which the pages
  do not supply. Witness: none against the statement; the step follows
  from $\alpha\to(\beta,3,3,3)^2_4$ under the constant coloring (W2).
  Replacement: add "(an answer has $\beta\le\alpha$, since the constant
  coloring and $\alpha\to(\beta,3,3,3)^2$ give a subset of $\alpha$ of
  type $\beta$)".
- **F5 (note).** Location: section, "Schipperus's proof of Theorem 28
  says that only its triangle-in-color-$1$ step, Lemma 26, is sensitive
  to the number of indecomposables". Defect: the remark opens Section 10
  (p. 1209), not the proof of Theorem 28 (p. 1212), and it names two
  sensitivities, the number of indecomposables and the size of the finite
  clique; Lemma 26 is the one-summand case, the two-summand case being
  the discussion that follows it (p. 1211). The proof of Theorem 28 also
  passes first through the Erdős--Milner theorem (Theorem 27), which the
  lead's summary of the route omits. Replacement: "Section 10 of
  Schipperus (p. 1209) says that only the triangle step, Lemma 26 and its
  two-summand adaptation, is sensitive to the number of indecomposables
  and to the size of the finite clique".
- **F6 (note).** Location: section, "completes the classification of
  Problem 592 as 'one or two indecomposables'". Defect: the boundary case
  $\beta=0$, the empty sum, has the property, since
  $\omega^{\omega^0}=\omega$ and $\omega\to(\omega,3)^2$; Schipperus's
  Theorem 3 (p. 1196) says "at most two". Witness: $\beta=0$.
  Replacement: "at most two indecomposables".

## Verdict

- S1: refutation-failed.
- S2: refutation-failed.
- S3: refutation-failed for countable $\beta$, the reading fixed by the
  section's identification of the premise with the undecided case of
  Problem 592 and stated on the lead; the section's unrestricted wording
  is corrected by F1.
- S4: refutation-failed, at the depth of Schipperus's report of Larson.
- S5: refutation-failed, with the omitted step $\beta\le\alpha$ supplied
  in W2 (F4).
- S6: refutation-failed.
- S7: refutation-failed.
- S8: refutation-failed; the instance with $5$ rests on the reported
  Larson result.
- S9: refutation-failed for the section's two interface checks;
  refuted-as-stated for the lead's sentence "both relations are two-color
  relations", whose intended check holds (F3).
- S10: refutation-failed for the route's structure; the attribution of the
  sensitivity remark is corrected by F5.
- S11: refutation-failed for the positive-outcome sentence;
  refuted-as-stated for the classification "one or two indecomposables"
  at the boundary case $\beta=0$, the intended classification "at most
  two" surviving (F6); proof defective; statement unresolved for "leaves
  Komjáth's question to the other shape of answer" and the lead's "fix
  the candidates" and "returns Komjáth's question to the shape with
  $\beta<\alpha$" (F2).
- S12: not a mathematical claim; unverified inside the read set.

Limitations. Theorem 29, Theorem 28 and the Baumgartner and Hajnal
relation are consumed at statement depth from a refereed paper and from a
survey and a review; Larson's results only as reported. The premise of S3
is open and nothing here bears on it. The report says nothing about
whether Komjáth's question is answered elsewhere in the literature, which
the read set excludes. This focused review assigns no tier and changes no
status.
