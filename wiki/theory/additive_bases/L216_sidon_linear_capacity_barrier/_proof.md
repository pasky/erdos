---
name: theory/additive_bases/L216_sidon_linear_capacity_barrier/_proof
title: "Proof of the linear-capacity barrier"
desc: "A rotated block-sampling law, exact pair moments, explicit all-N estimates, a simpler infinite family, and the separating-certificate consequence."
created: 2026-10-15T20:05:11Z
updated: 2026-10-15T20:05:11Z
---

***

This is a complete author-recorded proof of
[[theory/additive_bases/L216_sidon_linear_capacity_barrier/_index|L216]].

## The block law and its pair moments

Partition the cycle $\mathbb Z_N$ into $B\ge3$ consecutive blocks of lengths
$\ell_b\in\{Q,Q+1\}$, where $Q=\lfloor N/B\rfloor\ge2$. Choose integer
occupancies $m_b\in\{\lfloor k/B\rfloor,\lceil k/B\rceil\}$ summing to $k$,
with $0\le m_b\le\ell_b$. Independently choose a uniform $m_b$-subset of each
block, take their union, and rotate it by an independent uniform element of
$\mathbb Z_N$. Read the resulting set in $\{0,\ldots,N-1\}$. This always
has exactly $k$ points.

Put $y=k/N$ and let $p_t=m_b/\ell_b$ when $t$ lies in block $b$. Set

$$
c_b=\frac{p_b(1-p_b)}{\ell_b-1},\qquad p_b=\frac{m_b}{\ell_b}.
$$

Before rotation, two different positions in the same block have joint
inclusion probability $p_b^2-c_b$; positions in different blocks have joint
probability $p_t p_{t'}$. Hence after rotation the one-point probability is
$y$, and the two-point probability at cyclic separation $d\ne0$ is

$$
X(d)=\frac1N\sum_{t\in\mathbb Z_N}p_t p_{t+d}
     -\frac1N\sum_b c_b n_b(d),                         \tag{1}
$$

where $n_b(d)$ counts positions $t$ for which both $t$ and $t+d$ lie in
block $b$. In particular, if $1\le d<Q$ and $2Q+1<N$, then
$n_b(d)=\ell_b-d\ge Q-d$.

The average of $p_t-y$ is zero. Since
$|m_b-k/B|\le1$ and $|\ell_b-N/B|\le1$,

$$
|p_t-y|\le\frac{1+y}{Q}\le\frac2Q\quad\text{when }y\le1.
$$

Applying Cauchy--Schwarz to the cyclic correlation of these errors gives

$$
\frac1N\sum_t p_t p_{t+d}\le y^2+\frac4{Q^2}.          \tag{2}
$$

Suppose $A_0=y(1-y)-2/Q>0$. Because $|p_b-y|\le2/Q$,
$p_b(1-p_b)\ge y(1-y)-2/Q$: the map $v\mapsto v(1-v)$ is
$1$-Lipschitz on $[0,1]$. Also $\ell_b-1\le Q$. Thus (1)--(2) imply

$$
X(d)\le y^2+\frac4{Q^2}
       -\frac{B(Q-d)}{NQ}A_0\quad(1\le d<Q),           \tag{3}
$$

and $X(d)\le y^2+4/Q^2$ for every $1\le d<N$. The ordinary difference
count consequently satisfies $\mathbb E r_A(d)=(N-d)X(d)$.

## Explicit estimates for every large interval

Let $u=N^{1/4}\ge32$, $B=\lfloor u\rfloor$, $Q=\lfloor N/B\rfloor$, and
assume

$$
u^2\le k\le u^2+\frac u2-10.
$$

The indicated occupancies exist: $m_b\le k/B+1\le3u<Q$, while $m_b\ge0$.
We have $B\le u$, $B\ge u-1$, $Q\ge u^3-1$, $BQ\le N$ and $2Q+1<N$.
The elementary estimates

$$
y\ge u^{-2},\quad y\le2u^{-2},\quad y^2\le2u^{-4},
\quad \frac{2B}{Q}\le3u^{-2},\quad
\frac{4N}{Q^2}\le5u^{-2}                              \tag{4}
$$

hold for $u\ge32$. They also give
$A_0\ge u^{-2}-3u^{-3}-2u^{-4}>0$.

Put $w=k^2-N$. Since $0\le k-u^2\le u/2-10$,

$$
0\le w\le u^3-\frac{79}{4}u^2-10u+100
           \le u^3-\frac{79}{4}u^2.                   \tag{5}
$$

For $1\le d<Q$, multiply (3) by $N-d$, bound $N-d\ge N-Q$ in its
nonnegative subtracted term, and use
$(N-d)y^2\le1+(w-d)/N$. This gives the affine upper bound

$$
\mathbb E r_A(d)\le U(d):=
1+\frac{w-d}{N}+\frac{4N}{Q^2}
 -\left(1-\frac QN\right)B A_0\left(1-\frac dQ\right).
                                                               \tag{6}
$$

It is enough to check $d=0,Q$. First,

$$
\left(1-\frac QN\right)B A_0
\ge By-By^2-\frac{2B}{Q}-\frac{BQ}{N}y
\ge u^{-1}-7u^{-2},                                  \tag{7}
$$

using (4), $By\ge u^{-1}-u^{-2}$ and $2u^{-3}\le u^{-2}$. Equations
(4)--(7) yield

$$
U(0)\le1-\frac{31}{4}u^{-2},\qquad
U(Q)\le1-\frac{59}{4}u^{-2}+u^{-4}
       \le1-14u^{-2}.
$$

Thus $\mathbb E r_A(d)\le1-7u^{-2}$ for $1\le d<Q$. For $d\ge Q$, omit
the nonnegative depletion in (1) and use

$$
(N-d)X(d)\le(N-Q)(y^2+4/Q^2)\le U(Q).
$$

This proves every difference capacity, with the stated margin.

For any integer $s$, there are at most $N/2$ pairs $i<j$ with $i+j=s$ and
at most one diagonal pair. Therefore

$$
\mathbb E\sigma_A(s)
\le\frac{k^2}{2N}+\frac{2N}{Q^2}+y
\le\frac12+\frac1{2u}+\frac{9}{2u^2}<\frac34.         \tag{8}
$$

This proves the theorem for $k\ge\sqrt N$. For smaller positive $k$, first
construct the law at $K=\lceil\sqrt N\rceil$, which lies in the permitted
range because $u\ge32$, and choose a uniform $k$-subset of its set. Each
pair probability is multiplied by $k(k-1)/(K(K-1))\le1$ and each one-point
probability by $k/K\le1$. Both kinds of capacities therefore remain at most
one.

## An exact infinite family

For an integer $s\ge2$, put

$$
B_0=s^2-s+1,\qquad W=sB_0,\qquad N=sW,\qquad k=s^2.
$$

Use $s$ equal blocks of length $W$, with $s$ points in each, and rotate.
Here $y=s/W=1/B_0$ and the pair moment is exactly

$$
X(d)=y^2-\lambda\max(W-r(d),0),\qquad
\lambda=\frac{y-y^2}{W(W-1)},\qquad
r(d)=\min(d,N-d).                                    \tag{9}
$$

For $s=2$ the same formula holds with $W=N/2$: the two possible orientations
inside a half-cycle are disjoint. For $s>2$ it follows directly by counting
the rotations which place both points in the same block.

Writing $w=k^2-N=W-s$, one has $\lambda\ge N^{-2}$. Indeed this is
equivalent to $W(W-1)\le s^3(W-s)$, whose right side minus left side equals

$$
s\bigl((s-2)(s^3-s^2+s)+1\bigr)>0.
$$

For $d<W$, (9) gives

$$
(N-d)X(d)\le\frac{(N-d)(N-s+d)}{N^2}<1.
$$

For $d\ge W$, omit the depletion and use
$(N-d)y^2\le(N-W)(N+w)/N^2<1$, since $w<W$.
The sum-capacity bound is $Ny^2/2+y=(s^2+2)/(2B_0)\le1$ for $s\ge2$.
Finally,

$$
\sqrt N=s^2-\frac s2+\frac38+O(s^{-1}),\qquad
N^{1/4}=s-\frac14+O(s^{-1}),
$$

so $(k-\sqrt N)/N^{1/4}\to1/2$.

## Certificate consequence

More explicitly, suppose nonnegative numbers $\alpha_d,\beta_s$, a real
$\gamma$, and a function $\Psi$ on the $k$-subsets satisfy, for every such
subset,

$$
\Psi(A)\le\sum_d\alpha_dr_A(d)+\sum_s\beta_s\sigma_A(s)+\gamma,
\qquad
\Psi(A)>\sum_d\alpha_d+\sum_s\beta_s+\gamma.
$$

Taking expectations under the constructed law contradicts these two
inequalities. The first inequality may use any facts valid for all
$k$-subsets, including integrality, arbitrary-degree positivity and
combinatorial restrictions. Its obstruction is specifically the linear use
of the Sidon capacities. A proof using a disjunction of certificates depending
on the set is not asserted to have this form.
