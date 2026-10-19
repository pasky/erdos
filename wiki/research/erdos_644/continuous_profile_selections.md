---
name: research/erdos_644/continuous_profile_selections
desc: A fixed-point profile reduction, two sufficient three-profile criteria, and limits of Fano-only and mean-max selection.
tags: [proved, conditional, method-obstruction]
sources: []
created: 2026-09-22T22:54:42Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/continuous_profile_selections

***

The later [large-block profile results](large_block_profiles.md) settle the
continuous threshold when all capacities are at least one, and, for arbitrary
capacities, when two coordinates meet every heavy support. The unrestricted
arbitrary-capacity question remains open in these notes.

Let $S\subseteq\prod_{j=1}^m[0,c_j]$ be a finite nonempty profile family, with
$\sum_j A_j=1$ for every $A\in S$. Let $T(S;c)$ be the infimum deletion mass
$\sum_jd_j$ such that $0\le d_j\le c_j$ and no $A\in S$ satisfies $A\le c-d$
coordinatewise.

The unresolved continuous-profile question is whether $T(S;c)>3/4$ always allows
a weighted realization of at most seven profiles with no two-point transversal.
The results here do not answer it, much less the unrestricted original problem.
Weighted realizations may split each block among finitely many incidence
spectra.

## Fano spectra alone do not suffice

Take $S=\{(1,0),(0,1)\}$ and $c_1=c_2=7/5$. Both profiles must be blocked, so

$$
T(S;c)=2(7/5-1)=4/5.
$$

Yet seven such profiles cannot satisfy the Fano-cap line inequalities in every
block. A row assignment is a two-coloring of the Fano points. A monochromatic
line has demand three in one block, greater than $2c_j=14/5$. Every two-coloring
of the Fano plane has a monochromatic line, so a Fano realization is impossible.

For completeness, the latter fact follows from the elementary description of
Fano caps: a line-free set has size at most four, and a line-free four-set has a
line as its complement. One way to check the four-set assertion is to identify
points with the nonzero vectors of $\mathbb F_2^3$. Three noncollinear points
form a basis, and the only fourth point that creates no line is their sum. The
complementary three points sum to zero and hence form a line.

This is not a counterexample to the all-pattern question. Four unit-measure
subsets of the first block can have empty common intersection, since four
complements of measure $2/5$ can cover the block of measure $7/5$. Add a
unit-measure set in the second block. This five-row realization has no
two-cover, using non-Fano spectra.

The same Fano-only failure occurs with all capacities below one. Take four
capacities $18/25$ and profiles

$$
(x,1-x,0,0),\quad(0,0,x,1-x),
\qquad x\in\{7/25,8/25,\ldots,18/25\}.
$$

For one block pair, let its remaining capacities be $u,v$. It contains an
allowed profile exactly when $[1-v,u]$ contains one of the grid values. The
supremum of $u+v$ with no allowed profile is $1+1/25=26/25$; if either endpoint
lies beyond the grid range the sum is at most one, and otherwise the interval
lies in one grid gap of length $1/25$. Thus the deletion threshold of the pair
is $36/25-26/25=2/5$, and the full threshold is $4/5$. Any Fano assignment
colors rows by their occupied block pair. A monochromatic line has total demand
three in that pair, exceeding its combined Fano line capacity $2(36/25)=72/25$.

## A fixed-point reduction

If $T(S;c)>3/4$, there exist a nonempty subfamily $S_0\subseteq S$ and a
probability distribution on it, of mean $p$, such that

$$
A+\frac34p\le c\qquad(A\in S_0).
\tag{1}
$$


To prove this, on the compact convex set $P=\operatorname{conv}S$ consider

$$
F(p)=\operatorname{conv}\{A\in S:A\le c-3p/4\}.
$$

The deletion vector $3p/4$ is feasible and has total mass $3/4$, so $F(p)$ is
nonempty. Its values are compact and convex, and its graph is closed: along any
convergent sequence one can pass to a subsequence using the same subset of the
finite set $S$ and convergent convex coefficients. Kakutani's fixed-point
theorem gives $p\in F(p)$. Take the support of a convex representation
witnessing this membership.

Writing $M_j=\max_{A\in S_0}A_j$, equation (1) gives

$$
M+3p/4\le c.
\tag{2}
$$

For $m\le5$, this supplies seven profiles satisfying all Fano **total**
inequalities, but not necessarily the line inequalities. Indeed the deficit
vectors $b=M-A$ have common coordinate sum $\sum_jM_j-1$. Thus $\mu=M-p$ is a
convex combination of at most $m$ such vectors, by Caratheodory's theorem in
that affine hyperplane. Round each coefficient multiplied by three upward to an
integer. At most $m+2\le7$ copies are needed, and their deficit sum is
coordinatewise at least $3\mu$. Add arbitrary profiles to reach seven copies.
Their total demands are at most

$$
7M-3\mu=4M+3p\le4c.
$$

No argument has supplied the missing line inequalities or an alternative
bad-spectrum realization in general.

## The mean-max condition alone is insufficient

Condition (2), detached from the full deletion hypothesis, need not permit any
bad seven-tuple. Here is a five-block example.

Use five profile labels $i\in[5]$, each with probability $1/5$. All profiles
have demand $2/5$ in a common coordinate. There are four additional coordinates
indexed by

$$
E_1=123,\quad E_2=145,\quad E_3=245,\quad E_4=345.
$$

Their demands are $2/5$ on labels belonging to $E_1$ and $1/5$ on labels
belonging to each of $E_2,E_3,E_4$, and zero otherwise. Every profile has total
demand one. With $M,p$ as above, take capacities exactly $M+3p/4$:

$$
c=(7/10,29/50,29/100,29/100,29/100).
$$


Suppose seven rows had a bad weighted realization. Their restrictions to the
common block have demand $2/5$ each and capacity $7/10$. The equality
classification in [Indispensable local cores](indispensable_local_cores.md)
applies with counting replaced by weight, so all seven Fano-cap spectra occur
there with positive weight. Therefore a point in any other block cannot cover a
Fano line: paired with the common-block point on the complementary cap, it would
cover all rows.

Some profile label repeats among seven rows. The Fano line through two rows with
this label has at most two distinct profile labels. Every pair of labels is
contained in one of the four sets $E_j$ (and every single label belongs to one).
In that block, all three rows have the same positive demand $w$, whereas every
point covers at most two of them. This forces

$$
3w\le2c_j=2(29/20)w<3w,
$$

a contradiction. Thus this profile family has the local property in the weighted
model.

Its deletion threshold is at most $27/100$: blocking the coordinates for $E_1$
and $E_2$ costs arbitrarily little more than $(29/50-2/5)+(29/100-1/5)=27/100$.
It therefore does not contradict the original deletion-threshold question. It
shows exactly why the fixed-point reduction cannot discard the rest of that
hypothesis.

## A balanced good triple gives a seven-row certificate

**Lemma.** Suppose $T(S;c)>3/4$ and there are profiles $A,B,C\in S$ satisfying,
coordinatewise,

$$
A\le B+C,\qquad B\le A+C,\qquad C\le A+B,
\qquad A+B+C\le2c.
\tag{3}
$$

Then at most seven profiles from $S$ have a bad weighted realization.

**Proof.** In block $j$, realize three reference rows with profiles $A,B,C$
using only the pair spectra $AB,AC,BC$, with respective masses

$$
\frac{A_j+B_j-C_j}{2},\qquad
\frac{A_j+C_j-B_j}{2},\qquad
\frac{B_j+C_j-A_j}{2}.
$$

These masses are nonnegative, and their sum is $(A_j+B_j+C_j)/2\le c_j$. The
reference rows have empty triple intersection and no singleton spectra. Because
each profile has total mass one, each of the three global pair atoms has mass
$1/2$.

Assign these three pair atoms to the three perfect matchings of $K_4$. Split
each atom into two equal parts, assigning its two parts to the two edges of its
matching. For each vertex $v$ of $K_4$, let $D_v$ consist of the points assigned
to edges containing $v$. Each $D_v$ has mass $3/4$: it contains one part of mass
$1/4$ from each matching.

Every pair of points covering the three reference rows uses two different pair
atoms. The corresponding edges of $K_4$ belong to different perfect matchings
and therefore intersect. Consequently the two points both belong to some $D_v$.

For each $v$, delete $D_v$. Its blockwise deletion vector is feasible and has
total mass $3/4$, so the hypothesis supplies a profile from $S$ that can be
realized by a row $E_v$ avoiding $D_v$. Realize all four such rows on the same
weighted blocks, refining point classes as necessary. Every pair covering the
reference rows misses at least one $E_v$. Thus the three reference rows and four
new rows have no two-point transversal. $\square$

Condition (3) is sufficient but is not forced by the deletion threshold. In the
already considered example $S=\{(1,0),(0,1)\}$ with capacities $(7/5,7/5)$, one
has $T=4/5$. A triple using both profiles violates a coordinatewise triangle
inequality, while a triple repeating one profile three times violates
$A+B+C\le2c$.

## Three equally weighted profiles suffice for the mean-max condition

**Lemma.** Let $A,B,C\in S$, with repetitions allowed, and put

$$
M_j=\max\{A_j,B_j,C_j\}.
$$

If

$$
M+\frac{A+B+C}{4}\le c,
\tag{4}
$$

then seven profiles from $S$ have a bad weighted realization. No
deletion-threshold assumption is needed for this lemma.

**Proof.** Use the Fano lines

$$
123,\quad145,\quad167,\quad246,\quad257,\quad347,\quad356.
$$

Give rows $1,2,4$ profile $A$, rows $3,5$ profile $B$, and rows $6,7$ profile
$C$. None of the three color classes contains a Fano line. In one block write
$a,b,d$ for the three profile demands, $m=\max\{a,b,d\}$, and $s=a+b+d$.

Each row demand is at most $m\le c_j$. A line has either one row of each profile
or two rows of one profile and one of another. In the first case its demand is

$$
s\le2m+s/2\le2c_j,
$$

since $s\le3m$. In the second case, writing $x,y,z$ for the demands of the
repeated, singly occurring, and absent profile, respectively, its demand
satisfies

$$
2x+y=\frac{s}{2}+\frac{3x+y-z}{2}
\le\frac{s}{2}+2m\le2c_j.
$$

Finally, the total demand of the seven rows is

$$
3a+2b+2d=2s+a\le4m+s\le4c_j,
$$

because $s+a=2a+b+d\le4m$.

The [Fano-cap covering formula](fano_cap_covering.md) now gives a cap-spectrum
covering in every block. Delete excess incidences to obtain the exact demands.
Two Fano caps cannot cover all seven rows, and trimming preserves this property.
$\square$

In particular, the fixed-point reduction succeeds if its mean can be written as
$p=(A+B+C)/3$ for three profiles in its supporting subfamily: equation (2) then
implies (4). The fixed-point argument gives arbitrary convex weights, however,
and does not establish such an equal-weight representation. Neither lemma above
resolves that remaining selection problem or the arbitrary-capacity theorem.
