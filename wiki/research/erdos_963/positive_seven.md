---
name: research/erdos_963/positive_seven
title: 'Every seven positive reals contain a dissociated four-set'
desc: A sharp positive dimension-three bound, proved by coupling the odd and even parts rather than bounding them separately.
tags: []
sources: []
created: 2026-09-19T05:10:00Z
updated: 2026-09-19T05:13:23Z
---


# Every seven positive reals contain a dissociated four-set

***

**Theorem.** Every seven distinct positive real numbers contain
a dissociated four-set. Thus the maximum size of a positive set
of dissociation dimension at most three is exactly six.

Suppose otherwise. Use the established relation-preserving integer
realization, and divide out the largest common power of two.
Write the resulting set as $P=O\sqcup E$, its odd and even parts,
with $O$ nonempty. Appending an odd element to a dissociated
subset of $E$ shows $d(E)\le2$. The established positive
dimension-two bound gives $|E|\le3$; equality requires
$E=\{u,v,u+v\}$.

Also $|O|\le4$. To see this directly, take its three largest
elements $a<b<c$. For any additional $x<a$, dependence of the
four positive odd elements forces
$c=x+a+b$ or $x+c=a+b$. Hence $x=|c-a-b|$, permitting
at most one additional element. Thus $|O|=4$ and $|E|=3$.

Write $O=\{a<b<c<d\}$. Its dependence has one of the forms

$$
d=a+b+c,\qquad a+d=b+c.
\tag{1}
$$

For each $e\in E$, join two members $x,y$ of $O$ when
$e=x+y$ or $e=|x-y|$. Every three vertices contain an edge:
otherwise those three odd numbers together with $e$ would be
dissociated, since any relation must use exactly two of the odd
numbers, by parity.

This graph is triangle-free. For $x<y<z$, if $x+z=e$, the
pair $x,y$ is not an edge. If $z-x=e$, the differences on
$x,y$ and $y,z$ are both less than $e$, so those two edges
would require $x+y=y+z=e$, impossible. A triangle-free graph
on four vertices meeting every triple contains a perfect matching:
if it had no disjoint edges, all its edges would form a star or
contain a triangle, and a star leaves an independent triple.

The three perfect matchings give the following possible common
sum-or-difference labels for their two pairs:

$$
\begin{array}{c|c}
d=a+b+c& a+b,\ a+c,\ b+c\\
a+d=b+c& b-a,\ c-a,\ b+c.
\end{array}
\tag{2}
$$

These follow by substituting (1) into the sums and positive
differences of the three pairs of pairs. Disjoint positive pairs
cannot share two such labels, since their sum and positive
difference uniquely determine a pair. Every $e\in E$ belongs
to the indicated triple, so the three-element set $E$ equals it.
In the first row its largest element is strictly less than the
sum of the other two; in the second it is strictly greater.
Neither row is an additive triple, contradicting $E=\{u,v,u+v\}$.

Sharpness is witnessed by

$$
P=\{1,3,4,5,7,8\}.
$$

Its triple $\{1,3,5\}$ is dissociated. Every four-subset contains
one of the additive triples

$$
\{1,3,4\},\ \{1,4,5\},\ \{3,4,7\},\
\{1,7,8\},\ \{3,5,8\},
$$

except $\{1,3,5,7\}$ and $\{4,5,7,8\}$, which have equal
pair sums. Thus $d(P)=3$.

## Consequence and limitation

The established odd dimension-four bound $|O|\le8$, together
with this theorem for the even part, gives

$$
d(P)\le4\Longrightarrow |P|\le14.
$$

This improves the earlier bound fifteen. The proof shows why
separate odd/even extremal bounds can overcount: their equality
configurations may be incompatible. No general joint parity
inequality $|O|+|E|\le2^{d(O\cup E)}-1$ has been proved.
