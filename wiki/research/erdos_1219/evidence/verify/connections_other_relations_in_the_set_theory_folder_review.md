---
name: research/erdos_1219/evidence/verify/connections_other_relations_in_the_set_theory_folder_review
title: "Independent review of the connections section: Other relations in the set-theory folder"
desc: |
  Refutation-failed for all seven statements of the section (S1 to S7): no
  non-applicability claim fell. One required correction (the reason recorded
  for Problem 70 is false as written), one suggested rewording and four
  notes.
created: 2026-09-28T19:14:34Z
updated: 2026-09-28T20:42:32Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation. The reviewer took no part in writing the page or the folder's
reconstructions, had no contact with their authors, and read no earlier
review or grade of any page in the folder.

**Subject.** [[research/erdos_1219/connections|The connections page]]
(`wiki/research/erdos_1219/connections.md`) as it stood at
2026-09-28T13:50:48Z, section "## Other relations in the set-theory folder",
lines 542--567: the heading at line 542 and one paragraph at lines 544--567; the
next heading, "## Outcomes", is at line 569. No lead page is named for this
section.

**Reading, at full depth unless stated.** The section. The page's Scope
paragraph and its Tools section, (T1), (T2) and (T3), as inputs whose
interfaces were confirmed at each use and whose proofs were not reviewed.
The three reconstruction pages of the folder,
[[research/erdos_1219/lemma_1_1_reconstruction|Lemma 1.1]],
[[research/erdos_1219/theorem_1_2_reconstruction|Theorem 1.2]] and
[[research/erdos_1219/corollary_1_3_reconstruction|Corollary 1.3]], in
full, as premises at the standing of their review as of 2026-09-28T05:03:27Z.
The Statement paragraph, and nothing else, of the problem pages
[[problems/set_theory/E1168/_index|E1168]], [[problems/set_theory/E0070/_index|E0070]],
[[problems/set_theory/E1170/_index|E1170]], [[problems/set_theory/E1172/_index|E1172]],
[[problems/set_theory/E0598/_index|E0598]], [[problems/set_theory/E0623/_index|E0623]],
[[problems/set_theory/E1173/_index|E1173]], [[problems/set_theory/E1219/_index|E1219]],
[[problems/set_theory/E1218/_index|E1218]] and
[[problems/set_theory/E1167/_index|E1167]]. The provenance paragraph of
[[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|the Komjáth 2025 card]].
The sections "Whole-claim report", "Audit checklist" (both the general and
the Erdos-specific list) and "Grading and claim standing" of
`docs/verification.md`, "Source fidelity" of `docs/evidence.md`, and the
whole of `docs/approach_vetting.md` and `docs/math_authoring.md`. No held
PDF was opened: the section invokes no source theorem directly, and the one
source relation used in this report, (ER), is taken from the theorem page
at its recorded standing.

**Exposures.** Five reads went past the commissioned set; none is an
excluded review, grade, index, assessment or web source.

1. The page's "## Outcomes" section (lines 569--591) was read during the
   first scan of the page.
2. The Problem 1218 section (lines 446--510) was read in full, to locate
   and confirm the GCH remark the section cites (lines 486--505), rather
   than the remark alone.
3. The Problem 501 connections page was read at lines 480--600 (its
   Problem 623 and Problem 1173 sections, which contain that page's own
   standing sentence for the results it cites and a model-theoretic
   argument) and at lines 713--735, to confirm the citation "their
   obstructions are on the Problem 501 connections page".
4. The Problem 1171 connections page was read at lines 658--676, its own
   section "Other relations in the set-theory folder", to confirm the
   citation about Problem 1219.
5. A heading-only listing of `E1168.md` showed the names of its later
   sections (Current assessment, Progress, Known Results, Linked library
   material) with none of their content.

## Restatement

Throughout, *the mechanism* is the route of the reconstruction pages:
Lemma 1.1 through the interface (T1), and Theorem 1.2's reduction of a
coloring of pairs on $\chi=\sum_{\mu<\lambda}2^\mu$ to a coloring of pairs
on $\kappa=\operatorname{cf}\lambda$; (T2) and (T3) are the page's
compositions built on the same block decompositions. A block decomposition
of a set $X$ is, by the page's Scope paragraph, a partition of $X$ into
$\kappa$ pieces.

- **S1.** Every application of the mechanism has three features: a
  resource $A=\bigsqcup_{i<\kappa}A_i$ with $\kappa=\operatorname{cf}\lambda$,
  $|A_i|=\lambda_i=(2^{\mu(i)})^+$ regular and strictly increasing, and
  $\sup_i\lambda_i=|A|$; a coloring of pairs, triples entering only through
  the conditional route of the Conjecture 1A section with its gaps; and the
  positive relation $\kappa\to(\kappa)^2_2$ at the cofinality. Read as: each
  feature is consumed, so a problem lacking one lies outside the mechanism.
- **S2.** Problem 1168 asks for a proof in ZFC of
  $\aleph_{\omega+1}\not\to(\aleph_{\omega+1},(3)_{\aleph_0})^2$. The
  mechanism does not apply: the resource $\aleph_{\omega+1}$ is regular and
  the relation is negative. The page's only contact with the problem is the
  GCH remark of the Problem 1218 section, which applies (T2) with
  $\lambda=\aleph_\beta$ for $\beta=\omega_{\omega+1}$,
  $\kappa=\operatorname{cf}\aleph_\beta=\aleph_{\omega+1}$, $\gamma=\aleph_0$
  and $\rho_\nu=3$, and not with $\lambda=\aleph_{\omega+1}$.
- **S3.** Problem 70 asks whether $\mathfrak c\to(\beta,n)^3_2$ for every
  countable ordinal $\beta$ and every $n$ with $2\le n<\omega$, where
  $\mathfrak c$ is "the ordinal of the real numbers", read by the section as
  the order type of the reals. The mechanism does not apply; the reason
  recorded is that this order type has no block decomposition into regular
  cardinals.
- **S4.** Problem 1170 asks whether $\omega_2\to(\alpha)^2_2$ for every
  $\alpha<\omega_2$ is consistent. Problem 1172 asks, under GCH, whether
  $\omega_3\to(\omega_2,\omega_1+2)^2$,
  $\omega_3\to(\omega_2+\omega_1,\omega_2+\omega)^2$ and
  $\omega_2\to(\omega_1^{\omega+2}+2,\omega_1+2)^2$ hold, and whether
  $\omega_2\to(\omega_1+\omega)^2_2$, or $\omega_2\to(\xi)^2_2$ for all
  $\xi<\omega_2$, is consistent with GCH. The mechanism applies to none of
  these relations, described as balanced or ordinal-target relations on the
  regular cardinals $\omega_2$ and $\omega_3$.
- **S5.** Problem 598 asks, for an infinite cardinal $m$ and
  $\kappa=(2^{\aleph_0})^+$, whether the countable subsets of $m$ can be
  colored with $\kappa$ colors so that every $X\subseteq m$ with $|X|=\kappa$
  contains subsets of every color. The mechanism does not apply because the
  coloring is of countable subsets, not of finite tuples.
- **S6.** Problem 623: $|X|=\aleph_\omega$, $f:[X]^{<\omega}\to X$ with
  $f(A)\notin A$ for every finite $A$; is there an infinite $Y\subseteq X$
  with $f(B)\notin Y$ for every finite $B\subseteq Y$? Problem 1173: under
  GCH, $f:\omega_{\omega+1}\to[\omega_{\omega+1}]^{\le\aleph_\omega}$ with
  $|f(\alpha)\cap f(\beta)|<\aleph_\omega$ for $\alpha\ne\beta$; is there a
  free set of cardinality $\aleph_{\omega+1}$? The mechanism does not
  apply: a free set is not a homogeneous set, and no clause of Lemma 1.1
  produces one; the obstructions recorded for these problems are on the
  Problem 501 connections page.
- **S7.** The Problem 1171 connections page records that its color-merging
  induction does not apply to Problem 1219, a balanced cardinal relation;
  the mechanism reviewed here is what proves Problem 1219's relation
  (Corollary 1.3); and the two mechanisms have no consumed hypothesis in
  common.

## Checklist

- **Quantifiers and scope.** Pass, with one defect filed. Each
  non-applicability claim is scoped to the mechanism of S1, and every
  problem statement was compared with the section's description of it. The
  reason sentence for Problem 70 (S3) is false under the page's own
  definition of a block decomposition; the non-applicability it supports
  holds for the reason re-derived in W1 (F2).
- **Circularity.** Pass. No statement of the section is assumed in its own
  support; the citations run to the Problem 1218 section, the two other
  connections pages and the problem statements, none of which consumes this
  section.
- **Model and convention changes.** Pass. The section reads Problem 70's
  "ordinal of the real numbers" as the order type of the reals; under the
  other reading, the cardinal $2^{\aleph_0}$, the same floor blocks the
  mechanism (W1), so no conclusion depends on the reading. The
  characterization of (T2)'s use in the cited remark matches (T2)'s
  interface at $\lambda=\aleph_\beta$ (W2). No relaxed or transformed system
  is substituted anywhere.
- **Finite and statistical overreach.** Inapplicable: the section contains
  no finite verification and no statistics.
- **Uniformity.** Inapplicable: no constants, bounds or families with a
  parameter appear. The list in S1 is a list of features, each of which the
  reconstruction pages consume at a named step (Step 2, Steps 4--5, Step 7
  of the theorem page).
- **Extremal conclusions.** Inapplicable: no infimum, supremum, attained
  value or sharpness is asserted.
- **Consequences and composition.** Pass. Each "does not apply" was attacked
  separately (Strongest attack). The remark the section describes was
  checked against (T2)'s hypotheses. The comparison sentence in S7 is a
  comparison of the two pages' own lists of needs (F5, note). The sentence
  delegating obstructions to the Problem 501 page describes that page's
  obstructions to its own tools, not to this mechanism (F4, note).
- **Computation.** Inapplicable: no computation.
- **Reproduction.** Inapplicable: no rerun instruction or coverage claim.
- **Source and verdict fidelity.** Pass. The Problem 1171 page does say, in
  its own "Other relations" section, that its induction does not apply to
  "Problem 1219, a balanced cardinal relation". The Problem 501 page does
  carry Problem 623 and Problem 1173 sections recording obstructions. The
  Problem 1218 section's remark does apply (T2) at $\aleph_\beta$ with
  $\gamma=\aleph_0$ and $\rho_\nu=3$. Every problem is described in
  agreement with its Statement paragraph. No verdict of any review is
  quoted.

## Weakest steps

**W1. The size floor behind S3, S4 and every resource of the mechanism.**
(T1) passes to Lemma 1.1 the hypothesis $2^{\chi+\kappa}<\lambda_0$ with
the lemma's $\chi=2$ and $\kappa$ infinite regular, so
$\lambda_0>2^\kappa\ge2^{\aleph_0}$; since $|A_0|=\lambda_0\le|A|$, every
domain to which the lemma is applied has more than $2^{\aleph_0}$
elements. Independently, Theorem 1.2's resource satisfies
$\chi=\sup_i2^{\mu(i)}>2^{\mu(0)}\ge2^{\aleph_0}$ (Step 1: $\mu(0)$ is
infinite and the powers are strictly increasing; Step 2(d)), and
$\chi\ge\lambda\ge\aleph_\omega$ because $\lambda$ is singular by the
theorem page's preliminary paragraph. Both (T2) and (T3) need a singular
$\lambda$, hence $\lambda\ge\aleph_\omega$. Consequences: no set of size
$|\mathbb R|=2^{\aleph_0}$ is a domain of the lemma; no cardinal below
$\aleph_\omega$ is a resource of Theorem 1.2, (T2) or (T3). This is what
blocks Problem 70 and, with the regularity of $\omega_2$ and $\omega_3$,
Problems 1170 and 1172. The section's reason sentence for Problem 70 does
not state it (F2).

**W2. S2: no relation of the page lives at $\aleph_{\omega+1}$, and the
cited use of (T2).** Theorem 1.2 and (T3) have resource
$\chi=\sup_i2^{\mu(i)}$ with the powers strictly increasing along
$\kappa=\operatorname{cf}\lambda$, so $\chi$ is a limit cardinal of
cofinality $\kappa$; (T2) has a singular resource. A successor cardinal
such as $\aleph_{\omega+1}$ is neither, so no relation on the page has it
as resource, in either direction. The cited remark: (T2) requires
$\lambda$ singular, $\kappa=\operatorname{cf}\lambda$, $\gamma\ge1$,
$\rho_\nu\ge2$ and $\kappa\not\to(\kappa,(\rho_\nu)_{\nu<\gamma})^2$. At
$\lambda=\aleph_\beta$ with $\beta=\omega_{\omega+1}$: $\beta$ is a limit
ordinal, so $\operatorname{cf}\aleph_\beta=\operatorname{cf}\beta$, and
$\beta$ is a regular cardinal, so
$\operatorname{cf}\aleph_\beta=\omega_{\omega+1}=\aleph_{\omega+1}<\aleph_\beta$,
which makes $\aleph_\beta$ singular; $\gamma=\aleph_0$ and $\rho_\nu=3\ge2$;
the hypothesis $\aleph_{\omega+1}\not\to(\aleph_{\omega+1},(3)_{\aleph_0})^2$
is the GCH case of Problem 1168's relation, consumed as a premise. The
section's description of that use is exact, and it is a use of the
problem's relation, not a contribution to it (F1).

**W3. S6 at $\aleph_\omega$, the closest fit to S1.** The resource
$\aleph_\omega$ is a union of $\omega$ blocks of regular sizes $\aleph_n$,
$\operatorname{cf}\aleph_\omega=\omega$, and $\omega\to(\omega)^2_2$ holds;
Lemma 1.1 admits a family of $\aleph_0$ functions of unbounded finite
arity, $F_n(y_1,\ldots,y_n,y)=1$ exactly when $f(\{y_1,\ldots,y_n\})=y$,
and its counting hypotheses can hold for such a family (under GCH with
$\lambda_i=\aleph_{i+2}$ and $\mu(i)=\aleph_0$:
$2^{\aleph_0+\aleph_0}=\aleph_1<\aleph_2$ and
$\prod_{i<j}\aleph_{i+2}^{\aleph_0}=\aleph_{j+1}<\aleph_{j+2}$). So the
shape of S1 is available for Problem 623, and the non-applicability rests
entirely on the clause argument. Re-derived: (1A) and (1B) equate values of
an $F_n$ on tuples with one entry in $B_\alpha$, one in $B_\beta$
($\alpha<\beta$) and the rest in $\bigcup_{j<\alpha}B_j$; a free set needs
$F_n=0$ on every tuple of distinct elements of $Y$, including tuples with
two or more entries in one block, which no clause governs, and the
canonized value itself may be $1$. Clause (2) yields a property only
through (H), which for "$B_\alpha$ is free over $\bigcup_{i<\alpha}B_i$"
demands that every $C\subseteq A_\alpha$ of size $\lambda_\alpha$ contain
such a countable $B_\alpha$, the problem itself restricted to a block.
Nothing in the lemma's conclusion delivers freeness; the obstruction holds.
For Problem 1173 the resource $\omega_{\omega+1}$ is regular as well, so
the block shape of S1 fails there too, which the section does not say
(F4).

## Strongest attack

- **S1.** Attempted: exhibit a use of the mechanism lacking one of the
  three features, or a feature the list omits that would change a
  conclusion below. Each feature is consumed at a named step of the theorem
  page (the blocks and their sizes in Step 2 and Step 5, the pair coloring
  in Step 6, $\kappa\to(\kappa)^2_2$ in Step 7), so none can be dropped. The
  list omits (ER) at each block and the growth condition, but every
  conclusion of the section rests on grosser features (a regular or
  too-small resource, a wrong exponent or object, a negative direction),
  so the omission changes nothing. Failed.
- **S2.** Attempted: produce a relation at $\aleph_{\omega+1}$ from the
  page's tools. Theorem 1.2 and (T3) have a limit-cardinal resource, (T2)
  a singular one (W2); $\aleph_{\omega+1}$ is a successor. Attempted:
  read the cited remark as a use of (T2) at $\aleph_{\omega+1}$. It is a
  use at $\aleph_\beta$ with the $\aleph_{\omega+1}$ relation as
  hypothesis (W2). Failed; the wording is imprecise (F1).
- **S3.** Attempted: falsify the recorded reason. Under the page's
  definition of a block decomposition, the reals have one into regular
  cardinals: $\mathbb R=\bigsqcup_{x\in\mathbb R/\mathbb Q}(x+\mathbb Q)$ is
  a partition into countable pieces, and $\aleph_0$ is regular. So the
  reason as written is false. Attempted next: apply the mechanism to a
  set of size $2^{\aleph_0}$ anyway. Impossible by the floor of W1, in
  either reading of $\mathfrak c$; and (T2), (T3) give negative relations
  for pairs, which say nothing about a positive relation for triples with
  a countable-ordinal target. The non-applicability survives; the reason
  requires replacement (F2).
- **S4.** Attempted: apply the mechanism to $\omega_3$ under GCH, where
  $\omega_3=(2^{\aleph_1})^+$ is a single block of the shape $(2^\mu)^+$ of
  (ER). The block-to-cofinality reduction has one block and reduces to
  nothing; the resource is below $\aleph_\omega$ (W1). The mechanism does not
  apply. The attempt did show that the single-block input (ER) alone, at
  $\mu=\aleph_1$ under GCH, gives $\aleph_3\to(\aleph_3,\aleph_2)^2$, from
  which the first printed relation of Problem 1172 follows (F6, a note
  for the problem page, not a defect of the section). Attempted: the
  ordinal targets. The mechanism's homogeneous sets are controlled in
  cardinality only, and its resource never lies below $\aleph_\omega$.
  Failed.
- **S5.** Attempted: encode a coloring of $[m]^{\aleph_0}$ as functions of
  finitely many places. The lemma's $F_i$ have fixed finite arities $n_i$
  and the properties (1A), (1B) speak about finite patterns; a countable
  subset is no finite pattern, and the problem asks for a negative
  relation with $(2^{\aleph_0})^+$ colors, which no tool of the page
  produces on a regular or arbitrary $m$. Failed.
- **S6.** Attempted: the encoding of W3 at $\aleph_\omega$, which supplies
  the block shape. The clauses still give no free set (W3). For Problem
  1173 the resource is regular as well. Failed; two notes (F4).
- **S7.** Attempted: check the citation and the comparison. The Problem
  1171 page's sentence is as quoted; Corollary 1.3 does specialize the
  mechanism to Problem 1219's relation with the catalog's sum identified;
  the two pages' lists of needs share no item, though both consume
  two-place colorings, which "disjoint in what they consume" overstates
  (F5). Failed.

## Premises

- **Lemma 1.1** ([[research/erdos_1219/lemma_1_1_reconstruction|reconstruction]],
  read in full, reviewed as of 2026-09-28T05:03:27Z). Interface used: $\kappa$
  infinite regular; $\lambda_i$ regular, strictly increasing; the growth
  conditions $\prod_{i<j}\lambda_i^{\mu(i)}<\lambda_j$ and
  $2^{\chi+\kappa}<\lambda_0$; $F_i:A^{n_i}\to\chi$ with $1\le n_i<\omega$; the
  realizability hypothesis (H); conclusions (1A), (1B), (2), (3). Used in W1
  (the floor) and W3 (the clauses).
- **Theorem 1.2** ([[research/erdos_1219/theorem_1_2_reconstruction|reconstruction]],
  read in full, reviewed as of 2026-09-28T05:03:27Z). Interface used: $\lambda$
  with $\kappa=\operatorname{cf}\lambda$, $\kappa\to(\kappa)^2_2$, powers not
  eventually constant and eventually $\ge\lambda$; conclusion
  $\chi\to(\lambda)^2_2$; the preliminary $\kappa<\lambda$; Step 1
  ($\mu(0)\ge\kappa$, powers strictly increasing), Step 2 (blocks of sizes
  $(2^{\mu(i)})^+$, $\chi=\sup_i2^{\mu(i)}$), Steps 4--7. Imported there and
  used here only in F6: (ER), $(2^\mu)^+\to((2^\mu)^+,\mu^+)^2$ for infinite
  $\mu$, from Erdős, Hajnal and Rado (1965), not held, with the stronger
  form printed in the Komjáth survey's commentary on Problem 53.
- **Corollary 1.3** ([[research/erdos_1219/corollary_1_3_reconstruction|reconstruction]],
  read in full, reviewed as of 2026-09-28T05:03:27Z). Used for S7: the
  specialization to $\lambda=\aleph_\omega$ and the identification of the
  catalog's sum.
- **(T1), (T2), (T3)** of the page's Tools section, interfaces only, own
  proofs not reviewed here. (T2)'s interface confirmed at
  $\lambda=\aleph_\beta$ in W2.
- **The GCH remark of the Problem 1218 section** (lines 486--505), the
  input S2 describes; its own argument is another reviewer's subject.
- **The Problem 1171 connections page**, lines 658--676, and **the Problem
  501 connections page**, lines 480--600 and 713--735, read to confirm the
  two citations of S6 and S7; their mathematics is not consumed.
- **Problem statements**, Statement paragraphs only, of the ten problem
  pages listed above.
- **Komjáth 2025 card**, provenance paragraph; the conversion is held; not
  consulted for any theorem.
- Standard facts used without citation: the order type of a set of
  ordinals is at least the initial ordinal of its cardinality; the
  supremum of a strictly increasing $\kappa$-sequence of cardinals is a
  limit cardinal of cofinality $\operatorname{cf}\kappa$;
  $\operatorname{cf}\aleph_\beta=\operatorname{cf}\beta$ for limit $\beta$;
  a successor cardinal is regular; $2^\kappa\ge2^{\aleph_0}$ for infinite
  $\kappa$.

## Findings

- **F1 (suggested).** Location, lines 547--551: "It does not apply to
  Problem 1168, a negative relation on the regular cardinal
  $\aleph_{\omega+1}$, beyond the GCH remark in the Problem 1218 section,
  which uses (T2) at the singular $\aleph_\beta$ and not at
  $\aleph_{\omega+1}$". Defect: "beyond the GCH remark" reads as if the
  remark applied the page's tools to Problem 1168. The remark consumes the
  GCH case of the problem's relation as a premise, taken from the survey's
  report, and proves a relation at $\aleph_\beta$; nothing on the page
  proves anything at $\aleph_{\omega+1}$, and the problem asks for a proof
  without GCH. Witness: the remark's text at lines 491--500. Replacement:
  "It does not apply to Problem 1168, a negative relation on the regular
  cardinal $\aleph_{\omega+1}$: no relation on this page has a successor
  cardinal as its resource. The GCH remark in the Problem 1218 section
  consumes the GCH case of that relation as a premise and applies (T2) at
  the singular $\aleph_\beta$; it proves nothing at $\aleph_{\omega+1}$."
- **F2 (required).** Location, lines 551--553: "nor to Problem 70, a
  relation for triples on the order type of the reals, which has no block
  decomposition into regular cardinals". Defect: by the page's Scope
  paragraph a block decomposition of $X$ is any partition of $X$ into
  $\kappa$ pieces, and the reals, a set of size $2^{\aleph_0}$, have such
  partitions into pieces of regular cardinality. Witness:
  $\mathbb R=\bigsqcup_{x\in\mathbb R/\mathbb Q}(x+\mathbb Q)$, a partition
  into $2^{\aleph_0}$ countable pieces, $\aleph_0$ being regular. The
  recorded reason is therefore false as written; the non-applicability is
  true for a reason of a different kind, the size floor of W1, which no
  reader can recover from the sentence. Replacement: "nor to Problem 70, a
  relation for triples with an order-type target on the reals: (T1) passes
  to the lemma the hypothesis $2^{\chi+\kappa}<\lambda_0\le|A|$, which puts
  every domain of the lemma above $2^{\aleph_0}=|\mathbb R|$, and Theorem
  1.2's resource exceeds $2^{\mu(0)}\ge2^{\aleph_0}$, so no coloring of a
  set of size continuum is in the mechanism's scope; (T2) and (T3) produce
  negative relations for pairs and bear on no positive relation for
  triples." The problem page says "the ordinal of the real numbers"; the
  floor blocks both readings, the order type of $\mathbb R$ and the
  cardinal $2^{\aleph_0}$.
- **F3 (note).** Location, lines 554--556: "balanced or ordinal-target
  relations on the regular cardinals $\omega_2$ and $\omega_3$". Balance is
  not an obstruction for this mechanism, whose own output
  $\chi\to(\lambda)^2_2$ is balanced; it is an obstruction for the
  color-merging induction of the Problem 1171 page. The operative reasons
  are the regular resources below $\aleph_\omega$ (W1) and the ordinal
  targets, which homogeneous sets controlled only in cardinality do not
  deliver. Suggest dropping "balanced or".
- **F4 (note).** Location, lines 558--563: "their obstructions are on the
  Problem 501 connections page". Those sections record obstructions to that
  folder's set-mapping recursion and $\Delta$-system tools, not to the
  mechanism of this page, and the sentence can be read as delegating this
  page's obstruction. Suggest "the obstructions to that folder's
  set-mapping tools are on ...". Also, the resource $\omega_{\omega+1}$ of
  Problem 1173 is regular, which defeats the block shape of S1 as well and
  is worth one clause.
- **F5 (note).** Location, lines 565--567: "the two are disjoint in what
  they consume". Both mechanisms consume two-place colorings; "disjoint" is
  true of the structural hypotheses each page lists (a color-$0$ target
  equal to the ambient order type or a descending chain, with fixed targets
  in the other colors, against a singular sum with
  $\operatorname{cf}\lambda$ blocks of sizes $(2^{\mu(i)})^+$ and a positive
  relation at $\operatorname{cf}\lambda$). Suggest "share no hypothesis".
- **F6 (note, outside the section's mathematics).** Under GCH the first
  relation of Problem 1172 as the problem page prints it,
  $\omega_3\to(\omega_2,\omega_1+2)^2$, follows from the relation (ER) the
  theorem page imports: at $\mu=\aleph_1$ it reads
  $\aleph_3\to(\aleph_3,\aleph_2)^2$; a $0$-homogeneous set of size
  $\aleph_3$ contains a subset of order type $\omega_2$, and a
  $1$-homogeneous set of cardinality $\aleph_2$ has order type at least
  $\omega_2>\omega_1+2$, hence contains a subset of order type
  $\omega_1+2$. This does not touch S4: (ER) is a single-block input, not
  the block-to-cofinality mechanism. It does mean that the printed relation
  is a theorem given (ER), which suggests a misprint in the catalog's
  wording; flagged for the problem page's status search, at the standing of
  (ER) on the theorem page (imported, source not held).

## Verdict

- **S1**: refutation-failed. The three features are each consumed at a
  named step of the theorem page, and no conclusion of the section depends
  on the features the list omits.
- **S2**: refutation-failed. No relation of the page has a successor
  cardinal as resource; the cited use of (T2) is at $\aleph_\beta$ with
  the $\aleph_{\omega+1}$ relation as hypothesis. Wording, F1.
- **S3**: refutation-failed for the non-applicability statement, whose
  correct reason is the size floor of W1; the reason recorded in the
  section is false as written and requires the replacement in F2.
- **S4**: refutation-failed. The resources $\omega_2$ and $\omega_3$ lie
  below $\aleph_\omega$, the floor of every resource of the page, and are
  regular. Descriptor, F3; observation on the problem page's wording, F6.
- **S5**: refutation-failed. A coloring of countable subsets is not a
  function of finitely many places.
- **S6**: refutation-failed. At $\aleph_\omega$ the block shape is
  available, and the clauses of Lemma 1.1 still deliver no free set; at
  $\aleph_{\omega+1}$ the resource is regular as well. Wording, F4.
- **S7**: refutation-failed. The citation is faithful and Corollary 1.3
  is the specialization claimed. Wording, F5.

**Limitations.** The non-applicability claims were tested against the
mechanism as the reconstruction pages state it and against the page's
Tools; the review did not search for other uses of the source's ideas
(other properties $P_\alpha$, clause (3), or a different block shape) that
might reach these problems, since the section claims nothing about them.
The proofs of (T1), (T2) and (T3) and of the Problem 1218 remark are other
reviewers' subjects and were not checked here. F6 rests on (ER) at its
recorded standing, an imported relation whose source is not held.

This focused review assigns no tier and changes no status.
