---
name: research/erdos_132/unrestricted_frontier
title: Unresolved steps and failed unrestricted approaches
desc: |
  States the remaining unrestricted gap, proves a regular-core completion
  lemma, and gives an exact obstruction to scalar Fourier positivity.
sources: []
research_state: blocked
created: 2026-09-22T21:35:00Z
updated: 2026-10-14T00:26:52Z
---


# Unresolved steps and failed unrestricted approaches

***

Neither assertion of [Problem 132](../../problems/distance_problems/E0132/_index.md)
has been proved or disproved. No counterexample with $n\ge5$ and $R\le1$, and no
arbitrarily large bounded-$R$ family, has been obtained.

## Latest continuation: finite orders, long gaps, and precise obstructions

The full primary [six-distance classification](https://doi.org/10.37236/8565)
of Szöllősi--Östergård (2020) was checked. Its three thirteen-point
models all have at least two rare distances. Together with the
unique-diameter theorem this extends the [finite-order proof](small_orders.md)
to orders 13 and 14. The established range is 5 through 14 except
11. The rotational thirteen-point report is unnecessary for
this conclusion and remains unreviewed.

An [angular matching inequality](long_rank_gaps.md) proves that, under
$R(A)\le K$, every rich fixed largest rank $k$ satisfies
$r_{k-1}-r_k=O_{K,k}(\Delta/n^2)$. In an unbounded $R=1$ sequence,
all fixed top ranks therefore lie within $O_k(\Delta/n^2)$ of the
diameter. For general bounded rarity, gaps with a rare lower endpoint
are not controlled. The same note extends the odd-cycle contraction to
cycles whose edges are merely at least the disk radius, and proves
odd girth $\Omega_{K,k}(n^{1/8})$ for every fixed top-rank union.
A rich bipartite second-distance example explains why even cycles
do not give the same contraction.

The [immediate-shell surplus lemma](spectral_gaps.md) localizes the cycle
surplus of an $r$-graph core to pairs in $(r,2r)$. It counts pairs rather than
distinct lengths, so supplies no iteration forcing additional rare classes. The
[deletion-criticality examples](deletion_criticality.md) show that one spanning
bicyclic minimum graph can become rare after every deletion, even with nonstar
diameter and a sublinear global palette. Joint richness of the other classes is
still the missing input.

The [highest invariant-valuation level](dyadic_distances.md) always
contains a rare class; this does not iterate or cover split valuations.
The new exact six-point shell example further excludes a cactus-graph
shortcut. The [monic-quadratic cluster model](nonlinear_cluster_limits.md)
and [local patch field-alignment lemma](translated_triangles.md) retain
concrete subproblems, not global reductions. General cluster sizes and
near-linear many-anchor expansion remain unproved.

Targeted checks established the scopes above, but neither unrestricted
question was resolved.

## Previous continuation: stronger estimates, still no unrestricted resolution

The [three-off-circle theorem](three_off_circle.md) proves
$R(A)\ge2$ whenever $n-3$ points are concyclic. Its proof is finite:
small differences give a regular polygon with at most three holes,
two new palette-extension lemmas handle the extra hole patterns,
and first and second moments handle an added center. This does not
by itself settle arbitrary eleven- or thirteen-point configurations;
the latter order is excluded by the separate classification above.

The [refined short-incidence argument](quantitative_short_incidence.md)
counts each induced motion with its actual anchor multiplicity. It gives

$$R(A)+1\gg\frac{n^{1/64}}{L^{7/8}(\log(2n))^{1/8}}$$

for $L$ convex covering subsets, with an explicit exception-point
variant. In particular, divergence holds for
$L=o(n^{1/56}/(\log n)^{1/7})$ and $o(n)$ uncovered points.

The [arithmetic-palette obstruction](arithmetic_palettes.md) uses a
uniform lattice-point bound for ellipses. Under bounded rarity, covering
the squared-distance palette by progressions of polynomial length
requires at least $n^{1/10-o(1)}$ progressions. This is a restriction
on the global palette, not a progression-cover theorem for arbitrary
configurations.

The [weighted-circle argument](weighted_circle_energy.md) proves
$R(A)\ge m/4$ when a circle contains $m\ge C(q(A)+1)^{7/8}$ points.
It weights an anchor length by its number of anchor pairs, rather than
discarding it after any outside coincidence. This removes the angular
covering losses. The remaining $7/8$ threshold comes from the earlier
pinned-spectrum occupied-radius step, not from the new weighted count.
The resulting diameter-inactivity tradeoff is
$R(A)+t(A)+1\ge c n^{1/24}$.

The [moving-frame reduction](moving_frames.md) now applies to every
bounded-rarity sequence, not just $R=1$. Deleting a positive-sized convex
layer from a rich fixed-short-rank graph leaves linearly many roots of
noncollinear triangles. The bounded local palette supplies a single
triangle congruence type at linearly many roots. Convex difference energy,
the checked affine-group energy theorem, and the rich-motion second moment
then give

$$
\left|\bigcup_g g^{-1}C\right|
\gg_K n^{17/16}/\sqrt{\log n}.
$$

Every point of this union has its three anchor distances in the global
palette, but the updated, checked Solymosi--Zahl three-anchor bound gives
only $O_K(n^{12/7})$.
No contradiction follows. The many two-dimensional anchor strengthening
needed to close this exponent gap was not established. Long collinear
anchor sets cannot suffice, as an exact quadratic-size example shows.

At a fixed smallest-distance rank $\ell$, the quantitative short-incidence
estimate is $O_{K,\ell}(n^{55/56}(\log n)^{1/7})$.
In the $R=1$ reduction this permits
complete triangular patches of radius
$c n^{1/112}(\log n)^{-1/14}$ at linearly many centers. Their orientations
need not agree; growing patches alone do not provide the missing
many-anchor estimate.

The same improved three-anchor input gives $O(n^{5/7})$ centers per
minimum-lattice orientation, at least $\Omega(n^{2/7})$ orientations,
and $\Omega(n^{9/14})$ exceptional interior vertices in a one-rare
sequence. Any common finer triangular lattice must have
superpolynomial refinement. These bounds remain compatible with the
short-incidence upper bound.

The [four-point collision theorem](four_point_collisions.md) extends
the balanced analytic rarity increment to $b=4$, without generic-scale
exceptions. A three-value strict Monge matrix is excluded by nine
positive integer defects telescoping to at most six; a reflection-pair
analysis excludes nonflat cluster pairs. This does not prove the
corresponding theorem for arbitrary $b$, nor reduce arbitrary point sets
to collision families.

Finally, the [mixed-valuation certificate](mixed_valuation_selector.md)
rules out choosing maximal triadic valuation followed by maximal length
inside a dyadic shell. Its unit graph is two equally oriented equilateral
triangles joined by a bridge, with seven edges on six vertices. It obeys
the proposed simultaneous three-part residue restriction and has no
four-cycle. The other five lengths in the selected shell are rare,
so the per-shell existence question remains open.

These arguments were checked at the scopes stated in their proof notes.
No unrestricted proof or counterexample was produced for either target.
Stronger noncollinear-anchor bounds and larger analytic clusters remain
provisional research directions; no missing implication is being
assumed.

The new finite theorem, quantitative incidence proof, and
ellipse/palette argument were checked by the author and are
author-recorded. The new three-anchor theorem was checked in its
primary paper, including uniformity. The unsuccessful attempt to
improve the $7/8$ circle threshold by ordinary spectrum second moments
is recorded as an abstract set-system obstruction in
[weighted circle energy](weighted_circle_energy.md), not a Euclidean
counterexample. No unrestricted proof results.

## Preceding continuation: further restrictions, not a resolution

The [diameter-triangle theorem](triangle_diameter.md) settles the first
assertion whenever the diameter graph contains a triangle. A Reuleaux
triangle contraction controls inactive points, and an explicit lens
calculation handles its boundary paths; the sole golden-ratio exception
is resolved using the inactive set's diameter. The same contraction for
odd diameter cycles, combined with the long-core surplus, proves
rarity divergence for cycle length $o(n^{1/32})$. A cyclic $R=1$ family
would need a cycle of at least $(1/5-o(1))n$ vertices.

The [quantitative circle criterion](quantitative_circle.md) gives
$R(A)\ge m/4$ from $m\ge C(q(A)+1)^{31/32}$ concyclic points.
Consequently $R(A)+t(A)+1\ge c n^{1/96}$, with $t(A)$ the number of
diameter-inactive points. This still permits linearly many inactive
points.

The [translated-triangle bound](translated_triangles.md) combines convex
difference energy with the checked Sharir--Solymosi three-anchor theorem.
If $q(A)=O(n)$ and there is a linear-sized convex subset, any translated
family of a fixed noncollinear triangle has only $O(n^{5/6})$ members.
Thus a hypothetical $R=1$ sequence must have
$\Omega(n^{1/6})$ minimum-lattice orientations, no macroscopic
minimum-distance component, and a first nonlattice length. At least
$\Omega(n^{7/12})$ minimum pairs touch its outer two layers. This does
not contradict their $o(n)$ upper bound.

For arbitrary triangle orientations the same anchor theorem gives
$|\bigcup_g g^{-1}C|=O((q(A)+1)^{11/6})$, but the needed lower bound
for this union is missing. Convex difference multiplicity controls
translations, not the rotational overlaps. No common orientation is
inferred.

The new [moment identity](distance_partition_algebra.md) detects the
earlier three-dimensional rank countermodels, but abstract one-rare
shell data can satisfy it and the gap test simultaneously. A rich
connected unit graph can have no nonzero equilibrium stress, as the
explicit example in [variational_reduction](variational_reduction.md)
shows. The exact [dyadic examples](dyadic_distances.md) exclude both
choosing either shell extremum and the proposed three-residue maximum
lemma. They do not exclude a rare class somewhere in each level.

The separate [thirteen-point rotational report](independent/c3_13_unreviewed.md)
is retained as unreviewed input, not included among the proved cases.
No counterexample to either target was found, and neither unrestricted
proof was completed.

## Previous investigation: profiles and nonlinear collisions

The [rich-degree profile lemma](rich_degree_profiles.md) proves that,
under $R\le K$, a positive fraction of points having the same degrees
in every rich distance graph forces a positive circular fraction.
Consequently every such profile fiber is $o(n)$ in a hypothetical
bounded-rarity sequence. No large fiber or bounded equitable partition
was derived from the global multiplicity assumptions; the attempted
partial-isometry extension does not supply one.

The [nonlinear collision theorem](nonlinear_cluster_limits.md) proves
that two analytic clusters of size $b=2$ or $3$, collapsing to distinct
points, have at least $b$ cross-distances for all sufficiently small
positive parameters. Thus an arbitrary balanced analytic doubling or
tripling of an $N$-point limit set $P$ has $R\ge R(P)+1$, even when
distance coincidences persist identically throughout the family.
This removes the generic-scale qualification for these two cluster sizes.

The general cluster-size statement is not established. Pointwise
ordered rows cease to be constant when the cross palette has three
or more values, and the proposed general distinct-entry bound for
strictly Monge matrices remains unproved here. Exact counterexamples
in [the collision note](nonlinear_cluster_limits.md) and
[the order-type note](order_type_relaxations.md) exclude the weaker
ordinal replacement, the distinct-row shortcut, and a minimum/maximum
deletion induction, not the general collision statement. No reduction
of arbitrary configurations to the proved collision families is known.

The checked claims, exact limitations, and unfinished $b=4$ status are
documented. Neither target assertion is resolved.

## Previous continuation

The [generic cluster-replacement theorem](generic_cluster_replacement.md)
proves $R(A_t)\ge R(P)+1$ for arbitrary fixed equal-cardinality branch
shapes outside finitely many scale parameters. Congruent shapes give
$R(A_t)\ge R(P)+R(S)$. This handles nonstationary fine-scale hierarchies,
but the exceptional parameters depend on the shapes and base. An
arbitrary configuration has not been reduced to a generic hierarchy.

The [first-exceptional-length lemma](first_exceptional_distance.md)
propagates a complete radius-two triangular patch to every point within
the first nonlattice length. Its edge lenses avoid the deep lattice
centers. In a hypothetical unbounded $R=1$ family, that exceptional
length cannot have bounded rank from either end of the spectrum.
Independently, the fixed shells $2^j\sqrt7$ and the pair budget show
$n/2-q(A)\to\infty$.

Neither empty lenses nor this palette deficit controls the middle-ranked
exceptional graph. A proposed universal estimate
$m_A(r_2)\le2q(A)+C$ would exclude unbounded $R=1$ families, but no such
estimate is established; $C=2$ already fails on an exact ten-point
two-ring example. Even that proposed estimate would not by itself
answer the finite first assertion or the general bounded-$R$ question.

Finally the [even-ring spectrum](second_distance_extremality.md) is
computed exactly. Its entire sufficiently small neighborhood, not merely
generic deformations, has at least $3n/4-2$ rare distances. Thus the
no-five-concyclic second-distance extremizers in that note cannot serve
as bounded-rarity examples. Remote portions of their framework variety
and arbitrary long-distance supports are not controlled by this local
calculation.

## Scope of the retained results

The latest checked results are recorded below and in their linked proof
notes. The circle-extension theorem is an exact finite result; the
triangular-lattice spectrum and component conclusions assume an unbounded
sequence with $R=1$. They are eventual assertions at each fixed normalized
scale, not estimates uniform over scales growing with $n$, and not
conclusions for every bounded $R>1$.

The unresolved step is to control the long distance spectra between
the outer layers and the separate lattice components, or the error
in the critical multiplicities $n+o(n)$. No argument forces a common
lattice, a linear-sized component, or a second rare class from these
reductions. Investigating the small global palette at that interface is
only a provisional direction. The remote-anchor and component-joining
examples refute only the indicated shortcuts, not the unrestricted
conjectures.

## Further consequences of the checked input

The [all-but-two-circle theorem](two_off_circle.md) proves $R\ge2$
whenever any $n-2$ points are concyclic, without restricting the other
two points. A small-difference lemma puts a hypothetical counterexample's
circular subset in a regular polygon with at most two missing vertices;
explicit palette tests exclude every extension. Together with the exact
convex equality classification, it also handles
[even-order all-but-two convex sets](nearly_convex.md). The arbitrary
odd-order two-exception case is not proved.

The [linear-aspect-ratio theorem](layers_and_obstructions.md) strengthens
the sparse-layer separation consequence: $\Delta/\delta=O(n)$ already
forces rarity divergence. Thus a bounded-rarity sequence must satisfy
$\Delta/(n\delta)\to\infty$. The proof uses perimeter, local packing,
the short-edge inverse, and the circle theorem.

For a hypothetical unbounded $R=1$ family, the
[triangular-core reduction](one_rare_asymptotics.md) now determines the
exact distance spectrum at every fixed scale relative to the minimum
distance. Every entire minimum-distance component eventually lies in a
triangular lattice, not merely its good-vertex subcomponents. Fixed
lattice shells have the computed multiplicities, but the six-vector
shells give only $n+o(n)$ pairs, whose error can still make them rich.
Different components need not share a lattice. Their long cross-spectra
and their spectra to the outer layers remain uncontrolled.

The [proximal-anchor inverse](remote_anchors.md) also treats short edges
near a convex subset. A grid-and-parabola example rules out extending
its annular-occupancy step to arbitrary remote anchors using geometry
alone; the example has a quadratic palette, so it does not rule out a
stronger argument using few distances. The
[long-core surplus bounds](diameter_activity.md) give linear branching
and larger-distance matchings, and force linearly many diameter pairs
in an $R=1$ family. These restrictions still do not connect the outer
long-distance support to the interior short-distance support.

## Comparison with the second independent input

The review of
[the second independent record](independent/large_distance_graph_and_convex_extension.md)
verified its $(2k-1)|B_k|$ large-distance bound, which improves the previous
$2k|B_k|$ coefficient in [the layer note](layers_and_obstructions.md). It does
not remove the large-layer/interior-support gap. Its warning that rare distances
need not survive restoration of omitted points remains valid; exact top-rank
support, not monotonicity of rarity, is what licenses the layer argument.

Two gaps in that record are already closed by established arguments.
The [unique-diameter theorem](unique_diameter_obstruction.md) excludes
its remaining twelve-point spectrum and, more generally, every even
$R=1$ counting-boundary spectrum. The
[short-edge inverse](short_incident_inverse.md) proves convex rarity
divergence and its fixed-cover extension. This latter result does not
assume the general near-minimum convex classification whose absence
the input correctly notes. It uses bounded rarity to supply a rich
fixed-short-rank class. On a convex subset of an arbitrary set, that
class may instead be supported wholly in the complementary interior,
so neither unrestricted assertion follows.

## Comparison with the third independent input

The [third independent report](independent/layer_bound_and_circular_majority.md)
does not change the unrestricted status. Its checked elementary
small-difference argument and explicit circular-majority estimate are
recorded in [regular cores](regular_cores.md). The existing
positive-fraction circle theorem is asymptotically stronger; the new
$6/7$ error exponent is not a circle-concentration threshold and does
not improve the weighted theorem's $q^{7/8}$ hypothesis.

Its convex-asymptotic gap is internal to that report, not a current
gap: the short-edge inverse already proves divergence for fixed
convex covers with $o(n)$ exceptions. Likewise the unique-diameter
theorem settles its twelve-point deletion obstruction, and the
all-but-two-circle theorem settles a broader geometric family than
its cocircular-hull argument. The actual remaining interior-support
and global-palette gaps described above are unchanged.

The warning about restoring omitted points is valid; no arbitrary convex-subset
rarity transfer is available. Its perturbation warning also remains valid for
class-splitting deformations, but must not be read as excluding the proved
[equality-preserving affine criterion](affine_deformations.md) or the
equality-preserving monotonicity in
[variational reduction](variational_reduction.md). The report's unavailable
companion files and unused Ramsey bound were not adopted as evidence merely
because the archived summary calls them proved.

## Short-edge incidence advance

The [short-edge incidence inverse](short_incident_inverse.md) proves the
asymptotic assertion for all strictly convex sets, and for a fixed convex
cover with $o(n)$ exceptions. It requires a fixed smallest-distance rank
with linearly many edges touching a convex subset. Narrow convex chains
have bounded pinned occupancy in intervals of that length; deleting the
overloaded bins leaves quadratically many anchored triangles of only
linearly many types. Their congruences supply the rich-motion hypothesis
that the older unlabeled energy argument lacked.

For arbitrary bounded-rarity sequences this says that every fixed short
rank has $o(n)$ edges touching any convex subset, uniformly over that
subset. It does **not** say that a large convex layer must meet a rich
short-distance graph. Such graphs can still be supported in the interior.
Deleting the layer preserves their low-rank richness, not bounded total
rarity in the remaining set.

For $R=1$, this gives the stronger
[two-layer/triangular-core reduction](one_rare_asymptotics.md): the first
two layers have total size $(2/3+o(1))n$, later fixed layers have $o(n)$
points, and almost every point in the remaining $(1/3+o(1))n$-point set
has six minimum-distance neighbors. Its regular-hexagon neighborhoods
propagate a triangular lattice within each good-vertex component, but
the components need not share a lattice. No incompatibility with the
outer layers has been proved.

An attempted stability shortcut is false: the
[even-order analytic deformation](second_distance_extremality.md)
attains exact $3N/2$ second-distance multiplicity while no five points
are concyclic. It also preserves both longest cyclic chord families
of the outer even polygon. The missing inverse must use the small
global distance palette, not just extremal second-distance counting.

The [two-cover diameter bounds](two_cover_diameter.md) also exclude
some additional finite cases. They do not resolve two-cover graphs with
few diameter edges and inactive points, much less arbitrary diameter
graphs. The $n+4$ matching-two second-distance extremum is excluded,
as is full second-distance activity at even order.

The new inverse and asymptotic reduction were checked by the author and
are author-recorded. Neither unrestricted target is complete.

## Finite orders and star results

The [star-diameter theorem](star_diameter.md) proves $R(A)\ge2$
whenever all diameter pairs share one endpoint. The generalized arc
inequality shows that three diameter neighbors make the second distance
rare; two diameter neighbors give an exact-minimum convex core after
deleting the three endpoints. Thus an unrestricted counterexample needs
diameter vertex-cover number at least two, not merely multiple diameter
pairs. The refined bound for exactly two disjoint diameter pairs is
$m_A(r_2)\le n+2+\min_v k_v\le n+4$, with notation and proof in that
note; it does not settle that case.

The [activity bounds](diameter_activity.md) provide a convex subset of
size at least $n-4m_A(D)+1$ when the second distance is rich. This is
not a constant-width or bounded-rank-error reduction. The attempt to
prove the needed arbitrary-convex inverse through a
[side-rank inequality](side_rank_attempt.md) did not succeed. That
inequality is proved for concyclic sets, while a proposed matching
bound $k+O(1)$ is false even there.

The [full fixed-similarity orbit theorem](full_similarity_orbits.md)
removes the formal-density assumption for full word image sets.
Distinct-map entropy and a convex-sumset theorem handle generators
without a common fixed point; angular-group counts and nested convex
hulls handle the common-fixed-point case, including reflections.
Arbitrary exact overlaps therefore do not supply a bounded-rarity
family through full orbits of fixed similarities. Sparse selections
and nonstationary maps are outside this conclusion.

The star theorem and the other documented arguments were checked by
the author for their stated scopes and are author-recorded. Neither
unrestricted question has been answered.

## Results from the preceding attempt

The [unique-diameter theorem](unique_diameter_obstruction.md) proves
$R(A)\ge2$ whenever the diameter is attained once. In the extremal
second-distance case, every point is active for that distance; deleting
both diameter endpoints leaves a strictly convex set, because each
remaining point has a supporting disk containing the remainder. Under
$R=1$, its distance count attains the convex minimum. Altman--Fishburn
classification and a two-point extension argument give a contradiction.
This also eliminates every even counting-boundary spectrum and settles
[order twelve](small_orders.md). A counterexample must now have at
least two diameter pairs, and at even order $q\le n/2-1$.

The [quantitative inverse lemma](quantitative_rank_inverse.md) gives
a circle of size $\Omega(m/(L+1)^3)$ in the existing constant-width
setting. It uses repeated adjacent-side patterns, two-anchor uniqueness
on a specified half-plane, and an adjusted index shift. It does not
produce the bounded rank omissions needed for an arbitrary layer.

The [similarity-word theorem](similarity_word_sets.md) excludes fixed
contractive-similarity constructions whose selected distinct images
have positive density in formal word space. Its measure argument
forces every fixed convex layer to be negligible. Vanishing-density
word selections and nonstationary maps are outside its assumptions.

The unique-diameter proof, the quantitative inverse, and the
similarity-measure proofs were checked by the author against their full
derivations and are author-recorded. These are proved restricted
results; neither unrestricted target is complete.

## The latest new approaches

The [spectral-gap lemma](spectral_gaps.md) is an unrestricted positive
result: any occurring $r$ with no distance in $(r,2r)$ is rare,
even when $2r$ occurs. Thus each consecutive ratio at least two
supplies a rare class distinct from the diameter. The factor is
sharp, and no argument forces such gaps in a bounded-rarity sequence.

[Angular interpolation](angular_interpolation.md) gives exact vanishing
moments and one nonzero terminal moment for complex barycentric
edge charges. An explicit rich unit class on six points makes both
its holomorphic real-part charge and its Hermitian charge take either
sign with unbounded magnitude. This rules out the proposed
richness-implies-fixed-sign step, not every possible use of the
identities under additional joint hypotheses.

The [weighted-diameter argument](weighted_diameter.md) proves the sharp
nonnegative quadratic vertex-weight bound, but that bound already
holds for all pseudoforests. More strongly, every linear forest is
individually a planar diameter graph. Since every induced highest-color
graph in the existing abstract obstruction is a linear forest, no
collection of tests of those graphs in isolation can exclude it.
The issue is their simultaneous realization by one planar point set.

The [order/sweep note](order_type_relaxations.md) gives an all-rare
affine image with the same sweep sequence, a finite-alphabet strict
Monge block violating planar squared-distance rank, and a necessary
linear surplus of isosceles configurations for $R=1$. These establish
precise limits of the scalar order relaxations. The surplus was not
shown to concentrate on a line or circle.

Both target questions remain unresolved.

## Subsequent checked additions

The [monotone-chain inverse theorem](monotone_chain_inverse.md) proves
that a strictly convex distance-monotone $m$-point chain with
$q\le m-1+L$, for fixed $L$, has a positive circular fraction.
Thus a chain of at least $n/2-O(1)$ points forces $R(A)\to\infty$.
A general convex layer need not supply a chain that large; a maximal
diameter side does not even imply distance monotonicity, as the exact
quadrilateral in that note shows. The three-cap decomposition alone
leaves linear rank excess.

For the first assertion,
[all but one point in convex position](nearly_convex.md) is sufficient. The
[unique-diameter equality case](unique_diameter_obstruction.md) is settled by
deleting both endpoints, without bounding either circular fan. This closes that
specific gap, but not the multiple-diameter or asymptotic gaps.

The [sumset note](minkowski_sum_layers.md) handles selected subsets
of bounded-factor digit sums with formal size $N$, giving growth when
$|A|/N^{2/3}\to\infty$, and $\Omega(|A|^{1/6})$ for fixed positive
density. This closes the earlier deletion gap only in that regime.
The [dyadic note](dyadic_distances.md) establishes a rare class at the
lowest norm level for split residue field $\mathbb F_2$, and a
characteristic-two good-reduction criterion. Neither gives an iteration
or forces a second class different from the ordinary diameter.

These are checked restricted results, not answers to either target.

The checked results in this wiki do not cover a large arbitrary convex
layer. The [layer reduction](layers_and_obstructions.md) shows that every
hypothetical bounded-$R$ sequence must have such an outer-layer
concentration; it does not show that the large layer is circular or
arithmetically suitable for the valuation theorem.

## What bounded rarity implies by counting

If $q$ is the number of distinct distances and $b=R(A)$, then

$$\binom n2\ge(q-b)(n+1)+b=q(n+1)-bn,$$

and therefore

$$q\le\frac{n(n-1)/2+bn}{n+1}
 =\frac n2+b-1+\frac{1-b}{n+1}. \tag{1}$$

For a convex set, Altman's lower bound is $q\ge\lfloor n/2\rfloor$.
Thus bounded $R$ forces a bounded additive excess over the minimum
number of distances. The exact-minimum configurations are classified
in the checked supplied sources, but the needed general near-minimum
stability theorem is not available there. Fishburn's source explicitly
conjectures only unboundedness of its rigidity allowance $f(n)$, not
$f(n)\to\infty$.

Also, for a convex configuration with $b\le B$,

$$\sum_{m_A(r)>n}(m_A(r)-n)
 =\binom n2-nq+\sum_{m_A(r)\le n}(n-m_A(r))\le Bn.$$

Small total edge excess does not force distance graphs to be close to
2-regular: many isolated vertices can be balanced by a denser component.
Nor does $m>n$ imply planar bar-framework rigidity, whose generic edge
threshold is $2n-3$. No low-rank distance-matrix argument converting
these counts into a large circular subset has been proved.

## A regular core would be enough

Here is a proved completion lemma, retaining one concrete possible
route beyond exact-minimum classifications. Let $V$ be a regular
$m$-gon, with center $o$, and put $\ell=\lfloor m/2\rfloor$. If

$$|D(V\cup\{p\})|\le\ell+L,\qquad \ell>5L+2,$$

then $p\in V\cup\{o\}$.

Normalize the circumradius to one and suppose $p$ is neither a vertex
nor the center. If $p$ lies off every reflection axis, its $m$ pinned
distances differ, contradicting $m>\ell+L$. On an axis, write
$p=re^{i\phi}$, $r>0$, and $h=2\pi/m$. The increasing squared chord
list is $x_i=2-2\cos(ih)$, $1\le i\le\ell$. The distinct increasing
pinned list has the form

$$y_j=r^2+1-2r\cos(\alpha+jh),$$

with consecutive angles in $[0,\pi]$ and length $k\in\{\ell,\ell+1\}$.
At most $L$ pinned entries are absent from the chord list. If $s$ is
the number of matches, then $s\ge k-L\ge\ell-L$, and the two lists
have at most $\ell+k-2s\le2L$ unmatched entries altogether. The ordered
matches therefore break into at most $2L+1$ runs consecutive in both
lists. Since $s>4L+2$, one run has three matches.

Writing $c=\cos h$, the two lists satisfy

$$x_{i-1}+x_{i+1}=2cx_i+4(1-c),$$
$$y_{j-1}+y_{j+1}=2cy_j+2(r^2+1)(1-c).$$

Three consecutive matches force $r^2=1$. But a new circle point on a
reflection axis has half-integer angular steps, whereas the old chord
list has integer steps. Their folded angles, hence squared lengths,
are disjoint. This contradicts $L<\ell$ and proves the lemma.

More generally, suppose $A$ contains $V\setminus S$ with $s=|S|<m/2$.
All chord lengths of $V$ survive: deletion removes at most $2s<m$
edges of a nondiametral class, and at most $s<m/2$ diameters. If
$q=|D(A)|$, restoring the missing vertices creates at most $s$ new
pinned distances from each $p\in A$. Hence

$$\ell>5(q-\ell+s)+2
\quad\Longrightarrow\quad A\subseteq V\cup\{o\}. \tag{2}$$

In particular an almost-complete regular core would suffice in the
regime $q=n/2+o(n)$, $m=n+o(n)$, $s=o(n)$. No argument obtaining
such a core from bounded rarity has been found.

### Stronger core results

The [regular-core theorem](regular_cores.md) removes the need for an
almost-complete core: a regular polygon containing a fixed positive
fraction of all points already forces linearly many rare distances.
The same holds for a fixed-density subset of a regular polygon whose
order is comparable to the subset size.

Kneser's addition theorem also gives a concrete geometric consequence.
For fixed $\varepsilon>0$, if $m\ge(1/2+\varepsilon)n$ points of $A$
are concyclic, then, for sufficiently large $n$,

$$R(A)\ge(2m-n)/6.$$

The proof uses bounded overlap of distinct cosine-grid spectra to bound
the number of occupied dihedral orbits, then counts chord classes whose
entire multiplicity stays on one circle. This improves the available
completion mechanism but does not prove that an arbitrary bounded-$R$
configuration has a regular core or a circular majority.

### Arbitrary circular subsets

The subsequent [cosine-incidence theorem](circle_incidence.md)
removes both those hypotheses. For any fixed $c>0$, an $m$-point
circular subset with $m\ge cn$ gives

$$R(A)\ge(m-1)/2-O_c(n^{2/3}).$$

Under $q(A)\le n$, the stronger estimate is
$R(A)\ge q(A)-O_c(n^{2/3})$.
The proof uses an incidence bound for translated cosine curves and
Ruzsa covering, not regular-polygon rigidity.

The later [hyperbola-incidence argument](algebraic_concentration.md)
proves the same qualitative conclusion for a positive collinear
fraction. Together with the Pach--de Zeeuw curve theorem, it implies
that every fixed-degree algebraic curve contains only $o(n)$ points
in a hypothetical bounded-rarity sequence. The degree is fixed, but
the curve can vary. The layer argument still forces a linear number
of points into finitely many outer convex layers. Ruling out this
combination remains the unrestricted gap.

An attempted connection with distinct-angle expansion did not close
it. It would need an independent $O_K(n)$ angle bound on a
linear-sized convex layer under $R(A)\le K$. The known pair count only
gives $q(A)\le n/2+K-1$; the direct side-length description gives at
most $O(q^3)$ possible angles, not the required linear bound. No
stronger implication was established. This is a provisional
possibility, not a proved reduction.

## A restricted constant-width inverse theorem

The [constant-width boundary theorem](constant_width.md) places
all diameter-active points on one boundary whose subdiametral
distance graphs have maximum degree two. The new
[inverse theorem](constant_width_inverse.md) proves that a subset
$C$ of such a boundary with $q(C)\le |C|/2+L$, for fixed $L$,
has a positive fraction on one circle. Its proof uses bounded
omissions in ordered pinned-distance lists, finite van der Waerden,
and propagation of one rotation through three anchors.

This proves rarity growth when at most a fixed number of points
are diameter-inactive. A merely positive-fraction boundary anchor
does not meet its hypotheses: if $|C|=cn$, the pair budget permits
$q(C)-|C|/2$ to be linear in $n$. Equivalently, with
$d_r=|C|-m_C(r)$ and with all global distance values included,

$$\sum_r d_r=|C|q(A)-\binom{|C|}{2}$$

can be $c(1-c)n^2/2+O(n)$. The per-row omission count therefore
need not be bounded. No argument has bounded the number of
diameter-inactive points in a hypothetical bounded-rarity sequence.

For shortest-distance graphs, the [linear convex local-spectrum and
cross-matching bounds](short_distance_structure.md) are proved. They still do
not control numerous isolated or widely separated components. A near-spanning
boundary-chain conclusion, bounded branching, and an inference to two uniform
[long-diagonal families](long_chord_rigidity.md) remain unproved. The relevant
fixed-rank literature was identified, but no unread theorem from it is used to
assert these missing conclusions.

## A remaining arithmetic question

In an invariant dyadic valuation with nontrivial residue conjugation,
it is unproved here that every occurring valuation level contains
some rare distance. This would imply growth for a fixed finite residue
field. Taking the maximum distance of the level is false, as the exact
six-point certificate in [the obstruction note](layers_and_obstructions.md)
shows. Finite checks of one grid domain do not establish the weaker
per-level statement.

The invariance assumption matters: a
[split-prime construction](dyadic_distances.md) now disproves
per-norm-level rarity without it, even for rational squared
distances. This does not decide the invariant-prime question.

There is one limited positive observation. If a level contains only
one Euclidean distance $D$, that class is rare. Its blocks are complete
multipartite graphs with every cross-part distance equal to $D$.
Two parts can form only a star or $K_{2,2}$: two circle centers have at
most two common neighbors. With three parts, each part has size at
most two, and $K_{2,2,1}$ is impossible. Indeed, taking its singleton
as center puts the other four points on a radius-$D$ circle, on which
two distinct points have at most one common chord-$D$ neighbor.
Four parts would give four equidistant planar points. The only remaining
graph with more edges than vertices is $K_{2,1,1}$, the two equilateral
triangles sharing an edge. Its same-part tips have squared distance
$3D^2$, at the same dyadic norm valuation as $D^2$, contradicting their
membership in one child. Thus each block has at most its vertex count
in edges. This does not handle levels with two or more rich classes.

## Scalar radial Fourier positivity cannot suffice

For an actual configuration, angular averaging of the squared Fourier
sum gives

$$1+\frac2n\sum_r m_A(r)J_0(rt)\ge0\qquad(t\in\mathbb R).$$

Even this condition together with the exact integer pair budget and
the diameter bound does not force a second rare class. For every
sufficiently large odd $n$, set $k=(n-3)/2$ and prescribe

$$m_1=\cdots=m_k=n+1,\qquad m_{k+1}=(n+3)/2.$$

Their sum is $\binom n2$, and only the last is at most $n$. There are
increasing positive radii $r_1<\cdots<r_{k+1}$ making the corresponding
Bessel sum strictly positive everywhere.

To prove this, first note that $1+2J_0(t)>0$ for every $t$. It is one
third of the angular average of the squared exponential sum on a
unit equilateral triangle. In the direction perpendicular to one
edge, two phases coincide, so the modulus of that sum is at least
one; continuity makes its average positive. Since $J_0(t)\to0$ at
infinity, there is a positive global lower bound $\delta$.
The limit follows, for example, by writing $J_0$ as the Fourier
transform of the integrable density $1/(\pi\sqrt{1-u^2})$ on $(-1,1)$.
Thus $1+(2+2/n)J_0(t)>0$ uniformly when $2/n<\delta$.

If $f(t)=1+\sum a_iJ_0(r_it)$ has positive infimum $d$, and
$0<b<f(0)$, add $bJ_0(Rt)$ with $R$ sufficiently large. On a fixed
small interval about zero, $f(t)>b$ and $J_0\ge-1$ give a positive
bound. Outside that interval, choose $R$ so large that
$b|J_0(Rt)|<d/2$. The sum remains uniformly positive. Start with
$f(t)=1+(2+2/n)J_0(t)$, whose positive infimum was just proved, and
then add the remaining prescribed coefficients, finally $1+3/n$,
while increasing the radii.

These shell data are **not planar realizations** and may violate even
metric triangle constraints. They only disprove a positivity-only
relaxation as a proof route.

## Status of the work

### The subsequent unrestricted attempt

The renewed attempt produced neither a complete proof nor a counterexample.
The following are the precise outcomes, not additional assumptions that
can be used to close the argument.

The [motion-incidence note](motion_incidence.md) checks an applicable
inverse theorem: linearly many direct motions with linear overlap on a
strictly convex set force a positive circular fraction. Its additive
alternative is excluded by $E_+(C)\le3|C|^2-2|C|$. But the available
bound $q(C)=O(|C|)$ supplies only a cubic second moment of motion
overlaps, not those linearly rich motions or a quartic triangle moment.
No implication filling that gap was proved. Investigating such a
promotion is a provisional direction, not an established final lemma.

The [local inheritance estimate](short_distance_structure.md) after
deleting a convex subset of size $cn$ has error $O_c(\lambda s)$
below cutoff $\lambda r_s$. It does not bound the residual set's
total rarity, so no induction through convex layers follows. Likewise,
the attempted turning-word argument established neither bounded
word complexity from short chord lengths nor the necessary long
boundary chain.

The [matrix certificates](distance_partition_algebra.md) show that
uncentered squared-distance rank four, conditional negative definiteness,
and numerical class restrictions still allow three-dimensional $R=1$
sets. One satisfies the exact even-boundary spectrum; another satisfies
all hereditary diameter graph restrictions. They are not planar examples.
The centered-rank-two condition remains essential and has yielded no
new multiplicity inequality.

The [five-point dyadic obstruction](dyadic_distances.md) rules out a
universal arithmetic shortcut: its equality pattern has no injective
realization admitting a conjugation-invariant dyadic valuation. Thus a
change of algebraic realization cannot bypass the split-prime case.
The nontrivial-residue per-level question remains unanswered, and even
an affirmative answer to it would not complete the general reduction.

The construction search found no viable unrestricted family. The
[two-square extension certificate](circular_configurations.md) rules out
adding at most three points to that eight-point $R=2$ model: its smaller
diameter stays rare and remains below the full diameter. A second finite
extension test yielded no counterexample and is not used as an exhaustive
classification. A proposed general
stability statement for tiny clusters around regular polygons was not
checked to completion and is not incorporated as a theorem. There is
no claimed perturbation transfer or construction beyond the proved
scopes in the existing notes. No new exhaustive grid search was run.

The rational and ramified-characteristic-two bounds, line-cover bound,
sparse-layer theorem, one-off-circle theorem, and fixed-ring construction
obstructions are proved partial results. They do not combine into a
proof for arbitrary planar sets. The missing structural or arithmetic
step is substantive, not a matter of checking a finite configuration.
