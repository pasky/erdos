---
name: research/erdos_963/convex_route_obstructions
title: 'Exact limits of the new convex, topological, and spectral approaches'
desc: Verified obstructions to coherence extraction, coherent exchange, canonical lattice lifts, and cube-supported spectral counting.
tags: []
sources: []
created: 2026-09-19T01:10:00Z
updated: 2026-09-19T03:52:14Z
---


# Exact limits of the new convex, topological, and spectral approaches

***

None of these examples is a counterexample to Erdős 963.
Coherence and the new geometric proposal are defined in
[[research/erdos_963/convex_fibers|the convex-fiber note]].

## Dissociation is weaker than coherence

The set $D=(3,5,6,7)$ has the distinct subset sums

$$
0,3,5,6,7,8,9,10,11,12,13,14,15,16,18,21.
$$

But in its weight-$21$ fiber,

$$
\mathbf1=\tfrac13\bigl((0,0,0,3)+(1,0,3,0)+(2,3,0,0)\bigr).
$$

Thus $\mathbf1$ is not a vertex. A dissociated cube excludes two-point
midpoint decompositions, not convex decompositions with three or more
terms. One cannot replace maximum dissociation by convex extremality
without proving a stronger extraction theorem.

## Maximum coherent sets need not ternary-span

The set $P=(2,5,8,9)$ has the distinct subset sums

$$
0,2,5,7,8,9,10,11,13,14,15,16,17,19,22,24.
$$

Nevertheless,

$$
\mathbf1=\tfrac13\bigl((3,0,0,2)+(0,3,0,1)+(0,0,3,0)\bigr)
$$

in its weight-$24$ fiber. Every triple is coherent by the proved
triple lemma, so $c(P)=3<d(P)=4$. Since $P$ is dissociated, the
omitted element lies outside the ternary span of every maximum
coherent triple. Integer generation, proved in the main note, is
strictly weaker than ternary spanning.

## Largest-element exchange fails even for coherent sets

Let $D=(4,7,8,9)$ and append $12$. The weight-$28$ fiber of $D$,
apart from $\mathbf1$, consists of

$$
(0,4,0,0),(1,0,3,0),(3,0,2,0),(3,1,0,1),(5,0,1,0),(7,0,0,0).
$$

This list follows by considering the coefficient of $9$, which can
only be zero or one. The cost $(1,0,0,-3)$ is $-2$ at $\mathbf1$
and nonnegative at all six alternatives. Hence $D$ is coherent.

Every four-set containing $12$ is noncoherent. With coordinates in
the indicated order, the following are exact convex decompositions
within the appropriate total-sum fiber:

| Set | Decomposition of $\mathbf1$ |
|---|---|
| $(4,7,8,12)$ | $\frac12(0,1,0,2)+\frac14(0,1,3,0)+\frac14(4,1,1,0)$ |
| $(4,7,9,12)$ | $\frac12(0,2,2,0)+\frac12(2,0,0,2)$ |
| $(4,8,9,12)$ | $\frac12(0,0,1,2)+\frac14(0,3,1,0)+\frac14(4,1,1,0)$ |
| $(7,8,9,12)$ | $\frac14[(0,0,0,3)+(0,0,4,0)+(0,3,0,1)+(4,1,0,0)]$ |

Their fiber weights are $31,32,33,36$, respectively. Heredity also
excludes coherence of the full five-set. Its coherent dimension is
four, but no maximum coherent subset contains its largest element.

## Deleting the largest coherent element need not give modular dissociation

Take the coherent $C=\{4,7,8,9\}$ and put

$$
D=3C\cup\{28\}=\{12,21,24,27,28\}.
$$

In the weight-$112$ fiber, the coefficient of $28$ is congruent to
one modulo three, hence is at least one. Minimizing that coefficient
and then exposing the old $C$-fiber proves coherence of $D$.
But

$$
12+21+24+27=84=3\cdot28.
$$

Thus $D\setminus\{28\}$ is not dissociated modulo $28$.

## Canonical image lattices do not supply an essential inequality system

For $P=\{1,2,3\}$ and maximum dissociated $D=\{1,2\}$, the unique
ternary representation matrix has rows

$$
V=\begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix}.
$$

The other maximum choices give $e_1,e_2,-e_1+e_2$, up to row order.
All these matrices are totally unimodular.

For any system $Vz\le u$ with the origin feasible, replace $u$ by its
integer floor without changing the feasible integer points. The
resulting polyhedron is integral. Hence the origin is an integer-hull
vertex exactly when it is an ordinary vertex. Two independent tight
rows witness this, so the third row is inessential.

Consequently no maximum $D$, canonical ternary lifts, or right-hand
side makes all three rows essential to origin vertexhood. The
associated-prime construction proposed in the main note is false in
this form, not merely unproved. Noncanonical integer lifts or a
different polyhedral construction would be needed.

## Ordinary cube topology discards essential arithmetic information

For actual positive weights, every nonextreme level section of the
real cube is a convex polytope of dimension $n-1$, hence a ball.
Its ordinary homotopy type does not distinguish generic weights
from weights with many subset-sum collisions.

Even strict coordinate monotonicity, antipodal symmetry, and distinct
singleton values together are insufficient without affine additivity.
For arbitrary $n\ge3$, let $m(S)=\max S$, with $m(\varnothing)=0$, and
choose $0<\varepsilon<1/(4n)$. On cube vertices define

$$
f(S)=|S|+\varepsilon\bigl(m(S)-m(S^c)+n\bigr).
$$

This is strictly increasing along edges, satisfies $f(\varnothing)=0$
and
$f(S)+f(S^c)=n+2\varepsilon n$, and has distinct singleton values.
Its perturbation range is less than $1/2$, so different cardinality
layers have different values.

Every four-coordinate face has a collision. If its free coordinates
are $i_1<i_2<i_3<i_4$ and its fixed base is $B$, the two subsets

$$
B\cup\{i_4,i_1\},\qquad B\cup\{i_4,i_2\}
$$

have equal sizes and maxima, and their complements have equal maxima
because $i_3$ remains outside both. The face on the last three
coordinates is vertex-injective: the values of
$m(S)-m(S^c)$ within its singleton layer are $-2,-1,1$, and within
its pair layer are $-1,1,2$. Thus the largest injective coordinate-face
dimension is exactly three for arbitrarily large $n$.
The multilinear extension retains monotonicity and the antipodal
identity, but it is not affine. This rules out arguments using only
those weakened geometric features.

## Spectral mass on maximum subset-sum cubes is also insufficient

Let $P=\{3,4,5,6\}$, with $d(P)=3$. Every triple is dissociated,
whereas $3+6=4+5$. For a maximum triple $D$, set $S=\Sigma(D)$ and
take any nonzero spectral factor

$$
Q(t)=\sum_{s\in S}c_s e^{ist},\qquad
K(t)=\frac{|Q(t)|^2}{\sum_s|c_s|^2}.
$$

Let $A_D$ join vertices of $S$ whose absolute difference lies in $P$.
Then

$$
2\sum_{p\in P}\operatorname{Re}\widehat K(p)
 =\frac{c^*A_Dc}{\|c\|^2}<4.                                 \tag{1}
$$

Indeed, each graph is connected, has maximum degree four, and has
a vertex of degree three. These claims follow from the following
subset-sum and degree lists, in the same order:

| $D$ | $S$ | Vertex degrees |
|---|---|---|
| $345$ | $0,3,4,5,7,8,9,12$ | $3,4,4,3,3,4,4,3$ |
| $346$ | $0,3,4,6,7,9,10,13$ | $3,4,4,4,4,4,4,3$ |
| $356$ | $0,3,5,6,8,9,11,14$ | $3,4,4,4,4,4,4,3$ |
| $456$ | $0,4,5,6,9,10,11,15$ | $3,3,4,4,4,4,3,3$ |

Connectivity also follows from the canonical basis-color cube edges.
The strict inequality in (1) follows from

$$
4\|c\|^2-c^*A_Dc
 =\sum_{\{s,t\}\in E}|c_s-c_t|^2
  +\sum_s(4-\deg s)|c_s|^2>0.
$$

Equality would force $c$ to be constant on the connected graph and
zero at a deficient-degree vertex, hence zero everywhere.

Thus arbitrary spectral factors on maximum cubes, even after convex
mixing, cannot give the proposed aggregate Fourier domination
$2\sum_{p\in P}\operatorname{Re}\widehat K(p)\ge|P|$.
This only excludes that particular positive spectral-counting method.

## Coherent odd quadruples can have more than four smaller blocked extensions

Let $D=(15,17,27,33)$. Its pair sums are distinct, and its three
smallest elements sum to more than its largest, so it is dissociated.
By the proved odd-four-set lemma it is coherent. All six smaller odd
numbers

$$
p\in\{1,5,7,9,11,13\}
$$

give noncoherent extensions. Four are ruled out by

$$
1=33-15-17,\quad5=15+17-27,\quad
9=15+27-33,\quad11=17+27-33.
$$

For $p=7,13$, the five-sets remain dissociated: their pair sums are
distinct, and their three smallest entries sum to more than their
largest. Nevertheless they have the exact fiber decompositions

$$
\mathbf1=
\frac{(2,0,5,0,0)+2(0,3,0,2,0)+(4,0,1,2,0)+2(0,0,0,0,3)}6
$$

for the weight-$99$ fiber of $(7,15,17,27,33)$, and

$$
\mathbf1=
\frac{(0,0,3,2,0)+(0,3,0,1,1)+(3,0,0,0,2)}3
$$

for the weight-$105$ fiber of $(13,15,17,27,33)$.

Thus blocked smaller odd extensions cannot be counted just by the
four triples of a coherent four-set, or bounded by its cardinality.
This does not refute the global coherent bound. Indeed the ten-element
union in this example contains the coherent set $\{1,5,7,9,27\}$:
its first four entries form a dissociated odd quadruple, and $27$
exceeds their sum, so maximizing the coefficient of $27$ in the
total-sum fiber reduces to coherence of that quadruple.

## Minimum-element exchange also fails for coherence

Let

$$
P=\{33,36,37,38,41,45\},\qquad D=P\setminus\{33\}.
$$

Then $c(P)=5$, but no maximum coherent subset contains $33$.

In the coordinate order $(36,37,38,41,45)$, the weight-$197$ fiber
of $D$ consists of $\mathbf1$ and

$$
(0,0,4,0,1),\quad(0,3,0,1,1),\quad
(0,2,0,3,0),\quad(1,0,1,3,0).
$$

For exhaustiveness, every solution has degree five because
$4\cdot45<197<6\cdot36$. Taking deficits from $45$ reduces its
enumeration to the weight-$28$ fiber on $(4,7,8,9)$ already listed
above, restricted to representations of degree at most five.
The cost $(-3,0,0,1,0)$ equals $-2$ at $\mathbf1$ and is
nonnegative at the other four points, so $D$ is coherent.

Four five-subsets containing $33$ have a ternary relation from

$$
33+41=36+38,\qquad 33+45=37+41.
$$

The remaining set $E=(33,36,37,38,45)$ has the decomposition

$$
\mathbf1=\frac14\bigl[
(3,0,0,0,2)+(0,4,0,0,1)
 +(1,0,3,0,1)+(0,0,1,4,0)
\bigr].
$$

Every point displayed has weight $189=\sum E$, so $E$ is noncoherent.
Heredity also excludes coherence of the full $P$. Thus neither
extremal-element exchange principle can justify an iteration of the
[[research/erdos_963/empty_lift_quotient|one-step empty-lift construction]].

## A coherent vertex need not admit any modular pivot

The coherent set

$$
D=(9,20,42,44,49,63)
$$

has no pivot $p\in D$ for which $D\setminus\{p\}$ is dissociated
modulo $p$. Moreover its all-ones point is coordinatewise maximal
among vertices of all its integer fibers. Thus squarefree vertices
cannot in general be reduced to an asymptotic group-relaxation branch.

To prove coherence, its total weight is $227$. Minimize the cost
$12u_9+8u_{20}+5u_{44}$. Modulo seven, a feasible point of cost at
most $25$ must have

$$
(u_9,u_{20},u_{44})=(0,0,5),\ (0,1,2),\ \text{or }(1,1,1).
$$

This follows directly by taking $u_9=0,1,2$ in
$2u_9+6u_{20}+2u_{44}\equiv3\pmod7$ and the cost bound.
The residual weights, divided by seven, are $1,17,22$, to be
represented using $6,7,9$. The first two are impossible and the
last has the unique representation $6+7+9$. Hence $\mathbf1$ is
the unique cost minimizer.

Every proposed pivot has a modular collision:

$$
\begin{aligned}
2\cdot9&=20+42-44,&2\cdot20&=49-9,\\
2\cdot42&=44+49-9,&3\cdot44&=20+49+63,\\
2\cdot49&=44+63-9,&2\cdot63&=42+44+49-9.
\end{aligned}
$$

The coefficient-two relations make $\mathbf1+e_p$ a midpoint
nonvertex for every $p\ne44$. For the remaining coordinate,
in the displayed ordering of $D$,

$$
\mathbf1+e_{44}=\tfrac13\bigl[
(1,0,1,5,0,0)+(0,2,2,0,3,0)+(2,1,0,1,0,3)\bigr].
$$

All three terms have weight $271$. Translating these decompositions
by nonnegative integer vectors excludes every vertex properly
dominating $\mathbf1$ coordinatewise. This is an obstruction to a
pivot-based proof, not to the coherent cardinality conjecture.
