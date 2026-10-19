---
name: research/erdos_644/certificates_and_obstructions
desc: Proved conditional upper bounds, including rank-aware adaptive triple certificates and a minimum-edge-size restriction, and limitations of natural lower-bound mechanisms.
tags: [proved, conditional, methods]
sources: [fon_der_flaass_et_al_1999_transversals_uniform_hypergraphs_property_7_2]
created: 2026-09-22T20:23:03Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_644/certificates_and_obstructions

***

These results do not settle either assertion of Problem 644. Throughout, use the
condition that every subfamily of at most seven edges has a two-point
transversal. For families with at least seven edges this is equivalent to the
stated condition; smaller families have transversal number at most six and do
not affect the asymptotic question.

The later [block-profile theorem](block_profile_families.md) rules out all full
two-block profile constructions, including the failed example at the end of this
page. [Structural reductions](structural_reductions.md) records the subsequent
rank-aware analysis and its remaining gaps.

## Covering possible pairs by forbidden sets

Suppose $A_1,A_2,A_3\in\mathcal H$, with empty triple intersection. Put

$$
P_i=(A_j\cap A_l)\setminus A_i,\qquad
Q_i=A_i\setminus(A_j\cup A_l),\qquad \{i,j,l\}=\{1,2,3\}.
$$

The graph of pairs meeting all three edges has exactly the complete bipartite
pieces $P_i\times P_j$, $i\ne j$, and $P_i\times Q_i$. A point outside their
union cannot participate in such a pair.

Assign each point a nonempty support in $\{0,1,2,3\}$, so that supports of
endpoints of every such pair intersect. Let $S_a$ contain the points whose
support includes $a$. If $\tau(\mathcal H)>\max_a|S_a|$, choose
$B_a\in\mathcal H$ disjoint from $S_a$. Every pair covering $A_1,A_2,A_3$ is
contained in some $S_a$, and hence misses $B_a$. These at most seven edges
contradict the local condition. Therefore

$$
\tau(\mathcal H)\le\max_a|S_a|.
\tag{2}
$$


### A balanced-triple bound

Assume $|P_i|=xk+O(1)$ for all $i$. Then $|Q_i|=(1-2x)k+O(1)$, where
$0\le x\le1/2$. Fractional allocations below can be rounded with $O(1)$ error.

For $0\le x\le1/4$, give every point of $P_i$ support $\{0,i\}$. Give $(1/4-x)k$
points of $Q_i$ support $\{0\}$, and the remainder support $\{i\}$. All four
loads are $3k/4+O(1)$.

For $1/4\le x\le1/2$, put $b=(4x-1)/5$. Give $bk$ points of every $P_i$ support
$\{1,2,3\}$, and the remaining points support $\{0,i\}$. Give $Q_i$ support
$\{i\}$. The center load is $3(x-b)k$; each leaf load is $(1-x+2b)k$. They
coincide at

$$
\frac{3(1+x)}5k.
$$


A second allocation uses the three perfect matchings of $K_4$. Assign each $P_i$
to one matching and split its points equally between that matching's two edges,
using an edge as the support. Assign $Q_i$ equally among the four edges joining
the opposite matching's two parts. Cross-type supports intersect whenever
required. Each of the four coordinate loads is

$$
\frac12|A_1\cup A_2\cup A_3|+O(1)
=\frac32(1-x)k+O(1).
$$

The two bounds cross at $x=3/7$, with value $6k/7$. Hence a balanced good triple
implies

$$
\tau(\mathcal H)\le6/7k+O(1).
$$

If the three pair sizes differ by $o(k)$, the same conclusion holds with $o(k)$
error. No argument has been found forcing such a triple in an arbitrary extremal
family.

### Exact three-quarter threshold for a static four-set certificate

The following checked refinement of §9.3 in
[first independent record](independent/fano_ground_set_and_coding_constructions.md)
extends the earlier balanced obstruction. Normalize $k=1$, put $p_i=|P_i|$,
$s=p_1+p_2+p_3$, and $q_i=|Q_i|=1-s+p_i$. Assume **all six atom weights are
positive**, and allow atoms to be split into real weights. Four sets of weight
at most $3/4$ cover all candidate graph edges if and only if

$$
p_i+q_i\ge\frac34\quad(i=1,2,3),
\qquad\text{equivalently}\qquad s-2p_i\le\frac14.
\tag{S}
$$


For necessity, give a point the support of the four covering sets containing it.
Every point has a neighbor and hence nonempty support. A $P_i$-point cannot have
singleton support: its neighborhood has weight $p_j+p_\ell+q_i=1$, exceeding one
set's capacity. Total load is therefore at least

$$
2s+\sum_iq_i=3.
$$

Equality is forced: every $P$-support has size two, every $Q$-support size one,
and all four loads equal $3/4$.

The two-element $P$-supports intersect pairwise. Across different atoms this
follows from adjacency; within $P_i$ it follows because a singleton support in
the nonempty $Q_i$ must meet every such support. A pairwise-intersecting family
of two-subsets is contained in a star or a triangle. The triangle case leaves
the fourth coordinate empty, also for the $Q$-supports, a contradiction.

Let the star center be $0$. If one $P_i$ uses two arms, its entire opposite atom
$Q_i$ must have support $\{0\}$. The center load would then be at least
$s+q_i=1+p_i>3/4$. Thus each $P_i$ uses a fixed arm $\{0,a_i\}$. The three arms
must be different, since otherwise an unused leaf has zero load: every $Q_i$
singleton also lies in $\{0,a_i\}$. Leaf $i$ consequently needs $3/4-p_i$ weight
from $Q_i$, proving (S).

Conversely, summing (S) gives $s\le3/4$. Give $P_i$ support $\{0,i\}$, give
weight $3/4-p_i$ of $Q_i$ support $\{i\}$, and place the remaining weight of
$Q_i$ at $\{0\}$. The conditions make these weights feasible; all four loads are
$3/4$ and every candidate pair has intersecting supports.

For finite atoms the same exact criterion holds when $4\mid k$; otherwise the
continuous construction rounds with $O(1)$ error. In particular, balanced
$p_i=x$ fails (S) for $1/4<x<1/2$. This obstructs this static certificate for
the given triple, not the selection of a different triple or an adaptive
argument.

The positivity hypotheses matter. If $p_i=1/2$ and $q_i=0$, split each $P_i$
into two equal halves and use the four even-parity binary triples to choose one
half of each atom. Each covering set has weight $3/4$, and every cross-atom pair
is covered, although (S) fails. Vanishing overlap atoms also change the problem:
with $(p_1,p_2,p_3)=(0,1/4,1/4)$, the atom $Q_1$ is isolated. Split $Q_2$ into
weights $1/4,1/2$ and $Q_3$ into weights $1/2,1/4$. The sets consisting of
$P_2\cup P_3$ plus the first part of $Q_2$, $P_2$ plus its second part, and
$P_3$ plus each part of $Q_3$ cover the graph with weights $3/4,3/4,3/4,1/2$,
while $s-2p_1=1/2$.

### Checking the independent hub construction

Section 5.1 of
[second independent record](independent/fractional_reductions_and_good_triples.md)
gives a valid exact threshold for one particular static allocation. Return to
unnormalized sizes $p_i=|P_i|$, $s=\sum_i p_i$, $q_i=|Q_i|=k-s+p_i$. Put all
$P_i$ in a central set and also put $P_i$ in leaf $i$; split $Q_i$ between the
center and leaf $i$. A maximum load $T$ is feasible for this allocation exactly
when

$$
T\ge\max_i p_i,\qquad
s+\sum_i(p_i+q_i-T)_+\le T.
$$

The leaf requires at least $(p_i+q_i-T)_+$ points to be moved to the center.
Expanding the positive parts over the eight subsets of $[3]$ gives the least
real threshold

$$
T_{\rm hub}=\max\left\{
\frac{3k}{4},\ s,\ \frac{k}{2}+\max_i p_i,
\ \max_i\frac{2k+s-2p_i}{3}\right\}.
\tag{H}
$$

The separate constraint $p_i\le T$ follows from $T\ge s$. For finite atoms
$T=\lceil T_{\rm hub}\rceil$ gives integral splits with no further error.

This is not a stronger upper bound than the adaptive certificate (G0) below.
With $a=\max_i p_i$ and $b$ the sum of the two largest pair sizes,

$$
\frac{k+b}{2}\le\frac{k}{2}+a\le T_{\rm hub},\qquad
\frac{k+s+2a}{3}
=\frac{s}{3}+\frac23\left(\frac{k}{2}+a\right)
\le T_{\rm hub}.
$$

Thus every term of (G0) is at most (H). At $T=3k/4$ its feasibility condition
agrees with (S) when all atoms are positive. In particular the independent §5.2
obstruction at $p_i=3k/8$, $q_i=k/4$ is valid but already covered by (S).

The reported optimum $33/40$ for that balanced example is not certified here.
Its explicit **upper** allocation is the balanced construction above at $x=3/8$:
put $11k/40$ points of $P_i$ at support $\{0,i\}$, the remaining $k/10$ at
support $\{1,2,3\}$, and $Q_i$ at support $\{i\}$. Exact realization requires
$40\mid k$; otherwise it gives $33k/40+O(1)$. The independent record's other
solver-reported optima remain unverified, and its referenced
`good_triple_cover.py` is not present in this research folder. None is used in a
proof.

### Review of the independent static certificates

Section 7 of
[third independent record](independent/complete_family_limit_and_seven_edge_obstruction.md)
reproduces the balanced static obstruction and both balanced upper allocations
above. Its type classification is valid: a private atom forces its core's
two-element supports to share an index, and cross-adjacency makes supports from
different cores intersect. Hence all occurring two-element supports form a star
or triangle. Criterion (S) already gives the stronger asymmetric statement, with
its positivity hypotheses essential. The input's small-union bound is proved in
[Forbidden distances](forbidden_distances.md#a-four-set-certificate-from-an-empty-intersection-triple).
Its three solver-reported exact optima remain unverified; the explicit $33/40$
allocation certifies only an upper bound.

### Qualification to the small-intersection observation

For a fixed edge $A$, let $m=\min_E|A\cap E|$. If $m\ge1$, any $(k-m+1)$-subset
of $A$ is a transversal, so $\tau\le k-m+1$. The standalone claim in §9.1 of the
independent note needs this hypothesis: for $m=0$ that subset does not exist,
and arbitrary uniform families can have $\tau>k+1$ (take $k+2$ disjoint edges).
The intended consequence remains valid by a case split: if $\tau>3k/4$, either
an edge is disjoint from $A$, or $m<k/4+1$. This alone does not select the later
edges of a seven-edge obstruction.

## An adaptive sparse-triple certificate

For any three edges, not necessarily a good triple, let

$$
S=(A_1\cap A_2)\cup(A_1\cap A_3)\cup(A_2\cap A_3).
$$

Then

$$
\tau(\mathcal H)\le |S|+\lceil k/3\rceil.
\tag{3}
$$

Indeed, otherwise choose $D\in\mathcal H$ disjoint from $S$, partition
$D=D_1\cup D_2\cup D_3$ with $|D_i|\le\lceil k/3\rceil$, and choose
$E_i\in\mathcal H$ avoiding $S\cup D_i$. Any pair covering $A_1,A_2,A_3$ has a
point $x\in S$. To meet $D$ its other point must belong to some $D_i$. Then the
pair misses $E_i$, contradiction. This proves (3), but the hypothesis
$|S|\le5k/12+o(k)$ needed to deduce the conjectured bound has not been forced
globally.

## A three-part certificate and its dense obstruction

Section 9.5 of the same independent note gives another valid template. Partition
an edge $A=A_1\sqcup A_2\sqcup A_3$, and suppose edges
$B_1,B_2,B_3\in\mathcal H$ satisfy $B_i\cap A\subseteq A_i$. Put
$R_i=B_j\cap B_\ell$, where $\{i,j,\ell\}=[3]$. Then $R_i\cap A=\varnothing$,
and

$$
\tau(\mathcal H)\le\max_i\bigl(|A_i|+|R_i|\bigr).
\tag{T}
$$

Otherwise choose $C_i$ disjoint from $A_i\cup R_i$. A pair covering $A$ contains
a point in some $A_i$. That point misses $B_j,B_\ell$, forcing the other point
into $R_i$; both then miss $C_i$. The seven displayed edges therefore have no
two-cover. Repetitions may be removed.

The template does not give the conjectured bound automatically. Take the
complete $k$-uniform family on $n=7k/4-1$ points, with $12\mid k$, and balanced
$|A_i|=k/3$. Every permitted $B_i$ has at least $2k/3$ points outside $A$, so

$$
|R_i|\ge\frac{4k}{3}-(n-k)=\frac{7k}{12}+1,
\qquad |A_i|+|R_i|\ge\frac{11k}{12}+1.
$$

These families have $P_7$ and $\tau=3k/4$. Thus even at the conjectured boundary
the required outside-intersection estimates fail for this balanced template.
This is a method obstruction, not a counterexample to the problem.

## A four-part certificate

Partition an edge as $A=A_1\sqcup A_2\sqcup A_3\sqcup A_4$. Suppose four other
edges $B_{12},B_{34},B_{13},B_{24}$ satisfy

$$
B_{ij}\cap A\subseteq A_i\cup A_j.
$$

Put

$$
\begin{aligned}
D_{14}&=((B_{12}\cap B_{24})\cup(B_{13}\cap B_{34}))\setminus A,\\
D_{23}&=((B_{12}\cap B_{13})\cup(B_{24}\cap B_{34}))\setminus A.
\end{aligned}
$$

Then the local seven-edge property implies the exact bound

$$
\tau(\mathcal H)\le
\max\{|A_2\cup A_3|+|D_{14}|,
       |A_1\cup A_4|+|D_{23}|\}.
\tag{K4}
$$


Otherwise choose $B_{14}$ avoiding $A_2\cup A_3\cup D_{14}$ and $B_{23}$
avoiding $A_1\cup A_4\cup D_{23}$. All six edges $B_{ij}$ now have the indicated
trace restriction. Each triangle of $K_4$ indexes three edges with empty common
intersection: their traces on $A$ have empty intersection, while the
corresponding outside intersection is excluded by $B_{14}$ or $B_{23}$.

A pair covering $A$ contains a point $x\in A_i$ for some $i$. The point $x$
misses the three edges indexed by the triangle on $[4]\setminus\{i\}$. The other
point would have to lie in their empty common intersection. Thus these
at-most-seven edges form a bad subfamily, proving the bound.

For balanced parts the conclusion is

$$
\tau(\mathcal H)\le k/2+\max(|D_{14}|,|D_{23}|)+O(1).
$$

This would give the desired coefficient if one could arrange both outside
intersection unions to have size at most $k/4+o(k)$. No unrestricted selection
argument giving those two estimates has been established. The trace restrictions
alone do not supply them.

## A bound using the largest pair intersection in a good triple

### A rank-aware refinement

For a good triple in a rank-at-most-$k$ $P_7$ family, put $p_i=|P_i|$,
$s=p_1+p_2+p_3$, $a=\max_i p_i$, and let $b$ be the sum of the two largest
$p_i$. Then

$$
\tau(\mathcal H)\le
\left\lceil\max\left\{s,\frac{k+b}{2},
\frac{k+s+2a}{3}\right\}\right\rceil.
\tag{G0}
$$


Let $L$ be the displayed integer and suppose $\tau>L$. Choose $D$ avoiding all
three pair atoms. A two-cover of the reference triple and $D$ must have type
$P_i\times R_i$, where $R_i=D\cap Q_i$. Write $q_i=|R_i|$; the sets $R_i$ are
disjoint and $\sum q_i\le k$.

These three complete bipartite graphs can be covered by three induced vertex
sets of size at most $L$. If $p_i+q_i\le L$ for all $i$, use $P_i\cup R_i$.
Otherwise there is at most one overloaded type $h$: two overloaded types would
imply

$$
q_i+q_j>2L-p_i-p_j\ge k.
$$

Keep $P_j\cup R_j$ in its own bin for $j\ne h$. The capacities available for
splitting $R_h$, with $P_h$ included in every bin receiving a nonempty part, are

$$
L-p_h,\qquad
\max\{0,L-p_j-q_j-p_h\}\quad(j\ne h).
$$

Their sum is at least

$$
3L-s-2p_h-\sum_{j\ne h}q_j
\ge k-\sum_{j\ne h}q_j\ge q_h.
$$

If a secondary bin has zero capacity, retain its original contents without
adding $P_h$. Thus all bin-size claims remain valid even when an untruncated
capacity is negative. Integral splitting supplies the three required sets. Three
further edges avoiding them contradict $P_7$, proving (G0).

In particular, if every pair intersection of a good triple is at most
$a\le k/4$, then

$$
\tau(\mathcal H)\le\lceil k/2+a\rceil\le\lceil3k/4\rceil.
\tag{G0a}
$$

Indeed, $s\le3a$, $b\le2a$, and each expression in (G0) is at most $k/2+a$. This
certificate also restricts essential-incidence witnesses; see
[Incidence-minimal families](incidence_minimal_families.md).

### Allowing a common intersection

The same allocation extends to an arbitrary triple $A_1,A_2,A_3$ in a
rank-at-most-$k$ $P_7$ family. Put

$$
C=A_1\cap A_2\cap A_3,\qquad c=|C|,
$$

and define the exclusive pair atoms and single-row atoms by

$$
P_i=(A_j\cap A_\ell)\setminus C,\qquad
Q_i=A_i\setminus(A_j\cup A_\ell),
\qquad \{i,j,\ell\}=[3].
$$

As before, let $p_i=|P_i|$, $s=\sum_i p_i$, $a=\max_i p_i$, and let $b$ be the
sum of the two largest $p_i$. Then

$$
\tau(\mathcal H)\le c+
\left\lceil\max\left\{s,\frac{k+b}{2},
\frac{k+s+2a}{3}\right\}\right\rceil.
\tag{G0c}
$$


Write $G$ for the ceiling in (G0c), and suppose $\tau>c+G$. Choose an edge $D$
avoiding $C\cup P_1\cup P_2\cup P_3$, whose size is $c+s\le c+G$. Set

$$
R_i=D\cap Q_i,\qquad q_i=|R_i|,\qquad
R_0=D\setminus(R_1\cup R_2\cup R_3).
$$

Every two-cover of the reference triple and $D$ has type $C\times D$ or
$P_i\times R_i$. Indeed, a cover avoiding $C$ either uses two different pair
atoms, which both miss $D$, or has type $P_i\times Q_i$.

We construct three bins of capacity $G$ which cover the graphs $P_i\times R_i$
and whose union contains all of $D$. If $p_i+q_i\le G$ for every $i$, start with
$P_i\cup R_i$ in bin $i$. The total spare capacity is

$$
3G-s-\sum_i q_i\ge k-\sum_i q_i\ge |R_0|,
$$

so the points of $R_0$ can be distributed among the bins.

Otherwise at most one type $h$ overloads: two overloads would give

$$
q_i+q_j>2G-p_i-p_j\ge k,
$$

contrary to $\sum_iq_i\le k$. Start with $P_h$ in bin $h$ and $P_j\cup R_j$ in
each other bin. The capacities for portions of $R_h$, including a copy of $P_h$
in every receiving bin, are

$$
G-p_h,\qquad \max\{0,G-p_j-q_j-p_h\}\quad(j\ne h).
$$

Their sum is at least

$$
3G-s-2p_h-\sum_{j\ne h}q_j
\ge k-\sum_{j\ne h}q_j\ge q_h.
$$

Thus $R_h$ can be split integrally among these bins. A secondary bin receiving
no part of $R_h$ need not receive $P_h$. After this step the total occupancy is
at most

$$
s+\sum_iq_i+2p_h.
$$

Since $3G\ge k+s+2a$, the spare capacity is still at least
$k-\sum_iq_i\ge|R_0|$. Distribute $R_0$ into this spare capacity. This last step
is needed because a point of $D$ outside all three reference edges can still
partner a point of $C$.

Finally add $C$ to every bin. The resulting three sets have size at most $c+G$
and contain every possible two-cover of $A_1,A_2,A_3,D$. Three further edges
avoiding them contradict $P_7$, proving (G0c).

In particular, $p_i\le k/4$ for all $i$ gives

$$
\tau(\mathcal H)\le c+\lceil3k/4\rceil.
$$

If $C=\{v\}$ and $t=\tau(\mathcal H)>1+\lceil3k/4\rceil$, then $a>k/4$. For
$a\ge k/4$ all three expressions defining $G$ are at most $3a$, so

$$
a\ge\left\lceil\frac{t-1}{3}\right\rceil.
$$

The
[incidence-witness restrictions](incidence_minimal_families.md#a-one-sided-trace-classification-for-three-containing-rows)
give one application. This does not force the required triple in an arbitrary
family.

### The extremal-pair certificate

In this paragraph a good triple is an ordered triple of edges with empty triple
intersection, **allowing repeated edges**. Let $m$ be the largest
pair-intersection size occurring in such a triple of a $k$-uniform $P_7$ family.
Then

$$
\tau(\mathcal H)\le\max\{\lceil3k/4\rceil,2m\}.
\tag{G}
$$

If there is no good triple, the family is three-wise intersecting and the usual
partition of one edge into two parts gives $\tau\le\lceil k/2\rceil$.

To prove (G), suppose $\tau>t$, with integer $t\ge3k/4$ and $2m\le t$. Choose a
good triple with atom sizes $p_i=|P_i|$, $q_i=|Q_i|$, and put $d_i=p_i+q_i$.

If all $d_i\ge t$, give every $P_i$-point support $\{0,i\}$, give $d_i-t$ points
of $Q_i$ support $\{0\}$, and give the remaining $Q_i$-points support $\{i\}$.
The selected number lies between zero and $q_i$, because $p_i\le m\le t$. Every
leaf load is $t$, while the center load is

$$
\sum_i p_i+\sum_i(d_i-t)=3(k-t)\le t.
$$

The static four-set certificate yields a contradiction.

Otherwise assume $d_3<t$. Choose an edge $E$ avoiding $P_1\cup P_2$, whose size
is at most $2m\le t$. Both $(A_1,A_3,E)$ and $(A_2,A_3,E)$ are good, so

$$
|E\cap A_1|\le m,\qquad |E\cap A_2|\le m.
$$

Every pair covering $A_1,A_2,A_3,E$ is contained in one of

$$
\begin{aligned}
T_1&=P_1\cup(E\cap Q_1)\cup(E\cap P_3),\\
T_2&=P_2\cup(E\cap Q_2)\cup(E\cap P_3),\\
T_3&=P_3\cup Q_3.
\end{aligned}
$$

Indeed, the original pair types are $P_i\times P_j$ and $P_i\times Q_i$; $E$
excludes $P_1\times P_2$, and the other types have exactly the listed
containment. The three sizes are at most $2m,2m,d_3$, respectively. Three
further edges avoiding these sets give at most seven edges with no two-cover, a
contradiction.

This restricts any counterexample to having a good-triple pair intersection
larger than $3k/8+o(k)$. It gives no universal improvement: complete-family
examples themselves have much larger such intersections.

If the family contains two disjoint edges, the repetition convention gives
$m=k$, so this certificate reduces to the elementary bound $2k$. In an
intersecting family every good triple is automatically distinct. Allowing
repetitions ensures that the two response triples in the proof are always
admissible; repeated edges can be removed from the final bad tuple without
creating a two-cover.

## Bounded pair intersections force a bounded transversal number

Suppose every two **distinct** edges of a $P_7$ family intersect in at most an
integer $\lambda\ge0$ points. Then

$$
\tau(\mathcal H)\le\max\{2,3\lambda\}.
\tag{B}
$$

Uniformity is unnecessary. This certificate arose alongside the
[disjointness-graph route](helly_and_chromatic_reduction.md).

For $\lambda=0$, all edges are disjoint and $P_3$ permits at most two. For
$\lambda\ge1$, suppose $\tau>3\lambda$. Choose three distinct edges
$A_1,A_2,A_3$ with empty common intersection: if two intersect, choose a third
avoiding their intersection; if two are disjoint, take any third edge. Such an
edge exists since $\tau>3$.

Let $S$ be the union of their pair intersections. If $S$ meets all three edges,
choose $D$ disjoint from $S$, whose size is at most $3\lambda$. This $D$ is
distinct from all references. Otherwise precisely one reference edge is disjoint
from the other two, since three disjoint edges would violate $P_3$. Now
$|S|\le\lambda$; adjoin one point of the isolated reference to $S$ and choose
$D$ avoiding the enlarged set, of size at most $\lambda+1\le3\lambda$. Again $D$
is distinct from all three and avoids $S$.

Put $P_i=A_j\cap A_\ell$, where $\{i,j,\ell\}=[3]$. A pair covering the
reference triple and $D$ must have one point in $P_i$ and its other point in
$D\cap A_i$ for some $i$: pairs using two overlap points both miss $D$. Every
surviving pair is therefore contained in one of the three sets

$$
P_i\cup(D\cap A_i),
$$

each of size at most $2\lambda$, using the distinctness of $D$ and $A_i$. Three
further edges avoiding these sets produce at most seven edges with no two-cover,
a contradiction. This proves (B). It gives $\tau=o(k)$ when all distinct pair
intersections are $o(k)$, but does not control the large-intersection regime of
the original problem.

For $\lambda=1$, the later
[linear-family theorem](helly_and_chromatic_reduction.md#linear-families-six-local-edges-suffice-exactly)
sharpens this conclusion to $\tau\le2$, and needs only $P_6$.

## A minimum-edge-size restriction

Let $\mathcal H$ have rank at most $k$ and property $P_7$, and put
$t=\tau(\mathcal H)$. Every edge $E$ of size $e$ satisfies

$$
t\le\max\left\{e+1,\frac{k+2e+3}{3}\right\}.
\tag{R}
$$

Consequently, if $t\le k+1$, then

$$
e\ge\frac{3t-k-3}{2}.
$$

In particular, $t>(3/4+\varepsilon)k$ forces every edge to have size at least
$(5/8+3\varepsilon/2)k-O(1)$ in the range $t\le k+1$. This is a necessary
restriction, not an upper bound at the three-quarter threshold.

For the proof, the case $e\ge t-1$ is immediate in (R). Otherwise let
$\mathcal H_0$ be the family of edges disjoint from $E$. Covering all other
edges by $E$ gives

$$
\tau(\mathcal H_0)\ge t-e\ge2.
$$

For any two distinct $D,D'\in\mathcal H_0$, a two-cover of $D,E,D'$ consists of
one point of $E$ and one point of $D\cap D'$. The latter intersection is
nonempty by $P_3$. Partition $E$ and $D\cap D'$ into two balanced parts each.
The four unions of one part from each side contain every possible two-cover.
Choosing four further edges avoiding them, if all four unions had size less than
$t$, would contradict $P_7$. Hence

$$
t\le\left\lceil\frac e2\right\rceil+
\left\lceil\frac{|D\cap D'|}{2}\right\rceil,
\qquad
|D\cap D'|\ge2t-e-2.
$$

This is the $2\times2$ case of the [connected-disjointness-reference
certificate](helly_and_chromatic_reduction.md#connected-disjointness-references-without-helly).

Fix $D\in\mathcal H_0$ and write $h=2t-e-2>0$. There is another edge in
$\mathcal H_0$, so $|D|\ge h$. Any $(|D|-h+1)$-subset of $D$ meets every edge of
$\mathcal H_0$. It follows that

$$
t\le e+\tau(\mathcal H_0)
\le e+k-h+1=k-2t+2e+3,
$$

which proves (R). If $t\le k+1$, the alternative $e\ge t-1$ also implies
$e\ge(3t-k-3)/2$, giving the stated corollary.

## Rectangles from two disjoint reference edges

Section 5.4 of
[second independent record](independent/fractional_reductions_and_good_triples.md)
gives a useful exact description of the local condition **anchored at two
disjoint edges**. Let $A,B\in\mathcal H$ be disjoint $k$-sets. A two-cover of
them is precisely a pair $(x,y)\in A\times B$. For each further edge $C$ put

$$
R_C=(A\setminus C)\times(B\setminus C).
$$

The pair misses $C$ exactly when it lies in $R_C$. Thus every subfamily
consisting of $A,B$ and at most five further edges has a two-cover if and only
if no at-most-five available rectangles cover $A\times B$. In particular $P_7$
implies this prohibition.

Rank at most $k$ gives

$$
|A\setminus C|+|B\setminus C|
=2k-|C\cap(A\cup B)|\ge k.
$$

If $T<\tau(\mathcal H)$, every $X\subseteq A$, $Y\subseteq B$ with
$|X|+|Y|\le T$ has

$$
X\times Y\subseteq R_C
$$

for some available $C$: choose an edge avoiding $X\cup Y$. These are checked
necessary conditions, not a characterization of the unanchored $P_7$ property.
The proposed implication from these rectangle conditions to a three-quarter
bound is **disproved** in
[Disjoint reference families](disjoint_reference_families.md#the-fixed-disjoint-pair-relaxation-admits-coefficient-four-fifths):
a rank-$k$ family with $\tau=(4/5+o(1))k$ satisfies all these anchored
conditions. It is not $P_7$. The same page constructs genuine,
transversal-critical $P_7$ families with disjoint edges and $\tau/k\to5/7$. The
[uniform anchored triple relaxation](structural_reductions.md#uniform-rank-does-not-repair-the-anchored-relaxation)
gives a separate limitation of fixed references.

## Affine binary codes: an exact obstruction

Let $C\subseteq\mathbb F_2^n$ be an affine subspace, let $d=\min_{c\in C}|c|$,
and let $\mathcal H$ be a $k$-uniform family all of whose incidence vectors lie
in $C$. Suppose $n<2k$.

The condition

$$
d>4n-7k
\tag{4}
$$

ensures the local two-point property. In fact, seven bad edges have every point
of degree at most four: a point in five edges, together with a point in the
intersection of the remaining two, would cover them. Their XOR lies in $C$, and
its weight is at most the total deficiency $\sum_v(4-\deg v)=4n-7k$,
contradicting (4).

However, (4) also forces

$$
\tau(\mathcal H)\le\lceil3k/4\rceil.
\tag{5}
$$

To prove this, set $t=\lceil3k/4\rceil$ and suppose $\tau>t$. Every $w=n-t$
point subset contains an edge, so $w=k+j$ with $j\ge0$. Put

$$
D=4n-7k=4j+(4t-3k),\qquad0\le4t-3k\le3.
$$

Since $n<2k$, one has $w<2n/3$. There exist three $w$-sets $R_1,R_2,R_3$ whose
XOR has weight $\varepsilon\in\{0,1\}$, where $\varepsilon\equiv w\pmod2$: for
even $w$, take the three pairwise unions of three disjoint $w/2$-sets; for odd
$w$, use three disjoint $(w-1)/2$-sets and add one common point.

Choose $A_i\in\mathcal H$ contained in $R_i$. Their XOR belongs to $C$ and has
weight at most $3j+\varepsilon$. If $j\ge1$, this is at most $4j\le D$. If
$j=0<D$, it is at most $1\le D$. If $j=D=0$, then $4\mid k$, $w=k$ is even, and
$\varepsilon=0$. This contradicts $d>D$ in every case and proves (5).

This excludes lower-bound improvements using only the XOR-distance criterion. It
does **not** exclude more refined coding arguments exploiting the Fano structure
of near-extremal bad seven-tuples.

## Weighted density: another exact obstruction

Suppose a finite ground set has nonnegative weights and every edge satisfies

$$
w(A)>\frac47 w(V).
$$

The weighted degree argument implies the local two-point property. But the
$t=\lceil3k/4\rceil$ heaviest points form a transversal: if an edge $A$ missed
them, then

$$
w(V)\ge w(A)+w(T)\ge(1+t/k)w(A)\ge\tfrac74w(A),
$$

a contradiction. Thus this mechanism cannot produce an asymptotic counterexample
either.

## A two-block candidate that fails the local condition

Let $k=1000q$, partition the ground set into $|X|=500q$ and $|Y|=1499q$, and
take all $k$-sets satisfying

$$
|A\cap X|\le100q\quad\hbox{or}\quad |A\cap X|\ge340q.
$$

This family has transversal number $759q+2$. Indeed, for a remaining point set
$R$, the possible $X$-counts of its $k$-subsets form the interval

$$
[\max(0,k-|R\cap Y|),\,\min(k,|R\cap X|)].
$$

If $|R|\ge k$, it contains no edge precisely when this interval lies inside
$[100q+1,340q-1]$. The largest such $R$ has $|R\cap X|=340q-1$ and
$|R\cap Y|=900q-1$, giving the stated transversal number.

Nevertheless the local condition fails for every $q$. Here is a seven-edge
obstruction at $q=1$; multiply every class size by $q$ for the general case.
Label point classes by their incidence spectra in $[7]$:

| Part | Spectrum | Class size |
|---|---|---:|
| $X$ | $\varnothing$ | 96 |
| $X$ | $\{7\}$ | 54 |
| $X$ | $\{1,2,7\},\{1,3,7\},\{2,3,7\}$ | 50 each |
| $X$ | $\{5,7\},\{4,6,7\}$ | 100 each |
| $Y$ | $\{2,3,4,5\},\{1,3,4,6\},\{1,2,5,6\}$ | 301 each |
| $Y$ | $\{1,2,4,7\},\{1,3,5,7\},\{2,3,6,7\},\{4,5,6,7\}$ | 149 each |

Every edge has size 1000. The seven $X$-counts are
$(100,100,100,100,100,100,404)$, so all edges belong to the candidate family.
The complements of the seven four-element spectra are the Fano lines

$$
167,\ 257,\ 347,\ 356,\ 246,\ 145,\ 123.
$$

Hence two four-element spectra never cover $[7]$. None of the three-element
spectra is one of these lines, so no three-element spectrum complements a
four-element one. All other spectrum pairs have total size at most six. Thus no
two points cover the seven edges.

This is a verified rejection of a proposed counterexample, not a counterexample
to the problem. In particular, checking only pure degree-four Fano blowups can
miss lower-degree spectra essential to a bad tuple.

## Endpoint two-profile candidate: a finite correction

Section 8 of
[third independent record](independent/complete_family_limit_and_seven_edge_obstruction.md)
considers $k=120$, $|X|=104$, $|Y|=179$, and all edges of profiles $(0,120)$ or
$(70,50)$. Its stated transversal number $93$ should be **$95$**.

Every transversal needs at least $60$ points of $Y$ to hit all low
edges. To hit all high edges it must also contain either $35$ points
of $X$ or $130$ points of $Y$: otherwise a remaining $70$-subset
of $X$ and $50$-subset of $Y$ give a missed edge. Thus

$$
\tau=\min\{60+35,130\}=95.
$$

The value $93$ omits the $+2$ in the input's correct mixed-block
formula.

The rejection of this candidate is nevertheless correct. Choose four
low edges whose intersection is empty: their $59$-point complements
can cover $Y$, since three disjoint such complements leave just two
points, which can be included in the fourth. Choose three high edges
whose $50$-point $Y$ parts are pairwise disjoint; use any $70$-point
$X$ parts. Two $X$ points miss every low edge. One $X$ point and one
$Y$ point cannot cover the four low edges. Two $Y$ points cannot
meet the three disjoint high parts. These seven edges have no
two-cover. The family is therefore not a counterexample despite
having $\tau>3k/4$.
