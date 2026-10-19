---
name: research/erdos_1171/evidence/verify/connections_problem_1171_in_zfc_descent_chains_and_their_obs_review
title: "Independent review of the connections section: Problem 1171 in ZFC: descent chains and their obstruction"
desc: |
  Focused refutation review of the section's descent-chain deduction, its
  CH obstruction (a)+(b) and its by-products. Every statement survives
  (refutation-failed) under the section's convention that chain links are
  theorems of ZFC; one required correction (the Conclusion's consequence
  sentences drop that qualifier), two suggested changes and three notes.
created: 2026-09-28T19:01:50Z
updated: 2026-09-28T20:46:21Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation with only the assignment text. The reviewer took no part in
writing the connections page, the reconstruction pages or any library page,
and read only the material listed here.

**Frozen subject.** The source as it stood on 2026-09-28T13:50:48Z (called
"the commit" below). Page `wiki/research/erdos_1171/connections.md`, section
"## Problem 1171 in ZFC: descent chains and their obstruction", lines
125--258 (the H2 heading at line 125 through the line before the next H2 at
line 259). Line numbers below refer to this file at this commit.

**Lead page.** The same page. Its Scope paragraph and "## Tools" section
(lines 1--124) were read as inputs: the interfaces of (T1) transport, (T2)
restriction and weakening, (T3), (T4) the descent lemma and (T5) were
confirmed at each use. Their proofs belong to another reviewer; (T4) was
re-derived here only to confirm its interface.

**Read in full, as premises at their reviewed standing.**
[[research/erdos_1171/lemma_2_1_reconstruction|Lemma 2.1 reconstruction]]
and
[[research/erdos_1171/theorem_3_1_reconstruction|Theorem 3.1 reconstruction]]
at the commit.

**Problem pages.** [[problems/set_theory/E1171/_index|Problem 1171]] and
[[problems/set_theory/E1169/_index|Problem 1169]]: the header block before the
first H2 (statement, source line, references, formalization). The sections
"Current assessment", "Known Results", "Progress" and "Linked library
material" were not read; only their heading names were seen in a heading
listing.

**Library.** Read in full: the cards and result pages of
[[../library/set_theory/baumgartner_1987_remark_partition_relations_infinite_ordinals/_index|Baumgartner and Hajnal (1987)]]
(card, positive relation, negative relation),
[[../library/set_theory/baumgartner_1989_remarks_partition_ordinals/_index|Baumgartner (1989)]]
(card, main theorem) and
[[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth (2025)]]
(card). Held PDF of Komjáth 2025: printed pages 425--426 (Problem 13
commentary) and 442--443 (Problem 54 discussion), read as page images and as
extracted text. Held transcription of the 1999 booklet
[[../library/number_theory/various_1999_some_pauls_favorite_problems/_index|Some of Paul's favorite problems]]:
items 7.83--7.89, a search window around 7.84 and 7.85.

**Guidance.** `docs/verification.md` ("Report contract", "Grading and claim
standing", "Audit checklist" and the Erdos-specific "Whole-claim report" and
"Audit checklist"), `docs/approach_vetting.md`, `docs/evidence.md` "Source
fidelity" and `docs/math_authoring.md`.

**Exposures.**

- The header blocks of the two problem pages carry a one-phrase status line
  ("Not disprovable") beside the statement; it was seen while extracting the
  statement. The section itself quotes that status, so nothing new reached
  the reviewer.
- The library cards were read whole, beyond their provenance paragraphs,
  including the Komjáth card's digest of what it supplies for several
  problems, the Baumgartner cards' "Relation to Problem 1171" and "Read
  status" paragraphs, and the result pages' "Specialization" and
  "Consequence" sections. None carries standing, review or acceptance text
  about the section under review.
- A directory listing of `wiki/research/erdos_1171/evidence/verify/` and a
  working-tree status listing showed file names, among them other sections'
  reviews under this folder and under `wiki/research/erdos_15/`; none was
  opened.
- The folder index is excluded and was not read; (T3) and "the folder
  index's remark" are known here only through the Tools section's
  paraphrase, so the section's comparison with that remark is unassessed.
- No web search and no reading outside the repository.

## Restatement

Conventions, from the lemma page and the Tools section. Ordinals are von
Neumann ordinals and $[X]^2$ is the set of two-element subsets of $X$. The
relation $\gamma\to(\beta,H_1,\ldots,H_k)^2_{k+1}$ means that every coloring
of $[\gamma]^2$ with the colors $0,\ldots,k$ has a color-$0$ homogeneous
subset of order type $\beta$ or, for some $i\ge1$, a copy of $H_i$ all of
whose pairs have color $i$; the target $3$ is a triangle. A graph on an
ordinal is identified with the two-coloring that gives its edges color $1$,
so a *witness* for $\gamma\not\to(\beta,3)^2$ is a triangle-free graph on
$\gamma$ with no independent set of order type $\beta$. CH is the continuum
hypothesis and $\mathrm{MA}_{\aleph_1}$ is Martin's axiom for $\aleph_1$
dense sets. A relation "holds in ZFC" or "is a theorem of ZFC" when ZFC
proves it; "fails under CH" means ZFC+CH proves its negation.

- **S1 (Target, lines 127--137).** Problem 1171 asks whether
  $\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ with $k$ triangle
  targets holds for every finite $k$. Recorded: it holds under
  $\mathrm{MA}_{\aleph_1}$ for every $k$ (theorem page); the cases $k\le2$
  are theorems of ZFC, $k=1$ by Erdős and Hajnal and $k=2$ by Baumgartner
  and Hajnal; Komjáth 2025 records the case $k=3$ as unknown. The question
  taken up is the ZFC question for $k\ge3$. These are citations, not new
  mathematics; the date of the assessment is unassessed (excluded).
- **S2 (Chain deduction, lines 139--152).** Let $k\ge1$. If there are
  ordinals $\omega_1^2=\gamma_0\ge\gamma_1\ge\cdots\ge\gamma_k\ge\omega_1\omega$
  such that, for every $j\in\{1,\ldots,k\}$, the relation
  $\gamma_{j-1}\to(\gamma_j,3)^2$ is a theorem of ZFC, then
  $\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ with $k$ triangle
  targets is a theorem of ZFC.
- **S3 (First link, lines 152--158).** Imported: in ZFC,
  $\omega_1^2\to(\omega_1\alpha,3)^2$ for every $\alpha<\omega_1$ (Erdős and
  Hajnal 1970, through Komjáth 2025). Hence $\gamma_1=\omega_1\alpha$ is an
  admissible first step for every $\omega\le\alpha<\omega_1$; the chain of
  length one is the ZFC case $k=1$; and a chain of length two needs a
  theorem of ZFC of the form $\gamma_1\to(\gamma_2,3)^2$ with
  $\omega_1\omega\le\gamma_2\le\gamma_1\le\omega_1^2$.
- **S4 (Obstruction (a), lines 160--172).** Imported: CH implies
  $\omega_1^2\not\to(\omega_1^2,3)^2$ (Hajnal 1971; the paper is not held;
  the CH form is taken from the booklet item 7.85 and the catalog).
  Deduction: $\gamma_1=\omega_1^2$ heads no chain of S2 of length $\ge2$
  whose links are theorems of ZFC, since its first link would be
  $\omega_1^2\to(\omega_1^2,3)^2$, which fails under CH. Source
  qualification: Komjáth's Problem 13 commentary prints Hajnal's hypothesis
  as $\kappa^{<\kappa}=\kappa$ for $(\kappa^+)^2\not\to((\kappa^+)^2,3)^2$;
  at $\kappa=\omega$ that hypothesis is a ZFC truth, which would make the
  relation a ZFC theorem and contradict the commentary's later statement
  that the consistency of $\omega_1^2\to(\omega_1^2,3)^2$ is open.
- **S5 (Obstruction (b), lines 173--212; new mathematics).** Assume CH.
  Then for every ordinal $\gamma<\omega_1^2$ there is a triangle-free graph
  on $\gamma$ with no independent set of order type $\omega_1\omega$; that
  is, $\gamma\not\to(\omega_1\omega,3)^2$. CH enters only through the
  existence of a triangle-free graph $W$ on $\omega_1\omega$ with no
  independent set of type $\omega_1\omega$, the Erdős--Hajnal theorem cited
  on Baumgartner's result page.
- **S6 ((b) applied, lines 174--177).** If
  $\omega_1\omega\le\gamma_1<\omega_1^2$ and $\gamma_2\ge\omega_1\omega$,
  then $\gamma_1\to(\gamma_2,3)^2$ fails under CH, since by (T2) it would
  give $\gamma_1\to(\omega_1\omega,3)^2$; so it is not a theorem of ZFC.
- **S7 (Conclusion, lines 214--224).** In every model of CH there is no
  ordinal $\gamma_1$ with both $\omega_1^2\to(\gamma_1,3)^2$ and
  $\gamma_1\to(\gamma_2,3)^2$ for some $\gamma_2\ge\omega_1\omega$. Hence no
  chain of S2 of length $k\ge2$ has every link a theorem of ZFC, and the
  chain mechanism of S2 yields, in ZFC, exactly the case $k=1$: the ZFC case
  $k=2$ cannot be obtained by (T4) from two-color relations
  $\gamma\to(\gamma',3)^2$ between ordinals in $[\omega_1\omega,\omega_1^2]$
  *that are theorems of ZFC*, and (T4) cannot reduce the case $k=3$ to such
  theorems. The italic qualifier is supplied by the paragraph's setup at
  line 150 ("a theorem of ZFC for each $j$") and is absent from the
  consequence sentences as written; see F1.
- **S8 (First by-product, lines 226--236).** Under CH,
  $\gamma\not\to(\gamma,3)^2$ for every $\gamma$ with
  $\omega_1\omega\le\gamma<\omega_1^2$. For every such $\gamma$ the relation
  $\gamma\to(\omega_1\omega,3)^2$ holds under $\mathrm{MA}_{\aleph_1}$ and
  fails under CH, so it is independent of ZFC. The least $\gamma$ with
  $\gamma\to(\omega_1\omega,3)^2$ is $\omega_1\omega$ under
  $\mathrm{MA}_{\aleph_1}$ and $\omega_1^2$ under CH.
- **S9 (Second by-product, lines 236--243).** In ZFC,
  $\omega_1\omega\to(\omega_1\omega,3)^2$ implies
  $\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ for every finite $k$.
  Hence every model of $\omega_1^2\not\to(\omega_1\omega,3,3,3)^2$ is a model
  of $\omega_1\omega\not\to(\omega_1\omega,3)^2$, and the models of CH are
  among the models of the latter.
- **S10 (Next investigation, lines 245--255).** Two conditional deductions:
  a $4$-coloring of $[\omega_1^2]^2$ in a model of CH with no color-$0$ set
  of type $\omega_1\omega$ and no monochromatic triangle in the colors
  $1,2,3$ would show the case $k=3$ consistently false, hence not a theorem
  of ZFC; a proof that no such coloring exists under CH would leave the ZFC
  question open. The remaining sentences (acquire the 1987 paper; "any
  attack on $k=3$ starts from that ingredient"; CH as "the simplest
  hypothesis") are research guidance, not claims.
- **S11 (Outcome, line 257).** Bookkeeping; not a claim.

## Checklist

- **Quantifiers and scope.** Pass for S2--S6 and S8--S10, whose quantifiers
  were checked one by one: S2 "for each $j$" and "theorem of ZFC"; S5
  "every ordinal $\gamma<\omega_1^2$", including $\gamma<\omega_1\omega$,
  where the relation fails outright; S8 the half-open interval
  $[\omega_1\omega,\omega_1^2)$. Fail on wording for S7: the consequence
  sentences at lines 218--224 drop the qualifier "theorems of ZFC" (F1,
  required); the lead sentence at line 160 names the wrong failing link for
  $\gamma_1=\omega_1^2$ (F2); and "exactly the case $k=1$" is proved for
  chains whose non-zero colors carry triangles only (F3).
- **Circularity.** Pass. S5 uses the Erdős--Hajnal witness, not the target
  relation; S2 is a sufficient condition and assumes nothing about the
  target; S9's implication is the theorem page's Steps 1--3 with Theorem A
  replaced by its conclusion as a hypothesis.
- **Model and convention changes.** Pass. The graph-coloring translation in
  S5 is exact: edges are color $1$, an independent set is a color-$0$
  homogeneous set. The map $\varphi$ of S5 is not order preserving, and the
  proof never transports a relation along it; it computes the order type of
  $\varphi[X]$ directly from the block decomposition of $\omega_1\omega$,
  which is legitimate because $\varphi$ preserves order inside each block
  and sends distinct blocks to distinct blocks.
- **Finite and statistical overreach.** Inapplicable; no finite case or
  heuristic is used as a proof.
- **Uniformity.** Pass. The obstruction exhibits one class of models, the
  models of CH, in which every candidate link of S2 fails at once, so "no
  chain of ZFC theorems" needs no uniformity across candidates. The passage
  from "fails under CH" to "not a theorem of ZFC" uses the relative
  consistency of CH, which the section does not name (F5, note).
- **Extremal conclusions.** Pass. The two "least $\gamma$" values of S8 were
  recomputed in the relation's own terms: under $\mathrm{MA}_{\aleph_1}$,
  every $\gamma<\omega_1\omega$ fails $\gamma\to(\omega_1\omega,3)^2$
  outright (no subset of type $\omega_1\omega$) and $\omega_1\omega$ holds
  by Theorem A; under CH, every $\gamma<\omega_1^2$ fails by S5 and
  $\omega_1^2$ holds by the ZFC theorem of S3.
- **Consequences and composition.** Each "hence" was attacked separately.
  S2 composes (T4) and (T2) inside their hypotheses; S6 and S8 use (T2)'s
  weakening of the large target; S9 composes the theorem page's Steps 1--3.
  One consequence sentence fails as written (F1); the others pass.
- **Computation.** Inapplicable; the section has no computation.
- **Reproduction.** Inapplicable; the section states no rerun command and
  has no evidence code.
- **Source and verdict fidelity.** Pass with one note. Checked against the
  held PDF of Komjáth 2025: the attribution of
  $\omega_1^2\to(\omega_1\alpha,3)^2$ for $\alpha<\omega_1$ to Erdős and
  Hajnal (p. 425); the printed hypothesis $\kappa^{<\kappa}=\kappa$ and the
  sentence on the open consistency of $\omega_1^2\to(\omega_1^2,3)^2$
  (p. 425); the sentence that $\omega_1^2\to(\omega_1\omega,3,3,3)^2$ is
  unknown (p. 443). Checked against the held booklet transcription: item
  7.85 asks whether $\omega_1^2\not\to(\omega_1^2,3)^2$ and adds that Hajnal
  shows it follows from CH. The phrase "next sentence" at line 170 is
  inexact (F4). The library pages' statements are used at the strength they
  record; no characterization strengthens a source.

## Weakest steps

**W1. The order-type count in the proof of (b) (lines 192--207).** Let
$X\subseteq\omega_1\alpha$ be independent in $G$ with
$\operatorname{otp}(X)=\omega_1\omega$, and let $X_\eta$ be the part of $X$
in the block $[\omega_1\eta,\omega_1(\eta+1))$. The blocks are consecutive
intervals indexed by $\eta<\alpha$, so
$\operatorname{otp}(X)=\sum_{\eta<\alpha}\operatorname{otp}(X_\eta)$, with
each term at most $\omega_1$, and a term equals $\omega_1$ exactly when
$X_\eta$ is uncountable (an uncountable subset of a set of type $\omega_1$
has every proper initial segment countable, hence type $\omega_1$). Suppose only
finitely many terms, say $m$, are uncountable, at positions
$\eta_1<\cdots<\eta_m$. Group the sum as
$S_0+\omega_1+S_1+\omega_1+\cdots+\omega_1+S_m$, where $S_i$ is the sum of
the countable terms between consecutive uncountable positions; each $S_i$ is
the order type of a countable set, hence a countable ordinal, and
$\rho+\omega_1=\omega_1$ for countable $\rho$. So the sum equals
$\omega_1m+S_m<\omega_1(m+1)\le\omega_1\omega$, a contradiction. Hence
infinitely many $X_\eta$ are uncountable. Since $f$ is injective and
$\varphi$ is injective and order preserving on each block, $\varphi[X]$ meets
infinitely many distinct blocks of $\omega_1\omega$ in sets of type
$\omega_1$ and every other block in a countable set. Its order type is the
sum over $n<\omega$ of the types of its parts in the blocks
$[\omega_1n,\omega_1(n+1))$; if $n_0<n_1<\cdots$ are the blocks contributing
$\omega_1$, the partial sum through the block $n_i$ collapses to
$\omega_1(i+1)$ by the same grouping, the partial sums are nondecreasing, and
every term is at most $\omega_1$, so the sum is at least
$\sup_i\omega_1(i+1)=\omega_1\omega$ and at most $\omega_1\omega$. The set
$\varphi[X]$ is independent in $W$, because $\{x,y\}\notin G$ means
$\{\varphi(x),\varphi(y)\}\notin W$ and $\varphi$ is injective. This
contradicts the choice of $W$. The step composes with the rest: $G$ is
triangle-free because $\varphi$ is injective, so a triangle of $G$ has three
distinct images pairwise adjacent in $W$; and the restriction of $G$ for
$\alpha=\alpha_0+1$ to an initial segment $\gamma<\omega_1(\alpha_0+1)$
inherits both properties. Every $\gamma<\omega_1^2$ has the form
$\omega_1\alpha_0+\zeta$ with $\alpha_0,\zeta<\omega_1$, so every such
$\gamma$ is covered.

**W2. The case split of the Conclusion (lines 214--218).** A chain of S2 of
length $k\ge2$ contains the links $\omega_1^2\to(\gamma_1,3)^2$ and
$\gamma_1\to(\gamma_2,3)^2$ with $\gamma_2\ge\gamma_k\ge\omega_1\omega$. If
$\gamma_1=\omega_1^2$, the first link is $\omega_1^2\to(\omega_1^2,3)^2$,
which fails under CH by (a). If $\gamma_1<\omega_1^2$, the second link
implies $\gamma_1\to(\omega_1\omega,3)^2$ by (T2), which fails under CH by
(b). A link that fails under CH is not a theorem of ZFC, provided ZFC+CH is
consistent when ZFC is (the relative consistency of CH, Gödel 1940,
unnamed in the section; F5). Two extensions the section does not write out
were checked: a chain may start at any $\gamma_0\le\omega_1^2$ and finish
with (T2)'s restriction, and then $\gamma_1\le\gamma_0$, so (b) alone
blocks the second link when $\gamma_0<\omega_1^2$; and a link whose
non-zero target contains a triangle, or whose color-$0$ target is larger,
implies the triangle link, so the obstruction applies to it as well.

**W3. The second by-product (lines 236--243).** On the theorem page, Step 1
invokes Theorem A only to obtain $\omega_1\omega\to(\omega_1\omega,3)^2$ and
then applies Lemma 2.1, which is a theorem of ZFC; Steps 2 and 3 are the
restriction of a coloring of $[\omega_1^2]^2$ to the initial segment
$\omega_1\omega$ and the reading of the result in $\omega_1^2$, both in ZFC.
So ZFC proves the implication from $\omega_1\omega\to(\omega_1\omega,3)^2$ to
the relation of Problem 1171 for every finite $k\ge1$; the instance $k=0$ is
trivial. The contrapositive gives S9's model statement, and CH implies
$\omega_1\omega\not\to(\omega_1\omega,3)^2$ by the theorem that supplies $W$
in (b).

## Strongest attack

- **S5.** Three attacks. (i) Choose $X$ meeting every block in a countable
  set but of type $\omega_1\omega$: impossible, since a sum of countably
  many countable ordinals is countable. (ii) Exploit that $f$ scrambles the
  block order, hoping $\varphi[X]$ has a type other than $\omega_1\omega$:
  the type of $\varphi[X]$ is computed in the order of $\omega_1\omega$, and
  a block of $\omega_1\omega$ contributes $\omega_1$ or a countable ordinal
  whatever block of $\omega_1\alpha$ it came from, so the count in W1 is
  insensitive to the order of $f$. (iii) Attack the restriction step with a
  $\gamma$ not of the form $\omega_1\alpha$: an initial segment of a witness
  is a witness, so the form of $\gamma$ is irrelevant. All failed; S5 is
  proved from the existence of $W$ alone.
- **S7.** (i) Read the consequence sentence "(T4) cannot reduce the open
  case $k=3$ to such relations" on its own, as the audit checklist requires.
  It is false: (T3), the constant case of (T4), reduces the case $k=3$ to
  the single relation $\omega_1\omega\to(\omega_1\omega,3)^2$, a two-color
  relation $\gamma\to(\gamma',3)^2$ between ordinals in
  $[\omega_1\omega,\omega_1^2]$, and the section's own S9 records exactly
  this reduction; in every model of $\mathrm{MA}_{\aleph_1}$ the constant
  chain exists. The attack succeeds against the wording and fails against
  the qualified statement, which is what the paragraph's setup defines and
  what the proof establishes (F1). (ii) Attack "exactly the case $k=1$"
  with a (T4) chain of another shape: put $\omega_1\omega$ in color $1$, so
  the first link is $\omega_1^2\to(\gamma_1,\omega_1\omega)^2$ and the later
  links carry triangles with $\gamma_k\ge3$. Then $\gamma_1\to(\gamma_2,3)^2$
  with $\gamma_2\ge3$ forces $\gamma_1\ge6$, and
  $\omega_1^2\to(\gamma_1,\omega_1\omega)^2$ implies
  $\omega_1^2\to(\omega_1\omega,4)^2$ by relabeling and (T2), which fails
  under CH by the negative relation of Baumgartner and Hajnal. Shapes with
  $\omega_1\omega$ in a color $j\ge2$ force $\gamma_1\ge\omega_1\omega$ and
  $\gamma_1\to(\omega_1\omega,3)^2$, so (a)+(b) apply. The sentence
  survives, but its proof in the section covers only the triangle-target
  shape (F3).
- **S8.** Attack the independence claim at a decomposable $\gamma$, say
  $\gamma=\omega_1\omega+1$: under $\mathrm{MA}_{\aleph_1}$ the relation
  $\gamma\to(\omega_1\omega,3)^2$ holds by restriction to the initial
  segment $\omega_1\omega$, and under CH it fails by S5. Failed. The
  self-similar half, $\gamma\not\to(\gamma,3)^2$, is a ZFC fact for every
  additively decomposable $\gamma$ (give color $1$ to the pairs across a
  decomposition $\gamma=\gamma'+\gamma''$ with $\gamma',\gamma''<\gamma$),
  so S8's first sentence is new only at the indecomposable ordinals
  $\omega_1\omega^\beta$ with $1\le\beta<\omega_1$; a remark, not a defect.
- **S4.** Attack the standing of the imported theorem: the paper is not held
  and Komjáth prints a hypothesis that would make the relation a ZFC
  theorem. Under either reading of the hypothesis the instance
  $\kappa=\omega$ holds under CH, so the obstruction is unaffected by the
  discrepancy; the section's choice of the weaker form is the safe one.
  Failed.
- **S2, S3, S6, S9, S10.** Direct re-derivation; no attack found beyond the
  unnamed consistency facts (F5).

## Premises

- **(T1), (T2), (T4)** from the lead page's Tools section: interfaces
  confirmed at each use (transport along an order isomorphism onto a subset
  of the given type; restriction to a subset of the given type and
  weakening of the large target or of a non-zero target; the descent chain
  with color $j$ carrying $H_j$). (T4) was re-derived: merge the colors $0$
  and $k+1$, apply the chain of length $k$, then transport the last link to
  the color-$0$ set of type $\gamma_k$. Proofs owned by another reviewer.
- **Lemma 2.1 reconstruction**: $\alpha\to(\alpha,3)^2$ implies
  $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$ in ZFC; independently reviewed as it
  stood on 2026-09-28T05:03:27Z with corrections since; used in W3. Read in
  full.
- **Theorem 3.1 reconstruction**: Steps 1--3; Theorem A
  ($\mathrm{MA}_{\aleph_1}$ implies $\omega_1\omega\to(\omega_1\omega,3)^2$;
  the chapter is not held, statement from its zbMATH review and a held
  restatement); Theorem B (the ZFC case $k=2$); Theorem C (relative
  consistency of $\mathrm{MA}_{\aleph_1}$). Read in full.
- **Baumgartner (1989), main theorem page**: the statement under
  $\mathrm{MA}_{\aleph_1}$ and the sentence that the Erdős--Hajnal theorem
  cited by the chapter's review gives, under CH,
  $\omega_1\omega\not\to(\omega_1\omega,3)^2$ and
  $\omega_1\omega^2\not\to(\omega_1\omega^2,3)^2$. This is the source of $W$
  in S5; the Erdős--Hajnal paper is not held and the statement stands at
  the review's standing. Read in full.
- **Baumgartner and Hajnal (1987)**: positive relation page,
  $\omega_1^2\to(\omega_1\omega,3,3)^2$ in ZFC (not held; zbMATH review and
  Komjáth); negative relation page, CH implies
  $\omega_1^2\not\to(\omega_1\omega,4)^2$, used only in the reviewer's
  attack (ii) on S7, not by the section. Read in full.
- **Komjáth (2025)**, held PDF, pp. 425--426 and 442--443, read as page
  images: the Erdős--Hajnal attribution, the Problem 13 hypothesis and
  consistency sentence, the Problem 54 statements. Card read in full.
- **Hajnal (1971)**: not held and without a library page; S4's statement is
  taken from the booklet item 7.85 (held transcription, read) and the
  reference list of the Problem 1169 page. The catalog page was not read.
- **Booklet (1999)**, items 7.84 and 7.85: transcription lines read.
- **Standard facts not cited by the section**: the relative consistency of
  CH (Gödel 1940), needed for "not a theorem of ZFC" and "independent of
  ZFC"; the ordinal arithmetic used in W1.

## Findings

- **F1 (required).** Location: lines 218--224, "So (T4) yields exactly the
  case $k=1$ in ZFC. In particular the ZFC case $k=2$ of Baumgartner and
  Hajnal cannot be obtained by (T4) from two-color relations
  $\gamma\to(\gamma',3)^2$ between ordinals in $[\omega_1\omega,\omega_1^2]$,
  and (T4) cannot reduce the open case $k=3$ to such relations. This
  sharpens the folder index's remark: not only the constant chain through
  $\omega_1\omega$ but every descending chain is blocked in ZFC." Defect:
  the consequence sentences drop the qualifier, stated in the setup at line
  150, that the relations are theorems of ZFC; read on their own they assert
  that no reduction and no chain exists. Witness: (T3) reduces the case
  $k=3$ to $\omega_1\omega\to(\omega_1\omega,3)^2$, a relation of the named
  form, as S9 (lines 236--243) records, and in every model of
  $\mathrm{MA}_{\aleph_1}$ the constant chain through $\omega_1\omega$ is a
  descending chain in the section's sense. Proposed replacement: "...cannot
  be obtained by (T4) from two-color relations $\gamma\to(\gamma',3)^2$
  between ordinals in $[\omega_1\omega,\omega_1^2]$ that are theorems of
  ZFC, and (T4) cannot reduce the open case $k=3$ to such theorems. ... not
  only the constant chain through $\omega_1\omega$ but every descending
  chain fails in some model of ZFC, so none consists of theorems of ZFC."
- **F2 (suggested).** Location: lines 160--161, "No such second link is a
  theorem of ZFC, because under CH none holds:". Defect: with
  $\gamma_1=\omega_1^2$ and $\gamma_2=\omega_1\omega$, both allowed by the
  bounds at line 158, the second link $\omega_1^2\to(\omega_1\omega,3)^2$ is
  a theorem of ZFC; what fails for that $\gamma_1$ is the first link, as
  bullet (a) says. Proposed replacement: "No chain of length two has both
  links as theorems of ZFC, because under CH one of them fails:".
- **F3 (suggested).** Location: line 218, "So (T4) yields exactly the case
  $k=1$ in ZFC." Defect: (T4) admits target lists other than triangles, and
  the section's argument covers only chains whose ordinals descend in color
  $0$ while every other color carries a triangle or a target containing one.
  The shape with $\omega_1\omega$ as the target $H_1$ is also blocked under
  CH, but by the negative relation of Baumgartner and Hajnal, as in the
  attack on S7 above. Proposed replacement: "So (T4) with triangle targets
  yields exactly the case $k=1$ in ZFC", or add the one-line argument for
  the other shape with its citation.
- **F4 (note).** Location: line 170, "the same commentary's next sentence".
  In the held PDF (p. 425) the sentence on the open consistency of
  $\omega_1^2\to(\omega_1^2,3)^2$ opens the following paragraph, with three
  sentences between it and the hypothesis sentence. Proposed replacement:
  "a later sentence of the same commentary". The discrepancy does not
  weaken (a): under either reading of the hypothesis the instance
  $\kappa=\omega$ holds under CH.
- **F5 (note).** Location: lines 214--218 and 230--236. The steps from
  "fails under CH" to "not a theorem of ZFC" and to "independent of ZFC"
  use the relative consistency of CH, and the $\mathrm{MA}_{\aleph_1}$ half
  of the independence uses Theorem C of the theorem page; neither is named
  in the section. Proposed: one clause naming both, in the manner of the
  theorem page's Theorem C.
- **F6 (note).** Location: lines 173 and 179. The proof of (b) uses CH only
  to obtain the witness $W$, so (b) holds under the weaker hypothesis
  $\omega_1\omega\not\to(\omega_1\omega,3)^2$. Recording that hypothesis
  would tie (b) to S9: in every model where the case $k=3$ fails, every
  $\gamma<\omega_1^2$ fails $\gamma\to(\omega_1\omega,3)^2$. Not a defect.

## Verdict

- S1: not a claim; the citations were checked against the held sources and
  the premise pages.
- S2: refutation-failed.
- S3: refutation-failed, conditional on the imported theorem of Erdős and
  Hajnal at Komjáth's standing.
- S4: refutation-failed, conditional on the imported theorem of Hajnal at
  the standing of the booklet item and the catalog (paper not held, no
  library page).
- S5: refutation-failed; the proof is complete from the existence of $W$.
- S6: refutation-failed.
- S7: refutation-failed for the statement with the qualifier that the links
  are theorems of ZFC, which the paragraph's setup supplies; the consequence
  sentences as written are false without it and require the correction F1.
- S8: refutation-failed.
- S9: refutation-failed.
- S10: refutation-failed for the two conditional deductions; the rest is
  guidance and not a claim.
- S11: not a claim.

Limitations: the imported negative relations, (a) and the witness $W$, rest
on papers the corpus does not hold, at the standing their library pages and
the booklet record; the folder index and the problem pages' assessments were
excluded, so the sentence comparing the result with the folder index's
remark and the assessment date are unassessed; the relative consistency of
CH and of $\mathrm{MA}_{\aleph_1}$ is taken as standard.

This focused review assigns no tier and changes no status.
