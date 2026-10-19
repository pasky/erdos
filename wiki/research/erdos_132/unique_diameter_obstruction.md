---
name: research/erdos_132/unique_diameter_obstruction
title: A second rare distance whenever the diameter is unique
desc: |
  The sharp n+1 second-distance bound and convex equality classifications
  prove the first assertion for every configuration with a unique diameter.
sources: []
research_state: closed
created: 2026-09-22T22:15:00Z
updated: 2026-09-24T22:12:56Z
---


# A second rare distance whenever the diameter is unique

***

**New theorem.** Every planar $n$-point set with $n\ge5$ and a uniquely
attained diameter has at least two rare distances. The proof below
uses the equality structure in the sharp second-distance bound and
the convex minimum-distance classifications.

The subsequent [star-diameter theorem](star_diameter.md) extends this
to every set whose diameter pairs all share one endpoint.

The construction retained at the end is **not** a counterexample to
[Problem 132](../../problems/distance_problems/E0132/_index.md). For arbitrarily large
even $n$, the construction below has a unique diameter pair and exactly $n+1$
pairs at its second-largest distance. The latter graph has all $n$ vertices in
its $2$-core and vertex-cover number at least $(n-2)/2$. Thus neither of these
sizes is bounded merely by the number of diameter pairs.

## A unit-circle arc lemma

Let $p,q$ lie on the unit circle centered at $o$, and let their minor
arc have angle less than $\pi$. If $|x-p|,|x-q|\le1$, then for any
interior point $w$ of that arc,

$$|x-w|\le1,$$

with strict inequality unless $x=o$.

Translate $o$ to zero. We can write

$$w=\lambda p+\mu q,\qquad \lambda,\mu>0,\quad\lambda+\mu>1.$$

The last inequality follows from strict convexity of the unit disk.
The hypotheses give $2x\cdot p,2x\cdot q\ge|x|^2$, and hence

$$
|x-w|^2\le1-(\lambda+\mu-1)|x|^2.
$$

This proves the claim.

## The sharp upper bound and its equality structure

**Proposition.** If an $n$-point planar set has a unique diameter
pair $ab$ and has a second-largest distance $r$, then

$$m_A(r)\le n+1. \tag{1}$$

Normalize $r=1$, $a=0$, $b=(D,0)$, where $D>1$. Let $d$ be
the number of unit neighbors of $a$. For any such neighbor
$x=(\cos\theta,\sin\theta)$,

$$|x-b|\le1,\qquad \cos\theta\ge D/2.$$

When $d\ge2$, these neighbors therefore lie on an angular interval
of width less than $2\pi/3$. Their two extreme members $u,v$
are at distance at most one, so their angular separation is at
most $\pi/3$. The other $d-2$ neighbors form a set $L$ strictly
inside their minor unit-circle arc.

Every $w\in L$ has unit degree exactly one in $A$. Indeed, for
every $x\in A\setminus\{a\}$, both $|x-u|$ and $|x-v|$ are at
most one: neither pair is the exceptional diameter $ab$. The arc
lemma gives $|x-w|<1$. Thus the only unit neighbor of $w$ is $a$.

Delete $a$ and $L$. The remaining $n-d+1$ points have diameter
at most one and retain all $m_A(1)-d$ unit edges. The diameter
bound gives

$$m_A(1)-d\le n-d+1,$$

proving (1). If $d\le1$, simply deleting $a$ instead gives the
stronger $m_A(1)\le n$.

If equality $m_A(r)=n+1$ holds, then $d\ge2$ and the remaining
set $S_a=A\setminus(\{a\}\cup L)$ has exactly $|S_a|=n-d+1$
diameter-$r$ edges. Every point of $S_a$ is diameter-active:
deleting an isolated point otherwise violates the diameter bound.
By [diameter completion](constant_width.md), $S_a$ lies on the
boundary of one constant-width-$r$ body. In particular it is
strictly convex. The same decomposition holds at the other
diameter endpoint.

The decomposition leaves an arc of $d-2$ pendant points, whose size
need not be bounded. Nevertheless, using both diameter endpoints
at once gives a decisive convexity reduction, as follows.

## The unique-diameter theorem

We first prove the stronger distance-count statement: for $n\ge10$,

$$
ab\text{ is the unique diameter pair},\quad m_A(r)=n+1
\quad\Longrightarrow\quad q(A)\ge\lfloor n/2\rfloor+1,
\tag{2}
$$

where $r$ is the second-largest distance.

The equality decomposition shows that every point of $A$ is
$r$-active. This includes $a$, its deleted leaves, and all points
of $S_a$. Put $C=A\setminus\{a,b\}$ and $m=n-2$. For any $x\in C$,
choose an $r$-neighbor $y\in A$. The closed disk of radius $r$
centered at $y$ contains every point of $C$: the only pair longer
than $r$ in all of $A$ is $ab$. The tangent line to this disk at
$x$ supports $\operatorname{conv}(C)$ uniquely at $x$. Thus $C$
is in strictly convex position, including when $y$ is one of
the deleted endpoints.

Suppose, contrary to (2), that $q(A)\le\lfloor n/2\rfloor$.
The diameter disappears on deleting $a,b$, so Altman's convex
lower bound gives

$$
\lfloor m/2\rfloor\le q(C)\le q(A)-1
\le\lfloor n/2\rfloor-1=\lfloor m/2\rfloor.
\tag{3}
$$

All these inequalities are equalities. In particular the distance palette of $A$
consists exactly of the palette of $C$ and the unique diameter. Theorems 1 and 2
of the supplied
[Fishburn paper](../../../library/distance_problems/fishburn_1995_convex_polygons_few_intervertex_distances/_index.md)
now apply: for odd $m$, $C$ is a regular $m$-gon; for even $m\ge8$, it is a
regular $m$-gon or a regular $(m+1)$-gon with one vertex deleted. Both theorem
statements and their size hypotheses were checked in the full source.

If $m$ is odd, write $m=2s+1$. An additional point $p$ different
from the circumcenter has at most two neighbors of any given
distance on the circle of $C$. But its $m=2s+1$ distances to $C$
must all lie in the old palette of $s$ distances, which is
impossible. The circumcenter is impossible as well: its distance
to every vertex is the circumradius, and a regular odd polygon
has no chord of that length. Indeed $2\sin(\pi j/m)=1$ for an
allowable chord would require $6\mid m$.

If $C$ is a regular even $m$-gon of circumradius $R$, (3) makes
$r=2R$. Inside $C$ it occurs $m/2$ times. Each of $a,b$, unless
the circumcenter, contributes at most two further such pairs;
the circumcenter contributes none. Their mutual pair is longer.
Consequently

$$m_A(r)\le m/2+4=n/2+3\le n,$$

contrary to $m_A(r)=n+1$.

It remains that $C=V\setminus\{v\}$ for a regular odd polygon
$V$ of size $k=m+1=2s+1$. Normalize its circumradius to one,
its center to zero, and its missing vertex to $v=1$ in complex
coordinates. Its $s$ chord values all survive in $C$. Any point
$p\in\{a,b\}$ must have all its $2s$ distances to $C$ in this
palette. The circumcenter is excluded as before. Every allowable
distance must therefore occur exactly twice in this pinned list.

Reflection in the line $0p$ exchanges the two circle points at
each such distance, and hence preserves $C$. Since
$\sum_{z\in C}z=-1$, this reflection fixes $1$. Therefore
$p=\rho\in\mathbb R\setminus\{0\}$. Set
$c_j=\cos(2\pi j/k)$ for $1\le j\le s$. Equality of pinned and
chord squared-distance palettes reads

$$
\{1+\rho^2-2\rho c_j:1\le j\le s\}
=\{2-2c_j:1\le j\le s\}.
$$

Comparing their ranges, which are nonzero, gives $|\rho|=1$.
If $\rho=-1$, equality of their sums would give
$\sum_jc_j=0$, whereas $1+2\sum_jc_j=0$. Thus $\rho=1$:
the only possible added point is the missing vertex. Applying
this to both $a$ and $b$ makes them coincide, a contradiction.
This proves (2).

Finally suppose $R(A)=1$ and the diameter is unique. Every other
class has at least $n+1$ pairs, so

$$\binom n2\ge(q(A)-1)(n+1)+1,$$

which rearranges to $q(A)\le n/2$. The sharp bound (1) forces
$m_A(r)=n+1$. For $n\ge10$, (2) contradicts
$q(A)\le\lfloor n/2\rfloor$. Orders $5\le n\le9$ are already
covered by the checked [small-order theorem](small_orders.md).
This proves the stated unique-diameter theorem.

In particular, an unrestricted counterexample must have at least
two diameter pairs. At even order it must also satisfy
$q(A)\le n/2-1$: equality in the elementary pair budget at
$q(A)=n/2$ would force the diameter to occur uniquely.
Neither conclusion controls all sets with multiple diameter pairs,
and no uniform asymptotic rarity bound follows from this proof.

A separate author developed the convexity reduction and the
classification proof; the author checked the disk support argument,
all palette counts, and the missing-vertex calculation. The proof is
author-recorded.

## Construction and all distance checks

Let $\ell\ge5$ be odd, put

$$
\alpha=\frac{\pi}{\ell},\qquad
R=\frac1{2\cos(\alpha/2)},
$$

and take the regular polygon

$$C=\{Re^{2\pi ij/\ell}:0\le j<\ell\}.$$

Its diameter is one and has exactly $\ell$ pairs. Its diameter graph
is an odd cycle: the longest chords advance by $(\ell-1)/2$ indices,
which is coprime to $\ell$.

Set

$$
u=(R,0),\qquad a_\pm=Re^{\pm2i\alpha},\qquad
c_\pm=Re^{\pm i(\pi-\alpha)},\qquad v_0=(R-1,0).
$$

The two unit neighbors of $u$ in $C$ are $c_\pm$.
The point $v_0$ is in the interior of the minor unit-circle arc from
$c_+$ to $c_-$ centered at $u$. Applying the arc lemma to each
$c\in C\setminus\{u\}$ gives

$$|v_0-c|<1.$$

For a sufficiently small positive $\eta$, put

$$v=(R-1-\eta,0).$$

Then $|u-v|=1+\eta$, whereas $|v-c|<1$ for every other $c\in C$.

The vertices $u,a_+$ lie on a unit circle centered at $c_-$.
The minor arc between them has angle $\alpha$. Similarly $u,a_-$
lie on a minor unit-circle arc centered at $c_+$.
Intersect the unit circle centered at $v$ with these two arcs near
$u$, obtaining $w_+$ and $w_-$, respectively.

Here is an explicit local existence check. At $\eta=0$ the two circle
gradients for the upper intersection are proportional to

$$u-v_0=(1,0),\qquad u-c_-=(\cos(\alpha/2),\sin(\alpha/2)).$$

They are linearly independent. The implicit-function theorem gives an
intersection near $u$, and differentiating the two circle equations
gives

$$
w_+-u=(-\eta,\eta\cot(\alpha/2))+O(\eta^2).
$$

This is the direction into the required arc. Reflection gives

$$w_--u=(-\eta,-\eta\cot(\alpha/2))+O(\eta^2).$$

For sufficiently small $\eta$, these are distinct interior arc points,
different from all points of $C$ and from $v$.

By the arc lemma, $w_+$ has distance at most one from every point
of $C$, with equality exactly for its circle center $c_-$. The
analogous unique unit neighbor of $w_-$ in $C$ is $c_+$.
Also $|w_+-w_-|<1$: apply the lemma to the upper arc with $x=w_-$,
whose distances to the two arc endpoints $u,a_+$ are already at
most one. By construction, $|v-w_\pm|=1$.

Thus

$$A=C\cup\{v,w_+,w_-\},\qquad n=\ell+3,$$

has unique diameter $1+\eta$, attained by $uv$. Its second-largest
distance is one, and its unit pairs are exactly the $\ell$ original
cycle edges and

$$c_+w_-,\quad w_-v,\quad vw_+,\quad w_+c_-.$$

Their number is $\ell+4=n+1$.

## Structural consequence and limitation

The unit graph is the odd $\ell$-cycle with an additional four-edge
path between $c_+$ and $c_-$. Every vertex has degree at least two,
so the entire graph is its $2$-core. Every vertex cover must cover
the original odd cycle, and hence has at least

$$\lceil\ell/2\rceil=(n-2)/2$$

vertices.

The [small-cover restriction](layers_and_obstructions.md) remains
valid, but this family prevents a constant cover-size hypothesis from
being deduced just from a singleton diameter and richness of the
second distance. It says nothing sufficient about multiplicities at
smaller distances. In fact it contains a regular $(n-3)$-gon, so the
[regular-core theorem](regular_cores.md) gives linearly many rare
distances for large members of the family.
