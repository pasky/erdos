---
name: research/erdos_644/equal_three_blocks
desc: A proved 3k/4-scale upper bound for full profile families on three blocks of size k, using a three-color Fano construction.
tags: [proved, upper-bounds, restricted-class]
sources: []
created: 2026-09-22T21:36:57Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_644/equal_three_blocks

***

**Theorem.** Suppose a $k$-uniform family $\mathcal H$ is invariant under
arbitrary permutations within three blocks, each of size $k$. For $k\ge62$, the
local two-point property for at most seven edges implies

$$
\tau(\mathcal H)\le\frac{3k}{4}+24.
\tag{1}
$$

The same assertion holds for the property on exactly seven distinct edges: a
family violating (1) has more than seven edges, so any smaller bad subfamily
extends to seven.

This deals with ground size $3k$, outside the range $n\le9k/4+o(k)$ of the
general many-block bound in [Block-profile families](block_profile_families.md).
It does not settle unrestricted three-block families or either assertion of
Problem 644.

## A continuous lemma

For a finite nonempty set $S$ of profiles $a=(a_1,a_2,a_3)$ satisfying

$$
a_j\in[0,c],\qquad a_1+a_2+a_3=1,
$$

write $T(S;c)$ for the infimum of $d_1+d_2+d_3$ over deletions $0\le d_j\le c$
for which no $a\in S$ satisfies $a_j\le c-d_j$ for every $j$.

**Lemma.** If

$$
\frac{39}{44}\le c\le\frac98,
\qquad T(S;c)>\frac34,
\tag{2}
$$

then seven profiles from $S$, allowing repetitions, have a weighted realization
within three blocks of capacity $c$ in which no pair of points covers the seven
rows. Before deleting excess incidences, this realization uses at most seven
support classes per block.

Use the seven Fano caps as allowable point spectra. The
[Fano-cap covering formula](fano_cap_covering.md) says that demands
$q_1,\ldots,q_7$ in one block can be realized within capacity $c$, with at most
seven covering classes before trimming, provided

$$
\max_iq_i\le c,\qquad
\sum_{i\in L}q_i\le2c\quad\text{for every Fano line }L,
\qquad \sum_iq_i\le4c.
\tag{3}
$$

Subsets of caps remain allowable spectra. No two such spectra cover all seven
rows.

If some profile $B$ satisfies $B_j\le2c/3$ for every $j$, deletion $3B/4$ has
total mass $3/4$. Hence there is a profile $A\le c\mathbf1-3B/4$. Put profile
$B$ on one Fano line and $A$ on its complementary cap. In block $j$, weight that
cap by $\max(A_j-3B_j/4,0)$, and each of the six other caps by $B_j/4$. These
cover the row demands with total mass

$$
\max\{A_j+3B_j/4,\ 3B_j/2\}\le c.
$$

Trimming excess incidences gives the desired realization.

Otherwise every profile has a coordinate exceeding $2c/3$. Since $c>3/4$, it has
exactly one such coordinate; call this its type. For every represented type $i$,
let $h_i$ be the minimum $i$th coordinate of a profile of that type, and choose
a minimizing profile $A^i$. Deleting just more than $c-h_i$ from each
represented type's block removes all profiles, so

$$
T(S;c)\le\sum_{i\text{ represented}}(c-h_i).
\tag{4}
$$

With only one or two represented types, the right side is less than
$2c/3\le3/4$. Thus all three types occur. Relabel them so that

$$
1\ge h_1\ge h_2\ge h_3>\frac{2c}{3},
\qquad H:=h_1+h_2+h_3<3c-\frac34.
\tag{5}
$$

Every off-type coordinate of $A^i$ is at most $1-h_i$.

Put profile $A^1$ on one Fano point, and profiles $A^2,A^3$ on two complementary
triples of the other six points, neither triple being a line. For instance, with
Fano lines

$$
123,\ 145,\ 167,\ 246,\ 257,\ 347,\ 356,
$$

use the three type classes $\{1\},\{2,3,4\},\{5,6,7\}$. We verify (3) separately
in every coordinate.

The maximum individual demand is at most $c$. A line containing no row of a
coordinate's own type has demand less than $3-2c\le2c$. A line containing
exactly one such row has demand at most

$$
h_1+2(1-h_3)
<\frac c3+\frac54\le2c,
$$

where (5) gives $h_1<3c-3/4-2h_3$. No type class contains a line. A line with
two own-type rows can therefore involve only type 2 or 3; its demand is at most

$$
2h_2+1-h_3
<\frac{5c}{3}+\frac14\le2c,
$$

using $2h_2+h_3\le H<3c-3/4$. These inequalities use only $c\ge3/4$.

The total demands in coordinates 1, 2, and 3, respectively, satisfy

$$
\begin{aligned}
Q_1&\le h_1+3(1-h_2)+3(1-h_3)
 <6-3c\le4c,\\
Q_2&\le3h_2+(1-h_1)+3(1-h_3)
 \le4+2h_2-3h_3
 <\frac{13}{4}+\frac c3\le4c,\\
Q_3&\le3h_3+(1-h_1)+3(1-h_2)
 \le4-h_1<4-\frac{2c}{3}\le4c.
\end{aligned}
$$

For the first inequality use $h_1\le c$; for the middle one use $2h_2\le H-h_3$.
The outer two require only $c\ge6/7$, and the middle one requires $c\ge39/44$.
This proves (3), hence the lemma.

In the special case $c=1$, the no-light-profile argument works already under
$T(S;1)>2/3$: equation (4) then gives $H<7/3$, and the same line and total
estimates apply. The light-profile case above still uses the threshold $3/4$.

## Finite rounding

Suppose (1) fails. Reserve seven points in each of the three blocks and let
$\mathcal H'$ consist of the edges disjoint from these 21 points. Then

$$
\tau(\mathcal H')\ge\tau(\mathcal H)-21>\frac{3k}{4}+3.
\tag{6}
$$

The family $\mathcal H'$ is invariant within its three remaining blocks, each of
size $k-7$.

Let $S$ be its integer profiles divided by $k$, and put $c=(k-7)/k$. Any real
deletion in these remaining blocks which removes all allowed profiles can be
rounded up separately in each block. The resulting integer deletion still
removes every edge, with increase less than three in total size. Consequently

$$
kT(S;c)\ge\tau(\mathcal H')-3>\frac{3k}{4}.
$$

For $k\ge62$, we have $39/44\le c<1$, so the continuous lemma applies.

Scale its weighted covering construction by $k$. In each block its at most seven
cap weights have total at most $k-7$. Round each weight upward to an integer.
The resulting at most seven extra points fit in the reserved points of that
block. Every row's block degree is now at least its specified integer profile
coordinate. Delete excess incidences, separately for each row and block, until
all degrees agree with their specified profiles.

Each resulting row is an edge of $\mathcal H$, by block invariance. Every point
spectrum is a subset of a Fano cap, so no pair covers the rows. Removing
repeated rows, if any, leaves a bad subfamily of at most seven distinct edges, a
contradiction.

## Scope

The proof uses full invariance within each block and constructs new edges from
allowed profiles. It cannot be applied merely because an arbitrary family has
three reference blocks. The constants are not optimized. No counterexample among
general three-or-more-block profile families has been established.
