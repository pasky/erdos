---
desc: Independent deductions and adversarial checks supporting the conditional grades of the frozen arbitrary-cardinality coloring report and its full E111 implication.
---

# Independent checks of the whole-conclusion report

***

Examination date: **2026-10-17 UTC**. The mathematical subject was frozen
on **2026-10-17 at 06:43:02 UTC**. Project mathematics is credited to
**Plasma AI**. [The subject manifest](subject/manifest.json) identifies
the supplied mathematical snapshots. [The submitted report](submitted_review.md),
[its derivations](derivations.md), and [its dependency map](dependency_map.md)
are preserved unchanged. This document records the grader's own reasoning;
the grade states the separate independence and adoption conditions.

The targets are, in order: countable colorability of every set-sized
simple graph with one finite hereditary linear edge-bipartization budget;
and the full limit in E111 for every graph of chromatic number
$\aleph_1$, with no restriction on its vertex cardinality. The argument
is in ZFC. There is no computational or kernel leg.

## 1. The exact finite budget

For a finite graph $F$, let $m_F(c)$ count monochromatic edges in a
binary coloring $c$. Deleting those edges leaves a bipartite graph, so
$\beta(F)\le\min_c m_F(c)$. Conversely, a binary coloring of a
bipartized graph $F-D$ can leave only edges of $D$ monochromatic in $F$.
Thus

$$
\beta(F)=\min_c m_F(c).
$$

Restricting a bipartizing deletion set to a subgraph proves
monotonicity. In particular, the copied-pattern arguments may discard
all edges not explicitly listed. Ambient edges between copies impose
no obstacle to this operation. When a lower bound is needed for
packing, retaining ambient edges can only increase the deletion cost.

This equivalence is essential to the proof, whereas a choice of a good
cut separately for each finite vertex set would not provide a
compatible infinite law. The report does not make that latter
inference.

The countable base of cardinal induction does not need the budget:
every countable graph can give different colors to its vertices.
For the endpoint $C=0$, an additional direct check is available. A
finite odd cycle would violate the hypothesis. In each connected
component, parity of distance from a chosen vertex is therefore a
well-defined bipartition: a same-parity edge would produce an odd closed
walk and hence an odd cycle. This checks the zero-budget case without
taking any division by $C$. Empty and finite graphs are covered too.

## 2. Elementary models and singular cardinalities

Fix an uncountable vertex cardinal $\kappa$, and let
$\mu=\operatorname{cf}\kappa$. Choose regular $\theta>\kappa$ so large
that $G\in H(\theta)$. The extra membership condition matters for
arbitrary vertex labels; a cardinal inequality alone would not bound
their hereditary size.

Closing a parameter set $A$ under witness functions for the countably
many existential formulas in the membership language takes at most
$\max(|A|,\aleph_0)$ elements. Closure under those finite-arity functions
through countably many stages gives the existential-witness criterion
for elementarity. This supplies the hull size used in the source.

Choose a cover of the vertices by $\mu$ increasing sets of size less
than $\kappa$. At a successor, form a hull including the next covering
set, all elements of the old model, and the old model itself as a
parameter. At a proper limit $\lambda<\mu$, take the union. A finite
tuple of parameters in that union lies in one earlier model, so any
existential witness needed for elementarity already lies in that
earlier model. Also,

$$
\left|\bigcup_{\xi<\lambda}N_\xi\right|
 \le |\lambda|\cdot\sup_{\xi<\lambda}|N_\xi|<\kappa.
$$

The last strict inequality uses $\lambda<\operatorname{cf}\kappa$;
the supremum of those fewer than $\operatorname{cf}\kappa$ cardinals
is below $\kappa$. It is valid for singular as well as regular
$\kappa$. If $\operatorname{cf}\kappa=\omega$, there is no nonzero
proper limit index in this chain; its final union may have size
$\kappa$, as it must. That final union is not an induction layer.

Each model is itself in $H(\theta)$. It has fewer than $\theta$
members, each of hereditary size less than the regular cardinal
$\theta$; the union of their transitive closures still has size less
than $\theta$. It can therefore be included as a parameter at its
successor. The chain satisfies both $N_\xi\subseteq N_{\xi+1}$ and
$N_\xi\in N_{\xi+1}$.

Every vertex outside the initial model first enters at a successor,
because models at limit indices are unions. Its trace in the preceding
model contains every neighbor in an earlier layer. Each individual
layer has size less than $\kappa$. The argument thus invokes countable
colorability only for strictly smaller graphs. It does not assume that
an arbitrary uncountably chromatic graph has an $\aleph_1$-sized
uncountably chromatic subgraph.

For replication in a model $N$, a finite diagram over a finite root
tuple is a parameter in $N$. Its outside positions are not named.
Finite tuples of elements of $N$ and finite sets of such elements
belong to $N$; conversely, every entry of a finite tuple belonging to
$N$ belongs to $N$. With a finite forbidden set $D\subseteq N$ and
a forbidden set $Q\in N$, the original outside positions witness the
existential assertion of a copy avoiding $D\cup Q$ whenever they miss
$Q$. Elementarity gives a new tuple in $N$. Repeating with an enlarged
finite $D$ gives disjoint copies.

The successor uses this with $N=N_{\xi+1}$ and $Q=N_\xi$.
The element relation, not just inclusion, makes this a permitted
parameter. Original new positions outside $N_{\xi+1}$ miss $Q$,
so the resulting copies lie in $N_{\xi+1}\setminus N_\xi$.
Measures and infinite trace subsets need not belong to either model;
only their finite vertex subsets enter these diagrams.

## 3. Arbitrary products and fixed marginals

Write $\Omega_I=\{-1,1\}^I$ with the compact Hausdorff product topology.
Continuous finite-coordinate functions are uniformly dense in
$C(\Omega_I)$. To check this directly, cover the product by basic
finite-coordinate neighborhoods on which the oscillation of a given
continuous function is small. Compactness gives a finite subcover.
A function constant on each cell of the common finite-coordinate
refinement uniformly approximates the original function.

Consistent finite probability laws define a positive linear functional
of norm one on these functions. A common finite-coordinate refinement
checks that the value is well-defined, linear and bounded by the
uniform norm. Continuous extension and the compact-Hausdorff Riesz
representation theorem give a unique Radon probability measure.
The uniqueness asserted is among Radon laws; it does not assert that
finite cylinders generate every Borel set of an uncountable product.

The Radon probabilities correspond to positive functionals with value
one on the constant function. They form a closed subset of the dual
unit ball, hence a weak-star compact convex set by Banach--Alaoglu.
Prescribing the marginal on an arbitrary full coordinate subset is a
closed condition: test every continuous function on that subset after
pullback by projection. Continuous pushforward of a Radon law on a
compact space is Radon. Extension by constant new coordinates proves
nonemptiness of the fixed-marginal space.

Suppose $d_j$ are Borel signs under an old law $\nu$, each depending on
countably many old coordinates. Their finite joint distributions with
old coordinates are consistent, so they determine a joint Radon law
$\Lambda$. Its old marginal is exactly $\nu$, by the preceding
Radon uniqueness. For one $j$, project onto $j$ and its countable
determining coordinates. Finite cylinders generate the Borel sets of
this countable product, so finite-measure uniqueness identifies this
projection with the actual joint distribution under $\nu$.
Consequently the new coordinate equals $d_j$ almost surely.
This is an individual assertion for each $j$; it does not take an
uncountable intersection of events.

A finite minimizing choice of free root signs is a continuous
finite-coordinate function on $\Omega_{I\cup J}$. It therefore supplies
a Radon extension with the same entire marginal $\Lambda$. No
regular conditional distribution on an arbitrary uncountable space
is required at this interface.

These are the exact uses of classical product compactness, Riesz
representation, Banach--Alaoglu and countable-product uniqueness.
Their original source proofs were not supplied or inspected. The
functional, density, projection and closedness deductions just given
check their hypotheses and specializations.

## 4. Why the base law satisfies all rooted inequalities

For a finite pattern $P$ with roots $R$ and new positions $S$, its
cost $e_P$ minimizes the number of monochromatic prescribed edges
touching $S$, after fixing signs on $R$. It includes no root-root
edges. For finitely many patterns $P_i$ and integer weights $a_i\ge0$,
replicate $k a_i$ copies with their new positions mutually disjoint and
avoiding the finite union of all roots. Conditional on the root signs,
the copies minimize independently. C-linearity of their selected-edge
union gives

$$
k\min_\tau\sum_i a_i e_{P_i}(\tau)
 \le C|R|+Ck\sum_i a_i|S_i|.
$$

Dividing by $k$ and letting $k\to\infty$ removes the root overhead.
Homogeneity handles rational weights. The minimum of finitely many
linear functions is continuous in the weights, so the inequality
extends to all nonnegative real weights.

Let $Q$ be the convex hull of the finite vectors
$(e_{P_i}(\tau))_i$. If it misses the lower orthant with corner
$(C|S_i|)_i$, strict finite-dimensional separation gives a nonnegative
weight vector whose minimum on $Q$ exceeds its value at the corner.
The weights must be nonnegative because the orthant is unbounded in
each negative coordinate direction. This contradicts the weighted
inequality. Thus a root distribution meets all selected bounds.

Each cost is a continuous finite-coordinate function. Extending the
root law by constant coordinates and using the finite intersection
property in the compact set of Radon laws gives one law satisfying
every pattern inequality. Replication over the initial elementary
model makes every pattern in $J(\nu_0,0)$ eligible. This proves the
base input from the actual graph hypothesis without a coloring
assumption.

## 5. Uncountable traces do not need a simultaneous event

Let $T$ be an infinite trace of a vertex outside a model carrying a
law with property $J$. For finite $B\subseteq T$, a rooted star gives

$$
\mathbb E Z(B)\le C,\qquad
Z(B)=\min\bigl(\#\{u\in B:\sigma_u=1\},
              \#\{u\in B:\sigma_u=-1\}\bigr).
$$

For a countable $B$, increase finite subsets to $B$.
The functions increase to the smaller of the two possibly infinite
sign counts. Monotone convergence gives the same expectation bound.

Let $a$ be the supremum of these expectations over countable subsets
of $T$. Choose countable sets approaching $a$ and take their union
with any countably infinite subset of $T$. The result $A$ is countably
infinite and has expectation exactly $a$, by monotonicity and the
definition of the supremum. Since $a\le C<\infty$, its smaller sign
count is finite almost surely. Its other sign is the unique eventual
sign $s$, a Borel function of the countably many coordinates of $A$.

For each fixed $u\in T\setminus A$, outside a null set,

$$
Z(A\cup\{u\})=Z(A)+\mathbf1_{\sigma_u\ne s}.
$$

Adding $u$ cannot exceed the maximal expectation $a$. Both
expectations are finite and equal, hence
$\nu(\sigma_u\ne s)=0$. On $A$, countable monotone convergence gives

$$
\sum_{u\in A}\nu(\sigma_u\ne s)=\mathbb E Z(A)\le C.
$$

All remaining summands vanish individually. The sum over $T$, defined
as the supremum of finite subsums, is at most $C$.

The attempted objection is that the outside-$A$ exceptional events
might collectively cover the probability space. That possibility
does not invalidate the claimed sum. Neither the source nor the
report replaces it with a statement that the entire uncountable trace
has finite minority on one outcome.

## 6. The strongest fixed-law attack

Fix one old law $\nu$ satisfying $J$, not a law that may be changed to
fit future patterns. Let $X$ be the next layer's infinite-trace
vertices, $Y$ its finite-trace vertices, and $d_y=-s_y$ for $y\in X$.
Form the joint law $\Lambda$ of the old coordinates and these
prescribed signs. Let $\mathcal K$ contain all Radon laws on the next
coordinate set with this whole marginal. Section 3 proves it is
nonempty, compact and convex.

For finitely many future patterns $P_i$, divide their root union into
old roots, roots $R_X\subseteq X$, and free roots $R_Y\subseteq Y$.
For nonnegative weights $\rho_i$, every law in $\mathcal K$ has
weighted expected cost at least the expected pointwise minimum over
$R_Y$. Choosing the first minimizing free assignment separately for
each finite old-and-$X$ root assignment attains equality. Thus

$$
\min_{\pi\in\mathcal K}\sum_i\rho_i\mathbb E_\pi e_{P_i}
 =
\mathbb E_\Lambda\min_\eta\sum_i\rho_i e_{P_i}(\tau,d,\eta).
\tag{1}
$$

This equality is over finitely many signs. It does not interchange
expectation with an arbitrary optimization on the whole old space.
The continuous cost image of $\mathcal K$ is compact and convex.
If some finite family of upper bounds is infeasible, separation as
in Section 4 supplies nonnegative weights with a strict excess.
Since each cost is between zero and $|E(P_i)|$, the expression is
Lipschitz in the finitely many weights. Rational approximation and
scaling give integer weights $a_i$ with

$$
\alpha=
\mathbb E_\Lambda\min_\eta\sum_i a_i e_{P_i}(\tau,d,\eta)
 -C\sum_i a_i|S_i|>0.
\tag{2}
$$

This is the strongest putative obstruction: the fixed old law itself
could force incompatible expected future costs.

To test it, put $q=|R_X|+|R_Y|$ and choose an integer $k$ with
$k\alpha>Cq$. Section 2 replicates $k a_i$ copies of each pattern
inside the next model but outside the old one, disjoint from every
root and other copy. Keep these copies fixed. For each $y\in R_X$,
add a star from $y$ to the first $L$ members of its countable trace
set $A_y$.

The resulting object is an actual pattern over the old model. Its
new vertices are $R_X$, $R_Y$ and the copies, a total of

$$
q+k\sum_i a_i|S_i|,
$$

independently of $L$. Overlapping star neighborhoods cause no edge
duplication: the centers are distinct, and every copied edge touches
a fresh copied position. No edge between two roots in $R_X\cup R_Y$
is listed. Unlisted ambient edges may be discarded by Section 1.

For a fixed old assignment $\tau$, let $b_y^L$ be the number of signs
on the first $L$ trace positions that differ from $s_y$. After signs
$\delta$ on $R_X$ and $\eta$ on $R_Y$ are fixed, all copies minimize
independently. The exact total minimum is

$$
e_L(\tau)=
\min_{\delta,\eta}\left[
 \sum_{y\in R_X}
 \left(b_y^L\mathbf1_{\delta_y=d_y}
 +(L-b_y^L)\mathbf1_{\delta_y\ne d_y}\right)
 +k\sum_i a_i e_{P_i}(\tau,\delta,\eta)
\right].
\tag{3}
$$

The copied-edge contribution ranges from zero to
$W=k\sum_i a_i|E(P_i)|$. For the finitely many stars, almost surely
every $b_y^L$ remains bounded as $L$ grows. At fixed $k$, eventually
$L-2b_y^L>W$ for all of them. Correcting any wrong $\delta_y$ then
strictly lowers the total cost, regardless of all other choices.
Every minimizer has $\delta=d$, and eventually

$$
e_L(\tau)=\sum_{y\in R_X}b_y^L
       +k\min_\eta\sum_i a_i e_{P_i}(\tau,d,\eta).
\tag{4}
$$

The threshold may depend on $\tau$ and $k$. The proof does not need a
uniform threshold. When $R_X$ is empty the same conclusion holds
without any star limit. The pointwise costs $e_L$ are nonnegative and
nondecreasing, because only edges are added to a fixed finite set of
new optimization variables.

Property $J$ of this same old law gives

$$
\mathbb E_\nu e_L\le Cq+Ck\sum_i a_i|S_i|
\quad\text{for every finite }L.
\tag{5}
$$

Monotone convergence, or the source's weaker Fatou estimate, and
(4) imply

$$
\lim_L\mathbb E_\nu e_L
 \ge k\,\mathbb E_\Lambda\min_\eta\sum_i a_i e_{P_i}(\tau,d,\eta).
$$

The expectations agree because the finite joint signs in question
have their prescribed law $\Lambda$. By (2) and $k\alpha>Cq$, the
right side strictly exceeds the bound in (5). Some finite $L$
would already violate (5), an actual finite-pattern violation of old
$J$. This contradicts the assumed old law. The attempted obstruction
therefore fails.

Equivalently, division by $k$ first gives an excess bounded by $Cq/k$;
letting $k\to\infty$ removes it. The correct order is the star limit
at each fixed copy count, then the copy limit, then finite separation
and compactness. All future pattern constraints are closed because
their costs depend on finite root coordinates. Their finite
intersection property inside $\mathcal K$ gives one successor law.
The proof never declares the graph of a Borel sign function closed:
it fixes the whole joint marginal $\Lambda$ before using compactness.

This derivation checks the decisive inference in the frozen proof;
it adds no new hypothesis or repair.

## 7. Limit stages and an actual countable coloring

At a model limit, consistent finite-coordinate laws give a Radon law.
Its entire marginal on each earlier coordinate set is the specified
earlier Radon law. A future pattern's finite root set is contained
in one earlier model; its new vertices are outside the limit model
and therefore outside that earlier model too. The same pattern was
already covered by old $J$. Its expectation depends on those finite
roots, so the inequality persists. The final union is treated by the
same construction, at any cofinality.

For a vertex $v$ with infinite trace, its assigned identity
$\sigma_v=-s_v$ involves $v$ and countably many earlier coordinates.
The entire marginal at its entry stage is preserved; no claim that
those coordinates fit in a stage preceding that stage is needed.
For each trace neighbor $u$,

$$
\nu(\sigma_u=\sigma_v)=\nu(\sigma_u\ne s_v).
$$

Section 5 therefore gives a total equality probability at most $C$.
The coordinate signs are unit vectors of real $L^2(\nu)$ and satisfy

$$
1+\langle\sigma_u,\sigma_v\rangle
 =2\nu(\sigma_u=\sigma_v).
$$

The deterministic infinite-trace energy is at most $2C$. No sampled
outcome has been chosen as the final coloring.

To check the Hilbert partition, fix an orthonormal basis and well-order
its indices. Bessel's inequality makes every positive-threshold
support of a unit vector finite. A rational gap $0<b<a$ with a
nonempty support
$S_a(x)=\{i:|\langle x,e_i\rangle|\ge a\}$ and all other magnitudes
at most $b$ exists: take a gap among the finitely many magnitudes
above half of one nonzero coordinate magnitude. Assign the first
suitable rational pair and the sign of the coordinate at the least
member of $S_a(x)$. The index and the support set are not part of the
label.

Equally labeled vectors with different supports have a coordinate
where the magnitudes are at least $a$ and at most $b$, so
$\|x+y\|\ge a-b$. With equal supports their least support coordinates
have the same sign and give $\|x+y\|\ge2a$. In both cases

$$
1+\langle x,y\rangle=\tfrac12\|x+y\|^2
 \ge\tfrac12(a-b)^2=:\eta>0.
$$

The labels form a countable set, even in a nonseparable Hilbert space.

Fix a label and order vertices by layers, with any well-order inside
a layer. Retain only edges between layers. A finite-trace vertex has
finitely many earlier neighbors directly. For an infinite-trace
vertex, every same-label earlier neighbor contributes at least
$\eta$ to its finite energy, so there are finitely many of them.
Initial-layer vertices have none. Greedy coloring of this graph by
natural numbers is therefore justified.

Each layer, including the initial one, is a smaller C-linear graph,
so cardinal induction supplies a proper countable coloring inside it.
Use the triple: Hilbert label, inter-layer greedy color for that
label, and its layer color. Different labels, different layers within
a label, and edges in one layer are separated respectively by the
first, second and third coordinates. This is an actual proper
coloring with a countable palette.

The argument does not need a uniform energy bound at finite-trace
vertices, a uniform finite color bound for layers, a separable Hilbert
space, or an intersection of uncountably many conull events. The
strict layer size from Section 2 rules out a minimal-cardinality
counterexample. This verifies target 1 on its whole stated domain.

## 8. The full E111 consequence

For each positive $n$ in an infinite graph, the set of possible
$\beta(F)$ for $n$-vertex subgraphs is a nonempty subset of the finite
set of integers from zero to $\binom n2$. Its maximum exists.
Restricting to induced subgraphs gives the same maximum by
monotonicity. Any deletion bound allowed by the supplied problem
wording dominates this least profile.

If $\chi(G)=\aleph_1$ and $S$ is countable, then
$\chi(G-S)=\aleph_1$. Otherwise a countable coloring of $G-S$ and
a disjoint countable palette for $S$ would countably color $G$.
The reverse upper bound follows by restriction.

Fix a finite $K>0$. Assuming the established target 1, every
countable-deletion remainder has a finite subgraph with
$\beta(F)>2K|V(F)|$. Choose such witnesses recursively through
$\omega_1$. Each proper stage has removed only a countable union of
finite sets, so the construction continues and gives pairwise
vertex-disjoint witnesses. This reasoning does not restrict $|V(G)|$
to $\aleph_1$.

There are countably many finite simple graph isomorphism types.
If each occurred only finitely often, the entire witness family
would be countable. Thus one type occurs infinitely often. Let its
order be $v$ and deletion cost $b>2Kv$. For each integer $n\ge2v$,
take $q=\lfloor n/v\rfloor$ disjoint copies and pad to exactly $n$
vertices. Any bipartizing deletion set must delete at least $b$
edges from each copy. The copy edge sets are disjoint; cross edges
cannot reduce this obligation. Hence

$$
h_G(n)\ge b\lfloor n/v\rfloor
 \ge \frac bv(n-v)>2K(n-v)\ge Kn.
$$

This proves every sufficiently large order for each fixed $K$, with
a threshold allowed to depend on $G$ and $K$. It does not require a
uniform bound on the initially varying witness sizes.

For the claimed converse reduction, failure of the limit supplies
a positive finite $K$ with $h_G(n)\le Kn$ infinitely often; a
nonpositive threshold can be enlarged. A maximal disjoint family of
finite subgraphs with $\beta(F)>2K|V(F)|$ exists by the usual chain
union argument. If uncountable, repeated type and padding would
contradict these infinitely many orders. The family and its vertex
union $S$ are countable. Maximality says $G-S$ is $2K$-linear,
and it still has chromatic number $\aleph_1$. Conversely, a C-linear
graph with that chromatic number has $h_G(n)\le Cn$ and violates
the limit.

This is the equivalence of E111 with the restricted CC lemma whose
hypothesis has $\chi(G)\le\aleph_1$. It is not a claimed converse
equivalence with target 1 at unrestricted chromatic number.
The calculation establishes implications and does not supply an
example satisfying an inconsistent or unproved antecedent. The
unconditional target-2 warrant depends on the target-1 warrant;
it cannot retain that force if target 1 fails.

## 9. The retained hostile witnesses really test distinct errors

The report retains three diagnostic witnesses in Section 11 of its
derivations. Each is exact, although none refutes the actual theorem.

For the infinite star with unique center $z$ and $C=0$, a prescribed
edge with the center among new positions cannot have two copies with
disjoint new positions. Thus in an abundant rooted pattern every
prescribed edge touching a new position must join a new leaf to the
fixed root $z$. Put those leaves opposite $z$; all extension minima
are zero. The all-positive coordinate law satisfies every such
expected-minimum inequality but makes every actual edge
monochromatic. This refutes the tempting substitution of actual
coordinate cost for minimum extension cost. The layered proof does
not make that substitution. An elementary model containing the
infinite star contains its definable unique center, so outside leaves
have finite traces; the final coloring handles them without a
coordinate-energy bound.

For the null-event witness on $[0,1]$, set
$\sigma_t(\omega)=-1$ exactly when $\omega=t$. Each fixed coordinate
equals $+1$ almost surely, and any countable family does so
simultaneously almost surely, yet every outcome has a negative
coordinate. The claim concerns a family of individual measurable
variables; it does not assume their map into the full uncountable
Borel product is measurable. It correctly distinguishes the
countable-coordinate laws used by the proof from an unsupported
uncountable simultaneous event.

For the Borel-limit witness on $\{-1,1\}^{\mathbb N}$, let
$\tau^{(n)}$ have its first $n$ entries negative and the rest positive,
and let $d(\tau)=+1$ when infinitely many entries are positive,
$-1$ otherwise. Point masses at $(\tau^{(n)},+1)$ satisfy the sign
identity and converge weak-star to the point mass at
$(\text{all negative},+1)$, which violates it. The function is Borel.
This refutes closedness of arbitrary derived-sign identities under
varying old marginals. Lemma S fixes one entire joint marginal,
so the counterexample does not attack a step it actually takes.

The fixed-law separation attack in Section 6 could have refuted
Lemma S itself: a positive excess would produce a finite violation
of old $J$. Sections 2 and 7 independently test the other places
where that local assertion might fail to prove the whole theorem.
Section 8 tests the full consequence separately. These arguments
give the report's attacks mathematical force beyond agreement with
its conclusion.

## 10. Dependencies, source scope and outcome

The consumed order is finite budget and elementary replication;
arbitrary-product probability and the base rooted law; derived signs;
fixed-marginal successors; limit laws and trace energy; Hilbert
partition and actual layer coloring; cardinal induction; then
countable deletion, packing and the E111 implication.
There is no cycle and no native L-claim premise. This was derived
from the supplied proof sites on 2026-10-17 UTC, not from the
manifest's empty premise list. No live ledger or external standing
was used.

The rooted note's initial abundant-pattern proposition is needed.
Its later inequality (5) and its coloring consequence are not.
Proposition C contributes the Hilbert partition; its subsequent
finite-density compactness conclusion is not needed. Lemma G and
its specialized literature inputs, the alternative approaches,
Propositions A, B, D, E and U, historical analytic conclusions and
finite companion calculations are not premises or additional
acceptance targets.

The standard inputs retained at their exact use are choice and
set-sized recursion, elementary hull and chain-union facts,
compactness of products of finite spaces, Riesz representation,
Banach--Alaoglu, uniqueness of countable-product laws, monotone
convergence, Fatou, finite-dimensional separation, and orthonormal
bases with Bessel's inequality. Their original-source proofs remain
unread. The interfaces and deductions using them were checked;
this is not a reconstruction of all classical literature.

No counterexample to either target or unsupported essential
deduction in its frozen proof was found. The mathematical verdict
supported by these checks is **refutation-failed** for target 1
and then **refutation-failed** for target 2. The grade separately
judges the report contract and isolation facts and withholds an
operative standing warrant until its own stated eligibility and
durable-filing conditions are resolved.
