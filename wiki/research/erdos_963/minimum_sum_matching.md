---
name: research/erdos_963/minimum_sum_matching
title: 'Minimum-sum choice does not repair upper-endpoint matching'
desc: A ten-element positive integer configuration refutes endpoint Hall even for the unique minimum-sum maximum dissociated subset.
tags: []
sources: []
created: 2026-09-18T23:20:00Z
updated: 2026-09-18T23:20:00Z
---


# Minimum-sum choice does not repair upper-endpoint matching

***

The following is a counterexample to an auxiliary matching assertion,
**not** to the logarithmic lower bound.

Let

$$
D=\{5,18,22,30,38,58,82\},\qquad
P=D\cup\{243,248,253\}.
$$

Then $d(P)=7$, and $D$ is its unique minimum-sum maximum dissociated
subset. Nevertheless, for $S=\Sigma(D)$ and
$N(a)=\{s\in S:s-a\in S\}$,

$$
N(243)=\{248\},\quad N(248)=\{248,253\},\quad
N(253)=\{253\}. \tag{1}
$$

Thus these three colors violate Hall's condition.

## Dissociation certificate

Put $F=\{9,11,15,19,29,41\}$, so $D=\{5\}\cup2F$.
The pair sums of $F$ are

$$
20,24,26,28,30,34,38,40,44,48,50,52,56,60,70,
$$

all distinct. All elements of $F$ are odd, so any nonzero ternary
relation has support two, four, or six. Support two is impossible.
For support four, a two-versus-two relation is excluded by the pair list;
the only triple sums at most $41$ are $35,39$, neither in $F$,
excluding one versus three. For support six, a relation partitions the
total $124$ into two sums of $62$. An odd-cardinality subset has odd
sum, so one side must be a pair; the pair list contains no $62$.
Thus $F$ is dissociated. Parity then shows $D$ is dissociated.

Each deletion of one member of $F$ still permits a ternary
representation of $5$. The four identities

$$
5=9+11-15=9+15-19=15+19-29
 =9+19+29-11-41 \tag{2}
$$

have supports with empty intersection. Hence each deletion of one
member of $E=2F$ still ternarily represents $10$.

## Maximality and minimum sum

Write $x=5$, $r=\sum E=248$, and let the three added elements be
$a=r-x$, $c=r$, $b=r+x$. Consider an eight-subset of $P$.

If it contains one added element, it contains all of $D$, on which
that element has a ternary representation. If it contains both extreme
elements $a,b$, it omits at most one member of $E$, so (2), scaled
by two, supplies a dependence using $b-a=10$.

In the remaining case it contains $c$ and exactly one extreme
element. If $x$ is present, use $x+a=c$ or $x+c=b$. If $x$
is absent, all of $E$ is present, and use $c=\sum E$.
These cases also cover subsets containing all three added elements,
through the extreme-pair case. Thus every eight-subset is dependent
and $d(P)=7$. Since $D$ consists of the seven smallest elements,
it is the unique minimum-sum seven-subset.

## The endpoint sets

Put $U=\Sigma(E)\subseteq[0,r]$. Then $S=U\sqcup(x+U)$,
where the two parts are respectively even and odd. The difference $b$
is the full diameter of $S$, so its only edge is $0\to b$.
The even difference $c=r$ has just the edges $0\to r$ and
$x\to r+x$.

For the odd difference $a=r-x$, an edge with its upper endpoint in
$U$ requires $u-v=r$, hence is $x\to r$. An edge with its upper
endpoint in $x+U$ would require $u-v=r-2x=r-10$. This would give

$$
10=(r-u)+v,
$$

a sum of two nonnegative subset sums of $E$. Since every nonzero
such sum is at least $18$, this is impossible. This proves (1).

The four edges of these colors form a four-cycle on
$\{0,5,248,253\}$. Its graphic rank is three and it admits a
rainbow spanning tree. Consequently this example leaves the weaker
[[research/erdos_963/continuation_routes|rainbow-forest assertion]] open.
