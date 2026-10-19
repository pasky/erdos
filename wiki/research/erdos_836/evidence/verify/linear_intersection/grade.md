---
name: research/erdos_836/evidence/verify/linear_intersection/grade
title: Independent grade of the E0836 linear-intersection examination
desc: >-
  Separate grades for the non-2-colorable intersection theorem and the
  three-colorable counterexample, with the reconstruction ruling,
  independence evidence, exact coverage, and acceptance limits.
created: 2026-10-14T15:03:48Z
updated: 2026-10-14T15:03:48Z
---

# Independent grade of the E0836 linear-intersection examination

***

The [examined report](report.md) receives **pass** for each of its two
scoped verdicts. The first accepts the recorded mathematical argument with
its disclosed foundational expansion. The second accepts a refutation of
the weaker coloring formulation.

| Scoped conclusion | Report's verdict | Grade |
| --- | --- | --- |
| Every intersecting $r$-uniform hypergraph with no proper $2$-coloring, for every integer $r\ge2$, has distinct edges meeting in at least $\lfloor r/2\rfloor$ vertices. This includes arbitrary vertex sets in classical set theory with choice, the exact-chromatic-number-$3$ specialization, and the uniform linear consequence. | refutation-failed | **pass** |
| Existence of a proper $3$-coloring alone does not imply any uniform positive linear lower bound on the intersection of some two distinct edges. | refuted-as-stated | **pass** |

These grades warrant independent prose proof coverage of those exact
conclusions. They do not certify a proof in an unseen source, decide the
vertex-count question, or supply formal verification. No native claim tier
or corpus standing is changed by this grading record.

## Subject, assignment, and reading

**Grading date:** 2026-10-14 UTC. **Reviewer:** an independent adversarial
mathematical reviewer, model gpt-6-astra. **Grader:** a separate independent
grader, model gpt-6-astra, who neither authored nor collaborated on the
argument and did not conduct the original review. Both assignments began
in fresh contexts. The grader's only prior reading of this subject was
preparation within this same grading assignment. Project work is attributed
to Plasma AI.

The report graded here is
`wiki/research/erdos_836/evidence/verify/linear_intersection/report.md`,
examined in full, lines 1–546. Its submitted delivery was frozen at
2026-10-14T12:06:28.068191+00:00. The mathematical extraction was frozen at
2026-10-14T11:26:16.490126+00:00 and consists of:

- The [target extraction](../../assets/linear_intersection_subject/target.md),
  all 20 lines, preserving the displayed formulations from
  `wiki/problems/graph_coloring/E0836/_index.md`.
- The [argument extraction](../../assets/linear_intersection_subject/argument.md),
  all 39 lines, preserving the argument, Covers paragraph, and dependency
  statement from
  `wiki/problems/graph_coloring/E0836/claims/2026_04_27_price.md`.
- The [subject manifest](../../assets/linear_intersection_subject/manifest.json),
  read in full, recording those original paths, the freeze time, and the
  uniform cut marker.

The original cards were not opened. Their paths establish provenance;
coverage attaches to the preserved extracts and the examined report.
The launch and submitted mathematical copies were compared byte for byte.
The report and submitted inputs matched their frozen identities.

The actual original assignment was a whole-statement examination charged
to find a false statement, missing hypothesis, unsupported inference,
quantifier error, or false consequence. It covered the second question in
both displayed formulations, including finite and infinite scope. It
expressly permitted rederivation of ordinary foundations and elementary
finite combinatorics, required disclosure of reconstruction, and forbade
replacing a defective frozen argument with a new proof. It excluded the
first question and fidelity to another version of an external document.
Those terms, rather than any preferred result, govern this grade.

The grader also examined the frozen original assignment, original
operating records, primary isolation evidence, submitted inventory, and
the reviewer's continuation. The continuation was assessed as testimony,
not adopted as a grading decision. The original instruction snapshots
agree with the corresponding permitted guidance used here. No author
advocacy, outside assessment, original source document, other mathematical
page, or external formal artifact was supplied or read.

The governing standard is `docs/verification.md` in full, including
"Premises and source boundaries", "Whole-claim report", and the
Erdos-specific "Audit checklist", together with
`campaign/guides/verification.md` in full. Required corpus guidance and
the permitted evidence, authoring, and weaving guidance were also read.
Their examples and links were not followed to mathematical subjects.

## Independence ruling

**The independence requirement passes for both scoped conclusions.**
The record supports a separate, isolated review of the fixed extraction,
followed by a grader distinct from both author and reviewer. Using the
same disclosed model does not supply independence; the separation of the
assignments and their contexts does.

The primary records corroborate the frozen assignment and inputs,
disabled synchronization, sealed incoming communication, empty
subscriptions at the recorded preflight and terminal boundaries, and
disabled automatic memory and web search. The accepted operating settings
and original instruction snapshots agree. The supplied configuration
comparison shows no additional mathematical instructions or permitted
subject reads.

Both supplied communications were examined for content and direction. One
is an outbound administrative notice about interpreter invocation and
environment selection. It contains no mathematical steering. The other
is the reviewer's outbound result after the recorded delivery freeze.
Neither is an incoming author explanation, encouragement, reconciliation,
or sibling verdict. The interpreter-invocation deviation disclosed in the
first notice is not evidence that excluded mathematics was consumed.

The report and continuation state that no excluded content was received.
That testimony is consistent with the supplied primary records. The
report's mathematical content and attack choices can be accounted for
from the allowed extraction and the expressly permitted foundations;
no identified result or attack requires an excluded source. The
minimum-coloring attack actually tests a possible failure of the frozen
route, and the weak-formulation verdict preserves the refutation charge.
No documented exposure requires an immateriality exception, and this
grade does not invoke closing a channel as a cure for exposure.

There is a limit to this finding. The grading packet does not contain a
complete record of every reviewer read or every possible incoming
communication. The reviewer's own first-boundary and intermediate
subscription checks are reported in its continuation; the separately
supplied subscription receipts concern preflight and the terminal
boundary. Empty tables and isolation settings do not prove a universal
negative about reading. This grade accepts independence on the separated
assignment, those corroborating records, and the reviewer's disclosure;
it does not independently certify every historical no-read assertion.
No contrary exposure is established by the supplied evidence. The neutral
contract requires supported independence facts, not a public execution
transcript, and the absence of that complete transcript does not itself
void this report.

The grader's own subscriptions were empty at the initial boundary and
again before the substantive grading. No excluded communication or
material reached this grading context. Operational records remain private;
the facts and limits relevant to this ruling are stated here.

## Mathematical examination and reconstruction ruling

The report uses finite integer $r\ge2$, edges that are distinct
$r$-element subsets of a vertex set, and proper vertex colorings that
forbid monochromatic edges. A proper coloring need not use every
available color. It interprets $\chi(G)=3$ in its usual exact sense.
The following checks assess the report's existing derivations; they do
not supply a replacement proof for an incomplete examination.

The report also handles the convention extensions correctly. Repeated
occurrences of an edge can be removed without changing colorability;
two occurrences with the same support already intersect in $r$ vertices.
Colors on isolated vertices do not affect any edge, and the finite
argument uses only the union of its selected edges.

### Compactness and finite optimization

The interface invoked in the frozen argument is precise: absence of a
proper $2$-coloring implies a finite edge subfamily with the same absence.
The report's proof works for an arbitrary vertex set $V$. Its assignment
space $\{0,1\}^V$ is nonempty, since it contains a constant assignment.
Finite satisfiability of edge constraints gives a proper filter on that
space. The partially ordered collection of extending proper filters is
a set, and the union of a chain remains a proper filter. Thus the stated
application of Zorn's lemma is legitimate.

The resulting maximal filter selects exactly one cell of each two-cell
vertex-color partition. These selections define a color at every vertex.
If an edge were monochromatic, its constraint set and its selected
vertex-color cells would have empty intersection. They are all members
of the filter, and only finitely many are involved, because the edge
has $r$ vertices. This is the required contradiction. Neither countable
enumeration nor closure under infinite intersections has been assumed.

After this reduction, edge minimization occurs inside a finite family,
and the union of the selected edges is finite. An empty family and a
single edge are both $2$-colorable for $r\ge2$, so the family has distinct
pairs of edges. Deleting the chosen edge $A$ permits a proper coloring;
otherwise minimality fails. Every such coloring makes $A$ monochromatic,
or it would color the whole family properly. Swapping the two color
names makes $A$ red. The subsequent minimum blue count is over a nonempty
finite set of colorings, and is attained.

**Reconstruction ruling.** Compactness is an essential foundational
lemma for the report's infinite scope, and its proof is absent from the
extract. The report supplies an omitted proof of that explicitly invoked
lemma; this is more than a verbal explanation. It is nevertheless
admissible in this assignment: ordinary foundations were expressly
permitted to be rederived, the exact compactness interface is already in
the frozen route, the derivation is valid from the disclosed choice
foundation, and the report identifies its contribution without attributing
it to an unseen document. It does not insert a new hypergraph lemma or
replace the recoloring argument. The remaining finite minima are direct
expansions of choices already specified in the extract.

Accordingly the infinite result passes in ordinary classical set theory
with choice. No choice-free result is accepted. The finite result does
not require this compactness step. The extract's separate assertion that
the original note proves its own compactness lemma remains unchecked;
the report correctly refuses to certify that source assertion.

### The recoloring interface

The strongest proof attack is consequential: changing a blue vertex to
red leaves $A$ red, so noncolorability of the whole hypergraph cannot
force a new bad edge. The report identifies and tests this exact failure
mode. Its resolution is already present in the frozen subject: the
chosen coloring minimizes the number of blue vertices while being
proper on the other edges and leaving $A$ red.

For $x\in A$, making $x$ blue makes $A$ bichromatic and creates no new
all-red edge. Noncolorability therefore forces a newly all-blue edge
$F_x$ containing $x$ and no other point of $A$. In contrast, for a blue
vertex $b$, making $b$ red would reduce the blue count. Minimality forces
a newly all-red edge $G_b\ne A$, whose only originally blue vertex is
$b$. These are different reasons for failure of the two recolorings;
the report uses the correct reason in each case.

Put $C_x=F_x\setminus\{x\}$ and let $t$ be the largest intersection
size over distinct edges in the finite family. For each
$x\in A\setminus G_b$, intersectingness forces $F_x$ to meet $G_b$.
Their common point cannot be $x$, and any other point of $F_x$ was blue.
It must therefore be $b$. Consequently

$$
d(b):=\lvert\{x\in A:b\in C_x\}\rvert
\ge r-\lvert A\cap G_b\rvert\ge r-t.
$$

The pair $A,G_b$ is distinct because $b\notin A$. The pairs $F_x,F_y$
are distinct for $x\ne y$, because their traces on $A$ differ. The
argument using $F_x,G_b$ assumes $x\notin G_b$, which also makes that
pair distinct, even when $r=2$. No coordinated selection of recoloring
witnesses is needed. These checks close the claimed interface using
exactly the frozen hypotheses.

The report's distinct-pair definition of $t$ makes explicit the
convention required by the frozen distinct-edge conclusion. Allowing
self-pairs would make $t=r$ and would not furnish the desired distinct
witness. The accepted reading is the distinct-pair reading explicitly
recorded in the report; this is not an additional hypergraph hypothesis.

### Counting, endpoints, and the linear scale

For fixed $x$, every common vertex of $F_x$ and $F_y$ with $y\ne x$ is
originally blue. Counting its other occurrences gives

$$
\sum_{y\in A\setminus\{x\}}\lvert F_x\cap F_y\rvert
=\sum_{b\in C_x}(d(b)-1).
$$

There are $r-1$ terms on each side, each left term is at most $t$, and
each right term is at least $r-t-1$. Subtracting one is necessary because
$b$ already belongs to $C_x$. Since $r-1>0$,

$$
(r-1)t\ge(r-1)(r-t-1),\qquad
t\ge\left\lceil\frac{r-1}{2}\right\rceil
=\left\lfloor\frac r2\right\rfloor.
$$

The maximum is attained by a distinct pair in the finite subfamily,
hence by edges of the original hypergraph. All counts occur after the
finite reduction. Minimizing an infinite blue cardinality would not
justify removing one blue vertex; that invalid alternative is excluded.

For even $r$ the ratio $\lfloor r/2\rfloor/r$ is $1/2$; for
$r=2k+1\ge3$ it is $k/(2k+1)\ge1/3$. The constant is independent of
both $r$ and the hypergraph. The triangle gives a valid endpoint at
$r=2$; it has no proper $2$-coloring and maximum distinct-edge
intersection one. The report does not replace the floor by $r/2$ for
odd $r$ or infer a universal bound from these finite examples.

### The retained seven-edge diagnostic

The seven triples in the report are
$123,145,167,246,257,347,356$. Their unordered pairs are respectively

$$
\begin{gathered}
\{12,13,23\},\ \{14,15,45\},\ \{16,17,67\},\\
\{24,26,46\},\ \{25,27,57\},\ \{34,37,47\},\\
\{35,36,56\}.
\end{gathered}
$$

These are all 21 pairs of seven vertices without repetition, and every
vertex occurs in three triples. For any fixed triple its vertices have
six incidences with the other six triples, at most one in each, so all
distinct triples intersect in exactly one vertex.

A proper two-coloring would contribute two bichromatic vertex pairs
from each triple, thus 14 in total. Pair uniqueness makes this a count
of distinct pairs. A coloring with $a$ red vertices has only
$a(7-a)\le12$ bichromatic pairs. This proves noncolorability without
assuming a known property of the example. Coloring one triple red and
its complement blue properly colors all other triples, proving the
edge-deletion claim as well.

With $A=123$, the blue set $\{4,5,6,7\}$ is admissible but can be
reduced to $\{5,6,7\}$. In that reduced coloring the blue intersections
of the six other edges are, in their displayed order,
$\{5\},\{6,7\},\{6\},\{5,7\},\{7\},\{5,6\}$.
Thus recoloring 4 from the former blue set produces no new monochromatic
edge, exactly as the report claims. No edge previously had 4 as its only
blue vertex.

At most two blue vertices can meet at most five of the seven triples:
two distinct vertices each meet three triples and share one. Therefore
at least two triples would remain red, including one other than $A$.
The reduced three-vertex blue set is minimal. Its chosen $C_x$ are
$\{6,7\},\{5,7\},\{5,6\}$, so every blue degree is two and both
sides of the double count are two. The stated $G_5=145$, $G_6=246$, and
$G_7=347$ each have the required single blue vertex. This verifies the
diagnostic and why it defeats the shortcut, not the frozen proof. It
also gives $t=1$ at $r=3$, refuting the stronger replacement $t\ge r/2$.

## The weaker formulation and its verdict

The refutation is quantified correctly. For each integer $r\ge2$, let
$X,Y$ be disjoint sets of size $r-1$ and take exactly the two edges
$E=\{c\}\cup X$ and $F=\{c\}\cup Y$, with $c$ outside both sets.
The edges are distinct, uniform, and intersect in precisely one vertex.
Every vertex lies in an edge. Coloring the center red and the petals
blue is proper, and coloring the center, $X$, and $Y$ with three
different colors is also proper and uses every color.

The intersection ratio is $1/r$. For every proposed positive absolute
constant $\gamma$, an integer $r>\max\{2,1/\gamma\}$ makes
$1<\gamma r$, and $r$ can also be chosen beyond any prescribed
threshold. This disproves a uniform linear bound, including an eventual
one. The $r=4$ member also violates the displayed floor bound.
The report's separate single-edge example correctly defeats automatic
existence of a distinct pair under mere colorability, but is not needed
for the quantitative refutation.

These witnesses have chromatic number two. They therefore refute only
the reading that uses the first parenthetical as its entire hypothesis.
They do not refute the exact-$\chi=3$ theorem. The modified formulation
explicitly excludes proper two-colorings, so the theorem applies to it;
its condition on isolated vertices is unnecessary for this conclusion.
The standard exact reading of the first formulation also implies the
theorem's hypothesis. The report preserves all these distinctions.

The report's additional convention check, that an intersecting uniform
hypergraph with a nonempty edge family is three-colorable for $r\ge2$,
is valid: split a fixed edge into two nonempty colors and color its
complement with the third. A different edge meets both the fixed edge
and its complement, by intersection and equal finite sizes. This check
does not erase the difference between exact chromatic number and mere
colorability.

## Premises and source boundaries

**Dependency reading at grading, 2026-10-14 UTC:** the complete preserved
target, argument, and report, including their consequence sentences,
were examined for actual premise consumption. No native L-claim is used
as a premise, and no live claim ledger or dependency standing was read.
The reviewer's dated finding of no native dependency is supported by
these bytes. There is no pending premise grade or batch acceptance order.

The noncolorability, uniformity, intersection, and integer-range
conditions are explicit hypotheses of the theorem. They are not claims
that the reviewer was required to establish for every possible input.
All finite combinatorial interfaces used in the proof are derived in
the report. Zorn's lemma is used as an ordinary foundational principle
under the expressly stated classical choice assumption. The resulting
compactness interface was read and checked in proof depth; no external
proof of compactness was read.

The unseen note, the original page's Notes section, and the sources for
the historical $r/\log r$ attribution are outside both examinations.
The reviewer declares them unread, and the grader did not open them.
Their accepted reading depth is **unread**. They are not theorem premises:
the proof does not depend on the old bound or on the truth of an account
of what the note contains. The comparison of written scales is elementary, but
does not verify that historical theorem or its attribution. This grade
does not discharge an independent source-proof reconstruction or source
fidelity obligation for any unavailable document.

## Complete report contract

The report contains the required subject/independence account,
restatement, checklists, three weakest-step reconstructions, strongest
attack, premise reading, and scoped verdicts. Their adequacy was checked
against the mathematics above, not inferred from heading or row counts.

| Contract part | Non-2-colorable theorem | Weak-colorability refutation |
| --- | --- | --- |
| Subject and independence | Exact extracts, paths, freeze time, conventions, allowed reading and exclusions are specified; independence passes with the evidentiary limit stated above. | The same frozen target and independence record apply; the weaker reading is identified explicitly. |
| Restatement | All $r\ge2$, finite or infinite vertex sets, no proper two-coloring, distinct witnesses, and the floor bound are preserved. | The section on literal three-colorability states and negates the proposed uniform bound by quantifying over every positive constant. |
| Checklist | Every applicable deduction and qualification is addressed; the checklist review below finds no missing required coverage. | The tables identify the failed formulation, and the counterexample section checks its hypotheses, distinctness, and uniform quantifier; common inapplicable modes remain inapplicable. |
| Weakest steps | Compactness, finite minima, the two recolorings, and their composition with the count are rederived. | The constructed edges, proper coloring, exact intersection, and $1/r$ ratio are explicitly derived in the counterexample section. No missing bridge is supplied by this grade. |
| Strongest attack | The minimum-blue attack has an exact diagnostic and an explanation of why the actual frozen condition withstands it. | The two-edge family is a successful attack on the claimed linear conclusion, not merely on a proposed proof. |
| Premises | Foundations and elementary interfaces are disclosed; no native or external hypergraph theorem is silently imported. | The construction and its checks use only elementary finite sets and integer choice; no theorem verdict is needed as a premise. |
| Verdict and limits | refutation-failed with the infinite-foundation and source boundaries retained. | refuted-as-stated only for the weak reading, not for the non-2-colorable theorem. |

The shared organization does not conceal an unexamined second claim:
the counterexample section supplies the refutation's own derivation,
quantifiers, witness, and limitations. Repeating the administrative
sections or the inapplicable computational items would add no coverage.
This grade is not a second independent review cycle, and neither verdict
relies on computation. No distinct computational reproduction route or
claim of multiple complementary review cycles is being substituted.

## Checklist grading

The Erdos-specific checklist is controlling. Each item was checked for
both scoped conclusions.

| Item | Theorem assessment | Refutation assessment |
| --- | --- | --- |
| Quantifiers and scope | Complete, including arbitrary vertex sets, distinct edges, $r=2$, odd rounding, and isolated vertices. | The family works for every $r\ge2$ and defeats every positive uniform constant; it is confined to the weak reading. |
| Circularity | No target bound is used in constructing the finite minimum or the recoloring witnesses. | All witness properties are proved directly; the claimed theorem is not assumed. |
| Model and convention changes | Restriction to a finite subfamily preserves uniformity and intersection; the pair convention is explicit. | Proper three-colorability is checked without silently imposing exact chromatic number three. |
| Finite and statistical overreach | Compactness and symbolic counting support the universal claim; small examples only test inferences. | The symbolic family, not a finite sample of it, disproves uniformity. No statistical inference is used. |
| Uniformity | The factor $1/3$ is independent of both parameters and proved in both parities. | The exact ratio $1/r$ tends below any proposed positive constant by an explicit integer choice. |
| Extremal conclusions | The finite distinct-pair maximum exists and is attained. No general sharpness assertion is added. | The family has exactly one distinct edge pair, so its maximum intersection is exactly one. |
| Consequences and composition | Every displayed bridge and the linear consequence survives; scope and foundations are carried through. | The counterexample defeats the weak second question but has no bearing on the excluded vertex-count question or the noncolorability hypothesis. |
| Computation | No executable mathematics or numerical approximation is used; program failure cases and certified numerical caps are inapplicable. | Exact sets and counts suffice; the same computational items are inapplicable. |
| Reproduction | Full derivations and exact inputs are retained; no cached success or absent code carries the verdict. | The complete parametric witness and all checks are present in the report. |
| Source and verdict fidelity | The report's reconstruction is disclosed; no external-source or kernel finding is accepted. | The full verdict refuted-as-stated is attached to the weak formulation only. |

The shared canonical failure modes were also checked individually:

| Failure mode | Grading finding for both scopes |
| --- | --- |
| Almost all upgraded to all | Absent: the theorem covers every allowed integer, and the counterexample family has the stated full parameter range. |
| Induction presupposing termination | Absent: the theorem takes finite minima after compactness; the refutation uses no induction. |
| Probabilistic or averaging heuristics as proofs | Absent: the double count is an exact identity and the witness arguments are deterministic. |
| Circular use of an equivalent statement | Absent: the compactness interface, coloring choices, and witness properties do not assume either conclusion. |
| Exceptional sets dropped from density arguments | Inapplicable: neither argument uses density or discards an exceptional set. |
| Finite verification beyond its coverage | Absent: neither universal parameter statement is extrapolated from the diagnostic examples. |
| Relaxed convergence substituted for actual objects | Inapplicable: no relaxed or convergent surrogate is used; all edges are actual edges of the claimed hypergraphs. |

The shared named patterns have the following separate findings:

| Pattern | Grading finding |
| --- | --- |
| Model-class transport instead of entailment | No axiom-system classification is attempted. Exact chromatic number implies noncolorability; mere colorability does not. Both uses are checked directly. |
| Infinite-family uniformity from finitely many instances | Absent: the theorem uses an algebraic ratio bound and the refutation an explicit family for arbitrary $r$. |
| Extremal claims in their own units | Satisfied: maximum intersections and the ratios $\lfloor r/2\rfloor/r$ and $1/r$ are the quantities actually checked. |
| Consequence sentences as claim surfaces | Satisfied: integer rounding, the linear consequence, the affirmative exact-chromatic answer, and the negative weak answer are checked separately. |
| Carry hypotheses used by quantified arguments | Satisfied: finite $r$, the finite vertex union, minimum blue count, distinctness, and the infinite-case choice foundation remain explicit. The weak family meets its own stated hypotheses. |
| Composition inherits unproved premises | No unproved hypergraph interface is imported. The essential compactness proof is supplied within the original permission and retains its foundational qualification. |
| Reproducibility notes are claims | The report's retained-input and noncomputational-reproduction descriptions agree with the delivered mathematics. Administrative receipts are not mathematical checks. |
| Verifier quotations are claims | No earlier mathematical verdict supports the report. This grade checked its characterizations and submitted verdicts against the unchanged report. |
| Verdict words spelled in full | Satisfied: refutation-failed and refuted-as-stated name different conclusions throughout. |
| Certified-bracket functions fail loudly | Inapplicable: there is no bracket routine, approximation, periodic sampling window, or numerical cap. |
| A harness leg needs a failing input | Inapplicable: there is no mathematical executable leg. The explicit witnesses genuinely defeat the identified shortcut and weakened or strengthened statements. |
| A gate must rerun rather than read caches | Inapplicable to the mathematical warrant: it uses no gate or cached success. Byte checks only identify the frozen subject. |

The neighboring correlated-sample discipline is inapplicable. Evidence
coverage was checked against the actual finite argument, its stated
foundational extension, and the complete counterexample family. No
required source, computational leg, or mathematical case is left
unexamined within that scope.

## Accepted coverage and retained evidence

The **pass** on **refutation-failed** accepts the preserved
recoloring-and-counting route, including the permitted compactness
derivation, as independent prose proof coverage for the non-2-colorable
theorem. It accepts the exact-$\chi=3$ and modified-formulation
specializations and the uniform factor $1/3$. It does not assert that
the short extract itself contains the unseen note's full proof.

The **pass** on **refuted-as-stated** accepts the supplied family as a
disproof of the uniform linear claim under mere three-colorability. It
does not refute the theorem with noncolorability or settle the ambiguous
first formulation by silently choosing one meaning of its parenthetical.

No acceptance extends to the first vertex-count question, external
source fidelity, historical attribution, an external or native Lean
artifact, a choice-free infinite theorem, a later edited argument, or an
unexamined native claim. No report repair is required for these grades;
the qualifications above control the weight of its existing findings.

The mathematical keepers are the unchanged report, both exact extracts,
their path/date manifest, and the derivations and checks in this grade.
They use no mathematical executable, private computational input, or
cached output. Reproduction consists of checking the retained arguments
and finite sets at the named paths. Public reliance requires those files
to be preserved together in their stated durable homes; a private
delivery by itself is not a corpus warrant.
