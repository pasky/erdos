---
name: problems/analysis/E0910
title: Problem 910
desc: |
  Asks whether every connected set in $\mathbb{R}^n$ has a connected subset that
  is neither a point nor homeomorphic to the whole set.
tags:
- Topology
status: open
claim: none
created: 2026-09-04T09:17:27Z
updated: 2026-10-19T04:19:00Z
---

# Problem 910

[[problems/analysis/_index|..]]

[[problems/analysis/E0910/claims/_index|claims/]]: The 1 claim page of Problem 910, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Does every connected set in $\mathbb{R}^n$ contain a connected
subset which is not a point and not homeomorphic to the original set?

If $n\geq 2$ does every connected set in $\mathbb{R}^n$ contain more than
$2^{\aleph_0}$ many connected subsets?

**Statement (modified).** Does every connected set in $\mathbb{R}^n$ contain
a connected subset which is not a point and not homeomorphic to the original
set? (Points and the empty set do not count as connected sets.)

If $n\geq 2$ does every connected set in $\mathbb{R}^n$ of dimension greater
than one contain more than $2^{\aleph_0}$ many connected subsets?

**Notes.** Both questions are defective as Bloom's catalog words them: the first
does not exclude points or the empty set, and the second reads Erdős's
dimension hypothesis as the ambient dimension. Bloom's catalog labeled the
problem DISPROVED and its commentary says that "the answer to both is in fact
no, as shown by Rudin [Ru58] (conditional on the continuum hypothesis)"; its
thread has no comments. The modified Statement follows Erdős's own words, which
the curator's credit presupposes for the first question: [Er44], printed p. 445,
asks "Is it true that every connected set contains a connected subset not
homeomorphic to it? (Points do not count as connected sets.)", p. 443 states
the same convention, and [Er82e], p. 77, asks for a subset "which is not a
point"; the change inserts "(Points and the empty set do not count as connected
sets.)". For the second question [Er44], printed p. 446, asks whether "every
connected set of dimension greater than 1 contains $2^c$ connected subsets",
and [Er82e], p. 77, whether "every connected set (in a Euclidean space) of
dimension greater than one contains more than $c=2^{\aleph_0}$ connected
subsets"; the hypothesis is on the set's own dimension, and the change inserts
"of dimension greater than one". The erdosproblems.com wording reads that phrase
as the ambient dimension $n\ge2$. The curator's verdict follows [Er82e], where
Erdős writes that "Mary Ellen Rudin using the continuum hypothesis found the
required counter examples" to both questions. For the first question Rudin's
theorem gives countable complements, and the paper neither states nor proves
that every nondegenerate connected subset of her set is homeomorphic to the set;
that step is asserted by [Er82e] and erdosproblems.com and has not been found
here. For the second question Rudin's set has dimension one (Progress below), so
it answers erdosproblems.com's ambient wording under the continuum hypothesis
but not the corrected question, and [Ru58] does not support the attribution
there. The first defect is already in [Er82e], which excludes points for the
subset only; the second is erdosproblems.com's. The $2^c$ form of [Er44] is a
variant.

**Status.** Bloom's catalog labeled the problem DISPROVED on the strength of
Rudin's 1958 construction [Ru58]. Its commentary credits the construction, under
the continuum hypothesis, with a negative answer to both questions. That result
is recorded as a
[[problems/analysis/E0910/claims/1958_01_01_rudin|rejected conditional claim]]:
it answers the erdosproblems.com wording of the second question, and Rudin's
set, of dimension one, is outside the corrected second question. The page
departs from the DISPROVED label, as the Notes explain. The homeomorphism step
that the credit needs for the first question is not in the paper and is
unchecked here. A conditional claim derives nothing in any case, so the standing
is open.

**Source.** [erdosproblems.com/910](https://www.erdosproblems.com/910), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #910,
https://www.erdosproblems.com/910.

**References.**

- [Ru58] Rudin, M. E., A connected subset of the plane. Fund. Math. 46 (1958),
  15-24.
- [Er82e] Erdős, P., Some of my favourite problems which recently have been
  solved. Proceedings of the International Mathematical Conference
  (Singapore, 1981), North-Holland Math. Stud. 74 (1982), 59--79. Chapter V,
  §4, printed p. 77. Library home:
  [[../library/discrete_geometry/erdos_1982_my_favourite_problems_which_recently_have/_index|erdos_1982_my_favourite_problems_which_recently_have]].
- [Er44] Erdős, P., Some remarks on connected sets. Bull. Amer. Math. Soc. 50
  (1944), 442--446,
  [users.renyi.hu/~p_erdos/1944-06.pdf](https://users.renyi.hu/~p_erdos/1944-06.pdf).
  The convention on points, printed pp. 443 and 445; the non-homeomorphism
  question and the arc remark, printed p. 445; the dimension question,
  printed p. 446. Not an erdosproblems.com source key.

**Formalization.** None recorded.

## Current assessment

Rudin’s theorem gives, under CH, a nondegenerate connected planar set with at
most $\mathfrak c$ connected subsets, of dimension one, and its construction has
not been reconstructed. Nothing on this page removes CH from Rudin’s theorem or
settles either question of the modified Statement.

The source statements below are recorded at the stated scopes; complete source
proofs remain uncompiled. See
[[../library/analysis/rudin_1958_connected_subset_plane/_index|Rudin's source record]]
for the CH theorem and its distinct historical target.

Primary sources:
[Rudin 1958](https://matwbn.icm.edu.pl/ksiazki/fm/fm46/fm4612.pdf),
[Erdős 1944](https://users.renyi.hu/~p_erdos/1944-06.pdf), and
[Erdős 1982](https://users.renyi.hu/~p_erdos/1982-33.pdf); the physical and
PDF page numbers on this page index these files.

No separate wider status-search date or scope is recorded on this page.

The dimension argument in Progress is author-recorded, and no retained record
reviews it.

## Progress

Rudin's *A connected subset of the plane*, Fundamenta Mathematicae 46 (1958),
15–24, explicitly assumes the continuum hypothesis (CH). Her theorem (printed
p.15 / physical p.1) gives a nondegenerate connected planar set $M$ such that
every nondegenerate connected subset $N\subseteq M$ has $M\setminus N$ at most
countable. The full construction has not been reconstructed or independently
reviewed here.

This property gives the following conditional consequence for the second
question as Bloom's catalog words it. Write $\mathfrak c=2^{\aleph_0}$. Since
$M\subseteq\mathbb R^2$, there are at most $\mathfrak c^{\aleph_0}=\mathfrak c$
at-most-countable subsets of $M$. The map $N\mapsto M\setminus N$ is injective,
so there are at most $\mathfrak c$ nondegenerate connected subsets of $M$.
Singletons add at most $\mathfrak c$ more subsets, and allowing the empty set
does not change the bound. Under CH, therefore, the erdosproblems.com wording of
the second question fails already in ambient dimension two. The corrected
question also needs $M$ to have dimension greater than one, and $M$ has
dimension one, as the next paragraph shows, so the bound says nothing about the
corrected question.

Rudin's set $M$ has dimension one. Dimension here is topological dimension, as
in Hurewicz and Wallman: homeomorphic spaces have the same dimension, and no
subspace exceeds the dimension of its space. A space of dimension zero with
points $p\ne q$ has a set both open and closed that contains $p$ and has
diameter below the distance from $p$ to $q$, which separates the space; $M$ is
connected and nondegenerate, so its dimension is at least one. $M$ contains no
open disc, since a disc $D\subseteq M$ would contain a segment $N$, a
nondegenerate connected subset of $M$ with $M\setminus N\supseteq D\setminus N$
uncountable, against Rudin's theorem. A subset of the plane has dimension at
most two, and dimension two only if it contains a nonempty open set of the plane
(Engelking, Dimension Theory, Theorem 1.8.10; Hurewicz and Wallman, Theorem
IV 3), so $M$ has dimension at most one. The upper bound also follows from
Rudin's definition of the continuum $I\supseteq M$ alone, without the theorem.
By conditions 1.1 (1) and 1.2 (5) of [Ru58], links of a chain meet only when
adjacent and the links of $\Gamma_n$ have diameter below $1/n$, so the sets
$L\cap I$, $L$ a link of $\Gamma_n$, form a finite closed cover of $I$ of mesh
below $1/n$ in which no point lies in three members. Thickening each member by a
small amount, less than half the least distance between disjoint members, keeps
disjoint members disjoint, so $I$ has arbitrarily fine finite open covers in
which no point lies in three members, and $I$, with it $M$, has dimension at
most one. Every homeomorphic copy of $M$ in $\mathbb R^n$ therefore has
dimension one, and none satisfies the hypothesis of the corrected second
question.

The first clause requires a separate transfer. Rudin's direct citation is to
Erdős's *Some remarks on connected sets*, Bull. Amer. Math. Soc. 50 (1944),
printed p.443 / physical p.2: the conjecture that every nondegenerate connected
$C$ has a nondegenerate connected subset $C'$ with
$|C\setminus C'|=\mathfrak c$.
That is different from the non-homeomorphism question on printed p.445 /
physical p.4. The countable-complement theorem by itself does not show that
all nondegenerate connected subsets of $M$ are homeomorphic to $M$. The
first-clause implication remains unresolved on the checked materials.

The 1944 cardinality question is a variant. The 1944 paper, printed p.446 /
physical p.5, asks for $2^{\mathfrak c}$ connected subsets when the connected
set itself has dimension greater than one. The corrected second question
keeps that hypothesis and asks, with Erdős 1982, for more than $\mathfrak c$
subsets, a weaker conclusion. Rudin's set has dimension one, so it bears on
neither form.

Erdős's *Some of my favourite problems which recently have been solved* (1982),
§4, printed p.77 / physical p.19, lists the non-homeomorphism question and a
more-than-$\mathfrak c$ question with intrinsic dimension greater than one, the
corrected second question. Erdős attributes counterexamples to Rudin under CH.
This is a historical attribution: the homeomorphism transfer it needs for the
first question is unchecked, and for the second question Rudin's set, of
dimension one, does not meet the hypothesis. Physical p.18 is printed p.76 and
concerns the different measurable-differences problem.

Rudin's optimality remark (printed p.15) says every nondegenerate connected
set has a nondegenerate connected subset with infinite complement. It cites
Erdős 1944 p.443; that external proof is not independently reviewed here.
Rudin's printed p.24 / physical p.6 is §4, proving connectedness and the
countable-complement property of her main construction, not the separate
optimality remark.

**A deduction and its scope.**
[[research/erdos_910/product_thickening_obstruction|Product thickening creates many connected subsets]] gives the author-recorded
argument and source boundaries: a nondegenerate connected planar set times an interval has a connected dense core and freely attachable boundary fiber, giving two to the continuum connected subsets.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/analysis/rudin_1958_connected_subset_plane/_index|rudin_1958_connected_subset_plane]]

<!-- END problem library links -->
