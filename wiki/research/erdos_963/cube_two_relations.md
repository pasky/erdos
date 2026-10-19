---
name: research/erdos_963/cube_two_relations
title: 'Two-relation cube lifts and the uniform-core gap'
desc: Codimension-two lifting reduces to odd uniform cores; dense and sparse four-row criteria are proved, but neither is guaranteed universally.
tags: []
sources: []
created: 2026-09-19T03:50:00Z
updated: 2026-10-13T05:28:09Z
---


# Two-relation cube lifts and the uniform-core gap

***

The global assertion in [[research/erdos_963/global_lift_gap|the lift note]]
remains unproved. The following gives a new sufficient condition for a
cube-spanned extension of codimension two. It does not supply successive
compatible quotients or prove Erdős 963.

## Two relations with more than a one-coordinate exchange

**Theorem.** Let $r,s\in\{-1,0,1\}^n$ have even supports $A,B$.
If $a=|A\setminus B|$ and $b=|B\setminus A|$ are positive and
$(a,b)\ne(1,1)$, then $\ker r\cap\ker s$ is spanned by sign-cube
vertices and has dimension $n-2$.

After individual coordinate sign changes, the nonzero columns of the
two-row matrix have types

$$
(1,0),\quad(0,1),\quad(1,1),\quad(1,-1),
$$

with multiplicities $a,b,c,d$. The rows are independent because $a,b>0$.
Zero columns supply free coordinates and may be omitted from the argument.
For a cube solution, write $x,y$ for its sums in the last two groups.
The other group sums are $-x-y,-x+y$, so the feasible group sums satisfy

$$
|x|\le c,\quad |y|\le d,\quad |x+y|\le a,\quad |x-y|\le b,
\qquad x\equiv c,\quad y\equiv d\pmod2.                 \tag{1}
$$

Even row supports give $a\equiv b\equiv c+d\pmod2$.

The following feasible choices span all the available group-sum degrees
of freedom. A choice involving a positive even coordinate is omitted if
that group is empty.

* If $a,b,c,d$ are even, use $(0,0),(2,0),(0,2)$; here $a,b\ge2$.
* If $a,b$ are even and $c,d$ odd, use $(\pm1,\pm1)$.
* If $a,b\ge3$ are odd, interchange $c,d$ if needed so that $c$ is
  odd and $d$ even. Use $(\pm1,0)$ and $(\pm1,\pm2)$.
* If $a=1,b\ge3$, with $c$ odd and $d$ even, use
  $(1,0),(-1,0),(1,-2),(-1,2)$. Row interchange and sign changes
  give the remaining cases.

These same choices give a mixed-sign solution in every group of size at
least two: use zero in an even common group and $\pm1$ in an odd common
group; use group sum zero in an even exclusive group and $\pm1$ in an
odd exclusive group of size at least three. Permuting a mixed-sign
solution inside that group shows that differences of cube solutions
span its entire zero-sum coordinate subspace. Together with the
group-sum degrees of freedom and the free zero columns, this proves
the theorem.

## Exact reduction in codimension two

Let $U\subset\mathbb R^n$ be rational, admit an all-odd integer point,
and have distinct nonzero coordinate functions up to sign. Suppose
$d_U\le n-2$, in the notation of the global lift note. Consider the
inclusion-minimal supports of nonzero ternary vectors in $U^\perp$.
All have even cardinality. Their total intersection is empty, since
deleting any coordinate leaves a dependent $(n-1)$-set.

If two minimal supports differ by more than one coordinate on either
side, the theorem gives a cube-spanned $(n-2)$-space containing $U$.
Otherwise every pair differs by exactly one exchange. All supports
therefore have one common even size $k$ and form a clique in the Johnson
graph. Such a clique either consists of sets containing a fixed
$(k-1)$-set, or of sets contained in a fixed $(k+1)$-set $K$.

For completeness, write two members as $X\cup\{i\}$ and
$X\cup\{j\}$. Every other member either contains $X$, or contains
$i,j$ and all but one element of $X$. If the latter kind occurs, no
member $X\cup\{t\}$ with $t\notin\{i,j\}$ can occur; hence all
members lie in $X\cup\{i,j\}$. This proves the stated alternative.

The common-intersection alternative is impossible here. Empty total
intersection in the second alternative forces **all** the supports

$$
K\setminus\{i\},\qquad i\in K.                         \tag{2}
$$

Write $q=|K|=k+1$, which is odd and at least five, since a two-term relation
would identify two coordinates up to sign. The corresponding $q$ relation rows
form a zero-diagonal $\{\pm1\}$-matrix. Every principal $(q-1)$-minor reduces
modulo two to $I+J$ of even order, hence is invertible. Its rank is therefore
$q-1$, since the given odd point lies in its kernel. Thus the coordinate
projection $U|_K$ is an odd rational line, with distinct nonzero absolute
coordinates.

On $K$ each support in (2) has a unique relation up to reversal:
half the difference of two other orientations would be a smaller
nonzero ternary relation. Odd parity excludes a full-$q$-support
relation. Consequently the remaining scalar problem is precisely:

> If an odd $q$-vector $p$ has exactly $q$ antipodal pairs of nonzero
> ternary relations, one omitting each coordinate, must $p$ lie in a
> cube-spanned space of dimension at most $q-2$?

This is **unproved**. A solution on $K$ would suffice: add the
$n-q$ outside coordinates freely. The product of a nonzero
cube-spanned space with $\mathbb R^{n-q}$ is again cube-spanned,
by varying the added signs and using their negatives.

## Why three relation rows cannot repair a uniform core

Choose three deletion relations and let $R$ be their matrix, with
special zero coordinates $i,j,k$. All remaining entries are $\pm1$.
The principal-minor argument above implies that these rows are independent.
For a cube vertex $\varepsilon=\mathbf1-2z$,

$$
R\varepsilon/2\equiv R\mathbf1/2+
(I+J)(z_i,z_j,z_k)^{\mathsf T}+t\mathbf1\pmod2,          \tag{3}
$$

where $t$ is the parity of the other $z$-coordinates.

Only rational projective lines need consideration: on any other
line, every integer cube image $R\varepsilon$ is zero, leaving
span dimension at most $q-3$. Fix a rational line with primitive
integer generator $v$. If
$R\varepsilon$ belongs to it, then $R\varepsilon/2\in\mathbb Zv$.
The image of $I+J$ on $\mathbb F_2^3$ is the even-weight plane,
which does not contain $\mathbf1$. Its intersection with an affine
translate of $\operatorname{span}\{\mathbf1,\bar v\}$ has dimension
at most one. Equation (3) consequently restricts the special sign
triples to at most two antipodal pairs.

Two antipodal pairs in $\{\pm1\}^3$ always share an equation
$\varepsilon_a=\pm\varepsilon_b$ for some two coordinates.
The span of the whole projective-line group therefore forces that
same equality. It cannot contain $p$, whose absolute coordinates
are distinct. Thus no two-dimensional relation space inside the
span of these three rows gives the required cube-spanned annihilator.
At least four deletion relations must be involved in this repair.

## A sufficient four-row condition

There is a proved construction when four rows have sufficiently rich
sign patterns. Choose distinct $i,j,k,l$ and put
$t=r_i\pm r_j\pm r_k$. Change coordinate signs so that $r_l$ is
$1$ at every coordinate other than $l$. The coefficients of $t$ are
odd, in $\{-3,-1,1,3\}$, at the ordinary coordinates outside
$\{i,j,k,l\}$; they are in $\{-2,0,2\}$ at $i,j,k$, and
$t_l\in\{\pm1,\pm3\}$.

**Sufficient condition.** If two adjacent ordinary coefficient classes
$b_0,b_1=b_0+2$ each have multiplicity at least $23$, then
$\ker r_l\cap\ker t$ is cube-spanned of dimension $q-2$.

To prove this, fix $\varepsilon_l=1$. Choose the other three special
signs, and choose a sum in each ordinary class other than the two
large classes. In an even-sized class use $0,\pm2$, and in an
odd-sized class use $\pm1$; an empty class is omitted. The sums
$x_0,x_1$ in the two large classes must solve

$$
x_0+x_1=U,\qquad b_0x_0+b_1x_1=V,
$$

where $|U|\le7$ and $|V|\le21$. Thus $|x_0|,|x_1|\le21$.

The parity of $U$ is automatically the sum of the two large class
sizes. Requiring $x_1$ to have its prescribed parity is one congruence
modulo four,

$$
V-b_0U\equiv2m_1\pmod4.
$$

The three special signs have odd coefficients in this congruence.
Changing any one of them switches its residue by two; therefore
exactly four of their eight patterns satisfy it. These four form a
parity tetrahedron and affinely span three dimensions. The choices
in other ordinary classes do not affect the congruence, because
their coefficients $b-b_0$ are even and their allowed sums differ
by two.

Every chosen pattern is feasible in the two large classes, with
mixed signs, since their sizes are at least $23$. Independent
variations of the other class sums and the four special patterns
span the full affine space of group sums satisfying the two
equations. Permutations in each nontrivial group supply its
zero-sum subspace, as in the two-relation theorem. The resulting
cube vertices with $\varepsilon_l=1$ affinely span dimension $q-3$;
their linear span has dimension $q-2$. This proves the condition.

What remains is to guarantee such a four-row choice or handle the
sparse-pattern cases. No such general argument is established.

## A second four-row criterion for a sparse pattern

There is also a small-multiplicity case, requiring no large classes.
Let $q=a+b+4$ be odd. Suppose, after coordinate sign changes and
relabeling, that

$$
r=(0,1,\ldots,1),
$$

and $t$ has entry $1$ in the first coordinate, entries $0,0,2$ at
three special coordinates, and respectively $a$ entries $-1$ and
$b$ entries $1$ elsewhere. If $a\ge1$ and $b\ge2$, then

$$
\ker r\cap\ker t
\quad\text{is cube-spanned of dimension }q-2.             \tag{4}
$$

The first entry of $t$ may instead be $-1$, by changing that
coordinate's sign.

Fix the first cube coordinate to $1$, call the three special signs
$s_1,s_2,s_3$, and let $x_-,x_+$ be the sums in the two ordinary
groups. The equations give

$$
x_-=(1+s_3-s_1-s_2)/2,\qquad
x_+=(-1-3s_3-s_1-s_2)/2.
$$

For even $a$, the following four choices are feasible, since
$a\ge2$ and $b\ge3$ is odd:

$$
\begin{array}{c|c}
(s_1,s_2,s_3)&(x_-,x_+)\\\hline
(1,1,1)&(0,-3)\\
(-1,-1,1)&(2,-1)\\
(1,-1,-1)&(0,1)\\
(-1,1,-1)&(0,1).
\end{array}
$$

For odd $a$, use the following choices; here $b\ge2$ is even:

$$
\begin{array}{c|c}
(s_1,s_2,s_3)&(x_-,x_+)\\\hline
(1,-1,1)&(1,-2)\\
(-1,1,1)&(1,-2)\\
(1,1,-1)&(-1,0)\\
(-1,-1,-1)&(1,2).
\end{array}
$$

In either case the four special triples affinely span three
dimensions. Every ordinary group of size at least two has a
mixed-sign realization among the choices; permutations generate
its full zero-sum coordinate subspace. The affine span therefore
has dimension $3+(a-1)+(b-1)=q-3$. Since the first coordinate is
$1$, the linear span has dimension $q-2$, proving (4).

### Arranging the three special coefficients

For any four deletion rows, designate $r_l$. Some signed sum $t$
of the other three has one of the following patterns at their
three zero coordinates:

* all three coefficients are zero; or
* exactly one coefficient is $\pm2$, the other two are zero,
  and $|t_l|=1$.

Indeed, canceling each of the three special coefficients imposes
a prescribed product on one pair of row-orientation signs. If the
three constraints are compatible, satisfy them all. If they are
incompatible, six of the eight orientations satisfy exactly two
constraints. Independently, six orientations give $|t_l|=1$.
At least four orientations meet both conditions.

This controls the special coordinates but not the ordinary
$\pm1,\pm3$ classes. The new
[[research/erdos_963/large_uniform_cores|large-core theorem]] supplies a further
criterion and proves that a criterion always applies when
$q\ge761$. Smaller cores and the global extension theorem
remain unresolved.

## A checked uniform seven-point example

The known set $\{3,15,31,33,35,41,55\}$ does have a five-generator
full-sign cover, with external generators $1,7,10,12,25$:

$$
\begin{array}{rcl}
3&=&-1+7+10+12-25,\\
15&=&-1-7+10-12+25,\\
31&=&1+7+10-12+25,\\
33&=&-1+7-10+12+25,\\
35&=&1+7-10+12+25,\\
41&=&1-7+10+12+25,\\
55&=&1+7+10+12+25.
\end{array}
$$

This resolves that example only. Neither the uniform-core assertion
nor the unrestricted global extension statement follows from it.

Criterion (4) gives a direct four-row construction for the same
example. The two normals

$$
r=(0,1,-1,-1,1,-1,1),\qquad
t=(-1,0,-1,0,-1,-1,2)
$$

annihilate $p=(3,15,31,33,35,41,55)$. Orient each deletion relation
to have its first nonzero coefficient positive. Then $r$ omits
$3$, and $t$ is the relation omitting $15$, minus those omitting
$33$ and $55$. Multiplying the coordinates by
$(-1,1,-1,-1,1,-1,1)$ transforms the normals to

$$
r'=(0,1,1,1,1,1,1),\qquad t'=(1,0,1,0,-1,1,2).
$$

Thus $a=1,b=2$ in (4). This explains the successful small example
without asserting that its pattern must occur in other cores.
