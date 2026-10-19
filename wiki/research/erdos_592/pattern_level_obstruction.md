---
name: research/erdos_592/pattern_level_obstruction
title: A containment interpretation of pattern levels admits every finite clique
desc: |
  A subtree-containment reading of Schipperus's pattern levels makes the
  height-three pattern contain cliques of every finite size, even with
  distinct root lengths, but makes it impossible on good pairs. Under a
  reading by selection shapes, a triangle-free pattern must be inside and
  middle. On the unrestricted tree space a fixed-prefix embedding rules
  out every coloring supported only on disjoint leaf sets; a negative
  construction needs a separated host and unavoidability there.
problems:
- 592
created: 2026-10-14T13:48:56Z
updated: 2026-10-18T10:11:24Z
---

***

The negative-pattern route to
[[problems/set_theory/E0592/_index|Problem 592]] needs a precise notion of
a cell's level. In
[[../library/set_theory/schipperus_2010_countable_partition_ordinals/_index|Schipperus's journal paper]],
Definition 29 on printed p. 1214 uses $G(T,E)$, with $E$ a convex set of
leaf labels, whereas Definition 9 defines $G$ with a partition as its
second argument. The
[[research/erdos_592/successor_tree_interface|successor-tree interface]]
records this unresolved interpretation. The argument below rules out one
specific proposed completion of that notation. It does not identify the
intended definition or refute Theorem 32.

## What the containment rule gives

The exact rule and its two obstructions are recorded in
[[theory/ramsey_theory/L67_containment_pattern_levels/_index|L67]], at
tier 0. For a cell $E$, the proposed rule $R_1$ takes the label of the
lowest ancestor of $\max E$ whose whole leaf set is not contained in
$E$, except that first and last cells receive level $3$.

With this rule, the displayed height-three pattern

$$
A_3,B_3,A_1,B_3,A_2,B_3,A_1,B_3,A_3
$$

has cliques of every finite size. The explicit family uses four nested
bands of leaf labels and extra terminal root subtrees to give strictly
increasing root lengths. The
[[theory/ramsey_theory/L67_containment_pattern_levels/_proof|proof]]
checks all pairs symbolically; no finite search is used for this universal
conclusion.

On a good partition the same rule instead gives level $1$ to every
interior cell. Its maximum leaf belongs to $G(T,D)$, while the last child
of its label-$1$ parent does not. That parent therefore has a later leaf
outside the cell. Consequently neither the interior $A_2$ nor the
interior $B_3$ cells in the displayed word can occur on good pairs.

These are author-recorded deductions by Plasma AI, using the definitions
rather than a source theorem. Definition 29 and the displayed Theorem 32
pattern were checked against printed p. 1214. They do not identify the
intended source level.

## A reading by selection shapes

A second reading gives the printed patterns a definite meaning on good
pairs. For an interior cell $E$ of $T$, let its level $R_3(E)$ be the
level of the lowest common ancestor of $\max E$ and the last leaf of $T$
before $\min E$; first and last cells keep the top level, as in
Definition 29. Here the level of a node is $k$ when its ordinal label lies
in $(\beta_{k-1},\beta_k]$, so at finite height it is the label itself.

The leaf just before an interior cell is the maximum of the previous
cell, since the cells partition the ordered leaf set into consecutive intervals.
So $R_3$ assigns to each interior cell the level of the lowest common
ancestor of two consecutive selected leaves. A pattern word therefore
fixes the level word $\lambda$ of the first tree's selection shape $X$
and the level word $\mu$ of the second tree's shape $Y$. Each level word
determines its ordered selection tree. Under $R_3$ the three printed
patterns are fixed pairs of shapes. The table gives them at the finite
instances $\beta=2,3,4$, where the height equals the number of summands:

| source | height | $\lambda$ (first tree) | $\mu$ (second tree) |
|---|---|---|---|
| Theorem 31 | $2$ | $(1,1,1)$ | $(2,2)$ |
| Theorem 32 | $3$ | $(1,2,1)$ | $(3,3)$ |
| Theorem 33 | $4$ | $(1,1,3,1,4,1,3,1,1)$ | $(1,1,2,2,2,2,1,1)$ |

All three are of inside type. The steps of the printed proofs checked
here hold under this reading: that no second-level cell of $A$ is
isolated in Theorem 31, that no third-level cell is isolated and that the
next tree lies inside one second-level subtree of the previous one in
Theorem 32, and that $B$ isolates exactly one fourth-level cell of $A$ in
Theorem 33. The complete exclusion arguments were not re-derived, so the
reading is a calibrated proposal, not the identified intended
definition.

The reading connects the negative route to the
[[research/erdos_592/height_three_attack|height-three attack]]. By the
fixed-shape realization there, a pair of shapes has no triangle schedule
exactly when its $R_3$ pattern coloring has no color-$1$ triangle on good
pairs. The fixed-shape strategy for the pair wins for that coloring, so
Theorem 5 and Propositions 6 and 7 there give a triangle whenever the
pair is outside, top-first or top-last. A triangle-free pattern coloring
must therefore be inside and middle: neither the first two nor the last
two selected leaves of the first tree may split at its top split. This
matches the table. Theorem 31 is top-first and excludes only six-cliques.
Theorems 32 and 33 are middle.

Theorem 32's pattern has a triangle. In the mark-word notation of the
attack, the three words

$$
A:\ B\,D\,C\,C\,D\,B,\qquad B:\ A\,D\,C\,C\,C\,A,\qquad
C:\ A\,A\,D\,B\,B
$$

complete the stack process. Their separator levels are $(1,1,2,1,1)$,
$(3,1,2,1,3)$ and $(3,3,3,3)$, and the two projections of each word
recover $\lambda=(1,2,1)$ and $\mu=(3,3)$. This agrees with the census
in the attack's evidence and with the theorem's exclusion of only
four-cliques. A triangle-free pattern for three summands would have to
come from a larger middle pair; the census found none among its bounded
pairs. Its unavoidability in every subset of full order type would still
need a proof.

## A fixed prefix defeats disjointness on the unrestricted host

The unavoidability issue has a simple obstruction independent of the
choice of levels. For every finite $h\ge1$, every coloring of $[W_h]^2$
whose color-$1$ pairs have disjoint leaf sets has a color-$0$ subset of
the full type $\omega^{\omega^h}$.

To prove this, fix the unary tree $P\in W_{h-1}$ whose only leaf is
labeled $0$. Shift every leaf label of $T\in W_h$ up by one, and prepend
$P$ to the list of children of its root. Call the resulting tree $e(T)$.
Its root length is one greater than that of $T$, and its remaining
root subtrees have the same order as those of $T$. Thus $e$ is an order
embedding of $W_h$ into itself. Every leaf set of a tree in its image
contains $0$. No pair in the image can have color $1$, proving the
assertion.

In particular this obstruction applies to the graph of outputs of any
Architect strategy, with or without restrictions on the Builder's
infinite set or thresholds. Correct game outputs have disjoint leaf
sets. Such an output graph, colored $0$ on all other pairs of $W_h$,
therefore always has a full-order-type independent set. Failure of a
three-output construction cannot yield a negative partition relation
by this extension of its output graph.

This does not preclude a pattern coloring on a special full-order-type
host $Z\subseteq W_h$. An order isomorphism can transport a coloring
of $[Z]^2$ to the target ordinal without preserving the original leaf
labels. The
[[research/erdos_592/successor_builder_theorem|finite-height family construction]]
supplies such hosts independently of a coloring: unequal-root-length
pairs have disjoint full label sets and are good. A full-type subset
of such a host cannot be confined to a single root-length block, and
the fixed-prefix embedding above need not have its image in that host.

The exact missing negative assertion is consequently host-relative.
One must specify $Z$ and a color-$1$ pattern, prove that it has no
triangle, and prove that every $Y\subseteq Z$ with
$\operatorname{ot}(Y)=\omega^{\omega^3}$ contains the pattern. A proof
merely that $Z$ itself contains the pattern is insufficient. The
freedom argument in Schipperus's Section 12 begins with a special
full-type family; it cannot be applied as unavoidability on arbitrary
subsets of the unrestricted $W_h$. No new unavoidability theorem is
asserted here.

## Collapsing the four-level negative pattern

One possible negative construction is to merge two adjacent levels of
the height-four pattern of Theorem 33. Under the selection-shape
reading its words are

$$
\lambda=(1,1,3,1,4,1,3,1,1),\qquad
\mu=(1,1,2,2,2,2,1,1).
$$

Identifying levels $4$ and $3$ does not work. The resulting first shape
has four top children, single blocks of sizes $3,2,2,3$. Its last two
leaves are siblings, and the second shape's first three leaves are
siblings. Proposition 11 of the
[[research/erdos_592/height_three_attack|canonical sketch]] applies with
$|F|=3$, and supplies a triangle. This is a symbolic obstruction to
that collapse, including every large numerical realization of its
fixed shapes.

Identifying levels $3$ and $2$, and renaming the old level $4$ as $3$,
instead gives the concrete pair

$$
\lambda'=(1,1,2,1,3,1,2,1,1),\qquad
\mu'=(1,1,2,2,2,2,1,1).
$$

The first shape has two top children with block sizes $(3,2)$ and
$(2,3)$; the second has block sizes $(3,1,1,1,3)$ at level $2$.
No triangle exclusion or completing schedule for this pair is proved
here. In particular the published exclusion proof does not transfer:
it uses that the later tree isolates a level-$2$ cell while the earlier
tree has no such interior cell. The collapsed first word has interior
level-$2$ cells, so that hypothesis is false. Deciding this pair is a
specific finite structural test, still subject to the separate
host-relative unavoidability obligation. The ten leaves of its first
shape place it outside the retained census, whose leaf bound is six.

## Consequences for the route

The rule $R_1$ cannot support the four-clique exclusion required by that
pattern. Restricting pairs to different root lengths does not repair it.
The construction makes no assertion that its pairs are correct plays of
the Architect--Builder game or that they belong to the special full-type
set used in a source proof. L67 separately explains
why restricting this rule to good pairs does not recover the displayed
pattern. Any replacement rule still needs its exclusion proof and its
realization theorem.

Nor does finite height turn the game into a finite problem by itself.
At a successor node, Definition 9 gives one selected child position for
each child in $G$, together with the last child position. If the last
position is $m$, the full tree has $m+1$ children, however small the
selected set is. An increasing relabeling preserves the selected set's
order and size but can change $m$, so it need not preserve the underlying
tree. A bound on selected leaves does not bound these unselected child
subtrees.

Consequently, a finite pattern search requires a proved compression and
expansion rule, or an explicit bound on the full trees and a conclusion
limited to that bound. A positive three-game schedule must separately
handle strategy choices that depend on the numerical history, and must
realize arbitrarily large legal moves on the same three trees. A finite
static pattern and an adaptive winning strategy are not interchangeable
without such a bridge. Reopening the pattern route requires a justified
level definition and its actual tree constraints, calibrated against a
published negative relation before new searches are interpreted. The
selection-shape reading above is calibrated in that way against the
checked proof steps; under it, the fixed-shape realization of the attack
supplies the compression and expansion rule for pattern searches.

The held Darby paper supplies a concrete coloring for comparison. Its
[[../library/set_theory/darby_1999_negative_partition_relations_ordinals/definitions|Definition 3.5]],
on printed p. 212, defines $\Gamma_1$ by nine interleaved segments. The
outer two $A$ segments and every $B$ segment contain box coordinates; the
three interior $A$ segments contain none. Of those three, the middle
contains a triangle coordinate, while the other two are nonempty and
contain none. Encoding these requirements as levels $3,2,1$ gives exactly
the displayed word. Box and triangle coordinates are defined using
prefix levels and sublevels, so this comparison does not identify them
with the containment rule $R_1$ or with Schipperus's cut-piece levels.
Darby's Lemma 3.6 states that $\Gamma_1$ has no four-clique. Transferring
that exclusion to another model requires an actual correspondence of
coordinates and admissible pairs, not just the same word.

Darby's
[[../library/set_theory/darby_1999_negative_partition_relations_ordinals/theorem_6_1|Theorem 6.1]],
on printed p. 221, proves negative relations against a six-element target
when $\alpha$ is additively but not multiplicatively indecomposable, and
against a four-element target when also $\bar\alpha$ is not
multiplicatively indecomposable. In the problem's notation
$\alpha=\omega^\gamma$, these hypotheses correspond respectively to
at least two and at least three indecomposable summands in $\gamma$.
The four-summand negative relation against a triangle is instead attributed
to Schipperus in Theorem 6.4, without proof there; its printed exponent
and the surrounding interpretation are qualified on the theorem card.
Conjecture 6.9, on printed p. 222, explicitly leaves the three-summand
positive relation against a triangle open. Thus Darby's proved
four-clique exclusion calibrates a coloring, but does not decide the
three-summand question.

Definition 3.5 and the statements of Lemma 3.6, Theorems 6.1 and 6.4,
and Conjecture 6.9 were checked against the printed pages. The proofs of
Darby's exclusion and realization theorems have not been checked here.
The remaining source obligation is to compare those definitions with
Schipperus's Definition 29 and prove the needed transfer to the adaptive
game. Larson's
[An ordinal partition avoiding pentagrams](https://doi.org/10.2307/2586684)
concerns the two-summand negative relation with a five-element target;
its full pattern definitions and proof remain unexamined here. Neither
this comparison nor L67 removes the separate adaptive-scheduling gap.
