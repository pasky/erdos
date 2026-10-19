---
name: research/leads/four_clique_versus_triangle_colors
title: Four-Clique Versus Three Triangle Colors at a Countable Partition Ordinal
desc: |
  Any ordinal alpha with alpha -> (alpha, 3)^2 and alpha not-> (alpha, 4)^2
  answers, in ZFC, the question Komjáth records of whether alpha not->
  (beta, 4)^2 and alpha -> (beta, 3, 3, 3)^2 can hold together; the
  candidates omega^{omega^beta} with beta a sum of three indecomposables
  are exactly the undecided case of Problem 592.
problems:
- 592
- 1171
research_state: candidate
review_status: needs_update
created: 2026-09-28T05:29:06Z
updated: 2026-10-19T04:19:07Z
---

# Four-Clique Versus Three Triangle Colors at a Countable Partition Ordinal

[[research/leads/_index|..]]

***

This lead's notes that cite no source are author-recorded research, not claims.

## Target and status evidence

Two targets. The first is the question that
[[../library/set_theory/komjath_2025_erdos_hajnal_problem_list/_index|Komjáth 2025]]
records in its Problem 54 discussion next to the unknown case $k=3$ of
[[problems/set_theory/E1171/_index|Problem 1171]]: whether it is consistent that

$$
\alpha\not\to(\beta,4)^2
\quad\text{and}\quad
\alpha\to(\beta,3,3,3)^2
$$

hold together for some ordinals $\alpha,\beta$. The Problem 1171 page
quotes it in its dated assessment; that page records the status open, with
the erdosproblems.com label NOT DISPROVABLE and the not-disprovable side,
Baumgartner's relation under Martin's axiom, accepted as
[[problems/set_theory/E1171/claims/1989_01_01_baumgartner|a partial claim]], and
its ZFC question for $k\ge3$ is open. The second is
[[problems/set_theory/E0592/_index|Problem 592]], status `open`: determine the
countable $\beta$ with $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$.
Its page records the known boundary from Schipperus: yes for $\beta$ a sum of
one or two indecomposable ordinals
([[../library/set_theory/schipperus_2010_countable_partition_ordinals/theorem_28|Theorem 28]]),
no for a sum of four or more
([[../library/set_theory/schipperus_2010_countable_partition_ordinals/theorem_29|Theorem 29]],
part 3), and for a sum of three only the failure of the $4$-relation (Theorem
29, part 2), the $3$-relation being undecided. The outside status of that case
was checked against the report on the Isabelle formalization of ordinal
partition relations by Džamonja, Koutsoukou-Argyraki and Paulson
(arXiv:2011.13218, 2020; not held in the library, its text layer read from a
downloaded copy), which states Schipperus's theorem as its Theorem 2.2 and then
says that the case of at least three summands in the Cantor normal form is still
open; a web search found no later result, and the search covered that report and
the held sources only.

## Route and established inputs

- Lemma 2.1 of the deposit, reconstructed as
  [[research/erdos_1171/lemma_2_1_reconstruction|the color-reduction lemma]]
  (author-recorded): if $\alpha\to(\alpha,3)^2$ then
  $\alpha\to(\alpha,3,3,3)^2_4$, the case $k=3$.
- Theorem 29, part 2: $\omega^{\omega^\beta}\not\to(\omega^{\omega^\beta},4)^2$
  for every countable $\beta$ that is a sum of three indecomposable
  ordinals; the statement was read on the page images, and the proof
  (Theorem 32, p. 1214) was read and not checked.

The deduction (author-recorded on
[[research/erdos_1171/connections|the connections page]], section
"Problems 592 and 1171: four-clique versus triangle colors"): if
$\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ for some countable
$\beta$ that is a sum of three indecomposables, then with
$\alpha=\beta'=\omega^{\omega^\beta}$ both displayed relations hold, so the
pair $(\alpha,\alpha)$ answers Komjáth's question in ZFC, not merely
consistently. The interfaces match: the premise and Theorem 29, part 2, are
two-color relations in Schipperus's Definition 1, which is the lemma page's
relation at two colors, and Komjáth's $\alpha\to(\beta,3,3,3)^2$ is the
four-color relation of the lemma's conclusion at $k=3$; Komjáth asks for
some pair in some model and the deduction gives one pair in every model;
and the target $4$ of Theorem 29 is a four-element homogeneous set, the
four-clique of the question.

Two side facts narrow the candidates. The ordinal $\omega^{\omega^2}$ cannot
serve, because Larson proved $\omega^{\omega^2}\to(\omega^{\omega^2},4)^2$
(reported by Schipperus on p. 1197; Larson's paper is not held); what it gives
instead, from Theorem 29 part 1 and the lemma, is the ZFC instance
$\alpha\not\to(\alpha,6)^2$ with $\alpha\to(\alpha,3,3,3,3,3)^2_6$, and
with Larson's $\not\to(\alpha,5)^2$ the instance with $5$ against four
triangle colors. And every answer $(\alpha,\beta)$ to the question has
$\beta\not\to(\beta,4)^2$, since $\beta\to(\beta,4)^2$ would give
$\alpha\to(\beta,4)^2$ by restriction; so if $\beta$ is a partition
ordinal, $(\beta,\beta)$ is itself an answer, and the only other shape has
$\beta$ failing $\beta\to(\beta,3)^2$. That other shape contains the case
$k=3$ of Problem 1171 under CH: $(\omega_1^2,\omega_1\omega)$ is an answer
in a model of CH exactly when $\omega_1^2\to(\omega_1\omega,3,3,3)^2$ holds
there, by the negative relation of Baumgartner and Hajnal on the Problem
1171 page.

## Provisional premises

- The premise $\omega^{\omega^\beta}\to(\omega^{\omega^\beta},3)^2$ for some
  countable $\beta$ that is a sum of three indecomposables is open. No proof
  or refutation of that premise is supplied here. The color-merging lemma
  produces many-color relations from two-color ones and never supplies the
  required two-color relation.
- Theorem 29 part 2 is used at statement depth; its proof is not checked
  here.
- Larson's results are used only to exclude $\omega^{\omega^2}$ and for the
  sharper instance with $5$; both rest on Schipperus's report.

## The consequential gap

The premise is the whole gap: a proof or refutation of the $3$-relation at
$\omega^{\omega^\beta}$ for $\beta$ a sum of three indecomposables,
beginning with $\beta=3$ and $\alpha=\omega^{\omega^3}$.

## Next step

For the first case, the
[[research/erdos_592/successor_tree_interface|successor-tree interface]]
reconstructs the equal-block normalization from Erdős--Milner: a root-length
$2n$ block contains a color-0 copy of the $n$ block in a coloring with no
color-1 triangle. At $\beta=3$ every nonterminal node has a successor
ordinal label, so no collapsing-ladder maps are needed. The missing
construction must still make three complete games share the same trees,
with arbitrary strategy-prescribed sizes and sufficiently large labels.
The reconstruction is author-recorded and outside this lead's filed review.
The [[research/erdos_592/height_three_attack|height-three test]] isolates
a failed synchronization mechanism and an alternative schedule for the
same fixed strategy. It leaves both the general adaptive construction and
the transfer from a coherent successor game to the source theorems open.
Those obligations also lie outside this lead's filed review.

Attack $\omega^{\omega^3}\to(\omega^{\omega^3},3)^2$ with Schipperus's
machinery. The proof of Theorem 28 (p. 1212) reduces to the dichotomy of
Theorem 19, the homogeneous set of full type of Theorem 21 when every play
of the Builder wins, and the triangle of Lemma 26 when the Architect has a
winning strategy; the paper says that only Lemma 26 is sensitive to the
number of indecomposables, proving it for one summand and adapting it for
two on p. 1211. The first task is to determine whether Lemma 26, or a
replacement, survives a third summand, or whether the pattern method of
Theorems 31--33 yields a triangle-free coloring of $\omega^{\omega^3}$ with
no homogeneous set of full type. A positive outcome answers Komjáth's
question in ZFC and extends the positive boundary of Problem 592; a
negative outcome for every three-summand $\beta$ completes the
classification of Problem 592 as "at most two indecomposables" and returns
Komjáth's question to the shape with $\beta<\alpha$ or to the shape
$(\alpha,\alpha)$ at a partition ordinal whose four-clique relation is
undecided, such as $\omega^{\omega^\omega}$.

Everything here is author-recorded; its review standing is stated below,
and the lead changes the status of neither problem.

## Current review

The equal-block reconstruction and height-three interface above are outside
the filed review, so the expanded route needs an updated review. The
connection between the two partition questions was independently reviewed
on 2026-09-28 in the review
record
[[research/erdos_1171/evidence/verify/connections_problems_592_and_1171_four_clique_versus_triangl_review|the Problems 592 and 1171 review]]
(which covers the section of the connections page this lead files,
together with the lead's own sentences) and graded in
[[research/erdos_1171/evidence/verify/connections_grade|the grade]]. The
graded verdicts of the statements the route rests on are these. The core
deduction, that $\alpha\to(\alpha,3)^2$ with $\alpha\not\to(\alpha,4)^2$
gives $\alpha\to(\alpha,3,3,3)^2_4$ by Lemma 2.1 at $k=3$, so that
$(\alpha,\alpha)$ answers Komjáth's question in ZFC: refutation-failed.
Its instantiation through Theorem 29, part 2: refutation-failed for
countable $\beta$, the range Schipperus's paper covers, and unproved there
for uncountable $\beta$. The exclusion of $\omega^{\omega^2}$ by Larson's
$4$-relation, at the depth of Schipperus's report: refutation-failed. The
necessary condition $\beta\not\to(\beta,4)^2$ on every answer:
refutation-failed, with the omitted step $\beta\le\alpha$ supplied by the
review. The shape dichotomy, the CH instance and the ZFC instances at
$\omega^{\omega^2}$: refutation-failed. Three corrections were applied to
this page, so its current text differs from the reviewed text at those
places: C8 (the deduction sentence and the first provisional premise say
"countable $\beta$"), C9 (the interface sentence, refuted as worded
because Komjáth's $\alpha\to(\beta,3,3,3)^2$ has four colors, names the two
two-color relations and the four-color one) and C10 (the side
facts "narrow" rather than "fix" the candidates, and the negative outcome
in the next step returns Komjáth's question to the shape with
$\beta<\alpha$ or to the shape $(\alpha,\alpha)$ at a partition ordinal
whose four-clique relation is undecided, since Schipperus's Theorem 3
reads "at most two indecomposables" and $\beta=0$ has the property). The
same corrections were applied to the connections page; none is a step of
the route. After the review, the sentence on the Problem 1171 page's status
under "Target and status evidence" was reworded to that page's current
record; no statement, step or premise of the route changed. No tier is
assigned and the status of neither problem changes.
