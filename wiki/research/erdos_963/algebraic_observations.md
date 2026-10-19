---
name: research/erdos_963/algebraic_observations
title: 'High-girth counting and algebraic obstructions'
desc: A proved restriction on possible counterexamples, and two counterexamples to overly general product-space extraction principles.
tags: []
sources: []
created: 2026-09-18T22:00:00Z
updated: 2026-10-13T05:28:09Z
---


# High-girth counting and algebraic obstructions

***

These are partial results. They do not settle the regime with many short ternary
relations left open in [[research/erdos_963/proof_sketch|the proof sketch]].

## A proved counting inequality

Let $P$ be a nonempty finite positive real set, let $n=|P|$, and let
$d=d(P)$. Let $g$ be the minimum support size of a nonzero ternary
relation on $P$, with $g=\infty$ if $P$ is dissociated. For every
positive integer $h\le n$ with $2h<g$,

$$
 \binom nh\le\frac{(2h+1)^d-1}{2}.                 \tag{1}
$$


Indeed, choose a maximum dissociated $D\subseteq P$. Maximality
represents every element of $P$ as a ternary combination of $D$.
Every sum of an $h$-element subset of $P$ is therefore an image of
an integer vector in $[-h,h]^d$. Distinct such subsets have distinct
sums: otherwise canceling their intersection gives a nonzero ternary
relation of support at most $2h$. All their sums are positive. The
nonzero vectors of the cube occur in opposite pairs, each of which
contributes at most one positive image. There are
$((2h+1)^d-1)/2$ such pairs. This argument does not require rational
independence of $D$.

Consequently, a counterexample $n\ge2^d$ with $d\ge9$ must have a
ternary relation of support at most six. Otherwise (1), with $h=3$,
contradicts

$$
 \binom{512}{3}=22\,238\,720>
 \frac{7^9-1}{2}=20\,176\,803.
$$

The contradiction persists as $d$ increases: the ratio
$\binom{2N}{3}/\binom N3$ is greater than $8$, whereas
$(7^{d+1}-1)/(7^d-1)=7+6/(7^d-1)<8$ for $d\ge2$.

Also, the target $n\le2^d-1$ holds whenever $g\ge9$. If $P$
were a counterexample, maximality of $D$ would give $g\le d+1$,
so $d\ge8$. But the $h=4$ case of (1) excludes a counterexample
already for every $d\ge5$:

$$
 \binom{32}{4}=35\,960>\frac{9^5-1}{2}=29\,524.
$$

Under doubling of $N$, the left-hand side grows by a factor greater
than $16$; the ratio on the right is
$9+8/(9^d-1)<16$. The already dissociated case is immediate.

## A domain alone does not give the required product-space principle

For elements $f_1,\ldots,f_k$ of a field extension, call their
squarefree products independent if the $2^k$ products
$\prod_{i\in I}f_i$ are linearly independent over the base field.
There is no bound of the desired type using only the dimension of
$\operatorname{span}\{1,f_1,\ldots,f_n\}$ in a domain.

For distinct rational numbers $a_i$, put
$f_i=1/(t-a_i)\in\mathbb Q(t)$. The functions
$1,f_1,\ldots,f_n$ are linearly independent, as their distinct simple
poles show. However,

$$
 f_i f_j=\frac{f_i-f_j}{a_i-a_j}\qquad(i\ne j).
$$

Thus the largest subset with independent squarefree products has size
one, for arbitrarily large $n$. A linear-product argument must use
the distinguished monomial basis of a group algebra, not just the
absence of zero divisors.

## Generic linear combinations cannot simply be extracted to monomials

Even inside a monomial space, independent squarefree products of linear
combinations need not yield a monomial subset of the same size.
The exponent set $\{1,2,3\}$ has dissociation dimension two. But in
$W=\operatorname{span}_{\mathbb Q}\{x,x^2,x^3\}$, the three elements

$$
 f_1=x+x^2,\qquad f_2=x^2+x^3,\qquad f_3=x+x^3
$$

have all eight squarefree products linearly independent.

The three single factors are independent in degrees one through three:
their coefficient determinant is $2$. The coefficient matrix of
$f_1f_2,f_1f_3,f_2f_3$ in degrees four through six is

$$
 \begin{pmatrix}2&1&0\\1&1&0\\1&1&1\end{pmatrix},
$$

whose determinant is $1$. Hence their classes are independent modulo
the span of the constant and the single factors. Finally, the triple
product has degree eight, greater than every pair product. These facts
prove independence of all eight products. Any extraction from generic
linear combinations therefore needs an additional argument not supplied
by determinant expansion alone.

### The extraction obstruction also works in characteristic two

The determinant $2$ in the preceding example does not make
characteristic two an exception. Over **any** field, take

$$
f_1=t^2,\qquad f_2=t^3,\qquad f_3=t+t^2+t^3
$$

in the monomial space on exponents $\{1,2,3\}$. Their singles span
$t,t^2,t^3$. Their pair products are

$$
t^5,\qquad t^3+t^4+t^5,\qquad t^4+t^5+t^6.
$$

Modulo the span of $1,t,t^2,t^3$, their coefficient matrix in degrees
four, five, and six has determinant $-1$. The triple product
$t^6+t^7+t^8$ adds degree eight. Thus all eight squarefree products
are independent over any field, although the exponent set has
dissociation dimension two. Passing to a group algebra of characteristic
two does not repair generic-linear-combination extraction.

## A simple binary-matroid replacement is impossible

One proposed weaker alternative to a cube-spanned lift was a simple
binary matroid on $P$ such that every matroid-independent subset is
arithmetically dissociated. Its rank would be at most $d(P)$, and
simplicity would give the desired cardinality bound. Such a
replacement does not always exist, in any rank.

Take $P=\{1,2,3,4\}$. In a simple binary representation, all column
vectors $v_1,v_2,v_3,v_4$ are distinct and nonzero, so every pair
is independent. The arithmetic dependencies $1+2=3$ and $1+3=4$
would require both corresponding triples to be dependent in the
binary matroid. Therefore

$$
v_1+v_2+v_3=0,\qquad v_1+v_3+v_4=0,
$$

giving $v_2=v_4$, a contradiction.

This excludes that binary-matroid model, not the cubical covering
statement: the latter does not require arithmetic circuits to
become binary-matroid dependencies.
