---
name: research/erdos_644/constant_composition_families
desc: An exact Hall formula and arbitrary-seed Fano coupling give a three-quarter bound, with seed-dependent additive error, for all constant-composition families.
tags: [proved, restricted-upper-bounds, constructions, finite-certificate]
sources: []
created: 2026-09-23T05:33:44Z
updated: 2026-10-14T00:26:52Z
---


# research/erdos_644/constant_composition_families

***

This page treats a class different from the uniform product layers in
[Arbitrary local layers](arbitrary_local_layers.md): the entire distribution of
local subsets is prescribed, rather than just their total cardinality. It gives
an exact transversal formula and a proved three-quarter bound, with
seed-dependent additive error, for every finite seed.

The conceptual proof in [Arbitrary-seed coupling](arbitrary_seed_coupling.md)
now establishes the polytope inclusion for every seed size. The earlier
three-point **exact rational computational certificate** is retained below
as an independent finite verification. No unrestricted reduction from
arbitrary uniform families has been established.

## 1. The family and its exact transversal number

Let $V$ be a finite seed of size $N$, and take $q$ disjoint, identified copies
$V_1,\ldots,V_q$. For each $I\subseteq V$, prescribe a nonnegative integer
$m_I$, with

$$
\sum_{I\subseteq V}m_I=q,
\qquad
k=\sum_{I\subseteq V}|I|m_I>0.
$$

Let $\mathcal H(q,m)$ consist of all subsets $E$ of the union of the copies
for which exactly $m_I$ blocks satisfy $E\cap V_j=I$. Thus the blocks may be
permuted arbitrarily, but every local state has a fixed multiplicity. Every
edge has size $k$.

For $D\subseteq V$ put

$$
h_D=\sum_{I:I\cap D=\varnothing}m_I.
$$

Then

$$
\boxed{\displaystyle
\tau(\mathcal H(q,m))
=\min_{\substack{\varnothing\ne D\subseteq V\\h_D<q}}
 |D|(h_D+1).}
\tag{1}
$$


For the upper bound, delete a copy of $D$ in $h_D+1$ blocks. An edge avoiding
these deletions would have to assign compatible states to all these blocks,
although only $h_D$ compatible state occurrences are available.

For the reverse bound, let $T$ be a transversal, and write $D_j=T\cap V_j$.
An edge avoiding $T$ is exactly a matching assigning the prescribed multiset of
local states to the $q$ block positions, with a state $I$ allowed at position
$j$ when $I\cap D_j=\varnothing$. Hall's theorem gives a set $U$ of positions
whose union of compatible states has total multiplicity less than $|U|$.
No $D_j$ for $j\in U$ is empty, since an empty deletion admits every state.
Choose $j_0\in U$ minimizing $|D_j|$, and put $D=D_{j_0}$. Then

$$
h_D<|U|\le q,
\qquad
|T|\ge\sum_{j\in U}|D_j|
\ge |D||U|\ge |D|(h_D+1).
$$

This proves (1).

Delete unused seed points, meaning points belonging to no state $I$ with
$m_I>0$. This changes neither the family nor its transversal number. Thereafter
$h_D<q$ for every nonempty $D$. With

$$
\alpha_I=m_I/q,\qquad
a=\sum_I|I|\alpha_I=k/q,\qquad
b=\min_{\varnothing\ne D\subseteq V}
 |D|\sum_{I:I\cap D=\varnothing}\alpha_I,
$$

formula (1) gives the useful exact-error bounds

$$
qb\le\tau(\mathcal H(q,m))\le qb+N.
\tag{2}
$$

In particular, $m_\varnothing=0$ implies $\tau\le N$.

## 2. The finite Fano coupling problem

Index seven rows by the nonzero vectors of $\mathbb F_2^3$. Let $\mathcal R$
be the downward closure of the seven Fano caps, where a cap is the complement
of a Fano line. For $S,T\in\mathcal R$,

$$
S\cup T\ne[7].
\tag{3}
$$

Indeed, their complements contain two Fano lines, which intersect. Consequently
a seven-row array whose every point-spectrum lies in $\mathcal R$ has no
two-point transversal.

For a local array of seven subsets $I_1,\ldots,I_7\subseteq V$ whose columns
belong to $\mathcal R$, take its empirical distribution

$$
\frac17\sum_{r=1}^7\delta_{I_r}.
$$

Let $P_N$ be the convex hull of these finitely many distributions. Any seven
edges of a constant-composition family that have all their point-spectra in
$\mathcal R$ give $\alpha\in P_N$, by averaging over their blocks.
Conversely, a rational $\alpha\in P_N$ has a rational convex decomposition;
repeating its local arrays and symmetrizing the rows by an order-seven Fano
automorphism realizes a bad seven-tuple at suitable multiples of the common
denominator. The rounding argument below removes this divisibility issue under
a strict transversal excess.

Here is a smaller sufficient polytope. For pairwise disjoint $I,J,K\subseteq V$
(empty states may repeat), put

$$
\Gamma(I,J,K)=\frac{4\delta_I+2\delta_J+\delta_K}{7},
\qquad
K_N=\operatorname{conv}\{\Gamma(I,J,K):I,J,K\text{ pairwise disjoint}\}.
\tag{4}
$$

Then $K_N\subseteq P_N$. To realize a generator, partition the seven rows into a
Fano cap $C_1$ of size four, a two-element subset $C_2$ of its complementary
line, and the remaining singleton $C_3$. Give the rows in these three classes
the states $I,J,K$, respectively. Every seed point has spectrum $C_1,C_2,C_3$,
or the empty set. Each lies in $\mathcal R$; for $C_2$, use the fact that a Fano
line avoids any prescribed pair of points.

Define the probability polytope

$$
Q_N=\left\{\alpha:\
\alpha_I\ge0,\ \sum_I\alpha_I=1,\quad
 |D|\sum_{I:I\cap D=\varnothing}\alpha_I
 \ge\frac34\sum_I|I|\alpha_I
 \quad(\varnothing\ne D\subseteq V)\right\}.
\tag{5}
$$

The stronger inclusion $Q_N\subseteq K_N$ is proved for every $N$ in
[Arbitrary-seed coupling](arbitrary_seed_coupling.md), by a conceptual
separation argument. In particular, a distribution with $b\ge3a/4$
belongs to $P_N$. The original verification for $N\le3$ follows.

## 3. The checked three-point polytope inclusion

**Finite lemma.** For $1\le N\le3$,

$$
\boxed{Q_N\subseteq K_N\subseteq P_N.}
\tag{6}
$$


Here are the full data for the nontrivial $N=3$ inclusion. Identify subsets
of the seed with bit masks $0,\ldots,7$, in the order

$$
\varnothing,\ 1,\ 2,\ 12,\ 3,\ 13,\ 23,\ 123.
$$

Write $\Gamma_{ijk}=\Gamma(i,j,k)$. The polytope $Q_3$ has 52 vertices,
in the following 16 orbits under permutations of the three seed points.
In the middle column, the displayed vector is divided by $d$.

| Orbit size | $d$ | Numerator vector of $\alpha$ | Convex decomposition |
|---:|---:|---|---|
| 6 | 10 | $(2,1,3,0,4,0,0,0)$ | $(2\Gamma_{200}+\Gamma_{402}+\Gamma_{001}+6\Gamma_{421})/10$ |
| 3 | 19 | $(4,2,6,0,6,0,1,0)$ | $(7\Gamma_{240}+7\Gamma_{420}+3\Gamma_{106}+2\Gamma_{061})/19$ |
| 3 | 28 | $(6,3,9,0,9,0,0,1)$ | $(3\Gamma_{241}+3\Gamma_{421}+2\Gamma_{007})/8$ |
| 6 | 9 | $(2,1,2,1,3,0,0,0)$ | $(3\Gamma_{214}+2\Gamma_{430}+\Gamma_{421}+3\Gamma_{043})/9$ |
| 3 | 13 | $(3,2,2,2,4,0,0,0)$ | $(2\Gamma_{340}+2\Gamma_{102}+3\Gamma_{210}+6\Gamma_{403})/13$ |
| 1 | 13 | $(3,3,3,0,3,0,0,1)$ | $(7\Gamma_{240}+10\Gamma_{142}+7\Gamma_{070}+2\Gamma_{421})/26$ |
| 6 | 11 | $(3,0,3,0,5,0,0,0)$ | $(3\Gamma_{204}+\Gamma_{420}+7\Gamma_{402})/11$ |
| 3 | 10 | $(3,0,3,0,3,0,1,0)$ | $(2\Gamma_{600}+9\Gamma_{240}+3\Gamma_{060}+6\Gamma_{402})/20$ |
| 3 | 29 | $(9,0,9,0,9,0,0,2)$ | $(12\Gamma_{400}+29\Gamma_{240}+10\Gamma_{042}+7\Gamma_{700})/58$ |
| 6 | 9 | $(3,0,1,2,3,0,0,0)$ | $(3\Gamma_{420}+8\Gamma_{042}+7\Gamma_{340})/18$ |
| 3 | 13 | $(5,0,0,4,4,0,0,0)$ | $(4\Gamma_{304}+3\Gamma_{430}+6\Gamma_{043})/13$ |
| 3 | 7 | $(3,0,0,0,4,0,0,0)$ | $\Gamma_{400}$ |
| 1 | 13 | $(7,0,0,2,0,2,2,0)$ | $(7\Gamma_{600}+7\Gamma_{500}+2\Gamma_{300}+10\Gamma_{030})/26$ |
| 3 | 5 | $(3,0,0,0,0,0,2,0)$ | $(2\Gamma_{600}+3\Gamma_{060})/5$ |
| 1 | 13 | $(9,0,0,0,0,0,0,4)$ | $(6\Gamma_{000}+7\Gamma_{700})/13$ |
| 1 | 1 | $(1,0,0,0,0,0,0,0)$ | $\Gamma_{000}$ |

The displayed decompositions can be checked by direct rational arithmetic. The
exhaustiveness of the vertex list is checked by
[`evidence/main.py`](evidence/main.py), using the
machine-readable version of this table in
[`evidence/assets/couplings.json`](evidence/assets/couplings.json).
The verifier requires only the Python standard library and the shared
failure harness.

For clarity, the enumeration is finite and exhaustive for the following reason.
There are eight nonnegativity inequalities and seven inequalities in (5), in
the affine space $\sum_I\alpha_I=1$ of dimension seven. The polytope has full
dimension there: taking every nonempty coordinate sufficiently small and
positive makes all inequalities strict. Every vertex therefore has seven
linearly independent active inequalities. The verifier examines all
$\binom{15}{7}=6435$ choices, solves each nonsingular system with exact rational
arithmetic, retains precisely its feasible solutions, and checks that the
result is exactly the 52 symmetry images in the table. It also checks every
coefficient, every disjointness condition in (4), and every convex identity.
This proves $Q_3\subseteq K_3$ by convexity.

For $N<3$, add unused seed coordinates. Summing the singleton inequalities in
(5) gives

$$
a\le\frac{4N}{3N+4}<\frac43.
$$

An inequality involving at least one old coordinate is preserved when unused
coordinates are added to its deletion set; an inequality involving only unused
coordinates has left side at least one and right side $3a/4<1$. Thus the
embedded distribution belongs to $Q_3$. In a convex decomposition furnished
by the table, no positive term can use an added coordinate, since its state
probability is zero. This proves $Q_N\subseteq K_N$ for $N<3$ as well.

## 4. Integral realization with a reserve of empty blocks

The following argument also explains why a strict asymptotic excess cannot
hide in divisibility or in local states of bounded multiplicity.

Assume unused seed points have been removed, and let $N\ge1$. Suppose

$$
\eta=b-\frac34a>0,
\qquad
\delta=\frac{\eta}{2(N+1)a}.
$$

Inflate every nonempty state probability by $1+\delta$:

$$
\beta_I=(1+\delta)\alpha_I\quad(I\ne\varnothing),
\qquad
\beta_\varnothing=1-\sum_{I\ne\varnothing}\beta_I.
\tag{7}
$$

This is a probability distribution. Indeed, writing
$p=1-\alpha_\varnothing\le a$, one has

$$
\delta p\le\delta a=\frac{\eta}{2(N+1)}
\le\frac{N\alpha_\varnothing}{2(N+1)}<\alpha_\varnothing,
$$

where $\eta\le b\le N\alpha_\varnothing$ follows by taking $D=V$.

For a nonempty $D$, its avoidance probability changes by minus
$\delta\Pr_\alpha(I\cap D\ne\varnothing)$. Therefore

$$
\begin{aligned}
|D|\Pr_\beta(I\cap D=\varnothing)-\frac34\mathbb E_\beta|I|
&\ge \eta-\delta(N+3/4)a\\
&\ge\eta/2>0.
\end{aligned}
\tag{8}
$$

Here $\Pr_\alpha(I\cap D\ne\varnothing)\le a$ was used. Hence $\beta\in Q_N$.

By the arbitrary-seed inclusion and Carathéodory's theorem, write

$$
\beta=\sum_{j=1}^{L}\lambda_j\Gamma_j,
\qquad L\le2^N,\quad\lambda_j\ge0,\quad\sum_j\lambda_j=1.
$$

Consequently

$$
\alpha=\frac1{1+\delta}\sum_j\lambda_j\Gamma_j
 +\frac{\delta}{1+\delta}\delta_\varnothing.
\tag{9}
$$


Each $\Gamma_j$ has a seven-block realization in which **each row** has local
state counts $7\Gamma_j$. Take the local construction following (4) and apply
all seven powers of an order-seven Fano automorphism to its row labels. For the
binary labels $1,\ldots,7$ used above, one such automorphism is the Singer cycle

$$
(1\ 2\ 4\ 3\ 6\ 7\ 5).
$$

It is multiplication by $x$ in $\mathbb F_2[x]/(x^3+x+1)$, so it preserves
the Fano lines and caps.

Use

$$
n_j=\left\lfloor\frac{q\lambda_j}{7(1+\delta)}\right\rfloor
$$

copies of this seven-block realization, filling all other positions initially
with empty blocks. For each nonempty state $I$, every row has the same integer
deficit

$$
d_I=m_I-\sum_j7n_j(\Gamma_j)_I\ge0.
$$

Moreover

$$
D_*:=\sum_{I\ne\varnothing}d_I<7L.
\tag{10}
$$

At least $q\delta/(1+\delta)$ blank blocks are available. A further seven-block
construction corrects one unit of any specified $d_I$: in block $r$ put $I$
in row $r$ and the empty state in the other six rows. Every point-spectrum is
a singleton, so it remains in $\mathcal R$. Each row gains exactly one
occurrence of $I$. Thus all deficits can be corrected using $7D_*<49L$ blank
blocks. All remaining blocks stay empty. Each row now has precisely the
prescribed composition $m$, while (3) excludes a two-point transversal.

In particular the construction works whenever

$$
\frac{q\delta}{1+\delta}\ge49\cdot2^N.
\tag{11}
$$


## 5. Consequence for the local seven-edge property

**Theorem.** Every constant-composition family with an $N$-point seed
and property $P_7$ satisfies

$$
\boxed{\tau(\mathcal H(q,m))\le\frac34k+C_N,\qquad
C_N=N+49\cdot2^N\bigl(2N(N+1)+1\bigr).}
\tag{12}
$$

In particular, $C_3=9803$. For every sequence of these families with
$k\to\infty$ and fixed $N$, or more generally $N^2 2^N=o(k)$,

$$
\limsup\frac{\tau}{k}\le\frac34.
$$

The composition may vary arbitrarily along the sequence.

If unused seed points were removed, apply the bound with their
remaining number $N'\le N$ and use $C_{N'}\le C_N$.

To verify the stated, nonoptimized constant, suppose
$\tau>3k/4+C_N$. Formula (2) implies

$$
q\eta=qb-3k/4>C_N-N.
$$

Also $a\le N$ and $\eta\le b\le1$, the latter by taking any singleton deletion.
Thus

$$
\frac{q\delta}{1+\delta}
=\frac{q\eta}{2(N+1)a+\eta}
\ge\frac{q\eta}{2N(N+1)+1}
>49\cdot2^N.
$$

The integral construction gives seven edges without a two-cover, contradicting
$P_7$. Repeated rows cause no problem: their underlying subfamily still has at
most seven edges and no two-cover. This proves (12).

The large additive constant is only a convenient rounding allowance. The
substantive finite statement is the arbitrary-seed polytope inclusion;
no claim of optimal additive error is made. This remains a restricted-class
theorem, since no local-property-preserving constant-composition completion
of arbitrary uniform families is known here.

## 6. An arbitrary-seed constraint and its limitation

If $b>3a/4$, every pairwise-intersecting family $\mathcal F$ of nonempty
states has probability mass $x=\alpha(\mathcal F)<4/7$. For $x>0$, choose a
minimum-size state $I\in\mathcal F$. Then $|I|\le a/x$, and a state disjoint
from $I$ cannot lie in $\mathcal F$. Consequently

$$
b\le |I|\Pr(J\cap I=\varnothing)\le\frac{a(1-x)}x,
$$

which implies the claim. These are necessary inequalities for $K_N$: a
disjoint triple contains at most one nonempty member of $\mathcal F$, with
coefficient at most $4/7$. They do not establish membership in $K_N$.

The singleton inequalities alone must not replace the full hypothesis. They
give $p_{\max}+3a/4\le1$, where $p_{\max}=\max_v\Pr(v\in I)$, but this
does not imply membership in $K_N$. On five points, put mass $1/100$ on the
whole seed, mass $99/500$ on each singleton, and zero on the empty state.
Then $a=26/25$, $p_{\max}=26/125$, and

$$
p_{\max}+3a/4=247/250<1.
$$

Any disjoint-triple template containing the whole seed has empty states in
its other two slots, so a convex combination with positive whole-seed mass
must also have positive empty mass. The displayed law is not in $K_5$.
It has $b=0$ and is not a counterexample to $Q_N\subseteq K_N$, or to either
assertion of Problem 644.
