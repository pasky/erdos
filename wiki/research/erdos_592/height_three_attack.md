---
name: research/erdos_592/height_three_attack
title: The height-three three-game attack at omega to the omega cubed
desc: |
  The three-game step at omega to the omega cubed is constructed online,
  for strategies that read numerical history, when all outputs are outside
  or when they are inside with the first tree's top split at its first or
  last pair of selected leaves. The coherent finite-height dichotomy and
  Builder implication reduce the positive case to middle strategies,
  where the construction is open.
problems:
- 592
created: 2026-10-14T15:17:47Z
updated: 2026-10-17T22:11:11Z
---

***

This page is Plasma AI's editable proof sketch for the first unresolved
instance of [[problems/set_theory/E0592/_index|Problem 592]],

$$
\Omega_3\to(\Omega_3,3)^2,\qquad \Omega_3=\omega^{\omega^3}.
$$

It is the case $\gamma=3$ in the problem page's notation and $\beta=3$ in
[[../library/set_theory/schipperus_2010_countable_partition_ordinals/_index|Schipperus's journal paper]].
A result here would not settle the other sums of three indecomposable
ordinals. The page follows the
[[research/erdos_592/successor_tree_interface|successor-tree interface]],
which proposes the route through a three-game construction: from a winning
Architect strategy, build three trees whose three pairs are outputs of
correct plays.
For the explicit successor game used here, the
[[research/erdos_592/successor_builder_theorem|finite-height source interface]]
reconstructs the dichotomy, its finite-cover refinement, and the normalized
Builder implication.
The local arguments are author-recorded, tier 0, and unreviewed.

The main conclusion is a reduction. Theorem 5 and Propositions 6 and 7
build the three plays, one node at a time and for strategies that read
numerical history, in three classes of winning strategies: all outputs
outside, and all outputs inside with the first tree's top split at its
first or at its last pair of selected leaves. By Corollary 2 the only
remaining case is that of *middle* strategies, treated in its own section
with a structural lemma and a fixed-shape template. These arguments hold
at every finite height.

An earlier bounded conclusion is a precise obstruction to one proposed
mechanism: requiring every selected leaf of the first tree to be selected
in both of its games. A fixed, game-local winning strategy defeats that
requirement, independently of all numerical choices. The same strategy
admits the different explicit schedule below. Thus the obstruction
concerns the synchronization requirement, not the three-game conclusion
or the partition relation.

A three-element stack records which tree may move next. It is useful for
both the obstruction and the construction, but it does not erase numerical
histories from an adaptive strategy. The finite probes cover prescribed
selection shapes and a separately defined adversary with access to all
three games. Neither probe settles the general height-three problem.

## Conventions

$W_3$ is the set of trees of Definitions 6--8 with root label $3$. Every
internal node is a successor node, and each branch has labels $3,2,1,0$.
Children are indexed from $0$ as in Definition 9(4): a node $x$ with
children $x_0,\ldots,x_M$ has $M+1$ children. For a partition $D$,
$\Delta_x(D)=S_x\cup\{M\}$, where $S_x\subseteq\{0,\ldots,M-1\}$ is the set
of indices of the children in $G(T,D)$. The game prose after Definition 17
and in Definition 18(1) instead counts $\max\Delta_x$ children; the print
has this discrepancy on pp. 1200 and 1203. This page uses the zero-based
successor game of the interface: a maximum $M$ gives children
$0,\ldots,M$, with child $M$ unselected. A one-based version instead uses
children $1,\ldots,M$. The constructions below work in either consistent
convention: adding one to every numerical label and child index takes
the zero-based game to the one-based game, with identical full child
lists and conjugated strategies. The printed mixed convention is not
silently asserted to be a literal game definition. This translation
identifies two coherent game definitions; it does not by itself prove
the source theorems for either repair. The
[[research/erdos_592/successor_builder_theorem|separate reconstruction]]
supplies the needed dichotomy and normalized Builder implication for
this convention at finite height, at author standing.

Write $A$, $B$, $C$ for the three trees in the order of their first leaves.
In each pair the tree with the earlier first leaf moves first in that pair's
game. Its root's numbers come first, so it has fewer root children and is
the smaller tree. In tree $k$, a leaf is *marked* for $i$ if it is a selected
leaf of $G_i(T_k)$: a cell end of $T_k$ against $T_i$. A leaf marked for
both other trees is a *double*; a leaf marked for one is a *single* naming
that tree. Reading a tree's leaves in order gives its *mark word*.

The games are those of Definitions 15--19 on printed pp. 1203--1204, read at
statement depth. The positive labels $1,2,3$ are the partial sums of
$1+1+1$, so by Definition 19(1) the Architect moves at every internal node.
Only these compulsory finite-height prescriptions are used here; no
limit-ladder instruction is transplanted to a successor node. Write
$q(x)=|\Delta_x|-1$ for the prescribed number of selected children. This
is the source's $d_x$, not the cardinality of $\Delta_x$. A root may have
$q=0$, in which case its selection shape is empty. A nonroot node is
selected when its index was selected at its parent.

## Prescriptions at finite height

**Lemma 1.** Let $\sigma$ be a winning Architect strategy on an infinite
$H$. In every legal play against $\sigma$ whose Builder moves are
sufficiently large in $H$:

1. at an internal node outside the selected set, $\sigma$ prescribes one
   element, so no child is selected;
2. at a selected nonroot internal node, $\sigma$ prescribes at least two
   elements, so at least one child is selected;
3. the play is correct. Given (1) and (2), this holds exactly when the second
   tree has as many selected leaves as the first tree (*outside*) or one
   fewer (*inside*). A root with no selected child is allowed and has no
   selected leaf below it.

*Proof.* The Builder can always continue a legal play with sufficiently
large moves, and $\sigma$ wins every such continuation. A larger set at an
unselected node $x$ makes $\Delta_x\ne\Delta_x(D)=\{M\}$ in every
continuation. A singleton at a selected nonroot node leaves no selected
leaf below it, so its parent's label records a child outside $G(T,D)$.
There is no such parent obstruction at a root. For (3), the
play builds a run of the first tree up to its next selected leaf, then a run
of the second, and so on. Each selected leaf is a cell maximum exactly when
the other tree still has a leaf to build after it. With $t$ and $s$ selected
leaves, the $t+1$ and $s+1$ runs alternate from the first tree exactly when
$s\in\{t-1,t\}$. By (1) and (2), the selected nodes are then the upward
closure of the cell maxima, so every label equals $\Delta_x(D)$. $\square$

By the reconstructed finite-cover refinement, one may assume that every
output of $\sigma$ is inside, or that every output is outside. The searches
below treat both types.

## The stack criterion

In a pair's game, the tree being built *holds the turn*. Take three trees
with selected sets for both of each tree's games. Run the following process
on the unfinished trees. A tree may build its next node only when it holds
the turn in both of its games. The turn in a game passes at that game's
marked leaves and when a tree finishes, exactly as in Definition 18. Record
who holds each game's turn as a tournament on the unfinished trees. The
process *deadlocks* when the tournament is a 3-cycle: then no tree may move.

When the tournament is transitive, it is a linear order: the *stack*. The
top tree builds until it reaches a marked leaf or its last leaf. With stack
$(t,s,f)$:

- a single naming $s$ swaps the top two, giving $(s,t,f)$;
- a double sends $t$ to the bottom, giving $(s,f,t)$;
- a single naming $f$ deadlocks, since then $t$ holds the turn over $s$,
  $s$ over $f$, and $f$ over $t$;
- the last leaf removes $t$.

The process starts with stack $(A,B,C)$.

**Lemma 2 (local realization and the cycle obstruction).** At a transitive
prefix, both games containing the top tree are ready for that tree's next
node. Their actual numerical histories and prescriptions are therefore
available. Any ordered merge of their two prescribed child lists can be
realized with a shared maximum and sufficiently large choices in $H$.
Three complete legal plays sharing their trees cannot produce a cyclic
turn state.

*Proof.* Suppose the requested selected-child counts are $a$ and $b$.
An ordered merge is a word in $x,y,D$, with $a$ occurrences of $x$ or $D$
and $b$ occurrences of $y$ or $D$. Choose one fresh element of $H$ for
each letter, in increasing order, and then one larger element $M\in H$.
All these elements exceed every number already chosen and both games'
current thresholds. The first label contains the $x,D$ positions and
$M$; the second contains the $y,D$ positions and $M$. Thus their sizes
are $a+1,b+1$ and their maxima coincide. At a leaf choose a single common
element above the same bounds. No past choice is enlarged or relabeled.

For the obstruction, give a node its leaf label or, at an internal node,
the common maximum $M$ as its *key*. Within a game every key strictly
increases in play order. At a cyclic state, the next nodes of the three
trees would have keys $u<v<w<u$. This is impossible. $\square$

All children at positions $0,\ldots,M$ must actually be built. Children
absent from both selected lists have unselected subtrees, filled in tree
order using singleton labels and the same fresh-number rule. A child
selected in only one game still has the same full subtree in both games.
The other game's labels there are singletons. Since the height is finite
and every chosen maximum is finite, this recursion builds a finite tree.
The number of unselected nodes can be arbitrarily large; none is discarded
from either numerical history.

**Fixed-shape realization.** For fixed selection shapes, erase only the
children selected in neither game. The remaining ordered union at each
node is an ordered merge as above. Conversely, every such finite merged
tree can be padded by the preceding rule. If its stack run completes with
the correct pairwise cell endpoints, this gives three shared full trees
for every infinite $H$ and every finite, history-dependent threshold rule.
The last child of each internal node is unselected, so every tree has a
nonempty final cell after all its selected leaves. Inserted unmarked
leaves do not change which event ends a nonfinal cell. The induced
partitions therefore recover exactly the prescribed selected trees and
labels. Increasing labels give Definitions 11 and 13, including disjoint
Full sets within each pair and the placement of the second root after the
first cell. This proves the fixed-shape compression and expansion used by
the finite probes; it is not a finite basis for unrestricted strategies.

For an adaptive $\sigma$, the analogous construction must read both
prescriptions afresh at each actual position, including positions reached
after building unselected subtrees. If a rule for the arrangements and
actual numbers avoids a cycle throughout, it completes three legal plays;
winningness then gives correctness and color $1$. Lemma 2 guarantees local
availability of the requests, not a rule that avoids every future cycle.
Changing the numbers or the number of unselected children may change all
later prescriptions. A schedule computed for static shapes does not
control that dependence.

**Lemma 3 (endgame).** Once one tree has finished, the process cannot
deadlock. The first tree to finish is $A$ in the outside type and $C$ in the
inside type.

*Proof.* Suppose a remaining tree marks a leaf for the finished tree. Then
that game's play has a selected leaf that is not a cell maximum. That play
is legal, which contradicts Lemma 1(3). So the remaining two trees mark only
each other, and swaps never deadlock. In each pair, the first tree's last
run is last in the inside type and the second tree's is last in the outside
type. $\square$

So only the stretch before the first finish can fail. Every mark involving
the first finisher must be emitted in that stretch.

## Outside strategies: the spine construction

For outside strategies the forward-dependence problem disappears. The
argument below works at every finite height $h$ in the coherent successor
game, so it uses nothing special about $h=3$.

For a tree, call the smaller of its two partners its *left* partner and
the larger its *right* partner. Thus $A$ has left partner $B$ and right
partner $C$; $B$ has $A$ and $C$; $C$ has $A$ and $B$.

**Theorem 5 (outside strategies).** Let $\sigma$ be a winning Architect
strategy on an infinite $H$ for the coherent successor game at a finite
height $h$, and suppose every output of $\sigma$ is outside. For every
finite threshold rule there are three complete correct plays against
$\sigma$, one for each pair, that share their trees $A<B<C$ and use only
sufficiently large moves. Each prescription is used at the position where
$\sigma$ makes it; no later prescription is needed in advance.

*Construction.* Each tree is built along a *spine*: a path from its root
to a leaf whose nodes are all selected in both of the tree's games. When a
spine node $v$ is built, both games prescribe their counts $d_L$ (left
game) and $d_R$ (right game). The Builder lists the selected children of
$v$ as follows: $d_L-1$ children selected only in the left game; the next
spine node, which is the last child selected in the left game and the
first selected in the right game; then $d_R-1$ children selected only in
the right game; then padding ending in an unselected last child. The
spine ends at a leaf, which is a double. Every other selected child roots
a subtree selected in one game only. It is built with that game's
prescriptions, padded as in Lemma 2, and all of its marks are singles
naming that game's partner.

If the common first move of $\sigma$ is $0$, every first tree has no
marks; then no tree has marks and the three trees are simply built in
order. Otherwise every spine count is at least $1$: at a nonroot node by
Lemma 1(2), and at a root because an outside output has as many marks in
its second tree as in its first. So every mark word has the form

$$
(\text{singles for the left partner})\ D\ (\text{singles for the right}),
$$

where the double $D$ is the last mark for the left partner and the first
mark for the right partner. The selection trees themselves are not
restricted: the spine identifies the rightmost path of the left game's
selection tree with the leftmost path of the right game's.

*Schedule and proof.* Write $D_A,D_B,D_C$ for the three doubles. The
stack process runs in five stages.

1. From $(A,B,C)$, $A$ and $B$ alternate in their game until $A$ builds
   $D_A$. Before that, both emit left singles, which name each other.
2. The stack is $(B,C,A)$, and $B$ builds to $D_B$, giving $(C,A,B)$.
3. $C$ and $A$ alternate in their game until $C$ builds $D_C$. Here $C$
   emits left singles naming $A$, and $A$ emits right singles naming $C$.
4. The stack is $(A,B,C)$, and $A$ has no mark left: it finishes.
5. $B$ and $C$ alternate with right singles until $B$ finishes, and then
   $C$ finishes.

Every claim about the next mark follows from the alternation of an
outside play, which $\sigma$ guarantees in every legal continuation. In the
game of $A$ and $B$, the marks alternate $a_1<b_1<\cdots<a_t<b_t$. The
double $D_A$ is $a_t$, since $A$ has no later mark for $B$. Exactly one
mark of $B$ for $A$ remains after it, and $D_B$ is the last such mark, so
it is the next mark of $B$; no mark of $B$ for $C$ precedes $D_B$. In the
game of $A$ and $C$, $D_A$ is the first mark of $A$, so the alternation
continues with $C$'s left singles and $A$'s right singles. It ends with
$C$'s last mark for $A$, which is $D_C$. At that point $A$ has emitted all
its marks, and the remaining marks of $B$ and $C$ name each other. In the
game of $B$ and $C$, $D_B$ and $D_C$ are the first marks of the two trees,
and stage 5 is the rest of that alternation.

In each pair the global construction order restricted to the two trees is
that pair's play order: a tree builds only while it holds the turn in both
of its games, and the third tree's moves belong to neither game of the
pair. The finishing order $A,B,C$ is the outside order of Lemma 3, and
every last cell follows the partner's last mark. Choosing every new element
of $H$ above all earlier numbers and all three games' current thresholds
makes every move sufficiently large. The padding argument of Lemma 2 makes
each pair good and recovers the prescribed labels. Hence the three plays
are complete, legal and correct, and all three outputs have color $1$.
$\square$

**Consequence.** Use the source interface S proved on the companion page
and the equal-block normalization. In the Architect case, the finite-cover
refinement gives an
infinite subset on which the Architect wins with all outputs inside or with
all outputs outside. In the outside case Theorem 5 gives a color-$1$
triangle. Thus the positive relation $\Omega_3\to(\Omega_3,3)^2$ is
reduced to the inside case of G. The reduction is the same at every
finite height. In particular, at any finite height, a coloring without a
color-$1$ triangle has no infinite set on which the Architect wins with
all outputs outside. Such colorings exist at height $4$ by Schipperus's
Theorem 33, and all three printed negative patterns are indeed of inside
type: their first trees have one more cell than their second trees.

For inside strategies the same spine construction deadlocks. With the
same words, $B$ emits $D_B$ before $A$ emits $D_A$, since $D_B$ is now the
last mark of $B$ for $A$. After $D_A$ the stack is $(C,B,A)$. If $C$ starts
with singles naming $A$ it deadlocks at once. If $C$ is built with left
partner $B$ instead, the game of $B$ and $C$ ends with $C$'s double while
$B$ still owes its last single naming $C$, and the stack $(B,A,C)$ then
deadlocks. The inside case therefore needs a different idea.

## Inside strategies: two classes with online templates

Two further classes of inside strategies have online constructions. In a
selection tree with at least two leaves, the *top split* is the highest
node with at least two selected children. Call an inside output
*top-first* if the first two selected leaves of its first tree have their
lowest common ancestor at that tree's top split, and *top-last* if its
last two selected leaves do. Otherwise call it *middle*. A first tree with
one selected leaf counts as top-first. Under the level reading recorded on
the [[research/erdos_592/pattern_level_obstruction|pattern-level page]],
top-first means $\lambda_1=\max\lambda$ and top-last means
$\lambda_{t-1}=\max\lambda$, where $\lambda$ is the word of levels of
consecutive selected leaves.

Before its first mark, a first tree can keep its two games' histories
identical by giving each node the same label in both games. Then $\sigma$
prescribes the same counts in both, and the two games reach their top
split at the same node.

**Proposition 6 (top-first).** If every output of $\sigma$ is inside and
top-first, the conclusion of Theorem 5 holds.

*Proof.* Build $A$ with identical labels in its two games down to the
common top split $v$. Below $v$ in the first child both games have count
$1$, since the first selected leaf is alone in that child of a top-first
output. At $v$, list the first child, then the children selected only for
$C$, then those selected only for $B$. Thus the mark word of $A$ is
$D\,C^*B^*$. Build $B$ and $C$ along *mirror spines*: at each spine node,
the children selected only for the right partner come first, then the
spine child, then the children selected only for the left partner. Their
words are $C^*D_BA^*$ and $B^*D_CA^*$, and the double is the last mark for
the right partner and the first for the left one. The stack process runs
as follows. $A$ emits $D$, giving $(B,C,A)$. Then $B$ and $C$ alternate
until $C$ emits $D_C$ and $B$ emits $D_B$, giving $(A,C,B)$. Next $A$ and
$C$ alternate until $A$ emits its last single naming $C$, and $C$
finishes. Finally $A$ and $B$ alternate, $B$ finishes, and then $A$
finishes. Each step is forced by the inside alternation of the relevant
game, exactly as in the proof of Theorem 5. If $A$ has a single mark for
$B$, inside alternation forces a single mark for $C$ as well, and the run
reduces to $A$ emitting $D$ while $B$ and $C$ play out their game.
$\square$

**Proposition 7 (top-last).** If every output of $\sigma$ is inside and
top-last, the conclusion of Theorem 5 holds.

*Proof.* Build $A$ with identical labels down to the common top split
$z$. At $z$, list the children selected only for $B$, then a child $p$
selected in both games, then the children selected only for $C$, then a
child $q$ selected in both games. Here $p$ is the second-to-last child
selected for $B$ and the first selected for $C$, and $q$ is the last for
both. Below $z$, build the subtree of $p$ along an outside spine with left
partner $B$. In the subtree of $q$ the game with $B$ has count $1$
everywhere, because the last selected leaf of a top-last first tree is
alone in the last child of its top split. Build $q$'s subtree along the
rightmost path of the game with $C$, with the children selected only for
$C$ on its left. The mark word of $A$ is $B^*D_AC^*D'$, where $D_A$ is the
first mark for $C$ and $D'$ the last mark for both partners. Build $B$ and
$C$ along outside spines, with words $A^*D_BC^*$ and $A^*D_CB^*$. The run
is as follows. $A$ and $B$ alternate until $A$ emits $D_A$, and then $B$
emits $D_B$, giving $(C,A,B)$. Next $C$ and $A$ alternate until $C$ emits
$D_C$, giving $(A,B,C)$. Then $A$ emits $D'$, giving $(B,C,A)$. Finally
$B$ and $C$ alternate until $B$ emits its last single, and $C$, $B$ and
$A$ finish in that order. Every step is forced by the inside alternations.
If the game of $B$ and $C$ has a single mark of $B$, then $C$ has no mark
for $B$, and $D_C$ is a single naming $A$. $\square$

**Reduction.** The finite-cover refinement applies to the finite cover
of all pairs by the outside pairs, the inside top-first pairs, the inside
top-last pairs, the inside middle pairs, and the remaining pairs, which
are not good or have equal block types. In the Architect case some class
carries a winning strategy, and only the last two classes are not
covered. Correct plays output good pairs, and pairs of equal block type
have color $0$ after normalization, so the remaining class carries no
winning strategy. Theorem 5
and Propositions 6 and 7 therefore reduce G at height $3$ to *middle
strategies*: winning strategies all of whose outputs are inside and
middle. The reduction holds at every finite height.

At height $3$ a middle first tree has top split level $2$ or $3$, and the
first and last children of its top split each contain at least two
selected leaves. Under the level reading, the printed patterns behave
consistently with this reduction. The two-summand pattern of Theorem 31
is top-first; it has triangles, as Proposition 6 predicts, and excludes
only six-cliques. The three-summand pattern of Theorem 32 and the
triangle-free four-summand pattern of Theorem 33 are middle patterns.

## The middle class

Middle strategies remain open. This section records what holds for them
in the word formulation of the fixed-shape realization: each tree's mark
word over three letters, with a separator level between consecutive
letters, such that the two projections recover the two selection
shapes. A projection keeps the letters for one partner, and the level
between two kept letters is the largest separator level between them.
Given the words, levels exist exactly when every stretch of each
projection contains a separator whose two covering stretch levels are
both at least its own level. Separators outside the other projection's
span count as covered.

**Lemma 8 (the second tree is not a spine).** Fix an inside pair of
shapes $(X,Y)$ with $X$ middle. Thus the three trees carry $(X,X)$,
$(Y,X)$ and $(Y,Y)$ respectively. No completing schedule gives $B$ a
word of the form $A^*D\,C^*$ or $C^*D\,A^*$.

*Proof.* Following the stack process from $(A,B,C)$ with such a word for
$B$ forces the word of $A$ to be one of
$D\,C^*B^*$, $D\,C^*D\,B^*$, $B^*D\,C^*D$ and $B^*C^*D$. Write $\ell$
for the top split level of $X$. In the first two forms, the span of
$A$'s projection for $C$ lies between the first two marks for $B$; in
the last two it lies between the last two marks for $B$. The projection
for $C$ has shape $X$, so its span needs a separator of level $\ell$.
The two bounding marks for $B$ have common ancestor below level $\ell$,
since $X$ is middle. Their stretch cannot contain such a separator.
Thus no separator levels exist. $\square$

These two spine words cannot handle a fixed middle pair. The following
template uses a different second-tree word, with singles of one kind
on both sides of its double.

**Proposition 9 (two children at the top split).** Let the fixed shapes
be an inside pair $(X,Y)$ with $X$ middle, whose top split has exactly two
children $F$ and $L$. Let $f=|F|-1$ and let $\mu$ be the level word of
$Y$. If $\mu_f$ or $\mu_{f+1}$ is at least the top level of $X$, the pair
has a triangle schedule.

*Proof.* Let $t=|X|$, so $|F|+|L|=t$. Take for $A$ the word

$$
A:\ B^fD_1C^{t-2}D_2B^{|L|-1}.
$$

Here $D_1$ is the last leaf of $F$ for $B$ and the first leaf for $C$,
and $D_2$ is the first leaf of $L$ for $B$ and the last for $C$. Merge
$F$ along an outside spine and $L$ along a mirror spine. The run of
singles naming $C$ then lies in the stretch from $D_1$ to $D_2$ for $B$,
which crosses the top split and has the top level, and the other runs lie
outside the span of the other projection. So $A$ has separator levels for
all shapes. There are two forms for $B$ and $C$.

1. If $\mu_{f+1}$ is at least the top level, take
   $B:\ A^fD_BC^{t-1}A^{|L|-1}$ and the outside spine
   $C:\ A^{t-2}D_CB^{t-2}$. The run: $A$ and $B$ alternate with $f$
   singles each; $A$ emits $D_1$ and $B$ emits $D_B$; $C$ and $A$
   alternate until $C$ emits $D_C$; $A$ emits $D_2$; $B$ and $C$ alternate
   until $C$ finishes; $B$ and $A$ alternate; $B$ and then $A$ finish.
2. If $\mu_f$ is at least the top level, take
   $B:\ A^fC^{t-1}D_BA^{|L|-1}$ and the mirror spine
   $C:\ B^{t-2}D_CA^{t-2}$. The run: $A$ and $B$ alternate with $f$
   singles each; $A$ emits $D_1$; $B$ and $C$ alternate until $C$ emits
   $D_C$ and $B$ emits $D_B$; $A$ and $C$ alternate until $A$ emits $D_2$;
   $C$ finishes; $B$ and $A$ alternate; $B$ and then $A$ finish.

In both forms the double of $B$ is the $(f+1)$-th leaf of $Y$. Its run of
singles naming $C$ contains every level of $X$ and lies in the stretch of
$Y$ after or before that leaf, of level $\mu_{f+1}$ or $\mu_f$; this is
where the condition is used. The word of $C$ is a spine. Both runs were
checked against the three inside alternations. $\square$

Theorem 32's pattern under the selection-shape reading is the case
$X=(1,2,1)$, $Y=(3,3)$, $f=1$, $\mu_2=3$, with the triangle recorded on
the [[research/erdos_592/pattern_level_obstruction|pattern-level page]].

**Proposition 10 (flat second shape).** Let $X$ be middle, with exactly
two children $F$ and $L$ at its top split, each a single block of
$x_1,x_2\ge2$ leaves, and let $Y$ have all its leaves in one block. Then
the pair has a triangle schedule.

*Proof.* Take the words

$$
\begin{aligned}
A&:\ D\,C^{x_1-1}B^{x_1-1}\mid C\,C\,(B\,C)^{x_2-2}B\,B,\\
B&:\ C^{x_1}\mid D_BA^{x_1-2}D^{x_2-1}A,\\
C&:\ B^{x_1-1}D_CA^{x_1-2}D\,A\,D^{x_2-2},
\end{aligned}
$$

where the bar marks the separator of the top level and every other
separator has level $1$. The two projections of $A$ split as $(x_1,x_2)$
at the bar. The marks of $B$ for $C$ split as $(x_1,x_2)$ at the bar, and
its marks for $A$ all follow it. Both projections of $C$ lie in one block.
The run: $A$ emits $D$; $B$ and $C$ alternate, $B$ with $x_1$ singles,
until $C$ emits $D_C$ and $B$ emits $D_B$; $A$ and $C$ alternate until
$C$'s double hands the turn to $B$; $A$ and $B$ alternate until $B$'s
double hands it back. In the second block each double of $B$ or $C$
switches $A$ to the other partner, $C$ finishes after $A$'s last single
naming $C$, and $B$ and then $A$ finish. The case $x_1=3$, $x_2=2$ was
replayed in full against the three inside alternations, and the general
case follows the same counts. $\square$

The case $x_1=x_2=2$ is the hand-checked schedule

$$
A:\ D\,C\,B\,C\,C\,B\,B,\qquad B:\ C\,C\,D\,D\,A,\qquad C:\ B\,D\,D\,A.
$$

At height three the proposition covers the shapes with top level $2$ and
those with top level $3$ whose two top children are single blocks.

**Proposition 11 (first child a block).** Let $(X,Y)$ be an inside pair
with $X$ middle, and suppose the first child $F$ of the top split of $X$
has all its selected leaves in one block. If $\mu_j\le\lambda_{t-1}$ for
every $j<|F|$, the pair has a triangle schedule:

$$
\begin{aligned}
A&:\ D\,B^{|F|-1}C^{t-1}B^{t-|F|},\\
B&:\ C^{t-1}A^{|F|-1}D_BA^{t-|F|-1},\\
C&:\ B^{t-2}D_CA^{t-2}.
\end{aligned}
$$

*Proof.* At the top split of $A$ list $F$, then the children selected
only for $C$, then those selected only for $B$; inside the block $F$ list
$D$, then the other leaves selected for $B$, then those selected for $C$.
The run of singles naming $B$ after $D$ stays inside $F$, where every
level is $1$, and the run naming $C$ crosses the top split inside the
stretch of $B$'s projection from the last leaf of $F$, which has the top
level. In $B$ the run of singles naming $A$ before $D_B$ lies in the last
stretch of the projection for $C$, which needs $\mu_j\le\lambda_{t-1}$;
everything else lies outside the other projection's span. $C$ is a
mirror spine. The run: $A$ emits $D$; $B$ and $C$ alternate, $B$ with
$t-1$ singles, until $C$ emits $D_C$; $B$ emits its first single naming
$A$; $A$ and $B$ alternate through the leaves of $F$ until $B$ emits
$D_B$; $A$ and $C$ alternate until $A$'s last single naming $C$, and $C$
finishes; $A$ and $B$ alternate, and $B$ and then $A$ finish. $\square$

Its mirror image also holds. If the last child $L$ of the top split has
all its selected leaves in one block and $\mu_j\le\lambda_1$ for every
$j\ge t-|L|$, the words

$$
A:\ B^{t-|L|}C^{t-1}B^{|L|-1}D,\qquad
B:\ A^{t-|L|-1}D_BA^{|L|-1}C^{t-1},\qquad
C:\ A^{t-2}D_CB^{t-2}
$$

complete. Here $A$ alternates with $B$ until $B$'s double switches it to
$C$, alternates with $C$ until $C$'s double switches it back, and ends
with its double; $B$ and $C$ then alternate until $C$ finishes.

**Proposition 12 (two block children, peak at the boundary).** Let
$(X,Y)$ be an inside pair with $X$ middle, with exactly two children at
its top split, single blocks of $x_1,x_2\ge2$ leaves, and let $\ell$ be
the top level of $X$. If
$\mu_{x_1}=\max\mu$ and $\mu_j\le\ell$ for every $j<x_1$, the words

$$
\begin{aligned}
A&:\ D\,B^{x_1-1}C^{t-2}D'B^{x_2-1},\\
B&:\ C^{x_1}A^{x_1-1}D_BC^{x_2-1}A^{x_2-1},\\
C&:\ B^{x_1-1}D_{C}A^{t-3}D'_{C}B^{x_2-2}
\end{aligned}
$$

complete. In $A$, $D$ is the first leaf of both projections, and $D'$ is
the last leaf of the second block for $C$ and its first leaf for $B$, so
the second block is merged along a mirror spine. In $B$ the run of
singles naming $A$ before $D_B$ lies in the stretch of top level of the
projection for $C$, and the singles naming $C$ after $D_B$ lie inside its
second block. In $C$ the run of singles naming $A$ fills the stretch of
the projection for $B$ at position $x_1$, which is where
$\mu_{x_1}=\max\mu$ is used. The run: $A$ emits $D$; $B$ and $C$
alternate, $B$ with $x_1$ singles, until $C$ emits $D_C$; $B$ and $A$
alternate until $B$ emits $D_B$; $A$ and $C$ alternate until $C$ emits
$D'_C$; $A$ emits $D'$; $B$ and $C$ alternate until $C$ finishes; $B$ and
$A$ alternate, and $B$ and then $A$ finish. For $X=(1,3,1)$ and
$Y=(2,2)$, which Propositions 9 to 11 miss, the words are

$$
A:\ D\,B\,C\,C\,D\,B,\qquad B:\ C\,C\,A\,D\,C\,A,\qquad C:\ B\,D\,A\,D,
$$

replayed in full with separator levels $(1,1,3,1,1)$, $(1,3,2,1,2)$ and
$(2,2,2)$.

For two top children that are single blocks, Propositions 9 to 12 and the
mirror image of 11 leave open the second shapes $Y$ that have a
non-sibling pair among their first $x_1$ and among their last $x_2$
leaves, whose level at position $x_1$ is not their maximum, and, when
$d=2$, whose levels $\mu_{x_1-1}$ and $\mu_{x_1}$ are below the top level
of $X$. The pair $X=(1,1,3,1)$ with $Y=(3,1,2)$ has five leaves in $X$
and is not covered by these templates. The retained census includes it,
but its existence assertion is not an online construction. The other
five-leaf pair $X=(1,3,1,1)$, $Y=(2,1,2)$ has the explicit schedule
below.

For that latter pair, take

$$
\begin{aligned}
A&:\ D\,D\,C\,C\,C\,B\,B\,B,\\
B&:\ C\,C\,A\,C\,C\,D\,A\,A,\\
C&:\ B\,D\,B\,D\,A\,A.
\end{aligned}
$$

Their separator words are respectively
$(1,3,1,1,1,1,1)$, $(1,3,2,1,1,1,2)$ and
$(2,1,2,1,2)$. Projection gives $X,X$ in $A$, $Y,X$ in $B$ and
$Y,Y$ in $C$. The full marked-event order is

$$
\begin{gathered}
A_D,\ B_C,\ C_B,\ B_C,\ C_D,\ B_A,\ A_D,\\
B_C,\ C_B,\ B_C,\ C_D,\ B_D,\\
A_C,\ C_A,\ A_C,\ C_A,\ A_C,\ \operatorname{finish}(C),\\
A_B,\ B_A,\ A_B,\ B_A,\ A_B,\ \operatorname{finish}(B),
\ \operatorname{finish}(A).
\end{gathered}
$$

Every single names the second tree of the stack. Doubles rotate it;
the finishing order is $C,B,A$. This is a direct fixed-shape
construction and uses no numerical search. Its prescriptions are
fixed in advance, so it supplies no missing adaptive uniformity.

Proposition 11 is online in a class that Corollary 2 can select: all
outputs inside and middle, with the first top child of the first tree a
single block, its last two selected leaves siblings, and the first $|F|$
selected leaves of the second tree siblings. The block $F$ of $A$ is
built before the second tree starts, so its count $|F|$ is known when
$B$ builds the block that holds its first marks for $A$. In $B$ that
block is reached along a mirror spine, and $D_B$ is placed at the
$|F|$-th mark there.

Propositions 9 and 10 are not shown to be online. In each, a double of
$B$ answers a double of $A$, and its position among the marks of $B$ for
$A$ depends on counts that are prescribed after the node of $B$ fixing
that position is built: at the root of $B$ in Proposition 9, the
double's place among the root's children depends on $|F|$ and on the
counts of $Y$ below the root, and at the block of $B$ in Proposition 10
it depends on the size of the block $L$ of $A$. Theorem
5, Propositions 6 and 7 and Proposition 11 in its class avoid this: each
double is the first or last mark of a game, or sits at a position fixed
by counts that are already prescribed when the deciding node is built.

A structural observation organizes the open fixed-shape cases. If every
level of $Y$ is below the top level $\ell$ of $X$, then each top-level
stretch of the projection of $B$ for $C$ must contain a separator
outside the span of $B$'s marks for $A$. So all marks of $B$ for $A$ lie
in the region of a single child of the top split of $X$: the leaves of
the earlier children are singles naming $C$ before them, and those of
the later children are singles naming $C$ after them. Inside that region
the merge is a problem of height $h-1$, between that child and $Y$, with
boundary conditions set by the run. A proof of the fixed-shape middle
case at height three could therefore go through a lemma on such
height-two sub-schedules. At height four the corresponding sub-problem
has height three and may contain middle shapes, which is consistent with
the failure that Theorem 33 records.

Height two is a testbed for these cases. There the relation is known,
by Darby's theorem and Schipperus's Theorem 28, but the reduction above
leaves the same middle class, and the templates here do not cover it: the
analogue of the open pairs is $X$ with two blocks of three leaves and $Y$
with blocks of sizes $1,3,1$. A construction of middle schedules at
height two, fixed-shape and then online, would test whether the game
method reaches the known case before it is pushed to height three.

The fixed-shape question decides the reach of the pattern method. If
every inside middle pair at height three has a triangle schedule, then
every coloring for which some fixed-shape strategy wins has a color-$1$
triangle, and a negative answer would need a coloring for which no
fixed-shape strategy wins. If some middle pair has no schedule, its
pattern coloring under the selection-shape reading is triangle-free, and
a negative answer would follow from its unavoidability in every subset of
full order type.

## A game-local obstruction to synchronizing the first tree

Consider the proposed mechanism that keeps $G_B(A)=G_C(A)$: every marked
leaf of $A$ is a double. It allows arbitrary arrangements in $B$ and $C$,
arbitrary full child counts, and arbitrarily large numerical choices. It
still fails for the following fixed strategy at height three.

Write $\langle\cdot\rangle$ for a selected internal node and $\bullet$
for a selected leaf. Specify the two selection shapes

$$
X=\langle\langle\langle\bullet,\bullet,\bullet\rangle\rangle\rangle,
\qquad
Y=\langle\langle\langle\bullet\rangle,
                    \langle\bullet\rangle\rangle\rangle.       \tag{1}
$$

The first tree in each game has shape $X$, and the second has shape $Y$.
Thus the prescribed selected-child counts are

| role | root | selected depth-one node | selected depth-two nodes |
|---|---|---|---|
| first | $1$ | $1$ | $3$ |
| second | $1$ | $2$ | $1$ each |

Every unselected internal node has count $0$. The sizes given to the
Builder are these counts plus one. This defines a single strategy
$\sigma_{X,Y}$ on actual numerical histories: it reads the tree's role
and its position in the selected tree, and ignores numerical labels and
unselected nodes. It does not inspect either of the other games.

Every legal completion is correct and inside: there are three selected
leaves in its first tree and two in its second, with a nonempty final cell
in each. To witness the word *winning*, define an auxiliary coloring on
all pairs in $W_3$: it is $1$ precisely on pairs that are outputs of a
legal complete play against $\sigma_{X,Y}$, and $0$ otherwise. Equivalently,
compute a pair's induced partitions and their labels and check whether
they form such a play. Then $\sigma_{X,Y}$ wins every legal play, on every
infinite $H$, without a lower-threshold restriction. Every output has
unequal root lengths, so this coloring is normalized. It has the triangle
constructed below and is not proposed as a negative partition coloring.

**Obstruction.** No three correct complete plays against
$\sigma_{X,Y}$ can share their output trees while every selected leaf of
$A$ is common to its two games.

*Proof.* Suppose such plays exist. Let $a_1<a_2<a_3$ be the common
selected leaves of $A$, let $b_1<b_2$ be the selected leaves of $B$
relative to $A$, and let $c_1<c_2$ be those of $C$ relative to $A$.
Correct inside alternation gives

$$
a_1<b_1<a_2<b_2<a_3,\qquad
a_1<c_1<a_2<c_2<a_3.
$$

Let $p_1<p_2<p_3$ be the selected leaves of $B$ relative to $C$.
We claim

$$
p_1\le b_1<b_2\le p_3.                               \tag{2}
$$

If $b_1<p_1$, the later $B$ leaf $p_1$ is after the second $A$ cell in
the pair $(A,B)$, so $a_2<p_1$. The first $C$ leaf is after $p_1$ in
$(B,C)$, hence $p_1<c_1<a_2$, a contradiction. If $p_3<b_2$, then
$b_2$ is in $B$'s final cell relative to $C$. Since $(B,C)$ is inside,
all $C$ leaves precede that cell. But $(A,B)$ gives $b_2<a_3$, and
$(A,C)$ puts a nonempty final $C$ cell after $a_3$. Thus
$\max\operatorname{Seq}(C)<b_2<a_3<\max\operatorname{Seq}(C)$,
again a contradiction. This proves (2).

By shape $X$, all three $p_i$ lie below one depth-two node of $B$. By
shape $Y$, $b_1$ and $b_2$ lie below different depth-two nodes of $B$.
Equal-depth subtrees have disjoint convex leaf sets. At least one $b_i$
therefore lies outside the entire subtree containing the $p_i$, hence
outside $[p_1,p_3]$. This contradicts (2). $\square$

This is a symbolic obstruction for all numerical positions and all full
trees, not a bounded search failure. Deleting the common initial unary
level gives the same obstruction at height two, consistent with the fact
that the published positive relation requires a more flexible schedule.
The proof also applies for every $n\ge3$ when $X$ has $n$ leaves below
one depth-two node and $Y$ has $n-1$ leaves below distinct depth-two
nodes. Replace (2) by $p_1\le b_1<\cdots<b_{n-1}\le p_n$; its endpoint
proof is unchanged, and at least one $b_i$ lies outside the $p_i$ subtree.

### An explicit alternative for the same strategy

The obstruction is sharp with respect to the proposed synchronization:
the following schedule works against $\sigma_{X,Y}$. The mark words are

$$
A:B,D,C,D,\qquad B:A,C,D,C,\qquad C:D,D.        \tag{3}
$$

Here $D$ marks the leaf for both other trees. Specify the selected union
trees as follows. All three roots have exactly one child in the union of
their selected sets, and it is common to both games. In $A$ this
depth-one node has one common selected child, whose selected leaf union
is $B,D,C,D$. In $B$ the depth-one node has two selected children: the
first is selected only for $A$ and has one $A$-marked leaf; the second
is common and has leaf union $C,D,C$. In $C$ the depth-one node has two
common selected children, each with one double leaf. Projection onto
either game's selections gives exactly $X,X$ in $A$, $Y,X$ in $B$,
and $Y,Y$ in $C$. These are selected child lists; each full child list
also includes all the padding required by its numerical maximum.

The complete event order, with the resulting stack, is

| event | stack afterward |
|---|---|
| start | $A,B,C$ |
| $A:B$ | $B,A,C$ |
| $B:A$ | $A,B,C$ |
| $A:D$ | $B,C,A$ |
| $B:C$ | $C,B,A$ |
| $C:D$ | $B,A,C$ |
| $B:D$ | $A,C,B$ |
| $A:C$ | $C,A,B$ |
| $C:D$ | $A,B,C$ |
| $A:D$ | $B,C,A$ |
| $B:C$ | $C,B,A$ |
| $C$ finishes | $B,A$ |
| $B$ finishes | $A$ |
| $A$ finishes | empty |

Apply Lemma 2's padding procedure to these selected unions in this event
order. At each node take the maximum of both current thresholds and all
earlier numbers, then choose the required fresh elements of $H$. This
constructs the same full child list in the two games of each tree and a
common label on each leaf. Both requests are available before either
label is committed. Their sizes remain those in the table because
$\sigma_{X,Y}$ ignores the numbers. All unselected subtrees are built,
with their moves present in both relevant histories. The three pair
projections of the table have alternating cells with respectively three
and two nonfinal endpoints, so the marked paths end at the actual cell
maxima. Each game is correct, follows $\sigma_{X,Y}$ and meets its
threshold at every move. Thus (3) works for every infinite $H$ and every
finite threshold rule, although synchronizing $A$ does not.

The evidence retains these three selected union trees and the event
table, checks both projections of each tree, and independently reconstructs
the three leaf alternations. The proof above, rather than numerical
sampling, establishes the obstruction and the arbitrarily large
realization.

Keeping $C$ synchronized in (3) is specific to this example. For the
next pair $X=1$-$1$-$4$ and $Y=1$-$3$-$(1,1,1)$, exhaustive ordered
merging finds a schedule, but none with $C$ all doubles. This is an exact
finite obstruction for those fixed shapes, using the proved compression
rule, and is checked by the evidence program. Thus the displayed schedule
does not extend to that pair merely by lengthening its runs while keeping
$C$ synchronized. No universal obstruction for synchronizing $C$ is
inferred from a leaf-count bound.

## Phases and run matching

Before the first finish, between doubles two trees play *ping-pong* with
swaps while the third waits at the bottom. Suppose $t$ emits a single
naming $s$. Then $s$ must answer
with a single naming $t$ or with a double. After the double the stack is
$(t,f,s)$, so $t$'s next mark may not be a single naming $s$. A phase
therefore ends only when one side emits a double as the other side's run
of singles runs out. More precisely, if the phase starts with top $t$
and second $s$, the numbers of singles emitted before its ending double
are equal when $t$ emits the double, and differ by one in favor of $t$
when $s$ emits it. These endpoint conditions, not unconditional equality
of the two run lengths, must be matched.

A selected node can be *rigid* or *flexible*. A node selected in one game
only is *rigid*: every marked leaf below it is a single naming the same
tree. The
number of those leaves is fixed by $\sigma$ at the nodes below, each when it
is built. A node selected in both games is *flexible*: the policy chooses
how its two selected child lists interleave and which children they share.
These are order-preserving matchings, counted by Delannoy numbers. At a
flexible node of depth two, any word with the prescribed numbers of marks
for each tree can be realized. When the prescriptions differ at a flexible
node of depth zero or one, rigid children are unavoidable.

**Calibration at height one.** Here a tree's root is its only internal
node. With $m=q(\emptyset)$, Lemma 1 forces every count. $A$ has $m$
marks for each of $B$ and $C$, and $B$ has $m$ marks for $C$. Each second
tree's count is $m$ (outside) or $m-1$ (inside). For the outside type, all
doubles gives the rotation $(A,B,C)\to(B,C,A)\to(C,A,B)\to\cdots$, which
completes. For the inside
type, use the one-summand diagram on printed p. 1210:
$A=D\,C^{m-1}B^{m-1}$, $B=C^{m-1}D\,A^{m-2}$, $C=B^{m-2}D\,A^{m-2}$. Here
$D$ is a double, $X^r$ is $r$ singles naming $X$, and $m\ge2$. Its run
completes. For $m=1$, use $A=D$, $B=C$, and an empty word for $C$. For
$m=0$, only the outside case is possible: there are no marks and the
trees finish in order $A,B,C$. These statements concern the consistent
successor game specified above; they do not reconstruct the source's
limit-ordinal proof.

**The printed pattern does not transplant.** The inside diagram gives $A$
the word shape $D\,C^*B^*$: one double, then all singles naming $C$, then
all naming $B$. Suppose $\sigma$ selects at least two children at $A$'s
root and at least two at the depth-one node above $A$'s first marked leaf
in the game $(A,B)$. Then no arrangement gives $A$ that shape. That first
leaf $\ell$ is a double, so its ancestors $x_0,x_1,x_2$ are selected in
both games. The second $(A,B)$-selected child of $x_1$ comes after $x_2$,
and its leaves carry a $B$-mark. A second $(A,C)$-selected child of $x_0$
comes after $x_1$, and its leaves carry a $C$-mark. Neither mark may be a
second double, so a single naming $B$ precedes a single naming $C$. The
printed schedules separate the two games' splitting by ladder levels below
limit nodes. At height three every node is a successor node at which the
Architect prescribes, so that separation is not available. This rules out
only that schedule. The fixed-shape search below meets the hypothesis with
an inside pair whose first-tree shape has a root with two children: the
first has two children, the second one, and each depth-two node has one
leaf. It finds a schedule for that pair.

## Computations

The computations are in
[[research/erdos_592/height_three_evidence/_index|the evidence folder]],
whose program states its ranges and limits.

**Fixed-shape strategies.** Let $X$ and $Y$ be ordered trees of height $h$
whose leaves all have depth $h$. Suppose $\sigma$ selects the shape $X$
whenever it moves first in a game and $Y$ whenever it moves second. It
reads each count off the node's place in the selected tree and ignores the
numbers. Provided $Y$ has as many leaves as $X$ or one fewer, this is a
winning strategy for the colouring that is $1$ exactly on its outputs. That
colouring is normalized, since every output pair has unequal root counts.
Then $A$ carries $(X,X)$, $B$ carries $(Y,X)$ and $C$ carries $(Y,Y)$, and
the policies are exactly the merged mark words. The search is therefore
exhaustive for these strategies. It covers every pair with degrees at most
$d$ and at most $L$ leaves: $h=1$ ($d=L=6$), $h=2$ ($d=4$, $L=6$) and $h=3$
($d=3$, $L=6$; 33,278 pairs). It finds a deadlock-free schedule for every
pair, and an independent replay of the three games checks each schedule.

**Proposition 4 (erasing numerical and unselected history).** Suppose
$\sigma$'s prescription depends only on its own game's history after
erasing all numerical labels, full child positions and unselected nodes.
The retained history records the two tree roles, the ordered selected
nodes and their ordinal labels and counts. In particular, a prescription
cannot count the erased filler moves. Then the first tree's selection
tree is one fixed shape $X$ and the second tree's is one fixed shape $Y$,
whatever the Builder does. So $\sigma$ acts as the fixed-shape strategy for
$(X,Y)$.

*Proof.* Within a game, the next selected node to be built is determined
by the selection trees built so far, because play follows tree order and
switches at selected leaves. Unselected nodes receive one-element
prescriptions by Lemma 1 and add nothing to the selection structure. By
induction, the game's whole selection structure is a function of $\sigma$
alone. All three games start from the empty history, so they produce the
same pair. $\square$

Call such a strategy *number-blind* here. The fixed-shape search covers
every such strategy whose shapes lie in its range. A strategy outside
this checked class may read numerical labels, positions or filler
histories, or may have fixed shapes outside the range. Nothing in
Proposition 4 makes an arbitrary strategy invariant under this erasure.

One example shows that selections shared between games are needed. Take
the inside pair with $X$ the path $1$-$1$-$2$ (two leaves) and $Y$ the
path $1$-$1$-$1$. The schedule
$A{:}D,\ B{:}C,\ C{:}D,\ B{:}D,\ A{:}D$, followed by the finishes of $C$,
$B$, $A$, completes. Every schedule for this pair gives $A$ a double. Here
$A{:}D$ means that $A$ emits a double, and $B{:}C$ that $B$ emits a single
naming $C$.

**A finite adversary model with a coarse completion test.** A separate
probe lets an adversary see all three games and choose counts from $1$
to $K$ at every selected internal node, including the roots. Thus it
excludes empty root selections. The Builder chooses an ordered merge
after each pair of counts. The probe equates $A$'s two root counts and
$B$'s first-tree root count, and equates $A$'s counts while its initial
selections have remained common. These are only some of the equalities
that an actual strategy must respect.

The completion filter is deliberately weaker than correctness. A pending
selected subtree contributes at least one eventual leaf. An unexpanded
internal node is treated as allowing further growth without computing its
$K$-dependent upper bound. A pair is rejected if its two closed totals
are wrong, or if a closed total is already smaller than the other side's
required minimum. The probe does not prove that a surviving prefix extends
to a correct play with the bound $K$, much less to one game-local winning
strategy. It awards an adversary win upon a cycle, and Builder survival
when no admissible adversary move remains or a mark names a finished tree.
Exhaustive evaluation of this precisely defined finite process gives:

| height | $K$ | outside | inside |
|---|---|---|---|
| 1 | 3 | Builder survives | Builder survives |
| 2 | 2 | Builder survives | Builder survives |
| 2 | 3 | Builder survives | adversary wins |
| 3 | 2 | Builder survives | adversary wins |

For a concrete locality issue, compare root merges $BBCC$ and $BCD$ in
$A$, with counts $(2,2)$. The two $B$-selected positions and the maximum
can be identical in both arrangements. Before the first $B$-selected
child is built, the histories of $(A,B)$ can therefore be identical.
The global-state adversary is nevertheless permitted to give different
counts there, whereas a real $\sigma$ must give the same count. The model
also omits all numerical and unselected-node histories.

The inside loss at height two, where Theorem 28 is published, is a warning
against using this model to decide the source interface. No winning
game-local strategy or valid source-game counterexample is extracted.
In particular, the table does not establish that every universal schedule
must exploit a particular locality argument: its coarse completion test
is an additional discrepancy. The exact obstruction proved above for
$\sigma_{X,Y}$ does not rely on this model.

## The conditional bridge and the open gap

The held route has these links.

- **Normalization (author-recorded).** Equal-block pairs may be assumed
  to have colour $0$. This is author-recorded on the
  [[research/erdos_592/successor_tree_interface|interface page]], using
  Theorem 27 at statement depth.
- **Source interface S (author-recorded).** The
  [[research/erdos_592/successor_builder_theorem|finite-height reconstruction]]
  proves the dichotomy and finite-cover refinement for the coherent
  zero-based game by well-founded fusion and Nash-Williams, the latter
  an external statement-depth premise. It constructs the full-type
  color-$0$ family in the universal-Builder case by fresh-label stages,
  coarsening, and a finite-height freedom argument. Normalization is
  an explicit hypothesis of this Builder implication. The proof includes
  complete numerical and filler histories and gives a separate finite
  threshold for each current history and prescription. It does not
  extend the source interface to limit nodes. The local scheduling
  constructions themselves do not require S.
- **Local realization and fixed shapes.** Lemmas 1--3 and Proposition 4
  above are author-recorded. They give a finite model for a specified
  fixed-shape strategy, and a local extension rule for actual adaptive
  histories; they do not identify the two settings.
- **Gap G.** For every winning Architect strategy $\sigma$ on an infinite
  $H$ at height three, and every prescribed finite lower-threshold rule,
  construct three complete correct plays sharing the same three trees.
  A sufficient construction chooses actual numerical moves and child
  merges at the available histories while avoiding a cycle. This is the
  interface's unresolved three-game step.
- **Reduction of G (author-recorded).** Theorem 5 and Propositions 6 and
  7 construct the three plays, online and for actual histories, when all
  outputs are outside, inside top-first, or inside top-last. By
  Corollary 2 the remaining obligation is **G-mid**: the same
  construction for middle strategies.

Suppose a normalized colouring has no colour-$1$ triangle, and assume G.
Apply the author-recorded source interface S. In the Architect case,
G gives three legal plays with shared trees,
and their three outputs have colour $1$. This contradicts the assumption,
so the Builder case holds. Together with the author-recorded normalization,
this proves $\Omega_3\to(\Omega_3,3)^2$ conditional on G, and the
finite-cover reduction leaves G-mid as its open sufficient premise.

G splits into two parts along Proposition 4. Both parts are now proved
outside the middle class, and both remain open inside it.

- **G1 (fixed shapes).** Every pair of height-three shapes $(X,Y)$, with
  $Y$ having as many leaves as $X$ or one fewer, admits a deadlock-free
  schedule. This is a finite combinatorial statement about merging ordered
  trees. It is checked for degrees at most $3$ and at most $6$ leaves, and
  it is open in general. A proof would settle the number-blind class
  through Proposition 4 and the fixed-shape realization argument. The
  empty first-shape case is already handled by concatenating the three
  unmarked trees.
- **G2 (actual histories).** Strategies may read numerical labels, full
  child positions and all unselected-node moves. A new argument must
  handle their changing prescriptions without replacing them by counts
  chosen with knowledge of the other games. No canonization or uniform
  control of this dependence is proved here. A Ramsey reduction for two
  colors does not by itself make unbounded integer prescriptions
  constant on an infinite set.

The retained tools are these.

- *Identical histories.* While $A$'s initial selections and all numerical
  labels are common, its two histories and prescriptions agree.
- *Last-node forcing.* If every other selected-leaf count is determined
  and a single label-$1$ node is the only unresolved source of leaves,
  its count is fixed by Lemma 1(3). This does not determine a higher
  node's child count while its descendants' counts remain open.
- *The endgame.* After the first finish nothing can fail.
- *Flexible depth-two nodes.* Once both counts are known, they realize
  any ordered merge of those two prescribed leaf lists.

The difficult configuration is a rigid region whose eventual number of
marks is not known when an earlier shared child list is committed. Game
locality alone does not reveal that count before the numerical history
on which it depends exists. Lemma 2 resolves the current node's two
requests, but does not solve this forward-dependence problem.

A failure of three-output existence for fixed $\sigma,H$ and a specified
threshold rule would give a triangle-free graph of outputs obeying those
restrictions. Correct pair outputs determine their labels from their
induced partitions, so a triangle in that graph would itself supply three
coherent plays. This does not give a negative partition coloring on $W_3$. In fact the
[[research/erdos_592/pattern_level_obstruction|fixed-prefix obstruction]]
shows that every graph supported on disjoint leaf sets has a
full-order-type independent set on unrestricted $W_3$. A negative
construction must instead specify a full-type host and prove that
every full-type subset of that host contains a color-$1$ pair.

## Exact three-summand extension and obstruction

For the full countable target put

$$
\gamma=\omega^{\xi_1}+\omega^{\xi_2}+\omega^{\xi_3}<\omega_1,
\qquad \xi_1\ge\xi_2\ge\xi_3\ge0,
\qquad b_i=\sum_{j=1}^i\omega^{\xi_j},\quad b_0=0.
$$

Use a collapsible nested ladder on $[0,\gamma]$ as in Definitions 4
and 14, respecting these partial-sum boundaries. At a limit boundary
$b_i$ take $b_i(0)=b_{i-1}$, as in the remark after Theorem 12. Here
$b_{i-1}$ is zero or a limit: an infinite summand can only follow other
infinite summands in the displayed non-increasing decomposition. When
$b_i$ is a successor there is no ladder value $b_i(0)$ to prescribe;
the ancestral step is the ordinary predecessor step instead.

The missing replacement for Lemma 26 is this implication: for a
normalized coloring on this $W_\gamma$, an Architect win on an infinite
$H$, with history-dependent sufficiently-large bounds, implies a
color-$1$ triangle. Here normalized means color $0$ on equal block
types in Definition 12: equal root length at a successor root, and
equal root-child ladder index at a limit root. A sufficient stronger
construction uses the same winning strategy in three correct complete plays sharing
$T_1<T_2<T_3$. It has to satisfy all of the following simultaneously.

- At every shared successor node, the two maxima give the same full
  child list, including all unselected children; the two selected lists
  have the sizes actually prescribed at their respective histories.
- At every shared limit node, the common maximum gives the same
  ordinal-labeled child. The two sets $\delta$ specify splitting
  intervals in that same descendant tree; they are not lists of
  immediate children that can simply be interleaved.
- The Architect moves at each compulsory partial sum $b_i$ and at
  the optional lower nodes allowed by Definition 19. The collapsing
  maps $f^\alpha_{n,m}$ determining those moves must have compatible
  domains, images, and compositions in the shared tree, with the
  nested and commuting properties of Definition 14 retained.
- Leaf labels agree between the two games of each tree. The chronology
  in each pair is legal, its marked leaves are its true induced cell
  maxima, every label is sufficiently large, and the construction
  terminates. These requirements cover both inside and outside outputs,
  unless a justified finite-cover refinement removes a class.

The general-ladder dichotomy and Builder implication remain external
source inputs. The finite-height reconstruction does not establish
their limit-node compatibility. A replacement must state coherent
successor and limit conventions and check its composition with those
inputs; the finite-height proof alone does not supply that check.

At $\gamma=3$ the limit-node requirements disappear, but the middle
case still lacks a construction. The specific positive obstruction is
to the current phase templates: a shared child list of $B$ must place
its later double before the future prescriptions determining the
relevant size in $A$ have been made. The local merge lemma supplies
only the current two counts. Uniformity under erasing numerical and
unselected history is not available. This is an unproved scheduling
input, not a proof that G-mid is false. Fixed-shape schedules discharge
it only for strategies with those fixed prescriptions.

The negative direction has two separate outstanding inputs: a
triangle-free middle pattern or other coloring, and unavoidability in
every full-type subset of a specified host. The
[[research/erdos_592/pattern_level_obstruction|fixed-prefix embedding]]
proves that the unavoidability assertion on unrestricted $W_3$ is
false for every coloring supported on disjoint leaf sets, including
strategy-output graphs. The assertion on an appropriate separated
host remains unknown here. The containment interpretation is ruled
out by L67; the selection-shape interpretation is explicit but has
not supplied a triangle-free height-three pattern.

Thus neither direction decides $\gamma=3$, and no three-summand
Lemma-26 replacement is supplied. Reopening the positive construction
requires a rule handling the unknown future count, or a justified
refinement to strategies with a more usable dependency structure.
Reopening the negative construction requires both the specified host
and an exclusion argument respecting the actual shared trees. These
are obstructions to the recorded routes, not an impossibility theorem
for other approaches.

## Remaining test and standing

The positive route at $\Omega_3$ rests on the author-recorded
normalization and finite-height source interface S, and the unproved
G-mid, the three-game construction for middle strategies. Theorem 5
and Propositions 6 and 7 discharge G outside the middle class, online
and for actual histories.

The next discriminating test is G-mid. Its fixed-shape part asks for a
triangle schedule for every inside pair $(X,Y)$ at height three with $X$
middle. Lemma 8 excludes the two spine words for the second tree, and Proposition 9
settles the case of two children at the top split under a condition on
$Y$. The bounded census found schedules for all middle pairs in its
range, so a counterexample, which would be a triangle-free pattern
coloring, would have to be larger. The online part must place each double
of the second tree without knowing the size of the first tree's first
child. A failure of G-mid would not by itself give a negative partition
relation: that still needs a coloring of all pairs and a color-$1$ pair in
every subset of full order type.

The printed patterns support the reduction under the selection-shape
reading of the
[[research/erdos_592/pattern_level_obstruction|pattern-level page]].
All three are inside. Theorem 31's pattern is top-first and excludes only
six-cliques, and the triangle-free pattern of Theorem 33, at height four,
is middle. Its exclusion argument uses a level at which the second tree
has interior cells and the first has none, besides the first tree's own
two upper levels. At height three, once the first tree uses all three
levels, no such level remains. This is a heuristic for a positive answer,
not a proof.

The first-tree synchronization mechanism is closed by the symbolic
obstruction, and the fixed three-versus-two strategy is fully handled by
(3). A rule that instead keeps $C$ entirely synchronized is also not
general: the finite evidence contains a height-two fixed-shape
counterexample to that restriction. The literal $D C^* B^*$ transplant
has the branching obstruction above; Proposition 6 is exactly the class
in which it works.

The extension past $\gamma=3$ is not proved here. The constructions of
Theorem 5 and Propositions 6 and 7 use only successor nodes at which both
games prescribe. At a limit node on a spine the two games' labels must
share their maximum, which fixes the single child, while their sets
$\delta$ of ladder intervals can be chosen separately; each game's next
Architect move under Definition 19 is then a node of the shared tree, and
the spine merge applies at every successor node where either game
splits. This suggests that Theorem 5, Propositions 6 and 7 and the
reduction hold for every countable $\gamma$, but the check against
Definitions 11, 13 and 19 with limit nodes is open. Ladder levels give
the Builder freedom that height three lacks: in the printed one-summand
schedule they separate the two games of the first tree. So summands equal
to $1$, as in $\gamma=3$, are expected to be the hardest part of the
three-summand family.

All local arguments and computations are author-recorded and unreviewed.
Definitions 6--19 and the scheduling discussion of Lemma 26 were read in
the held journal transcription, with Definitions 9--11 on printed
p. 1200, the game rules on pp. 1203--1204 and the one- and two-summand
diagrams on pp. 1210--1212 inspected in page images. The two-summand
placement rules are stated through the sets $\delta$ of Definition 9(5),
which exist only at limit nodes. Read with $\delta$ replaced by the
selected positions at a successor root, the rule for $T_1$'s root
contradicts the diagram's first leaves, so the printed schedules do not
literally cover $\beta=2$. Theorems 19 and 21 and
Corollary 2 were read with their proof prose; the companion reconstruction
proves the finite-height source interface for the coherent game, using
Nash-Williams at statement depth. Theorems 27 and 28 supply external
statement-depth premises, not independently checked proofs. The negative
patterns in Theorems 31--33 are used only through the reading and
calibration stated on the pattern-level page. No negative coloring, full-order-type avoidance
proof, or resolution of $\Omega_3\to(\Omega_3,3)^2$ is claimed.
