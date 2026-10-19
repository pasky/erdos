---
name: research/erdos_940/metric_coefficients
title: Real coefficient averaging and the rational-coefficient obstruction
desc: Almost all real rounded forms have positive upper density, but a fixed polylogarithmic perturbation of powers can make every rational coefficient tuple exceptional.
tags: []
sources: []
created: 2026-09-22T03:06:14Z
updated: 2026-09-23T01:47:49Z
---


# Real coefficient averaging and the rational-coefficient obstruction

***

## Status

The metric theorem below is proved and author-recorded. It concerns **rounded
real values**, not sums of powerful integers. In particular, it supplies no
rational or integral coefficient tuple and does not resolve Erdős 940. The
[finite-core reduction](finite_core_reduction.md) still requires a fixed
integral diagonal form.

## A log-free averaged estimate

**Theorem.** Let $r\ge3$ be an integer. For Lebesgue-almost every
$\mathbf a\in[1,2]^r$, the set


$$
\left\{\left\lfloor\sum_{i=1}^r a_i x_i^r\right\rfloor:
x_1,\ldots,x_r\in\mathbb N\right\}
$$


has positive upper natural density.

For $N\ge1$, put


$$
Q_{\mathbf a}(N)=\#\left\{\mathbf x,\mathbf y\in[1,N]^r\cap\mathbb Z^r:
\left|\sum_i a_i(x_i^r-y_i^r)\right|\le1\right\}.
$$


We prove the uniform estimate


$$
\int_{[1,2]^r}Q_{\mathbf a}(N)\,d\mathbf a\ll_r N^r.
\tag{1}
$$


First, for $T\ge1$,


$$
B(N,T):=\#\{1\le u,v\le N:0<|u^r-v^r|\le T\}
\ll_r T^{2/r}.
\tag{2}
$$


By symmetry suppose $u>v$. If $v\le T^{1/r}$, then $u^r\le v^r+T\le2T$, giving
$O_r(T^{2/r})$ pairs. Otherwise


$$
u^r-v^r\ge r v^{r-1}(u-v),
$$


so summing the upper bound $T/(rv^{r-1})$ over $v>T^{1/r}$ proves (2). Here
$r>2$ is essential.

For distinct vectors define $D=\max_i|x_i^r-y_i^r|$. Equation (2) implies


$$
\#\{\mathbf x\ne\mathbf y:D\le T\}
\le (N+C_rT^{2/r})^r-N^r.
\tag{3}
$$


For any fixed distinct pair, hold all but a coefficient corresponding to a
maximal difference fixed. The allowed interval in that coefficient has length at
most $2/D$. Thus its slab in $[1,2]^r$ has measure at most $2/D$.

Divide $1\le D\le N^r$ into dyadic intervals and expand (3). The off-diagonal
contribution to (1) is at most a constant depending on $r$ times


$$
\sum_{j=1}^r N^{r-j}
\sum_{k=0}^{\lceil\log_2 N^r\rceil}2^{k(2j/r-1)}.
\tag{4}
$$


The $j$th term is $O_r(N^{r-j})$ when $2j<r$, $O_r(N^{r/2}\log(2N))$ when
$2j=r$, and $O_r(N^j)$ when $2j>r$. All are $O_r(N^r)$. The diagonal contributes
exactly $N^r$, proving (1).

Fatou's lemma gives


$$
\int_{[1,2]^r}\liminf_{N\to\infty}\frac{Q_{\mathbf a}(N)}{N^r}\,d\mathbf a<\infty.
$$


Consequently, for almost every $\mathbf a$, there are a finite constant
$C_{\mathbf a}$ and arbitrarily large $N$ with
$Q_{\mathbf a}(N)\le C_{\mathbf a}N^r$. Equal rounded values have unrounded
difference less than one. Cauchy--Schwarz therefore gives at least
$N^r/C_{\mathbf a}$ distinct rounded values from $[1,N]^r$. They are at most
$2rN^r$, proving positive upper density.

## Why this does not produce integral coefficients

The exceptional set in the theorem may contain every rational vector.
Approximating coefficients separately at finite scales gives no fixed rational
vector that works along an unbounded sequence.

There is also a precise obstruction to replacing the continuous measure in the
proof by a discrete distribution. Suppose a measure has an atom of mass $p>0$ at
a rational vector $\mathbf a$. Choose a nonzero integer vector $\mathbf v$ with
$\mathbf a\cdot\mathbf v=0$. Then for every positive integer $k$,


$$
\mu\{\mathbf b:|\mathbf b\cdot(k\mathbf v)|\le1\}\ge p.
$$


Thus no uniform slab bound $C/\|k\mathbf v\|_\infty$ is available. This excludes
that termwise replacement, not every arithmetic averaging argument: requiring
$k\mathbf v$ to be an actual vector of power differences restores a difficult
Diophantine condition.

More directly, if a countable weighted average over rational coefficient vectors
satisfied


$$
\sum_j p_j E_{\mathbf a_j}(N)\le C N^r,
\qquad p_j>0,
$$


along a common unbounded sequence, then positivity would already imply
$E_{\mathbf a_j}(N)\le(C/p_j)N^r$ for **every** supported vector. Such an
estimate contains the individual arithmetic energy theorem; the probabilistic
extraction does not bypass it.

## What an adaptive arithmetic average would need

There is a precise conditional extraction criterion for the weaker
logarithmic moment. For a positive rational coefficient tuple $\mathbf a$,
let

$$
L_{\mathbf a}(N)=N^{-r}\sum_v R_{\mathbf a,N}(v)
\log R_{\mathbf a,N}(v),
$$

where the sum is over its exact rational output values, not rounded ones.
Suppose probability measures $\mu_N$ on the countable set of rational
tuples satisfy $\sum_{\mathbf a}\mu_N(\mathbf a)L_{\mathbf a}(N)\le C$.
If one **fixed finite set** $K$ has $\mu_N(K)\ge\eta>0$ at arbitrarily
large $N$, then some fixed $\mathbf a\in K$ has
$L_{\mathbf a}(N)\le C/\eta$ along an unbounded subsequence. Select such a
tuple in $K$ at each scale and use finite pigeonhole. The logarithmic
multiplicity criterion gives positive upper density after clearing its
fixed denominators.

A uniformly bounded moment of a proper arithmetic height, whose bounded
sublevel sets are finite, would guarantee this discrete tightness by
Markov's inequality. Ordinary weak compactness in a real or $p$-adic
coefficient space does not guarantee it: measures can escape every finite
arithmetic set. No adaptive average satisfying both the moment estimate
and this tightness condition was constructed. This is a conditional
criterion, not a new positive-density theorem.

## A fixed sequence for which every rational tuple is exceptional

The following countermodel has been checked. It concerns a perturbation
of powers, **not** actual powerful numbers. It shows that the difference
estimate used in the metric proof, very accurate approximation to powers,
and all eventual fixed congruences do not suffice for rational extraction.

**Proposition.** For every integer $r\ge3$ there is a strictly increasing
sequence of positive integers $f(n)$ with the following properties:

1. $f(n)=n^r+O((\log n)^{1+o(1)})$.
2. For each fixed $m$, $f(n)\equiv n^r\pmod m$ for all sufficiently large $n$.
3. Uniformly for $N,T\ge1$,

$$
   \#\{u,v\le N:0<|f(u)-f(v)|\le T\}\ll_r T^{2/r}.
   \tag{5}
$$

4. For every fixed positive integral coefficient tuple $\mathbf a$,

$$
   \#\{v\le X:v=\textstyle\sum_{i=1}^r a_i f(x_i)
             \text{ for some }x_1,\ldots,x_r\in\mathbb N\}=o(X), \tag{6}
$$

   where the left side counts distinct values.

Nevertheless, the rounded values $\lfloor\sum_i a_i f(x_i)\rfloor$
have positive upper density for almost every real
$\mathbf a\in[1,2]^r$.

**Construction.** For integers $k\ge0$, put

$$
m_k=\max\{1,\lfloor\log\log(k+e^e)\rfloor\},\quad
M_k=\operatorname{lcm}(1,\ldots,m_k),\quad
q_k=2^{\lfloor\log_2(k+1)\rfloor}M_k.
$$

Both $M_k$ and $q_k$ divide their successors. Also
$M_k\le m_k!$ implies $\log M_k=o(\log k)$, whence
$q_k=k^{1+o(1)}$. On $2^k\le n<2^{k+1}$, define, apart from finitely
many initial inputs,

$$
f(n)=q_k\left\lfloor\frac{n^r}{q_k}\right\rfloor
                   +(n^r\bmod M_k),                            \tag{7}
$$

using the least nonnegative residue. Since $M_k\mid q_k$,

$$
0\le n^r-f(n)<q_k.
\tag{8}
$$

This proves property 1 and the required congruence modulo $M_k$.
Since $m_k\to\infty$, property 2 follows.

For sufficiently large $n$, even across block boundaries, the total
possible change of the error in (8) is smaller than half of
$(n+1)^r-n^r$. Start (7) beyond such a point and set $f(n)=n^r$
at the finitely many earlier inputs. The transition also obeys this
inequality after choosing the starting point sufficiently large.
We obtain positive integers and

$$
f(n+1)-f(n)\ge\tfrac12((n+1)^r-n^r)
$$

for every $n$. Hence for $u>v$,
$f(u)-f(v)\ge(u^r-v^r)/2$; the already proved power-difference estimate
(2), with $2T$ in place of $T$, proves (5).

**Rational-coefficient value count.** Fix $\mathbf a$ and an integer
$J\ge1$, and write $2^K\le N<2^{K+1}$. If all $x_i>2^{K-J}$,
their block indices lie between $K-J$ and $K$. By nested divisibility,
each $f(x_i)$ is a multiple of $q_{K-J}$ plus an integer in $[0,M_K)$.
Consequently $\sum_i a_i f(x_i)$ occupies at most
$O_{\mathbf a}(M_K)$ residue classes modulo $q_{K-J}$.
All these sums are $O_{\mathbf a}(N^r)$, so they contribute at most

$$
O_{\mathbf a}\left(N^r\frac{M_K}{q_{K-J}}+M_K\right)
\tag{9}
$$

distinct values.

For fixed $J$, eventually $m_K-m_{K-J}\le1$. Therefore
$M_K/M_{K-J}\le m_K$, while
$2^{\lfloor\log_2(K-J+1)\rfloor}\gg K$. Thus
$M_K/q_{K-J}\ll m_K/K\to0$, and (9) is $o_{\mathbf a,J}(N^r)$.
The tuples with some $x_i\le2^{K-J}$ number at most
$r2^{-J}N^r$. Let $N\to\infty$ and then $J\to\infty$ to obtain

$$
\#\{\textstyle\sum_i a_i f(x_i):1\le x_i\le N\}=o(N^r).
$$

Since $f(n)\asymp n^r$ and the coefficients are positive, values up to
$X$ have all $x_i=O_{\mathbf a}(X^{1/r})$. This proves (6).
Clearing fixed denominators gives the analogous assertion for rational
coefficients. Rounding rational outputs cannot increase their number,
so every rational tuple is exceptional for the metric conclusion.

Finally (5) and $f(n)\ll n^r$ are exactly the two sequence estimates
used in the slab argument (3)--(4). Repeating that argument gives
the same log-free averaged near-collision estimate, and Fatou and
Cauchy--Schwarz give the last assertion. $\square$

This countermodel does not preserve the exact polynomial identity
$f(n)=n^r$, nor does it claim all growing-modulus or major-arc estimates
of the actual powers. It excludes extraction arguments based only on
the properties explicitly listed above. No fixed rational coefficient
tuple for the original problem was obtained.

## Coordinate power rescaling does not remove height escape

For actual powers, positive upper density is invariant under replacing
$a_i$ by $a_i b_i^r$ with fixed $b_i\in\mathbb Q_{>0}$, interpreting
rational value sets after clearing a fixed common denominator.
For integral $b_i$, writing $V_{\mathbf a}$ for the positive value set
and $M=\operatorname{lcm}(b_1,\ldots,b_r)$ gives

$$
V_{(a_i b_i^r)}\subseteq V_{\mathbf a},\qquad
M^r V_{\mathbf a}\subseteq V_{(a_i b_i^r)}.
$$

The second inclusion uses the roots $(M/b_i)x_i$.
General rational $b_i$ follow by a common denominator and fixed output
dilation. This is a qualitative invariance for a fixed rescaling.
If the rescaling grows with the counting parameter, the resulting
density constants can tend to zero. No tight arithmetic coefficient
average was constructed.
