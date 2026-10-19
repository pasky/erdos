---
name: research/erdos_132/four_point_collisions
title: Analytic four-point collisions increase rarity
desc: |
  A three-value Monge obstruction and reflection-pair analysis prove
  four cross distances for two collapsing four-point analytic clusters.
sources: []
research_state: closed
created: 2026-09-23T06:20:00Z
updated: 2026-09-24T22:12:56Z
---


# Analytic four-point collisions increase rarity

***

**Theorem.** Let $X_1(t),\ldots,X_4(t)$ and $Y_1(t),\ldots,Y_4(t)$ be
planar curves real-analytic at zero, distinct within each cluster for
all sufficiently small $t>0$. Suppose $X_i(t)\to p$, $Y_j(t)\to q$,
where $p\ne q$. Then there are at least four distinct cross-distances
for all sufficiently small $t>0$.

This extends [nonlinear_cluster_limits](nonlinear_cluster_limits.md)
from cluster sizes two and three to four. It does not reduce arbitrary
configurations to collision families or settle either Erdős assertion.

## A finite Monge lemma

A strictly Monge $4$ by $4$ matrix has at least four distinct entries.
If there are three, normalize them to $0<a<1$. According as $a<1/2$,
$a=1/2$, or $a>1/2$, replace them respectively by

$$ (0,1,3),\qquad(0,1,2),\qquad(0,2,3). $$

This preserves every comparison between sums of two entries: the only
non-fixed comparison between the six unordered pair sums is that of
$2a$ and $1$. The nine adjacent strict Monge defects are now positive
integers, with sum at least nine. Their sum telescopes to

$$M_{14}+M_{41}-M_{11}-M_{44}\le2(\max M-\min M)\le6,$$

a contradiction. For two values, normalization to $0,1$ gives the same
contradiction; a constant matrix is not strictly Monge.

## Analytic stabilization and nonflat pairs

Normalize $p=(0,0)$ and $q=(d,0)$, $d>0$. Every nonzero analytic germ
has a fixed sign near zero, so all finite equality and order patterns
below stabilize. Suppose for contradiction that the squared
cross-distances have at most three values.

A within-cluster pair is called flat when its vertical difference is a
nonzero germ and $\Delta x=o(\Delta y)$. For any nonflat pair, distinctness
and analyticity imply $\Delta x\not\equiv0$ and
$\Delta y=O(\Delta x)$. For a nonflat pair in the $X$ cluster,

$$
|X_i-Y_j|^2-|X_k-Y_j|^2=-2d\,\Delta x+o(\Delta x)
\tag{1}
$$

uniformly in the four columns. Thus its two rows are strictly pointwise
ordered. If such a pair occurs in the $Y$ cluster, interchange the
clusters. Choose a nonflat $X_1,X_2$ whose first row is larger.

With three palette values $A<B<C$, put $g=B-A$, $h=C-B$. The possible
ordered value pairs are

$$ (B,A),\quad(C,A),\quad(C,B), $$

with gaps $g,g+h,h$. Every occurring gap is asymptotic to the same
positive germ from (1), so all three types cannot occur. A single type
allows at most two $Y$ points, by intersection of the two distinct
circles about $X_1,X_2$. Hence exactly two types occur, each twice.
This also rules out a nonflat pair if the palette has at most two values.

The two points of any repeated type are reflections across $X_1X_2$.
Their midpoint lies on that axis and tends to $q$, while $X_1\to p$.
The axis therefore tends to $pq$. A parameter-dependent analytic rigid
motion puts

$$X_1=(0,0),\quad X_2=(s,0),\quad Y_j\to(d,0),\quad s>0,\ s\to0.$$

For the analyticity, factor $X_2-X_1=t^\ell v(t)$ with $v(0)\ne0$ and
use the analytic direction $v(t)/|v(t)|$. The strict ordering of the
rows orients the axis toward $q$. All occurring gaps are now
asymptotic to $2ds$.

## Unbalanced types

The types $(B,A),(C,A)$ put all four $Y$ points on a circle centered at
$O=X_2$, with squared radius $A$. The types $(C,A),(C,B)$ put them on
a circle centered at $O=X_1$, with squared radius $C$.

For any other cluster point $Z\ne O$, four pinned distances using three
values have a repetition. Thus $Z$ is on a perpendicular bisector of a
$Y$-chord. This line contains $O$ and the chord midpoint, whose
difference from $O$ tends to $(d,0)$. It follows that $Z-O$ is nonflat.
Its row is strictly ordered against the constant extreme row at $O$,
so uses only the other two palette values. Each occurs twice: a
constant row, or a value occurring three times, would violate the
two-circle intersection bound.

Reflection in $OZ$ therefore preserves all four $Y$ points. Such a
reflection fixes the nonzero vector

$$\sum_j(Y_j-O)\longrightarrow4(d,0),$$

so its axis is unique. The original axis already preserves $Y$.
Consequently all $X$ points lie on this axis. Two distinct noncentral
$X$ points have strictly ordered rows, each using the same two values
nonconstantly. This is impossible: strictly ordered binary rows must
be the constant high and constant low rows. Thus there are at most
two $X$ points, a contradiction.

## Balanced types

The remaining types are $(B,A),(C,B)$, and
$g\sim h\sim2ds$. Write

$$
Y=(a,\pm u),(c,\pm v),\qquad u,v>0,
$$
$$
a=\frac{g+s^2}{2s},\qquad
c=\frac{h+s^2}{2s},\qquad
\beta=c-a=\frac{h-g}{2s}.
$$

Here $a,c\to d$ and $u,v\to0$. The circle equations imply

$$v^2-u^2=h-(a+c)\beta. \tag{2}$$

Take another $X=(x,y)\to0$, first with $y\not\equiv0$. The differences
within its two mirror pairs are $4|y|u$ and $4|y|v$. Both belong to
$\{g,h,g+h\}$, giving

$$|y|u=\Theta(s),\qquad v=\Theta(u),\qquad
\beta=O(s+u^2).$$

Every squared distance differs from $B$ by $O(s)$. The first pair mean
therefore gives $x^2+y^2-2ax=O(s)$. Since $a\to d>0$ and $x\to0$,

$$x=O(s+y^2)=O(s+s^2/u^2),$$

and hence

$$
x\beta=O(s^2+su^2+s^3/u^2)=o(s).
\tag{3}
$$

For the last equality use $u\to0$ and $s/u=\Theta(|y|)\to0$.
The second pair mean minus the first is, by (2),
$h-2x\beta\sim2ds$. Each mean is one of

$$ (A+B)/2,\quad(A+C)/2,\quad(B+C)/2. $$

Only the largest minus the smallest has the required asymptotic gap.
Thus the first mirror pair uses $\{A,B\}$, and the second uses
$\{B,C\}$. Put $T=x^2+y^2$. Their means give

$$T-2ax=-g/2,\qquad T-2cx=-h/2,$$

so $2\beta x=s\beta$. If $\beta\not\equiv0$, analyticity permits
division near zero, giving

$$x=s/2,\qquad T=s^2/2,\qquad |y|=s/2.$$

Then the first pair gap gives $u=g/(2s)\to d$, contradicting $u\to0$.
If $\beta\equiv0$, then $g=h$, the pair gaps imply $u=v$, and (2)
would give $0=h>0$. No off-axis $X$ point exists.

For an on-axis $X$, the same distance estimate gives $x=O(s)$.
Its second-pair distance minus the first is asymptotic to $2ds$,
so the ordered pair of values is $(A,B)$ or $(B,C)$, not $(A,C)$.
The first-pair equation has roots respectively

$$x=s,\ 2a-s,\qquad\text{or}\qquad x=0,\ 2a.$$

The second root in each case tends to $2d$, leaving only the original
points $X_1,X_2$. This is again a contradiction.

## All-flat completion and rarity

There can therefore be no nonflat pair in either cluster. All vertical
coordinates are distinct as germs. Order each cluster by these
coordinates. For $i<k$, $j<\ell$, the positive vertical product dominates
the horizontal product, so

$$
D_{ij}+D_{k\ell}-D_{i\ell}-D_{kj}
=-2(X_i-X_k)\cdot(Y_j-Y_\ell)<0.
$$

The squared cross-distance matrix is strictly Monge, contradicting the
first lemma. The theorem follows.

As in [nonlinear_cluster_limits](nonlinear_cluster_limits.md), suppose
$A(t)$ has four analytic branches converging to each point of an
$N$-point base set $P$, with all $n=4N$ points distinct. Every rare base
distance has a limiting cross-distance group of at most
$16N=4n$ pairs, but at least four actual distance classes. Some such
class has multiplicity at most $n$. Distinct positive limiting groups
remain separate, and the largest internal cluster distance supplies one
additional rare class, by summing the four-point diameter bound.
Consequently

$$R(A(t))\ge R(P)+1$$

for all sufficiently small positive $t$. There is no generic-parameter
qualification. The author checked the full argument, including the
balanced asymptotics and the Monge normalization; it is author-recorded.
Neither the analogous arbitrary-cluster-size statement nor a reduction
of arbitrary point sets to these families has been established.
