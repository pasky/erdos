---
name: research/erdos_1219/evidence/verify/connections_problem_1167_the_negative_stepping_up_lemma_review
title: "Independent review of the connections section: Problem 1167: the negative stepping-up lemma"
desc: |
  Refutation-failed for the section's restatement of Problem 1167, its
  no-transfer obstruction, the trivial negative relation, the conditional
  deduction, the compatibility remark and the placement of Problem 1218; one
  required correction (the closing clause names only the conjecture while its
  support in the text also needs the open implication; the missing summand
  relation is proved here outright), one suggested and four notes.
created: 2026-09-28T19:25:20Z
updated: 2026-09-28T19:25:20Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, given only the
commissioning assignment. The reviewer took no part in writing the page or
any page of the folder, had no contact with the authors or with other
reviewers, and had not read the page before the assignment. Charge:
refutation.

**Subject.** Path `wiki/research/erdos_1219/connections.md` as it stood at
2026-09-28T13:50:48Z, section "## Problem 1167: the negative stepping-up lemma",
lines 511--540 (the H2 at line 511; the next H2, "Other relations in the
set-theory folder", at line 542). Lead pages: none are named; the section's
Outcome records no lead.

**Read, as of that time.** The section in full. The page's preamble (Scope and
notation, lines 1--37) and its Tools section (T1--T3, lines 39--108) as
inputs, interfaces only; their proofs belong to another reviewer. The
reconstruction pages `theorem_1_2_reconstruction.md` and
`corollary_1_3_reconstruction.md` in full and the Statement section of
`lemma_1_1_reconstruction.md`, as premises. The Statement of
`wiki/problems/set_theory/E1167/_index.md` (lines 1--42, before its first H2) and
of `wiki/problems/set_theory/E1218/_index.md` (lines 1--37). The Statement section
of the result page `corollary_1_3.md` and the result page `conjecture_1a.md`
under the Shelah 1975 card; the provenance paragraphs of the Shelah 1975 and
Komjáth 2025 cards; Komjáth p. 419 (PDF p. 2) by text extraction and on the
page image, including a 300 dpi crop of Problem 2; Shelah p. 1261 (PDF p. 5)
on the page image. `docs/verification.md` "Grading and claim standing",
"Audit checklist" (general and Erdos-specific) and "Whole-claim report";
`docs/approach_vetting.md`; `docs/evidence.md` "Source fidelity";
`docs/math_authoring.md`.

**Not read.** The catalog pages (web excluded); EHMR84 (not held); the
folder's `_index.md`; the Problem 1218 section and every other target section
of the page; every existing review and grade; every Current assessment, Known
results and standing text of the problem pages.

**Exposures.** (1) `conjecture_1a.md` was printed whole, so its Standing
paragraph (three sentences: a conjecture as posed; Komjáth records it
unproven; no later resolution found in the search on the Problem 1219 page),
its Proof pointer (naming a lead page on triple canonization) and its Bears
on list were seen; nothing from them is used. (2) The Komjáth card's digest
paragraph beyond its provenance (about other catalog problems) and the
Shelah card's generated link rows were seen. (3) A listing of the H2 headings
of `E1167.md` and `E1218.md` showed the heading names "Current assessment",
"Progress" and "Known Results" with no text. (4) A file listing of the folder
showed the names of three review files and a grade file under
`evidence/verify/`; none was opened. (5) Lines 639--660 of
`docs/verification.md` (the head of "Durable reports and current standing")
were seen. (6) The Statement of `E1218.md` was read although the section's
target is Problem 1167; it was needed for S7.

## Restatement

Notation as on the page: $\theta\to(\mu_0,\ldots)^r$ for cardinals,
$(\rho)_\gamma$ for $\gamma$ repetitions, $\chi=\sum_{\mu<\lambda}2^\mu$,
and for $\lambda=\aleph_\omega$, $\chi=\sum_{n<\omega}2^{\aleph_n}$.

- **S1** (target). Problem 1167 asks: for finite $r\ge2$, infinite
  $\lambda$, an index ordinal $\gamma$ and cardinals $\kappa_\alpha$
  ($\alpha<\gamma$), does $2^\lambda\to(\kappa_\alpha+1)^{r+1}_{\alpha<\gamma}$
  imply $\lambda\to(\kappa_\alpha)^r_{\alpha<\gamma}$, with $+$ cardinal
  addition, so $\kappa_\alpha+1=\kappa_\alpha$ for infinite $\kappa_\alpha$?
  Attached: (S1a) the catalog page lists the proved cases from EHMR84 and
  names "$r=2$ with one singular $\kappa_\alpha$ and the others finite" as
  the difficult case; (S1b) Komjáth prints the problem as Problem 2 on
  p. 419 with the same case list; (S1c) the problem's status is open and no
  assessment is compiled.
- **S2** (obstruction). Nothing transfers: Theorem 1.2, (T2) and (T3) each
  conclude a relation of exponent 2 (Theorem 1.2: $\chi\to(\lambda)^2_2$
  from $\kappa\to(\kappa)^2_2$ at $\kappa=\operatorname{cf}\lambda$ and the
  block relations $(2^\mu)^+\to((2^\mu)^+,\mu^+)^2$; (T2):
  $\lambda\not\to(\lambda,(\rho_\nu)_{\nu<\gamma})^2$ from the same relation
  at $\kappa$; (T3): $\chi\not\to(\lambda)^2_2$ from
  $\kappa\not\to(\kappa)^2_2$), whereas Problem 1167 relates exponent $r$ on
  $\lambda$ to exponent $r+1$ on $2^\lambda$.
- **S3.** For every $n<\omega$, $\aleph_n\not\to(\aleph_\omega,3)^2$, and
  trivially so.
- **S4** (conditional). For every $n<\omega$: if the implication of
  Problem 1167 holds at $\lambda=\aleph_n$, $r=2$, $\gamma=2$,
  $\kappa_0=\aleph_\omega$, $\kappa_1=3$, then
  $2^{\aleph_n}\not\to(\aleph_\omega,4)^3$.
- **S5.** Conjecture 1A asserts $\chi\to(\aleph_\omega,4)^3$, under its
  hypothesis $\aleph_\omega<2^{\aleph_{n(0)}}<2^{\aleph_{n(1)}}<\cdots$ for
  some sequence $n(k)$; the relations $2^{\aleph_n}\not\to(\aleph_\omega,4)^3$
  for all $n$ and the conjecture are compatible, in the way Sierpiński's
  $2^{\aleph_n}\not\to(\aleph_{n+1})^2_2$ is compatible with the corollary's
  $\chi\to(\aleph_\omega)^2_2$.
- **S6.** A proof of Conjecture 1A would show that $\chi$ behaves differently
  from each summand $2^{\aleph_n}$ at exponent 3, as it does at exponent 2:
  a positive relation at $\chi$ against negative ones at every summand.
- **S7.** Problem 1218 is the instance of the difficult case of S1a that is
  itself a catalog problem, as the previous section records.
- **S8.** Outcome: not applicable; no lead. Not a claim.

## Checklist

- **Quantifiers and scope.** S3 and S4 are stated for every $n<\omega$ and
  hold instance by instance. S5 carries the conjecture's chain hypothesis
  implicitly through the name "Conjecture 1A"; that hypothesis is what makes
  the compatibility true (W2), so it is silently load-bearing (F5, note). S6
  as supported in the text depends on the implication of S4 as well as on
  the conjecture, and names only the conjecture (F1, required). Pass with
  those findings.
- **Circularity.** None. The section derives nothing from Problem 1167 and
  uses it only as a hypothesis in S4. Pass.
- **Model and convention changes.** The cardinal-addition convention is the
  problem page's and Komjáth's ($1+4=5$, $1+\aleph_0=\aleph_0$), and S4 uses
  it correctly ($\aleph_\omega+1=\aleph_\omega$, $3+1=4$). Komjáth prints the
  contrapositive form with side conditions ($\gamma\le2$ as printed,
  $\kappa_\nu>r$) that the catalog form lacks; S4's instance satisfies both,
  so no conclusion changes (F3, note). Pass.
- **Finite and statistical overreach.** Not applicable: no finite
  verification or heuristic is used.
- **Uniformity.** Not applicable beyond "for every $n$", which is checked
  instance by instance with no constant depending on $n$.
- **Extremal conclusions.** Not applicable: no infimum, supremum or
  sharpness is asserted.
- **Consequences and composition.** S4's "so" is a correct contrapositive of
  the problem's implication at the named parameters. S6's "would show"
  composes the conjecture with the summand relations; as written, the
  summand relations are supplied only by the open implication, so the
  composition inherits that unproved premise (F1). The premise is
  discharged by Lemma B below, which the section does not cite. S2's "and"
  lists the three tools correctly. Pass with F1.
- **Computation.** Not applicable: none.
- **Reproduction.** Not applicable: no rerun line or coverage claim.
- **Source and verdict fidelity.** S1 matches the Statement of E1167 word
  for word in substance. Conjecture 1A and its Remark match Shelah p. 1261.
  Corollary 1.3 and Sierpiński's relation match the reconstruction pages.
  Komjáth p. 419 prints Problem 2 and the case list (a)--(e), in the
  contrapositive form with side conditions (F3). The catalog-page
  attributions in S1a (the case list, the phrase "difficult case", the edit
  date) and S1c's "no compiled assessment" could not be checked in this read
  set (F6). Pass with those notes.

## Weakest steps

**W1. The instance of S3 and S4, and what its conclusion is.** The
contrapositive of the problem's implication reads: if
$\lambda\not\to(\kappa_\alpha)^r_{\alpha<\gamma}$ then
$2^\lambda\not\to(\kappa_\alpha+1)^{r+1}_{\alpha<\gamma}$. At
$\lambda=\aleph_n$,
$r=2$, $\gamma=2$, $\kappa_0=\aleph_\omega$, $\kappa_1=3$ the hypothesis is
witnessed by the constant coloring $F\equiv0$ of $[\aleph_n]^2$: a color-0
homogeneous set would have $\aleph_\omega>\aleph_n$ elements, and a color-1
homogeneous set of size $3$ would need a pair of color 1. This is S3. The
conclusion is $2^{\aleph_n}\not\to(\aleph_\omega+1,3+1)^3$, which under the
cardinal-addition convention is $2^{\aleph_n}\not\to(\aleph_\omega,4)^3$. This
is S4, and it is a valid deduction. The instance lies inside the case named
in S1a ($r=2$, $\kappa_0$ singular, $\kappa_1$ finite) and outside every
printed proved case (a)--(e) of Komjáth p. 419: (a) needs all targets
finite, (b) needs $\kappa_1$ infinite, (c)--(e) need $r\ge3$.

The conclusion, however, is a theorem of ZFC, so the instance is a settled
instance of the implication. The argument, re-derived here, is the following
three steps; no source for it was consulted, and the argument is elementary.

*Lemma A.* Let $\kappa$ be an infinite cardinal. The lexicographic order of
${}^\kappa2$ has no strictly increasing and no strictly decreasing sequence
of length $\kappa^+$.

*Proof.* Let $\eta\le\kappa$ be the least ordinal such that ${}^\eta2$
carries a strictly increasing sequence
$\langle x_\alpha:\alpha<\kappa^+\rangle$;
$\eta\ge1$ because ${}^02$ is a singleton. For each $\alpha$ let
$\delta_\alpha<\eta$ be the least coordinate at which $x_\alpha$ and
$x_{\alpha+1}$ differ, so $x_\alpha(\delta_\alpha)=0$ and
$x_{\alpha+1}(\delta_\alpha)=1$. Since $|\eta|\le\kappa<\kappa^+$ and
$\kappa^+$ is regular, there are $\delta<\eta$ and $S\subseteq\kappa^+$ with
$|S|=\kappa^+$ and $\delta_\alpha=\delta$ for all $\alpha\in S$. Restriction
to $\delta$ is weakly order-preserving: if
$x\restriction\delta>y\restriction\delta$
then $x>y$. For $\alpha<\alpha'$ in $S$ the restrictions
$x_\alpha\restriction\delta$ and $x_{\alpha'}\restriction\delta$ differ:
otherwise $x_{\alpha+1}$ and $x_{\alpha'}$ share the restriction $t$, with
$x_{\alpha+1}(\delta)=1$ and $x_{\alpha'}(\delta)=0$, so
$x_{\alpha'}<x_{\alpha+1}$ although $\alpha+1\le\alpha'$. Hence
$\langle x_\alpha\restriction\delta:\alpha\in S\rangle$ is strictly increasing
of length $\kappa^+$ in ${}^\delta2$ with $\delta<\eta$, against the choice
of $\eta$. Decreasing sequences: exchange the values $0$ and $1$. $\square$

*Lemma B.* $2^\kappa\not\to(\kappa^+,4)^3$ for every infinite cardinal
$\kappa$.

*Proof.* Let $X={}^\kappa2$ with its lexicographic order $<$ and a
well-order $\prec$ of $X$. For $x<y<z$ in $X$ put $g(\{x,y,z\})=1$ if
$y\prec x$ and $y\prec z$, and $g(\{x,y,z\})=0$ otherwise. No four-element
set is homogeneous in color 1: if $a<b<c<d$ had all triples of color 1, the
triple $\{a,b,c\}$ would give $b\prec c$ and the triple $\{b,c,d\}$ would
give $c\prec b$. No set of size $\kappa^+$ is homogeneous in color 0: let
$H\subseteq X$ with $|H|=\kappa^+$ and let $I$ be the set of $h\in H$ with at
most $\kappa$ elements of $H$ below $h$, an initial segment of $H$. If
$|I|=\kappa^+$, every proper initial segment of $I$ has size at most
$\kappa$, so $I$ has no largest element and no cofinal subset of size at
most $\kappa$, since such a subset would cover $I$ by at most $\kappa$ sets
of size at most $\kappa$; choosing $y_\alpha\in I$ above every $y_\beta$
($\beta<\alpha$) for $\alpha<\kappa^+$ gives a strictly increasing sequence
of length $\kappa^+$, against Lemma A. So $|I|\le\kappa$, and symmetrically
the set $J$ of $h\in H$ with at most $\kappa$ elements of $H$ above $h$ has
$|J|\le\kappa$. Let $H'=H\setminus(I\cup J)$, of size $\kappa^+$, and let $y$
be the $\prec$-least element of $H'$. Since $y\notin I$, $\kappa^+$ elements
of $H$ lie below $y$, so some $x\in H'$ has $x<y$; likewise some $z\in H'$
has $z>y$. Then $y\prec x$ and $y\prec z$, so $g(\{x,y,z\})=1$ and $H$ is not
homogeneous in color 0. $\square$

*Corollary C.* For every $n<\omega$, $2^{\aleph_n}\not\to(\aleph_\omega,4)^3$:
the coloring of Lemma B for $\kappa=\aleph_n$ has no color-0 homogeneous
set of size $\aleph_{n+1}$, hence none of size $\aleph_\omega$, and no
color-1 homogeneous four-element set.

*Observation D.* More generally, for $r=2$, finite $\gamma\ge2$ and finite
$\kappa_\alpha\ge3$ for $1\le\alpha<\gamma$, the implication of Problem 1167
holds in ZFC for every cardinal $\kappa_0$, singular or not. If
$\kappa_0\le\lambda$, the consequent holds: (EDM) gives
$\lambda\to(\lambda,\omega)^2$ for the two-coloring that merges the colors
$1,\ldots,\gamma-1$, and Ramsey's theorem for finitely many colors, obtained
by iterating (R), splits an infinite homogeneous set of the merged color
into a homogeneous set of size $\kappa_\alpha$ in one original color. If
$\kappa_0>\lambda$, then $\kappa_0\ge\lambda^+$ and the antecedent fails:
the coloring of Lemma B, read as a $\gamma$-coloring in which the colors
$2,\ldots$ are unused, has no color-0 homogeneous set of size $\kappa_0$, no
color-1 homogeneous set of size $1+\kappa_1\ge4$, and no homogeneous set of
size $1+\kappa_\alpha\ge4$ in an unused color, because such a set contains a
triple. Hence the open instances of the case named in S1a have infinitely
many colors, as Problem 1218 has; the section's instance is not one of
them.

**W2. Compatibility (S5).** Under the conjecture's hypothesis the powers
$2^{\aleph_{n(k)}}$ are strictly increasing and cofinal among the
$2^{\aleph_n}$ (the corollary page shows $n(k)$ is strictly increasing), so
$\chi=\sup_n2^{\aleph_n}$ exceeds every $2^{\aleph_m}$. A negative relation
at each $2^{\aleph_n}$ and a positive relation at the larger cardinal $\chi$
contradict nothing: a positive relation passes upward and a negative one
downward in the left cardinal, and no rule passes either across the gap. So
S5 holds. The same reason makes the exponent-2 analogy exact: Sierpiński's
$2^{\aleph_n}\not\to(\aleph_{n+1})^2_2$ gives
$2^{\aleph_n}\not\to(\aleph_\omega)^2_2$,
and Corollary 1.3 gives $\chi\to(\aleph_\omega)^2_2$ under the same chain
hypothesis. Without the chain hypothesis the powers may be eventually
constant, $\chi$ then equals $2^{\aleph_m}$ for large $m$, and the two
relations would contradict each other; the conjecture asserts nothing in
that case, so the compatibility rests on its hypothesis (F5).

**W3. The obstruction (S2).** Theorem 1.2, (T2) and (T3) are read at their
interfaces on the page: each is a statement about pairs, so none produces a
relation of exponent 3 or relates $\lambda$ to $2^\lambda$; the exponent
argument is correct. A stronger reason is available and was used in the
attack on S2: under the non-constancy hypothesis of Theorem 1.2 and (T3),
$\chi=\sup_{i<\kappa}2^{\mu(i)}$ over strictly increasing powers, so
$\operatorname{cf}\chi=\kappa$; if $\chi=2^\nu$ for an infinite $\nu$ then
$\nu<\kappa$ because $\operatorname{cf}2^\nu>\nu$, so
$2^\nu\le2^\kappa\le\chi=2^\nu$ (the
preliminary of the theorem page gives $\kappa<\lambda$, so $2^\kappa$ is a
summand of $\chi$), whence
$\operatorname{cf}\chi=\operatorname{cf}2^\kappa>\kappa$,
a contradiction. So $\chi$ is never the right-hand cardinal $2^\lambda$ of
the stepping-up, and the mechanism's positive relations can neither test
nor refute an instance of Problem 1167. (T2)'s negative relations live on a
singular $\lambda$, which may equal a power $2^{\lambda'}$; but they have
exponent 2, which is the stepping-up conclusion only for $r=1$, excluded by
$r\ge2$.

## Strongest attack

- **S1.** Fidelity attack against E1167 and Komjáth p. 419. The restatement
  matches E1167. Komjáth prints the contrapositive with the side conditions
  $\gamma\le2$ (as printed) and $\kappa_\nu>r$; the section's "prints it"
  glosses this (F3). The attack also found that the catalog form without
  $\kappa_\alpha>r$ fails at degenerate parameters (F4); this concerns the
  problem page, not the section's instances. S1a and S1c could not be
  attacked (F6). Refutation of S1 failed.
- **S2.** Attempted to route a conclusion of the mechanism onto a cardinal
  of the form $2^{\lambda'}$, so that Theorem 1.2 or a proof of
  Conjecture 1A would refute an instance of Problem 1167 whose hypothesis
  holds. The attack fails by W3. Attempted to use (T2) on a singular
  $2^{\lambda'}$; the shape matches only $r=1$. Refutation failed.
- **S3.** No attack is available; the constant coloring is a witness.
- **S4.** Checked the parameters against both forms of the problem: cardinal
  addition, $\kappa_\nu>r$, $\gamma=2$. The contrapositive is exact. The
  attack "the conclusion could fail, refuting the implication at this
  instance" fails because the conclusion is Corollary C. Refutation of the
  conditional failed; the conditional is, however, vacuous as a test of the
  open problem (F1, F2).
- **S5.** Attempted to force $\chi=2^{\aleph_m}$ by eventually constant
  powers; excluded by the conjecture's hypothesis (W2). Refutation failed.
- **S6.** The attack succeeded against the support the text gives and
  failed against the statement: as written, the negative summand relations
  come only from the open implication, so the sentence's stated hypothesis
  (a proof of the conjecture) is not the whole of what the text uses;
  Corollary C supplies the summand relations outright, after which the
  sentence is correct with the conjecture as its only hypothesis (F1).
- **S7.** Checked that Problem 1218 is Komjáth's Problem 1 and can be written
  as an instance of the case in S1a: with $\mu=\aleph_{\omega_{\omega+1}}$,
  singular of cofinality $\aleph_{\omega+1}$ (the index $\omega_{\omega+1}$ is
  a regular limit ordinal), GCH gives
  $2^\mu=\mu^+=\aleph_{\omega_{\omega+1}+1}$,
  the cardinal of Problem 1218; at $\lambda=\mu$, $r=2$, $\gamma=\omega$,
  $\kappa_0=\mu$ and $\kappa_m=3$ for $m\ge1$, the contrapositive reads:
  $\mu\not\to(\mu,(3)_{\aleph_0})^2$ implies
  $\mu^+\not\to(\mu,(4)_{\aleph_0})^3$, and the latter implies the relation
  Problem 1218 asks, since a color-0 homogeneous set of size $\mu^+$
  contains one of size $\mu$. The instance's hypothesis reduces by (T2) to
  $\aleph_{\omega+1}\not\to(\aleph_{\omega+1},(3)_{\aleph_0})^2$ under GCH, a
  relation outside this read set and not examined. The reading with
  $\kappa_0=\mu^+$ instead matches Problem 1218's relation directly but has
  a regular $\kappa_0$ and so is not the case of S1a. Uniqueness among
  catalog problems and the content of "the previous section" were not
  checkable (F5, F6). Refutation of the placement failed.

## Premises

- **Theorem 1.2** (`theorem_1_2_reconstruction.md`, read in full).
  Interface: $\lambda$ infinite, $\kappa=\operatorname{cf}\lambda$,
  $\kappa\to(\kappa)^2_2$, $\langle2^\mu:\mu<\lambda\rangle$ not eventually
  constant but eventually $\ge\lambda$; conclusion $\chi\to(\lambda)^2_2$
  and $\chi\to(\lambda,\lambda,\omega)^2$. Its imports as stated there and
  used here: (ER) $(2^\mu)^+\to((2^\mu)^+,\mu^+)^2$; (S) Sierpiński,
  $2^\mu\not\to(\mu^+)^2_2$; (EDM) $\theta\to(\theta,\omega)^2$ for every
  infinite $\theta$; all three not held. Its preliminary $\kappa<\lambda$ is
  used in W3. Standing as the folder records: reviewed as of
  2026-09-28T05:03:27Z with corrections since; taken as established here.
- **Corollary 1.3** (`corollary_1_3_reconstruction.md`, read in full).
  Interface: $\aleph_\omega<2^{\aleph_{n(0)}}<2^{\aleph_{n(1)}}<\cdots$;
  conclusion $\sum_{n<\omega}2^{\aleph_n}\to(\aleph_\omega)^2_2$; the
  identification $\chi=\sum_{n<\omega}2^{\aleph_n}=\sup_n2^{\aleph_n}$ and
  the forced strict increase of $n(k)$. Import (R) Ramsey's theorem
  $\omega\to(\omega)^2_2$, not held; used in Observation D for finitely many
  colors by iteration.
- **Lemma 1.1** (`lemma_1_1_reconstruction.md`, Statement section only).
  Interface: canonization of finitely many finite-place functions on blocks;
  used only to confirm that the mechanism's exponent generality lies in the
  lemma, not in the three tools the section names.
- **Tools T1--T3** (the page's Tools section, lines 39--108). Interfaces as
  restated in S2; the proofs of (T2) and (T3) were read for their statements
  and hypotheses only. (T2) is used in the S7 check as a reduction to the
  cofinality.
- **Conjecture 1A** (`conjecture_1a.md`, and Shelah p. 1261 on the page
  image). Statement: if
  $\aleph_\omega<2^{\aleph_{n(0)}}<2^{\aleph_{n(1)}}<\cdots$
  then $\sum_{n<\omega}2^{\aleph_n}\to(\aleph_\omega,4)^3$; the Remark adds
  $\sum_{n<\omega}2^{\aleph_n}\not\to(\aleph_\omega,5)^3$ without proof.
  Held scan, read clause by clause on the image. A conjecture, not a
  result.
- **Komjáth 2025, p. 419** (held PDF, text extraction and page image, with a
  300 dpi crop of Problem 2). Problem 1 (GCH):
  $\lambda\not\to(\kappa_n:n<\omega)^3$ with
  $\lambda=\kappa_0=\aleph_{\omega_{\omega+1}+1}$ and $\kappa_m=4$ for $m>0$.
  Problem 2: assume $2\le r<\omega$, $\lambda$ infinite, $\gamma\le2$ (as
  printed), cardinals $\kappa_\nu>r$ ($\nu<\gamma$) and
  $\lambda\not\to(\kappa_\nu)^r_\gamma$; does
  $2^\lambda\not\to(1+\kappa_\nu)^{r+1}_\gamma$
  hold? Addition is cardinal addition. The cases reported proved in EHMR84
  Section 24: (a) all $\kappa_\nu$ finite; (b) $\kappa_0,\kappa_1$ infinite,
  $\kappa_0$ regular; (c) $r\ge3$, $\kappa_0$ infinite regular; (d) $r\ge3$,
  $\kappa_0,\kappa_1$ infinite; (e) $r\ge4$, $\kappa_0$ infinite. The page
  also records Problem 3 as proved by Shelah and Hajnal's conjecture as
  unproven, and the necessity remark under Problem 4.
- **E1167, Statement.** As restated in S1; the page states cardinal
  addition explicitly and no side condition on $\gamma$ or $\kappa_\alpha$.
- **E1218, Statement.** Assume GCH and $\lambda=\aleph_{\omega_{\omega+1}+1}$;
  is $\lambda\not\to(\lambda,4,4,\ldots)^3$ with countably infinitely many
  fours?
- **Lemma A and Lemma B** above are the reviewer's own derivations from
  first principles, with no external premise beyond ZFC.

## Findings

**F1** (required). Location, lines 529--536: "so the implication asked would
give $2^{\aleph_n}\not\to(\aleph_\omega,4)^3$ for every $n$, while
Conjecture 1A asserts the positive relation for the sum $\chi$ of these
powers; the two are compatible, ..., and a proof of the conjecture would show
that the sum of the powers behaves differently from each summand at
exponent $3$ as well." Defect: the closing clause is a conditional
conclusion whose stated hypothesis is a proof of the conjecture, but the
negative summand relations it needs are supplied in the text only as what
"the implication asked would give", so as written the clause also depends
on the open implication and does not say so. Witness: the text's own
derivation chain; nothing in the section establishes
$2^{\aleph_n}\not\to(\aleph_\omega,4)^3$ unconditionally. Repair: the
summand relation holds outright by Corollary C (Lemma B with
$\kappa=\aleph_n$), so replace "the implication asked would give
$2^{\aleph_n}\not\to(\aleph_\omega,4)^3$ for every $n$" by a sentence stating
that $2^{\aleph_n}\not\to(\aleph_\omega,4)^3$ holds for every $n$, from
$2^{\aleph_n}\not\to(\aleph_{n+1},4)^3$ (the lexicographic order of
${}^{\aleph_n}2$ with a well-order, a triple colored by whether its middle
element is the well-order-least of the three; or a citation), so that this
instance of the implication is settled; then the closing clause stands with
the conjecture as its only hypothesis. The statement of S6 itself is not
refuted.

**F2** (suggested). Location, lines 527--530: "Theorem 1.2 and Hajnal's
conjecture sit next to the difficult case: for $\lambda=\aleph_n$ the
relation $\aleph_n\not\to(\aleph_\omega,3)^2$ is trivial, so the implication
asked would give ...". Defect: the instance chosen to locate the mechanism
is a settled instance, and by Observation D every instance of the named
case with finitely many colors is settled by (EDM), Ramsey's theorem and
Lemma B, whatever $\kappa_0$ is; the open part of the case has infinitely
many colors. Proposed replacement: say that the two-color instances of the
case are settled (Observation D), that the open instances need infinitely
many finite targets, and that this is why the catalog instance is
Problem 1218 with its $\aleph_0$ fours, which the second remark already
records.

**F3** (note). Location, lines 519--520: "Komjáth prints it as Problem 2 with
the same case list (p. 419)". Komjáth prints the contrapositive form with
the side conditions "$\gamma\le2$" (so printed; read on a 300 dpi crop) and
"$\kappa_\nu>r$", neither of which the catalog form carries. Read literally,
$\gamma\le2$ confines Problem 2 to at most two colors, so Problem 1218
(countably many colors) is an instance of the catalog form but not of the
printed Problem 2; and (b) of the case list reads naturally for two colors.
Whether the catalog's case list is "the same" could not be checked. A
clause saying "prints the contrapositive, with the side conditions
$\kappa_\nu>r$ and, as printed, $\gamma\le2$" would be exact.

**F4** (note, outside the section's own claims). The catalog form restated
in S1, without Komjáth's side condition $\kappa_\alpha>r$, is false at
degenerate parameters: with $r=2$, $\gamma=2$, $\lambda=\aleph_0$,
$\kappa_0=\aleph_1$, $\kappa_1=2$, the antecedent
$2^{\aleph_0}\to(\aleph_1,3)^3$
holds (a coloring either gives some triple the color 1, a homogeneous
three-element set, or is constantly 0, and then any set of size $\aleph_1$
is homogeneous), while the consequent $\aleph_0\to(\aleph_1,2)^2$ fails for
the constant coloring 0. In general $\kappa_1=r$ with
$\lambda<\kappa_0\le2^\lambda$
gives the failure. The section's instances have $\kappa_\alpha\ge3>r$, so
nothing in the section is affected; the problem page's formulation is.

**F5** (note). Location, line 532: "the two are compatible". The
compatibility rests on the conjecture's chain hypothesis, under which
$\chi$ exceeds every $2^{\aleph_n}$ (W2); with eventually constant powers the
two relations would contradict each other and the conjecture would assert
nothing. One clause naming the reason would make the remark
self-contained. Likewise lines 536--537, "the instance of the difficult case
that is itself a catalog problem is Problem 1218": the instance reading is
verified (S7), but its hypothesis rests on
$\aleph_{\omega+1}\not\to(\aleph_{\omega+1},(3)_{\aleph_0})^2$ under GCH via
(T2), and uniqueness among catalog problems was not checkable here.

**F6** (note). Lines 513--519: "(status `open`, no compiled assessment)" and
the catalog-page attributions (the proved-case list, the phrase naming the
difficult case, "last edited 1 September 2026"). The status is confirmed by
the page's frontmatter; the rest could not be checked, since the catalog is
excluded from this read set and Current assessment text is excluded, while
the problem page does carry a heading of that name. No defect is asserted.

## Verdict

- **S1**: refutation-failed as a restatement of the problem page, with the
  fidelity notes F3 and F4; S1a and S1c not checkable here (F6).
- **S2**: refutation-failed; the obstruction holds, and a stronger reason is
  recorded in W3.
- **S3**: refutation-failed.
- **S4**: refutation-failed as a conditional; its conclusion is a theorem
  (Corollary C), so the conditional does not test the open problem (F1,
  F2).
- **S5**: refutation-failed; the compatibility rests on the conjecture's
  chain hypothesis (F5).
- **S6**: refutation-failed for the statement; the support the text gives
  it is incomplete as written and is repaired by Corollary C (F1,
  required).
- **S7**: refutation-failed for the instance placement, with the limits in
  F5.
- **S8**: not a claim.

**Limitations.** The catalog pages, EHMR84 and the Problem 1218 section were
outside the read set, so S1a, S1c, the "same case list" and "as the previous
section records" are unverified. Whether Lemma B appears in the literature
was not checked; it is an elementary argument retained here in full. The
relation $\aleph_{\omega+1}\not\to(\aleph_{\omega+1},(3)_{\aleph_0})^2$ under
GCH, on which the Problem 1218 instance's hypothesis rests, was not
examined.

This focused review assigns no tier and changes no status.
