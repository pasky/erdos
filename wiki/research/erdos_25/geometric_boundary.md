---
name: research/erdos_25/geometric_boundary
desc: Boundary-supported defects and a sufficient local reciprocal criterion, with a primitive natural-density example showing that the criterion need not hold anywhere.
tags: [density, profinite-geometry, partial-results]
sources: []
created: 2026-09-22T04:28:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/geometric_boundary

***

Write $G=\widehat{\mathbb Z}$, $C_q=[a_q]_q$,
$U=\bigcup_q C_q$, and $K=G\setminus U$. The Haar measures are
$\beta=\mu(U)$ and $\delta=\mu(K)$. The actual excluded set is
$$
 B=\{n\ge1:\exists q\le n,\ n\equiv a_q\pmod q\}.
$$
The boundary model below does not alone settle the problem. It does
give a sufficient condition for **natural** density, uniform under
common profinite affine transformations of the residues.

## Location of a possible logarithmic defect

The ambient measures
$$
 \lambda_X=\frac1{H_{\lfloor X\rfloor}}
       \sum_{n\le X}\frac1n
       \delta_{(\log n/\log X,\,n)}
$$
on $[0,1]\times G$ converge weakly to $dt\,d\mu$.
For a fixed residue class modulo $L$ and $0\le s<t\le1$, harmonic
summation between $X^s$ and $X^t$ gives the required mass
$(t-s)/L+o(1)$. Finite unions of such product sets, or approximation
of continuous functions by them, prove the assertion.

Replace the sum by its restriction to $n\in B$, obtaining $\lambda_X^B$.
Every subsequential weak limit $\lambda^B$ has the form
$$
 d\lambda^B
 =\mathbf1_U(z)\,dt\,d\mu(z)
   +\rho(t,z)\mathbf1_{\partial U}(z)\,dt\,d\mu(z),
 \qquad0\le\rho\le1.
 \tag{1}
$$
Indeed $0\le\lambda_X^B\le\lambda_X$ implies domination of the limit
by $dt\,d\mu$. Every compact subset of $U$ is covered by a fixed
finite set of cylinders. Away from $t=0$, these are all active for
large $X$, so the limit agrees with the ambient measure on
$[0,1]\times U$. No deleted integer lies in $G\setminus\overline U$;
open-set approximation makes the limit zero there. The slice $t=0$
has zero ambient measure. These observations prove (1).

In particular, a positive discrepancy from $\beta$ requires
$\mu(\partial U)>0$. If $\mu(\partial U)=0$, the analogous ordinary
counting argument already gives natural density. Formula (1) locates
the possible defect; it does not prove that $\rho=0$.

## A local reciprocal criterion

Define the closed set
$$
 D=\left\{x\in G:\ \text{for every }L\ge1,
       \sum_{\substack{q\,:
        a_q\equiv x\pmod{(q,L)}}}\frac1q=\infty\right\}.
 \tag{2}
$$
The compatibility condition in the sum is exactly
$C_q\cap[x]_L\ne\varnothing$. The complement of $D$ is open:
a clopen fiber witnessing convergence does so for all its points.
On any such fiber, only a reciprocal-summable collection of classes
can contribute. The ordinary activated union bound therefore gives
finite-periodic approximation on that fiber. In (1), the defect is
consequently supported on $[0,1]\times(K\cap D)$ as well.

**Theorem.** If $\mu(K\cap D)=0$, the delayed survivor set has natural
density $\delta$. Convergence is uniform when all residues are changed
simultaneously by
$$
 a_q\longmapsto ua_q+z\pmod q,
 \qquad u\in\widehat{\mathbb Z}^{\times},\quad
 z\in\widehat{\mathbb Z}.
 \tag{3}
$$

**Proof.** Given $\varepsilon>0$, choose a clopen
$O\supset K\cap D$ with $\mu(O)<\varepsilon$.
The compact set $K\setminus O$ has a finite cover by clopen fibers
whose intersecting cylinder families have convergent reciprocal sums.
Their union $V$ satisfies
$$
 \sum_{q:C_q\cap V\ne\varnothing}\frac1q<\infty.
$$
The compact set $W=G\setminus(O\cup V)$ is contained in $U$, so a
finite prefix, with moduli at most $Q_0$, covers $W$.
Choose $Q\ge Q_0$ such that
$$
 \sum_{\substack{q>Q\,: C_q\cap V\ne\varnothing}}\frac1q
 <\varepsilon,\qquad \beta-\mu(U_{\le Q})<\varepsilon.
$$
Every actual deletion outside the prefix has a witnessing modulus
$q>Q$. It cannot lie in $W$, since $n\ge q>Q_0$ makes the old
covering class there active. If $P$ is a period of $O$, then
$$
 |(B\setminus B_{\le Q})\cap[1,N]|
 \le \mu(O)N+P+
 N\sum_{\substack{q>Q\,: C_q\cap V\ne\varnothing}}\frac1q
 \le2\varepsilon N+P.
 \tag{4}
$$
The bound $N/q$ per class is exact for delayed classes; there is no
accumulated inactive-root error. Finite-prefix counting and (4) prove
natural density $\beta$ for $B$.

Under (3), transport $O,V,W$ by $x\mapsto ux+z$. Their measures,
periods, cylinder intersections, and reciprocal sums are unchanged.
The finite-prefix counting error is uniform over these transformations,
as is (4). Thus the conclusion is uniform in $(u,z)$. $\square$

## A noncoherent example with unbounded prime rank

Let $R_j$ be the product of the first $j$ odd primes and set
$M_j=2^{2j}R_j$. Choose $c_j\pmod{M_j}$ with
$$
 c_j\equiv2^{2j-1}\pmod{2^{2j}},\qquad c_j\equiv0\pmod{R_j}.
$$
The cylinders $W_j=[c_j]_{M_j}$ are pairwise disjoint. For every $j$
and every prime $p\nmid M_j$, use modulus $M_jp$, with residue $c_j$
modulo $M_j$ and any chosen residue modulo $p$. All moduli are
distinct: their $2$-adic valuations distinguish different $j$, and
within a fixed $j$ the prime $p$ distinguishes them. They can therefore
be enumerated strictly increasingly.

For a fixed $j$, independent prime coordinates and
$\sum_{p\nmid M_j}1/p=\infty$ show that these classes cover $W_j$
almost everywhere. Hence
$$
 \beta=\sum_{j\ge1}\frac1{M_j}<\frac13.
$$
Moreover
$$
 D\subseteq\bigcup_j W_j\ \cup\ \{x:x_2=0\}.
$$
To see this, a point of finite $2$-adic valuation can have a neighborhood
meeting only its matching $W_j$, if there is one. If it is outside
that $W_j$, refine the neighborhood to avoid it too. The last displayed
$2$-adic zero set is Haar-null, and $K\cap W_j$ is null for each $j$.
Thus the theorem gives natural density $1-\sum_j1/M_j$, uniformly
under (3). The reciprocal sum diverges, the survivor density is
positive, and both modulus prime rank and pairwise-gcd prime rank are
unbounded. The residues need not be coherent.

The geometric argument permits multi-residue families as well, with
reciprocal sums counting congruence pairs with multiplicity. The next
example shows that its local reciprocal hypothesis is not automatic,
even for primitive zero-residue singleton families whose natural density
exists.

## Positive natural density with $D=G$: proved obstruction

For every $0<\varepsilon<1$, there is a primitive family of distinct
zero-residue moduli such that
$$
 \mu(K)>1-\varepsilon,\qquad D=G,\qquad\partial U=K,
 \tag{5}
$$
and the original delayed survivor set nevertheless has natural density
$\mu(K)$. Thus positive survivor measure, primitivity, and even actual
natural-density existence do not force local reciprocal summability on
any positive-measure part of the survivor set.

### Construction and Haar measure

Choose sufficiently large integers $k_j\to\infty$ such that
$$
 \sum_j\frac1{k_j}<\infty,
 \qquad
 \sum_j\exp\bigl(-(2\log2-1)k_j+k_j^{-3}\bigr)<\varepsilon.
 \tag{6}
$$
For example, a sufficiently large multiple of $2^j$ works. Choose
pairwise disjoint finite prime blocks $P_j$, all primes in $P_j$ larger
than $k_j^3$, with
$$
 k_j\le\lambda_j:=\sum_{p\in P_j}\frac1p
                   <k_j+k_j^{-3}.
 \tag{7}
$$
They can be chosen successively, beyond all primes already used, by
stopping when the prime reciprocal sum first reaches $k_j$.

Let $\mathcal Q_j$ consist of all products of $2k_j$ distinct primes
from $P_j$, and install the zero class at every
$q\in\bigcup_j\mathcal Q_j$. All moduli are distinct and primitive:
within a block they are squarefree of the same rank, and different
blocks use disjoint prime sets. They therefore admit the required
strictly increasing enumeration.

Let $U_j=\bigcup_{q\in\mathcal Q_j}qG$ and $\beta_j=\mu(U_j)$.
For Haar-random $z$, let $Y_j(z)$ count the primes of $P_j$ dividing
$z$. Then $U_j=\{Y_j\ge2k_j\}$, and independent prime coordinates give
$$
 \beta_j
 \le 2^{-2k_j}\mathbb E2^{Y_j}
 =2^{-2k_j}\prod_{p\in P_j}(1+1/p)
 \le\exp\bigl(-(2\log2-1)k_j+k_j^{-3}\bigr).
 \tag{8}
$$
Consequently $\mu(U)\le\sum_j\beta_j<\varepsilon$.

### Reciprocal divergence in every neighborhood

The reciprocal sum of one block is
$$
 \sum_{q\in\mathcal Q_j}\frac1q
 =e_{2k_j}\bigl((1/p)_{p\in P_j}\bigr)
 =\bigl(1+O(k_j^{-2})\bigr)
                 \frac{\lambda_j^{2k_j}}{(2k_j)!}.
 \tag{9}
$$
To check the approximation, draw $2k_j$ primes independently with
probabilities $(1/p)/\lambda_j$. The probability of no collision is
$(2k_j)!e_{2k_j}/\lambda_j^{2k_j}$. Each draw has maximal point mass
at most $k_j^{-4}$, so the union bound over pairs gives collision
probability $O(k_j^{-2})$. Stirling's formula shows that the right side
of (9) tends to infinity. Increase the initial choice of the $k_j$ if
necessary so that every block reciprocal sum is at least one.

Fix a modulus $L$. All sufficiently late blocks consist entirely of
primes coprime to $L$. For every $q$ in these blocks, the cylinder
$qG$ meets every residue fiber modulo $L$, by CRT. Summing (9) over
these blocks proves divergence in every fiber. This is exactly $D=G$.
The same observation shows that $U$ is dense in $G$. Since $U$ is open,
$\partial U=G\setminus U=K$, establishing (5).

### Uniform counting bound for one block

Fix one block, abbreviating $k=k_j$, $P=P_j$, and
$\lambda=\lambda_j$. For an integer $X\ge1$, let
$$
 Z_X(n)=\sum_{\substack{p\in P\\p\le\sqrt X}}\mathbf1_{p\mid n},
 \qquad
 \lambda_X=\sum_{\substack{p\in P\\p\le\sqrt X}}\frac1p,
$$
and let $s$ be the number of primes in this sum. Average over
$1\le n\le X$. Exact floor counts imply
$$
 \lambda_X-s/X\le\mathbb E Z_X\le\lambda_X,
 \qquad
 \mathbb E Z_X^2\le\lambda_X+\lambda_X^2.
$$
Therefore
$$
 \mathbb E(Z_X-\lambda_X)^2
 \le\lambda_X+2\lambda_Xs/X
 \le\lambda+1,
 \tag{10}
$$
using $\lambda_X\le s/2$ and $s\le\sqrt X$.

If a positive integer $n\le X$ is deleted by a modulus in this block,
that modulus divides $n$ and hence is at most $X$. At most one of its
$2k$ prime factors can exceed $\sqrt X$. Thus
$Z_X(n)\ge2k-1$. By (7), for sufficiently large $k$,
$2k-1-\lambda_X\ge k/2$. Chebyshev's inequality and (10) give the
uniform bound
$$
 \frac1X\#\{n\le X:\exists q\in\mathcal Q_j,\ q\mid n\}
 \le\frac{C}{k_j},
 \tag{11}
$$
with an absolute constant $C$.

### Natural-density conclusion and activation

For zero residues, a positive full hit $q\mid n$ automatically has
$n\ge q$, so original activation introduces no exception at all.
By (11), the union of blocks after $J$ has at most
$$
 CX\sum_{j>J}\frac1{k_j}
$$
hits below $X$, uniformly in $X$. For each $X$ only finitely many
distinct moduli can be active, so this countable union bound follows
directly from the finite one. Its normalized upper bound tends to zero
as $J\to\infty$ by (6).

Every finite union of blocks is periodic, and its Haar measure tends
to $\mu(U)$ as the blocks exhaust the family. The last tail estimate
therefore proves natural density $\mu(U)$ for the excluded set and
$\mu(K)>1-\varepsilon$ for its complement. This construction is an
obstruction to making the local reciprocal criterion automatic, not a
counterexample to the target density statement.
