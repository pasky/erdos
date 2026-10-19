---
name: research/erdos_132/regular_cores
title: Linear rarity from regular cores and a majority on a circle
desc: |
  Gives regular-core bounds and an elementary small-difference proof of
  the explicit circular bound R at least h minus n/2 minus 10n^(6/7).
sources: []
research_state: closed
created: 2026-09-22T22:10:00Z
updated: 2026-09-24T22:12:56Z
---


# Linear rarity from regular cores and a majority on a circle

***

The unrestricted questions in
[Problem 132](../../problems/distance_problems/E0132/_index.md) remain unresolved. The
results below concern substantial additional families; they do not extract a
regular or circular core from arbitrary sets. All multiplicities count unordered
pairs. The arguments were checked by the author and are author-recorded; no
novelty claim is made.

The later [cosine-incidence argument](circle_incidence.md) proves an
asymptotic linear bound from **any** fixed positive fraction of
concyclic points, without requiring a regular core or a majority.
The quantitative regular-core proof below remains independently valid.

## Results

**Dense regular-core theorem.** Fix $C\ge1$. Suppose an $n$-point
planar set $A$ contains $m>k/2$ vertices of a regular $k$-gon, and


$$
n\le Cm.
$$


For all sufficiently large $k$, depending only on $C$,


$$
R(A)\ge k/4. \tag{1}
$$


In particular, containing a regular polygon of any fixed positive
fraction of the total cardinality forces linearly many rare distances.
The core need not account for almost all points.

**Circular-majority theorem.** Fix $0<\varepsilon\le1/2$. Suppose


$$
m\ge(1/2+\varepsilon)n
$$


points of $A$ lie on one circle. For all sufficiently large $n$,
depending only on $\varepsilon$,


$$
R(A)\ge\frac{2m-n}{6}. \tag{2}
$$


Unlike the [one-off-circle argument](circular_configurations.md), this
allows a positive fraction of arbitrary off-circle points. The original
proof used Kneser's addition theorem; the elementary small-difference
lemma below replaces that input. The review of
the [third independent report](independent/layer_bound_and_circular_majority.md)
also gives the fully explicit bound


$$
R(A)\ge h-\frac n2-10n^{6/7} \tag{A}
$$


when a circle contains $h$ points. For a fixed circular majority this is
asymptotically weaker than the later [circle theorem](circle_incidence.md),
which gives $(h-1)/2-O(n^{2/3})$ with a uniform constant for $h\ge n/2$.
Its value here is its explicit constant and elementary, self-contained
proof, not a larger scope or a better circle-concentration threshold.

## A cosine-grid intersection bound

For $k\ge3$, put


$$
h=\frac{2\pi}{k},\qquad E_k=12\bigl(1+(2k)^{2/3}\bigr).
$$


Consider the two sets


$$
U=\{a-b\cos(jh+\alpha):j\in\mathbb Z/k\mathbb Z\},
\quad
U'=\{a'-b'\cos(jh+\alpha'):j\in\mathbb Z/k\mathbb Z\},
$$


where $b,b'>0$ and $(a,b)\ne(a',b')$. Then


$$
|U\cap U'|\le E_k. \tag{3}
$$


Fold the angular grids into $[0,\pi]$. Each folded grid is contained
in two translates of $h\mathbb Z$. Equality of values at folded
angles $x,y$ is equivalent to


$$
y=f(x)=\arccos(A+B\cos x),\qquad
A=\frac{a'-a}{b'},\quad B=\frac b{b'}>0.
$$


Its domain is an interval. On the nondegenerate interior the function
is strictly increasing, and the sign of $f''(x)$ is the sign of


$$
-AB\cos^2x+(1-A^2-B^2)\cos x-AB.
$$


This polynomial is identically zero only for $A=0,B=1$, excluded by
the parameter hypothesis. It has at most two roots in the domain.
Thus the graph splits into at most three strictly convex or strictly
concave pieces. Domain endpoints can be included in adjacent pieces;
an empty or singleton domain causes no difficulty.

Fix one piece and one of the four pairs of translated grids. After
scaling both coordinates by $k/(2\pi)$, the coincidence points lie
in a translate of $\mathbb Z^2$, increase strictly in both
coordinates, and have total Manhattan span at most $k$.
If there are $q$ such points, their $s=q-1$ consecutive gap
vectors are positive integral vectors with distinct slopes, hence
distinct vectors. At most $s/2$ positive integral vectors have
Manhattan norm at most $\sqrt s$, since their number is at most


$$
\frac{\lfloor\sqrt s\rfloor(\lfloor\sqrt s\rfloor-1)}2\le s/2.
$$


Consequently $k\ge s^{3/2}/2$, giving


$$
q\le1+(2k)^{2/3}.
$$


Summing over the three pieces and four grid pairs proves (3).
This supplies the same bound used in the earlier fixed-ring argument,
now with its proof included for the present application.

## Few distance values force few dihedral orbits

Normalize the regular $k$-gon $V$ to the unit circle centered at
zero, and let $B\subseteq A\cap V$, with $|B|=m$.
Write $q=|D(A)|$ for the number of positive distances and $q_0=q+1$,
allowing zero when working with squared distances.

Let $H$ be the number of orbits of the dihedral group $D_k$ meeting
$A\setminus\{0\}$. Choose a representative
$p_i=\rho_i e^{i\phi_i}$ from each occupied orbit. Its full pinned
spectrum to $V$ is


$$
T_i=\{1+\rho_i^2-2\rho_i\cos(jh-\phi_i):j\in\mathbb Z/k\mathbb Z\}.
$$


Use the actual pinned subsets


$$
U_i=\{|p_i-b|^2:b\in B\}\subseteq T_i.
$$


Since $\rho_i>0$, a given value has at most two preimages on the
circle. Hence


$$
m/2\le |U_i|\le m.
$$


Every $U_i$ lies in the $q_0$ nonnegative squared distances of $A$.
For different representatives,


$$
|U_i\cap U_j|\le E_k. \tag{4}
$$


Indeed, if $\rho_i\ne\rho_j$, their parameter pairs
$(1+\rho_i^2,2\rho_i)$ differ, so (3) applies to $T_i,T_j$.
If the radii agree, even one common value would imply
$\phi_i\equiv\pm\phi_j\pmod{2\pi/k}$, contradicting the choice of
different $D_k$-orbits. Their full spectra are then disjoint.

If $d(s)$ counts the sets $U_i$ containing a squared value $s$,
Cauchy--Schwarz and (4) give


$$
\frac{H^2m^2}{4}
\le\left(\sum_s d(s)\right)^2
\le q_0\sum_s d(s)^2
\le q_0(Hm+H^2E_k).
$$


Thus


$$
H(m^2-4q_0E_k)\le4q_0m. \tag{5}
$$


Notice that $B$ need not be invariant under $D_k$. Only the full
spectra $T_i$ are used for overlap control; the actual $U_i$ are
used to count values occurring in $A$.

## Chords occurring only on the core circle

The occupied dihedral orbits are contained in at most $2H$
concentric regular $k$-gons: each dihedral orbit is the union of at
most two rotation orbits. These auxiliary polygons may contain
additional points not in $A$; this enlargement is used only to
bound possible distance values.

Let $S\subseteq D(B)^2$ be any collection of squared chord values
that occur in $B$. An unordered pair of auxiliary polygons,
including a polygon paired with itself, has squared-distance spectrum


$$
\{r_i^2+r_j^2-2r_ir_j\cos(jh+\eta):j\in\mathbb Z/k\mathbb Z\}.
$$


Unless both radii are one, its parameter pair differs from $(2,2)$.
By (3), it contains at most $E_k$ values of $S$, since $S$ is
contained in the full unit-polygon chord spectrum. There are at most
$H(2H+1)$ unordered polygon pairs. If the center belongs to $A$,
pairs involving it supply at most $H$ further values, one per
occupied radius.

After excluding these values, every remaining value in $S$ occurs
only between points of $A$ on the unit circle. Its distance graph
has maximum degree at most two, so it has at most $n$ unordered
edges. Therefore


$$
R(A)\ge |S|-H(2H+1)E_k-H. \tag{6}
$$


## Proof of the dense regular-core theorem

There are fewer than $n/2$ rich distances, by the total pair count.
Thus $R(A)>q-n/2$. If


$$
q\ge n/2+k/4,
$$


then (1) follows. Otherwise, using $n\le Cm$ and $k<2m$,


$$
q_0<n/2+k/4+1\le(C+1)m.
$$


Since $E_k=O(k^{2/3})=o(m)$, for all sufficiently large $k$ we
have $E_k\le m/[8(C+1)]$. Equation (5) then implies


$$
H\le8q_0/m\le8(C+1).
$$


Every chord length of $V$ occurs in $B$. Indeed, deleting
$t=k-m<k/2$ vertices removes at most $2t<k$ edges from a
nondiametral class, which originally had $k$ edges. When $k$ is
even, deletion removes at most $t<k/2$ edges from its diametral
class, which originally had $k/2$ edges. Hence in (6) we may take
$|S|=\lfloor k/2\rfloor$.

Putting $H_0=\lceil8(C+1)\rceil$ now gives


$$
R(A)\ge\lfloor k/2\rfloor-H_0(2H_0+1)E_k-H_0\ge k/4
$$


for sufficiently large $k$. An explicit, very loose sufficient
threshold is


$$
k\ge\left[512H_0(2H_0+1)\right]^3.
$$


To check it, use $E_k\le32k^{2/3}$. The threshold guarantees the
condition in (5), bounds the $E_k$ term by $k/16$, and bounds
$H_0+1$ by $k/8$, including the floor loss.

More generally, if $B$ has $m$ vertices in a regular $k$-gon,
$k\le Dm$, and $n\le Cm$, with fixed $C,D$, then


$$
R(A)\ge m/4
$$


for sufficiently large $m$. Split instead at $q=n/2+m/4$.
Equation (5) again bounds $H$; in (6) take the actual chord spectrum
of $B$, which has at least $(m-1)/2$ values by pinning one point.
This does not require density greater than one half.

## An elementary small-difference lemma

**Lemma.** Let $S$ be a finite nonempty subset of an abelian group, with
$a=|S|$ and $b=|S-S|<2a-1$. After translating $S$ to contain zero,
there is a finite subgroup $H\le\langle S\rangle$, of order $M$, such
that, if $S$ meets $k$ cosets of $H$, then


$$
M\ge2a-b,\qquad b=(2k-1)M,\qquad kM-a<M/2. \tag{B}
$$


Moreover $S-S$ is a union of complete $H$-cosets.

Write $G=\langle S\rangle$. If $S-S=G$, take $H=G$: then $G$ is
finite, $k=1$, and all conclusions follow from $a\le b<2a-1$.
Otherwise minimize


$$
f(X)=|X+S|-|X|
$$


over nonempty finite $X\subseteq G$ with $X+S\ne G$. The minimum $\kappa$
exists, since $f(X)$ is a nonnegative integer, and $X=-S$ gives
$\kappa\le b-a<a-1$. Choose a minimizer $U$ of least size,
translated so that $0\in U$.

We first justify applying submodularity to intersecting translates
$U,V$ of this minimizer. If $G$ is infinite, their union is admissible
because it is finite. If $G$ is finite, set $E=G\setminus(U+S)$.
The minimum expansion for $-S$ equals $\kappa$ by reflection, while


$$
E-S\subseteq G\setminus U,\qquad
|E-S|-|E|\le\kappa.
$$


Thus $E$ is a minimizer for $-S$, and $-E$ is one for $S$.
Minimality of $|U|$ gives $|E|\ge|U|$, hence
$|G|\ge2|U|+\kappa$. If $(U+S)\cup(V+S)=G$, their intersection
would have size at most $\kappa$, but it contains $x+S$ for any
$x\in U\cap V$, of size $a>\kappa$. This is impossible. So
$U\cup V$ is admissible in the finite case as well.

The inclusions for sumsets of intersections and unions imply


$$
f(U\cap V)+f(U\cup V)\le f(U)+f(V)=2\kappa.
$$


Both terms on the left are at least $\kappa$. The intersection is
therefore a minimizer, and least cardinality forces $U=V$.
For every $u\in U$, the sets $U$ and $U+u$ intersect at $u$, so
$U+u=U$. Consequently $U$ is a finite subgroup $H$.

Let $M=|H|$ and let $k$ count the occupied cosets. Then
$\kappa=(k-1)M$, and $u=kM-a$ satisfies


$$
u<M,\qquad 2a-b\le a-\kappa=M-u\le M.
$$


Here $k\ge2$: otherwise $S\subseteq H$, so $G=H$ and $H+S=G$,
contrary to admissibility. Any two distinct occupied fibers have total size
at least $2M-u>M$. Their differences fill the corresponding coset
of $H$. At least one fiber has more than $M/2$ points, so its
self-difference fills $H$ too. Hence $S-S$ is a union of $H$-cosets.
Finally


$$
b\ge a+\kappa=(2k-1)M-u>(2k-2)M,
\qquad b<2a\le2kM.
$$


Divisibility by $M$ forces $b=(2k-1)M$, and $b<2a$ now gives
$u<M/2$. This proves (B). The finite-group admissibility step and
the distinction between $k=1$ and $k\ge2$ are essential.

## From a circular majority to a dense regular core

Write $b=R(A)\ge1$. Counting at least $n+1$ pairs per rich class
and at least one per rare class gives


$$
\binom n2\ge(q-b)(n+1)+b,
\quad
q\le\frac n2+b-1+\frac{1-b}{n+1}\le\frac n2+b-1. \tag{7}
$$


Represent the $m$ points on the given circle by their angular
coordinates $B\subset\mathbb R/\mathbb Z$. The two oriented angular
differences corresponding to a chord are negatives of one another,
so for $d=|B-B|$,


$$
d\le2q+1\le n+2b-1. \tag{8}
$$


Put $\delta=2m-n\ge2\varepsilon n$, and suppose, toward a
contradiction, that $b<\delta/6$. Then (8) gives $d<2m-1$.
Apply (B) to obtain a finite subgroup $G$, of order $g$, with $B$
meeting $j$ cosets and


$$
d=(2j-1)g,
\qquad g\ge2m-d. \tag{9}
$$


This replaces the original use of Kneser's theorem in precisely the
small-difference regime needed here; no general sumset theorem is
claimed. Equations (8)--(9) imply


$$
d<2m,\qquad
g\ge2m-d\ge\delta-2b+1>2\delta/3\ge4\varepsilon n/3.
$$


Moreover $m>d/2\ge(j-1/2)g$. Since each occupied coset has at
most $g$ points, every occupied coset must contain more than
$g/2$ points; otherwise their total would be at most
$(j-1/2)g$.

A finite subgroup of $\mathbb R/\mathbb Z$ of order $g$ is
$\{0,1/g,\ldots,(g-1)/g\}$. Choose one occupied coset. Its
corresponding points form a subset of more than half the vertices
of a regular $g$-gon. If it contains $s$ points, then


$$
s>g/2>2\varepsilon n/3,
\qquad n<\frac{3}{2\varepsilon}s.
$$


The dense regular-core theorem applies uniformly as $n\to\infty$,
because $g\ge4\varepsilon n/3$. It gives


$$
b\ge g/4>\delta/6,
$$


the required contradiction. This proves (2).

## Explicit transfer from shifted angular grids

Here is a checked proof of (A), rather than reliance on the independent
report's unavailable companion files. Let $B=A\cap C$, $|B|=h$, and
normalize $C$ to the unit circle. Taking every point of $A$ on $C$
can only strengthen (A). Suppose the angular set $S\subset\mathbb R/\mathbb Z$
meets $k$ cosets of the subgroup of order $M$, and $S-S$ meets $l$
such cosets. Define


$$
J(M)=27M^{2/3}+17,\qquad F=klJ(M).
$$


Every off-circle, noncentral point $p$ has at most $F$ neighbors in
$B$ whose distances to $p$ occur within $B$. To check the constant,
write $p=\rho e^{i\phi}$, with $\rho>0$, $\rho\ne1$. For a
source coset and a difference coset, the incidence equation is


$$
\cos y=c+\rho\cos x,\qquad c=(1-\rho^2)/2.
$$


Fold the source angle relative to $\phi$ into $x\in[0,\pi]$,
keeping the two semicircle branches separate. Each branch is contained
in one translated grid of step $2\pi/M$. Take the principal difference
angle $y\in[0,\pi]$. Because $S-S$ is symmetric, its principal
representatives still belong to its $l$ cosets; each target coset
is contained in one grid of the same step.

On its nonsingleton domain, an interval in $[0,\pi]$,
$f(x)=\arccos(c+\rho\cos x)$ is strictly increasing. The sign of
$f''$ in the interior is the sign of


$$
(1-c^2-\rho^2)\cos x-c\rho(1+\cos^2x).
$$


This polynomial is not identically zero, since that would force
$c=0,\rho=1$. There are at most two zeros, giving at most three
strictly convex or strictly concave pieces. On each piece, scale both
axes by $M/(2\pi)$. The coincidence points lie in a translate of
$\mathbb Z^2$, strictly increase in both coordinates, and have total
Manhattan span at most $M$. The distinct-gap argument proving (3)
therefore bounds their number by $1+(2M)^{2/3}$. The two source
branches and three pieces give at most


$$
6\bigl(1+(2M)^{2/3}\bigr)\le J(M)
$$


incidences per coset pair. Endpoints may be included in adjacent pieces,
only overcounting; a singleton domain gives at most two source vertices.
Keeping folded branches separate also handles two vertices with the
same folded angle. Summing proves the bound $F$.

Put $t=n-h$. Every chord class in $B$ has at most $h$ unordered
pairs, and $B$ determines at least $\lfloor h/2\rfloor$ distances.
Discard the circumradius class if necessary, to avoid incidences from
the center. The other old classes receive at most
$tF+\binom t2$ new pairs in total. Each that becomes rich must
receive at least $t+1$ new pairs. Thus


$$
R(A)\ge\left\lfloor\frac h2\right\rfloor-1
-\frac{tF+\binom t2}{t+1}
\ge h-\frac n2-F-1. \tag{C}
$$


For the second inequality when $t\ge1$, use
$\lfloor h/2\rfloor\ge(h-1)/2$ and
$\binom t2/(t+1)\le(t-1)/2$. If $t=0$, (C) follows directly
from $R(A)\ge\lfloor h/2\rfloor$.

Now write $s=R(A)$ and $y=h-n/2-s$. Pair counting as in (7) gives


$$
b:=|S-S|\le2q(A)+1\le n+2s=2h-2y.
$$


If $y>1/2$, (B) applies and supplies
$M\ge2y$, $l=b/M=2k-1$, and $k\le l$. Also $b<2n$.
Since $J(M)\le44M^{2/3}$, we obtain


$$
F\le44(b/M)^2M^{2/3}
\le\frac{176n^2}{(2y)^{4/3}}.
$$


By (C), $y\le F+1$. For $y\ge2$, it follows that


$$
y^{7/3}\le\frac{352}{2^{4/3}}n^2<10^{7/3}n^2.
$$


The case $y<2$ is immediate, proving (A).

The same transfer also verifies the report's regular-polygon bound.
If $m$ points belong to a regular $M$-gon, increase $m$ to the actual
number of such points if necessary; proving (D) for the larger $m$
suffices. Let $B$ consist of these $m$ vertices. A point on the
polygon's circumcircle but not a
vertex has no distances to its vertices in the polygon's chord
palette: equality would force its angle onto the same grid.
For all other noncentral points the preceding bound applies with
$k=l=1$ and $F=J(M)$. The pair budget gives


$$
R(A)\ge m-\frac n2-27M^{2/3}-18. \tag{D}
$$


The center exception and the strict richness cost $t+1$ must not be
omitted. Neither (C) nor (D) is a transfer principle for an arbitrary
convex subset. The author checked (B), the folded-grid incidence
proof, the pair budget, and the numerical constants; the argument is
author-recorded.

## The remaining unrestricted gap

The [layer reduction](layers_and_obstructions.md) forces a hypothetical
bounded-$R$ sequence to have a positive fraction in finitely many
outer convex layers. It does not make such a layer circular, regular,
or a dense subset of a regular polygon. Neither (1) nor (2) fills
that structural gap. No configuration refuting either unrestricted
assertion, and no proof of either assertion, has been obtained.
