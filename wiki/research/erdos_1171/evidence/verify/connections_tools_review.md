---
name: research/erdos_1171/evidence/verify/connections_tools_review
title: "Independent review of the connections section: Tools"
desc: |
  Refutation-failed for all eight mathematical statements of the Tools
  section, from the transport definition through the two-color equivalence.
  No required corrections; three suggested precision corrections and three
  notes.
created: 2026-09-28T18:46:20Z
updated: 2026-09-28T20:42:19Z
---

***

## Subject and independence

**Role.** Independent reviewer in a fresh context, commissioned for
refutation and given only the assignment. The reviewer took no part in
writing the connections page, the reconstruction pages or their reviews, and
had no contact with the page author or with the reviewers and grader of the
reconstruction pages.

**Subject.** The source as it stood on 2026-09-28T13:50:48Z (called "the
subject commit" below), page
`wiki/research/erdos_1171/connections.md`, section `## Tools`, lines
32--123; the next H2 heading is line 125. The section records a definition
and transport fact (T1), restriction and weakening (T2), the induction with
general targets (T3), the descent lemma (T4) with its proof, witness
extraction (T5) with its proof, and a closing equivalence between
$\alpha\to(\alpha,3)^2$ and its finite-color form. The lead page is the same
page; its Scope paragraph (lines 18--30) was read as the page's standing
statement.

**Reading.** Read in full at the subject commit: the section; the two
reconstruction pages
[[research/erdos_1171/lemma_2_1_reconstruction|Lemma 2.1]] and
[[research/erdos_1171/theorem_3_1_reconstruction|Theorem 3.1]], as premises;
the Statement paragraphs of [[problems/set_theory/E1171/_index|Problem 1171]] and
[[problems/set_theory/E0118/_index|Problem 118]]; the provenance paragraph of the
library card
[[../library/set_theory/gao_2026_finite_color_partition_relation_omega_1_squared/_index|Gao (2026)]]
and the Statement section of its
[[../library/set_theory/gao_2026_finite_color_partition_relation_omega_1_squared/lemma_2_1|Lemma 2.1 result page]];
the held four-page PDF of that source, all pages by text extraction and
pages 2 and 4 on page images (Lemma 2.1 with its proof; Remark 3.2); and the
guidance pages named in the commission (`docs/verification.md`, sections
"Whole-claim report", "Audit checklist" and "Grading and claim standing";
`docs/approach_vetting.md`; `docs/evidence.md`, section "Source fidelity";
`docs/math_authoring.md`). The other sections of the lead page were
consulted only through a keyword scan for the uses of (T1)--(T5), of graph
targets and of order types, and one paragraph (lines 458--463, on Problem
118) was read in full as the consumer of the order-type remark in (T1).

**Exposure.** The folder index is excluded and was not read, so the
attribution of (T3) to it is unchecked here; (T3) is verified below as the
constant case of (T4). A directory listing of `evidence/verify/` showed the
file names of the two reconstruction reviews and the grade; none was opened.
No Current assessment, Known results, standing or acceptance text was read.
Nothing else reached the reviewer.

## Restatement

Throughout, a coloring of $[X]^2$ with the colors $0,\ldots,k$ is a function
on the two-element subsets of a linearly ordered set $X$; a subset is
homogeneous in color $i$ when all its pairs have color $i$; a target is an
order type or a graph; and a *copy* of a target $H$ in $X$ is a subset of $X$
of order type $H$ when $H$ is an order type, and a subgraph of the complete
graph on $X$ isomorphic to $H$ when $H$ is a graph. The copy is *in color
$i$* when all pairs of the subset, respectively all edges of the subgraph,
have color $i$. This is the reading of "all of whose pairs have color $i$"
adopted here; F2 records the ambiguity. A triangle is a copy of the order
type $3$.

- **S0 (provenance sentence).** "Five facts are used below. The first two
  are on the reconstruction pages, the third is stated on the folder index,
  and the last two are recorded here with their proofs." Not a mathematical
  claim; assessed under Source and verdict fidelity.
- **S1 (T1, definition and transport).** For an order type $\gamma$, an
  order type $\beta$, targets $H_1,\ldots,H_k$ and $k\ge1$, the relation
  $\gamma\to(\beta,H_1,\ldots,H_k)^2_{k+1}$ means: every coloring of
  $[\gamma]^2$ with the colors $0,\ldots,k$ has a subset of order type
  $\beta$ homogeneous in color $0$, or, for some $i\in\{1,\ldots,k\}$, a
  copy of $H_i$ in color $i$. If $Y$ is a linearly ordered set (in the
  section, a set of ordinals) with $\operatorname{otp}(Y)=\gamma$, the same
  conclusion holds for every coloring of $[Y]^2$, with subsets of $Y$ and
  copies inside $Y$; the proof of fact 1 of the lemma page carries over.
  Since only order isomorphisms are used, the facts (T2)--(T5) hold with
  ordinals replaced by arbitrary linear order types, the relation for an
  order type being read on any representative.
- **S2 (T2, restriction).** If $\gamma\to(\beta,H_1,\ldots,H_k)^2_{k+1}$
  and $\gamma'$ has a subset of order type $\gamma$ (for ordinals,
  $\gamma'\ge\gamma$), then $\gamma'\to(\beta,H_1,\ldots,H_k)^2_{k+1}$.
- **S3 (T2, weakening).** Three monotonicity clauses, each from a fixed
  relation $\gamma\to(\beta,H_1,\ldots,H_k)^2_{k+1}$: (a) if a set of order
  type $\beta$ has a subset of order type $\beta'$ (for ordinals,
  $\beta'\le\beta$), then $\gamma\to(\beta',H_1,\ldots,H_k)^2_{k+1}$; (b) a
  target $H_i$ may be replaced by any $H_i'$ that embeds in $H_i$; (c) a
  color may be left unused, so the relation with $k$ triangle targets
  implies the relation with $k-1$ triangle targets, and in particular
  $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$ implies $\alpha\to(\alpha,3)^2$.
- **S4 (T3).** If $\alpha\to(\alpha,H_i)^2$ for every $i=1,\ldots,k$, then
  $\alpha\to(\alpha,H_1,\ldots,H_k)^2_{k+1}$, with color $i$ carrying $H_i$.
- **S5 (T4, descent lemma).** Let $k\ge1$, let $\gamma_0,\ldots,\gamma_k$
  be ordinals (or order types, by S1) and $H_1,\ldots,H_k$ targets, and
  suppose $\gamma_{j-1}\to(\gamma_j,H_j)^2$ for every $j=1,\ldots,k$, each a
  two-color relation with the large target in color $0$ and $H_j$ in color
  $1$. Then $\gamma_0\to(\gamma_k,H_1,\ldots,H_k)^2_{k+1}$, with color $j$
  carrying $H_j$.
- **S6 (T5, witness extraction).** Let $k\ge1$ and let
  $c:[\alpha]^2\to\{0,\ldots,k\}$ have no subset of order type $\alpha$
  homogeneous in color $0$ and no triangle homogeneous in any color
  $j\ge1$. Then there are $Y\subseteq\alpha$ with
  $\operatorname{otp}(Y)=\alpha$ and $j\in\{1,\ldots,k\}$ such that the
  coloring $d_j$ of $[Y]^2$ with $d_j(p)=1$ when $c(p)=j$ and $d_j(p)=0$
  otherwise has no subset of $Y$ of order type $\alpha$ homogeneous in color
  $0$ and no triangle of color $1$; pulled back along an order isomorphism
  from $\alpha$ onto $Y$, $d_j$ witnesses $\alpha\not\to(\alpha,3)^2$.
- **S7 (equivalence).** For every order type $\alpha$ and every finite
  $k\ge1$: $\alpha\to(\alpha,3)^2$ if and only if
  $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$ with $k$ triangle targets. The
  section derives this from Lemma 2.1, (T2) and (T5).
- **S8 (consequence).** A witness for the negative relation with $k$
  triangle targets contains, on a subset of order type $\alpha$, a witness
  for $\alpha\not\to(\alpha,3)^2$ (this is S6), and adding finitely many
  triangle colors changes neither the positive nor the negative relation
  (this is S7 together with its negation).

## Checklist

- **Quantifiers and scope.** No defect. Every statement is for each finite
  $k\ge1$ and each order type separately; none claims the relation with
  infinitely many colors, a uniform bound, or an "almost all" reading. The
  existential quantifiers of S6 ($Y$ and $j$) are constructed by the proof,
  and S5's conclusion names which color carries which target. The scope of
  "everything below" in (T1) is verified for (T2)--(T5) only (F3).
- **Circularity.** No defect. S4 is derived from S5; S5 and S6 are proved by
  finite induction on $k$ whose base case is the hypothesis itself; S7 uses
  Lemma 2.1, a premise from another page, only for the direction that S6
  also proves; nothing assumes S7 or an equivalent of it.
- **Model and convention changes.** No defect in substance; one wording
  finding. The passage from ordinals to order types (S1) is stated with its
  bridge (order isomorphisms only) and is checked below for each of
  (T2)--(T5); graph targets are defined in the section, and the definition
  agrees with the lemma page's relation when every target is an order type.
  The word "pairs" for the edges of a graph copy admits a stronger
  misreading (F2).
- **Finite and statistical overreach.** Inapplicable: no finite case, sample
  or heuristic is used as evidence.
- **Uniformity.** No defect. No constants or bounds occur; the only
  parameter is $k$, every statement is proved for each $k$ by an induction
  that yields no limit statement, and the section claims none.
- **Extremal conclusions.** Inapplicable: no infimum, supremum, attained
  value or sharpness sentence occurs.
- **Consequences and composition.** No defect in substance; findings on
  attribution. The "so" and "gives" sentences (S3(c), S4 as the constant
  case of S5, S7 with S8) were checked separately and each follows. The
  consumed interfaces (fact 1 and fact 2 of the lemma page, Steps 2 and 3
  of the theorem page, the statement of Lemma 2.1) were confirmed on their
  pages at the subject commit. Lemma 2.1 as filed is for ordinals, so the
  forward direction of S7 over non-ordinal order types rests on (T3) or
  (T5), not on the citation as written (F3).
- **Computation.** Inapplicable: the section has no computation.
- **Reproduction.** Inapplicable: the section carries no rerun command or
  coverage claim.
- **Source and verdict fidelity.** No defect in substance; findings on
  provenance. "Fact 1 of the lemma page is stated for ordinal targets" and
  "The lemma page merges the colors $0$ and $1$ and renames the rest" match
  the lemma page; "Steps 2 and 3 of the theorem page" are the restriction
  and reading-back steps as described; the held source states Lemma 2.1 for
  an ordinal $\alpha$ (p. 2) and Remark 3.2 (p. 4) as the reconstruction
  page reports. The sentence placing (T1) and (T2) "on the reconstruction
  pages" overstates: those pages carry fact 1 and the restriction principle
  for ordinal targets only (F1). The attribution of (T3) to the folder index
  could not be checked (F5).

## Weakest steps

**W1: the induction step of (T4), where the last relation is applied on the
merged set.** Assume the lemma for chains of length $k$, let the $k+1$
relations hold, and fix $c:[\gamma_0]^2\to\{0,\ldots,k+1\}$. Put $c'(p)=0$
when $c(p)\in\{0,k+1\}$ and $c'(p)=c(p)$ otherwise. The first $k$ relations
form a chain of length $k$ from $\gamma_0$ to $\gamma_k$, so the lemma gives,
for $c'$, either a copy of some $H_j$ ($1\le j\le k$) in $c'$-color $j$,
which is in $c$-color $j$ because $c'=c$ off $\{0,k+1\}$, or a set
$Y\subseteq\gamma_0$ with $\operatorname{otp}(Y)=\gamma_k$ in the order of
$\gamma_0$ and $c[\,[Y]^2\,]\subseteq\{0,k+1\}$. In the second case let $d$ be
the coloring of $[Y]^2$ with $d(p)=0$ when $c(p)=0$ and $d(p)=1$ when
$c(p)=k+1$, a bijective relabeling (fact 2 of the lemma page). Fix an order
isomorphism $\pi$ from $\gamma_k$ onto $Y$ with the order inherited from
$\gamma_0$, and pull $d$ back to $d'$ on $[\gamma_k]^2$. The relation
$\gamma_k\to(\gamma_{k+1},H_{k+1})^2$ gives $X\subseteq\gamma_k$ of order
type $\gamma_{k+1}$ with $d'\equiv0$ on $[X]^2$, or a copy of $H_{k+1}$ in
$d'$-color $1$. Then $\pi[X]\subseteq Y\subseteq\gamma_0$ has order type
$\gamma_{k+1}$ in the order of $\gamma_0$, because $\pi$ is an order
isomorphism onto $Y$ in that order, and $c\equiv0$ on $[\pi[X]]^2$; and the
image of a copy of $H_{k+1}$ is a copy of $H_{k+1}$ (an order isomorphism is
a bijection) with every edge of $c$-color $k+1$. Both cases give the
conclusion for $k+1$ with color $j$ carrying $H_j$ for every $j\le k+1$. The
base case $k=1$ is the hypothesis itself. The step is sound; the point that
carries it is that $Y$'s order type and the isomorphism $\pi$ are both taken
in the order of $\gamma_0$.

**W2: the inductive case of (T5), where the two extracted colorings must
coincide.** Let $k\ge2$ and let $c$ be a witness. Put $c'(p)=0$ when
$c(p)\in\{0,k\}$ and $c'(p)=c(p)$ otherwise. Case A: $c'$ has
$Y\subseteq\alpha$ of order type $\alpha$ with $c'\equiv0$ on $[Y]^2$. Then
$c[\,[Y]^2\,]\subseteq\{0,k\}$, so $d_k$ on $[Y]^2$ has color $0$ exactly on the
pairs of $c$-color $0$ and color $1$ exactly on those of $c$-color $k$. A
subset of $Y$ of order type $\alpha$ homogeneous in $d_k$-color $0$ would be
homogeneous in $c$-color $0$, and a $d_k$-color-$1$ triangle would be a
$c$-color-$k$ triangle; $c$ has neither. Case B: otherwise $c'$ has no
subset of order type $\alpha$ homogeneous in color $0$, and a $c'$-triangle
in a color $j\in\{1,\ldots,k-1\}$ would be a $c$-triangle in color $j$, so
$c'$ is a witness with $k-1\ge1$ triangle targets. The induction hypothesis
gives $Y$ and $j\le k-1$ such that the coloring $d'_j$ built from $c'$
witnesses. For $1\le j\le k-1$ and any pair $p$, $c'(p)=j$ if and only if
$c(p)=j$, so $d'_j=d_j$ on $[Y]^2$. The base case $k=1$ takes $Y=\alpha$,
$j=1$ and $d_1=c$. The pull-back clause: if $\pi$ is an order isomorphism
from $\alpha$ onto $Y$ and $e(\{\xi,\eta\})=d_j(\{\pi\xi,\pi\eta\})$, then a
subset of $\alpha$ of order type $\alpha$ homogeneous in $e$-color $0$ maps
onto a subset of $Y$ of order type $\alpha$ homogeneous in $d_j$-color $0$,
and an $e$-color-$1$ triangle maps onto a $d_j$-color-$1$ triangle; neither
exists. The step is sound.

**W3: the equivalence over order types that are not ordinals.** The lemma
page states Lemma 2.1 for an ordinal $\alpha$, and the held source does the
same (p. 2). For a linear order type $\alpha$ that is not well ordered, the
forward direction of S7 is obtained inside the section twice over: as the
contrapositive of S6, since a witness for the $k$-color negative relation
yields, after the pull-back of W2, a witness for $\alpha\not\to(\alpha,3)^2$;
and as (T3) at $H_1=\cdots=H_k=3$, the constant case of W1. Neither argument
uses that $\alpha$ is well ordered: the inductions are on $k$, the only sets
compared are subsets of one representative of $\alpha$ in its own order, and
order types of such subsets are transported by order isomorphisms. The
backward direction is S3(c): a coloring with the colors $0,1$ is a coloring
with the colors $0,\ldots,k$ in which $2,\ldots,k$ are unused, and a
triangle in an unused color cannot occur. Sanity checks at the small types:
for $\alpha=0$ and $\alpha=1$ both sides hold vacuously (the empty set and a
singleton are homogeneous); for $\alpha=2$ both sides fail (color the single
pair $1$); for $k=1$ the two sides coincide. The equivalence holds as
stated; only its attribution is imprecise (F3).

## Strongest attack

- **S1.** Attacked the transport of a graph target by asking whether an
  order isomorphism is needed at all: it is not, since a copy of a graph is
  carried by any bijection, and the order matters only for the order-type
  targets; the fact holds a fortiori. Attacked the order-type extension by
  looking for a hidden use of well-foundedness in (T2)--(T5): none (no
  induction on $\alpha$, no least element, no ordinal arithmetic). Attacked
  the definition by reading "all of whose pairs have color $i$" as all pairs
  of the copy's vertex set; under that reading a graph target is equivalent
  to the clique on its vertex set, and the two readings give different
  relations (witness in F2), so the wording matters, but the phrase "a
  subgraph isomorphic to $H_i$" fixes the edge reading. Refutation failed.
- **S2.** Attacked with a subset $Y$ of $\gamma'$ of order type $\gamma$
  that is not an initial segment, and with a graph copy found inside $Y$:
  the argument uses only the order inherited from $\gamma'$, which $Y$
  carries by definition, and a subgraph of the complete graph on $Y$ is a
  subgraph of the complete graph on $\gamma'$. For ordinals, $\gamma'$ has a
  subset of order type $\gamma$ if and only if $\gamma'\ge\gamma$, since a
  subset of an ordinal has order type at most that ordinal. Refutation
  failed.
- **S3.** (a) Attacked with $\beta'$ embeddable in $\beta$ but not an
  initial segment: the clause only needs a subset of order type $\beta'$.
  (b) Attacked with $H_i'$ a non-induced subgraph of $H_i$: the edges of
  $H_i'$ map to edges of $H_i$, so a copy of $H_i$ in color $i$ contains a
  copy of $H_i'$ in color $i$. (c) Attacked the unused-color clause with an
  edgeless target: for $E$ the one-vertex graph, $2\to(2,3,E)^2_3$ holds,
  because a single vertex is a copy of $E$ in color $2$ under every coloring
  of the one pair, while $2\not\to(2,3)^2$; so "a color may be left unused"
  is false for targets without a pair. The clause's stated conclusion
  concerns triangle targets, for which a copy in an unused color cannot
  exist; the section applies the clause to triangles only (F4). Refutation
  failed as stated.
- **S4.** Attacked whether the constant chain meets the hypotheses of S5:
  with $\gamma_0=\cdots=\gamma_k=\alpha$ the $j$-th relation is
  $\alpha\to(\alpha,H_j)^2$, exactly the hypothesis of S4, and the
  conclusion of S5 is that of S4. Refutation failed.
- **S5.** Attacked with a non-constant chain, checking which relation the
  step applies where: the induction hypothesis on the first $k$ relations
  returns a color-$0$ set of order type $\gamma_k$, and the $(k+1)$-st
  relation has $\gamma_k$ on its left, so the types match (W1). Attacked the
  merge order: merging $0$ with color $1$ instead would leave a color-$0$
  set of order type $\gamma_{k+1}$ on which the relation with $H_1$ would be
  needed from $\gamma_{k+1}$, which the chain does not supply; the proof
  merges $0$ with the last color, which the chain does supply, so the proof
  is unaffected and only the closing remark needs its scope (F6). Attacked
  the relabeling of $\{0,k+1\}$ to $\{0,1\}$: fact 2. Refutation failed.
- **S6.** Attacked with $k=2$ and a witness $c$ whose merged coloring $c'$
  has no color-$0$ set of order type $\alpha$: the proof returns $Y=\alpha$,
  $j=1$, and $d_1$ has color $0$ on the pairs of $c$-colors $0$ and $2$
  together; $d_1=c'$, and $c'$ was shown to be a witness, so $d_1$ is one.
  Attacked case A by asking whether $d_k$'s color-$0$ class could contain
  pairs of a color other than $0$: not on $[Y]^2$, where $c$ takes only the
  values $0$ and $k$. Attacked the pull-back clause: W2. Refutation failed.
- **S7.** Attacked the forward direction for a non-ordinal order type
  through the citation of Lemma 2.1, which the lemma page and the source
  state for ordinals only; the direction is supplied inside the section by
  (T5) and by (T3) (W3), so the equivalence holds as claimed and the
  attribution is the only defect (F3). Attacked the quantifier "for every
  order type" by asking whether the relation depends on the representative
  of the type: it does not, by transport. Checked the small types and $k=1$
  (W3). Refutation failed.
- **S8.** The first clause is S6 and the second is S7 read together with its
  negation; nothing is added. Refutation failed.

## Premises

- **Lemma 2.1 reconstruction page** at the subject commit, read in full.
  Interface used: the statement (an ordinal $\alpha$ with
  $\alpha\to(\alpha,3)^2$ satisfies $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$
  for every finite $k\ge1$); fact 1 (transport along an order isomorphism,
  ordinal targets); fact 2 (bijective relabeling of colors carries the list
  of targets). Standing: treated as established at the standing the
  commission states, an independent review as it stood on 2026-09-28T05:03:27Z
  with corrections applied since; the review itself was not read. The section
  uses the statement within its hypotheses for ordinals; for other order
  types see F3.
- **Theorem 3.1 reconstruction page** at the subject commit, read in full.
  Interface used: Steps 2 and 3 (restriction of a coloring of
  $[\omega_1^2]^2$ to $[\omega_1\omega]^2$ and reading the homogeneous set
  back in $\omega_1^2$) and the closing paragraph stating restriction for
  any $\alpha$ with a subset of order type $\beta$, ordinal targets. Same
  standing. S2 is re-proved here rather than imported.
- **Gao (2026)**, the held deposit, cited through the lemma page. Held; read
  by text extraction of all four pages and on the page images of pp. 2 and 4.
  Lemma 2.1 (p. 2) is stated for an ordinal $\alpha$ with the two-color
  hypothesis, and Remark 3.2 (p. 4) restates the lemma as stability of
  $\alpha\to(\alpha,3)^2$ under adding finitely many colors with target $3$.
  Standing per its library card: unrefereed deposit, proofs followed, no
  independent review.
- **Folder index**, cited for (T3). Excluded from the read set and not read;
  (T3) is verified as the constant case of (T4) (F5).
- **Problem statements.** Problem 1171 asks
  $\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ for all finite $k$;
  Problem 118 concerns a cardinal, ordinal or order type $\alpha$ with the
  two-color triangle relation. Used only to confirm that "the setting of
  Problem 118" is the order-type setting; for a cardinal read as its initial
  ordinal, a subset of full cardinality has full order type and conversely,
  so the readings agree there.

## Findings

- **F1 (suggested).** Location: "Five facts are used below. The first two
  are on the reconstruction pages, the third is stated on the folder index,
  and the last two are recorded here with their proofs." Defect: (T1) in its
  mixed-target form and three of the four clauses of (T2) are not on the
  reconstruction pages, which carry fact 1 and the restriction principle
  for ordinal targets only; the sentence invites a reader to extend the
  reviewed standing of those pages to extensions that are this page's own.
  Witness: fact 1 of the lemma page quantifies over ordinals
  $\beta_0,\ldots,\beta_{n-1}$, and the theorem page's closing paragraph
  states restriction for ordinal targets; neither page states weakening of
  the large target, replacement of a target by one that embeds in it, or the
  unused color. Replacement: "The first two extend facts on the
  reconstruction pages (fact 1 of the lemma page and the closing restriction
  paragraph of the theorem page, both for ordinal targets), the third is
  stated on the folder index, and the last two are recorded here with their
  proofs."
- **F2 (suggested).** Location: (T1), "a copy of $H_i$ all of whose pairs
  have color $i$, a copy being a subset of type $H_i$ when $H_i$ is an order
  type and a subgraph isomorphic to $H_i$ when $H_i$ is a graph". Defect:
  for a graph target, "pairs" can be read as all pairs of the copy's vertex
  set, under which a graph target is equivalent to the clique on its
  vertices; the two readings define different relations. Witness: with
  $P_3$ the path on three vertices, $5\to(3,P_3)^2$ holds under the edge
  reading, since if the color-$1$ edges contain no two adjacent edges they
  form a matching of at most two edges and the color-$0$ graph, a $K_5$
  minus a matching, contains a triangle; under the clique reading the
  relation is $5\to(3,3)^2$, which the two-coloring of $K_5$ by a
  pentagon and its complement refutes. Replacement: "a copy of $H_i$ in
  color $i$, a copy being a subset of type $H_i$ all of whose pairs have
  color $i$ when $H_i$ is an order type, and a subgraph isomorphic to $H_i$
  all of whose edges have color $i$ when $H_i$ is a graph".
- **F3 (suggested).** Location: (T1), "Only order isomorphisms are used, so
  everything below also holds with the ordinals replaced by arbitrary order
  types", and the closing sentence "Together with Lemma 2.1 and (T2), (T5)
  gives, for every order type $\alpha$ and every finite $k\ge1$". Defect:
  "everything below" is unbounded and is verified here for (T2)--(T5) only;
  and Lemma 2.1 as filed on the lemma page, and in the source, is for
  ordinals, so for a non-ordinal order type the forward direction of the
  equivalence rests on (T3) or on (T5) after transport, not on the citation
  as written. The equivalence itself holds (W3). Witness: the lemma page's
  Statement begins "Let $\alpha$ be an ordinal". Replacement: scope the
  first sentence to "(T2)--(T5) below", and write the closing sentence as
  "By (T2) in one direction and (T5) after transport in the other (Lemma 2.1
  when $\alpha$ is an ordinal), for every order type $\alpha$ and every
  finite $k\ge1$".
- **F4 (note).** Location: (T2), "a color may be left unused, so a relation
  with fewer triangle colors is weaker". The general clause needs the
  dropped target to have a pair (an order type of at least two elements, or
  a graph with an edge); with an edgeless target the copy exists vacuously
  and the clause fails, as the witness under S3 shows. As stated the
  conclusion concerns triangle targets and holds. If the clause is ever
  applied to a general target, add "whose target has a pair".
- **F5 (note).** Location: (T3), "This is the observation recorded on the
  folder index". The folder index is outside the read set, so the match
  between the index's wording and (T3) is unchecked here; (T3) is verified
  as the constant case of (T4), and the lemma page's Checks and scope
  confirm that the index states a generalization to distinct fixed targets.
- **F6 (note).** Location: end of the proof of (T4), "merging $0$ with the
  last color is the same induction with the colors relabeled". This holds
  for the constant chain of the lemma page. For a non-constant chain the
  merge order is forced: with $k=2$, relations
  $\gamma_0\to(\gamma_1,H_1)^2$ and $\gamma_1\to(\gamma_2,H_2)^2$, merging
  $0$ with color $1$ would produce a color-$0$ set of order type $\gamma_2$
  on which a relation from $\gamma_2$ with target $H_1$ would be needed, and
  the chain supplies none. The proof merges with the last color and is
  unaffected; the remark should say it concerns the constant case.

## Verdict

- S0: not a mathematical claim; provenance sentence corrected by F1.
- S1 (T1, definition and transport): refutation-failed.
- S2 (T2, restriction): refutation-failed.
- S3 (T2, weakening, clauses (a)--(c)): refutation-failed.
- S4 (T3, the induction with general targets): refutation-failed.
- S5 (T4, descent lemma): refutation-failed.
- S6 (T5, witness extraction): refutation-failed.
- S7 (the equivalence for every order type and every finite $k\ge1$):
  refutation-failed.
- S8 (the closing consequence sentence): refutation-failed.

Limitations. The folder index was not read, so (T3)'s attribution to it is
verified only through the mathematics. The reconstruction pages were taken
at the standing the commission states, without reading their reviews. The
uses of (T1)--(T5) in the other sections of the page were not reviewed here
beyond the keyword scan that located them; in particular the graph-target
definition was checked for internal consistency and for agreement with the
lemma page's relation, not against the literature's convention for the
problems that later sections target. No required correction was found; the
three suggested corrections concern provenance and wording, and the three
notes record scope provisos. This focused review assigns no tier and changes
no status.
