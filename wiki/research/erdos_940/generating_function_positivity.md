---
name: research/erdos_940/generating_function_positivity
title: Positivity tests at generating-function singularities
desc: Fixed finite singularity-positivity tests are exactly progression first-moment tests and cannot contradict quintic cofiniteness.
tags: []
sources: []
created: 2026-09-23T00:59:15Z
updated: 2026-09-23T00:59:15Z
---


# Positivity tests at generating-function singularities

***

## The attempted mechanism

If every sufficiently large integer is representable, subtracting the
generating function of an integer tail from the representation generating
function leaves nonnegative coefficients. This gives positive-semidefinite
matrices at arbitrary collections of angles, apparently stronger than
individual progression counts. The idea was to contradict this positivity
using the exact power tracks and their singularities.

The calculation below proves that every **fixed finite** test involving
rational or irrational limiting angles and $O(t)$ angular offsets reduces
to the existing progression first moments. For the quintic problem, the
strict first-moment floor makes every such matrix eventually strictly
positive definite, without assuming cofiniteness. This rules out that
analytic test, not a generating-function argument of growing complexity.

## 1. The exact boundary limits

Fix $r\ge3$. Let

$$
A(z)=\sum_{n\in\mathcal P_r}z^n,\qquad
U(z)=\sum_{n\ge1}R(n)z^n,
$$

where $R(n)$ counts unordered representations with between one and $r$
positive $r$-powerful summands. Write $m$ for probability Haar measure
on $\widehat{\mathbb Z}$, $\gamma=\Gamma(1+1/r)$, and define finite measures

$$
\kappa=\sum_{d\in\mathcal C_r}d^{-1/r}(x\mapsto dx^r)_*m,
\qquad \mu=\frac{\gamma^r}{r!}\kappa^{*r}.
\tag{1}
$$

The [canonical weight](finite_core_reduction.md) makes the series converge.
For $h\in\mathbb Q/\mathbb Z$, use
$\widehat\mu(h)=\int\chi_h(z)\,d\mu(z)$, where $\chi_h$ is the corresponding
profinite additive character.

For fixed $h=a/q$ and fixed real $u$,

$$
\lim_{t\downarrow0}t\,U(e^{-t+i(2\pi h+tu)})
=\frac{\widehat\mu(h)}{1-iu}.
\tag{2}
$$

Indeed, the canonical expansion of $A$ and a Riemann sum on root residues
modulo $q$ give

$$
t^{1/r}A(e^{-t+i(2\pi h+tu)})\longrightarrow
\gamma(1-iu)^{-1/r}
\sum_d d^{-1/r}\frac1q\sum_{b\bmod q}e(adb^r/q).
$$

The dominating bound for the $d$-term is

$$
t^{1/r}\sum_{x\ge1}e^{-tdx^r}\le\gamma d^{-1/r},
$$

obtained by integrating a decreasing function. It justifies the infinite
core sum. The finite multiset cycle-index formula gives, uniformly in
the argument of $z$ with $|z|=e^{-t}$,

$$
U(z)=A(z)^r/r!+O_r(t^{-(r-1)/r}).
\tag{3}
$$

Every other monomial in the power sums $A(z^j)$ has at most $r-1$
factors, each $O_r(t^{-1/r})$. Equations (1)–(3) prove (2).

For every fixed irrational $\alpha$ and real $u$,

$$
t\,U(e^{-t+i(2\pi\alpha+tu)})\longrightarrow0.
\tag{4}
$$

For each fixed core, the polynomial sequence $e(\alpha d x^r)$ has
vanishing mean. This follows by induction using van der Corput
differencing, starting from the geometric-sum bound for an irrational
linear phase. Partial summation with the weight
$e^{-(1-iu)tdx^r}$ gives the corresponding zero limit for
$t^{1/r}A$. The same core majorant and (3) prove (4).

Fixed-core lattice counting also identifies

$$
\lim_{X\to\infty}\frac qX
\sum_{\substack{n\le X\\n\equiv a\ (q)}}R(n)
=q\mu(a+q\widehat{\mathbb Z}).
\tag{5}
$$

The archimedean volume is $\gamma^r$, and the core weights are summable.
Repeated summands and shorter representations contribute $o(X)$.

## 2. Positive definiteness adds no fixed-scale condition

If $S_r$ were cofinite, then for some fixed $N$ the function

$$
H_N(z)=U(z)-\frac{z^N}{1-z}
$$

would have nonnegative coefficients. Therefore, for any finite collection
of angles $\theta_j(t)$, the Hermitian matrix

$$
B_t(i,j)=tH_N(e^{-t+i(\theta_j(t)-\theta_i(t))})
\tag{6}
$$

would be positive semidefinite. Its quadratic form is

$$
t\sum_{n\ge0}[z^n]H_N(z)e^{-tn}
\left|\sum_j v_j e^{in\theta_j(t)}\right|^2.
$$


Take $\theta_j(t)=2\pi h_j+tu_j$, with rational $h_j$.
Equations (2) and the elementary limit for $z^N/(1-z)$ show that
the limiting kernel is

$$
K(h,u)=\frac{\widehat\nu(h)}{1-iu},\qquad \nu=\mu-m.
\tag{7}
$$

This kernel is positive definite **if and only if** $\mu\ge m$.
For sufficiency, its quadratic form is

$$
\int_{\widehat{\mathbb Z}}\int_0^\infty e^{-x}
\left|\sum_jv_j\chi_{h_j}(z)e^{iu_jx}\right|^2\,dx\,d\nu(z).
$$

For necessity set all $u_j=0$ and take $h_j=j/q$.
Discrete Fourier diagonalization gives the eigenvalues
$q\mu(a+q\widehat{\mathbb Z})-1$. Nonnegativity for every $q,a$
means $\nu$ is nonnegative on every clopen cylinder, hence is a positive
measure. By (5), this is precisely the condition that every progression
first moment be at least one.

At the critical number of summands, the archimedean factor is the
positive Laplace kernel $(1-iu)^{-1}$. It therefore adds no condition
to positivity of the profinite measure.

## 3. Strict blindness in the quintic case

Suppose for some $\delta>0$ that every progression mean is at least
$1+\delta$. Then $\nu\ge\delta m$. Fix $N$ and any finite collection
of distinct pairs

$$
(\alpha_j,u_j)\in(\mathbb R/\mathbb Z)\times\mathbb R,
\qquad \theta_j(t)=2\pi\alpha_j+tu_j.
$$

The actual matrices (6) are strictly positive definite for sufficiently
small $t$, **whether or not** $S_r$ is cofinite.

Partition the indices according to rational differences of their
$\alpha_j$. Irrational differences give zero limiting entries by (4).
Within a block write $\alpha_j=\alpha_0+h_j$, with rational $h_j$.
The limiting quadratic form is bounded below by

$$
\delta\sum_h\int_0^\infty e^{-x}
\left|\sum_{j:h_j=h}v_j e^{iu_jx}\right|^2dx.
$$

Within each equal-$h$ group, distinct pairs have distinct $u_j$.
Linear independence of these exponentials makes this expression strictly
positive for every nonzero vector. Entrywise convergence of a fixed
finite matrix then proves the assertion.

The [quintic lower bound](quintic_first_moment_barrier.md) exceeds $2.468$,
so it supplies such a $\delta$ unconditionally. Lower-order terms cannot
overcome this positive limiting spectral margin in a fixed test.

The qualifications are essential: $N$, the matrix size, and the pairs
$(\alpha_j,u_j)$ are fixed. Growing denominators, increasing matrix size,
or other frequencies depending on $t$ are not covered. No statement
about nonnegativity of the actual coefficients, or absence of missing
integers, has been proved.
