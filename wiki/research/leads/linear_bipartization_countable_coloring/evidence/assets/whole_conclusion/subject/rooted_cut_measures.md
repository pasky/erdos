[cut]

# Compatible measures for abundant rooted extensions

The target, conventions, Lemma F and Proposition C are in the
[[research/leads/linear_bipartization_countable_coloring/_index|canonical proof sketch]].
[cut] They strengthen the
replication interface, but do not close CC or PV.

## One measure for all abundant patterns

Let $G$ be $C$-linear. A finite rooted pattern $P$ consists of a finite root
set $R\subseteq V(G)$, a disjoint finite set $S$ of new positions, and
prescribed edges on $R\cup S$. Call it abundant if $G$ realizes arbitrarily
many copies whose new vertices are pairwise disjoint, fixing every root.
Only prescribed edges are used; the copies need not be induced. For a root
sign assignment $\tau$, put

$$
 e_P(\tau)=\min_{\eta\in\{-1,1\}^S}
 \bigl|\{uv\in E(P):\{u,v\}\cap S\ne\varnothing,
       \ (\tau\cup\eta)(u)=(\tau\cup\eta)(v)\}\bigr|.
$$

Edges having both endpoints in $R$ are omitted from this cost.

**Proposition.** There is a probability measure $\mu$ on
$\{-1,1\}^{V(G)}$ such that, for every abundant $P$,

$$
 \mathbb E_\mu e_P(\sigma|_R)\le C|S|. \tag{3}
$$

**Proof.** Fix finitely many abundant patterns $P_i$, with root union $R$,
and nonnegative integer multiplicities $a_i$. Realize $ka_i$ copies of each
pattern with all new vertices mutually disjoint and outside $R$.
Abundance allows avoidance of any finite set, so the choices can be made
successively, even when the patterns have different roots. Keep only the
prescribed edges touching new vertices. Linearity of this finite subgraph
gives

$$
 k\min_\tau\sum_i a_i e_{P_i}(\tau)
 \le C|R|+kC\sum_i a_i|S_i|.
$$

Let $k\to\infty$, then use homogeneity and rational approximation. The
same inequality without $C|R|$ holds for all nonnegative real weights.
Finite convex separation therefore gives a distribution on the finitely
many root assignments with all the expected costs at most $C|S_i|$.
Otherwise a nonnegative separating linear combination of these costs
would contradict the weighted inequality.

Each $e_P$ is a continuous finite-coordinate function on the compact
product $\{-1,1\}^{V(G)}$. The probability measures on that product form
a weak-star compact space, and the inequalities (3) are closed conditions.
The finite-family result gives the finite intersection property, proving
the proposition for all patterns at once. No countability of $V(G)$ or
separability of the probability space is required.

## Infinite traces force derived signs

Let $M$ be a countable elementary submodel containing $G$ and its relevant
parameters. Write

$$
 X_M=\{x\in V(G)\setminus M:|N(x)\cap M|=\aleph_0\}.
$$

Lemma F makes every finite pattern on roots in $M$ and new positions
outside $M$ abundant. For $x\in X_M$, apply (3) to stars with successively
larger finite root sets exhausting $N(x)\cap M$. Their extension costs
are the smaller of the two root-color counts. Monotone convergence shows
that, almost surely, one sign occurs only finitely often on this trace.
Let $s_x$ be the other, infinite-majority sign. This is a measurable sign
variable, defined arbitrarily on the exceptional null set, with

$$
 \mathbb E_\mu b_x\le C,
 \qquad
 b_x=|\{u\in N(x)\cap M:\sigma_u\ne s_x\}|.
 \tag{4}
$$

The sign is independent, modulo null sets, of the chosen exhaustion.
Equivalently,
$\sum_{u\in N(x)\cap M}\|\sigma_u-s_x\|_{L^2(\mu)}^2\le4C$.

More strongly, for every finite $A\subseteq X_M$,

$$
 \mathbb E_\mu\left[
    \sum_{x\in A}b_x+
    \sum_{xy\in E(G[A])}\mathbf1_{s_x=s_y}
 \right]\le C|A|. \tag{5}
$$

To prove this, exhaust the traces of all $x\in A$ simultaneously by finite
root sets and include the edges of $G[A]$ in each pattern. The minimum
extension costs increase with the exhaustion and have expectations at
most $C|A|$. Their limit is finite almost surely. Any extension that gives
some $x$ its trace-majority sign has a cost tending to infinity. Thus the
eventual minimizing assignment gives every $x$ the opposite sign, and its
limiting cost is exactly the expression inside (5). Another application
of monotone convergence proves the assertion.

The unit vectors $s_x\in L^2(\mu)$ consequently satisfy

$$
 \sum_{xy\in E(G[A])}(1+\langle s_x,s_y\rangle)\le2C|A|.
$$

Proposition C then countably colors $G[X_M]$. This conclusion alone also
follows from the finite-root common-neighborhood argument. The additional
content here is the single measure and the boundary budget (5).

## Exact remaining compatibility gap

The minimum in $e_P$ is taken after the root coloring is known. Formula
(3) does not bound the cost of the actual coordinate signs $\sigma_x$ on
the new vertices. Formula (5) instead uses derived signs $s_x$, and these
need not equal $-\sigma_x$. When the elementary model changes, its trace
can change too. For nested countable models $M\subseteq N$, if $x$ is
outside $N$ and its trace in $M$ is infinite, the two derived signs for
this same measure agree almost surely: the infinite majority in the
smaller trace persists in the larger trace, whose minority is finite.
This does not identify either derived sign with $-\sigma_x$ when $x$
enters a later model.

Thus the construction does not give one representation of all vertices
with hereditary energy bounded by $2C$, and it supplies no partition for
PV. A closing argument must control the compatibility of these derived
repairs across models, or produce the fixed finite partition before the
weights in PV. Exchanging the expected minimum with the cost of the
coordinate signs would be an unsupported strengthening. The only
compactness used above is for the stated extension-cost inequalities.

The
[[research/leads/linear_bipartization_countable_coloring/layered_rooted_measures|layered measure argument]]
proposes a different, compatible family of measures along an elementary
chain. It preserves each old marginal, assigns infinite-trace vertices
the opposite of their trace signs, and chooses the finite-trace
coordinates by a coupling that retains all future rooted inequalities.
That is a [cut] candidate proof of CC. It claims only a bound on each infinite earlier trace, not a
single hereditary energy coefficient on every finite subgraph, and it
does not settle PV.
