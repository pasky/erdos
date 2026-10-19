---
name: research/erdos_940/palm_void_strategy
title: A one-sided deletion coupling for missing targets
desc: A single bounded Palm comparison would force gaps at any finite representation mean; the arithmetic coupling remains unproved.
tags: []
sources: []
created: 2026-09-22T22:46:25Z
updated: 2026-09-22T23:09:46Z
---


# A one-sided deletion coupling for missing targets

***

## Status and purpose

This is a new proposed mechanism, not a solution. The probability
inequalities below are proved and author-recorded. **No
arithmetic deletion coupling or Palm comparison has been established.**

The proposal concerns empty representation fibers rather than second
or fifth moments. Unlike a first-moment deficit, it would work at
every finite mean, including above the
[quintic progression floor](quintic_first_moment_barrier.md).
It tolerates compound-Poisson clustering and does not require a
Poisson limit law.

## The two ways to sample a fiber

Fix $r\ge3$. Let $R(n)$ count unordered representations of $n$ as **exactly
$r$** positive $r$-powerful integers. For a uniform target
$V_X\in\{1,\ldots,X\}$, write $R_X=R(V_X)$ and $\lambda_X=\mathbb E R_X$. The
established
[tuple asymptotic](finite_core_reduction.md#unrestricted-tuple-counting-has-a-growing-constant)
gives

$$
\lambda_X\longrightarrow
\lambda_r=\frac{\Gamma(1+1/r)^r W_r^r}{r!}\in(0,\infty).
\tag{1}
$$


Alternatively, choose one unordered representation uniformly from all
such representations with sum at most $X$, and let $U_X$ be its sum.
Then $R(U_X)$ has the size-biased law $R_X^s$:

$$
\Pr(R_X^s=k)=\frac{k\Pr(R_X=k)}{\lambda_X},\qquad k\ge1.
$$

The selected representation accounts for one of these $k$ representations.

For fixed $0<z<1$, put

$$
G_X(z)=\mathbb E z^{R_X},\qquad
H_X(z)=\mathbb E z^{R_X^s-1}.
$$

Thus

$$
G_X'(z)=\lambda_X H_X(z).                            \tag{2}
$$

Both expectations are bounded. Even the derivative statistic
$kz^{k-1}$ is bounded in $k$ for fixed $z<1$.

## One comparison point already forces gaps

**Proposition.** Let $\lambda_X\to\lambda>0$ and set
$z=(1+\lambda)^{-1}$. If

$$
\limsup_{X\to\infty}\bigl(H_X(z)-G_X(z)\bigr)\le0,     \tag{3}
$$

then

$$
\liminf_{X\to\infty}\Pr(R_X=0)
\ge(1+\lambda)^{-1-\lambda}>0.                       \tag{4}
$$


**Proof.** Let $p_{0,X}=\Pr(R_X=0)$. Termwise comparison gives

$$
zG_X'(z)=\sum_{k\ge1}k\Pr(R_X=k)z^k
\ge G_X(z)-p_{0,X}.
$$

Together with (2), this implies

$$
p_{0,X}\ge
(1-\lambda_Xz)G_X(z)
-\lambda_Xz\bigl(H_X(z)-G_X(z)\bigr).                 \tag{5}
$$

Jensen gives $G_X(z)\ge z^{\lambda_X}$. Eventually
$1-\lambda_Xz>0$, so (3) and (5) prove (4). $\square$

If the limsup in (3) is at most $\varepsilon$, the right side of
(4) can instead be replaced by

$$
(1+\lambda)^{-1-\lambda}
-\frac{\lambda}{1+\lambda}\varepsilon.
$$


Applied to (1), (3) would give positive lower density of
$\mathbb N\setminus S_r$: targets with fewer than $r$ summands
number only $O_r(X^{1-1/r})$. A comparison along an unbounded
sequence would already give infinitely many missing targets.

## What a deletion coupling would supply

A sufficient arithmetic mechanism would couple a uniform target
$V_X$ and a uniformly sampled representation with target $U_X$ so
that, after deleting the selected representation at $U_X$,

$$
R(U_X)-1\ge R(V_X)
$$

except for a vanishing expected deficit. More precisely, if a
coupling of $R_X,R_X^s$ satisfies

$$
\delta_X=\mathbb E(R_X+1-R_X^s)_+\longrightarrow0,    \tag{6}
$$

then, for every fixed $0\le z\le1$,

$$
H_X(z)-G_X(z)\le(1-z)\delta_X.                       \tag{7}
$$

For integers $a\ge1,b\ge0$, use
$(z^{a-1}-z^b)_+\le(1-z)(b+1-a)_+$, with $0^0=1$.

Integrating (2) and (7) gives the stronger bound

$$
\Pr(R_X=0)\ge e^{-\lambda_X}
-\delta_X\left(1-\frac{1-e^{-\lambda_X}}{\lambda_X}\right).
\tag{8}
$$

The one-point criterion (3) is weaker than requiring such a coupling.

**Unproved arithmetic step.** No construction of this coupling is
known here. Conditioning on one representation does not automatically
create other integral representations. A fixed rational transformation
or grouping of existing summands does not supply the missing step.

The signed identity

$$
\Pr(R_X=0)=e^{-\lambda_X}
-\int_0^1e^{-\lambda_Xz}
 \bigl(G_X'(z)-\lambda_XG_X(z)\bigr)\,dz
$$

is only an identity; naming its integral would restate the void problem.
The substantive proposed input is the one-sided comparison, preferably
from an arithmetic coupling.

## Compatibility with clustering, but no automatic theorem

For a compound-Poisson law

$$
G(z)=\exp\!\left(\sum_{j\ge1}\nu_j(z^j-1)\right),
\qquad 0<\lambda=\sum_{j\ge1}j\nu_j<\infty,
$$

one has

$$
\frac{H(z)}{G(z)}
=\frac{\sum_{j\ge1}j\nu_jz^{j-1}}{\lambda}\in(0,1]
\qquad(0<z<1).
$$

Thus collision clusters would not themselves invalidate the comparison.
Mixed-Poisson laws also satisfy its upper inequality: if
$R\mid L$ is Poisson$(L)$, then
$G(z)=\mathbb E e^{-(1-z)L}$ and
$H(z)=\mathbb E[L e^{-(1-z)L}]/\mathbb E L\le G(z)$,
by the negative covariance of an increasing and a decreasing function.

These are model checks, not theorems about powerful sums.
The comparison is false for general laws: $R\equiv m\ge1$ gives
$H(z)=z^{m-1}>z^m=G(z)$.

Nor do convex-track spacing and critical cardinality alone force gaps.
Put $a=1-1/r$ and

$$
A=\{m^r:m\ge1\},\qquad
B=\bigcup_{j\ge0}
\bigl([2^j-1,\ 2^j+\lceil r2^{ja}\rceil]\cap\mathbb Z\bigr).
$$

Then $B(X)=O_r(X^a)$ but $A+B$ contains every positive integer.
For $2^j<n<2^{j+1}$, choose
$m=\lfloor(n-2^j)^{1/r}\rfloor\ge1$. The mean value theorem gives
$0\le n-2^j-m^r<r2^{ja}$, so $n-m^r\in B$.
For $n=2^j$, choose $m=1$. Summing the geometric sequence of
block lengths proves the bound for $B(X)$. A successful argument
must therefore use the specific arithmetic of the other powerful
summands, not merely their counting exponent.

## Positive density and the treatment of rich fibers

Let $M_z=\sup_{k\ge1}kz^{k-1}<\infty$. Then

$$
\Pr(R_X>0)\ge\frac{\lambda_XH_X(z)}{M_z}.             \tag{9}
$$

A one-point sandwich

$$
cG_X(z)-o(1)\le H_X(z)\le G_X(z)+o(1),\qquad c>0,     \tag{10}
$$

would therefore give positive lower densities of both represented
and missing targets. The support lower bound is
$\lambda c z^\lambda/M_z$. When $\lambda\ge1$ and
$z=(1+\lambda)^{-1}$, $M_z=1$.

There is an essential qualification: under (1), the existence of some
$c>0$ in the **lower** comparison is equivalent to positive lower density
of represented targets. If that density is at least $\eta>0$, bounded
means imply $\Pr(1\le R_X\le K)\ge\eta/2$ for a sufficiently large
fixed $K$, which bounds $H_X(z)$ below. Thus the lower comparison is
a reformulated density target, not independent progress.

The upper comparison has a feature absent from high-moment estimates:
contributions from $R_X>K$ are at most

$$
z^K\ \text{in }H_X(z),\qquad z^{K+1}\ \text{in }G_X(z).
$$

The first bound uses
$\mathbb E[R_X\mathbf1_{R_X>K}]/\lambda_X\le1$.
Rich fibers can therefore be discarded with an exponentially small
error, without a second-moment bound.

The arithmetic comparison (3), the coupling (6), and a nonzero lower
bound in (9) remain unproved. No target case is resolved.

## Quantitative stability under core truncation

The bounded comparison statistic has a useful proved continuity
property. Let $Q\le R$ be nonnegative integer-valued random variables,
with

$$
\lambda=\mathbb ER<\infty,\qquad 0<\mu=\mathbb EQ\le\lambda,\qquad
\Delta=\mathbb E(R-Q).
$$

For $0<z<1$ define
$G_R=\mathbb Ez^R$ and
$H_R=\lambda^{-1}\mathbb E[Rz^{R-1}]$, and similarly
for $Q$, normalizing its latter expectation by $\mu$. Then

$$
|G_R-G_Q|\le(1-z)\Delta,\qquad
|H_R-H_Q|\le2\Delta/\lambda.                           \tag{11}
$$


Indeed $k\mapsto z^k$ is $(1-z)$-Lipschitz on the nonnegative
integers. Put $h_z(0)=0$ and $h_z(k)=kz^{k-1}$ for $k\ge1$.
The increment from zero to one equals one. For $k\ge1$,

$$
h_z(k+1)-h_z(k)=z^k-k(1-z)z^{k-1}.
$$

Both terms on the right lie in $[0,1]$; the second is the
probability of exactly one failure in $k$ independent trials
with success probability $z$. Thus $h_z$ is $1$-Lipschitz.
Writing $A=\mathbb E h_z(R)$ and $B=\mathbb E h_z(Q)$,
we have $|A-B|\le\Delta$ and $0\le B\le\mu$. Therefore

$$
\left|\frac A\lambda-\frac B\mu\right|
\le\frac{\Delta}{\lambda}
\;+\;B\frac{\lambda-\mu}{\lambda\mu}
\le\frac{2\Delta}{\lambda},
$$

as required. In particular,

$$
|(H_R-G_R)-(H_Q-G_Q)|
\le(2/\lambda+1-z)\Delta.                             \tag{12}
$$


For the uniform target in $[1,X]$, let $Q=R_{X,Y}$ retain
only representations all of whose canonical cores are at most
$Y$, and let $R=R_X$ be the full exactly-$r$ count. The
[canonical tail estimate](finite_core_reduction.md) gives

$$
\Delta\ll_r Y^{-1/[r(r+1)]}.
$$

Since $\lambda_X$ tends to a positive constant, (12) is uniform
for sufficiently large $X$. Consequently, a one-point upper Palm
comparison established for every finite cutoff, at the same fixed
$z$, would pass to the full powerful sumset by first taking
$X\to\infty$ and then $Y\to\infty$. No coefficient-uniform
higher-moment estimate would be necessary for that passage.
**The finite-cutoff arithmetic comparison itself is unproved.**

## Why direct positive association does not prove the comparison

If two individual representation tuples have different sums
$a\ne b$, their occurrence events under a random target $V$ are
$\{V=a\}$ and $\{V=b\}$. When both have positive probability,
their covariance is

$$
-\Pr(V=a)\Pr(V=b)<0.
$$

Thus these events cannot directly satisfy a positive-association
inequality, whatever smooth or nonsmooth target measure is chosen.
Exponential weights make summands independent when sampling an
ordered representation, but that is the size-biased target law;
it does not supply a comparison with a uniform target.

There is a genuine monotone structure on a missing ray: the
[primitive-denominator identity](remaining_questions.md#scaling-along-a-ray-an-exact-identity-not-a-descent)
$R_t(m)=\sum_{h\mid m}A_t(h)$ makes the count increasing in the prime exponents
of $m$, with $A_t(1)=0$. Under independent prime-exponent sampling, the
avoidance events are decreasing and positively associated. This does not ensure
new missing targets. The abstract example $A_t(h)=1$ for every $h>1$ gives
$R_t(m)=\tau(m)-1$, whose only zero is $m=1$. A quantitative arithmetic bound on
the actual primitive-denominator support is still needed. No such bound,
deletion coupling, or target resolution was obtained from this association
attempt.

## Even exact global dilation identities do not force further holes

The preceding one-ray warning admits a global strengthening. This is a
countermodel to a proposed inference, not a multiplicity function for
powerful sums.

**Proposition.** Fix $r\ge2$, an $r$th-power-free integer $t>1$, and
$\lambda\ge1$. There are nonnegative integer functions $A,R$ on
$\mathbb N$ satisfying all of

$$
R(n)=\sum_{d^r\mid n}A(n/d^r),\qquad R(n)=0\iff n=t,
$$


$$
R(nk)\ge R(n)\quad(k\in\mathcal P_r),\qquad
\sum_{n\le X}R(n)=\lambda X+
O_{r,t,\lambda}(X^{1/r}\log(2X)).
\tag{13}
$$

Here $1\in\mathcal P_r$ and "$r$th-power-free" means that no $d^r>1$
divides the integer. Thus a missing seed, the global primitive
decomposition, powerful-multiplier monotonicity, and any prescribed
finite mean compatible with cofiniteness do not force another zero.

**Proof for $\lambda=1$.** Define

$$
A(n)=\mathbf1_{n\text{ is }r\text{th-power-free}}
-\mathbf1_{n=t}
+\mathbf1_{\{n=tq:\ q\in\mathcal P_r\setminus\{1\}\}}.
$$

This is nonnegative (in fact binary). Every $n$ has exactly one divisor
$d^r$ for which $n/d^r$ is $r$th-power-free, so the first term contributes
exactly one to $R(n)$. Put

$$
C(q)=\sum_{d^r\mid q}\mathbf1_{q/d^r\in\mathcal P_r}.
$$

All changes from that baseline are supported on $t\mathcal P_r$, and
for $q\in\mathcal P_r$ one obtains

$$
R(tq)=1+C(q)-2\mathbf1_{q\text{ is an }r\text{th power}}.
\tag{14}
$$

At $q=1$ this is zero. If $q>1$ is not an $r$th power it is at least
two. If $q=m^r$, then $C(q)=\tau(m)$, so $R(tm^r)=\tau(m)-1$.
This is positive for $m>1$. Hence $t$ is the only zero.

For an exponent $e=ar+s\ge r$, $0\le s<r$, the local factor of $C$ is
$a+1$ if $s=0$ and $a$ otherwise. Its factor at exponent zero is one.
Increasing an exponent by at least $r$ never decreases this factor.
Thus $C(qk)\ge C(q)$ for $q,k\in\mathcal P_r$.
The only possible difficulty in (14) is when $q$ is not an $r$th power
but $qk$ is. At a prime with $s>0$, the added exponent must have the
form $br+r-s$, with $b\ge1$. The new local factor is $a+b+2$,
exceeding the old factor $a$ by at least three. All other factors are
nondecreasing, so $C(qk)-C(q)\ge3$, more than compensating for the new
subtraction of two.

This proves monotonicity on $t\mathcal P_r$. Outside it $R=1$; a
powerful multiple cannot equal $t$, since $t$ is $r$th-power-free.
All other values of $R$ are at least one, proving global monotonicity.
Finally the powerful-number count gives

$$
\sum_{q\le Y}C(q)
=\sum_{d\le Y^{1/r}}\#(\mathcal P_r\cap[1,Y/d^r])
\ll_r Y^{1/r}\log(2Y).
$$

Equation (14) therefore proves (13) with $\lambda=1$.

**Prescribing the mean.** Choose a prime $p\nmid t$ and nonnegative
integers $b_k$ such that

$$
\lambda-1=\sum_{k\ge1}b_kp^{-k},\qquad
0\le b_k\le p-1\quad(k\ge2);
$$

the first digit may be larger. Add
$B(n)=\sum_{k\le v_p(n)}b_k$ to the function $R$ above. It vanishes at
$t$, is monotone under every positive integer multiplier, and satisfies

$$
\sum_{n\le X}B(n)
=\sum_{k\ge1}b_k\lfloor X/p^k\rfloor
=(\lambda-1)X+O_{p,\lambda}(\log(2X)).
$$

Its primitive Möbius inverse is nonnegative. Indeed, if a prime
$q\ne p$ has $q^r\mid n$, pairing divisors with and without $q$
makes that inverse zero. Otherwise it is
$B(p^v)-B(p^{v-r})$, where $v=v_p(n)$ and the second term is
interpreted as zero for $v<r$. This is nonnegative. Adding this
inverse to $A$ preserves the required primitive decomposition and
finishes the proof. $\square$

The proposition rules out a dilation-only proof even if the actual
limiting mean is known exactly. It does not impose the additive or
local properties of actual powerful representations. An arithmetic
comparison such as (3) could still prove gaps, but it does not follow
from the properties in (13).
