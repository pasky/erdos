---
name: research/erdos_617/partial_net_obstruction
desc: Partial clique resolutions alone permit linearly large deficiencies in every class; a parameterized model that fails the actual independence constraints.
tags: [graph-theory, constructions, obstruction, proved]
sources: []
created: 2026-09-22T00:36:06Z
updated: 2026-09-24T22:12:59Z
---


# research/erdos_617/partial_net_obstruction

***

**Proved obstruction to a relaxation, not a coloring counterexample.**
The partial resolutions supplied by the
[two-support reduction](two_supported_private_cliques.md), considered
only as an incidence system, do not force a class with small maximum
private deficit. For every power of two $q\ge8$, the construction below
has $q^2+1$ points and $q-1$ classes with the following properties:

- Each class consists of $q$ disjoint blocks of size at most $q$.
- Blocks from different classes intersect in at most one point.
- Every point belongs to a block in all but at most one class.
- An anchor set $Q$ of order $q$ meets every block exactly once.
- The defined anchor symbols of any point outside $Q$ are distinct.
- Every class has a block whose deficit from $q$ is $\Theta(q)$, and
  each class misses at most $q$ points.

Here the anchor symbol of a point in a class means the anchor in its
block. These are incidence conditions only: independence-number
constraints on color graphs are not assumed.

## Construction

Start with $\mathbb F_q^2$, and take $Q=\{(0,y):y\in\mathbb F_q\}$.
Choose a set $A\subseteq\mathbb F_q$ of $q-2$ slopes, and write the
remaining two slopes as $c_0,c_1$. Retain the $q-1$ nonvertical parallel
classes with slopes in $A\cup\{c_0\}$.

For every slope $a$, distinguish the line

$$
L_a:\quad y=ax+a^2.
$$

Its anchor is $(0,a^2)$, so the distinguished anchors are distinct.
For distinct $a,b$, characteristic two gives

$$
L_a\cap L_b=\{(a+b,ab)\}.
$$

This point is off $Q$. No three distinguished lines concur: a point
$(x,y)$ on $L_a$ satisfies $a^2+xa+y=0$, a quadratic with at most two
roots. In particular, distinct unordered pairs of distinguished lines
have distinct intersection points.

Orient the complete graph on $A$ with every indegree in

$$
\left\{\frac{q-4}{2},\frac{q-2}{2}\right\}.
$$

Such an orientation is obtained by deleting one vertex from a regular
tournament on the odd number $q-1$ of vertices. A regular tournament
itself is given by orienting $i$ toward $i+1,\ldots,i+(q-2)/2$ modulo
$q-1$.

For each oriented pair $b\to a$, delete the point $L_a\cap L_b$ from
the block $L_a$, but not from the other blocks containing that point.
Add a new point $p$ to every distinguished block $L_a$ with $a\in A$.
It belongs to no block of the class $c_0$.

Finally, delete any $q/2$ nonanchor points from $L_{c_0}$ in its own
class. None was deleted previously, since such a point cannot be the
intersection of two distinguished lines with slopes in $A$.

## Verification of the relaxation

The modifications never delete an anchor. Within a class, blocks remain
disjoint, and $p$ is added to just one block. Between two modified
classes, the old intersection of their distinguished blocks was deleted
from one of them; adding $p$ therefore leaves their intersection of
size one. All other pairs of blocks still intersect in at most one
point.

Every old point is deleted from at most one class, because the pairwise
intersection points used for the first deletions are all distinct and
none lies on $L_{c_0}$. The new point misses just the class $c_0$.

For an old point $(x,y)$ outside $Q$, the anchor symbols of its blocks
are $(0,y-ax)$ as $a$ ranges over the retained slopes. They are distinct
because $x\ne0$. Deletion of a symbol preserves this property. The
defined symbols of $p$ are $(0,a^2)$ for $a\in A$, also distinct.

If the indegree of $a\in A$ is $h_a$, its distinguished block has
order $q-h_a+1$ and deficit $h_a-1$. All other blocks in that class
still have order $q$, and the class misses exactly $h_a$ points.
Thus its maximum deficit lies between $(q-6)/2$ and $(q-4)/2$.
The distinguished block in class $c_0$ has order $q/2$, and that
class misses $q/2+1$ points. These formulas prove the claimed size,
deficiency, and missing-point bounds.

## Why this is not a coloring

In every class exactly one block is deficient. It cannot be the
two-supported private-clique system of a color graph satisfying the original
independence and local-cap conditions. In such a system an exception
cannot be supported on two full rows. Consequently every exception
would have to join the single deficient anchor to a full anchor.
The [full-row capacity lemma](two_supported_private_cliques.md)
then makes all these exceptions a clique complete to the deficient
private block. Their number is its deficit plus one, producing a
forbidden $K_{q+1}$.

Therefore incidence/rank arguments using only the listed partial-net
conditions cannot prove a sublinear maximum-deficit conclusion. This
does not rule out an incidence argument that also uses the missing
independence constraints, nor does it produce an edge coloring of the
complete graph with the required property.
