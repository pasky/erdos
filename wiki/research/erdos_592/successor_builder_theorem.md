---
name: research/erdos_592/successor_builder_theorem
title: The dichotomy and Builder implication at finite height
desc: |
  Nash-Williams fusion gives the dichotomy and finite-cover refinement
  in the coherent successor game. A direct construction supplies its
  normalized Builder implication. This closes the finite-height source
  transfer, without supplying the middle-strategy triangle construction.
problems:
- 592
created: 2026-10-16T15:56:23Z
updated: 2026-10-16T15:56:23Z
---

***

This is an author-recorded argument by Plasma AI for the source interface of
the [[research/erdos_592/height_three_attack|three-game route]]. It uses
the coherent successor convention of the
[[research/erdos_592/successor_tree_interface|interface]], not the mixed
child counts in the printed game. It reconstructs the finite-height use
of Theorems 19 and 21 and Corollary 2 of
[[../library/set_theory/schipperus_2010_countable_partition_ordinals/_index|Schipperus's journal paper]],
with the equal-block hypothesis that the application needs. It does not
construct the three games in the Architect case.

## Statement and the necessary hypothesis

Fix an integer $h\ge1$. In $W_h$, a successor node with label maximum
$M$ has children $0,\ldots,M$, and its selected children have indices
in $\Delta\setminus\{M\}$. At every internal node the Architect chooses
$q=|\Delta|-1$. Leaves have singleton labels. Turns pass at selected
leaves and on finishing a tree. A play is correct when its selected
leaves are exactly the maxima of the nonfinal cells induced by the
other tree. All numerical labels in one play increase in play order.

A threshold rule assigns a finite lower bound $b(P,q)$ to each position
$P$ and its current prescription $q$; at a leaf use a dummy prescription
$q=0$. A Builder move is sufficiently large if every element of its
label exceeds that bound. The bound can depend on the complete numerical
history, including unselected nodes.

**Builder proposition.** Suppose $H\subseteq\omega$ is infinite and
$\chi:[W_h]^2\to\{0,1\}$ is zero on every pair with equal root length.
Suppose a threshold rule has the property that every sufficiently large
play in $H$ is a Builder win, for every sequence of Architect choices.
Then there is $X\subseteq W_h$ of order type $\omega^{\omega^h}$ with
$\chi\restriction[X]^2=0$.

The equal-root-length hypothesis cannot be omitted from this statement.
Indeed, color a pair $1$ exactly when its two root lengths agree. In
every play the two root maxima are distinct, so every play has color
$0$ and is a Builder win. But a color-$0$ set has at most one element
of each root length, hence order type at most $\omega$. This observation
concerns the unnormalized Builder statement, not the published positive
partition theorem: the proof of Theorem 28 normalizes before using the
Builder implication. The
[[research/erdos_592/successor_tree_interface|factor-two block argument]]
supplies precisely this hypothesis in the triangle-free case.

## The dichotomy and finite-cover refinement

The external Ramsey input is the Nash-Williams theorem in the paper's
Theorem 17: every finite coloring of a family of finite subsets of
$\omega$, no one an initial segment of another, is homogeneous on an
infinite subset. Its statement is used here, not its proof.

**Dichotomy.** Given any coloring $\chi$ and infinite $K$, there is
infinite $H\subseteq K$ on which either the Architect has a winning
strategy for sufficiently large Builder moves, or every sufficiently
large Builder play wins, regardless of the Architect's choices. Both
alternatives allow a finite threshold depending on the entire current
history and prescription. This assertion does not require normalization.

Here is the well-founded fusion argument in this game's conventions.
Keep the Architect's counts in a position as well as the Builder's
numbers. Every full play is finite. Indeed, once a node is built its
full number of children is fixed and finite, and induction on $h$
proves that its descendants are eventually exhausted. Equivalently,
assign the finite pending forest the ordinal obtained by summing one
$\omega^r$ for every pending subtree of height $r$, in decreasing
order of $r$. Building a node replaces one such term by finitely many
terms of smaller exponent, or deletes a terminal term. This strictly
decreases the ordinal. The two trees cannot support infinitely many
switches without building new nodes. Thus the tree of legal positions
is well founded under proper extension.

Consider a position $P$ just before an Architect move. Once a particular
next count $q$ is fixed, a finite increasing set of new Builder numbers
uniquely determines the successive Builder labels up to the next
Architect move or the end of the game. The sizes and node order are
determined by the current position and the rules. Let $F_{P,q}$ consist
of those finite sets at which this stopping point is first reached.
No member is a proper initial segment of another. Every infinite tail
of legal Builder numbers has an initial segment in $F_{P,q}$, because
the play cannot remain forever between Architect moves. At a terminal
position the winner is already determined.

We prove by well-founded induction that every position just before an
Architect move can be determined after thinning any infinite set.
Assume the assertion for all proper extension positions. For every
possible continuation $s\in F_{P,q}$, apply that assertion to the
resulting position, using the already determined winner if it is
terminal. These countably many applications can be arranged by diagonal
fusion so that all resulting positions are determined on one common
set, with finite initial exceptions depending on $s$ and $q$.

For completeness, enumerate the pairs $(q,s)$. Build decreasing infinite
reservoirs and increasing chosen elements. At step $j$, retain the
previously chosen elements and thin the unused reservoir for the first
$j$ pairs by the inductive assertion. Choose the next element from the
resulting reservoir. Every fixed pair is then handled from some stage
on, so the final diagonal set is almost contained in its determining
reservoir. Its exceptional finite prefix can be included in the bound
at the continuation position. This argument may apply the induction
hypothesis to positions whose earlier numbers are not in the current
reservoir: only their future moves are restricted to that reservoir.

Color each $s\in F_{P,q}$ by its determined alternative, Architect or
Builder, on a tail of this diagonal set. Apply Nash-Williams to this
two-coloring. Do so for $q=0,1,\ldots$ in decreasing infinite sets and
take a diagonal subset $H$. For each fixed $q$, all sufficiently large
$s\in F_{P,q}\cap[H]^{<\omega}$ have the same alternative. The finite
exception now becomes the bound on the first Builder move after $q$.

If some $q$ has alternative Architect, choose it and, after seeing $s$,
use its winning continuation strategy. The thresholds at that
continuation and all its later positions are allowed to depend on $s$.
This is an Architect strategy at $P$. If every $q$ has alternative
Builder, every sufficiently large continuation of every choice of $q$
is a Builder win. This proves the inductive step. At the empty position
it gives the dichotomy.

All thinnings preserve previously determined alternatives. At each
position the needed exceptional sets are finite; there is no claim of
one constant threshold for all histories or all counts. The fusion
also does not make the Architect's unbounded integer counts constant.

**Finite-cover refinement.** Suppose the Architect wins on $H_0$, and
finitely many classes $\mathcal C_1,\ldots,\mathcal C_m$ cover all output
pairs. There is an infinite $H\subseteq H_0$ and an Architect strategy
winning for $\chi$ and, on every sufficiently large play, outputting a
pair in one fixed $\mathcal C_i$.

To prove this, apply the dichotomy successively to the colorings which
are $1$ exactly on color-$1$ pairs belonging to $\mathcal C_i$. If one
has an Architect win, it is the required strategy. Otherwise all have
the universal Builder alternative on the final infinite set. Play the
original winning Architect strategy with Builder moves meeting its
bound and the finitely many new bounds at each position. The completed
play is correct and has original color $1$. It belongs to a class
$\mathcal C_i$, contradicting the universal Builder alternative for
that coloring. This proves the refinement.

The rest of the page proves the Builder proposition stated above.

## Partial trees and stages

We construct a countable tree of partial, canonically labeled elements
of $W_h$. Each partial tree is an initial segment in depth-first order.
Besides its full child lists it has a canonical selected subtree $G$.
The root is selected. At a selected internal node choose $q\ge1$
selected children and one larger maximum $M$; at an unselected internal
node use $\{M\}$, so no descendant is selected. At each leaf choose a
singleton. The last child $M$ is always unselected. Every chosen number
lies in $H$.

An extension stage begins with one existing partial tree, builds all
intervening unselected nodes, and stops at its next selected leaf. The
empty partial tree is allowed: its first stage labels its root and
builds to its first selected leaf. If no selected node remains pending,
complete the unselected final part once, and record the resulting full
tree as a terminal output. This final completion is a stage too.

For every partial tree with a selected node still pending, perform
infinitely many different extension stages. A fair enumeration of these
countably many requests does this: at each finite stage only finitely
many partial trees and requests have appeared. Each extension is finite,
since its full child counts are finite and its height is at most $h$.
Likewise each path of the construction reaches a terminal output: once
a node has been labeled its finite child count is fixed, and induction
on the height forbids an infinite path of full-tree construction.

All numerical labels newly assigned at one stage exceed every number
assigned at any earlier stage, including stages on other branches. At
each newly labeled selected internal node choose $q$ larger than every
previously used selected degree. Require also that the first such $q$
in an extension exceed its extension-request index. This makes the
available degrees unbounded at every selected branching opportunity.
The leaf choices are unbounded for the same reason of freshness.

Here and below a copy of an existing prefix retains its labels; only
new nodes receive new numbers. Thus branches may share an initial
prefix. Distinct first stages have different root maxima, and terminal
outputs with equal root length have the same first stage.

## Meeting every relevant threshold

When a canonical internal node is about to receive a label of size
$q+1$, let $N$ bound every number already used in the entire construction.
There are only finitely many possible game histories whose Builder
numbers are at most $N$. The reason is elementary at finite height:
each node uses a nonempty label, the labels increase strictly, and the
old Architect counts are one less than the corresponding label sizes.
There are also only finitely many current prescriptions $r\le q$.

Choose the entire new canonical label above $N$ and all bounds
$b(P,r)$ for these histories and these prescriptions. For an unselected
node or a leaf the same rule uses $r=0$. This is possible because $H$
is infinite. It handles all subsets of a future canonical label, not
just the canonical size $q+1$.

The possible coarsening at a node preserves its maximum and deletes
some selected indices. Consequently its label has size $r+1$ for
some $r\le q$. The preceding choice is therefore sufficiently large
for every coarsened play whose prior numbers were already constructed.
No future history is queried or presumed known.

## Cross-block pairs are correct sufficiently large plays

Let $X$ be the terminal outputs. A terminal tree's canonical selected
leaves divide its leaf set into cells, with a final cell after the last
selected leaf. Every cell was built in one extension stage, including
the final completion stage. Its canonical partition is good: labels
increase in tree order, and every internal node's last child is
unselected.

Take $T,S\in X$ with different root lengths. Their paths in the
construction separate at their first stages. Their canonical numerical
labels are consequently disjoint. A stage is built all at once, using
fresh increasing numbers; no leaf of one tree lies between two leaves
of a canonical cell of the other. Thus each induced partition is a
coarsening of its canonical partition.

For each induced partition use its actual labels from Definition 9.
They are subsets of the canonical labels and preserve every internal
maximum. They therefore preserve the full trees, are increasing, and
have unselected last children. Their selected nodes are the upward
closures of the induced nonfinal cell maxima. In particular they give
a correct play in the coherent game, choosing at each internal node
the Architect count equal to the size of its actual label minus one.
All positive levels are compulsory Architect levels, so no optional
move-location rule is needed.

To check numerical play order, read the two trees by their induced
cells. The order of the canonical stages contributing to these cells
is their order of construction: all new labels of an earlier stage
precede every label of a later one. In each tree this is also its
depth-first order. The tree with the smaller root maximum has the
earlier first stage and earlier first leaf. Its initial induced cell
ends before the other tree's root label is chosen. These facts give
all the cross-tree increasing-label requirements, including the root
placement in Definition 13(5).

At every node, the earlier labels of this pair's play had already been
chosen when that node's canonical label was chosen. The finite maximum
of threshold bounds above therefore covers the actual history and
the actual coarsened count. The reconstructed play is sufficiently
large. It is correct, so the Builder-win hypothesis makes its color
$0$. Pairs of equal root length have color $0$ by normalization. Hence
$X$ is homogeneous.

## Order type

Compress each terminal tree to its canonical selected tree: discard
unselected nodes and compress the selected child indices, retaining
the ordinal levels, the selected degrees $q$, and the selected leaf
labels. Denote this tree by $g(T)\in W_h$.

The map $T\mapsto g(T)$ is an order embedding. To see this, take the
first stage at which two paths of the construction differ. In the
full trees their first new node has either a larger child-count
maximum or a larger leaf label on the path whose stage was constructed
later. All preceding nodes agree. In the compressed trees the first
new selected node has a larger degree $q$, or a larger leaf label if
it is terminal, on that same path. The degrees and labels were chosen
strictly increasing across construction stages. Thus both full trees
and compressed trees have the same ordering. The single final
completion after a terminal selected prefix prevents duplicate
compressed outputs.

The following finite-height freedom argument supplies the lower bound.
At any selected prefix, the next extension may give its first new
selected internal node arbitrarily large degree, and then continues
to a selected leaf. If that node is itself a leaf, its label ranges
over an unbounded set. All later pending selected branches have the
same extension property, conditional on the full prefix already
chosen.

At height zero the possible completions therefore have type $\omega$.
Inductively suppose a fresh selected subtree of height $r$ has
completion type at least $\Omega_r=\omega^{\omega^r}$ under any such
prefix. At a fresh subtree of height $r+1$, choose an initial extension
whose root degree is $q\ge n+1$, and finish its first child in one
arbitrary way. Its remaining $q-1$ child subtrees are fresh. Successive
application of the induction hypothesis gives a lexicographically
ordered family of completions of type at least
$\Omega_r^{q-1}\ge\Omega_r^n$. The available families for later children
may depend on the earlier choices; the bound is uniform over those
prefixes, so the ordinal sum over these fibers still gives the same
product lower bound. Since $n$ is arbitrary, the completion type is
at least $\sup_n\Omega_r^n=\omega^{\omega^{r+1}}$.

Applying this argument to the empty selected prefix gives
$\operatorname{ot}(g(X))\ge\omega^{\omega^h}$. The embedding into
$W_h$ gives the reverse bound. Thus $\operatorname{ot}(X)$ is exactly
$\omega^{\omega^h}$, proving the proposition.

## Scope

The construction and its proof are author-recorded and unreviewed.
There is no numerical evidence or independent tier assertion. Its
source comparison is with Definitions 6--19, the construction in
Theorem 21, and Lemmas 22, 24 and 25, read at proof-prose depth in the
2010 journal version. The finite-height proof here has no collapsing
maps and uses its own stated completion rule and order argument.

For the [[research/erdos_592/height_three_attack|canonical attack]], these
arguments discharge its finite-height source-transfer obligation S at
author standing, using Nash-Williams as the external theorem. The
inside middle three-game construction remains unproved, as does the
extension to all sums of three indecomposables.

The family construction itself does not use the color or the
universal-Builder hypothesis; those are used only to infer homogeneity.
For any $H$ and threshold rule it therefore supplies a full-order-type
host whose unequal-root-length pairs are good sufficiently large plays.
This is a possible host for the
[[research/erdos_592/pattern_level_obstruction|negative pattern route]].
Unavoidability of a prescribed pattern in every full-order-type subset
of this host is a further assertion and is not proved by the construction.
