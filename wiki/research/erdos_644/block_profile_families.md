---
name: research/erdos_644/block_profile_families
desc: Proved 3k/4-scale upper bounds for block-permutation-invariant families, including an absolute-error bound for every two-block profile family.
tags: [proved, upper-bounds, restricted-class]
sources: []
created: 2026-09-22T21:16:40Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/block_profile_families

***

Neither assertion of Problem 644 is resolved here. The results below require
invariance under arbitrary permutations inside specified blocks. Completing an
arbitrary family under those permutations need not preserve its local two-point
condition.

Use the at-most-seven form of the local condition. For the stated condition on
exactly seven distinct edges, the same bounds follow: a counterexample to any
bound below has more than seven edges, so a smaller bad subfamily can be
extended to seven.

## Any number of blocks, with a ground-size term

**Theorem.** Let a $k$-uniform family $\mathcal H$ on $n$ points be invariant
under all permutations within each of $m$ blocks. If $\mathcal H$ has the local
two-point property, then

$$
\tau(\mathcal H)\le \max\{n/3,3k/4\}+8m.
\tag{1}
$$

In particular, the conjectured upper bound holds for such families when $m=o(k)$
and $n\le9k/4+o(k)$.

**Proof.** Write the block sizes as $N_j$ and put $M_j=\max(N_j-7,0)$. Suppose
the asserted bound fails. Leaving $\lfloor2M_j/3\rfloor$ points in block $j$
deletes fewer than $n/3+6m$ points altogether. Thus some edge $B$ remains; write
$b_j=|B\cap V_j|$. In particular $b_j\le2M_j/3$.

Next leave $\lfloor M_j-3b_j/4\rfloor$ points in each block. This deletes fewer
than $3k/4+8m$ points, so some edge $A$ remains. Its profile $a_j=|A\cap V_j|$
satisfies

$$
a_j+3b_j/4\le M_j.
$$


Label seven new rows by the points of a Fano plane. Three rows, on one line $L$,
are to have profile $B$; the other four, on the complementary cap $C$, are to
have profile $A$. A cap means the complement of a Fano line.

In block $j$, assign weight $\max(a_j-3b_j/4,0)$ to incidence spectrum $C$, and
weight $b_j/4$ to each of the other six caps. The $B$-rows receive exactly
$b_j$; the $A$-rows receive $\max(a_j,3b_j/4)\ge a_j$. The total weight is

$$
\max\{a_j+3b_j/4,3b_j/2\}\le M_j.
$$

Round these seven weights upward. This uses at most the seven reserved points
per block. Delete excess incidences independently in each row and block to
restore its exact integer profile. Blocks with $M_j=0$ have $a_j=b_j=0$ and
require no points.

The resulting seven sets belong to $\mathcal H$ by block invariance. Each
point's spectrum is a subset of a Fano cap. Any two caps have union of size at
most six, so no pair of points covers the seven rows. This contradiction proves
(1). $\square$

The continuous form is particularly short. If deleting any total mass below
$t>3/4$ leaves an allowed unit profile, and total capacity $N$ satisfies
$N/3<t$, first choose $B\le2n/3$, then choose $A\le n-3B/4$. The same three-$B$,
four-$A$ construction is a weighted bad tuple.

## All two-block profile families

**Theorem.** For arbitrary disjoint finite sets $X,Y$ and any collection $S$ of
feasible integer profiles, let

$$
\mathcal H=\{A\subseteq X\cup Y:|A|=k,\ |A\cap X|\in S\}.
$$

If $\mathcal H$ has the local two-point property, then

$$
\boxed{\tau(\mathcal H)\le3k/4+16.}
\tag{2}
$$

There is no restriction on $|X|+|Y|$, and $S$ need not be an interval or a union
of just two intervals. This strengthens and subsumes the earlier
[two-tail result](two_tail_obstruction.md).

### Weighted endpoint lemma

Let $0\le a\le b\le1$, put $h=b-a$, and suppose

$$
3a/4\le s\le3b/4.
$$

There is a weighted bad seven-tuple fitting block capacities

$$
x=b+s,\qquad y=7/4-a-s,
\tag{3}
$$

whose first-block row measures are all either $a$ or $b$, and whose total row
measures are one. The construction starts with at most seven weighted support
classes in each block, covering the prescribed row demands, and then deletes
excess incidences. All supports belong to one fixed downward-closed collection
in which two supports never cover $[7]$. Trimming may split a class into several
smaller spectra; the seven-class bound is needed only before trimming.

Here and below, deleting incidences from a weighted spectrum is allowed: it
replaces that spectrum by subsets and cannot create a two-point transversal.

#### Fano constructions

Choose high rows $p,q$, and let $r$ complete their Fano line. The seven caps
split into $C_0$, the cap avoiding $p,q,r$; four caps $C_1$ containing exactly
one of $p,q$; and two caps $C_2$ containing both.

For first-block demands $b,b,a,a,a,a,a$, use

$$
w(C_1)=a/4,\quad w(C_2)=(a+2h)/4,\quad
w(C_0)=\max\{0,(a-2h)/4\}.
$$

The demands are covered; trim the excess. The total mass is

$$
m_X=\max\{7a/4+h/2,3a/2+h\}.
$$

Writing $d=1-a$, the complementary demands are covered in the second block by

$$
w(C_1)=d/4,\quad w(C_2)=\max\{0,(d-2h)/4\},\quad
w(C_0)=d/2-w(C_2).
$$

Their total mass is

$$
m_Y=\max\{7(1-a)/4-h/2,3(1-a)/2\}.
$$

All weights are nonnegative. Throughout the prescribed interval for $s$, the
first mass is at most $x$; the second is at most $y$ if

$$
s\le U_F:=\min\{3a/4+h/2,\ 1/4+a/2\}.
$$

Swapping the blocks supplies a five-high construction when

$$
s\ge L_F:=\max\{3a/4+h/4,\ a/2+h/2\}.
$$

For $h\le1/2$, all four comparisons between the two upper and two lower
expressions are nonnegative: their differences are $h/4$, $a/4$, $(1-b)/4$, and
$(1-2h)/4$. Thus $U_F\ge L_F$, proving the lemma in this range.

If $h>1/2$, then $a\le1-h<h$, and the only uncovered interval is

$$
1/4+a/2<s<a/2+h/2.
\tag{4}
$$


#### A non-Fano construction

Use high rows $2,3$. The five triples

$$
F=\{136,246,237,235,234\}
$$

are pairwise intersecting. Allow their complementary four-element spectra, and
every spectrum of size at most three except the members of $F$. This is a
downward-closed collection: a forbidden triple cannot be contained in the
complement of an intersecting triple. No two allowed spectra cover $[7]$.

Since $h>1/2$ and $a\le1-h$, we have $b>2a$. In the first block put weight
$b-2a$ on $23$, and weight $a$ on each of $123,346,257$. These realize the
first-block demands exactly, with total mass $b+a$.

For the second block put $c=1-b$, $d=1-a$; then $0\le c/d<1/2$. The following
three certificates have row demands $c$ at rows $2,3$ and demand one at each
other row:

| Spectrum | $c=0$ | $c=2/7$ | $c=1/2$ |
|---|---:|---:|---:|
| $1456$ | $1/3$ | $2/7$ | $5/16$ |
| $457$ | $1/3$ | $0$ | $0$ |
| $1467$ | $1/3$ | $2/7$ | $5/16$ |
| $1567$ | $1/3$ | $2/7$ | $1/8$ |
| $346$ | $0$ | $1/7$ | $1/16$ |
| $1357$ | $0$ | $1/7$ | $1/4$ |
| $2457$ | $0$ | $2/7$ | $5/16$ |
| $236$ | $0$ | $0$ | $3/16$ |

The row sums verify the assertions directly. The total masses are
$4/3,10/7,25/16$. Interpolate adjacent columns at $c/d$, then multiply all
weights by $d$. The resulting mass is

$$
\psi(c,d)=\max\{(c+4d)/3,\ (5c+10d)/8\}.
$$

Each adjacent pair of columns uses at most seven spectra.

This construction fits (3) whenever

$$
a\le s\le U_N:=
\min\{1/12+(2a+h)/3,\ (-1+7a+5h)/8\}.
$$

Its block-swapped version fits when

$$
L_N:=\max\{(2a+h)/3,\ (7a+2h)/8\}
\le s\le b-1/4.
$$

The side conditions hold throughout (4), since $a<1/2<b$. The four comparisons
proving $U_N\ge L_N$ have differences

$$
1/12,\quad (2-5a+2h)/24,\quad
(-3+5a+7h)/24,\quad (3h-1)/8.
$$

They are positive for $h>1/2$ and $0\le a\le1-h$. The two constructions
therefore cover (4), completing the endpoint lemma.

### Proof of the finite theorem

Suppose $\tau(\mathcal H)>3k/4+16$, and write $n=|X|+|Y|$. The elementary bound
$\tau\le n-k+1$ gives $n>7k/4+15$.

If $|X|<7$, then profile zero must be allowed: otherwise $X$ itself is a
transversal. The other block has size greater than $7k/4+8$. Seven Fano classes
of size $\lceil k/4\rceil$ fit there; their cap rows have size at least $k$ and
can be trimmed to $k$. They are a bad tuple in $\mathcal H$. The case $|Y|<7$ is
symmetric.

Hence reserve seven points per block and put

$$
x_0=|X|-7,\quad y_0=|Y|-7,\quad n_0=n-14.
$$

The interval

$$
J=[\,k-4y_0/7,\ 4x_0/7\,]
$$

is nonempty. If an allowed profile $z$ lies in $J$, a uniform Fano construction
with cap weights $z/4$ in $X$ and $(k-z)/4$ in $Y$ fits inside $x_0,y_0$.

If all allowed profiles lie above $J$, let $u=\min S$. Then

$$
\tau\le |X|-u+1<3x_0/7+8<3k/4+8,
$$

where the last inequality follows from $4x_0/7<u\le k$. This is a contradiction.
The below-$J$ case is symmetric.

Thus, unless the uniform construction already applies, consecutive allowed
profiles $A<B$ surround $J$. A remaining set with block sizes $B-1,k-A-1$
contains no edge, so

$$
\tau\le n-k-(B-A)+2.
$$

Writing $h=B-A$, our assumption implies $h<n_0-7k/4$. Choose

$$
s\in[\,7k/4-A-y_0,\ x_0-B\,].
$$

This interval is nonempty and contained in $[3A/4,3B/4]$, by the strict
inequalities placing $A,B$ around $J$. The endpoint lemma, scaled by $k$, gives
a weighted bad tuple with exact row profiles $A,B$, fitting capacities
$B+s\le x_0$ and $7k/4-A-s\le y_0$.

In either construction, use the untrimmed covering certificate and round its
at-most-seven support-class weights upward separately in each block. The
reserved points absorb the increase. Delete excess incidences in each row and
block to restore its exact integer profile. The rows then belong to
$\mathcal H$, and deletion of incidences preserves the absence of a two-cover.
This contradiction proves (2). $\square$

## A checked six-spectrum certificate from the independent input

The two-profile conclusion in §8 of
[third independent record](independent/complete_family_limit_and_seven_edge_obstruction.md)
is subsumed by (2), which allows any number of profiles and has absolute error
$16$. One compact alternative certificate in that input is useful independently.

For any $x,y\ge0$, the spectra

$$
123,\quad4,\quad1456,\quad2457,\quad3467,\quad567
$$

realize row demands $(x,x,x,y,y,y,y)$ with total mass

$$
M(x,y)=\max\{x+y,\,2y-2x\}.
$$

To prove this, put $z=\min(x,y/3)$, give each of the three four-spectra
weight $z$, and give $123,4,567$ weights $x-z,y-3z,y-2z$, respectively.
These are nonnegative and give the stated row demands. Their sum is
$x+2y-3z=M(x,y)$. Any two four-spectra intersect in two positions.
Each three-spectrum intersects each four-spectrum, and all other
pairs have total size at most six. Thus no pair of spectra covers
the seven rows.

In particular, for two normalized profiles $(a,1-a),(b,1-b)$ with
$0\le a<b\le1$, on blocks of capacities $u,v$, this produces a bad
tuple whenever

$$
2-v<a+b<u,\qquad 2(b-a)<\max(u,v).
$$

If $2(b-a)<u$, use demands $(a,b)$ in the first block and
$(1-a,1-b)$ in the second; the needed masses are
$\max(a+b,2(b-a))$ and $2-a-b$. If instead $2(b-a)<v$, exchange
the two row profiles. The same spectra are used in both blocks,
so pairs from different blocks also fail to cover the rows.

For integer families whose normalized parameters converge to values
satisfying these strict inequalities, round the six class weights
up in each block and trim excess incidences in each row to restore
its exact profile. This costs fewer than six extra points per block
and cannot create a two-cover, since spectra only shrink. Strict
limiting slack absorbs this bounded cost. No claim is made at budget
equalities without separately checking rounding.

The input's numerical endpoint candidate has a separate finite arithmetic
correction and still fails the local condition; see
[Certificates and obstructions](certificates_and_obstructions.md#endpoint-two-profile-candidate-a-finite-correction).

## Scope and remaining gap

The two-block theorem includes parity restrictions, arbitrary unions of
intervals, and arbitrary subsets of allowed intersection sizes. It rules out
this entire construction class as a source of an asymptotic counterexample.

It does not provide a symmetrization theorem for arbitrary families. The proof
constructs new edges with prescribed profiles, and those edges need not belong
to a family lacking block-permutation invariance. No transfer preserving the
local property and losing only $o(k)$ in transversal number has been
established.
