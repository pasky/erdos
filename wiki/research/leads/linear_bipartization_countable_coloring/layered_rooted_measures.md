---
name: research/leads/linear_bipartization_countable_coloring/layered_rooted_measures
title: Layered rooted measures and countable colorings of linear graphs
desc: |
  Independently reviewed proof that every finite-C $C$-linear graph has
  countable chromatic number at every vertex cardinality. Along a chain of elementary submodels, the
  rooted extension measure is corrected layer by layer so that each
  infinite-trace vertex takes the opposite of its countably determined
  sign, with expected trace defect at most $C$; Proposition C's classes
  then color. A uniform bound including finite-trace vertices fails.
created: 2026-10-17T05:40:00Z
updated: 2026-10-17T05:40:00Z
---

# Layered rooted measures and countable colorings of linear graphs

The target, conventions, Lemma F, Proposition C and the reviewed Steps 1 to
3 are in the
[[research/leads/linear_bipartization_countable_coloring/_index|canonical proof sketch]],
and the single compatible measure is in the
[[research/leads/linear_bipartization_countable_coloring/rooted_cut_measures|rooted measure note]].
This proof is Plasma AI's. The whole-conclusion
[review](evidence/verify/whole_conclusion/review.md) and separate
[PASS grade](evidence/verify/whole_conclusion/grade.md) accept
**refutation-failed** for the theorem below at every vertex cardinality,
then for its full E111 implication. The current mathematical statements and
proof are the examined text frozen on 2026-10-17 at 06:43:02 UTC.
The [record](evidence/verify/whole_conclusion/_index.md) preserves exact
inputs, reasoning and limits. The reviewer's operating-section exposure is
ruled immaterial by the grader; the grader's heading-only disclosure is
ruled permitted navigation by the distinct commissioning authority in the
[scope finding](evidence/verify/whole_conclusion/eligibility.md). The grade's
filing and ordered-adoption conditions are fulfilled. Original proofs of
classical inputs and the unused Proposition U are outside its coverage.
Catalog adoption and Lean verification remain separate.

**Theorem (independently reviewed).** For every $C\ge0$, every
$C$-linear graph has countable chromatic number.

Here $C$ is finite, and $C$-linear means that every finite subgraph $F$
can be made bipartite by deleting at most $C|V(F)|$ edges. The graph is
simple and its vertex set can have any cardinality. All sums of
nonnegative terms over an arbitrary index set mean the supremum of the
finite subsums.

Through Steps 1 to 3, the theorem gives $h_G(n)/n\to\infty$ for every graph
$G$ with $\chi(G)=\aleph_1$, of any cardinality: if the limit failed, Step 3
would give a countable $S$ with $G-S$ a $2K$-linear graph of chromatic
number $\aleph_1$.

## Chains, layers, traces and patterns

Let $G$ be $C$-linear with $\kappa=|V(G)|$ uncountable, and put
$\mu=\operatorname{cf}\kappa$. Choose a regular $\theta>\kappa$ with
$G\in H(\theta)$ and a
continuous chain $(N_\xi)_{\xi<\mu}$ of elementary submodels of $H(\theta)$,
each of cardinality below $\kappa$, with $G\in N_0$, $N_\xi\in N_{\xi+1}$,
unions at limits, and $V(G)\subseteq\bigcup_\xi N_\xi$. When
$\kappa=\aleph_1$ the models are countable. Such a chain exists also when
$\kappa$ is singular: cover $V(G)$ by an increasing sequence of $\mu$
sets of size below $\kappa$, and take elementary hulls, including the
previous model both as a subset and as an element at each successor.
At a limit $\lambda<\operatorname{cf}\kappa$ the union still has size
below $\kappa$ and is elementary. Write $V_\xi=V(G)\cap N_\xi$.
For $v\notin N_0$ the least $\xi$ with $v\in N_\xi$ is a successor, so
$v\in N_{\beta+1}\setminus N_\beta$ for a unique $\beta=\beta(v)$, the
**layer** of $v$; the set $V_0$ counts as one more layer, placed first. The
**trace** of $v\notin N_0$ is $T_v=N(v)\cap N_{\beta(v)}$, which contains
every neighbour of $v$ in an earlier layer.

A **pattern over $N_\xi$** is a triple $P=(R,S,E_P)$: a finite
$R\subseteq V_\xi$, a finite nonempty $S\subseteq V(G)\setminus N_\xi$, and
a set $E_P$ of edges of $G$, each meeting $S$ and lying inside $R\cup S$.
For $\tau\in\{-1,1\}^R$ let

$$
 e_P(\tau)=\min_{\eta\in\{-1,1\}^S}
 \bigl|\{uv\in E_P:(\tau\cup\eta)(u)=(\tau\cup\eta)(v)\}\bigr| .
$$

For a Radon probability measure $\nu$ on $\{-1,1\}^{V_\xi}$ write
$J(\nu,\xi)$ for the property

$$
 \mathbb E_\nu\,e_P(\sigma|_R)\le C|S|
 \qquad\text{for every pattern }P\text{ over }N_\xi. \tag{J}
$$

**Replication.** Let $N$ be one of the models, $F$ a finite vertex set,
$R=F\cap N$, $D\subseteq N$ finite and $Q\in N$ a set disjoint from
$F\setminus R$. There is an injection $\varphi:F\setminus R\to
N\setminus(D\cup Q\cup R)$ such that the identity of $R$ together with
$\varphi$ is an isomorphism $G[F]\to G[R\cup\varphi(F\setminus R)]$. The
statement has parameters $G,R,D,Q$ and the finite adjacency pattern, all in
$N$, and $F\setminus R$ witnesses it in $H(\theta)$, so a witness lies in
$N$. The formula names the finite diagram over $R$, not the vertices of
$F\setminus R$. A finite tuple belonging to $N$ has all its entries in
$N$. This is Lemma F with the extra parameter $Q$; repeating it gives any
finite number of pairwise disjoint copies. In particular, for $\zeta<\xi$
one may take $Q=N_\zeta$, since $N_\zeta\in N_\xi$.

## Probability on arbitrary products

For an index set $I$, put $\Omega_I=\{-1,1\}^I$ with the compact product
topology. A consistent family of probability laws on its finite
coordinate sets determines a unique Radon probability measure. Indeed,
expectations of continuous finite-coordinate functions give a positive
linear functional of norm one. Such functions are uniformly dense in
$C(\Omega_I)$, by compactness and the basic finite-coordinate
neighbourhoods. Extend the functional by continuity and apply the Riesz
representation theorem. The same construction applies to consistent
marginals on an increasing family of coordinate sets.

Radon probability measures on $\Omega_I$ form a weak-star compact convex
set. Fixing a marginal is a closed condition, as is a bound on the
expectation of a continuous finite-coordinate function. A nonempty
family of measures with fixed marginal remains nonempty after adding
unconstrained coordinates, for example by setting them all to $+1$.

Only countably determined random variables are used below. Given a law
on $\Omega_I$ and any family of signs $d_j$, each a Borel measurable
function of countably many coordinates, the finite joint laws of the old
coordinates and the $d_j$ are consistent. The preceding construction
therefore gives their joint Radon law on $\Omega_{I\sqcup J}$. Its
restriction to any countable set of coordinates agrees with the ordinary
joint distribution, since finite cylinders determine a probability
measure on a countable product. Consequently each identity
$\sigma_j=d_j(\sigma|_I)$ holds almost surely in this law. No common
probability-one event for uncountably many such identities is required.

## The base measure

**Lemma 0.** There is $\nu_0$ with $J(\nu_0,0)$.

This is the proposition of the rooted measure note restricted to patterns
over $N_0$. Replication makes each such pattern abundant: arbitrarily many
copies of $S$ with pairwise disjoint new vertices, avoiding $R$ and any
given finite subset of $N_0$, all fixing $R$; the copies lie in $N_0$,
which does not matter, since only the finite union graph is used. The
proof there applies with root assignments restricted to $V_0$. It uses
$C$-linearity on the finite union of copies, finite convex separation, and
weak-star compactness of the Radon probability measures on
$\{-1,1\}^{V_0}$.

No probability measure is required to belong to an elementary model.
Replication uses only the graph and finite diagrams. In particular a
finite set of roots lies in the model whenever all its vertices do.

## Derived signs

**Lemma D.** Assume $J(\nu,\xi)$, and let $y\notin N_\xi$ have infinitely
many neighbours in $N_\xi$; write $T=N(y)\cap N_\xi$. There are a countable
infinite $A\subseteq T$ and a sign $s_y$, a measurable function of
$\sigma|_A$, such that $\nu$-almost surely only finitely many $u\in A$ have
$\sigma_u\ne s_y$, and

$$
 \sum_{u\in T}\nu(\sigma_u\ne s_y)\le C. \tag{D}
$$

*Proof.* For finite $B\subseteq T$ the pattern $(B,\{y\},\{yb:b\in B\})$
has $e=Z(B)$, the smaller of the numbers of $+1$ and $-1$ signs on $B$. So
$\mathbb E_\nu Z(B)\le C$. For countable $B$ let $Z(B)$ be the supremum
over its finite subsets, which is again the smaller sign count; monotone
convergence gives $\mathbb E_\nu Z(B)\le C$. Since $Z$ increases with $B$,
choose countable sets whose expectations approach the supremum, and take
their union together with any countable infinite subset of $T$. The
result is a countable infinite $A$ with $\mathbb E_\nu Z(A)$ maximal
among countable subsets of $T$. Then $Z(A)$ is
finite almost surely, so one sign occurs only finitely often on the
infinite set $A$; let $s_y$ be the other, setting $s_y=+1$ on the
exceptional null set. The eventual-sign events along an enumeration of
$A$ are Borel, so $s_y$ is a Borel function of these countably many
coordinates. For $u\in T\setminus A$,
almost surely $Z(A\cup\{u\})=Z(A)+\mathbf1_{\sigma_u\ne s_y}$, and
maximality gives $\mathbb E Z(A\cup\{u\})=\mathbb E Z(A)$, so
$\nu(\sigma_u\ne s_y)=0$. Finally
$\sum_{u\in A}\mathbf1_{\sigma_u\ne s_y}=Z(A)$ almost surely, and summing
gives (D). For an uncountable $T\setminus A$, the zero-probability
conclusion is used separately for each $u$, so its finite subsums are
zero; no uncountable union of null events is taken. $\square$

When $T$ is countable one may take $A=T$, and $s_y$ is the almost sure
eventual sign along $T$, as in formula (4) of the rooted measure note.
For uncountable $T$, (D) is only a sum of probabilities. It does not
assert a common conull event on which the whole trace has finite
minority.

## The successor step

Let $X_\xi$ be the set of vertices of layer $\xi$ with infinite trace, and
$Y_\xi$ the other vertices of layer $\xi$. Thus $V_{\xi+1}$ is the disjoint
union of $V_\xi$, $X_\xi$ and $Y_\xi$.

**Lemma S.** Assume $J(\nu,\xi)$. There is a Radon probability measure
$\nu'$ on $\{-1,1\}^{V_{\xi+1}}$ such that

1. its marginal on $\{-1,1\}^{V_\xi}$ is $\nu$;
2. $\nu'(\sigma_y=-s_y)=1$ for each $y\in X_\xi$, with $s_y$ given by
   Lemma D for $\nu$;
3. $J(\nu',\xi+1)$ holds.

*Proof.* Under $\nu$ the signs $d_y=-s_y$ ($y\in X_\xi$) are measurable
functions of $\tau=\sigma|_{V_\xi}$, each depending on countably many
coordinates. Let $\Lambda$ be their joint Radon law with $\tau$, supplied
by the finite-law construction above, and let $\mathcal K$ be the set of Radon
probability measures on $\{-1,1\}^{V_{\xi+1}}$ whose marginal on the
coordinates $V_\xi\cup X_\xi$ is $\Lambda$. It is nonempty, convex and
weak-star compact. Every member satisfies 1 and 2. For a pattern $P$ over
$N_{\xi+1}$ the map $\pi\mapsto\mathbb E_\pi e_P$ is continuous and affine,
because $e_P$ depends on finitely many coordinates. By compactness it is
enough to find, for finitely many patterns $P_1,\ldots,P_r$ over
$N_{\xi+1}$, some $\pi\in\mathcal K$ with
$\mathbb E_\pi e_{P_i}\le C|S_i|$ for all $i$. By finite-dimensional
convex separation, it is enough that for all weights $\rho_i\ge0$

$$
 \min_{\pi\in\mathcal K}\sum_i\rho_i\,\mathbb E_\pi e_{P_i}
 =\mathbb E_\Lambda\min_{\eta}\sum_i\rho_i\,
   e_{P_i}\bigl(\tau|_{R_i\cap N_\xi},\,d|_{R_i\cap X_\xi},\,
   \eta|_{R_i\cap Y_\xi}\bigr)
 \le C\sum_i\rho_i|S_i| . \tag{S}
$$

For the separation step, the image of $\mathcal K$ under the $r$
expectation maps is compact and convex in $\mathbb R^r$. If it misses
the lower orthant with corner $(C|S_i|)_i$, separation gives
nonnegative weights violating (S). For the equality in (S), choose the
first minimizing $\eta$ in a fixed ordering of the finitely many
assignments to the $Y_\xi$-roots. This choice depends only on finitely
many coordinates of $\Lambda$; extend it by $+1$ on the other
$Y_\xi$-coordinates. It defines a member of $\mathcal K$ without a
conditional-distribution theorem. The left side of (S) is Lipschitz in
$\rho$, since $0\le e_{P_i}\le|E_{P_i}|$. By homogeneity and rational
approximation, it suffices to prove (S) for nonnegative integer weights
$a_i$, not all zero; the zero case is immediate.

Write $R_X=X_\xi\cap\bigcup_iR_i$, $R_Y=Y_\xi\cap\bigcup_iR_i$ and
$R_{\mathrm{low}}=V_\xi\cap\bigcup_iR_i$. For $y\in R_X$ let $A_y$ be given by
Lemma D, and let $A_y^L$ be its first $L$ elements in a fixed enumeration.
Fix an integer $k\ge1$ and put $m_i=ka_i$. By replication in
$N_{\xi+1}$, with $Q=N_\xi$, choose for each $i$ pairwise
disjoint copies $S_i^{(1)},\ldots,S_i^{(m_i)}$ of $S_i$ over $R_i$, all
disjoint from each other, from every $R_j$ and from $N_\xi$; the finite set
$D$ of replication collects the roots and the copies already chosen.
Keep these copies fixed while $L$ increases. Consider the pattern
$P_L^*$ over $N_\xi$ with

- new vertices $S^*=R_X\cup R_Y\cup\bigcup_{i,c}S_i^{(c)}$, all outside
  $N_\xi$;
- roots $R^*=R_{\mathrm{low}}\cup\bigcup_{y\in R_X}A_y^L\subseteq V_\xi$;
- edges: for each $y\in R_X$ all edges from $y$ to $A_y^L$, and for each copy
  $S_i^{(c)}$ the image of $E_{P_i}$ under the copying isomorphism, which
  fixes $R_i$.

Each listed edge meets $S^*$ and lies in $R^*\cup S^*$. Because the copies
are disjoint from each other and from all roots, and no edges between
vertices of $R_X\cup R_Y$ are listed, these edge sets are pairwise
disjoint. So $P_L^*$ is a pattern over $N_\xi$, and $J(\nu,\xi)$ gives

$$
 \mathbb E_\nu e_{P_L^*}(\tau|_{R^*})
 \le C(|R_X|+|R_Y|)+Ck\sum_i a_i|S_i|.
$$

For any signs $\eta$ on $S^*$, each copy of $S_i$ contributes at least
$e_{P_i}$ evaluated at $\tau$ on $R_i\cap N_\xi$ and at $\eta$ on
$R_i\setminus N_\xi$. Let $W=\sum_im_i|E_{P_i}|$, which bounds the copies'
total contribution. Almost surely the number $b_y^L$ of signs on $A_y^L$
differing from $s_y$ stays bounded as $L\to\infty$. If $L>2b_y^L+W$ for
every $y\in R_X$, changing any $\eta_y\ne d_y$ to $d_y$ lowers the star cost
of $y$ by $L-2b_y^L$ and raises the rest by at most $W$, so every minimizer
has $\eta|_{R_X}=d|_{R_X}$. Hence, almost surely,

$$
 \liminf_{L\to\infty}e_{P_L^*}(\tau|_{R^*})
 \ge k\min_{\eta}\sum_i a_i\,
 e_{P_i}\bigl(\tau,\,d,\,\eta|_{R_Y}\bigr),
$$

with the arguments restricted as in (S). Only the finitely many roots in
$R_X$ need a common probability-one event here. Fatou's lemma and division
by $k$ give

$$
 \mathbb E_\Lambda\min_{\eta}\sum_i a_i
 e_{P_i}\bigl(\tau,\,d,\,\eta|_{R_Y}\bigr)
 \le C\sum_i a_i|S_i|+\frac{C(|R_X|+|R_Y|)}{k}.
$$

The joint law of $(\tau,d)$ is fixed, independent of $k$ and $L$.
Letting $k\to\infty$ proves (S) for the integer weights. Thus the order
is first $L\to\infty$ for each fixed replication count, then
$k\to\infty$, and only then the finite-family separation and compactness.
If $R_X$ is empty, the same lower bound holds without the star limit. $\square$

## The limit measure and the trace bound

**Proposition L (examined within the whole proof).** There is a Radon probability measure
$\nu$ on $\{-1,1\}^{V(G)}$ such that every $v\notin N_0$ with infinite
trace satisfies

$$
 \sum_{u\in T_v}\nu(\sigma_u=\sigma_v)\le C. \tag{L}
$$

*Proof.* Define $\nu_\xi$ on $\{-1,1\}^{V_\xi}$ by recursion, with
$J(\nu_\xi,\xi)$ and $\nu_\zeta$ the marginal of $\nu_\xi$ for $\zeta<\xi$.
Lemma 0 gives $\nu_0$ and Lemma S gives $\nu_{\xi+1}$. At a limit $\lambda$
the consistent finite-coordinate laws of the measures $\nu_\xi$
($\xi<\lambda$) give a Radon measure $\nu_\lambda$ by the product
construction above, with precisely those marginals. For a pattern $P$ over
$N_\lambda$, the finite set $R$ lies in some $N_\xi$ with $\xi<\lambda$,
and $S$ misses $N_\xi$, so $P$ is a pattern over $N_\xi$ and
$\mathbb E_{\nu_\lambda}e_P=\mathbb E_{\nu_\xi}e_P\le C|S|$. The same
construction at the end gives $\nu$ on $\{-1,1\}^{V(G)}$.

Let $v\in X_\xi$. By Lemma S, $\sigma_v=-s_v$ almost surely, where $s_v$
comes from Lemma D for $\nu_\xi$, the marginal of $\nu$. Thus
$\nu(\sigma_u=\sigma_v)=\nu(\sigma_u\ne s_v)$ for each $u\in T_v$,
and (D) is (L).
$\square$

The coordinates $\sigma_u$ of $\nu$ are unit vectors of $L^2(\nu)$, and
$1+\langle\sigma_v,\sigma_u\rangle=2\nu(\sigma_u=\sigma_v)$. So (L) says
that every infinite-trace vertex has trace-star energy at most $2C$. This
resolves the gap recorded in the rooted measure note. There, the
coordinate of a vertex need not equal minus its countably determined
trace sign. Here each layer's infinite-trace coordinates are assigned
exactly that value. The replacement is rigid, because the trace lies in
the earlier model whose coordinates the property $J$ already controls.
The remaining coordinates of the layer are chosen afresh by a coupling.
Neither change
disturbs $J$ at the next model.

## Countable coloring

**Lemma T (examined within the whole proof).** Suppose unit vectors $x_v$ in a real
Hilbert space satisfy $E_v=\sum_{u\in T_v}(1+\langle x_v,x_u\rangle)<\infty$
for every $v\notin N_0$ with infinite trace, and suppose every layer
induces a graph of countable chromatic number. Then $\chi(G)\le\aleph_0$.

*Proof.* Use the countably many classes of the proof of Proposition C:
any two vectors $x,y$ in one class satisfy
$1+\langle x,y\rangle\ge\eta>0$ for a constant $\eta$ of the class. Fix a
class $K$ and let $H_K$ consist of the edges of $G$ between vertices of $K$
in different layers. Well-order the vertices in each layer and place
earlier layers first. A vertex $v\notin N_0$ has its $H_K$-neighbours in
earlier layers inside $T_v\cap K$: finitely many if $T_v$ is finite,
and at most
$E_v/\eta$ otherwise. A vertex of $V_0$ has none. So greedy coloring along
this well-order colors $H_K$ with natural numbers. Color each vertex by its
class, its greedy color in its class, and its color in a fixed countable
coloring of its layer. An edge inside a class joins different layers or
lies in one layer, and the second or the third coordinate separates its
ends. $\square$

*Proof of the theorem.* Induct on $|V(G)|$; countable graphs are trivial.
For uncountable $\kappa$, every layer, including $V_0$, has fewer than
$\kappa$ vertices and is $C$-linear, so it has countable chromatic number
by induction. Proposition L supplies vectors with $E_v\le2C$, and Lemma T
gives $\chi(G)\le\aleph_0$. $\square$

## What the argument uses

The proof uses Lemma F in the replication form above, the rooted measure's
compactness argument for $J(\nu_0,0)$, Proposition C's classes,
the elementary-chain construction, and the probability facts stated
above: the Riesz representation theorem and weak-star compactness,
monotone convergence, Fatou's lemma and finite-dimensional convex
separation. Derived signs are countably determined, marginal constraints
are imposed on the whole old coordinate set, and every rigidity argument
uses only finitely many signs at once.
The quantitative use of $C$-linearity is in Lemma 0; the coloring
induction also uses its inheritance by induced subgraphs. The proof does
not use
Erdős–Hajnal's Corollary 5.6 or Theorem 3.1, Lemma G, or any
hypothesis on $\chi(G)$. The whole-conclusion examination checks the
consumed Hilbert partition of Proposition C and rooted base-law proposition,
as well as every deduction in the composition with Steps 1 to 3. It does not
certify the unused parts of those companion pages.

The mathematical argument is noncomputational. It claims to close CC
directly, and does not prove the finite partitioned vector assertion
(PV). The bounds apply only to traces in preceding models, not to all
finite subgraphs with one hereditary energy coefficient. The argument
therefore does not use or contradict the failed single-representation
proposal. The separate whole-conclusion grade accepts this exact proof
under its stated classical interfaces; it supplies no kernel or external
catalog warrant.

## A uniform bound must exclude finite traces

The bound (L) concerns only vertices with infinite trace. It cannot be
extended to a uniform bound for all vertices outside $N_0$. The following
independent by-product is not used in the candidate theorem.

**Proposition U (author-recorded).** For all $C,K>0$ there is a
$C$-linear graph of size $\aleph_1$ and chromatic number three such that,
for every chain as above, no unit vectors satisfy

$$
 \sum_{u\in R}\bigl(1+\langle x_v,x_u\rangle\bigr)\le K
 \qquad(v\notin N_0,\ R\subseteq T_v\ \text{finite}).
$$

*Construction.* Fix an integer $k\ge4K$ and an odd $\ell\ge5$ with
$k\le C(\ell-1)$. Take a set $V_0'$ of $k$ vertices and, for each
$i<\omega_1$, a petal consisting of disjoint independent parts
$V_1^i,V_2^i,\ldots,V_{\ell-1}^i$ with $|V_1^i|=k$ and
$|V_j^i|=\aleph_1$ for $j\ge2$. Join all pairs between cyclically
consecutive parts of $V_0',V_1^i,\ldots,V_{\ell-1}^i$, for every $i$. Call
the graph a bouquet. It is three-colorable: color $V_0'$ by $2$ and
$V_j^i$ by the parity of $j$.

*Linearity.* Let $F$ be finite and let $n_0,n_1^i,\ldots,n_{\ell-1}^i$ be
the sizes of its intersections with the parts. Call petal $i$ full if
$n_0$ and all its $n_j^i$ are positive. In each full petal delete the edges
between one consecutive pair of parts minimizing the product
$b_i=\min(n_0n_1^i,n_1^in_2^i,\ldots,n_{\ell-1}^in_0)$. What remains is a
union of blow-ups of paths that meet only in $V_0'$, which is bipartite.
Put $s_i=\sum_{j\ge1}n_j^i$. The $(\ell-1)/2$ disjoint consecutive pairs
$(n_1^i,n_2^i),(n_3^i,n_4^i),\ldots$ each have product at least $b_i$, so
$s_i\ge(\ell-1)\sqrt{b_i}$, and $\sqrt{b_i}\le\sqrt{n_0n_1^i}\le k$. Thus
$b_i\le ks_i/(\ell-1)$ and $\beta(F)\le\sum_ib_i\le
k|V(F)|/(\ell-1)\le C|V(F)|$.

*Placement in every chain.* $V_0'$ is the least finite set whose removal
leaves uncountably many components. Removing $V_0'$ leaves the petals; a
finite set missing some $p\in V_0'$ leaves $p$ joined to all but finitely
many whole petals. So $V_0'$ is definable from $G$ and $V_0'\subseteq N_0$.
A petal is definable from any of its vertices together with $V_0'$, as a
component of $G-V_0'$, and so are its parts. Fix a petal $i$ missing $N_0$
and let $\gamma$ be least with $N_\gamma$ meeting it. Then $V_1^i\subseteq
N_\gamma$, and each $U_j=V_j^i\cap N_\gamma$ ($j\ge2$) is infinite, since an
infinite definable set in $N_\gamma$ has infinitely many elements there.
Put $O_j=V_j^i\setminus N_\gamma$, which is nonempty for $j\ge2$. Every
$v\in O_j$ has $T_v\supseteq U_{j-1}\cup U_{j+1}$ when $3\le j\le\ell-2$,
$T_v\supseteq V_1^i\cup U_3$ when $j=2$, and
$T_v\supseteq U_{\ell-2}\cup V_0'$ when $j=\ell-1$. Every $q\in V_1^i$ lies
outside $N_0$ and has $T_q\supseteq V_0'$.

*Contradiction.* Suppose such vectors exist. For even $j$ with
$2\le j\le\ell-3$, take $v\in O_j$ and $v'\in O_{j+2}$. Both bound the energy
of the same infinite set $U_{j+1}$, so for every $\varepsilon>0$ some
$u\in U_{j+1}$ has $1+\langle x_v,x_u\rangle<\varepsilon$ and
$1+\langle x_{v'},x_u\rangle<\varepsilon$, and

$$
 \|x_v-x_{v'}\|\le\|x_v+x_u\|+\|x_u+x_{v'}\|<2\sqrt{2\varepsilon}.
$$

Hence all vertices of $O_2,O_4,\ldots,O_{\ell-1}$ carry one vector $a$;
here $\ell-1$ is even because $\ell$ is odd. Let $m_0,m_1$ be the averages of
the vectors on $V_0',V_1^i$ and put $\delta=K/k\le1/4$. The constraints of a
vertex of $O_2$ on $V_1^i$, of a vertex of $O_{\ell-1}$ on $V_0'$, and of the
vertices of $V_1^i$ on $V_0'$ give

$$
 1+\langle a,m_1\rangle\le\delta,\qquad
 1+\langle a,m_0\rangle\le\delta,\qquad
 1+\langle m_1,m_0\rangle\le\delta.
$$

The first two give $\|a+m_1\|^2\le2\delta$ and $\|a+m_0\|^2\le2\delta$, so
$\|m_0-m_1\|^2\le8\delta$. The last, with
$\|m_0\|,\|m_1\|\ge1-\delta$, gives
$\|m_0-m_1\|^2\ge2(1-\delta)^2+2-2\delta$. For $\delta\le1/4$ the lower
bound is at least $21/8$ and the upper at most $2$. $\square$

The failing constraint is the one at the gate vertices $V_1^i$, whose
traces are finite. Proposition L imposes nothing there: in the bouquet its
vectors may make $V_1^i$ and $V_0'$ agree. So a compactness argument
asking for one uniform bound at every vertex is false. The layered
recursion above avoids it by treating finite-trace vertices as free
coordinates.
