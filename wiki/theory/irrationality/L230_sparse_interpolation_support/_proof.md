---
name: theory/irrationality/L230_sparse_interpolation_support/_proof
title: Counting sparse changes without congruences
desc: |
  Proof of L230. The integer changes to consecutive differences have
  total variation O(N log N) and support o(N/log log N). Uniform support
  bounds give binary-scale covers with arbitrarily small positive
  Hausdorff exponent; countable unions give the full dimension bound.
created: 2026-10-15T21:15:43Z
updated: 2026-10-15T21:15:43Z
---

***

This proves
[[theory/irrationality/L230_sparse_interpolation_support/_index|L230]]
at author-recorded standing. All logarithms are natural.

Write $D=\{n:a_n\ne p_n\}$. Since $D$ has density zero, for every fixed
$\eta>0$ and all sufficiently large $n$ there is an unchanged index
in each of $[(1-\eta)n,n]$ and $[n,(1+\eta)n]$. Monotonicity and
$p_n\sim n\log n$ then imply $a_n\sim p_n$. The series converges,
and for some integer $B\ge1$,

$$
a_n\le Bn\log(n+1),\qquad p_n\le Bn\log(n+1)
\quad(n\ge1).
\tag{1}
$$

We first fix $B$ and take its countable union at the end.

Define integer gap changes, without halving them, by

$$
v_n=(a_{n+1}-a_n)-(p_{n+1}-p_n),\qquad n\ge1.
$$

Their support $E$ is contained in $D\cup\{n:n+1\in D\}$, so
$|E\cap[1,N]|=o(N/\log\log N)$. Positivity of both sets of gaps
and telescoping give, for $N\ge3$,

$$
\sum_{n=1}^N|v_n|
\le a_{N+1}-a_1+p_{N+1}-p_1
\le6BN\log N.
\tag{2}
$$

Fix $\epsilon>0$ and an integer $N_0\ge16$, and restrict to the class
with (1) and

$$
|E\cap[1,N]|\le\frac{\epsilon N}{\log\log N}
\quad(N\ge N_0).
\tag{3}
$$

For each fixed $\epsilon$, every sequence in the class with fixed $B$
satisfies (3) for some $N_0$.

Put $M=\lceil6BN\log N\rceil$ and
$\rho_N=\epsilon/\log\log N$. For all sufficiently large $N$,
$0<\rho_N<1/4$. An integer vector $(v_1,\ldots,v_N)$ with support of
size $t$ has at most $\binom Nt$ choices of support, $2^t$ choices
of signs and $\binom Mt$ choices of positive absolute values with
sum at most $M$. Thus (2)--(3) give the upper bound

$$
\sum_{0\le t\le\lfloor\rho_NN\rfloor}
\binom Nt\,2^t\binom Mt.
\tag{4}
$$

The summand for $t=0$ is $1$. For $1\le t\le\rho_NN$, using
$M\le(6B+1)N\log N$ and $\binom ut\le(eu/t)^t$ gives

$$
\binom Nt\,2^t\binom Mt
\le \left(2e^2(6B+1)\log N\,(N/t)^2\right)^t.
\tag{5}
$$

The logarithm of the right side is increasing as a function of
$t/N$ on $(0,1/4]$. It is therefore at most

$$
\begin{aligned}
N\rho_N\log\frac{2e^2(6B+1)\log N}{\rho_N^2}
&=N\frac{\epsilon}{\log\log N}
 \left(\log\log N+2\log\log\log N+O_{B,\epsilon}(1)\right)\\
&=(\epsilon+o_{B,\epsilon}(1))N.
\end{aligned}
\tag{6}
$$

There are at most $N+1$ summands in (4) and finitely many possibilities
for $a_1$ under (1). The initial value and vector $(v_n)$ determine the
position prefix. Thus the number of prefixes through index $N$ in this
class is at most

$$
\exp\bigl((\epsilon+o_{B,\epsilon}(1))N\bigr).
\tag{7}
$$

Each prefix determines an interval of possible series values of length
at most $C_BN\log N\,2^{-N}$, by (1). For any
$s>\epsilon/\log2$, the sum of the $s$th powers of these covering
lengths is bounded above by

$$
\exp\bigl((\epsilon-s\log2+o_{B,\epsilon,s}(1))N\bigr)
\longrightarrow0.
$$

The definition of Hausdorff dimension gives a bound of
$\epsilon/\log2$ for the values in the class (1), (3). Its countable
union over $N_0$ includes the full class with fixed $B$ and the
required little-oh support bound, so it has the same dimension bound.
Letting $\epsilon\downarrow0$ proves dimension zero for that class.
Taking the countable union over $B$ proves the assertion about $V$.
A fixed exceptional set with the stated size bound gives a subset of
$V$; such a subset cannot contain an interval of positive length.
$\square$
