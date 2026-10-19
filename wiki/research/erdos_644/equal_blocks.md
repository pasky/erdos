---
name: research/erdos_644/equal_blocks
desc: A three-quarter upper bound for full profile families on any number of equal blocks of size k.
tags: [proved, upper-bounds, restricted-class]
sources: []
created: 2026-09-22T22:29:48Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/equal_blocks

***

The later [large-block theorem](large_block_profiles.md) extends the
three-quarter bound to unequal block sizes, provided every block has size at
least the uniformity.

**Theorem.** Let the ground set of a nonempty $k$-uniform family $\mathcal H$ be
partitioned into $m$ blocks, each of size $k$, and suppose the family is
invariant under arbitrary permutations within every block. If $k\ge62$ and every
at-most-seven edges have a two-point transversal, then

$$
\tau(\mathcal H)\le\frac34k+15m.
\tag{1}
$$

In particular, these families satisfy the conjectured upper bound whenever
$m=o(k)$, without a restriction on their total ground-set size. This extends
[Equal three blocks](equal_three_blocks.md), but does not address arbitrary
families.

## Continuous profiles

Let $S$ be a finite nonempty subset of

$$
\{a\in[0,c]^m:\textstyle\sum_j a_j=1\}.
$$

Write $T(S;c)$ for the infimum of $\sum_jd_j$ over vectors $0\le d_j\le c$ such
that no $a\in S$ satisfies $a\le c\mathbf1-d$ coordinatewise.

**Lemma.** If

$$
39/44\le c\le1,
\qquad T(S;c)>\frac34+m(1-c),
\tag{2}
$$

then seven profiles from $S$, with repetitions allowed, have a realization
within $m$ blocks of capacity $c$ whose point spectra are subsets of Fano caps.
Consequently no pair of points covers all seven rows.

By the [Fano-cap covering formula](fano_cap_covering.md), demands
$q_1,\ldots,q_7$ in one block can be realized in this way if

$$
q_i\le c,\qquad
\sum_{i\in L}q_i\le2c\quad\text{for every Fano line }L,
\qquad \sum_iq_i\le4c.
\tag{3}
$$

Before trimming excess incidences, at most seven cap classes are needed in each
block.

Suppose first that some $B\in S$ satisfies $B_j\le2c/3$ for all $j$. The
deletion $3B/4$ has total mass $3/4$, so (2) supplies $A\in S$ with
$A\le c\mathbf1-3B/4$. Put $B$ on one Fano line and $A$ on its complementary
cap. In block $j$, give this cap weight $\max(A_j-3B_j/4,0)$ and each of the
other six caps weight $B_j/4$. These weights cover the prescribed demands and
have total

$$
\max(A_j+3B_j/4,3B_j/2)\le c.
$$

Trim excess incidences.

Otherwise every profile has a coordinate greater than $2c/3$. This coordinate is
unique, since $4c/3>1$; call it the profile's type. For each represented type
$i$, choose a profile $A^i$ minimizing its own coordinate $h_i=A^i_i$, and set

$$
e_i=c-h_i,\qquad \epsilon=1-c.
$$

Deleting slightly more than $e_i$ in each represented coordinate removes all
profiles. Therefore

$$
T(S;c)\le\sum_{i\text{ represented}}e_i,
\qquad 0\le e_i<c/3.
\tag{4}
$$

One or two represented types contradict (2), since $2c/3\le2/3<3/4$.

If exactly three types occur, the three-type construction in
[Equal three blocks](equal_three_blocks.md) applies to their three coordinates.
Its proof uses only

$$
h_1\ge h_2\ge h_3>2c/3,
\qquad h_1+h_2+h_3<3c-3/4,
$$

and the fact that each off-type coordinate of $A^i$ is at most $1-h_i$; it does
not require all the profile mass to lie in these three coordinates. These
hypotheses follow from (4). Use the same type classes
$\{1\},\{2,3,4\},\{5,6,7\}$ on the Fano rows. The cited calculations verify (3)
in the three type coordinates. In every other coordinate each demand is less
than $1-2c/3$, so every line sum is less than $3-2c\le2c$ and the total is less
than $7-14c/3\le4c$. Thus (3) holds there as well.

It remains to handle at least four represented types. Relabel them so that

$$
e_1\ge e_2\ge e_3\ge e_4\ge\cdots.
$$

If $e_2<\epsilon$, then (4) gives

$$
T(S;c)<c/3+(m-1)\epsilon<3/4+m\epsilon,
$$

contradicting (2). Hence $e_1,e_2\ge\epsilon$.

Use the Fano lines

$$
123,\ 145,\ 167,\ 246,\ 257,\ 347,\ 356.
$$

Put $A^1$ on rows $1,2,4$, $A^2$ on rows $3,5$, $A^3$ on row $6$, and $A^4$ on
row $7$. Write

$$
\delta_i=1-h_i=\epsilon+e_i.
$$

Then $\delta_1\ge\delta_2\ge\delta_3\ge\delta_4$, and each off-type coordinate
of $A^i$ is at most $\delta_i$. Also $\delta_1<1-2c/3$.

The three type-1 rows are noncollinear. A line containing two of them has its
third row of type 2 or 3, so its demand in coordinate 1 is at most

$$
2h_1+\delta_2\le2c,
$$

because $\epsilon+e_2\le2e_1$. The line through both type-2 rows is $356$, and
its demand in coordinate 2 is at most

$$
2h_2+\delta_3\le2c,
$$

because $\epsilon+e_3\le2e_2$. Every other line-coordinate check involves zero
or one own-type row, and follows from

$$
3\delta_1<3-2c\le2c,
\qquad c+2\delta_1<2-c/3\le2c.
$$


For total demands, the first two coordinates satisfy

$$
\begin{aligned}
Q_1&\le3h_1+2\delta_2+\delta_3+\delta_4
\le3+\delta_1<4-2c/3\le4c,\\
Q_2&\le2h_2+3\delta_1+\delta_3+\delta_4
\le2+3\delta_1<5-2c\le4c.
\end{aligned}
$$

Each of coordinates 3 and 4 has total demand at most

$$
c+6\delta_1<6-3c\le4c.
$$

Every other coordinate has total demand at most

$$
7\delta_1<7-14c/3\le4c.
$$

All these estimates hold for $c\ge39/44$ (indeed $c\ge6/7$ suffices for this
four-type construction). Individual demands are already at most $c$. This proves
(3) and the lemma.

## Integer realization

Suppose (1) fails. Reserve seven points in each block and let $\mathcal H'$
consist of the edges avoiding the reserved $7m$ points. Then

$$
\tau(\mathcal H')\ge\tau(\mathcal H)-7m.
$$

In particular, $\mathcal H'$ is nonempty. Normalize its integer profiles by $k$
and put $c=(k-7)/k$. Any real deletion removing all these profiles can be
rounded upward coordinatewise to an integer deletion, increasing its size by
less than $m$. Consequently

$$
kT(S;c)\ge\tau(\mathcal H')-m
\ge\tau(\mathcal H)-8m
>3k/4+7m.
$$

Since $k\ge62$, we have $c\ge39/44$, and this is precisely (2).

Apply the lemma and multiply its cap weights by $k$. In each block their total
is at most $k-7$. Round the at-most-seven weights upward to integers; the
reserved points absorb the increase. Each row's block degree is at least its
prescribed integer value. Trim excess incidences separately in each row and
block to restore all degrees exactly.

Full block invariance ensures that every resulting row is an edge of
$\mathcal H$. Every point spectrum is still a subset of a Fano cap, so the rows
have no two-point transversal. Removing repetitions leaves a bad subfamily of at
most seven distinct edges, a contradiction.

The exactly-seven convention gives the same result: a family violating (1) has
more than seven edges, so a smaller bad subfamily can be extended to seven
distinct edges.

## Scope

The proof requires complete freedom to realize any allowed profile within every
block. It does not provide such freedom in an arbitrary family. With singleton
blocks it is not applicable, since its blocks must each have size equal to the
uniformity. Neither assertion of Problem 644 is resolved.
