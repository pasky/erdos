---
name: research/erdos_1171/evidence/verify/connections_problem_1169_two_color_and_finite_color_negative_review
title: "Independent review of the connections section: Problem 1169: two-color and finite-color negative relations"
desc: |
  Refutation-failed for the finite-color equivalence, the witness containment
  and the conditional strengthening; proof defective, statement unresolved for
  two conditional clauses of the context paragraph; zero required corrections,
  three suggested, three notes.
created: 2026-09-28T18:51:17Z
updated: 2026-09-28T18:51:17Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the assignment.
The reviewer took no part in writing the page or the folder's reconstruction
pages and had not read the page before this assignment. Charge: refutation of
every author-recorded statement of one section.

**Subject.** Page `wiki/research/erdos_1171/connections.md` as it stood on
2026-09-28T13:50:48Z, section
"## Problem 1169: two-color and finite-color negative relations on omega_1^2",
lines 259--317 (the heading is line 259; the next H2 is line 318). No lead
page is named beyond the section. The page's Scope paragraph (lines 18--30)
and Tools section (lines 32--123) were read as shared inputs.

**What was read, and at what depth.**

- The section in full. The Scope paragraph and the Tools section in full;
  the interfaces of (T1)--(T5) were confirmed at each use, and the proofs of
  (T4) and (T5) were re-derived for the reviewer's own use, since every
  mathematical statement of the section rests on them. Their proofs are
  another reviewer's subject.
- The reconstruction pages `lemma_2_1_reconstruction.md` and
  `theorem_3_1_reconstruction.md` in full, as premises at their reviewed
  standing.
- Problem pages: `wiki/problems/set_theory/E1169/_index.md` lines 1--34 (the
  frontmatter and the statement block; the page has no "Statement" heading,
  so the block between the H1 and the first H2 was taken as the statement)
  and `E1171.md` lines 1--75 (the same block), plus the heading lists of both
  pages and a count, with no content, of the lines of `E1171.md` mentioning
  the arXiv identifier `2608.13213` (one line).
- Library: the booklet card
  [[../library/number_theory/various_1999_some_pauls_favorite_problems/_index|Some of Paul's favorite problems (1999)]]
  in full, its transcription at items 7.84--7.91, and the page images of PDF
  pp. 8--9 (item 7.85 on the right leaf of p. 8, printed p. 13);
  [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth 2025]]:
  the card in full, the conversion at Problem 13, and the page image of PDF
  p. 8 (printed p. 425);
  [[../library/set_theory/baumgartner_1989_remarks_partition_ordinals/_index|Baumgartner 1989]]:
  the card and the main-theorem result page in full;
  [[../library/set_theory/baumgartner_1987_remark_partition_relations_infinite_ordinals/_index|Baumgartner and Hajnal 1987]]:
  the card and the positive-relation result page in full.
- Wiki: `docs/verification.md` "Grading and claim standing" and the shared
  "Audit checklist", and the Erdos-specific "Whole-claim report" and "Audit
  checklist"; `docs/approach_vetting.md` in full; `docs/evidence.md` "Source
  fidelity"; `docs/math_authoring.md` in full.

**Exposures.** Four, none a review, grade, index, assessment or standing text
about the subject: (1) the preceding section of the same page, "Problem 1171
in ZFC: descent chains and their obstruction", lines 125--258, was read in
full; it is not a shared section, and it carries author-recorded mathematics
only; (2) the frontmatter `status:` lines of both problem pages, and the
Source paragraph inside the E1171 statement block, which quotes the catalog's
status label and one-line remark; (3) the library cards and result pages
beyond their provenance paragraphs and statement sections: Bears-on rows,
result summaries, and the author-recorded "Consequence for Problem 1171"
section of the Baumgartner 1989 result page; (4) the heading lists of the
problem pages, line numbers and names only; the E1169 page has a "Current
assessment" heading at line 35 whose content was not read. No folder index,
no file under any `evidence/` folder, no Known-results or assessment text and
no web page reached the reviewer.

## Restatement

Conventions are those of the lemma page: a coloring of $[\alpha]^2$ with the
colors $0,\ldots,k$; a set is homogeneous in color $i$ when all its pairs have
color $i$; $\alpha\to(\beta,3,\ldots,3)^2_{k+1}$ with $k$ triangle colors
means that every such coloring has a subset of type $\beta$ homogeneous in
color $0$ or a three-element set homogeneous in some color $j\ge1$; a
*witness* for the negative relation is a coloring with neither. A witness for
$\alpha\not\to(\alpha,3)^2$ is the same thing as a triangle-free graph on
$\alpha$ (color $1$) with no independent set of type $\alpha$.

- **S1 (forms of the question).** The catalog page, as the problem page
  reproduces it, asks "for all finite $k<\omega$" whether
  $\omega_1^2\not\to(\omega_1^2,3)^2$, a display in which $k$ does not occur;
  the booklet item [Va99, 7.85] asks the same relation with no quantifier and
  adds that Hajnal derived it from CH; the catalog cites [Ha71] and lists no
  proof claim.
- **S2 (the open part).** Under CH the negative relation holds (Hajnal 1971,
  not held). What is open is whether it is a theorem of ZFC, equivalently
  whether $\omega_1^2\to(\omega_1^2,3)^2$ is consistent with ZFC; Komjáth
  2025, Problem 13 commentary, records that consistency as open as far as he
  knows.
- **S3 (finite-color equivalence).** For every finite $k\ge1$,
  $\omega_1^2\not\to(\omega_1^2,3)^2$ if and only if
  $\omega_1^2\not\to(\omega_1^2,3,\ldots,3)^2_{k+1}$ with $k$ triangle
  colors.
- **S4 (witness containment).** For every witness
  $c:[\omega_1^2]^2\to\{0,\ldots,k\}$ of the $k$-triangle-color negative
  relation there are $Y\subseteq\omega_1^2$ with
  $\operatorname{otp}(Y)=\omega_1^2$ and $j\in\{1,\ldots,k\}$ such that the
  two-coloring of $[Y]^2$ giving color $1$ to the pairs of $c$-color $j$ and
  color $0$ to all other pairs, pulled back to $\omega_1^2$ along the order
  isomorphism, witnesses $\omega_1^2\not\to(\omega_1^2,3)^2$.
- **S5 (harmlessness of the stray quantifier).** Reading the catalog's $k$ as
  the number of triangle colors, the catalog's statement is equivalent to the
  booklet's "for every $k$"; the display just above fixes $k\ge1$.
- **S6 (conditional strengthening).** In every model of ZFC in which
  $\omega_1^2\to(\omega_1^2,3)^2$ holds,
  $\omega_1^2\to(\omega_1^2,3,\ldots,3)^2_{k+1}$ holds for every finite $k$;
  this is the relation of Problem 1171 with $\omega_1^2$ in place of
  $\omega_1\omega$, it implies the Problem 1171 relation
  $\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ and is therefore stronger
  than what $\mathrm{MA}_{\aleph_1}$ gives; its premise is the open
  consistency question of S2, which the section does not attack.
- **S7 (limitation).** The mechanism produces positive relations from
  positive relations and yields nothing toward the ZFC question; toward the
  negative relation it yields only S4.
- **S8 (context, conditional on an unheld, unrefereed abstract).** If the
  abstract's claims hold, namely (i) a finite-support iteration of
  $\sigma$-centered forcings over a model of CH carrying Hajnal's coloring
  yields a model of $\mathrm{MA}_{\omega_1}(\sigma\text{-centered})$,
  $2^{\aleph_0}=\aleph_2$ and $\omega_1^2\not\to(\omega_1^2,3)^2$, and (ii)
  under $\mathrm{MA}_{\omega_1}$ every c.c.c. forcing preserves an existing
  witness, then (a) the negative relation is compatible with a fragment of
  Martin's axiom, (b) "unlike $\omega_1\omega\not\to(\omega_1\omega,3)^2$",
  and (c) a model of the positive relation is not reached from a model of CH
  by such iterations.
- **S9 (cross-references).** The E1169 page carries the status
  `not_disprovable` and no compiled assessment; the E1171 page's search log
  lists the preprint; S6 is the folder index's remark with its proof.
- **S10 (outcome).** The mechanism transfers conditionally and gives no
  lead, because the premise of S6 is the open problem itself and "the
  unconditional conclusion for Problem 1171 is already known by the
  $\mathrm{MA}_{\aleph_1}$ route".

## Checklist

- **Quantifiers and scope.** S3 and S4 carry $k\ge1$ and hold for each such
  $k$. S6's "for every $k$" holds at $k=0$ as well: with one color the whole
  of $\omega_1^2$ is homogeneous. S5's prose "for every $k$", read with the
  catalog's "$k<\omega$", includes $k=0$, where the negative one-color
  relation is false outright, so the sentence needs the display's range
  (F1). S8(c) quantifies over all "such iterations" where the paraphrased
  source supplies one (F3). Pass for S3, S4 and S6; two scoped findings.
- **Circularity.** None. S6 takes the open positive relation as an explicit
  premise and never feeds it back into S2 or S3; the induction behind (T5)
  descends on the number of colors and presupposes nothing about its
  conclusion. Pass.
- **Model and convention changes.** The relation, witness, transport and
  order-type conventions are the lemma page's, and colorings and graphs are
  interchanged only through the identification stated above. S8(b) changes
  the hypothesis from Theorem A's full $\mathrm{MA}_{\aleph_1}$ to the
  fragment $\mathrm{MA}_{\omega_1}(\sigma\text{-centered})$ without a bridge
  (F2). Pass elsewhere.
- **Finite and statistical overreach.** No finite verification, sample or
  heuristic is used. Not applicable.
- **Uniformity.** No constants or error terms; each statement is proved for
  each finite $k$ by the same argument, with no parameter dependence to
  track. Pass.
- **Extremal conclusions.** The one comparative claim is "stronger" in S6.
  The implication holds by (T2), and the two relations differ under CH at
  $k=1$ (Erdős and Hajnal's ZFC theorem
  $\omega_1^2\to(\omega_1\omega,3)^2$ against Hajnal's CH
  $\omega_1^2\not\to(\omega_1^2,3)^2$), so the comparison is even strict,
  although the section claims only the implication. Pass.
- **Consequences and composition.** "hence the relation of Problem 1171 with
  the target $\omega_1^2$ in place of $\omega_1\omega$" is the same relation
  under another name: pass. "So the stray quantifier is harmless": F1. "If
  so, the negative relation, unlike ...": F2. "a model of the positive
  relation is not reached ...": F3. "the unconditional conclusion ... is
  already known": F4. The composition behind S6 is Lemma 2.1 at
  $\alpha=\omega_1^2$ followed by (T2); it inherits no premise beyond the one
  the section states.
- **Computation.** None. Not applicable.
- **Reproduction.** No rerun instructions or coverage claims. Not applicable.
- **Source and verdict fidelity.** Komjáth's sentence was checked on the page
  image (PDF p. 8, printed p. 425): "The consistency of
  $\omega_1^2\to(\omega_1^2,3)^2$ is, as far as I know, open." Pass. The
  booklet item was checked on the page image (PDF p. 8, right leaf, printed
  p. 13): "7.85 (Erdős, Hajnal) Is it true that
  $\omega_1^2\not\to(\omega_1^2,3)^2$? [Hajnal showe-" with the right margin
  cropped, then "this follows from CH.]"; the item has no quantifier, as the
  section says; the quotation follows the transcription's "shows" and omits
  the printed attribution (F5, a note). The catalog page and the arXiv
  abstract lie outside the read set, so the section's characterization of
  them is unverified here. The E1169 status value matches the frontmatter;
  "no compiled assessment" was not checked, since the page's "Current
  assessment" heading has content excluded from this review. The E1171 page
  mentions the preprint's identifier once (count only). "This is the folder
  index's remark" was not checked, the index being excluded.

## Weakest steps

**W1. (T5) at $\alpha=\omega_1^2$, and the equivalence S3.** Let $c$ witness
$\omega_1^2\not\to(\omega_1^2,3,\ldots,3)^2_{k+1}$. For $k=1$ take
$Y=\omega_1^2$, $j=1$. For $k\ge2$ let $c'$ merge the colors $0$ and $k$ of
$c$. If $c'$ has $Y$ of type $\omega_1^2$ homogeneous in color $0$, then $c$
takes only the values $0$ and $k$ on $[Y]^2$; the two-coloring $d$ of $[Y]^2$
with $d=1$ exactly on the $c$-color-$k$ pairs has no color-$1$ triangle, which
would be a $c$-color-$k$ triangle, and no color-$0$ subset of type
$\omega_1^2$, which would be a $c$-color-$0$ homogeneous subset of
$\omega_1^2$ of type $\omega_1^2$. Otherwise $c'$ has no color-$0$ subset of
type $\omega_1^2$ and, agreeing with $c$ on the colors $1,\ldots,k-1$, no
triangle in them, so $c'$ is a witness with $k-1$ triangle colors and the
induction gives $Y$ and $j\le k-1$; the two-colorings built from $c'$ and
from $c$ with this $j$ are the same function. Pulling $d$ back along the
order isomorphism $\pi:\omega_1^2\to Y$ gives a coloring of $[\omega_1^2]^2$
whose color-$0$ homogeneous sets are the $\pi$-preimages of those of $d$, of
the same order type, and whose color-$1$ triangles are preimages of
triangles; so it witnesses $\omega_1^2\not\to(\omega_1^2,3)^2$. This is S4,
and it is the backward direction of S3. The forward direction: a witness
$c:[\omega_1^2]^2\to\{0,1\}$ is a coloring with the colors $0,\ldots,k$
leaving $2,\ldots,k$ unused; it has no color-$0$ set of type $\omega_1^2$, no
color-$1$ triangle, and no triangle in an unused color, since a triangle
needs three pairs of that color. This is the contrapositive of the
unused-color clause of (T2). Both directions compose into the contrapositive
of the equivalence displayed at the end of the Tools section.

**W2. The boundary $k=0$ in S5.** With $k=0$ triangle colors the relation
reads $\omega_1^2\to(\omega_1^2)^2_1$: there is exactly one coloring of
$[\omega_1^2]^2$ with one color, and under it $\omega_1^2$ itself is
homogeneous of type $\omega_1^2$; the relation holds and its negation fails.
So the catalog's sentence, read with $k$ triangle colors over all $k<\omega$,
is false, while the booklet's question is consistently true (CH). The two are
equivalent exactly on $k\ge1$, the range of the section's display; the prose
sentence does not carry the range. The sibling theorem page treats the
analogous instance $k=0$ of Problem 1171 explicitly, where it holds.

**W3. The comparison in S6.** The premise $\omega_1^2\to(\omega_1^2,3)^2$ is
the hypothesis of Lemma 2.1 with $\alpha=\omega_1^2$, an ordinal, so the
reviewed reconstruction gives $\omega_1^2\to(\omega_1^2,3,\ldots,3)^2_{k+1}$
for every finite $k\ge1$, and $k=0$ holds outright. Since $\omega_1\omega$ is
an initial segment of $\omega_1^2$, a subset of type $\omega_1^2$ has a
subset of type $\omega_1\omega$, so (T2) with $\beta'=\omega_1\omega$ gives
$\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$, the Problem 1171
relation. The step uses neither $\mathrm{MA}_{\aleph_1}$ nor Theorem A; the
comparison with the $\mathrm{MA}_{\aleph_1}$ route is a comparison of
conclusions, not a composition with it.

## Strongest attack

- **S3 and S4.** Attempted to build a many-color witness containing no
  two-color witness on a subset of full type. With $k=2$: choose $c$ with no
  color-$0$ set of type $\omega_1^2$ and no triangle in the colors $1$, $2$,
  and merge $0$ with $2$ into $c'$. Either $c'$ has a color-$0$ set $Y$ of
  type $\omega_1^2$, and then the $c$-color-$2$ graph on $Y$ is triangle-free
  with every independent set of type below $\omega_1^2$, because an
  independent set is $c$-color-$0$ homogeneous in $\omega_1^2$; or $c'$ is
  itself a two-color witness on $\omega_1^2$. The attack fails for every $k$
  by the descent of W1, since the merged coloring is a witness with one fewer
  triangle color. A second attack on the transport, that the pulled-back
  coloring could acquire a color-$0$ set of type $\omega_1^2$, fails because
  an order isomorphism carries pairs to pairs and preserves order type in
  both directions. Refutation failed.
- **S5.** The $k=0$ instance of W2 refutes the prose "for every $k$" under
  the literal reading "$k<\omega$" and does not touch the displayed range
  $k\ge1$ (F1).
- **S6.** Attempted to find a model of $\omega_1^2\to(\omega_1^2,3)^2$ in
  which some $\omega_1^2\to(\omega_1^2,3,\ldots,3)^2_{k+1}$ fails:
  impossible, Lemma 2.1 is a theorem of ZFC for every ordinal. Attempted to
  deny "stronger": (T2) gives the implication, and strictness under CH is
  recorded in the checklist. Attempted to read the conditional as
  unconditional: the section states the premise and calls it the open
  consistency question. Refutation failed.
- **S2.** "The negative relation is a theorem of ZFC" is equivalent to "ZFC
  refutes the positive relation", that is, to "ZFC together with the positive
  relation is inconsistent"; so "not a theorem" is equivalent to "the
  positive relation is consistent". Refutation failed. Komjáth's own phrasing
  of Hajnal's hypothesis, $\kappa^{<\kappa}=\kappa$, holds at
  $\kappa=\omega$ in ZFC and would make the negative relation a ZFC theorem,
  against the same page's "open"; the section uses the CH form of the catalog
  and the booklet, and its sibling section records the discrepancy, so no
  error attaches to the section under review.
- **S8(b).** Attempted to support the strong reading, that the fragment
  $\mathrm{MA}_{\omega_1}(\sigma\text{-centered})$ already excludes
  $\omega_1\omega\not\to(\omega_1\omega,3)^2$. That needs Baumgartner's
  argument to run on $\sigma$-centered partial orders; nothing held states
  it, and the corpus states Theorem A under full $\mathrm{MA}_{\aleph_1}$
  for every c.c.c. partial order. The weak reading, that full
  $\mathrm{MA}_{\aleph_1}$ excludes it, follows from Theorem A. The sentence
  does not say which it means (F2).
- **S8(c).** Attempted to derive the universal clause from the paraphrased
  abstract: claim (i) supplies one iteration, and claim (ii) needs
  $\mathrm{MA}_{\omega_1}$ in the ground model, which a model of CH lacks.
  The reviewer's closest independent support is a one-step statement. Let
  $W$ be a graph on $\omega_1^2$ in $V$ with no independent set of type
  $\omega_1^2$, let $P=\bigcup_n C_n$ be $\sigma$-centered with each $C_n$
  centered, and suppose $p$ forces that $\dot X\subseteq\omega_1^2$ is
  independent in $W$ and has type $\omega_1^2$. Put
  $A_n=\{x<\omega_1^2 : \text{some } q\le p \text{ in } C_n \text{ forces } x\in\dot X\}$.
  Each $A_n$ is independent in $W$: two of its points have conditions in
  $C_n$ with a common extension, which forces both into $\dot X$ and hence
  forces the pair out of $W$, and $W$ lies in $V$. In $V[G]$ with $p\in G$,
  $X\subseteq\bigcup_n A_n$. Write $B_\eta=[\omega_1\eta,\omega_1(\eta+1))$
  for $\eta<\omega_1$. A sum over $\eta<\omega_1$ of terms at most $\omega_1$
  in which only countably many terms equal $\omega_1$ is below
  $\omega_1\cdot\omega_1$: the countable terms between two consecutive
  $\omega_1$-terms sum to at most $\omega_1$, so the whole sum is at most
  $\omega_1\cdot\gamma$ for a countable $\gamma$. Hence uncountably many
  $\eta$ have $X\cap B_\eta$ uncountable; for each, some $n$ has
  $A_n\cap B_\eta$ uncountable in $V[G]$, hence in $V$; one $n$ serves
  uncountably many $\eta$; the set of those $\eta$ lies in $V$ and is
  uncountable in $V[G]$, hence in $V$; so in $V$ the set $A_n$ meets
  uncountably many blocks in sets of type $\omega_1$, has type $\omega_1^2$
  and is independent in $W$, a contradiction. So one $\sigma$-centered
  forcing preserves every witness. This does not reach a finite-support
  iteration whose initial segments are not themselves $\sigma$-centered, and
  the section supplies no argument of its own; the clause stays unresolved
  (F3).
- **S1 and S9.** The verifiable parts (the problem page's statement block,
  the booklet item, the status value, the count of preprint mentions) pass;
  the rest is outside the read set.

## Premises

- [[research/erdos_1171/lemma_2_1_reconstruction|Lemma 2.1 reconstruction]],
  read in full. Interface: for an ordinal $\alpha$ with
  $\alpha\to(\alpha,3)^2$ and every finite $k\ge1$,
  $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$ with $k$ triangle colors, in ZFC,
  with its transport and relabeling facts. Independently reviewed as it stood
  on 2026-09-28T05:03:27Z; used by the section, through (T3), at
  $\alpha=\omega_1^2$, within its hypotheses.
- [[research/erdos_1171/theorem_3_1_reconstruction|Theorem 3.1 reconstruction]],
  read in full. Interface: under $\mathrm{MA}_{\aleph_1}$, Martin's axiom for
  $\aleph_1$ dense sets of every c.c.c. partial order,
  $\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ for every finite
  $k\ge1$, through Theorem A (Baumgartner 1989, §3, the case $n=3$; the
  chapter is not held) and Lemma 2.1; Theorem C (Solovay and Tennenbaum, not
  held) for relative consistency; its fidelity note treats the instance
  $k=0$. Independently reviewed as it stood on 2026-09-28T05:03:27Z; used only
  as the comparison point of S6 and S10.
- The Tools section of the page, lines 32--123: (T1) transport along order
  isomorphisms; (T2) restriction, weakening of the large target, embedding of
  targets, and unused colors; (T3) the constant case of (T4); (T4) the
  descent lemma; (T5) witness extraction, with the displayed equivalence.
  Interfaces confirmed; proofs of (T4) and (T5) re-derived here; the Tools
  section's own standing is another reviewer's subject.
- [[../library/set_theory/baumgartner_1989_remarks_partition_ordinals/main_theorem|Baumgartner 1989, main theorem]],
  statement section: $\mathrm{MA}_{\aleph_1}$ implies
  $\omega_1\omega\to(\omega_1\omega,n)^2$ and
  $\omega_1\omega^2\to(\omega_1\omega^2,n)^2$ for every finite $n$, and the
  hypothesis cannot be dropped, since CH gives $\alpha\not\to(\alpha,3)^2$
  for both ordinals (Erdős and Hajnal, as the zbMATH review reports). The
  chapter is not held; the statement is the review's account. Used for the
  weak reading of S8(b).
- [[../library/set_theory/baumgartner_1987_remark_partition_relations_infinite_ordinals/positive_relation|Baumgartner and Hajnal 1987, positive relation]],
  statement section: $\omega_1^2\to(\omega_1\omega,3,3)^2$ in ZFC, containing
  $\omega_1^2\to(\omega_1\omega,3)^2$, which Komjáth attributes to Erdős and
  Hajnal (1970). The paper is not held. Used only in the reviewer's
  strictness remark under the extremal item.
- [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth 2025]],
  held; Problem 13 commentary read on the page image of PDF p. 8 (printed
  p. 425): the consistency of $\omega_1^2\to(\omega_1^2,3)^2$ is open as far
  as the author knows; Hajnal's negative relation is stated there under
  $\kappa^{<\kappa}=\kappa$ in [76]; Erdős and Hajnal's
  $\omega_1^2\to(\omega_1\alpha,3)^2$ for $\alpha<\omega_1$ in [40].
- [[../library/number_theory/various_1999_some_pauls_favorite_problems/_index|The 1999 booklet]],
  held scan without a text layer; item 7.85 read on the page image of PDF
  p. 8, right leaf (printed p. 13), and in the retained transcription at
  line 363; item 7.84 on the same leaf carries the quantifier "for every
  $k<\omega$" that the catalog's Problem 1169 sentence repeats.
- Problem pages `E1169.md` and `E1171.md`, statement blocks: the catalog
  sentences with their quantifiers, the references [Ha71] and, for E1171,
  [Va99, 7.84], [Ko25], [Ba89b], [BaHa87], [SoTe71], [Ga26].
- Not held and not read: Hajnal 1971 [Ha71]; Erdős and Hajnal 1970; the
  catalog pages for Problems 1169 and 1171; the arXiv abstract
  `2608.13213`. The section's sentences about them are recorded here as
  unverified, not as refuted.
- Explicit assumptions: Con(ZFC) behind "theorem of ZFC" versus
  "consistent"; the reading of the catalog's $k$ as a number of triangle
  colors, which the section states.

## Findings

- **F1 (suggested).** Location: "So the stray quantifier is harmless: read
  with $k$ triangle colors, the catalog's statement is equivalent to the
  booklet's for every $k$". Defect: the catalog quantifies over all finite
  $k<\omega$, and at $k=0$ the relation with $k$ triangle colors is the
  one-color relation $\omega_1^2\to(\omega_1^2)^2_1$, which holds outright,
  so its negation is false and the catalog's sentence, read literally with
  $k$ triangle colors, is false rather than equivalent to the booklet's
  question; the equivalence holds exactly for $k\ge1$, the range of the
  display but not of the sentence. Witness: $k=0$ (W2). Proposed
  replacement: "So the stray quantifier is harmless once $k$ ranges over
  $k\ge1$: read with $k$ triangle colors, the catalog's statement is
  equivalent to the booklet's for every $k\ge1$, while the instance $k=0$ is
  the one-color relation $\omega_1^2\to(\omega_1^2)^2_1$, which holds
  outright, as the theorem page notes for the same instance of Problem 1171."
- **F2 (suggested).** Location: "If so, the negative relation, unlike
  $\omega_1\omega\not\to(\omega_1\omega,3)^2$, is compatible with a fragment
  of Martin's axiom". Defect: on its natural reading the contrast asserts
  that the same fragment, $\mathrm{MA}_{\omega_1}(\sigma\text{-centered})$,
  excludes $\omega_1\omega\not\to(\omega_1\omega,3)^2$; the read set supports
  only that full $\mathrm{MA}_{\aleph_1}$ excludes it (Theorem A), and no
  held statement says that Baumgartner's argument needs only
  $\sigma$-centered partial orders. Witness: Theorem A's hypothesis as the
  corpus states it. Proposed replacement: "If so, the negative relation is
  compatible with the fragment
  $\mathrm{MA}_{\omega_1}(\sigma\text{-centered})$, whereas
  $\omega_1\omega\not\to(\omega_1\omega,3)^2$ contradicts full
  $\mathrm{MA}_{\aleph_1}$ (Theorem A); whether that fragment alone already
  excludes $\omega_1\omega\not\to(\omega_1\omega,3)^2$ is not settled by
  anything held here."
- **F3 (suggested).** Location: "and a model of the positive relation is not
  reached from a model of CH by such iterations". Defect: the paraphrased
  abstract states that one finite-support iteration of $\sigma$-centered
  forcings over a CH model with Hajnal's coloring preserves the witness, and
  that over a model of $\mathrm{MA}_{\omega_1}$ every c.c.c. forcing
  preserves an existing witness; neither quantifies over all finite-support
  iterations of $\sigma$-centered forcings over a CH model, which "such
  iterations" asserts, and the section adds no argument. Witness: the
  paraphrase's own quantifiers, and the absence of $\mathrm{MA}_{\omega_1}$
  in a CH ground model. Proposed replacement: "and the iteration the
  abstract describes does not reach a model of the positive relation".
- **F4 (note).** Location: "the unconditional conclusion for Problem 1171 is
  already known by the $\mathrm{MA}_{\aleph_1}$ route". Defect: that route's
  conclusion is conditional on $\mathrm{MA}_{\aleph_1}$; what is known
  without condition is the relative consistency of the Problem 1171 relation
  (Theorem C). Proposed replacement: "the consistency of the Problem 1171
  relation is already known outright by the $\mathrm{MA}_{\aleph_1}$ route,
  while the strengthening's premise is not known to be consistent".
- **F5 (note).** Location: the quotation "Is it true that
  $\omega_1^2\not\to(\omega_1^2,3)^2$? [Hajnal shows this follows from
  CH.]", attributed to the retained transcription. Defect: on the page image
  (PDF p. 8, right leaf, printed p. 13) the item reads "7.85 (Erdős, Hajnal)
  Is it true that $\omega_1^2\not\to(\omega_1^2,3)^2$? [Hajnal showe-" with
  the right margin cropped, then "this follows from CH.]"; the transcription's
  "shows" is a reading of a cropped word, and the printed attribution is not
  in the quotation. No mathematical content changes; "has no quantifier" is
  confirmed. Proposed replacement: cite the page image beside the
  transcription, quote the item with its attribution, and mark the cropped
  verb.
- **F6 (note).** Location: "Second, by (T3) and (T2), every model of
  $\omega_1^2\to(\omega_1^2,3)^2$ satisfies ...". Defect: none in the
  mathematics; (T3) at $\alpha=\omega_1^2$ with all targets $3$ is exactly
  Lemma 2.1, the folder's independently reviewed reconstruction, whereas
  (T3) itself is proved only on this page as a case of (T4), and (T2) enters
  only in the comparison sentence that follows. Proposed replacement: "by
  Lemma 2.1 at $\alpha=\omega_1^2$ (the constant case of (T3))", with (T2)
  cited at "stronger than".

## Verdict

- **S1.** refutation-failed for the parts inside the read set (the problem
  page's statement block reproduces the quantified sentence and cites
  [Ha71]; the booklet item has no quantifier); the catalog page's access
  date, edit date and proof-claim tab are unverified here.
- **S2.** refutation-failed. Komjáth's "open" sentence is verified on the
  page image; the equivalence between "not a theorem of ZFC" and "consistent"
  is standard given Con(ZFC).
- **S3.** refutation-failed.
- **S4.** refutation-failed.
- **S5.** refutation-failed for the displayed range $k\ge1$; the prose "for
  every $k$" fails at $k=0$ under the catalog's "$k<\omega$" and needs the
  range stated (F1).
- **S6.** refutation-failed.
- **S7.** not a claim: a scope statement about the mechanism, consistent with
  (T5) and with everything above.
- **S8(a).** refutation-failed as a conditional deduction from the
  paraphrased abstract, whose content is unverified here.
- **S8(b).** proof defective; statement unresolved: the strong reading has no
  bridge in the read set, the weak reading follows from Theorem A, and the
  sentence does not fix which it asserts (F2).
- **S8(c).** proof defective; statement unresolved: the universal clause is
  not derived from the paraphrase or from anything the section supplies
  (F3); the reviewer's one-step derivation does not close the gap.
- **S9.** refutation-failed for the status value and the count of preprint
  mentions; "no compiled assessment" and "the folder index's remark" are
  outside the read set and unverified.
- **S10.** not a claim, except the wording noted in F4; the underlying fact,
  that the Problem 1171 relation is consistent by the
  $\mathrm{MA}_{\aleph_1}$ route, is the theorem page's result with Theorem
  C.

**Limitations.** The catalog pages, the arXiv abstract, Hajnal 1971 and the
two unheld chapters were not read; sentences resting on them are marked
unverified above, not refuted. The Tools section's proofs were re-derived
only as far as the section needs them; their standing is another reviewer's
subject. The one-step preservation argument under S8(c) is the reviewer's
own and carries author-recorded standing at most; it is retained for reuse,
not as a correction. Zero required corrections; three suggested; three notes.

This focused review assigns no tier and changes no status.
