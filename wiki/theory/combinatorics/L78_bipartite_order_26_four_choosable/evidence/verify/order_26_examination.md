---
name: theory/combinatorics/L78_bipartite_order_26_four_choosable/evidence/verify/order_26_examination
title: Independent examination of four-choosability through order 26
desc: >-
  Whole-conclusion adversarial examination of the frozen order-26 argument,
  with an independent exact derivation of its compact table, full evidence
  replay, failure-exit probes, scope qualifications, and dependency findings.
created: 2026-10-15T00:04:51Z
updated: 2026-10-15T00:04:51Z
---

# Independent examination of four-choosability through order 26

***

## Subject and independence

**Mathematical verdict: refutation-failed.** The frozen argument establishes
four-choosability for every bipartite graph with at most 26 vertices and the
catalog consequence $n(4)\ge27$. This is an examination, not a grade, tier
assertion, or acceptance decision. The final weighting sentence and the
metadata validator have the scope qualifications below; neither is a gap in
the proof of these conclusions from the frozen integer inputs.

The reviewer is an independent mathematical examiner, with disclosed model
GPT-6 Astra. The examiner neither authored nor collaborated on the subject and
had no prior exposure to it beyond the assignment. The examination began in a
fresh context, with synchronization disabled and communication channels sealed.
The subscription table was checked before mathematical reading and again at
subsequent boundaries; it was empty. That check supports isolation but does not
by itself establish what was read. The actual reading is specified below.

The subject was frozen on **2026-10-14 at 20:34:18 UTC**. The UTC examination
date is **2026-10-14**. Its original claim directory is
`wiki/theory/combinatorics/L78_bipartite_order_26_four_choosable/`.
The following table gives original paths relative to that directory and their
assessed snapshots relative to its `evidence/assets/review_subject/` directory.

| Original subject path | Assessed snapshot | Reading depth |
| --- | --- | --- |
| `_index.md` | `statement.md` | Entire supplied statement extraction; standing and other excluded card text were not supplied or read. |
| `_proof.md` | `proof.md` | Entire supplied proof, including conventions, all reductions, both tables, and the section on the origin of the weights. |
| `evidence/_index.md` | `evidence.md` | Entire supplied mathematical evidence description and rerun claims. |
| `evidence/main.py` | `evidence/main.py` | Entire program and complete default and optimized executions. |
| `evidence/produce.py` | `evidence/produce.py` | Entire source as provenance only; never imported or executed. |
| `evidence/util/certificate.py` | `evidence/util/certificate.py` | Entire helper implementation. |
| `evidence/assets/compact_certificate.json` | `evidence/assets/compact_certificate.json` | Entire retained input. |
| `evidence/assets/certificates.json` | `evidence/assets/certificates.json` | Entire retained input, including every ordered split. |
| `evidence/assets/controls.json` | `evidence/assets/controls.json` | Entire retained input. |

The remaining original subject is
`wiki/problems/graph_coloring/E0629/_index.md`, represented by
`evidence/assets/review_subject/catalog_question.md` in the claim directory.
Only its supplied question and definition of $n(k)$ were read, in full.
The [subject manifest](../assets/review_subject/manifest.json) records the
original repository-relative paths, freeze time, and uniform omission marker
`[cut]`. The assessed subject is the prepared extraction, not the excluded
parts of those original pages.

The manifest was read before the mathematical files. Their exact identities
were verified before reading, after resumption, and at delivery. The three
Python files arrived with an administrative `.txt` suffix; removing only that
suffix materialized the executable files without changing any bytes. The
snapshots preserve the supplied extraction exactly. No argument or input was
repaired. This report covers those snapshots, not later changes to the original
paths.

Allowed supporting reads were the commissioned operating guidance, the
rendered commission and steps, accepted configuration, the examiner's own
continuation, and the pinned `tools/`, `pyproject.toml`, and `uv.lock`
infrastructure. Actual guidance reading covered `README.md`; the introduction,
Claims, Evidence, Tiers, Naming, Project claims, Claim scrutiny, and Authoring
and checks in `docs/anatomy.md`; all of `docs/verification.md`,
`docs/evidence.md`, `docs/math_authoring.md`, `docs/weaving.md`,
`campaign/AGENTS.md`, and `campaign/guides/verification.md`; and Reading in
`campaign/guides/research.md`. The supplied root `AGENTS.md`, installed
operating skills, and relevant configuration and step instructions were also
used. Their identities were checked against the operating manifest before
reading. Infrastructure inspection included the imports in `tools/__init__.py`,
the core and CLI package initializers, constants and utility initializer, and
the complete `Checker` and `evidence_parser` in `tools/core/harness.py`.
The actual imported tools package was the verified package.

No canonical claim card, ledger, external source, network search, author's
working context, inbox, prior examination, sibling report, or excluded
communication was read. General guidance links were not followed into the
corpus. No excluded-content exposure is observed. Preparation used more
simultaneous file-reading calls than commissioned; this was disclosed, and every
file involved remained in the allowed read set. Its contract significance is
left to the distinct grader. No mathematical advice or reconciliation was
received during the examination.

The independent mathematical leg is the explicit derivation below. The
independently designed [failure-exit keeper](check_failure_exits.py) tests the
runtime claims; it is not a second implementation of the weighted arithmetic.
Its exact inputs are the retained subject files. The report's intended durable
path is
`wiki/theory/combinatorics/L78_bipartite_order_26_four_choosable/evidence/verify/order_26_examination.md`,
and the keeper's is the sibling `check_failure_exits.py`. Reproduction
instructions appear below. Project mathematics is attributed to Plasma AI;
the source-method attribution remains as supplied and is not independently
verified bibliographic coverage.

## Restatement

For every finite bipartite graph $G$ with $|V(G)|\le26$, and every function
$L$ assigning to each vertex a set of exactly four colours, there exists a
function $c$ on the vertices such that $c(v)\in L(v)$ and $c(u)\ne c(v)$
whenever $uv$ is an edge. The colour universe need not be fixed in advance.
Distinct vertices may have equal lists, and vertices on the same side may use
equal colours. Empty graphs and bipartitions with an empty side are included.

With $n(4)$ the least vertex count of a bipartite graph whose list chromatic
number exceeds four, the asserted consequence is $n(4)\ge27$. No exact value,
general-$k$ result, novelty assertion, complete catalog solution, literature
acceptance, or formal-proof acceptance is examined or inferred.

## Weakest steps and the complete reduction

The three weakest links selected for attack are: the passage to a minimum
palette and then to distinct lists; the transfer from bad assignments to the
weighted inequality and its complete list-type domain; and the exact compact
arithmetic with its small strict margin. The following derivation places them
in the whole argument, including the initial and final transfers.

### From all graphs to a minimum bad palette

Suppose a permitted graph and assignment were bad. Add isolated vertices with
four-element lists to reach 26 vertices, extend a bipartition, and add all
cross edges. Any colouring of the resulting $K_{a,b}$ restricts to a colouring
of the original graph. Thus this transformation preserves badness in the
direction needed for the contradiction. It does not assert the converse for
arbitrary subgraphs. An empty side gives an edgeless graph, which is colourable
by choosing one colour from each nonempty list. Swapping sides changes neither
badness nor list size, so take $1\le a\le b$ and $a+b=26$.

Let $P$ be the finite union of the lists. A colouring of $K_{a,b}$ determines
$T\subseteq P$, the colours used on its left side. Every left list meets
$T$, while each right vertex must use a colour outside $T$, so no right list
is contained in $T$. Conversely, these two properties let each left vertex
choose from its intersection with $T$ and each right vertex choose from its
difference with $T$. Completeness of the cross edges makes the forward
implication valid, and the disjoint colour pools make the reverse implication
valid. No distinct-list assumption is used here.

For this fixed $K_{a,b}$, the set of palette sizes of bad assignments is a
nonempty set of positive integers, each at most $4\cdot26=104$. It therefore
has a minimum. This elementary existence argument is implicit in the frozen
proof and is made explicit here; it is not a search or a termination
assumption.

In a minimum-palette bad assignment, suppose $x,y$ never share a list.
Identifying $y$ with $x$ leaves every list with four distinct elements and
decreases the palette size by exactly one. Given a colouring of the identified
assignment, change its colour $x$ back to $y$ precisely at vertices whose
original list contained $y$. Every chosen colour then belongs to the original
list. Applying the identification map to any equality between two lifted
colours gives equality of their identified colours, so an edge cannot become
monochromatic. A colouring of the smaller assignment would therefore lift to
one of the original assignment. This contradicts minimality. Every unordered
pair of palette colours must consequently occur together in a list.

### Every palette case and the duplicate-list attack

Count list occurrences, including repetitions at this stage. Pair coverage
implies

$$
\binom N2\le26\binom42=156.
$$

Since $\binom{19}2=171$, this gives $N\le18$. For each colour, the lists
containing it cover at most three partner colours per occurrence. Its degree
in the list-incidence relation is at least $\lceil(N-1)/3\rceil$. Summing
gives $104\ge N\lceil(N-1)/3\rceil$. At $N=18$ the right side is 108,
excluding that case.

For $N\le6$, partition the palette into two parts of size at most three.
Every four-element list meets both, and either part supplies the required
subset $T$. Palette sizes below four cannot support even one four-element
list, so no extra small-palette exception is hidden here.

For $N\ge7$, on the layer of $l$-element subsets the total number of left
misses and right containments is

$$
a\binom{N-4}{l}+b\binom{N-4}{l-4}.
$$

Badness requires every such subset to have an event. Adding the bounds for
$l$ and $N-l$ and using $a+b=26$ yields

$$
26\left(\binom{N-4}{l}+\binom{N-4}{l-4}\right)
\ge2\binom Nl.
$$

Here and throughout, an out-of-range lower binomial index gives zero. The
following exact calculation independently checks all eight small layers.

| $N$ | $l=\lfloor N/2\rfloor$ | $\binom Nl$ | $\binom{N-4}{l}+\binom{N-4}{l-4}$ | Required lower bound on 26 |
| --- | --- | --- | --- | --- |
| 7 | 3 | 35 | 1 | 70 |
| 8 | 4 | 70 | 2 | 70 |
| 9 | 4 | 126 | 6 | 42 |
| 10 | 5 | 252 | 12 | 42 |
| 11 | 5 | 462 | 28 | 33 |
| 12 | 6 | 924 | 56 | 33 |
| 13 | 6 | 1716 | 120 | $143/5$ |
| 14 | 7 | 3432 | 240 | $143/5$ |

Every last-column value is greater than 26. This excludes precisely
$7\le N\le14$, not larger palettes by extrapolation.

At $N=15$, the layers $l=7,8$ give $330a+165b\ge6435$ and
$165a+330b\ge6435$. Dividing by 165 and substituting $a+b=26$ gives
$a,b\ge13$, hence $a=b=13$. Equality holds in the layer counts, so each
7-subset would have exactly one event. Two left list occurrences have union
size at most eight and hence have a common disjoint 7-subset. That subset has
two events, including if the two lists were equal. This is a contradiction.

At $N=16$, the 8-layer has total event count
$26\binom{12}4=26\cdot495=12870=\binom{16}8$. Again every subset would
have exactly one event. A side with two list occurrences exists. If they are
left lists, their union leaves at least eight colours outside it; if they are
right lists, their union fits in an 8-subset. In either case an 8-subset has
two events. Thus $N=16$ is excluded without assuming distinct lists.

Only $N=17$ remains. Now collapse equal four-element sets among the 26 lists
and let $q$ be the number of distinct sets. Pair coverage is unchanged by this
collapse. Each colour belongs to at least $\lceil16/3\rceil=6$ distinct
sets, so $4q\ge102$ and the integer $q$ is at least 26. Since there are only
26 occurrences, $q=26$. All lists are distinct, also across the two sides.
This defeats the attempted escape through repeated lists; distinctness was
proved after, rather than assumed during, the minimal-palette reduction.

For $T=A_1$, no right event is possible: a four-element right list contained
in $A_1$ would equal it. Badness therefore supplies a left list disjoint from
$A_1$. Likewise $T=P\setminus B_1$ rules out a left event and supplies a
right list disjoint from $B_1$. Thus both sides have at least two vertices.
After side symmetry, $2\le a\le13$. Relabel the two disjoint left lists as
$U=\{0,1,2,3\}$ and $V=\{4,5,6,7\}$, leaving a nine-element set $W$.
This relabeling is a bijection of colours and changes no colouring condition.

### Weighted transfer and completeness of its domain

Let $\mathcal S$ consist of all palette subsets meeting both $U$ and $V$.
Their two fixed left lists have no miss event on $\mathcal S$. For a bad
assignment, each $T\in\mathcal S$ must therefore have an event among the
remaining $a-2$ left and $b$ right lists. Multiplying this pointwise fact by
nonnegative $w(T)$ and interchanging finite sums gives

$$
Z\le\sum_{i=3}^a\ell(A_i)+\sum_{j=1}^b r(B_j)
\le(a-2)L+bR.
$$

Here $Z=\sum_Tw(T)$ and $L,R$ are the maxima of the miss and containment
weights over the allowed remaining lists. Multiple events increase the right
side; neither disjointness nor probabilistic independence of events is
assumed. A zero weight causes no difficulty. Global distinctness excludes the
two fixed lists from every remaining position. Maximizing over *all* other
four-subsets only enlarges the upper bound; it does not assume that arbitrary
maximizers coexist in a realizable assignment.

Write a list type as $(x,y,z)$ with $x+y+z=4$, counting its elements in
$U,V,W$. The compact weights are invariant under interchanging $U,V$, so take
$x\ge y$. The possibilities are $x=0$ with $y=0$; $x=1$ with $y=0,1$;
$x=2$ with $y=0,1,2$; and $x=3$ with $y=0,1$. The sole $x=4$ case is a
fixed list and is excluded. The eight type multiplicities, including the
interchange, are respectively

$$
126,\ 672,\ 576,\ 432,\ 432,\ 36,\ 72,\ 32.
$$

Their sum is 2378, equal to $\binom{17}4-2=2380-2$. This independently
checks both type completeness and the mask enumeration's intended domain.
The unrestricted profile domain for $T\in\mathcal S$ is
$1\le t_1,t_2\le4$, $0\le t_3\le9$, containing 160 profiles. The compact
input assigns positive weights to ten of them and zero to every other one.

## Independent exact arithmetic

This section derives the compact table without using the author's arithmetic
functions or subset transforms to obtain its entries. The shared combinatorial
identity is justified by direct choices; the displayed intermediate integer
contributions make the numerical leg independently reproducible on paper.
Agreement between the two algorithms in the supplied program is not used as
the independence warrant.

Group the ten individual profiles into six symmetric groups, named $A$ through
$F$ in the following order. An interchange contributes a second profile only
when the first two coordinates differ.

| Group | Profile and interchange | Weight | Exact multiplicity | Contribution to $Z$ |
| --- | --- | --- | --- | --- |
| $A$ | $(1,1,6)$ | 7 | $4\cdot4\cdot84=1344$ | 9408 |
| $B$ | $(1,2,5)$ | 3 | $2\cdot4\cdot6\cdot126=6048$ | 18144 |
| $C$ | $(1,2,6)$ | 1 | $2\cdot4\cdot6\cdot84=4032$ | 4032 |
| $D$ | $(1,3,4)$ | 8 | $2\cdot4\cdot4\cdot126=4032$ | 32256 |
| $E$ | $(2,3,3)$ | 4 | $2\cdot6\cdot4\cdot84=4032$ | 16128 |
| $F$ | $(3,3,2)$ | 6 | $4\cdot4\cdot36=576$ | 3456 |

Thus $Z=9408+18144+4032+32256+16128+3456=83424$.

For type $(x,y,z)$ and profile $(t_1,t_2,t_3)$, disjointness leaves
$4-x,4-y,9-z$ available colours in the three parts. Containment already uses
$x,y,z$ prescribed colours and leaves $t_1-x,t_2-y,t_3-z$ choices to fill.
Consequently the two unweighted counts for that individual profile are

$$
\binom{4-x}{t_1}\binom{4-y}{t_2}\binom{9-z}{t_3},
\qquad
\binom{4-x}{t_1-x}\binom{4-y}{t_2-y}\binom{9-z}{t_3-z}.
$$

The following tables expose the six *weighted* contributions to each row.
Each entry already includes the interchange belonging to its group.

| Type | $\ell_A$ | $\ell_B$ | $\ell_C$ | $\ell_D$ | $\ell_E$ | $\ell_F$ | $\ell$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $(0,0,4)$ | 0 | 144 | 0 | 1280 | 1920 | 960 | 4304 |
| $(1,0,3)$ | 84 | 540 | 30 | 1920 | 1440 | 360 | 4374 |
| $(1,1,2)$ | 441 | 1134 | 126 | 1680 | 840 | 126 | 4347 |
| $(2,0,2)$ | 392 | 1008 | 112 | 2240 | 560 | 0 | 4312 |
| $(2,1,1)$ | 1176 | 1512 | 252 | 1120 | 224 | 0 | 4284 |
| $(2,2,0)$ | 2352 | 1512 | 336 | 0 | 0 | 0 | 4200 |
| $(3,0,1)$ | 784 | 1008 | 168 | 2240 | 0 | 0 | 4200 |
| $(3,1,0)$ | 1764 | 1134 | 252 | 1008 | 0 | 0 | 4158 |

| Type | $r_A$ | $r_B$ | $r_C$ | $r_D$ | $r_E$ | $r_F$ | $r$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $(0,0,4)$ | 1120 | 720 | 480 | 256 | 0 | 0 | 2576 |
| $(1,0,3)$ | 560 | 810 | 360 | 768 | 120 | 0 | 2618 |
| $(1,1,2)$ | 245 | 630 | 210 | 1008 | 504 | 54 | 2651 |
| $(2,0,2)$ | 0 | 420 | 140 | 1344 | 448 | 48 | 2400 |
| $(2,1,1)$ | 0 | 210 | 56 | 896 | 1008 | 288 | 2458 |
| $(2,2,0)$ | 0 | 0 | 0 | 0 | 1344 | 864 | 2208 |
| $(3,0,1)$ | 0 | 0 | 0 | 1792 | 672 | 192 | 2656 |
| $(3,1,0)$ | 0 | 0 | 0 | 1008 | 1008 | 648 | 2664 |

For example, at $(1,0,3)$ the six miss contributions use remaining part sizes
$(3,4,6)$. They are

$$
7(3)(4)(1),\quad
3(3\cdot6+3\cdot4)(6),\quad
(3\cdot6+3\cdot4)(1),
$$

$$
8(3\cdot4+1\cdot4)(15),\quad
4(3\cdot4+1\cdot6)(20),\quad
6(1)(4)(15),
$$

giving $84,540,30,1920,1440,360$. At $(3,1,0)$, containment kills the first
three groups because they choose fewer than three colours in the first part.
The others contribute
$8\binom94=1008$, $4\cdot3\binom93=1008$, and
$6\cdot3\binom92=648$, giving 2664. These examples check the shifts in the
containment formula, rather than only totals at a symmetric type.

It follows that $L=4374$, attained for instance by
$X=\{0,8,9,10\}$, and $R=2664$, attained by
$X=\{0,1,2,4\}$. The maxima have been checked in the claimed units of event
weight and on the full admissible domain. Their maximizing lists need not be
simultaneously present in an assignment.

For $2\le a\le13$, the upper bound on the actual event sum is

$$
(a-2)4374+(26-a)2664=1710a+60516\le82746.
$$

Its maximum is at $a=13$, and $83424-82746=678>0$. This contradicts the
pointwise covering inequality. Thus no bad assignment on any completed
order-26 bipartite graph exists. Restriction then proves the statement for
every original graph of order at most 26.

## Consequence, auxiliary claims, and strongest attack

### The catalog minimum

If a graph is $k$-choosable, it is $q$-choosable for $q\ge k$: choose a
$k$-subset of each assigned $q$-list and apply the former property. A finite
graph on $m\ge1$ vertices is $m$-choosable by greedily colouring its vertices,
since each step forbids at most $m-1$ colours. Hence the catalog condition
$\chi_L(G)>4$ is exactly failure of four-choosability.

The minimum's nonempty domain can also be checked elementarily. Take four
left vertices with disjoint four-element lists. For each choice of one colour
from each left list, put a right vertex whose list is exactly those four
colours, and join all cross edges. Every colouring of the left side blocks
the right vertex corresponding to its four chosen colours. This is a finite
bipartite non-four-choosable graph, so a least vertex count exists by
well-ordering. This construction is only a check of the word “least”; it is
not an investigation of the sharp value or of order 27.

The main argument excludes every order at most 26 in that minimum's domain;
therefore $n(4)\ge27$. The explicit well-ordering, list-size monotonicity,
finite greedy bound, and nonemptiness arguments are routine elementary
reconstructions not spelled out in the frozen text. No additional theorem
from the literature or native claim is being substituted for a missing
substantive link.

### Auxiliary scope and the origin of the weights

The auxiliary JSON supplies one weighting for every $a=2,\ldots,24$ with
$b=26-a$. The full checker replay covers all of them, including the asymmetric
ones. The universal proof above consumes only the compact certificate and
$2\le a\le13$ after side symmetry. Auxiliary certificates do not extend the
theorem to a different order or replace the structural reduction.

The 160 profile weights, with nonnegative auxiliary variables bounding the two
event maxima, give the linear program described in the proof. The supplied
discovery source constructs those linear inequalities and the normalization.
It was read, not run. No optimum, solver status, floating-point calculation,
or provenance of a search result is a premise of this examination.

The claimed rounding relationship is checkable from the retained balanced
auxiliary row alone. Scaling its largest weight to 8 gives, for the profiles
$(1,1,6)$, $(1,2,5)$, $(1,2,6)$, $(1,3,4)$, $(2,3,3)$, $(2,4,1)$,
and $(3,3,2)$ before their interchanges and zero entries are handled,

$$
7.410808,\ 2.919120,\ 1.009312,\ 8,\ 3.813624,\ 0.395712,\ 5.991392.
$$

These terminating decimals are exact rational values. Rounding gives
$7,3,1,8,4,0,6$, with the stated interchanges, precisely the
compact input. Thus this relationship does not require executing optimization.
It makes no optimality or uniqueness claim about the compact weights.

For the full 8-layer of the 17-colour palette, a left list has
$\binom{13}8=1287$ miss events and a right list has
$\binom{13}4=715$ containment events. At $(13,13)$ this gives
$13(1287+715)=26026>\binom{17}8=24310$. The simple full-layer count therefore
does not contradict badness, as stated.

There is a scope qualification to the closing sentence that the weighting
“has to concentrate” on subsets meeting the two fixed lists. In this proof,
restriction to $\mathcal S$ is the specified device that removes their events.
The text does not establish a necessity theorem about all possible weighted
proofs. In particular, an interpretation requiring zero weight outside
$\mathcal S$ is false: extend the compact weighting to all palette subsets
and give $\varnothing$ one extra unit of weight. The new total is 83425.
The two fixed left lists each gain one event unit, every other left event
weight gains one, and right event weights do not change. The full event bound
is therefore at most $1711a+60516\le82759<83425$. The same strict
contradiction still holds. This exact perturbation limits that wording; it
neither refutes the stated theorem nor supplies a replacement for a defective
step in its proof.

### Strongest attempted refutation

The strongest attack sought an assignment outside the numerical domain:
repeated lists surviving palette minimization, an unhandled palette endpoint,
or an omitted four-list type whose event weight exceeded the proposed maximum.
Such an escape would invalidate the all-assignments conclusion despite a green
checker. It failed because the incidence argument forces all 26 lists to be
distinct only after the palette is exactly 17; the equality-layer arguments
explicitly tolerate repetitions; the two disjoint fixed lists then follow
from the subset criterion; and the eight types exhaust all 2378 remaining
four-subsets. Independently expanding every event row gives a positive
worst-case gap of 678 in the exact units used by the covering inequality.

Separate attacks challenged colour-identification lifting, empty sides,
side symmetry, the direction of graph completion, and the catalog consequence.
Their resolutions are given above. The executable attack below targets a
different failure surface: a checker that reports success after a domain,
coverage, arithmetic, or control failure, especially under optimized Python.
This is one independent examination with multiple attacks, not a claimed
second independent review cycle.

## Computational inspection and reproduction

### What was replayed

The complete materialized `main.py` was executed freshly in ordinary Python
and with `python -O`, using the verified root tools package and numpy. Both
exited zero. All compact-table checks, every auxiliary split from $(2,24)$
through $(24,2)$, both bad controls, every singleton-profile control and their
uniform versions, the colourable deletion control, the noncertifying uniform
weighting, and all listed malformed controls executed. This coverage comes
from reading and executing the complete entry point, not from a cached success
summary or an assertion count. There is no reduced mode.

The environment used Python 3.14.6 and numpy 2.5.3, the latter matching the
lock-file branch for Python at least 3.12. A full run took about a second in
this environment; the negative-test keeper took several seconds. These are
approximate reproduction expectations, not performance guarantees.

The entry point reads the three retained JSON assets. It does not read
discovery output, a solver receipt, a previous report, or a cached result.
`produce.py` is not imported. The imported evidence helpers resolve beside the
materialized program, preserving the supplied layout.

### Algorithm and integer-domain audit

The profile vector is indexed by every mask from zero to $2^n-1$. It assigns
the specified weight to a subset with that exact profile, and zero otherwise.
The row validator rejects negative and noninteger weights, booleans in rows,
repeated profiles, and profiles outside the fixed-list domain. Every allowed
profile has positive binomial multiplicity. Before allocating the int64 weight
array it computes, with Python integers, the sum of weight times multiplicity
and rejects a total larger than the int64 maximum. Thus each stored weight is
itself bounded by that total.

For processed bit set $I$, the subset transform at $S$ equals the sum of
$w(T)$ over $T\subseteq S$ with $S\setminus T\subseteq I$. The superset
transform equals the sum over $T\supseteq S$ with $T\setminus S\subseteq I$.
Processing a new bit partitions the terms according to that bit, so each
update adds disjoint sets of terms. At completion, querying the complement of
$X$ in the subset transform gives its miss weight, and querying $X$ in the
superset transform gives its containment weight. The advanced-index updates
read the opposite bit class, which is not being updated in that operation.
All terms are nonnegative, and every intermediate sum is at most the
validated total. This proves the int64 sums cannot overflow on the accepted
domain. The later conservative product guard in `split_bound` is additional
protection; side coefficients and returned bounds are Python integers for the
retained inputs. Independently, every retained auxiliary weight is at most
$10^6$ and $|\mathcal S|=(2^4-1)^2 2^9=115200$, so its total is at most
$115200000000$ and 26 times its total is at most $2995200000000$,
well below $2^{62}$. The actual retained domain is far from the overflow limit.

The actual data has palette size 17, list size four, order 26, and the two
specified fixed lists. Comparing the sorted split pairs to the complete
expected list detects missing and repeated splits. `itertools.combinations`
enumerates every four-subset once and excludes exactly the two fixed masks.
The independent multiplicity calculation above checks its intended size.
The program's correctness here concerns these retained inputs and documented
helper domains, not arbitrary calls with malformed Python container types.

**Metadata validation limit.** Side counts are compared by numeric equality,
not checked with a strict integer-type predicate. Replacing the balanced row's
two side counts by `13.0` is accepted in both execution modes, as the retained
keeper confirms. Such a call evaluates the side-coefficient expression using
floating-point operations, although this particular mutation still represents
the same small integer calculation exactly. Therefore the validator must not
be characterized as enforcing integer types for arbitrary JSON side metadata.
The frozen file has integer side counts throughout, and its replay uses Python
integer coefficients. No false certificate or error in its computed bounds is
asserted from the broader validation limitation.

`assignment_masks` requires integer colour and list sizes, nonempty sides,
the stated list size, distinct colours within a list, and in-palette integer
colour labels; bool colour labels are rejected. It permits repeated lists at
different vertices. The particular controls are separately checked to have
distinct lists. Its bounded witness domain is not asserted as the reduction
for arbitrary graphs.

The $K_{2,4}$ control is bad because any subset meeting its two disjoint
2-lists contains one of their four cross pairs, which is a right list. The
3-list control is checked over all $2^9=512$ subsets by the frozen exhaustive
criterion. The singleton-profile checks cover all $k^2(n-2k+1)$ profiles:
four in the 2-list case and 36 in the 3-list case. Their total weights are
positive, so the comparison used to select the minimum event-to-weight ratio
loses no zero-denominator case. Nonnegative linear combinations then preserve
the event-cover inequality for these profile weightings.

Deleting the first right list of the 3-list control has an explicit witness:
$T=\{2,3,4,8\}$. In the retained left-list order one may use
$(4,2,2,3,3,2,3,8)$; in the remaining right-list order one may use
$(5,5,1,5,6,0,0,5,0)$. Each entry belongs to its list, and the two colour sets
are disjoint. Thus the badness control is tested against a mathematically
colourable neighboring input, not only against declared bad data.

### Actual failure exits

`check_failure_exits.py` copies the exact frozen checker and helper, changes
only the specified asset in a temporary directory, and executes the complete
checker. It runs sequentially in both ordinary and optimized Python. The
keeper itself was executed with optimization enabled. Its checks use
`Checker`, not removable Python assertions.

| Changed input | Expected failure surface | Observed exit in each mode |
| --- | --- | --- |
| None: exact baseline copies | Complete positive control | 0 |
| First compact weight changed from 7 to 6 | Compact total and event arithmetic | 1 |
| Compact order changed to 25 | Declared compact domain | 1 |
| Balanced auxiliary weighting replaced by an empty weighting | Strict covering inequality becomes $0<0$ | 1 |
| Auxiliary split with left size 24 removed | Complete side-split coverage | 1 |
| Balanced side counts changed to `13.0`, `13.0` | Numeric equality accepts them; records the metadata-type limit | 0 |
| First right list removed from the declared bad 3-list control | Exhaustive badness test on the colourable witness above | 1 |
| First compact weight changed to $-1$ | Negative-weight rejection | 1 |
| First compact weight changed to $2^{62}$ | Python-integer total rejects overflow before array conversion | 1 |
| First compact weight changed to $0.5$ | Noninteger-row rejection | 1 |
| A colour label in the 2-list control changed to `true` | Invalid assignment label | 1 |

For every negative case the keeper also checks the intended diagnostic, so an
unrelated import failure cannot count as a successful probe. Some failures
are accumulated checks and some are uncaught validation exceptions; both
produce nonzero exits. The shared `Checker.finish()` returns one after any
failed check and after zero checks, and zero only for a nonempty successful
run. The entry point returns that value through `sys.exit`. Inspection and
the actual negative executions support the optimized-Python claim.

The accepted floating-point metadata probe is a limit finding, not a negative
input claimed to be rejected. The keeper's mutations are deterministic
functions of the exact retained assets. Those assets, the checker source, the
helper source, and the keeper itself therefore preserve every required probe
input without storing output logs or relying on private scratch. This leg
would fail if the baseline failed,
a specified rejection were missed, the recorded metadata behavior changed, or
a run failed for a different reason.

### Clone-relative reruns

The complete subject remains under the claim's
`evidence/assets/review_subject/`; rerun that snapshot rather than a later
canonical checker. From a clone's repository root with its declared tools and
numpy environment prepared, use:

```sh
l78_subject=wiki/theory/combinatorics/L78_bipartite_order_26_four_choosable/evidence/assets/review_subject
l78_keeper=wiki/theory/combinatorics/L78_bipartite_order_26_four_choosable/evidence/verify/check_failure_exits.py

env -u VIRTUAL_ENV OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 10 uv run --no-sync python "$l78_subject/evidence/main.py"
env -u VIRTUAL_ENV OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 10 uv run --no-sync python -O "$l78_subject/evidence/main.py"
env -u VIRTUAL_ENV OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 10 uv run --no-sync python -O "$l78_keeper" --subject "$l78_subject" --work-dir tmp/l78_failure_exit_review
```

During the examination these invocations addressed freshly materialized exact
copies at the permitted working location. They were also executed with the
displayed relative paths in a minimal layout of the proposed retained files,
using the verified root project environment. Both full runs and the keeper
exited zero there. This checks the retained layout and commands, not integration
of an entire new clone. The excluded canonical source command was not executed
against a live card tree. No source code or asset changes are required to rerun
the retained files.
The keeper writes and removes temporary fixtures only below the supplied
working directory. The paper derivation needs only the compact weighting and
the explicitly displayed binomial calculations.

## Premises

At verdict filing on **2026-10-14**, the dependency finding was derived again
from the complete frozen statement, proof, consequence, code, and input scope:
**no native L-claim is consumed as an established premise**. L78 identifies
the subject itself. No ledger read was needed or made, and there is no pending
dependency grade or batch acceptance order.

The proof's Hanson, MacGillivray and Toft reference identifies a method and
locates Lemmas 1–3 and Theorem 1 on pages 184–187. Reading depth of that
external source is **unread**: it is outside the commissioned set. Its citation
and bibliographic accuracy are not verified here. The exact mathematical
interfaces required by the present proof—colour identification, pair and
incidence coverage, layer-event counts, and the weighted covering
inequality—are derived from the supplied text and elementary finite counting
in this report. Thus no unread source theorem is used as a premise.

The catalog extraction supplies the definition of list chromatic number and
$n(k)$, not a proof or a status ruling. The compact certificate supplies ten
explicit integer weights, whose needed properties are derived above. The
auxiliary certificates and controls are retained finite inputs, all replayed
at their stated scope. Discovery correctness is not a premise.

The elementary foundations used are finite set counting, the binomial
coefficient convention, well-ordering of nonempty sets of natural numbers,
finite choice, and the elementary graph and list-colouring definitions.
There is no conditional hypothesis about a conjecture, solver completeness,
statistical model, or unverified inventory. No additional external theorem
interface or substantive missing lemma was found.

## Checklist

### Erdos-specific checklist

| Item | Verdict and basis |
| --- | --- |
| Quantifiers and scope | Survives. The reduction starts with an arbitrary graph and arbitrary four-element lists, permits duplicate lists initially, treats empty sides and all smaller orders, and only then uses justified palette and side restrictions. |
| Circularity | Survives. Minimum palette exists by well-ordering; identification reduces it while preserving badness. No target-equivalent result is assumed. |
| Model and convention changes | Survives. Graph completion is used in the correct restriction direction; the subset criterion is proved for the completed graph; list occurrences are distinguished from distinct sets until distinctness is established. |
| Finite and statistical overreach | Survives. The finite table is connected to every hypothetical bad assignment by the complete palette reduction. There are no sampled probabilities or statistical independence claims. |
| Uniformity | Survives. Order is bounded by 26, every list has size four, and arbitrary colour labels reduce to a palette of size 17 in a minimal counterexample. No assertion is extrapolated in order or list size. |
| Extremal conclusions | Survives. Both event maxima are attained by explicit admissible lists; the affine bound is maximized at $a=13$; the catalog minimum is in vertex counts and has a nonempty domain. No sharp value of $n(4)$ is claimed. |
| Consequences and composition | Survives. The all-graphs and $n(4)$ consequences are separately derived. Every consumed property of the list inventory is supplied. The final wording about weight concentration has the explicit nonessential scope qualification above. |
| Computation | Survives on the frozen integer domain. Exact retained inputs, full mask ranges, Python-integer prebounds, nonnegative int64 transforms, meaningful negative cases, and observed nonzero exits are documented. Side-metadata type validation has the explicit limit above. No numerical enclosure or iteration-cap result is involved. |
| Reproduction | Survives within the commissioned materialization. Both full modes were freshly executed; the independent runtime keeper and all inputs are retained. The path substitution from the excluded canonical command is explicit. |
| Source and verdict fidelity | Survives at the examined boundary. Source attribution is not elevated to inspected source proof. No prior verifier ruling was supplied or quoted. The mathematical verdict is written in full and carries no grading or tier assertion. |

### Shared canonical modes

| Canonical failure mode | Disposition |
| --- | --- |
| “Almost all” upgraded to “all” | Absent. Every palette subset is quantified in the criterion; no exceptional assignment is discarded. |
| Induction presupposing termination | Inapplicable as induction. The only minimality argument uses a nonempty bounded set of integer palette sizes; a one-step strict reduction suffices. |
| Probabilistic or averaging heuristics presented as proofs | Absent. Every weighted inequality follows from a pointwise cover and finite nonnegative sums. |
| Circular use of an equivalent statement | Absent. The colouring/subset equivalence is proved in both directions, not invoked as a prior theorem establishing existence. |
| Exceptional sets dropped from density arguments | Inapplicable as density. Low palettes, equality cases, empty sides, fixed lists, zero weights, and repeated lists are explicitly handled. |
| Finite verification cited beyond base-case coverage | Absent. The precise structural reduction proves that the displayed finite domain is complete for the claimed order bound. |
| Relaxed or averaged convergence substituted for actual objects | Absent. No convergence result is used; explicit weights give a deterministic contradiction for actual bad assignments. |

### Named patterns

| Named pattern | Disposition |
| --- | --- |
| Model-class transport instead of entailment | Absent. All changes of graph, palette, and subset representation have explicit implication directions. No model-class classification or axiom extension is claimed. |
| Infinite-family uniformity from finitely many instances | Absent. Infinite possible colour names are handled by relabeling and palette minimality, not sampled; no bound uniform in unbounded graph order is asserted. |
| Extremal claims in their own units | Satisfied. Exact event weights, their maximizing types, the vertex-count minimum, and the gap 678 are checked in their stated coordinates. |
| Consequence sentences as claim surfaces | Satisfied. Graph restriction, $n(4)\ge27$, rounding, and the failed full-layer bound are checked separately. A universal support-necessity interpretation of the final wording is expressly declined with a witness. |
| Hypotheses used by a quantified argument | Satisfied. Four-element sets, 26 list occurrences, pair coverage, distinctness, disjoint fixed lists, nonnegative weights, and $2\le a\le13$ are established before use. |
| Composition inherits unproved premises | No missing consumed premise found. Elementary interfaces are derived locally; neither source acceptance nor an optimizer is imported. |
| Reproducibility notes are claims | Satisfied with the disclosed path mapping. Fresh full replays and negative exits cover the documented modes and controls; no cached count is treated as evidence. |
| Verifier quotations are claims | Inapplicable to this blind subject. Prior reports and standing characterizations were excluded, and none is asserted here. |
| Verdict words spelled in full | Satisfied: refutation-failed for the examined theorem and consequence. No ambiguous abbreviation is used. |
| Certified-bracket functions fail loudly | Inapplicable. There is no enclosure routine, tolerance, convergence test, or iteration cap. Integer overflow is instead prevented before conversion. |
| A leg with no failing input is decoration | Satisfied. The retained negative mutations fail at arithmetic, coverage, domain, badness, and validation surfaces in both modes. The colourable control has an explicit colouring witness. |
| A gate reading caches instead of rerunning is defective | Absent. No broad gate is relied on; the relevant checker and keeper were executed from exact source and inputs and read no success cache. |

The neighboring statistical discipline is inapplicable: no correlated samples
or statistical inference occur. The evidence-coverage discipline is applied
throughout: code checks finite arithmetic and controls, while the written
argument supplies the all-graphs bridge. Neither leg is assigned the other's
coverage.

## Verdict and grading

**Refutation-failed** for the whole frozen assertion of four-choosability
through order 26 and $n(4)\ge27$. The complete structural reduction, every
palette case, duplicate-list issue, weighted transfer, compact arithmetic,
catalog consequence, and mandatory computational replay survived the stated
attacks. The ordinary foundational inferences made explicit here are listed
above. No substantive proof repair or additional theorem premise was needed.

The final weighting prose is supported as a description of the chosen proof,
not as a necessity theorem about all possible weights; the retained
perturbation explains this limitation precisely. The side-metadata validator
accepts value-equivalent floats, so its integer guarantee is limited to the
inspected frozen integer inputs. Source bibliographic fidelity,
optimizer execution or optimality, novelty, earlier literature, the exact value
of $n(4)$, the general catalog problem, and any formal proof remain outside
coverage. The mathematical conclusion is a lower bound, not a full catalog
solution.

The report, exact subject snapshots, and runtime keeper are delivered for
separate grading. A distinct grader must assess the report contract,
independence, operating disclosure, and any standing consequence. This report
does not grade itself, change claim standing, or confer a tier.
