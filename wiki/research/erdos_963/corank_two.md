---
name: research/erdos_963/corank_two
title: 'The rational-rank defect at most two case'
desc: A proved residue-class and coordinate-width argument establishing the target and odd-slice strengthening at intrinsic rank defect at most two.
tags: []
sources: []
created: 2026-09-18T21:30:00Z
updated: 2026-09-18T21:30:00Z
---


# The rational-rank defect at most two case

***

## Statement

Let $P$ be a finite nonempty set in a finite-dimensional rational vector
space, containing neither zero nor an antipodal pair. Let
$r=\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}P$, and let
$d=d(P)$ be its maximum dissociated-subset size. Then

$$
 d\le r+2\quad\Longrightarrow\quad |P|\le2^d-1. \tag{1}
$$

The cases $d\le r+1$ were proved in [[research/erdos_963/corank_one|the
preceding note]]. The proof below treats $d=r+2$. Together with the intrinsic
lift in that note, it establishes the target for positive real sets whose
intrinsic ternary-relation rank $\rho$ satisfies $\rho\ge d-2$.

This is a proved special case, not a solution of the unrestricted problem.

## Maximum-volume coordinates

Choose a maximum-absolute-determinant rational basis
$B=\{b_1,\ldots,b_r\}\subseteq P$, and use it as coordinate basis.
All coordinate columns belong to $[-1,1]^r$, and every $r$-column
determinant has absolute value at most one. More generally, every square
minor of coordinate columns has absolute value at most one: extend that
minor to an $r$-column determinant using the missing coordinate columns
of $B$. When the minor is nonzero, no repeated column is introduced.

The integral-coordinate columns $I$ satisfy

$$
 |I|\le2^r-1. \tag{2}
$$

For completeness, such columns are ternary vectors. Distinct ones are not
proportional, since nonzero proportional ternary vectors are equal or
opposite. If two reduced to the same vector modulo two, extend them to a
basis using $B$; its coordinate determinant would be a nonzero even
integer, contradicting the maximum-volume bound. Their distinct reductions
are therefore among the $2^r-1$ nonzero binary vectors.

We will prove that the nonintegral columns $N=P\setminus I$ satisfy

$$
 |N|\le3\cdot2^r. \tag{3}
$$

Together with (2), this gives $|P|\le2^{r+2}-1=2^d-1$.

Individual sign changes preserve dissociation and the absolute minor bounds.
They never identify columns because $P$ has no antipodal pair. We may
therefore orient each nonintegral column to a specified representative of
its signed residue class in $\mathbb Q^r/\mathbb Z^r$.

## Two elementary coordinate counts

Consider an oriented nonzero residue class $g$. Suppose it has $s\ge1$
nonzero fractional coordinates and $z=r-s$ zero coordinates. In a
fractional coordinate, a column has at most two possible values, differing
by one. In the other coordinates its values belong to $\{-1,0,1\}$.

For a fixed support $S$ in these $z$ integral positions, at most two
integer sign patterns occur, and if two occur they are opposites. Indeed,
two patterns on the same support that are neither equal nor opposite agree
at one nonzero coordinate and disagree at another. The corresponding
$2$-by-$2$ minor has absolute value two, which is impossible. The
empty support has just one pattern. Thus any one oriented residue class has
at most

$$
 2^s\bigl(1+2(2^z-1)\bigr)
 =2^{r+1}-2^s<2^{r+1}
 \tag{4}
$$

columns. This conclusion does not use a dissociation hypothesis.

There is a better bound if every pair of its columns satisfies

$$
 x-y\in\{-1,0,1\}^r
 \quad\hbox{or}\quad
 x+y\in\{-1,0,1\}^r. \tag{5}
$$

If $2g\ne0$, only the difference can be integral. Every coordinate
then has at most two consecutive values, giving at most $2^r$ columns.
If $2g=0$, orient the first half-integral coordinate to $+1/2$.
There are only $2^{s-1}$ fractional patterns, so the minor argument just
given bounds the number of columns by
$2^{s-1}(2^{z+1}-1)<2^r$. In either case, (5) implies

$$
 \text{number of columns in the signed residue class}\le2^r. \tag{6}
$$


We also use the following box count. If four nonempty sets each have at most
two consecutive values in each of $q\ge1$ coordinates, and at most
two of the four sets vary at any coordinate, their total cardinality is at
most

$$
 2^{q+1}+2\le3\cdot2^q. \tag{7}
$$

To prove it, let $k_i$ be the number of coordinates varying in set $i$.
Its size is at most $2^{k_i}$, while $0\le k_i\le q$ and
$\sum_i k_i\le2q$. Convexity of $2^k$, or transferring one unit
from a smaller positive $k_i$ to a larger one below $q$, shows that
the sum is maximized at $(q,q,0,0)$. This proves (7).

## Residue configurations of dissociation dimension at most two

Let $R$ be the residues of $N$. A dissociated triple of residues
would, together with $B$, give $r+3=d+1$ dissociated columns:
reduce a putative relation modulo $\mathbb Z^r$, and then use the
rational independence of $B$. Hence

$$
 d(R)\le2. \tag{8}
$$

Let $m$ be the number of nonzero signed residue classes occurring.
If $m\ge2$, choose dissociated representatives $g,h$ of two distinct
such classes.
By (8), every other residue belongs to the ternary span of $g,h$.
Consequently

$$
 m\le4,
 \qquad\text{with possible classes }\{
 \pm g,\ \pm h,\ \pm(g+h),\ \pm(g-h)\}. \tag{9}
$$


The following observation forces (5) for many classes. If a residue class
$g$ has an occurring residue

$$
 h\notin\{0,\pm g,\pm2g\}, \tag{10}
$$

choose any column $y$ of residue $h$. For distinct columns
$x,x'$ oriented to residue $g$, the set
$B\cup\{x,x',y\}$ has $d+1$ elements and has a ternary relation.
If the coefficient of $y$ were nonzero, reduction modulo
$\mathbb Z^r$ would contradict (10). Thus the relation omits $y$
and must use both $x,x'$; it gives (5). Such a class therefore obeys (6).

## Zero, one, two, or three signed classes

If $m=0$, there are no nonintegral columns. If $m=1$, (4) is
already stronger than (3).

Suppose $m=2$, with representatives $g,h$. If at least one of
$h\notin\{\pm2g\}$ or $g\notin\{\pm2h\}$ holds, that
choice supplies (10) for one of the two classes. Bound this class by (6)
and the other by (4), proving (3).

The remaining two-class case has $h=\pm2g$ and $g=\pm2h$.
After orientation take $h=2g$. Then either $3g=0$ or $5g=0$.
The first would identify the two signed classes. Thus $g$ has order
five, and the classes are precisely the two nonzero signed classes of
$\langle g\rangle\cong\mathbb Z/5\mathbb Z$. This exceptional
case is handled below.

If $m=3$, every class $g$ has another occurring class outside
$\{\pm g,\pm2g\}$. All three therefore obey (6), proving (3).

## The four-class case: an elementary abelian group of order nine

Suppose $m=4$, so all four classes in (9) are distinct. The triple
$\{g,g+h,g-h\}$ is dependent. Its relation must use all three
residues, since their signed classes differ. If the coefficients of
$g+h$ and $g-h$ are equal, the relation implies $3g=0$
(the alternative $g=0$ is excluded). If those coefficients are
opposite, it implies $g=\pm2h$, which identifies two of the four
signed classes. Therefore $3g=0$. Similarly $3h=0$.
As $g,h$ are dissociated, they generate a copy of $\mathbb F_3^2$,
and the four occurring signed classes are its four one-dimensional
subspaces.

Every class obeys (10), so, after fixing orientations, it has at most two
consecutive coordinate values. Any three distinct classes have a unique
ternary relation up to sign on their three representatives. For arbitrary
columns $x,y,z$ from these classes, the dependence of
$B\cup\{x,y,z\}$ must use all three and has exactly those residue
signs. Hence their correspondingly signed sum belongs to
$\{-1,0,1\}^r$.

At a fixed coordinate, let the width of a class be zero or one according as
it is constant or varying. Since the three columns can be chosen
independently, the width of a signed sum from three classes is the sum of
their three widths. The preceding ternary bound makes this sum at most two.
Every three of the four widths therefore have sum at most two, so at most
two classes vary at that coordinate. Apply (7) with $q=r$ to obtain
$|N|\le2^{r+1}+2\le3\cdot2^r$, proving (3).

## The two-class group of order five

Orient the two classes to $g$ and $2g$, where $g$ has order
five; call their column sets $A$ and $C$. They have the same
$s\ge1$ fractional-coordinate positions and the same $z=r-s$
integral-coordinate positions. Fix a support $S$ in the latter.
Within each of $A$ and $C$, at most two integer sign patterns
occur, by the minor bound preceding (4).

If at most three pattern groups occur across the two classes, their total
size is at most $3\cdot2^s$. Otherwise there are four nonempty groups
$A_1,A_2,C_1,C_2$, with different integer patterns inside each class.
Any $x\in A_1$ and $x'\in A_2$ disagree in an integral
coordinate of their common support, so $x-x'$ is not ternary; their
sum is not integral. Thus they cannot have a ternary relation with $B$
alone. For any $y\in C_j$, the dependence of
$B\cup\{x,x',y\}$ must use all three columns. Its unique residue
signs give

$$
 x+x'-y\in\{-1,0,1\}^r. \tag{11}
$$

Similarly, for any $y\in C_1$, $y'\in C_2$, and $x\in A_i$,
the unique residue relation gives

$$
 y+y'+x\in\{-1,0,1\}^r. \tag{12}
$$


In a fractional coordinate, each pattern group has width zero or one.
Equations (11)--(12), with the columns chosen independently, say that every
three of the four widths have sum at most two. Thus at most two groups vary
in each of the $s$ fractional coordinates. Their integral coordinates
are fixed within each group. Applying (7) with $q=s$ bounds their
total size by $3\cdot2^s$.

There are $2^z$ choices of $S$. Summing the bound gives

$$
 |N|=|A|+|C|\le2^z\,3\cdot2^s=3\cdot2^r,
$$

as required. This completes the proof of (1).

## What this leaves open

The intrinsic lift preserves positivity, distinctness, and all ternary
relations, and its rank $\rho$ satisfies $\rho\le d$. The present argument
and [[research/erdos_963/corank_one|the defect-one argument]] settle all
configurations with $d-\rho\le2$. No argument for arbitrary intrinsic defect
at least three is proved here.

## The odd-slice strengthening

The following strengthening is also proved. Under the hypotheses of (1),
suppose that $L=\langle P\rangle_{\mathbb Z}$ has a homomorphism
$\chi:L\to\mathbb F_2$ taking the value one on every column. Then

$$
 |P|\le2^{d-1}. \tag{13}
$$

The intrinsic lift of a positive odd integer set retains this homomorphism, as
shown in [[research/erdos_963/corank_one|the defect-one note]]. Thus the
odd-slice bound also holds whenever its intrinsic rank is at least $d-2$.

Again only $d=r+2$ remains to prove. The integral columns have odd-weight
reductions modulo two, so $|I|\le2^{r-1}$. We show

$$
 |N|\le3\cdot2^{r-1}. \tag{14}
$$


For columns $x,y$ in the same oriented residue class, $x-y$ is
integral and
$\sum_i(x_i-y_i)=\chi(x)-\chi(y)=0\pmod2$. Consequently a box with
$k\ge1$ varying consecutive-coordinate choices contains at most
$2^{k-1}$ such columns. A constant box contains at most one. Write

$$
 \phi(k)=\max\{1,2^{k-1}\}\qquad(k\ge0).
$$

This is a convex sequence. The same transfer argument as for (7) gives

$$
 \sum_{i=1}^4\phi(k_i)\le2^q+2
 \quad\text{if }0\le k_i\le q,\quad\sum_i k_i\le2q. \tag{15}
$$


A general nonzero signed residue class has at most $2^r$ columns in
the present odd setting. If its residue is not of order two, fix an integral
sign pattern in the argument for (4). Parity halves the $2^s$ fractional
choices, giving at most
$2^{s-1}(2^{z+1}-1)<2^r$ columns in total. For an order-two residue,
the number $s$ of half-integral coordinates is even: apply $\chi$
to $2x$. Hence $s\ge2$. Orient its first half-integral coordinate
positively. Parity halves the remaining $2^{s-1}$ fractional choices,
giving fewer than $2^{r-1}$ columns. Finally, a class satisfying (5)
has at most $2^{r-1}$ columns, either by the checkerboard restriction
on its width-one box or by this order-two count.

These estimates prove (14) in every ordinary case of the preceding proof:
one class uses the general bound; two nonexceptional classes use one general
and one (5) bound; three classes all satisfy (5).

In the four-class $\mathbb F_3^2$ case, at most two fibers vary in
each coordinate, exactly as before. Equation (15), with $q=r$, bounds
their total size by $2^r+2$. Here $r\ge2$, since the subgroup of
elements killed by three in $\mathbb Q^r/\mathbb Z^r$ has dimension
$r$ over $\mathbb F_3$. Therefore
$2^r+2\le3\cdot2^{r-1}$, proving (14) in this case.

It remains to refine the order-five argument, retaining its notation. Fix
an integral support $S$. Each fixed-pattern group has at most
$2^{s-1}$ columns by parity. Three or fewer groups therefore contribute
at most $3\cdot2^{s-1}$. If four groups occur and $s\ge2$, their
width constraints and (15) give at most
$2^s+2\le3\cdot2^{s-1}$ columns.

Suppose instead that four groups occur and $s=1$. Necessarily
$S\ne\varnothing$. In each residue class the two integral sign
patterns are opposites, by the minor argument. The difference of their
integral-coordinate sums is even. Since the only fractional coordinate has
two consecutive possibilities and the total coordinate-sum difference must
be even, this coordinate is the same for both groups in each class. Denote
these fixed values by $a$ for the residue $g$ and $b$ for
the residue $2g$. Equations (11)--(12) give

$$
 m=2a-b\in\{-1,0,1\},\qquad n=a+2b\in\{-1,0,1\}.
$$

The total coordinate sums of the integral vectors in (11) and (12) have
parity one, since their $\chi$-values are respectively
$1+1-1=1$ and $1+1+1=1$. Their integral-position contributions
both have parity $|S|$. Thus $m,n$ have the same parity
$1-|S|$. If both are even, they are zero, forcing $a=b=0$,
contrary to the nonzero fractional residue. Otherwise $m,n\in\{-1,1\}$,
and

$$
 a=(2m+n)/5,\qquad b=(-m+2n)/5.
$$

One of $|a|,|b|$ is $3/5$. The two opposite integral patterns
in that class, together with its fixed fractional coordinate, give a
$2$-by-$2$ minor of absolute value $2(3/5)=6/5$, a contradiction.
Hence four groups cannot occur when $s=1$.

In every case the columns for one support contribute at most
$3\cdot2^{s-1}$. Summing over its $2^z$ possible supports proves
(14). Adding $|I|\le2^{r-1}$ proves (13).
