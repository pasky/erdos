---
desc: Independent derivations and adversarial witnesses for the arbitrary-cardinality coloring theorem and its E111 implication.
---

# Independent derivations for the whole-conclusion examination

***

Examination date: 2026-10-17 UTC. The subject is the mathematical extraction
frozen on 2026-10-17 at 06:43:02 UTC. Project mathematics is credited to
Plasma AI. These derivations test that subject; they neither amend it nor
supply a verdict on later text. The exact retained inputs are identified by
[the subject manifest](subject/manifest.json).

The two conclusions tested are countable colorability of every finite-C
C-linear simple graph, with arbitrary vertex cardinality, and the full
limit h_G(n)/n tending to infinity for every graph of chromatic number
exactly aleph_1. The argument below is in ZFC. Its classical analytic
inputs are stated explicitly in the report. No specialized literature
proof or computational output is used.

## 1. Edge deletion and the actual finite budget

For a finite graph F,

$$
\beta(F)=\min_{c:V(F)\to\{-1,1\}}
  |\{uv\in E(F):c(u)=c(v)\}|.
$$

Indeed, deleting the monochromatic edges of any coloring leaves a
bipartite graph. Conversely, a proper binary coloring of F-D makes every
monochromatic edge of F belong to D. The two inequalities give equality.
Restricting a bipartizing deletion set to a subgraph proves monotonicity
of beta. Thus induced subgraphs and graphs obtained by retaining selected
edges inherit C-linearity.

The proof may therefore discard unlisted edges between copies. It never
requires the copied union to be induced. This is essential: extra edges
in the ambient graph do not invalidate the finite budget or the lower
bounds obtained from the selected edges.

The empty graph causes no problem. If C=0, no finite odd cycle exists;
otherwise that cycle would have beta equal to one. Independently, a
component can be colored by the parity of distance from a chosen root:
an edge joining vertices of equal parity would give an odd closed walk
and hence an odd cycle. Choice of a root in each component gives a
bipartition. The general measure proof also permits C=0 throughout.

## 2. Elementary chains, including singular cardinalities

Let kappa be an uncountable vertex cardinal and mu=cf(kappa). Choose a
regular theta sufficiently large that G belongs to H(theta). This
requires more than the bare inequality theta>kappa if the vertex labels
have large hereditary size; the subject explicitly also requires
G in H(theta), and such a larger regular theta can be chosen.

A structure in the countable language of membership has elementary hulls
of size at most max(aleph_0, |A|) over a parameter set A. To see the size
point, choose witness functions for the countably many existential
formulas and close A under these finitely arity functions through omega
stages. The closure has that cardinal bound and the witness criterion
makes it elementary. This is the downward elementary-submodel input
used here; it does not require the models to be transitive or countably
closed.

Choose increasing sets of vertices of size less than kappa whose union
is V(G), indexed by mu. Construct N_0 containing G, and construct each
N_(xi+1) to contain the vertices required at that stage, every element
of N_xi, and N_xi itself as an element. At a limit lambda<mu take the
union of the earlier models. The union is elementary: an existential
formula with finitely many parameters from the union has those
parameters together in one earlier elementary model, which already
supplies a witness whenever H(theta) does.

At a limit lambda<cf(kappa), the sizes of the fewer than cf(kappa)
earlier models have supremum below kappa. Their union still has size
less than kappa. This checks the singular case as well as the regular
case. At the end, the union may have size kappa, as intended; it is not
an induction layer. Every individual layer and V(G) intersect N_0 has
size less than kappa. When kappa=aleph_1 the construction uses countable
models at every stage below omega_1.

Each N_xi is itself in H(theta). Its hereditary size is less than theta,
using regularity of theta, |N_xi|<theta, and membership of its elements
in H(theta). Thus it is a legitimate parameter in the next hull. For
zeta<xi, N_zeta belongs to N_xi: it enters as an element at the first
successor and persists in the increasing chain.

Every vertex outside N_0 first enters at a successor. First entrance at
a nonzero limit would contradict the union definition. Consequently its
trace in the model preceding its layer contains all its neighbors in
earlier layers. This remains true when cf(kappa)=omega or when kappa is
singular of uncountable cofinality.

## 3. Replication without naming an outside vertex

Let N be one of these elementary models, F a finite vertex set,
R=F intersect N, D a finite subset of N, and Q an element of N disjoint
from F minus R. Enumerate R and encode the graph induced by F as a
finite diagram with the other positions labeled by natural numbers.
All the parameters of the following existential assertion belong to N:
G, the finite root tuple, D, Q, the number of new positions, and the
finite diagram.

The assertion says that there are distinct new vertices outside
D union Q union R realizing the diagram over the fixed roots. It does
not name any member of F minus R. The original vertices F minus R
witness the assertion in H(theta): they miss N and hence D and R, and
miss Q by hypothesis. Elementarity supplies a finite witness tuple in N.
Every entry of a finite tuple belonging to an elementary model belongs
to that model, so the new vertices are actually in N.

A finite set of elements of N, and any chosen finite tuple of them, is
an element of N. This justifies both the root parameters and repeated
use of the finite forbidden set D. At each repetition add all previous
new vertices and all other roots to D. The repetitions yield pairwise
disjoint new copies avoiding every root.

The successor proof needs the stronger avoidance Q=N_xi when copying
inside N_(xi+1). This is legitimate precisely because
N_xi belongs to N_(xi+1), not merely because the models are nested.
The original pattern vertices outside N_(xi+1) miss Q. The resulting
copies lie in N_(xi+1) minus N_xi. No countability assumption was used.

The measures, derived signs, and whole countable trace subsets need not
belong to a model. Only the finite root subsets used in a particular
diagram must belong to it, and they do. No measure-theoretic object is
used as a parameter in this replication argument.

## 4. Probability laws on an arbitrary sign product

Write Omega_I={-1,1}^I with its compact Hausdorff product topology. A
continuous function depending on finitely many coordinates is called a
cylinder function. Cylinder functions are uniformly dense in C(Omega_I).
For a direct check, for each point take a basic finite-coordinate
neighborhood on which the oscillation of a given continuous function is
small. Compactness yields finitely many such neighborhoods. On the
common finite coordinate refinement, choose one value per cell. The
result is a cylinder function with the desired uniform approximation.

Consistent finite-coordinate probability laws define a positive
norm-one functional on the cylinder functions. Consistency makes it
well-defined; integration against a common finite-coordinate law checks
linearity, positivity, and the bound by the uniform norm. Continuity
extends it to C(Omega_I). The compact-Hausdorff Riesz representation
theorem gives a unique Radon probability law. Uniform density also
proves uniqueness among Radon laws with those finite marginals. This
argument does not identify all Borel sets with the sigma-algebra
generated by finite cylinders when I is uncountable.

The Radon probabilities form a weak-star compact convex subset of
C(Omega_I)^*: positivity and value one on the constant function are
closed conditions in the dual unit ball. This is the precise
Banach-Alaoglu compactness input. A prescribed full marginal is a
closed condition, tested on continuous functions pulled back by the
coordinate projection. It is not merely a finite list of moment
conditions. Extension by constant extra coordinates is continuous and
shows that a prescribed marginal has at least one extension.

Now fix a Radon law nu on Omega_I and any family d_j of Borel signs,
each determined by a countable subset of I. For every finite set of old
coordinates and finitely many d_j, their joint law under nu is defined;
these finite laws are consistent. The preceding construction gives a
Radon law Lambda on the old and new coordinates. Its old marginal is
nu by Radon uniqueness.

For one j, project Lambda to its new coordinate together with its
countably many determining old coordinates. On this countable product,
finite cylinders generate the Borel sigma-algebra: they are a countable
base. Uniqueness of finite probability measures on a generating
pi-system shows that this marginal is the ordinary joint distribution
under nu. In particular, the new coordinate equals d_j of the old
coordinates almost surely. This reasoning is applied separately for
each j. It does not assert that an uncountable intersection of those
probability-one events is measurable or has probability one.

Consistent Radon marginals on an increasing family of coordinate sets
are handled in the same way: every finite coordinate set belongs to
one member of the family. The projected law on each old coordinate set
is exactly its specified Radon law, again by uniqueness.

## 5. Initial rooted inequalities from the finite graph budget

For a rooted pattern P, write R_P for its finite root set, S_P for its
finite new set, and e_P(tau) for the least monochromatic cost of its
listed edges touching S_P after fixing the root signs tau. Root-root
edges are excluded. Replication makes each pattern over N_0 abundant.

Fix finitely many such patterns P_i and nonnegative integer weights
a_i. Their root union R is finite. For each positive integer k,
realize k a_i copies of pattern i, with all new sets disjoint and
avoiding R. Retain only the prescribed edges touching new vertices.
For any common root assignment the copies minimize independently;
the minimum cut cost of this finite graph is

$$
k\min_\tau\sum_i a_i e_{P_i}(\tau).
$$

C-linearity therefore implies

$$
\min_\tau\sum_i a_i e_{P_i}(\tau)
\le C\sum_i a_i|S_i|+\frac{C|R|}{k}.
$$

The left side is independent of k. Let k tend to infinity. Scaling
handles rational weights, and continuity of the minimum of finitely
many linear functions handles nonnegative real weights.

Let Q be the convex hull in a finite-dimensional Euclidean space of
the vectors (e_(P_i)(tau))_i. If Q missed the lower orthant with corner
(C|S_i|)_i, strict separation of the compact convex set from this
closed convex orthant would give nonnegative weights whose weighted
minimum exceeds the weighted corner. The weights must be nonnegative
because the orthant is unbounded in every negative coordinate
direction. This contradicts the inequality just obtained. Thus one
distribution of root signs meets all the chosen expected-cost bounds.

Each bound is a closed condition on Radon laws because e_P depends
continuously on finitely many coordinates. Extend each finite-family
root distribution by constant unused coordinates. Compactness and the
finite intersection property then give a single law satisfying every
pattern inequality J at N_0. The copied roots cost C|R| only before the
replication limit; that term is legitimately removed by division by k.

## 6. A derived sign for an uncountable trace

Assume J holds for a fixed law nu at a model N. Let y be outside N
with infinite trace T. A finite star with center y and roots B subset T
has extension cost

$$
Z(B)=\min\bigl(|\{u\in B:\sigma_u=1\}|,
              |\{u\in B:\sigma_u=-1\}|\bigr).
$$

Hence E Z(B)<=C for every finite B. For countable B, increasing finite
exhaustions and monotone convergence give the same bound for the
smaller of the two possibly infinite sign counts.

Let a be the supremum of E Z(B) over countable subsets of T. It lies
in [0,C]. Choose countable B_n with expectations approaching a and
take their union together with any fixed countably infinite subset of
T. Call the resulting set A. Monotonicity gives E Z(A)>=a, while the
definition of a gives the reverse inequality. Thus the supremum is
attained on this countably infinite A; no compactness of a space of
subsets is being assumed.

Since E Z(A) is finite, Z(A) is finite almost surely. On that event one
sign occurs only finitely often and the other infinitely often on A.
Let s be the latter sign, with an arbitrary value on the exceptional
null event. The eventual-sign event along a fixed enumeration of A is
Borel, so s is a countably determined measurable sign.

For each u in T minus A, adding u cannot change which sign is infinite,
outside the same exceptional event. Therefore

$$
Z(A\cup\{u\})=Z(A)+\mathbf1_{\sigma_u\ne s}
\quad\hbox{almost surely}.
$$

Both expectations of Z are equal to a, by maximality and monotonicity.
It follows that nu(sigma_u != s)=0, separately for each u outside A.
On A, countable monotone convergence gives

$$
\sum_{u\in A}\nu(\sigma_u\ne s)=\mathbb E Z(A)\le C.
$$

The arbitrary sum over all of T, defined as a supremum of finite sums,
is the same sum: every summand outside A is zero. Thus

$$
\sum_{u\in T}\nu(\sigma_u\ne s)\le C.
$$

This is a sum of probabilities, not the expected value of a newly
assumed measurable count over all of an uncountable T. No assertion
about simultaneous agreement at all the outside-A coordinates is used.

## 7. The fixed-marginal successor assertion

Put N=N_xi and N^+=N_(xi+1). Let X be the new vertices with infinite
trace in N, and Y the new vertices with finite trace. For each y in X,
let d_y=-s_y, where s_y is supplied by the preceding section for the
fixed old law nu. Form their joint Radon law Lambda with all old
coordinates. Let K be the Radon laws on the full next coordinate set
having this entire marginal Lambda on the old coordinates together
with X. Section 4 proves that K is nonempty, convex, and compact and
that every member has the required individual almost-sure identities.

For finitely many patterns P_i over N^+, let
R_X, R_Y, and R_low be their root union in X, Y, and the old model,
respectively. A finite-dimensional separation argument, exactly as in
Section 5, reduces simultaneous expected-cost feasibility to every
nonnegative weighted inequality. For weights rho_i its left side is

$$
\min_{\pi\in K}\sum_i\rho_i\mathbb E_\pi e_{P_i}
 =\mathbb E_\Lambda\min_{\eta\in\{-1,1\}^{R_Y}}
      \sum_i\rho_i e_{P_i}(\tau,d,\eta),
$$

where each pattern uses only its own root coordinates. The left side
is at least the right side by the pointwise minimum. For equality,
choose the first minimizing assignment eta in a fixed finite enumeration, separately for
each assignment to the finitely many old and X root coordinates.
Assign +1 to the other Y coordinates. This is a continuous function of
finitely many coordinates of Lambda; adjoining it yields a law in K
attaining equality. No regular conditional probability or measurable
selection theorem on an uncountable space is needed.

Both sides are Lipschitz in the finitely many weights, since
0<=e_(P_i)<=|E_(P_i)|. Homogeneity and rational approximation reduce the
problem to nonnegative integer weights a_i, not all zero.

Fix k>=1. Replicate k a_i copies of each S_i inside N^+ but outside N,
using Q=N in Section 3. Make every copy disjoint from all other copies
and all roots. Fix these copies while a separate integer L increases.
For y in R_X, let A_y^L be the first L elements of its countable trace
set A_y. Form a pattern over N whose new vertices are R_X, R_Y, and
all the copies, whose roots are R_low and the union of the A_y^L, and
whose listed edges are the copied pattern edges and the stars from y
to A_y^L.

These are actual edges of G. Each copied edge touches that copy's new
vertices; the stars have endpoints in R_X and N. Thus the copied edge
sets and star edges do not overlap. No edge between vertices of
R_X union R_Y is listed. Extra edges of G can be discarded by Section 1.
The new-vertex count is independent of L, namely

$$
q+k\sum_i a_i|S_i|,\qquad q=|R_X|+|R_Y|.
$$

J at N bounds its expected minimum e_L by

$$
\mathbb E_\nu e_L\le Cq+Ck\sum_i a_i|S_i|. \tag{7.1}
$$

Here is an independent expression for this minimum. With tau fixed,
let b_y^L count the members of A_y^L whose signs differ from s_y. After
fixing signs delta on R_X and eta on R_Y, all copies minimize
independently, and their total minimum cost is

$$
k\sum_i a_i e_{P_i}(\tau,\delta,\eta).
$$

The star at y costs b_y^L if delta_y=d_y and L-b_y^L otherwise.
The total possible copied-edge cost is at most

$$
W=k\sum_i a_i|E_{P_i}|.
$$

For almost every tau, the finitely many b_y^L stay bounded as L grows.
For all sufficiently large L, each L-2b_y^L exceeds W. Changing one
wrong delta_y to d_y then saves more star cost than it could add to
all copied edges. Every minimizing assignment must consequently have
delta=d on R_X. It follows that, eventually for this tau,

$$
e_L(\tau)=\sum_{y\in R_X}b_y^L
 + k\min_\eta\sum_i a_i e_{P_i}(\tau,d,\eta). \tag{7.2}
$$

Only finitely many trace signs are combined here. The threshold for L
may depend on tau and k; no uniform threshold is asserted. The
functions e_L are nonnegative and nondecreasing in L, since each
larger star list adds edges to the same fixed new-vertex optimization.
Either monotone convergence or the subject's Fatou argument is
therefore valid. Dropping the nonnegative star contribution in (7.2)
and using (7.1) gives

$$
\mathbb E_\Lambda\min_\eta\sum_i a_i e_{P_i}(\tau,d,\eta)
 \le C\sum_i a_i|S_i|+\frac{Cq}{k}.
$$

The expectation agrees with that under nu of its derived signs: only
finitely many d_y and old coordinates are involved, and their joint
law was prescribed in Lambda. It is independent of k. Let k tend to
infinity. This proves the required weighted inequality, and hence
finite-family feasibility inside K. All the pattern-cost constraints
are closed; compactness gives one extension meeting every one of them.

The limit order is indispensable: first L tends to infinity for fixed
k and fixed copies, then k tends to infinity, then separation and the
finite intersection property supply the full law. No cut is optimized
independently at incompatible thresholds. The same old law is used in
every inequality.

### The attempted separation counterexample, in reverse

Suppose the fixed old law admitted no successor satisfying the target
constraints. Compact separation would give finitely many patterns and
nonnegative weights with a strict excess. Approximation would give
integer weights with

$$
\alpha=
\mathbb E_\Lambda\min_\eta\sum_i a_i e_{P_i}(\tau,d,\eta)
 -C\sum_i a_i|S_i|>0.
$$

Choose k with k alpha>Cq, and build the copied patterns just described.
Equation (7.2) would imply

$$
\lim_L\mathbb E e_L
 \ge k\mathbb E_\Lambda\min_\eta\sum_i a_i e_{P_i}
 > Cq+Ck\sum_i a_i|S_i|.
$$

Consequently some finite L would already violate (7.1). This is a
finite rooted pattern violating J of the assumed old law. It explains
why the strongest attempted obstruction fails: incompatible future
requirements cannot hide inside a fixed old law satisfying all of J.
The roots added to the new layer cost only Cq, whereas the alleged
weighted excess grows with k. This is a check of the supplied
successor argument, not a replacement hypothesis for it.

## 8. Limit laws and trace energy

Choose a starting law from Section 5 and use Section 7 at successors.
At a limit lambda, Section 4 gives a Radon law with all earlier
marginals. For a pattern over N_lambda, its finitely many roots belong
together to some N_xi with xi<lambda. Its new vertices, outside
N_lambda, are also outside N_xi. It is therefore already a pattern over
N_xi, with exactly the same finite root-cost function. Its expectation
and J inequality are preserved. This proof does not require countable
cofinality or any bound on the number of patterns.

The final consistent law nu on all vertex coordinates retains every
stage marginal. For an infinite-trace vertex v entering after N_xi,
the identity sigma_v=-s_v depends on its coordinate and countably many
old coordinates. That countable marginal is preserved by all later
extensions and by the final law. For each u in its trace,

$$
\nu(\sigma_u=\sigma_v)=\nu(\sigma_u\ne s_v).
$$

Section 6 therefore proves the claimed arbitrary-sum bound at v.
All coordinates are unit vectors in the real Hilbert space L^2(nu),
and

$$
1+\langle\sigma_u,\sigma_v\rangle
 =2\nu(\sigma_u=\sigma_v).
$$

Hence each infinite trace has energy at most 2C. This is a deterministic
inequality of expectations for each vertex. There is no sampling of
one coloring claimed to be good simultaneously at all vertices.

## 9. Actual countable coloring without separability

Choose an orthonormal basis of the real Hilbert space and well-order
its index set. Bessel's inequality makes the set of coordinates with
magnitude at least any positive a finite for each unit vector x.
Every such vector has a nonzero coordinate. Choose one magnitude m>0.
Only finitely many magnitudes exceed m/2, so rationals 0<b<a<m can be
chosen above m/2 with no coordinate magnitude in [b,a]. Thus

$$
S_a(x)=\{i:|\langle x,e_i\rangle|\ge a\}
$$

is nonempty and finite, and every coordinate outside it has magnitude
at most b. Assign x the first suitable rational pair in a fixed
countable enumeration, together with the sign of its coordinate at
the least member of S_a(x).

For x,y with the same label, distinct sets S_a give a coordinate at
which one magnitude is at least a and the other at most b. Thus
||x+y||>=a-b. If the sets agree, their least coordinate has the same
sign for x and y, so ||x+y||>=2a. In either case

$$
1+\langle x,y\rangle=\tfrac12\|x+y\|^2
 \ge\tfrac12(a-b)^2=\eta>0.
$$

There are only countably many labels. The support set or its least
index is not part of the label; recording it would incorrectly create
an uncountable palette. Only its coordinate sign is recorded. No
separability assumption appears in this construction.

Fix one label class, and retain only edges between different layers.
Order vertices by layers and well-order within layers. An earlier
neighbor in this retained graph belongs to the trace. A finite trace
supplies finitely many such neighbors directly. On an infinite trace,
each same-class neighbor contributes at least eta to the nonnegative
energy sum, which is at most 2C. There can be at most 2C/eta of them:
otherwise finite subsets of arbitrarily large size would violate the
sum bound. Initial-layer vertices have no earlier inter-layer
neighbors. Greedy coloring along the well-order therefore always has
a natural-number color available. No within-layer edge is being
ignored by the final coloring; those edges will use a different label.

For a minimal-cardinality counterexample to countable colorability,
every layer would itself have a proper countable coloring: it has
smaller cardinality, is C-linear, and would otherwise be a smaller
counterexample. The cardinal estimates of Section 2 justify this even
at singular kappa. Countable graphs are never counterexamples.

Color each vertex by the triple consisting of its Hilbert label, its
greedy inter-layer color within that label, and its color in a fixed
proper coloring of its own layer. The product of these three countable
palettes is countable. An edge whose labels differ is separated by
the first coordinate; one within a label but between layers by the
second; one within a layer and label by the third. This contradicts
the proposed minimal counterexample and proves the first target.

The proof uses only the partition portion of Proposition C. It does
not apply its separate hereditary-density conclusion to a trace-star
bound. It also imposes no uniform energy bound at finite-trace vertices.

## 10. The entire E111 implication

For an infinite graph, the least profile h_G(n) is well-defined. There
is at least one n-vertex subgraph for every positive n, and its beta
value belongs to the finite set of integers from zero to binom(n,2).
Thus the supremum is a maximum. Taking the induced graph on the same
vertices can only increase beta, so either convention for taking the
maximum gives the same least profile. Any deletion bound permitted by
the supplied problem wording is at least this least profile.

If chi(G)=aleph_1 and S is countable, then chi(G-S)=aleph_1. A countable
coloring of G-S, together with disjoint fresh colors for the individual
vertices of S, would be a countable proper coloring of G. The reverse
upper bound follows by restricting an aleph_1-coloring of G.

Fix any real K>0. At stage xi<omega_1 of a recursion, the union of the
previously selected finite vertex sets is countable. Its deletion
leaves chromatic number aleph_1. By the first target, this remainder
cannot be 2K-linear, so choose a finite F_xi in it with
beta(F_xi)>2K|V(F_xi)|. The recursion yields aleph_1 pairwise disjoint
finite witnesses. There are only countably many finite isomorphism
types. If every type occurred only finitely often, the whole family
would be countable. Hence one type F occurs infinitely often, with
v=|V(F)| and b=beta(F)>2Kv.

For every n>=2v take q=floor(n/v) disjoint copies and fill the remaining
n-qv vertices from elsewhere in G. Any bipartizing edge deletion in
the induced graph on these n vertices must delete at least b edges
from each copy. The copy edge sets are disjoint. Cross edges and
padding vertices can only add constraints. Consequently

$$
h_G(n)\ge qb
 \ge \frac bv(n-v)
 >2K(n-v)\ge Kn.
$$

The threshold 2v may depend on K and G; the limit statement permits
this dependence. Since K was arbitrary, this gives the full
limit to infinity, not only unboundedness or a subsequence.

For the separately asserted remainder formulation, suppose the limit
fails. Choose a positive finite K with h_G(n)<=Kn for infinitely many
positive n, enlarging a zero threshold if necessary. Take a maximal
pairwise disjoint family of finite graphs with beta(F)>2K|V(F)|. If
it were uncountable, the preceding repeated-type and packing argument
would contradict infinitely many such n. The family and its vertex
union S are therefore countable. Maximality says that G-S is
2K-linear, while countable deletion preserves chi(G-S)=aleph_1. This
contradicts the first target. Conversely, a C-linear graph of chromatic
number aleph_1 would have h_G(n)<=Cn for every n and would refute the
E111 limit. This checks the equivalence of the restricted CC lemma
with E111; it does not claim a converse equivalence between E111 and
the stronger theorem with unrestricted chromatic number.

No step assumes that |V(G)|=aleph_1. Only the chromatic number is fixed
in this application. Countable unions of earlier finite witnesses,
finite isomorphism types, and exact-n padding are the only size
arguments in the packing reduction.

## 11. Exact hostile witnesses to nearby invalid inferences

These witnesses test genuine risks in the proof. They are not
counterexamples to the two target conclusions.

### Expected minimum versus actual coordinate cost

Let G be the infinite star with center z and leaves L, and take C=0.
For an abundant rooted pattern, any prescribed edge involving a new
vertex must run from the fixed root z to a new leaf. A prescribed edge
between two new vertices, or from a leaf root to a new vertex, would
require the unique center among the new vertices in every copy and
would prevent two copies with disjoint new vertices. Thus every
abundant pattern has minimum extension cost zero for every root
assignment: put its new leaves opposite z. The law concentrated on
all-positive coordinates satisfies all abundant-pattern inequalities,
yet every actual edge has equal coordinate signs and positive cost.

This explicitly refutes replacing the expected minimum by the cost of
the same law's coordinates. It does not refute the supplied argument.
An elementary model containing G contains its unique center, so every
outside leaf has finite trace. The successor lemma leaves those
coordinates free; the final greedy coloring handles their finite
traces. For infinite traces, Section 7 supplies the missing prescribed
coordinate relation by a new extension, rather than assuming it of
the original rooted measure.

### Individual null events versus a simultaneous event

On the probability space [0,1] with Lebesgue measure, define a sign for
each t in [0,1] by sigma_t(omega)=-1 exactly when omega=t. Each coordinate
is +1 almost surely, and every countable collection is simultaneously
+1 almost surely. Nevertheless every outcome has one negative
coordinate. This is a family of measurable random variables; no
measurability of its map into the full uncountable Borel product is
assumed.

This witnesses the danger of taking an uncountable intersection of
probability-one events. The supplied argument survives because its
trace bound is a sum of individual probabilities, every rigidity
calculation uses only finitely many signs, and its final coloring uses
L^2 vectors rather than a sampled outcome. The Radon construction
preserves the required countable-coordinate identities only; it is not
claimed to preserve arbitrary uncountably quantified events.

### A derived-sign condition is not generally weak-star closed

In {-1,1}^N let tau^(n) have its first n coordinates negative and all
later coordinates positive. Then tau^(n) converges to the all-negative
point. Define d(tau)=+1 if infinitely many coordinates of tau are
positive and d(tau)=-1 otherwise. Each point mass at (tau^(n),+1)
satisfies the derived-sign identity. Its weak-star limit at the
all-negative point with new coordinate +1 violates that identity.

Thus compactness cannot be invoked merely by calling an arbitrary
Borel derived-sign constraint closed. Here the old marginals vary, so
this example does not defeat the successor lemma. That lemma fixes
one entire joint Radon law Lambda before invoking compactness. Its
constraint is the genuinely closed marginal constraint established in
Section 4. This is exactly the distinction needed to reject the
attempted compactness objection.

## 12. Result of the attacks

The attempted fixed-marginal obstruction yields the explicit finite
contradiction in Section 7. The uncountable-null-event and Borel-limit
objections identify real failure modes but not inferences the subject
uses. The size and induction checks include all singular cardinals;
the coloring check treats finite traces separately and handles all
within-layer edges. The E111 check obtains every sufficiently large n
for each fixed K and checks the countable-deletion remainder as well.

These derivations find neither a counterexample nor an unsupported
essential deduction in the two frozen conclusions under the stated
classical inputs. The report records the scoped mathematical verdict,
reading limits, and the separate eligibility and grading conditions.
