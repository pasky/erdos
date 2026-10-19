---
name: research/erdos_644/incidence_minimal_families
desc: Simultaneous criticality, exact critical-cover trace numbers, a critical projection obstruction, and mandatory-point witness restrictions; no global rank estimate.
tags: [proved, reductions, criticality, limitations]
sources: []
created: 2026-09-23T02:15:00Z
updated: 2026-10-13T05:28:09Z
---


# research/erdos_644/incidence_minimal_families

***

Unlike deleting edges to preserve a large transversal number, deleting an
incidence shrinks an edge and can only increase the transversal number. This
suggests minimizing incidences subject to $P_7$. The resulting witness
conditions are proved below; they do not yield a general three-quarter upper
bound.

## Simultaneous minimality

Suppose a finite rank-at-most-$k$ $P_7$ family has transversal number at least
$t$. Among such finite families choose one with the fewest edges, and then with
the fewest incidences. Its transversal number is exactly $t$: deleting any edge
leaves a family with transversal number at most $t-1$, and adjoining one point
of that edge covers the whole family.

It is therefore transversal-critical. Moreover, deleting any incidence from an
edge of size at least two must destroy $P_7$. Otherwise rank is unchanged or
lowered and the transversal number cannot decrease, contradicting the minimal
choice. If a shrinking makes two edges equal, removing the duplicate also
contradicts minimality.

This yields simultaneous edge criticality and incidence minimality. The latter
alone is insufficient for a small ground set, as explained below.

## A critical-cover trace constraint

There is an exact compatibility condition between edge criticality and its
minimum covers. Let $\mathcal H$ be a finite transversal-critical family of
nonempty edges with $\tau(\mathcal H)=t\ge2$. For any edge $E$, choose a
$(t-1)$-point transversal $T_E$ of $\mathcal H\setminus\{E\}$. Necessarily
$T_E\cap E=\varnothing$, since otherwise it would cover $\mathcal H$.

For every $u\in T_E$ and every $v\in E$, there is an edge $F$ such that

$$
F\cap T_E=\{u\},\qquad v\notin F.
\tag{C}
$$

To prove this, $T_E\cup\{v\}$ is a minimum transversal of $\mathcal H$.
Removing $u$ leaves a set of size $t-1$ and hence misses some edge $F$.
This $F$ misses $v$ and $T_E\setminus\{u\}$. It is not $E$, because
$v\in E$, so it meets $T_E$ and must do so exactly at $u$.

Equivalently, each nonempty singleton-trace class satisfies

$$
E\cap\bigcap_{\substack{F\in\mathcal H\\F\cap T_E=\{u\}}}F
=\varnothing.
$$

This uses only edge criticality, not $P_7$ or incidence minimality. The edge
$F$ may depend on both $u$ and $v$. Selecting one such edge for each $v\in E$
gives a witness using at most $|E|$ rows for each $u$; no bound independent of
$|E|$, or useful aggregate rank estimate for these classes, was proved.
Combining (C) with all essential-incidence
witnesses to deduce $k\ge4t/3-o(k)$ remains unproved. In particular, (C) does
not supply an extra local-test slot for a seven-row mandatory-point witness.

### Exact transversal numbers on the critical-cover trace cube

The same critical cover gives an exact normalization for all its
subsets. Fix $E$ and $T=T_E$, with $|T|=t-1$ and $T\cap E=\varnothing$.
For $S\subseteq T$, define

$$
\mathcal H[S]=\{F\in\mathcal H:F\cap T\subseteq S\}.
$$

Then

$$
\boxed{\tau(\mathcal H[S])=|S|+1.}
\tag{C1}
$$

For the upper bound, $S$ covers all members except $E$, so add any
point of $E$. For the lower bound, a cover of size at most $|S|$,
together with $T\setminus S$, would cover $\mathcal H$ with at most
$t-1$ points.

For each $x\in E$, there is also the exact residual formula

$$
\boxed{\tau(\{F\in\mathcal H[S]:x\notin F\})=|S|.}
\tag{C2}
$$

The upper bound uses $S$, because $E$ is the only edge missed by
$T$ and has been removed. Adding $x$ to a cover of the residual
covers $\mathcal H[S]$, so (C1) gives the opposite bound. For
$S=\varnothing$, the residual is empty and has transversal number
zero. All these families inherit $P_7$ when $\mathcal H$ has it.

These identities constrain every trace class simultaneously, but
do not proportionately lower the rank as $|S|$ decreases. In
particular, (C1) retains the original edge $E$ even at
$S=\varnothing$. No rank-sensitive extraction or three-quarter
bound follows from these formulas alone.

### The critical-cover projection can destroy locality

Tracing a critical family onto $U=E\cup T_E$ preserves its
transversal number exactly. Shrinking edges cannot decrease it,
while $T_E$ together with one point of $E$ covers all traces and has
size $t$. All traces are nonempty. However, even simultaneous edge
criticality and incidence minimality do not make this projection
preserve $P_7$, or even $P_3$.

For a finite example, take $C_9$ with vertices $0,\ldots,8$ in
cyclic order. Its nine independent four-subsets are the points of a
new hypergraph, and its rows are

$$
E_i=\{I:i\in I,\ |I|=4,\ I\text{ independent in }C_9\}.
$$

There are nine such independent sets because their cyclic gaps are
$2,2,2,3$; by cyclic symmetry each row has size four. The family
has transversal number three: two independent sets cannot cover an
odd cycle, while, for example, $\{0,2,4,6\}$,
$\{1,3,5,7\}$, and $\{8,1,3,5\}$ cover it. Deleting any row
leaves a path on eight vertices, whose two four-point color
classes are allowable ground points. Thus the family is
transversal-critical and has $P_8$.

Every incidence $i\in I$ is essential for $P_7$. The independent
four-set $I$ is the larger color class of a seven-vertex induced
path, determined by its three gaps of length two. Any cover of
this path by two independent sets gives its unique bipartition.
The four-point class can be covered only by the ground point $I$
itself. Deleting the incidence of row $i$ with point $I$ prevents
that point from covering the class, and no other independent
four-set contains it. Those seven rows consequently lose every
two-cover.

Take $E=E_0$ and

$$
T_E=\{\{1,3,5,7\},\{2,4,6,8\}\}.
$$

On $U=E_0\cup T_E$, the traces of $E_0,E_1,E_8$ are pairwise
disjoint. The last two are respectively the two singleton points
of $T_E$: no independent set contains $0$ together with $1$ or
$8$. Thus the trace family fails $P_3$ despite both criticality
conditions and $\tau/k=3/4$ in the original family. This fixed-rank
example is not an asymptotic counterexample and does not exclude
a projection theorem requiring a fixed excess above three quarters.

## Mandatory-point witnesses

Let $v\in E$, where $|E|\ge2$, be an essential incidence. There is a subfamily
$\mathcal C$ of $m\le7$ original rows containing $E$ such that replacing $E$ by
$E\setminus\{v\}$ makes its transversal number greater than two. Every two-cover
of $\mathcal C$ is consequently of the form $\{v,w\}$ with $w\notin E$.

The point $v$ cannot lie in every witness row. Otherwise, after the deletion,
$\{v,x\}$ for any $x\in E\setminus\{v\}$ would still cover them. Choose a
partner $w$ in a two-cover of the original rows. The rows missing $w$ all
contain $v$, include $E$, and have common intersection exactly $\{v\}$. Any
other common point $x$ would give the cover $\{x,w\}$ avoiding $v$. At least one
row contains $w$ and misses $v$, so there are at most six rows in this
singleton-intersection certificate.

## Short witnesses force smaller global covers

Suppose $m\le6$, and set

$$
W=\bigcap_{\substack{F\in\mathcal C\\v\notin F}}F.
$$

This is the intersection of a nonempty family. It is nonempty because it
contains every possible partner $w$, and $W\cap E=\varnothing$: a point in that
intersection would still supplement $v$ after the incidence deletion.

Every at-most-$(7-m)$ edges avoiding $v$ have a common point in $W$. Indeed,
adjoining them to $\mathcal C$ and applying $P_7$ forces a cover $\{v,w\}$ with
$w$ in all these edges and in $W$.

Partition $W$ into $7-m$ parts of size at most $\lceil |W|/(7-m)\rceil$. If none
of these parts covers the family of edges avoiding $v$, choose an avoiding edge
for each part. Their intersection with $W$ is empty, a contradiction. Adding $v$
to a cover of the residual family gives

$$
\tau(\mathcal H)\le1+\left\lceil\frac{|W|}{7-m}\right\rceil
\le1+\left\lceil\frac{k}{7-m}\right\rceil.
\tag{1}
$$

Thus $\tau>1+\lceil k/2\rceil$ excludes all witnesses with at most five rows. A
six-row witness has $|W|\ge\tau(\mathcal H)-1$.

## A restriction on six-row witnesses

For $k\ge4$, if $\tau(\mathcal H)>\lceil3k/4\rceil$, a six-row witness cannot
have its mandatory point $v$ in exactly two rows.

To prove this, denote those two rows by $E,A$. If some $w\in W$ lay in $A$, the
only row missing $w$ would be $E$, contradicting the preceding
singleton-intersection certificate because $|E|\ge2$. Hence
$W\cap(E\cup A)=\varnothing$, and the same certificate gives $E\cap A=\{v\}$.

Choose a witness row $B$ missing $v$. The triple $E,A,B$ has empty common
intersection, and its pair-intersection sizes are

$$
1,\qquad |E\cap B|\le k-|W|,\qquad |A\cap B|\le k-|W|.
$$

Writing $t=\tau(\mathcal H)$ and using $t\ge\lceil3k/4\rceil+1$, all three sizes
are at most $\lfloor k/4\rfloor$. The new rank-aware good-triple certificate
(G0a) in [Certificates and obstructions](certificates_and_obstructions.md) then
gives $\tau\le\lceil3k/4\rceil$, a contradiction.

### A one-sided trace classification for three containing rows

Let $\mathcal H$ be a rank-at-most-$k$ $P_7$ family with transversal number $t$,
and suppose

$$
\mathcal C=\{E,A,B,F_1,F_2,F_3\}
$$

is a six-row witness for the essential incidence $v\in E$, with $|E|\ge2$.
Assume that $v$ belongs to exactly $E,A,B$, that

$$
E\cap A=E\cap B=\{v\},
\tag{2}
$$

and that $t\ge\lceil3k/4\rceil+2$. Put

$$
E_0=E\setminus\{v\},\qquad
P=(A\cap B)\setminus\{v\},\qquad
W=F_1\cap F_2\cap F_3.
$$

Then one of the following two configurations holds:

- Every $F_i$ avoids $P$, and the three traces $F_i\cap E_0$ are pairwise
  intersecting with empty total intersection.
- Every $F_i$ avoids $E$, and the three traces $F_i\cap P$ are pairwise
  intersecting with empty total intersection.

To prove this, write $w=|W|\ge t-1$ and $q=k-w$. The earlier witness argument
gives $W\cap E_0=\varnothing$. Also $W\cap P=\varnothing$: a point in this
intersection, together with any point of the nonempty $E_0$, would cover
$\mathcal C$ without $v$. By (2), every non-$v$ two-cover of $E,A,B$ is a pair
from $E_0\times P$.

Suppose some pair $i,j$ satisfies

$$
E_0\cap F_i\cap F_j=P\cap F_i\cap F_j=\varnothing.
\tag{3}
$$

Every non-$v$ cover of $E,A,B,F_i,F_j$ then has both endpoints in

$$
U=(E_0\cup P)\cap(F_i\cup F_j).
$$

Indeed, neither endpoint can meet both $F_i,F_j$, so one endpoint must meet
each. Since $W$ avoids $E_0\cup P$, we have $|U|\le2q$. Moreover, (3) gives
$U\cap W_{ij}=\varnothing$, where $W_{ij}=F_i\cap F_j$.

Choose an edge $D$ avoiding $v$, $U$, and enough of $W_{ij}$ to leave
$|D\cap W_{ij}|\le t-2$. The required avoiding set has size

$$
1+|U|+\max\{0,|W_{ij}|-(t-2)\}\le t-1,
$$

because the assumed lower bound on $t$ gives

$$
|U|\le2(k-t+1)\le t-2,
\qquad
|U|+|W_{ij}|\le2q+k\le3k-2t+2\le2t-4.
$$

Thus such $D$ exists by the definition of $t$.

Every two-cover of the at-most-six rows $E,A,B,F_i,F_j,D$ must contain $v$, and
its partner belongs to $W_{ij}\cap D$. Appending any edge avoiding $v$ and using
$P_7$ shows that $W_{ij}\cap D$ covers all edges avoiding $v$. Consequently

$$
\tau(\mathcal H)\le1+|W_{ij}\cap D|\le t-1,
$$

a contradiction. Therefore every pair $F_i,F_j$ has a common point in $E_0$ or
in $P$.

A point in $E_0\cap F_i\cap F_j$ forbids every point in $P\cap F_\ell$ for the
remaining index $\ell$: these two points would otherwise cover all six rows
without $v$. The same assertion holds with $E_0,P$ interchanged. In particular,
common points on opposite sides cannot occur for two different pairs of indices,
since the two pairs together cover all three indices. If one pair has a common
point in $E_0$, the other two pairs must therefore also have common points in
$E_0$, and the three forbidden-complement assertions imply
$P\cap F_i=\varnothing$ for every $i$. Otherwise all three pairs have common
points in $P$ and all $E_0\cap F_i$ vanish. The total intersections of these
traces are empty because $W$ avoids both $E_0$ and $P$. This proves the
classification.

Hypothesis (2) holds automatically if $W$ meets both $A$ and $B$. For example, a
point of $W\cap A$, together with any point of $(E\cap B)\setminus\{v\}$, would
be a forbidden non-$v$ cover; hence $E\cap B=\{v\}$. The other equality is
symmetric. The two configurations above have not themselves been excluded.

There is also a necessary restriction without (2). In any mandatory witness with
exactly three $v$-containing rows, their total intersection is $\{v\}$: another
common point could replace $v$ in a cover with a partner from $W$. The
arbitrary-common-intersection certificate
[(G0c)](certificates_and_obstructions.md#allowing-a-common-intersection)
therefore implies that, when $t>1+\lceil3k/4\rceil$, some exclusive pair
intersection of these three rows has size at least $\lceil(t-1)/3\rceil$.

### The remaining seven-row gap

No theorem was obtained saying that a seven-row essential-incidence witness
forces $\tau\le3k/4+O(1)$. Even the case where $v$ belongs to exactly two
witness rows remains untreated. Denote those rows by $E,A$ and the other five by
$F_1,\ldots,F_5$. The mandatory-point argument gives

$$
E\cap A=\{v\},\qquad
W=\bigcap_{i=1}^5F_i\ne\varnothing,\qquad
W\cap(E\cup A)=\varnothing.
$$

For $x\in E\setminus\{v\}$ and $y\in A\setminus\{v\}$, define their
missing-index sets

$$
M_x=\{i:x\notin F_i\},\qquad
N_y=\{i:y\notin F_i\}.
$$

The absence of non-$v$ two-covers is precisely $M_x\cap N_y\ne\varnothing$ for
all such pairs. On deleting $F_i$, the new non-$v$ candidate pairs are exactly
those with $M_x\cap N_y=\{i\}$. The possible partners of $v$ become
$W_i=\bigcap_{j\ne i}F_j$.

This is an exact local formulation, not a small-endpoint-set bound or a
counterexample construction. In contrast to a six-row witness, it leaves no room
to append an arbitrary ambient edge and deduce $|W|\ge t-1$. No argument
combining this seven-row formulation with the full ambient $P_7$ condition and
large $t$ was completed. The rank-feasible local patterns considered during this
approach have small transversal number and do not constitute counterexamples to
the three-quarter conjecture.

## Incidence minimality alone does not bound the ground set

The family in [Indispensable local cores](indispensable_local_cores.md) has rank
$16m+1$, transversal number $12m$, and $\binom{2m}{m}$ added points $v_S$. Each
has three incidences protected by a seven-row witness.

In that witness every core point has degree four, $v_S$ has degree three, no
pair of core points covers all rows, and every other exterior point has degree
at most one. After deleting any one of the three $v_S$ incidences, a pair using
$v_S$ covers at most six rows. All other pairs already failed. Therefore each
incidence is essential to $P_7$.

Further incidence shrinkings cannot restore a lost two-cover. Hence any
incidence-minimal $P_7$ descendant retaining these original rows still contains
all these exponentially many vertices. This excludes a polynomial ground-set
theorem based on incidence minimality alone, even at a ratio tending to three
quarters.

It does not exclude a stronger theorem under simultaneous edge criticality and
incidence minimality, nor one assuming a fixed excess above three quarters. The
exceptional rows of the cited construction have a two-point transversal, so
preliminary edge minimization or low-transversal deletion may change the example
substantially.
