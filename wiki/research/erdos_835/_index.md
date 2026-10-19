---
name: research/erdos_835
title: "Erdős 835: what a full Steiner partition forces"
desc: "The exact root-of-unity formulation of a full Steiner partition, its forced intersection counts, an explicit feasible two-point positive-semidefinite relaxation, and the unresolved compatibility of local large sets for prime k+1 at least 17."
problems:
- 835
created: 2026-10-15T11:10:09Z
updated: 2026-10-15T11:10:09Z
---

# Erdős 835: what a full Steiner partition forces

[[research/_index|..]]

***

This folder's results that are not drawn from a cited source are Plasma
AI's, author-recorded and not independently reviewed.

[[problems/set_systems/E0835/_index|Problem 835]] asks whether some
$k>2$ has $\chi(J(2k,k))=k+1$. As the
[[research/methods/steiner_color_partitions|Steiner-partition method page]]
shows, this means partitioning all $k$-subsets of a $2k$-set into $k+1$
Steiner systems $S(k-1,k,2k)$. Divisibility leaves exactly the $k$ with
$k+1$ prime, and then $k$ is even and every block's complement lies in its
own class. The problem page records the open cases as the $k>8$ with $k+1$
prime; this page concerns prime $k+1\ge17$. It tests
partition-level obstructions: arguments about how the $k+1$ classes fit
together, rather than only one design. The tested counts and two-point
relaxation do not exclude a prime $k+1\ge17$. The root-of-unity formulation
remains equivalent to the unresolved problem. No finite search was made.

Throughout, $p=k+1$ is prime, $k$ is even, and $V$ is the set of
$k$-subsets of $[2k]$. For a hypothetical proper coloring
$c:V\to\mathbb Z/p$ of $J(2k,k)$, write $F_a=c^{-1}(a)$ for its classes.
The two-point construction below does not assume a coloring exists.

## A root-of-unity vector in the top eigenspace

Put $\zeta=e^{2\pi i/p}$ and $f=\zeta^{c}$.

**Proposition 1.** A map $c:V\to\mathbb Z/p$ is a proper coloring if and
only if, for every $(k-1)$-set $T$,

$$
\sum_{y\notin T}f(T\cup\{y\})=0.
$$

Equivalently, $f$ lies in the top eigenspace $V_k$ of the Johnson scheme,
of dimension $\binom{2k}k-\binom{2k}{k-1}=\binom{2k}k/(k+1)$. Then every
power $f^m$ with $p\nmid m$ lies in $V_k$ as well.

*Proof.* The $k+1=p$ sets $T\cup\{y\}$ are pairwise adjacent, and
every edge of $J(2k,k)$ lies in such a star; so $c$ is proper exactly when
each star sees each residue once. If it does, the sum is the sum of all
$p$-th roots of unity, which is zero. Conversely, write the sum as
$\sum_an_a\zeta^a$ with $n_a\ge0$ and $\sum_an_a=p$. The only rational
linear relation among $1,\zeta,\ldots,\zeta^{p-1}$ is that their sum
vanishes, so a vanishing sum has all $n_a$ equal, hence all equal to one.
If $D$ is the inclusion map from $k$-sets to $(k-1)$-sets, then
$D^*D=kI+A$, where $A$ is the Johnson adjacency matrix: the diagonal
counts the $k$ subsets obtained by deletion and an adjacent pair has one
common deletion. Thus $\ker D$ is the eigenspace of eigenvalue $-k$,
denoted $V_k$ (highest degree, not largest eigenvalue).
For $p\nmid m$, the values of $f^m$ on each star are again all $p$-th
roots of unity. $\square$

So the question is whether the top eigenspace of $J(2k,k)$ contains a
vector whose entries are all $p$-th roots of unity. Membership in $V_k$
is a linear condition. Requiring each entry to lie in this particular
finite set is stronger than unimodularity and remains unresolved. Merely
finding a nonzero vector in $V_k$ does not pass this test.

## Every pair-level count is forced

**Proposition 2.** Let $B$ be a block of class $F_a$ and $0\le s<k$.
The number of blocks of $F_a$ meeting $B$ in exactly $s$ points is

$$
x_s=\frac{\binom ks\left(\binom ks+(-1)^sk\right)}{k+1},
$$

and for every other class $F_b$ the number of its blocks meeting $B$ in
exactly $s$ points is

$$
y_s=\frac{\binom ks\left(\binom ks-(-1)^s\right)}{k+1}.
$$

Both are nonnegative integers for every even $k$ with $k+1$ prime.

*Proof.* Each class is an $S(k-1,k,2k)$, so a $j$-set with $j<k$ lies in
$\lambda_j=\binom{2k-j}{k-j}/(k+1)$ of its blocks. For a class $F$ and a
fixed $k$-set $B$, let $N_s$ count the blocks of $F$ meeting $B$ in
exactly $s$ points. Counting pairs $(J,B')$ with $J\subseteq B\cap B'$
and $|J|=j$ gives $\sum_s\binom sjN_s=\binom kj\lambda_j$ for $j<k$, while
the $j=k$ count is $N_k=\mathbf 1_{B\in F}$. Inverting,

$$
N_s=\sum_{j=s}^{k-1}(-1)^{j-s}\binom js\binom kj\lambda_j
+(-1)^{k-s}\binom ks\mathbf 1_{B\in F}.
$$

The same inversion for the family of all $k$-sets, which has
$\lambda_j=\binom{2k-j}{k-j}$ and contains $B$, counts the
$\binom ks^2$ sets meeting $B$ in $s$ points. Hence the sum over $j<k$
equals $\bigl(\binom ks^2-(-1)^{k-s}\binom ks\bigr)/(k+1)$, which gives
$y_s$ when $B\notin F$ and $x_s=y_s+(-1)^s\binom ks$ when $B\in F$; here
$k$ is even. Since $\binom ks=\binom{p-1}s\equiv(-1)^s\pmod p$, both
numerators are divisible by $p$. Finally $\binom ks\ge k$ for
$0<s<k$, so both counts are nonnegative. $\square$

Thus any such partition is equitable for every relation "meeting in
$s$ points", with forced quotient matrices. In particular the adjacency
quotient is $k(J-I)$ and has the spectrum consistent with equality in
Hoffman's bound. The value $x_0=1$ gives complement closure, and
$x_1=y_0=0$. Integrality and nonnegativity of these counts do not show
that the classes exist. The following calculation gives a precise
limitation of a two-point relaxation, without claiming that every
possible condition involving pairs is satisfied.

## A feasible two-point relaxation

Let $N=\binom{2k}k$, and let $J_V$ denote the $N$ by $N$ all-ones
matrix. Define a real symmetric matrix on the entire $k$-layer by

$$
E(B,C)=\frac{(-1)^{|B\cap C|}}{p\binom{k}{|B\cap C|}}.
\tag{1}
$$

The [[theory/combinatorics/L153_johnson_pair_moments/_proof|projection calculation in L153]]
proves that this is the orthogonal projection onto $\ker D$ by downward
summation and binomial inversion. Its trace is $N/p$, which also proves
the dimension asserted in Proposition 1. This is an author-recorded
argument at tier 0.

Put $K=J_V/p+(p-1)E$. This matrix is positive semidefinite, has diagonal
one, and satisfies $0\le K(B,C)\le1$. Indeed its entry at intersection
size $s$ is

$$
K_s=\frac{1+k(-1)^s/\binom{k}s}{p}.
$$

At $s=0,k$ it is one; at other $s$ use $\binom{k}s\ge k$.
In particular $K_{k-1}=0$, as a proper coloring requires.

For every two vertices $B,C$ and colors $a,b$, prescribe formal moments

$$
M_{(B,a),(C,b)}=
\begin{cases}
K(B,C)/p,&a=b,\\
(1-K(B,C))/(p(p-1)),&a\ne b.
\end{cases}
\tag{2}
$$

By [[theory/combinatorics/L153_johnson_pair_moments/_index|L153's feasible pair moments]],
they are nonnegative, have uniform one-point marginals $1/p$, assign
zero to two different colors at one vertex, and assign zero to equal
colors at adjacent vertices. The full moment matrix, including a
constant coordinate, is positive semidefinite. Its covariance acts as
$E$ on each color direction perpendicular to the constant direction.

For a fixed color at $B$, summing the conditional moments over all $C$
with intersection size $s$ gives exactly $x_s$ for that color and $y_s$
for each other color, including the diagonal case. Thus the two-point
relaxation consisting of these marginals, edge exclusions, the forced
counts, entrywise nonnegativity and positive semidefiniteness is feasible
for every prime $p\ge3$. It cannot prove nonexistence in the remaining
regime. The moments need not be the moments of any distribution on
proper colorings; constructing such a distribution would solve the
problem. No assertion about stronger higher-point constraints follows.

## Every (k+3)-set carries a large set of triple systems

**Proposition 3.** Let $U\subseteq[2k]$ have $k+j$ points, $1\le j\le k$.
Map each $k$-subset of $U$ to its complement in $U$, a $j$-set. Then the
$k+1$ classes give a partition of all $j$-subsets of $U$ into $k+1$
Steiner systems $S(j-1,j,k+j)$, that is, a large set.

*Proof.* Two $k$-subsets of $U$ share $k-1$ points exactly when their
complements in $U$ share $j-1$ points. For a $(j-1)$-subset $Y$ of $U$,
the $k+1$ $j$-sets containing $Y$ have as complements the $k$-subsets of
the $(k+1)$-set $U\setminus Y$, which are pairwise adjacent. So their
colors are distinct and each color occurs once. $\square$

For $j=1$ and $j=2$ this says only that each $(k+1)$-set is rainbow and
that each $(k+2)$-set carries a one-factorization of $K_{k+2}$, which
exists because $k$ is even. For $j=3$ each $(k+3)$-set carries a large set
of Steiner triple systems on $k+3$ points.

For prime $p=k+1\ge17$, the order $k+3=p+2$ is congruent to $1$ or $3$
modulo $6$ and differs from $7$. Large sets of Steiner triple systems of
every such order exist, by the theorem of Lu Jiaxi (J. Combin. Theory
Ser. A 34 (1983) and 37 (1984)) completed by
[L. Teirlinck, *A completion of Lu's determination of the spectrum for
large sets of disjoint Steiner triple systems*, J. Combin. Theory Ser. A
57 (1991), 302–305](https://doi.org/10.1016/0097-3165(91)90053-J).
This classical theorem is used as an external premise; its proof is not
reconstructed here. The spectrum is stated in the publisher's indexed
abstract. Subject to that literature premise, existence on
one $(k+3)$-set gives no obstruction.
It supplies no compatibility among the choices on different sets.

## A parity count gives nothing

Fix a linear order of $[2k]$ and of $\mathbb Z/p$. For a $(k+1)$-set $S$
let $\beta_S:x\mapsto c(S\setminus\{x\})$, and for a $(k-1)$-set $T$ let
$\gamma_T:y\mapsto c(T\cup\{y\})$; both are bijections onto
$\mathbb Z/p$. Each edge $\{T\cup\{a\},T\cup\{a'\}\}$ of $J(2k,k)$, with
$a<a'$, is an inversion of exactly one of $\gamma_T$ and
$\beta_{T\cup\{a,a'\}}$: the first when $c(T\cup\{a\})>c(T\cup\{a'\})$,
the second otherwise. Hence the total number of inversions is the number
of edges, $\binom{2k}kk^2/2$, which is even for even $k$. The product of
all the signs is therefore $+1$, and this count gives no obstruction.

## What remains

The forced counts and the explicit two-point relaxation are feasible;
the parity identity is consistent. The local triple-system existence
theorem, used at its stated external standing, does not supply a
compatible global partition. The root-of-unity condition is an exact
reformulation, whose nonlinear requirement is still open. Possible
ways beyond these tests include:

- the restrictions of width $4\le j\le k$ in Proposition 3, beginning with
  large sets of Steiner quadruple systems on $k+4$ points, whose existence
  is not settled here;
- the compatibility among the local large sets on different $(k+3)$-sets,
  which share their triple systems through common $(k+2)$-subsets;
- the arithmetic of the root-of-unity vector of Proposition 1 beyond its
  membership in $V_k$.

No construction or analytic obstruction for these stronger requirements
is supplied here. This is the stopping point of the tested mechanism,
not an exclusion of other methods. No prime $k+1\ge17$ is settled here.
