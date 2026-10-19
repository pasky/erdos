---
name: research/erdos_1171/evidence/verify/connections_problems_1174_595_and_596_countably_many_colors_review
title: "Independent review of the connections section: Problems 1174, 595 and 596: countably many colors"
desc: |
  Refutation review of the countably-many-colors section: the cardinality
  obstruction and its consequences for Problems 1174 and 595 survive; the
  sentence extending the coloring to every relation on the page is refuted,
  and the reach claim for the finite side of Problem 596 is supported only
  for two colors. Two required corrections, one suggested, three notes.
created: 2026-09-28T19:08:24Z
updated: 2026-09-28T19:08:24Z
---

***

## Subject and independence

Role: independent reviewer in a fresh context, given only the assignment,
with no part in writing the reviewed page or its folder. Charge: refutation
of the author-recorded mathematics of one section.

Subject: path `wiki/research/erdos_1171/connections.md` as it stood on
2026-09-28T13:50:48Z, section "Problems 1174, 595 and
596: countably many colors", lines 549–595 (the heading to the last line
before the next H2 heading at line 597). Lead pages: none; the section
closes with "no lead".

Read, at full depth: the section; the page's frontmatter, scope paragraph
and Tools section (lines 1–124), as inputs whose proofs another reviewer
checks; the two reconstruction pages of the folder, as premises; the
Statement sections and frontmatter of
[[problems/set_theory/E1174/_index|Problem 1174]],
[[problems/set_theory/E0595/_index|Problem 595]] and
[[problems/set_theory/E0596/_index|Problem 596]] (the lines above their "Current
assessment" headings only); the library cards of
[[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth 2025]]
and
[[../library/set_theory/shelah_1989_consistency_positive_partition_theorems_graphs_models/_index|Shelah 1989]]
in full, since neither separates a provenance paragraph from its digest;
the held PDF of Komjáth 2025 at pp. 441–443 (page images) and its
bibliography entry [161]; the held PDF of Shelah 1989 at p. 188 (page
image), the statement of Lemma 5.1 only; and the named sections of
`docs/verification.md`, `docs/approach_vetting.md`, `docs/evidence.md` and
`docs/math_authoring.md`.

Exposures: the section's sentence "refutes the countable-color form of
every relation on this page" quantifies over the rest of the page, so to
test it the reviewer read the H2 heading list of the page, a listing of the
lines of other sections that display a partition relation, and the
"Target" paragraphs of the Problem 597 section (lines 318–330) and the
Problem 601 section (lines 620–640); no other section's argument, outcome or
review was read. The file names in the folder's `evidence/verify/` directory
were seen when this report was placed; no file there was opened. No Current
assessment, Known results, standing or acceptance text, no evidence-folder
content and no web source was read.

## Restatement

Colorings, homogeneous sets, order types and the relation
$\alpha\to(\beta_0,\ldots,\beta_{n-1})^2_n$ for finite $n$ are those of the
Lemma 2.1 page; graph targets follow (T1): a copy of a graph target is a
subgraph isomorphic to it whose edges carry the color. The section extends
the relation to $\aleph_0$ colors without a definition; the reading used
here, and the one its proof addresses, is that
$\alpha\to(\beta_0,\beta_1,\ldots)^2_{\aleph_0}$ holds when every
$c:[\alpha]^2\to\omega$ has some $i$ and a set of type $\beta_i$ homogeneous
in color $i$, and $(3)_{\aleph_0}$ abbreviates the constant list of triangle
targets in the colors $1,2,\ldots$.

- **S1 (targets).** Problem 1174 asks (a) for a $K_4$-free graph every edge
  coloring of which with countably many colors has a monochromatic $K_3$,
  and (b) for a $K_{\aleph_1}$-free graph every such coloring of which has a
  monochromatic $K_{\aleph_0}$; its recorded status is `not_disprovable`.
  Problem 595 (status `open`) asks for an infinite $K_4$-free graph that is
  not a union of countably many triangle-free graphs. Problem 596 (status
  `open`) asks for the pairs $(G_1,G_2)$ such that for every $n\ge1$ some
  $G_1$-free graph forces a monochromatic $G_2$ under every $n$-coloring of
  its edges, while every $G_1$-free graph has an $\aleph_0$-coloring with no
  monochromatic $G_2$.
- **S2.** Problem 595 is question (a) of Problem 1174 in other words: a
  graph is a countable union of triangle-free graphs exactly when some
  countable edge coloring of it has no monochromatic triangle.
- **S3.** Komjáth 2025, under Problem 53, records a consistency proof by
  Shelah for question (a), located by the corpus as Shelah 1989, Lemma 5.1,
  and records that existence in ZFC is open.
- **S4.** The pair $(K_4,K_3)$ of Problem 596 "is Problem 595": whether it
  belongs to the class of Problem 596 is the question of Problem 595.
- **S5 (description).** The color-reduction induction adds one color per
  step and has no limit step; for $\aleph_0$ colors the merging that drives
  a step leaves infinitely many colors on the set of full type, so nothing
  applies.
- **S6 (obstruction).** For every order type $\alpha$ with
  $2\le|\alpha|\le2^{\aleph_0}$, $\alpha\not\to(\alpha,(3)_{\aleph_0})^2$,
  witnessed as follows: fix an injection $\iota:\alpha\to2^\omega$, color
  $\{x,y\}$ by $1+n$ with $n$ the least position at which $\iota(x)$ and
  $\iota(y)$ differ, and leave color $0$ unused. This is the fact Komjáth
  states for Problems 51 and 52, that $K_{\mathfrak c}$ is a union of
  $\aleph_0$ bipartite graphs.
- **S7.** On $\omega_1^2$, on $\omega_1\omega$ and on every countable
  ordinal, the $\aleph_0$-color relation with triangle targets and the
  ordinal itself as the color-$0$ target fails.
- **S8.** No ordinal partition relation on these ordinals can supply the
  graph of Problem 1174 or of Problem 595, since such a graph has more than
  $2^{\aleph_0}$ vertices.
- **S9.** Shelah's consistent example has $2^\lambda$ vertices for a
  suitable $\lambda$.
- **S10.** The same coloring, with color $0$ unused, refutes the
  $\aleph_0$-color form of every relation on the page.
- **S11.** For Problem 596 the mechanism says only that the finite side of
  the pair $(K_4,K_3)$ is reachable from ordinal partition relations, as
  the argument Komjáth attributes to Hajnal shows for two colors, and that
  the countable side is not. The finite side of Problem 596 is "for every
  $n\ge1$"; S11a is the two-color instance, S11b the sentence read for every
  finite $n$, S11c the clause about the countable side.
- **S12 (outcome).** The transfer fails with the cardinality obstruction;
  no lead.

## Checklist

- **Quantifiers and scope.** Fails at S10, whose "every relation on this
  page" covers bipartite targets and cardinals above the continuum that the
  coloring does not touch (F1); fails at S11b, where an instance proved for
  two colors is stated for every finite number of colors (F2); a boundary
  slip at S7, where the ordinals $0$ and $1$ satisfy the relation vacuously
  and are excluded only by the display's hypothesis $|\alpha|\ge2$ (F3). S6
  states its hypotheses exactly.
- **Circularity.** None. The obstruction is an explicit coloring; nothing
  assumes a target relation.
- **Model and convention changes.** The $\aleph_0$-color relation is used
  without a definition (F6); the natural reading above is the one the
  witness refutes. Graph targets are read under (T1)'s subgraph convention,
  which the Problem 601 section confirms ("as a subgraph"); the "all of
  whose pairs" wording of (T1) is not read as "all pairs of vertices". The
  passage from ordinals to arbitrary order types in S6 is legitimate: the
  witness uses only the underlying set.
- **Finite and statistical overreach.** S11b extends a two-color instance
  to every finite $n$ without a bridge; the held source records the
  three-color bridge as unknown (F2). No other finite-to-infinite step.
- **Uniformity.** Not applicable beyond S6, where the witness depends on
  $\alpha$ only through an injection that exists for every $\alpha$ with
  $|\alpha|\le2^{\aleph_0}$; no constants or limits are exchanged.
- **Extremal conclusions.** S8's bound "more than $2^{\aleph_0}$" is a lower
  bound derived in the claim's own units (vertex count); no sharpness or
  attainment is claimed, and none is implied.
- **Consequences and composition.** Each "so" sentence was attacked on its
  own: S7 (boundary only), S8 (holds), S10 (refuted), S11 (S11a holds, S11b
  unsupported, S11c holds under the readings given below). The interfaces
  of the imported facts were checked at each use (Premises).
- **Computation.** None in the section; not applicable.
- **Reproduction.** No rerun instructions or coverage claims; not
  applicable.
- **Source and verdict fidelity.** Komjáth 2025 pp. 441–443 and Shelah 1989
  p. 188 were checked against the page images: the Problem 53 record, the
  bipartite-union sentence, the two-color argument and the "unknown"
  sentence on p. 443 read as the section uses them. Two fidelity notes: the
  lemma number is the corpus's location, not the survey's (it cites [161]
  without a lemma number), and Lemma 5.1 carries a large-cardinal
  hypothesis the section does not mention (F4). No verifier is quoted.

## Weakest steps

**W1: the obstruction S6, re-derived.** Let $\alpha$ be a linearly ordered
set with $2\le|\alpha|\le2^{\aleph_0}$ and let $\iota:\alpha\to2^\omega$ be
injective. For distinct $x,y$ let $\Delta(x,y)$ be the least $n$ with
$\iota(x)(n)\ne\iota(y)(n)$, defined because $\iota$ is injective, and set
$c(\{x,y\})=1+\Delta(x,y)$. Color $0$ is not in the range of $c$, so a set
homogeneous in color $0$ has at most one element, and no such set has order
type $\alpha$ because $|\alpha|\ge2$. If $\{x,y,z\}$ were homogeneous in
color $1+n$, the three values $\iota(x)(n),\iota(y)(n),\iota(z)(n)$ would be
pairwise distinct elements of $\{0,1\}$, which is impossible. Hence $c$
witnesses $\alpha\not\to(\alpha,(3)_{\aleph_0})^2$, and in fact
$\alpha\not\to(2,(3)_{\aleph_0})^2$. More is true, and it is what Komjáth's
sentence says: for a binary string $s$ of length $n$ let $A_s^0$ and
$A_s^1$ be the sets of $x$ with $s0$, respectively $s1$, an initial segment
of $\iota(x)$; the class of color $1+n$ is the disjoint union over $s$ of
the complete bipartite graphs between $A_s^0$ and $A_s^1$. So every color
class is bipartite and contains no odd cycle. This stronger form is what
decides S10.

**W2: the cardinality consequence S8, re-derived.** Let $G$ be a graph with
at most $2^{\aleph_0}$ vertices. Order its vertex set arbitrarily and apply
W1 to it; the restriction of $c$ to the edges of $G$ is an edge coloring
with countably many colors and no monochromatic triangle, hence no
monochromatic $K_{\aleph_0}$. So a graph answering question (a) or (b) of
Problem 1174, or Problem 595, has more than $2^{\aleph_0}$ vertices. The
ordinals $\omega_1^2$, $\omega_1\omega$ and every countable ordinal have at
most $\aleph_1\le2^{\aleph_0}$ elements, so a graph carried by one of them,
in particular the graph of a color class of a witness for a negative
relation on it, has at most $2^{\aleph_0}$ vertices and cannot be that
graph. Graphs carried by the ordinal are the only graphs the section's
mechanism produces, so S8 holds as stated.

**W3: the reach sentences S10 and S11, re-derived.** Both are consequence
sentences with no proof in the section. S10 rests on W1 and would follow
if every target in the colors $\ge1$ on the page contained an odd cycle and
every ordinal on the page had at most $2^{\aleph_0}$ elements; neither is
the case (Strongest attack). S11 rests on the argument Komjáth attributes
to Hajnal (pp. 442–443): from $\alpha\to(\beta,(3)_n)^2$ and a witness for
$\alpha\not\to(\beta,4)^2$ whose color-$1$ graph $X$ is $K_4$-free with no
independent set of type $\beta$, every $n$-coloring of the edges of $X$,
extended by color $0$ off $X$, meets the positive relation, and a color-$0$
set of type $\beta$ would be independent in $X$, so some triangle of $X$ is
monochromatic. For $n=2$ the relations are Baumgartner–Hajnal's ZFC theorem
$\omega_1^2\to(\omega_1\omega,3,3)^2$ and the CH relation
$\omega_1^2\not\to(\omega_1\omega,4)^2$; compactness gives a finite
subgraph, and finite graphs are absolute, so the finite graph exists in
every model. For $n\ge3$ the two relations are needed in one model, and
the section supplies no such pair.

## Strongest attack

- **S1.** Compared clause by clause with the three Statement sections and
  frontmatter statuses. The paraphrase of Problem 596 says "$G_1$-free
  graphs force" where the catalog quantifies "for every $n$ there is a
  graph $H$"; the existential reading is the only one under which the
  finite side is a theorem for $(K_4,K_3)$, and the sentence admits it. No
  defect.
- **S2.** Attacked through the finite/infinite mismatch (Problem 595 says
  "infinite", Problem 1174 does not) and through "countably many" against
  "finitely many". If $G=\bigcup_n G_n$ with each $G_n$ triangle-free,
  coloring an edge by the least $n$ with the edge in $G_n$ is a countable
  coloring whose classes lie inside the $G_n$, so no triangle is
  monochromatic; conversely the classes of a countable coloring without
  monochromatic triangles are triangle-free graphs whose union is $G$. A
  finite graph is a finite union of single edges, so "infinite" excludes
  nothing, and a finite coloring is a countable one. The equivalence holds;
  the section states only the first direction as its reason (F5).
- **S3.** Komjáth p. 442: "Shelah proved the consistency of the existence
  of such a graph in [161]. The existence of a graph like this in ZFC is
  open." Entry [161] is the 1989 Lecture Notes 1401 paper the corpus holds.
  Its §5 (p. 188) opens with the question, and Lemma 5.1 gives, for
  $\mu<\lambda<\kappa$ with $\kappa$ measurable (or one of two weaker
  partition hypotheses the lemma names in its place) and
  $\lambda=\lambda^{<\lambda}$, a $\lambda^+$-c.c. $\lambda$-complete forcing
  of power $\kappa$ that forces $2^\lambda=\kappa$ and a graph $G$ of power
  $\kappa$ with $G\to(K_{k(*)})^2_\mu$ that embeds no $K_{k(*)+1}$; with
  $k(*)=3$ and $\mu=\aleph_0$ this is question (a). The attack that remains
  is the omitted large-cardinal hypothesis (F4); the record sentence itself
  is faithful.
- **S4.** For $(K_4,K_3)$ the finite side of Problem 596 is a theorem
  (Nešetřil–Rödl, as Komjáth records under Problem 54: for every $r$ a
  finite $K_4$-free graph forcing a monochromatic $K_3$ under $r$ colors),
  so $(K_4,K_3)$ is in the class of Problem 596 exactly when every
  $K_4$-free graph has an $\aleph_0$-coloring without a monochromatic
  triangle, that is, exactly when Problem 595 has a negative answer. The
  shorthand "is Problem 595" is correct with the direction understood;
  attack failed.
- **S5.** A description, not a claim; it matches the Lemma 2.1 page, whose
  induction step applies $P(k)$ once and then the two-color hypothesis on a
  set of full type.
- **S6.** Attacked at $|\alpha|=2^{\aleph_0}$ (the injection is a bijection;
  the triangle argument is unchanged), at $|\alpha|=\aleph_1$ without CH
  (the injection exists since $\aleph_1\le2^{\aleph_0}$ in ZFC), at
  $|\alpha|=2$ (one pair, colored $1+n$, no triangle, no color-$0$ pair),
  and by trying to place a triangle across two classes (a triangle
  homogeneous in one color is required). All failed; W1 is a complete
  proof. The identification with Komjáth's bipartite-union fact is exact
  (W1, last part).
- **S7.** Holds for $\omega_1^2$ and $\omega_1\omega$ (both of cardinality
  $\aleph_1\le2^{\aleph_0}$) and for every countable ordinal
  $\alpha\ge2$. Witness against the sentence as written: $\alpha=1$; the
  only coloring of $[1]^2=\emptyset$ is empty, and $\{0\}$ is a set of order
  type $1$ homogeneous in color $0$, so $1\to(1,(3)_{\aleph_0})^2$ holds;
  likewise $\alpha=0$. Boundary only (F3).
- **S8.** Attacked by asking whether a relation on these ordinals could
  produce a graph not carried by the ordinal itself; the mechanism's graphs
  are color classes on the ordinal, and any graph with at most
  $2^{\aleph_0}$ vertices fails by W2, whatever produced it. Attack failed.
- **S9.** Lemma 5.1, p. 188: $G$ has power $\kappa$ and the forcing forces
  $2^\lambda=\kappa$, so in the extension $G$ has $2^\lambda$ vertices, with
  $\lambda$ subject to the lemma's hypotheses. Attack failed.
- **S10.** Refuted. Witness 1 (bipartite targets). The page carries
  $\alpha\to(\alpha,P)^2$ with $P$ the one-way infinite path (Problem 601
  section) and $\omega_1^2\to(\omega_1\omega,G)^2$ for $G$ with no $K_4$ and
  no $K_{\aleph_0,\aleph_0}$ (Problem 597 section), which includes bipartite
  $G$ such as a path or a star. Let $\alpha$ be uncountable with
  $|\alpha|\le2^{\aleph_0}$ and $\iota:\alpha\to2^\omega$ any injection. Let
  $T$ be the set of binary strings $s$ that are initial segments of
  $\iota(x)$ for uncountably many $x$; the empty string is in $T$ and every
  member of $T$ has a child in $T$. If no $s\in T$ had both children
  extended by infinitely many $\iota(x)$, each $s\in T$ would have exactly
  one child in $T$ and the other child extended by finitely many
  $\iota(x)$; following the unique branch $b$ through $T$, every $x$ would
  have $\iota(x)=b$ or would leave $b$ into a finite set, making $\alpha$
  countable. So some $s\in T$, of length $n$ say, has $A_s^0$ and $A_s^1$
  both infinite, and the class of color $1+n$ contains the complete
  bipartite graph between them, a copy of $K_{\aleph_0,\aleph_0}$ with every
  edge of color $1+n$, which contains a one-way infinite path and every
  countable bipartite graph. So on $\omega_1$, $\omega_1\omega$ and
  $\omega_1^2$ the coloring has a monochromatic copy of $P$ and of every
  bipartite target of the Problem 597 section, and refutes none of their
  $\aleph_0$-color forms. For countable $\alpha=\{x_0,x_1,\ldots\}$ the
  injection $\iota(x_{2k})=0^{k+1}10^\omega$,
  $\iota(x_{2k+1})=1^{k+1}01^\omega$ makes the class of color $1$ a
  $K_{\aleph_0,\aleph_0}$, so the sentence, which fixes no injection, fails
  there too. Witness 2 (above the continuum). The page carries
  $\kappa\to(\kappa,\omega)^2$ for every infinite cardinal $\kappa$ and
  $\lambda\to(\lambda,\aleph_1)^2$ (Problem 1168 and Problem 1220 sections);
  for $\kappa>2^{\aleph_0}$ there is no injection into $2^\omega$, and at
  $\kappa=(2^{\aleph_0})^+$ the $\aleph_0$-color form holds outright,
  $(2^{\aleph_0})^+\to((2^{\aleph_0})^+,(\aleph_1)_{\aleph_0})^2$, the
  Erdős–Rado relation Komjáth displays on p. 442, so no coloring refutes it.
  Whether some other coloring refutes the $\aleph_0$-color forms in Witness
  1, or whether they hold, is not decided here and is not what the sentence
  claims.
- **S11.** S11a: the two-color argument is as in W3 and as Komjáth records
  it; attack failed. S11b: read for every finite $n$, the sentence has no
  support in the section for $n\ge3$, and Komjáth p. 443 records: "It is
  unknown if $\omega_1^2\to(\omega_1\omega,3,3,3)^2$ holds or at least if it
  is consistent that $\alpha\not\to(\beta,4)^2$ and
  $\alpha\to(\beta,3,3,3)^2$, for some ordinals $\alpha,\beta$", which is
  exactly the pair the route needs for three colors. The mechanism does not
  fill the gap: under $\mathrm{MA}_{\aleph_1}$ Theorem 3.1 gives the
  positive relation for every $n$, but Theorem A at the strength the
  Theorem 3.1 page reports, $\omega_1\omega\to(\omega_1\omega,4)^2$, with
  (T2) gives $\omega_1^2\to(\omega_1\omega,4)^2$, so the negative relation
  is unavailable in the same model. Proof defective for $n\ge3$; the
  statement is open there. S11c: read as "the mechanism yields nothing for
  $\aleph_0$ colors on the ordinals it handles", it follows from S6 and W2;
  read as "the countable side of Problem 596 for $(K_4,K_3)$ is not
  provable from ordinal relations", it also holds, since that side is the
  negation of Problem 595, which Shelah's lemma makes consistently false
  relative to its hypothesis. Attack failed under both readings.
- **S12.** Consistent with S6 and S8; the "no lead" outcome is an
  assessment, not a claim.

## Premises

- [[research/erdos_1171/lemma_2_1_reconstruction|Lemma 2.1 page]]:
  definitions of colorings, homogeneity, order type and the finite-color
  relation; the lemma
  $\alpha\to(\alpha,3)^2\Rightarrow\alpha\to(\alpha,(3)_k)^2_{k+1}$ for
  ordinals and finite $k$; facts 1 (transport) and 2 (relabeling). Premise
  at its reviewed standing; read in full. Used only for the conventions and
  for S5's description.
- [[research/erdos_1171/theorem_3_1_reconstruction|Theorem 3.1 page]]:
  under $\mathrm{MA}_{\aleph_1}$,
  $\omega_1^2\to(\omega_1\omega,(3)_k)^2_{k+1}$ for every finite $k$;
  Theorem A imported with its proof not held, cited for $n=3$ and reported
  at the strength "every finite $n$" from a review; the restriction
  principle of Step 2. Read in full. Used in the attack on S11b, with
  Theorem A at its reported strength flagged as such.
- Tools (T1), (T2) of the reviewed page: transport with mixed targets under
  the subgraph convention for graphs; restriction to a subset of the given
  type and weakening of targets. Interfaces confirmed at each use; proofs
  not re-checked (another reviewer's subject).
- Komjáth 2025 (held; card and pp. 441–443 at page-image depth; entry [161]
  in the bibliography): Problems 51–54, the sentence "no graph of
  cardinality $\le\mathfrak c$ may have those properties as
  $K_{\mathfrak c}$ is the union of $\aleph_0$ bipartite graphs", the
  Problem 53 record, the Erdős–Rado relation
  $(2^\kappa)^+\to((2^\kappa)^+,(\kappa^+)_\kappa)^2$, the two-color
  argument on pp. 442–443 and the "unknown" sentence on p. 443. A survey;
  cited at the standing its card records.
- Shelah 1989 (held; card and p. 188 at page-image depth): the statement of
  Lemma 5.1 only; its proof was not read.
- Problem pages E1174, E0595, E0596: Statement sections and frontmatter
  statuses, read in full above their assessment headings.
- Not held and not read: Baumgartner–Hajnal 1987 (Komjáth's [11]),
  Nešetřil–Rödl (Komjáth's [134], [135]), Folkman 1970 (Komjáth's [54]);
  each is used only as Komjáth records it.

## Findings

- **F1 (required).** Location: "The same coloring, with the color $0$
  unused, refutes the countable-color form of every relation on this
  page." Defect: the color classes of the coloring are bipartite (W1), so
  it refutes only relations whose targets in the colors $\ge1$ contain an
  odd cycle, and it exists only on sets of at most $2^{\aleph_0}$ elements.
  Witness: the infinite-path target of the Problem 601 section and the
  bipartite instances of the Problem 597 section (Strongest attack, S10,
  Witness 1); the cardinal relations of the Problem 1168 and Problem 1220
  sections at $\kappa=(2^{\aleph_0})^+$ (Witness 2). Replacement: "The same
  coloring, with the color $0$ unused, refutes the countable-color form of
  every relation on this page whose ordinal has at most $2^{\aleph_0}$
  elements and whose targets in the colors $\ge1$ each contain an odd cycle
  (a triangle, a larger clique, an ordinal $\ge3$, or any graph containing
  a triangle): its color classes are bipartite. It says nothing about the
  bipartite targets of Problems 597 and 601, and nothing above the
  continuum, where
  $(2^{\aleph_0})^+\to((2^{\aleph_0})^+,(\aleph_1)_{\aleph_0})^2$ holds
  (Erdős–Rado, Komjáth 2025, p. 442)."
- **F2 (required).** Location: "For Problem 596 the mechanism says only
  that the finite side of the pair $(K_4,K_3)$ is reachable from ordinal
  relations, as Hajnal's argument shows for two colors, and the countable
  side is not." Defect: the finite side of Problem 596 is "for every
  $n\ge1$"; the sentence's only support covers $n=2$, and for $n\ge3$ the
  held source records the needed pair of relations as unknown even up to
  consistency (Komjáth 2025, p. 443), while the mechanism cannot supply the
  pair (Strongest attack, S11b). Replacement: "For Problem 596 the
  mechanism adds nothing to what ordinal relations already give: the
  two-color finite side of the pair $(K_4,K_3)$ is reachable from them
  (Baumgartner–Hajnal's $\omega_1^2\to(\omega_1\omega,3,3)^2$ with the CH
  witness for $\omega_1^2\not\to(\omega_1\omega,4)^2$, compactness and
  absoluteness, Komjáth 2025, pp. 442–443); for three or more colors the
  route needs $\alpha\not\to(\beta,4)^2$ and $\alpha\to(\beta,3,3,3)^2$ in
  one model, which Komjáth (p. 443) records as unknown, and under
  $\mathrm{MA}_{\aleph_1}$, where Theorem 3.1 supplies the positive
  relation, the negative one fails; the countable side is out of reach by
  the cardinality obstruction."
- **F3 (note).** Location: "on every countable ordinal the countable-color
  relation with triangle targets fails outright". Defect: the ordinals $0$
  and $1$ satisfy the relation vacuously (Strongest attack, S7); the
  display's hypothesis $|\alpha|\ge2$ is dropped in the consequence.
  Replacement: "on every countable ordinal with at least two elements".
- **F4 (suggested).** Location: "Komjáth 2025 (Problem 53) records Shelah's
  consistency proof (Shelah 1989, Lemma 5.1)". Defect: Lemma 5.1 assumes a
  measurable cardinal $\kappa$ above $\lambda$, or one of two weaker
  partition hypotheses it names in its place; the consistency is relative
  to that hypothesis, which neither the survey's sentence nor the section
  states, and a reader passing from "consistent" to the problem page's
  `not_disprovable` needs it. Replacement: append "relative to a measurable
  cardinal, or the weaker partition hypothesis the lemma allows in its
  place".
- **F5 (note).** Location: "since a countable union of triangle-free graphs
  is a countable edge coloring without monochromatic triangles". Defect:
  "in other words" needs both directions; only one is given. Replacement:
  add "and the color classes of such a coloring are triangle-free graphs
  whose union is the graph".
- **F6 (note).** Location: the display
  $\alpha\not\to(\alpha,3,3,\ldots)^2_{\aleph_0}$. Defect: the relation with
  $\aleph_0$ colors is defined neither on the lemma page nor in the Tools
  section, which define finite lists only. Replacement: one sentence before
  the display: "with $\aleph_0$ colors the relation means that every
  $c:[\alpha]^2\to\omega$ has a set of type $\alpha$ homogeneous in color
  $0$ or a triangle homogeneous in some color $i\ge1$".

## Verdict

- S1: refutation-failed. S2: refutation-failed. S3: refutation-failed, with
  F4. S4: refutation-failed. S5: not a claim. S6: refutation-failed.
  S7: refuted-as-stated at the boundary $\alpha\in\{0,1\}$ only; correct
  for every other countable ordinal and for $\omega_1^2$ and
  $\omega_1\omega$. S8: refutation-failed. S9: refutation-failed.
  S10: refuted-as-stated (F1). S11a: refutation-failed. S11b: proof
  defective; statement unresolved (F2). S11c: refutation-failed.
  S12: an assessment consistent with S6 and S8.

Limitations: the proofs of the Tools facts and of the reconstruction pages
were taken as premises; Theorem A was used only at the strength the Theorem
3.1 page reports from a review, in the attack on S11b, and that attack also
stands on Komjáth's p. 443 alone; the proof of Shelah's Lemma 5.1 was not
read; whether the $\aleph_0$-color forms in F1's first witness are refuted
by some other coloring, or hold, was not decided. This focused review
assigns no tier and changes no status.
