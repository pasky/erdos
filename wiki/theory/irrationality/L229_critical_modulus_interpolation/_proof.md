---
name: theory/irrationality/L229_critical_modulus_interpolation/_proof
title: Sparse gap corrections and Hausdorff covers
desc: |
  Proof of L229. At logarithmic congruence moduli, the integer
  quotients of gap corrections have linear total variation and sparse
  support. Counting these quotients gives interval covers of the series
  values with arbitrarily small positive Hausdorff exponent.
created: 2026-10-15T21:06:12Z
updated: 2026-10-15T21:06:12Z
---

***

This proves
[[theory/irrationality/L229_critical_modulus_interpolation/_index|L229]]
at author-recorded standing. Logarithms are natural. We use the following
form of the definition of Hausdorff dimension: if a set admits interval
covers with maximum length tending to zero and the sum of the $s$th
powers of the lengths tending to zero, its dimension is at most $s$.
Dimension is stable under countable unions, in the sense that the
dimension of the union is the supremum of the dimensions.

## Growth and the sparse integer vector

Let $(a_n)$ be one of the sequences in the statement, and put
$D=\{n:a_n\ne p_n\}$. For each fixed $0<\eta<1$, density zero provides,
for all sufficiently large $n$, indices outside $D$ in both
$[(1-\eta)n,n]$ and $[n,(1+\eta)n]$. Monotonicity and the prime number
theorem sandwich $a_n/p_n$ between $1-\eta+o(1)$ and
$1+\eta+o(1)$. Thus

$$
a_n\sim p_n\sim n\log n.
\tag{1}
$$

In particular the series converges. For some integer $B\ge1$,

$$
a_n\le Bn\log(n+1),\qquad p_n\le Bn\log(n+1)
\quad(n\ge1).
\tag{2}
$$

We first restrict to the class with a fixed $B$; the full class is its
countable union over $B$.

For $n\ge2$ put

$$
h_n=\frac{p_{n+1}-p_n}{2},\qquad
h'_n=\frac{a_{n+1}-a_n}{2},\qquad
s_n=\frac{h'_n-h_n}{q_n}.
\tag{3}
$$

These are integers: $a_n$ is odd for $n\ge2$, and the two position
differences $a_n-p_n$ and $a_{n+1}-p_{n+1}$ are divisible by $2q_n$,
because $q_n\mid q_{n+1}$. Both $h_n$ and $h'_n$ are positive. The
support $E=\{n\ge2:s_n\ne0\}$ is contained in
$D\cup\{n:n+1\in D\}$, so $E$ has density zero. Moreover, for $N\ge3$,

$$
\begin{aligned}
\sum_{n=2}^N q_n|s_n|
&\le\sum_{n=2}^N(h'_n+h_n)\\
&=\frac{a_{N+1}-a_2+p_{N+1}-p_2}{2}
\le3BN\log N.
\end{aligned}
\tag{4}
$$

For sufficiently large $N$, all $n\ge\lceil\sqrt N\rceil$ satisfy
$q_n\ge c\log n\ge(c/2)\log N$. Consequently

$$
\sum_{n=\lceil\sqrt N\rceil}^N|s_n|\le C_BN,
\qquad C_B=\max(1,6B/c).
\tag{5}
$$

For the earlier coordinates, (4) and $q_n\ge1$ give the crude but
sufficient individual bound $|s_n|\le3BN\log N$.

## Counting prefixes uniformly

Fix $0<\rho<1/4$ and an integer $N_0$. Restrict the class further by
requiring

$$
|E\cap[2,N]|\le\rho N\qquad(N\ge N_0).
\tag{6}
$$

Every sequence in the class with fixed $B$ belongs to one of these
classes for some $N_0$, for each fixed $\rho$.

There are only finitely many choices of $a_1,a_2$ under (2). The first
$\lceil\sqrt N\rceil$ coordinates of $(s_n)$ have at most

$$
(6BN\log N+1)^{\lceil\sqrt N\rceil}=\exp(o_B(N))
\tag{7}
$$

possibilities. For the remaining coordinates, put
$M=\lceil C_BN\rceil$. A vector with support of size $t$ has at most
$\binom Nt$ choices of support and $2^t$ choices of signs. The number
of positive integer $t$-tuples with sum at most $M$ is
$\binom Mt$, including the value $1$ when $t=0$. By (5)--(6), an upper
bound for their total number is therefore

$$
\sum_{0\le t\le\lfloor\rho N\rfloor}
 \binom Nt\,2^t\binom Mt.
\tag{8}
$$

For $1\le t\le\rho N$ the usual bound
$\binom ut\le(eu/t)^t$ and $M\le(C_B+1)N$ give

$$
\binom Nt\,2^t\binom Mt
\le\left(2e^2(C_B+1)(N/t)^2\right)^t
\le\exp\bigl(Nf_B(\rho)\bigr),
\tag{9}
$$

where

$$
f_B(\rho)=\rho\log\frac{2e^2(C_B+1)}{\rho^2}
\longrightarrow0\quad(\rho\downarrow0).
$$

The last inequality follows because
$u\log(2e^2(C_B+1)/u^2)$ is increasing for $0<u\le1/4$.
Equations (7)--(9), with the at most $N+1$ summands in (8), show that
the number of possible prefixes through index $N$ is at most

$$
\exp\bigl(Nf_B(\rho)+o_B(N)\bigr).
\tag{10}
$$

Here we may count vectors through gap index $N$, since this only
overcounts position prefixes through $N$. Each vector and $a_1,a_2$
determine the corresponding position prefix by (3). Ignoring positivity
or congruence restrictions in the upper count causes no difficulty.

## Covers of the series values

By (2), the tail after index $N$ is bounded uniformly in this class by

$$
0\le\sum_{n>N}\frac{a_n}{2^n}
\le C'_B N\log N\,2^{-N}
\tag{11}
$$

for a constant $C'_B$. Each prefix counted in (10) therefore specifies
one interval of this length covering all its series values. For any
$s>f_B(\rho)/\log2$, the sum of the $s$th powers of these lengths is
at most

$$
\exp\bigl(N(f_B(\rho)-s\log2)+o_{B,s}(N)\bigr)
\longrightarrow0.
\tag{12}
$$

Thus the set of series values in the class (2), (6) has Hausdorff
dimension at most $f_B(\rho)/\log2$. Taking its countable union over
$N_0$ gives the same bound for the entire class with fixed $B$.
As $\rho$ can tend to zero, that class has dimension zero. Finally take
the countable union over $B$. This proves L229. $\square$
