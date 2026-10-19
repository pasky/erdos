---
name: research/erdos_1171/evidence/verify/connections_problems_590_591_592_and_118_countable_partition_review
title: "Independent review of the connections section: Problems 590, 591, 592 and 118: countable partition ordinals"
desc: |
  Refutation review of the section's eleven author-recorded statements: the
  ten mathematical and reporting statements are refutation-failed and the
  closing novelty remark is unverifiable within the read set; no required
  corrections, two suggested wording corrections and three notes.
created: 2026-09-28T18:59:22Z
updated: 2026-09-28T18:59:22Z
---

***

## Subject and independence

Role: independent reviewer, working in a fresh context from the commissioned
assignment alone. The reviewer took no part in writing the connections page,
its Tools section, the reconstruction pages or any library page, and had no
contact with the author, the grader or any other reviewer. Charge:
refutation.

Subject: path `wiki/research/erdos_1171/connections.md` as it stood on
2026-09-28T13:50:48Z (called "the commit" below), section "Problems 590, 591,
592 and 118: countable partition ordinals", lines 410--491 (the next H2
begins at line 493). No separate lead page is named; the section is the
subject.

Read, at that commit:

- The section, clause by clause. The page's frontmatter and Scope paragraph
  (lines 1--31) and its Tools section (lines 32--123) as inputs; the section
  uses (T1), (T2) and (T5), and (T5) was re-derived here because the
  section's "conversely" rides on it. (T3) and (T4) are not used by the
  section. The page's H2 heading list was seen when locating the section.
- [[research/erdos_1171/lemma_2_1_reconstruction|the Lemma 2.1 page]] and
  [[research/erdos_1171/theorem_3_1_reconstruction|the Theorem 3.1 page]] in
  full, as premises at their reviewed standing.
- The Statement paragraphs of the pages of Problems 590, 591, 592 and 118
  under `wiki/problems/set_theory/`.
- Library: the provenance of
  [[../library/set_theory/chang_1972_partition_theorem_complete_graph_omega_omega/_index|Chang (1972)]]
  and the Statement, Source and Read depth paragraphs of its
  [[../library/set_theory/chang_1972_partition_theorem_complete_graph_omega_omega/theorem_p396|theorem page]];
  the same paragraphs of
  [[../library/set_theory/schipperus_2010_countable_partition_ordinals/theorem_28|Theorem 28]]
  and
  [[../library/set_theory/schipperus_2010_countable_partition_ordinals/theorem_29|Theorem 29]];
  [[../library/set_theory/baumgartner_1989_remarks_partition_ordinals/main_theorem|Baumgartner's result page]]
  in full, since its "Consequence for Problem 1171" is the finite-Ramsey
  bridge the section compares against; the provenance of
  [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth (2025)]];
  and, for the Nešetřil--Rödl theorem the section invokes, the digest
  paragraphs of the two library cards found by searching the library for
  Problem 924, the Erdős surveys of 1969 (chromatic graph theory) and 1975
  (combinatorial number theory).
- Held PDFs, in the text layer: Chang 1972, printed pp. 396--397 (the
  theorem, its notation and footnote 1); Schipperus 2010, printed
  pp. 1195--1197 and 1212--1215 (Definitions 1 and 2, Theorems 1--4, 28, 29
  and 31--33 with their proofs, the closing remark), plus a search of the
  whole text for any axiom beyond ZFC; Komjáth 2025, printed pp. 425--426
  (Problem 13 commentary) and 441--443 (Problems 53 and 54).
- `docs/verification.md` ("Grading and claim standing", the shared and the
  Erdos-specific "Audit checklist", "Whole-claim report"),
  `docs/approach_vetting.md`, `docs/evidence.md` ("Source fidelity") and
  `docs/math_authoring.md`.

Exposures. (1) Locating the statement of Problem 590 printed the heading
"Current assessment" and its first paragraph, which says that no current
assessment is recorded and that the page's notes are author-recorded
transfers; it carries no mathematics and was not used. (2) Searching the
library for Problem 924 printed the first seventy lines of the Ramsey-theory
library index and of the Spencer 1975 card; neither bears on the section.
(3) The Source and Read depth paragraphs of the result pages and the standing
line of Baumgartner's result page were read as provenance; they record
reading depth and holding, not verdicts. Not read: the folder index,
everything under `evidence/`, every Current assessment, Known results,
standing or acceptance text, the other sections of the connections page
(including the "next section" the section cites twice), the pages of
Problems 924 and 54, anything among the private working files, and the web.

## Restatement

Conventions. $\alpha\to(\beta_0,\ldots,\beta_{n-1})^2_n$ means that every
coloring of $[\alpha]^2$ with the colors $0,\ldots,n-1$ has, for some $i<n$,
a subset of order type $\beta_i$ homogeneous in color $i$; color $0$ carries
the large target; $\not\to$ is the negation, and a witness for a negative
relation is a coloring that refutes it. This is the lemma page's convention
and Schipperus's Definition 1 (color $0$ for the first entry, color $1$ for
the second). Chang's paper puts the triangle in class $R$ and the large set
in class $B$; the relabeling is fact 2 of the lemma page. The relation
$\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$ has $k$ triangle colors.

- **S1** (Problem 590, reporting). $\omega^\omega\to(\omega^\omega,3)^2$ is
  the theorem on printed p. 396 of Chang 1972, held. The relation
  $\omega^\omega\to(\omega^\omega,m)^2$ for every finite $m$ is reported in
  the held corpus and not proved there: Chang's footnote 1 (p. 397) reports
  Milner's proof, communicated by letter, and Larson's shorter proof of both
  results; Larson's paper is not held.
- **S2** (Problem 591, reporting).
  $\omega^{\omega^2}\to(\omega^{\omega^2},3)^2$ is the case
  $\beta=2=\omega^0+\omega^0$ of Schipperus's Theorem 28: for every
  countable $\beta$ that is the sum of one or two indecomposable ordinals,
  $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$.
- **S3** (Problem 592, reporting). Among countable $\beta$, the relation
  $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ holds when $\beta$
  is a sum of one or two indecomposables (Theorem 28) and fails when
  $\beta$ is a sum of four or more (Theorem 29, part 3, as printed); the
  held sources do not decide $\beta$ a sum of exactly three.
- **S4** (Problem 118, reporting). The question whether
  $\alpha\to(\alpha,3)^2$ implies $\alpha\to(\alpha,n)^2$ for every finite
  $n$ is refuted at $\alpha=\omega^{\omega^2}$ by Theorem 28 (the case
  $n=3$ holds) with Theorem 29 part 1 (the case $n=6$ fails), and, as
  Schipperus reports on p. 1197 without proof, by Larson's
  $\omega^{\omega^2}\not\to(\omega^{\omega^2},5)^2$ next to her
  $\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$; Larson's paper is not
  held.
- **S5** (transfer). For every ordinal $\alpha$ and every finite $k\ge1$,
  $\alpha\to(\alpha,3)^2$ if and only if
  $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$: forward by Lemma 2.1, backward by
  (T2) (leave colors unused) or by (T5) (a many-color witness contains a
  two-color witness on a subset of full type).
- **S6** (Problem 592). For every countable ordinal $\beta$ and every finite
  $k\ge1$, $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ if and only
  if $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3,\ldots,3)^2_{k+1}$.
  The attached assessment, that the reformulation enables nothing new, is
  an author's judgment and not a claim.
- **S7** (Problem 591). For every finite $k\ge1$,
  $\omega^{\omega^2}\to(\omega^{\omega^2},3,\ldots,3)^2_{k+1}$ (Theorem 28
  with Lemma 2.1), while $\omega^{\omega^2}\not\to(\omega^{\omega^2},6)^2$
  (Theorem 29 part 1). Comparison: the finite-Ramsey bridge recorded on
  Baumgartner's result page derives the relation with $k$ triangle colors
  from $\alpha\to(\alpha,n)^2$ with $n$ the $k$-color Ramsey number of the
  triangle; for $k=2$ that is $n=R(3,3)=6$, so at $\alpha=\omega^{\omega^2}$
  the bridge's hypothesis fails while Lemma 2.1's holds, and the lemma's
  hypothesis is strictly weaker. At $\alpha=\omega^\omega$ both hypotheses
  are available, the bridge's through Milner's reported result.
- **S8** (Problem 118's color sibling). For every $\alpha$ that is a
  cardinal, an ordinal or an order type, and every finite $k\ge1$: if
  $\alpha\to(\alpha,3)^2$ then $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$, where
  for an order type a subset "of type $\alpha$" is one order-isomorphic to
  the whole and for a cardinal one of the same cardinality.
- **S9** (ZFC instance). At $\alpha=\omega^{\omega^2}$, in ZFC,
  $\alpha\not\to(\alpha,6)^2$ and $\alpha\to(\alpha,3,3,3,3,3)^2_6$; on
  Larson's unheld result, $\alpha\not\to(\alpha,5)^2$ and
  $\alpha\to(\alpha,3,3,3,3)^2_5$. Komjáth's recorded question (p. 443)
  asks whether $\alpha\not\to(\beta,4)^2$ and $\alpha\to(\beta,3,3,3)^2$ can
  hold together for some ordinals $\alpha,\beta$; the instance has the same
  shape with $6$ against five triangle colors ($5$ against four) and does
  not answer that question.
- **S10** (finite corollary). Let $c$ witness $\alpha\not\to(\alpha,6)^2$
  and let $X$ be the graph on $\alpha$ whose edges are the pairs of color
  $1$. Then $X$ has no $K_6$ and no independent set of order type $\alpha$;
  every coloring of the edges of $X$ with five colors has a monochromatic
  triangle; and some finite subgraph of $X$, a finite $K_6$-free graph, has
  the same five-color property, in the pattern of the argument Komjáth
  attributes to Hajnal but without its forcing step. The finite statement
  is implied by the Nešetřil--Rödl theorem as Komjáth reports it: for every
  number of colors there is a finite $K_4$-free graph every edge coloring of
  which has a monochromatic triangle.
- **S11** (novelty remark). "Only the derivation through a countable ordinal
  is new here": a claim about the literature, offered without a search.

## Checklist

- **Quantifiers and scope**: pass. Every transfer is stated for each fixed
  finite $k$ and for the exact $\alpha$ named. "For every countable $\beta$"
  in S6 includes $\beta=0$, where $\omega\to(\omega,3)^2$ is Ramsey's
  theorem and the equivalence holds. "Every cardinal" in S8 needs the
  one-line bridge of F3, after which the quantifier is correct. "Four or
  more" in S3 is the printed theorem's own range (F4).
- **Circularity**: pass. Lemma 2.1 consumes $\alpha\to(\alpha,3)^2$ as its
  hypothesis; the converse in S5 uses only unused colors or (T5); nothing
  assumes its own conclusion.
- **Model and convention changes**: pass. The color conventions of the lemma
  page, of Schipperus's Definition 1 and of Chang's classes were compared
  by their definitions, not by shape. The passage from ordinals to order
  types in S5 and S8 was checked inside the lemma's proof, which uses only
  order isomorphisms and subsets; the passage to cardinals is the bridge of
  F3. The compactness step of S10 replaces an infinite graph by a finite one
  with a proved transfer (W3).
- **Finite and statistical overreach**: pass; no finite case stands in for a
  proof, and the finite corollary is derived, not sampled.
- **Uniformity**: pass. There are no constants; the number of colors is a
  free finite parameter and every relation is asserted for each value of it
  separately.
- **Extremal conclusions**: pass. "Strictly stronger" in S7 was checked in
  the claim's own units: $R(3,3)=6$ was re-derived (a pentagon and its
  pentagram two-color $K_5$ without a monochromatic triangle; in $K_6$ three
  of the five edges at a vertex share a color and their far endpoints close
  a monochromatic triangle either way), and
  $\omega^{\omega^2}\not\to(\omega^{\omega^2},6)^2$ is Theorem 29 part 1.
- **Consequences and composition**: pass, with two wording findings. Each
  "hence" was attacked separately (Weakest steps, Strongest attack). The
  composition S9 names both held theorems and Lemma 2.1 and marks Larson's
  input "not held"; the last sentence of S7 consumes Milner's result at a
  higher standing than the corpus records (F1).
- **Computation**: not applicable; nothing beyond $R(3,3)=6$ is computed.
- **Reproduction**: not applicable; the section carries no rerun
  instructions or coverage claims.
- **Source and verdict fidelity**: pass, with one finding. Theorems 28 and
  29, Definition 1, the closing remark and the report of Larson's results
  were checked against the Schipperus PDF; Chang's theorem and footnote 1
  against the Chang PDF; Hajnal's argument and the open question against
  the Komjáth PDF; the Nešetřil--Rödl statement against Komjáth's report
  and the two Erdős digests, the paper itself not being held. The standing
  words "held", "not held" and "author-recorded" are used correctly except
  in the sentence of F1. The novelty sentence S11 claims more than the
  page's declared reading can support (F2).

## Weakest steps

**W1. The backward direction of S5 through (T5).** Let
$c:[\alpha]^2\to\{0,\ldots,k\}$ witness
$\alpha\not\to(\alpha,3,\ldots,3)^2_{k+1}$. Claim: there are
$Y\subseteq\alpha$ of order type $\alpha$ and $j\in\{1,\ldots,k\}$ such
that the two-coloring $d_j$ of $[Y]^2$ with $d_j(p)=1$ if $c(p)=j$ and
$d_j(p)=0$ otherwise witnesses $\alpha\not\to(\alpha,3)^2$ after transport.
For $k=1$ take $Y=\alpha$, $j=1$: $d_1=c$. For $k\ge2$ let $c'$ send the
values $0$ and $k$ to $0$ and fix the others. Case A: some $Y$ of type
$\alpha$ has $c'=0$ on $[Y]^2$, so $c$ takes only the values $0$ and $k$
there. Take $j=k$. A $d_k$-color-$0$ subset of $Y$ of type $\alpha$ would
have $c=0$ on all its pairs, which the witness forbids; a $d_k$-color-$1$
triangle would be a $c$-color-$k$ triangle, also forbidden. Case B: $c'$ has
no color-$0$ subset of type $\alpha$, and no triangle in a color
$1,\ldots,k-1$, since $c'$ equals $c$ on those colors; so $c'$ witnesses the
relation with $k-1$ triangle colors and the induction gives $Y$ and
$j\le k-1$ for $c'$; the coloring $d_j$ built from $c$ is the same function,
because $c(p)=j$ if and only if $c'(p)=j$ for $j\le k-1$. Transport along
the order isomorphism $\alpha\to Y$ carries subsets of type $\alpha$ and
triangles both ways. The step composes with Lemma 2.1 to give the
equivalence of S5 and, at $\alpha=\omega^{\omega^\beta}$, S6. The degenerate
orders $\alpha<3$ were checked: for $\alpha=2$ the single pair colored $k$
falls in Case A and $d_k$ is the witness for $2\not\to(2,3)^2$.

**W2. S8 beyond ordinals.** Lemma 2.1 is stated for ordinals. Its induction
step, re-derived: given $c$ on $[A]^2$ with colors $0,\ldots,k+1$, merge
$0$ and $1$ into $0$; the case $k$ gives a triangle in a color $i\ge1$ of
the merged coloring, hence a $c$-triangle in color $i+1$, or a subset $Y$
of $A$ of type $\alpha$ with $c\in\{0,1\}$ on $[Y]^2$; an order isomorphism
$A\to Y$ pulls $c\restriction[Y]^2$ back to a two-coloring of $[A]^2$, and
$\alpha\to(\alpha,3)^2$ gives a subset of $Y$ of type $\alpha$ homogeneous
in $0$ or a triangle in color $1$. Nothing uses that $A$ is well ordered, so
the lemma holds for a linear order type $\alpha$ with "type $\alpha$"
meaning order-isomorphic to $A$, which is (T1)'s remark. For a cardinal
$\kappa$, the statement of Problem 118 reads $K_\kappa$ as the complete
graph on $\kappa$ vertices and a red $K_\kappa$ as a red complete subgraph
on $\kappa$ vertices, a cardinality relation. Bridge: transport along a
bijection to the initial ordinal $\kappa$; a subset of the ordinal $\kappa$
has order type at most $\kappa$, and an ordinal of cardinality $\kappa$ is
at least $\kappa$, so its subsets of cardinality $\kappa$ are exactly its
subsets of order type $\kappa$; the ordinal lemma then gives the cardinal
statement. The bridge is not written in the section or in (T1) (F3), but
the statement S8 is true as written.

**W3. The compactness step of S10.** Let $P(G)$ say that every coloring of
the edges of $G$ with five colors has a monochromatic triangle. $P(X)$ was
derived first: extend a five-coloring $e$ of the edges of $X$ to
$d:[\alpha]^2\to\{0,\ldots,5\}$ by $d=0$ on non-edges; by
$\alpha\to(\alpha,3,3,3,3,3)^2_6$ either some set of type $\alpha$ is
$d$-homogeneous in $0$, that is, independent in $X$ and of type $\alpha$,
contradicting the witness, or some triangle is $d$-homogeneous in a color
$1,\ldots,5$, and its three pairs are edges of $X$ carrying one $e$-color.
Now suppose no finite subgraph of $X$ satisfies $P$, so each finite
$F\subseteq X$ has a five-coloring of its edges with no monochromatic
triangle. In the product space $\{1,\ldots,5\}^{E(X)}$, compact by
Tychonoff's theorem for finite discrete factors (or by König's lemma, as
$\alpha$ is countable), the set $C_F$ of colorings of $E(X)$ whose
restriction to $E(F)$ has no monochromatic triangle is closed, being
determined by finitely many coordinates, and nonempty; the intersection
$C_{F_1}\cap\cdots\cap C_{F_m}$ contains $C_{F_1\cup\cdots\cup F_m}$, which
is nonempty; so the intersection of all $C_F$ is nonempty and holds a
five-coloring of $E(X)$ with no monochromatic triangle, contradicting
$P(X)$. Hence some finite subgraph, $K_6$-free as a subgraph of $X$,
satisfies $P$. With the Nešetřil--Rödl theorem at five colors, a $K_4$-free
graph is $K_6$-free, so that theorem implies the finite statement, which is
the "weaker" of S10.

## Strongest attack

- S1--S4 (reporting). Attack: find a misquotation or a wrong range. The
  Chang text layer prints the theorem and the footnote as the section
  reports them; Schipperus prints Theorem 28 for "the sum of one or two
  indecomposable ordinals", Theorem 29 with the ranges two, three and
  $\ge4$, the closing remark at $\beta=2$, and on p. 1197 Larson's
  improvement of $6$ to $5$ with $\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$
  cited to a reference not held. The attack found only that "three
  undecided" and "four or more" are relative to the held sources (F4) and
  that S4's sentence names the negative half alone, the positive half being
  the preceding sentence; both are wording.
- S5 and S6. Attack: a coloring of $[\alpha]^2$ with $k+1$ colors, no
  color-$0$ set of type $\alpha$ and no monochromatic triangle in a color
  $\ge1$, for some $\alpha$ with $\alpha\to(\alpha,3)^2$. Lemma 2.1 excludes
  it for every ordinal; the attack then aimed at (T5)'s extraction, trying
  a merged coloring whose color-$0$ set of full type carries only the color
  $k$ (then $d_k$ is constantly $1$ and any three points are a forbidden
  $c$-color-$k$ triangle, so the case cannot arise for $|\alpha|\ge3$), and
  at $\alpha<3$ (W1). It failed.
- S7. Attack: show that the finite-Ramsey bridge at $k=2$ can run on a
  hypothesis weaker than $\alpha\to(\alpha,6)^2$. As recorded on
  Baumgartner's page the bridge merges the triangle colors and needs a
  monochromatic $n$-set with every two-coloring of $K_n$ having a
  monochromatic triangle; the least such $n$ is $6$, so the recorded bridge
  needs exactly $\alpha\to(\alpha,6)^2$, which Theorem 29 part 1 refutes at
  $\omega^{\omega^2}$; and $\alpha\to(\alpha,6)^2$ implies
  $\alpha\to(\alpha,3)^2$ by (T2), so the lemma's hypothesis is weaker and,
  at this $\alpha$, strictly so. The attack failed; the "which is false"
  clause is grammatically attached to the $6$-relation, not to the $k=2$
  relation (F5).
- S8. Attack: an order type or cardinal where the induction breaks. Order
  types: the proof needs only order isomorphisms and subsets (W2), and a
  non-well-ordered example such as $\omega^*$ or a scattered sum behaves
  identically. Cardinals: the cardinality reading of the relation reduces
  to the order-type reading on the initial ordinal (W2). The attack failed;
  the unstated cardinal bridge is F3.
- S9. Attack: an axiom beyond ZFC hidden in Schipperus's proofs. The paper
  lists Martin's axiom among its keywords, but a search of the whole text
  finds no other occurrence; Theorem 28's proof reduces to the
  Erdős--Milner theorem and the paper's own game dichotomy, and Theorems
  31--33 exhibit explicit pattern colorings. Nothing beyond ZFC is invoked.
  A second attack, that the instance answers Komjáth's question, fails on
  the clique numbers ($6$ or $5$, not $4$); the section claims only a
  cousin. The attack failed.
- S10. Attack: (a) the extended coloring might produce a "triangle" with a
  non-edge, but non-edges carry only color $0$ and the triangle's color is
  $\ge1$; (b) compactness might fail to preserve "every five-coloring has a
  monochromatic triangle", but the property is finitary and W3 gives the
  transfer; (c) the comparison with Nešetřil--Rödl might be reversed, but
  $K_4$-free implies $K_6$-free and the Komjáth report states the theorem
  for every number of colors and every clique size. The attack failed.
- S11. No mathematical attack exists; the claim is about the literature and
  the page's declared reading contains no search for it (F2).

## Premises

- [[research/erdos_1171/lemma_2_1_reconstruction|Lemma 2.1 reconstruction]]:
  for an ordinal $\alpha$ with $\alpha\to(\alpha,3)^2$ and every finite
  $k\ge1$, $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$, in ZFC, with facts 1
  (transport along an order isomorphism) and 2 (relabeling). Reviewed as it
  stood on 2026-09-28T05:03:27Z per the assignment; read in full; consumed by
  the section at $\alpha=\omega^{\omega^\beta}$ and, through (T1), for order
  types and cardinals (W2).
- [[research/erdos_1171/theorem_3_1_reconstruction|Theorem 3.1 reconstruction]]:
  read in full; the section uses it only through (T2)'s citation of its
  Steps 2 and 3 (restriction of a coloring to a subset and reading the
  result in the larger order); interface confirmed.
- Tools of the connections page: (T1) transport, extended to order types;
  (T2) restriction and weakening, including unused colors; (T5) witness
  extraction. Their proofs are another reviewer's; (T5) was re-derived
  (W1) and the interfaces of all three were confirmed at each use.
- Chang 1972, theorem on printed p. 396, $\omega^\omega\to(\omega^\omega,3)^2$,
  held; the text layer of pp. 396--397 read; footnote 1 reports Milner's
  $\omega^\omega\to(\omega^\omega,m)^2$ for finite $m$ and Larson's shorter
  proof; those proofs are not held.
- Schipperus 2010, Theorem 28 (p. 1212) and Theorem 29 (p. 1213) with
  Theorems 31--33 and the closing remark (pp. 1214--1215), held; statements
  read clause by clause in the text layer; proofs read but not checked,
  and taken at the standing the result pages record (not independently
  reviewed). The report of Larson's $5$ and $4$ (p. 1197) is a citation to
  a paper not held.
- Baumgartner's result page, "Consequence for Problem 1171": the
  finite-Ramsey bridge, author-recorded; read in full; used by the section
  only as the object of comparison in S7.
- Komjáth 2025, held; Problem 54 discussion (pp. 442--443) read: Hajnal's
  argument, the Nešetřil--Rödl statement, and the open question with $4$
  against three triangle colors; Problem 13 commentary (pp. 425--426) read.
- The Nešetřil--Rödl theorem: not held; taken from Komjáth's report and the
  digests of the two Erdős surveys, which give the same statement.
- $R(3,3)=6$ and the compactness of $\{1,\ldots,5\}^{E(X)}$: classical,
  re-derived in the Checklist and W3.

## Findings

- **F1** (suggested). Location: "For Problem 590 the two bridges agree,
  since $\omega^\omega\to(\omega^\omega,m)^2$ holds for every finite $m$."
  Defect: the relation is consumed at a higher standing than the corpus
  records; the held Chang paper only reports Milner's proof by letter and
  Larson's proof in a thesis, and Larson's paper is not held, as the
  section's own Targets paragraph says ("reported"). Witness: Chang 1972,
  footnote 1, p. 397; the Chang card's provenance. Proposed replacement:
  "since $\omega^\omega\to(\omega^\omega,m)^2$ for every finite $m$ is
  reported from Milner and Larson (proofs not held)."
- **F2** (suggested). Location: "only the derivation through a countable
  ordinal is new here." Defect: a novelty claim about the literature that
  the page's declared reading (the held corpus, the catalog pages and one
  arXiv abstract) cannot support; the derivation is the compactness pattern
  the section itself attributes to Hajnal, applied to another partition
  ordinal. Witness: the page's Scope paragraph; `docs/approach_vetting.md`
  "Compare substance, not vocabulary" (an incomplete search is described
  as such). Proposed replacement: "the derivation through a countable
  ordinal is not in the held sources; no literature search was made for
  it."
- **F3** (note). Location: "holds for every cardinal, ordinal or order type
  $\alpha$ and every finite $k$, by Lemma 2.1 with (T1)." Defect: for a
  cardinal the relation of Problem 118 counts vertices, and neither the
  lemma (ordinals) nor (T1) (order types, order isomorphisms) states the
  step from cardinality to order type. Witness: W2. Proposed replacement:
  add "for a cardinal, read as the initial ordinal, whose subsets of full
  cardinality are its subsets of full order type".
- **F4** (note). Location: "no for four or more (Theorem 29, part 3), with
  three undecided." Defect: none in the section's own terms, which cite
  the theorem at the standing its result page records; the reader should
  know that the result page records the printed proof (Theorem 33) as
  treating exactly four summands, and that "undecided" is relative to the
  held sources, no literature search having been made. Witness: the
  Theorem 29 result page; Schipperus p. 1215. Proposed replacement: "no for
  four or more (Theorem 29, part 3, whose printed proof treats four), with
  three undecided in the held sources."
- **F5** (note). Location: "would need
  $\omega^{\omega^2}\to(\omega^{\omega^2},6)^2$ through the Ramsey number
  $R(3,3)=6$, which is false." Defect: none mathematically; a hostile
  reading attaches "which is false" to the $k=2$ relation of the same
  sentence, which is true. Proposed replacement: "and that relation is
  false."

## Verdict

- S1: refutation-failed.
- S2: refutation-failed.
- S3: refutation-failed, read at the standing of the held sources (F4).
- S4: refutation-failed.
- S5: refutation-failed.
- S6: refutation-failed.
- S7: refutation-failed; the closing sentence on Problem 590 consumes a
  reported result (F1).
- S8: refutation-failed, with the cardinal bridge of W2 supplied here (F3).
- S9: refutation-failed.
- S10: refutation-failed.
- S11: not a mathematical claim and unverifiable within the read set; it
  receives none of the three verdicts (F2).

Limitations. The section's two references to "the next section" were
checked against the Komjáth PDF, not against that section, which lies
outside the read set. The sentence that none of the four problem pages has
a compiled assessment beyond its references was not checked, since the
pages' assessment text is excluded. Schipperus's proofs were not checked
and enter at the standing their result pages record; Larson's and Milner's
results and the Nešetřil--Rödl paper are not held; no web search was made,
so "undecided" and "new" were judged against the held corpus only. The
Tools section's own proofs were another reviewer's subject, and only (T5)
was re-derived here.

This focused review assigns no tier and changes no status.
