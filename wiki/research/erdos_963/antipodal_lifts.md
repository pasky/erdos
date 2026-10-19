---
name: research/erdos_963/antipodal_lifts
title: 'A sufficient antipodal-lift formulation and its global gap'
desc: An exact norm criterion and elementary volume bound give a weaker sufficient lifting problem; even minimal-circuit greedy projection is false.
tags: []
sources: []
created: 2026-09-19T05:38:45Z
updated: 2026-09-19T05:43:11Z
---


# A sufficient antipodal-lift formulation and its global gap

***

This is a new sufficient formulation, **not a proof** of Erdős 963. It uses a
weaker requirement than [[research/erdos_963/global_lift_gap|Boolean lifting]]:
no integrality or Boolean coordinates are required. Antipodality is not claimed
to follow from lattice emptiness. Its global existence assertion remains
unproved.

Let $P=\{p_1,\ldots,p_n\}$ be distinct positive reals, set $p_0=0$,
and put

$$
H=\{u\in\mathbb R^{n+1}:\sum_i u_i=0,\ \sum_i u_i p_i=0\}.
$$

For $K\subseteq H$, project the vertices of the standard affine
$n$-simplex modulo $K$. The resulting configuration $X_K$ has
affine dimension $n-\dim K$, and the prescribed heights $p_i$
descend to an affine functional on it.

## Exact criterion

A finite configuration is **antipodal** if every pair of distinct
points lies on two distinct parallel supporting hyperplanes of its
convex hull. The quotient $X_K$ is antipodal, with all its labeled
points distinct, if and only if

$$
\boxed{\max_i u_i-\min_i u_i\le\tfrac12\|u\|_1
       \quad\text{for every }u\in K.}                       \tag{1}
$$


For a fixed pair $i,j$, a normalized supporting functional is a
vector $y\in K^\perp$ satisfying

$$
y_i=1,\quad y_j=-1,\quad |y_\ell|\le1\quad(\ell\ne i,j).
$$

The image of the box of remaining coordinates in $K^*$ is compact
and convex. The elementary separating-hyperplane criterion for
membership in that image gives precisely

$$
|u_i-u_j|\le\sum_{\ell\ne i,j}|u_\ell|\quad(u\in K).       \tag{2}
$$

For a nonzero balanced vector $u$, write $M=\max u_i>0$ and
$m=\min u_i<0$. Applying (2) at these two coordinates yields
$2(M-m)\le\|u\|_1$. Conversely, for arbitrary $i,j$,

$$
|u_i-u_j|+|u_i|+|u_j|\le2(M-m),
$$

so (1) implies (2). This proves the criterion. In particular,
no vector $e_i-e_j$ can belong to an admissible $K$, which also
ensures distinct quotient points.

Every individual ordinary ternary relation gives an admissible
line in $H$. Suppose it has $a$ positive and $b$ negative
coefficients on $P$, and augment it by $u_0=b-a$. Positivity
forces $a,b\ge1$. If $a=b$, distinctness excludes $a=b=1$,
so its coordinate range is $2\le a=\|u\|_1/2$.
If $a>b$, its range is $a-b+1\le a=\|u\|_1/2$; reversal
handles $b>a$. This proves the claim for the whole line by
homogeneity.

## Why a global lift would prove the target

An antipodal set $X$ of affine dimension $r$ has at most $2^r$
points. Here is the full volume argument. Let $Q=\operatorname{conv}X$
in its affine span. Each homothet $(x+Q)/2$, $x\in X$, lies in
$Q$. Their relative interiors are pairwise disjoint. Otherwise,
for distinct $x,y$ there would be $u,v\in\operatorname{relint}Q$
with $x+u=y+v$. A functional attaining its maximum at $x$ and
minimum at $y$ gives

$$
f(x)-f(y)=f(v)-f(u)<\max_Q f-\min_Q f,
$$

a contradiction. Comparing $r$-dimensional volumes proves
$|X|2^{-r}\operatorname{vol}Q\le\operatorname{vol}Q$.

Consequently, the following **unproved** assertion suffices:

$$
\text{There is }K\subseteq H\text{ satisfying (1) with }
\dim K\ge n-d(P).                                         \tag{3}
$$

It would give

$$
|P|+1=|X_K|\le2^{n-\dim K}\le2^{d(P)}.
$$

No implication from maximum dissociation to (3) has been established.
Individual admissible ternary lines cannot simply be summed.

## An exact two-relation test

For two augmented ternary relations $u,v$, their span satisfies
(1) if and only if (1) holds for the following five vectors,
ignoring zero vectors:

$$
u,\qquad v,\qquad u+v,\qquad u-v,\qquad v_0u-u_0v.        \tag{4}
$$

Only coordinate zero can have coefficient outside $\{-1,0,1\}$.
Thus coordinate signs of $su+tv$ can change only on the lines

$$
s=0,\quad t=0,\quad s=t,\quad s=-t,\quad u_0s+v_0t=0.
$$

On each sector of this arrangement, $\|su+tv\|_1$ is linear.
Each inequality
$(su+tv)_i-(su+tv)_j\le\|su+tv\|_1/2$ is consequently
linear there, so it suffices to check the bounding rays. Their
images, up to sign, are exactly the vectors in (4). Necessity
is immediate. This is a finite compatibility test, not an
extension theorem.

## Minimal ternary circuits do not justify greedy projection

There is a projection-minimal antipodal lift of dimension greater
than ordinary dissociation dimension even when its kernel is
generated entirely by support-minimal ternary relations.

Take

$$
P=\{1,2,3,4,5,6,7,8,10,13,17,22,28\}.
$$

Its sum is $126$. Any seven-element subset has its $128$ subset
sums in $\{0,\ldots,126\}$, and hence is dependent. Thus
$d(P)\le6$. Also $\{1,2,4,8,17\}$ is dissociated, since
the first four elements have subset sums $0,\ldots,15$, disjoint
from their translate by $17$. In particular this set is not a
counterexample to the cardinality bound.

Order seven leaves as $(7,1,2,3,4,5,6)$, lift them to
$e_1,\ldots,e_7$, and lift the six successive prefix sums

$$
8,10,13,17,22,28
$$

to the corresponding prefix indicator vectors. Together with zero
this is a subset of $\{0,1\}^7$, hence antipodal. Its heights
are given by the leaf weights. Its six independent defining
relations are

$$
7+1=8,\quad8+2=10,\quad10+3=13,\quad13+4=17,
\quad17+5=22,\quad22+6=28.
$$

Each is a support-minimal ternary relation, because every pair
of distinct positive numbers is dissociated. The six relations
generate the full affine kernel, which has dimension $13-7=6$.
Every intermediate span satisfies (1), since it is contained in
the final admissible kernel.

Nevertheless this lift admits no lower-dimensional antipodal
projection retaining all labeled points distinctly, even if the
height requirement is dropped. It contains

$$
0,e_1,\ldots,e_7,\mathbf1.
$$

For any such distinctness-preserving antipodal image under a linear
map $T$, normalize a
supporting functional for $0,T(e_i)$ to have values $0,1$.
All displayed image points have values in $[0,1]$. Since
$T(\mathbf1)=\sum_jT(e_j)$, nonnegativity forces this functional
to vanish on every $T(e_j)$ with $j\ne i$. The seven such
functionals show that $T(e_1),\ldots,T(e_7)$ are linearly
independent. Thus the projection still has dimension at least
seven, greater than $d(P)$.

There is no contradiction to the existence assertion (3): a
different five-dimensional cube lift is already supplied by
the binary digits of the integers in $P\subseteq[1,31]$.
The obstruction proves that earlier relations may have to be
**replaced**, not just supplemented, in a global construction.

## Status

The exact norm criterion, the sufficient implication, the
two-relation test, and the greedy obstruction are proved.
Existence of a globally chosen $K$ as in (3) is the precise
remaining gap. No new universal bound on $d(P)$ or on $f(n)$
follows from this note.
