---
name: research/erdos_644/polarized_blocker_powers
desc: Exact parameters and explicit local obstructions for standard polarized powers of complete-family blockers.
tags: [proved, amplification, method-obstruction]
sources: []
created: 2026-09-22T22:03:21Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/polarized_blocker_powers

***

This page analyzes another possible transversal amplification. Starting with a
complete uniform family, the construction multiplies its transversal number by
an arbitrary integer. However, an explicit Fano-pattern obstruction shows that
every asymptotically large output with power at least two preserving the
seven-edge local property has transversal-to-rank ratio at most $4/7+o(1)$. Thus
this construction cannot improve the complete-family coefficient $3/4$, and it
does not prove the general convergence assertion in
[Problem 644](../../problems/set_systems/E0644/_index.md).

Everything below is stated in terms of finite set families; no commutative
algebra results are needed. Write $P_r$ for the condition that every subfamily
of **at most** $r$ edges has a transversal of size at most two. As usual, for a
family with at least $r$ edges this is equivalent to checking exactly $r$
distinct edges.

## Prefix families and their blockers

Fix integers $1\le k\le n$ and $m\ge1$, and put

$$
t=n-k+1,\qquad M=m(k-1)+1.
$$

The ground set is

$$
U=[n]\times[m].
$$

For an integer vector $a\in\{0,\ldots,m\}^n$, define its prefix set

$$
P(a)=\{(i,j):1\le j\le a_i\}.
$$

Let

$$
\mathcal G_{n,t,m}
=\{P(a):a\in\{0,\ldots,m\}^n,\ \textstyle\sum_i a_i=mt\},
\tag{1}
$$

and let $\mathcal K_{n,k,m}$ be its **blocker**, the family of all
inclusion-minimal transversals of $\mathcal G_{n,t,m}$.

At $m=1$, the family in (1) consists of all $t$-subsets of $[n]$, and its
blocker consists of all $k$-subsets. For comparison with the algebraic operation
motivating this construction, let $B$ be the squarefree monomial ideal generated
by the $t$-subsets. The exponent vectors of the degree-$mt$ monomials in $B^m$
are exactly the vectors in (1); standard polarization replaces each monomial by
its prefix set. Thus $\mathcal K_{n,k,m}$ is the hypergraph obtained by taking
the Alexander dual after standard polarization of $B^m$.

The assertion about exponent vectors is elementary. Given $a\in\{0,\ldots,m\}^n$
of sum $mt$, at least $t$ coordinates are positive and at most $t$ coordinates
equal $m$. Choose $t$ positive coordinates containing all those equal to $m$,
and subtract their incidence vector. The result has coordinates at most $m-1$
and total $(m-1)t$. Induction decomposes $a$ into $m$ incidence vectors of
$t$-subsets.

## Exact transversal number and rank

Give clone $(i,j)$ the positive integer weight

$$
w(i,j)=m-j+1.
$$


**Covering criterion.** Every inclusion-minimal transversal of
$\mathcal G_{n,t,m}$ contains at most one clone from each original index $i$.
For a set $T$ satisfying that restriction,

$$
T\text{ is a transversal of }\mathcal G_{n,t,m}
\quad\Longleftrightarrow\quad
w(T)\ge M.
\tag{2}
$$

It is inclusion-minimal precisely when

$$
w(T)\ge M
\quad\text{and}\quad
w(T)-\min_{x\in T}w(x)<M.
\tag{3}
$$


**Proof.** If $j<j'$, every prefix set containing $(i,j')$ also contains
$(i,j)$. Thus a transversal containing both may discard $(i,j')$.

Suppose now that at most one clone per index is selected. Avoiding a selected
clone $(i,j)$ restricts $a_i$ to $0\le a_i\le j-1$; an unselected index retains
its upper bound $m$. Consequently the maximum possible sum of an exponent vector
whose prefix avoids $T$ is

$$
mn-w(T).
$$

Every integer total between zero and that maximum is achievable under these
coordinate bounds. Therefore an edge of (1) avoids $T$ exactly when
$mn-w(T)\ge mt$. Taking the complementary integer inequality gives (2). Checking
the deletion of each selected point gives (3). $\square$

**Theorem.** For all $n,k,m$ in the stated range,

$$
\boxed{\quad
\tau(\mathcal K_{n,k,m})=m(n-k+1),
\qquad
\operatorname{rank}(\mathcal K_{n,k,m})
=\min\{n,m(k-1)+1\}.
\quad}
\tag{4}
$$


**Proof of the transversal formula.** More generally, if $\mathcal G$ is a
finite nonempty uniform family and $b(\mathcal G)$ denotes its blocker, a set
$S$ meets every member of $b(\mathcal G)$ exactly when it contains an edge of
$\mathcal G$. One implication follows because every transversal of $\mathcal G$
meets each of its edges. For the converse, if $S$ contains no edge, its
complement is a transversal of $\mathcal G$ and contains an inclusion-minimal
transversal disjoint from $S$.

Applying this to the $mt$-uniform family (1) gives
$\tau(\mathcal K_{n,k,m})=mt$. This argument is also the usual elementary proof
of blocker involution for a family with no edge containing another.

**Proof of the rank formula.** The covering criterion gives the upper bound $n$.
It also gives the upper bound $M$: if a transversal has more than $M$ points,
any $M$ of them have total weight at least $M$, so the original transversal is
not inclusion-minimal.

If $M\le n$, choose $M$ different indices and their level-$m$ clones, all of
weight one. This is a minimal transversal of size $M$. If $M>n$, use one clone
from every index, with weights in $[1,m]$ summing to $M$. Such weights exist
because $n\le M\le mn$. The total weight is exactly $M$, so the resulting
transversal is minimal. This attains the other upper bound. $\square$

### Private padding does not improve the local property

The outputs in (4) need not be uniform. They may be padded to their rank $R$ by
giving each edge $E$ its own disjoint set of $R-|E|$ new private points. This
preserves the transversal number of **every** subfamily: a private point in a
transversal may be replaced by any original point of its unique edge, without
increasing the number of chosen points. Conversely an original transversal
remains a transversal after padding. Thus padding preserves both the global
transversal number and failure of any $P_r$.

## A uniform Fano obstruction for every power $m\ge2$

**Theorem.** For $m\ge2$,

$$
\boxed{\quad
m(n-k+1)\ge4\lceil n/7\rceil+1
\quad\Longrightarrow\quad
\mathcal K_{n,k,m}\text{ fails }P_7.
\quad}
\tag{5}
$$

The conclusion is uniform in $m$; the power is allowed to grow with $n$ and $k$.

**Proof.** Label seven rows by $\mathbb Z/7\mathbb Z$. For every type
$i\in\mathbb Z/7\mathbb Z$, partition the row labels into

$$
C_i=[7]\setminus\{i,i+1,i+3\},
\qquad Q_i=\{i,i+1\},
\qquad R_i=\{i+3\},
\tag{6}
$$

where $[7]$ here denotes the seven cyclic labels. The sets complementary to
$C_i$ are the seven Fano lines. Any two of them intersect: the differences
between elements of $\{0,1,3\}$ include every nonzero residue modulo seven.
Hence two sets $C_i,C_j$ never have union $[7]$.

Assign a type to each of the $n$ original indices, using $\lfloor n/7\rfloor$
complete cycles of the seven types followed by a partial cycle with distinct
types. At an original index of type $i$, assign the following incidence spectra
among seven prospective rows:

- the level-one clone has spectrum $C_i$;
- the level-two clone has spectrum $Q_i$;
- if $m\ge3$, the level-three clone has spectrum $R_i$;
- all remaining clone levels have empty spectrum.

When $m=2$, the singleton spectrum $R_i$ is omitted. At each original index,
every row contains at most one clone. Let $A_h$ be the clone set in row $h$.

No two clone points meet all seven rows. Two level-one spectra fail because two
Fano caps do not cover $[7]$. Every other pair includes a spectrum of size at
most two and has union of size at most six.

Relative to the maximum weight $m$ available at an original index, the weight
deficit in row $h$ is zero, one, or two according as $h\in C_i,Q_i,R_i$. This
remains true for $m=2$, because a row in $R_i$ then selects no clone and has
weight zero. In each complete cycle of the seven types, every row belongs to two
of the pairs $Q_i$ and one of the singletons $R_i$, so its total deficit is
four. A partial cycle contributes at most four, since all deficits are
nonnegative and the complete cycle contributes four. Therefore

$$
w(A_h)\ge mn-4\lceil n/7\rceil
\qquad(h\in[7]).
$$

The hypothesis of (5) implies

$$
w(A_h)\ge mn-m(n-k+1)+1=M.
$$

By (2), every $A_h$ is a transversal of $\mathcal G_{n,t,m}$. Choose an
inclusion-minimal transversal $E_h\subseteq A_h$ in each row. These $E_h$ are
edges of $\mathcal K_{n,k,m}$. Deleting incidences cannot create a two-point
transversal, so they still have no such transversal. If some rows coincide,
remove repetitions; the resulting bad subfamily has at most seven distinct
edges. $\square$

**Corollary.** If $n\ge3$, $m\ge2$, and $\mathcal K_{n,k,m}$ has $P_7$, then

$$
\operatorname{rank}(\mathcal K_{n,k,m})=n,
\qquad
\tau(\mathcal K_{n,k,m})\le4\lceil n/7\rceil.
\tag{7}
$$

In particular, any sequence of such outputs with ranks tending to infinity
satisfies

$$
\frac{\tau(\mathcal K_{n,k,m})}
{\operatorname{rank}(\mathcal K_{n,k,m})}
\le\frac47+o(1).
\tag{8}
$$

The same statements apply after private padding to the rank.

**Proof.** The transversal bound is the contrapositive of (5). If instead the
rank in (4) were $M<n$, then

$$
m(n-k+1)=mn-M+1\ge(m-1)n+2\ge n+2.
$$

For every $n\ge3$, one has $n+2>4\lceil n/7\rceil$, contradicting the
transversal bound. This proves (7), and (8) follows immediately. $\square$

## The tempting square has an explicit four-edge obstruction

Take

$$
n=7q-1,\qquad k=4q,\qquad m=2,\qquad q\ge1.
$$

The complete seed has $P_7$, and (4) gives

$$
\tau(\mathcal K_{7q-1,4q,2})=6q,
\qquad
\operatorname{rank}(\mathcal K_{7q-1,4q,2})=7q-1.
$$

The apparent coefficient $6/7$ is therefore tempting. Nevertheless, this output
fails even $P_4$ for every $q\ge1$.

To check the seed property directly, any seven seed edges have total incidence
$28q>4(7q-1)$, so some point meets at least five of them. Any two seed edges
intersect, since $2k>n$, and a second point covers the at most two remaining
rows.

For the obstruction in the output, partition the original indices into $P,A,B,C$
of sizes

$$
|P|=q,\qquad |A|=2q-1,\qquad |B|=|C|=2q,
$$

and fix $u\in P$. Use subscripts $\ell$ and $h$ for levels one and two, of
weights two and one. Consider

$$
\begin{aligned}
E_0&=P_\ell\cup(A\cup B\cup C)_h,\\
E_1&=(A\cup B)_\ell\cup\{u_h\},\\
E_2&=(A\cup C)_\ell\cup\{u_h\},\\
E_3&=(B\cup C)_\ell.
\end{aligned}
\tag{9}
$$

Here $M=8q-1$. The first three sets in (9) have weight exactly $M$, and hence
are minimal transversals by (3). The fourth has weight $8q=M+1$, but all its
points have weight two, so deleting any point drops its weight below $M$. It too
is an edge of $\mathcal K_{7q-1,4q,2}$.

Now $E_0$ is disjoint from each of $E_1,E_2,E_3$, while

$$
E_1\cap E_2\cap E_3=\varnothing.
$$

A two-point transversal would need one point in $E_0$ and a second point common
to the other three edges, which is impossible. Private padding cannot remove
this obstruction.

## Genuine polarizations in a fixed number of variables

There is a separate obstruction to **unbounded amplification of one fixed seed**
by any genuine polarization, including nonstandard ones. This does not give the
preceding $4/7$ bound for nonstandard polarizations when the seed also varies.

Let $I_m$ be proper nonzero monomial ideals in a polynomial ring with $n$
variables, where $n$ is fixed. Suppose their least minimal-generator degrees
$d_m$ tend to infinity. Let $J_m$ be any squarefree polarization, in the sense
that identifying the clone variables is quotienting by a regular sequence of
linear forms on the quotient ring and recovers $I_m$. Let $\mathcal K_m$ be the
blocker of the minimal-generator supports of $J_m$. Then

$$
\tau(\mathcal K_m)=d_m,
\qquad \operatorname{rank}(\mathcal K_m)\le n.
\tag{10}
$$


The first equality follows from blocker involution, also for nonuniform
clutters: a set meets every minimal transversal exactly when it contains an
original edge. For the rank assertion, the minimal primes of the squarefree
monomial ideal $J_m$ correspond to its minimal transversals, with prime height
equal to transversal size. Each such height is at most
$\operatorname{pd}(S'/J_m)$. Indeed, localizing at a minimal prime gives a
nonzero zero-dimensional module over a regular local ring; the
Auslander--Buchsbaum formula gives projective dimension equal to that prime's
height, and localization cannot increase projective dimension.

The regular-sequence condition for polarization gives

$$
\operatorname{pd}(S'/J_m)=\operatorname{pd}(S/I_m)\le n.
$$

For the equality, tensor a minimal free resolution with the quotient by the
identifying linear forms: regularity makes it exact, and its differentials still
have entries in the homogeneous maximal ideal, so it remains minimal. The last
inequality is Hilbert's syzygy theorem. This proves (10).

For the at-most-$r$ convention, $P_r$ with $r\ge3$ forces matching number at
most two. A maximal matching in a rank-$n$ hypergraph gives a transversal of
size at most $2n$. Therefore the families in (10) fail $P_r$ whenever $d_m>2n$.
For the exactly-$r$ convention, the same conclusion holds when
$d_m>\max\{2n,r-1\}$, since then $|\mathcal K_m|\ge\tau(\mathcal K_m)=d_m\ge r$.

In particular, changing the polarization of powers of a fixed blocker cannot
yield an unbounded $P_r$ amplifier. A construction outside this obstruction
would have to abandon the regular-sequence polarization condition or introduce a
number of base variables growing with the amplification parameter. No such
construction preserving $P_r$ and the required ratio was obtained.

## Scope of the obstruction

The explicit $4/7$ bound concerns the prefix family (1), or equivalently
**standard** polarization of powers of the blocker of a **complete** seed
family. Equation (10) separately excludes unbounded powers in a fixed number of
variables under any genuine polarization. Neither argument excludes all
nonregular squarefree lifts, constructions with growing base rings, or other
nonconvex amplifications. They provide no inequality establishing convergence of
$f(k,r)/k$, and both assertions of Problem 644 remain unresolved here.
