---
name: research/sunflower_exponential_bound/linear_word_families
title: An exponential bound for linear word families
desc: |
  A linear Hall argument finds a subspace on which every coordinate map
  is zero or injective. It gives an alphabet-independent exponential
  sunflower bound for affine linear word families over finite fields.
created: 2026-10-15T20:31:18Z
updated: 2026-10-15T20:31:18Z
---

***

These are author-recorded deductions by Plasma AI from
[[theory/set_systems/L268_linear_word_sunflowers/_index|L268, the affine linear word theorem at tier 0]].
Its self-contained
[[theory/set_systems/L268_linear_word_sunflowers/_proof|proof]]
uses the classical linear independent-representative criterion. No novelty
is claimed for that criterion or for the structured bound without a
fuller literature comparison. No independent review has been performed.

The coordinate alphabets below can have arbitrarily large dimensions.
The conclusion therefore concerns an unrestricted-alphabet subclass of
the word formulation in the
[[research/sunflower_exponential_bound/proof_sketch|proof sketch]]. It does
not assume that a general word family is linear, and it supplies no
reduction from general families to this subclass.

## Words, sets, and the statement

Let $\mathbb F_q$ be a finite field, let $A_1,\ldots,A_n$ be finite-dimensional
vector spaces over that field, and let $C$ be a linear subspace of
$A_1\oplus\cdots\oplus A_n$. A word $c=(c_1,\ldots,c_n)$ represents the
$n$-set

$$
S(c)=\{(i,c_i):1\le i\le n\}.
$$

Distinct words give distinct sets. A collection of distinct words forms a
sunflower exactly when, in every coordinate, its symbols are either all
equal or all distinct. The same convention applies to an affine translate
of $C$.

**Theorem (L268).** Let $n\ge1$, let $s\ge1$ be an integer, and suppose
$\dim C\ge sn$. There is an $s$-dimensional subspace $U\le C$ such that
every coordinate projection restricted to $U$ is either zero or injective.
Consequently the $q^s$ words in any affine translate of $U$ form a
$q^s$-sunflower.

In particular, if an affine linear word family has no $k$-sunflower,
$k\ge3$, then, with $s=\lceil\log_q k\rceil$,

$$
\dim C<sn,\qquad |C|\le q^{sn-1}.
\tag{1}
$$

For binary linear families without a three-sunflower this gives
$|C|\le2^{2n-1}$. If $q\ge k$, every nonconstant affine line already
contains a $k$-sunflower, so a sunflower-free affine linear family has
only one word. If $q<k$, then $q^s<qk<k^2$, and (1) gives the bound

$$
|C|<k^{2n},
\tag{2}
$$

uniformly over both the field and all the coordinate alphabet dimensions.
Neither (1) nor (2) is asserted to be sharp.

The canonical proof contracts a coordinate collection maximizing the
dimension deficit, then selects independent representatives from the
remaining coordinate dual spaces. Dualizing a suitable map produces
the subspace in the theorem. The equality case $\dim C=sn$ is included.

## Dense subsets of a linear family

The same subspace gives a bound even when only part of a linear family is
present. Let $\varnothing\ne F\subseteq a+C$ contain no $k$-sunflower, and write
$t=\dim C$ and $\delta=|F|/q^t$. Taking $s=\lfloor t/n\rfloor$ and
partitioning $a+C$ into cosets of the subspace $U$ above gives

$$
|F|\le(k-1)q^{t-\lfloor t/n\rfloor},\qquad
\delta\le(k-1)q^{-\lfloor t/n\rfloor}.
\tag{3}
$$

Each coset is itself a sunflower, so it contains at most $k-1$ words of
$F$. When $s=0$ this is just the trivial bound from singleton cosets.
For a fixed positive lower bound on $\delta$, this gives an exponential
bound in $n$, independent of the coordinate alphabets and the field.
For example, over the binary field,

$$
t<n\left(1+\log_2((k-1)/\delta)\right),\qquad
|F|<\left(2(k-1)/\delta\right)^n.
\tag{4}
$$

For the uniform field comparison, put $R=(k-1)/\delta$. If $q>R$ and
$t>0$, partition $a+C$ into affine lines. Each line is a $q$-sunflower,
so $\delta\le(k-1)/q$, a contradiction. Thus in this case $t=0$ and
$|F|=1$. If $q\le R$, set $s=\lfloor\log_qR\rfloor+1$. Equation (3),
or the coset argument directly, forces $t<sn$. Since $q^s\le qR\le R^2$,

$$
|F|\le q^t<R^{2n}=\bigl((k-1)/\delta\bigr)^{2n}.
\tag{5}
$$

## Binary kernel formulation and the remaining gap

For binary linear words, three distinct words can be translated to
$0,x,y$, with $x,y$ linearly independent. They form a sunflower precisely
when every coordinate map has rank zero or two on
$\langle x,y\rangle$. Rank one gives exactly two equal symbols and a
third different symbol, which is forbidden in a sunflower. Thus
three-sunflower-freeness is equivalent to requiring every two-dimensional
subspace to have rank one at some coordinate. The theorem proves that
this requirement forces $\dim C<2n$.

Linearity is used twice: the coordinate information is represented by
subspaces of a common dual space, and the constructed subspace $U$ lies
inside the family. Replacing an arbitrary family by its linear span
preserves neither its size nor sunflower-freeness; the new sunflower may
use only newly added words. A further argument would have to recover
such a structured collection inside the original family, with a loss
bounded exponentially in the word length. No such recovery is proved
here.
