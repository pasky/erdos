---
name: research/erdos_963/primitive_order_obstructions
title: 'Exact limits of order and primitive-kernel reductions'
desc: Small examples refute two local compressions and odd ordered splitting, including in a primitive rank-one short presentation.
tags: []
sources: []
created: 2026-09-19T02:15:34Z
updated: 2026-09-19T02:15:34Z
---


# Exact limits of order and primitive-kernel reductions

***

None of these configurations violates the target cardinality bound.
They rule out the specific local reductions stated below.

## Neither Euclidean replacement of a fixed pair need preserve dimension

Let $P=\{1,4,5,6,7\}$, which has dimension three. Its four-subsets
are covered by

$$
1+4=5,\quad1+5=6,\quad1+6=7,\quad4+7=5+6,
$$

and $\{1,4,6\}$ is dissociated. Replacing either $4$ or $1$ by
their difference $3$ produces a set containing the dissociated
four-set $\{3,5,6,7\}$, whose subset sums are already listed in
[[research/erdos_963/convex_route_obstructions|the convex obstruction note]].

This refutes a dimension-preserving replacement guarantee for an
arbitrarily prescribed pair. It does not refute the existence of some
other usable pair or a more global compression.

## No one-unit suffix-gap closure need preserve dimension

Let $P=\{2,3,4,5,9\}$. Every four-subset is dependent, using

$$
2+3=5,\quad4+5=9,\quad2+3+4=9,
$$

while $\{2,3,4\}$ is dissociated. Thus $d(P)=3$.

Consider decreasing an entire suffix by one while retaining positive
distinct entries. The only possibilities are

$$
\{1,2,3,4,8\},\qquad \{2,3,4,5,8\}.
$$

They contain the dissociated sets $\{1,2,4,8\}$ and
$\{2,3,4,8\}$, respectively. For the latter the subset sums are

$$
0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17.
$$

Hence even the existence of a dimension-preserving unit suffix
compression is false.

## Odd ordered splitting fails in the primitive rank-one regime

Put

$$
O=\{1,7,11,13,15,17,19,21,25,31\}.
$$

Its lower five and upper five points are both dissociated, but $d(O)=5$.
For either five-set, its pair sums are distinct and its three smallest
points sum to more than its largest; parity rules out other relations.

Here is the exact finite certificate for the upper bound, run during
the exploration. Among the 210 six-subsets, just one has every
four-subset dissociated:

$$
E=\{1,17,19,21,25,31\}.
$$

It has the relation $1+25+31=17+19+21$. The following self-contained
checker verifies the finite coverage assertion and both lower bounds.

~~~python
from itertools import combinations

O = (1, 7, 11, 13, 15, 17, 19, 21, 25, 31)

def dissociated(D):
    S = {0}
    for a in D:
        T = {s + a for s in S}
        if S & T:
            return False
        S |= T
    return True

assert dissociated(O[:5]) and dissociated(O[5:])
exceptions = [
    C for C in combinations(O, 6)
    if all(dissociated(Q) for Q in combinations(C, 4))
]
assert exceptions == [(1, 17, 19, 21, 25, 31)]
assert 1 + 25 + 31 == 17 + 19 + 21
~~~

Every four-subset has gcd one: no prime divides more than two entries
of $O$. Moreover, its short ternary relations have a primitive,
binary-connected rank-one presentation. Nine such relations are

$$
\begin{gathered}
1+17=7+11,\quad1+7+11=19,\quad1+19=7+13,\\
1+7+13=21,\quad1+21=7+15,\quad1+7+17=25,\\
1+31=7+25,\quad1+11+13=25,\quad7+21=11+17.
\end{gathered}
$$

To verify primitivity without a determinant computation, denote the
ten generators by $a,b,c,d,e,f,g,h,i,j$ in displayed order.
The first seven relations give

$$
f=b+c-a,\quad g=a+b+c,\quad d=2a+c,\quad
h=3a+b+c,\quad e=4a+c,\quad
i=2b+c,\quad j=3b+c-a.
$$

The last two then give $c=2b-3a$ and $c=b+4a$, hence $b=7a$,
$c=11a$, and all ten generators are the specified integer multiples
of $a$. Each elimination has unit coefficient. The quotient lattice is
therefore exactly $\mathbb Z$, with no torsion, and reduction modulo
two has relation rank nine.

Thus oddness, a primitive short presentation, and primitive nearly
maximum subsets do not repair ordered splitting. A successful argument
in the remaining rank-one regime must also exploit the cardinality
threshold; this ten-point example is far below it.

## Full compression to an initial interval also fails

This is stronger than the local suffix-gap obstruction. Let

$$
P=\{1,2,3,4,5,6,7,8,9,10,12,13,15\}.
$$

Then $d(P)=4$, whereas $d(\{1,\ldots,13\})\ge5$.
The four-set $\{1,2,4,8\}\subset P$ is dissociated. The absence of
a dissociated five-subset is certified by the following exact finite
check over all $\binom{13}{5}=1287$
five-subsets. The final assertion verifies a five-subset of the
compressed interval.

~~~python
from itertools import combinations

P = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15)

def dissociated(D):
    sums = {0}
    for a in D:
        translated = {s + a for s in sums}
        if sums & translated:
            return False
        sums |= translated
    return True

assert dissociated((1, 2, 4, 8))
assert all(not dissociated(D) for D in combinations(P, 5))
assert dissociated((6, 9, 11, 12, 13))
~~~

The witness was suggested by an [online research note on small values of Problem
963](https://api.scinet.pub/f/f3753296-6ab0-4eb0-a93b-f7c0f302ca95); the three
assertions above were checked by the author from the definition and are
author-recorded. No other claim in that note is needed here.

Thus initial intervals are not universal minimizers of dissociation
dimension, even among positive integer sets. This rules out full
one-dimensional compression as a general dimension-nonincreasing
operation. It is not a counterexample to the requested bound:
$13<2^4$.
