---
name: research/erdos_25/full_survivor_trace_obstruction
desc: Bounded canonical survivor weights have nonvanishing arithmetic signed traces even with pointwise vanishing square tails and original-activation natural density.
tags: [prime-filtration, entropy, obstructions, conditional-measures]
sources: []
created: 2026-09-22T16:03:00Z
updated: 2026-09-24T22:13:01Z
---


# research/erdos_25/full_survivor_trace_obstruction

***

The entropy budget in [prime filtration](prime_filtration.md) uses the
conditional marginals of the full Haar survivor law. The construction
below shows that these particular marginals can have incorrect arithmetic
signed traces even when their densities are bounded and the exact
activated forbidden fractions have pointwise summable square tails.
This is a counterexample to that transfer mechanism, **not** to Problem
25: the constructed sieve has natural density equal to its Haar candidate.
Weights defined from finite activated sieves are not covered by the
obstruction.

## The obstruction, uniformly at high primes

For every $Y\ge2$, there is an explicitly specified increasing-modulus
singleton system with the following properties. Write $S$ for its
full Haar survivor set in $G=\prod_p\mathbb Z_p$, and put
$\delta=\mu(S)$, $\nu=\mathbf1_S\mu/\delta$.

* The actual survivor set, with activation exactly $n\ge q$, has
  natural density $\delta>1/4$, and therefore logarithmic density
  $\delta$.
* For every integer $n$ and prime $p$, its exact activated fraction
  satisfies $\alpha_p(n)\le1/p$. Thus, uniformly in the system and
  in $n$,
  $$
   \sum_{p>K}\alpha_p(n)^2\le\sum_{p>K}p^{-2}\longrightarrow0.
   \tag{1}
  $$
* There is a finite set $P$ of primes above $Y$ such that the
  canonical earlier-prime marginal densities $w_{p-}$ of $\nu$
  obey $0\le w_{p-}\le1/\delta<4$, but
  $$
   \sum_{p\in P}\lim_{X\to\infty}\frac1{H_X}
       \sum_{n\le X}\frac{w_{p-}(n)
           (\mathbf1_{B_p(n)}-\alpha_p(n))}{n}
   \ge\frac12(1-1/Y).
   \tag{2}
  $$
  Every corresponding Haar signed integral is zero. Here $B_p(n)$
  is the actual activated deletion event at largest prime $p$.

The system is allowed to depend on $Y$. Consequently (2) refutes a
**uniform** high-prime transfer bound based only on a positive lower
bound for $\delta$, bounded full-survivor weights, and the square
tails (1). It does not assert a nonvanishing high-prime tail for one
fixed system as $Y\to\infty$.

## Construction

Take successive primes greater than $Y$, stopping at the first
finite block $P=\{p_1<\cdots<p_t\}$ for which
$$
 s=\prod_{p\in P}(1-1/p)\le\frac12.
$$
Divergence of the prime reciprocal sum ensures termination. The
preceding product exceeded $1/2$, and $p_t\ge3$, so
$1/3<s\le1/2$. Put
$$
 M=\prod_{p\in P}p,\qquad
 D=\{n:\text{some }p\in P\text{ divides }n\}.
$$
Enumerate the positive integers coprime to $M$ as
$b_1<b_2<\cdots$. Set, for example,
$$
 k_j=4+j+\lceil\log_2(b_j+1)\rceil,
 \quad C_j=[b_j]_{2^{k_j}}\subset\mathbb Z_2,
 \quad O=\bigcup_j C_j,\quad C=\mathbb Z_2\setminus O.
 \tag{3}
$$
The exponents $k_j$ strictly increase, $b_j<2^{k_j}$, and
$$
 \tau=\sum_j2^{-k_j}\le2^{-4}\sum_{j\ge1}2^{-j}<\frac14,
 \qquad \mu_2(C)\ge1-\tau>\frac34.
 \tag{4}
$$
Overlaps of the binary balls are permitted and cause no difficulty.

Partition the primes greater than $p_t$ into disjoint sets $R_j$,
each with divergent reciprocal sum, by the following deterministic rule.
Use the label sequence $1;1,2;1,2,3;\ldots$. At each occurrence of
label $j$, assign to $R_j$ successive unused primes until that
batch first has reciprocal sum at least one. Each batch is finite,
every label recurs infinitely often, and every prime is eventually
assigned.

Install $[0]_p$ for $p\in P$. For every $j$ and $r\in R_j$,
install one residue class at
$$
 q_{j,r}=2^{k_j}r,
 \qquad a_{j,r}\equiv b_j\pmod{2^{k_j}},
 \qquad a_{j,r}\equiv0\pmod r.
 \tag{5}
$$
CRT specifies a unique normalized residue in $[0,q_{j,r})$.
All moduli are distinct: the binary exponent identifies $j$, and
the odd factor identifies $r$. None equals a selected pure prime.
They therefore have a strictly increasing enumeration, and each has at
most two distinct prime factors. All subsequent arithmetic assertions
use the prescribed activation $n\ge q$.

## The arithmetic trace of the binary set

Every positive integer outside $D$ is one of the roots $b_j$,
and hence lies in $O$. Therefore
$$
 C\cap\mathbb N\subseteq D.
 \tag{6}
$$
If $W\subseteq D$ is periodic modulo $M$, a positive point of
$C_j\cap W$ cannot be the root $b_j\notin D$. Since
$0<b_j<2^{k_j}$, it has the form $b_j+u2^{k_j}$ with $u\ge1$.
Consequently
$$
 |C_j\cap W\cap[1,X]|\le X2^{-k_j}.
 \tag{7}
$$
For $O_J=\bigcup_{j\le J}C_j$, CRT gives
$d(O_J\cap W)=\mu_2(O_J)d(W)$, since its binary period is coprime
to $M$. The uniform tail bound (7) now proves
$$
 d(C\cap W)=\mu_2(C)d(W)\qquad(W\subseteq D).
 \tag{8}
$$
The same limits hold under harmonic averaging by partial summation.
Notice the restriction $W\subseteq D$: the roots deliberately make
the unrestricted trace of $C$ very different from Haar measure.

## Canonical full-survivor marginals

Fix the complete binary coordinate $x_2$. If $x_2\notin O$, no
class in (5) can hit. If $x_2\in C_j$, surviving all the classes
indexed by $R_j$ requires avoiding zero at every prime in $R_j$,
an event of conditional probability
$\prod_{r\in R_j}(1-1/r)=0$. Thus integration over the remaining
independent coordinates gives, **for every** $x_2$,
$$
 \mu(S\mid x_2)=s\mathbf1_C(x_2),\qquad
 \delta=s\mu_2(C)>\frac14.
 \tag{9}
$$
This is the canonical product-fiber integral, not an arbitrary
modification of a conditional expectation on an exceptional set.

Write $s_0=1$, $s_j=\prod_{i\le j}(1-1/p_i)$. Before exposing
the coordinate at $p_j$, the density of the corresponding marginal
of $\nu$ is exactly
$$
 w_{p_j-}(x)=
 \frac{\mathbf1_C(x_2)
       \prod_{i<j}\mathbf1_{x_{p_i}\not\equiv0\ (p_i)}}
      {\mu_2(C)s_{j-1}}.
 \tag{10}
$$
All primes used in (5) exceed $p_t$; other earlier coordinates are
irrelevant. Since $s_{j-1}\ge s$, these densities are at most
$1/\delta<4$. At $p_j$ the forbidden Haar event is
$[0]_{p_j}$, with fraction $1/p_j$. Independence from the
earlier-coordinate weight gives its zero Haar signed integral.

For arithmetic averages, pure-prime activation differs from this
formula only on a fixed finite initial segment. Using (6)--(8), the
signed arithmetic limit is
$$
 T_j=\frac1{s_{j-1}}\mathbb E_P\left[
   \mathbf1_D\prod_{i<j}\mathbf1_{x_{p_i}\ne0}
           (\mathbf1_{x_{p_j}=0}-1/p_j)\right]
     =\frac{s}{p_js_{j-1}}>0.
 \tag{11}
$$
Here $\mathbb E_P$ is uniform averaging on the finite product of
the $P$-coordinates. To check the equality, the expectation without
$\mathbf1_D$ is zero. On $D^c$, of probability $s$, the
earlier factors equal one and the final factor is $-1/p_j$.
Finally,
$$
 \sum_j\frac{T_j}{1-1/p_j}
   =s\sum_j(1/s_j-1/s_{j-1})=1-s.
$$
As $p_j>Y$, this proves (2).

## Square tails and the actual natural density

For $p\in P$, the activated fraction is either zero or $1/p$.
Each prime $r>p_t$ occurs in exactly one modulus (5); therefore
$$
 \alpha_r(n)=\frac1r
     \mathbf1_{\{2^{k_j}r\le n,\ n\equiv b_j\ (2^{k_j})\}}
       \quad(r\in R_j).
$$
There is no class with largest prime factor two. This proves (1)
pointwise, including the activation condition.

Let $B_j$ be the activated union of the classes with $r\in R_j$.
For every finite $F\subset R_j$, its activated union is eventually
periodic and its complement in $C_j$ has density
$2^{-k_j}\prod_{r\in F}(1-1/r)$. Letting $F$ increase proves
$d(C_j\setminus B_j)=0$. On the other hand, every activated point
of $B_j$ is beyond the root $b_j<2^{k_j}$, whence
$$
 |B_j\cap[1,X]|\le X2^{-k_j}.
 \tag{12}
$$
For finitely many $j\le J$, the deletion set including the classes
at $P$ thus has density
$1-s+s\mu_2(O_J)$. Equation (12) makes the remaining tail at most
$X\sum_{j>J}2^{-k_j}$, uniformly in $X$. Letting $J\to\infty$
proves that the actual survivor density is
$s(1-\mu_2(O))=\delta$, as claimed.

## A fixed-prime illustration and the remaining gap

Using just $P=\{3\}$ in the same construction gives
$$
 d(C\cap\mathbb N)=\mu_2(C)/3,\qquad
 w_{3-}=\mathbf1_C/\mu_2(C).
$$
The Haar signed integral is zero, but the arithmetic signed harmonic
average equals $2/9$. Thus even cancellation at one fixed prime
cannot be transferred for the infinite-future conditional law.

Finite unions $O_J$ are periodic and have ordinary Haar arithmetic
averages. Passing to their infinite limit before arithmetic sampling
is exactly the invalid step. A proof based on activated finite-prefix
weights would need an estimate retaining that truncation; nothing here
refutes such an estimate. No original-activation logarithmic-density
counterexample, or general tail theorem, follows from this obstruction.
