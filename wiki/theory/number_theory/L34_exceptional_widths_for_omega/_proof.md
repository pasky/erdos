---
name: theory/number_theory/L34_exceptional_widths_for_omega/_proof
title: Enlarging widths only on exceptional locations
desc: A dyadic second-moment argument bounds the count at ordinary locations and identifies a density-zero set where large widths are harmless.
created: 2026-10-14T18:42:37Z
updated: 2026-10-14T18:42:37Z
---

***

Write $\omega(n)$ for the number of distinct prime divisors of $n$, with
$\omega(1)=0$. The external input is
[[../library/arithmetic_functions/erdos_1997_locally_repeated_values_arithmetic_functions_iv/lemma_1|Erdős–Pomerance–Sárközy Lemma 1]]:
with modulus $m=1$, additive function $\omega$ and $K=1$, it gives for $X\ge2$

$$
\sum_{n\le X}(\omega(n)-A(X))^2\ll X(A(X)+1),
\qquad A(X)=\sum_{p\le X}\frac1p.                 \tag{1}
$$

The condition concerning primes dividing the modulus is vacuous.
The function is nonnegative and additive, and $\omega(p^a)=1$.
Euler's divergence of the prime reciprocal sum implies $A(X)\to\infty$;
the elementary bound $A(X)\le1+\log X$ will also suffice below.

For sufficiently large integers $j$, put

$$
X_j=2^{j+2},\quad A_j=A(X_j),\quad H_j=\lceil A_j^{3/4}\rceil,
\quad
D_j=\{1\le n\le X_j:|\omega(n)-A_j|>H_j\}.
$$

By (1) and Chebyshev's inequality,

$$
|D_j|\ll X_j\frac{A_j+1}{H_j^2}=o(2^j).          \tag{2}
$$

For an integer $u\in[2^j,2^{j+1})$, let $b_j(u)$ count those $n\in D_j$
whose image $n+\omega(n)$ belongs to $(u,u+H_j+1)$. Each integer image
belongs to at most $H_j+1$ of these windows. Hence

$$
\sum_{2^j\le u<2^{j+1}} b_j(u)\le(H_j+1)|D_j|.
$$

Set $E_j=\{u\in[2^j,2^{j+1})\cap\mathbb Z:b_j(u)>H_j+1\}$.
Then $|E_j|\le|D_j|=o(2^j)$. Both the union $E=\bigcup_jE_j$ and

$$
D=\bigcup_j(D_j\cap[2^j,2^{j+1}))
$$

have natural density zero. Indeed, for any $\varepsilon>0$ their
dyadic counts are at most $\varepsilon2^j$ for all sufficiently large
$j$. Summing complete dyadic intervals and bounding the last partial
one by its whole interval gives at most $2\varepsilon x+O(1)$ elements
below $x$.

If $u\notin E_j$, consider all positive integers $n$ with
$n+\omega(n)\in(u,u+H_j+1)$. They satisfy $n\le X_j$ for sufficiently
large $j$, since $\omega(n)\ge0$ and
$2^{j+1}+H_j+1<2^{j+2}$. The latter inequality follows from
$H_j=O((j+1)^{3/4}+1)$. Those $n$ outside $D_j$ obey

$$
u-A_j-H_j<n<u+2H_j+1-A_j.
$$

There are at most $3H_j+2$ integers in this interval. The exceptional
inputs contribute at most $b_j(u)\le H_j+1$. The whole count is thus
at most $4H_j+3$.

For real $x\ge1$, put $u=\lfloor x\rfloor$ and choose the dyadic
index $j$ with $2^j\le u<2^{j+1}$. Define

$$
F(x)=
\begin{cases}
H_j,&u\notin E_j,\\
2(u+1),&u\in E_j.
\end{cases}                                                     \tag{3}
$$

For the finitely many initial $u$ not covered by the construction use
the second alternative. Both alternatives tend to infinity with $x$.
At a nonexceptional location,
$(x,x+F(x))\subset(u,u+H_j+1)$, so the normalized count is at most
$4+3/H_j\le7$. At an exceptional location, every counted positive
integer satisfies $n<x+F(x)<3(u+1)$. Its normalized count is therefore
less than $3/2$. This proves the asserted bound at every sufficiently
large real location, including nonintegral ones.

Finally, let $G$ be the positive integers outside $E\cup D$, omitting
the finitely many initial values. This set has natural density one.
For $u\in G\cap[2^j,2^{j+1})$, eventually

$$
\omega(u)\ge A_j-H_j\ge A_j/2,
\qquad
\frac{F(u)}{\omega(u)}\le\frac{2H_j}{A_j}\longrightarrow0.
$$

Thus (3) satisfies the density-one width condition but its normalized
image count cannot tend to infinity along any sequence of locations.
This establishes L34 exactly as stated.
