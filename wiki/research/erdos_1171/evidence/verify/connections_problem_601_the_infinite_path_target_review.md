---
name: research/erdos_1171/evidence/verify/connections_problem_601_the_infinite_path_target_review
title: "Independent review of the connections section: Problem 601: the infinite-path target"
desc: |
  Refutation-failed for all six statements of the section: the target
  formulation, the finite-union transfer, its non-triviality witness, the
  no-bearing obstruction, the catalog and holding sentence, and the outcome.
  Zero required corrections; two notes.
created: 2026-09-28T18:57:48Z
updated: 2026-09-28T20:42:19Z
---

***

## Subject and independence

**Role.** The reviewer is an independent reviewer in a fresh context, given
only the assignment. The reviewer took no part in writing the connections
page, its Tools section, the reconstruction pages or the problem page, had
read none of them before this review, and holds no stake in the outcome. The
charge is refutation of the section's author-recorded mathematics.

**Subject.** Page `wiki/research/erdos_1171/connections.md` as it stood on
2026-09-28T13:50:48Z, section
"Problem 601: the infinite-path target", lines 620-639: the H2 heading at
line 620 through the Outcome paragraph at line 639, the next H2 heading being
at line 641. The section names no lead page and files no lead.

**Reading.** In full, unless a depth is stated:

- the section;
- the page's Scope paragraph and Tools section (lines 18-123), as inputs whose
  proofs are another reviewer's subject; the interfaces of (T1) and (T3) were
  confirmed at each use, and the proof of (T4) was re-derived for graph
  targets, since (T3) is stated as its constant case;
- [[research/erdos_1171/lemma_2_1_reconstruction|the Lemma 2.1 reconstruction]]
  and
  [[research/erdos_1171/theorem_3_1_reconstruction|the Theorem 3.1 reconstruction]],
  as premises at their reviewed standing; the section's inputs use only the
  Definitions and facts 1 and 2 of the lemma page;
- the statement block of [[problems/set_theory/E0601/_index|Problem 601]] (lines
  17-37 of the page: the statement, status, prize and tags, source,
  references and formalization lines) and nothing else of that page;
- the library tree (folder names only) and a file-name search for Larson and
  [La90], to check the words "not held"; and lines 824-836 of the held
  conversion of
  [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth (2025)]],
  that survey's only mention of an infinite path, to check the words "not in
  the corpus";
- the named guidance: `docs/verification.md` ("Whole-claim report", "Audit
  checklist", "Grading and claim standing"), `docs/approach_vetting.md`,
  `docs/evidence.md` ("Source fidelity") and `docs/math_authoring.md`.

**Exposures.** No excluded content reached the reviewer: no folder index, no
evidence folder, no review or grade, no assessment, known-results or standing
text, no web search. Two reads fall outside the items the assignment names and
are disclosed here. The page's Outcomes section (lines 678 to the end) was
read to check that its Problem 601 row agrees with the section; it lists the
author's summaries of the other sections and carries no review or standing
text. The Komjáth lines above were read although the section invokes no
theorem of that source.

## Restatement

**Conventions.** Ordinals are von Neumann ordinals and $[X]^2$ is the set of
two-element subsets of $X$ (lemma page, Definitions). A coloring of
$[\gamma]^2$ with the colors $0,\ldots,k$ is a function
$c:[\gamma]^2\to\{0,\ldots,k\}$. In the relation
$\gamma\to(\beta,H_1,\ldots,H_k)^2_{k+1}$ of (T1), a target $H_i$ that is a
graph is met by a *copy*: a graph with vertex set inside $\gamma$ and edge set
inside $[\gamma]^2$, isomorphic to $H_i$, all of whose edges have color $i$.
$P$ is the one-way infinite path: pairwise distinct vertices $v_0,v_1,\ldots$
with the edges $\{v_n,v_{n+1}\}$ for $n<\omega$. A graph *contains* a path
when the path is a subgraph, not necessarily induced. The subscript $k+1$ is
omitted for two colors.

- **S1 (target formulation).** Let $\alpha$ be an ordinal. The relation
  $\alpha\to(\alpha,P)^2$ says: every $c:[\alpha]^2\to\{0,1\}$ has a set
  $S\subseteq\alpha$ with $\operatorname{otp}(S)=\alpha$ and $c=0$ on
  $[S]^2$, or a copy of $P$ all of whose edges have color $1$. The section
  asserts that this relation holds exactly when every graph with vertex set
  $\alpha$ has an infinite path or an independent set whose vertex set has
  order type $\alpha$, the property the catalog asks about for limit ordinals
  $\alpha$, and that the catalog status is open.
- **S2 (finite-union transfer).** Let $\alpha$ be an ordinal with
  $\alpha\to(\alpha,P)^2$ and let $k$ be finite. For all graphs
  $X_1,\ldots,X_k$ with vertex set $\alpha$ such that no $X_i$ contains a
  one-way infinite path, the graph $X_1\cup\cdots\cup X_k$ (vertex set
  $\alpha$, edge set the union of the edge sets) has an independent set $S$
  with $\operatorname{otp}(S)=\alpha$. The section's proof: color a pair by
  the least $i$ with the pair in $X_i$, and by $0$ when there is none, and
  apply (T3) with $H_1=\cdots=H_k=P$.
- **S3 (non-triviality).** There are two graphs on an infinite ordinal, each
  containing no infinite path, whose union contains one; so S2 is not a
  restatement of the property.
- **S4 (obstruction).** S2 gives no information about which ordinals
  $\alpha$ satisfy $\alpha\to(\alpha,P)^2$, which is the whole question.
- **S5 (catalog and holding sentence).** On the catalog page Problem 601 is
  open; its reference [La90] is Larson's 1990 paper on Martin's axiom and
  ordinal graphs, which carries the Martin's-axiom side of the problem; that
  paper is not held, and that side of the problem is not in the corpus.
- **S6 (outcome).** The mechanism transfers to Problem 601 as S2, without
  bearing on the question; no lead.

## Checklist

- **Quantifiers and scope.** Pass. S2 quantifies over all ordinals $\alpha$
  with the property, all finite $k$ and all $k$-tuples of graphs; no
  almost-all, eventual or exceptional-set clause appears. The catalog's
  restriction to limit ordinals is carried in S1 and is not needed for S2.
  The one loose quantifier is "for every finite $k$", which includes $k=0$,
  an instance (T3) does not cover; it holds trivially (F1).
- **Circularity.** Pass. S2 takes the property as its hypothesis and says
  so; S4 refuses to draw any conclusion about which $\alpha$ have it. Nothing
  equivalent to the target is assumed and then presented as progress.
- **Model and convention changes.** Pass. The passage from graphs on
  $\alpha$ to two-colorings of $[\alpha]^2$ and back is re-derived under
  Weakest step 1, including the reading of "infinite path" and the subgraph
  reading of a copy. The passage from the ordinal $\alpha$ to a subset of
  type $\alpha$ is (T1) transport, re-derived for graph targets under
  Weakest step 2.
- **Finite and statistical overreach.** Inapplicable: no finite case,
  average or sample is used.
- **Uniformity.** Inapplicable: no constant or error term appears; the only
  parameter is $k$, and the number of colors, $k+1$, depends on it
  explicitly.
- **Extremal conclusions.** Inapplicable: no infimum, supremum or sharpness
  claim is made.
- **Consequences and composition.** Pass. The consumed clause is (T3) at the
  constant chain $\gamma_0=\cdots=\gamma_k=\alpha$ with graph targets; its
  hypotheses, $\alpha\to(\alpha,H_i)^2$ for each $i$ with $H_i$ a graph, are
  supplied by the property through S1. Each "so" was checked on its own: "a
  color-$i$ infinite path is a path of $X_i$" (the copy's edges have color
  $i$, so each lies in $X_i$); "independent in every $X_i$" (no pair of the
  color-$0$ set lies in any $X_i$); "the union of two graphs without infinite
  paths can contain one" (witness under S3).
- **Computation.** Inapplicable: none is used.
- **Reproduction.** Inapplicable: the section states no rerun instruction
  and no coverage claim.
- **Source and verdict fidelity.** Pass within the read set. The paraphrase
  of the problem matches the statement block in substance
  (limit ordinals; a graph with vertex set $\alpha$; an infinite path or an
  independent set on a set of vertices of order type $\alpha$). The status
  line reads "Open". The reference [La90] is Larson, Jean A., Martin's axiom
  and ordinal graphs: large independent sets or infinite paths, Ann. Pure
  Appl. Logic (1990), so "the Martin's-axiom side" matches the title. The
  library has no folder for it, and the held Komjáth survey lists the
  $\omega_1^\rho$ form of the question (its Problem 66) with no
  Martin's-axiom result, so "not held" and "not in the corpus" stand. What
  [La90] proves is not assessed, since the paper is not held.

## Weakest steps

**1. The bridge between graphs and colorings (S1).** For a graph
$G=(\alpha,E)$ put $c_G(p)=1$ if $p\in E$ and $c_G(p)=0$ otherwise; every
$c:[\alpha]^2\to\{0,1\}$ equals $c_G$ for exactly one $G$, namely
$E=c^{-1}(1)$. A set $S\subseteq\alpha$ of type $\alpha$ with $c_G=0$ on
$[S]^2$ is an independent set of $G$ whose vertex set has order type
$\alpha$, and conversely. A copy of $P$ all of whose edges have color $1$
under $c_G$ is a subgraph of $G$ isomorphic to $P$, that is, a one-way
infinite path in $G$, and conversely. It remains to match "has an infinite
path" with "has a one-way infinite path": a one-way infinite path is an
infinite path, and an infinite path, one-way or two-way, contains a one-way
infinite path (from any vertex, follow one direction). So
$\alpha\to(\alpha,P)^2$ holds exactly when every graph on $\alpha$ has an
infinite path or an independent set of order type $\alpha$. This bridge is
what lets the section apply tools stated for colorings to a problem stated
for graphs.

**2. (T3) with graph targets (S2).** Let $c:[\alpha]^2\to\{0,\ldots,k\}$ be
the section's coloring and $k\ge1$. Claim: $c$ has a set of type $\alpha$
homogeneous in color $0$ or, for some $j\in\{1,\ldots,k\}$, a copy of $P$
all of whose edges have color $j$. Induction on $k$. For $k=1$ this is
$\alpha\to(\alpha,P)^2$ read through the bridge. For $k\ge2$ let $c'$ be $c$
with the color $k$ merged into $0$, so $c'(p)=j\ge1$ exactly when $c(p)=j$.
The case $k-1$ gives either a copy of $P$ whose edges have $c'$-color
$j\le k-1$, hence $c$-color $j$, or a set $Y$ of type $\alpha$ with
$c(p)\in\{0,k\}$ for all $p\in[Y]^2$. In the second case let
$\pi:\alpha\to Y$ be the order isomorphism and color $[\alpha]^2$ by
$d(\{\xi,\eta\})=1$ if $c(\{\pi\xi,\pi\eta\})=k$ and $0$ otherwise. The
hypothesis gives $Z\subseteq\alpha$ of type $\alpha$ with $d=0$ on $[Z]^2$,
whence $\pi[Z]\subseteq Y$ has type $\alpha$ and $c=0$ on $[\pi[Z]]^2$; or a
copy of $P$ whose edges have $d$-color $1$, whose image under the bijection
$\pi$ is a copy of $P$ inside $Y$ whose edges have $c$-color $k$. This is the
claim, and it is (T4) at the constant chain with the last color merged. Now
a copy of $P$ whose edges have color $j\ge1$ has every edge in $X_j$, so
$X_j$ contains a one-way infinite path, which the hypothesis of S2 excludes;
hence the color-$0$ set $S$ of type $\alpha$ exists, and no pair of $S$ lies
in any $X_i$, so $S$ is independent in $X_1\cup\cdots\cup X_k$.

**3. The obstruction (S4).** For a fixed $\alpha$ write $U_k(\alpha)$ for
the conclusion of S2 at $k$. S2 says that the property implies $U_k(\alpha)$
for every $k\ge1$, and $U_1(\alpha)$ is the property itself: a single graph
without an infinite path has an independent set of type $\alpha$. So the
family of union statements is equivalent to the property, and what S2 says
about a given $\alpha$ never exceeds the property for that $\alpha$. The
section's sentence that the transfer "says nothing about which $\alpha$ have
the property" is therefore exact, and the transfer could only be combined
with independent knowledge of the property.

## Strongest attack

- **S1.** Three readings were tried against the bridge. Reading "infinite
  path" as a two-way infinite path changes nothing, since a two-way infinite
  path contains a one-way one and a one-way one is an infinite path. Reading
  it as an induced path would be a different problem; the catalog statement
  says "have an infinite path", the standard subgraph containment, (T1)
  defines a copy as a subgraph, and the section's words "as a subgraph" fix
  the reading it uses. Reading the (T1) phrase "all of whose pairs have color
  $i$" as all pairs of the copy's vertex set would turn the color-$1$
  alternative into an infinite clique and break the equivalence; (T1) defines
  a copy of a graph as a subgraph, so the pairs are its edges, and the
  section's step "a color-$i$ infinite path is a path of $X_i$" uses exactly
  that reading. The attack failed.
- **S2.** A counterexample was sought: an $\alpha$ with the property and
  graphs $X_1,X_2$ without infinite paths whose union has no independent set
  of type $\alpha$. Weakest step 2 shows none exists. The concrete attempt
  $\alpha=\omega$, which has the property by Ramsey's theorem (an infinite
  clique contains an infinite path), with the two matchings of S3 fails: the
  union, the path $0,1,2,\ldots$, has the even numbers as an independent set
  of type $\omega$. The step from a color-$j$ copy of $P$ to a path of $X_j$
  was checked against the "least $i$" rule: color $j$ means the pair lies in
  $X_j$ and in no $X_i$ with $i<j$, so the copy is a subgraph of $X_j$. The
  only gap found is the instance $k=0$, outside (T3) and trivially true
  (F1). The attack failed.
- **S3.** Witness, on any infinite ordinal $\alpha$: $X_1$ with the edges
  $\{2n,2n+1\}$ and $X_2$ with the edges $\{2n+1,2n+2\}$ for $n<\omega$, all
  other vertices isolated. Each has maximum degree $1$, so each of its paths
  has at most one edge; their union contains the one-way infinite path
  $0,1,2,\ldots$. The attack, that no such pair exists, failed.
- **S4.** It was asked whether S2 could yield information about a new
  ordinal, for instance by transferring the property from $\alpha$ to a
  larger ordinal or by producing a negative instance. Weakest step 3 shows
  the family of union statements is equivalent to the property, so any such
  derivation needs an input about the property itself. The obstruction
  claims only that this transfer says nothing about which $\alpha$ have the
  property; it does not claim that no other use of the mechanism exists, and
  it was not read as such. The attack failed.
- **S5.** Checked against the statement block: status "Open"; reference
  [La90] as quoted under Source and verdict fidelity; no library folder for
  the paper; the held Komjáth survey records the $\omega_1^\rho$ form of the
  question without a Martin's-axiom result. The attack, that the words
  misdescribe the page or the library, failed within the read set.
- **S6.** Not a mathematical claim; it is consistent with S2 and S4 and with
  the Problem 601 row of the page's Outcomes section.

## Premises

- **(T1) Transport**, Tools section of the page, held, read in full.
  Interface: the relation $\gamma\to(\beta,H_1,\ldots,H_k)^2_{k+1}$ with
  order-type and graph targets, copies of graphs being subgraphs, transported
  to any set of type $\gamma$ by an order isomorphism. Confirmed at its use
  inside (T3) for the graph target $P$; the transport of a copy of $P$ needs
  only a bijection.
- **(T2) Restriction and weakening**, Tools section: not used by the
  section.
- **(T3) The induction with general targets** and **(T4) Descent lemma**,
  Tools section, held, read in full; (T3) is the constant case
  $\gamma_0=\cdots=\gamma_k=\alpha$ of (T4), which assumes $k\ge1$.
  Interface: from $\alpha\to(\alpha,H_i)^2$ for $i=1,\ldots,k$ to
  $\alpha\to(\alpha,H_1,\ldots,H_k)^2_{k+1}$ with color $i$ carrying $H_i$.
  The proof of (T4) is another reviewer's subject; it was re-derived here for
  graph targets at the constant chain (Weakest step 2).
- **(T5) Witness extraction**, Tools section: not used by the section.
- [[research/erdos_1171/lemma_2_1_reconstruction|Lemma 2.1 reconstruction]],
  held, read in full, taken as established at its reviewed standing. Used
  through its Definitions (von Neumann ordinals, $[X]^2$, colorings,
  homogeneous sets, order types) and facts 1 (transport) and 2 (relabeling),
  on which (T1) and (T4) rest.
- [[research/erdos_1171/theorem_3_1_reconstruction|Theorem 3.1 reconstruction]],
  held, read in full, taken as established at its reviewed standing; not used
  by the section.
- [[problems/set_theory/E0601/_index|Problem 601]], statement block (lines 17-37)
  read; the statement, the status line and the reference [La90] are the
  facts consumed.
- **Larson (1990), [La90]**: not held; not read; only its bibliographic
  entry on the problem page was seen. Its content is not assessed.
- [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth (2025)]],
  held; lines 824-836 of the conversion read, to test the words "not in the
  corpus".
- No local claim card is consumed. No axiom beyond ZFC enters: S2 is a ZFC
  deduction from the property of $\alpha$. No batch acceptance order
  applies.

## Findings

- **F1 (note).** Location: line 628, "then for every finite $k$". Defect:
  (T3) is the constant case of (T4), which assumes $k\ge1$, so the cited tool
  does not cover the instance $k=0$. Witness: $k=0$, where the union of no
  graphs is the edgeless graph on $\alpha$ and $\alpha$ itself is an
  independent set of type $\alpha$, so the instance holds trivially and
  nothing false is asserted. Proposed replacement: "then for every finite
  $k\ge1$".
- **F2 (note).** Location: lines 634-635, "but it says nothing about which
  $\alpha$ have the property, which is the whole question". Defect: none;
  the sentence is exact but gives no reason. The reason is that the instance
  $k=1$ of the transfer is the property itself, so the family of union
  statements is equivalent to the property (Weakest step 3). Proposed
  addition after "property": "(the instance $k=1$ is the property itself, so
  the union statements are equivalent to it)".

## Verdict

- S1 (target formulation): refutation-failed.
- S2 (finite-union transfer): refutation-failed, with the instance $k=0$
  noted as trivially true and outside the cited tool (F1).
- S3 (non-triviality): refutation-failed; the witness is retained above.
- S4 (obstruction): refutation-failed; the transfer is equivalent to the
  property, so it decides no instance.
- S5 (catalog and holding sentence): refutation-failed within the read set.
- S6 (outcome): not a mathematical claim; consistent with S2 and S4.

**Limitations.** The paper [La90] is not held and was not read; the review
takes no position on what it proves beyond what its title and the section's
words say. The proofs of the Tools section are another reviewer's subject;
this review confirmed the interfaces the section uses and re-derived (T4) at
the constant chain for graph targets, not the general chain. The
reconstruction pages were taken as established at their reviewed standing.
No lead page exists for this section. Nothing in the section rests on a
computation or on a source theorem, so no computation was rerun and no source
PDF was consulted beyond the Komjáth lines named above.

This focused review assigns no tier and changes no status.
