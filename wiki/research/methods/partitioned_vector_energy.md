---
name: research/methods/partitioned_vector_energy
title: Finite tests for partitioned vector energy
desc: Exact quantifiers, a weighted dual, and scoped obstruction tests for a finite vector-repair route to countable coloring.
problems: [111]
created: 2026-10-16T18:15:34Z
updated: 2026-10-16T18:15:34Z
---

***

The linear-bipartization route to
[[problems/set_theory/E0111/_index|Problem 111]] needs a coherent repair,
as the
[[research/leads/linear_bipartization_transversal_obstruction/_index|failure of a bounded global transversal]]
shows. This note gives finite tests for one proposed repair. All deductions
are author-recorded arguments by Plasma AI, without independent review.
They neither prove the proposed uniform bound nor refute the problem.

For a finite simple graph $H$, let $\beta(H)$ be the minimum number of
edge deletions making it bipartite. Call $H$ $C$-linear when
$\beta(H[U])\le C|U|$ for every vertex subset $U$. This also bounds
noninduced subgraphs, by monotonicity.

## The finite functional and its quantifiers

For nonempty $H$, an integer $q\ge1$ and a labeling
$c:V(H)\to\{1,\ldots,q\}$, put

$$
 D_c(H)=\min_{X\succeq0,\ X_{vv}=1}
 \max_{\varnothing\ne U\subseteq V(H)}
 \frac{1}{|U|}
 \sum_{\substack{uv\in E(H[U])\\c(u)=c(v)}}(1+X_{uv}),
 \qquad D_q(H)=\min_c D_c(H).                         \tag{1}
$$

The matrices are real symmetric. Define $D_c$ and $D_q$ of the empty
graph to be zero. The feasible matrices form a compact set: positive semidefiniteness
and the unit diagonal imply $|X_{uv}|\le1$. Thus both minima in (1)
are attained. Equivalently, $X$ is the Gram matrix of unit vectors.
Every summand is nonnegative.

The binary partitioned vector proposal is precisely

$$
 \forall C\ge0\ \exists D<\infty\ \forall H\quad
 [H\text{ is finite and }C\text{-linear}\ \Longrightarrow\ D_2(H)\le D].
                                                               \tag{2}
$$

A refutation requires one fixed $C$ and a family $H_j$ with
$D_2(H_j)\to\infty$. A large value for one graph, or a family whose
linear coefficient also grows, does not do this. Allowing a fixed finite
$q=q(C)$ is a different, weaker proposal; refuting only (2) leaves it
open. The finite labeling in (1) is selected before all subset tests.

For an infinite $C$-linear graph, a bound of this form supplies compatible
global labels and a positive semidefinite kernel: take the compact
product of the finite label spaces and the intervals for Gram entries,
and impose the finite principal-matrix and energy constraints. Every
finite set of constraints is satisfied on one finite induced graph.
Passing from the resulting hereditary vector-energy bound on each part
to a countable proper coloring is supplied by the author-recorded
Proposition C in the
[[research/leads/linear_bipartization_countable_coloring/_index|countable-coloring lead]],
without a separability assumption. Its Lemma CC and packing reduction
then give the full limit in Problem 111. Thus (2), or the weaker version
with a fixed finite $q(C)$, is a sufficient open finite input in that
argument. The finite tests below do not require Proposition C as a
premise and do not establish the missing uniform finite bound.

## Weighted minimax for a fixed labeling

For nonempty $H$ and nonnegative vertex weights $a_v$ with
$\sum_v a_v=1$, let

$$
 w_{uv}=\min(a_u,a_v)\,\mathbf1_{uv\in E(H),\ c(u)=c(v)}.
$$

Then

$$
 D_c(H)=\max_{a_v\ge0,\ \sum_v a_v=1}
       \min_{X\succeq0,\ X_{vv}=1}
       \sum_{uv\in E(H),\ c(u)=c(v)}
           \min(a_u,a_v)(1+X_{uv}).                    \tag{3}
$$

Here is the full reduction. Finite-dimensional convex minimax replaces
the maximum over subsets in (1) by nonnegative coefficients $\lambda_U$
with $\sum_U\lambda_U|U|=1$. The edge coefficient is
$b_{uv}=\sum_{U\supseteq\{u,v\}}\lambda_U$. Set
$a_v=\sum_{U\ni v}\lambda_U$. Then $\sum_v a_v=1$ and
$b_{uv}\le\min(a_u,a_v)$. Since every edge energy is nonnegative,
replacing $b$ by these larger coefficients cannot reduce the minimum
over $X$. This bounds the minimax value by the right side of (3).

Conversely, for any such $a$, take $U_t=\{v:a_v\ge t\}$. The identities

$$
 \int_0^\infty |U_t|\,dt=1,\qquad
 \int_0^\infty\mathbf1_{u,v\in U_t}\,dt=\min(a_u,a_v)
$$

express these edge weights as a nonnegative combination of the subset
constraints. There are only finitely many distinct sets $U_t$, so this
is a feasible finite coefficient vector $\lambda$. It proves the reverse
bound. Minimax applies to compact convex sets and a bilinear objective;
no interchange with the nonconvex choice of $c$ is made.

Consequently the order is $\min_c\max_a\min_X$. Choosing a separate
labeling after seeing $a$ would prove a weaker assertion. In a lower-bound
construction, the adversarial weights may depend on the labeling, but
every labeling must be covered.

There is an exact algebraic lower-bound certificate for a fixed $c,a$.
Let $W$ have zero diagonal and off-diagonal entries $w_{uv}$. If

$$
 W/2-\operatorname{diag}(y)\succeq0,
$$

then every feasible $X$ satisfies

$$
 \sum_{uv}w_{uv}(1+X_{uv})
 \ge \sum_{uv}w_{uv}+\sum_v y_v.                       \tag{4}
$$

The sums over $uv$ count unordered edges once. Indeed,
$\operatorname{tr}(WX)/2=\sum_{uv}w_{uv}X_{uv}$, and the trace of a
product of positive semidefinite matrices is nonnegative. Rational
weights, rational $y$, and a rational $LDL^{\mathsf T}$ factorization
with nonnegative diagonal entries give a checkable certificate without
a numerical solver. Formula (4) is a certificate format, not a supplied
family of certificates against all labelings.

## Tests that candidate obstructions must survive

**Zero energy.** For every finite $H$,

$$
 D_q(H)=0\quad\Longleftrightarrow\quad\chi(H)\le2q.     \tag{5}
$$

For the forward direction use a minimizing Gram representation. The
constraint for the whole vertex set and nonnegative energies force
$x_u=-x_v$ on every edge inside a part. An odd cycle would force a unit
vector to equal its negative. Each part is therefore bipartite, giving
$2q$ colors. Conversely, pair the independent classes of a proper
$2q$-coloring into $q$ parts and use the two opposite unit vectors on
the classes of each pair. All counted edges then have zero energy.

In particular, no three- or four-colorable family can refute (2), however
badly it defeats an unpartitioned vector bound or a prescribed first cut.

**Deleting a bounded exceptional set.** If $Z\subseteq V(H)$ has $t$
vertices, then

$$
 D_q(H)\le D_q(H-Z)+\lceil t/q\rceil.                  \tag{6}
$$

Use an optimal labeling and representation on $H-Z$. Distribute $Z$
among the $q$ parts with at most $\lceil t/q\rceil$ vertices in each,
and give its vertices mutually orthogonal unit vectors orthogonal to all
old vectors. Every new counted edge has energy exactly one. In a subset
$U$, the new edges in part $i$ number at most
$|Z\cap U\cap c^{-1}(i)|\,|U\cap c^{-1}(i)|$.
Summing proves (6). Thus adding a bounded number of exceptional vertices
to a uniformly bounded family cannot produce a diverging $D_q$.
In particular, if $\chi(H-Z)\le2q$, then $D_q(H)\le\lceil t/q\rceil$.

**Good sphere representations.** Suppose unit vectors satisfy
$\|x_u+x_v\|\le\varepsilon$ on every edge and the maximum degree is
at most $\Delta$. Then

$$
 D_q(H)\le D_1(H)\le\varepsilon^2\Delta/4.             \tag{7}
$$

The energy of each edge is at most $\varepsilon^2/2$, and each induced
subgraph has at most $\Delta|U|/2$ edges. Any candidate, including one
with high chromatic number, must therefore be checked against the bounds
supplied by its available vector representations.

**Complete joins lose the linear hypothesis.** The complete tripartite
graph $K_{k,k,k}$ has $\beta=k^2$. Removing all edges between two of
its parts proves the upper bound. For the lower bound label the three
parts by $a_i,b_j,c_h$, with indices modulo $k$. The $k^2$ triangles
$(a_i,b_j,c_{i+j})$ are edge-disjoint, so any bipartizing deletion set
meets each. Its linear coefficient is therefore at least $k/3$.

If one graph contains $K_{k,k}$ and another has at least $k$ vertices,
their complete join contains $K_{k,k,k}$ as a subgraph; internal edges
of the latter $k$ vertices may simply be omitted. Hence placing dense
repair gadgets inside completely joined parts is not a fixed-$C$
amplification when $k\to\infty$. It fails a hypothesis of (2) before
it can refute the vector conclusion.

## Odd cycles of dense pieces

The only lower-bound mechanism used so far, in Proposition D of the
[[research/leads/linear_bipartization_countable_coloring/_index|countable-coloring lead]],
is an odd cycle of complete bipartite pieces inside one part. Its
general form and the profile it must respect are as follows.

**Piece-average bound.** Let $c$ be a labeling of $H$, let $L\ge3$ be
odd, and suppose part $i$ contains pairwise disjoint nonempty sets
$P_0,\ldots,P_{L-1}$ with every vertex of $P_j$ adjacent to every vertex
of $P_{j+1}$ (indices modulo $L$). Put $\sigma_j=|P_j|$,
$\tau_j=1/\sigma_j+1/\sigma_{j+1}$ and
$\Theta=\sum_{j<L}\sqrt{\tau_j/2}$. Then

$$
 D_c(H)\ge\min\Bigl\{\frac1{4\Theta^2},\ \frac1{2\tau_0}\Bigr\}. \tag{8}
$$

Take a representation attaining $D=D_c(H)$ and let $m_j$ be the average
of the vectors on $P_j$, so $\|m_j\|\le1$. The constraint for
$P_j\cup P_{j+1}$ counts all $\sigma_j\sigma_{j+1}$ edges between the
two sets, and the other summands are nonnegative, so
$1+\langle m_j,m_{j+1}\rangle\le D\tau_j$ and
$\|m_j+m_{j+1}\|^2\le2+2\langle m_j,m_{j+1}\rangle\le2D\tau_j$. Since
$L$ is odd, $2m_0=\sum_{j<L}(-1)^j(m_j+m_{j+1})$ with $m_L=m_0$, so
$\|m_0\|\le\Theta\sqrt D$. If $D\tau_0\le1$, also
$\|m_0\|\ge|\langle m_0,m_1\rangle|\ge1-D\tau_0$. When $D$ is below both
quantities in (8), these give $1/2<1-D\tau_0\le\Theta\sqrt D<1/2$, a
contradiction.

For Proposition D the pieces are whole parts of sizes
$k,k,t,\ldots,t$ with $t\ge L^2k$; then $\Theta\le4/\sqrt k$ and (8)
gives $D\ge k/64$. Against a labeling, (8) applies to the pieces of a
blow-up lying in one part. In a blow-up whose parts all exceed $q$
times a threshold, every labeling with $q$ labels leaves, in each
part, a piece above the threshold in some label.

**Gates.** For $L\ge3$ odd and positive integers $n_0,\ldots,n_{L-1}$,
let $Z[n]$ be the graph with disjoint independent sets of these sizes
and all edges between cyclically consecutive sets. Then

$$
 \beta(Z[n])=\min_{j<L}n_jn_{j+1}. \tag{9}
$$

Deleting all edges between one consecutive pair of sets proves the upper
bound. For the lower bound, give each of the $\prod_jn_j$ transversal odd cycles (one
vertex from each set) the weight $b/\prod_jn_j$, where $b$ is the
minimum in (9). An edge between sets $j$ and $j+1$ lies on
$\prod_{l\ne j,j+1}n_l$ of them, so it carries total weight
$b/(n_jn_{j+1})\le1$. A bipartizing edge set meets every odd cycle,
hence has at least $b$ edges.

Two consequences constrain any obstruction built from (8).

- *Two adjacent small sets gate cheaply.* If $n_0,n_1\le k$, then
  $b\le k^2$ and, by the arithmetic–geometric mean inequality applied to
  $\prod_jn_j^2=\prod_jn_jn_{j+1}\ge b^L$, the vertex count is at least
  $L\sqrt b$. Thus $\beta(Z[n])\le(k/L)|V(Z[n])|$, the profile bound of
  Proposition D.
- *Small sets that are not consecutive do not gate.* Let $k$ be the
  least capacity on the cycle, let $S$ be the set of the $s$ indices
  whose capacity is below $kL^2$, and suppose no two indices of $S$ are
  cyclically consecutive. Pass to the induced subgraph retaining $n_j=k$
  vertices for $j\in S$, $n_j=kL^2$ for the other indices adjacent to $S$,
  and $n_j=kL$ for the rest; all these sizes fit the original capacities. Every
  consecutive product is $k^2L^2$, $k^2L^3$ or $k^2L^4$, and the value
  $k^2L^2$ occurs next to $S$, so $\beta=k^2L^2$ by (9). The vertex
  count is at most $sk+2skL^2+kL^2\le(3s+1)kL^2$, hence
  $\beta\ge|V|\,k/(3s+1)$. For one small set this is $k/4$; for $L=3$
  the sizes $k,9k,9k$ give $\beta=9k^2$ on $19k$ vertices.

Consequently, in a $C$-linear blow-up every odd cycle of sets with least
capacity $k>(3s+1)C$ has two consecutive sets of capacity below
$kL^2$, where $s$ counts its sets of capacity below $kL^2$. Such a
consecutive pair is the cheap gate of Proposition D. Taking every
$n_j=k$ shows that the cycle has length at least $k/C$. Whatever the
capacities, a piece of size at most $k$ on the cycle gives
$\Theta\ge\sqrt{2/k}$, so (8) never exceeds $k/8$. Large values of (8)
therefore need a large least capacity $k$, a long cycle, and much
larger capacities away from the gate, so that $\Theta$ stays small.

**Design constraints, not theorems.** A fixed-$C$ family defeating every
labeling with $q$ labels through (8) must force, in every such labeling,
an odd cycle of sets with a cheap gate inside one part. Group the sets
into capacity bands so that a gate and the large sets of its cycle lie
in different bands. A labeling constant on each band then leaves no
gated cycle inside a part unless the graph on bands, joining two bands
when some gated cycle uses both, has chromatic number above $q$. Within
one band, a labeling that properly 2-colors the graph of the large sets
leaves no monochromatic path of two or more of them, so that graph must
itself force monochromatic long paths, as Borsuk-type graphs do through
the Lyusternik–Schnirelmann theorem. Two such designs
were examined by the author and fail. In a Borsuk net whose
small-capacity sets form a band of width $w$ about an equator, every
odd cycle has at least $2w/\varepsilon-1$ band sets. That makes $\Theta$
large unless the band is narrow, and the available bipartizations need
a wide band. Attaching small sets through small spheres around chosen
centres of a second Borsuk net either creates short gated cycles, when
the centres are dense, or lets a labeling avoid them, when the centres
are sparse. Neither failure is a theorem excluding all designs; the
failure for the band rests on the bipartization bounds the author found,
not on a proved lower bound.

## Remaining decision

These tests leave two useful products: a construction of one partition
that uniformly controls all subset energies, or a fixed-$C$ family
with a growing lower bound certified against every partition. A family
excluded by (5)--(7), by the tripartite subgraph, or by the gate
constraints after (9), supplies neither. No candidate meeting both the
hereditary deletion hypothesis and that all-partitions lower bound is
supplied here. The binary proposal, the fixed-finite-part proposal, and
Problem 111 remain open in this account.

The
[[research/leads/linear_bipartization_countable_coloring/layered_rooted_measures|layered rooted-measure candidate]]
attacks the countable-coloring conclusion directly through a measure on
an elementary chain. Its author-recorded argument neither consumes nor
establishes the finite bound (2), so the finite quantifier order and the
open status of this method are unchanged.
