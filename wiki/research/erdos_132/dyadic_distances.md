---
name: research/erdos_132/dyadic_distances
title: A logarithmic rare-distance bound for rational planar sets
desc: |
  Dyadic hypotheses give logarithmic growth; a five-point equality pattern
  obstructs invariant reduction, while a split F2 valuation has a rare
  class at its lowest norm level.
sources: []
research_state: closed
created: 2026-09-22T21:20:00Z
updated: 2026-09-24T22:12:56Z
---


# A logarithmic rare-distance bound for rational planar sets

***

This is a restricted-family result, not a solution of either unrestricted
question in [Problem 132](../../problems/distance_problems/E0132/_index.md).
Multiplicities throughout count unordered pairs. The argument was checked by the
author and is author-recorded; no novelty claim is made.

## Bichromatic maximum-distance lemma

This bound is also Theorem 3(i) of Dumitrescu--Guha,
[*Extreme Distances in Multicolored Point Sets*](https://www.emis.de/ft/51034)
(2004). Its statement and disk-intersection proof on pp. 33--34 were
checked. The Minkowski-difference proof below is self-contained.

If disjoint nonempty finite planar sets $X,Y$ have largest cross-distance
$D=\max_{x\in X,y\in Y}|x-y|$, then at most $|X|+|Y|$ cross-pairs attain $D$.

Put $P=\operatorname{conv}X$ and $Q=\operatorname{conv}Y$. Every point of
$P-Q$ is a convex combination of cross-differences, so $P-Q$ is contained
in the closed disk of radius $D$. Every norm-$D$ difference $v=x-y$ is
an exposed vertex: the functional $u\mapsto v\cdot u$ uniquely maximizes
at $v$ on that disk.

Different maximizing pairs give different differences. Otherwise, writing
$x-y=x'-y'=v$ and $w=x'-x=y'-y\ne0$, the two cross-differences $v+w,v-w$
would both have norm at most $D$, contrary to

$$|v+w|^2+|v-w|^2=2D^2+2|w|^2>2D^2.$$

The Minkowski sum of two planar convex polygons has at most the sum of
their vertex counts: their cyclic lists of edge directions merge, with
parallel directions coalescing. The same bound holds when either polygon
is a segment or a point, directly or by its normal fan. Thus

$$\#\{(x,y)\in X\times Y:|x-y|=D\}
 \le |\operatorname{vert}P|+|\operatorname{vert}Q|
 \le |X|+|Y|.$$

## Theorem

For a finite $A\subset\mathbb Q^2$ of cardinality $n\ge2$,

$$R(A)\ge\lceil\log_2 n\rceil.$$

Identify the plane with $\mathbb C$ and $A$ with a subset of
$\mathbb Q(i)$. Let $\nu$ be the discrete valuation at $1+i$, normalized
by $\nu(1+i)=1$. Its residue field is $\mathbb F_2$. Conjugation preserves
$\nu$, and $\nu(q)=2v_2(q)$ for $q\in\mathbb Q^\times$. Consequently

$$v_2(|z-w|^2)=\nu(z-w).$$

In particular an entire Euclidean distance class has the same valuation
level. Let $T$ be the finite set of occurring pair levels $\nu(z-w)$.
For $t\in T$, partition $A$ by $\nu(z-w)\ge t$. Each block has at most
two nonempty children under the finer equivalence $\nu(z-w)>t$, since
the residue field has two elements. The pairs of level exactly $t$ are
therefore the cross-pairs in disjoint complete bipartite blocks.

Let $D_t$ be the largest Euclidean distance among those pairs. In each
block which contributes a $D_t$ pair, it is the maximum cross-distance
of the two children. The preceding lemma bounds its contribution by
the number of points in that block. Its entire distance class has
level $t$, so summing over the blocks proves $m_A(D_t)\le n$.
The $D_t$ for different levels are different. Hence $R(A)\ge|T|$.

Finally the binary cluster tree has $n$ leaves and at most $|T|$
branching levels along every root-to-leaf path. Thus $n\le2^{|T|}$.
Equivalently, this follows by induction on $|T|$: split at the smallest
pair level into at most two children, each of which uses at most
$|T|-1$ levels. This proves the theorem.

There is also a simpler first-question check. At the highest level,
every block has at most two points, so every distance graph there is a
matching. At the second-highest level, each child has at most two
points, so each distance graph has maximum degree at most two. At
least two levels occur when $n\ge3$.

## A stronger valuation criterion

The same logarithmic bound holds if the complex coordinates lie in a
conjugation-stable field $L\subset\mathbb C$ having a discrete valuation
$\nu$ such that:

1. $\nu(\bar z)=\nu(z)$;
2. the residue field $k$ has characteristic two; and
3. conjugation acts trivially on $k$.

The residue field need not be finite. Choose a uniformizer $\pi$.
For a difference $z-w$ of level $t$, let
$a=\operatorname{res}((z-w)/\pi^t)\in k^\times$. Because the residue
characteristic is two, the same $a$ belongs to $w-z$, so this is a type
of unordered pair. Its squared Euclidean distance $q$ determines both
$t$ and $a$: first $\nu(q)=2t$, and then

$$\operatorname{res}\left(\frac{q}{(\pi\bar\pi)^t}\right)=a^2.$$

Squaring is injective in a field of characteristic two. In a fixed
level-$t$ cluster, label its children by their residues relative to a
fixed base point. Pairs of type $(t,a)$ connect labels $b$ and $b+a$.
This is a fixed-point-free involution, so the entire graph of pairs
of this type is again a disjoint union of complete bipartite graphs.
Its maximum Euclidean distance is rare by the same geometric lemma.
Different types give different distance classes.

Let $s_t$ be the finite number of occurring leading residues at level
$t$. Every cluster at that level has at most $s_t+1$ children: fix one
child and subtract its label from the others. The finite cluster tree
therefore gives

$$n\le\prod_t(s_t+1)\le2^{\sum_t s_t},
\qquad R(A)\ge\sum_t s_t\ge\lceil\log_2 n\rceil.$$

## Scope and the exact obstruction

These hypotheses do not hold for arbitrary algebraic realizations.
In an equilateral triangle all three pairs would have the same type
$(t,a)$. If two differences have leading residue $a$, their difference
has leading residue $a-a=0$, contradicting the third pair's type.
Thus an equilateral triangle rules out this valuation criterion.
Such triangles occur in arbitrarily large planar sets.

In $\mathbb Q(\sqrt3,i)$, the dyadic residue field is $\mathbb F_4$
and conjugation acts nontrivially on it, consistently with this
obstruction. The issue is not merely the size of the residue field:
the norm-leading-residue map is then not injective.

Without the refinement into bipartite types, an abstract multipartite
maximum-distance bound of $n$ is false. In the unit rhombus formed
from two equilateral triangles, put the endpoints of the long diagonal
in one part and each remaining point in its own part. The maximum
cross-part distance has five pairs on four points. This coloring does
not itself respect the dyadic norm levels; an actual Eisenstein-coordinate
counterexample to taking the maximum distance at each level is recorded
in [the obstruction note](layers_and_obstructions.md).

## Two further obstructions to choosing a shell extremum

These are exact certificates, not counterexamples to Problem 132.
Use Eisenstein coordinates $a+b\omega$, $\omega=e^{i\pi/3}$, with
squared norm $a^2+ab+b^2$.

The nine points


$$
\{(0,1),(0,2),(1,1),(1,3),(2,3),(3,0),(-1,4),(1,2),(2,2)\}
$$


have squared-distance spectrum


$$
1:10,\quad3:8,\quad4:4,\quad7:12,\quad12:1,\quad16:1.
$$


Thus both the smallest and largest values in the dyadically odd shell
are rich; its middle value (3) is rare. Taking either extremum is not
a valid repair of the earlier maximum-only argument.

Even reducing to three residue classes does not repair the maximum
argument over $\mathbb Q(\omega)$. The five points


$$
0,\quad1,\quad\omega,\quad
\frac{-55+40\omega}{97},\quad
\frac{42-57\omega}{97}
$$


have squared spectrum


$$
25/97:1,\quad27/97:1,\quad1:6,\quad192/97:1,\quad196/97:1.
$$


Their residues modulo two are only $0,1,\omega\in\mathbb F_4$, since
97 is odd. The squared norms with zero dyadic valuation are
$25/97,27/97,1$. The largest, 1, has six pairs and is rich. The two
larger occurring norms have positive dyadic valuation and do not belong
to that shell. Thus the proposed three-residue maximum lemma is false.

The author checked every pair with exact rational arithmetic; the
[saved certificate](evidence/util/valuation_counterexample.py) includes both
examples. Neither example disproves the existence of *some* rare class
at every invariant-valuation level. A mixed dyadic/triadic selection
remains unproved; in the five-point example its maximal-triadic-valuation
choice is $27/97$, which is rare.

## Odd dyadic ramification is sufficient

The criterion also covers every real coordinate field $F$ having
a dyadic prime $\mathfrak p$ with odd ramification index. Put
$K=F_{\mathfrak p}$. The local extension $K(i)/K$ has degree two:
otherwise $K$ would contain $\mathbb Q_2(i)$, whose ramification
index is two, contradicting odd $e(K/\mathbb Q_2)$.
Likewise $K(i)/K$ cannot be unramified, because its total
ramification index over $\mathbb Q_2$ must be even. Thus it is
ramified quadratic. Its valuation is conjugation-invariant and
conjugation acts trivially on its characteristic-two residue field.
The proved criterion gives $R(A)\ge\lceil\log_2 n\rceil$.

In particular, this applies if $[F:\mathbb Q]$ is odd: in
$[F:\mathbb Q]=\sum_{\mathfrak p\mid2}e_{\mathfrak p}f_{\mathfrak p}$,
at least one summand, hence one ramification index, is odd.

## Split dyadic norm levels can contain no rare class

The conjugation-invariance hypothesis cannot simply be dropped,
even if all squared distances are rational. Put

$$
u=(3+i\sqrt7)/4,\qquad
A_k=\left\{\sum_{j=0}^{k-1}\epsilon_j u^j:
                  \epsilon_j\in\{0,1\}\right\}.
$$

Here $|u|=1$. Choose a valuation $\nu$ of $\mathbb Q(i\sqrt7)$
above $v_2$, normalized to restrict to $v_2$ on $\mathbb Q$.
Since $u\bar u=1$ and $u+\bar u=3/2$, their valuations are
$1,-1$ in some order: equal valuations would both be zero and
could not give a sum of valuation $-1$; unequal valuations have
minimum $-1$ and sum zero. Exchange conjugate valuations so that
$\nu(u)=1$, $\nu(\bar u)=-1$.

If two binary sums differ first at index $a$ and last at index $b$,
their difference has the form

$$z-w=\sum_{j=a}^b\delta_j u^j,
\quad\delta_j\in\{-1,0,1\},\quad\delta_a\delta_b\ne0.$$

The uniquely lowest-valuation term proves $\nu(z-w)=a$, and
after conjugation it proves $\nu(\bar z-\bar w)=-b$. In particular
all $2^k$ points are distinct, and

$$v_2(|z-w|^2)=a-b.$$

Valuation zero therefore consists exactly of pairs differing in
one bit, all of which have distance one. Its sole distance class
has multiplicity $k2^{k-1}>2^k$ for $k\ge3$.

For $k=3$, an exact squared-distance spectrum is

$$
\begin{array}{c|rrrrrrrr}
q&1/4&1/2&1&7/4&9/4&11/4&7/2&25/4\\\hline
m(q)&1&4&12&2&2&2&4&1
\end{array}
$$

and the multiplicities sum to $28$. This is **not** a counterexample
to Problem 132; it disproves only the unrestricted per-norm-level
claim. The conjugation-stable, nontrivial-residue-action case
remains a different unresolved question. The general family also
falls within the [small-factor Minkowski-sum bound](minkowski_sum_layers.md),
which forces its number of rare distances to grow.

## A rare class at the lowest split level

The split construction above does not preclude rarity at its *lowest*
norm-valuation level. The following one-stage lemma needs no
conjugation invariance or discreteness.

**Lemma.** Let $A=\{z_1,\ldots,z_n\}\subset L\subset\mathbb C$, $n\ge2$,
where $L$ is conjugation-stable and has a valuation $\nu$ with residue
field $\mathbb F_2$. Some distance of minimum occurring
squared-distance valuation is rare.

Set

$$a=\min_{i\ne j}\nu(z_i-z_j),\qquad
b=\min_{i\ne j}\nu(\bar z_i-\bar z_j).$$

Choose $u,v$ with valuations $a,b$, respectively; actual differences
attaining the minima suffice. Reduce

$$\left((z_i-z_1)/u,(\bar z_i-\bar z_1)/v\right)$$

to a label $(\alpha_i,\beta_i)\in\mathbb F_2^2$. Both coordinate
projections are nonconstant. A subset of this four-cell square
without opposite cells lies in a single row or column. Therefore
opposite occupied cells exist, and

$$t_0:=\min_{i\ne j}\nu(|z_i-z_j|^2)=a+b.$$

Equality holds precisely when both residue coordinates differ.
The entire graph of pairs at level $t_0$ is consequently

$$K(V_{00},V_{11})\ \sqcup\ K(V_{01},V_{10}).$$

Take the greatest Euclidean distance $D$ among these pairs. Its full
distance class has valuation $t_0$. In each contributing bipartite
block it is the maximum cross-distance, so the bichromatic maximum
lemma bounds its total multiplicity by $n$.

Thus, if the ordinary diameter squared has valuation greater than
$t_0$, there are at least two rare distances. This does not assert
that the diameter must have that valuation, nor that later levels
contain rare classes. In particular it is consistent with the
rich-only nonminimal level in the saved split construction.

### Characteristic-two good reduction at one scale

There is also an elementary criterion without complex coordinates.
Suppose $A\subset F^2$, with $F\subset\mathbb R$ valued and residue
field $k$ of characteristic two. Choose a nonzero real $c\in F$
so all translated coordinates

$$X_i=(x_i-x_1)/c,\qquad Y_i=(y_i-y_1)/c$$

are integral. Such a choice is possible by selecting an entry of
minimum valuation among the nonzero translated coordinate entries.
Put $s_i=\operatorname{res}(X_i+Y_i)$ and $S=\{s_i\}$. Then

$$\operatorname{res}\bigl(|p_i-p_j|^2/c^2\bigr)=(s_i-s_j)^2.$$

For each nonzero $\alpha\in S-S$, the pairs with normalized
squared-distance residue $\alpha^2$ form disjoint complete bipartite graphs
between fibers labeled $s$ and $s+\alpha$. Their maximum Euclidean
distance is globally rare. Squaring is injective in a field, so
different $\alpha$ give different rare distances. Hence

$$R(A)\ge |(S-S)\setminus\{0\}|.$$

Normalization does not ensure that $S$ is nonconstant: for
$(0,0),(1,1)$ at a dyadic valuation both residues are zero.
Neither one-stage argument supplies a general iteration. The author
checked both proofs and their normalizations; both are author-recorded,
and neither settles the unrestricted problem.

## A distance pattern that forbids every invariant dyadic realization

The unrestricted attempt found a stronger obstruction than failure of a
particular coordinate field. Take

$$a=(0,0),\quad b=(1,0),\quad c=(1,1),\quad d=(0,1),
\quad p=(1/2,\sqrt7/2).$$

The squared-distance multiplicities are

$$1:4,\qquad2:4,\qquad3-\sqrt7:2.$$

This is not an Erdős-132 counterexample: all three classes are rare.
But **no injective planar realization preserving its original distance
equalities admits a conjugation-invariant valuation of residue
characteristic two on a conjugation-stable complex coordinate field**.

Indeed, the equalities $ab=bc=cd=da$ make $abcd$ a rhombus. To check
this without assuming simplicity, $b,d$ are the two distinct intersections
of the equal-radius circles centered at $a,c$, so they are on opposite
sides of $ac$. The additional equality $ac=bd$ makes the rhombus a
square. Put $q=|a-b|^2>0$ in any such realization. Its preserved
equalities then imply

$$|p-a|^2=|p-b|^2=|a-c|^2=2q.$$

If $\nu$ were a conjugation-invariant valuation as above, then
$\nu(|z-w|^2)=2\nu(z-w)$ and $\nu(2)>0$. Consequently

$$\nu(p-a)=\nu(p-b)=\frac{\nu(q)+\nu(2)}2
 >\frac{\nu(q)}2=\nu(a-b),$$

contradicting the ultrametric inequality for
$a-b=(p-b)-(p-a)$. Mergers of originally unequal distance classes
do not evade the argument; only the displayed preserved equalities
and distinctness were used.

Thus changing an algebraic realization cannot always bring its distance
partition into the invariant-dyadic setting. Proving the still-unresolved
per-level assertion for nontrivial residue conjugation would not, on its
own, settle arbitrary planar sets. No mechanism combining the invariant
and split cases was obtained. The finite pattern and valuation contradiction
were checked by the author and are author-recorded.

## A rare class at the highest invariant-valuation level

Let $A\subset L\subset\mathbb C$, where $L$ is conjugation-stable
and has a conjugation-invariant valuation $\nu$. No condition on the
residue characteristic or field is needed. Some occurring distance whose
squared value has maximal valuation is rare.

Let $s=\max_{z\ne w\in A}\nu(z-w)$. The relation
$\nu(z-w)\ge s$ partitions $A$ into equivalence classes. Every distinct
pair in one class has valuation exactly $s$, by maximality, and

$$\nu(|z-w|^2)=2\nu(z-w).$$

Thus the maximal squared-norm level is a disjoint union of complete
graphs. Choose the largest Euclidean distance $r$ among its pairs.
In each contributing component the $r$-pairs are diameter pairs and
number at most its cardinality. The whole distance class has that
valuation, so summing gives $m_A(r)\le|A|$.

Consequently an $R=1$ set must have its diameter squared of maximal
valuation for every available invariant valuation. There is no assertion
that enough different valuations produce different classes, or that this
argument iterates down the levels. Split valuations are not covered.

## A smaller exact obstruction to a shell-maximum graph restriction

Put $\omega=e^{i\pi/3}$, $t=(2+8\omega)/7$, and

$$A=\{0,1,\omega,t,t-1,t-\omega\}.$$

Its complete squared-distance spectrum is

$$1/7:2,\quad3/7:2,\quad4/7:1,\quad1:8,\quad12/7:1,\quad16/7:1.$$

The two equilateral triples supply six unit pairs. The additional unit
pairs are $0$ with $t-1$ and $1$ with $t$, since $|t-1|=1$.
Modulo the inert dyadic prime of $\mathbb Q(\omega)$, $t=0$, so
its residue fibers are $\{0,t\}$, $\{1,t-1\}$, and
$\{\omega,t-\omega\}$. The norm-valuation-zero shell is precisely
$\{1/7,3/7,1\}$; its greatest distance is rich. Its unit graph contains
the cycle $0,1,t,t-1,0$, sharing edges with the two triangles.
Thus shell-maximum graphs need not be cactus graphs.

The [exact certificate](evidence/util/continuation_checks.py) checks all fifteen
pairs using rational axial coordinates. There are five rare distances,
so this is not an Erdős-132 counterexample. It does not refute existence
of some rare class at each invariant dyadic level. The author checked
both this spectrum and the general highest-level proof; the proof is
author-recorded.
