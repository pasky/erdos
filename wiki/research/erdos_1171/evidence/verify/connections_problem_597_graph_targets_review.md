---
name: research/erdos_1171/evidence/verify/connections_problem_597_graph_targets_review
title: "Independent review of the connections section: Problem 597: graph targets"
desc: |
  Refutation review of the section "Problem 597: graph targets" and of the
  lead "graph targets under Martin's axiom" as they stood on
  2026-09-28T13:50:48Z. Of the thirteen author-recorded statements, twelve are
  refutation-failed at their stated hypotheses and one conditional deduction,
  the negative outcome of the infinite-graph investigation, is proof
  defective; statement unresolved. One required correction, three suggested,
  three notes.
created: 2026-09-28T18:58:49Z
updated: 2026-09-28T20:42:19Z
---

***

## Subject and independence

**Role.** The reviewer worked in a fresh context from the commissioning
assignment alone, took no part in writing the section, the lead, the Tools
section or the reconstruction pages, and had no contact with their author or
with the reviewers of the other sections. The charge was refutation. No tier
is assigned and no status changes.

**Subject.** The source as it stood on 2026-09-28T13:50:48Z (called "the
commit" below). The section
"## Problem 597: graph targets" of `wiki/research/erdos_1171/connections.md`,
lines 318--409 (the H2 at line 318 up to the line before the next H2 at line
410), and the lead page
`wiki/research/leads/graph_targets_under_martin_axiom/_index.md`, read
whole. Line numbers below refer to these two files at this commit.

**Reading and depth.**

- The section, every sentence, with each deduction re-derived.
- The page's Tools section (lines 32--124) as input: the interfaces of
  (T1), (T2), (T3) and (T4) were confirmed at each use, and the proof of
  (T4) was re-derived because (T3), which the section uses, is stated as
  its constant case. (T5) is not used by the section and was not checked.
- The reconstruction pages `lemma_2_1_reconstruction.md` and
  `theorem_3_1_reconstruction.md` (premises), read whole, checked for the
  hypotheses under which the section uses them.
- The statement blocks of the problem pages `E0597`, `E1171` and `E0924`.
- Library material where a source theorem is invoked: the cards and result
  pages of Baumgartner (1989), Baumgartner and Hajnal (1987), Folkman
  (1970), Chen, Garti and Weinert (2018), Gao (2026) and Komjáth (2025);
  the held PDFs of Chen, Garti and Weinert (p. 5 page image and text layer,
  and the first page for its identity), Folkman (printed p. 19 text layer,
  printed p. 20 page image) and Komjáth (printed pp. 425--426 and 442--443
  page images).
- `docs/verification.md` (Whole-claim report, Audit checklist, Grading and
  claim standing), `docs/approach_vetting.md`, `docs/evidence.md` (Source
  fidelity) and `docs/math_authoring.md`.

**Exposures.** (1) The three problem pages have no separate Statement
heading; the block read for each ran from its H1 to its "Current
assessment" heading and so included the page's Status line and Source
paragraph. For `E1171` that paragraph quotes the catalog's status wording
and mentions a discussion thread and a proof-claim tab; for `E0924` the
Status paragraph is where the Nešetřil--Rödl theorem is recorded, and it
was read for that record. (2) A heading listing showed that `E0597` carries
"Current assessment", "Progress" and "Known Results" sections; their
contents were not read. (3) A search for the quoted sentences ran over the
whole connections page and returned four one-line fragments of other
sections (lines 218, 287, 452 and 542); nothing else of those sections was
read. (4) The library cards were read whole, including their read-status
and standing lines. (5) A working-tree status listing showed the file
names of parallel reviews of other sections and folders; none was opened.
Nothing under any `evidence/` folder, no folder `_index.md`, no existing
review or grade, and no web content was read; the catalog page for Problem
597 was not consulted, so the section's three catalog attributions are
recorded here as unverified.

## Restatement

Conventions (S1, not a claim). Ordinals are von Neumann ordinals;
$[X]^2$ is the set of two-element subsets. For an ordinal $\gamma$, an
ordinal $\beta$ and targets $H_1,\ldots,H_k$, each an order type or a graph,
$\gamma\to(\beta,H_1,\ldots,H_k)^2_{k+1}$ means: every
$c:[\gamma]^2\to\{0,\ldots,k\}$ has $X\subseteq\gamma$ with
$\operatorname{otp}(X)=\beta$ and $c\equiv0$ on $[X]^2$, or for some $i$ a
copy of $H_i$ in color $i$, a copy being a subset of type $H_i$ for an order
type and, for a graph, an injection of the vertices of $H_i$ into $\gamma$
under which every edge of $H_i$ goes to a pair of color $i$ (subgraph
copies, not induced). For $k=1$ and a graph $G$ this says: every graph on
$\gamma$ has an independent set of type $\beta$ or contains $G$ as a
subgraph. (Q1) asks whether $\omega_1^2\to(\omega_1\omega,G)^2$ for every
graph $G$ on at most $\aleph_1$ vertices with no $K_4$ and no
$K_{\aleph_0,\aleph_0}$ subgraph; (Q2) asks the same for finite $G$, for
which the $K_{\aleph_0,\aleph_0}$ exclusion is vacuous. The problem page
carries status `open`. Two conventions bear on everything below: a finite
$n$-element set homogeneous in color $1$ is the same object as a copy of
$K_n$ in color $1$, and a positive relation on an ordinal $\gamma$ transfers
to every ordinal $\gamma'\ge\gamma$ by restriction of the coloring (T2),
while a negative relation transfers only downward.

- **S2.** Assume $\mathrm{MA}_{\aleph_1}$ and the imported theorem that
  $\omega_1\omega\to(\omega_1\omega,n)^2$ for every finite $n$. Then for
  every finite graph $G$, $\omega_1\omega\to(\omega_1\omega,G)^2$.
- **S3.** Under the same hypotheses, for every finite graph $G$,
  $\omega_1^2\to(\omega_1\omega,G)^2$. Hence in every model of
  $\mathrm{MA}_{\aleph_1}$ the answer to (Q2) is yes for every finite $G$,
  $K_4$-free or not; with the relative consistency of
  $\mathrm{MA}_{\aleph_1}$ (Theorem C), ZFC does not refute (Q2). The
  color-merging lemma is not used.
- **S4.** Under the same hypotheses, for every finite $k\ge1$ and finite
  graphs $G_1,\ldots,G_k$,
  $\omega_1^2\to(\omega_1\omega,G_1,\ldots,G_k)^2_{k+1}$, with color $i$
  carrying $G_i$; once by (T3) at $\alpha=\omega_1\omega$ followed by
  restriction, and once from the imported theorem at $n$ equal to the
  multicolor Ramsey number of the cliques on the $G_i$, followed by the
  finite Ramsey theorem and restriction.
- **S5.** Under any hypothesis that gives
  $\omega_1\omega\to(\omega_1\omega,G_i)^2$ for $i=1,\ldots,k$, with the
  $G_i$ graphs of any size,
  $\omega_1^2\to(\omega_1\omega,G_1,\ldots,G_k)^2_{k+1}$; the finite Ramsey
  bridge of S4 does not give this when some $G_i$ is infinite.
- **S6 (obstruction).** The mechanism of the folder, Lemma 2.1 with its
  general form (T4) and the transfers (T2), does not produce the two-color
  relation $\omega_1^2\to(\omega_1\omega,G)^2$ from any input weaker than
  that relation: (T4) with one link is its own hypothesis, and any relation
  $\gamma\to(\beta,G)^2$ with $\gamma\le\omega_1^2$ and
  $\beta\ge\omega_1\omega$ that (T2) could feed in already implies the
  target.
- **S7.** For every finite $k\ge1$ there is a finite $K_4$-free graph $F_k$
  such that every coloring of its edges with $k$ colors has a monochromatic
  triangle: for $k=2$ by Folkman's Theorem 1, for every $k$ by the theorem
  of Nešetřil and Rödl.
- **S8.** For every finite $k\ge1$ and every such $F_k$: if
  $\omega_1^2\to(\omega_1\omega,F_k)^2$, then
  $\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ with $k$ triangle
  targets. Consequently, if ZFC proves (Q2) at every $F_k$, ZFC proves the
  relation of Problem 1171 for every $k$; every model of
  $\omega_1^2\not\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ is a model in
  which (Q2) fails at the $K_4$-free finite graph $F_k$; and (Q2) at $F_3$
  implies the case $k=3$ of Problem 1171.
- **S9.** In the converse direction, the relation of Problem 1171 yields a
  two-color relation $\omega_1^2\to(\omega_1\omega,G)^2$ only for graphs
  $G$ that are subgraphs of a triangle. (Read as: by leaving colors unused
  and weakening the target under (T2); see F4 for the stronger reading.)
- **S10.** In any model, a positive answer to (Q1) implies that every graph
  on $\omega_1^2$ with no independent set of type $\omega_1\omega$ contains
  every admissible $G$ as a subgraph; the negative relation
  $\omega_1^2\not\to(\omega_1\omega,K_{\aleph_0,\aleph_0})^2$ attributed to
  Baumgartner (hypothesis unrecorded) is exactly the failure of that
  condition at $K_{\aleph_0,\aleph_0}$.
- **S11.** The route of S2--S3 reaches (Q1) only for those infinite
  admissible $G$ with $\omega_1\omega\to(\omega_1\omega,G)^2$ under
  $\mathrm{MA}_{\aleph_1}$; the imported theorem is stated for finite $n$
  only, and nothing held in the corpus decides any infinite case.
- **S12.** Investigation (ii) of the section and step 2 of the lead. (a) If
  $\mathrm{MA}_{\aleph_1}$ gives $\omega_1\omega\to(\omega_1\omega,G)^2$
  for an admissible $G$, then (Q1) at $G$ is not disprovable in ZFC. (b) If
  the extension fails for some admissible $G$, "a counterexample $G$ under
  $\mathrm{MA}_{\aleph_1}$", then (Q1) has no positive answer in ZFC and
  $G$ is a third necessary exclusion.
- **S13.** Investigation (iii) of the section and step 3 of the lead. A
  positive answer to (Q2) at $F_3$ settles the case $k=3$ of Problem 1171;
  a consistent negative answer to that case "refutes (Q2) at $F_3$".
- **S14 (provenance and standing sentences, not mathematics).** The
  imported theorem is taken "from the zbMATH review and one refereed
  restatement"; the lead reads copies as subgraph copies, "the convention
  of the lemma page and of Komjáth's survey"; the lead cites a CH
  obstruction recorded in the first section of the connections page, which
  is outside this review's read set and is not assessed here.

## Checklist

- **Quantifiers and scope.** S2--S8 carry their quantifiers correctly: the
  universal over finite $G$ in S3 holds in one model at a time, so "not
  disprovable" is the right modality; S8 is stated per $k$ with any choice
  of $F_k$. One defect: S12(b) moves from a failure on the initial segment
  $\omega_1\omega$ to a conclusion about $\omega_1^2$, a change of the
  ordinal in the relation with no bridge (F1).
- **Circularity.** None. S6 observes that (T4) at one link is the target
  itself; that is an obstruction statement, not a circular use.
- **Model and convention changes.** The subgraph reading of copies is
  declared and used consistently in S2, S8 and S10. Two silent
  identifications are harmless but should be explicit: the ordinal target
  $n$ read as the graph $K_n$ in S2, and (T1)'s "all of whose pairs" read
  as "all of whose edges" for graph targets (F6). The lead misattributes
  the convention to the lemma reconstruction page (F5).
- **Finite and statistical overreach.** None. The finite Ramsey theorem and
  the existence of $F_k$ are used for their exact finite content.
- **Uniformity.** The Ramsey number in S4 depends on $G_1,\ldots,G_k$ and
  the graph $F_k$ depends on $k$; both dependences are stated. No constant
  is claimed uniform.
- **Extremal conclusions.** "At least as strong" in S8 is an implication
  and holds. "Only for subgraphs of a triangle" in S9 is exact for the
  weakening route but, read as an independence statement, is unsupported
  (F4).
- **Consequences and composition.** Every "hence" was checked separately.
  S3 inherits the unproved premise (the imported theorem at full strength)
  and says so; S12(b) does not follow from its hypothesis (F1); S13's
  "refutes" overstates a consistency conclusion (F2).
- **Computation.** Inapplicable: no computation is used or claimed.
- **Reproduction.** Inapplicable: no rerun command or coverage claim.
- **Source and verdict fidelity.** The restatement of the imported theorem
  was checked on the page image of Chen, Garti and Weinert (p. 5): it reads
  that ZFC with $\mathrm{MA}_{\aleph_1}$ implies
  $\omega_1\omega\to(\omega_1\omega,n)^2$ for all natural numbers $n$, as
  the section says. Folkman's Theorem 1 and the editor's footnote were
  checked on the page images. Komjáth's record of the Baumgartner--Hajnal
  relations and of the Nešetřil--Rödl theorem was checked on the page
  images. The word "refereed" for the restatement is not supported by the
  held artifact, an arXiv preprint, or by its library card (F3).

## Weakest steps

**W1 (S2--S3): from the ordinal target $n$ to a graph target, and up to
$\omega_1^2$.** Let $G$ be a finite graph with vertex set of size $n$; if
$n=0$ or $n=1$ the copy is trivial, so let $n\ge2$. Let
$c:[\omega_1\omega]^2\to\{0,1\}$. The imported theorem gives
$X\subseteq\omega_1\omega$ of type $\omega_1\omega$ with $c\equiv0$ on
$[X]^2$, or an $n$-element $Y$ with $c\equiv1$ on $[Y]^2$. In the second
case any bijection from the vertices of $G$ onto $Y$ sends every edge of
$G$ to a pair of color $1$, so it is a copy of $G$ in color $1$; non-edges
of $G$ impose no condition under the subgraph reading. This is S2. Now let
$c:[\omega_1^2]^2\to\{0,1\}$. Since $\omega_1\omega<\omega_1^2$, the
ordinal $\omega_1\omega$ is the set of ordinals below it, a subset of
$\omega_1^2$, and $c\upharpoonright[\omega_1\omega]^2$ is a two-coloring to
which S2 applies. A set $X\subseteq\omega_1\omega$ of type $\omega_1\omega$
has the same order as a subset of $\omega_1^2$ (membership in both), so its
type is unchanged, and a copy of $G$ inside $\omega_1\omega$ is a copy
inside $\omega_1^2$ with the same colors. This is S3; nothing beyond
$\omega_1\omega\subseteq\omega_1^2$ is used. The consistency step is
Theorem C: a model of $\mathrm{MA}_{\aleph_1}$ satisfies (Q2) for every
finite $G$ simultaneously, so ZFC, if consistent, cannot prove the
negation of (Q2). Composition: S3 is conditional on the imported theorem
at full strength; if only $n=3$ were available, S2 would cover exactly the
subgraphs of a triangle, as the lead's provisional premise says.

**W2 (S8): the Folkman merge.** Fix $k\ge1$ and $F_k$ as in S7, and assume
$\omega_1^2\to(\omega_1\omega,F_k)^2$. Let
$c:[\omega_1^2]^2\to\{0,\ldots,k\}$ and put $c'(p)=0$ if $c(p)=0$ and
$c'(p)=1$ otherwise. The assumed relation applied to $c'$ gives either
$X$ of type $\omega_1\omega$ with $c'\equiv0$, hence $c\equiv0$, on
$[X]^2$, which is the color-$0$ alternative of the target relation; or an
injection $\varphi$ of the vertices of $F_k$ into $\omega_1^2$ sending each
edge $e$ to a pair $\varphi(e)$ with $c(\varphi(e))\in\{1,\ldots,k\}$. Then
$e\mapsto c(\varphi(e))$ is a $k$-coloring of the edges of $F_k$, so some
triangle $\{u,v,w\}$ of $F_k$ has its three edges of one color $j\ge1$;
the three points $\varphi(u),\varphi(v),\varphi(w)$ are distinct and all
three pairs among them have $c$-color $j$, a triangle of color $j$. The
merge never uses that $F_k$ is $K_4$-free; that property only places $F_k$
inside the class (Q2) asks about, which is what the consequences need. The
contrapositive gives the model statement, and $k=3$ gives the last clause.

**W3 (S4--S5): (T4) with graph targets, re-derived.** Let
$\gamma_{j-1}\to(\gamma_j,H_j)^2$ for $j=1,\ldots,k$, with the $H_j$
arbitrary graphs or order types. Claim:
$\gamma_0\to(\gamma_k,H_1,\ldots,H_k)^2_{k+1}$. For $k=1$ this is the
hypothesis. For the step, let $c$ use the colors $0,\ldots,k+1$ and let
$c'$ send $k+1$ to $0$ and fix the other colors. The case $k$ gives a copy
of some $H_j$ ($j\le k$) in $c'$-color $j$, which is $c$-color $j$ since
$c'=c$ off $\{0,k+1\}$; or $Y\subseteq\gamma_0$ of type $\gamma_k$ with
$c[\,[Y]^2\,]\subseteq\{0,k+1\}$. In the latter case transport
$\gamma_k\to(\gamma_{k+1},H_{k+1})^2$ to $Y$ along the order isomorphism
$\pi:\gamma_k\to Y$ (pull the coloring back, take the homogeneous set or
copy in $\gamma_k$, push it forward; $\pi$ is injective, preserves order and
carries pairs to pairs, so types and copies are preserved) and apply it to
the two-coloring of $[Y]^2$ in which $k+1$ is read as $1$. The result is a
subset of $Y$ of type $\gamma_{k+1}$ of $c$-color $0$ or a copy of
$H_{k+1}$ of $c$-color $k+1$. No property of the targets is used, so the
constant case (T3) holds for graphs of any size, and with
$\alpha=\omega_1\omega$ and the restriction of W1 it gives S4 and S5. The
Ramsey alternative in S4: with $n_i$ the number of vertices of $G_i$ and
$n=R(n_1,\ldots,n_k)$, merge colors $1,\ldots,k$, obtain an $n$-element set
in the merged color, split it back and find an $n_i$-clique of color $i$,
which contains a copy of $G_i$. For infinite $G_i$ no finite $n$ contains
a copy, so that bridge stops, as S5 says; the induction bridge does not.

## Strongest attack

- **S2, S3.** Attack 1: the direction of transfer. Positive relations
  restrict upward (W1); the attack would need a downward use, and there is
  none. Attack 2: the copy convention. Under induced copies S2 fails
  already for $G$ the graph on two vertices with no edge, since an
  $n$-element set of color $1$ contains no induced non-edge; the section
  and lead declare subgraph copies, which the problem's exclusion of
  $K_{\aleph_0,\aleph_0}$ as a subgraph also presupposes, so the attack
  hits a convention, not the argument. Attack 3: a finite $G$ with
  $\omega_1^2\not\to(\omega_1\omega,G)^2$ under $\mathrm{MA}_{\aleph_1}$.
  Impossible given the imported theorem, since $G\subseteq K_n$; the only
  exposure is the theorem's full strength, which the section discloses as
  a premise. Attack 4: the CH negative relation for $K_4$ against S3's
  "whether or not $G$ is $K_4$-free". No conflict: the two hold in
  different models, and the held restatement (Chen, Garti and Weinert,
  p. 5) draws the same conclusion, that the negative relation needs a
  hypothesis. The attacks failed.
- **S4, S5.** Attack: a hidden use of finiteness in (T3). The re-derivation
  W3 shows none. Attack on the Ramsey alternative: the multicolor Ramsey
  number must be taken for the cliques $K_{n_i}$, not for the $G_i$
  themselves, which is what the sentence says. Failed.
- **S6.** Attack: exhibit an input of the mechanism strictly weaker than
  (Q2) at $G$ that still yields it. Every input the tools accept is a
  two-color relation $\gamma\to(\beta,G)^2$ that (T2) turns into the target
  when $\gamma\le\omega_1^2$ and $\beta\ge\omega_1\omega$, and the induction
  only adds colors. Failed; the statement is modest and exact.
- **S7.** Checked against Folkman's Theorem 1 on the page image
  ($f(3,3)=3$, so a graph of clique number $3$, hence $K_4$-free, lies in
  $\Gamma(3,3)$) and against Komjáth's record of the Nešetřil--Rödl theorem
  (for $Y$ finite without $K_{k+1}$ and $r<\omega$, a finite $X$ omitting
  $K_{k+1}$ in which every $r$-coloring of the edges has a monochromatic
  induced copy of $Y$; take $Y=K_3$). The second is second-hand, as the
  section and Problem 924 say. Failed.
- **S8.** Attack: the monochromatic triangle of $F_k$ might not be a
  triangle of $\omega_1^2$ because non-edges of $F_k$ are uncolored. A
  triangle of $F_k$ consists of three edges, all of which are colored, so
  the image is a triangle in the ordinal (W2). Attack: the merged relation
  is the wrong instance of (Q2) because $F_k$ might contain
  $K_{\aleph_0,\aleph_0}$; it is finite. Failed.
- **S9.** Attack on the literal reading: the sentence "yields (Q2) only for
  subgraphs of a triangle" asserts, for every other $G$, that the relation
  of Problem 1171 does not give (Q2) at $G$. No argument is offered for
  that, and none is available here: it would need, for each such $G$, a
  model of the Problem 1171 relations in which (Q2) fails at $G$, and for
  $K_4$-free $G$ such as $C_4$ nothing held says whether ZFC proves (Q2)
  at $G$ outright. Under the route reading the statement is exact. The
  refutation of the literal reading is not a counterexample but the
  absence of any proof; filed as F4.
- **S10.** Attack: "necessary" hides a stronger claim. The condition is in
  fact equivalent to (Q1) in the model, by unfolding the relation, so
  "necessary" is true and weaker than what holds. The identification of
  the $K_{\aleph_0,\aleph_0}$ exclusion with a failure of the condition is
  exactly the imported negative relation, whose hypothesis the section
  correctly leaves open. Failed.
- **S11.** Attack: find a held result deciding an infinite case. None of
  the held or cited material states a relation
  $\omega_1\omega\to(\omega_1\omega,G)^2$ or
  $\omega_1^2\to(\omega_1\omega,G)^2$ for an infinite $G$. Failed as a
  statement about the corpus; see F7 for what the sentence must not be
  read as.
- **S12.** (a) holds by S3's argument: a positive relation on
  $\omega_1\omega$ restricts upward. (b) is where the attack succeeded.
  The hypothesis, read in the sentence's own context ("whether the proof
  of $\omega_1\omega\to(\omega_1\omega,n)^2$ extends"), is
  $\omega_1\omega\not\to(\omega_1\omega,G)^2$ in a model of
  $\mathrm{MA}_{\aleph_1}$; the conclusion needs
  $\omega_1^2\not\to(\omega_1\omega,G)^2$ in some model. A negative
  relation does not pass from $\omega_1\omega$ to $\omega_1^2$: the
  witness is $G=K_3$ under CH, where
  $\omega_1\omega\not\to(\omega_1\omega,3)^2$ (Erdős and Hajnal, as the
  theorem page and the Baumgartner card record from the review) while
  $\omega_1^2\to(\omega_1\omega,3)^2$ is a theorem of ZFC (the ZFC relation
  $\omega_1^2\to(\omega_1\omega,3,3)^2$ with one color unused; Komjáth
  p. 425 attributes the two-color instance to Erdős and Hajnal). The
  witness is not an instance of the sentence's exact hypothesis, which
  names $\mathrm{MA}_{\aleph_1}$, so the verdict is not a disproof of the
  conclusion but a missing bridge: proof defective; statement unresolved.
- **S13.** The first clause is S8 at $k=3$. The second: from a model of
  $\omega_1^2\not\to(\omega_1\omega,3,3,3)^2$, S8 gives a model in which
  (Q2) fails at $F_3$, hence that ZFC does not prove (Q2) at $F_3$. It does
  not give a ZFC disproof, which "refutes" suggests. Filed as F2; the
  intended consistency reading survives.

## Premises

- **Lemma 2.1 reconstruction** (`lemma_2_1_reconstruction.md`, premise at
  its reviewed standing, read whole). Interface: for an ordinal $\alpha$,
  $\alpha\to(\alpha,3)^2$ implies $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$
  for every finite $k\ge1$; its fact 1 (transport along an order
  isomorphism) and fact 2 (relabeling). The section uses it only through
  the Tools section and to say it is not needed for S3; its convention
  covers ordinal targets only.
- **Theorem 3.1 reconstruction** (`theorem_3_1_reconstruction.md`,
  premise, read whole). Interface used: Steps 2 and 3, the restriction of
  a coloring of $[\omega_1^2]^2$ to $[\omega_1\omega]^2$ and the reading
  of the result in $\omega_1^2$, with its general remark that a subset of
  the right type suffices; Theorem A (the imported theorem at $n=3$);
  Theorem C (relative consistency of $\mathrm{MA}_{\aleph_1}$); and its
  fidelity note that CH gives $\omega_1\omega\not\to(\omega_1\omega,3)^2$,
  used as the witness in F1.
- **Tools (T1)--(T4)** (`connections.md`, lines 38--93; proofs owned by
  another reviewer). Interfaces confirmed; (T4) re-derived in W3 with
  graph targets. (T1)'s phrase "all of whose pairs have color $i$" was
  read as "edges" for graph targets (F6).
- **Baumgartner (1989), main theorem.** Not held. Interface:
  $\mathrm{MA}_{\aleph_1}$ implies $\omega_1\omega\to(\omega_1\omega,n)^2$
  for every finite $n$, two colors, the large target in color $0$. Read
  through the card and result page (which cite the zbMATH review, not read
  here) and the introduction of Chen, Garti and Weinert, p. 5, page image.
  The card and the section call the restatement refereed; the held file is
  `arXiv:1801.00238v1`, and its own card records an arXiv preprint (F3).
- **Baumgartner and Hajnal (1987), negative relation.** Not held.
  Interface: CH gives $\omega_1^2\not\to(\omega_1\omega,4)^2$. Result page
  read; Komjáth pp. 425 and 442, page images.
- **Baumgartner and Hajnal (1987), positive relation.** Not held.
  Interface: $\omega_1^2\to(\omega_1\omega,3,3)^2$ in ZFC. Result page
  read; Komjáth pp. 425 and 442, page images. Used only for the witness in
  F1.
- **Erdős and Hajnal, CH negative relation.** Not held;
  $\omega_1\omega\not\to(\omega_1\omega,3)^2$ under CH, as reported on the
  theorem page, the Baumgartner card and its result page from the review.
  Used only for the witness in F1.
- **Folkman (1970), Theorem 1.** Held; $f(k_1,k_2)=\max(k_1,k_2)$ for
  $k_1,k_2\ge2$, with the definitions of p. 19 (finite graphs; $\Gamma$;
  the dimension $\delta$). Printed p. 20 page image and p. 19 text layer
  read; proof not read.
- **Nešetřil and Rödl (1976).** Not held. Interface as recorded on Problem
  924 and by Komjáth p. 442 (page image): for a finite $Y$ with no
  $K_{k+1}$ and $r<\omega$ there is a finite $X$ omitting $K_{k+1}$ such
  that every $r$-coloring of its edges has a monochromatic induced copy of
  $Y$. Second-hand at both places.
- **Solovay and Tennenbaum (1971).** Not held; Theorem C on the theorem
  page.
- **Problem statements** of `E0597`, `E1171` and `E0924` at this commit.
- **Catalog page for Problem 597.** Not read (web excluded); the section's
  attributions to it (the Erdős--Hajnal relation, the original $K_4$-free
  formulation, Baumgartner's $K_{\aleph_0,\aleph_0}$ relation) are
  unverified here; Komjáth p. 425 supports the first.
- **Explicit assumptions.** $\mathrm{MA}_{\aleph_1}$ for S2--S4; the
  imported theorem at full strength for S2--S4; subgraph copies throughout.

## Findings

- **F1 (required).** Location: section lines 394--399, "(ii) Under
  $\mathrm{MA}_{\aleph_1}$, whether the proof of
  $\omega_1\omega\to(\omega_1\omega,n)^2$ extends to countable, then
  $\aleph_1$-sized, $K_4$-free and $K_{\aleph_0,\aleph_0}$-free $G$: ... a
  negative outcome, a counterexample $G$ under $\mathrm{MA}_{\aleph_1}$,
  shows that (Q1) has no positive answer in ZFC and names a third
  necessary exclusion"; lead lines 135--140, "determine whether the proof
  for finite $n$ extends ... A negative outcome, a counterexample $G$ under
  $\mathrm{MA}_{\aleph_1}$, shows that (Q1) has no positive answer in ZFC
  and names a third necessary exclusion." Defect: the investigation is
  about the relation on $\omega_1\omega$, so its negative outcome is
  $\omega_1\omega\not\to(\omega_1\omega,G)^2$ in a model of
  $\mathrm{MA}_{\aleph_1}$; the conclusion needs
  $\omega_1^2\not\to(\omega_1\omega,G)^2$ in some model, and a negative
  relation does not transfer from the initial segment to $\omega_1^2$.
  Witness: under CH, $\omega_1\omega\not\to(\omega_1\omega,3)^2$ while
  $\omega_1^2\to(\omega_1\omega,3)^2$ holds in ZFC, so the same pattern of
  inference at $G=K_3$ from CH would conclude falsely that Problem 597 at
  $K_3$ has no positive ZFC answer. Replacement: "a negative outcome shows
  only that this route does not cover $G$; (Q1) has no positive answer in
  ZFC, and $G$ is a third necessary exclusion, if some model satisfies
  $\omega_1^2\not\to(\omega_1\omega,G)^2$ for an admissible $G$, which a
  failure on $\omega_1\omega$ does not give."
- **F2 (suggested).** Location: section lines 400--402, "a consistent
  negative answer for that case refutes (Q2) at $F_3$"; lead lines
  141--143, "a consistent negative answer to that case refutes (Q2) at
  $F_3$." Defect: the consequence proved (S8) is that (Q2) fails at $F_3$
  in every model of $\omega_1^2\not\to(\omega_1\omega,3,3,3)^2$, hence is
  not a theorem of ZFC; "refutes" reads as a ZFC disproof. Replacement:
  "shows that (Q2) at $F_3$ is not provable in ZFC."
- **F3 (suggested).** Location: section lines 336--338, "the statement is
  taken from the zbMATH review and one refereed restatement"; lead lines
  106--107, "rests on the review and one refereed restatement." Defect:
  the held restatement is the file `arXiv:1801.00238v1` of Chen, Garti and
  Weinert, dated 31 December 2017, which its library card records as an
  arXiv preprint; nothing held establishes that it was refereed, and the
  page's own scope rule cites sources at the standing their library pages
  record. The Baumgartner (1989) card is the origin of the word. Witness:
  the first page of the held PDF and the Chen, Garti and Weinert card.
  Replacement: "one held restatement (an arXiv preprint)", or record the
  publication data on that card first and cite it at that standing.
- **F4 (suggested).** Location: section lines 379--380, "The converse
  implication gives nothing: the relation of Problem 1171 yields (Q2) only
  for subgraphs of a triangle." Defect: read literally, "only for" claims
  that no other $G$ is reached, an independence statement with no
  argument; what is shown is that target weakening reaches exactly the
  subgraphs of a triangle. Replacement: "In the converse direction, target
  weakening gives (Q2) exactly for the subgraphs of a triangle; whether
  the relation of Problem 1171, or ZFC alone, gives (Q2) for any other
  $G$ is not addressed here."
- **F5 (note).** Location: lead lines 110--112, "the convention of the
  lemma page and of Komjáth's survey." Defect: the lemma reconstruction
  page defines the relation for ordinal targets only; the subgraph
  convention for graph targets is (T1) in the Tools section of the
  connections page. Komjáth's usage ($K_4\not\le X$ for subgraph
  containment, and the reformulation of the CH relation as a $K_4$-free
  graph on $\omega_1^2$ without an independent set of type
  $\omega_1\omega$) is consistent with it. Replacement: cite (T1) of the
  connections page in place of the lemma page.
- **F6 (note).** Location: Tools (T1), lines 42--43, "a copy of $H_i$ all
  of whose pairs have color $i$"; section lines 339--341, "$G$ embeds in
  $K_n$, so $\omega_1\omega\to(\omega_1\omega,G)^2$ by (T2)". Defect: for
  a graph target the pairs meant are the edges of the copy, as S8 and the
  lead's definition use it, and the (T2) step replaces the ordinal target
  $n$ by a graph, which (T2) states only for a target embedding in a
  target of the same kind. Both are harmless once the identification of an
  $n$-element homogeneous set with a copy of $K_n$ is written. Replacement:
  say "all of whose edges have color $i$" in (T1), and in the section "an
  $n$-element set homogeneous in color $1$ is a copy of $K_n$ in color
  $1$, which contains a copy of $G$".
- **F7 (note).** Location: section lines 384--385, "nothing held decides
  the infinite case." Not a defect: the sentence is true of the corpus.
  It should not be read as "nothing is known". The reviewer records, from
  memory and outside the held corpus, that the classical theorem of Erdős
  and Hajnal that a graph of uncountable chromatic number contains
  $K_{n,\aleph_1}$ for every finite $n$ would give ZFC instances of (Q1)
  at $G=K_{n,\aleph_1}$ (bipartite, hence $K_4$-free, and
  $K_{\aleph_0,\aleph_0}$-free): a graph on $\omega_1\omega$ that is a
  countable union of independent sets has an independent set of type
  $\omega_1\omega$, because each block of type $\omega_1$ meets some
  class in an uncountable set and one class serves infinitely many
  blocks, so a graph with no such independent set has uncountable
  chromatic number. This is offered for investigation (ii), is not part
  of the verdict, and needs the source before use.

## Verdict

- S1: not a claim (conventions).
- S2: refutation-failed, conditional on $\mathrm{MA}_{\aleph_1}$ and the
  imported theorem at full strength.
- S3: refutation-failed, under the same conditions; the consistency step
  rests on Theorem C.
- S4: refutation-failed, under the same conditions.
- S5: refutation-failed, under the hypothesis it names.
- S6: refutation-failed.
- S7: refutation-failed, resting on Folkman's Theorem 1 (held, statement
  checked on the page image) and the Nešetřil--Rödl theorem (second-hand).
- S8: refutation-failed.
- S9: refutation-failed under the route reading; the literal reading is
  not established (F4).
- S10: refutation-failed, with the imported negative relation's hypothesis
  left open as the section leaves it.
- S11: refutation-failed as a statement about the held corpus.
- S12(a): refutation-failed. S12(b): proof defective; statement
  unresolved (F1).
- S13: refutation-failed for the consistency reading; the word "refutes"
  overstates it (F2).
- S14: not a claim; F3 and F5 record the fidelity corrections, and the
  lead's reference to the first section's CH obstruction was not assessed.

Limitations: the chapter of Baumgartner (1989) and the paper of Nešetřil
and Rödl are not held, and the catalog page for Problem 597 was not
consulted, so the three catalog attributions in the section's first
paragraph and the full-strength statement of the imported theorem are
taken at the standing their library pages record. The first section of the
connections page, which the lead cites for a CH obstruction, is outside
this review's read set. This focused review assigns no tier and changes no
status.
