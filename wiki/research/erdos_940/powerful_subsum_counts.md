---
name: research/erdos_940/powerful_subsum_counts
title: Powerful subsums and shifted powerful targets
desc: A coefficient-uniform plane-curve estimate gives a power saving for tuples with powerful subsums, but not for arbitrary targets.
tags: []
sources: []
created: 2026-09-22T22:14:11Z
updated: 2026-09-22T22:14:11Z
---


# Powerful subsums and shifted powerful targets

***

## Status and scope

The bounds below are proved, with the quantitative argument independently
checked. They count **ordered input tuples whose sum, or shifted sum, is
itself powerful**. They do not bound arbitrary targets in $S_r$ and do not
settle a density or infinitude case.

Write $\mathcal P_r$ for the positive $r$-powerful integers. The
[canonical-core bounds](finite_core_reduction.md) give, for $r\ge3$,

$$
\#(\mathcal P_r\cap[1,X])\ll_r X^{1/r},\qquad
\#(\mathcal C_r\cap[1,Y])\ll_r Y^{1/(r+1)},
$$

and

$$
\#\{a\in\mathcal P_r:a\le X,\ \operatorname{core}(a)>Y\}
\ll_r X^{1/r}Y^{-1/[r(r+1)]}.                         \tag{1}
$$


## A uniform shifted-target bound

**Theorem.** Fix $r\ge3$, $k\ge2$, and $\varepsilon>0$. Put

$$
\delta_r=\frac{r-1}{r^2(2r+1)}.
$$

Uniformly for integers $|h|\le X$,

$$
\#\left\{(a_1,\ldots,a_k)\in\mathcal P_r^k:
  \sum_i a_i\le X,\quad \sum_i a_i+h\in\mathcal P_r\right\}
\ll_{r,k,\varepsilon}X^{k/r-\delta_r+\varepsilon}.    \tag{2}
$$

There is no primitivity hypothesis.

**Proof.** Set $c=\sum_i a_i+h$, so that every counted tuple has
$1\le c\le2X$. Choose a cutoff $Y\ge1$. If
$\operatorname{core}(a_k)>Y$, enumerate all inputs independently and
use (1), giving

$$
O_{r,k}\bigl(X^{k/r}Y^{-1/[r(r+1)]}\bigr).             \tag{3}
$$

If $\operatorname{core}(c)>Y$, first fix $a_1,\ldots,a_{k-1}$
and then enumerate such $c$. The remaining input
$a_k=c-h-\sum_{i<k}a_i$ is determined. Formula (1), with $2X$ in
place of $X$, gives the same bound (3).

Otherwise write $a_k=dx^r$, $c=fz^r$, with $d,f\in\mathcal C_r$ and
$d,f\le Y$. After fixing the first $k-1$ inputs, put
$C=\sum_{i<k}a_i+h$. If $C\ne0$, the equation

$$
dx^r-fz^r+C=0                                       \tag{4}
$$

is absolutely irreducible. For example, choose any complex root
$\lambda$ of $fz^r-C$. It is simple since $C\ne0$, and Eisenstein
at $z-\lambda$ proves irreducibility of (4) over $\mathbb C[z,x]$.

The coefficient-uniform Bombieri--Pila estimate in [Browning--Verzobio, Section
2.1, Lemma
2.2](../../../library/diophantine_problems/browning_verzobio_2026_sums_three_powerful_numbers/_index.md)
states that an absolutely irreducible integral plane curve of degree $e$ has
$O_{\varepsilon,e}(B^{1/e+\varepsilon})$ integer points in $[-B,B]^2$. Its full
statement and coefficient dependence have been checked. Since
$x,z\le(2X)^{1/r}$, it gives $O_{r,\varepsilon}(X^{1/r^2+\varepsilon})$ pairs in
(4). Thus this bounded-core part contributes

$$
O_{r,k,\varepsilon}
\left(X^{(k-1)/r+1/r^2+\varepsilon}Y^{2/(r+1)}\right). \tag{5}
$$


When $C=0$, fixing the first $k-2$ inputs determines $a_{k-1}$.
The variable $a_k=c$ has $O_r(X^{1/r})$ possibilities. These tuples
number $O_{r,k}(X^{(k-1)/r})$, including when $k=2$.

Take

$$
Y=X^{(r^2-1)/(r(2r+1))}.
$$

The exponents in (3) and (5) balance at $k/r-\delta_r$ (with
the stated $\varepsilon$ in (5)). Also $\delta_r<1/r$, so the
$C=0$ contribution is smaller. This proves (2). $\square$

## Consequence for grouping an existing representation

Among ordered $r$-tuples in $\mathcal P_r^r$ with total at most $X$,
those having an $r$-powerful subsum indexed by **at least two**
coordinates number

$$
O_{r,\varepsilon}(X^{1-\delta_r+\varepsilon}).        \tag{6}
$$

For a fixed index set of size $k\ge2$, apply (2) with $h=0$ to that
subtuple and bound the other inputs independently by
$O_r(X^{(r-k)/r})$. A finite union over the index sets proves (6).
Taking $\varepsilon<\delta_r$ makes the count $o(X)$.

This is an input-multiplicity statement. Distinct outputs admitting
a **proper** $r$-powerful subsum already have the stronger elementary
bound $O_r(X^{(r-1)/r})$: replace that block by its sum to obtain a
representation with at most $r-1$ summands. The full $r$-term subsum
is also allowed in (6).

## Qualitative extension to lower powerful exponents

**Proposition.** Fix $r\ge3$ and $t,k\ge2$. Then

$$
\sup_{h\in\mathbb Z}
\#\left\{\mathbf a\in(\mathcal P_r\cap[1,X])^k:
                    \sum_i a_i+h\in\mathcal P_t\right\}
=o(X^{k/r}).                                        \tag{7}
$$

Here $h$ is unrestricted in size. The argument uses Chebotarev's
theorem only when $k=2$.

Fix a finite cutoff on the input cores and a resulting form
$F(\mathbf x)=\sum_{i=1}^k d_i x_i^r$. For $k\ge3$, additive
orthogonality and the Gauss-sum bound give, at primes
$p\nmid r\prod_i d_i$,

$$
\#\{\mathbf x\bmod p:F(\mathbf x)=b\}
=p^{k-1}+O_r((r-1)^k p^{k/2}),
$$

uniformly in $b$. The only possible singular root is the zero
vector. Consequently all sufficiently large good primes have at
least $\tfrac12p^{k-1}$ nonsingular roots for every target.

For $k=2$, instead use the primes splitting completely in the finite
Galois extension

$$
L=\mathbb Q\bigl(\zeta_{2r},(d_2/d_1)^{1/r}\bigr).
$$

Chebotarev gives positive prime density, hence a divergent sum of
reciprocals, for these primes. Outside finitely many bad primes,
$-d_2/d_1$ is an $r$th power modulo $p$, so the zero target has
exactly $r(p-1)$ nonsingular roots. For nonzero targets the
two-variable character expansion gives $p+O_r(\sqrt p)$ roots:
after summing the nonzero additive frequency, a nonprincipal
product character contributes $O(\sqrt p)$ per character pair,
and a principal product contributes $O(1)$. These estimates
follow from the ordinary Gauss-sum identity. All such roots
are nonsingular. Thus, in this
case also, there are at least $\tfrac12p^{k-1}$ nonsingular roots
for every target at every sufficiently large selected prime.

For each nonsingular root of $F=-h\pmod p$, exactly
$(p-1)p^{k-1}$ of its lifts modulo $p^2$ have
$v_p(F+h)=1$. Therefore at least $1/(4p)$ of all root-vector
residues modulo $p^2$ are forbidden for a $t$-powerful output,
uniformly in $h$. For any finite set of selected primes, CRT and
box counting bound the surviving proportion by

$$
\prod_p(1-1/(4p))+o_{F,\{p\}}(1),
$$

uniformly in $h$. First let $X\to\infty$, then enlarge the prime
set. Its divergent reciprocal sum makes the product tend to zero.
This proves (7) for each fixed core tuple, and hence for any fixed
finite family. Finally remove the input-core cutoff using (1) and
the convergent weights. The tail is uniformly at most an arbitrarily
small multiple of $X^{k/r}$, completing the proof.

In particular, grouping $r$ given $r$-powerful entries into fewer
blocks whose sums are $t$-powerful, for any fixed $t\ge2$, is possible
for only $o(X)$ of the original ordered tuples with total at most
$X$. Every such partition contains a block of size at least two;
apply (7) to that block. This does not restrict a representation by
entirely different summands.

## Why these estimates do not force a missing target

If $S_r$ were cofinite, almost every number $c-1$ with
$c\in\mathcal P_r$ would have a representation using at most $r$
summands. Formula (2), with $k=r$ and $h=1$, still permits
$X^{1-\delta_r+\varepsilon}$ such tuples, much more than the
$X^{1/r}$ possible powerful targets $c$. The qualitative estimate
(7) likewise allows concentration on all of this sparse target set.
No contradiction to cofiniteness, or density estimate for arbitrary
targets, follows.
