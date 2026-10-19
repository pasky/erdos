---
name: research/erdos_644/two_tail_obstruction
desc: A proved weighted Fano obstruction for full two-tail block-profile families; this does not settle general set families.
tags: [proved, construction-obstruction]
sources: []
created: 2026-09-22T20:38:17Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_644/two_tail_obstruction

***

This page rules out one class of proposed lower-bound constructions. Neither
assertion of Problem 644 is resolved by it.

The result is subsumed by
[Block-profile families](block_profile_families.md), which proves
$\tau\le3k/4+16$ for every full two-block profile family, without restrictions
on the ground-set size or number of allowed intervals. The proof below is
retained as an earlier, independently checked construction.

**Established continuous lemma.** Let $0 \le a \le b \le 1$, put $h=b-a$, and
suppose $h \le 1/4$. Let two block capacities satisfy

$x+y = 7/4+h$, $x \ge  b$, and $y \ge  1-a$.

There exist seven sets of measure one, with no two-point transversal at the
level of their incidence spectra, fitting in these two blocks, such that every
set has first-block measure at most $a$ or at least $b$. All spectra used have
size at most four. All degree-four spectra used are Fano caps, and every
degree-three spectrum used is a nonline of that Fano plane.

Here a Fano cap is the complement of a line. Any two caps have union of size at
most six. A triple and a cap have union seven exactly when the triple is the
complementary line. Consequently the asserted support restrictions suffice for
the absence of a two-point transversal; degree-at-most-two spectra cause no
additional restriction.

## Fano weight calculation

Let $M$ be the incidence matrix of the seven Fano caps. Then

$M^{-1} = (1/2) M^T - (1/4) J$.

For a desired vector of first-block row measures $q_i$, its cap weights are

$z_L = (\sum_i q_i - 2 \sum_{i\in L} q_i)/4$.

The second-block weights giving row measures $1-q_i$ are $1/4-z_L$. Thus a pure
Fano construction exists if all $z_L$ belong to $[0,1/4]$ and its first-block
mass $\sum_i q_i/4$ belongs to $[7/4-y,x]$.

Write

$x=b+s$, $y=7/4-a-s$, where $0\le s\le 3/4$.

All-low or all-high pure Fano constructions apply unless

$3a/4 \le  s \le  3b/4$.                                  (H)

Indeed, for $s\le 3a/4$ take all row measures $4(a+s)/7 \le  a$; for $s\ge 3b/4$
take all row measures $4(b+s)/7 \ge  b$.

In particular, these two cases already prove the lemma when $h=0$.

## Four standard pure-Fano cases

Give three or four rows measure $b$, and the other rows measure $a$. The
following choices make all cap weights lie in $[0,1/4]$:

1. The three high rows form a line, provided $a\ge 3h$.
2. The three high rows form a nonline, provided $a\ge h$ and $a+3h\le 1$.
3. The four high rows form a cap, provided $a+4h\le 1$.
4. The four high rows are the complement of a nonline, provided $a\ge 2h$ and
   $a+2h\le 1$.

For three high rows the first-block mass is $(7a+3h)/4$; for four it is
$(7a+4h)/4$. Either mass lies in $[a+s,b+s]$ throughout (H).

These cases cover every $a$ if $h\le 1/5$. If $1/5<h\le 1/4$, the only remaining
intervals are

$G_1: 1-4h<a<h$,
$G_2: 1-3h<a<2h$,
$G_3: 1-2h<a<3h$.

Swapping the blocks replaces $(a,b,s)$ by $(1-b,1-a,3/4-s)$ and exchanges $G_1$
and $G_3$.

## The central interval G2

Here $h<a<1/2$, $b>1/2$, and $a+2h\le 1$.

If $s\le a$, take six low rows of measure $a$ and one high row of measure

$B=\max(b,4s-2a)$.

Then $b\le B\le 2a\le 1$, so the cap weights are nonnegative. Their first-block
mass $(6a+B)/4$ lies in $[a+s,b+s]$.

If $s\ge b-1/4$, take six high rows of measure $b$ and one low row of measure
$2b-1$. The low measure lies in $[0,a]$. The cap weights are nonnegative and
their first-block mass is $2b-1/4$. This lies in $[a+s,b+s]$: the upper
inequality is the stated lower bound on $s$; the lower follows from (H) and
$a+5h\ge 1$.

These two ranges cover (H), since $b-1/4\le a$.

## The interval G1

Here $a<h$, hence $b<1/2$.

First, a pure Fano construction with six high rows of measure $b$ and one low
row of measure zero works whenever $s\ge b/2$. Its first-block mass is $3b/2$;
the other capacity inequality follows from (H) and $a\le 3h$.

Second, a one-high construction using smaller spectra works whenever

$s\le a+h/3$.

Put $z=x=b+s$, and choose

$\max(0,(3a+3s-h)/6) \le  A \le  \min(a,x/3)$.

The interval is nonempty: the first upper-bound condition is precisely
$s\le a+h/3$; the second is $a+s\le 3h$, which holds throughout (H) because
$a<h$. We have $z<1$ and $A<1/4$.

Choose one high index $p$. In the first block use spectra $\{p,i,j\}$ where
$\{i,j\}$ ranges over the twelve edges of the graph on the other six indices
obtained by deleting the three pairs which complete Fano lines with $p$. Give
each such spectrum weight $A/4$, and give $\{p\}$ weight $z-3A$. The high row
has measure $z\ge b$, all six low rows have measure $A\le a$, and the
first-block mass is $z=x$.

In the second block use Fano caps. The three caps excluding $p$ have weight
$(1-2A+z)/4$; the four caps containing $p$ have weight $(1-z)/4$. These weights
are nonnegative, and their total is $7/4-3A/2-z/4 \le  y$ by the lower bound on
$A$.

If $a\ge h/3$, these constructions cover (H), since $a+h/3\ge b/2$.

It remains to consider $a\le h/3$. The following two-high construction covers
all of (H). Choose high indices $p,q$, let $r$ complete their Fano line, and let
$J$ be the other four indices. Put

$B=x-a/2=a/2+h+s$.

In the first block use:

* each $\{p,r,j\}$ and $\{q,r,j\}$, $j\in J$, with weight $a/8$;
* each $\{p,q,j\}$, $j\in J$, with weight $3a/4$;
* $\{p,q\}$ with weight $B-7a/2$.

The last weight is nonnegative because $h+s\ge 3a$. Total mass is $B+a/2=x$. The
two high rows have measure $B\ge b$, and the five low rows have measure $a$.

In the second block take the Fano cap weights for row measures $1-B$ on the two
high rows and $1-a$ on the five low rows. These weights are nonnegative because

$2B-a=2(h+s)\le 1$:

indeed (H) and $a\le h/3$ imply $s\le 3b/4\le h\le 1/4$. Their total mass is

$7/4-(5a+2B)/4 = 7/4-a-x/2 \le  y$,

since (H) implies $s\le 3b/4\le b$, hence $x=b+s\ge 2s$.

Every first-block triple used is a Fano nonline. This finishes G1, hence G3 by
symmetry, and proves the lemma.

## Consequence and rounding scope

For the full two-tail profile family (all rank-k sets whose first-block count is
at most ak or at least bk), with both tails feasible, its asymptotic transversal
coefficient is

$x+y-1-(b-a)$.

This follows by leaving first-block capacity just below b and second-block
capacity just below 1-a; conversely any surviving capacity interval avoiding
both tails must lie strictly inside the forbidden gap. Discreteness changes the
answer by at most two.

More precisely, for $a<b$, integer thresholds $A=\lfloor ak\rfloor$,
$B=\lceil bk\rceil$, and both tails feasible, the exact value is

$$
\tau=|X|+|Y|-k-B+A+2.
$$


If $x+y<2$ and this coefficient exceeds $3/4$, then $h<1/4$ and the continuous
lemma applies after shrinking the capacities to total $7/4+h$, keeping $x\ge b$
and $y\ge 1-a$. Thus every such profile template admits a weighted bad-seven
configuration.

For fixed rational parameters, multiplying by a common denominator gives an
exact finite bad-seven certificate. The stronger asymptotic statement also
follows by bounded rounding:

* If $x>b$ and $y>1-a$, reserve a small positive amount of both block capacities
  and slightly widen the forbidden gap (decrease a unless a=0, increase b unless
  b=1). The strict transversal margin allows this while still leaving total
  capacity above $7/4+h$. Apply the lemma inside the reserved capacities.
* Round every spectrum weight down at scale k, and restore each row's size to k
  by private vertices (singleton spectra). There are only 128 possible spectra,
  so this costs O(1) points. For a low row with a=0, pad in the second block;
  for a high row with b=1, pad in the first block; otherwise the widened gap
  absorbs the O(1) error. Singleton spectra preserve the obstruction, and the
  reserved capacities absorb the padding.
* If $x=b$, the strict transversal margin gives $y>7/4-a$. A pure all-low Fano
  construction can then be chosen with both capacity inequalities strict and row
  measure strictly below a when a>0; if a=0 choose row measure zero. This
  directly permits the same rounding. The case $y=1-a$ is symmetric.

For parameters varying with $k$, the same conclusion with an $o(k)$ error
follows by taking a convergent subsequence if the proposed excess over $3k/4$ is
bounded below. The boundary constructions above supply the required strict room
at the limiting parameters. This excludes an asymptotic coefficient above $3/4$
for two-tail profile families on $n<2k$ vertices with positive limiting block
sizes and both tails feasible.

Degenerate limiting block sizes also cannot produce such an excess. If $x\to0$,
then $a,b\to0$ and an excess bounded below forces $y>7/4+\varepsilon$ along a
subsequence. The low tail contains every $k$-subset of the second block, which
already contains a bad Fano tuple. The case $y\to0$ follows by symmetry.
