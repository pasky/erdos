---
name: research/erdos_644/large_block_profiles
desc: A non-Fano construction handles a two-coordinate transversal of heavy supports, and yields the three-quarter bound for unequal blocks of size at least the uniformity.
tags: [proved, upper-bounds, restricted-class]
sources: []
created: 2026-09-23T01:12:19Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/large_block_profiles

***

This page proves two restricted results. The first applies to arbitrary
capacities when the heavy supports have a transversal of size at most two. The
second proves

$$
\tau(\mathcal H)\le \frac34k+15m
$$

for full $m$-block $k$-uniform families with the local seven-edge property,
provided every block has size at least $k$ and $k\ge70$. The block sizes need
not be equal, and there is no upper bound on their total size. These results do
not resolve the arbitrary-capacity profile question or either unrestricted
assertion of [Problem 644](../../problems/set_systems/E0644/_index.md).

## Definitions

Let $S\subseteq\prod_{j=1}^m[0,c_j]$ be a finite nonempty set of profiles, each
of coordinate sum one. Define $T(S;c)$ to be the infimum of $\sum_jd_j$ over
vectors $0\le d_j\le c_j$ for which no $A\in S$ satisfies $A\le c-d$
coordinatewise.

A weighted realization of an ordered tuple of profiles assigns nonnegative mass
to point spectra, separately in each block. A spectrum is the subset of row
indices containing the point. Its total mass in block $j$ is at most $c_j$, and
its row demands equal the chosen profiles. A realization is **bad** if no two
appearing spectra have union equal to the whole row set. Repeated profiles are
allowed.

We may first cover, rather than realize exactly, the prescribed row demands, and
then delete excess incidences. Deleting incidences replaces spectra by subsets,
so it cannot create a two-point cover.

The **heavy support** of $A$ is

$$
H(A)=\{j:A_j>2c_j/3\}.
$$

A profile with empty heavy support is called light on this page.

We will use subadditivity of the deletion threshold. If $S=S_1\cup S_2$ with
both subfamilies nonempty, then

$$
T(S;c)\le T(S_1;c)+T(S_2;c).
\tag{1}
$$

Indeed, combine deletion vectors for the two subfamilies by adding them
coordinatewise and truncating at $c$. The combined deletion removes both
subfamilies and has no greater total mass than the sum of the two original
deletion masses. Taking infima proves (1).

## A non-Fano seven-row construction

Distinguish four rows $X_1,\ldots,X_4$ and three rows $Y_1,Y_2,Y_3$. Allow
spectra consisting of any three $X$ rows together with one $Y$ row, and also the
spectrum consisting of all three $Y$ rows. Allow subsets of these spectra as
well.

No two allowed spectra cover all seven rows. Two spectra of the first kind cover
at most two $Y$ rows. A spectrum of the first kind together with the all-$Y$
spectrum misses an $X$ row. Two all-$Y$ spectra miss every $X$ row.

**Proper-triple covering lemma.** Suppose the four $X$ demands in a block are
$a_1,\ldots,a_4\ge0$, and all three $Y$ demands are $b\ge0$. Put

$$
z=\max\left\{\max_i a_i,\ \frac{a_1+a_2+a_3+a_4}{3}\right\}.
\tag{2}
$$

The demands have a covering realization using the allowed spectra and total mass

$$
\max\{z,\ b+2z/3\}.
\tag{3}
$$


**Proof.** Each $z-a_i$ is nonnegative, and

$$
\sum_{i=1}^4(z-a_i)\ge z.
$$

Choose $w_i\ge0$ with $\sum_iw_i=z$ and $w_i\le z-a_i$. Give the triple of $X$
rows omitting $X_i$ total weight $w_i$, divided equally among its three possible
accompanying $Y$ singletons. Each $X_i$ receives weight $z-w_i\ge a_i$, and each
$Y$ row receives $z/3$. Add weight $\max\{b-z/3,0\}$ on the all-$Y$ spectrum.
The resulting mass is (3). The case $z=0$ is included. $\square$

In particular, four copies of a profile $A$ and three copies of $B$ are
bad-realizable if

$$
\frac43A\le c,
\qquad B+\frac89A\le c.
\tag{4}
$$

The sufficient conditions $A\le3c/4$ and $A+B\le c$ imply (4). The selection
argument below needs the unequal-demand form (2), not just this special case.

## Two coordinates meeting all heavy supports

**Theorem.** Suppose $T(S;c)>3/4$. If $S$ has a light profile, or if its heavy
supports have a transversal of size at most two, then at most seven profiles
from $S$ have a bad weighted realization.

### The light-profile case

Take a light profile $B$. Deleting $3B/4$ costs $3/4$, so there is an $A\in S$
with

$$
A+3B/4\le c.
$$

Place three copies of $B$ on a Fano line and four copies of $A$ on its
complementary cap. In block $j$, give this cap weight $\max\{A_j-3B_j/4,0\}$ and
each of the other six caps weight $B_j/4$. These weights cover the prescribed
demands, and their total is

$$
\max\{A_j+3B_j/4,\ 3B_j/2\}\le c_j.
$$

Two Fano caps cannot cover all seven rows. Trimming therefore gives a bad
realization. This is the same light-profile construction as in
[Full profile families](block_profile_families.md).

### The two-coordinate case

Assume that there is no light profile. If one coordinate $g$ is heavy for every
profile, put $h=\min_{A\in S}A_g$. Deleting slightly more than $c_g-h$ in that
coordinate removes all profiles. But

$$
c_g-h<c_g/3<1/2,
$$

where $c_g<3/2$ follows from $1\ge h>2c_g/3$. This contradicts $T(S;c)>3/4$.

It remains to consider two distinct coordinates $g_1,g_2$ meeting all the heavy
supports. Partition $S$ into nonempty subfamilies $S_1,S_2$ so that $g_i$ is
heavy for every profile in $S_i$. Write

$$
t_i=T(S_i;c),\qquad
h_i=\min_{A\in S_i}A_{g_i},\qquad
e_i=c_{g_i}-h_i.
$$

Deleting slightly more than $e_i$ in coordinate $g_i$ removes $S_i$.
Consequently

$$
t_i\le e_i<c_{g_i}/3<1/2,
\qquad h_i>2e_i\ge2t_i,
\qquad c_{g_i}/3>t_i.
\tag{5}
$$

Subadditivity and the hypothesis give $t_1+t_2>3/4$. Relabel so that
$t_1\ge t_2$. Then

$$
t_1>3/8,\qquad t_2>1/4,\qquad t_1+2t_2>1.
\tag{6}
$$


Choose $Q\in S_1$. Since $t_1>1/3$, deletion of $Q/3$ leaves an $A\in S_1$ with

$$
A+Q/3\le c.
\tag{7}
$$

For the four profiles $Q,A,A,A$, define

$$
z_j=\max\{Q_j,\ A_j+Q_j/3\}.
\tag{8}
$$

This is exactly the quantity (2) for their four demands in block $j$, and (7)
gives $z\le c$. Every profile in $S_1$ has mass outside $g_1$ less than
$1-2t_1$, by (5). Since $z_j\le Q_j+A_j$,

$$
\sum_{j\ne g_1}z_j<2(1-2t_1).
\tag{9}
$$


Delete $2z_j/3$ in each coordinate $j\ne g_1$, and delete nothing at $g_1$. This
deletion is feasible, and its total mass is less than

$$
\frac43(1-2t_1)<\frac34-t_1<t_2.
\tag{10}
$$

For the middle inequality, subtract its right-hand side from its left-hand side
to obtain $7/12-5t_1/3<0$, using $t_1>3/8$. Hence some $B\in S_2$ satisfies

$$
B_j+2z_j/3\le c_j\qquad(j\ne g_1).
$$

The remaining coordinate also satisfies this inequality: because $g_1\ne g_2$,
equations (5) and (6) give

$$
B_{g_1}<1-2t_2<t_1<c_{g_1}/3
\le c_{g_1}-2z_{g_1}/3.
\tag{11}
$$

Thus $B+2z/3\le c$ everywhere. Apply the proper-triple covering lemma in each
block, with four $X$ profiles $Q,A,A,A$ and three $Y$ profiles $B,B,B$. Its
required mass is at most $c_j$ by (3). Trim the excess incidences to finish the
proof. $\square$

No uniqueness assumption on heavy coordinates was used. A profile in $S_i$ may
also be heavy at other coordinates. In particular, this theorem applies to
arbitrary capacities whenever there are at most two distinct profiles: choose
one heavy coordinate of each nonlight profile.

## Unequal capacities close to or above one

**Continuous theorem.** Let $0\le\epsilon\le1/10$, and suppose

$$
c_j\ge1-\epsilon\quad(1\le j\le m),
\qquad
T(S;c)>\frac34+m\epsilon.
\tag{12}
$$

Then seven profiles from $S$, with repetitions allowed, have a bad weighted
realization.

**Proof.** A light profile has already been handled. Otherwise every profile has
exactly one heavy coordinate: two such coordinates would have total demand
greater than $4(1-\epsilon)/3>1$. Call this coordinate its type.

For each represented type $i$, choose a profile $A^i$ minimizing its demand in
coordinate $i$. Put

$$
h_i=A^i_i,\qquad e_i=c_i-h_i,\qquad\delta_i=1-h_i,
\qquad D=\frac{1+2\epsilon}{3}.
$$

Every off-type coordinate of $A^i$ is at most $\delta_i$. Moreover,

$$
0\le e_i<c_i/3,\qquad e_i<1/2,
\qquad
0\le\delta_i<D,\quad
\delta_i\le e_i+\epsilon,\quad
\delta_i<1-2e_i.
\tag{13}
$$

For example, $h_i>2c_i/3$ gives $h_i>2e_i$ and hence $e_i<1/2$, while
$c_i\ge1-\epsilon$ gives $\delta_i\le e_i+\epsilon$.

Deleting slightly more than $e_i$ in every represented type coordinate removes
every profile. Therefore

$$
\sum_{i\text{ represented}}e_i
\ge T(S;c)>\frac34+m\epsilon.
\tag{14}
$$

One or two represented types are covered by the preceding theorem. We henceforth
assume that there are at least three.

We use the Fano lines

$$
123,\quad145,\quad167,\quad246,\quad257,\quad347,\quad356.
\tag{15}
$$

By the [Fano-cap covering formula](fano_cap_covering.md), seven demands
$q_1,\ldots,q_7$ in a block of capacity $c$ have a cap-spectrum covering
precisely when

$$
q_i\le c,\qquad
\sum_{i\in L}q_i\le2c\quad(L\text{ a Fano line}),
\qquad
\sum_iq_i\le4c.
\tag{16}
$$

Individual demand bounds are automatic. Two estimates used repeatedly below are

$$
3D\le2(1-\epsilon),\qquad
1+2D\le2(1-\epsilon),
\tag{17}
$$

valid for $\epsilon\le1/10$. Thus a line-coordinate check involving no own-type
row, or only one own-type row, follows respectively from the bounds $3D$ and
$1+2D$.

### Exactly three represented types

Order them so that $e_1\ge e_2\ge e_3$. Since $m\ge3$, equation (14) gives

$$
e_1+e_2\ge\frac23(e_1+e_2+e_3)
>\frac12+2\epsilon.
$$

It follows that

$$
\delta_1<1-2e_1<2e_2-4\epsilon,
\qquad e_2>2\epsilon.
\tag{18}
$$


Put type 1 on rows $2,3,4$, type 2 on rows $5,6,7$, and type 3 on row $1$.
Neither three-row type class is a Fano line. A line containing two type-1 rows
has demand in coordinate 1 at most

$$
2h_1+\max\{\delta_2,\delta_3\}\le2h_1+2e_1=2c_1,
$$

because $\delta_2,\delta_3\le e_1+\epsilon\le2e_1$. A line containing two type-2
rows has demand in coordinate 2 at most

$$
2h_2+\max\{\delta_1,\delta_3\}\le2h_2+2e_2=2c_2,
$$

using (18) and $\delta_3\le e_3+\epsilon\le e_2+\epsilon\le2e_2$. All other line
inequalities follow from (17).

Write $Q_i$ for the total demand in coordinate $i$. For the two repeated types,

$$
\begin{aligned}
4c_1-Q_1
&\ge h_1+4e_1-3\delta_2-\delta_3
\ge h_1-4\epsilon>0,\\
4c_2-Q_2
&\ge 1-\delta_2+4e_2-3\delta_1-\delta_3
>2e_2-4\epsilon>0.
\end{aligned}
\tag{19}
$$

The first strict inequality follows from $h_1>2(1-\epsilon)/3>4\epsilon$. For
the second line, use $3\delta_1<1+2\epsilon$ and
$\delta_2+\delta_3\le2e_2+2\epsilon$.

Coordinate 3 has total demand less than

$$
1+6D=3+4\epsilon\le4(1-\epsilon)\le4c_3.
$$

Every other coordinate has total demand less than

$$
7D\le4(1-\epsilon)\le4c_j.
$$

Both displayed comparisons hold for $\epsilon\le1/10$. This proves (16) in the
three-type case.

### At least four represented types

Order all represented types so that $e_1\ge e_2\ge\cdots$. Then
$e_2\ge\epsilon$. Otherwise (13) and (14) would give the contradiction

$$
T(S;c)\le\sum_i e_i
<\frac12+(m-1)\epsilon<\frac34+m\epsilon.
$$


Use type 1 on rows $1,2,4$, type 2 on rows $3,5$, type 3 on row $6$, and type 4
on row $7$. A line containing two type-1 rows has its third row of type 2 or 3,
and hence its coordinate-1 demand is at most $2h_1+2e_1=2c_1$. Indeed,
$\delta_2,\delta_3\le e_1+\epsilon\le2e_1$. The line through the two type-2 rows
is $356$; its coordinate-2 demand is at most $2h_2+\delta_3\le2h_2+2e_2=2c_2$.
Other line inequalities follow from (17).

The first two total demands satisfy

$$
\begin{aligned}
Q_1
&\le3h_1+2\delta_2+\delta_3+\delta_4
\le3c_1+e_1+4\epsilon\le4c_1,\\
Q_2
&\le2h_2+3\delta_1+\delta_3+\delta_4
\le2c_2+1+4\epsilon\le4c_2.
\end{aligned}
\tag{20}
$$

For the final comparison in the first line, use $e_1<c_1/3$ and
$4\epsilon\le2c_1/3$. For the second line, use $3\delta_1<3D=1+2\epsilon$ and
$1+4\epsilon\le2c_2$. These inequalities hold since $c_i\ge1-\epsilon$ and
$\epsilon\le1/10$.

Each of coordinates 3 and 4 has total demand at most $1+6D\le4(1-\epsilon)$.
Every other coordinate, including any unselected represented type, has total
demand at most $7D\le4(1-\epsilon)$. Thus (16) holds in every block.

In both cases the Fano-cap formula supplies the covering realizations. Trimming
excess incidences gives exact demands without a two-point cover. This proves the
continuous theorem. $\square$

## Sparsifying a covering certificate

**Lemma.** Any finite weighted covering certificate on seven rows can be
replaced by one using at most seven nonempty spectra, preserving every row's
covered demand and not increasing total mass. Only spectra from the original
certificate are needed.

**Proof.** Delete empty spectra and zero weights. If more than seven
positive-weight spectra remain, their incidence columns in $\mathbb R^7$ have a
nonzero linear dependence $\alpha$. Because the columns are nonzero and
nonnegative, $\alpha$ has both positive and negative entries. Change its sign if
necessary so that $\sum_i\alpha_i\le0$. Add a positive multiple of $\alpha$ to
the weight vector, increasing the multiple until the first weight reaches zero.
No weight becomes negative, row coverage is unchanged, and total mass does not
increase. Delete a zero weight and repeat. $\square$

This operation is performed before trimming excess incidences. Trimming may
split a class into several smaller spectra, but the seven-class bound is needed
only for rounding the untrimmed certificate.

## Finite families on blocks of size at least the uniformity

**Theorem.** Let $\mathcal H$ be a nonempty full $m$-block $k$-uniform family,
with every block of size at least $k$. Suppose $k\ge70$ and every subfamily of
at most seven edges has a two-point transversal. Then

$$
\boxed{\tau(\mathcal H)\le\frac34k+15m.}
\tag{21}
$$


**Proof.** Suppose the inequality fails. Reserve seven points in each block, and
let $\mathcal H'$ consist of the edges avoiding all reserved points. A
transversal of $\mathcal H'$, together with the reserved points, is a
transversal of $\mathcal H$. Thus

$$
\tau(\mathcal H')\ge\tau(\mathcal H)-7m>0.
$$

In particular, $\mathcal H'$ is nonempty.

If the original block sizes are $n_j$, normalize the profiles of $\mathcal H'$
by $k$ and set

$$
c_j=\frac{n_j-7}{k},\qquad\epsilon=\frac7k.
$$

Then $c_j\ge1-\epsilon$ and $\epsilon\le1/10$. Any real deletion removing all
normalized profiles can be rounded upward coordinatewise to an integer deletion
in the unreserved blocks, increasing its size by less than $m$. The full-profile
transversal criterion from
[Block-profile convergence](block_profile_convergence.md) therefore gives

$$
kT(S;c)\ge\tau(\mathcal H')-m
\ge\tau(\mathcal H)-8m
>\frac34k+7m.
\tag{22}
$$

Consequently $T(S;c)>3/4+m\epsilon$, and the continuous theorem applies.

In each block, sparsify the resulting untrimmed covering certificate to at most
seven spectra. Multiply its weights by $k$ and round each positive weight upward
to an integer. Before rounding the total mass is at most $n_j-7$; the seven
reserved points absorb the rounding increase. Every row has at least its
prescribed integer block degree. Delete excess incidences independently in each
row and block to recover the exact profile.

Full block invariance ensures that all seven resulting rows are edges of
$\mathcal H$. Their spectra are still subsets of allowed bad spectra, so no two
points meet all rows. Removing repeated edges leaves a bad subfamily of at most
seven distinct edges, a contradiction. $\square$

The same bound holds under the exactly-seven convention. A family violating (21)
has more than seven edges, so any smaller bad subfamily can be extended to seven
distinct edges.

## Scope

Taking $\epsilon=0$ in the continuous theorem handles arbitrary capacities
$c_j\ge1$, not just equal capacities. The finite theorem extends
[Equal blocks](equal_blocks.md) to unequal blocks of size at least the
uniformity. It gives the conjectured asymptotic upper bound when the number of
such blocks is $o(k)$.

For arbitrary capacities, the two-heavy-coordinate theorem excludes every
profile family whose heavy supports have a transversal of size at most two, as
well as every family with a light profile. No theorem here handles all remaining
heavy-support families. In particular, a heavy-support transversal number of at
least three, with small block capacities, remains an unresolved case of the
continuous-profile question.

All constructions require complete freedom to realize the selected profiles
inside each block. There is no proved reduction of an arbitrary family to this
setting preserving the local property with an asymptotically negligible loss.
