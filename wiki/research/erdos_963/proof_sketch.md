---
name: research/erdos_963/proof_sketch
title: 'Dissociated subsets: current argument'
desc: Improved recursive universal bound from affine extraction and congruence extensions, with precise remaining gaps; the target remains unresolved.
tags: []
sources: []
created: 2026-09-18T20:28:04Z
updated: 2026-10-16T06:44:50Z
---


# Dissociated subsets: current argument

***

## Target and status

For nonempty finite $A\subset\mathbb R$, let $d(A)$ be the largest
cardinality of a subset having pairwise distinct subset sums. The target is
equivalent to

$$
|A|<2^{d(A)+1}.
$$

No proof or counterexample to this target has been established. The work is
incomplete. The sound partial arguments and the precise remaining assumptions
are recorded below. The
[[research/sharp_dissociated_subset/proof_sketch|bounded-ratio extraction sketch]]
contains the author-recorded L212 and L213 proofs, including the universal
bound $d(A)>\log_2 n-\log_2\log_2\log_2 n-4$ for $n=|A|\ge2^{16}$.
Those results have tier 0; the separate L22 Lean warrant applies only to its
own statement. The same sketch records L270's obstruction to a stronger
recentered odd-set certificate condition, without resolving the catalog target.

## Proved baseline

Choose an inclusion-maximal dissociated subset $D\subseteq A$. If
$a\in A\setminus D$, a nontrivial signed relation on $D\cup\{a\}$
has coefficient $1$ or $-1$ at $a$, since $D$ is dissociated.
Consequently

$$
A\subseteq\left\{\sum_{d\in D}\varepsilon_d d:
\varepsilon_d\in\{-1,0,1\}\right\},
\qquad |A|\le3^{|D|}\le3^{d(A)}.
$$

This proves only $d(A)\ge\lceil\log_3|A|\rceil$.

## Exact remaining gap

Maximum-cardinality dissociation must supply additional structure beyond this
ternary spanning property. Replacing the three coefficient choices by two is
not justified by maximality. Translation of an ambient set is also not allowed
without a separate argument: unequal-cardinality subset-sum relations change.

## Proved reductions

Let $P=\{|a|:a\in A,\ a\ne0\}$. Changing individual signs preserves
dissociation, and a dissociated set contains neither zero nor an antipodal pair.
Thus $d(P)=d(A)$ and $|A|\le2|P|+1$. The target is equivalent to
$|P|\le2^{d(P)}-1$ for every finite positive real set: the reverse
implication uses $A=\{0\}\cup P\cup(-P)$.

Every finite real configuration can be replaced by an integer configuration
preserving all ternary relations, distinctness, and positivity when applicable.
Choose a rational basis for the rational span of the given numbers. Their
coordinate vectors are rational. A rational linear functional sufficiently
close to the original real-valued functional preserves the signs of all
nonzero ternary combinations (there are finitely many); zero combinations
remain zero. Clear denominators. This is not a translation.

## New collision-code approach: proved restrictions, no resolution

The [[research/erdos_963/collision_trade_method|collision-trade note]] takes a
different route from congruence splitting and geometric lifting. For increasing
positive weights, let $L$ be the span of prescribed ternary relations and set
$\tau(u)_j=\sum_{i\ge j}u_i$. Such relations admit strictly increasing positive
weights exactly when

$$
\tau(L)\cap\mathbb R_{\ge0}^n=\{0\}.
$$

The necessity is summation by parts against the positive consecutive
gaps; sufficiency follows from a proved finite-dimensional separation
argument. This controls all linear trades, not merely individual
antichain collision fibers.

For $d=d(P)<n$, let $R$ be the largest support-minimal circuit size.
Counting circuit completions and the circuits inside $(d+1)$-sets gives

$$
\sum_{s=3}^{R}\frac{2^{s-2}\binom{d+1}{s}}{n-s+1}\ge1.
$$

Hence any counterexample $n\ge2^d$ must have
$R>\theta(d+1)$, where $H_2(\theta)+\theta=1$ and
$\theta\approx0.2271$. The existing high-girth bound supplies a
circuit of size at most six when $d\ge9$. No contradiction between
these short and long circuits has been established.

Two special cases are proved directly: circuits whose pairwise
intersections have size at most one are necessarily disjoint, giving
$d\ge2n/3$; and when all circuits have a singleton side, a
minimum-sum maximum dissociated subset positively subset-sum spans
$P$. Both imply the target under their respective hypotheses.
Mixed-sign overlaps give no restriction on a pair of circuits whose
orientation is free. The
[[research/erdos_963/pairwise_circuit_models|pairwise-model note]]
proves that with free signs and order the trade criterion forbids
exactly the implied relations of support at most two, that its
two-circuit content is the unique completion already used by the
counting bound, and that the ternary projective model satisfies all
such pairwise data with $(3^d-1)/2$ points and both forced circuit
sizes. Replacing a coefficient two by minus one in that model gives a
relation modulo three, while the corresponding real vector is not a relation.
One common positive orientation already excludes the model. In a fixed order,
the note's two-profile interval test gives the exact joint-realization
restriction for each pair, including short supports of sizes three through
six. No coupled covering bound follows. The ordered greedy estimate gives
the target for $d\le3$, but $18$ instead of $15$ at $d=4$, and has base
three asymptotically. Failure of this estimate does not refute the ordered
conditions. The retained 25-point construction has intersecting circuits of
sizes four and seventeen; its cardinality is below the counterexample
threshold. The full all-$d$ interface remains open.

A bounded, unbounded-height SMT attempt at $(n,d)=(32,5)$ produced
neither a validated counterexample nor an UNSAT certificate. The
[[research/erdos_963/continuation_routes|continuation note]] also records exact failures
of two new auxiliary ideas: merging the two smallest weights can
increase dimension, and threshold Euler variation does not distinguish
dissociated odd sets from dependent ones. The universal estimates below
remain unchanged. The target is unresolved.

## Strongest current universal argument

The [[research/erdos_963/affine_eight|eight-point theorem]] proves that eight
distinct reals contain an affinely dissociated five-set. The subsequent
[[research/erdos_963/affine_fourteen|fourteen-point theorem]] proves that fourteen
distinct reals contain an affinely dissociated six-set. Both are
structural extraction arguments, not searches over integer intervals.

For the latter theorem, a seven-point set without an affine five-set
is first classified as a translate of
$\{0,\pm a,\pm b,\pm(a+b)\}$. In a hypothetical fourteen-point
failure, every nonconstant binary character annihilating short balanced
relations splits the points $7+7$. Two independent such characters
apart from the constant one would have intersection size $7/2$;
hence the short-relation kernel has dimension two. An affine
normalization makes the points integers, with parity fibers two such
hexagons. Explicit compatible triples, one in each fiber, exclude
all additive quadruples. Balanced six-term relations are excluded
by the parity of their three points in each fiber. This gives the
required affine six-set.

For general affine dimension, the matrix of all short balanced ternary
relations annihilates both the degree and weight vectors. Its binary
kernel therefore supplies a nonconstant coloring that lowers affine
dimension in both classes. Induction propagates the fourteen-point theorem:

$$
|X|\le13\,2^{d_{\rm aff}(X)-5}\qquad(d_{\rm aff}(X)\ge5).
\tag{A}
$$

Ordinary dissociation is not replaced by affine dissociation here.
The passage back uses congruence and positivity. A positive integer
unit class modulo $q$ of ordinary dimension $d\le q$ has affine
dimension exactly $d$: a relation on at most $d+1$ points has
coefficient sum divisible by $q$ and magnitude at most $d-1$.

The [[research/erdos_963/congruence_extension|extension proof]] goes one
dimension further for even $q\ge4$. At $d=q+1$, split the unit class modulo
$2q$. A maximum $d$-set in one fiber can represent an element in the other only
as its total sum $S$ or as $2x-S$. There are at most two positive possibilities.
Large fibers therefore both drop dimension. A two-point fiber forces every
maximum set in the other fiber to contain the same midpoint, giving a deletion
argument. For a singleton fiber, positivity forces all short circuits through it
to have the same affine degree; the resulting second functional again permits a
binary-character split. Applying the eight-point affine bound after these
reductions gives $7\,2^{d-4}$ for $4\le d\le q+1$, $q\ge4$ even. With (A), it
improves further to

$$
|O|\le13\,2^{d-5}
\quad(5\le d\le q+1,\ q\ge6\text{ even}),
\tag{B}
$$

for a positive set in one unit class modulo $q$. The special
$q=4,d=5$ bound remains fourteen, not thirteen.

The [[research/erdos_963/congruence_grid|polynomial grid theorem]] settles the
endpoint $q=4,d=6$, with bound $31$. Split modulo eight and
suppose a full-dimensional fiber $A$ occurs. Its affine dimension is six; the
other fiber $B$ has at most twelve points. An affine binary split $A=U\sqcup V$
supplies a five-set $E\subset U$ such that every $E\cup\{a\}$, $a\in V$, is
dissociated. Each $b\in B$ must then satisfy a relation of type $1=5$ on that
set with $b$ adjoined. After excluding at most two constant values, these
relations place every pair $(a,b)$ on one of ten slope-one or five
slope-minus-one lines. Their degree-fifteen product has all leading coefficients
nonzero. Bivariate interpolation bounds $|V|+|B\setminus K|\le16$, with
$|K|\le2$. Since $|U|\le13$ by (A), the total is at most $31$.

There is also a direct ordinary-dissociation improvement:
[[research/erdos_963/positive_seven|every seven positive reals contain a dissociated
four-set]], sharply. A hypothetical seven-point failure must
have four odd and three even elements. Each even element induces
a triangle-free sum/difference graph on the four odds with a
perfect matching. The three possible matching labels, in either
possible odd four-point relation, cannot form the additive triple
required for the even part. This rules out simultaneous equality
in the separate odd/even bounds.

Write

$$
B_d=\min\{2^{d+\lfloor\log_2(d+1)\rfloor-1}-1,
2^{\lceil\log_2d\rceil-1}(2^d-1)\}
$$

for the established positive-set bounds when $d\ge2$. Put

$$
(U_0,U_1,U_2,U_3,U_4,U_5,U_6)=(0,1,3,6,14,42,104),
$$

and for $d\ge7$ put $q_d=2^{\lceil\log_2(d-1)\rceil}$ and

$$
\boxed{U_d=\min\{B_d,\ 13q_d2^{d-6}+U_{d-1}\}.}
\tag{C}
$$

Then

$$
\boxed{|P|\le U_{d(P)},\qquad |A|\le2U_{d(A)}+1.}
\tag{D}
$$

For (C), make the positive integer realization primitive at two.
Its nonempty odd part splits into $q_d/2$ unit classes, each
bounded by (B). Its even part has dimension at most $d-1$,
because one odd point can be adjoined. Symmetrization gives (D).
For the initial values, the sharp positive $U_3=6$ gives
$U_4=8+6=14$. The odd dimension-five count is at most $28$,
so $U_5=28+14=42$. The grid theorem gives odd dimension-six
count at most $62$, hence $U_6=62+42=104$.
The resulting values include

$$
U_5=42,\quad U_6=104,\quad U_7=312,\quad U_8=728,\quad U_9=1560.
$$

In particular $d(A)\le5$ forces $|A|\le85$, and $d(A)\le6$
forces $|A|\le209$. The required bounds are $63$ and $127$,
respectively, so the central question remains unresolved.

The affine note also proves the unit-class count $2^{d-1}$ through
$d\le q+2$ for even $q\ge6$, $d\le q+3$ for $q\ge10$,
and $d\le\lfloor4q/3\rfloor$ for $q\ge56$. In each case
a full-dimensional modulo-$2q$ fiber has the strict affine bound
(A), and a count of cross-fiber coefficient vectors fits within
its remaining $2^{d-4}$ allowance. These can sharpen (C) at some
further dimensions. They do not prove the unrestricted odd bound.

### Exact gaps after this improvement

The first unresolved strong odd case remains $F(5)\le16$;
we have only $F(5)\le28$. A least-dimensional failure at
dimension five must be primitive with common difference divisor two.
The unrestricted dimension-six odd bound remains $F(6)\le62$,
versus the desired $32$, although the one-class modulo-four
endpoint is proved. No joint odd/even inequality at general
dimension, nor a global compression from maximum-cardinality
dissociation, has been established.

The most concrete new mechanism is the grid theorem: a binary
split makes every point on one side extend a fixed independent
set on the other, so all representations simultaneously cover a
Cartesian product by a controlled family of lines. The next
substantive step is to obtain comparably small representation
families for unrestricted odd sets, or a joint parity count as
in the sharp dimension-three proof. Merely applying the existing
congruence estimates separately does not supply that step.

There is a dimension-uniform simultaneous-basis statement in
[[research/erdos_963/common_subsum|the common-subsum note]]. If $r\ge4$ is even and
a fixed value belongs to the $(r-1)$-sums of every affinely
dissociated $r$-subset of $E$ in a finite abelian $2$-group, then

$$
|E|\le2^{r-2}+\max\{r-1,2^{r-3}\}.
$$

Its proof combines a parity split with variable binary-tree
transversals. It gives the modular unit-class endpoint
$|A|\le2^{q-1}$ when $d(A)=q=2^s\ge8$ and $A$ lies in
one odd class modulo $q$. The mixed-sign representation families
of unrestricted odd sets do not satisfy the lemma's hypothesis;
no new bound on $f(n)$ follows yet.

More specifically, a hypothetical odd seventeen-set of dimension
five has a modulo-four class $A$ of size at least nine. Every
eight points of $A$ contain an ordinarily dissociated five-set,
by the eight-point affine theorem and congruence modulo four.
Every point $b$ of the other class must be represented on
**every** such five-set. Its representation coefficient sum is
$3$ or $-1$: congruence gives $3\pmod4$ and the only other
possibility, $-5$, would make the represented value negative.
No argument yet exploits these simultaneous requirements strongly
enough to rule out seventeen points. In particular, consistency
of affine degrees across all crossing circuits has not been proved.

The separate sufficient global cube-extension conjecture remains unproved. The
[[research/erdos_963/large_uniform_cores|new large-core theorem]] handles
every odd deletion core of size at least 761 and excludes size five, leaving odd
core sizes 7–759. This reduces a stated auxiliary gap; it does not justify
compatible successive lifts.

## Proved near-logarithmic bound via a binary tree

For every finite real set with $d=d(A)$,

$$
 |A|\le 2^{d+\lfloor\log_2(d+1)\rfloor}\le(d+1)2^d.
\tag{1}
$$

Here is a direct argument, independent of the supplied papers. Use the
integer reduction above. Choose $M$ large enough that the integers remain
distinct modulo $2^M$. Form the finite tree whose level $j$ consists
of their occupied residue classes modulo $2^j$, for $0\le j\le M$.
There is one terminal leaf for each integer; suppress vertices with just one
child. A binary
tree with more than $2^h$ leaves has a root-to-leaf path with at least
$h+1$ branching vertices. If its terminal leaf is $a$, choose one
integer from the other child at every branching vertex. The resulting
differences from $a$ have pairwise distinct 2-adic valuations: a split
from a class modulo $2^j$ into its two children gives valuation exactly
$j$. Here $v_2(z)$ for nonzero integer $z$ is the exponent of 2
dividing $|z|$.

Put $L=\lfloor\log_2(d+1)\rfloor$ and suppose
$|A|>2^{d+L}$. We obtain a pivot $a$ and $d+L+1$ other points,
whose differences $\delta_i$ from $a$ have distinct valuations.
If $a=0$, the other points are dissociated already. If $a\ne0$,
put $u=v_2(a)$ and delete the points for which
$v_2(\delta_i)\in\{u,u+1,\ldots,u+L\}$. There are at most $L+1$
of them, leaving at least $d+1$ points including $a$.
Choose $d+1$ survivors, including the pivot.

A ternary relation among these points has the form

$$
 s a+\sum_i\varepsilon_i\delta_i=0,
 \qquad |s|\le d+1.
$$

If $s=0$, pairwise distinct valuations force every
$\varepsilon_i=0$, and then the pivot coefficient is zero. If
$s\ne0$, the valuation of $sa$ belongs to $\{u,\ldots,u+L\}$,
whereas every remaining $\delta_i$ has valuation outside that range.
All nonzero terms therefore have distinct valuations, so their sum cannot
be zero. This contradicts the definition of $d$, proving (1).

In particular,

$$
 d(A)\ge\log_2|A|-\log_2(\log_2|A|+1).
$$

For the last inequality, if $d\ge\log_2|A|$ it is immediate; otherwise
substitute $d+1\le\log_2|A|+1$ into (1).
This does **not** establish the exact floor bound.
This argument is machine-checked as the native claim
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_index|L22]]
(tier 2 for the Lean sources and statement as they stood on 2026-09-28, the
default branch at 13:50:48Z, with its fidelity audit graded pass and the
warrant bound to the Lean v4.34.1 tree that the non-author clean gate of
2026-10-13 checked); the Lean transfers only the product form $(d+1)2^d$ to real
sets, while the sharper $2^{d+\lfloor\log_2(d+1)\rfloor}$ is proved there for
integer sets. The claim's
[[theory/number_theory/L22_near_logarithmic_dissociated_subset/_proof|proof page]]
maps the modules under `lean/Erdos/Problem963/`.

### A further bound from coherent supports

The proved affine-coherence argument in
[[research/erdos_963/affine_coherence|the new note]] gives, for positive integer $P$
of coherent dimension $C\ge2$,

$$
|P|\le2^{\lceil\log_2 C\rceil-1}(2^C-1).
$$

Its two ingredients are a binary-tree extraction of an affine-coherent
set of size $\lceil\log_2|P|\rceil+1$, and conversion to ordinary
coherence for an affine-coherent $k$-set in a unit class modulo $q$
when $k\le q+1$. The latter follows by minimizing total degree in the
integer fiber.

Since $C\le d(P)$, integer reduction and symmetrization give, for
$d=d(A)\ge2$,

$$
|A|\le
\min\{2^{d+\lfloor\log_2(d+1)\rfloor},
       2^{\lceil\log_2d\rceil}(2^d-1)+1\}.                 \tag{1a}
$$

This slightly improves the previous estimate at some dimensions,
but not to the requested logarithmic bound.

### The current geometric gap is global, not greedy iteration

A weaker sufficient geometric formulation is proved in
[[research/erdos_963/antipodal_lifts|the antipodal-lift note]]. Put $p_0=0$ and let
$H=\{u:\sum u_i=\sum u_i p_i=0\}$. A subspace $K\subseteq H$
gives an antipodal lift of these heights exactly when

$$
\max u_i-\min u_i\le\tfrac12\|u\|_1\qquad(u\in K).
$$

If such a $K$ could always be chosen with
$\dim K\ge |P|-d(P)$, the elementary packing bound for antipodal
sets would give $|P|+1\le2^{d(P)}$. This existence statement is
**unproved**. The note gives an exact five-vector compatibility
test for two augmented ternary relations.

Greedy projection fails for antipodal lifts even when every imposed
relation is a minimal ordinary ternary circuit.
For

$$
P=\{1,2,3,4,5,6,7,8,10,13,17,22,28\},
$$

the sum $126$ gives $d(P)\le6$. Six Schur-triple relations produce
a seven-dimensional cube lift containing
$0,e_1,\ldots,e_7,\mathbf1$, which admits no dimension-lowering
antipodal projection retaining all labeled points distinctly.
A different five-dimensional binary-digit lift already exists.
Thus earlier relations may have to be replaced,
not merely supplemented. This does not refute the global existence
statement and yields no improvement in the universal bound.

The [[research/erdos_963/global_lift_gap|global lift note]] proves that
arbitrary iteration of the normal empty-lift quotient is false:
$P=\{3,7,8,9,12\}$ has $c(P)=3$, but the valid first relation $0+2\cdot9=3+7+8$
gives an empty normal four-dimensional lift with no further empty
height-preserving projection retaining all vertices. An alternative pair of
relations gives a three-dimensional cube lift. The proof uses Howe's width-one
theorem for empty three-polytopes, checked in Scarf's primary source.

Thus a projection-minimal lift need not expose a coherent subset of
its dimension. Existence of a globally minimum lift of dimension at
most $c(P)$ is still unproved. The one-step construction can be made
Boolean in coordinates; that strengthening and a separate sufficient
full-sign-cover subspace statement are proved/formulated in the same
note. Neither supplies the required global replacement theorem.

### New structural progress without a resolution

The [[research/erdos_963/cube_two_relations|two-relation cube theorem]] gives a
cube-spanned codimension-two extension whenever two minimal even
ternary supports differ by more than one coordinate exchange.
The remaining codimension-two case reduces exactly to an odd
uniform core: $q$ odd coordinates with precisely one minimal
relation omitting each coordinate. Three-row replacements are
impossible there. A four-row construction works when two adjacent
coefficient classes each have at least $23$ coordinates; no
argument supplies such a choice or handles all sparse patterns.
This is progress on the sufficient global lift, not a proof of it.

A further [[research/erdos_963/cube_two_relations|sparse four-row criterion]]
handles normals of the form $(0,1,\ldots,1)$ and
$(1,0,0,2,-1,\ldots,-1,1,\ldots,1)$, with at least one $-1$
and two ordinary $1$ entries. Its cube solutions are exhibited
explicitly. A signed sum of three deletion relations can always
be chosen so that their special coordinates either all vanish,
or have only one coefficient $\pm2$ with coefficient $\pm1$ at
the fourth zero position. The ordinary $\pm1,\pm3$ coefficient
classes were not controlled by those criteria alone. The subsequent
[[research/erdos_963/large_uniform_cores|one-large-class criterion and balance dichotomy]]
settle every core of size at least 761, but not all smaller cores.

The [[research/erdos_963/forest_obstruction|new positive integer example]]
refutes the rainbow-forest assertion for **every** maximum subset. It has
$d(P)=16$ and nine colors whose entire graph on the subset sums of one maximum
$D$ is $K_{4,4}$, of rank seven. The existence and maximum-sum versions remain
unproved.

The [[research/erdos_963/half_size_reduction|half-size note]] strengthens the
necessary conditions on failures: every nonzero parity residue has multiplicity
at least two more than the zero residue; every odd failure has a rank-one short
presentation, without minimal-dimension assumptions. The
[[research/erdos_963/odd_reflection|odd reflection note]] proves one-dimension
augmentation through seven differences, but explicitly refutes general
two-dimension augmentation. None of these results improves the universal bound
(1a) or resolves the original target.

### Limits established before the latest improvement

The exact support formulation for the full-sign cover is
$h(p)=\min\{|\operatorname{supp}a|:Ea=p,\ a\ge0\}$, where $E$ lists all
sign-cube vertices. The natural linear-programming relaxation has value
$\|p\|_\infty$; an optimal extreme point can have more than $d(p)$ supported
columns, already for $p=(1,3,5,7)$. The
[[research/erdos_963/global_lift_gap|explicit LP certificate]] rules out
arbitrary extreme-point extraction, not existence of a suitable sparse optimum
or the cube-cover conjecture.

The [[research/erdos_963/maximum_sum_orbits|seventeen-point odd example]] shows
that ternary spanning and single-exchange sum optimality alone do not imply the
strong odd count: its chosen five-set has both properties, but the ambient set
contains a dissociated six-set. True maximum cardinality cannot be discarded.
For the forest approach, an inclusion-minimal deficient color family does yield
rainbow alternate paths by the established forest criterion, as proved in
[[research/erdos_963/forest_restrictions|the forest note]]. The missing step is still
converting the resulting color relations into a cardinality- or
sum-improving dissociated exchange; substituting representations
on $D$ need not keep coefficients in $\{-1,0,1\}$.

The proposal that differences of individual ternary representations
generate all short multi-element relations is false,
by the seven-point example explained in
[[research/erdos_963/parity_fibers|the parity-fiber note]]. Keeping the individual
representations does not preserve cross-relations. This reduction
is not used in any proved bound.

### Earlier continuation

That earlier continuation did not improve the universal bound (1a) or
resolve the target. It established the following narrower facts.

For $O\subseteq\mathbb Z/2^M$ lying in one signed odd class
$\pm a\bmod q$, where $q$ is a power of two dividing $2^M$,

$$
q\ge d(O)+1\quad\Longrightarrow\quad |O|\le2^{d(O)}.
$$

The endpoint $q=d(O)+1$ is included. A binary-tree cluster partition gives
affine-dissociated transversals; two transversals differing in one choice cannot
both have zero total. The full proof and remaining multiple-class gap are in
[[research/erdos_963/finite_group_observations|the group note]].

The [[research/erdos_963/global_lift_gap|global lift note]] now gives an exact
projective-line test for a cube-spanned extension of a rational $r$-space to
dimension $r+1$. This is a finite equivalence, not a proof that an extension of
the necessary dimension exists. The
[[research/erdos_963/convex_fibers|coherent-fiber note]] proves Boolean spanning
when vector coherent dimension equals rational rank; that case also has
dissociation dimension equal to rank and does not address positive rank defect.

The cyclic-half-window assertion for odd sets is still conjectural. It is proved
for generic positive evaluations of bipartite graphic configurations, as
recorded in [[research/erdos_963/half_size_reduction|the half-size note]]. No
valid general sliding-basis exchange was obtained.

Two additional shortcuts are ruled out exactly: full compression to an initial
interval can increase dissociation dimension
([[research/erdos_963/primitive_order_obstructions|the 13-point certificate]]),
and simple binary matroids cannot in general model all the needed independences
([[research/erdos_963/algebraic_observations|the four-point obstruction]]).
Neither obstruction is a counterexample to Erdős 963.

## Concrete obstacles

**Subset-sum coverage fails even after choosing the maximum subset.**
For $P=\{3,4,5,6\}$, the triple $\{3,4,5\}$ is dissociated and
$3+6=4+5$, so $d(P)=3$. A subset of $P$ whose subset sums
cover $P$ must contain 3, 4, and 5, since each is smaller than the sum
of the two smallest elements. But 6 is not a subset sum of $\{3,4,5\}$.

**Matching to positive supports fails for an arbitrary maximum subset.**
Take $P=\{1,3,5,7,8\}$, $D=\{1,3,5\}$. Every four-subset
is dependent, by one of $1+7=3+5$, $3+5=8$, or $1+7=8$,
so $D$ is maximum. Both 7 and 8 have only the positive support
$\{3,5\}$ in their ternary representations on $D$:
$7=-1+3+5$, $8=3+5$. This rules out this matching assertion for
arbitrary maximum $D$; no universal conclusion follows from the example.

**Affine dissociation cannot generally be upgraded by deleting one point.**
The set $\{2,3,5,7,12\}$ has distinct equal-cardinality subset sums.
Its pair sums are the ten distinct values
$5,7,8,9,10,12,14,15,17,19$; complementation checks cardinalities
three and four. But every four-subset has a relation among
$2+3=5$, $2+5=7$, $5+7=12$, and $2+3+7=12$.
The triple $\{2,3,7\}$ is dissociated, so the maximum size is three.

## A failed matching lemma (rigorous obstruction)

For a maximum dissociated $D$, write $S=\Sigma(D)$ and
$N(a)=\{s\in S:s-a\in S\}$. It is **false** that these sets always
have distinct representatives for the positive elements of the ambient set.
Take

$$
D=\{1,15,19,29,31\},\qquad P=D\cup\{7,22,37\}.
$$

Its 32 distinct subset sums are

$$
\begin{split}
S=\{&0,1,15,16,19,20,29,30,31,32,34,35,44,45,46,47,\\
&48,49,50,51,60,61,63,64,65,66,75,76,79,80,94,95\}.
\end{split}
$$

But $N(7)=\{51\}$, $N(22)=\{51,66\}$, and
$N(37)=\{66\}$, violating Hall's condition.

Here is a certificate that $d(P)=5$. Put
$X=\{7,15,22,29,37\}$, $Y=\{1,19,31\}$.
Every four-element subset of $X$ contains a relation from

$$
7+15=22,\quad15+22=37,\quad7+22=29,\quad15+29=7+37.
$$

A dissociated six-subset would consequently have to be $Y\cup T$,
where $T$ is a three-subset of $X$. The triples containing
$\{7,37\}$ are excluded by $7+31=1+37$; those containing
$\{22,29\}$ by $22+29=1+19+31$. The triples
$\{7,15,22\}$ and $\{15,22,37\}$ already contain displayed
relations. The remaining two triples are excluded by

$$
7+15+29=1+19+31,\qquad15+1+19+31=29+37.
$$


Matching to unsigned supports of ternary representations fails as well:
the unique representations of 7 and 37 are

$$
7=1-15+19-29+31,\qquad37=1+15+19-29+31,
$$

both with full support $D$. Deleting 22 gives an all-odd example of
this failure. This is not a counterexample to the target bound.

### Minimizing the basis sum does not repair unsigned-support matching

Let

$$
P=\{27,53,65,66,79,105\},\qquad D=\{27,53,65,66\}.
$$

The subset sums of $D$ are

$$
0,27,53,65,66,80,92,93,118,119,131,145,146,158,184,211,
$$

so $D$ is dissociated. The two omitted elements have the unique ternary
representations

$$
79=27+53+65-66,\qquad105=27-53+65+66.
$$

Uniqueness follows by checking the displayed subset sums: the only upper
endpoints of differences 79 and 105 are respectively 145 and 158. Both
representations have full support, violating unsigned-support Hall.

Every five-subset of $P$ is dependent. The two displayed relations handle
deletion of 105 or 79; the other deletions are handled by

$$
53+65+66=79+105,\quad27+65+79=66+105,\quad27+105=53+79.
$$

Thus $D$ is maximum. Since it consists of the four smallest elements,
it is the unique minimum-sum maximum subset. This excludes the minimum-sum
choice as a general repair; it does not exclude a matching for some other
maximum subset.

## The odd-slice reduction and low dimensions

The following stronger assertion would imply the target:

$$
|O|\le2^{d(O)-1}\quad\text{for every finite set of positive odd integers }O.
\tag{2}
$$

Indeed, partition a positive integer set into its nonempty 2-adic valuation
layers $P_1,\ldots,P_r$ in increasing order. Choosing one representative
from each earlier layer shows $d(P_i)\le d(P)-i+1$: every relation
using an earlier representative has a unique least valuation. In particular
$r\le d(P)$. Applying (2) to each scaled layer gives

$$
|P|\le\sum_{i=1}^{r}2^{d(P)-i}\le2^{d(P)}-1.
$$

Assertion (2) is not proved in general.

It is proved for dimensions at most three. Any two distinct positive numbers
are dissociated, and any three distinct positive odd integers are dissociated:
odd-support relations are excluded by parity, and a two-term relation would
require equality or opposite signs. Thus odd sets of dimensions one and two
have at most one and two elements, respectively.
For five positive odd integers $a<b<c<d<e$, suppose every quadruple
is dependent. In a quadruple the only possibilities are
largest = sum of the other three, or smallest + largest = middle two.
Applying this to $a,b,c,d$ and $a,b,c,e$ gives
$d=b+c-a$, $e=a+b+c$. Applying it to $a,b,d,e$ gives
$b=3a$; applying it to $a,c,d,e$ then gives either $c=3a=b$
or $c=a$, a contradiction. Thus five positive odd integers contain a
dissociated four-subset. The layer argument proves
$|A|\le2^{d(A)+1}-1$ whenever $d(A)\le3$. Consequently sets of
sizes 2, 4, 8, and 16 have dimension at least 1, 2, 3, and 4, respectively.
Monotonicity gives the requested bound for every $n\le31$.

### Nine positive odd integers contain a dissociated five-set

This additional small-case assertion is proved. Suppose that
$O=\{x_1<\cdots<x_9\}$ had $d(O)\le4$. For any dissociated
four-subset $D$ and any $x\in O\setminus D$, a dependence on
$D\cup\{x\}$ must use $x$. Parity makes its support even, and
distinct positive elements rule out support two. Thus $x$ is a signed
sum of exactly three members of $D$.

For a positive triple $p<q<r$, the only absolute signed sum using all
three that can be smaller than $p$ is $|p+q-r|$. Consequently
each triple of $D$ represents at most one element below $\min D$.

Write the four largest elements as $u<v<w<M$. If these were
dissociated, their five smaller companions would have to be represented
by their four triples, which is impossible. Their dependence therefore
has one of the forms

$$
M=u+v+w,\qquad u+M=v+w.
$$

Put $a=x_5<u$. The set $D=\{a,v,w,M\}$ is dissociated: its
only possible dependencies would be $M=a+v+w$ or $a+M=v+w$,
each incompatible with either displayed relation and $0<a<u$.
The four elements below $a$ must therefore be represented by the
four triples of $D$. But $\{v,w,M\}$ offers only the small
candidate $|v+w-M|=u>a$, so it represents none of them. The
remaining three triples can represent at most three, a contradiction.

Thus (2) holds also when $d(O)=4$. The valuation-layer argument
gives $|P|\le15$ when $d(P)\le4$, and hence
$|A|\le31$ when $d(A)\le4$. Every 32-element real set contains
a dissociated five-subset. Together with the earlier cases, this proves
the requested floor bound for every $n\le63$.

## Current gap

The exact floor bound remains unproved. The universal bound (1) allows
$|A|$ as large as $2^{d+\lfloor\log_2(d+1)\rfloor}$, whereas the
target requires $|A|\le2^{d+1}-1$. No counterexample to the latter is
known from this work. The new proved rank-defect cases below reduce a
counterexample to intrinsic defect at least four. The matching and cyclic
routes afterward are conditional only.

### A new convex-geometric avenue

The new [[research/erdos_963/convex_fibers|integer-fiber approach]] uses a
stronger property than dissociation. A positive set $D=(a_1,\ldots,a_k)$ is
called coherent when $\mathbf1$ is a vertex of

$$
\operatorname{conv}\{u\in\mathbb Z_{\ge0}^k:
                     a\cdot u=\textstyle\sum_i a_i\}.
$$

Coherence is hereditary and implies dissociation. If $c(P)$ is the
maximum coherent-subset size, it is exactly the largest support of
any vertex of any nonnegative integer knapsack fiber on the weights
$P$. Thus the stronger assertion $|P|\le2^{c(P)}-1$ would prove the
target, but it remains unproved here.

The following facts were proved:

* Every inclusion-maximal coherent subset $D$ generates $\mathbb ZP$.
  More precisely, failure to extend it by $p$ forces
  $\sum D+p\in\mathbb ND$ and $\sum D-mp\in\mathbb ND$ for some
  integer $m\ge1$.
* Every dissociated positive triple is coherent, as is every
  dissociated four-set of positive odd integers.
* The stronger coherent bound holds for positive integer sets with
  $c(P)\le3$, using the established five-odd-elements theorem and
  the coherent version of valuation-layer extension.

An exact cost-interval criterion for coherent extension is given in
the new note. A possible global route is to build an empty lattice
polytope in dimension at most $c(P)$ with at least $|P|+1$ vertices;
the parity bound for such polytopes would finish the argument.
Neither this construction nor a bound on simultaneous failures of
the cost-interval criterion is established.

The [[research/erdos_963/convex_route_obstructions|obstruction note]] rules out
three shortcuts: maximum coherent sets need not ternary-span; coherent
largest-element exchange fails; and the canonical ternary image lattice does not
yield an irredundant origin-vertex system, already for $\{1,2,3\}$. It also
gives exact obstructions to using only monotone antipodal cube topology or
Fourier mass supported on maximum subset-sum cubes. These failures do not
disprove the original bound or the stronger coherent cardinality conjecture.

There is a proved [[research/erdos_963/empty_lift_quotient|one-step
empty-lift theorem]]. If a positive integer $n$-set $P$ is noncoherent, the
simplex on $\{0,e_1,\ldots,e_n\}$ has a height-preserving primitive quotient of
dimension $n-1$ that retains all $n+1$ vertices and is empty. It has a
unimodular star triangulation. The proof extracts, from a convex decomposition
of $\mathbf1$, an affine relation whose negative coefficients are all $-1$ and
whose two sign supports each have at least two elements; strict convexity of the
square function handles the equal-degree case.

An iteration down to dimension $c(P)$ would prove the stronger coherent
bound by parity. **No such iteration is proved.** The one-step argument
controls a simplex, not all simplices in a later projected polytope.
The new six-point example $\{33,36,37,38,41,45\}$ also refutes
minimum-element exchange for coherent maxima, so neither extremal-element
exchange shortcut supplies the missing iteration.

### Proved intrinsic rank-defect at most three cases

For a positive set $P$, let $T$ be the rational span in
$\mathbb Q^P$ of all its zero ternary relations and put
$\rho=\dim_{\mathbb Q}(\mathbb Q^P/T)$. The images of the coordinate
vectors preserve exactly the original ternary relations, remain distinct
and nonzero, and have no antipodal pair. Maximum dissociation gives
$\rho\le d(P)$.

The parity-fiber argument in [[research/erdos_963/parity_fibers|the parity
note]] establishes

$$
\rho\ge d(P)-3\quad\Longrightarrow\quad |P|\le2^{d(P)}-1.
$$

For positive odd integer sets, under the same rank condition it proves
the stronger estimate $|P|\le2^{d(P)-1}$.
These are universal theorems under the stated rank hypothesis, not finite
search observations.

Here is the counting mechanism. Let $L$ be the integer lattice generated
by the universal columns, and partition $P$ by $L/2L\cong\mathbb F_2^\rho$.
A nonzero fiber has dimension at most $d-\rho+1$: extend its residue to
a binary basis using $\rho-1$ occurring residues, whose representatives
can be adjoined to any dissociated subset of that fiber. The zero fiber
has dimension at most $d-\rho$. Every nonzero fiber admits a positive
odd integer realization preserving its ternary relations, by rounding a
large positive real functional in a prescribed parity class.

Write $F(k)$ and $G(k)$ for the largest sizes of positive odd and
positive real sets, respectively, of dimension at most $k$. Thus

$$
|P|\le(2^\rho-1)F(d-\rho+1)+G(d-\rho).
$$

The proved estimates $F(k)\le2^{k-1}$ for $k\le4$ and
$G(k)\le2^k-1$ for $k\le3$ give the stated bound at defect at most
three. In the globally odd case only $2^{\rho-1}$ nonzero fibers can
occur, giving the stronger odd estimate. The parity-realization details
are in the linked note.

The earlier maximum-volume proofs for defect at most two remain valid;
see [[research/erdos_963/corank_one|the defect-one proof]] and
[[research/erdos_963/corank_two|the defect-two proof]].

No corresponding argument for arbitrary intrinsic defect at least four is
established. In particular, the hypothesis cannot be dropped merely because
an integer projection has rational rank one.

### Exact obstruction to induction on the stronger odd bound

If the stronger odd bound first fails in dimension $d$, take a violating
positive odd set $O$. Let $R\subseteq\mathbb Z^O$ be generated by its
zero ternary relations of support at most $d+1$, and let
$H=\mathbb Z^O/R$. Then

$$
\dim_{\mathbb F_2}(H/2H)=1.
$$

Otherwise there is a binary character nonconstant on $O$, in addition
to the character constantly one. The two color classes both have
dimension at most $d-1$: append an element of the opposite class to
a hypothetical dissociated $d$-set and apply the appropriate character
to its short dependence. The smaller-dimensional odd bound would then
bound each class by $2^{d-2}$, a contradiction.

Consequently these short-relation supports span the entire even-weight
binary hyperplane. Their rational span has codimension one as well:
choose $|O|-1$ rows independent modulo two, which have an odd maximal
minor. Even the universal rational lift using only these short relations
has rank one. Some short relation must be unbalanced.

The proof and exact hypotheses are in [[research/erdos_963/parity_fibers|the
parity note]]. No argument excludes this rank-one, binary-connected case. These
are necessary conditions on a least-dimensional failure of the **strong odd
bound**, not an unconditional rank-one restriction on a least-dimensional
counterexample to the original bound.

The [[research/erdos_963/short_relation_height|new cofactor bound]] gives a
finite height restriction in this rank-one short-presentation case. After
primitive integer normalization,

$$
\max O\le d(d+1)^{d-1}(d-1)^{(d-1)/2}.
$$

This bounds the search space at each fixed least-failure dimension,
but does not bound that dimension or exclude a failure. No search of
this space has been carried out. The
[[research/erdos_963/primitive_order_obstructions|new odd ordered-split example]] shows
that primitive nearly maximum subsets and a torsion-free rank-one
short presentation alone do not repair order-based exchange.

### Other proved restrictions

The [[research/erdos_963/pair_multiplicity|repeated-pair argument]] proves the
target whenever the restricted pair-sum multiplicity

$$
\mu(P)=\max_t\#\{\{a,b\}\subseteq P:a\ne b,\ a+b=t\}
$$

is at most two. More generally, for $n=|P|$ and $d=d(P)<n$,

$$
\mu(P)\ge\frac{(n-d)(n-d+1)}{3^{d+1}-1}.
$$

Thus a counterexample $n\ge2^d$ has an exponentially large family of
disjoint reflected pairs. The same note proves the stronger odd bound for
positive odd sets with restricted pair-sum multiplicity one. Consequently
the original target holds whenever every individual valuation layer is
restricted-Sidon. No augmentation from a large reflected-pair family has
been established; the rank-one, binary-connected case remains open here.

There are additional arbitrary-defect cases in
[[research/erdos_963/quotient_special_cases|the quotient note]]. For a maximum-volume basis
of the lifted rank-$r$ configuration, let $G=L/\mathbb Z^r$ be
its finite coordinate-lattice quotient. The target and odd-slice bounds
hold if $G$ has exponent at most two, or if some prime $p$ satisfies
$\dim_{\mathbb F_p}(G/pG)=d-r$. The latter equality enables circuit
extensions and coordinate-width bounds. The case of defect strictly larger
than every such prime rank remains open.

The counting argument in [[research/erdos_963/algebraic_observations|the
algebraic note]] also proves the target when there is no nonzero ternary
relation on fewer than nine elements. Any counterexample with $d\ge9$ must
have a relation on at most six elements. These restrictions do not exclude the
dense short-relation configurations in the remaining gap.

### Unsigned-support matching is refuted in its existence form

The set

$$
P=\{3,15,31,33,35,41,55\}
$$

has every five-subset dissociated and every six-subset dependent. Thus every
maximum $D$ has size five, and each of its two omitted elements has only
full-support ternary representations on $D$. Their unsigned-support
neighborhoods are both $\{D\}$, violating Hall for every choice of maximum
$D$. See [[research/erdos_963/matching_obstruction|the exact certificate]].
This rules out that matching approach completely; it does not refute the
different complement-orbit assertion below.

### A rainbow-forest route (conditional)

For a maximum $D\subseteq P$, put $S=\Sigma(D)$ and color
each edge $\{s,s+a\}\subseteq S$ by $a\in P$. A forest
containing one edge of every color would immediately give
$|P|\le|S|-1=2^{d(P)}-1$. Such a forest exists exactly when

$$
 |S|-\#\operatorname{components}(S,E(C))\ge |C|
 \qquad(C\subseteq P),
$$

where $E(C)$ consists of all edges with colors in $C$, including isolated
vertices when counting components. The graph criterion and its short proof are
in [[research/erdos_963/continuation_routes|the continuation note]].

This is weaker than upper-endpoint matching: distinct upper endpoints
force a forest, but a forest can have repeated upper endpoints. The
recorded endpoint-Hall obstruction does not violate the graph condition
for its deficient three-color family. Colors with full-support
representations alone satisfy the graph condition, since they have
disjoint complement-pair edges.

It is **not proved** that some maximum $D$ satisfies the graph condition for
every $C$. Taking $C=P$ already entails the target cardinality inequality.
The missing substantive step is an augmentation argument from a deficient color
family to a larger dissociated set, or a counterexample to this existence
assertion. No such argument has been established. The stronger every-maximum
assertion is false by the exact example in
[[research/erdos_963/forest_obstruction|the new note]].

The later construction in
[[research/erdos_963/minimum_sum_matching|the minimum-sum matching note]] shows that even
choosing the **unique minimum-sum maximum** $D$ does not guarantee
upper-endpoint Hall. Its ten-element example has $d=7$ and still admits
a rainbow tree for the deficient three-color family. Thus it rules out
that basis-optimization repair, not the weaker forest route or the target.

The new [[research/erdos_963/forest_restrictions|forest restrictions]] prove

$$
r(E(C))\ge|\mathcal U(C)|,
$$

where $\mathcal U(C)$ is the family of distinct unsigned supports
occurring in representations of its colors. They also prove that a
deficient family for a maximum $D$ must have graphic rank at least
seven; for a maximum-sum maximum $D$, at least eight.
This does not settle deficiencies of
larger rank or justify an exchange from one. The arbitrary-maximum
rank-seven threshold is attained by the $K_{4,4}$ example.

### A proved compression when a nearly maximum subset has large index

For any dissociated $(d-1)$-subset $D\subseteq P$, set
$L=\langle P\rangle_{\mathbb Z}$ and $L_D=\langle D\rangle_{\mathbb Z}$.
The quotient $L/L_D$, if nontrivial, is cyclic, and all nonzero images
of $P$ belong to one signed class. If its order is infinite or greater
than $d+1$, there is a positive set $C$ with

$$
 d(C)\le d-1,\qquad |C|\ge (|P|-1)/2.
$$

This is a proved compression theorem; $C$ need not be a subset of $P$. Its
proof is in [[research/erdos_963/large_quotient_compression|the
quotient-compression note]].

Consequently a counterexample of minimum dissociation dimension must have
every $(d-1)$-element dissociated subset generate either the whole
integer lattice $L$, or a subgroup of cyclic index at most $d+1$.
In particular every such subset spans the full intrinsic rational space.
The primitive and small-index cases remain unresolved; the compression
does not establish a general induction.

For a least-dimensional failure of the **strong odd bound**, normalized
to a primitive positive odd integer set, the same note now improves the
restriction to

$$
\gcd(D)\le d-1
$$

for every dissociated $(d-1)$-subset $D$. This gcd is odd, so it is at
most $d-2$ when $d$ is odd. If $d$ is even and the gcd equals $d-1$,
the divisible part of the set has size $d-1$ or $d$ and lies in an
explicit complement-sum configuration. These refinements still allow
the primitive case.

### A half-size dimension-drop induction (conditional)

The new [[research/erdos_963/half_size_reduction|half-size note]] asks whether
every positive $n$-set $P$ of dimension $d$ has a subset $C$ with

$$
|C|\ge\lfloor n/2\rfloor,\qquad d(C)\le d-1.
$$

If true, induction would give $n\le2^d-1$. This assertion is not
proved in general.

It is proved when $n\le2d+1$. The main new ingredient is a
subset-sum fiber-code count: if every $d$-subset is dissociated and
$n<2d+2$, then

$$
\binom n{d+1}\le
\left(\left\lfloor\frac{2(d+1)}{2(d+1)-n}\right\rfloor-1\right)2^d.
$$

At $n=2d$ this is impossible for $d\ge5$. A parity determinant
argument handles even $d$, and the established small positive cases
complete the claim. These local estimates do not reach the dense
range relevant to a counterexample to the original bound.

Ordered splitting is false: the separated triples $\{1,2,4\}$ and
$\{5,6,7\}$ are dissociated, but their union has dimension three.
A general half-size drop would have to allow noncontiguous subsets.

For odd configurations, the half-size assertion now also follows whenever
the intrinsic rank is at least two: two independent binary characters
partition the set into two nonempty classes, each of dimension at most
$d-1$. Thus an odd half-size failure has intrinsic rank one. More generally,
if an even-sized failure has $n=2m$, intrinsic rank $\rho$, and $z$
columns reducing to zero modulo twice the intrinsic lattice, the
character evaluation code gives

$$
m\ge2^\rho-1+2^{\rho-1}z.
$$

Neither restriction handles the remaining primitive odd case.

### Complement-orbit matching (conditional route)

For a nonempty positive odd set $O$, let $D\subseteq O$ be maximum
dissociated, $S=\Sigma(D)$, and $T=\sum D$. Associate to each $x\in O$ the
complement orbits $\{s,T-s\}$ for which $s,s-x\in S$. There are exactly
$2^{|D|-1}$ orbits: uniqueness of subset sums identifies the involution with
taking complementary subsets, which has no fixed points. A system of distinct
representatives would prove (2). A sufficient precise statement is: for every
such $O$, there exists a maximum $D$ such that for every $C\subseteq O$,
the union of the orbit-neighborhoods of its elements has size at least $|C|$.
This existence version is **unproved**. The stronger assertion for every maximum
$D$ is **false**: the new
[[research/erdos_963/orbit_matching_obstruction|exact obstruction]] gives an
18-element positive odd set with $d=13$, and a maximum $D$ for which five colors
occupy only four complement orbits. Its chosen $D$ is not maximum-sum; the
maximum-sum version remains unproved. The structural observation below holds for
every maximum $D$.

For odd $|D|$, each neighborhood has size one or at least four. Indeed,
an odd represented value has odd signed support. At most one full-support
representation exists, since subtracting two and dividing by two gives a
nonzero ternary relation on $D$. A representation with zero coordinates
has at least two of them and gives a face of dimension at least two among
the upper-endpoint subset vertices. These vertices lie in distinct complement
orbits because a nonzero fixed coordinate prevents two vertices from being
complementary. A singleton neighborhood therefore has a unique full-support
representation and its value is $|2s-T|$; singleton neighborhoods for
distinct positive values cannot coincide.

The missing step is a global augmentation argument for larger neighborhoods.
Replacing elements of $D$ by represented ambient elements can create
relations with coefficients 2 or 3 on $D$, which dissociation does not
exclude. It has not been proved that simultaneous blocking of all candidate
exchanges forces additional orbit-neighbors. This is a specific unresolved
lemma, not a proof of the target.

The new [[research/erdos_963/maximum_sum_orbits|maximum-sum charging argument]]
proves Hall for odd $d\ge5$ when all representations of the colors under
consideration together omit at most three coordinates. Exclusively full-support
colors lie in a central antichain. Partitioning the folded cube into
three-coordinate cubes leaves at most a unit local excess, and maximum-sum
exchange charges each excess to a distinct color represented in two cubes. Four
or more omission coordinates remain unresolved. Since the basis colors alone
collectively omit all coordinates, this does not establish Hall for the whole
ambient set.

The [[research/erdos_963/maximum_sum_candidate|fixed new candidate]] has 28
positive odd entries, a proved dissociated eleven-subset $D$, and seventeen
colors whose entire orbit neighborhood on $D$ has size sixteen. **It is not
proved that $D$ is maximum.** The exact pending task is to find a dissociated
twelve-subset or a relation-cover certificate excluding all of them. Only
exclusion would refute the maximum-sum version, because $D$ consists of the
eleven largest entries. This candidate is not a counterexample to the original
cardinality bound. The same note gives a checked robust higher-multiple
obstruction to the proposed six axial forms from the central $C_3$
configuration.

### Cyclic 2-group route (conditional)

The [[research/erdos_963/finite_group_observations|finite-group note]] proves
the ordinary modular odd-set bound in dimensions at most three and for complete
symmetric congruence classes. It also records a dense torsion model and why its
complete affine-plane relations do not lift to distinct real numbers. None of
these results proves the general cyclic assertions below.

Call a set weakly dissociated here if every nonzero ternary relation has all
nonzero coefficients of the same sign. A weakly dissociated subset modulo
$2^k$ lifts to a genuinely dissociated subset of positive integers: a
real zero relation would also vanish modulo $2^k$, but coefficients of
one sign cannot sum to zero on positive numbers. Thus the assertion that
every $m$-element subset of a cyclic 2-group contains a weakly dissociated
set of size $\lfloor\log_2m\rfloor+1$ would prove the target after
injective reduction modulo a sufficiently large power of two.

That assertion is unproved. Induction closes when a set of size $2^j$
has at least $2^{j-1}$ even residues and a nonempty odd part: extract
$j$ weakly dissociated even residues and append one odd residue. The
majority-odd case remains. Ordinary downward compression is invalid: in
$\mathbb Z/8\mathbb Z$, $\{3,4,7\}$ has weak dimension two,
whereas replacing 4 by 0 gives the weakly dissociated triple $\{0,3,7\}$.

Another sufficient, still unproved, cyclic assertion is

$$
 |O|\le2^{d(O)}
 \quad\text{for odd residue sets }O\subseteq\mathbb Z/2^M\mathbb Z,
$$

where dissociation here is ordinary modular dissociation. Splitting an
arbitrary residue set into its even and odd parts would then prove
$|A|\le2^{d(A)+1}-1$ by induction on $M$: when the odd part is
nonempty, adjoining one of its elements to any dissociated even subset
shows $d(A_{\rm even})\le d(A)-1$. The even part would have at most
$2^{d(A)}-1$ elements, and the asserted odd bound gives at most
$2^{d(A)}$ others. Injective reduction of an integer configuration
modulo a large power of two would give the original target.

A prospective quotient-exchange lemma is false: an order-two quotient
can lower dissociation dimension by two. The set

$$
D=\{20,40,57,5,48,61\}\subseteq\mathbb Z/128\mathbb Z
$$

is dissociated, but every five-subset of its image modulo 64 is
dependent, as witnessed by

$$
40+5-48-61=-64,\quad20+57+48-61=64,\quad
20+40-57+61=64,\quad20+40+57-5-48=64.
$$

The coordinates omitted by these relations cover all six elements.
For a direct check of dissociation modulo 128, the even subset is
$4\{5,10,12\}$, with scaled subset sums
$E=\{0,5,10,12,15,17,22,27\}$ modulo 32. The odd elements
$5,57,61$ are all 1 modulo 4, so their subset cardinalities are
distinguished modulo 4. For cardinality one, the disjointness of
$E,E+13,E+14$ proves injectivity; complementation gives the same
check for cardinality two. Cardinalities zero and three need only the
injectivity within $E$. Thus all 64 subset sums are distinct.
This invalidates that exchange lemma, not the cyclic assertions themselves.

There is also a quantitative obstruction to a full-preimage induction.
For the order-two projection, let $Q$ be the occupied residue classes
of an odd set $O$, and $R\subseteq Q$ the classes whose two lifts
both occur. Then $|O|=|Q|+|R|$ and $d(Q)\le d(O)$.
Even a general augmentation assertion
$d(\pi^{-1}R)\ge d(R)+1$ would give
only $d(R)\le d(O)-1$. Separate applications of the desired
lower-level odd bound would yield
$|O|\le3\cdot2^{d(O)-1}$, not $2^{d(O)}$.
A successful version of this induction needs a joint bound for the
occupied and double fibers, rather than that augmentation assertion alone.
Moreover, the augmentation assertion is false without qualifications:
$\{1\}\subseteq\mathbb Z/2\mathbb Z$ and its inverse image
$\{1,3\}\subseteq\mathbb Z/4\mathbb Z$ both have dimension one.
The continuation note proves an exact affine binary consistency criterion
for selecting one doubled lift of a dissociated odd residue set. Consistency
for a prescribed doubled element is refuted by the exact example in
[[research/erdos_963/cyclic_extension_obstructions|the cyclic lifting note]]. That note also
shows an order-two quotient drop of two for an all-odd dissociated set.
Augmentation with some suitable choice of doubled element, and the required
joint fiber bound, remain unproved.

The same note gives rigorous obstructions to ordered-interval difference
augmentation and to one proposed binary blowup. None is a counterexample
to the target. These obstructions do not improve the proved universal
or special-case lower bounds.

## Why a longer binary chain alone cannot close the gap

The logarithmic loss from an isolated binary chain is real. For any $t\ge1$,
put $k=2^{t+1}-2+2t$ and choose $R$ with $2^R>k$.
Form disjoint blocks of $2^j+1$ positive summands, for $j=1,\ldots,t$.
One summand overall is 1, and every other summand is $1+2^r$, with
all exponents distinct and at least $R$. Let $O$ consist of these
summands and all $t$ block sums. Then $|O|=k$, every element is odd,
and all differences from the pivot 1 have distinct 2-adic valuations:
the block sum for block $j$ has valuation $j$ after subtracting 1,
while the other differences have their distinct exponents $r\ge R$.

The $t$ disjoint block relations show $d(O)\le k-t$. All
$k-t$ summands are dissociated: a ternary relation reduced modulo
$2^R$ forces its coefficient sum to vanish, after which distinct
valuations of the powers of two force all coefficients zero. Thus
$d(O)=k-t$, with a loss $t$ of logarithmic order. A proof using the
tree must exploit its branching/cardinality, not merely a long path.

## A proved full-rational-rank case

If $\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}A=d(A)=d$, then
the target bound holds. The case $d=0$ is immediate. Otherwise choose
a rational basis $B\subseteq A$ of
maximum determinant magnitude, measured relative to any fixed basis.
Every $a\in A\setminus B$ has ternary coordinates in $B$, because
$B\cup\{a\}$ cannot be dissociated; elements of $B$ have unit
coordinates. Hence determinants of coordinate
bases are integers, and maximum volume makes every nonzero one $\pm1$.

Two nonzero rationally proportional elements of $A$ are equal or
opposite: extend one to a rational basis from $A$ and apply the same
ternary-coordinate property. Representatives of distinct antipodal classes
are therefore rationally independent in pairs. If two such representatives
had the same coordinates modulo 2, extending them to a basis would produce
an even nonzero determinant, a contradiction. No nonzero ternary coordinate
vector is zero modulo 2. There are consequently at most $2^d-1$
nonzero antipodal classes, so $|A|\le2^{d+1}-1$.

This is a special case only: preserving ternary relations under a generic
integer projection can lower rational rank, so it does not give a reduction
of the general problem to this case.

## A bounded finite candidate excluded

Let $V$ be the 40 representatives of nonzero antipodal pairs in
$\{-1,0,1\}^4$, choosing the representative whose first nonzero coordinate
is positive. A potential counterexample would be a 32-subset of $V$
with dissociation dimension five, embedded into the reals by a rationally
independent linear map and symmetrized.

This particular possibility is excluded by an exact finite certificate in
[`evidence/assets/cube4.json`](evidence/assets/cube4.json), checked by
[`evidence/main.py`](evidence/main.py).
The certificate partitions $V$ into blocks of sizes 13, 13, and 14 and
lists respectively 13, 11, and 11 dissociated six-subsets. In each block,
every pair of vertices is disjoint from at least one listed six-subset.
Consequently a set meeting every listed six-subset must delete at least
three vertices from each block, or nine in total. Every 32-subset of
$V$ deletes only eight vertices and therefore contains a dissociated
six-subset. The checker verifies all 64 subset sums of each listed set,
the partition, and the pair-avoidance condition. This is a finite exclusion,
not a universal extremal conclusion.

This particular exclusion is also a consequence of the proved
rank-defect theorem: a rank-four configuration of dissociation dimension
five has at most 31 nonzero antipodal classes. The finite certificate is
retained as a historical independent check; it need not be rerun to advance
the current gap.
