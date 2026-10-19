---
name: research/smooth_successor_estimates/proxy_densities
title: Rough-integer densities and the Buchstab identity
desc: |
  The weighted-dilation manuscript's Lemma 7.4 derived at the ranges the
  successor extraction consumes: an absolute bound for the balanced prime
  proxy, short-cell upper densities for x^gamma-rough integers on compact sets
  with w-gamma bounded below, the cofactor bound (7.17) with w-gamma at least
  2kappa, the minimum-coordinate identity (7.18), the bound (7.19) from a lower
  count and the block sieve, and the mesh step that sums the bins.
created: 2026-10-15T15:28:45Z
updated: 2026-10-15T15:28:45Z
---

# Rough-integer densities and the Buchstab identity

***

This page reconstructs Lemma 7.4 of the
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation manuscript]]
for the
[[research/smooth_successor_primes/successor_prime_extraction|extraction of primes 2u-1]],
as part of the
[[research/smooth_successor_estimates/_index|elementary estimates of the smooth-successor route]].
The formulation and use of the estimates follow OpenAI; the densities and
minimum-coordinate identity are classical Buchstab rough-number estimates
(A. Buchstab, Mat. Sbornik 2(44) (1937), 1239–1246). The derivation and
the range checks below are Plasma AI's. The
[[research/smooth_successor_estimates/evidence/verify/elementary_estimates/_index|E3 examination]]
has a distinct **PASS** grade, examined on 2026-10-16 UTC, accepting
**refutation-failed** at its stated classical-premise and parameter scopes.
The [grade](evidence/verify/elementary_estimates/grade.md) retains the original-source
reading limits and, for the weighted E3 consumer consequence, its Type II/P
hypothesis.
Notation is that of the
[[research/smooth_successor_estimates/proxy_discrepancy|proxy-discrepancy page]]:
cells $C=(Y,e^\Delta Y]$ with $\Delta=L^{-S}$, $R(C)$ the number of $W$-rough
integers in $C$, and $c_I(C)$ the proxy constant of a test $I$.

## The densities

For $w>\gamma>0$ put $D_\gamma(w)=\sum_{l\ge1}T_l(\gamma,w)$, where
$T_1(\gamma,w)=1/w$ and, for $l\ge2$, with $s(t)=t_1+\cdots+t_{l-1}$,

$$
T_l(\gamma,w)=\frac1{l!}\int_{\Omega_l(\gamma,w)}\frac1{w-s(t)}
\prod_{i<l}\frac{dt_i}{t_i},\qquad
\Omega_l(\gamma,w)=\{t\in\mathbb R^{l-1}:t_i\ge\gamma,\ s(t)\le w-\gamma\}.
$$

This is the manuscript's (7.15). $T_l$ vanishes unless $l\gamma\le w$, so the
sum is finite. Writing $t_l=w-s(t)$, the $l$-th term is $1/l!$ times the
integral of $\prod_{i\le l}t_i^{-1}$ over
$\{t\in\mathbb R^l:t_i\ge\gamma,\ \sum t_i=w\}$ against $dt_1\cdots dt_{l-1}$:
ordered lists of $l$ prime logarithms, scaled by $L$, with sum $w$.

As a cross-check that the arguments below do not use, $D_\gamma(w)=
\omega(w/\gamma)/\gamma$ for Buchstab's function $\omega$; for
$2\gamma\le w\le3\gamma$ both sides equal $(1+\log(w/\gamma-1))/w$.

**Continuity.** For fixed $b,\varepsilon>0$ and $w_{\max}$, $D$ is jointly
continuous on the compact set
$K(b,\varepsilon,w_{\max})=\{(\gamma,w):\gamma\ge b,\
\gamma+\varepsilon\le w\le w_{\max}\}$, thresholds $w=l\gamma$ included.
Indeed only $l\le w_{\max}/b$ occur. On $\Omega_l(\gamma,w)$ the integrand is
at most $b^{-l}$, since $t_i\ge\gamma$ and $w-s(t)\ge\gamma$, and
$\Omega_l(\gamma,w)\subset[b,w_{\max}]^{l-1}$. As $(\gamma',w')\to(\gamma,w)$
the integrand on $\Omega_l(\gamma',w')$ converges to that on
$\Omega_l(\gamma,w)$ at every point off the hyperplanes $t_i=\gamma$ and
$s(t)=w-\gamma$, a null set, so dominated convergence gives continuity of each
$T_l$; at $w=l\gamma$ the domain shrinks to a point and $T_l\to0$.

## Counts in short cells

Fix the precision $S\ge1$, as in every consumed application. The prime
number theorem with error
$O_A(y(\log y)^{-A})$, used with $A=S+2$, gives uniformly for $y$ with
$\log y\ge c_0L$, $c_0>0$ fixed,

$$
\pi(e^\Delta y)-\pi(y)=\frac{\Delta y}{\log y}\bigl(1+O(L^{-1})\bigr).
$$

**The balanced prime proxy (7.16).** Let $0<\kappa<1/50$. A cell meeting
$\mathcal B_\kappa=[x^{1/2-2\kappa},x^{1/2+2\kappa}]$ has
$w=\log Y/L\in[0.46-o(1),0.54]$, so by the display and item 1 of the
proxy-discrepancy proposition

$$
c_{\rm pr}(C)=\frac{\pi(e^\Delta Y)-\pi(Y)}{R(C)}=\frac{1+o(1)}{wL\,V(W)}
\le\frac3{LV(W)}
$$

for $x\ge x_0(\kappa,S)$. The constant $3$ is absolute: it does not depend on
$\kappa$ or $S$, which affect only $x_0$. This is the uniformity that the
balanced constant $C_{\rm bal}$ of the extraction requires.

**Rough counts (7.20).** Fix $b,\varepsilon>0$ and $w_{\max}$. Uniformly for
cells $C=(Y,e^\Delta Y]$ and exponents $\gamma$ with
$(\gamma,\log Y/L)\in K(b,\varepsilon,w_{\max})$,

$$
N_\gamma(C)=\#\{m\in C:P^-(m)>x^\gamma\}\le\bigl(D_\gamma(w)+o(1)\bigr)
\frac{\Delta Y}L,\qquad w=\frac{\log Y}L .
$$

*Proof.* The integers of $C$ divisible by $p^2$ for some prime $p>x^\gamma$
number at most $\sum_{p>x^\gamma}e^\Delta Y/p^2\le3Yx^{-b}=o(\Delta Y/L)$. A
squarefree $m\in C$ with $P^-(m)>x^\gamma$ is a product of $l\le l_{\max}=
\lfloor(w_{\max}+1)/b\rfloor$ distinct primes above $x^\gamma$, and its $l!$
orderings give it total weight one when each ordered list carries weight
$1/l!$. Dropping distinctness only adds lists, so the squarefree count is at
most $\sum_{l\le l_{\max}}\mathcal N_l/l!$, where $\mathcal N_l$ counts ordered
$l$-tuples of primes above $x^\gamma$ with product in $C$.

For $l=1$, every prime of $C$ exceeds $x^\gamma$ because
$w\ge\gamma+\varepsilon$, so $\mathcal N_1=(1+O(L^{-1}))\Delta Y/(wL)$, the term
$T_1$. For $l\ge2$ fix $p_1,\dots,p_{l-1}$ with product $Q$ and
$t_i=\log p_i/L$. A last prime exists
only if $e^\Delta Y/Q>x^\gamma$, that is $s(t)<w-\gamma+\Delta/L$; then
$\log(Y/Q)=L(w-s(t))\ge bL/2$, and the last prime lies in $(Y/Q,e^\Delta Y/Q]$.
Dropping its lower cutoff and using the display,

$$
\mathcal N_l\le\bigl(1+O(L^{-1})\bigr)\frac{\Delta Y}L
\int\varphi\,d\mu^{\otimes(l-1)},\qquad
\varphi(t)=\frac{\mathbf 1_{s(t)<w-\gamma+\Delta/L}}{w-s(t)},\qquad
\mu=\sum_{x^\gamma<p\le x^{w_{\max}}}\frac1p\,\delta_{\log p/L}.
$$

It remains to compare $\mu^{\otimes(l-1)}$ with $\nu^{\otimes(l-1)}$, where
$\nu=dt/t$. By Mertens' estimate
$\sum_{p\le y}1/p=\log\log y+M+O(1/\log y)$, every interval satisfies
$\mu((a,a'])=\nu((a,a'])+O(1/(bL))$ for $\gamma\le a<a'\le w_{\max}$. Fix
$\eta>0$ and cover $(\gamma,w_{\max}]^{l-1}$ by the cubes
$\prod_i(\gamma+k_i\eta,\gamma+(k_i+1)\eta]$, truncating the last interval
in each coordinate at $w_{\max}$. There are at most
$N_\eta=(w_{\max}/\eta+1)^{l-1}$ of them. Each cube has
$\mu^{\otimes}$-measure equal to its $\nu^{\otimes}$-measure up to
$O_{\eta,b,l}(1/L)$. Replace $\varphi$, which is at most $2/b$, by its supremum
$\varphi^+$ on each cube. Then

$$
\int\varphi\,d\mu^{\otimes}\le\int\varphi^+d\nu^{\otimes}
+O_{\eta,b,l,w_{\max}}(L^{-1}).
$$

On cubes inside $\{s<w-\gamma+\Delta/L\}$ the oscillation of $1/(w-s)$ is at
most $4(l-1)\eta/b^2$. The cubes meeting the hyperplane
$s=w-\gamma+\Delta/L$ lie in a slab of width $2(l-1)\eta$, whose
$\nu^{\otimes}$-measure is $O_{b,l,w_{\max}}(\eta)$. The faces $t_i=\gamma$ are
cube faces, so they cause no boundary error. Finally the strip
$w-\gamma\le s<w-\gamma+\Delta/L$ has $\nu^{\otimes}$-measure
$O_{b,l,w_{\max}}(\Delta/L)$. Hence

$$
\int\varphi\,d\mu^{\otimes(l-1)}\le l!\,T_l(\gamma,w)+O(\eta)+o_\eta(1),
$$

uniformly on $K(b,\varepsilon,w_{\max})$. Here the constant in $O(\eta)$
depends only on $b,l,w_{\max}$, and the $o_\eta(1)$ tends to zero uniformly
once $\eta$ and $S$ have been fixed. For any desired error first choose a
fixed $\eta$, then let $x$ grow; this proves a uniform $o(1)$ without
interchanging the choices of $S$ and $x$. $\square$

**The cofactor bound (7.17).** Let $b_1\le\gamma<\gamma'\le1/2-\kappa$ be a bin.
Suppose $C$ contains an integer $m=N/p$ with $x\le N\le5x$ and $p$ a prime in
$(x^\gamma,x^{\gamma'}]$. With $a=\log p/L\in(\gamma,\gamma']$,

$$
w=\frac{\log Y}L=1-a+O(L^{-1}),\qquad w-\gamma\ge1-2\gamma'-O(L^{-1})
\ge2\kappa-O(L^{-1}),\qquad
w\le1-b_1+\frac{\log5}L\le1
$$

for all sufficiently large $x$. Thus $(\gamma,w)$ lies in the compact set
$K(b_1,\kappa,1)$, where the rough-count bound holds uniformly and $D$ is
uniformly continuous. Dividing by
$R(C)=(1+o(1))\Delta YV(W)$,

$$
c_\gamma(C)\le\frac{D_\gamma(w)+o(1)}{LV(W)}
\le\frac{\sup_{\gamma\le a\le\gamma'}D_\gamma(1-a)+o(1)}{LV(W)},
$$

uniformly over all such cells. This is (7.17) exactly at the consumed range.
The only property of $N=2u-1$ used is $x\le N\le5x$, which also holds for
$2u+1$; the change of sign moves $w$ by $O(1/L)$ and does not change the
rough-integer density or its prime-factor cutoff. No density at $w=\gamma$ is
used: on the consumed range $w-\gamma\ge2\kappa+o(1)$, with $b_1$ and $\kappa$
fixed before $x$.

## The minimum-coordinate identity (7.18)

**Identity.** For $0<b_1<1/2$,

$$
\int_{b_1}^{1/2}D_\alpha(1-\alpha)\frac{d\alpha}\alpha=D_{b_1}(1)-1,
$$

with the integrand at $\alpha=1/2$ read as its left limit $2$; for
$1/3<\alpha<1/2$ only $T_1$ survives and $D_\alpha(1-\alpha)=1/(1-\alpha)$.

*Proof.* $T_1(b_1,1)=1$. For $l\ge2$ write $T_l(b_1,1)$ on the simplex
$\Sigma_l=\{t\in\mathbb R^l:t_i\ge b_1,\ \sum t_i=1\}$ with the measure
$\frac1{l!}\prod_{i\le l}t_i^{-1}\,dt_1\cdots dt_{l-1}$. This measure is
invariant under all permutations of the $l$ coordinates: the density is
symmetric, a transposition of two of $t_1,\dots,t_{l-1}$ has Jacobian $-1$, and
the transposition of $t_j$ with $t_l=1-\sum_{i<l}t_i$ replaces $t_j$ by
$1-\sum_{i<l}t_i$, a linear change with determinant $-1$. Off a null set
exactly one coordinate is minimal; by symmetry,

$$
T_l(b_1,1)=\frac l{l!}\int_{\Sigma_l\cap\{t_1<t_i,\ 2\le i\le l\}}
\prod_{i\le l}\frac1{t_i}\,dt_1\cdots dt_{l-1}.
$$

Put $\alpha=t_1$. Two coordinates are at least $\alpha$ and sum to at most one,
so $b_1\le\alpha\le1/2$. For fixed $\alpha$, the remaining
$t_2,\dots,t_{l-1}$ range, up to null boundaries, over
$\Omega_{l-1}(\alpha,1-\alpha)$, with integrand
$(1-\alpha-\sum_{2\le i<l}t_i)^{-1}\prod_{2\le i<l}t_i^{-1}$; for $l=2$ the
inner integral is the value $(1-\alpha)^{-1}$. Since $l/l!=1/(l-1)!$, Tonelli's
theorem gives

$$
T_l(b_1,1)=\int_{b_1}^{1/2}T_{l-1}(\alpha,1-\alpha)\frac{d\alpha}\alpha .
$$

Summing the finitely many $l\ge2$ proves the identity. $\square$

The term $1$ is the one-prime contribution to $D_{b_1}(1)$; the integral is
the composite part, organized by the least prime factor.

## The bound (7.19)

**Bound.** There are absolute $b_0,c'>0$ such that for $0<b_1\le b_0$,

$$
D_{b_1}(1)\le\frac{e^{-\gamma_E}}{b_1}\bigl(1+c'e^{-1/(20b_1)}\bigr).
$$

*Lower count.* Let $\Phi(x)=\#\{x<m\le2x:P^-(m)>x^{b_1}\}$. Every $m$ with
$\Omega(m)=l$ has at most $l!$ ordered prime factorizations, so ordered lists of
primes above $x^{b_1}$ with product in $(x,2x]$, each with weight $1/l!$, give
every integer total weight at most one, repetitions included. Fix
$\eta'>0$. The case $l=1$ gives $\pi(2x)-\pi(x)=(1+o(1))x/L$. For $l\ge2$
restrict the first $l-1$ primes to $t_i>b_1$ and $s(t)<1-b_1-\eta'$ and sum the
last prime over $(x/Q,2x/Q]$; it is then automatically above
$x^{b_1+\eta'}$, and the prime number theorem gives
$(1+O(L^{-1}))x/(QL(1-s(t)))$ of them. The same cube comparison, with infima on
cubes in place of suprema, gives

$$
\liminf_{x\to\infty}\frac Lx\Phi(x)\ge1+\sum_{l\ge2}\frac1{l!}
\int_{\Omega_l(b_1,1)\cap\{s<1-b_1-\eta'\}}\frac1{1-s(t)}\prod_{i<l}
\frac{dt_i}{t_i}\xrightarrow[\eta'\to0]{}D_{b_1}(1)
$$

by monotone convergence.

*Upper count.* The fourth instance of the
[[research/smooth_successor_estimates/block_sieve|block sieve]], at
$z=x^{b_1}$ with $g(p)=1/p$ and $h=2\lfloor1/(40b_1)\rfloor$, gives
$\Phi(x)\le xV(x^{b_1})(1+c_1e^2e^{-1/(20b_1)})+x^{1/5+2b_1}$ once $h\ge h_0$,
which fixes $b_0$. By Mertens, $LV(x^{b_1})\to e^{-\gamma_E}/b_1$, and the
remainder is $o(x/L)$.

Combining, $D_{b_1}(1)\le\liminf L\Phi(x)/x\le\limsup L\Phi(x)/x\le
(e^{-\gamma_E}/b_1)(1+c'e^{-1/(20b_1)})$ with $c'=c_1e^2$. $\square$

The bound is a statement about a fixed number, obtained from two ordinary
counts; no unrestricted pointwise density theorem is imported.

## The mesh step

The extraction sums the bin constants
$\sup_{\gamma\le a\le\gamma'}D_\gamma(1-a)\log(\gamma'/\gamma)$. On
$\{(\gamma,a):b_1\le\gamma\le a\le1/2-\kappa\}$ the map
$(\gamma,a)\mapsto D_\gamma(1-a)$ is uniformly continuous, since there
$1-a-\gamma\ge2\kappa$; let $\omega$ be its modulus. For a partition of
$[b_1,1/2-\kappa]$ of mesh at most $\delta_0$, every $\alpha$ and $a$ in the
bin $[\gamma,\gamma']$ satisfy
$D_\gamma(1-a)\le D_\alpha(1-\alpha)+\omega(2\delta_0)$. Integrating against
$d\alpha/\alpha$ over each bin and summing,

$$
\sum_{\rm bins}\sup_{\gamma\le a\le\gamma'}D_\gamma(1-a)\log\frac{\gamma'}\gamma
\le\int_{b_1}^{1/2-\kappa}D_\alpha(1-\alpha)\frac{d\alpha}\alpha
+\omega(2\delta_0)\log\frac1{2b_1}.
$$

A fixed mesh makes the last term at most $1/10$, as the extraction requires.
The bins then remove at most
$\frac{\mathfrak SX_A}L\{D_{b_1}(1)-1+\frac1{10}+o(1)\}$ by the identity, while
the preliminary sieve retains at least
$\frac{\mathfrak SX_A}L\{\frac{e^{-\gamma_E}}{b_1}(1-O(e^{-1/(20b_1)}))+o(1)\}$.
By (7.19) the difference is at least
$\frac{\mathfrak SX_A}L\{1-\frac1{10}-O(b_1^{-1}e^{-1/(20b_1)})+o(1)\}$, as on
the extraction page.
