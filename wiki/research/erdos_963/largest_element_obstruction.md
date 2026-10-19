---
name: research/erdos_963/largest_element_obstruction
title: 'A largest element need not lie in any maximum dissociated subset'
desc: Exact counterexamples to largest-element exchange, including a positive odd set of intrinsic rank one.
tags: []
sources: []
created: 2026-09-18T22:10:00Z
updated: 2026-09-18T22:17:33Z
---


# A largest element need not lie in any maximum dissociated subset

***

The following proposed exchange lemma is false: every finite positive set
has a maximum-cardinality dissociated subset containing its largest element.
Take

$$
 D=\{1,2,8,13,17\},\qquad P=D\cup\{20\}.
$$

The subset sums of $D$ are the disjoint union of the eight integer
intervals

$$
 [0,3],\ [8,11],\ [13,16],\ [17,20],\ [21,24],\ [25,28],
 [30,33],\ [38,41].
$$

There are therefore 32 distinct subset sums, so $D$ is dissociated.

Every five-subset of $P$ containing 20 is dependent. If the omitted
element is 1, use

$$
 13+17=2+8+20.
$$

If the omitted element is 2 or 17, use $8+13=1+20$. If the omitted
element is 8 or 13, use $1+2+17=20$. Thus $d(P)=5$, and $D$
is its unique maximum dissociated subset, despite omitting the largest
element.

## Exact intrinsic-rank certificate

Since $D$ is dissociated, every nonzero ternary relation on $P$
must use 20. Up to reversing all signs, the complete list is

$$
 \begin{aligned}
 20&=-1+8+13,\\
 20&=-2-8+13+17,\\
 20&=1-2+8+13,\\
 20&=1+2+17.
 \end{aligned} \tag{1}
$$

Here is a finite certificate that the list is exhaustive, without relying
on a numerical rank computation. Let $S=\Sigma(D)$, as displayed
above. The upper endpoints of its differences equal to 20 are exactly

$$
 \{s\in S:s-20\in S\}
 =\{20,21,22,23,28,30,31,33,38,39,40,41\}.
$$

There are twelve such ordered pairs of subset sums. The four signed
representations in (1) have respectively two, one, one, and two unused
coordinates of $D$. Adding an arbitrary subset of the unused
coordinates to both sides realizes respectively $4,2,2,4$ distinct
ordered pairs. These twelve pairs are distinct, because the subset-sum
map on $D$ is injective and cancellation recovers the signed
representation. They exhaust the displayed endpoint set, proving (1).

Write $(a,b,c,e,f,h)$ for formal coordinates corresponding to
$(1,2,8,13,17,20)$. The four linear equations in (1) are equivalent
to

$$
 b=2a,\qquad e=5a+c,\qquad f=a+2c,\qquad h=4a+2c.
$$

Indeed, subtraction of the first and third equations gives $b=2a$;
comparison of the first and second gives $f=a+2c$; comparison of
the first and fourth then gives $e=5a+c$, after which the first
gives $h=4a+2c$. Conversely these four identities satisfy all of
(1). Thus their relation matrix has rank exactly four, with two free
coordinates $a,c$.

The universal rational quotient by all ternary relations therefore has
intrinsic rank $\rho=6-4=2$. This example has
$d(P)-\rho=3$, just beyond the
[[research/erdos_963/corank_two|proved defect-at-most-two range]]. It is not a counterexample
to the target cardinality bound: $|P|=6$ is far below $2^5-1$.

## Search scope

The example was found by a bounded exact check of dissociated four-subsets
of $\{1,\ldots,32\}$, followed by dissociated five-subsets of
$\{1,\ldots,22\}$. For each candidate $D$, the check enumerated
its ternary representations of values above $\max D$ and sought a
value for which every coordinate is omitted by some representation.
The search stopped at the displayed counterexample. The proof and
intrinsic-rank certificate above are independent of that search.

## The exchange lemma also fails for all-odd sets

Parity does not repair the proposed lemma. Let

$$
 D'=\{1,5,7,9,19,37\},\qquad P'=D'\cup\{41\}.
$$

For $E=\{1,5,7,9\}$, its sixteen subset sums are

$$
 S=[0,1]\cup[5,10]\cup[12,17]\cup[21,22].
$$

The sets $S$ and $19+S$ are disjoint: their possible overlap is
in $[19,22]$, where they contain respectively $\{21,22\}$
and $\{19,20\}$. Put $T=S\cup(19+S)$. This has 32 elements
in $[0,41]$, with
$T\cap[37,41]=\{40,41\}$ and
$(37+T)\cap[37,41]=\{37,38\}$. Thus $T$ and $37+T$
are disjoint. These are the 64 subset sums of $D'$, proving that
$D'$ is dissociated.

Every six-subset of $P'$ containing 41 is dependent. When 1 is
omitted, use $41=-5+9+37$. When 5 is omitted, use
$41=1-7-9+19+37$. When 7, 9, or 19 is omitted, use
$41=-1+5+37$. When 37 is omitted, use
$41=1+5+7+9+19$. Hence $d(P')=6$, and its unique maximum
dissociated subset $D'$ omits the largest element, although every
element of $P'$ is positive and odd.

This example even has intrinsic rank one. Six ternary relations are

$$
\begin{aligned}
41&=-1-5-9+19+37,&41&=-1+5+37,\\
41&=-5+9+37,&41&=1-7-9+19+37,\\
41&=1+5+7-9+37,&41&=1+5+7+9+19.
\end{aligned}
$$

Replace the seven values by formal variables
$(a,b,c,u,v,w,x)$. Comparison of these equations gives successively

$$
 u=2b-a,\qquad v=u+2b,\qquad c=2a+b,\qquad u=2a+c.
$$

Thus $b=5a$, $c=7a$, $u=9a$, and $v=19a$.
The last displayed relation gives $x=41a$, and the second gives
$w=37a$. These six relations therefore have rank six. The intrinsic
quotient has rank at most one and at least one, since the original
nonzero integer configuration is a realization. Consequently
$\rho(P')=1$ and $d(P')-\rho(P')=5$.

A bounded search of odd five-subsets with largest element at most 45
found no obstruction; the subsequent search of odd six-subsets with
largest element at most 39 stopped at this example. No further search
was made. The displayed certificates prove all stated properties.

## The displayed dimension thresholds are sharp

The largest-element exchange property holds for every positive
dissociated set of size at most four, and for every positive odd
dissociated set of size at most five. Thus the two obstructions above
occur at the first possible dimensions.

The key fact holds without a bound on the size of the basis:

**Lemma.** Let $D$ be positive and dissociated, and let
$a>\max D$. If $a$ has a ternary representation on $D$ supported
on at most three coordinates, then all such representations have a
coordinate in common.

**Proof.** A support-one representation is impossible. A support-two
representation must be all-plus. A support-three representation is
either all-plus or $a=x+y-z$, where $z<x,y$: the inequalities
follow from $a>x,y$. There is at most one all-plus representation,
since subtracting two different ones would be a nonzero ternary
relation on $D$.

Two different representations must have opposite signs at some shared
coordinate. Otherwise their difference would again be a nonzero ternary
relation on $D$. Among the representations with one negative
coordinate, let $z_*$ be the largest negative coordinate. Any
representation whose negative coordinate is $z<z_*$ cannot oppose
the $z_*$-representation at $z$, because every positive coordinate
of the latter exceeds $z_*$. It must therefore contain $z_*$
positively. Representations with negative coordinate $z_*$ already
contain it. Any all-plus representation must oppose a
$z_*$-representation at its only negative coordinate, and thus also
contains $z_*$. If there is no negative-coordinate representation,
there is just one representation, and any of its coordinates works.
This proves the lemma.

Now suppose $D$ has size at most four and every exchange
$(D\setminus\{b\})\cup\{a\}$ is dependent. For each $b\in D$,
the dependence represents $a$ without using $b$. These nonfull
representations have support at most three. The lemma gives a coordinate
present in all of them, a contradiction. If $D$ and $a$ are odd
and $|D|\le5$, every representation of $a$ has odd support, so
again every nonfull representation has support at most three. The same
proof applies.

In particular, every positive odd set of dissociation dimension five
has a maximum dissociated subset containing its largest element. This
does not prove the stronger odd cardinality bound in dimension five:
longer, simultaneous exchanges are still needed for that inference.

## Retaining the top two of a given five-set

There is a modest strengthening. If
$D=\{d_1<\cdots<d_5\}$ is positive odd and dissociated and
$a>d_5$, one can exchange $a$ for one of $d_1,d_2,d_3$.
In the common-support proof, the largest negative coordinate
$z_*$ in a representation $a=x+y-z_*$ is smaller than both
positive coordinates; it therefore belongs to the first three
positions. If all nonfull representations are all-plus, there
is only one, and its smallest coordinate also lies among the
first three. Full-support representations impose no additional
restriction. If there are no nonfull representations, every
exchange works.

This cannot be iterated to obtain a maximum set containing the
two largest ambient elements. Take

$$
D=\{1,3,5,11,21\},\qquad O=D\cup\{15\}.
$$

The subset sums of $\{1,3,5\}$ are
$0,1,3,4,5,6,8,9$. Their translate by eleven is disjoint,
and the resulting sixteen sums lie in $[0,20]$, disjoint from
their translate by twenty-one. Thus $D$ is dissociated. But

$$
15=1+3+11=-1+5+11=-1-5+21=5-11+21
$$

has representations with empty common support. Every replacement
of one point of $D$ by fifteen is consequently dependent.
Thus $D$ is the unique maximum subset of $O$, omitting its
second-largest element. This rules out the proposed top-two
iteration, not the logarithmic bound.
