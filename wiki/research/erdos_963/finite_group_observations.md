---
name: research/erdos_963/finite_group_observations
title: 'Checked finite-group observations'
desc: Small and structured cases of the cyclic odd bound, and an exact torsion model whose relations cannot be lifted directly to the reals.
tags: []
sources: []
created: 2026-09-18T23:48:02Z
updated: 2026-09-18T23:48:02Z
---


# Checked finite-group observations

***

These are results about ordinary modular dissociation. None is a
counterexample to the real-number target or a proof of it.

## Odd residues of dimension at most three

For odd $O\subseteq\mathbb Z/2^M\mathbb Z$,

$$
d(O)\le3\quad\Longrightarrow\quad |O|\le2^{d(O)}. \tag{1}
$$

The cases $M\le1$ are immediate. For $M\ge2$, close $O$ under
negation without changing its dimension, and take the representatives
of its antipodal classes that are $1\bmod4$. Any three such
representatives are dissociated: odd-support relations are excluded
by parity, and two-term relations by the choice of representatives.

Suppose five representatives have every quadruple dependent. A
quadruple relation is either a balanced pair-sum equality or an
all-plus zero sum. Indeed, a three-versus-one sum is $2\bmod4$.
At most one quadruple can have an all-plus relation: its omitted
point must equal the sum of all five points. Choose a point $p$
omitted by that quadruple if it exists, and otherwise any point.
Every quadruple containing $p$ has a balanced relation.

Translate $p$ to zero. Among the other four distinct nonzero points,
every triple has one member equal to the sum of the other two. Write
three as $x,y,x+y$. The fourth must be $z=\pm(x-y)$; interchange
$x,y$ if necessary so that $z=x-y$. The triple
$x,x+y,x-y$ forces $x=0$, $x=2y$, or $x=-2y$. The first two
give forbidden coincidences. In the last case the triple
$y,-y,-3y$ forces $y=0$, $3y=0$, or $5y=0$, impossible
in a $2$-group for nonzero $y$.

Thus five signed classes contain a dissociated quadruple. Along with
the three-point observation, this proves (1).

## Complete symmetric congruence classes

Let $q=2^r\ge4$, $N=q2^m$, and $a$ odd. For

$$
O=\{x\bmod N:x\equiv\pm a\pmod q\},
$$

one has

$$
d(O)\ge m+1=\log_2|O|. \tag{2}
$$

Multiplication by the inverse of $a$ reduces to $a=1$.
Starting with $b_1=1$, choose each next term as the least positive
integer congruent to $\pm1\bmod q$ exceeding the preceding total.
The sequence begins

$$
1,\ q-1,\ q+1,\ 3q-1,\ 5q+1,\ 11q-1,\ldots.
$$

If $S_j=\sum_{i\le j}b_i$, direct induction gives

$$
S_{2t}=\frac{q(4^t-1)}3,\qquad
S_{2t+1}=\frac{2q(4^t-1)}3+1.
$$

These formulas imply $S_{m+1}<N$. The first $m+1$ terms are
superincreasing, with all subset sums in $[0,N)$, proving (2).

For the full odd coset in $\mathbb Z/2^M$, $M\ge2$, the dimension
is exactly $M-1$. The superincreasing set
$\{1,3,7,\ldots,2^{M-1}-1\}$ gives the lower bound; its total is
$2^M-M-1$. If $M$ odd elements were dissociated, their subset
sums would exhaust the group. At a primitive $2^M$-th root $\zeta$,
this would imply

$$
\prod_{a\in D}(1+\zeta^a)=0,
$$

whereas no factor vanishes.

## An exact torsion model

For $r\ge0$, put $G_r=\mathbb F_3^r\times\mathbb Z/2$. Then

$$
d(G_r)=r+t_r,\qquad
t_r=\max\left\{t\ge1:\frac{3^t-1}{2}-t\le r\right\}. \tag{3}
$$


For the upper bound, take a dissociated $n$-set, write its binary
coordinates as $b_i$, and let $C\subseteq\mathbb F_3^n$ be the
kernel of its ternary-coordinate matrix. Put $t=\dim C\ge n-r$.
If $t=0$, then $n\le r$, which suffices. Otherwise dissociation
is exactly the requirement

$$
\sum_{i:c_i\ne0}b_i=1\pmod2
\quad(c\in C\setminus\{0\}).
$$

Consider the matrix on projective points of $C$ and projective
nonzero linear forms on $C$,

$$
A_{[c],[f]}=\mathbf1_{\{f(c)\ne0\}}.
$$

Over $\mathbb F_2$, $AA^{\mathsf T}=I$: a diagonal entry counts
$3^{t-1}$ forms, and an off-diagonal entry counts
$2\cdot3^{t-2}$. The latter assertion is needed only for $t\ge2$;
for $t=1$, the matrix is $(1)$. Also $A\mathbf1=\mathbf1$.

The vector recording, modulo two, the multiplicities of projective
classes among the coordinate forms with $b_i=1$ therefore equals
$\mathbf1$. Each nonzero projective class occurs at least once.
Thus $n\ge(3^t-1)/2$, and

$$
r\ge n-t\ge(3^t-1)/2-t.
$$

It follows that $t\le t_r$ and $n\le r+t_r$.

For attainment, take the ternary simplex code of dimension $t$:
evaluate all linear forms on one representative from each projective
point. Its length is $N=(3^t-1)/2$, and every nonzero word has odd
weight $3^{t-1}$. A parity-check matrix for this code has rank
$N-t$. Mark each of its columns by binary coordinate one. The
resulting $N$-set in $\mathbb F_3^{N-t}\times\mathbb Z/2$ is
dissociated, by the same kernel test. Adjoin independent unmarked
coordinates to obtain $r+t$ elements whenever $N-t\le r$.
Taking $t=t_r$ proves (3).

In particular, adding a binary coordinate does not merely add one
to the dimension of a ternary vector space. For example,
$\mathbb F_3^2\times\mathbb Z/2$ contains the dissociated four-set

$$
(0,1,1),\ (1,0,1),\ (1,1,1),\ (1,2,1).
$$


## Why the complete affine ternary block does not lift

Suppose $f:\mathbb F_3^2\to H$, with $H$ torsion-free, preserves
all distinct-point parallelogram relations. For $h\ne0$ and
$y\notin x+\langle h\rangle$, those relations give

$$
f(x+h)-f(x)=f(y+h)-f(y).
$$

Comparing through another coset shows that this difference is
independent of $x$. Summing around a three-cycle gives
$3\Delta_h f=0$, hence $\Delta_h f=0$. This holds for every
nonzero $h$, so $f$ is constant.

Thus the dense torsion model in (3) cannot be turned into distinct real
numbers by preserving its complete affine-plane relation blocks.
No relation-subselection construction yielding a real counterexample
was established.

## One signed congruence class, including the endpoint

The following additional modular special case is proved.
Let $N=2^M$, let $q=2^r\mid N$ with $r\ge1$, and let $a$ be odd.
Suppose that the nonempty residue set $O$ satisfies

$$
O\subseteq\{x\in\mathbb Z/N:x\equiv a\text{ or }-a\pmod q\}.
$$

Writing $d=d(O)$ for ordinary modular dissociation dimension, one has

$$
\boxed{q\ge d+1\quad\Longrightarrow\quad |O|\le2^d.}        \tag{4}
$$


For $q=2$ the hypothesis forces $d=1$. Any two distinct elements
which are not opposites are dissociated, so $|O|\le2$.

Suppose $q\ge4$. Symmetrizing $O$ does not change its dimension,
so it suffices to treat symmetric $O$. Let
$A=\{x\in O:x\equiv a\pmod q\}$. The two congruence classes are
disjoint, and each antipodal pair contributes exactly one member of
$A$. Hence $|O|=2|A|$.

Assume $|A|>2^{d-1}$ and put $k=d+1$. The binary residue tree modulo
$N$ has a path with at least $k-1$ branching vertices. Take its first
$k-1$ branches. Their sibling subtrees and the continuing subtree
after the last branch partition $A$ into $k$ nonempty clusters.
Every transversal of these clusters is affinely dissociated modulo
$N$: relative to the point in the continuing subtree, the other
differences have distinct valuations below $M$. A balanced ternary
relation would have a unique term of least valuation.

Every ternary relation on a transversal has coefficient sum divisible
by $q$, because all its entries are $a\bmod q$ and $a$ is a unit.
If $q>k$, this coefficient sum must be zero, contradicting affine
dissociation.

If $q=k$, a nonbalanced relation can only have all $q$ coefficients
equal to $1$, or all equal to $-1$. Thus a transversal is ordinarily
dissociated whenever its total is nonzero modulo $N$. But

$$
|A|>2^{q-2}\ge q\qquad(q\ge4\text{ a power of two}).
$$

Some cluster has two members. Two transversals differing in that
single choice have distinct totals modulo $N$, so at least one has
nonzero total. This again gives a dissociated $(d+1)$-set, a
contradiction, and proves (4).

This does not establish the unrestricted cyclic odd bound.
A counterexample must occupy at least two signed classes modulo the
smallest power of two $q\ge d+1$. This modulus divides $N$: otherwise
$d\ge M$, when $|O|\le N/2\le2^d$ already excludes a counterexample.
The unresolved task remains a joint estimate for multiple occupied
classes and their doubled fibers, rather than separate estimates
for each class.
