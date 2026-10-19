---
name: research/erdos_644/six_row_exchanges
desc: A lexicographic six-row exchange lemma, its missing aggregate inequality, endpoint-core obstructions, and a 37k/49 ambient bound for one eight-row example.
tags: [proved, conditional, limitations]
sources: []
created: 2026-09-23T05:00:08Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/six_row_exchanges

***

The exchange lemma below is proved, but the aggregate estimate needed to obtain
the three-quarter coefficient is not. In particular, the proposed
perfect-matching sufficient condition for that estimate is false and is
explicitly withdrawn below. Nothing here resolves either unrestricted assertion
of Problem 644.

Let $\mathcal H$ be a finite family of nonempty sets of rank at most $k$,
with property $P_7$: every subfamily of at most seven edges has a transversal
of size at most two. Write $t=\tau(\mathcal H)$. Repetitions are permitted in
selected tuples and are counted when defining point degrees.

## The lexicographic exchange lemma

Suppose $t>\lceil k/2\rceil$. The
[balanced exclusion lemma](degree_bounded_selections.md#a-balanced-exclusion-lemma),
with $p=6$ and $b=4$, supplies a six-tuple

$$
\mathcal E=(E_1,\ldots,E_6)
$$

in which every point has degree at most four. For such a tuple, let $G$ be the
graph whose edges are the two-point covers of all six rows. Let $W$ be its set
of nonisolated vertices, and write

$$
w=|W|,\qquad A=\sum_{x\in W}d(x).
$$

Choose $\mathcal E$ lexicographically minimizing $(w,A)$ among all
six-tuples with maximum degree at most four.

For each $i$, let $Q_i$ be the graph of two-point covers of the other five
rows, let $V_i$ be its set of nonisolated vertices, and put

$$
T_i=V_i\setminus E_i.
$$

The five rows have empty common intersection, since their point degrees are at
most four. Thus every endpoint of an edge of $Q_i$ belongs to the union of
those five rows; points outside the old six-row union cannot become endpoints
merely by replacing $E_i$.

**Lemma.** The chosen tuple satisfies

$$
\boxed{\quad w\ge t,\qquad |T_i|\ge t-1\quad(i\in[6]).\quad}
\tag{1}
$$


**Proof.** For any $E\in\mathcal H$, apply $P_7$ to the six reference rows
together with $E$. The resulting pair is an edge of $G$ and meets $E$.
Therefore $W$ is a transversal, proving $w\ge t$.

Fix $i$. There is a point $v\in E_i\cap W$, since a pair covering the six
rows must meet $E_i$. Suppose $|T_i|+1<t$, and choose an edge $E$ avoiding
$T_i\cup\{v\}$. Replace $E_i$ by $E$.

The new pair-cover graph consists precisely of those edges of $Q_i$ touching
$E$. Since

$$
E\cap V_i\subseteq E_i\cap V_i,
$$

this graph is contained in the old pair-cover graph. Its endpoint set $W'$
therefore satisfies $W'\subseteq W$.

The new tuple still has maximum degree at most four. The only possible violation
would come from a point $x\notin E_i$ having old degree four and belonging to
$E$. Such an $x$ lies in four of the other five rows. Pair it with any point
of the remaining nonempty row; this shows $x\in V_i\setminus E_i=T_i$,
contrary to the choice of $E$.

If $|W'|<|W|$, lexicographic minimality is contradicted. Otherwise $W'=W$.
Since $W\subseteq V_i$, no active point outside $E_i$ enters the replacement
row, while the active point $v$ leaves it. Hence the sum of active incidences
strictly decreases, again a contradiction. Therefore $|T_i|+1\ge t$, proving
(1). $\square$

## The conditional aggregate target

For a point $x$, let its spectrum be

$$
I_x=\{i\in[6]:x\in E_i\},\qquad d(x)=|I_x|.
$$

Only points in the six-row union are counted below. For an occurring spectrum
$I$, define

$$
h(I)=\bigl|\{i\notin I:\text{ there is an occurring spectrum }J
\text{ with }I\cup J\cup\{i\}=[6]\}\bigr|.
$$

Then

$$
\sum_{i=1}^6|T_i|=\sum_x h(I_x).
\tag{2}
$$

For an active point $x\in W$, a partner covering all six rows also covers any
five of them. Consequently

$$
h(I_x)=6-d(x)\qquad(x\in W).
\tag{3}
$$


A sufficient, but unproved, target for the lexicographically chosen tuple is

$$
\boxed{\quad \sum_i|T_i|\le6k-2w.\quad}
\tag{4}
$$

Indeed, (1) and (4) would give

$$
6t-6\le6k-2w\le6k-2t,
\qquad
t\le\frac{3k+3}{4}.
$$


Writing $L=\sum_xd(x)\le6k$, the exact identity behind a potentially stronger
form of (4) is

$$
\sum_i|T_i|-(L-2w)
=\sum_{x\in W}(8-2d(x))
 +\sum_{x\notin W}\bigl(h(I_x)-d(x)\bigr).
\tag{5}
$$

Thus nonpositivity of the right side would suffice. No argument makes it
nonpositive at a global lexicographic minimizer. It can be positive for
otherwise well-structured six-tuples, as the next example shows.

## A perfect matching does not supply the aggregate estimate

Fix a positive integer $a$, and partition the six row indices into sets
$X,Y$ of size three. Introduce disjoint point classes as follows:

- For each cross-pair $\{x,y\}$, with $x\in X$ and $y\in Y$, introduce
  $a$ points having spectrum $[6]\setminus\{x,y\}$.
- For each two-subset of $X$, and each two-subset of $Y$, introduce $2a$
  points having that two-subset as their spectrum.

Each row contains $6a$ points of degree four and $4a$ points of degree two,
so its size is

$$
k=10a.
$$

Every degree-four point is active: its missing cross-pair has a disjoint
cross-pair, and the corresponding two spectra cover all six rows. A degree-two
point is inactive. Its spectrum lies wholly in one part and cannot contain a
missing cross-pair, so it cannot cover all six rows together with a degree-four
point; two degree-two points also cannot cover six rows. Therefore

$$
W=\{\text{all degree-four points}\},\qquad w=9a.
$$


Fix $x\in X$. The active points outside row $x$ contribute $3a$ to
$T_x$. All degree-two points whose spectra lie in $Y$ contribute a further
$6a$: if such a spectrum contains $y$, a degree-four point missing
$\{x,y\}$ partners it to cover the other five rows. The only degree-two
spectrum contained in $X$ and missing $x$ is $X\setminus\{x\}$. It does
not participate in a cover of the other five rows: a degree-four partner misses
a cross-pair and would leave a $Y$-row uncovered, while a degree-two partner
cannot cover five rows. Hence

$$
|T_x|=9a.
$$

The same argument applies to every row, giving

$$
\sum_i|T_i|=54a
>42a=6k-2w.
\tag{6}
$$


The graph of missing pairs of the degree-four classes is $K_{3,3}$, which has
a perfect matching. Thus (6) disproves the proposed assertion that active degree
four together with a perfect matching of missing pairs ensures the aggregate
bound. In particular, the attempted intermediate claim $h(I)\le |I|$ for
inactive spectra under that hypothesis is false: an inactive two-subset of one
part has $h(I)=3>2$. The overlooked partners are active degree-four points.
**That perfect-matching lemma is withdrawn.**

This is an obstruction to the stated local estimate, not a counterexample to the
exchange method with further global information. The displayed family of six
rows itself has a two-point transversal. It is not asserted to be a
lexicographic minimizer in a high-transversal ambient family.

## An unconditional small-core shortcut also fails

There is a separate obstruction to claiming that every $P_7$ family admits six
reference rows with a small endpoint union, without a high-transversal or
normalization hypothesis.

Take nine row indices. For each four-subset $I\subseteq[9]$, introduce $a$
points with spectrum $I$, where $a\ge1$. Each row has size

$$
k=\binom83a=56a.
$$

Two points meet at most eight rows, so all nine rows have no two-cover. Any
eight rows can be partitioned into two four-subsets, whose point classes supply
a two-cover. Three points suffice for all nine rows: partition the indices into
three triples and extend each triple to a four-subset. Thus the nine-row family
is a minimal bad family, satisfies $P_8$ and hence $P_7$, and has
transversal number three.

Fix six of its rows, with index set $R$. A point with spectrum $I$ belongs
to their endpoint union exactly when $|I\cap R|\ge2$: its partner must contain
$R\setminus I$, and such a four-subset exists exactly in this range. An
inactive spectrum therefore contains all three omitted row indices and exactly
one index of $R$. There are six such spectra. The endpoint union consequently
has size

$$
\left(\binom94-6\right)a=120a.
$$

This is much larger than $3k/4=42a$. Repeated selections cannot improve it:
their set of distinct reference rows can be extended to six distinct rows, and
adding reference rows only shrinks the endpoint union.

The example refutes an unconditional endpoint-core lemma. Its transversal number
is only three, so it does not address the missing high-transversal normalization
needed for (4).

## Eight critical rows, even with pairwise intersection

The same limitation occurs for a minimum bad subfamily of size **eight**,
including under the degree-four six-row normalization.

For $a\ge1$, take six disjoint old classes $A_0,A_1,A_2,B_1,B_2,B_3$ of size
$2a$, a class $D$ of size $a$, and six private classes $P_{ij}$ of size $a$,
where $i\in\{1,2\}$ and $j\in\{1,2,3\}$. Set

$$
F=A_0\cup A_1\cup A_2\cup D,\quad
G=B_1\cup B_2\cup B_3\cup D,\quad
E_{ij}=A_i\cup\bigcup_{\ell\ne j}B_\ell\cup P_{ij}.
\tag{8}
$$

All eight edges have size $k=7a$ and are pairwise intersecting. There is no
two-cover. A pair of old points covering $F,G$ must use an $A$-class and a
$B$-class; a pair from $A_i,B_j$ misses $E_{3-i,j}$ for $i=1,2$, and a pair from
$A_0,B_j$ misses $E_{1j}$. An old point has degree at most five and a new point
degree at most two, so a pair involving a new point also cannot cover eight
rows.

Deleting any edge gives an old-point two-cover: use two different $B$-classes
after deleting $F$, the classes $A_1,A_2$ after deleting $G$, and $A_{3-i},B_j$
after deleting $E_{ij}$. Thus the family has $P_7$, transversal number three,
and is minimal without a two-cover.

For any six distinct rows, the two critical covers associated with the omitted
rows both cover those six. Their unordered class pairs are different and occupy
at least three old classes. Every point of each such class is a cover endpoint.
Hence

$$
|W_R|\ge6a=6k/7>3k/4.
$$

The bound also holds with repeated reference rows: extend the distinct
references to six rows, which can only shrink the endpoint union.

Equality is attained by omitting $G,E_{ij}$. The remaining six-row pair-cover
graph is exactly

$$
K_{A_{3-i},\,A_i\cup B_j},
$$

so its endpoint union has size $6a$. Its maximum point degree is four. For the
graph assertion, a cover must meet $F$. A point in $A_{3-i}$ covers $F$ and all
three mixed rows of that index, and its possible partners for the other two rows
are exactly $A_i\cup B_j$. A point in $A_i$ instead needs a partner in
$A_{3-i}$. Points in $A_0\cup D$ cannot be completed to a cover, and new private
points occur in only one row. This checks the asserted graph and degree bound.

Thus even global minimization of the endpoint union among degree-at-most-four
six-tuples does not yield the desired bound without using large ambient
transversal number.

### A restriction on a containing ambient family

If a rank-$k$ $P_7$ family $\mathcal H$ contains (8), it does satisfy

$$
\tau(\mathcal H)\le2a+\lceil7a/2\rceil
=11k/14+O(1).
\tag{9}
$$

Every two-cover of $F,E_{i1},E_{i2},E_{i3}$ uses a point of $A_i$. Indeed a
point meeting $F$ outside $A_i$ misses all three mixed rows, whose common
intersection is exactly $A_i$. Adjoining any three edges of $\mathcal H$
avoiding $A_i$ therefore forces those three edges to have a common point. This
residual is three-wise intersecting and has a transversal of size at most
$\lceil k/2\rceil$: otherwise partition one edge into two balanced parts and
choose an edge avoiding each, obtaining an empty triple intersection. Adding
$A_i$ proves (9).

This is an ambient restriction, not the required three-quarter estimate. The
general version of this argument works for four references whose every two-cover
meets their common intersection $C$, giving $\tau\le |C|+\lceil k/2\rceil$.

### Improving this particular ambient bound

The two residual families in that argument give the stronger bound

$$
\boxed{\tau(\mathcal H)\le
\left\lfloor\frac{37a+3}{7}\right\rfloor
=\frac{37}{49}k+O(1).}
\tag{10}
$$

This remains larger than $3k/4$ by $k/196+O(1)$.

Write $t=\tau(\mathcal H)$ and
$\mathcal H_i=\{E\in\mathcal H:E\cap A_i=\varnothing\}$.
As proved above, $\mathcal H_i$ is three-wise intersecting, and

$$
t-2a\le\tau(\mathcal H_i)\le\lceil7a/2\rceil.
\tag{11}
$$

If $t\le4a+1$, (10) is immediate for $a\ge1$. Otherwise set
$m=t-4a-1$. By (11), $1\le m\le2a$. Choose $S\subseteq B_1$ of
size $m$, and choose $H\in\mathcal H$ avoiding
$A_1\cup A_2\cup S$, whose size is $t-1$.

Put

$$
b_j=|H\cap B_j|,\qquad
p=|H\cap(P_{12}\cup P_{13}\cup P_{22}\cup P_{23})|.
$$

For $i\in\{1,2\}$ and $j\in\{2,3\}$, the edges $H,E_{ij}$
belong to $\mathcal H_{3-i}$. Their intersection is a transversal of
that three-wise intersecting family. Thus
$|H\cap E_{ij}|\ge t-2a$. Summing gives

$$
4b_1+2b_2+2b_3+p\ge4t-8a.
$$

The rank bound supplies $b_1+b_2+b_3+p\le7a$, so

$$
3b_1+b_2+b_3\ge4t-15a.
$$

On the other hand, $b_1\le2a-m=6a-t+1$ and $b_2+b_3\le4a$.
Consequently $4t-15a\le22a-3t+3$, proving (10).

These six residual-intersection inequalities alone still do not
force the three-quarter coefficient. In continuous units, put
$t=(21/4+\eta)a$, where $0\le\eta\le1/28$. The trace counts

$$
(b_1,b_2,b_3)=((3/4-\eta)a,2a,2a),\qquad
|H\cap P_{i2}|=|H\cap P_{i3}|=(1/2+2\eta)a,\quad
|H\cap P_{i1}|=0
$$

satisfy $|H\cap E_{ij}|\ge t-2a$ for all six references, and have
total size $(27/4+7\eta)a\le7a$. For rational $\eta$, denominators
can be cleared. This is only a feasible local trace profile, not a
construction of an ambient family. Further use of $P_7$ is needed.
