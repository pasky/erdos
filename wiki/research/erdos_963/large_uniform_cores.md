---
name: research/erdos_963/large_uniform_cores
title: 'Cube extensions for every sufficiently large deletion core'
desc: A proved codimension-two sign-cube extension for odd deletion cores of size at least 761; smaller cores and the global theorem remain open.
tags: []
sources: []
created: 2026-09-19T04:30:00Z
updated: 2026-09-19T04:46:10Z
---


# Cube extensions for every sufficiently large deletion core

***

**Theorem.** Let $q\ge761$ be odd. Let $R$ be a $q\times q$
matrix with zero diagonal and off-diagonal entries $\pm1$.
If $Rp=0$ and the coordinates of $p$ have distinct nonzero
absolute values, then $p$ lies in a cube-spanned subspace of
dimension $q-2$.

Here cube-spanned means spanned over $\mathbb R$ by vectors in
$\{\pm1\}^q$. This settles all sufficiently large uniform
cores in [[research/erdos_963/cube_two_relations|the two-relation reduction]].
It does not prove the global extension assertion or Erdős 963.
The proof does not require uniqueness of the deletion relations.

## A one-large-class criterion

Suppose two normals are $r=(0,1,\ldots,1)$ and $t$, where $t$
has coefficient $1$ at the zero position of $r$, coefficients
$0,0,2$ at three special coordinates, and ordinary coefficients
with multiplicities

$$
a\text{ at }-3,\quad b\text{ at }-1,\quad
N\text{ at }1,\quad c\text{ at }3.
$$

Put $m=b+c$. If

$$
m\ge2,\qquad N\ge a+m+5,
\tag{1}
$$

then $\ker r\cap\ker t$ is cube-spanned of dimension $q-2$.

Fix the cube coordinate at the zero position of $r$ to be one.
Subtract the $r$ equation from the $t$ equation, negate the first
two special signs and the signs in the $+3$ class. The resulting
equation on the small groups is

$$
S-4x-2y=-1,\qquad S=s_1+s_2+s_3,
\quad\hbox{or}\quad 2x+y=u=(1+S)/2,
\tag{2}
$$

where $x$ sums $a$ signs and $y$ sums $m$ signs. If $m$ is even,
the allowed special patterns have $u=0,2$; if $m$ is odd, they
have $u=-1,1$. In either case the four patterns form a parity
tetrahedron and affinely span the three special coordinates.

For $a>0$, the following group sums are feasible:

$$
\begin{array}{c|c|c}
(a\bmod2,m\bmod2)&u&(x,y)\\\hline
(0,0)&0&(0,0)\\
&2&(0,2),(2,-2)\\\hline
(0,1)&-1&(0,-1)\\
&1&(0,1),(2,-3)\\\hline
(1,0)&0&(1,-2),(-1,2)\\
&2&(1,0)\\\hline
(1,1)&-1&(-1,1),(1,-3)\\
&1&(1,-1)
\end{array}
$$

Positive even $a$ is at least two, and odd $m\ge2$ is at least
three, so capacities and parities hold. At one fixed special
pattern, the two listed choices give an additional group-sum
direction. Each group of size at least two has a mixed-sign
choice; permutations generate its full zero-sum coordinate space.
Together these give affine dimension $a+m+2$, the full dimension
of the hyperplane (2). If $a=0$, use $x=0,y=u$ instead; the
same dimension statement follows without the extra group-sum
direction.

The $r$ equation determines the sum in the large group. For every
small solution its absolute value is at most $a+m+3\le N-2$.
Its parity is $N$, since $q=4+a+m+N$ is odd. Thus every small
solution lifts with mixed signs in that group. Permutations add
$N-1$ affine dimensions, for a total of $q-3$. Because the fixed
coordinate is one, the linear span has dimension $q-2$.

## Four-wise sign balance

Choose four deletion rows. If their coordinatewise product has
at least $92$ positive and $92$ negative coordinates outside
the four deleted positions, the previously proved dense criterion
applies.

To see this, normalize the fourth row to one outside its zero.
The other three rows give eight three-bit patterns, four in each
parity class. Each parity class has a pattern occurring at least
$23$ times. The two selected patterns have odd Hamming distance.
If their distance is one, orient the three rows so their signed
sums differ by two. If their distance is three, they are antipodal;
orient the rows to give signed sums $1,-1$. Thus two adjacent
coefficient classes each have multiplicity at least $23$, as
required by [[research/erdos_963/cube_two_relations|the dense four-row lemma]].

## If no quadruple is balanced

Assume no quadruple meets that criterion. Fix three indices
$a,b,c$, and set

$$
f_j=r_{aj}r_{bj}r_{cj}\quad(j\notin\{a,b,c\}),
$$

choosing arbitrary signs on the three exceptional coordinates.
For every other row $i$, orient it so $r_{ij}f_j$ is negative
at most $91$ times outside $\{a,b,c,i\}$. This is possible by
the failed balance criterion. Now apply the common coordinate
signing $f$. Each of the $q-3$ resulting good rows has at most

$$
D=91+3=94
$$

negative entries. Write $N_i$ for its negative support.

These supports are distinct. If $N_i=N_j$, neither set contains
$i$ or $j$, and the two rows differ by $e_j-e_i$. Applying them
to the transformed kernel vector would equate two of its
coordinates, contrary to distinct absolute values.

On the good indices, join $i,j$ when $i\in N_j$ or $j\in N_i$.
Every induced subgraph has at most $D$ times its number of vertices
edges, so it is $2D$-degenerate and $(2D+1)$-colorable. Since

$$
q-3>4(2D+1)=756,
$$

there is an independent set of five good indices.

Among five distinct binary sets, some four have symmetric difference
of size at least two. Otherwise, writing $T$ for the symmetric
difference of all five and $U_i=T\mathbin\triangle N_i$, the
five $U_i$ would be distinct sets of size at most one whose
symmetric difference is empty. At least four are distinct
singletons, which makes that impossible.

Choose four of the independent indices $i,j,k,l$ with this
property, and put $t=r_i+r_j-r_k$. Independence says every
internal off-diagonal entry is $+1$, so

$$
t_i=t_j=0,\quad t_k=2,\quad t_l=1.
$$

Normalize $r_l$ to one outside $l$; its zero coordinate may be
left unchanged. The special coefficients do not change. Let
$a,b,N,c$ denote the ordinary multiplicities of $-3,-1,1,3$.
The normalized coefficient is $-1$ or $3$ exactly when the
four-row product is negative. None of the five selected indices
belongs to any of their negative supports. Consequently

$$
m=b+c=|N_i\triangle N_j\triangle N_k\triangle N_l|\ge2.
$$

Outside the union of these four negative supports, every ordinary
coefficient is one. Hence

$$
N\ge q-4-4D,\qquad a+m\le4D.
$$

The assumption $q\ge8D+9=761$ implies $N\ge a+m+5$.
Criterion (1) proves the theorem. All constructed normals are
linear combinations of transformed rows of $R$, so their common
kernel contains the transformed $p$; undoing coordinate signs
preserves cube-spannedness.

## The size-five core is impossible

A zero-diagonal sign relation matrix on five distinct nonzero
absolute coordinates cannot have such a kernel vector. Change
coordinate signs and sort it as $0<a<b<c<d<e$. A signed relation
on four ordered positive values $x<y<z<w$ requires
$w=y+z\pm x$. Applying this to deletion of $e$ and $d$, and
using $d<e$, gives

$$
d=b+c-a,\qquad e=b+c+a.
$$

Deletion of $c$ gives either $a=b$ or $b=3a$. In the latter
case $d=c+2a$ and $e=c+4a$. Deletion of $b$ then gives either
$c=a$ or $c=3a=b$, again impossible.

Thus the uniform-core extension question remains only at odd
sizes $7\le q\le759$. This is a bounded range of sizes, not a
checked finite certificate for all those configurations. Moreover,
even settling every such core would not establish the unrestricted
global cube-extension assertion.
