---
name: research/erdos_1171/evidence/verify/connections_problem_1168_review
title: "Independent review of the connections section: Problem 1168"
desc: |
  Refutation review of the Problem 1168 section of the connections page:
  ten statements, all refutation-failed; no required correction, one
  suggested source-fidelity correction and four notes.
created: 2026-09-28T19:03:59Z
updated: 2026-09-28T19:03:59Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation. The reviewer took no part in writing the connections page, the
reconstruction pages or their sources, received only the assignment, and
read no verification record, grade or standing text of this folder.

**Subject.** Page `wiki/research/erdos_1171/connections.md` as it stood on
2026-09-28T13:50:48Z, section `## Problem 1168`,
lines 597--619 (heading at line 597, last content line 618, next H2 at
line 620). The section files no lead page: its outcome line reads "Fails;
no lead", so there is no lead page to review.

**Read, and at what depth.**

- The subject page: frontmatter, scope paragraph and Tools section (lines
  1--123) in full, as the page's shared conventions and the interfaces of
  (T1)--(T5), whose proofs are another reviewer's; the section "Problems
  1174, 595 and 596" (lines 549--596) in full, because the subject section
  consumes its bit coloring by the words "One remark of the previous
  section applies", and that witness is re-derived below.
- The reconstruction pages
  [[research/erdos_1171/lemma_2_1_reconstruction|Lemma 2.1]] and
  [[research/erdos_1171/theorem_3_1_reconstruction|Theorem 3.1]] in full,
  as premises at the standing the assignment states: their statements,
  definitions, facts 1 and 2 of the lemma page, and the paragraph "An
  alternative bridge" of the theorem page, the only place where the term
  "Ramsey bridge" is explained.
- [[problems/set_theory/E1168/_index|Problem 1168]]: the statement block under
  its H1 (lines 13--32) only; the page has no `## Statement` heading.
- [[../library/set_theory/garti_2025_problem_erdos_hajnal/_index|Garti, Hayut and Shelah]]:
  the card's provenance and digest paragraph and its list of results to
  transcribe; the held PDF (arXiv:2502.16625v2) by text extraction at the
  abstract, the introduction (pp. 2--3), Theorem 1.1 (p. 5), Corollary 1.2
  and Theorem 1.3 (p. 7), Theorem 2.2 (pp. 10--11), the forcing argument at
  $\lambda=\aleph_\omega$ (pp. 15--18) and Theorem 3.3 (p. 20). No page
  images were read.
- [[../library/set_theory/erdos_1956_partition_calculus_set_theory/_index|Erdős and Rado 1956]]:
  the card's provenance paragraph and the held PDF by text extraction at
  the definition of the partition relation (printed pp. 429--430) and
  Theorem 44 (printed p. 475), the statement the section invokes as the
  Erdős--Dushnik--Miller theorem without a citation.
- `docs/verification.md` sections "Whole-claim report", "Audit checklist"
  and "Grading and claim standing" (the shared and the Erdos-specific
  versions of the first two), `docs/approach_vetting.md`,
  `docs/evidence.md` section "Source fidelity" and `docs/math_authoring.md`.

**Exposures.** Four, none bearing on a verdict. (1) The section "Problem
597: graph targets" of the subject page (lines 318--409) was read while
locating where the term "Ramsey bridge" is defined; it holds no review,
standing or acceptance text, and nothing from it is used here. (2) The
heading list of the Problem 1168 page was seen while locating its
statement; the bodies of `Current assessment`, `Progress`, `Known Results`
and `Linked library material` were not read. (3) The digest paragraph of
the Garti--Hayut--Shelah card carries one editorial sentence on the
problem's openness and one on Problem 597; both were read and neither is
used. (4) Each reconstruction page opens with a Standing paragraph
(author-recorded reconstruction; unrefereed deposit); it was read as part
of the premise pages. No `_index.md`, nothing under any `evidence/`
folder, no review or grade, and no web page was read.

## Restatement

Conventions. Colorings, homogeneous sets, triangles and the relation
$\alpha\to(\beta_0,\ldots,\beta_{n-1})^2_n$ are those of the lemma page:
the subscript counts the colors, color $0$ carries the large target, and a
homogeneous set of order type $\beta_i$ is meant. A cardinal is its initial
ordinal. The catalog and the held sources use the cardinality form, in
which the large homogeneous set has cardinality $\kappa$; when the large
target is the ambient cardinal the two forms coincide, because a subset of
the ordinal $\kappa$ of cardinality $\kappa$ has order type exactly
$\kappa$: its order type is an ordinal of cardinality $\kappa$, so at least
$\kappa$, and at most $\kappa$ as a subset of $\kappa$. The section's ten
statements:

- **S1 (target).** Problem 1168, carried at status `open`, asks for a proof
  without GCH, that is in ZFC, of
  $\aleph_{\omega+1}\not\to(\aleph_{\omega+1},3,\ldots,3)^2_{\aleph_0}$:
  a coloring $c:[\aleph_{\omega+1}]^2\to\omega$ with no set of cardinality
  $\aleph_{\omega+1}$ homogeneous in color $0$ and no triangle homogeneous
  in any color $\gamma\ge1$.
- **S2 (source characterization).** The library card of Garti, Hayut and
  Shelah records (a) the classical case: for singular $\lambda$ with
  $2^\lambda=\lambda^+$,
  $\lambda^+\not\to(\lambda^+,(3)_{\mathrm{cf}(\lambda)})^2$; and (b) the
  consistency of that negative relation with $2^\lambda>\lambda^+$ under
  pcf and guessing hypotheses.
- **S3 (imported theorem).** For every infinite cardinal $\kappa$,
  $\kappa\to(\kappa,\omega)^2$ (Erdős--Dushnik--Miller), read in the
  order-type convention: every two-coloring of $[\kappa]^2$ has a subset of
  order type $\kappa$ homogeneous in color $0$ or a subset of order type
  $\omega$ homogeneous in color $1$.
- **S4.** For every infinite cardinal $\kappa$, $\kappa\to(\kappa,3)^2$.
- **S5.** For every infinite cardinal $\kappa$ and every finite $k$,
  $\kappa\to(\kappa,3,\ldots,3)^2_{k+1}$ with $k$ triangle targets, by
  Lemma 2.1 at $\alpha=\kappa$.
- **S6.** The conclusion of S5 also follows, by the Ramsey bridge, from
  $\kappa\to(\kappa,n)^2$ for finite $n$.
- **S7 (obstruction).** The problem's relation has $\aleph_0$ colors; the
  color-merging induction proves the relation for each finite $k$ and has
  no limit step, so it does not reach the $\aleph_0$-color relation.
- **S8 (conditional witness).** If $\aleph_{\omega+1}\le2^{\aleph_0}$, the
  bit coloring of the previous section witnesses
  $\aleph_{\omega+1}\not\to(\aleph_{\omega+1},3,3,\ldots)^2_{\aleph_0}$,
  which is the problem's relation.
- **S9 (reduction).** Hence the content of the problem is the case
  $2^{\aleph_0}<\aleph_{\omega+1}$, and the cited work operates in that
  case.
- **S10 (outcome).** The mechanism of the folder gives no lead on Problem
  1168: only the finite-color positive relations transfer, and they are
  trivial.

## Checklist

- **Quantifiers and scope.** Pass. S3--S5 quantify over every infinite
  cardinal, singular ones included, and every finite $k$; S5 includes
  $k=0$, the one-color relation, which holds outright since $\kappa$ itself
  is homogeneous under the only coloring. S8 states its hypothesis. S6
  leaves $n$ unquantified (F3, a note). S9's case split is a trichotomy of
  cardinals, so no case is dropped.
- **Circularity.** Pass. The only inputs are an external theorem (S3), the
  reviewed Lemma 2.1, the finite Ramsey theorem and the bit coloring; none
  is equivalent to a statement of the section, and no statement of the
  section is the problem's relation or its negation.
- **Model and convention changes.** Pass with a note. The held sources
  state S3 and the problem in the cardinality convention and the section
  states them in the order-type convention; the bridge is the sentence
  under Conventions above together with the fact that an infinite set of
  ordinals has a subset of order type $\omega$. The section leaves it
  implicit (F2). The countable-color relation is read with the subscript
  counting colors, as on the lemma page and in the source's definition of
  $\lambda\to(\kappa,(3)_\theta)^2$.
- **Finite and statistical overreach.** Pass. The finite-color positives
  are not used to say anything about the $\aleph_0$-color relation; the
  section says the opposite (S7).
- **Uniformity.** Pass. The only parameter-dependent quantity is the Ramsey
  number in S6, which depends on $k$ and is used for one $k$ at a time.
- **Extremal conclusions.** Inapplicable; the section states no extremum.
- **Consequences and composition.** Pass with a note. Each "so" is checked
  separately below: S3 to S4 by (T2); S4 to S5 within Lemma 2.1's
  hypotheses; S3 to S6 by (T2) and the finite Ramsey theorem; S8 to S9 by
  the trichotomy of cardinals. S9 is true as written and can be sharper
  (F4).
- **Computation.** Inapplicable; no computation is claimed.
- **Reproduction.** Inapplicable; no rerun command or coverage line is
  claimed.
- **Source and verdict fidelity.** One suggested correction. S1 matches the
  problem page's statement block in every clause. S2 is faithful to the
  card but, checked against the held PDF, reads more than the source proves
  on the guessing route and omits the large-cardinal hypotheses of the
  consistency results (F1). S3 is invoked by name with no citation; the
  held Erdős--Rado paper states it as Theorem 44 (F2). The clause "which is
  where the cited work operates" is confirmed by the source's standing
  assumption $2^{\mathrm{cf}(\lambda)}<\lambda$ (p. 2). The section quotes
  no verdict of another reviewer.

## Weakest steps

**W1: the convention bridge behind S3--S5.** Theorem 44 of Erdős and Rado
(printed p. 475) states, for every cardinal $a\ge\aleph_0$,
$a\to(\aleph_0,a)^2$ in the cardinality form of their Section 1: whenever
$|S|=a$ and $[S]^2=K_0\cup K_1$ with $K_0\cap K_1=\emptyset$, some
$B\subseteq S$ has $|B|=\aleph_0$ and $[B]^2\subseteq K_0$, or has $|B|=a$
and $[B]^2\subseteq K_1$. Swapping the two classes gives
$a\to(a,\aleph_0)^2$. Take $S=\kappa$, the initial ordinal, and a coloring
$c:[\kappa]^2\to\{0,1\}$; put $K_0=c^{-1}(0)$ and $K_1=c^{-1}(1)$. Either
some $B$ with $|B|=\kappa$ is homogeneous in color $0$, and then
$\operatorname{otp}(B)=\kappa$ by the sentence under Conventions; or some
infinite $B$ is homogeneous in color $1$, and its first $\omega$ elements
form a subset of order type $\omega$ homogeneous in color $1$. This is S3
in the order-type form. S4 is (T2) with $3\le\omega$. S5: Lemma 2.1 asks
for an ordinal $\alpha$ with $\alpha\to(\alpha,3)^2$ and returns, for every
finite $k\ge1$, $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$; $\kappa$ is an
ordinal and S4 is the hypothesis, so S5 holds for $k\ge1$, and for $k=0$
outright. The proof of Theorem 44 treats singular $a$ in its Case 2, so
nothing restricts S3--S5 to regular cardinals.

**W2: the witness of S8 in the problem's own convention.** Assume
$\aleph_{\omega+1}\le2^{\aleph_0}$ and fix an injection
$\iota:\aleph_{\omega+1}\to2^\omega$. Color $\{x,y\}$ by $1+n$, where $n$
is the least position at which $\iota(x)$ and $\iota(y)$ differ; $n$
exists because $\iota$ is injective. The coloring takes values in
$\{1,2,\ldots\}\subseteq\omega$, so it is a coloring with $\aleph_0$ colors
in which color $0$ is unused. No set with two or more elements is
homogeneous in color $0$, since it contains a pair and no pair has color
$0$; in particular no set of cardinality $\aleph_{\omega+1}$, and no set of
order type $\aleph_{\omega+1}$, is. If $\{x,y,z\}$ were homogeneous in
color $1+n$, the three sequences $\iota(x)$, $\iota(y)$, $\iota(z)$ would
agree below $n$ and differ pairwise at $n$, which needs three distinct
bits. So the coloring witnesses
$\aleph_{\omega+1}\not\to(\aleph_{\omega+1},(3)_{\aleph_0})^2$ in the
source's definition (a $0$-homogeneous set of full cardinality or a
$\gamma$-homogeneous triangle with $0<\gamma<\aleph_0$) and equally in the
order-type form. The source records the same fact on p. 2: forcing
$2^{\mathrm{cf}(\lambda)}\ge\lambda^+$ gives the negative relation, as the
monograph of Erdős, Hajnal, Máté and Rado notes.

**W3: the reduction S9.** By the trichotomy of cardinals, either
$\aleph_{\omega+1}\le2^{\aleph_0}$, where S8 settles the problem
negatively, or $2^{\aleph_0}<\aleph_{\omega+1}$. Since
$\operatorname{cf}(2^{\aleph_0})>\aleph_0=\operatorname{cf}(\aleph_\omega)$
by König's theorem, $2^{\aleph_0}\ne\aleph_\omega$, so the second case is
$2^{\aleph_0}<\aleph_\omega$, that is, $2^{\aleph_0}=\aleph_n$ for some
finite $n$. That is the source's standing assumption
$2^{\mathrm{cf}(\lambda)}<\lambda$ at $\lambda=\aleph_\omega$ (p. 2), and
every consistency result of the source has $\lambda$ a strong limit, which
is stronger. So the cited work operates inside the case S9 names. The case
is not all open: its sub-case $2^{\aleph_\omega}=\aleph_{\omega+1}$ is the
classical theorem the section itself records (Theorem 0.1 of the source at
the singular cardinal $\lambda=\aleph_\omega$), so what remains is
$2^{\aleph_0}<\aleph_\omega$ together with
$2^{\aleph_\omega}>\aleph_{\omega+1}$ (F4).

## Strongest attack

- **S1.** Compared clause by clause with the problem page's statement
  block: the relation, the subscript, the "without GCH" qualification and
  the status agree. No attack is available.
- **S2.** Attacked as a source characterization. Against the card: the card
  lists Theorem 0.1 as the classical case and describes Theorem 1.1,
  Corollary 1.2 and Theorem 1.3 as giving the negative relation with
  $2^\lambda>\lambda^+$ under pcf-style scales and a guessing principle, so
  the sentence reports the card correctly and survives as stated. Against
  the held PDF the attack lands in part: the hypotheses (a)--(h) of Theorem
  1.1 are cardinal-arithmetic and pcf conditions with no guessing
  principle; the guessing principle enters only in Theorem 3.3 (from
  stick), and the source says on p. 3 that it does not know whether stick
  at $\lambda$ is consistent with $2^\lambda>\lambda^+$ for strong limit
  singular $\lambda$; and the consistency results assume a supercompact
  cardinal (Corollary 1.2, and the argument at $\aleph_\omega$) or a strong
  cardinal (Theorem 1.3). The sentence is therefore true of the card and
  imprecise about the mathematics; filed as F1, suggested, since no
  deduction of the section consumes it.
- **S3.** Attacked at singular $\kappa$, where the original argument of
  Dushnik and Miller needed Erdős's addition: the held Theorem 44 covers
  every $a\ge\aleph_0$ and its proof treats $a'<a$ separately. Attacked at
  the convention: the bridge of W1 closes it. Failed.
- **S4, S5.** Attacked by looking for a hypothesis of Lemma 2.1 that a
  cardinal might miss: the lemma needs only an ordinal with
  $\alpha\to(\alpha,3)^2$, used on subsets of order type exactly $\alpha$,
  which fact 1 of the lemma page transports; the cardinal $\kappa$ is an
  ordinal. Failed.
- **S6.** Attacked by asking which $n$: the bridge needs
  $\kappa\to(\kappa,n)^2$ for $n$ the least integer such that every
  $k$-coloring of the pairs of an $n$-element set has a monochromatic
  triangle, which exists by the finite Ramsey theorem, and S3 with (T2)
  gives $\kappa\to(\kappa,n)^2$ for every finite $n$. Re-derived: given
  $c:[\kappa]^2\to\{0,\ldots,k\}$, merge the colors $1,\ldots,k$ into $1$;
  a color-$0$ set of type $\kappa$ is what is wanted, and an $n$-element
  set all of whose pairs have merged color $1$ carries a $k$-coloring by
  $c$, hence a triangle homogeneous in some color $j\in\{1,\ldots,k\}$. The
  statement survives; the unquantified $n$ is F3.
- **S7.** Attacked by trying to build a limit step. Given
  $c:[\aleph_{\omega+1}]^2\to\omega$, merging every color above $k$ into
  $0$ gives a coloring with the colors $0,\ldots,k$, and S5 gives for each
  $k$ either a triangle homogeneous under $c$ in a color in
  $\{1,\ldots,k\}$ or a set $Y_k$ of full type on which $c$ takes values in
  $\{0\}\cup(k,\omega)$; the sets $Y_k$ need not have a common subset of
  full type, and no diagonal argument produces one. The attack cannot
  succeed in ZFC at all: the $\aleph_0$-color positive relation at
  $\aleph_{\omega+1}$ fails under $2^{\aleph_\omega}=\aleph_{\omega+1}$
  (Theorem 0.1 of the source) and under $\aleph_{\omega+1}\le2^{\aleph_0}$
  (S8), so no ZFC argument, with or without a limit step, reaches it. The
  obstruction stands; that it is an obstruction of the statement rather
  than of the proof is F5.
- **S8.** Attacked in the problem's convention (W2), at the hypothesis (the
  injection exists exactly when $\aleph_{\omega+1}\le2^{\aleph_0}$) and at
  the color count (the colors $1+n$ for $n<\omega$ are $\aleph_0$ many, and
  the unused color $0$ is allowed by the definition on the lemma page and
  by the source's, both of which quantify over all colorings into the color
  set). Failed.
- **S9.** Attacked at the case split (W3) and at the clause about the cited
  work, which p. 2 of the source confirms. Failed; sharpened in F4.
- **S10.** Attacked by looking for a transfer the section misses. The
  mechanism produces positive relations from positive relations ((T3),
  (T4)), and its one negative-direction tool, (T5), turns a finite-color
  witness into a two-color witness, which cannot exist at
  $\aleph_{\omega+1}$ by S3 and transport; a countable analog of (T5) is
  false, since under $2^{\aleph_\omega}=\aleph_{\omega+1}$ the
  $\aleph_0$-color relation fails while every finite-color relation holds
  by S5. Nothing in the folder bears on the case S9 leaves open. Failed.

## Premises

- [[research/erdos_1171/lemma_2_1_reconstruction|Lemma 2.1]]: for an
  ordinal $\alpha$ with $\alpha\to(\alpha,3)^2$ and every finite $k\ge1$,
  $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$ with $k$ triangle targets; with
  fact 1 (transport along order isomorphisms) and fact 2 (relabeling of
  colors). Read in full; treated as established at the standing the
  assignment states; used at $\alpha=\kappa$ within its hypotheses.
- [[research/erdos_1171/theorem_3_1_reconstruction|Theorem 3.1]]: read in
  full; its theorem is not used by the section. Its paragraph "An
  alternative bridge" describes the Ramsey bridge as an author-recorded
  step with no written source; the section uses that bridge at $\kappa$,
  and the S6 attack re-derives it here.
- Tool (T2) of the subject page (restriction and weakening; a target may be
  replaced by a smaller one, a color left unused): interface confirmed;
  proof another reviewer's. (T3)--(T5) are not used by the section.
- The bit coloring of the section "Problems 1174, 595 and 596" (subject
  page, lines 549--596): for every order type $\alpha$ with
  $2\le|\alpha|\le2^{\aleph_0}$,
  $\alpha\not\to(\alpha,3,3,\ldots)^2_{\aleph_0}$, author-recorded;
  re-derived in W2 at $\alpha=\aleph_{\omega+1}$.
- Erdős and Rado 1956, Theorem 44 (held PDF, printed p. 475; text
  extraction): for every cardinal $a\ge\aleph_0$, $a\to(\aleph_0,a)^2$ in
  the cardinality convention of the paper's Section 1 (printed
  pp. 429--430). Held. Not cited by the section (F2).
- Garti, Hayut and Shelah, arXiv:2502.16625v2 (held PDF; text extraction):
  Theorem 0.1 (p. 2; $\lambda$ singular and $2^\lambda=\lambda^+$ imply
  $\lambda^+\not\to(\lambda^+,(3)_{\mathrm{cf}(\lambda)})^2$); the remark
  on p. 2 that $2^{\mathrm{cf}(\lambda)}\ge\lambda^+$ gives the negative
  relation, and the standing assumption $2^{\mathrm{cf}(\lambda)}<\lambda$;
  Question 0.2 (p. 2); Theorem 1.1 (p. 5, hypotheses (a)--(h): $\mu$
  singular strong limit with $2^\mu>\mu^+$, an increasing sequence of
  singular strong limit cardinals $\mu_i$ of the same cofinality with
  $2^{\mu_i}=\mu_i^+$ and union $\mu$, and true cofinality $\mu^+$ of the
  product of the $\mu_i^+$ modulo the bounded ideal); Corollary 1.2 (p. 7,
  from a supercompact cardinal); Theorem 1.3 (p. 7, from a strong
  cardinal, at $\mu=\aleph_{\omega^2}$); the argument of the second section
  forcing the negative relation at $\lambda=\aleph_\omega$ with
  $2^{\aleph_\omega}=\aleph_{\omega+2}$ (pp. 15--18, from a supercompact
  cardinal); Theorem 3.3 (p. 20, from stick at $\lambda$) and the remark
  on p. 3 that the consistency of stick with $2^\lambda>\lambda^+$ at
  strong limit singular $\lambda$ is not known. Held.
- The finite Ramsey theorem for triangles in $k$ colors and König's theorem
  ($\operatorname{cf}(2^{\aleph_0})>\aleph_0$): standard, used in W3 and
  the S6 attack; no library source consulted.
- [[problems/set_theory/E1168/_index|Problem 1168]]: statement block only.

## Findings

- **F1 (suggested).** Location: lines 603--605, "records the classical case
  $2^\lambda=\lambda^+$ and the consistency of the negative relation with
  $2^\lambda>\lambda^+$ under pcf and guessing hypotheses." Defect: read
  against the held PDF, the consistency of the negative relation with
  $2^\lambda>\lambda^+$ is obtained on the pcf route only (Corollary 1.2,
  Theorem 1.3 and the second section at $\aleph_\omega$), each from a
  supercompact or a strong cardinal; the guessing route (Theorem 3.3, from
  stick) yields the negative relation, and the source states on p. 3 that
  whether stick at $\lambda$ is consistent with $2^\lambda>\lambda^+$ for
  strong limit singular $\lambda$ is not known. The sentence attributes the
  consistency to both kinds of hypothesis and omits the large-cardinal
  hypotheses. It follows the card's digest, which places a guessing
  principle among the hypotheses of Theorem 1.1; the theorem's list
  (a)--(h) contains none. Witness: the PDF, pp. 3, 5, 7, 18 and 20.
  Replacement: "records the classical case $2^\lambda=\lambda^+$ (Theorem
  0.1), the negative relation from pcf hypotheses (Theorem 1.1) and from
  the guessing principle stick (Theorem 3.3), and, from a supercompact or a
  strong cardinal, the consistency of the negative relation with
  $2^\lambda>\lambda^+$ along the pcf route (Corollary 1.2, Theorem 1.3 and
  the second section at $\lambda=\aleph_\omega$)." The card's own digest is
  outside this review's subject.
- **F2 (note).** Location: lines 607--609, "by the Erdős--Dushnik--Miller
  theorem $\kappa\to(\kappa,\omega)^2$ for every infinite cardinal
  $\kappa$". Defect: no source is cited, although the page's scope
  paragraph says that sources are cited at the standing their library
  pages record, and the theorem is stated in the order-type convention
  while the held source states it in the cardinality convention. Witness:
  Theorem 44 of the held Erdős--Rado paper. Replacement: cite
  [[../library/set_theory/erdos_1956_partition_calculus_set_theory/_index|Erdős and Rado 1956]],
  Theorem 44, and add "a subset of $\kappa$ of cardinality $\kappa$ has
  order type $\kappa$, so the cardinality form gives the order-type form".
- **F3 (note).** Location: lines 610--611, "the Ramsey bridge gives the
  same from $\kappa\to(\kappa,n)^2$". Defect: $n$ is unquantified; the
  bridge for $k$ triangle colors needs $n$ equal to the $k$-color Ramsey
  number of the triangle. Replacement: "from $\kappa\to(\kappa,n)^2$ for
  every finite $n$, which (T2) gives from the same theorem".
- **F4 (note).** Location: lines 614--616, "so the content of the problem
  is the case $2^{\aleph_0}<\aleph_{\omega+1}$, which is where the cited
  work operates." Defect: true, but the sub-case
  $2^{\aleph_\omega}=\aleph_{\omega+1}$ is the classical theorem the Target
  paragraph records, and by König's theorem the case equals
  $2^{\aleph_0}<\aleph_\omega$, the source's own standing assumption.
  Replacement: "so the content of the problem is the case
  $2^{\aleph_0}<\aleph_\omega$ (the same as $2^{\aleph_0}<\aleph_{\omega+1}$
  by König's theorem) with $2^{\aleph_\omega}>\aleph_{\omega+1}$, the
  classical case being settled; the cited work operates there, with
  $\aleph_\omega$ a strong limit."
- **F5 (note).** Location: line 612, "where the induction has no limit
  step." Defect: none in the sentence; the record can say, as the previous
  section does for its targets, that the obstruction is of the statement:
  the $\aleph_0$-color positive relation at $\aleph_{\omega+1}$ fails under
  $2^{\aleph_\omega}=\aleph_{\omega+1}$ and under
  $\aleph_{\omega+1}\le2^{\aleph_0}$, so no ZFC argument reaches it, and
  the mechanism produces positive relations while the problem asks for a
  negative one.

## Verdict

- S1: refutation-failed.
- S2: refutation-failed as a report of what the card records; as a
  characterization of the held source it needs the precision of F1.
- S3: refutation-failed.
- S4: refutation-failed.
- S5: refutation-failed.
- S6: refutation-failed.
- S7: refutation-failed.
- S8: refutation-failed.
- S9: refutation-failed.
- S10: refutation-failed.

Required corrections: none. Suggested: F1. Notes: F2--F5.

Limitations. The held PDFs were read by text extraction and not on page
images; the statements relied on (Theorem 0.1, the remarks on p. 2, the
hypothesis list of Theorem 1.1, Corollary 1.2, Theorem 1.3, Theorem 3.3 and
Theorem 44 of Erdős and Rado) extracted legibly. The proofs of (T1)--(T5)
and of the reconstruction pages were not re-verified here; the section uses
only (T2) and Lemma 2.1, both within their stated hypotheses. The bit
coloring was re-derived because the section consumes it as a witness. This
review does not assess the proofs of the cited sources.

This focused review assigns no tier and changes no status.
