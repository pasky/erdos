---
name: research/erdos_774/lemmas/moment_modular_depth
title: The arithmetic depth of the moment cancellation target
desc: Growing congruence depth exactly captures the moment cancellation target; the critical target itself is proved by a separate stable-lattice argument.
tags: [E0774, Boolean-moments, lattice, reduction, proved, incomplete]
sources: []
created: 2026-09-19T01:00:00Z
updated: 2026-09-19T01:00:00Z
---


# The arithmetic depth of the moment cancellation target

***

The [weak stable-lattice bridge](../routes/moment_boundary_extraction.md)
establishes the required fixed-scale cancellation without this reduction.
The modular-depth bounds remain valid; no explicit coding estimate at the
sufficient depth is proved. The target language below describes the
reduction's role as an exact alternative formulation.

The [integer-graph reduction](moment_integer_graph.md) leaves the
fixed-scale cancellation probability $\Pr(CZ=0)$ unestimated. This page
gives an exact growing-modulus reformulation and a lower bound on the
modulus scale that could certify extraction. It does **not** prove the
required exponential cancellation.

## 1. Notation and the cancellation target

Let

$$
n=2^d,\quad r=\sum_{i=0}^k\binom di,\quad m=n-r,
\qquad
C_{B,T}=(-1)^{k-|B|+1}1_{B\subseteq T}
              \binom{|T|-|B|-1}{k-|B|},
$$

where $0\leq k<d$ and $|B|\leq k<|T|$. Write

$$
\theta(s)=\sum_{j\in\mathbb Z}e^{-\pi s^2j^2},\qquad
\Pr(Z_i=j)=\theta(s)^{-1}e^{-\pi s^2j^2},
$$

with independent coordinates and fixed $s>0$. Set
$p(s)=\Pr(CZ=0)$ and $p_q(s)=\Pr(CZ\equiv0\pmod q)$.
The hard-kernel theta mass equals $\theta(s)^m p(s)$.
At $r=o(n)$, the sufficient extraction target is, for fixed $s,b>0$,

$$
\log s+\frac mn\log\theta(s)+\frac1n\log p(s)\leq-b+o(1).
\tag{1}
$$

## 2. Every congruence has substantial mass

For **any** integer $r\times m$ matrix and any $q\geq2$,

$$
\boxed{p_q(s)\geq q^{-r}.}                         \tag{2}
$$

Indeed the single-coordinate characteristic function is positive
everywhere. Fourier expansion of the periodized Gaussian gives

$$
\phi_s(t)=\mathbb E e^{2\pi itZ_i}
=\frac1{s\theta(s)}
  \sum_{\ell\in\mathbb Z}e^{-\pi(\ell-t)^2/s^2}>0.
$$

This formula follows directly from the Gaussian Fourier transform by
periodization. Orthogonality of characters of $(\mathbb Z/q)^r$ now gives

$$
p_q(s)=q^{-r}\sum_{u\in(\mathbb Z/q)^r}
          \prod_{i=1}^m\phi_s((C^{\mathsf T}u)_i/q).
$$

All summands are nonnegative, and $u=0$ contributes $q^{-r}$.
No rank or surjectivity assumption on $C\bmod q$ is used.

Suppose one tries to establish (1) by the relaxation $p\leq p_q$.
Equations (1)--(2) then require

$$
\frac{r\log q}{n}\geq
b+\log s+\frac mn\log\theta(s)+o(1).               \tag{3}
$$

At $r=o(n)$, the limiting right side is positive: the same periodization
identity gives $s\theta(s)=\theta(1/s)>1$. Consequently bounded $q$
cannot supply such an estimate.

### The precise boundary scale

For even $d$ and
$k=\lfloor d/2-\tfrac12\sqrt{d\log d}\rfloor$,

$$
\frac rn\sim\frac1{\sqrt{2\pi d\log d}}.
\tag{4}
$$

Here is an elementary check, including the tail rather than just its
largest term. Put $u=d/2-k=\tfrac12\sqrt{d\log d}+O(1)$.
Stirling's formula and the central-binomial ratio product give

$$
2^{-d}\binom dk\sim\sqrt{2/\pi}\,d^{-1}.
$$

Put $\lambda=4u/d$. For each fixed $R>0$, uniformly for
$0\leq j\leq R/\lambda$, the logarithm of
$\binom d{k-j}/\binom dk$ is
$-\lambda j+o(1)$: the additional summed error is
$O(j/d+j^2/d+ju^2/d^2)=o(1)$ in this range.
Thus these terms sum to
$(1-e^{-R}+o(1))/\lambda$.
Conversely every successive ratio is at most $k/(d-k+1)$, so the
whole sum is at most
$(d-k+1)/(d-2k+1)\sim1/\lambda$.
Letting $R$ increase proves
$r/\binom dk\sim d/(4u)$, and hence (4).

It follows from (3) that any congruence-relaxation certificate at this
boundary needs

$$
\boxed{\log q=\Omega_{s,b}(\sqrt{d\log d}).}        \tag{5}
$$

For powers $q=2^J$, the binary depth must be
$J=\Omega_{s,b}(\sqrt{d\log d})$. Fixed depth and moduli polynomial
in **$d$** are insufficient. Several scalar moduli combine to their
least common multiple, to which the same bound applies. This assertion
concerns congruences of the same full matrix $C$, not arbitrary extra
equations or conditioning.

## 3. Depth $O(d)$ already captures exact equality

For the actual matrix above let

$$
M_2=\max_B\sum_T C_{B,T}^2.
$$

Since $j=|T|-|B|\geq1$ whenever the entry is nonzero, we have
$\binom{j-1}{k-|B|}\leq2^{j-1}$. Therefore

$$
M_2\leq\max_B\sum_{j\geq1}\binom{d-|B|}{j}4^{j-1}
       \leq\frac{5^d-1}{4}.                       \tag{6}
$$

The moment-generating function has the elementary bound

$$
\mathbb E e^{tZ_i}\leq e^{t^2/(4\pi s^2)}.
\tag{7}
$$

To check it, complete the square; the remaining shifted Gaussian sum
is at most its value at zero. The latter maximality follows by
periodization, whose Fourier coefficients are nonnegative. Independence,
Chernoff's bound applied to either sign of each row, and a union bound give

$$
\Pr(\|CZ\|_\infty\geq q)
\leq 2r\exp(-\pi s^2 q^2/M_2).                   \tag{8}
$$

Choose a fixed $A>0$ with
$\pi s^2A>\log\theta(s)$, and choose $q=2^J$ to be the smallest
power of two at least $\max\{2,\sqrt{AnM_2}\}$. A nonzero vector congruent to
zero modulo $q$ has some coordinate of absolute value at least $q$.
Thus

$$
0\leq p_q(s)-p(s)\leq2r e^{-\pi s^2 A n}.
$$

But $p(s)\geq\Pr(Z=0)=\theta(s)^{-m}$. Since $m,r\leq n$,

$$
\boxed{p_q(s)=p(s)(1+O_s(e^{-c_s n}))}             \tag{9}
$$

for some $c_s>0$, after fixing $A$ with a positive margin. Equation
(6) gives

$$
\boxed{J\leq\tfrac12\log_2(10)\,d+O_s(1).}        \tag{10}
$$

Thus replacing exact equality by this one growing binary modulus does
not change the normalized logarithmic target, and in fact changes the
probability by exponentially small relative error.

## 4. What this advances, and what remains

The exact cancellation problem can be studied as a multilevel binary
coding problem. A bounded number of $2$-adic levels is quantitatively
insufficient for the intended estimate; $O(d)$ levels suffice to retain
the entire exact problem. No upper estimate for $p_q$ at that depth
has been proved here. In particular, neither a shallow-code calculation
nor lattice covolume is being promoted to extraction.

The arguments are analytic, finite-dimensional, and computationally
independent. No new experiment or imported paper theorem is used.

The inequalities, normalization, boundary asymptotic, and relative-error
conclusion are author-recorded; a separate reviewer checked them
independently. These are internal checks, not external review.
