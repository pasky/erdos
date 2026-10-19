---
name: research/erdos_963/half_size_reduction
title: 'Half-size dimension drop and a subset-sum code bound'
desc: An unproved sufficient induction, proved through size 2d+1, and an exact obstruction to ordered splitting.
tags: []
sources: []
created: 2026-09-19T01:37:39Z
updated: 2026-09-19T03:52:14Z
---


# Half-size dimension drop and a subset-sum code bound

***

The following sufficient assertion remains **unproved**:

> Every nonempty finite positive set $P$, with $n=|P|$ and $d=d(P)$,
> contains $C$ with
>
$$
> |C|\ge\lfloor n/2\rfloor,\qquad d(C)\le d-1.                 \tag{1}
>
$$


If (1) holds, induction on $d$, starting with the empty set, gives

$$
\lfloor n/2\rfloor\le |C|\le2^{d-1}-1,\qquad n\le2^d-1.
$$

Thus this would prove the positive-set form of Erdős 963. It is stronger
than a mere reformulation of the target: $C$ must be a subset of $P$.
Equivalently, the hypergraph of maximum dissociated subsets must have a
transversal of size at most $\lceil n/2\rceil$.

## A proved subset-sum code inequality

Suppose $Q$ has $n$ elements, $d(Q)=d<n$, every $d$-subset is
dissociated, and $n<2d+2$. Put

$$
M=\left\lfloor\frac{2(d+1)}{2(d+1)-n}\right\rfloor.
$$

Then

$$
\boxed{\binom n{d+1}\le (M-1)2^d.}                           \tag{2}
$$


This argument works in any abelian group. Partition the Boolean cube
$\{0,1\}^n$ by the value of its subset sum. Distinct vertices in a fiber
have Hamming distance at least $d+1$, since a closer pair would give a
relation supported on at most $d$ coordinates.

For a fiber of size $m$, the sum of the distances over unordered pairs
is at least $(d+1)m(m-1)/2$. In each coordinate at most $m^2/4$ pairs
differ. Therefore

$$
(d+1)m(m-1)/2\le nm^2/4,\qquad m\le M.
$$

The total number of unordered equal-sum pairs is consequently at most
$(M-1)2^{n-1}$.

Every $(d+1)$-subset has a ternary relation, necessarily of full support.
Choose one such relation for each support. Its two disjoint sides give
$2^{n-d-1}$ equal-sum pairs, by adjoining the same arbitrary subset of
the complementary coordinates to both sides. Pairs from different
supports are different because their symmetric differences differ.
Thus there are at least $\binom n{d+1}2^{n-d-1}$ pairs, proving (2).

At $n=2d$, inequality (2) says

$$
\binom{2d}{d-1}\le d2^d.
$$

This is false for $d=5$, since $210>160$, and remains false for all
larger $d$: the ratio of its left side to its right side is multiplied,
as $d$ increases by one, by $(2d+1)/(d+2)>1$. Hence, for $d\ge5$, a
$2d$-element set of dimension $d$ has a dependent $d$-subset.

## A parity argument for even dimensions

If $d$ is even, $d(P)=d$, and every $d$-subset is dissociated, then

$$
|P|\le d+1.                                                  \tag{3}
$$

Otherwise choose $d+2$ points. For each deletion of one point, choose a
relation on the other $d+1$ points; every coefficient on that support
is $\pm1$. The resulting square integer matrix has zero diagonal and
off-diagonal entries $\pm1$. Modulo two it is $J+I$.

Its order $d+2$ is even, so this matrix is invertible over $\mathbb F_2$:
an element of its kernel must be a constant vector, and substituting
that vector forces the constant to be zero. The integer matrix therefore
has nonzero determinant, contradicting the fact that the nonzero vector
of point values lies in its real kernel.

## Half-size drop through $n=2d+1$

Assertion (1) holds whenever $n\le2d+1$. For $n\le2d-1$, any
$\lfloor n/2\rfloor$ points suffice. For $n=2d$ or $2d+1$, it is enough
to find a dependent $d$-subset. The preceding two arguments handle even
$d$ and all $d\ge5$.

For $d=3$, suppose a positive set of size at least six had all triples
dissociated. Fix its three smallest elements $a<b<c$. Every later $x$
must make $\{a,b,c,x\}$ dependent, necessarily with full support.
Positivity and order leave only

$$
x=a+b+c\quad\hbox{or}\quad x=b+c-a.
$$

There are at most two later elements, a contradiction. The $d=1$ case
follows from the fact that any two distinct positive numbers are
dissociated.

Thus a failure of (1) requires $n\ge2d+2$. In a failure of minimum
cardinality, $n=2m$ is even, and the largest subset of dimension at most
$d-1$ has size exactly $m-1$. Indeed, deletion of one point cannot lower
$d$ (that would already provide a large enough subset). An odd-cardinality
minimal failure reduces by deletion to a smaller failure, while deletion
from an even-cardinality one supplies the claimed $(m-1)$-subset.

This does not close the induction: the minimum-distance argument above
requires all $d$-subsets to be dissociated, a hypothesis absent in the
remaining range.

## Ordered splitting is false

The stronger claim that two separated dissociated $d$-sets force dimension
$d+1$ is false. Take

$$
X=\{1,2,4\},\qquad Y=\{5,6,7\}.
$$

Both triples are dissociated and $\max X<\min Y$, but every four-subset
of their union is dependent. It contains one of

$$
\{1,4,5\},\ \{1,5,6\},\ \{1,6,7\},\
\{2,4,6\},\ \{2,5,7\},
$$

except for $\{1,2,4,7\}$ and $\{4,5,6,7\}$, which satisfy
$1+2+4=7$ and $4+7=5+6$. This refutes ordered splitting, not (1) or
the original target.

## Computation and the exact gap

Bounded checks found no failure of (1) among subsets of $[1,16]$ in
the first nontrivial $n=10,d=4$ regime, or in thirty prescribed
18-point samples. These are computational observations only and are
not used above. They do not establish a universal minimum over all
real configurations.

For a maximum-cardinality lower-dimensional subset $C$, every
$t\in P\setminus C$ extends some dissociated $(d-1)$-subset
$D_t\subset C$ to size $d$. The sets $D_t$ may vary with $t$.
No rank-preserving exchange proving $|P\setminus C|\le |C|+1$
has been established.

## Odd lifts of rank at least two admit a two-class drop

Let $P$ be represented in the free lattice $L=\langle P\rangle_{\mathbb Z}$
of rank $\rho$, preserving its ternary relations. Suppose there is a
character $\lambda:L\to\mathbb F_2$ with $\lambda(p)=1$ for every
$p\in P$. If $\rho\ge2$, then $P$ partitions into two nonempty
sets, both of dimension at most $d(P)-1$.

Choose $\chi\notin\{0,\lambda\}$. Both classes $P_0,P_1$ of $\chi$
are nonempty, because $P$ generates $L$. Adjoining any point of $P_1$
to a dissociated subset of $P_0$ preserves dissociation: applying
$\chi$ to a ternary relation first eliminates that one coefficient.
Thus $d(P_0)\le d(P)-1$. On $P$, the other class $P_1$ is the
kernel of $\chi+\lambda$, so the same argument proves its bound.
The larger class has size at least $\lceil |P|/2\rceil$.

In the intrinsic lift of a positive odd integer set, the odd evaluation
character descends, since every ternary relation has even support.
Therefore an odd counterexample to (1) must have intrinsic rank one,
without a minimal-dimension hypothesis. This is a special case, not a
solution of the primitive rank-one case.

## A binary-code restriction on half-size failures

More generally put

$$
b=\max\{|C|:C\subseteq P,\ d(C)\le d(P)-1\},
$$

and let $z$ be the number of columns that reduce to zero in $L/2L$.
Every nonzero character has a zero class of dimension at most $d(P)-1$,
by the same adjoining argument. Its evaluation word therefore has
weight at least $n-b$.

These words form a binary linear code of dimension $\rho$; the
evaluation map is injective because the columns generate $L$.
Delete its $z$ identically zero positions. Summing pairwise Hamming
distances, as in the proof of (2), gives

$$
2^\rho\le\frac{2(n-b)}{n-2b+z}
\quad\text{when }n-2b+z>0.                                 \tag{4}
$$

For an even-sized failure of (1), write $n=2m$; then $b\le m-1$.
Alternatively sum the weights of the nonzero evaluation words directly:
each nonzero column takes the value one on exactly $2^{\rho-1}$
characters. Hence

$$
(2^\rho-1)(m+1)\le2^{\rho-1}(2m-z),
$$

or

$$
m\ge2^\rho-1+2^{\rho-1}z.                                  \tag{5}
$$

In particular $2^\rho\le m+1$. These necessary restrictions do not
exclude the remaining rank-one, zero-free odd case.

### Residuewise strengthening

For an even failure $|P|=2m$, let $t_v$ be the multiplicity of a
residue $v\in L/2L$ and put $z=t_0$. Then

$$
\boxed{t_v\ge z+2\qquad(v\ne0).}                         \tag{6}
$$

Every nonzero character has a zero class of size at most $m-1$.
For fixed $v\ne0$ and $\rho\ge2$, sum this inequality over the
$2^{\rho-1}$ characters $\chi$ with $\chi(v)=1$. The residue zero
contributes $2^{\rho-1}z$, the residue $v$ contributes nothing, and
each other nonzero residue contributes half as often. Hence

$$
2^{\rho-2}(2m+z-t_v)\le2^{\rho-1}(m-1),
$$

which is (6). For $\rho=1$, it follows directly from $z\le m-1$.
Thus every nonzero residue occurs at least twice. Summing (6)
recovers (5), but (6) is stronger.

### Short presentations of every odd failure

An odd half-size failure has a rank-one short presentation, without
any minimal-dimension hypothesis. Let $R\subset\mathbb Z^P$ be
generated by genuine ternary relations supported on at most $d+1$
coordinates and set $H=\mathbb Z^P/R$. Then

$$
\dim_{\mathbb F_2}(H/2H)=1.                              \tag{7}
$$

The odd evaluation gives the all-ones character $\lambda$. If an
independent character $\chi$ existed, its two nonempty classes
would each have dimension at most $d-1$. For a dissociated $d$-set
in one class, adjoining a point from the other gives a short
relation. Applying $\chi$, or $\chi+\lambda$, forces the
adjoined coefficient to vanish, a contradiction. The larger class
would contradict half-size failure, proving (7).

The kernel calculation in [[research/erdos_963/parity_fibers|the parity-fiber
note]] now applies without minimality: $R$ has rational rank $|P|-1$ and odd
index in the primitive integer kernel. After normalizing the weights to gcd one,
if $h=\gcd\{x-y:x,y\in P\}$, then $h\le d-1$, and some short relation has
coefficient sum of valuation exactly $v_2(h)$. These necessary conditions still
do not handle primitive odd rank one.

## Limit of one attempted fixed-basis repair

The stronger proposal that some largest lower-dimensional $C$ has a
basis $D$ with $P\cap\operatorname{Span}_{\{-1,0,1\}}(D)=C$
was tested on

$$
P=\{1,2,8,10,11,13,14,15,16,17,19,20,21,24,25,27,28,29\}.
$$

The exact finite enumeration reported $d(P)=6$, a largest rank-five
subset of size $16$, and rank-five ternary closures of five-element
bases of size at most $15$. No portable certificate is retained here,
so this observation is not used as a proved obstruction or in any
argument above. The general half-size lemma remains unproved regardless.

## Cyclic windows: an unproved route and a graphic special case

A stronger sufficient assertion for positive odd sets would be:
some cyclic block of $\lfloor |P|/2\rfloor$ entries in numerical
order has dimension at most $d(P)-1$. Here a cyclic block is an
ordinary interval or a union of a prefix and a suffix.
No proof or counterexample to this assertion was obtained.
Sliding maximum dissociated subsets does not supply a valid exchange,
because their independence system is not matroidal.

The assertion is proved for generic positive scalar evaluations of
a bipartite graphic configuration $v_{uv}=e_u+e_v$. “Generic” means
that the scalar evaluation creates no new ternary relations or
coincidences. Dissociated sets of these columns are exactly forests:
bipartite cycles have alternating ternary relations, and forests
are linearly independent. Thus dissociation dimension is graphic rank.

Write the edge heights as $\alpha_u+\beta_v$. Suppose both sides
of an ordered cut had the original graphic rank. Each side would
then span every connected component of the original graph. In a
nontrivial component choose $u_*$ maximizing $\alpha_u$ and $v_*$
minimizing $\beta_v$. A lower-side edge incident to $u_*$ has height
at least $\alpha_{u_*}+\beta_{v_*}$, while an upper-side edge
incident to $v_*$ has height at most that value. This contradicts
the strict ordering of the cut.

Apply this at the middle cut. One side has smaller rank; if its
size is $\lceil |P|/2\rceil$, take a consecutive
$\lfloor |P|/2\rfloor$-subset of it. This proves the window
assertion in this graphic case, without requiring oddness.
It does not address the primitive rank-one case left open above.
