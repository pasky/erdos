---
name: research/erdos_836/evidence/verify/linear_intersection/report
title: Independent examination of the E0836 edge-intersection argument
desc: >-
  Whole-statement examination of the frozen linear-intersection argument,
  including finite and infinite hypergraphs, recoloring, distinct edges,
  the uniform constant, and the two problem formulations.
created: 2026-10-14T15:03:48Z
updated: 2026-10-14T15:03:48Z
---

# Independent examination of the E0836 edge-intersection argument

***

## Subject and independence

**Examination date:** 2026-10-14 UTC. **Subject freeze:**
2026-10-14T11:26:16.490126+00:00. **Reviewer:** an independent adversarial
mathematical reviewer, model gpt-6-astra. The reviewer neither authored nor
collaborated on this argument and had no exposure to it before this examination.
The context began fresh, with the charge to find a false statement, missing
hypothesis, unsupported inference, quantifier error, or false consequence.
Project attribution is to Plasma AI.

The mathematical subject consists of these two preserved extractions and their
path/date/cut manifest:

- The [frozen problem formulations](../../assets/linear_intersection_subject/target.md)
  preserve the supplied extraction of
  `wiki/problems/graph_coloring/E0836/_index.md`. Their retained path is
  `wiki/research/erdos_836/evidence/assets/linear_intersection_subject/target.md`.
  All 20 lines were read; lines 3–18 display the two formulations.
- The [frozen argument](../../assets/linear_intersection_subject/argument.md)
  preserves the supplied extraction of
  `wiki/problems/graph_coloring/E0836/claims/2026_04_27_price.md`. Its retained
  path is
  `wiki/research/erdos_836/evidence/assets/linear_intersection_subject/argument.md`.
  All 39 lines were read: the conclusion and argument at lines 3–25, the Covers
  paragraph at lines 29–32, and the dependency statement at lines 36–37.
- The [subject manifest](../../assets/linear_intersection_subject/manifest.json)
  identifies the original paths, freeze time, and uniform `[cut]` marker. Its
  retained path is
  `wiki/research/erdos_836/evidence/assets/linear_intersection_subject/manifest.json`.

These are snapshots of the supplied extracts, not copies of the complete
original cards. The original paths identify provenance and were not opened.
The extraction's first, vertex-count question was visible but is outside this
examination. All coverage here concerns the second, edge-intersection question.
The mathematical subject is the recorded argument itself; fidelity to another
version of an external document is not asserted.

The frozen packet was checked against its supplied identity manifest before
mathematical reading and remained unchanged through the examination. The
subscription table was checked and was empty. No incoming communication,
author account, private plan, prior examination, sibling result, mathematical
history, other source, or web search was consumed. No excluded exposure occurred.
The review used its own continuation only. Agreement with a previous result or
with an author's computation supplies no part of the reasoning below.

The allowed mathematical reading was exactly the two extracts and their
manifest, and all of it was read. Operating reading was limited to the supplied
root AGENTS instructions; README.md; the introduction, Claims, Evidence, Tiers,
Naming and Project claims sections of `docs/anatomy.md`; all of
`docs/verification.md`, `docs/evidence.md`, `docs/math_authoring.md` and
`docs/weaving.md`; `campaign/AGENTS.md`; all of
`campaign/guides/verification.md`; the Reading section of
`campaign/guides/research.md`; and the verified commission, steps, configuration,
and native operating instructions. Operating links were not followed to other
mathematical material.

The independent derivations and exact witnesses are contained in this report.
The review uses no mathematical inputs beyond the frozen packet and ordinary
foundations. No computer calculation, executable mathematical checker, or
kernel proof carries the verdict. Reproduction consists of reading the
preserved extracts and checking the displayed derivations and finite sets
below; there is no mathematical rerun command or cached-success premise.

**Finding.** The stated non-2-colorable theorem, including its specialization
to chromatic number exactly 3 and uniform linear consequence, has verdict
**refutation-failed** under the conventions below. The first formulation's
parenthetical, if taken as the complete hypothesis of mere 3-colorability,
gives a false extension: **refuted-as-stated**. The frozen argument explicitly
acknowledges that distinction. These are separate scopes, not opposing verdicts
on the same proposition.

## Restatement and conventions

Let $r$ be any integer with $r\ge 2$. A hypergraph is a pair
$G=(V,\mathcal E)$, where $V$ is a set and $\mathcal E$ is a family of distinct
$r$-element subsets of $V$. The vertex set and edge family may be infinite.
Intersecting means that every two distinct edges meet. A proper $q$-coloring is
a map from $V$ to a set of $q$ colors with no monochromatic edge; it need not
use every available color. The coloring is of vertices, and properness does
not require every edge to use all $q$ colors. The equation $\chi(G)=3$ means
that a proper 3-coloring exists and a proper 2-coloring does not exist.

The proposition being assessed is:

> For every such intersecting hypergraph that admits no proper 2-coloring,
> there are distinct edges $E,F\in\mathcal E$ with
> $\lvert E\cap F\rvert\ge\lfloor r/2\rfloor$.

The finite and infinite cases are both included. Infinitary assertions are read
in ordinary classical set theory with choice; the exact compactness use is
proved below from Zorn's lemma. The finite argument requires no infinitary
compactness. No choice-free claim is made.

The numerical consequence to check is a constant independent of both $r$ and
$G$. The displayed bound gives the explicit all-order conclusion
$\lvert E\cap F\rvert\ge r/3$, so it implies the asserted $\gg r$ statement.
No extremal optimality claim for each value of $r$ is being added.

Isolated vertices are permitted by this proposition. Colors on isolated
vertices do not affect any edge, and the proof below restricts a finite
subhypergraph to the union of its edges. Thus the modified formulation's
requirement that every vertex lie in an edge is harmless for this conclusion.

The simple-hypergraph convention is sufficient for the statement. If repeated
edge occurrences are allowed instead, removing repeated copies leaves
colorability unchanged. Distinct supports obtained from the simple family
are also distinct occurrences; alternatively, two occurrences with the same
support already have intersection $r$. No counterexample is introduced by
that extension of convention.

The exact-chromatic-number condition implies the non-2-colorability hypothesis
immediately. In fact every nonempty intersecting $r$-uniform hypergraph with
$r\ge2$ has a proper 3-coloring: fix an edge $A$, give one vertex of $A$ color
2, the other vertices of $A$ color 3, and all vertices outside $A$ color 1.
The edge $A$ uses colors 2 and 3. Every different edge meets $A$ and, by equal
finite sizes and distinctness, also meets its complement, so it uses color 1
and another color. This is an elementary convention check, not a replacement
for the intersection-bound argument. Mere 3-colorability omits the essential
absence of a proper 2-coloring.

## Weakest steps

### 1. Compactness, finite minimality, and the optimized coloring

The frozen argument invokes compactness but does not include a separate proof
of the lemma whose proof it attributes to the note. The following is an
explicit foundational expansion of that invoked step. It does not certify
anything about an unseen document.

Suppose every finite edge subfamily of a hypergraph is properly 2-colorable.
Let $\Omega=\{0,1\}^V$. For each edge $e$, let $C_e\subseteq\Omega$ consist
of assignments nonconstant on $e$. Every finite intersection of sets $C_e$ is
nonempty: a coloring of the corresponding finite subhypergraph can be extended
by color 0 off its vertex set. These finite intersections generate a proper
filter on $\Omega$.

Consider the proper filters extending the generated filter, ordered by
inclusion. A nonempty chain has its union as a proper-filter upper bound,
because each finite collection of members lies together in one filter in
the chain; the generated filter itself is an upper bound for the empty chain.
Zorn's lemma therefore gives a maximal proper filter $\mathcal U$.
Maximality implies that for every $S\subseteq\Omega$, exactly
one of $S$ and $\Omega\setminus S$ belongs to $\mathcal U$. Both cannot
belong to a proper filter. If $S$ does not belong, adjoining it must make the
generated filter improper, so some member of $\mathcal U$ is disjoint from
$S$; upward closure then puts $\Omega\setminus S$ in $\mathcal U$.

For each vertex $v$, the two assignment sets specifying its two possible
colors partition $\Omega$. Give $v$ the color whose assignment set belongs
to $\mathcal U$. If an edge $e$ were monochromatic in this coloring, the
intersection of $C_e$ with those same-color assignment sets for all vertices
of $e$ would be empty. All these sets belong to $\mathcal U$, and there are
only finitely many of them because $e$ has $r$ vertices. This contradicts
properness of the filter. The resulting coloring is therefore proper on the
entire hypergraph. Contrapositively, a non-2-colorable hypergraph has a finite
non-2-colorable edge subfamily.

Apply this to $G$ and choose a non-2-colorable subfamily with the fewest edges
inside the resulting finite family. Denote it by $H$, with vertex set
$W=\bigcup_{e\in H}e$. Both $H$ and $W$ are finite, and $H$ remains
intersecting and $r$-uniform. This is a finite minimum, not an infinite
deletion procedure whose termination is assumed. The family has at least two
distinct edges: an empty family is colorable, and a single edge of size at
least two can be colored with both colors.

Fix $A\in H$. By minimality, $H\setminus\{A\}$ has a proper red-blue
coloring. Such a coloring must make $A$ monochromatic, since otherwise it
would color $H$ properly. Interchanging color names makes $A$ red. Among all
proper colorings of $H\setminus\{A\}$ with $A$ red, choose one with the
fewest blue vertices. This set of colorings is nonempty and finite. Write
$B\subseteq W$ for its blue vertex set.

Define

$$
t=\max\{\lvert E\cap F\rvert:E,F\in H,\ E\ne F\}.
$$

The set being maximized is nonempty and finite, so the maximum is attained
by distinct edges. Intersectingness and simplicity give $1\le t\le r-1$.
The word distinct in this definition is necessary: allowing $E=F$ would
instead give the useless value $r$. Reading the frozen paragraph's largest
intersection in the convention of its stated distinct-edge conclusion is
made explicit here.

### 2. The two recolorings and the incidence lower bound

Fix $x\in A$ and change just $x$ from red to blue. The edge $A$ is now
bichromatic because $r\ge2$. No new red monochromatic edge can be created
by this change. Since $H$ is not 2-colorable, some edge $F_x$ becomes
monochromatic blue. It must contain $x$, and all its other vertices were
already blue. Consequently

$$
F_x\cap A=\{x\},\qquad C_x:=F_x\setminus\{x\}\subseteq B,
\qquad \lvert C_x\rvert=r-1.
$$

Choose one such $F_x$ for each $x\in A$. These choices are finite. Distinct
values of $x$ give distinct edges, because their intersections with $A$
are different singletons. Also $F_x\ne A$.

Now fix any $b\in B$ and change just $b$ from blue to red. The edge $A$
stays red. Non-2-colorability of $H$ alone would say nothing useful about
this change: $A$ is already monochromatic. The relevant reason is instead
the minimum defining $B$. If the new coloring were proper on
$H\setminus\{A\}$, it would be an admissible coloring with one fewer
blue vertex. Therefore a new red monochromatic edge $G_b$ appears in
$H\setminus\{A\}$. It contains $b$, and all its other vertices were
originally red. In particular,

$$
G_b\cap B=\{b\},\qquad G_b\ne A,
\qquad \lvert G_b\cap A\rvert\le t.
$$

For every $x\in A\setminus G_b$, the edges $F_x$ and $G_b$ are distinct
and meet. Their common vertex cannot be $x$. Every other vertex of $F_x$
is originally blue, whereas $G_b$ has only the one originally blue vertex
$b$. Thus their intersection is exactly $\{b\}$, and $b\in C_x$.
It follows that the integer

$$
d(b):=\lvert\{x\in A:b\in C_x\}\rvert
\ge r-\lvert A\cap G_b\rvert\ge r-t.
$$

This holds for every blue vertex. It is valid for any fixed choices of the
$F_x$ and any allowed choice of each $G_b$; it does not require coordinated
choices or a common $G_b$. The possible equality $F_x=G_b$ when $r=2$
causes no problem: the comparison just made only uses $x\notin G_b$, which
already rules out that equality.

### 3. Double counting, integer rounding, and the linear consequence

Fix $x\in A$. For $y\ne x$, a common vertex of $F_x$ and $F_y$ must be
originally blue: their only originally red vertices are the different
vertices $x$ and $y$. Hence the following is an exact count of the pairs
$(y,b)$ with $y\in A\setminus\{x\}$ and $b\in F_x\cap F_y$:

$$
\sum_{y\in A\setminus\{x\}}\lvert F_x\cap F_y\rvert
=\sum_{b\in C_x}(d(b)-1).
$$

The subtraction of 1 removes the already counted membership of $b$ in
$C_x$. Each summand on the left is at most $t$, since $F_x\ne F_y$.
There are $r-1$ such summands. Each of the $r-1$ summands on the right is
at least $r-t-1$ by the incidence lower bound. Therefore

$$
(r-1)t\ \ge\ (r-1)(r-t-1).
$$

Because $r-1>0$, cancellation is valid, and $2t\ge r-1$. Since $t$ is an
integer,

$$
t\ge\left\lceil\frac{r-1}{2}\right\rceil
=\left\lfloor\frac r2\right\rfloor.
$$

The distinct pair attaining $t$ belongs to $H\subseteq\mathcal E$, so it
is the required pair in $G$. The argument neither substitutes a supremum
for an attained value nor silently includes an edge paired with itself.

The all-order linear factor is checked in the ratio actually claimed.
For even $r=2k$, the displayed lower bound divided by $r$ is $1/2$.
For odd $r=2k+1\ge3$, it is $k/(2k+1)\ge1/3$, because $k\ge1$.
Thus $\lfloor r/2\rfloor/r\ge1/3$ for every integer $r\ge2$, with
equality in this numerical comparison at $r=3$. This proves the claimed
linear scale with an absolute constant, not merely for large $r$.
It does not turn the integer bound into $\lvert E\cap F\rvert\ge r/2$
when $r$ is odd.

## Strongest attack and exact witnesses

### The blue recoloring cannot follow from noncolorability alone

The strongest attempted proof attack targeted the existence of $G_b$. After
changing a blue vertex to red, $A$ is still red, so a careless appeal to
noncolorability cannot force any other bad edge. The following exact finite
witness demonstrates this obstruction even without isolated vertices.

On $V=\{1,2,3,4,5,6,7\}$ take the seven triples

$$
123,\quad145,\quad167,\quad246,\quad257,\quad347,\quad356,
$$

where, for example, $145$ denotes $\{1,4,5\}$. Each vertex occurs in three
triples, and every pair of vertices occurs in exactly one triple. These facts
can be checked directly from the seven displayed sets. No two triples share
two vertices. For a fixed triple, its three vertices have six incidences with
the other six triples, at most one in each; therefore it meets every other
triple in exactly one vertex. In particular $t=1$.

This hypergraph is not 2-colorable. In a proper red-blue coloring each triple
would contribute exactly two pairs of differently colored vertices. Pair
uniqueness would then require 14 such pairs. If there are $a$ red vertices,
there are only $a(7-a)\le12$ such pairs, a contradiction. Deleting any edge
does give a proper 2-coloring: color that edge red and its complement blue.
Every remaining edge has one red vertex and two blue vertices. Thus this is
also an edge-minimal example of the kind used by the frozen argument.

Choose $A=123$ and initially color exactly $\{4,5,6,7\}$ blue. The
coloring is proper on $H\setminus\{A\}$, and $A$ is red. Changing vertex
4 to red keeps every other edge bichromatic. In the original coloring no
edge has 4 as its only blue vertex. Thus the asserted $G_4$ does not exist
for this admissible but nonminimal coloring.

This attacks an omitted-minimum shortcut, not the actual frozen hypothesis.
The coloring with blue set $B=\{5,6,7\}$ is proper on
$H\setminus\{A\}$ and has fewer blue vertices. It is minimal: at most
two blue vertices meet at most five of the seven triples, since each vertex
lies in three triples and any two vertices share exactly one triple. At least
two all-red triples would remain, including one other than $A$.

For this minimizing coloring the recoloring witnesses can be chosen as

$$
F_1=167,\quad F_2=257,\quad F_3=356,
\qquad G_5=145,\quad G_6=246,\quad G_7=347.
$$

Every $b\in B$ occurs in exactly two of the $C_x$, so $d(b)=2=r-t$.
The double-count bounds are both equal to 2, and $2t=r-1=2$.
The attempt to refute the recorded argument therefore fails precisely
because its minimum-blue condition supplies the missing force. That condition
is present in the frozen paragraph, not added by this review. The same witness
also refutes an attempted strengthening to $2t\ge r$ or intersection at
least $r/2$ for odd $r$.

### Endpoint, distinctness, and infinite-domain attacks

At $r=2$, the three edges $12,13,23$ on three vertices form an intersecting
non-2-colorable hypergraph with $t=1$. Noncolorability follows because two of
three vertices must receive the same one of two colors, and their pair is an
edge. Here the target bound is exactly 1. In the general derivation,
$r-1=1$ remains a legal divisor, recoloring one vertex of $A$ really makes
$A$ bichromatic, and the integer rounding still gives the correct bound.
The seven-triple witness supplies the odd endpoint $r=3$ and the lost unit
in $r-1$. These finite examples test boundary inferences; the universal
statement rests on the symbolic derivation, not extrapolation from examples.

The distinctness attack was to allow a repeated $F_x$ or to use the self-pair
in defining $t$. The singleton traces $F_x\cap A=\{x\}$ prohibit the
first, and the explicit distinct-pair maximum prohibits the second.
The only other intersection bounded by $t$ is $A\cap G_b$, and those edges
are distinct because $G_b$ contains the blue vertex $b$. No estimate uses
$t$ to bound an unverified distinct pair.

For infinite hypergraphs, minimizing the cardinality of an infinite blue set
would not justify a strict improvement after changing one vertex: an infinite
cardinality can stay unchanged. The frozen argument avoids that failure by
reducing to a finite non-2-colorable subhypergraph first. The foundational
derivation above supplies exactly that interface for arbitrary vertex sets.
Thereafter every minimum and count is finite. Extra isolated vertices have no
effect on the edge witnesses. No countable-enumeration assumption or finite
experimental evidence is substituted for this compactness step.

### The literal 3-colorability formulation has counterexamples

For each integer $r\ge2$, take a center $c$ and disjoint sets $X,Y$ of
$r-1$ vertices each, neither containing $c$. Let the entire edge family be

$$
E=\{c\}\cup X,\qquad F=\{c\}\cup Y.
$$

This finite hypergraph is $r$-uniform, intersecting, and has every vertex
in an edge. Its only distinct pair has intersection $\{c\}$. It has a
proper 2-coloring, with $c$ red and all other vertices blue, and also a
proper 3-coloring using all three colors: color $c$ with 1, $X$ with 2,
and $Y$ with 3. Its chromatic number is 2, not 3.

At $r=4$, its intersection size 1 is less than $\lfloor r/2\rfloor=2$.
For any proposed absolute constant $\gamma>0$, choosing an integer
$r>\max\{2,1/\gamma\}$ gives $1<\gamma r$. Thus no positive uniform
linear bound follows from mere 3-colorability, even when there are two
distinct edges and no isolated vertices. This independently establishes
the precise obstruction described in the frozen argument's star caveat.

There is also a separate distinctness obstruction: a hypergraph with one
$r$-element edge is properly 3-colorable but has no pair of distinct edges
at all. This is not needed for the quantitative counterexample, which has
two edges, but prevents treating distinct-edge existence as automatic under
the weakened hypothesis.

## Correspondence to the displayed questions

| Reading of the second question | Hypothesis relevant to this proof | Result |
| --- | --- | --- |
| First formulation, with chromatic number 3 in its standard exact sense | No proper 2-coloring | The bound applies; its second question has an affirmative answer. |
| First formulation, taking its parenthetical as the entire condition | Existence of a proper 3-coloring only | Refuted-as-stated by the two-edge family above; no uniform linear bound follows. |
| Modified formulation | Proper 3-coloring exists, proper 2-coloring does not, and every vertex lies in an edge | The bound applies. The extra vertex condition is not used for this question. |
| Argument's non-2-colorable formulation | No proper 2-coloring, with no finiteness or vertex-support restriction | The full bound follows, with the stated classical compactness foundation in the infinite case. |

The frozen Covers paragraph identifies the modified formulation and is
consistent with the proof. Its affirmative consequence must not be extended
to the literal weak parenthetical reading of the first formulation. The
frozen paragraph already records this qualification. Nothing here decides
the first, vertex-count question in either formulation.

## Premises, reconstruction, and actual reading

**Dependency reading at verdict filing, 2026-10-14 UTC:** the complete supplied
target and argument extracts, including their consequence and dependency
sentences, were inspected for actual premise consumption. No native L-claim
is cited or needed by this derivation. No live native dependency standing or
ledger was consumed. There is no pending native premise grade or batch
acceptance order on which this verdict rests.

The assumptions are finite integer $r\ge2$, uniformity, pairwise
intersection, absence of a proper vertex 2-coloring, and ordinary classical
foundations with choice for the infinitary compactness argument. The
non-2-colorability hypothesis is assumed as part of the conditional theorem;
this review does not decide colorability for arbitrary inputs.

| Consumed interface | Justification and reading depth |
| --- | --- |
| Finite-color compactness for constraints on finite edges | Explicitly invoked in the extract. An independent foundational derivation from Zorn's lemma is given in Weakest step 1. No external lemma proof was read. |
| Finite edge-minimal subhypergraph and a minimum-blue coloring | Derived in Weakest step 1 from finite minima and the assumed non-2-colorability. |
| Existence of both kinds of recoloring witness | Derived separately in Weakest step 2, using noncolorability for $F_x$ and minimum blue count for $G_b$. |
| Incidence multiplicity and distinctness | Derived in Weakest step 2 from actual vertex colors, intersection, and the distinct-pair definition of $t$. |
| Double count, cancellation, rounding, and uniform consequence | Exact finite identities and integer inequalities in Weakest step 3. |
| Correspondence to the problem formulations | The full supplied formulations were read. The stronger and weaker coloring conditions are distinguished and the weaker one has explicit counterexamples. |

The reconstruction is disclosed rather than attributed to the supplied
paragraph. It expands the invoked foundational compactness step, the finite
minimum, the two different reasons the recolorings fail, the incidence count,
and the integer and constant calculations. It also makes the distinct-pair
convention for $t$ explicit. These use the frozen argument's same sequence
$H,A,F_x,G_b,t$ and its displayed double count. No substantive new hypergraph
lemma or alternative proof route replaces a missing link. The strongest
attack above explains why the already stated minimum-blue condition matters.

The extract's assertion that the note proves its compactness lemma is not
independently verified as a statement about that note. Neither the note nor
the problem page's Notes section was supplied or read. Likewise the historical
attribution of an earlier $r/\log r$ bound is context, not a premise used to
prove this result, and has not been checked against external literature.
The linear consequence here is established directly. As a comparison of the
written scales alone, $(r/3)/(r/\log r)=\log r/3$ grows without bound; this
checks the claimed improvement in scale, not the historical theorem or its
attribution. No source-fidelity or external-source proof-coverage conclusion
is claimed.

## Checklist

The following tables cover both the Erdos-specific checklist and every
shared canonical failure mode and named pattern in `docs/verification.md`.
They assess the precise non-2-colorable proposition and separately record
the false weak-parenthetical extension.

### Erdos-specific checklist

| Item | Verdict and evidence |
| --- | --- |
| Quantifiers and scope | No defect in the theorem: arbitrary integer $r\ge2$, finite or infinite $G$, attained distinct pair, and all-order constant are covered. The literal 3-colorability extension fails by the explicit counterexample family. |
| Circularity | No defect found. Noncolorability is a stated hypothesis. Finite minimality and minimum blue count are constructed before the intersection bound, not deduced from it. |
| Model and convention changes | Exact vertex-coloring conventions and distinct supports are preserved through restriction to $H$. Replacing exact chromatic number 3 with mere 3-colorability is invalid and is not accepted. |
| Finite and statistical overreach | No defect found. The universal argument is symbolic; compactness, not finite testing, handles infinite $G$. The two small examples are diagnostic witnesses only. No statistical inference is used. |
| Uniformity | No defect found. The factor $1/3$ is independent of $r$ and $G$, and its proof covers both parities and the smallest allowed integers. No limits or infinite sums are interchanged. |
| Extremal conclusions | No defect found. The finite maximum over distinct pairs exists and is attained. The numerical ratio giving the linear factor is evaluated in its own units; no new per-$r$ optimality claim is made. |
| Consequences and composition | No missing interface remains under the stated foundations. Each recoloring has its correct justification, the incidence count is proved, and the final yes answer is restricted to the exact-chromatic-number reading or modified formulation. |
| Computation | No mathematical executable or numerical approximation is used. Exact counts and finite witnesses are fully displayed; certified bounds, stopping caps, failing program inputs, and nonzero program exits are inapplicable. |
| Reproduction | The derivations and complete witnesses are retained here with the exact extracts. No missing code, private mathematical input, cached output, or unexecuted claimed rerun is relied upon. |
| Source and verdict fidelity | Scope is explicit: the supplied record is examined, not an unseen note, historical theorem, Notes section, or prior review. Verdicts are stated in full, and grading is left separate. |

### Shared canonical failure modes

| Failure mode | Verdict and evidence |
| --- | --- |
| Almost all quietly upgraded to all | Not present. The argument and the constant calculation address every allowed integer, including 2 and 3. |
| Induction that presupposes termination | Not present. No iterative infinite deletion is used; the minimum is taken inside a finite family. The foundational Zorn argument is stated as such. |
| Probabilistic or averaging heuristics presented as proofs | Not present. The pair count is an equality of two finite enumerations, not a probabilistic estimate. |
| Circular use of an equivalent statement | No defect found. None of compactness, finite minimization, or recoloring assumes the target intersection bound. |
| Exceptional sets dropped from density arguments | Inapplicable: there is no density argument or discarded exceptional set. Boundary values and coloring conventions are addressed explicitly. |
| Finite verification cited beyond base-case coverage | Not present. The examples do not carry the universal conclusion; the general derivation does. |
| Relaxed or averaged convergence substituted for actual objects | Inapplicable: no relaxed dynamical or limiting system is used. The witnesses are edges of an actual subfamily of $G$. |

### Shared named patterns

| Pattern | Verdict and evidence |
| --- | --- |
| Model-class transport instead of entailment | No axiom-extension classification is attempted. The relevant entailment, exact chromatic number 3 implying non-2-colorability, is checked; the weak-parenthetical reverse substitution is explicitly refuted. |
| Uniformity over an infinite family inferred from finitely many instances | Not present. Uniformity in $r$ is proved by algebra, and arbitrary vertex sets are covered by the foundational compactness derivation. |
| Extremal claims checked in the claim's own units | Satisfied: the attained maximum is an intersection size, and the uniform consequence is checked as the exact ratio $\lfloor r/2\rfloor/r$. No neighboring count is substituted. |
| Consequence sentences are claim surfaces | Satisfied: the linear scale, integer rounding, yes answer, and weak-parenthetical caveat are checked separately. The odd endpoint prevents an unsupported replacement by $r/2$. |
| Carry hypotheses used by a quantified argument | Satisfied: finite $r$, finite $H$ and $W$, minimum blue count, noncolorability, distinctness, and intersectingness are each used at an identified step. The infinite case's foundational assumption is explicit. |
| Composition inherits unproved premises | No unproved native or external hypergraph premise is consumed. The invoked compactness interface is proved from stated foundations, and all finite bridges are derived. |
| Reproducibility notes are claims | No executable reproduction assertion is made. The mathematical input is the preserved extracts; the exact witness sets and derivations are present in the report. |
| Verifier quotations are claims | Inapplicable: no earlier verifier's report or ruling was supplied, read, or characterized. No verdict is inferred from the removed material. |
| Verdict words spelled in full | Satisfied: refutation-failed and refuted-as-stated are spelled out and attached to different explicitly named scopes. |
| Certified-bracket functions fail loudly | Inapplicable: no numerical routine, enclosure, periodic sampling window, or iteration cap is used. |
| A harness leg with no failing input is decoration | Inapplicable: there is no mathematical harness leg. The two-edge family and seven-triple system are explicit logical counterexamples to identified weakened or strengthened statements. |
| A gate reading caches instead of rerunning is defective | Inapplicable: no computational gate or cached success carries the verdict. Packet-identity checks establish the examined bytes, not the theorem. |

The neighboring correlated-sample discipline is inapplicable because there is
no statistical inference. Evidence coverage is as stated: a general finite
derivation, its explicit foundational extension to infinite hypergraphs, and
exact witnesses for the convention and inference attacks. The examination is
neither a computational batch nor a second review cycle; no claim of multiple
independent cycles is made.

## Verdict and grading

**Refutation-failed** for the complete frozen non-2-colorable
linear-intersection proposition, in ordinary classical foundations, and for
its application to the modified second question and to the first formulation
when chromatic number 3 has its standard exact meaning. The recorded proof's
specific recoloring-and-counting route survives the attacks above, with the
disclosed foundational and elementary inference expansions. The stated bound
is $\lfloor r/2\rfloor$ and gives the uniform factor $1/3$ for all $r\ge2$.

**Refuted-as-stated** for the extension obtained by treating the first
formulation's parenthetical, mere proper 3-colorability, as the entire
hypothesis. The displayed two-edge family is a counterexample to a uniform
linear bound; at $r=4$ it also contradicts the displayed floor bound. This
does not refute the frozen theorem, whose non-2-colorability hypothesis
excludes the witness, and agrees with the precise limitation the frozen
argument records.

No verdict covers the vertex-count question, any unprovided external document
or proof, historical attribution, a kernel formalization, or subsequent changes
to the subject. No native dependency standing was consumed. No substantive
missing mathematical interface remains for the scoped theorem under the
foundations stated here.

This report does not grade itself, assert a tier, or change standing. A grader
distinct from the author and reviewer must assess its independence, complete
contract, reconstructed inferences, coverage, and verdict before any acceptance
decision.
