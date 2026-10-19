---
name: research/erdos_774/routes/prime_tensor_extraction
title: Uniform extraction for all distinct-prime tensors
desc: Explicit elementary prime estimates extend the tensor theorem to every squarefree prime grid and to all roots of unity additively; unbounded dissociated coloring remains unproved.
tags: [E0774, proved, construction, incomplete]
sources: []
created: 2026-09-18T00:38:00Z
updated: 2026-10-14T00:26:52Z
---


# Uniform extraction for all distinct-prime tensors

***

## Theorem and standing

There is one $\delta_0>0$ such that **every** finite subset of **every**
tensor $\bigotimes_{p\in J}S_p$, where $J$ is a finite set of
distinct odd primes, contains a dissociated subset of relative size at least
$\delta_0$.

More generally, all roots of unity, considered in the **discrete additive**
group $\mathbb C_d$, are proportionately dissociated and therefore Sidon. The
proof below is author-recorded; two separate reviewers checked it, and it
remains subject to external review. No publication-priority claim is made.
The roots-of-unity conclusions are also machine-checked in Lean and recorded
as the native claims
[[theory/integer_sequences/L20_roots_of_unity_analytic_sidon/_index|L20]] (analytic
Sidon) and
[[theory/integer_sequences/L21_roots_of_unity_proportional_dissociation/_index|L21]]
(one extraction denominator) at tier 2; the
[[research/erdos_774/lean_proof_map|Lean proof map]] lists the modules and
the finite Pisier implication they prove in place of the cited theorem.

**This is not a counterexample to E0774.** The missing theorem is still
unbounded full-dissociated coloring. Distinct-prime grids are a more
structured candidate than the original large-side schedule; unlike that
schedule they include the checked $S_3\otimes S_5\otimes S_7$
three-color obstruction.

## 1. What the tensor theorem supplies

The [proved tensor extension and rounding lemmas](tensor_extraction.md)
apply to any finite list of side sizes at least three, not only the list
chosen there. For prime sides set

$$
a_p=\frac{p-1+H_{p-1}}p,
\qquad Q(P,x)=\pi^2\prod_{P<p\leq x}a_p.
$$

Starting at the free singleton, the loss in positive-real Sidon parameter
from adding all primes above $P$, through any finite stage, is at most

$$
\frac12\sum_{p>P}\frac{Q(P,p^-)}{p^2}. \tag{1}
$$

We prove the completely explicit bound

$$
P=2^{40}\quad\Longrightarrow\quad
\frac12\sum_{p>P}\frac{Q(P,p^-)}{p^2}<2^{-18}. \tag{2}
$$

All logarithms on this page are natural.

## 2. Elementary prime estimates, with constants

Let $\Lambda(n)$ be the von Mangoldt function,
$\psi(x)=\sum_{n\leq x}\Lambda(n)$, and
$A(x)=\sum_{p\leq x}(\log p)/p$. For every real $x\geq2$,

$$
\psi(x)<4x,\qquad |A(x)-\log x|\leq5. \tag{3}
$$

For a positive integer $n$, the exponent of a prime in
$\binom{2n}{n}$ is a sum of nonnegative terms
$\lfloor2n/p^j\rfloor-2\lfloor n/p^j\rfloor$. Each prime power
in $(n,2n]$ contributes one. Hence
$\psi(2n)-\psi(n)\leq\log\binom{2n}{n}\leq2n\log2$.
Sum on dyadic scales and then round $x$ up to the next power of two to
obtain $\psi(x)<4x$.

The identity

$$
\log(n!)=\sum_{m\leq n}\Lambda(m)\lfloor n/m\rfloor
$$

and (3)'s first bound show
$\sum_{m\leq n}\Lambda(m)/m\in[\log n-1,\log n+4]$, using
$n\log n-n\leq\log(n!)\leq n\log n$.
The omitted prime-power terms satisfy

$$
\sum_p\sum_{j\geq2}\frac{\log p}{p^j}
\leq\sum_{n\geq2}\frac{\log n}{n(n-1)}<3.
$$

For the last estimate use $1/[n(n-1)]\leq2/n^2$ and
$\sum_{n\geq2}(\log n)/n^2 \leq(\log2)/4+\int_2^\infty(\log t)/t^2\,dt<5/4$.
Thus $A(n)\in[\log n-4,\log n+4]$. Passing to $n=\lfloor x\rfloor$ costs less
than $\log2<1$, proving (3).

Write $A(x)=\log x+E(x)$, $|E(x)|\leq5$. Partial summation gives

$$
B(x):=\sum_{p\leq x}\frac1p
=\log\log x+C+R(x),\qquad |R(x)|\leq\frac{10}{\log x}. \tag{4}
$$

Explicitly, take $C=1-\log\log2+\int_2^\infty E(t)/(t\log^2t)\,dt$; the
remainder is $E(x)/\log x-\int_x^\infty E(t)/(t\log^2t)\,dt$. These estimates
are proved here. They also agree with the checked full statements of Theorems 13
and 15 in
[Tao's author lecture notes](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/).

## 3. The logarithmic saving makes the full prime tail summable

Put $\beta=\log(3/2)$, so $1/3<\beta<1/2$. Convexity of
$1/x$ on each interval $[j-1/2,j+1/2]$ gives

$$
H_{p-1}-1=\sum_{j=2}^{p-1}\frac1j
\leq\int_{3/2}^{p-1/2}\frac{dx}{x}
<\log p-\beta.
$$

Consequently $\log a_p\leq(\log p-\beta)/p$. From (3)–(4), for
$x\geq P\geq e^{20}$,

$$
\begin{aligned}
\log\frac{Q(P,x)}{\pi^2}
&\leq A(x)-A(P)-\beta(B(x)-B(P))\\
&\leq\log(x/P)-\beta\log\frac{\log x}{\log P}
       +10+\frac{20\beta}{\log P}\\
&<\log(x/P)-\beta\log\frac{\log x}{\log P}+11.
\end{aligned}
$$

Thus

$$
Q(P,x)\leq\pi^2e^{11}\frac xP
                    \left(\frac{\log P}{\log x}\right)^\beta. \tag{5}
$$

One more partial summation, now integrating
$(\log t)^{-1-\beta}$ against $dA(t)$, gives

$$
\sum_{p>P}\frac1{p(\log p)^\beta}
\leq(\log P)^{-\beta}
       \left(\frac1\beta+\frac{10}{\log P}\right)
<4(\log P)^{-\beta}. \tag{6}
$$

Indeed the main term is the integral against $d\log t$; the boundary
error and error integral are each at most
$5(\log P)^{-1-\beta}$. This also proves convergence, without the
prime number theorem.

Since $a_p\geq1$, (5) may bound $Q(P,p^-)$ by $Q(P,p)$.
Combining (5)–(6) bounds (1) by
$2\pi^2e^{11}/P<2^{22}/P$. The last numerical inequality follows
from $\pi^2<10$, $e<3$, and $20\cdot3^{11}<2^{22}$.
For $P=2^{40}$, $\log P>20$, proving (2).

## 4. One extraction constant for all finite prime sets

Nest the tensors over the increasing primes above $P$ using the primitive slice
embeddings of the original tensor theorem. By (2), their union has positive-real
Sidon parameter at least $1-2^{-18}$.
[Pisier's Theorem 2](../../../../library/analysis/pisier_1983_arithmetic_characterizations_sidon_sets/_index.md)
applies **once** to that union, giving a single $\delta>0$ for every finite
subset. Any finite prime-tail tensor is a slice of a sufficiently large initial
tensor and inherits this same constant.

Let $M=\prod_{p\leq P}p$, a fixed finite integer. In a tensor containing
small primes, partition a given subset by its small-prime coordinates. There
are at most $M$ slices. One contains at least $1/M$ of the subset;
it is a scalar-tensor copy of a prime-tail configuration. Extract in that
slice. Thus $\delta_0=\delta/M$ works for all distinct-prime tensors.
The constant is small and unquantified, but crucially it is independent of the
finite prime set. No finite-stage sequence of Pisier constants is used.

## 5. Cyclotomic interpretation and prime powers

For squarefree $r$, multiplication identifies
$\bigotimes_{p\mid r}\mathbb Q(\zeta_p)$ with $\mathbb Q(\zeta_r)$:
the map is surjective and both dimensions are
$\prod_{p\mid r}(p-1)=\varphi(r)$. The frequency configuration becomes
exactly the $r$-th roots of unity $\mu_r$. For $p=2$, the two
antipodal columns are dealt with by the small-coordinate slice selection;
the analytic extension never uses $S_2$.

For arbitrary $n$, put $r=\operatorname{rad}(n)$. The $n/r$
distinct multiplicative $\mu_r$-cosets span subspaces
$\zeta\mathbb Q(\zeta_r)$. They sum to $\mathbb Q(\zeta_n)$, and
the sum of their dimensions is
$(n/r)\varphi(r)=\varphi(n)$. Hence their sum is direct: every rational,
and therefore every signed, relation separates by these cosets.

The cyclotomic degree fact is Proposition 1.2 of the checked publisher copy of
[Ramsey–Graham](../../../../library/analysis/ramsey_graham_2006_planar_sidonicity_quasi_independence_multiplicative_subgroups_roots_unity/_index.md),
pp. 330 and 338 of the held copy; the same coset separation is their Theorem
2.12, whose proof was also checked.

Apply $\delta_0$-extraction in each coset and unite the extracted sets.
Coset separation makes the union dissociated. Every finite set of roots of
unity lies in some $\mu_n$, proving the global assertion.
This is ordinary Sidonicity, **not** positive-real Sidonicity of the full
root set: antipodal pairs make its positive-real parameter zero.

## 6. Exact E0774 obligation remaining

Let $p_1=3,p_2=5,\ldots$ be all odd primes, and let
$E_k=\bigotimes_{i\leq k}S_{p_i}$. The proved extraction constant
$\delta_0$ is uniform. These grids have no zero or antipodal pair, so
the positive-integer realization and separated-block assembly apply exactly.
It now suffices to prove

$$
\sup_k\chi_{\rm diss}(E_k)=\infty. \tag{7}
$$

Equation (7) is **unproved**. The divergence of $\sum_p1/p$ only
establishes unbounded rational-independent covering, not (7). The existence
of all regular-polygon relations likewise does not by itself establish a
coloring obstruction. This package does not claim that all roots of unity,
or the associated positive-integer block union, fail a finite dissociated
partition.
