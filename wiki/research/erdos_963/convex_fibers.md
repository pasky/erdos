---
name: research/erdos_963/convex_fibers
title: 'A new convex-geometric route through integer knapsack fibers'
desc: Coherent subsets, an exact vertex-support formulation, small cases, and a still-unproved stronger cardinality bound.
tags: []
sources: []
created: 2026-09-19T01:10:00Z
updated: 2026-09-19T02:15:34Z
---


# A new convex-geometric route through integer knapsack fibers

***

This approach replaces ternary spanning and matching by convex extremality
in integer knapsack fibers. It has not proved the requested bound.
The stronger cardinality assertion below is a conjectural sufficient
condition, not a reformulation already known to be equivalent to the target.

## Coherent subsets and the support parameter

For a finite positive set $D=\{a_1,\ldots,a_k\}$, put $S=\sum_i a_i$ and

$$
F_D=\{u\in\mathbb Z_{\ge0}^k:a\cdot u=S\}.
$$

This set is finite by positivity. Call $D$ **coherent** if
$\mathbf1=(1,\ldots,1)$ is a vertex of $\operatorname{conv}F_D$.
Write $c(P)$ for the maximum size of a coherent subset of $P$.

Coherence implies dissociation. A nonzero ternary relation $\varepsilon$
would make $\mathbf1+\varepsilon$ and $\mathbf1-\varepsilon$ distinct
members of $F_D$ with midpoint $\mathbf1$. Thus $c(P)\le d(P)$.
Coherence is hereditary: a convex decomposition on a subset extends to
one on $D$ by putting coefficient one on the complementary coordinates.

There is an exact, useful interpretation of $c(P)$. For
$P=(a_1,\ldots,a_n)$ and $b\ge0$, define

$$
K_b(P)=\operatorname{conv}
\{u\in\mathbb Z_{\ge0}^n:a\cdot u=b\}.
$$

Then

$$
\boxed{c(P)=
\max_b\max_{u\in\operatorname{Vert}K_b(P)}
|\operatorname{supp}u|.}                                      \tag{1}
$$

If a vertex $u$ has support $D$, any nontrivial convex decomposition
of $\mathbf1_D$ in its restricted fiber can be shifted by
$u-\mathbf1_D$, contradicting vertexhood of $u$. Conversely, if $D$
is coherent, its Boolean vector in the full $P$-fiber remains a vertex:
all outside coordinates are zero, so every term in a proposed convex
decomposition must also have zero outside coordinates.

The new sufficient conjecture is

$$
\boxed{|P|\le2^{c(P)}-1.}                                     \tag{2}
$$

Since $c(P)\le d(P)$, (2) would prove the positive version of Erdős 963.
For this implication it suffices to prove (2) for positive integers:
the established integer reduction preserves dissociation.
No proof of (2), and no counterexample to (2), was obtained.

## What maximal coherence does imply

Let $D$ be coherent, $S=\sum D$, and $p>0$ outside $D$.
If $D\cup\{p\}$ is not coherent, then

$$
S+p\in\mathbb N D,\qquad S-mp\in\mathbb N D
\quad\text{for some integer }m\ge1.                           \tag{3}
$$

Here $\mathbb N D$ includes the zero combination.

Indeed, a nontrivial decomposition of $(\mathbf1,1)$ uses integer
solutions $(u,v)$ of

$$
a\cdot u+pv=S+p,\qquad u,v\ge0.
$$

If all participating $v$ equal one, coherence of $D$ makes the
decomposition trivial. Since their weighted average is one, some
participating $v$ must equal zero and another must be at least two.
These yield (3).

Consequently

$$
p\in\mathbb ZD,\qquad p\le S.                                \tag{4}
$$

Every inclusion-maximal coherent $D\subseteq P$ therefore generates
$\mathbb ZP$. In particular, integer lifts of all of $P$ into
$\mathbb Z^{|D|}$ exist. The resulting homomorphism has saturated
kernel, since its image is torsion-free. These lifts need not be
ternary; the obstruction note gives an explicit example.

A useful special extension follows directly. If $C$ is a coherent
positive integer set, $q\ge2$, and $\gcd(p,q)=1$, then
$qC\cup\{p\}$ is coherent. In its total-sum fiber the coefficient
of $p$ is congruent to one modulo $q$, hence is at least one.
A convex decomposition of the all-ones vector forces that coefficient
to be one in every term, reducing to coherence of $C$.

## Proved small coherent cases

Every distinct positive pair is coherent. In the fiber of $a+b$,
where $a<b$, the coefficient of $b$ is at most one. Maximizing that
coefficient selects the all-ones point.

Every dissociated positive triple is coherent. Write $a<b<c$.
A representation of $a+b+c$ using $c$ at least twice would leave
$a+b-c<a$; this is possible only if the remainder is zero, namely
$c=a+b$, which dissociation excludes. More than two copies leave a
negative remainder. Thus the $c$-coordinate is at most one.
Maximizing it reduces to the coherent pair $\{a,b\}$.

Every dissociated four-set of positive odd integers is coherent.
Write $a<b<c<M$ and $S=a+b+c+M$.
If $M>a+b+c$, its fiber coordinate is at most one, and maximizing it
reduces to the triple case. Equality is excluded by dissociation.
Otherwise $S>2M$. All fiber points have even total coefficient sum,
and that sum cannot be two. Minimize it to select the nonempty
degree-four slice. There the $M$-coordinate cannot be three or four:
$3M+a>S$. If it were two, the other two terms would sum to

$$
a+b+c-M<a+b.
$$

They must both equal $a$, forcing $a+M=b+c$, again a contradiction.
Thus in this slice the $M$-coordinate is at most one. Maximizing it
and then exposing the remaining coherent triple selects $\mathbf1$.
Successive exposed faces are faces of the original finite polytope,
so this proves coherence.

The previously proved fact that five positive odd integers contain
a dissociated four-set consequently gives a coherent four-set.
Thus positive odd sets of coherent dimensions one, two, and three
have sizes at most one, two, and four, respectively.

The $q=2$ extension above lets one adjoin representatives of successive
lower valuation layers to a coherent subset of a later layer. The
existing valuation-layer counting argument therefore applies to $c$
as well, giving the new special case for positive integer $P$:

$$
\boxed{c(P)\le3\quad\Longrightarrow\quad |P|\le2^{c(P)}-1.}     \tag{5}
$$

This establishes the stronger coherent bound in these small dimensions;
it does not improve the existing unrestricted dissociation bound.

## An exact extension problem, rather than an exchange assumption

Adjoining $p$ is equivalent to an integer-hull question in $k=|D|$
variables:

$$
K_p=\operatorname{conv}\left\{
u\in\mathbb Z_{\ge0}^k:
a\cdot u\le S+p,\quad a\cdot u-S\in p\mathbb Z
\right\}.
$$

The affine bijection

$$
u\longmapsto
\left(u,\frac{S+p-a\cdot u}{p}\right)
$$

shows that $D\cup\{p\}$ is coherent exactly when $\mathbf1$ is a
vertex of $K_p$.

Equivalently, let $w$ range over costs strictly exposing $\mathbf1$
in $F_D$, and set

$$
L_p(w)=
\max_{\substack{v\ge2,\ u\in\mathbb Z_{\ge0}^k\\
                 a\cdot u+pv=S+p}}
\frac{w\cdot(\mathbf1-u)}{v-1},
\qquad
U_p(w)=
\min_{\substack{u\in\mathbb Z_{\ge0}^k\\a\cdot u=S+p}}
w\cdot(u-\mathbf1).
$$

Empty extrema mean $-\infty$ and $+\infty$, respectively.
Then

$$
D\cup\{p\}\text{ coherent}
\quad\Longleftrightarrow\quad
\exists w:\ L_p(w)<U_p(w).                                   \tag{6}
$$

For such a $w$, choose the cost of the new variable strictly between
these two bounds. Conversely, any exposing cost for the extension
restricts to such a $w$. The inequalities simply compare the candidate
with fiber points having new coordinate zero, one, or at least two.

## The geometric opportunity and exact gap

An empty lattice polytope, meaning one whose only lattice points are
its vertices, has at most $2^k$ vertices in $\mathbb R^k$:
two vertices of the same parity have an integer midpoint that is
not a vertex. Thus a construction, from $P$ and a maximum coherent
$D$, of an empty lattice polytope of dimension at most $c(P)$ with
at least $|P|+1$ vertices would prove (2). Integer lifts exist by (4),
but convex position and emptiness in dimension $c(P)$ have not been
established in general.

The [[research/erdos_963/empty_lift_quotient|one-step quotient theorem]]
constructs an empty lift in dimension $|P|-1$ whenever $P$ is noncoherent,
retaining every prescribed height and all $|P|+1$ vertices. It even has a
unimodular star triangulation. This proves the proposed lift statement when
$c(P)=|P|-1$, but no iteration to arbitrary $c(P)$ is justified. The
[[research/erdos_963/global_lift_gap|new exact obstruction]] shows that a valid
first quotient can be a local minimum of dimension greater than $c(P)$, even
with normality and a unimodular star triangulation. A global choice or
replacement of relation spaces is therefore necessary. The
[[research/erdos_963/affine_coherence|affine-coherence argument]] does give a
universal near-logarithmic bound in $c(P)$ itself.

Two checked sources show relevant mechanisms, not an application:
[Dash–Günlük–Wolsey, *The continuous knapsack set*, Lemma 2.8 and Theorem
2.9](https://optimization-online.org/wp-content/uploads/2014/02/4227.pdf) use an
empty projected lattice polytope to bound the number of distinct continuous
coefficients of a mixed-integer facet. The required facet has not been
constructed here. [Hoşten–Maclagan, *The Vertex Ideal of a Lattice*, Proposition
3.3 and Theorem 3.6](https://arxiv.org/html/math/0012197) give a $2^k-1$
codimension bound for associated primes of a rank-$k$ lattice's vertex ideal,
characterized by inequalities essential to integer-hull vertexhood. The natural
kernel lattice has the wrong rank, and the proposed canonical image-lattice
construction is explicitly refuted in the obstruction note.

The next substantive step is a global construction controlling the simultaneous
failures of (6), or a counterexample to the stronger coherent bound (2). A
counterexample to (2) would only reject this stronger route; it would not by
itself disprove Erdős 963. See
[[research/erdos_963/convex_route_obstructions|the exact obstructions]] before
using ternary spanning, largest-element exchange, or canonical image lattices.

## Boolean lifting in the zero-defect vector case

There is a proved boundary case of the stronger binary-lift proposal.
Let $A$ be a rational rank-$r$ vector configuration admitting a
strictly positive linear functional. Define $c(A)$ using its vector
integer fibers. If $c(A)=r$, its row space has a basis of Boolean
vectors. Thus every rational scalar height vector on $A$ is contained
in the subset-sum set of $r$ external rational generators.

First, every primitive circuit must have all its nonzero coefficients
equal to $1$ or $-1$. Otherwise the integer fiber of the all-ones
point on its support lies on a line, with integer parameters
along the primitive circuit. A coefficient of absolute value
greater than one prevents a nonzero parameter in one of the two
directions. The all-ones point is therefore an endpoint (possibly
the only point), hence
coherent. Extend the circuit support by columns independent modulo
its span. The added coefficients are fixed in every fiber point,
so coherence is preserved, giving a coherent $(r+1)$-set.
This contradicts $c(A)=r$.

Choose a column basis and use it as coordinates, obtaining
$V=[I\mid C]$. Fundamental circuits make $C$ integral with entries
in $\{-1,0,1\}$. Exchanging adjacent column bases shows that every
nonzero maximal minor is $\pm1$, since each exchange coefficient
is a circuit coefficient.

The polytope

$$
K=\{t\in\mathbb R^r:0\le V^{\mathsf T}t\le1\}
$$

is bounded by its identity-column inequalities. A sufficiently small
positive-height functional lies in its interior, so it is
full-dimensional. At each vertex, $r$ independent tight inequalities
have determinant $\pm1$; Cramer's rule gives an integer vertex.
Consequently all vertex images $V^{\mathsf T}t$ are Boolean.
They span the row space, since the vertices span the full-dimensional
polytope $K$. Choose $r$ independent images.

This case also forces $d(A)=r$, because every rational circuit is
ternary. It therefore does not extend the existing zero-defect
dissociation bound to integer configurations of positive defect.
Neither the general inequality between Boolean covering dimension
and $c(A)$ nor a global quotient replacement theorem was established.
