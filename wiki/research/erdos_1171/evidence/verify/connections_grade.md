---
name: research/erdos_1171/evidence/verify/connections_grade
title: "Distinct grade of the Problem 1171 connections reviews"
desc: |
  Distinct grader's record for the eleven focused reviews of the connections
  page and its two leads as they stood on 2026-09-28T13:50:48Z: all eleven
  reports pass, sixteen corrections are accepted, both lead routes survive
  after the corrections, and no tier is assigned.
created: 2026-09-28T19:36:33Z
updated: 2026-09-28T19:36:33Z
---

***

## Subject

The source as it stood on 2026-09-28T13:50:48Z, then the tip of the default
branch (called "the commit" below). Page:
`math/research/erdos_1171/connections.md`, read whole with `git show` at
that commit; line numbers below refer to that file at that commit. Leads:
`wiki/research/leads/graph_targets_under_martin_axiom/_index.md` and
`wiki/research/leads/four_clique_versus_triangle_colors/_index.md`, each
read whole at the commit. The working-tree copies of the three files are
unchanged from the frozen bytes.

Reports, each read whole:
[[research/erdos_1171/evidence/verify/connections_tools_review|Tools]],
[[research/erdos_1171/evidence/verify/connections_problem_1171_in_zfc_descent_chains_and_their_obs_review|Problem 1171 in ZFC]],
[[research/erdos_1171/evidence/verify/connections_problem_1169_two_color_and_finite_color_negative_review|Problem 1169]],
[[research/erdos_1171/evidence/verify/connections_problem_597_graph_targets_review|Problem 597]],
[[research/erdos_1171/evidence/verify/connections_problems_590_591_592_and_118_countable_partition_review|Problems 590, 591, 592 and 118]],
[[research/erdos_1171/evidence/verify/connections_problems_592_and_1171_four_clique_versus_triangl_review|Problems 592 and 1171]],
[[research/erdos_1171/evidence/verify/connections_problems_1174_595_and_596_countably_many_colors_review|Problems 1174, 595 and 596]],
[[research/erdos_1171/evidence/verify/connections_problem_1168_review|Problem 1168]],
[[research/erdos_1171/evidence/verify/connections_problem_601_the_infinite_path_target_review|Problem 601]],
[[research/erdos_1171/evidence/verify/connections_problems_582_and_924_finite_folkman_graphs_review|Problems 582 and 924]]
and
[[research/erdos_1171/evidence/verify/connections_other_relations_in_the_set_theory_folder_review|Other relations]].

Read for adjudication, at the same commit unless stated: the sections
"Independence and the assignment", "Exact subjects and durable evidence",
"Report contract", "Grading and claim standing", "Whole-claim report" and
"Audit checklist" of `docs/verification.md`; the earlier
[[research/erdos_1171/evidence/verify/grade|reconstruction grade]] and the
verify index, for the local form of a grade; the Mechanism paragraph of the
folder index, for the attribution of (T3); the conventions, imported
theorems and "Fidelity and scope" section of
[[research/erdos_1171/theorem_3_1_reconstruction|the Theorem 3.1 page]] and
the statement of
[[research/erdos_1171/lemma_2_1_reconstruction|the Lemma 2.1 page]]; the
card and main-theorem page of
[[../library/set_theory/baumgartner_1989_remarks_partition_ordinals/_index|Baumgartner (1989)]]
and the card of
[[../library/set_theory/chen_2018_cardinal_characteristics_continuum_partitions/_index|Chen, Garti and Weinert]];
the statement blocks of Problems 70, 592, 1172, 1218 and 1220; and, by text
extraction of the held PDFs,
[[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth (2025)]]
at printed pp. 425 and 442--443,
[[../library/set_theory/schipperus_2010_countable_partition_ordinals/_index|Schipperus (2010)]]
at printed pp. 1195--1197, 1209 and 1212--1213,
[[../library/set_theory/shelah_1989_consistency_positive_partition_theorems_graphs_models/_index|Shelah (1989)]]
at the statement of Lemma 5.1, and Chen, Garti and Weinert at pp. 1 and 5.
No other review, evidence folder, workspace file or web page was read; the
arXiv abstracts the page cites are not held and were not read.

Independence, by role: distinct grader in a fresh context, given only this
assignment. The grader wrote none of the page, the leads, the reconstruction
pages, the library cards or the eleven reports, and had no communication
with the author or with any reviewer. A grader is not blind: the standing
text of the cards, the folder index, the earlier grade and all eleven
reports were read by design.

Exposure rulings. Each report discloses what reached it beyond its
commissioned set: status words and Source paragraphs of problem pages,
library cards read whole, the file names of sibling reviews, and in five
cases another section of the same page. The Problem 1169 review read the
descent section; the Problem 1168 review read the Problem 597 section and
the countable-colors section, the latter as the declared input for the bit
coloring it re-derives; the countable-colors review read the Target
paragraphs of the Problem 597 and Problem 601 sections, to test the sentence
it refuted; the Problem 601 review read the Outcomes section; the Folkman
review read the instance passage it cites as an input. Content test: nothing
in any report could only have come from an exposed text except the declared
inputs, which the reports re-derive from their own hypotheses; no exposed
text is a review of, or a verdict on, the section under review; and the
direction of every attack follows from its own subject. All exposures are
ruled immaterial.

## Reports graded

All eleven reports pass. Each opens with a subject block that resolves
(the commit, the path and the section's line range, with the next heading's
line named), states the reviewer's role, the allowed and actually read
material and every exposure, restates the section's statements with their
quantifiers and conventions, gives an explicit verdict on each of the ten
checklist items of `docs/verification.md` "Audit checklist" with the
inapplicable ones marked, re-derives up to three weakest steps in its own
words, records a real strongest attack, lists its premises with interfaces
and reading depth, and closes with a per-statement verdict written in full.
The grader re-derived the mathematics behind every accepted correction and
every refuted or defective verdict; the report-specific observations
follow.

**Tools: pass.** The three weakest steps are the induction step of (T4)
with the transport taken in the order of $\gamma_0$, the coincidence of the
two extracted colorings in (T5), and the equivalence over non-ordinal order
types; the grader agrees with each. The strongest attacks are real: the
clique reading of a graph copy with the witness $5\to(3,P_3)^2$ against
$5\not\to(3,3)^2$, the edgeless-target counterexample to the unused-color
clause, and the merge order of (T4). The unverified attribution of (T3) to
the folder index is resolved below.

**Problem 1171 in ZFC: pass.** The order-type count in the proof of (b) is
re-derived with the block grouping, the case split of the Conclusion is
re-derived with the two extensions the section leaves implicit, and the
second by-product is traced through Steps 1--3 of the theorem page. The
strongest attack on S7, reading the consequence sentence on its own and
refuting it with the constant chain under $\mathrm{MA}_{\aleph_1}$, is the
attack the checklist asks for; the grader confirms the witness.

**Problem 1169: pass.** (T5) at $\alpha=\omega_1^2$, the boundary $k=0$ and
the comparison of S6 are re-derived. The attacks on S8 are serious and
retained: the one-step preservation argument for a $\sigma$-centered forcing
is a real derivation, and the report says correctly that it does not reach
the section's universal clause. The read of the descent section is ruled
immaterial above.

**Problem 597: pass.** The graph-target step, the Folkman merge and (T4)
with graph targets are re-derived. The required finding on the negative
outcome of investigation (ii) carries an exact witness, CH at $G=K_3$, which
the grader checked against the theorem page's fidelity note and Komjáth
(2025), p. 425. The recollection filed as F7 is marked as outside the
corpus and is not part of the verdict.

**Problems 590, 591, 592 and 118: pass.** The backward direction of the
equivalence through (T5), the lemma beyond ordinals with the cardinal
bridge, and the compactness step of the finite corollary are re-derived,
the last with a proof. The attack on Schipperus's proofs for a hidden axiom
is a real one and its answer, a text search, is recorded.

**Problems 592 and 1171: pass.** The core deduction, the necessary
condition with the omitted step $\beta\le\alpha$ supplied, and the
negative-outcome consequence are re-derived. The two required findings, the
countable restriction and the unsupported census of candidates, were
checked by the grader on Schipperus pp. 1195--1197: the paper restricts
itself to countable ordinals, Theorem 3 reads "at most two", and the exact
boundary is stated for $\beta=2$ only.

**Problems 1174, 595 and 596: pass.** The obstruction, the cardinality
consequence and the two reach sentences are re-derived; the refutation of
S10 carries a complete witness, the monochromatic $K_{\aleph_0,\aleph_0}$
inside a color class on any uncountable set of size at most the continuum,
which the grader re-derived, and the Erdős--Rado display was checked on
Komjáth p. 442.

**Problem 1168: pass.** The convention bridge from Theorem 44 of Erdős and
Rado, the bit coloring at $\aleph_{\omega+1}$ and the reduction by König's
theorem are re-derived. The attack on S7, trying to build a limit step and
showing that none can exist in ZFC, is the right one.

**Problem 601: pass.** The graph-coloring bridge, (T3) with the path target
at the constant chain, and the equivalence of the union statements with the
property are re-derived; the attacks on the reading of "infinite path" and
on the instance $k=0$ are recorded with their outcomes.

**Problems 582 and 924: pass.** Hajnal's argument is re-derived with $k$
colors, including the forcing of CH, compactness and absoluteness, and the
$\mathrm{MA}_{\aleph_1}$ obstruction and the instance at $\omega^{\omega^2}$
are re-derived; the refutation of the clause "neither follow from" is
exactly that derivation, and the grader agrees.

**Other relations: pass.** The exponent-free re-derivation of transport,
restriction, descent and witness extraction is complete and the grader
confirms that no step uses the exponent; the corollary for Problem 1220 and
the obstruction from a color-$0$ target below the resource are re-derived.
The cross-reference to the Problem 1219 connections page is marked
unverified, as the read set requires.

## Corrections

The numbering is this record's own; the reconstruction grade's C1 is a
different correction to a different page. Every correction below is
confined to text outside any claim card's `statement:` field; the page and
the leads are author-recorded and carry no tier.

**C1.** Page: `connections.md`. Location: section "Tools", (T1), lines
42--44, the clause "a copy of $H_i$ all of whose pairs have color $i$, a
copy being a subset of type $H_i$ when $H_i$ is an order type and a subgraph
isomorphic to $H_i$ when $H_i$ is a graph." Replace with: "a copy of $H_i$
in color $i$, a copy being a subset of type $H_i$ all of whose pairs have
color $i$ when $H_i$ is an order type, and a subgraph isomorphic to $H_i$
all of whose edges have color $i$ when $H_i$ is a graph." Basis: two
reviewers (Tools F2, Problem 597 F6) read the word "pairs" as admitting the
vertex-pair reading, under which a graph target is the clique on its
vertices; the two readings define different relations, as the Tools
review's witness shows ($5\to(3,P_3)^2$ under the edge reading, while
$5\not\to(3,3)^2$), and every later use of a graph target on the page (the
Folkman merge, the path target) is the edge reading. The definition is
load-bearing for the sections on Problems 597 and 601.

**C2.** Page: `connections.md`. Location: section "Problem 1171 in ZFC",
lines 160--161, the sentence "No such second link is a theorem of ZFC,
because under CH none holds:". Replace with: "No chain of length two has
both links theorems of ZFC, because under CH one of them fails:". Basis
(descent F2): with $\gamma_1=\omega_1^2$ and $\gamma_2=\omega_1\omega$, both
allowed by the bounds at line 158, the second link
$\omega_1^2\to(\omega_1\omega,3)^2$ is the ZFC theorem of Erdős and Hajnal;
what fails for that $\gamma_1$ is the first link, as bullet (a) says.

**C3.** Page: `connections.md`. Location: section "Problem 1171 in ZFC",
bullet (a), line 170, "the same commentary's next sentence". Replace with:
"a later sentence of the same commentary". Basis (descent F4), checked on
Komjáth p. 425: between the sentence printing Hajnal's hypothesis
$\kappa^{<\kappa}=\kappa$ and the sentence "The consistency of
$\omega_1^2\to(\omega_1^2,3)^2$ is, as far as I know, open" stand three
sentences on Baumgartner's extensions, and the consistency sentence opens a
new paragraph.

**C4.** Page: `connections.md`. Location: section "Problem 1171 in ZFC",
Conclusion paragraph, lines 218--225, the sentences "So (T4) yields exactly
the case $k=1$ in ZFC. In particular the ZFC case $k=2$ of Baumgartner and
Hajnal cannot be obtained by (T4) from two-color relations
$\gamma\to(\gamma',3)^2$ between ordinals in $[\omega_1\omega,\omega_1^2]$,
and (T4) cannot reduce the open case $k=3$ to such relations. This sharpens
the folder index's remark: not only the constant chain through
$\omega_1\omega$ but every descending chain is blocked in ZFC." Replace
with: "So (T4) with triangle targets yields, from two-color relations that
are theorems of ZFC, exactly the case $k=1$. In particular the ZFC case
$k=2$ of Baumgartner and Hajnal cannot be obtained by (T4) from two-color
relations $\gamma\to(\gamma',3)^2$ between ordinals in
$[\omega_1\omega,\omega_1^2]$ that are theorems of ZFC, and (T4) cannot
reduce the open case $k=3$ to such theorems. This sharpens the folder
index's remark: not only the constant chain through $\omega_1\omega$ but
every descending chain of length at least two has a link that fails under
CH, so none consists of theorems of ZFC." Basis (descent F1, with the scope
word of F3): read on their own, as the checklist requires of consequence
sentences, the frozen sentences deny a reduction that exists, since (T3),
the constant case of (T4), reduces the case $k=3$ to
$\omega_1\omega\to(\omega_1\omega,3)^2$, a relation of the named form that
the section's own second by-product records, and in every model of
$\mathrm{MA}_{\aleph_1}$ the constant chain through $\omega_1\omega$ is a
descending chain; the qualifier "theorems of ZFC" from the setup at line 150
is what the argument establishes. The words "with triangle targets" record
that the section's obstruction is proved for chains whose non-zero colors
carry triangles, the shape the section defines.

**C5.** Page: `connections.md`. Location: section "Problem 1169", lines
306--309, the sentence "If so, the negative relation, unlike
$\omega_1\omega\not\to(\omega_1\omega,3)^2$, is compatible with a fragment
of Martin's axiom, and a model of the positive relation is not reached from
a model of CH by such iterations." Replace with: "If so, the negative
relation is compatible with the fragment
$\mathrm{MA}_{\omega_1}(\sigma\text{-centered})$, whereas
$\omega_1\omega\not\to(\omega_1\omega,3)^2$ contradicts full
$\mathrm{MA}_{\aleph_1}$ (Theorem A on the theorem page); whether that
fragment alone excludes $\omega_1\omega\not\to(\omega_1\omega,3)^2$ is not
settled by anything held here; and the iteration the abstract describes
does not reach a model of the positive relation." Basis (Problem 1169 F2
and F3): the contrast "unlike" asserts on its natural reading that the same
fragment excludes $\omega_1\omega\not\to(\omega_1\omega,3)^2$, which nothing
held states, since the corpus records Theorem A under full
$\mathrm{MA}_{\aleph_1}$ for every c.c.c. partial order and the held
restatement of Chen, Garti and Weinert (p. 5) does the same; and "such
iterations" quantifies over all finite-support iterations of
$\sigma$-centered forcings where the section's own paraphrase of the
abstract supplies one. The sentence is context the page marks as not used.

**C6.** Pages: `connections.md`, section "Problem 597", line 337, "the
statement is taken from the zbMATH review and one refereed restatement";
and the lead `graph_targets_under_martin_axiom/_index.md`, section
"Provisional premises", second bullet, "rests on the review and one refereed
restatement, not on the chapter". Replace "one refereed restatement" with
"one held restatement (an arXiv preprint)" in both. Basis (Problem 597 F3):
the held file is `arXiv:1801.00238v1`, dated 31 December 2017, and the
library card of Chen, Garti and Weinert records "arXiv preprint (2018)"; the
page's Scope paragraph cites sources at the standing their library pages
record, and nothing held records a refereed version. The Baumgartner (1989)
card calls the same paper "a held refereed paper"; that card is outside this
subject and is flagged, not changed.

**C7.** Pages: `connections.md`, section "Problem 597", Next investigation
(ii), lines 397--399, "a negative outcome, a counterexample $G$ under
$\mathrm{MA}_{\aleph_1}$, shows that (Q1) has no positive answer in ZFC and
names a third necessary exclusion."; and the lead
`graph_targets_under_martin_axiom/_index.md`, section "Next step", item 2,
"A negative outcome, a counterexample $G$ under $\mathrm{MA}_{\aleph_1}$,
shows that (Q1) has no positive answer in ZFC and names a third necessary
exclusion." Replace both with: "a negative outcome shows only that this
route does not cover $G$; (Q1) has no positive answer in ZFC, and $G$ is a
third necessary exclusion, only if some model satisfies
$\omega_1^2\not\to(\omega_1\omega,G)^2$ for a $G$ with the exclusions of
(Q1), which a failure on $\omega_1\omega$ does not give: under CH,
$\omega_1\omega\not\to(\omega_1\omega,3)^2$ while
$\omega_1^2\to(\omega_1\omega,3)^2$ is a theorem of ZFC." (In the lead,
capitalize the first word.) Basis (Problem 597 F1, required): the
investigation concerns the relation on $\omega_1\omega$, so its negative
outcome is $\omega_1\omega\not\to(\omega_1\omega,G)^2$ in a model of
$\mathrm{MA}_{\aleph_1}$; a negative relation does not pass from the initial
segment to $\omega_1^2$, and the witness is the CH pair at $G=K_3$ recorded
on the theorem page and on Komjáth p. 425.

**C8.** Pages: `connections.md`, section "Problems 592 and 1171", lines
513--517: in "Theorem 29(2) supplies the second half for every
$\alpha=\omega^{\omega^\beta}$ with $\beta$ a sum of three indecomposables"
write "with countable $\beta$ a sum of three indecomposables", and in "if
$\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ for some $\beta$ that
is a sum of three indecomposables, then Komjáth's question has a positive
answer in ZFC" write "for some countable $\beta$ that is a sum of three
indecomposables"; and the lead `four_clique_versus_triangle_colors/_index.md`,
section "Route and established inputs", the deduction sentence "for some
$\beta$ that is a sum of three indecomposables, then with
$\alpha=\beta'=\omega^{\omega^\beta}$", and section "Provisional premises",
first bullet, "for some $\beta$ that is a sum of three indecomposables is
open": insert "countable" before $\beta$ in both. Basis (Problems 592 and
1171 F1, required), checked on Schipperus p. 1195 ("we shall only consider
the relation $\alpha\to(\delta,\gamma)^2$ in the case where $\alpha$,
$\delta$, $\gamma$ are countable") and p. 1212 (Theorem 28 is stated for
$\beta<\omega_1$): Theorem 29 supplies nothing for uncountable $\beta$, so
the unrestricted sentences are unproved there; the lead's Theorem 29 bullet
already says "countable".

**C9.** Page: the lead `four_clique_versus_triangle_colors/_index.md`,
section "Route and established inputs", the sentence "The interfaces match:
both relations are two-color relations in the convention of the lemma page,
Komjáth asks for some pair in some model and the deduction gives one pair in
every model, and the target $4$ of Theorem 29 is a four-element homogeneous
set, the four-clique of the question." Replace with: "The interfaces match:
the premise and Theorem 29, part 2, are two-color relations in Schipperus's
Definition 1, which is the lemma page's relation at two colors, and
Komjáth's $\alpha\to(\beta,3,3,3)^2$ is the four-color relation of the
lemma's conclusion at $k=3$; Komjáth asks for some pair in some model and
the deduction gives one pair in every model; and the target $4$ of Theorem
29 is a four-element homogeneous set, the four-clique of the question."
Basis (Problems 592 and 1171 F3): the antecedent of "both relations" is the
two displayed relations, one of which has four colors, so the sentence is
false as worded while the check it intends holds.

**C10.** Pages: `connections.md`, section "Problems 592 and 1171", Next
investigation, lines 542--544, "a negative outcome for every such $\beta$
completes the classification of Problem 592 as "one or two indecomposables"
and leaves Komjáth's question to the other shape of answer." Replace with:
"a negative outcome for every such $\beta$ completes the classification of
Problem 592 as "at most two indecomposables" ($\beta=0$ included, since
$\omega\to(\omega,3)^2$) and leaves Komjáth's question to the other shape
of answer, or to the shape $(\alpha,\alpha)$ at a partition ordinal whose
four-clique relation is undecided, such as $\omega^{\omega^\omega}$, where
Theorem 28 gives the $3$-relation and nothing held decides the
$4$-relation." In the lead `four_clique_versus_triangle_colors/_index.md`:
section "Route and established inputs", "Two side facts fix the candidates."
becomes "Two side facts narrow the candidates."; and section "Next step",
"completes the classification of Problem 592 as "one or two indecomposables"
and returns Komjáth's question to the shape with $\beta<\alpha$." becomes
"completes the classification of Problem 592 as "at most two
indecomposables" and returns Komjáth's question to the shape with
$\beta<\alpha$ or to the shape $(\alpha,\alpha)$ at a partition ordinal
whose four-clique relation is undecided, such as $\omega^{\omega^\omega}$."
Basis (Problems 592 and 1171 F2, required, and F6): a negative outcome
removes only the three-summand ordinals from the shape $(\alpha,\alpha)$;
for $\beta=\omega$, a single indecomposable, Theorem 28 gives the
$3$-relation and Theorem 29 has no negative relation for one summand, and
Schipperus p. 1197 states the exact boundary for $\beta=2$ only. The
boundary case $\beta=0$ is a countable ordinal in the range of Problem 592,
$\omega^{\omega^0}=\omega$ has the property by Ramsey's theorem, and
Schipperus's Theorem 3 (p. 1196) itself reads "at most two".

**C11.** Page: `connections.md`. Location: section "Problems 1174, 595 and
596", lines 559--561, "Komjáth 2025 (Problem 53) records Shelah's
consistency proof ([[../library/set_theory/shelah_1989_consistency_positive_partition_theorems_graphs_models/_index|Shelah 1989]],
Lemma 5.1) and that existence in ZFC is open." Replace "Lemma 5.1)" with
"Lemma 5.1, relative to a measurable cardinal or the weaker partition
hypothesis the lemma allows in its place)". Basis (countable-colors F4),
checked on the held PDF: Lemma 5.1 assumes $\mu<\lambda<\kappa$ with
$\kappa$ measurable, or one of two partition hypotheses on $\kappa$ named in
its place, and $\lambda=\lambda^{<\lambda}$; the survey's sentence and the
section omit the hypothesis, which strengthens a consistency result.

**C12.** Page: `connections.md`. Location: section "Problems 1174, 595 and
596", lines 588--590, "The same coloring, with the color $0$ unused, refutes
the countable-color form of every relation on this page." Replace with:
"The same coloring, with the color $0$ unused, refutes the countable-color
form of every relation on this page whose ordinal has at most $2^{\aleph_0}$
elements and whose targets in the colors $\ge1$ each contain an odd cycle
(a triangle, a larger clique, an ordinal $\ge3$, or a graph containing a
triangle): its color classes are bipartite, so it says nothing about the
bipartite targets of Problems 597 and 601, and nothing above the continuum,
where $(2^{\aleph_0})^+\to((2^{\aleph_0})^+,(\aleph_1)_{\aleph_0})^2$ holds
(Erdős and Rado, displayed by Komjáth 2025 under Problem 53)." Basis
(countable-colors F1, required): the class of color $1+n$ is a disjoint
union of complete bipartite graphs between the sets of $x$ whose codes
extend $s0$ and $s1$ for the strings $s$ of length $n$; on an uncountable
set of size at most the continuum some $s$ has both sets infinite (the
review's tree argument, re-derived here), so some class contains a
monochromatic $K_{\aleph_0,\aleph_0}$, hence a copy of the infinite path of
Problem 601 and of every countable bipartite $G$ of Problem 597; and the
cardinal relations of the Problem 1168 and Problem 1220 sections live above
the continuum, where no injection into $2^\omega$ exists and the
Erdős--Rado relation holds outright.

**C13.** Page: `connections.md`. Location: section "Problems 1174, 595 and
596", lines 590--593, "For Problem 596 the mechanism says only that the
finite side of the pair $(K_4,K_3)$ is reachable from ordinal relations, as
Hajnal's argument shows for two colors, and the countable side is not."
Replace with: "For Problem 596 the mechanism says only that the two-color
finite side of the pair $(K_4,K_3)$ is reachable from ordinal relations, by
Hajnal's argument; that for three or more colors the same route needs
$\alpha\not\to(\beta,4)^2$ and $\alpha\to(\beta,3,3,3)^2$ in one model,
which Komjáth 2025 (p. 443) records as unknown (see the section on Problems
582 and 924); and that the countable side is out of reach, by the
cardinality obstruction." Basis (countable-colors F2, required): the finite
side of Problem 596 is "for every $n\ge1$", the sentence's only support is
the two-color case, and the section on Problems 582 and 924 itself records
that the $k$-color analog is open for $k\ge3$.

**C14.** Page: `connections.md`. Location: section "Problems 582 and 924",
lines 652--653, "So the finite theorems neither follow from nor feed the
open case of Problem 1171;". Replace with: "So a positive answer to the open
case of Problem 1171 would only re-derive, by the same argument, the
triangle case of finite theorems already proved, and the finite theorems
give nothing back to Problem 1171;". Basis (Folkman F1, required): if
$\omega_1^2\to(\omega_1\omega,3,\ldots,3)^2_{k+1}$ is a theorem of ZFC, then
in a forcing extension satisfying CH the witness for
$\omega_1^2\not\to(\omega_1\omega,4)^2$ exists, every $k$-coloring of its
graph's edges has a monochromatic triangle, compactness gives a finite
$K_4$-free subgraph with that property, and the finite graph is absolute to
the ground model, exactly the argument Komjáth attributes to Hajnal
(pp. 442--443) with $k$ colors; so the triangle case of the finite theorems
does follow from a positive answer, and the clause "neither follow from" is
false as an implication.

**C15.** Page: `connections.md`. Location: section "Other relations in the
set-theory folder", lines 660--668, "The mechanism needs a color-$0$ target
equal to the ambient order type, or a descending chain as in (T4), and fixed
targets in the other colors. It does not apply to Problem 1170 and Problem
1172, whose relations $\omega_2\to(\alpha)^2_2$ and
$\omega_2\to(\omega_1+\omega)^2_2$ are balanced with both targets below the
resource; nor to Problem 70 and Problem 1218, whose exponent is $3$; nor to
Problem 1219, a balanced cardinal relation." (the wikilinks to the problem
pages are kept). Replace with: "The mechanism needs a color-$0$ target equal
to the ambient order type, or a descending chain as in (T4), fixed targets
in the other colors, and finitely many colors; the exponent plays no part in
its proofs. It does not apply to Problem 1170 and Problem 1172, whose
relations, one for Problem 1170 and five under GCH for Problem 1172, all
have both targets below the resource; nor to Problem 70,
$\mathfrak{c}\to(\beta,n)^3_2$ for countable $\beta$ and finite $n$, whose
color-$0$ target lies below the resource; nor to Problem 1219, a cardinal
relation with both targets below the resource. For Problem 1218,
$\lambda\not\to(\lambda,4,4,\ldots)^3$ with countably many colors under GCH,
the mechanism runs in exponent $3$: for every finite $k$ the negative
relation with $k$ colors carrying $4$ is equivalent to
$\lambda\not\to(\lambda,4)^3$, which implies the asked relation by (T2); the
induction does not reach countably many colors, and that, not the exponent,
is the obstruction." In the Outcomes section, the bullet "Problems 582, 924
and the balanced or higher-exponent relations: not applicable." becomes
"Problems 582, 924 and the relations of the last section: not applicable,
Problem 1218 by the countable color count." Basis (other-relations F1,
required, and F2): the proofs of (T1)--(T5) use only order isomorphisms,
restriction, merging of colors and induction on the number of colors, none
of which mentions the exponent, and the review's exponent-free
re-derivation is complete; Problem 1218's relation has the shape the
criterion names; Problem 1172's statement lists five relations, three of
them unbalanced, all with both targets below the resource; and the Outcomes
bullet, which no report was assigned, restates the refuted reason.

**C16.** Page: `connections.md`. Location: section "Other relations in the
set-theory folder", lines 669--670, "For Problem 1220,
$\lambda\to(\lambda,\aleph_1)^2$ for singular $\lambda$,". Replace with:
"For Problem 1220, $\lambda\to(\lambda,\aleph_1)^2$ for a singular cardinal
$\lambda$ with $\lambda$ and $\mathrm{cf}(\lambda)$ both
$\aleph_0$-inaccessible,". Basis (other-relations F3): the problem page
states both hypotheses; without them the relation fails for every singular
$\lambda$ of countable cofinality, by the block coloring the review gives,
so the description as written names a false relation as the one asked.

## Rejected and downgraded findings

Findings not listed here were accepted into the corrections above. "No
change" means the frozen text stands; "optional" means the reviewer's
wording may be adopted but nothing false or unsupported is corrected by it.

- Tools F1 (suggested: the provenance sentence places (T1) and (T2) "on the
  reconstruction pages"). Downgraded to optional. Each of (T1) and (T2)
  states in its own text what it takes from the reconstruction pages and
  what it extends, so the summary sentence misleads no reader of the
  section.
- Tools F3 (suggested: scope of "everything below", and Lemma 2.1 cited for
  the forward direction over non-ordinal order types). Downgraded to
  optional. The equivalence holds, as the review's W3 shows and the grader
  agrees: the forward direction over order types is (T3), which the section
  proves as the constant case of (T4), and the backward direction is the
  unused-color clause. Only the attribution is loose.
- Tools F4 (note: the unused-color clause fails for edgeless targets).
  Rejected; no change. The clause's stated conclusion concerns triangle
  colors, and the page applies it to triangles only; the witness is correct
  and is recorded in the report for any later general use.
- Tools F5 (note: the attribution of (T3) to the folder index is
  unchecked). Resolved by the grader; no change. The folder index at the
  commit states, in its Mechanism paragraph, that the same argument gives
  $\alpha\to(\alpha,H_1,\ldots,H_k)^2_{k+1}$ from $\alpha\to(\alpha,H_i)^2$
  for fixed order types or finite graphs $H_i$; (T3) states it for
  arbitrary targets and the page proves that form as the constant case of
  (T4), so the citation is to a narrower statement of the same observation.
- Tools F6 (note: the closing remark of the proof of (T4) holds for the
  constant chain). Rejected; no change. The remark compares the proof with
  the lemma page's, which is the constant chain; the proof merges with the
  last color and is unaffected, as the review says.
- Descent F5 (note: the relative consistency of CH and Theorem C are
  unnamed). Rejected; no change. Standard facts the theorem page names once
  suffice for the folder.
- Descent F6 (note: (b) holds under $\omega_1\omega\not\to(\omega_1\omega,3)^2$
  alone). Rejected; no change. True and useful, but not a defect; the proof
  of (b) says where CH is used.
- Problem 1169 F1 (suggested: "for every $k$" at $k=0$). Downgraded to
  optional. The display one sentence earlier fixes $k\ge1$, and the prose
  refers to that display's $k$; the instance $k=0$ is the degenerate
  one-color relation.
- Problem 1169 F4 (note: "the unconditional conclusion ... is already
  known"). Downgraded to optional. What the sentence means is the
  consistency of the Problem 1171 relation, known outright by Theorem C;
  the reviewer's wording is clearer, but the frozen sentence is in an
  outcome remark and misleads no deduction.
- Problem 1169 F5 (note: the booklet quotation follows the transcription).
  Rejected; no change. The section says it read the retained transcription
  and quotes it; the cropped verb is a matter for the transcription, and
  the mathematical content is confirmed.
- Problem 1169 F6 (note: cite Lemma 2.1 rather than (T3) at
  $\alpha=\omega_1^2$). Rejected; no change. (T3) at that instance is
  Lemma 2.1, and (T3) is proved on the page.
- Problem 597 F2 (suggested: "refutes (Q2) at $F_3$" reads as a ZFC
  disproof). Downgraded to optional, in the section and the lead. The
  antecedent "a consistent negative answer" carries the modality, and the
  preceding sentence states the consequence as a model statement.
- Problem 597 F4 (suggested: "yields (Q2) only for subgraphs of a triangle"
  read as an independence statement). Downgraded to optional. The sentence
  describes what the mechanism yields, in a paragraph about the mechanism;
  no independence claim is made.
- Problem 597 F5 (note: the lead attributes the subgraph convention to the
  lemma page). Downgraded to optional. The lemma page's relation for
  order-type targets is the non-induced reading, which (T1) extends to
  graphs with C1; citing (T1) would be more precise.
- Problem 597 F7 (note: a recollection outside the corpus). Rejected as a
  finding; no change. It is offered for investigation (ii) and marked as
  needing its source.
- Problems 590--118 F1 (suggested: Milner's result consumed above its
  standing). Downgraded to optional. The section's Targets paragraph
  already says the relation is reported, and the sentence draws no
  conclusion beyond the agreement of two bridges.
- Problems 590--118 F2 (suggested: "only the derivation ... is new here" is
  a literature claim). Downgraded to optional. The sentence contrasts the
  paragraph with the finite theorems it cites; the page's Scope paragraph
  limits its reading to the held corpus and named catalog pages, so "new
  here" is relative to that reading.
- Problems 590--118 F3 (note: the cardinal bridge for Problem 118's
  sibling). Downgraded to optional. The statement is true; the bridge is
  the one line the review gives.
- Problems 590--118 F4 and F5 (notes: "four or more" and "which is false").
  Rejected; no change. The section cites Theorem 29 at the standing its
  result page records, and the clause attaches to the $6$-relation.
- Problems 592 and 1171 F4 (note: (T2) needs $\beta\le\alpha$). Downgraded
  to optional. The step follows from the answer's positive relation under
  the constant coloring, as the review's W2 shows.
- Problems 592 and 1171 F5 (note: the sensitivity remark is the opening of
  Section 10). Downgraded to optional. Checked on Schipperus p. 1209: the
  remark opens Section 10, which proves the triangle step of the main
  theorem, and also names the size of the finite clique; "Schipperus's
  proof of Theorem 28 says" is loose but attributes the remark to the right
  argument.
- Countable-colors F3 (note: the boundary $\alpha\in\{0,1\}$). Downgraded
  to optional. The display's hypothesis $|\alpha|\ge2$ stands one sentence
  earlier.
- Countable-colors F5 (note: "in other words" needs both directions).
  Rejected; no change. The converse is immediate and the review supplies
  it.
- Countable-colors F6 (note: the $\aleph_0$-color relation is undefined).
  Downgraded to optional. The reading is the evident extension of the
  finite definition, and it is the one the witness refutes.
- Problem 1168 F1 (suggested: the source characterization omits the
  large-cardinal hypotheses and misplaces the guessing route). Downgraded to
  optional. The sentence reports what the library card records, and says
  so; the card's digest is outside this subject and is flagged for its
  maintainers, since the review's reading of the PDF is precise.
- Problem 1168 F2 (note: the Erdős--Dushnik--Miller theorem is uncited).
  Downgraded to optional. A citation of Theorem 44 of Erdős and Rado would
  meet the page's own rule; the theorem is classical and correctly used.
- Problem 1168 F3, F4 and F5 (notes). Rejected; no change. The Ramsey
  number is used one $k$ at a time, the case split is true as written, and
  the obstruction sentence is correct.
- Problem 601 F1 and F2 (notes: $k=0$, and the reason for "says nothing").
  Rejected; no change. The instance $k=0$ is trivially true, and the
  sentence is exact.
- Folkman F2 (suggested: the necessity phrasing). Downgraded to optional.
  The obstruction stands whichever model supplies the witness, and the
  sentence names the route's input.
- Folkman F3 (suggested: the ingredient list omits the forcing of CH; "Folkman's
  two-color graph"). Downgraded to optional. The absoluteness clause names
  the step that needs the forcing, and "Folkman's two-color graph" reads as
  a graph with the property of Problem 582; the reviewer's wording is more
  exact.
- Folkman F4, F5 and F6 (notes). Rejected; no change. The restriction step
  is (T2) as the section's Tools state it; "only" is exact for the finite
  statement obtained from held sources; and the standing of the
  Nešetřil--Rödl theorem is carried on the problem page the section links.
- Other-relations F4 (note: "balanced" names no obstruction). Rejected as a
  separate change; C15 rewrites the sentence and drops the word.
- Other-relations F5 (note: the cardinal-to-order-type bridge). Downgraded
  to optional. The bridge holds because the resources and targets are
  initial ordinals, as the review's W2 shows.
- Other-relations F6 (note: the cross-reference to the Problem 1219
  connections page). Not adjudicated; that page is outside this subject.

Checks of the grader's own that produced no correction: the proof of
statement (b) of the descent section was re-derived from the existence of
the witness $W$ alone; the Komjáth attributions at p. 425 (Erdős and Hajnal's
$\omega_1^2\to(\omega_1\alpha,3)^2$ for $\alpha<\omega_1$; the printed
hypothesis $\kappa^{<\kappa}=\kappa$) and at p. 443 (the two unknowns) read
as the page states them; Theorem 29 of Schipperus reads at p. 1213 as the
page cites it; and the held restatement of Baumgartner's theorem at Chen,
Garti and Weinert p. 5 is for full $\mathrm{MA}_{\aleph_1}$ and every finite
$n$. Two matters outside the subject are flagged for their maintainers: the
statement block of Problem 592 prints the ordinal as
"$\alpha=\omega^{^\beta}$", with the exponent's base missing, and the
Baumgartner (1989) card calls the held Chen, Garti and Weinert file a
refereed paper while that file's own card records an arXiv preprint.

## Graded verdicts

Verdicts are written in full. Where a reviewer's verdict is changed or
qualified, the reason is given; "corrected by" names the correction that
repairs the frozen text.

**Tools.** S0 (provenance sentence): not a claim. S1 (T1, definition and
transport): refutation-failed, with the definition made exact by C1. S2
(T2, restriction), S3 (T2, weakening), S4 (T3), S5 (T4), S6 (T5), S7 (the
equivalence for every order type and finite $k\ge1$) and S8 (the closing
consequence): refutation-failed.

**Problem 1171 in ZFC.** S1 (target): not a claim; citations checked. S2
(chain deduction), S3 (first link), S4 (obstruction (a), at the standing of
the booklet item and the catalog), S5 (obstruction (b), proved from the
witness $W$), S6 ((b) applied), S8 (first by-product), S9 (second
by-product) and S10 (the two conditional deductions): refutation-failed.
S7 (Conclusion): the consequence sentences at lines 218--224 are
refuted-as-stated on their own, unqualified reading, with the witness the
review gives; the qualified statement the section proves is
refutation-failed; corrected by C4. The lead sentence of the obstruction at
line 160 is refuted-as-stated at the pair
$(\gamma_1,\gamma_2)=(\omega_1^2,\omega_1\omega)$ and corrected by C2. S11
(outcome): not a claim.

**Problem 1169.** S1 (forms of the question) and S9 (cross-references):
refutation-failed for what lies in the read set, unverified beyond it. S2
(the open part), S3 (finite-color equivalence), S4 (witness containment),
S5 (harmlessness of the stray quantifier, at the display's range $k\ge1$)
and S6 (conditional strengthening): refutation-failed. S7 (limitation) and
S10 (outcome): not claims. S8(a): refutation-failed as a conditional
deduction from an unheld abstract. S8(b) and S8(c): proof defective;
statement unresolved as written, since the contrast and the universal
clause are not supported by the paraphrase or by anything held; corrected
by C5, after which the sentence claims only what is supported.

**Problem 597.** S1 (conventions): not a claim. S2, S3 and S4:
refutation-failed, conditional on $\mathrm{MA}_{\aleph_1}$ and on the
imported theorem at full strength, which the section and the lead disclose
as a premise. S5, S6, S7 (with Folkman's Theorem 1 held and the
Nešetřil--Rödl theorem second-hand), S8, S10 and S11: refutation-failed. S9:
refutation-failed on the route reading, which is the reading of the
sentence. S12(a): refutation-failed. S12(b): proof defective; statement
unresolved, the missing bridge being the passage of a negative relation
from $\omega_1\omega$ to $\omega_1^2$; corrected by C7 in the section and
the lead. S13: refutation-failed on the consistency reading its antecedent
fixes. S14 (provenance sentences): not claims; the word "refereed" is
corrected by C6.

**Problems 590, 591, 592 and 118.** S1--S10: refutation-failed, S3 and S9
at the standing of the held sources, S4 and S9 with Larson's results as
reported. S11 (novelty remark): not a mathematical claim; unverifiable
within the read set and left as the page's own reading.

**Problems 592 and 1171.** S1, S2, S4 (at the depth of Schipperus's report
of Larson), S5 (with the omitted step supplied), S6, S7, S8 (the instance
with $5$ on the reported result) and S10: refutation-failed. S3:
refutation-failed for countable $\beta$; the unrestricted wording is
corrected by C8. S9: refutation-failed for the section's interface checks;
the lead's sentence "both relations are two-color relations" is
refuted-as-stated and corrected by C9. S11: the positive-outcome sentence
is refutation-failed; the classification "one or two indecomposables" is
refuted-as-stated at $\beta=0$; the clauses confining Komjáth's question to
the other shape, in the section and the lead, are proof defective;
statement unresolved; all corrected by C10. S12 (provenance): not a claim.

**Problems 1174, 595 and 596.** S1, S2, S4, S6 (the obstruction, with a
complete proof), S8, S9 and S11a: refutation-failed. S3: refutation-failed,
with the hypothesis of Shelah's lemma supplied by C11. S5 and S12: not
claims. S7: refutation-failed for every ordinal with at least two elements,
the hypothesis the display states; the boundary wording is optional. S10:
refuted-as-stated, with the bipartite witness and the relation above the
continuum; corrected by C12. S11b: proof defective; statement unresolved
for three or more colors; corrected by C13. S11c: refutation-failed.

**Problem 1168.** S1--S10: refutation-failed; S2 as a report of the library
card.

**Problem 601.** S1 (target formulation), S2 (finite-union transfer), S3
(non-triviality, with its witness), S4 (obstruction) and S5 (catalog and
holding sentence, within the read set): refutation-failed. S6: not a claim.

**Problems 582 and 924.** S1, S2, S3, S4 and S6: refutation-failed. S5:
refuted-as-stated as an implication, since a positive ZFC answer at $k$
derives the $k$-color triangle statement by Hajnal's argument; the clause
"nor feed" and the outcome survive; corrected by C14. S7: not a claim.

**Other relations in the set-theory folder.** S1: refutation-failed as a
list of necessary conditions, completed by C15 with the finite color count.
S2 and S4: refutation-failed on the ground that the color-$0$ target lies
below the resource; the description of Problem 1172 is corrected by C15.
S3: refuted-as-stated, the exponent being no obstruction, with the
exponent-free re-derivation as witness; corrected by C15. S5:
refutation-failed for the conditional corollary; the restatement of the
problem is corrected by C16. S6: a cross-reference outside the subject,
unverified. S7: not a claim.

**Leads.**

- Graph targets under Martin's axiom:
  reviewed. Its route rests on S2, S3, S7 and S8 of the Problem 597 section
  (the deduction of (Q2) under $\mathrm{MA}_{\aleph_1}$ from Baumgartner's
  theorem at full strength with the restriction step, and the Folkman
  implication to Problem 1171), all refutation-failed at the hypotheses the
  lead states as provisional premises. The defective sentence S12(b) is in
  its Next step and not on the route; it is corrected by C7, and C6 corrects
  the word "refereed"; the outcome holds once C6 and C7 are applied to the
  lead page.
- [[research/leads/four_clique_versus_triangle_colors/_index|Four-clique versus triangle colors]]:
  reviewed. Its route rests on S2, S3 (for countable $\beta$), S4 and S5 of
  the Problems 592 and 1171 section (Lemma 2.1 at $k=3$ with Theorem 29,
  part 2, the exclusion of $\omega^{\omega^2}$ and the necessary condition),
  all refutation-failed. The refuted interface sentence and the unsupported
  return-to-the-other-shape clause are descriptions beside the route, not
  steps of it; they are corrected by C8, C9 and C10, and the outcome holds
  once those are applied to the lead page.

No tier is assigned and no status changes.
