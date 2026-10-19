---
name: research/erdos_644/arbitrary_local_layers
desc: A gcd residue correction extends the three-quarter product-layer bound to arbitrary finite local families, without heredity.
tags: [proved, constructions, restricted-upper-bounds]
sources: []
created: 2026-09-23T02:28:00Z
updated: 2026-09-24T22:12:53Z
---


# research/erdos_644/arbitrary_local_layers

***

This extends the [fixed-seed join-layer obstruction](join_layer_families.md)
from hereditary families to arbitrary finite local families. It does **not**
resolve either unrestricted assertion in Problem 644.

Let $V$ be a finite set, $N=|V|$, and let $\mathcal K\subseteq 2^V$ satisfy

$$
\varnothing\in\mathcal K,\qquad a=\max_{I\in\mathcal K}|I|\ge1.
$$

There is no assumption that $\mathcal K$ is hereditary. Put

$$
g=\gcd\{|I|:I\in\mathcal K,\ I\ne\varnothing\}.
$$

For positive integers $q,k$, take $q$ disjoint identified copies $V_1,\dots,V_q$
of $V$, and define

$$
\mathcal H_{q,k}(\mathcal K)=
\{A\subseteq V_1\sqcup\cdots\sqcup V_q:
 |A|=k,\ A\cap V_j\in\mathcal K\text{ for every }j\}.
$$

Here and below a block intersection is interpreted in the identified copy of
$V$. Write $P_7$ for the condition that every subfamily of at most seven edges
has transversal number at most two.

## Theorem

If $\mathcal H_{q,k}(\mathcal K)$ has $P_7$, then

$$
\boxed{\tau\bigl(\mathcal H_{q,k}(\mathcal K)\bigr)
\le \frac34k+\frac{51Na}{g}.}
\tag{1}
$$

In particular, for every fixed finite local family $\mathcal K$, every sequence
of its $P_7$ uniform product layers with $k\to\infty$ satisfies

$$
\limsup\frac{\tau(\mathcal H_{q,k}(\mathcal K))}{k}\le\frac34.
$$

More generally this holds for varying seeds whenever $Na/g=o(k)$.

The empty output family has transversal number zero, so assume henceforth that
$\mathcal H_{q,k}(\mathcal K)$ is nonempty. In particular $1\le k\le qa$ and
$g\mid k$.

## 1. A deletion upper bound that needs no heredity

For $D\subseteq V$ define

$$
r(D)=\max\{|I|:I\in\mathcal K,\ I\cap D=\varnothing\}.
$$

The maximum exists because the empty set belongs to $\mathcal K$. For
$0\le b\le a$ put

$$
\gamma(b)=\min\left\{
 \sum_{D\subseteq V}\lambda_D|D|:
 \lambda_D\ge0,\quad\sum_D\lambda_D=1,
 \quad\sum_D\lambda_Dr(D)\le b
 \right\}.
\tag{2}
$$

This is a nonincreasing convex function, $\gamma(a)=0$, and $\gamma(0)\le N$.
The last inequality can be strict: unlike the hereditary case, a set $D\ne V$
can meet every nonempty member of $\mathcal K$.

For the uniform product layer,

$$
\boxed{\tau(\mathcal H_{q,k}(\mathcal K))
 \le q\gamma(k/q)+2N.}
\tag{3}
$$

Indeed, an optimal extreme point in (2) has at most two positive coefficients.
If there are two, label their deletion sets $D_0,D_1$ so that
$r(D_0)\le r(D_1)$, and write $p$ for the coefficient of $D_1$. Use
$\lfloor qp\rfloor$ blocks of type $D_1$ and the other blocks of type $D_0$.
Rounding the larger-rank coefficient down makes the sum of surviving local ranks
at most $k$, and increases the total deletion cost by at most $N$. With just one
positive coefficient no rounding is required.

If the surviving rank sum is strictly less than $k$, the deletion set meets
every edge of the output family: every edge surviving all these deletions would
have its size bounded above by this rank sum. If the sum is exactly $k$, choose
a block of positive remaining rank and delete its remaining vertices. This costs
at most $N$ and reduces the rank sum strictly below $k$. Such a block exists
because $k\ge1$.

Only the implication

$$
\sum_jr(D_j)<k\quad\Longrightarrow\quad
D_1\sqcup\cdots\sqcup D_q\text{ is a transversal}
$$

was used. The converse, which can fail without heredity because of cardinality
gaps, is neither claimed nor needed.

## 2. The finite deletion inequality also needs no heredity

Choose $A_1\in\mathcal K$ of maximum size, then $A_2\in\mathcal K$ of maximum
size among members avoiding $A_1$, then $A_3\in\mathcal K$ of maximum size among
members avoiding $A_1\cup A_2$. These choices are possible because the empty set
is available. Write

$$
a_j=|A_j|,\qquad a_1=a\ge a_2\ge a_3\ge0,
$$

and put

$$
M=4a_1+2a_2+a_3,\qquad b_0=M/7.
\tag{4}
$$

Thus $4a\le M\le7a$ and $g\mid M$.

We claim

$$
\gamma(b_0)\le\frac34b_0.
\tag{5}
$$

Here is the complete deletion-LP argument. For $\lambda\ge0$ let

$$
m_\lambda=\min_{D\subseteq V}\bigl(|D|+\lambda r(D)\bigr).
$$

Finite linear-program duality gives

$$
\gamma(b)=\sup_{\lambda\ge0}\bigl(m_\lambda-\lambda b\bigr).
\tag{6}
$$

The three deletion choices $\varnothing,A_1,A_1\cup A_2$ give respectively

$$
m_\lambda\le\lambda a_1,
\qquad m_\lambda\le a_1+\lambda a_2,
\qquad m_\lambda\le a_1+a_2+\lambda a_3.
\tag{7}
$$

For $0\le\lambda\le1$,

$$
\frac{m_\lambda}{\lambda+3/4}
\le\frac{\lambda a_1}{\lambda+3/4}
\le\frac{4a_1}{7}\le b_0.
$$

For $\lambda\ge1$, successive use of (7) yields

$$
\begin{aligned}
7b_0
&\ge \left(4-\frac1\lambda\right)a_1
 +\left(2-\frac1\lambda\right)a_2
 +\frac{m_\lambda}{\lambda}\\
&\ge \left(4-\frac3\lambda+\frac1{\lambda^2}\right)a_1
 +\left(3-\frac1\lambda\right)\frac{m_\lambda}{\lambda}\\
&\ge \left(7-\frac4\lambda+\frac1{\lambda^2}\right)
 \frac{m_\lambda}{\lambda}.
\end{aligned}
\tag{8}
$$

All coefficients of $a_1,a_2$ used in these substitutions are nonnegative. With
$x=1/\lambda\in(0,1]$,

$$
\left(1-\frac47x+\frac17x^2\right)
\left(1+\frac34x\right)-1
=\frac{x(1-x)(5-3x)}{28}\ge0.
$$

Consequently (8) implies $m_\lambda\le(\lambda+3/4)b_0$ also in this range.
Substitution in (6) proves (5).

Every step uses only maxima over the given local family and disjoint greedy
choices. No subsets of a member of $\mathcal K$ were asserted to belong to
$\mathcal K$.

## 3. Explicit admissible seven-row spectra

Identify the seven row indices with $\mathbb Z/7\mathbb Z$. Let $\mathcal L$ be
the seven translates of $\{0,1,3\}$, and let $\mathcal C$ be the downward
closure of their complements.

The seven sets in $\mathcal L$ are the lines of a Fano plane. Directly, the six
differences of distinct elements of $\{0,1,3\}$ are the six nonzero residues
modulo seven, so each two translates meet. Therefore

$$
S\cup T\ne[7]\qquad(S,T\in\mathcal C).
\tag{9}
$$

Any seven-row incidence assignment whose every point-spectrum belongs to
$\mathcal C$ has no two-point transversal. This includes one-point covers by
taking $S=T$ in (9).

The collection $\mathcal C$ contains every singleton and every two-element set.
For the latter assertion, at most five of the seven Fano lines meet a given pair
(each point lies on three lines and the pair lies on one common line), so some
line avoids it.

There are two useful assignments, each occupying seven copies of the seed.

**Base assignment.** Partition the rows into a Fano cap $C_1$ of size four, a
pair $C_2$ of the three remaining rows, and their final singleton $C_3$. In one
seed block assign spectrum $C_j$ to each vertex of $A_j$, for $j=1,2,3$, and
assign the empty spectrum to the other vertices. The sets $A_1,A_2,A_3$ are
disjoint, so this is well-defined. Every row is exactly one of $A_1,A_2,A_3$,
and hence belongs to $\mathcal K$. Repeat this assignment in seven blocks, using
the seven cyclic translates of all spectra. Cyclic translation preserves
$\mathcal C$. Every row receives $A_1$ four times, $A_2$ twice, and $A_3$ once,
so every row has total size $M$.

**Cardinality correction assignment.** Given any nonempty $I\in\mathcal K$ of
size $d$, use seven blocks. In the block indexed by $h\in[7]$, assign spectrum
$\{h\}$ to every point of the copy of $I$, and assign the empty spectrum to the
other points. Every local row is either $I$ or the empty set, so belongs to
$\mathcal K$. Every row has total size $d$. All spectra remain in the same
collection $\mathcal C$.

Disjoint unions of these assignments, together with all-empty additional blocks,
still satisfy (9). No deletion of incidences is used.

## 4. Exact row cardinalities by a bounded residue correction

Let

$$
\mathcal D=\{|I|:I\in\mathcal K,\ I\ne\varnothing\},
\qquad L_0=M/g-1.
\tag{10}
$$

For every integer $k$ divisible by $g$, there is a sequence
$d_1,\dots,d_L\in\mathcal D$, with

$$
0\le L\le L_0,\qquad
r=d_1+\cdots+d_L\equiv k\pmod M,
\qquad 0\le r\le aL_0.
\tag{11}
$$

To prove this, divide all residues and generators by $g$ and work in the cyclic
group $\mathbb Z/(M/g)\mathbb Z$. The generators $d/g$ generate that group
because their gcd is one. Their nonnegative sums also generate it: in a finite
group the inverse of an element is a nonnegative multiple of the same element. A
shortest directed walk from zero to the desired residue has no repeated vertex,
so uses at most $M/g-1$ generators. Multiplying by $g$ proves (11).

Suppose now that $k\ge aL_0$. Choose (11) and put

$$
h=(k-r)/M\in\mathbb Z_{\ge0}.
$$

Take $h$ base assignments and $L$ cardinality correction assignments. Every row
then has size exactly $hM+r=k$, and each block restriction belongs to
$\mathcal K$. The number of occupied seed blocks is

$$
7h+7L
=\frac{7k}{M}+7L-\frac{7r}{M}
\le\frac{7k}{M}+7L_0.
\tag{12}
$$

If $q\ge7k/M+7L_0$, these assignments fit into the $q$ blocks. The remaining
blocks are assigned empty spectra. By (9), the resulting seven valid output
edges have no two-point transversal. Repeated rows, if any, may be removed
without changing that fact, so they give a forbidden subfamily of at most seven
distinct edges.

Consequently, if $P_7$ holds and $k\ge aL_0$, then

$$
\boxed{q-\frac{k}{b_0}<7L_0.}
\tag{13}
$$

This is the replacement for hereditary trimming.

## 5. Completion of the bound

First suppose $k\ge aL_0$, and write $b=k/q$. If $b\ge b_0$, monotonicity and
(5) give

$$
q\gamma(b)\le q\gamma(b_0)
\le\frac34qb_0\le\frac34k.
$$

If $b<b_0$, convexity between $0$ and $b_0$, the bound $\gamma(0)\le N$, and (5)
give

$$
q\gamma(b)
\le N\left(q-\frac{k}{b_0}\right)+\frac34k
<7NL_0+\frac34k.
$$

Together with (3), in either case

$$
\tau(\mathcal H_{q,k}(\mathcal K))
\le\frac34k+7NL_0+2N
\le\frac34k+\frac{51Na}{g}.
\tag{14}
$$

For the final inequality, use $L_0\le7a/g-1$ and $a/g\ge1$; the looser constant
51 is chosen to avoid any rounding issue.

If $k<aL_0$, use only the matching condition implied by $P_7$. There cannot be
three pairwise disjoint edges. A maximal matching therefore has at most two
edges, whose union is a transversal; hence $\tau\le2k$. Thus

$$
\tau-\frac34k\le\frac54k
<\frac54aL_0
\le\frac{35a^2}{4g}
\le\frac{51Na}{g},
$$

where $a\le N$. This proves (1) also in the remaining range.

## Scope

The result permits arbitrary local incidence patterns and arbitrary gaps among
the permitted local cardinalities. In particular the seed can be a nonlinear
finite code interpreted as a set family, with the all-zero codeword included. It
excludes constructions that repeat one fixed such local language independently
and then impose only a total-cardinality condition. It does not treat global
constraints coupling different copies, nor seeds growing so quickly that $Na/g$
is a positive fraction of the final uniformity.

The empty-set hypothesis is essential to the stated proof. It allows empty
remaining blocks, the local rows in cardinality correction assignments, and the
greedy choices when no nonempty member remains disjoint from earlier choices. A
fixed seed not containing the empty set has a simpler bounded transversal: any
whole block $V_j$ meets every output edge if every local member is nonempty, so
$\tau\le N$. Thus it too cannot give an asymptotic counterexample with fixed
$N$.
