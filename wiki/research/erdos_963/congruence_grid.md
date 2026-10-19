---
name: research/erdos_963/congruence_grid
title: 'A polynomial grid bound for the dimension-six congruence endpoint'
desc: A checked degree-fifteen interpolation argument proves at most 31 points in a positive odd unit class modulo four of dissociation dimension six.
tags: []
sources: []
created: 2026-09-19T05:10:00Z
updated: 2026-09-19T05:13:23Z
---


# A polynomial grid bound for the dimension-six congruence endpoint

***

**Theorem.** If $O$ is a positive integer set in one odd class
modulo four and $d(O)=6$, then $|O|\le31$.

This resolves the concrete endpoint $q=4,d=6$ left in
[[research/erdos_963/affine_eight|the earlier congruence argument]]. It does not
establish the unrestricted odd-set bound $2^{d-1}$.

## Reduction to a Cartesian product

The [[research/erdos_963/affine_fourteen|fourteen-point theorem]] and binary
splitting give affine bounds $7,13,26$ in dimensions $4,5,6$, respectively.
Split $O=A\sqcup B$ modulo eight. If both ordinary dimensions are at most five,
both affine dimensions are at most five, by congruence and positivity, and
$|O|\le26$. Otherwise orient the split so that $d(A)=6$. The same congruence
argument gives $d_{\rm aff}(A)=6$, so $|A|\le26$.

For any dissociated six-set $D\subset A$, of total $S_D$,
every $b\in B$ has a ternary representation on $D$ with
coefficient sum $5$ or $-3$. Positivity leaves only

$$
b=S_D-x_i\quad\hbox{or}\quad
b=2x_j+x_i-S_D\quad(i\ne j).
\tag{1}
$$

With $x_1<\cdots<x_6$, the second expression is positive
only if $j=6$, or if $i=6,j=5$. Thus $|B|\le12$.
If $|B|\le4$, already $|O|\le30$.

Assume henceforth $|B|\ge5$. Apply the binary affine split
to $A=U\sqcup V$, using all balanced ternary relations of
support at most seven. Both fibers have affine dimension at
most five. Every affinely dissociated five-set $E\subset U$
extends by **every** $a\in V$ to an affinely dissociated
six-set: a new relation would use exactly one point of $V$,
contrary to the character.

If both fibers have affine dimension at most four, then
$|O|\le14+12=26$. Otherwise orient the split so $U$ contains
an affinely dissociated five-set

$$
E=\{e_1<\cdots<e_5=M\},\qquad N=e_4,\qquad S=\sum E.
$$

We have $|U|\le13$. Each $E\cup\{a\}$, $a\in V$, is
ordinarily dissociated as well, because it lies in one unit
class modulo eight.

## Fifteen lines cover the product

Substitute $D=E\cup\{a\}$ into (1). Every $b\in B$ belongs
to one of

$$
K=\{S,2M-S\},\qquad
a+C,\qquad -a+\mathcal D,
\tag{2}
$$

where

$$
C=\{\pm(S-e):e\in E\},
$$

and $\mathcal D$ is the five-element **multiset**

$$
\{2M+e-S:e\in E\setminus\{M\}\}
\cup\{2N+M-S\}.
$$

Indeed, the constant expressions $2e-S>0$ require $e=M$.
In a negative-slope expression $2f+e-S-a>0$, $e\ne f$,
positivity requires $f=M$, or $f=N,e=M$: otherwise
$f-\sum(E\setminus\{e,f\})$ is negative because an omitted
element exceeds $f$. These cases exhaust (1).

Therefore

$$
P(x,y)=\prod_{c\in C}(y-x-c)
       \prod_{t\in\mathcal D}(y+x-t)
\tag{3}
$$

vanishes on $V\times(B\setminus K)$. Retaining repetitions
in $\mathcal D$ ensures degree fifteen. Its leading homogeneous
part is $(y-x)^{10}(y+x)^5$. The coefficients of
$x^{15-j}y^j$, $0\le j\le15$, are

$$
1,-5,5,15,-35,-1,65,-45,-45,65,-1,-35,15,5,-5,1;
$$

in particular none is zero.

For finite real sets $X,Y$ of sizes $m,n$, a polynomial of
total degree at most $m+n-2$ vanishing on $X\times Y$ has
zero coefficient of $x^{m-1}y^{n-1}$. To see this directly,
apply the univariate interpolation weights

$$
\frac{1}{\prod_{x'\in X\setminus\{x\}}(x-x')}
$$

and the analogous weights on $Y$, and sum their products times
the polynomial over the grid. Each monomial vanishes under this
functional if either exponent is too small; under the total-degree
constraint only the indicated monomial can survive, with coefficient
one. The functional is zero on a polynomial vanishing on the grid.

Both $V$ and $B\setminus K$ are nonempty. If their size sum
were at least seventeen, take nonempty subgrids whose side sizes
sum to seventeen and apply the preceding fact to (3). This
contradicts its nonzero leading coefficients. Consequently

$$
|V|+|B\setminus K|\le16.
$$

Finally,

$$
|O|\le|U|+|V|+|B\setminus K|+|B\cap K|
\le13+16+2=31.
$$


The argument was checked by the author, including its coefficient
list and the need to treat $\mathcal D$ as a multiset, and is
author-recorded. It is not
an extrapolation from searches of integer intervals.

## What remains

Splitting an arbitrary positive odd set of dimension at most six
modulo four now bounds it by $62$. The desired bound is $32$.
The analogous dimension-five odd bound remains $28$, versus the
desired $16$. The grid mechanism has not been generalized to
control the many more representation types in those unrestricted
odd configurations.

One attempted shortcut was not established: the points individually
dependent on a fixed affinely independent set were asserted to
form a lower-dimensional set. That does not follow from pointwise
dependence. The proof above avoids this claim: $U$ is a genuine
binary-character fiber whose dimension bound is proved, not an
assumed matroid closure.
