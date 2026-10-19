---
name: research/erdos_963/forest_obstruction
title: 'Rainbow forests fail for an arbitrary maximum subset'
desc: A 25-point positive integer set has a maximum 16-set whose nine-color graph is K4,4, refuting the every-maximum forest assertion.
tags: []
sources: []
created: 2026-09-19T03:50:00Z
updated: 2026-09-19T03:52:14Z
---


# Rainbow forests fail for an arbitrary maximum subset

***

The assertion in [[research/erdos_963/continuation_routes|the forest route]] for
**every** maximum dissociated subset is false. The existence version, and its
maximum-sum specialization, remain unproved. This example is not a
counterexample to Erdős 963.

Put

$$
A=\{15,54,66,90,114,174,246,734\},\qquad D=A\cup2000A,
$$


$$
C=\{9975,9990,10005,19995,20010,20025,49995,50010,50025\}.
$$

Then

$$
\boxed{d(D\cup C)=16=|D|,\qquad r(E(C))=7<9=|C|.}       \tag{1}
$$

Here $E(C)$ consists of the edges on $\Sigma(D)$ with differences
in $C$. In fact, its nonisolated graph is exactly $K_{4,4}$.

## One block

Let $F=\{9,11,15,19,29,41\}$, $E=6F\cup\{734\}$, $x=15$, and $c=10$, so that
$A=E\cup\{x\}$. Dissociation of $F$ is already proved in
[[research/erdos_963/minimum_sum_matching|the minimum-sum note]]. Reduction
modulo two, then modulo three, in a ternary relation on $A$ eliminates $x$, then
$734$; dissociation of $F$ eliminates the other coefficients. Thus $A$ is
dissociated.

The block has three useful properties:

1. $c$ has the unique ternary representation on $E$

$$
   10=\sum_{f\in F}6f-734.
$$

2. Neither $c+2x=40$ nor $c-2x=-20$ is ternarily represented on $E$.
3. Both $2x=30$ and $4x=60$ remain represented after any one deletion
   from $E$.

For the first two properties, reduction modulo six forces the
$734$-coefficient to be $-1$. The required sums on $6F$ are
$744,774,714$, respectively. Its total is $744$; the first sum
has only the all-positive representation, the second is too large,
and the third would reduce the total by $30<\min6F=54$.

For the third property, multiply by six the identities

$$
\begin{split}
5&=9+11-15=9+15-19=15+19-29\\
 &=9+19+29-11-41,\\
10&=19-9=29-19=41+9-11-29.
\end{split}                                               \tag{2}
$$

In each family the supports have empty intersection. Deleting
$734$ does not affect them. If $x$ is also available, these
representations and $3x=2x+x$ represent every $kx$, $|k|\le4$.
They are ternary representations on distinct block elements, not
coefficients $2,3,4$ on the element $x$.

## The two-coordinate configuration

Work first with independent coordinates $e_1,e_2$ and put

$$
\mathcal D=Ae_1\cup Ae_2,\qquad
g_{ij}=(c+ix)e_1+(c+jx)e_2,quad i,j\in\{-1,0,1\},
$$


$$
\mathcal C=\{g_{ij}:i,j\in\{-1,0,1\}\}.
$$

The set $\mathcal D$ is dissociated. We prove that every
seventeen-subset of $\mathcal D\cup\mathcal C$ is dependent.

Call a nonzero assignment of coefficients in $\{-1,0,1\}$ to
distinct grid points a *balanced move* if its coefficient sum is
zero. If its two coordinate sums are $(a,b)$, then

$$
\sum_{i,j}\varepsilon_{ij}g_{ij}=ax e_1+bx e_2.            \tag{3}
$$

We need the following elementary grid facts.

* Four grid points have two with the same first coordinate.
* Four grid points admit a balanced move with $|a|\le1$ and
  $b\in\{0,\pm2,\pm4\}$. If two points of the same second-coordinate
  parity have first-coordinate difference at most one, use their
  difference. Otherwise each second-parity class has at most two
  points, in first-coordinate rows $-1,+1$. Each class must have
  two; subtract the two parity-class sums.
* Five grid points admit a balanced move with $a=0$ and
  $b\in\{0,\pm2,\pm4\}$. A repeated first-coordinate/second-parity
  class gives a pair difference. Otherwise five of those six classes
  occur; two rows contain both parities. Subtract their within-row
  differences.
* Five grid points have two with both coordinate differences at
  most one, by the four rectangles defined by the splits
  $\{-1,0\}\cup\{1\}$. They also have two with the same
  coordinatewise parity.
* Six grid points contain a parallelogram on four distinct points.
  A full row and another row with at least two points give a
  rectangle. Otherwise all rows have two points. Repeated column
  pairs again give a rectangle. If their omitted columns, in row
  order, are distinct $u,v,w$, use the outer-row points with
  columns $w,u$ and both middle-row points; their sums agree.

## Dependence of every seventeen-subset

If a seventeen-subset contains $t$ colors, it omits $t-1$ members of
$\mathcal D$. Six colors already contain a parallelogram, so assume
$1\le t\le5$. An $x$-deletion removes $xe_k$; the other deletions
are $E$-deletions. The two block coordinates may be interchanged.

For $t=1$, no basis element was deleted, so use the defining
representation of the color.

For $t=2$, the deletion distribution is $(1,0)$. If the deletion is
from $E$, the color difference is represented in both blocks. If it
removes $x$, use a pair difference when the first indices have the
same parity. Otherwise one first index is zero; that individual
color is represented using $c$ in the first block and the intact
second block.

For $t=3$, a distribution $(2,0)$ is handled by a pair with
first-index difference at most one if $x$ survives, or a pair of
equal first-index parity if it does not. These always exist among
three indices. The intact block represents the second difference.
For distribution $(1,1)$, any pair works if neither $x$ was deleted;
with one $x$-deletion use a pair of equal parity in that coordinate.
With two $x$-deletions, use a repeated coordinatewise parity class,
if present. Otherwise there are three distinct parity classes. If
$(0,0)$ occurs, its central color is represented by the intact
$E$-blocks. The remaining possibility is classes $(1,0),(0,1),(1,1)$.
Give their three index vectors signs canceling both coordinates.
Their signed color sum is $kc(e_1+e_2)$, $k\in\{\pm1,\pm3\}$,
represented in the intact $E$-blocks by $c$ or $3c=2x$.

For $t=4$, distribution $(3,0)$ uses a pair with the same first
index. For $(2,1)$, consider the twice-damaged block first:

| Its $x$ survives? | Other deletion | Move used |
|---|---|---|
| Yes | $E$ | Pair with the same first index |
| Yes | $x$ | Four-point move with $|a|\le1$, $b$ even |
| No | $E$ | Pair of equal first-index parity |
| No | $x$ | Pair of equal coordinatewise parity, if present |

In the last row, if there is no such pair, all four parity classes
occur. Any two-versus-two balanced move then has both coordinate
sums even, with absolute values at most four. All required multiples
survive by (2): a block with $x$ and two $E$-deletions is used only
for $0,\pm x$; one without $x$ has at most one $E$-deletion and
is used only for $0,\pm2x,\pm4x$.

For $t=5$, distribution $(4,0)$ again uses a pair with equal first
indices. For $(3,1)$, use that pair when the single deletion is from
$E$, and the five-point move $a=0$, $b$ even when it deletes $x$.
For $(2,2)$, if both $x$'s survive use a pair with both differences
at most one. If exactly one survives use the four-point move, with
that coordinate first. If neither survives use a pair with equal
coordinatewise parity.

Equation (3) and the surviving block representations give genuine
ternary relations in all these cases. Thus
$d(\mathcal D\cup\mathcal C)=16$.

## Scalar realization and the deficient graph

Apply $\lambda(a,b)=a+2000b$ and replace the color images by their
absolute values. This gives exactly $D,C$ displayed above. The sum
of absolute first coordinates over all columns is

$$
\sum A+3(5+10+25)=1493+120=1613<2000.
$$

Every ternary relation is therefore preserved: a scalar zero has
first coordinate zero modulo $2000$, hence zero, and then second
coordinate zero. Individual sign changes preserve dissociation.
This proves the dimension assertion in (1).

For a block coordinate $c+ix$, parity forces the $x$-coefficient to
be zero when $i=0$, and $\pm1$ otherwise. The wrong sign would
require a representation of $c\pm2x$, which was excluded. Thus
each color has exactly its prescribed ternary representation on
$\mathcal D$, with unused $x$-coordinates free only when their
indices are zero. The carry bound excludes additional scalar
representations as well.

Write

$$
U=744\cdot2001,\qquad V=734\cdot2001,\qquad
Q=\{0,15,30000,30015\}.
$$

The complete color graph consists exactly of the cross edges between
$U+Q$ and $V+Q$. Each cross difference has absolute value in $C$,
and uniqueness of the representations excludes other edges.
These are eight distinct vertices, so the graph is $K_{4,4}$ with
all other vertices of $\Sigma(D)$ isolated. Its graphic rank is
seven, proving (1).

This also shows that the arbitrary-maximum rank-seven threshold in
[[research/erdos_963/forest_restrictions|the forest restriction note]] is sharp. It
does not rule out choosing a different maximum $D$ with a rainbow
forest, or choosing a maximum-sum maximum subset.

## Two-element local exchanges are insufficient even for the count

A separate local-exchange shortcut is false. Let

$$
D=\{1,3,9,27\},\quad
P=\{1,2,3,6,7,8,9,10,17,18,20,21,26,27,29,30\}.
$$

Every element of $P$ is ternarily spanned by $D$, and every
$(D\setminus\{b\})\cup\{x,y\}$, with distinct $x,y\in P\setminus D$,
is dependent, although $|P|=16>2^{|D|}-1$.

Balanced ternary gives a unique representation of each integer in
$[-40,40]$ on $D$. If one of $x,y$ has zero $b$-coefficient, it
already lies in the span of $D\setminus\{b\}$. Otherwise change
their individual signs to make both $b$-coefficients positive.
The possible signed outside values are

$$
\begin{array}{c|l|l}
b&H_b&\operatorname{Span}_{\{-1,0,1\}}(D\setminus\{b\})\\ \hline
1&\{-29,-26,-20,-17,-8,-2,7,10\}&3[-13,13]\\
3&\{-7,-6,2,20,21,29,30\}&9[-4,4]+\{-1,0,1\}\\
9&\{-21,-20,-18,-17,6,7,8,10\}&27\{-1,0,1\}+[-4,4]\\
27&\{17,18,20,21,26,29,30\}&[-13,13].
\end{array}
$$

Intervals in this table consist of integers. Every pair difference
in $H_b$ lies in the displayed span. For the middle two rows,
the residues are respectively $2,3\pmod9$ and $6,\ldots,10\pmod{27}$;
the ranges give the displayed bounds. Thus a difference relation
excludes every proposed two-element exchange.

Nevertheless $\{1,2,6,10,20\}$ is dissociated. The first four have
subset sums $[0,3]\cup[6,13]\cup[16,19]$, and adjoining $20$
gives a disjoint translate. Thus $D$ is not maximum. This shows
that two-element local optimality cannot replace true maximal
cardinality in an argument for the desired count.
