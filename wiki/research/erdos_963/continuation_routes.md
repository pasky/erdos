---
name: research/erdos_963/continuation_routes
title: 'Remaining forest and carry routes'
desc: An unproved rainbow-forest criterion, a proved binary carry-consistency test, and exact obstructions to two proposed augmentations.
tags: []
sources: []
created: 2026-09-18T22:38:00Z
updated: 2026-09-19T11:11:01Z
---


# Remaining forest and carry routes

***

The later [[research/erdos_963/forest_restrictions|forest restrictions]] prove
that any deficient color family for a maximum subset has graphic rank at least
seven. The new [[research/erdos_963/forest_obstruction|forest obstruction]]
attains that threshold and refutes the every-maximum version of the forest
assertion. Its existence version remains open. The
[[research/erdos_963/parity_fibers|parity-fiber note]] gives a proved inductive reduction;
neither route closes the target.

This note contains no proof or counterexample to the target.
The conditional statements below are not established consequences of maximum
dissociation. The carry-consistency test and the displayed obstructions are
proved. The established universal and special-case bounds remain those in
[[research/erdos_963/proof_sketch|the proof sketch]].

## A weaker replacement for upper-endpoint matching

Let $P$ be a finite positive set, let $D\subseteq P$ be maximum
dissociated, and set $S=\Sigma(D)$. On the vertex set $S$, put
an edge of color $a\in P$ between $s$ and $s+a$ whenever both
belong to $S$. Every color occurs, by ternary spanning.

The following would suffice for the target:

> For every positive $P$, some maximum $D\subseteq P$ admits a
> forest containing one edge of each color $a\in P$.

Such a forest has $|P|$ edges on $2^{|D|}$ vertices, giving

$$
 |P|\le2^{|D|}-1.
$$

The assertion for some maximum $D$ is **unproved**. The stronger
assertion for every maximum $D$ is **false**: the
[[research/erdos_963/forest_obstruction|new exact example]] has $d(P)=16$ and nine
colors inducing $K_{4,4}$ on the subset sums of one maximum $D$.
Their graphic rank is seven. The example does not refute the
existence or maximum-sum versions.

For $C\subseteq P$, write $E(C)$ for the edges with colors in
$C$, and let

$$
 r(E(C))=|S|-\#\{\text{connected components of }(S,E(C))\},
$$

counting isolated vertices as components. A forest selecting every color
exists if and only if

$$
 r(E(C))\ge |C|\qquad(C\subseteq P). \tag{1}
$$

Thus (1) states the exact missing graph inequality, not a proved estimate.
In particular, taking $C=P$ already requires the desired cardinality
bound, since the edges of the basis colors connect the whole subset-sum
cube.

Here is a self-contained justification of the forest criterion. Necessity
is immediate by restricting a selected forest to a set of colors. For
sufficiency, induct on the number of colors, allowing graph contractions
and hence parallel edges and loops. If a nonempty proper color set $J$
has rank exactly $|J|$, first select its forest by induction. It spans
all edges of $E(J)$. Contract this forest. For any remaining color set
$K$, its rank after contraction is

$$
 r(E(K)\cup E(J))-|J|\ge |K|.
$$

Apply induction to the remaining colors and lift the resulting forest.
If there is no such tight proper set and there is more than one color,
choose any nonloop edge of one color and contract it. Every nonempty set
of remaining colors previously had rank at least its size plus one;
contraction reduces rank by at most one. Induction again applies.
The one-color case follows directly from positive rank.

### Why the recorded endpoint obstruction does not settle this criterion

An upper-endpoint matching would imply such a forest: orient the chosen
edges increasingly. Distinct upper endpoints give indegree at most one,
whereas an undirected cycle would have two edges entering its greatest
vertex.

For the earlier obstruction $D=\{1,15,19,29,31\}$ and
$C=\{7,22,37\}$, the edges of these three colors are

$$
 \{44,51\},\quad\{29,51\},\quad\{44,66\},\quad\{29,66\}.
$$

They have graphic rank three, although their upper endpoints occupy only
two vertices. Selecting the first, second, and fourth edges gives a tree
with all three colors. Hence that specific Hall-deficient family for
upper endpoints is not a counterexample to (1).

There is also a valid structural observation. Colors admitting a
full-support ternary representation on $D$ can all be assigned
disjoint complement-pair edges. A full-support representation of a fixed
positive value is unique: subtracting two such representations and
dividing by two would otherwise give a nonzero ternary relation on $D$.
Its positive and negative supports are complementary subsets of $D$,
so its edge joins $s$ to $\sum D-s$. Different positive colors
give different complement pairs, which are vertex-disjoint.
These colors alone therefore satisfy (1).

The unresolved step is handling mixtures with shorter-support colors.
Neither maximality nor the full-support observation proves (1).
The next focused question is whether a graphic-rank-deficient family
forces a dissociated $(|D|+1)$-subset after a suitable basis change,
or whether a concrete counterexample refutes this forest assertion.

## Exact carry-consistency criterion for a doubled lift

Let $N$ be a power of two, and let $T=\{a_i:i\in I\}$ be an odd
dissociated set in $\mathbb Z/N\mathbb Z$. Fix integer representatives
of the $a_i$, and choose $q\in I$. For bits $s_i\in\mathbb F_2$
with $i\ne q$, form

$$
 U_s=\{a_q,a_q+N\}\cup
       \{a_i+Ns_i:i\ne q\}\subseteq\mathbb Z/2N\mathbb Z.
$$

For every vector

$$
 r_q=2,\qquad r_i\in\{-1,0,1\}\ (i\ne q),\qquad
 \sum_i r_i a_i=Nc_r,
$$

impose the binary equation

$$
 \sum_{\substack{i\ne q\\r_i\ne0}}s_i=c_r\pmod2. \tag{2}
$$

Then $U_s$ is dissociated if and only if all equations (2) hold.

To prove this, reduce a putative ternary relation on $U_s$ modulo
$N$. If the coefficients on the doubled pair sum to $-1,0,$ or
$1$, dissociation of $T$ forces every other coefficient to vanish
and the pair coefficients to sum to zero. A nontrivial opposite pair
would give the nonzero residue $N$ modulo $2N$, so it is impossible.
The two pair coefficients must therefore be equal and nonzero.
Reverse the relation so both are $1$; the projected coefficient at
$q$ is now $2$, giving exactly a vector $r$ above. The lifted
sum is

$$
 N\left(c_r+1+\sum_{i\ne q}r_i s_i\right).
$$

It vanishes modulo $2N$ precisely when the left side of (2) differs
from $c_r$. Thus imposing (2) excludes every possible new relation,
and failing any one equation supplies a relation.

Consequently such a doubled lift exists exactly when this affine binary
system is consistent. Equivalently, every binary dependency among its
row-support vectors must have corresponding right-hand sides summing to
zero. Oddness ensures each row support has even size.
No general consistency theorem was obtained.

The unrestricted full-preimage augmentation statement
$d(\pi^{-1}R)\ge d(R)+1$ is itself false: for
$\pi:\mathbb Z/4\to\mathbb Z/2$ and $R=\{1\}$, both $R$
and $\pi^{-1}R=\{1,3\}$ have dimension one. The latter elements
are antipodal. This does not refute the cyclic odd-coset cardinality
bound. Even a valid augmentation statement for larger moduli would still
leave the joint occupied-fiber/double-fiber counting gap described in
the proof sketch.

## Odd sign-compression does not always lower dimension

The following stronger-than-needed compression is false: for a positive
odd set $O$, choose $M=\max O$ and signs $\sigma_x\in\{-1,1\}$
so that

$$
C=\{M+\sigma_xx:x\in O\setminus\{M\}\}
$$

has dimension at most $d(O)-1$.

Take

$$
E=\{3,15,31,33,35,41,55\},\qquad O=E\cup\{215\}.
$$

The [[research/erdos_963/matching_obstruction|existing seven-point certificate]]
proves that every five-subset of $E$ is dissociated and every six-subset is
dependent. Since $215>\sum E=213$, adjoining $215$ increases dimension by
exactly one, so $d(O)=6$.

For any signs, the seven elements $215+\sigma_xx$ are distinct and
positive. A ternary relation on them has the form

$$
215\sum_x\varepsilon_x+\sum_x\varepsilon_x\sigma_xx=0.
$$

The second sum has absolute value at most $213$, forcing
$\sum_x\varepsilon_x=0$. Hence it gives a relation on $E$.

Each six-subset of $E$ has a unique ternary relation up to reversal.
Indeed, all its coefficients are nonzero, since every five-subset is
dissociated. Two sign vectors that were not equal or opposite would
have a nonzero half-difference supported on at most five coordinates.

Suppose $d(C)\le5$. Each of its six-subsets must therefore retain,
in balanced form, the unique corresponding relation in the seven-row
table of the cited certificate. Write the sign vector in its displayed
order as $(a,b,c,d,e,f,g)\in\{-1,1\}^7$. It must satisfy all seven
linear equations obtained from that table. Subtracting row five from
row three gives $2d=c+e$, so $c=d=e$. Subtracting row seven from
row two gives $g=2e-b$, so $b=e=g$. Row one now forces $f=e$,
and row two forces $a=e$. Row four then asserts $2e=4e$, impossible.
Thus every sign choice has $d(C)\ge6$.

This refutes the stated full-cardinality compression, not the weaker
half-cardinality compression left open in
[[research/erdos_963/large_quotient_compression|the large-quotient note]].

## Ordered disjoint intervals do not give an extra dimension

It is false that dissociated differences of $k$ disjoint ordered
intervals force a dissociated $(k+1)$-subset of their endpoints.
Choose positive rationally independent $x,y,z$ with
$x<y<z<x+y$, for example $1,\sqrt2,\sqrt3$, and put

$$
 P=\{x,y,z,x+y,y+z,x+y+z\}.
$$

These are the six positive differences between the four ordered points
$0,x,x+y,x+y+z$. Any four of those six edges contain a cycle,
which gives a ternary relation. Since $\{x,y,z\}$ is dissociated,
$d(P)=3$.

The consecutive endpoint pairs

$$
 (x,y),\quad(z,x+y),\quad(y+z,x+y+z)
$$

are disjoint ordered intervals. Their differences are

$$
 y-x,\quad x+y-z,\quad x.
$$

Their coordinate matrix relative to $x,y,z$ has determinant $-1$,
so the differences are rationally independent, hence dissociated.
This refutes the proposed increment from three differences to four
endpoints; it does not refute the target bound for the six-element set.

## A tested binary blowup does not give a low-dimensional construction

For the explicit set

$$
 P_4=\{1,2,\ldots,10,12,13,15\},
$$

the candidate $Q=\{1\}\cup2P_4\cup(2P_4+1)$ contains the
dissociated six-set

$$
 \{1,2,13,21,26,30\}.
$$

The subset sums of the last four elements are

$$
0,13,21,26,30,34,39,43,47,51,56,60,64,69,77,90.
$$

Their successive gaps are at least four. Adjoining $1,2$ replaces
each sum by its disjoint four-point block of offsets $0,1,2,3$.
Thus this specific blowup cannot serve as a dimension-five ambient
counterexample. No general blowup recurrence was proved.

Two projected-cube optimization tests also produced no counterexample.
No exact certificates were preserved for their numerical upper bounds,
and no such exclusion is used in any proof here.

## A subtraction tournament does not encode dissociation

One attempted replacement for the binary residue tree was a tournament
in which each Schur triple is cyclic. Define its antisymmetric orientation
$F(a,b)\in\{-1,1\}$ on distinct positive integers by

$$
F(a,2a)=1,\qquad F(a,b)=-F(a,b-a)\quad(a<b,\ b\ne2a).
$$

Antisymmetry and subtraction make this a terminating recursive definition.
A hoped-for implication was that a transitive subset would be dissociated.

It is false: on $\{1,2,5,8\}$, the recursion gives the transitive order

$$
5\longrightarrow1\longrightarrow2\longrightarrow8
$$

with all three other edges pointing forward as well. But $1+2+5=8$.
The set has dimension three, since $\{1,2,5\}$ is dissociated.
This rules out both the proposed extraction from this tournament's
transitive subsets and a bound of its maximum transitive size by
$d(P)$. It says nothing about the target inequality.

## Merging the two smallest elements can increase dimension

A proposed Huffman-type compression replaced the two smallest positive
weights by their sum. It was hoped that this would not increase
dissociation dimension. This is false.

Take

$$
P=\{1,2,5,6,7\},\qquad Q=\{3,5,6,7\}.
$$

The subset sums of $Q$ are the sixteen distinct values

$$
0,3,5,6,7,8,9,10,11,12,13,14,15,16,18,21.
$$

Thus $d(Q)=4$. On the other hand, every four-subset of $P$
contains one of the relations

$$
1+5=6,\qquad1+6=7,\qquad2+5=7.
$$

The triple $\{5,6,7\}$ is dissociated, so $d(P)=3$.
This also refutes the precise extension lemma asserting that
$E\cup\{a+b\}$ dissociated and $0<a<b<\min E$ force
a dissociated $(|E|+1)$-subset of $E\cup\{a,b\}$.

The obstruction persists in every higher dimension: append the same
new weight, larger than the total of all preceding weights, to both
sets. This increases both dimensions by one. Their totals agree,
so the operation can be repeated while $1,2$ remain the two smallest
weights. This rules out that particular dimension-monotone merge,
not a different compression or the logarithmic bound.

## Threshold Euler variation does not detect dissociation

For a finite positive set $D$, consider the signed atomic measure

$$
\mu_D=\sum_{S\subseteq D}(-1)^{|S|}\delta_{\sum S}.
$$

It is the distributional derivative of the threshold Euler function
$t\mapsto\sum_{\sum S\le t}(-1)^{|S|}$. Its total variation is
$2^{|D|}$ precisely when each subset-sum fiber has a single
cardinality parity; this does not require that the fiber be a singleton.

In particular, if all elements of $D$ are odd integers, then
$\sum S\equiv|S|\pmod2$. There is no cancellation within any
fiber, and $\|\mu_D\|_{\mathrm{TV}}=2^{|D|}$ regardless of
dissociation. The set $\{1,3,5,7\}$ has dimension three, because
$1+7=3+5$ while every three distinct positive odd integers are
dissociated; nevertheless its variation is sixteen.
Also $\mu_D\ne0$ for every positive $D$, since its atom at zero
comes only from the empty subset. Thus neither nonvanishing nor
maximal total variation of this Euler summary supplies dissociation
extraction. This does not rule out every use of the full threshold
family.
