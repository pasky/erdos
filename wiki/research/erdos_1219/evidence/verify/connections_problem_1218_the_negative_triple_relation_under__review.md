---
name: research/erdos_1219/evidence/verify/connections_problem_1218_the_negative_triple_relation_under__review
title: "Independent review of the connections section: Problem 1218: the negative triple relation under GCH"
desc: |
  Refutation review of the Problem 1218 section of the connections page as of
  2026-09-28T13:50:48Z. Every mathematical statement of the section survives
  (refutation-failed); the transcribed catalog condition is reportage. Zero
  required corrections, two suggested (a page number and a convention
  gloss), and five notes.
created: 2026-09-28T19:15:09Z
updated: 2026-09-28T19:15:09Z
---

***

## Subject and independence

**Role.** The reviewer worked in a fresh context from the commissioned
assignment alone, took no part in writing the connections page or the
reconstruction pages of the folder, and read nothing outside the read set
listed below. The charge was refutation of the author-recorded mathematics
of one section.

**Subject.** Page `wiki/research/erdos_1219/connections.md` as it stood at
2026-09-28T13:50:48Z, section "## Problem 1218: the negative triple relation
under GCH", lines 446--510 (the H2 heading is line 446; the next H2 is line
511). No lead page was named for this section.

**Read, and at what depth.**

- The section, in full, repeatedly.
- The page's Scope paragraph (lines 18--37) for notation, and its Tools
  section (lines 39--108): the interface of (T2) confirmed at the section's
  one use and its proof re-derived in the instance used; (T1) and (T3) are
  not used by the section and were read only to confirm that.
- [[research/erdos_1219/theorem_1_2_reconstruction|Theorem 1.2]]: Source,
  Standing, Definitions, Sum formula, Imported results and Statement
  (lines 1--131), as premises; the proof was not read.
- [[research/erdos_1219/lemma_1_1_reconstruction|Lemma 1.1]] and
  [[research/erdos_1219/corollary_1_3_reconstruction|Corollary 1.3]]:
  Statement sections only, to confirm what "the mechanism" produces.
- [[problems/set_theory/E1218/_index|Problem 1218]] (lines 12--37),
  [[problems/set_theory/E1167/_index|Problem 1167]] (lines 12--42) and
  [[problems/set_theory/E1168/_index|Problem 1168]] (lines 13--32): the Statement
  blocks only, including their printed Status line.
- [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth (2025)]]:
  the card's provenance paragraph and the held PDF, printed pp. 419--420
  (PDF pp. 2--3), read on rendered page images and cross-checked against a
  text extraction; the bibliography entry [45] located in the extraction.
- `docs/verification.md` ("Grading and claim standing", both audit
  checklists, "Whole-claim report"), `docs/approach_vetting.md`,
  `docs/evidence.md` ("Source fidelity") and `docs/math_authoring.md`.

**Exposures.** None of the excluded kinds: no evidence folder, no Current
assessment, Known Results, standing table, acceptance text, other section's
review or web page was opened. For completeness: the card body of the
survey was read whole, including its "Bears on" and "Results to transcribe"
lists, which go beyond the provenance paragraph; the theorem page's own
Source and Standing paragraphs and the connections page's Scope paragraph
(author-recorded self-descriptions, no review content) were inside the
ranges read; a heading listing of the three problem pages and of the whole
connections page was seen without their content; and the page's Scope,
Tools and the section were searched for the citation string "[45" to learn
whether the reference is named on the page. A read-only status listing of
the working tree showed the file names of other sections' review reports;
none was opened.

## Restatement

Throughout, $\beta=\omega_{\omega+1}$, GCH is assumed where a statement
says so, and cardinal partition relations follow the theorem page's
Definitions: $\theta\to(\mu_0,\ldots)^r$ asks for a homogeneous set of
cardinality $\mu_\nu$ in color $\nu$, $(\rho)_\gamma$ is $\gamma$
repetitions of the target $\rho$, and $\chi=\sum_{\mu<\lambda}2^\mu$ runs
over all cardinals $\mu<\lambda$, finite ones included. Two relations are
named, both under GCH: the *page's form* (P),
$\aleph_{\beta+1}\not\to(\aleph_{\beta+1},(4)_{\aleph_0})^3$, and the
*site's current form* (S),
$\aleph_{\beta+1}\not\to(\aleph_\beta,(4)_{\aleph_0})^3$; and $R$ denotes
$\aleph_\beta\not\to(\aleph_\beta,(3)_{\aleph_0})^2$.

- **S1 (target).** The problem page's statement is (P) with
  $\lambda=\aleph_{\omega_{\omega+1}+1}$ and countably many targets $4$,
  and (P) is the relation of Problem 1 of the survey (p. 419), which sets
  $\lambda=\kappa_0=\aleph_{\omega_{\omega+1}+1}$ and $\kappa_n=4$ for
  $n>0$.
- **S2 (the two forms).** (S) and (P) are distinct relations; (S) implies
  (P) in ZFC, because lowering the first target strengthens a negative
  relation.
- **S3 (reportage).** The catalog page currently prints (S) and the general
  conjecture
  $\aleph_{\beta+1}\not\to(\aleph_\beta,(4)_{\aleph_{\operatorname{cr}(\beta)}})^3$
  for ordinals $\beta$ with
  $\beta>\operatorname{cf}\beta>\operatorname{cf}\beta-1>\operatorname{cr}\beta$,
  with $\beta=\omega_{\omega+1}$ the least such ordinal; the page leaves
  $\operatorname{cr}$ undefined. The section asserts this as the catalog
  page's content, not as its own mathematics.
- **S4 (regular resource).** $\aleph_{\beta+1}$ is regular, so every
  partition of it into fewer than $\aleph_{\beta+1}$ pieces has a piece of
  cardinality $\aleph_{\beta+1}$, and the block-to-cofinality reduction of
  Theorem 1.2 has nothing to reduce to.
- **S5 (the sum of powers).** Under GCH and at $\lambda=\aleph_\beta$,
  $\chi=\sum_{\gamma<\beta}\aleph_{\gamma+1}=\aleph_\beta\ne\aleph_{\beta+1}$,
  and Theorem 1.2's hypothesis that $\langle2^\mu:\mu<\lambda\rangle$ is
  eventually $\ge\lambda$ fails.
- **S6 (wrong exponent).** (T2) yields negative relations for pairs on
  singular cardinals, so it says nothing about a relation for triples on
  the regular cardinal $\aleph_{\beta+1}$.
- **S7 (the stepping-up instance).** Under GCH,
  $2^{\aleph_\beta}=\aleph_{\beta+1}$, and (S) is the conclusion of the
  implication asked in Problem 1167, in
  its instance $r=2$, $\lambda=\kappa_0=\aleph_\beta$, $\kappa_n=3$ for
  $1\le n<\omega$ ($\gamma=\omega$ colors, cardinal addition), applied to
  the premise $R$.
- **S8 (the premise, author-recorded).** Under GCH, $R$ holds:
  $\operatorname{cf}\aleph_\beta=\aleph_{\omega+1}$; the survey's
  commentary on Problem 5 records the theorem of its [45, Section 20] that
  $2^\lambda=\lambda^+$ implies
  $\lambda^+\not\to(\lambda^+,(3)_{\operatorname{cf}\lambda})^2$ for singular
  $\lambda$; at $\lambda=\aleph_\omega$ this is
  $\aleph_{\omega+1}\not\to(\aleph_{\omega+1},(3)_{\aleph_0})^2$ under GCH,
  the GCH case of Problem 1168; and (T2) with $\gamma=\aleph_0$,
  $\rho_\nu=3$ lifts it to $\aleph_\beta$.
- **S9 (conditional, forward).** If the implication of Problem 1167 holds
  in its case $r=2$ with one singular target and the others finite, then
  under GCH (S) holds, hence (P).
- **S10 (conditional, backward).** A model of GCH in which (S) fails
  refutes the implication of Problem 1167.
- **S11 (outcome).** The mechanism fails on the regular-resource
  obstruction; the connection to Problem 1167 is recorded; no lead. This
  is a summary, not a separate mathematical claim.

## Checklist

- **Quantifiers and scope.** Pass. GCH is carried explicitly in every
  sentence that needs it (S5, S7--S10); $R$ is tagged author-recorded;
  both conditional deductions are written with "would" and neither is
  read as unconditional. The one scope defect is in transcribed text: the
  "least such ordinal" sentence of S3 is unsatisfiable under the page's
  own cofinality convention (F2).
- **Circularity.** Pass. $R$ is derived from an imported theorem and (T2),
  not from either form of the target; (S) and (P) are related by
  monotonicity only; nothing assumes Problem 1167's implication except the
  two sentences that name it as a hypothesis.
- **Model and convention changes.** One instance, in reportage: the
  transcribed condition
  $\beta>\operatorname{cf}\beta>\operatorname{cf}\beta-1>\operatorname{cr}\beta$
  uses $\operatorname{cf}$ as an index into the aleph sequence, whereas
  the page's convention (theorem page, Definitions) makes
  $\operatorname{cf}\beta$ the cofinality of the ordinal $\beta$, under
  which $\operatorname{cf}\omega_{\omega+1}=\omega_{\omega+1}$ (F2). The
  section's own use of the partition-relation notation, of $\chi$ and of
  cardinal addition in Problem 1167 matches the conventions of the pages
  it cites.
- **Finite and statistical overreach.** Inapplicable: no finite sample or
  heuristic average appears.
- **Uniformity.** Inapplicable: there are no constants, error terms or
  exchanged limits; $\beta$ is a single fixed ordinal.
- **Extremal conclusions.** The only extremal sentence is the transcribed
  "least such ordinal" of S3. Under the index reading it is correct (the
  derivation is in Findings, F2); under the page's convention the condition
  it minimizes over is not satisfied at $\omega_{\omega+1}$ at all.
- **Consequences and composition.** Pass. Each "so" and "hence" was
  attacked separately: (S) to (P) by monotonicity (S2); $R$ from the
  imported theorem and (T2) with every interface clause of (T2) matched
  (S8); the E1167 instance with cardinal addition (S7); the two
  conditionals (S9, S10). The composition in S8 inherits the standing of
  the imported theorem, which the section takes from the survey's
  characterization of a source it does not hold; the author-recorded label
  on $R$ states exactly that.
- **Computation.** Inapplicable: the section runs no code.
- **Reproduction.** Inapplicable: the section makes no rerun or coverage
  claim.
- **Source and verdict fidelity.** The characterization of Problem 1 is
  exact and its page is right (p. 419). The characterization of the
  Problem 5 commentary is exact in content, but that commentary is printed
  on p. 420 (PDF p. 3), not p. 419 (F1). The characterizations of
  Problems 1167 and 1168 match the corpus statements clause for clause.
  The reference [45] is not named on the page (F4). The catalog page's
  current text, its edit date, its forum contents and the attribution "the
  case its authors could not settle even under GCH per the catalog page of
  Problem 1167" lie outside the read set and are unverified here (F5).

## Weakest steps

**W1: the lift of the premise (S8).** Since $\beta=\omega_{\omega+1}$ is a
limit ordinal, $\operatorname{cf}\aleph_\beta=\operatorname{cf}\beta$, and
$\beta$ is a successor cardinal, hence regular, so
$\kappa:=\operatorname{cf}\aleph_\beta=\aleph_{\omega+1}$; as
$\omega+1<\omega_{\omega+1}$, $\kappa<\aleph_\beta$ and $\aleph_\beta$ is
singular. The imported theorem, applied to the singular cardinal
$\aleph_\omega$ with $2^{\aleph_\omega}=\aleph_{\omega+1}$ (GCH) and
$\operatorname{cf}\aleph_\omega=\aleph_0$, gives
$\kappa\not\to(\kappa,(3)_{\aleph_0})^2$. The interface of (T2) is then
met clause by clause: $\lambda=\aleph_\beta$ singular,
$\kappa=\operatorname{cf}\lambda$, $\gamma=\aleph_0\ge1$, $\rho_\nu=3\ge2$,
and the hypothesis just obtained. Re-derived in this instance: fix a witness
$c:[\aleph_{\omega+1}]^2\to\omega$ with no color-$0$ homogeneous set of
cardinality $\aleph_{\omega+1}$ and no triangle in any color $n\ge1$, and
partition $\aleph_\beta$ into $\omega$ and the intervals
$[\aleph_i,\aleph_{i+1})$ for $i<\beta$, that is into $\aleph_{\omega+1}$
blocks each of cardinality below $\aleph_\beta$. Color a pair inside a
block $0$ and a pair across blocks $i\ne j$ by $c(\{i,j\})$. A color-$0$
homogeneous $H$ of cardinality $\aleph_\beta$ meets a set $J$ of blocks;
if $|J|<\aleph_{\omega+1}$ then $J$ is bounded by some $i_0<\omega_{\omega+1}$,
so $H\subseteq\aleph_{i_0}$, of cardinality below $\aleph_\beta$; hence
$|J|=\aleph_{\omega+1}$ and, choosing one point of $H$ per block, $J$ is
$c$-homogeneous in color $0$, impossible. A color-$n$ homogeneous set of
three points, $n\ge1$, has its points in three distinct blocks, which form
a $c$-triangle in color $n$, impossible. So $R$ holds under GCH. The
composition is sound; its standing is that of the imported theorem, which
the section correctly leaves at author-recorded.

**W2: the identification and the two conditionals (S7, S9, S10).** The
corpus statement of Problem 1167 asks, for every finite $r\ge2$, infinite
$\lambda$, and cardinals $\kappa_\alpha$ ($\alpha<\gamma$), whether
$2^\lambda\to(\kappa_\alpha+1)^{r+1}_{\alpha<\gamma}$ implies
$\lambda\to(\kappa_\alpha)^r_{\alpha<\gamma}$, with cardinal addition. Its
contrapositive at $r=2$, $\lambda=\aleph_\beta$, $\gamma=\omega$,
$\kappa_0=\aleph_\beta$, $\kappa_n=3$ ($1\le n<\omega$) reads: $R$ implies
$2^{\aleph_\beta}\not\to(\aleph_\beta,(4)_{\aleph_0})^3$, because
$\aleph_\beta+1=\aleph_\beta$ and $3+1=4$ in cardinal addition; under GCH
$2^{\aleph_\beta}=\aleph_{\beta+1}$, and the conclusion is exactly (S).
Had the problem used ordinal addition, the conclusion would forbid only
color-$0$ homogeneous sets of order type $\omega_\beta+1$, which gives (P)
but not (S); the corpus statement fixes cardinal addition, so the section's
identification is exact. S9 composes a positive answer covering this
instance with $R$ (W1) and GCH to get (S), then (P) by S2. S10: in a model
of GCH where (S) fails, $\aleph_{\beta+1}\to(\aleph_\beta,(4)_{\aleph_0})^3$
holds while $R$ holds, so the implication of Problem 1167 has a true
antecedent and a false consequent there and is not a theorem of ZFC. Both
deductions are stated as conditionals in the section.

**W3: the obstruction arithmetic (S4, S5).** $\aleph_{\beta+1}$ is a
successor cardinal, hence regular; a union of fewer than
$\operatorname{cf}\theta$ sets each of cardinality below $\theta$ has
cardinality below $\theta$, so any partition of $\aleph_{\beta+1}$ into
fewer than $\aleph_{\beta+1}$ pieces has a piece of full cardinality. Under
GCH the cardinals below $\aleph_\beta$ are the finite ones and the
$\aleph_\gamma$, $\gamma<\beta$; their powers are the finite $2^n$ and
$\aleph_{\gamma+1}$, so by the theorem page's sum formula

$$
\chi=\aleph_0+\sum_{\gamma<\beta}\aleph_{\gamma+1}
=|\beta|\cdot\sup_{\gamma<\beta}\aleph_{\gamma+1}
=\aleph_{\omega+1}\cdot\aleph_\beta=\aleph_\beta ,
$$

using that $\beta$ is a limit ordinal. "Eventually $\ge\lambda$" requires a
cardinal $\mu_0<\lambda$ with $2^\mu\ge\lambda$ for every cardinal
$\mu\in[\mu_0,\lambda)$; since
$2^{\aleph_\gamma}=\aleph_{\gamma+1}<\aleph_\beta$ for every $\gamma<\beta$,
no such $\mu_0$ exists. Both obstructions stand.

## Strongest attack

- **S1.** Attack: a mismatch between the corpus statement and Problem 1 of
  the survey in the subscript or in the number of finite targets. The
  corpus page prints $\lambda=\aleph_{\omega_{\omega+1}+1}$ with countably
  many $4$s; the survey's Problem 1 prints
  $\lambda=\kappa_0=\aleph_{\omega_{\omega+1}+1}$ and $\kappa_n=4$ for $n>0$
  over $n<\omega$, read on the page image.
  Failed.
- **S2.** Attack: reverse the direction, or find that the first targets
  are incomparable. A coloring with no color-$0$ homogeneous set of
  cardinality $\aleph_\beta$ has none of cardinality $\aleph_{\beta+1}$,
  since the larger set contains a subset of the smaller cardinality; so
  (S) implies (P) and the section's direction is right. Failed.
- **S3.** Attack: evaluate the transcribed condition at the ordinal named
  as least. Under the page's convention
  $\operatorname{cf}\omega_{\omega+1}=\omega_{\omega+1}$, so
  $\beta>\operatorname{cf}\beta$ is false and $\operatorname{cf}\beta-1$
  is undefined for this limit ordinal; under the index reading the
  sentence is correct (F2). The sentence is reportage of a page outside
  the read set and carries no mathematics of the section; the defect is
  a missing gloss, filed as F2.
- **S4.** Attack: a decomposition of $\aleph_{\beta+1}$ into $\aleph_\beta$
  pieces of cardinality $\aleph_\beta$. Impossible by regularity: the union
  would have cardinality $\aleph_\beta$. Failed.
- **S5.** Attack: (a) the finite $\mu$ omitted from the displayed sum
  change $\chi$; (b) "eventually $\ge\lambda$" holds vacuously; (c) a
  different singular $\lambda$ gives $\chi=\aleph_{\beta+1}$. (a) adds
  $\aleph_0$, absorbed. (b) The definition requires a witness $\mu_0$ and
  every $2^{\aleph_\gamma}=\aleph_{\gamma+1}$ is below $\aleph_\beta$.
  (c) Under GCH $\chi=\lambda$ for every infinite $\lambda$ (a limit
  $\lambda$ is the supremum of the successors below it; a successor
  $\nu^+$ has $2^\nu=\nu^+$), so $\chi=\aleph_{\beta+1}$ forces
  $\lambda=\aleph_{\beta+1}$, regular; the section states only the
  $\lambda=\aleph_\beta$ case, which is the case its sentence names. Failed.
- **S6.** Attack: (T2) with $\rho_\nu=4$ or with exponent $3$. (T2) is
  stated for pairs on a singular $\lambda$ and its proof colors pairs;
  $\aleph_{\beta+1}$ is regular. Failed.
- **S7.** Attack: (a) Problem 1167 restricts $\gamma$ to finitely many
  colors or excludes $\kappa_0=\lambda$; (b) the addition is ordinal. The
  corpus statement bounds nothing and fixes cardinal addition (W2). The
  survey's own Problem 2 prints "$\gamma\le2$" (F7), but the section cites
  Problem 1167, not Problem 2. Failed.
- **S8.** Attack: (a) the imported theorem has $\lambda$ colors rather
  than $\operatorname{cf}\lambda$; (b) its hypothesis at $\aleph_\omega$
  is not met by GCH; (c) a color-$0$ homogeneous set of cardinality
  $\aleph_\beta$ concentrated in fewer than $\aleph_{\omega+1}$ blocks; (d)
  a monochromatic triangle inside a block. (a) The page image prints
  $(3)_{\operatorname{cf}(\lambda)}$. (b) $2^{\aleph_\omega}=\aleph_{\omega+1}$
  under GCH. (c) and (d) are excluded in W1 by regularity of
  $\aleph_{\omega+1}$ and by the in-block color $0$. Failed.
- **S9, S10.** Attack: a positive answer to Problem 1167 could be a
  consistency statement rather than a ZFC implication, or a GCH model
  where (S) fails might also make $R$ fail. The corpus statement asks
  whether the implication is true, so a positive answer holds in every
  model, in particular every GCH model; and $R$ holds in every GCH model
  by W1 because the imported theorem is a ZFC implication from
  $2^\lambda=\lambda^+$. Failed.
- **S11.** Not a claim; the sentence "recorded for both problem pages"
  describes text outside the read set (F5).

## Premises

- **Problem 1218, Statement** (`wiki/problems/set_theory/E1218/_index.md`, lines
  12--37 as of 2026-09-28T13:50:48Z): GCH,
  $\lambda=\aleph_{\omega_{\omega+1}+1}$, $\lambda\not\to(\lambda,4,\ldots,4)^3$
  with countably many $4$s; printed Status "Open". Read in full.
- **Problem 1167, Statement** (`wiki/problems/set_theory/E1167/_index.md`, lines
  12--42): for finite $r\ge2$, infinite $\lambda$, cardinals $\kappa_\alpha$
  ($\alpha<\gamma$): does $2^\lambda\to(\kappa_\alpha+1)^{r+1}_{\alpha<\gamma}$
  imply $\lambda\to(\kappa_\alpha)^r_{\alpha<\gamma}$, with cardinal
  addition. No bound on $\gamma$, no lower bound on $\kappa_\alpha$. Read in
  full.
- **Problem 1168, Statement** (`wiki/problems/set_theory/E1168/_index.md`, lines
  13--32): prove
  $\aleph_{\omega+1}\not\to(\aleph_{\omega+1},3,\ldots,3)^2_{\aleph_0}$ without
  GCH. Read in full.
- **(T2)** (connections page, lines 68--88): $\lambda$ singular,
  $\kappa=\operatorname{cf}\lambda$, $\gamma\ge1$, $\rho_\nu\ge2$,
  $\kappa\not\to(\kappa,(\rho_\nu)_{\nu<\gamma})^2$ implies
  $\lambda\not\to(\lambda,(\rho_\nu)_{\nu<\gamma})^2$. Its proof is
  another reviewer's subject; the interface was confirmed at the section's
  use and the argument re-derived in the instance (W1). (T1) and (T3) are
  not consumed by the section.
- **Theorem 1.2 reconstruction** (Definitions, Sum formula, Imported
  results, Statement): the definitions of "eventually $\ge\lambda$", "not
  eventually constant" and $\chi$; the hypotheses $\kappa\to(\kappa)^2_2$,
  not eventually constant, eventually $\ge\lambda$; the imported (S)
  Sierpiński relation $2^\mu\not\to(\mu^+)^2_2$ used only in a remark here
  (F3). Taken as established at its reviewed standing.
- **Lemma 1.1 and Corollary 1.3 reconstructions**: Statement sections
  only; they confirm that the mechanism produces positive relations for
  pairs from positive relations on blocks.
- **Komjáth, The Erdős--Hajnal problem list, Bull. Symb. Logic 31 (2025)
  418--461**, held. Problem 1 (p. 419), Problem 2 with its list (a)--(e)
  of proved special cases (p. 419), Problem 4's necessity remark (p. 419),
  Problem 5 and its commentary (p. 420); bibliography entry [45]
  (p. 449 of the extraction's pagination). Read on page images for
  pp. 419--420, text extraction for [45]. The survey's Problem 2 as printed
  reads "$\gamma\le2$" in its hypotheses.
- **[45] Erdős, Hajnal, Máté and Rado, Combinatorial Set Theory: Partition
  Relations for Cardinals, North-Holland, 1984**, not held. Its Section 20
  theorem enters only through the survey's sentence; the section's premise
  $R$ is author-recorded at that standing.
- **Erdős, Hajnal and Rado (1965)**, not held; the catalog's citation
  "[EHR65, p. 131]" was not checked.
- **The catalog pages** of Problems 1218 and 1167 at erdosproblems.com: not
  read (web excluded).

## Findings

- **F1 (suggested).** Location: "Komjáth's commentary on Problem 5
  (p. 419) records the theorem of [45, Section 20]". Defect: Problem 5 and
  its commentary are printed on p. 420 of the survey (PDF p. 3); p. 419
  ends inside the commentary on Problem 4. Witness: the rendered page
  images of PDF pp. 2--3, whose running heads read 419 and 420. The
  theorem itself is transcribed exactly. Replacement: "(p. 420)".
- **F2 (suggested).** Location: "for ordinals $\beta$ with
  $\beta>\operatorname{cf}\beta>\operatorname{cf}\beta-1>\operatorname{cr}\beta$,
  with $\beta=\omega_{\omega+1}$ the least such ordinal (the page does not
  define $\operatorname{cr}$)". Defect: under the page's own convention
  $\operatorname{cf}\beta$ is the cofinality of the ordinal $\beta$, and
  $\omega_{\omega+1}$ is a regular cardinal, so $\beta>\operatorname{cf}\beta$
  is false at the ordinal named as least and $\operatorname{cf}\beta-1$ is
  undefined; the transcription silently changes convention. Witness: the
  computation $\operatorname{cf}\omega_{\omega+1}=\omega_{\omega+1}$. Under
  the index reading, in which $\operatorname{cf}\beta$ is the ordinal
  $\delta$ with $\operatorname{cf}\aleph_\beta=\aleph_\delta$ and
  $\operatorname{cr}\beta$ the ordinal $\varepsilon$ with
  $\operatorname{cf}\aleph_{\delta-1}=\aleph_\varepsilon$, the condition
  says that $\aleph_\beta$ is singular, that its cofinality is a successor
  cardinal $\aleph_{\delta}=\aleph_{(\delta-1)+1}$, and that
  $\aleph_{\delta-1}$ is singular; the least instance is $\delta-1=\omega$,
  $\delta=\omega+1$, and the least limit ordinal $\beta$ with
  $\operatorname{cf}\beta=\omega_{\omega+1}$ is $\omega_{\omega+1}$, so the
  sentence is then correct, the target count is
  $\aleph_{\operatorname{cr}\beta}=\aleph_0$, and the conjecture is exactly
  the stepping-up of
  $\aleph_\delta\not\to(\aleph_\delta,(3)_{\operatorname{cf}\aleph_{\delta-1}})^2$.
  This reading is the reviewer's reconstruction; the catalog page and the
  1965 paper are outside the read set. Replacement: after "(the page does
  not define $\operatorname{cr}$)", add a clause such as "and writes
  $\operatorname{cf}\beta$ for the index $\delta$ with
  $\operatorname{cf}\aleph_\beta=\aleph_\delta$, so that
  $\operatorname{cf}\beta=\omega+1$ here; with this page's convention the
  displayed condition would fail at $\beta=\omega_{\omega+1}$".
- **F3 (note).** Location: "$\sum_{\gamma<\beta}\aleph_{\gamma+1}=\aleph_\beta$"
  and "its hypothesis 'eventually $\ge\lambda$' fails". The displayed sum
  omits the finite $\mu$ that the theorem page's $\chi$ includes; the
  omission adds $\aleph_0$ and changes nothing. The obstruction can be
  stated more strongly, at no cost: under GCH $\chi=\lambda$ for every
  infinite $\lambda$, so no singular $\lambda$ makes $\chi=\aleph_{\beta+1}$;
  and Theorem 1.2's other hypothesis $\kappa\to(\kappa)^2_2$ also fails at
  $\lambda=\aleph_\beta$, since $\kappa=\aleph_{\omega+1}=2^{\aleph_\omega}$
  under GCH and $2^{\aleph_\omega}\not\to(\aleph_{\omega+1})^2_2$ by the
  Sierpiński relation the theorem page imports. No change is required.
- **F4 (note).** Location: "the theorem of [45, Section 20]". The
  reference number is the survey's; the page never names [45]. Naming it
  (Erdős, Hajnal, Máté and Rado, Combinatorial Set Theory: Partition
  Relations for Cardinals, 1984, not held) would make the citation
  self-contained and make its standing, a source not held, visible where
  it is used.
- **F5 (note).** Sentences outside the read set, listed so the integrator
  knows they were not checked here and are not defects found: "no compiled
  assessment"; the catalog page's current text, its "last edited" date and
  its forum contents; "the case its authors could not settle even under
  GCH per the catalog page of Problem 1167"; and "recorded for both
  problem pages" in the Outcome. The survey's list (a)--(e) of proved
  special cases of the stepping-up lemma is consistent with the instance
  being unsettled, since $r=2$ and $\kappa_1=3$ is finite, $\kappa_0$
  singular; it does not by itself support the words "even under GCH".
- **F6 (note).** The labels "the site's form" and "the page's form" name
  (S) and (P), but the page's form was also the site's wording on
  2026-09-04, and the Target paragraph introduces (S) as "the site's
  current one". Writing "the site's current form" throughout the Context
  and Outcome paragraphs would remove the ambiguity.
- **F7 (note).** The survey's Problem 2, its own statement of the
  negative stepping-up question, prints the hypothesis "$\gamma\le2$",
  which as printed would exclude the $\aleph_0$-color instance used here;
  the section correctly cites the corpus statement of Problem 1167, which
  has no such bound. Should the survey's Problem 2 ever be cited for this
  instance, the printed bound must be addressed.

## Verdict

- **S1**: refutation-failed.
- **S2**: refutation-failed.
- **S3**: not a claim of the section's mathematics; reportage of a page
  outside the read set, with the convention gloss of F2 needed for the
  sentence to be true under the page's own notation.
- **S4**: refutation-failed.
- **S5**: refutation-failed.
- **S6**: refutation-failed.
- **S7**: refutation-failed.
- **S8**: refutation-failed, at the author-recorded standing the section
  assigns it; its standing is bounded by that of the imported Section 20
  theorem, known here only through the survey's sentence.
- **S9**: refutation-failed, as the conditional it is written as.
- **S10**: refutation-failed, as the conditional it is written as.
- **S11**: not a claim.

Required corrections: none. Suggested: F1 (a page number) and F2 (a
convention gloss). Notes: F3--F7.

**Limitations.** The imported theorem behind $R$ was checked against the
survey's printed sentence and not against its source, which is not held;
the catalog pages, their edit history and forum, and the 1965 paper were
not read; the proof of (T2) is another reviewer's subject, and the
re-derivation in W1 is a check of the instance, not a review of the tool.
This focused review assigns no tier and changes no status.
