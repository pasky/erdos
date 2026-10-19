---
name: research/erdos_774/lemmas/binary_circuit_lifting
title: Exact binary circuit threshold in distinct-prime grids
desc: Every binary dependence on at most eighteen distinct-prime-grid columns contains a ternary dependence; nineteen is sharp, and singleton-layer descent gives a prime-tail refinement.
tags: [E0774, proved, algebra, incomplete]
sources: []
created: 2026-09-18T16:44:29Z
updated: 2026-09-18T16:49:38Z
---


# Exact binary circuit threshold in distinct-prime grids

***

## Result and scope

Let $E=\bigotimes_{p\in P}S_p$, where $P$ is a finite set of
distinct odd primes, and let $A$ be its standard integer column matrix.
A **binary circuit** is a minimal nonempty support in
$\ker_{\mathbb F_2}\overline A$. Call it liftable if its entire
support carries a relation with coefficients $\pm1$ over $\mathbb Z$.

**Theorem.** Every binary circuit with at most eighteen vertices is liftable.
There is an unliftable binary circuit with nineteen vertices already in
$S_3\otimes S_5\otimes S_7$.

Consequently, for every dissociated $C\subseteq E$, the binary code
$\ker_{\mathbb F_2}\overline A_C$ has minimum distance at least
nineteen. More generally, if the permitted primes start with
$r_1<r_2<r_3$, the minimum distance is at least
$\max(19,2r_3)$. With fewer than three factors, this kernel is zero.

This is a proved finite-support lifting theorem, **not** an unbounded
dissociated-coloring theorem or fixed-height focusing premise. In particular
the modular kernel here is the full kernel of the reduced column matrix,
not merely the reduction of the integer relation lattice on $C$.
The coordinates are the standard tensor basis, or a unimodular change of
that basis, not an arbitrary integer encoding or a scaled matrix.

## 1. Singleton-layer descent

In a binary relation on $B\otimes S_p$, all layer sums in the reduced
base agree. If one layer is empty, all sums vanish, so each occupied layer
separately supports a relation. For a binary circuit this forces exactly one
occupied layer. Such an inactive coordinate can be deleted without changing
liftability. Every active coordinate of a circuit therefore occupies all
$p$ layers.

Suppose a circuit $D$ has a singleton layer $D_0=\{a\}$ in an
active coordinate. Every
other layer $D_j$ is binary-independent, since a dependence in one
layer would be a proper subdependence of $D$. Its binary sum is $a$.
If $a\in D_j$, independence forces $D_j=\{a\}$. Otherwise
$D_j\cup\{a\}$ is a binary circuit: any proper relation would have
to contain $a$, and its difference with the full relation would be
a dependence in $D_j$. Its size is at most
$$
|D_j|+1\leq |D|-p+2<|D|.
\tag{1}
$$

If every such smaller circuit lifts, normalize its coefficient at $a$
to $-1$. Then each layer has a signed sum equal to the actual vector
$a$. For layers $\{a\}$, use coefficient $+1$. Equal layer
sums reconstruct a full-support ternary relation on $D$.
Thus an unliftable circuit with a singleton layer descends to a strictly
smaller unliftable circuit on one fewer factor.

This descent may combine projections of points from different old layers.
It does not preserve their colors under an arbitrary original coloring.

## 2. Two factors and the first tail bound

On $S_p\otimes S_q$, every binary kernel array has form
$a_i+b_j$, with $a_i,b_j\in\mathbb F_2$. This follows directly
by solving the equations on the first $(p-1)(q-1)$ coordinates; the
last row and column determine all entries. Choose representatives in
$\{0,1\}$. The integer array $a_i-b_j$ has the same support,
entries in $\{-1,0,1\}$, and lies in the integer kernel because
each whole row and column is a simplex relation. The one-factor case is
immediate.

Repeated singleton descent from an unliftable circuit must therefore end
at one with at least three active factors and no singleton layers. Its size
is at least twice its largest active prime, hence at least $2r_3$.
This proves the tail bound, with no statement of liftability at its endpoint.

## 3. A two-point reference layer over $S_3\otimes S_5$

To exclude bad circuits of size at most eighteen, choose one of smallest
size. Delete its inactive coordinates. Section 1 excludes singleton layers;
Section 2 forces at least three active primes. Each active prime is at most
nine, so the active factors are exactly $3,5,7$. Its seven layers
over $B=S_3\otimes S_5$ have size at least two. Some layer has size
two, since otherwise the total size would be at least twenty-one. Denote
this reference layer by $R=\{a,b\}$.

Identify the fifteen base labels with the edges of $K_{3,5}$, oriented
from the three-vertex part to the five-vertex part. Over either $\mathbb Q$
or $\mathbb F_2$, the base kernel consists of graph gradients
$t_{\mathrm{row}}-t_{\mathrm{col}}$. In particular, a label set $D$ is
binary-independent exactly when $K_{3,5}\setminus D$ is connected:
a supported nonzero gradient exists exactly when its complement is disconnected.

Every other layer $D$ is binary-independent and has the same binary
sum as $R$. We determine the possible signs $\epsilon_a,\epsilon_b$
for which $\epsilon_a a+\epsilon_b b$ has a representation on all
of $D$ with coefficients $\pm1$.

- If $D$ contains both $a,b$, then $D=R$, by independence;
  both relative sign choices work.
- If $D$ contains exactly one, say $a$, then
  $(D\setminus\{a\})\cup\{b\}$ is a binary circuit. It is a
  minimal cut (a bond) of the graph, whose integer cut vector is a
  full-support $\pm1$ relation. This represents either sign of
  $b$ on $D\setminus\{a\}$, independently of the sign at
  $a$. Again both relative signs work.
- Suppose $D\cap R=\varnothing$. The graph
  $H=K_{3,5}\setminus D$ is connected, and deleting $a,b$
  leaves either two or three components. It cannot leave one: the nonzero
  binary cut vector on $D\cup R$ is constant on each component of
  its complement, but changes on $a,b$.

  With two components, $D\cup R$ is a bond. Its cut vector forces
  one relative sign at $a,b$, and realizes that sign choice with
  coefficients $\pm1$ everywhere on $D$.

  With three components, the edges $a,b$ form a tree connecting
  them. The binary cut labels the center component differently from both
  leaves. Every edge in $D$ consequently joins the center to a leaf,
  never the two leaves or a component to itself. For any prescribed signs
  at $a,b$, assign integer potentials to the three components with
  those gradients on the tree edges. Every $D$-edge then has gradient
  $\pm1$. Negating the gradient on $D$ gives the desired
  full-support representation of $\epsilon_a a+\epsilon_b b$.
  Thus this case imposes no relative-sign constraint.

Only bond layers $D\cup R$ can constrain the relative sign, and
their constraints have just the two possible values.

## 4. Incompatible constraints cost at least nineteen points

If $a,b$ share an endpoint, every cut containing both gives the same
relative orientation. All layer constraints agree, and the signed layer
sums reconstruct a ternary lift, a contradiction.

Otherwise write $a=(u_1,v_1)$, $b=(u_2,v_2)$, with distinct
endpoints on both sides. A cut containing $r$ row vertices and $s$
column vertices on one side has size
$$
5r+3s-2rs.
\tag{2}
$$
For a bond containing these two disjoint edges, both complementary induced
graphs are connected, so $r\in\{1,2\}$, $1\leq s\leq4$.
(An extreme side would be an isolated single vertex, which cannot cut both
disjoint edges.)

If $a,b$ have opposite cut orientations, (2) is at least six:
for $r=1$ it is $5+s\geq6$, and for $r=2$ it is
$10-s\geq6$. If they have the same orientation, after exchanging
the sides the two row endpoints are inside and the two column endpoints
outside. Hence $r=2$, $s\leq3$, and the cut size is at least
seven. These possibilities give layers $D$ of size at least four
and five, respectively, after removing the reference edges.

An unliftable circuit needs both types of constraint; otherwise choose a
compatible relative sign and reconstruct its lift as in Section 3. All
seven layers have at least two points, and these two constrained layers
therefore force
$$
|D_{\rm total}|\geq 7\cdot2+(4-2)+(5-2)=19.
$$
This contradicts the proposed counterexample of size at most eighteen.

## 5. Sharpness without a new search

Use the recorded
[twenty-point coefficient-two circuit](prime_tensor_circuit.md). Its integer
kernel has one generator with nineteen coefficients $\pm1$ and one coefficient
$-2$. Its verified unit minor gives rank nineteen also modulo two. Consequently
its full binary kernel is one-dimensional, supported on exactly the nineteen
odd-coefficient columns. Those nineteen columns form a binary circuit.

They are rationally independent, since they are a proper subset of the
twenty-point rational circuit. In particular they admit no ternary lift.
This proves sharpness. It uses the existing algebraic certificate; no prior
experiment or certificate was rerun.

## 6. What this does and does not give the main route

For a dissociated $n$-point set $C$, every nonzero modular kernel
word contains a binary circuit, so the theorem excludes weights below
nineteen. Disjoint radius-nine Hamming balls give
$$
\operatorname{rank}_{\mathbb Q}A_C\geq
\operatorname{rank}_{\mathbb F_2}\overline A_C
\geq\log_2\sum_{j=0}^{9}\binom nj.
\tag{3}
$$
On a prime tail, replace nine by
$\lfloor(\max(19,2r_3)-1)/2\rfloor$. We use $\binom nj=0$
for $j>n$. The modular nullity need not equal the rational nullity:
the sharp nineteen-column example itself has rational nullity zero and
modular nullity one.

For the already considered even-$H$, $H I$-pivot mechanism, let
$k$ be the integer-kernel rank and $m=n-k$ the number of nonpivot
coordinates. The integral-kernel basis stays independent modulo two, while
its pivot rows vanish. Its reduced code is therefore a $k$-dimensional
subcode supported on these $m$ positions, with distance at least nineteen.
The corresponding form of the same Hamming bound is
$$
2^k\sum_{j=0}^{9}\binom mj\leq2^m.
\tag{4}
$$
This applies to dissociated subsets of the distinct-prime grids under the
stated integral-pivot hypothesis. It sharpens the half-density ceiling only
by lower-order terms; no high-density descent follows.

The new singleton descent is a precise recursive lifting alternative, but
its conclusion is still local in support size. Hamming bounds of this form
permit nullity density tending to one. No monochromatic structure is forced,
and descent in a projected grid does not transfer actual colors. Thus neither
the fixed-height premise nor the main unbounded-coloring theorem follows.

The singleton reduction, graph-potential sign analysis, bond-size bounds,
and sharpness witness received independent internal review. No numerical
search was run; internal review is not external review.
