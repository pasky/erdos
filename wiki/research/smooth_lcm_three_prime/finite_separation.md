---
name: research/smooth_lcm_three_prime/finite_separation
title: The three-prime carry matrix has infinite rank
desc: |
  An elementary derivation of the known finite-separation obstruction,
  using dense fractional parts and triangular carry matrices.
tags: []
sources: []
created: 2026-10-15T16:35:43Z
updated: 2026-10-15T16:35:43Z
---

***

The reciprocal running-lcm term for three distinct primes has square
submatrices of every order on each coordinate face. Consequently it admits
no finite termwise separation across any split of the three exponents.
This is a special case of Will Cook's Theorem 7.3 in
[Running least common multiples: distinct values and multiplicities](https://wcook04.github.io/plectis/maths/papers/erdos269-running-lcm-reasoning-surface--complete.html),
Section 7, revised 5 October 2026, accessed 2026-10-15. That theorem also
makes the selected indices work uniformly at every value of the third
exponent. Its statement and argument were read in HTML and extracted PDF
text; page-image access was unavailable. No formalization or independent
acceptance is imported here.

The elementary derivation below is recorded by Plasma AI without independent
review or a novelty claim. It supports the termwise obstruction in the
[[research/smooth_lcm_three_prime/_index|three-prime sketch]], not an
irrationality conclusion. The local evidence checks finite examples of the
construction. For distinct primes $x,y$ write
$\lambda_{xy}=\log y/\log x$, so that $\log_x(y^k)=k\lambda_{xy}$. Each
$\lambda_{xy}$ is irrational: $\lambda_{xy}=b/a$ with positive integers $a,b$
would give $y^a=x^b$, contradicting unique factorization. Write $\{t\}$ for the
fractional part of a real number $t$.

## The running lcm

Let $m$ be a positive integer whose prime factors lie in $\{p,q,r\}$. For each
of the three primes $w$, the power $w^{\lfloor\log_w m\rfloor}$ is at most $m$
and has its prime factors in $\{p,q,r\}$, so it divides $D(m)$. Conversely,
every positive integer $n\le m$ with prime factors in $\{p,q,r\}$ has
$w$-adic valuation at most $\lfloor\log_w n\rfloor\le\lfloor\log_w m\rfloor$.
Hence

$$
D(m)=p^{\lfloor\log_p m\rfloor}q^{\lfloor\log_q m\rfloor}
     r^{\lfloor\log_r m\rfloor}.
$$

## The face where the exponent at z vanishes

Fix distinct $u,v\in\{p,q,r\}$ with third prime $z$, and let $i,j\ge0$. For
$m=u^iv^j$ the formula gives
$\lfloor\log_u m\rfloor=i+\lfloor j\lambda_{uv}\rfloor$,
$\lfloor\log_v m\rfloor=j+\lfloor i\lambda_{vu}\rfloor$ and
$\lfloor\log_z m\rfloor=\lfloor i\lambda_{zu}+j\lambda_{zv}\rfloor$. Splitting
the last floor,

$$
\lfloor i\lambda_{zu}+j\lambda_{zv}\rfloor
 =\lfloor i\lambda_{zu}\rfloor+\lfloor j\lambda_{zv}\rfloor+e(i,j),
\qquad
e(i,j)=\bigl\lfloor\{i\lambda_{zu}\}+\{j\lambda_{zv}\}\bigr\rfloor\in\{0,1\}.
$$

Therefore

$$
T_{uv}(i,j)=\alpha(i)\,\beta(j)\,z^{-e(i,j)},
$$

with the positive factors

$$
\alpha(i)=u^{-i}v^{-\lfloor i\lambda_{vu}\rfloor}
           z^{-\lfloor i\lambda_{zu}\rfloor},
\qquad
\beta(j)=v^{-j}u^{-\lfloor j\lambda_{uv}\rfloor}
          z^{-\lfloor j\lambda_{zv}\rfloor}.
$$

## A triangular pattern of carry digits

Because $\lambda_{zu}$ and $\lambda_{zv}$ are irrational, the fractional parts
$\{i\lambda_{zu}\}$ for $i\ge1$ are pairwise distinct, nonzero and dense in
$[0,1)$, and the same holds for $\{j\lambda_{zv}\}$ with $j\ge1$; this is the
density of the orbit of an irrational rotation of the circle. Fix $N\ge1$.
Choose $j_1,\ldots,j_N\ge1$ such that $y_t=\{j_t\lambda_{zv}\}$ satisfy

$$
0<y_1<y_2<\cdots<y_N<1,
$$

and put $y_0=0$. For $s=1,\ldots,N$ the interval $(1-y_s,\,1-y_{s-1})$ is a
nonempty open subinterval of $(0,1)$, so there is $i_s\ge1$ with
$x_s=\{i_s\lambda_{zu}\}$ in it. Then $e(i_s,j_t)=1$ exactly when
$y_t\ge1-x_s$. Since $y_{s-1}<1-x_s<y_s$, this happens exactly when $t\ge s$,
and equality $y_t=1-x_s$ never occurs. Hence

$$
e(i_s,j_t)=\begin{cases}1,&t\ge s,\\0,&t<s.\end{cases}
$$

## Invertibility

By the two previous sections,

$$
\bigl(T_{uv}(i_s,j_t)\bigr)_{s,t}
 =\operatorname{diag}\bigl(\alpha(i_s)\bigr)\,M\,
  \operatorname{diag}\bigl(\beta(j_t)\bigr),
\qquad
M_{st}=\begin{cases}z^{-1},&t\ge s,\\1,&t<s.\end{cases}
$$

The diagonal factors are invertible. Subtracting row $s+1$ of $M$ from row $s$
for $s=1,\ldots,N-1$ leaves the multiple $(z^{-1}-1)$ of the $s$-th unit row
vector in row $s$, and the last row $(1,\ldots,1,z^{-1})$. Expanding,

$$
\det M=z^{-1}\bigl(z^{-1}-1\bigr)^{N-1}\ne0,
$$

since $z\ge2$. This proves the first assertion.

## No finite separation

Let $B_1,B_2$ be a partition of $\{p,q,r\}$ into nonempty sets, and suppose
$T=f_1g_1+\cdots+f_Kg_K$ at every exponent triple, with each $f_k$ a function
of the exponents at the primes of $B_1$ and each $g_k$ a function of the
exponents at the primes of $B_2$. Choose $u\in B_1$ and $v\in B_2$, and let $z$
be the third prime, which lies in $B_1$ or in $B_2$. At an exponent triple with
exponent $0$ at $z$, each $f_k$ becomes a function $\varphi_k(i)$ of the
exponent $i$ at $u$ and each $g_k$ a function $\gamma_k(j)$ of the exponent $j$
at $v$, so that

$$
T_{uv}(i,j)=\sum_{k=1}^K\varphi_k(i)\gamma_k(j)
\qquad(i,j\ge0).
$$

For any exponents $i_1,\ldots,i_N$ and $j_1,\ldots,j_N$ the matrix
$(T_{uv}(i_s,j_t))$ is then the product of the $N\times K$ matrix
$(\varphi_k(i_s))$ and the $K\times N$ matrix $(\gamma_k(j_t))$, so its rank
is at most $K$. Taking $N=K+1$ and the exponents of the first assertion gives
an invertible $(K+1)\times(K+1)$ matrix of rank at most $K$, a contradiction.
This proves the second assertion.
