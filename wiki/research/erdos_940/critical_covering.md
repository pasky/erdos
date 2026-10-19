---
name: research/erdos_940/critical_covering
title: Proper-subsum sparsity does not force holes
desc: Cassels bases defeat abstract sparsity arguments; nearby powerful-sum targets almost never admit sufficiently close root representations.
tags: []
sources: []
created: 2026-09-22T23:49:00Z
updated: 2026-09-23T00:59:15Z
---


# Proper-subsum sparsity does not force holes

***

The final section records a different, arithmetic obstruction to a
local-repair covering argument: almost every pair of nearby targets
lacks representations with sufficiently close physical root vectors.
It too does not force holes.

## Status and scope

The interval bounds below are proved. The Cassels basis theorem is the external
input; its statement and proof were checked in [Nathanson, *Cassels Bases*,
Theorem 10](https://www.theoryofnumbers.com/melnathanson/pdfs/nath2010-138.pdf).
The resulting counterexample strengthens the elementary
[convex-track warning](palm_void_strategy.md#compatibility-with-clustering-but-no-automatic-theorem).
It rules out a general covering argument based only on counting regularity,
finite representation mean, and proper-subsum anti-concentration. It is not a
counterexample about powerful numbers.

## An interval bound from bounded-error counting

Suppose $r\ge3$ and $A\subset\mathbb N$ satisfies

$$
A(t):=\#(A\cap[1,t])=c\,t^{1/r}+O(1),\qquad c>0.
$$

For $1\le k\le r$ and $1\le H\le X$, let $T_{A,k}(X,H)$
count ordered tuples in $A^k$ with sum in $[X,X+H]$. Then

$$
T_{A,k}(X,H)\ll_{A,r,k}
X^{(k-1)/r}+H X^{k/r-1}.                              \tag{1}
$$


Every counted tuple has an entry at least $X/k$. Fix its index
and the other $k-1$ entries, allowing at most
$O(X^{(k-1)/r})$ choices. The remaining entry lies in an interval
of length at most $H$ contained in $[X/k,2X]$. The counting
hypothesis and the mean value theorem bound its possibilities by
$O(1+H X^{1/r-1})$. Summing over the possible indices proves (1).

## An actual basis with this regularity

Cassels' theorem supplies, for every $r\ge3$, an additive basis
$C=\{c_n\}\subset\mathbb N_0$ of order $r$ with

$$
c_n=\gamma n^r+O(n^{r-1}),\qquad \gamma>0.
$$

Inverting this estimate gives
$C(t)=\gamma^{-1/r}t^{1/r}+O(1)$.
After replacing $C$ by $A=C+1$, all its terms are positive,
$rA$ is cofinite, and the same counting estimate holds.
Thus (1) applies to an actual additive basis.

In particular, at the natural root-gap scale $H=X^{1-1/r}$,

$$
T_{A,r-1}(X,H)\ll X^{1-2/r}=H X^{-1/r}.               \tag{2}
$$

Every such interval contains only a vanishing proportion of
$(r-1)$-fold sums, although adding one more copy of $A$ covers
all sufficiently large integers.

These bases also have finite limiting unordered representation mean:

$$
\frac1X\sum_{n\le X}R_{A,r}(n)
\longrightarrow
\frac{c^r\Gamma(1+1/r)^r}{r!},
\qquad c=\gamma^{-1/r}.
$$

Indeed, scaled counting measures from $A(t)\sim ct^{1/r}$
give the usual simplex integral for ordered tuples. Its constant
is $c^r\Gamma(1+1/r)^r$, since $r(1/r)=1$.
Tuples with repeated entries number $O(X^{1-1/r})$, so division
by $r!$ gives the unordered constant.

## Comparison with powerful sums

For a finite canonical-core set $D$,

$$
A_D=\bigcup_{d\in D}\{d m^r:m\ge1\}
$$

has disjoint tracks, by canonical uniqueness. Therefore

$$
A_D(t)=\left(\sum_{d\in D}d^{-1/r}\right)t^{1/r}+O_D(1).
$$

Thus the bounded-error counting property of these finite unions,
and all the bounds (1), are shared by the Cassels example.

For the full powerful set $\mathcal P_r$, the established
[core count and tail](finite_core_reduction.md) give

$$
\begin{aligned}
\mathcal P_r(t)
&=\sum_{\substack{d\in\mathcal C_r\\d\le t}}
       \left\lfloor(t/d)^{1/r}\right\rfloor\\
&=W_rt^{1/r}+O_r(t^{1/(r+1)}).
\end{aligned}
$$

The floor errors are bounded by the core count, and the missing
weight contributes $t^{1/r}T_r(t)=O(t^{1/(r+1)})$.
The same interval argument now yields

$$
T_{\mathcal P_r,k}(X,H)
\ll_{r,k}H X^{k/r-1}+X^{(k-1)/r+1/(r+1)}.             \tag{3}
$$

For $k=r-1$ and $H=X^{1-1/r}$, in particular,

$$
\#\bigl((r-1)\mathcal P_r\cap[X,X+H]\bigr)
\ll_r H X^{-1/[r(r+1)]}.                              \tag{4}
$$

This is genuine local sparsity of proper subsums. But (2) is
stronger and holds for an additive basis, so it cannot by itself
force missing targets.

## What the attempt rules out

No universal gap criterion can use only the above counting
regularity, finite mean, and gap-scale proper-subsum upper bounds.
This counterexample does not have multiplicative closure and is
not an exact union of the root lattices
$\{d^{1/r}m:m\in\mathbb N\}$. It also does not prescribe the
particular numerical mean of the powerful representation function.
An argument exploiting those additional features is not excluded.
No such argument was established in this continuation.

## An arithmetic obstruction to local repair

For a representation $n=\sum_i a_i$, call
$(a_1^{1/r},\ldots,a_r^{1/r})$ its physical root vector, padding with
zeros when there are fewer summands and allowing permutations when
comparing two representations.

**Proposition.** Fix $r\ge3$, a nonzero integer $h$, and $\eta>0$.
Put $B=X^{1/r}$. Only $o(X)$ integers $n\le X$ admit powerful-sum
representations of both $n$ and $n+h$ whose matched physical root
vectors have sup-distance at most $B^{1/(r-1)-\eta}$.

This is an all-core statement about **targets**, not a bound for the
number of all representation pairs. It rules out repairing almost
every target by changing its roots by this amount. A cofinite cover
whose representations make larger jumps is not excluded.

### A uniform binary bound for fixed coefficients

For fixed positive integers $d,e$ and $r\ge3$, uniformly for
$c\ne0$, $|c|\ll B^r$,

$$
\#\{1\le x,y\ll B:dx^r-ey^r=c\}
\ll_{d,e,r,\epsilon}B^\epsilon.
\tag{5}
$$

Here and below the constants implicit in the ranges are fixed.

If $(e/d)^{1/r}=a/b\in\mathbb Q$ in lowest terms, then
$d=kb^r$, $e=ka^r$ for an integer $k$. When solutions exist,
$(bx)^r-(ay)^r=c/k$ is an integer equation. The nonzero difference
$bx-ay$ divides $c/k$. Fixing that divisor leaves a nonconstant
polynomial of degree $r-1$ in $ay$, so the divisor bound proves (5).

Otherwise let $\gamma=d(e/d)^{1/r}$ and $K=\mathbb Q(\gamma)$,
of degree $m\ge2$. The element $\gamma$ is integral, and its monic
minimal polynomial $P(T)$ divides $T^r-ed^{r-1}$ in $\mathbb Z[T]$.
Homogenizing that factorization proves

$$
0\ne N_{K/\mathbb Q}(dx-\gamma y)
=y^mP(dx/y)\mid d^{r-1}c.
\tag{6}
$$

This remains true if the degree-$r$ binomial is reducible.

There are at most $\tau(|d^{r-1}c|)^m$ integral ideals whose norms
divide $|d^{r-1}c|$: at a rational prime of exponent $v$, there
are at most $m$ prime ideals above it, each with exponent at most $v$.
For any solution $\beta=dx-\gamma y$, its conjugates satisfy

$$
(CB)^{-(m-1)}\le|\sigma(\beta)|\le CB.
$$

The lower bound uses its nonzero integral norm. For each occurring
principal ideal choose one solution-generator $\beta_0$. Every other
one is $\varepsilon\beta_0$, where the unit logarithms lie in a box
of side $O(\log B)$. The logarithmic unit image is discrete, with
finite kernel: bounded logarithms bound all conjugates, and only
finitely many algebraic integers of a fixed degree have all conjugates
bounded. The image lies in a hyperplane of dimension at most $m-1$.
Packing gives $O_K((1+\log B)^{m-1})$ possible generators, uniformly
in the ideal. Finally $(x,y)\mapsto dx-\gamma y$ is injective.
The divisor bound, with its exponent chosen smaller initially,
absorbs these logarithms and proves (5).

### Counting nearby pairs and removing the core cutoff

Fix two canonical coefficient tuples $\mathbf d,\mathbf e$.
Suppose the outputs differ by $h\ne0$ and

$$
|d_i^{1/r}x_i-e_i^{1/r}y_i|\le H\quad(1\le i\le r).
$$

At least one coordinate has $d_jx_j^r-e_jy_j^r\ne0$.
Choose such a coordinate and fix the other $r-1$ coordinate pairs;
each pair has $O_{\mathbf d,\mathbf e}(B(H+1))$ possibilities.
The last coordinate satisfies a nonzero equation covered by (5).
Thus the number of pairs for these fixed cores is

$$
O_{\mathbf d,\mathbf e,r,\epsilon}
\bigl(B^{r-1+\epsilon}(H+1)^{r-1}\bigr).
\tag{7}
$$

For $H=B^{1/(r-1)-\eta}$ this is $o(B^r)$ after choosing
$\epsilon>0$ sufficiently small. The nonzero-coordinate condition
is essential: (5) is false for $c=0$.

Now fix a core cutoff $Y$. The finitely many core tuples and coordinate
permutations contribute $o_Y(X)$ targets. Targets having any
representation with a core exceeding $Y$ number at most
$O_r(XT_r(Y))$, by the established canonical first-moment tail; the
same bound applies after the fixed shift $h$. Shorter representations
contribute $O_r(X^{1-1/r})$ targets. Hence the upper density in the
proposition is $O_r(T_r(Y))$. Let $Y\to\infty$ to prove the claim.
No uniform power-saving rate after summing all cores is asserted.

### Why the covering argument does not close

There is no theorem making a cofinite cover continuous in root space.
Simple cap pigeonholing does not supply one at the required scale.
For targets comparable to $B^r$, a block of $L$ targets lies in an
$\ell^r$-shell of thickness $O(L/B^{r-1})$. If this is at most $H$,
the shell has $O_r((B/H)^{r-1})$ caps of diameter $O(H)$.
Forcing a positive fraction of close pairs by overfilling these caps
requires

$$
L H^{r-1}\gg B^{r-1}.
$$

By contrast, summing (7) over differences $1\le|h|\le L$ makes the
nearby-pair count $o(B^r)$ only in the sufficient range
$L(H+1)^{r-1}\ll B^{1-\epsilon}$.
The scales are separated by $B^{r-2}$. This defeats that particular
pigeonhole argument, not every use of exact root geometry. No required
root-coherence theorem or higher-exponent gap follows.
