---
name: research/erdos_963/quotient_special_cases
title: 'Arbitrary-defect cases from the finite residue quotient'
desc: Two proved sufficient conditions on the quotient by a maximum-volume rational basis; the unrestricted problem remains open.
tags: []
sources: []
created: 2026-09-18T21:55:00Z
updated: 2026-09-18T21:55:00Z
---


# Arbitrary-defect cases from the finite residue quotient

***

## Setup and statements

Let $P$ be a finite nonempty set of rational vectors containing neither
zero nor an antipodal pair. Write $r=\operatorname{rank}_{\mathbb Q}P$
and $d=d(P)$. Choose a maximum-absolute-determinant basis
$B\subseteq P$, and use its elements as coordinates. Set

$$
 L=\langle P\rangle_{\mathbb Z},\qquad G=L/\mathbb Z^r.
$$

The group $G$ is finite because all coordinates are rational. Every
coordinate column lies in $[-1,1]^r$, and every square coordinate
minor has absolute value at most one, as explained in
[[research/erdos_963/corank_two|the defect-two proof]].

Each of the following additional hypotheses implies

$$
 |P|\le 2^d-1. \tag{1}
$$


1. The group $G$ has exponent at most two.
2. For some prime $p$,

$$
   \dim_{\mathbb F_p}(G/pG)=d-r.
   \tag{2}
$$


These are proved special cases allowing unbounded defect $d-r$. They do not
settle arbitrary quotients. They can also be applied after the intrinsic
relation lift in [[research/erdos_963/corank_one|the defect-one note]].

## Coordinate estimates

Let $I$ be the integral-coordinate columns. The modulo-two injection
proved in the preceding notes gives

$$
 |I|\le 2^r-1. \tag{3}
$$

In any fixed set of coordinate positions, two occurring nonzero sign
patterns on the same support must be equal or opposite: otherwise two
coordinates give a minor of absolute value two.

For a nonzero residue $g$ of order two, let $s\ge1$ be the
number of half-integral positions and put $z=r-s$. Orient each column
in this signed residue class so its first half-integral coordinate is
$+1/2$. There are at most $2^{s-1}$ fractional patterns. For each
nonempty support in the other $z$ positions there are at most two
opposite sign patterns; the empty support has one. Thus this class has at
most

$$
 2^{s-1}\bigl(2^{z+1}-1\bigr)<2^r
 \tag{4}
$$

columns. Orienting columns never identifies distinct elements, since
$P$ has no antipodal pair.

## Elementary two-group quotients

Suppose $G\cong\mathbb F_2^k$. The occurring residues span $G$,
so choose $k$ columns whose residues are linearly independent. Those
columns together with $B$ are dissociated: reduction modulo
$\mathbb Z^r$ first eliminates their coefficients, and rational
independence then eliminates the coefficients on $B$. Therefore
$r+k\le d$.

There are at most $2^k-1$ nonzero residue classes. Applying (3) and
(4), with the weaker bound $2^r$ in (4), yields

$$
 |P|\le (2^r-1)+(2^k-1)2^r
       =2^{r+k}-1\le2^d-1.
$$

This also covers $k=0$.

## Quotients attaining the defect at an odd prime

Assume (2), and set $k=d-r$. If $k=0$, the full-rational-rank
case already proves (1), so suppose $k\ge1$. Let
$V=G/pG\cong\mathbb F_p^k$. The images of the coordinate columns
span $V$. A choice of $k$ columns forming a basis of $V$ is
dissociated in $G$. Conversely, a dissociated set of residues in
$G$, adjoined to $B$, is dissociated in the rational vector space.
Consequently the set of occurring residues has dissociation dimension
exactly $k$.

### Simple residue classes and their circuits

No occurring nonzero residue can map to zero in $V$. If $g\ne0$
did so, choose columns representing a basis of $V$ and a column of
residue $g$. Along with $B$, these are $r+k+1=d+1$
distinct columns. Any ternary relation among them, reduced in $V$,
would have zero coefficients at the basis columns. It would then force
$g=0$, a contradiction.

Likewise, two distinct signed residue classes cannot have parallel images
in $V$. Take representatives $g,h$ of such classes, extend the
image of $g$ to a basis of $V$, and take columns for the other
basis elements. A ternary relation on these columns, representatives of
$g,h$, and $B$ must use $g,h$ with coefficients $\pm1$
and omit all complementary basis elements. It would imply $g=\pm h$
in $G$, a contradiction. This argument also rules out parallel
images whose scalar ratio is not $\pm1$, since then no such ternary
relation could exist even in $V$.

Thus the nonzero signed residue classes, with one representative chosen
from each, form a simple rank-$k$ linear matroid over $\mathbb F_p$.
Let their number be $N$. A maximum dissociated residue set of size
$k$ ternary-spans all occurring residues. Counting nonzero ternary
coefficient vectors up to sign gives

$$
 N\le\frac{3^k-1}{2}. \tag{5}
$$


Let $C$ be a circuit of this matroid. Extend $C\setminus\{c\}$
to a basis using other occurring residue classes, and denote the added
classes by $E$. Then $|C\cup E|=k+1$, and its space of relations
over $\mathbb F_p$ is one-dimensional, supported on $C$. Choose
arbitrary oriented columns $x_g$ in the classes of $C$, and fixed
columns in the classes of $E$. Together with $B$ they have
$d+1$ elements, so there is a ternary relation. Reduction to $V$
shows that its coefficients outside $C$ vanish. Its coefficients on
$C$ are all $\pm1$.

These signs are unique up to simultaneous reversal. Indeed, two vectors
with all their nonzero coordinates in $\{1,-1\}$ and spanning the
same one-dimensional subspace over an odd field differ by the scalar
$1$ or $-1$, as is seen at any one coordinate. Therefore there
are fixed signs $\varepsilon_g\in\{1,-1\}$, depending only on
the oriented residue representatives, such that for every choice of
columns in the circuit classes,

$$
 \sum_{g\in C}\varepsilon_gx_g\in\{-1,0,1\}^r.
 \tag{6}
$$


### Width of a residue class

Fix an oriented nonzero residue class $g$ and distinct columns
$x,x'$ in it. Extend its image in $V$ to a basis using $k-1$
other residue classes. As before, the resulting $k+1$ columns together
with $B$ must be dependent. Their unique relation in $V$ is
supported on $x,x'$, with opposite coefficients. Thus

$$
 x-x'\in\{-1,0,1\}^r.
 \tag{7}
$$

All columns in this residue class have integral differences, so each
coordinate has either one value or two consecutive values. Write $s_g$
for the number of varying coordinates in the class. It contains at most
$2^{s_g}$ columns.

For each coordinate $j$, let $W_j$ be the residue classes varying
in that coordinate. This set is independent in the rank-$k$ matroid.
Otherwise it contains a circuit $C$. Since the matroid is simple,
$|C|\ge3$. Independently choosing the columns in these classes makes
the width in coordinate $j$ of the signed sum in (6) equal to
$|C|$, whereas (6) confines that sum to an interval of length two.
This is impossible. Consequently

$$
 |W_j|\le k,\qquad \sum_g s_g\le rk. \tag{8}
$$


### Counting the columns

For $0\le s\le r$, convexity gives the chord bound

$$
 2^s\le1+\frac{2^r-1}{r}s.
$$

Using (3), (5), and (8), we obtain

$$
 \begin{split}
 |P|&\le2^r-1+\sum_g2^{s_g}\\
 &\le(k+1)2^r+N-k-1. \tag{9}
 \end{split}
$$

The finite subgroup $G\subseteq\mathbb Q^r/\mathbb Z^r$ has
$p$-rank at most $r$: its subgroup killed by $p$ embeds in
$\mathbb F_p^r$, and for a finite abelian group that subgroup and
$G/pG$ have the same cardinality. Thus $k\le r$.

For $k=1$, (5) gives $N\le1$, and (9) is exactly
$|P|\le2^{r+1}-1$. For $k=2$, $N\le4$ and $r\ge2$
give $N-k\le2\le2^r=(2^k-k-1)2^r$. For $k\ge3$,
$k+1\le2^{k-1}$, so

$$
 (2^k-k-1)2^r\ge2^{2k-1}
 >\frac{3^k-1}{2}\ge N-k.
$$

In all cases, (9) is at most $2^{r+k}-1=2^d-1$, proving (1).

## The prime two with minimal defect

Suppose $k=\dim_{\mathbb F_2}(G/2G)=d-r$. The case $k=0$
is again the full-rank theorem. For $k\ge1$, the same extension
argument used above shows that an occurring nonzero residue cannot have
zero image in $G/2G$. It also shows that two distinct signed residue
classes cannot have the same nonzero image: extend that common image to
a basis, adjoin representatives of the two classes, and use a ternary
relation on these $k+1$ columns together with $B$. Reduction
modulo two forces the relation to use just the two residue columns, so
their residues would have to be equal or opposite. There are therefore
at most $2^k-1$ nonzero signed residue classes.

For distinct columns $x,x'$ in a single oriented nonzero residue
class $g$, extend the image of $g$ to a basis of $G/2G$.
A ternary relation on these two columns, the $k-1$ complementary
columns, and $B$ must again use just $x,x'$ outside $B$.
Consequently $x-x'$ or $x+x'$ is ternary. If $2g\ne0$,
only the difference is integral, and the residue class lies in a box
with at most two consecutive values per coordinate. Its cardinality is
at most $2^r$. If $2g=0$, estimate (4) gives the same bound.
Combining all classes with (3) proves

$$
 |P|\le(2^r-1)+(2^k-1)2^r=2^{r+k}-1=2^d-1.
$$

Unlike the odd-prime proof, this argument needs no uniqueness assertion
for signs on longer quotient circuits.

## Limitation

The odd-prime argument uses equality between the defect and a field rank.
It is this equality that lets every field circuit extend to exactly
$k+1$ residue columns with a unique signed relation. For arbitrary
defect larger than every such field rank, several quotient relations can
compete and the uniform width statement (6) has not been established.

## The odd-slice strengthening

Suppose in addition that there is a homomorphism
$\chi:L\to\mathbb F_2$ taking the value one on every column of $P$.
Under either of the two sufficient conditions stated above, one has

$$
 |P|\le2^{d-1}. \tag{10}
$$

This applies to positive odd integer sets after the intrinsic lift, as
explained in [[research/erdos_963/corank_one|the defect-one note]].

The integral columns have odd-weight binary reductions, so
$|I|\le2^{r-1}$. For a nonzero order-two residue, the number $s$
of half-integral coordinates is even, since applying $\chi$ to $2x$
gives $0=s\pmod2$. In particular $s\ge2$. Orient the first
half-integral coordinate positively. For any fixed integer sign pattern,
the parity constraint halves the remaining $2^{s-1}$ fractional
patterns, giving at most
$2^{s-2}(2^{z+1}-1)<2^{r-1}$ columns in this signed residue class.
Thus an elementary two-group quotient of rank $k$ gives

$$
 |P|\le2^{r-1}+(2^k-1)2^{r-1}
       =2^{r+k-1}\le2^{d-1}.
$$


For the prime-two minimal-defect case, there are again at most
$2^k-1$ nonzero signed residue classes. An order-two class obeys
the preceding bound. Every other class lies in a width-one coordinate
box. Differences of its columns have even coordinate sum, so a box
with $s\ge1$ varying coordinates contains at most $2^{s-1}$
columns, and a constant box contains at most one. Each class therefore
has at most $2^{r-1}$ columns. Adding the integral columns gives
$|P|\le2^{r+k-1}=2^{d-1}$.

For the odd-prime case, retain its oriented width-one boxes and the bound
$\sum_gs_g\le rk$. Within a fixed residue class, the difference of
two columns is integral and has even coordinate sum, since its
$\chi$-value is zero. A box with $s\ge1$ varying coordinates
therefore contains at most $2^{s-1}$ columns; a constant box has at
most one. The convex function on integers
$\phi(s)=\max\{1,2^{s-1}\}$ satisfies

$$
 \phi(s)\le1+\frac{2^{r-1}-1}{r}s
 \qquad(0\le s\le r).
$$

Consequently

$$
 |P|\le(k+1)2^{r-1}+N-k. \tag{11}
$$

For $k=1$, $N\le1$ gives (10) immediately. For $k=2$,
$N-k\le2\le2^{r-1}$, since $r\ge k=2$, and (11) again
gives (10). For $k\ge3$,

$$
 (2^k-k-1)2^{r-1}\ge2^{2k-2}
 >\frac{3^k-1}{2}\ge N-k.
$$

The strict inequality holds at $k=3$ and persists because
$(4/3)^k$ increases. Thus (11) is at most
$2^{r+k-1}=2^{d-1}$, proving (10).
