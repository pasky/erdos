---
name: research/erdos_963/affine_eight
title: 'Eight real points contain an affinely dissociated five-set'
desc: A proved eight-point extraction and a strict factor 7/8 improvement in the affine cardinality bound, propagated to unit-congruence classes.
tags: []
sources: []
created: 2026-09-19T04:40:00Z
updated: 2026-09-19T04:46:10Z
---


# Eight real points contain an affinely dissociated five-set

***

Write $d_{\rm aff}(X)$ for the largest size of a subset with no
nonzero **balanced** ternary relation. This parameter concerns
distinct equal-cardinality subset sums. It is not ordinary
dissociation; the distinction is essential below.

## The eight-point theorem

**Theorem.** Every eight distinct real numbers contain five whose
restricted pair sums are distinct. Equivalently, they contain an
affinely dissociated five-set.

Form the integer matrix whose rows encode all equalities
$x_i+x_j=x_k+x_l$ on four distinct elements. Its real kernel
contains the independent vectors $\mathbf1$ and $(x_i)$, so
its rank is at most six. Reduction modulo two cannot increase
rank. There is therefore a nonconstant two-coloring such that
every additive quadruple meets each color evenly.

Suppose there is no desired five-set. A four-set with distinct
restricted pair sums in either color could be extended by any
point of the other color: a new additive quadruple would meet
that color exactly once. Thus neither color has such a four-set.
Every five distinct reals do have one: for $x_1<\cdots<x_5$,
at most one of the quadruples $(x_1,x_2,x_3,x_4)$ and
$(x_1,x_2,x_3,x_5)$ can satisfy its sole possible pair-sum
equality. Hence both color classes have exactly four elements,
each a parallelogram:

$$
T=\{t_1<t_2<t_3<t_4\},\quad t_1+t_4=t_2+t_3,
$$

and similarly $U=\{u_1<u_2<u_3<u_4\}$.

Assume $t_4-t_1\ge u_4-u_1$. Seek a five-set consisting of
$t_1,t_4$ and three points of $U$. The coloring excludes all
$3+1$ additive quadruples. A $2+2$ quadruple is possible only
at a pair of $U$ satisfying

$$
u_i+u_j=t_1+t_4\quad\hbox{or}\quad
u_j-u_i=t_4-t_1.
\tag{1}
$$

If the parallelogram centers differ, the sum condition gives at
most one pair and never the inner pair $\{u_2,u_3\}$. The
difference condition gives at most the outer pair $\{u_1,u_4\}$,
and only when diameters agree. If both offending pairs occur,
they intersect. Deleting a common endpoint leaves the required
three points, a contradiction.

If the centers agree, translate them to zero and write the eight
points as $\{\pm a,\pm b,\pm c,\pm d\}$ with
$0<a<b<c<d$. The set $\{-d,d,a,b,c\}$ has distinct restricted
pair sums unless $d=b+c-a$. In this exceptional case use
$\{-d,d,-a,b,c\}$. A quadruple containing both $-d,d$ cannot
have an equality. The other two quadruples would require
$d=a+c-b$ or $d=a+b+c$, both impossible under the exceptional
identity. This proves the theorem.

On five distinct points a nonzero balanced ternary relation must
have support four (support two would equate two points), proving
the stated equivalence.

## A binary split for affine dimension

If $|X|\ge2$ and $d_{\rm aff}(X)=d$, there is a partition into
two nonempty sets, each of affine dimension at most $d-1$.
Use all balanced ternary relations of support at most $d+1$ as
rows of an integer matrix. Again the real kernel contains
$\mathbf1$ and the distinct weight vector, so its binary kernel
has dimension at least two. Choose a nonconstant binary kernel
vector to color the points.

If one color contained an affinely dissociated $d$-set, adjoining
a point of the other would produce a balanced relation of support
at most $d+1$ using that point. The coloring contradicts the
relation. For the color-one class, use the complementary coloring,
which also annihilates the even-support rows.

The eight-point theorem and induction on this split give

$$
\boxed{d_{\rm aff}(X)=d\ge4
\quad\Longrightarrow\quad |X|\le7\,2^{d-4}.}
\tag{2}
$$

This improves the old affine count $2^{d-1}$ by a factor $7/8$.
It makes no unrestricted ordinary-dissociation claim.

## Consequences for unit classes

If a positive integer set lies in a unit class modulo $q$ and
its ordinary dimension $d$ satisfies $d\le q$, then
$d_{\rm aff}=d$. Indeed, on a set of size at most $d+1$, a
nonzero relation has both signs by positivity, so its coefficient
sum has magnitude at most $d-1<q$. Congruence forces that sum
to be zero. A larger affine-independent set would therefore give
an ordinary-independent $(d+1)$-set.

For even $q\ge4$, the proof of
[[research/erdos_963/congruence_extension|the one-more-dimension theorem]] propagates
the same factor through $d=q+1$. In its nontrivial cases the
two remaining classes have dimension at most $d-1$, giving
$2\cdot7\,2^{d-5}=7\,2^{d-4}$. The two-point exception instead
gives $7\,2^{d-5}+3\le7\,2^{d-4}$; an empty fiber is handled
directly modulo $2q$. Thus

$$
\boxed{q\ge4\text{ even},\quad4\le d\le q+1
\quad\Longrightarrow\quad |O|\le7\,2^{d-4}}
\tag{3}
$$

for positive $O$ in one unit class modulo $q$.

In particular an arbitrary positive odd set of ordinary dimension
at most five has at most $28$ elements, by its two modulo-four
classes. The known smaller odd bounds and valuation-layer
augmentation then give

$$
d(P)\le5\Longrightarrow |P|\le28+8+4+2+1=43
$$

for positive sets, and $|A|\le87$ for arbitrary real sets of
dimension at most five. This is still short of the requested
positive bound $31$, or real bound $63$.

## Two further congruence endpoints

For even $q\ge6$, the weaker count $|O|\le2^{d-1}$ also holds
when $d=q+2$. Split modulo $2q$ as $O=A\sqcup B$.
If both fibers have dimension at most $d-1$, (3) applies to
each. Otherwise choose a dissociated $d$-set
$D=\{x_1<\cdots<x_d=M\}\subset A$, and put $S=\sum D$.
Every $b\in B$ has a ternary representation on $D$ whose
coefficient sum is $d-1$ or $3-d$. Positivity leaves only

$$
b=S-x_i\quad\hbox{or}\quad b=2x_j+x_i-S\quad(i\ne j).
\tag{4}
$$

There are at most $d$ values of the first kind. A positive value
of the second kind requires $j=d$, or $i=d$ and $j=d-1$:
if neither index is $d$, the sum of the omitted positive terms
contains $M>x_j$; if $i=d$ and $j<d-1$, it contains
$x_{d-1}>x_j$. There are at most $d$ such values. Thus
$|B|\le2d$.

Since $d-1<2q$, the full fiber has affine dimension $d$ and
$|A|\le7\,2^{d-4}$ by (2). Therefore

$$
|O|\le7\,2^{d-4}+2d\le2^{d-1}\qquad(d\ge8).
\tag{5}
$$

The endpoint $q=4,d=6$ is outside this argument except when
the opposite fiber has at most four points. The subsequent
[[research/erdos_963/congruence_grid|polynomial grid proof]] settles that endpoint
in full, with the stronger bound $31$.

There is a further endpoint: for even $q\ge10$, the count holds
through $d=q+3$. If a full $d$-set lies in one modulo-$2q$
fiber, the possible coefficient sums for the opposite fiber are
$d-2$ and $4-d$. For $d-2$, the representation has either two
zeros and otherwise plus signs, or one minus sign and otherwise
plus signs, giving at most $\binom d2+d$ values. For $4-d$,
positivity allows one positive coefficient and two zeros, or
two positive coefficients with full support. For each omitted
pair there is at most one positive dominant coordinate, giving
at most $\binom d2$ values of the former type. The positive
pairs of the latter type have sum greater than $S/2$; any two
such pairs intersect, so there are at most $d-1$ of them.
Consequently the opposite fiber has at most $d^2+d-1$ values.
For $d\ge13$,

$$
7\,2^{d-4}+d^2+d-1\le2^{d-1}.
$$

If neither fiber is full-dimensional, apply the already established
$q+2$ endpoint to both. These refinements do not handle general
odd sets or establish the logarithmic target.

## A proportional congruence range

**Corollary.** For every even $q\ge56$, a positive integer set
in one unit class modulo $q$, of dimension
$d\le\lfloor4q/3\rfloor$, has at most $2^{d-1}$ elements.

Proceed by induction on $d$ at fixed $q$, starting with the
proved range $d\le q+1$. Split modulo $2q$. If both parts have
dimension at most $d-1$, induction applies. Otherwise take a
maximum $d$-set $D$ in one fiber $A$, and write $d=q+k$.
The other fiber's ternary representations on $D$ have coefficient
sum $q+1$ or $1-q$, since $d<2q$. With

$$
C_{d,j}=[x^j](1+x+x^2)^d,
$$

the numbers of such coefficient vectors are respectively
$C_{d,k-1}$ and $C_{d,k+1}$, by measuring deviations from
all plus or all minus signs. Thus

$$
|B|\le C_{d,k-1}+C_{d,k+1}.
$$

The condition $d\le4q/3$ gives $k\le d/4$. Evaluation at
$x=1/4$, using nonnegative coefficients, yields

$$
C_{d,k-1}+C_{d,k+1}
\le\frac{17}{4}\left(\frac{21\sqrt2}{16}\right)^d
\le2^{d-4}\qquad(d\ge58).
$$

For the last inequality, its square at $d=58$ is the exact
integer inequality $4624\cdot441^{58}<512^{58}$, and the
ratio decreases with $d$. Here $d\ge q+2\ge58$.

Since $d-1<2q$, the full fiber has affine dimension $d$ and
at most $7\,2^{d-4}$ points. The remaining $2^{d-4}$ slack
absorbs $B$, completing the induction. This supplies a range of
unit congruence classes, not the unrestricted odd-set bound.
