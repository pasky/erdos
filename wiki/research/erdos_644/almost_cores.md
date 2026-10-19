---
name: research/erdos_644/almost_cores
desc: A Fano selection bound for a small core with sparse or low-degree exterior vertices, and the remaining structural gap.
tags: [proved, reductions, conditional-upper-bounds]
sources: []
created: 2026-09-23T00:40:31Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/almost_cores

***

A vertex restriction need not preserve $P_7$ to support a three-quarter upper
bound. The criterion below permits exterior vertices, provided each edge has few
uncontrolled exterior points and the other exterior points have sufficiently
small edge-degree. It does not establish that an arbitrary near-extremal family
has such a core.

All families below are finite, have nonempty edges, and satisfy the
**at-most-seven** condition $P_7$. Repeated edges may be used in selections:
their underlying subfamily still has at most seven members. Rank at most $k$ is
sufficient throughout.

## Two elementary ingredients

### Covers of small edge subfamilies

Put

$$
W=(35k)^{1/3}.
$$

Every nonempty $P_7$ rank-$k$ family of $M$ edges has a transversal of size at
most

$$
g_k(M)=\lceil W\log M\rceil+1,
\tag{1}
$$

where logarithms are natural. This is the greedy bound also recorded in
[Structural reductions](structural_reductions.md).

For completeness, sample seven edges independently and uniformly, allowing
repetitions. A two-point cover makes some point occur in at least four sample
positions. If $p_v$ is the proportion of edges containing $v$, a union bound
gives

$$
1\le35\sum_vp_v^4
\le35\bigl(\max_vp_v\bigr)^3\sum_vp_v
\le35k\bigl(\max_vp_v\bigr)^3.
$$

Thus some point meets at least a $1/W$ proportion of the edges. Apply this to
each remaining subfamily. After $\lceil W\log M\rceil$ selections at most one
edge remains, which can be covered by one further point.

### Balanced Fano templates

For every $n$-point set $U$ there are subsets $B_1,\ldots,B_7\subseteq U$ with
the following properties:

- each point belongs to exactly four of the $B_i$;
- no pair of points meets all seven $B_i$;
- every complement $U\setminus B_i$ has size at most $L(n)$, where

$$
  L(7q+r)=3q+\ell_r,\qquad
  (\ell_0,\ldots,\ell_6)=(0,1,2,2,2,3,3).
  \tag{2}
$$


In particular,

$$
L(n)\le\frac{3n+8}{7}.
\tag{3}
$$


To construct the templates, partition $U$ into seven classes indexed by the
nonzero vectors $v\in\mathbb F_2^3$, and, for nonzero $i\in\mathbb F_2^3$, put

$$
B_i=\bigcup_{i\cdot v=1}U_v.
$$

Each point has a four-row Fano-cap spectrum. For any two class indices $v,w$,
there is a nonzero $i$ orthogonal to both, so the corresponding two points miss
$B_i$.

Give each class $q$ points, then place the remaining $r$ points in different
classes. The complements of the templates correspond to Fano lines. The largest
number of extra classes on a line can be bounded by the values $\ell_r$ in (2):
for $r=3$ choose a noncollinear triple, and for $r=4$ choose a Fano cap; the
other values are immediate. The maximum of $7\ell_r-3r$ is eight, proving (3).

## The combined almost-core criterion

**Theorem.** Let $\mathcal H$ have rank at most $k$, property $P_7$, and
transversal number $t$. Let $U$ be a set of $n$ vertices. Partition the exterior
vertices as

$$
V(\mathcal H)\setminus U=Z\mathbin{\dot\cup}R,
$$

where every point of $Z$ belongs to at most $D$ edges, and

$$
|E\cap R|\le d\qquad(E\in\mathcal H).
\tag{4}
$$

Here $D\ge1$ and $d\ge0$ are integers. Define

$$
s=\left\lceil W\log\max\{1,6kD\}\right\rceil+1.
\tag{5}
$$

If $Z=\varnothing$, one may instead take $s=0$. Then

$$
\boxed{\quad t\le L(n)+3d+s
\le\frac{3n+8}{7}+3d+s.\quad}
\tag{6}
$$


The points of $R$ need not actually have degree greater than $D$; their degrees
are unrestricted.

**Proof.** Suppose $t>L(n)+3d+s$, and choose the Fano templates above. We
construct edges $E_1,\ldots,E_7$ successively.

Before choosing $E_i$, let $Q_i\subseteq R$ consist of the points that occur in
at least two preceding selected rows. Counting previous incidences with $R$
gives

$$
|Q_i|\le\left\lfloor\frac{(i-1)d}{2}\right\rfloor\le3d.
\tag{7}
$$

Let $Z_i=Z\cap\bigcup_{j<i}E_j$ and let $\mathcal F_i$ be the subfamily of all
edges meeting $Z_i$. There are at most $6k$ points in $Z_i$, so

$$
|\mathcal F_i|\le6kD.
$$

By (1), $\mathcal F_i$ has a transversal $S_i$ of size at most $s$; if it is
empty, take $S_i=\varnothing$.

The set

$$
(U\setminus B_i)\cup Q_i\cup S_i
$$

has size at most $L(n)+3d+s<t$. Choose $E_i$ avoiding it. Its core trace lies in
$B_i$. Avoidance of $Q_i$ ensures that every point of $R$ occurs in at most two
selected rows. Avoidance of $S_i$ ensures that $E_i\notin\mathcal F_i$, so no
point of $Z$ occurs in two selected rows.

A core point occurs in at most four selected rows, and an exterior point in at
most two. A core point together with an exterior point therefore covers at most
six rows, and two exterior points cover at most four. Two core points miss one
of the Fano templates, hence miss the corresponding selected edge. Thus no two
points cover the seven selected rows, contrary to $P_7$. This proves (6).
$\square$

## Consequences at the three-quarter scale

Suppose, in the theorem, that

$$
n\le k+t-1+c.
\tag{8}
$$

Substituting this in (6) and rearranging gives

$$
\boxed{\quad
t\le\frac34k+\frac34c+\frac{21}{4}d+\frac74s+\frac54.
\quad}
\tag{9}
$$

Consequently the conjectured upper coefficient follows for any sequence of such
families with

$$
c=o(k),\qquad d=o(k),\qquad \log D=o(k^{2/3}).
\tag{10}
$$

Indeed, (5) then gives $s=o(k)$.

Two special cases are useful. If every edge has at most $d$ points outside $U$,
take $R=V\setminus U$ and $Z=\varnothing$, obtaining (9) with $s=0$. Thus a
$(k+t+o(k))$-point set containing all but $o(k)$ points of every edge suffices;
its traces need not retain $P_7$. Conversely, if every exterior point has degree
at most $D$, take $R=\varnothing$ and $d=0$. Polynomial-degree exterior padding
is then harmless, with no bound on the number of exterior points in an
individual edge.

The assertion also tolerates deletion of a low-transversal subfamily. Suppose
$\mathcal D\subseteq\mathcal H$ has $\tau(\mathcal D)\le q$, and apply the
theorem to $\mathcal H'=\mathcal H\setminus\mathcal D$. Its transversal number
$t'$ satisfies $t'\ge t-q$. If the core for $\mathcal H'$ satisfies
$n\le k+t-1+c$, with $t$ the original transversal number, then

$$
t\le\frac34k+\frac74q+\frac34c+\frac{21}{4}d
 +\frac74s+\frac54.
\tag{11}
$$

All exterior degrees in this application are measured in $\mathcal H'$. If the
stronger size bound $n\le k+t'-1+c$ holds, the coefficient of $q$ in (11) can be
replaced by one. In either formulation, $q=o(k)$ adds only $o(k)$ loss.

## A separate dense-core deletion lemma

Suppose a finite family, not necessarily initially satisfying $P_7$, has

$$
|E\cap U|\ge a>0\qquad(E\in\mathcal H),\qquad |U|=n.
$$

Put

$$
b=\max\left\{0,\left\lfloor n-\frac{7a}{4}\right\rfloor+1\right\}.
\tag{12}
$$

Choose any $b$-point set $T\subseteq U$, and delete the subfamily $\mathcal D_T$
of edges meeting $T$. Then $\tau(\mathcal D_T)\le b$, and the remaining traces
on $U\setminus T$ have $P_7$ and transversal number at least
$\tau(\mathcal H)-b$.

To prove the local assertion, seven sets of size at least $a$ on $N<7a/4$ points
always have a two-point cover. Since $N<2a$, every pair of sets intersects. A
point in at least five rows can be combined with a point common to the remaining
at most two rows. Otherwise every point has degree at most four, contradicting
$7a\le4N$. The same argument applies to fewer than seven sets by repetition. Now
use $N=n-b<7a/4$. Finally, a cover of the remaining traces covers the remaining
original edges, while adding $T$ covers the deleted edges.

In particular, the construction in
[Indispensable local cores](indispensable_local_cores.md) has $n=7a/4$ and every
core trace has size $a$. Deleting the star of **any one** core point makes that
core preserve $P_7$. Its exponentially many indispensable labels therefore do
not obstruct a deletion-tolerant core theorem, even without using the separate
two-point cover of its exceptional subfamily.

## Scope and the missing structural theorem

The combined criterion is a conditional upper bound, not a core-existence
theorem. A sufficient unresolved target is the following: after deleting a
subfamily of transversal number $o(k)$ from a putative family with
$t>(3/4+\varepsilon)k$, find $k+t+o(k)$ vertices such that each remaining edge
has only $o(k)$ exterior points whose degrees exceed a threshold $D$ with
$\log D=o(k^{2/3})$. The theorem would then contradict the excess. No argument
here obtains this target from maximal pair intersections, near-twin classes, or
$\tau$-criticality. The available critical set-pair bounds allow exponentially
many vertices; the three-reference reduction gives a linear ground set but no
corresponding bound on exterior incidences or degrees.

The $k+t+o(k)$ size target also needs a near-three-quarter or excess hypothesis;
it is false for arbitrary families with merely $t=\Theta(k)$. For sufficiently
large $k$, take two disjoint blocks of

$$
n_0=\lfloor6k/5\rfloor-1
$$

points and include all $k$-sets within either block. Within one block every
at-most-six edges intersect, because $6k-5n_0>0$. A mixed at-most-seven tuple
has at most six members in either block and is covered by one point from each
block. A tuple contained in one block is likewise covered by two points. Thus
the union has $P_7$, and

$$
t=2(n_0-k+1)=\frac25k+O(1).
$$


If a deleted subfamily has a $q$-point transversal $T$, all $k$-sets avoiding
$T$ in each block remain. Suppose every remaining edge has at most $d$ points
outside $U$, where $q,d=o(k)$. For large $k$, each block minus $T$ still has at
least $k$ points. If more than $d$ of those points were outside $U$, one could
extend $d+1$ of them to a remaining $k$-edge, a contradiction. Hence

$$
|U|\ge2n_0-q-2d=\frac{12}{5}k-o(k),
$$

whereas $k+t=7k/5+O(1)$. This rules out the unrestricted almost-containment
target of size $k+t+o(k)$, not an $O(k)$ core and not the target restricted to a
fixed excess above $3k/4$.

## An anchored almost-core bound

When the core contains an entire edge, fixing that edge as the first selected
row improves the error terms.

**Theorem.** Let $\mathcal H$ have rank at most $k$, property $P_7$, and
transversal number $t$. Suppose

$$
A\in\mathcal H,\qquad |A|=a,\qquad
U=A\mathbin{\dot\cup}T,\qquad |T|=t-1+c,
$$

where $c\ge0$ is an integer. Partition the exterior as $Z\mathbin{\dot\cup}R$,
with every point of $Z$ having degree at most an integer $D\ge1$ and every edge
containing at most an integer $d\ge0$ points of $R$. Define $s$ by (5), again
allowing $s=0$ when $Z=\varnothing$. Then

$$
\boxed{\quad
t\le3\lceil a/4\rceil+3d+
\left\lceil\frac{3s+c}{2}\right\rceil.
\quad}
\tag{13}
$$

The set $T$ need not be a transversal. In particular, a critical edge and its
disjoint critical $(t-1)$-cover supply the required core with $c=0$, but do not
by themselves supply the exterior hypotheses.

**Proof.** Index seven vertex classes by the nonzero vectors
$v\in\mathbb F_2^3$, and index the seven rows by the nonzero vectors $i$. Fix
one row index $i_1$. Partition $A$ nearly equally among the four classes with
$i_1\cdot v=1$, and partition $T$ nearly equally among the other three classes.
Put

$$
B_i=\bigcup_{i\cdot v=1}U_v.
$$

Thus $B_{i_1}=A$. For every other row $i$, its complementary Fano line meets the
complementary line of $i_1$ in one class. Consequently

$$
|U\setminus B_i|
\le 2\lceil a/4\rceil+\lceil(t-1+c)/3\rceil=:h.
\tag{14}
$$


Set $E_{i_1}=A$ and order the remaining six rows arbitrarily. Before selecting a
row $i$, let $Q_i\subseteq R$ be the union of $R\cap E_j\cap E_\ell$ over
preceding pairs $j,\ell$ with $i+j+\ell=0$. There are three possible pairs
through $i$. One contains $i_1$ and contributes nothing, because $E_{i_1}$ has
no exterior points. Each of the other two contributes at most $d$ points, so
$|Q_i|\le2d$.

As in the combined criterion, let $S_i$ cover every edge meeting a $Z$-point in
a preceding row. At most $6kD$ edges meet those points, so $|S_i|\le s$. If
$t>h+2d+s$, choose $E_i$ avoiding

$$
(U\setminus B_i)\cup Q_i\cup S_i.
$$


For every vertex, its spectrum of selected row indices contains no Fano line.
This follows from the cap templates for core vertices, from avoidance of $Q_i$
for vertices of $R$, and from nonrepetition for vertices of $Z$. Every line-free
subset of the Fano plane is contained in a four-point cap: a noncollinear triple
extends to its unique four-point cap, and any further point creates a line. The
complements of two caps are lines and therefore intersect. Hence two vertices
cannot cover the seven selected rows, contradicting $P_7$. We have proved

$$
t\le 2\lceil a/4\rceil+\lceil(t-1+c)/3\rceil+2d+s.
\tag{15}
$$

For the integer $x=2\lceil a/4\rceil+2d+s$, the inequality
$t\le x+\lceil(t-1+c)/3\rceil$ is equivalent to
$2t\le3x+c+1$, and thus to $t\le\lceil(3x+c)/2\rceil$.
This gives (13). $\square$

For a critical pair, (13) gives

$$
t\le\frac34k+3d+\frac32s+O(1).
$$

This is still a conditional bound, not an almost-core existence theorem.

## Small edge density need not mean small transversal number

An average-incidence estimate cannot, without further structural information,
justify deleting an exceptional subfamily merely because that subfamily has few
edges relative to the whole family.

For a precise example, take $k=4m$, $n=7m-1$, and $\mathcal H=\binom Xk$ on an
$n$-point set. Then $t=\tau(\mathcal H)=3m$. This family has $P_7$: seven rows
have total incidence $28m>4n$, so some point meets at least five rows; any two
rows intersect, and a second point covers the at most two remaining rows.
Repetition gives the same conclusion for smaller subfamilies.

For $Q\subseteq X$ with $|Q|=q\le t-1$, let

$$
\mathcal B_Q=\{E\in\mathcal H:E\cap Q=\varnothing\}.
$$

It is a complete $k$-uniform family on $n-q$ points, so

$$
\tau(\mathcal B_Q)=t-q.
$$

On the other hand,

$$
\frac{|\mathcal B_Q|}{|\mathcal H|}
=\frac{\binom{n-q}{k}}{\binom nk}
=\prod_{j=0}^{q-1}\frac{n-k-j}{n-j}
\le\left(1-\frac{k}{n}\right)^q.
$$

Taking $q\to\infty$ with $q=o(k)$ makes the relative edge density tend to zero
exponentially in $q$, while the exceptional subfamily still has transversal
number $t-o(k)$. Thus small average exterior incidence, or small exceptional
edge density obtained from it, does not alone yield the low-transversal deletion
required by an almost-core reduction.
