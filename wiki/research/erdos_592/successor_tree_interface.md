---
name: research/erdos_592/successor_tree_interface
title: The successor-tree interface at omega to the omega cubed
desc: |
  Equal-block normalization for finite-height ordinal trees follows from
  Erdős-Milner with a factor-two increase in root length. At height three,
  a fixed strategy defeats one synchronization mechanism but admits another
  schedule. A companion proof supplies the coherent finite-height source
  interface; compatibility for every adaptive middle strategy remains open.
problems:
- 592
created: 2026-10-14T11:11:14Z
updated: 2026-10-17T22:11:11Z
---

***

This note is Plasma AI's reconstruction of a step in Schipperus's route to
[[problems/set_theory/E0592/_index|Problem 592]]. Write
$\Omega_d=\omega^{\omega^d}$ for a positive integer $d$. The first
unresolved case is $\Omega_3\to(\Omega_3,3)^2$. This is the case
$\gamma=3$ in the problem page's notation, and $\beta=3$ in Schipperus's
paper. It does not exhaust the three-indecomposable-summand family.

The
[[../library/set_theory/schipperus_2010_countable_partition_ordinals/theorem_28|published positive theorem]]
covers one or two summands. Its proof begins by arranging that pairs with
equal block type have color 0. The explicit reconstruction below supplies
that normalization for finite $d$. It leaves the three-game step open and
does not change the problem's standing.

## Root-length blocks

Use the ordered tree representation $W_d$ of Schipperus's Definitions 6--8.
For finite $d$, every branch has labels $d,d-1,\ldots,0$. All nonterminal
nodes are successor nodes. Leaves carry increasing natural numbers. A tree
is ordered first by the number of children of its root and then
lexicographically by the ordered list of its child subtrees.

Let $B_{d,n}$ be the trees whose root has $n\ge1$ children. Then

$$
\operatorname{ot}(B_{d,n})
=\bigl(\omega^{\omega^{d-1}}\bigr)^n
=\omega^{\omega^{d-1}\cdot n}.                         \tag{1}
$$

Here the product in the exponent is ordinal multiplication by the finite
integer $n$. To check the leaf-label restriction in (1), fix a finite bound
$M$. Trees in $W_{d-1}$ all of whose leaf labels exceed $M$ still have the
full order type of $W_{d-1}$: shift every leaf label by $M+1$. After any
initial list of child subtrees, the next subtree is chosen from such a
tail. Induction on the list length therefore gives the lexicographic order
type $\bigl(\operatorname{ot}(W_{d-1})\bigr)^n$. Starting from
$\operatorname{ot}(W_0)=\omega$ and summing over $n$ gives (1) and
$\operatorname{ot}(W_d)=\Omega_d$. This is the specialization of the
paper's Lemma 7 to finite height.

## Equal-block normalization

The external input is the Erdős--Milner implication stated as Theorem 27
on printed p. 1212 of
[[../library/set_theory/schipperus_2010_countable_partition_ordinals/_index|Schipperus's journal paper]]:

$$
\omega^a\to(\omega^{1+b},k)^2
\quad\Longrightarrow\quad
\omega^{a+b}\to(\omega^{1+b},2k)^2,
\qquad a,b<\omega_1,\quad k<\omega.                   \tag{2}
$$

Its statement is used as an external premise; its proof is not reconstructed
here. The letters in (2) are separate from the exponent of $\Omega_d$.

**Normalization.** If $\chi:[W_d]^2\to\{0,1\}$ has no color-1 triangle,
there is an order embedding $e:W_d\to W_d$ such that

$$
e(B_{d,n})\subseteq B_{d,2n}
\quad\text{and}\quad
\chi\restriction[e(B_{d,n})]^2=0
\qquad(n\ge1).                                         \tag{3}
$$

For $d\ge2$, put $\mu=\omega^{d-1}\cdot n$. Since $1+\mu=\mu$,
the trivial relation $\omega^\mu\to(\omega^\mu,2)^2$, followed by (2)
with $a=b=\mu$ and $k=2$, gives

$$
\omega^{\mu\cdot2}\to(\omega^\mu,4)^2.                 \tag{4}
$$

The trivial relation holds because either some edge has color 1, or the
whole set has color 0. By (1), the source of (4) is exactly the order type
of $B_{d,2n}$ and its first target is the order type of $B_{d,n}$. A color-1
four-set would contain a color-1 triangle, so (4) gives a color-0 subset of
$B_{d,2n}$ of type $B_{d,n}$.

For $d=1$, take $a=n$, $b=n-1$ and $k=2$ instead. Formula (2) gives
$\omega^{2n-1}\to(\omega^n,4)^2$. The block $B_{1,2n}$ has type
$\omega^{2n}$ and contains a copy of that source, so the same conclusion
holds, including $n=1$.

Choose an order embedding into each of these color-0 subsets. Since the
blocks $B_{d,2n}$ occur in increasing order, their union is the embedding
$e$ in (3). Thus the pulled-back coloring
$\widetilde\chi(T,S)=\chi(e(T),e(S))$ has no color-1 triangle and is
color 0 on every pair of equal root length. The embeddings need preserve
only the well-order. They need not preserve the underlying trees' ancestry
or their leaf labels: the game is played on the domain $W_d$ with the
pulled-back coloring.

Consequently, proving the desired relation for all colorings normalized
this way proves it for all colorings of $W_d$. If a coloring already has a
color-1 triangle, that conclusion needs no normalization.

## The remaining height-three construction

After (3), the
[[research/erdos_592/successor_builder_theorem|finite-height source interface]]
supplies an infinite set of natural numbers on which either every
sufficiently large Builder play wins, or the Architect has a winning
strategy. In the first case its Builder proposition gives a color-0
subset of the full order type. These are author-recorded proofs for the
coherent game, reconstructing the uses of Schipperus's Theorems 19 and
21 and Corollary 2 with Nash-Williams as an external premise. The
missing construction at $d=3$ is in the second case.

The successor indices in this note start at zero: a node with
$m=\max\Delta_x$ has children $0,\ldots,m$, hence $m+1$ children.
This agrees with Definition 9(4) and the paragraph after Definition 10 on
printed p. 1200. The paragraph after Definition 17 and the stopping rule in
Definition 18(1), on printed p. 1203, instead bound the number of children
by $\max\Delta_x$. The discrepancy occurs in the printed paper. A
construction using the zero-based convention needs its own dichotomy and
Builder implication. The companion proof supplies them at finite height;
changing indices alone is not that argument. Equality of the two maxima
at a shared node remains necessary under either convention.

More precisely, fix one such winning Architect strategy $\sigma$ on an
infinite $H\subseteq\omega$. It would suffice to construct three trees
$T_1<T_2<T_3$ in $W_3$ and, for each pair, a correct complete play against
$\sigma$ whose Builder moves are sufficiently large in $H$ and whose output
is that pair. Each pair then has color 1. This is a sufficient interface;
no equivalence with an arbitrary finite scheduling model is asserted.

At this parameter there are no limit nodes and no collapsing-ladder maps.
The source's Definitions 16--19 still impose the following constraints.

- Each tree has the same underlying child lists in its two games. At a
  shared nonterminal node the two finite label sets must have the same
  maximum, which fixes the last child index. The two sets can have
  different sizes when the two game histories prescribe different moves.
- The selected child positions determine the two sets of paths to
  nonfinal partition maxima. The partitions those paths encode must
  coincide with the actual alternation of the two leaf sets in each pair.
- The two labels on a shared leaf agree. The labels increase in the order
  required by each game, and the selected moves must meet the strategy's
  thresholds for sufficiently large play.
- At every place where both games prescribe an Architect move, both
  prescriptions must be satisfied. For height three, the only positive
  ordinal labels are $3,2,1$, all partial sums of $1+1+1$.

The source's one- and two-summand schedules on printed pp. 1209--1212
illustrate this obligation. A third-summand extension must specify which
nodes are shared by the two path sets, the relative order of the selected
child positions there, and the order of construction, and verify these
properties for every winning strategy. A successful construction for one
strategy or bounded labels does not establish this universal statement.

The alternative negative route must define a coloring on a specified
host of type $\Omega_3$, prove that it has no color-1 triangle, and prove
that every full-type subset of that host contains a color-1 pair.
The host matters: the
[[research/erdos_592/pattern_level_obstruction|fixed-prefix obstruction]]
rules out unavoidability on unrestricted $W_3$ for every coloring
supported on disjoint leaf sets. Failure of one positive schedule
does not supply the negative construction on a separated host.

## Limits of block-pattern tests

A [partial report by Patrick White](https://www.erdosproblemaday.com/report/592)
dated 28 July 2026 gives a useful warning about a relaxation. Its model
keeps an ordered word of labeled blocks and compresses pair projections,
but omits the shared trees. It constructs a word triangle even for the
four-summand pattern for which Schipperus's Theorem 33 excludes an actual
triangle. The report is an unreviewed source account, not an ordinal
proof. A computation in that model therefore needs a separate realization
argument before it can bear on the present interface.

The negative route also owes a precise interpretation of the journal
paper's Definition 29 on printed p. 1214. It writes $G(T,E)$ in defining
a block's level, whereas Definition 9 defines $G(T,D)$ for a partition
$D$, and the immediately preceding $E$ is a convex subset of leaf labels.
The public [earlier TeX](https://users.math.cas.cz/~jech/library/schipperus/countable.tex),
accessed 14 October 2026, instead describes the first ancestor not maximal
in its conjugacy class, without defining that term in the text inspected.
These expressions are not a ready specification for a checker. A proposed
interpretation must be justified against the tree structure and the
published pattern arguments. This notation issue is separate from the
positive-game interface above; it is not a refutation of any published
partition relation.

One specific completion of the notation fails: assigning a cell the label
of the first ancestor of its largest leaf whose leaves are not all in the
cell. The
[[research/erdos_592/pattern_level_obstruction|explicit nested-tree construction]]
makes Theorem 32's word under that rule contain cliques of every finite
size, even with strictly increasing root lengths. Conversely, every
interior cell of a good partition has level $1$ under that rule, so the
word cannot occur on good pairs. Both statements are proved at tier 0 in
[[theory/ramsey_theory/L67_containment_pattern_levels/_index|L67]]. They
rule out that interpretation, not the source theorem.

## Standing and useful next test

The author-recorded
[[research/erdos_592/height_three_attack|height-three test]] uses the
coherent zero-based successor game above. It gives a fixed game-local
strategy with selected shapes $1$-$1$-$3$ and $1$-$2$-$(1,1)$ for which
the mechanism requiring every selected endpoint of the first tree to
serve both games is impossible. The obstruction concerns the convex
depth-two subtrees, so changing numerical positions or adding filler
subtrees does not remove it. An explicit alternative schedule realizes
three complete games for this same strategy, for any infinite $H$ and
finite lower thresholds. The failed mechanism therefore gives no negative
ordinal partition relation.

Its finite checker exhausts the stated bounded pairs of fixed shapes and
checks the alternative schedule and its shared-tree realization. A fixed
shape prescribes selected child counts independently of later numerical
choices. That hypothesis is stronger than the requirement that a strategy
use only its own game's actual history. In particular, the finite census
does not decide the adaptive-strategy interface above.

The combined route distinguishes three interfaces: **S**, the
[[research/erdos_592/successor_builder_theorem|author-recorded coherent
finite-height source argument]]; **G1**, compatible schedules for all
fixed height-three shapes; and **G2**, compatible construction for
strategies that read actual numerical choices and filler histories.
The latter two remain open in the middle class isolated by the attack.
G1 is only the fixed-shape special case of G2. Together with S and the
normalization, a general construction for middle strategies would
prove the positive relation at $\gamma=3$.

The normalization proof and the specialization of the interface to finite
height are author-recorded. No independent review or formalization is
claimed. Definitions 6--19, Lemma 7 and the relevant game statements were
read from the held transcription; the schedules, Theorem 27 and Theorem 28
were also read on printed pp. 1209--1212. Definition 29 and the
three-summand negative pattern were checked against printed p. 1214.
The successor-index discrepancy was checked against printed pp. 1200 and
1203; the transcription agrees with those pages.
Neither the full positive theorem nor the negative pattern arguments were
independently verified.

The next discriminating test is an invariant for schedules that permit
single endpoints and survive the completion of actual histories. It must
work for arbitrary strategy-prescribed sizes and sufficiently large
labels; expanding the fixed-shape census alone does not test that
requirement. A finite model must retain common child counts and path-set
consistency and recover the known one- and two-summand constructions.
Bounding the number of selected
$G$-leaves does not bound the full successor trees: their last selected
positions also prescribe all the intervening child subtrees. Likewise,
a static pattern's triangle test does not supply a schedule against an
adaptive strategy. Any compression to a finite model must prove these
interfaces. No finite-basis theorem or successful three-summand schedule
is supplied here. A positive result for $d=3$
would give the instance described by the
[[research/leads/four_clique_versus_triangle_colors/_index|four-clique lead]],
while the remaining countable three-summand parameters would still need
their own argument.
