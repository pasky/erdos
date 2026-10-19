---
name: research/erdos_132/three_off_circle
title: Two rare distances with all but three points on a circle
desc: |
  Explicit regular-polygon palette extensions and radius-palette moments
  prove the first assertion when n minus three points are concyclic.
sources: []
research_state: closed
created: 2026-09-23T07:03:23Z
updated: 2026-09-24T22:12:56Z
---


# Two rare distances with all but three points on a circle

***

**Theorem.** Let $A$ be an $n$-point planar set, $n\ge5$. If $n-3$
points of $A$ are concyclic, then $R(A)\ge2$.

The other three points may be anywhere. The proof extends the
[two-off-circle theorem](two_off_circle.md) by two further
regular-polygon palette lemmas and three radius-palette tests. It uses
the checked [small-order theorem](small_orders.md), the
[unique-diameter theorem](unique_diameter_obstruction.md), and the
elementary small-difference lemma already proved in the two-off-circle
note. No asymptotic circle theorem or general near-minimum convex
classification is needed.

The argument below was developed by a separate author and checked by the author;
it is author-recorded. This note concerns a restricted family, not the
unrestricted questions in
[Problem 132](../../problems/distance_problems/E0132/_index.md).

## 1. Two further regular-polygon palette extensions

Let $V$ be a regular $k$-gon on the unit circle, and let $P(V)$ be its
positive chord-length palette.

**Palette extension lemma.** No point off the circumcircle and off its
center has all distances to $C$ in $P(V)$ in either of these cases:

- $k\ge8$ is even and $C$ is $V$ minus two vertices;
- $k\ge9$ is odd and $C$ is $V$ minus three vertices.

Write $M=\lfloor k/2\rfloor$. In both cases $|C|=2M-2>M$. A
noncentral pin has at most two circle points at any prescribed distance,
so at least one pinned distance is repeated. Reflection in the line
joining the center to the pin exchanges its two circle points. Since
these points are vertices of $V$, this line is a reflection axis of $V$.
Different reflection orbits give different pinned values. As there are
at most $M$ available values, at most two singleton reflection orbits
survive in $C$.

### 1.1. Even order: reflection patterns

An edge-midpoint axis has no fixed vertices. If the two holes are not
exchanged by reflection, every pinned orbit survives. The pin then has
the same spectrum as on $V$, contrary to the existing
[even full-polygon palette lemma](two_off_circle.md). Thus its holes
form an exchanged pair.

A vertex axis has two fixed vertices. If exactly one hole is fixed,
deleting the other hole, which is one member of a pair, leaves the
pinned spectrum unchanged from $V$ minus the fixed hole. The existing
even one-hole lemma excludes this. If neither hole is fixed and they
are not exchanged, four singletons survive, impossible. If neither is
fixed and they are exchanged, both fixed vertices survive, and there
are $M$ pinned values. Thus the pinned palette equals $P(V)$. Its
maximum is $|p|+1$, whereas $\max P(V)=2$, forcing $|p|=1$.
The only remaining vertex-axis case has the two fixed vertices as holes.

Put

$$a=\pi/k,\qquad c=\cos a,\qquad T=\cos(2a),\qquad s=\sin a.$$

Here $0<a\le\pi/8<\pi/6$.

### 1.2. Even order: an edge axis with exchanged holes

Orient the axis toward the pin and put $r=|p|>0$. Its cosine list is

$$E=\{\cos((2j-1)a):1\le j\le M\}\setminus\{e_t\}.$$

There are $M-1$ pinned values, so their squared palette equals

$$\{2-2\cos(2ja):1\le j\le M\}\setminus\{d_u^2\}.$$

The full midpoint cosine list has range $2c$, reduced to $2cT$ if
one endpoint is deleted. The target cosine list has range $2c^2$,
$2T^2$, or $2T$, according as the omitted entry is interior, first,
or last.

Suppose the nearest pair, at angle $a$, survives. Comparing the
squared-distance ranges gives

$$\frac{T^2}{c}\le r\le\frac cT.$$

Both endpoints lie strictly between $c-\sqrt3s$ and $c+\sqrt3s$.
Indeed,

$$c-\frac{T^2}{c}=\frac{s^2(4c^2-1)}c<\sqrt3s,
\qquad
\frac cT-c=\frac{2cs^2}{T}<\sqrt3s.$$

The first inequality follows from
$(4c^2-1)\tan a<3\tan a<\sqrt3$, and the second from
$\tan(2a)<\sqrt3$. Therefore the smallest pinned square is

$$(r-c)^2+s^2<4s^2,$$

smaller than the shortest squared chord, a contradiction.

If the nearest pair is deleted, the smallest surviving angle is $3a$.
Its distance is at least $\sin(3a)>2\sin a$. Thus the shortest chord
is absent from the pinned spectrum: the target omits its first entry.
Range comparison now gives $r=T/c$. But

$$
\bigl(1+r^2-2r\cos(3a)\bigr)-4\sin^2(2a)
=\frac{(T-1)(4T+3)}{T+1}<0,
$$

contrary to matching the new smallest target chord.

### 1.3. Even order: a vertex axis with fixed holes

The cosine list is

$$\{\cos(2ja):1\le j\le M-1\},$$

of range $2T$. It is symmetric, so the sign of the real pin is
irrelevant. If the target omits its first, last, or an interior chord,
range comparison gives, respectively,

$$r=T,\qquad r=1,\qquad r=\frac{1+T}{2T}.$$

The middle case is on the circle. In the first case the smallest
pinned square is $1-T^2$, while the smallest target square is
$4(1-T^2)$. In the last case minimum equality would require
$r^2=2-T$, whereas

$$r^2-(2-T)=\frac{(T-1)^2(4T+1)}{4T^2}>0.$$

This proves the even part of the lemma.

### 1.4. Odd order: reduction to one deletion in two cosine lists

There is one fixed vertex. If it is deleted and the other two holes
are not exchanged, no paired pinned orbit disappears. The pin has
the same spectrum as $V$ minus its fixed vertex, excluded by the
existing [odd one-hole lemma](two_off_circle.md).

If the fixed vertex survives, the three holes must contain an exchanged
pair; otherwise four singleton orbits survive. The third hole removes
just one vertex of a surviving pair. Thus the pinned spectrum is the
same as for $V$ minus the exchanged pair, excluded by the existing
odd two-hole lemma.

The remaining holes are the fixed vertex and one exchanged pair.
Normalize the fixed vertex to $1$ and write the pin as signed real
$\rho$, where $\rho\ne0$ and $|\rho|\ne1$. Put

$$
a=\pi/k,\quad c=\cos a,\quad t=\cos(2a),\quad
w=\cos(4a),\quad v_3=\cos(3a),
$$

and

$$F=\{\cos(2ja):1\le j\le M\}.$$

There are $M-1$ pinned values. Hence, for sets $E$ and $G$ each
obtained from $F$ by deleting one entry,

$$G=\rho E+(1-\rho^2)/2. \tag{1}$$

For either deletion, use type I for an interior deletion, type F for
a first-entry deletion, and type L for a last-entry deletion. Their
extrema are as follows.

| Type | Maximum | Negative minimum | Range |
| --- | --- | --- | --- |
| I | $t$ | $c$ | $L_0=t+c$ |
| F | $w$ | $c$ | $L_1=w+c$ |
| L | $t$ | $v_3$ | $L_2=t+v_3$ |

Set $u=2c-1$ and $v=4c^2-2c-1$. Direct factorization gives

$$L_0=(1+c)u,\qquad L_1=(1+c)uv,\qquad L_2=(1+c)v,$$

with

$$0<L_1<L_2<L_0,\qquad0<v<u<1.$$

Here $c>\sqrt3/2$ ensures $v>0$, and
$u-v=4c(1-c)>0$.

### 1.5. Odd order: positive signed radius

If $\rho>1$, the affine map in (1) strictly decreases every $x<1$.
Thus $\max G<\max E$, forcing $E$ to have type I or L and $G$
type F. But then $\operatorname{range}G<\operatorname{range}E$,
forcing $\rho<1$.

If $0<\rho<1$, range comparison gives

$$\rho\ge L_1/L_0=v>2t-1.$$

The last inequality is $v-(2t-1)=2(1-c)>0$.

The affine map therefore strictly increases every $x\le t$.
Consequently $\max G>\max E$, forcing $E$ type F and $G$ type I
or L. Their range ratio is greater than one, again a contradiction.

### 1.6. Odd order: negative signed radius and the nonagon check

Put $r=-\rho>0$. Equal deletion types force $r=1$, excluded by
hypothesis. For different types,

$$r=\frac{\operatorname{range}G}{\operatorname{range}E}.$$

If $\max G=f$ and $\min E=-C_0$, the maximum equation requires

$$H:=2f-2rC_0-1+r^2=0.$$

Substitution and factorization give this finite table.

| Type of $E$ | Type of $G$ | $r$ | $H$ |
| --- | --- | --- | --- |
| I | F | $v$ | $2(c-1)(2c-1)(2c+1)(4c+1)$ |
| I | L | $v/u$ | $2(c-1)(8c^3-6c+1)/u^2$ |
| F | I | $1/v$ | $2(c-1)(2c-1)(2c+1)(8c^3-6c-1)/v^2$ |
| F | L | $1/u$ | $2(c-1)(8c^3-6c+1)/u^2$ |
| L | I | $u/v$ | $-2(c-1)(8c^3+4c^2-6c-1)/v^2$ |
| L | F | $u$ | $2(c-1)(4c^2+4c-1)$ |

For $k\ge11$ every entry is nonzero: $8c^3-6c=2\cos(3a)>1$,
and all remaining displayed factors other than $c-1$ are positive.
For $k=9$, all remain nonzero except type F to type I.

In that exceptional case $M=4$, $t=\cos(2\pi/9)$, and
$r=1/v=2t$. The last identity follows from

$$2tv-1=(2c-1)(8c^3-6c-1)=0.$$

The source set $E$ has entries $\cos(4\pi/9),-1/2,-c$. The affine
image of its middle entry is

$$z=(1+2t-4t^2)/2.$$

Since $3/4<t<4/5$, one has

$$0<z<\cos(4\pi/9)=2t^2-1.$$

The bounds on $t$ follow from $t>1/2$, $4t^3-3t=-1/2$, and
monotonicity of $4x^3-3x$ for $x>1/2$. The first inequality for $z$ follows by
substituting $t<4/5$ into its decreasing quadratic; the second follows
from $w-z=(4t-3)(2t+1)/2>0$ when $t>3/4$.
But $G$ has unchanged endpoints $t,-c$ and middle entry either
$\cos(4\pi/9)$ or $-1/2$. Neither equals $z$. Thus (1) fails also
for $k=9$, proving the odd part of the lemma.

## 2. Adding the radius to the chord palette

Three supplementary tests handle an added point at the center.

**Radius-palette lemma.** Let $V$ lie on the unit circle and write
$P=P(V)$. No noncentral off-circle point has all distances to $C$ in
$P\cup\{1\}$ in any of these cases:

- $V=C$ is a regular odd polygon of order at least nine;
- $V=C$ is a regular even polygon of order at least eight and $1\notin P$;
- $V$ is a regular odd polygon of order at least nine and $C$ is $V$
  minus one vertex.

### 2.1. A full odd polygon

Write $k=2m+1$. The pin has a repeated distance and hence lies on a
reflection axis. Its spectrum has $m+1$ entries and equals
$P\cup\{1\}$, since an odd regular polygon has no chord of length
one. Normalize its fixed vertex to $1$ and write the pin as signed
$\rho$. Put $M=m+1$.

The cosine list $\{\cos(2\pi j/k):0\le j\le m\}$ has sum $1/2$
and square sum $(2m+3)/4$. Comparing first and second power sums of
the squared palettes gives

$$M\rho^2-\rho-M=0,\qquad
\rho^2=\frac{2M(M-1)}{(2M-1)(M+1)}<1.$$

For completeness, the target sums are $2M$ and $6M-2$. After using
the first equality, the second pinned sum is
$4M+(2M+1-1/M)\rho^2$, giving the displayed formula.
The first equality now gives

$$\rho=-\frac{M(3M-1)}{(2M-1)(M+1)}<-1,$$

because numerator minus denominator is $(M-1)^2>0$. This contradicts
$\rho^2<1$.

### 2.2. A full even polygon

Write $k=2m$. Again the pin lies on a reflection axis. A vertex-axis
pin has $m+1$ distinct values and uses the full augmented palette.
The sum of its squared distances is $(m+1)(1+r^2)$, whereas the
target sum is $2m+3$. Thus $r^2=1+1/(m+1)>1$, and the opposite
vertex has distance $r+1>2=\max(P\cup\{1\})$, impossible.

An edge-axis pin has $m$ distinct values. The existing full-polygon
lemma excludes using only $P$. Thus the pin replaces one chord square
$2-2b$, where $b=\cos(j\pi/m)$, by $1$. The midpoint cosine list
has sum zero and square sum $m/2$; the chord cosine list has sum $-1$
and square sum $m/2$. The first two moments give

$$m(1+r^2)=2m+1+2b,$$

$$m(1+4r^2+r^4)=6m+5+8b-4b^2.$$

Eliminating $r^2$ yields $(1+1/m)(1+2b)^2=0$, hence $r^2=1$,
again impossible.

### 2.3. An odd polygon minus one vertex

Write $k=2m+1$, with $m\ge4$. The pin is on a reflection axis. If
its fixed vertex is not the hole, removal of the hole does not remove
a pinned value; Section 2.1 applies.

Otherwise put the fixed hole at $1$ and write the pin as signed
$\rho$. It has $m$ pinned values. The existing odd one-hole lemma
excludes using only $P$, so its squared palette replaces one chord
square $2-2b$, where $b=\cos(2\pi j/k)$, by $1$.
Since $1$ lies between the shortest and longest chords, the target
squared-distance palette has range at most that of the old squared
chord palette. The squared pinned palette has range $|\rho|$ times
that old range, so $|\rho|\le1$. Since the pin is off the circle,
$|\rho|<1$.

The first moment gives

$$m\rho^2+\rho-m-2b=0.$$

The second moment, after substituting $b$ from this equality, factors as

$$
(\rho^2-1)
\bigl[m(m+1)\rho^2+2(m+1)\rho-m(m-1)\bigr]=0.
$$

Let $Q(x)=m(m+1)x^2+2(m+1)x-m(m-1)$. Since $Q(-1)=-2<0$ and
$Q(0)<0$, its negative root is less than $-1$. Thus $\rho$ is its
positive root. Combining $Q(\rho)=0$ with the first moment yields

$$\rho=-2b-\frac{2m}{m+1}<\frac2{m+1}.$$

But

$$Q\left(\frac2{m+1}\right)
=\frac{4m}{m+1}+4-m(m-1)<8-12<0,$$

so the positive root is greater than $2/(m+1)$. This contradiction
completes the radius-palette lemma.

## 3. Proof of the theorem

The [small-order theorem](small_orders.md) covers $5\le n\le10$.
Assume $n\ge11$ and $R(A)=1$. Let $C$ be the $h=n-3$ points on
the chosen circle. If another point lies on that circle, the
[two-off-circle theorem](two_off_circle.md) gives a contradiction.
Thus $B=A\setminus C$ consists of three off-circle points.

The pair budget and the
[unique-diameter theorem](unique_diameter_obstruction.md) give

$$q(A)\le
\begin{cases}
n/2-1,&n\text{ even},\\
(n-1)/2,&n\text{ odd}.
\end{cases}$$

Equivalently, $q(A)\le\lfloor h/2\rfloor+1$. For the angle set
$S$ of $C$,

$$h\le|S-S|\le2q(A)+1\le
\begin{cases}
h+2,&h\text{ odd},\\
h+3,&h\text{ even}.
\end{cases}$$

These upper bounds are strictly below $3h/2$, since $h\ge8$.
The elementary [small-difference lemma](two_off_circle.md) makes
$S-S$ a finite subgroup of the circle group. Therefore $C$ lies in
a regular $k$-gon $V$ with

$$
\begin{cases}
h\le k\le h+2,&h\text{ odd},\\
h\le k\le h+3,&h\text{ even}.
\end{cases}
$$

Normalize its circumradius to one. Every chord value of $V$ survives
in $C$: at most three deletions remove at most six edges from a
nondiametral class, which originally has $k\ge8$ edges. At even
order a diametral class survives because fewer than $k/2$ vertices
were deleted. Write $P=P(V)$.

If $\lfloor k/2\rfloor=\lfloor h/2\rfloor+1$, then $P$ exhausts
the allowed distance count. The possibilities are an even polygon
minus one or two vertices, or an odd polygon minus two or three
vertices. The old palette lemmas and Section 1 exclude every
noncentral point of $B$. This is impossible since $B$ has three points.

The remaining cases are that $C$ is a full odd regular polygon, a
full even regular polygon, or an odd regular polygon minus one vertex.
Here $P$ has $\lfloor h/2\rfloor$ values, leaving at most one extra
value.

First suppose no point of $B$ is the center. Any value outside $P$
has at most

$$2|B|+\binom{|B|}{2}=9\le n$$

pairs, so it is rare. There must be such a value: a noncentral pin on
a full odd polygon has more pinned values than $|P|$, and in the
other two cases the old palette lemmas exclude using only $P$.
Thus there is exactly one new value $D$, which must be the diameter.
In particular, $D>\max P$.

Each pin must see $D$ on $C$, since using only $P$ is impossible.
Delete its one or two $D$-neighbors from $C$. All remaining distances
from that pin lie in $P$. The remaining circular set is, respectively,
an odd polygon minus one or two vertices, an even polygon minus one
or two vertices, or an odd polygon minus two or three vertices. The
old palette lemmas and Section 1 exclude the pin in every case.
The thresholds apply even at $n=11$: the smallest even polygon here
has order eight and the smallest odd polygon has order nine.

Finally suppose the center belongs to $B$. In the odd cases, the
radius $1$ is not in $P$, so it is the only extra value. Sections 2.1
and 2.3 exclude either noncentral pin. In the even case, if $1\notin P$,
Section 2.2 does the same. If $1\in P$, any new value again has at
most nine pairs: the center contributes no core pairs at a value
outside $P$. The preceding new-diameter and deletion argument applies
to either noncentral pin. All cases contradict $R(A)=1$, proving
the theorem.

## Verification and scope

The new finite algebra consists of six factored extremum identities,
the explicit nonagon middle-entry check, and the three moment arguments.
A separate author checked all identities, including a bounded symbolic
check of the six table entries. The author checked the reflection
patterns, range comparisons, nonagon inequalities, and final reduction;
the argument is author-recorded. The author also checked the extension lemmas
and the radius-palette lemmas with the final reduction; both audits
passed without gaps.

This establishes an exact finite bound for three circular exceptions.
It does not extract a large circular subset from arbitrary planar sets,
and does not settle the unrestricted first assertion or asymptotic
question.
