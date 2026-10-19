---
name: research/erdos_1171/evidence/verify/connections_problems_582_and_924_finite_folkman_graphs_review
title: "Independent review of the connections section: Problems 582 and 924: finite Folkman graphs"
desc: |
  Seven statements: five refutation-failed, one not a claim, and the
  consequence clause "neither follow from" refuted-as-stated, since a
  positive ZFC answer to the open case of Problem 1171 implies the triangle
  case of the finite theorems by the section's own argument; one required
  correction, two suggested, three notes.
created: 2026-09-28T19:06:53Z
updated: 2026-09-28T19:06:53Z
---

***

## Subject and independence

The reviewer is an independent examiner in a fresh context who took no part
in writing the connections page, the reconstruction pages or any library
page they cite, and who read only the commissioned set listed here; no
review, grade, current assessment, known-results, standing or acceptance
text was opened.

Subject: page `wiki/research/erdos_1171/connections.md` as it stood on
2026-09-28T13:50:48Z, section
"## Problems 582 and 924: finite Folkman graphs", heading at line 641, body
lines 643--656, next H2 at line 658. Lead pages: none; the section files no
lead, and its outcome is "no lead".

Read, and at what depth:

- The section, clause by clause, with every deduction re-derived below. The
  page's frontmatter and Scope paragraph (lines 1--30) for the standing
  sentence and the witness convention, and the Tools section (lines
  32--123) for the interfaces of (T1) and (T2), used here as inputs whose
  proofs another reviewer checks. The passage "A ZFC instance and its finite
  corollary" of the countable-ordinals section (lines 465--488), which the
  section cites as the instance "above", read in full as an input, with the
  target and transfer paragraphs of that section (lines 410--464) read once
  for the notation the passage uses.
- [[research/erdos_1171/lemma_2_1_reconstruction|The Lemma 2.1 reconstruction]]
  and
  [[research/erdos_1171/theorem_3_1_reconstruction|the Theorem 3.1 reconstruction]]
  in full, as premises at the standing the assignment gives them.
- The statement regions of
  [[problems/ramsey_theory/E0582/_index|Problem 582]],
  [[problems/ramsey_theory/E0924/_index|Problem 924]] and
  [[problems/set_theory/E1171/_index|Problem 1171]], from each H1 to the line
  before "Current assessment".
- Library: the card of
  [[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth 2025]]
  and its held PDF at printed pp. 425--426 (Problem 13 commentary) and
  442--443 (Problems 53 and 54), read on the page images; the card and the
  result pages
  [[../library/set_theory/folkman_1970_graphs_monochromatic_complete_subgraphs_every_edge/theorem_1|Theorem 1]],
  [[../library/set_theory/folkman_1970_graphs_monochromatic_complete_subgraphs_every_edge/theorem_2|Theorem 2]]
  and
  [[../library/set_theory/folkman_1970_graphs_monochromatic_complete_subgraphs_every_edge/conjecture_p23|the Remarks]]
  of Folkman 1970, with its held PDF at printed pp. 20 and 23--24 on the
  page images; the card and
  [[../library/set_theory/baumgartner_1989_remarks_partition_ordinals/main_theorem|main theorem]]
  of Baumgartner 1989; the card, source record,
  [[../library/set_theory/baumgartner_1987_remark_partition_relations_infinite_ordinals/positive_relation|positive relation]]
  and
  [[../library/set_theory/baumgartner_1987_remark_partition_relations_infinite_ordinals/negative_relation|negative relation]]
  of Baumgartner and Hajnal 1987; the statement sections of Schipperus's
  [[../library/set_theory/schipperus_2010_countable_partition_ordinals/theorem_28|Theorem 28]]
  and
  [[../library/set_theory/schipperus_2010_countable_partition_ordinals/theorem_29|Theorem 29]];
  and printed p. 5 of the held paper of
  [[../library/set_theory/chen_2018_cardinal_characteristics_continuum_partitions/_index|Chen, Garti and Weinert]]
  (text layer) for its restatement of Baumgartner's theorem.
- The commissioned sections of `docs/verification.md` and
  `docs/evidence.md`, and the pages `docs/approach_vetting.md` and
  `docs/math_authoring.md`.

Exposures: (1) the problem pages carry no separate Statement heading, so
their statement regions were read whole, and each includes a Status
paragraph, a Source paragraph and a reference list; (2) a keyword search of
the connections page printed single lines from other sections, among them
summary lines of the Outcomes section (lines 682--704), none read further;
(3) a directory listing of `evidence/verify/` in the working tree showed the
names of other filed reviews and of a grade, none opened.

## Restatement

Conventions. $\gamma\to(\beta,H_1,\ldots,H_k)^2_{k+1}$ is the relation of
(T1); its negation is written with $\not\to$. A *witness* for a negative
relation is a coloring that refutes the positive relation. The *graph of a
two-coloring* $c$ of $[\gamma]^2$ is the graph on $\gamma$ whose edges are
the pairs of color $1$; a witness for $\gamma\not\to(\beta,4)^2$ is then the
same thing as a $K_4$-free graph on $\gamma$ with no independent set of order
type $\beta$, the equivalence the negative-relation page states. Finite
graphs are Folkman's: finite, undirected, simple. Three abbreviations are
used below: $R_k$ is $\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ with
$k$ triangle targets, the relation of Problem 1171; $N$ is
$\omega_1^2\not\to(\omega_1\omega,4)^2$; and $F_k$ is the statement "there
is a finite $K_4$-free graph every $k$-coloring of whose edges has a
monochromatic triangle", so that $F_2$ is the statement of Problem 582 and
$F_k$ is the case $l=3$ of Problem 924.

- **S1.** Problem 582 ($F_2$) is proved, by Folkman's Theorem 1 at
  $k_1=k_2=3$; Problem 924 (for every $k\ge2$ and $l\ge3$, a finite
  $K_{l+1}$-free graph every $k$-coloring of whose edges has a monochromatic
  $K_l$) is proved, by the theorem of Nešetřil and Rödl (1976).
- **S2.** (Hajnal's argument, as Komjáth reports it in the Problem 54
  discussion.) $F_2$ holds in ZFC, derived from four ingredients: the ZFC
  theorem $R_2$, that is $\omega_1^2\to(\omega_1\omega,3,3)^2$ (Baumgartner
  and Hajnal, relation 3 at $\kappa=\omega$); a witness for $N$ under CH
  (their relation 1 at $\kappa=\omega$); compactness for the two-color
  triangle property; and the absoluteness of finite graphs.
- **S3.** The analog $F_k$ obtained through Problem 1171, that is by the
  argument of S2 with $k$ colors, needs the ZFC relation $R_k$, which is open
  for every $k\ge3$, together with the CH witness for $N$ in the same model.
- **S4.** Under $\mathrm{MA}_{\aleph_1}$ the relation $R_k$ holds for every
  finite $k$, and no $K_4$-free graph on $\omega_1^2$ without an independent
  set of type $\omega_1\omega$ exists, because Baumgartner's theorem gives
  $\omega_1^2\to(\omega_1\omega,4)^2$ there.
- **S5.** (Consequence.) The finite theorems of S1 neither follow from nor
  feed the open case of Problem 1171, the case $k\ge3$ of $R_k$ in ZFC.
- **S6.** The only derivation of a Folkman-type finite graph from the page's
  material is the ZFC instance at $\alpha=\omega^{\omega^2}$: a finite
  $K_6$-free graph every $5$-coloring of whose edges has a monochromatic
  triangle, from $\alpha\to(\alpha,3)^2$ (Theorem 28),
  $\alpha\not\to(\alpha,6)^2$ (Theorem 29, part 1), Lemma 2.1 with $k=5$,
  and compactness; and the finite theorems of S1 give strictly more, namely
  clique number $3$ for every number of colors.
- **S7.** Outcome: nothing transfers in either direction; no lead is filed.

## Checklist

- **Quantifiers and scope.** Defect in S5: "follow from" is denied for the
  finite theorems as a whole, but their triangle case $F_k$ follows from a
  positive ZFC answer to $R_k$ by the section's own route (W1, F1). In S3
  the words "would need the ZFC relation" are read as naming the route's
  input, a positive answer to Problem 1171; a proof of $R_k$ from CH alone
  would serve as well, and is equally unknown (F2). In S6 "the only
  derivation" overlooks the second instance recorded in the cited passage
  (F5). Elsewhere the quantifiers are exact: "open for $k\ge3$" is uniform
  in $k$, since by (T2) a relation with more triangle colors implies the one
  with fewer, so $R_k$ for any $k\ge3$ would give $R_3$, which Komjáth
  records as unknown.
- **Circularity.** None. Nothing about Problem 1171 is assumed in order to
  conclude anything about Problem 1171, and the finite theorems enter only
  as known results.
- **Model and convention changes.** The passage between the graph form and
  the partition form of a witness is the equivalence of the negative-relation
  page, and the passage from an edge coloring to a coloring of all pairs is
  the extension by color $0$ on the non-edges, under which a color-$0$
  homogeneous set is an independent set of the graph; both are sound.
  Baumgartner's theorem is stated at $\omega_1\omega$ and used at
  $\omega_1^2$ through the restriction (T2), a bridge the section does not
  name (F4). Pass.
- **Finite and statistical overreach.** The passage from the infinite graph
  to a finite subgraph is by compactness, which the section names; no finite
  case is used as a universal proof. Pass.
- **Uniformity.** The only parameter is the finite $k$, every claim is made
  for each $k$ separately, and the monotonicity in $k$ is (T2). Pass.
- **Extremal conclusions.** "Which the finite theorems exceed" compares
  clique numbers, the claim's own unit: a graph forcing a monochromatic
  triangle contains a triangle, so clique number $3$ is least possible; the
  theorem of Nešetřil and Rödl attains $3$ for every $k$, while the instance
  gives at most $5$ for $k=5$. Folkman's own printed inequality gives
  $f(3,3,3,3,3)\le5$, equal to the instance and not below it, so the
  exceeding rests on the theorem that is not held (F6). Pass with a note.
- **Consequences and composition.** S5 is a consequence sentence that does
  not follow from S3 and S4, and its first clause is false as an implication
  for the triangle case (F1). The composition in S2 inherits the standing of
  Baumgartner and Hajnal's relations, which are not held, and omits the
  forcing of CH from its list of ingredients (F3). Defect.
- **Computation.** Inapplicable: the section computes nothing. The one
  arithmetic fact this review uses, Folkman's bound at five classes, is
  $3+\min(\tfrac12\cdot4,\,3)=5$, computed by hand from the printed
  inequality.
- **Reproduction.** Inapplicable: the section states no rerun commands and
  no coverage claims.
- **Source and verdict fidelity.** Komjáth's Problem 54 discussion, read on
  the page images: the attribution to Hajnal matches ("Hajnal was very proud
  of this argument all his life"); the ingredients are as the section lists
  them, plus the forcing of CH, which the source states in so many words and
  the section omits (F3); the graph derived is a graph with the property of
  Problem 582, not Folkman's construction and not Theorem 1 at general
  $(k_1,k_2)$ (F3). The theorem of Nešetřil and Rödl is cited without the
  qualification that the problem page carries, that its text is not held
  and its statement is quoted second-hand (F6). Baumgartner's theorem at
  $n=4$ was checked against the result page and the held restatement of
  Chen, Garti and Weinert (printed p. 5: Martin's axiom for $\aleph_1$ dense
  sets implies $\omega_1\omega\to(\omega_1\omega,n)^2$ for all natural
  numbers $n$). No verdict of another report is characterized. Minor
  infidelities; no strengthening.

## Weakest steps

**W1. Hajnal's argument, with $k$ colors.** This is S2 at $k=2$ and the
route of S3 for general $k$; it is also the witness for F1. Let $k\ge1$ and
suppose $R_k$ is a theorem of ZFC. Let $V$ be any model of ZFC. Force with
countable conditions to add a subset of $\omega_1$ (or to collapse the
continuum to $\omega_1$): the forcing is $\sigma$-closed, so it adds no
reals, preserves $\omega_1$, and forces CH; Komjáth states the fact used,
"CH can be added by forcing". In the extension $V[G]$, CH holds, so relation
1 of Baumgartner and Hajnal at $\kappa=\omega$ (which needs $\omega$ regular
and $2^\omega=\omega_1$) gives a coloring $c:[\omega_1^2]^2\to\{0,1\}$ with
no color-$0$ set of type $\omega_1\omega$ and no color-$1$ four-element set.
Let $X$ be the graph of $c$: $X$ is $K_4$-free and has no independent set of
type $\omega_1\omega$. Let $d$ be any coloring of the edges of $X$ with the
colors $1,\ldots,k$, and let $e(p)=0$ when $c(p)=0$ and $e(p)=d(p)$
otherwise. Since $R_k$ is a theorem of ZFC it holds in $V[G]$, and applied
to $e$ it gives either a set $Y$ of type $\omega_1\omega$ with $e$ constantly
$0$ on $[Y]^2$, which is an independent set of $X$ and is excluded, or a
three-element set $T$ with $e$ constantly $j$ on $[T]^2$ for some
$j\in\{1,\ldots,k\}$, a triangle of $X$ monochromatic under $d$. So every
$k$-coloring of the edges of $X$ has a monochromatic triangle. Compactness:
if every finite induced subgraph of $X$ had a $k$-coloring of its edges with
no monochromatic triangle, then, since "no monochromatic triangle" is a
family of constraints each involving the three edges of one triangle, the
compactness theorem of propositional logic (equivalently, the compactness of
the product space $\{1,\ldots,k\}^{E(X)}$) would give such a coloring of all
of $X$; hence some finite induced subgraph $Y$ of $X$ has every $k$-coloring
of its edges with a monochromatic triangle, and $Y$ is $K_4$-free as a
subgraph of $X$. Absoluteness: up to isomorphism $Y$ is a graph on a natural
number, a hereditarily finite object, and $V$ and $V[G]$ have the same
hereditarily finite sets; the property "$K_4$-free, and every $k$-coloring of
the edges has a monochromatic triangle" quantifies only over finite objects
built from $Y$, so it is absolute between $V[G]$ and $V$. Hence $V$
satisfies $F_k$. As $V$ was arbitrary, ZFC proves $F_k$. At $k=2$, $R_2$ is
the ZFC theorem of Baumgartner and Hajnal, and this is Hajnal's argument as
Komjáth reports it, with the forcing of CH as the step the section's list
omits (F3). At $k\ge3$ the derivation is the implication "$R_k$ in ZFC
implies $F_k$", which is exactly what the first clause of S5 denies (F1).

**W2. The $\mathrm{MA}_{\aleph_1}$ obstruction (S4).** Assume
$\mathrm{MA}_{\aleph_1}$. Baumgartner's theorem, as the result page and the
held restatement give it, is $\omega_1\omega\to(\omega_1\omega,n)^2$ for
every finite $n$; take $n=4$. Let $X$ be a $K_4$-free graph on $\omega_1^2$,
the graph of a two-coloring $c$. The ordinal $\omega_1\omega$ is an initial
segment of $\omega_1^2$ carrying the inherited order, so the restriction
$c_0$ of $c$ to $[\omega_1\omega]^2$ is a two-coloring of the pairs of
$\omega_1\omega$, and the relation gives a color-$0$ set $Y$ of type
$\omega_1\omega$ or a color-$1$ four-element set; the latter is a $K_4$ in
$X$ and is excluded. The set $Y$ has type $\omega_1\omega$ as a subset of
$\omega_1^2$ too, and $c$ agrees with $c_0$ on $[Y]^2$, so $Y$ is an
independent set of $X$ of type $\omega_1\omega$. This is the restriction
step (T2), the same step as Steps 2 and 3 of the Theorem 3.1 page. Hence
$\omega_1^2\to(\omega_1\omega,4)^2$ under $\mathrm{MA}_{\aleph_1}$ and no
witness for $N$ exists there. The obstruction composes with W1 as follows:
W1 needs one model in which both $R_k$ and a witness for $N$ are available
and which is reached from an arbitrary ground model by forcing; under
$\mathrm{MA}_{\aleph_1}$ the relation is available and the witness is not;
under CH the witness is available and $R_k$ for $k\ge3$ is not known,
Komjáth recording as unknown even whether some ordinals $\alpha,\beta$ have
$\alpha\not\to(\beta,4)^2$ together with $\alpha\to(\beta,3,3,3)^2$
consistently; and in ZFC $R_3$ is open. So the route of S3 cannot be run
today for any $k\ge3$.

**W3. The instance at $\omega^{\omega^2}$ and the comparison (S6).** Let
$\alpha=\omega^{\omega^2}$; $\beta=2=\omega^0+\omega^0$ is a sum of two
indecomposables, so Theorem 28 gives $\alpha\to(\alpha,3)^2$ and Theorem 29,
part 1, gives $\alpha\not\to(\alpha,6)^2$, both in ZFC. Lemma 2.1 at this
$\alpha$ with $k=5$ gives $\alpha\to(\alpha,3,3,3,3,3)^2_6$. Let $c$ witness
$\alpha\not\to(\alpha,6)^2$ and let $X$ be its graph: $X$ is $K_6$-free with
no independent set of type $\alpha$. For a $5$-coloring $d$ of the edges of
$X$, extend by $0$ on the non-edges; the six-color relation gives a color-$0$
set of type $\alpha$, independent in $X$ and excluded, or a triangle of $X$
monochromatic under $d$. Compactness, as in W1, gives a finite induced
$K_6$-free subgraph with the five-color triangle property, and no forcing is
needed since every ingredient is a theorem of ZFC. The comparison: the
theorem of Nešetřil and Rödl, not held, gives clique number $3$ for every
number of colors, which exceeds this. Folkman's printed inequality, "a
straightforward generalization of the proof of Theorem 1" with no proof
printed, gives for five classes with every $k_i=3$ the bound
$f(3,3,3,3,3)\le3+\min(\tfrac12\cdot4,\,3)=5$, a $K_6$-free graph, the same
as the instance; and for four classes it gives $3+\min(\tfrac32,\,2)$, so
$f(3,3,3,3)\le4$, a $K_5$-free graph, the same as the instance the cited
passage records from Larson's sharpening, which is not held. So the held
finite text matches the instances without exceeding them, and "exceed" is
true through the theorem that is not held (F6).

## Strongest attack

- **S1.** Attack: check that the filed theorems prove the catalog
  statements. Folkman's Theorem 1 at $(3,3)$ says $f(3,3)=3$, so some graph
  of clique number $3$, hence $K_4$-free, lies in $\Gamma(3,3)$, which is the
  statement of Problem 582 word for word. For Problem 924 the quoted theorem
  (a graph $H$ with $H\to(G)_c$ and $\omega(H)=\omega(G)$, taken at $G=K_l$)
  is the statement, but the paper is not held and the problem page quotes it
  second-hand, so "proved" is asserted at the problem page's standing, which
  the section does not carry (F6). The attack fails.
- **S2.** Attacks: whether $R_2$ applies to a coloring of the edges only
  (it does, after the extension by color $0$, whose color-$0$ homogeneous
  sets are independent sets); whether compactness applies (the property is
  a family of finitary constraints); whether the finite graph and its
  property pass to the ground model (hereditarily finite objects and a
  bounded property); whether the ground model needs CH (it does not, but the
  extension does, and the forcing that supplies it is missing from the
  section's list, F3); whether the derived object is "Folkman's two-color
  graph" (it is a graph with the property of Problem 582, not Folkman's
  construction, F3). The attack fails; the findings are presentational.
- **S3.** Attack on the necessity: exhibit a weaker input that would run
  the route. A proof of $R_k$ from CH alone would do, since W1 forces CH
  anyway; so would $R_k$ holding in the constructible universe, an inner
  model of every ground model that satisfies CH and has the same finite
  graphs. Neither is known, and Komjáth records the consistency question as
  open, so the obstruction stands; the sentence is read as naming the
  route's input, a positive answer to Problem 1171 at $k$, and F2 records
  the sharper phrasing. Attack on "open for $k\ge3$": if $R_k$ were a ZFC
  theorem for some $k\ge3$, then $R_3$ would follow by leaving colors unused
  (T2), and $R_3$ is recorded as unknown on printed p. 443. The attack
  fails.
- **S4.** Attacks: produce a $K_4$-free graph on $\omega_1^2$ with no
  independent set of type $\omega_1\omega$ under $\mathrm{MA}_{\aleph_1}$
  (impossible by W2); check that Baumgartner's theorem is used inside its
  filed interface (every finite $n$, on the result page and in the held
  restatement); check that "the relation is known" is asserted at the
  corpus's standing (the Theorem 3.1 reconstruction, author-recorded and
  conditional on the chapter that is not held, and the result page's
  bridging step; the problem's status "not disprovable" rests on the same);
  look for a witness on another ordinal $\gamma$ with the target
  $\omega_1\omega$ (for $\gamma\ge\omega_1\omega$ the relation
  $\gamma\to(\omega_1\omega,4)^2$ transfers by (T2), and for
  $\gamma<\omega_1\omega$ the positive relation $R_k$ has no analog, since
  $\gamma$ has no subset of type $\omega_1\omega$). The attack fails.
- **S5.** Attack: W1 at $k\ge3$ derives $F_k$ from $R_k$ in ZFC, so the
  triangle case of the finite theorems does follow from a positive answer
  to the open case; the case $l\ge4$ of Problem 924 does not, since Problem
  1171 has triangle targets only. The first clause is refuted as an
  implication, and it is vacuous under the alternative reading "cannot be
  derived today", since nothing is derivable from an open case. The second
  clause, "nor feed": no implication from the finite theorems, which are
  statements about finite graphs, to $R_k$ is known, and the section's own
  S3 and S4 exhibit nothing of the kind; the attack on it fails.
- **S6.** Attacks: break the instance (W3 re-derives it); test "the only
  derivation" (the cited passage also records, from Larson's sharpening,
  not held, the instance with $5$ and four triangle colors, a $K_5$-free
  four-color graph, and the same derivation runs at $\omega^{\omega^\beta}$
  for every $\beta$ that is a sum of two indecomposables, giving the same
  finite statement, F5); test "exceed" (true through the theorem of
  Nešetřil and Rödl, not held; Folkman's held bound only matches, F6). The
  attack succeeds only against the word "only", at the level of a note.
- **S7.** Not a claim. The outcome survives the corrected reasoning: a
  positive answer to the open case would re-derive $F_k$, which is already
  proved, and the finite theorems give nothing to $R_k$.

## Premises

- (T1) and (T2), Tools section, lines 37--61: transport of a relation along
  an order isomorphism, and restriction to a subset of the given type,
  weakening of the large target, embedding of a graph target, and leaving a
  color unused. Used in W2 and for "open for $k\ge3$". Their proofs are
  another reviewer's subject; the interfaces were confirmed at each use.
- [[research/erdos_1171/lemma_2_1_reconstruction|Lemma 2.1]]: for an
  ordinal $\alpha$ with $\alpha\to(\alpha,3)^2$ and every finite $k\ge1$,
  $\alpha\to(\alpha,3,\ldots,3)^2_{k+1}$; ZFC; reviewed as it stood on
  2026-09-28T05:03:27Z. Used in W3 at $\alpha=\omega^{\omega^2}$, $k=5$,
  inside its hypothesis, which Theorem 28 supplies. Read in full.
- [[research/erdos_1171/theorem_3_1_reconstruction|Theorem 3.1]]: under
  $\mathrm{MA}_{\aleph_1}$, $R_k$ for every finite $k\ge1$; conditional on
  its Theorem A (Baumgartner's chapter at $n=3$, not held); reviewed as it
  stood on 2026-09-28T05:03:27Z. Used in S4 for "the relation is known". Read
  in full.
- Baumgartner 1989, §3 main theorem: $\mathrm{MA}_{\aleph_1}$ implies
  $\omega_1\omega\to(\omega_1\omega,n)^2$ for every finite $n$. Not held;
  the statement is the zbMATH review's, restated in the held paper of Chen,
  Garti and Weinert, printed p. 5, read in the text layer. Used at $n=4$ in
  W2.
- Baumgartner and Hajnal 1987, relation 3 at $\kappa=\omega$
  ($\omega_1^2\to(\omega_1\omega,3,3)^2$ in ZFC) and relation 1 at
  $\kappa=\omega$ (CH implies $\omega_1^2\not\to(\omega_1\omega,4)^2$). Not
  held; the zbMATH review's statements, corroborated on Komjáth's printed
  pp. 425 and 442 on the page images and in Chen, Garti and Weinert on
  printed p. 5. Used in W1.
- Komjáth 2025, held: Problem 13 commentary (pp. 425--426) and Problem 54
  discussion (pp. 442--443), read on the page images: the argument, its
  ingredients including the forcing of CH, its attribution to Hajnal, and
  the two open questions ($R_3$ in ZFC, and the consistency of
  $\alpha\not\to(\beta,4)^2$ with $\alpha\to(\beta,3,3,3)^2$ for some
  $\alpha,\beta$). Also the statement of the general case of Problem 54 as
  proved by Nešetřil and Rödl (p. 442).
- Folkman 1970, held: the definitions and Theorem 1 (printed p. 20) and the
  Remarks with the $n$-class definitions, the conjecture and the inequality
  (pp. 23--24), read on the page images; the inequality is printed without
  proof. Used in S1 and W3.
- Nešetřil and Rödl 1976: not held; the statement is taken second-hand from
  the problem page and from Komjáth, p. 442. Used in S1 and for "exceed".
- Schipperus 2010, held: Theorem 28 at $\beta=2$ and Theorem 29, part 1,
  from the result pages' statement sections, which record a page-image
  reading. Used in W3.
- Larson's sharpening ($\omega^{\omega^2}\not\to(\omega^{\omega^2},5)^2$
  with $\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$): not held; mentioned
  only in F5 and W3.
- Standard set theory used in W1 and not taken from held sources: a
  $\sigma$-closed forcing adds no reals, preserves $\omega_1$ and, for the
  forcings named, adds CH; a finite set of ground-model elements lying in a
  set-generic extension lies in the ground model; a bounded statement about
  hereditarily finite objects is absolute; the compactness theorem of
  propositional logic.
- The statement regions of Problems 582, 924 and 1171.

## Findings

- **F1 (required).** Location: "So the finite theorems neither follow from
  nor feed the open case of Problem 1171". Defect: the first clause denies
  an implication that holds. Witness: W1 at $k\ge3$ derives $F_k$, the
  $k$-color statement of Problem 582 and the case $l=3$ of Problem 924, from
  $R_k$ in ZFC, by the very route S3 describes; only the cases $l\ge4$ of
  Problem 924 lie outside the reach of Problem 1171's triangle targets.
  Under the reading "cannot be derived today" the clause is vacuous. The
  conclusion "no lead" survives on the corrected reasoning. Proposed
  replacement: "So a positive answer to the open case of Problem 1171 would
  only re-derive, by the same argument, the triangle case of finite theorems
  already proved, and the finite theorems give nothing back to Problem 1171."
- **F2 (suggested).** Location: "would need the ZFC relation with $k$
  triangle targets, open for $k\ge3$, and the CH witness in the same model".
  Defect: read as a necessity, the sentence asks for more than the route
  needs, since a proof of $R_k$ from CH alone would run it (W1 forces CH in
  any case), and "the CH witness" is one witness among those available, a
  witness under $\mathfrak d=\aleph_1$ serving equally. The obstruction is
  unaffected, because $R_k$ for $k\ge3$ is open in ZFC and unknown in every
  model that has a witness (Komjáth's weaker consistency question).
  Proposed replacement: "would need the relation with $k$ triangle targets
  in a model that also has a witness for
  $\omega_1^2\not\to(\omega_1\omega,4)^2$, for instance any model of CH;
  the relation is open in ZFC for $k\ge3$, and Komjáth records as unknown
  whether it is even consistent with such a witness".
- **F3 (suggested).** Location: "derives Folkman's two-color graph from the
  ZFC relation $\omega_1^2\to(\omega_1\omega,3,3)^2$, the CH witness for
  $\omega_1^2\not\to(\omega_1\omega,4)^2$, compactness, and the absoluteness
  of finite graphs". Defect: the list omits the forcing that adds CH to an
  arbitrary ground model, which the source states ("As CH can be added by
  forcing, each model has a forcing extension having the above $Y$, and then
  each model must have it") and without which the argument proves $F_2$ only
  under CH; and the derived graph is a graph with the property of Problem
  582, not Folkman's construction and not Theorem 1 at general $(k_1,k_2)$.
  Proposed replacement: "derives a graph with the property of Problem 582
  from the ZFC relation $\omega_1^2\to(\omega_1\omega,3,3)^2$, the witness
  for $\omega_1^2\not\to(\omega_1\omega,4)^2$ in a forcing extension
  satisfying CH, compactness, and the absoluteness of a finite graph and
  its finite property between the extension and the ground model".
- **F4 (note).** Location: "since Baumgartner's theorem gives
  $\omega_1^2\to(\omega_1\omega,4)^2$ there". The theorem is stated at
  $\omega_1\omega$; the passage to $\omega_1^2$ is the restriction (T2),
  re-derived in W2. Naming it ("with (T2)") would close the gap in the
  text.
- **F5 (note).** Location: "the only derivation of a Folkman-type finite
  graph from the material here is the $K_6$-free, five-color instance". The
  cited passage also records, from Larson's sharpening (not held), the
  instance with $5$ and four triangle colors, whose finite corollary is a
  $K_5$-free four-color graph; and the same derivation runs at
  $\omega^{\omega^\beta}$ for every countable $\beta$ that is a sum of two
  indecomposables, with the same finite conclusion. "Only" is exact for the
  finite statement obtained from held sources, and the sentence could say
  so.
- **F6 (note).** Locations: "Problem 924 by Nešetřil and Rödl" and "which
  the finite theorems exceed". The theorem of Nešetřil and Rödl is not held
  and is quoted second-hand, a qualification the problem page carries and
  the section, which promises to cite sources at their library standing,
  does not. The exceeding rests on that theorem alone: Folkman's held
  inequality gives $f(3,3,3,3,3)\le5$ and $f(3,3,3,3)\le4$, which match the
  two instances of W3 exactly and do not exceed them.

## Verdict

- S1: refutation-failed. The attributions match the filed theorems; the
  standing of the second is not carried (F6).
- S2: refutation-failed. Hajnal's argument re-derives (W1 at $k=2$); the
  ingredient list omits the forcing of CH and names the derived graph
  loosely (F3).
- S3: refutation-failed. Read as the description of the route through a
  positive answer to Problem 1171, the requirement and the openness for
  $k\ge3$ are correct; the sharper phrasing is F2.
- S4: refutation-failed. Re-derived in W2 from Baumgartner's theorem at
  $n=4$ and the restriction (T2), within the filed interfaces.
- S5: refuted-as-stated. The clause "neither follow from" is false as an
  implication: $F_k$ follows from $R_k$ in ZFC (W1); the clause "nor feed"
  survives; the outcome survives on corrected reasoning (F1).
- S6: refutation-failed. The instance re-derives (W3); "only" and "exceed"
  hold at the level the notes F5 and F6 state.
- S7: not a claim; the outcome "no lead" survives.

Limitations. The chapter of Baumgartner and the paper of Baumgartner and
Hajnal are not held, and their statements enter at the library's standing,
from the zbMATH reviews corroborated by held texts; the theorem of Nešetřil
and Rödl and Larson's sharpening are not held; Theorems 28 and 29 of
Schipperus, Lemma 2.1 and Theorem 3.1 are premises and were not re-proved;
the set-theoretic steps of W1 (forcing CH, absoluteness of finite objects,
compactness) are re-derived from standard facts rather than from held
sources. This focused review assigns no tier and changes no status.
