---
name: research/erdos_774/routes/tensor_extraction
title: Uniformly Sidon tensor-simplex blocks
desc: A randomized lattice-rounding argument gives one uniform full dissociated extraction constant for an explicit tensor family; unbounded dissociated coloring is not proved.
tags: [E0774, proved, construction, incomplete]
sources: []
created: 2026-09-17T23:53:25Z
updated: 2026-09-18T01:24:28Z
---


# Uniformly Sidon tensor-simplex blocks

***

## Standing and precise result

**Proved here, but not an E0774 counterexample.** Put

$$
q_i=\left\lceil1000i\log_2(i+1)\right\rceil,
\qquad
S_q=\{e_1,\ldots,e_{q-1},-e_1-\cdots-e_{q-1}\},
$$

and define the distinct integer-vector configuration

$$
E_k=S_{q_1}\otimes\cdots\otimes S_{q_k}
\subseteq\mathbb Z^{d_k},\qquad
d_k=\prod_{i\leq k}(q_i-1),\quad N_k=|E_k|=\prod_{i\leq k}q_i.
\tag{1}
$$

There is **one** $\delta>0$ such that every subset of every $E_k$
contains a dissociated subset of relative size at least $\delta$.
Moreover $d_k/N_k\to0$, so their rational-linearly-independent coloring
numbers are unbounded. The latter assertion is **not** a lower bound for
dissociated coloring. The unproved obligation is

$$
\sup_k\chi_{\mathrm{diss}}(E_k)=\infty. \tag{2}
$$

The proof of the extraction statement uses the checked full-source Pisier
Theorem 2 only at its last step. The new analytic estimate is proved below.
Its lattice-rounding and analytic steps are author-recorded and were checked
by a separate reviewer; this is not a claim of external review or publication
priority.

## 1. The real Sidon estimate to prove

For a finite frequency family $E$ in a free abelian group with dual torus
$G$, write $\rho(E)$ for the largest number such that

$$
\max_{g\in G}\operatorname{Re}\sum_{v\in E}c_v\,v(g)
\geq\rho(E)\sum_{v\in E}|c_v|
\tag{3}
$$

for all complex coefficients. Here $v(g)$ denotes the unit-modulus
character value. A positive lower bound for $\rho$ gives the usual Sidon
constant at most $1/\rho$, since the supremum of absolute value is at
least the supremum of real part. The initial configuration is the free singleton
$E_0=\{1\in\mathbb Z\}$, on the dual torus $\mathbb T$, for which
$\rho=1$. This is the character $z\mapsto z$, **not** the constant
character. We use the empty product convention $Q_0=\pi^2$.

We shall prove uniformly in $k$ that

$$
\rho(E_k)>1-\frac1{90000}. \tag{4}
$$

## 2. Integer lattice of phase lifts

For side sizes $q_1,\ldots,q_k$, let $I=\prod_i[q_i]$, $N=|I|$,
and let $W\subseteq\mathbb R^I$ be the space of arrays whose sum on every
coordinate line is zero. Set $L=W\cap\mathbb Z^I$.

The integer vectors $b_j=e_j-e_q$, $1\leq j<q$, form a basis of the
one-factor zero-sum lattice. Their tensor products form an integer basis of
$L$. Indeed, array entries with every coordinate less than its last value
are arbitrary integers, and the line-sum equations uniquely determine all
remaining entries by signed sums of those entries. In particular

$$
L=\bigotimes_i A_{q_i-1},\qquad \dim W=\prod_i(q_i-1).
$$

The character-value torus of (1) is precisely
$\exp(2\pi iW)\subseteq\mathbb T^I$. In these normalized coordinates,
the map $x\mapsto\exp(2\pi ix)$ has period lattice $L$.
Equivalently, choose the phases on the interior grid arbitrarily and
extend by reciprocal products on boundary lines. This also proves that this
torus is connected. In radian coordinates the map is
$X\mapsto\exp(iX)$, and its period lattice is $2\pi L$. The random
variable $x$ in Section 3 is normalized; $X$ in (7) and Section 4 is
measured in radians.

## 3. Randomized lattice rounding — proved

For every $x\in W$ there is a finite random lattice point $Z\in L$
such that $\mathbb E(x-Z)=0$ and, for every coordinate $a\in I$,

$$
\mathbb E(x_a-Z_a)^2
\leq\frac14\prod_{i=1}^k
\frac{q_i-1+H_{q_i-1}}{q_i},
\qquad H_n=\sum_{j=1}^n\frac1j. \tag{5}
$$

Here is the full rounding argument. Take an ordered integer basis
$b_1,\ldots,b_d$ of $L$, with orthogonal Gram–Schmidt vectors
$u_1,\ldots,u_d$. Starting with residual $x$, process indices in
descending order. If its coefficient along $u_i$ is $\alpha_i$, round
$\alpha_i$ to one of its adjacent integers, with probabilities chosen so
that the rounded integer has conditional expectation $\alpha_i$, and
subtract that integer times $b_i$. At termination the residual is

$$
e=x-Z=\sum_i\eta_i u_i.
$$

Conditional on the choices at larger indices,
$\mathbb E\eta_i=0$ and $\mathbb E\eta_i^2\leq1/4$.
For $i<j$, $\eta_j$ is determined by those larger-index choices, so
$\mathbb E\eta_i\eta_j=0$. Therefore

$$
\mathbb E e_a^2\leq\frac14\sum_i u_i(a)^2. \tag{6}
$$

The same conditional expectations also give $\mathbb E e=0$.
Both assertions hold for every fixed target and every chosen basis, so
the mean-zero assertion survives the basis randomization below.

For the anchored basis of $A_{q-1}$, the Gram–Schmidt squared lengths are
$2,3/2,\ldots,q/(q-1)$: its leading $j$-by-$j$ Gram determinant
is $j+1$, because the Gram matrix is $I+\mathbf1\mathbf1^T$.
Thus their sum is $q-1+H_{q-1}$. In lexicographic order the tensor basis
has tensor-product Gram–Schmidt vectors (by triangularity and orthogonality).
Its total squared Gram–Schmidt length is consequently

$$
T=\prod_i(q_i-1+H_{q_i-1}).
$$

Finally choose a uniform independent permutation of the $q_i$ coordinate
values in every factor and use that permuted lattice basis for rounding.
These permutations preserve $L$, act transitively on $I$, and preserve
$T$. Averaging (6) gives $T/(4N)$ in every coordinate, which is (5).
The target $x$ stays fixed: (6) is a target-independent bound for each
chosen basis. There is no assumption that $x$ is permutation invariant.

Multiplying the residual by $2\pi$ gives a random lift $X$ of any
prescribed torus element such that

$$
\mathbb E X=0,\qquad \mathbb E X_a^2\leq Q_k,
\qquad
Q_k=\pi^2\prod_{i\leq k}
\frac{q_i-1+H_{q_i-1}}{q_i},\quad Q_0=\pi^2. \tag{7}
$$

## 4. Tensor extension inequality — proved

Write a polynomial on $E\otimes S_q$ as $q$ column polynomials
$f_1,\ldots,f_q$ on the base torus $G$. Their character tuples are
exactly $(g_1,\ldots,g_q)$ satisfying $\prod_jg_j=1$.

First maximize $\operatorname{Re}f_j$ independently, at points $g_j$.
Their total real value is at least $\rho(E)\sum_{v,j}|c_{v,j}|$.
Choose a random real lift $X$ of $(\prod_jg_j)^{-1}$ obeying (7),
and replace each $g_j$ by $g_j\exp(iX/q)$. The new tuple has product
one and is therefore admissible for the tensor polynomial.

For a single complex term $z$,

$$
\operatorname{Re}(ze^{it})\geq
\operatorname{Re}z-t\operatorname{Im}z-\tfrac12|z|t^2.
$$

Since $\mathbb E X_a=0$, each first-order term vanishes in expectation.
Taking expectations of the second-order bound and summing the columns proves

$$
\rho(E_{k+1})\geq\rho(E_k)-\frac{Q_k}{2q_{k+1}^2}. \tag{8}
$$

All random choices have finite support; an outcome attains at least the
expected value. No simultaneous phase interpolation or tensor
multiplicativity of ordinary Sidon constants is assumed.

The earlier stationarity proof is also valid: at each column maximum its
derivative vanishes in every tangent direction $X\in W$. The mean-zero
proof records a stronger property of the rounding lemma and does not require
that calculation. A separate adversarial check covered
the lattice basis, the target-dependent quantifiers, and the cyclotomic
transfer and found no defect. This is internal checking, not external review.

## 5. Explicit summable loss

Let $a_i=(q_i-1+H_{q_i-1})/q_i$. With the side sizes in (1),

$$
q_i\geq1000i\log_2(i+1),\qquad q_i\leq2000i^2,
$$

and $H_{q_i-1}-1\leq\log q_i$. All unmarked logarithms here are natural.
Consequently

$$
\log a_i\leq\frac{\log q_i}{q_i}
\leq\frac{\log8000}{1000i}<\frac1{100i}.
$$

It follows that $Q_{i-1}\leq\pi^2e^{1/100}i^{1/100}$. Hence

$$
\sum_{i\geq1}\frac{Q_{i-1}}{2q_i^2}
\leq\frac{\pi^2e^{1/100}}{2\cdot10^6}
\sum_{i\geq1}i^{-199/100}
<\frac1{90000}. \tag{9}
$$

For explicit elementary numerical bounds use $\pi^2<10$,
$e^{1/100}\leq100/99$, and
$\sum_i i^{-199/100}\leq1+\int_1^\infty x^{-199/100}dx=199/99$.
Summing (8) from $\rho(E_0)=1$ proves (4).

## 6. One full dissociation constant, not a sequence of constants

Embed the ambient free abelian group of $E_k$ into that of $E_{k+1}$
by $v\mapsto v\otimes e_1$. This is a primitive direct-summand embedding,
and it identifies $E_k$ with a slice of $E_{k+1}$. In the direct-limit
free abelian group, let $E=\bigcup_kE_k$. Every finite polynomial on
$E$ lies in some $E_k$, and every character of that finite-stage group
extends to the limit group. By (4), $E$ is Sidon with constant at most
$90000/89999$.

[Pisier's Theorem 2](../../../../library/analysis/pisier_1983_arithmetic_characterizations_sidon_sets/_index.md),
checked in the held reading copy on page 3, applies **once** to this single set
$E$. It supplies one $\delta>0$ for dissociated extraction from every finite
subset of $E$, hence from every subset of every block $E_k$. This avoids
assuming any unprovided quantitative dependence in Pisier's announcement.

This last implication uses Pisier's stated theorem as a literature theorem;
the supplied announcement refers elsewhere for its proof. No numerical value
of $\delta$ is obtained in these notes.

The blocks have no zero or equal-up-to-sign columns: each factor has that
property for $q_i\geq3$, and equality of nonzero pure tensors forces
proportionality in every factor. The
[finite realization lemma](../lemmas/rational_realization.md) therefore turns
each block into distinct positive integers, preserving its entire signed
support hypergraph and the common extraction constant.

Explicitly, order the $d_k$ coordinates, put $B_k=N_k+2$, and take

$$
F_k=\left\{\left|\sum_{j=0}^{d_k-1}v_jB_k^j\right|:v\in E_k\right\}.
\tag{10}
$$

Every column entry is $0$ or $\pm1$, so a signed sum has coordinate
absolute values at most $N_k<B_k-1$. The leading nonzero digit therefore
cannot be canceled. This verifies the exact finite integer encoding directly.
It preserves dissociated subsets and their coloring number, up to coordinate
sign changes. We do **not** claim that this scalar encoding preserves the
displayed numerical real-Sidon constant.

## 7. What is still missing

Since $q_i\leq2000i\log_2(i+1)$, $\sum_i1/q_i=\infty$. Therefore

$$
\frac{d_k}{N_k}=\prod_{i\leq k}(1-1/q_i)\longrightarrow0.
$$

Any partition into rationally independent classes needs at least $N_k/d_k$
classes. But dissociated classes can be rationally dependent; the
[saturated recurrence example](../lemmas/full_relation_rank.md) emphasizes
this distinction. No argument yet proves (2), and **the constructed integer
blocks are not claimed to have unbounded dissociated coloring number**.

The next task is specifically to prove (2) for this tensor family, or to
modify the family while retaining the summable bound (9) and introducing a
verified unbounded dissociated coloring obstruction.
