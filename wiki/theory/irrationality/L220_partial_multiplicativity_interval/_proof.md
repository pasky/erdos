---
name: theory/irrationality/L220_partial_multiplicativity_interval/_proof
title: Proof of the interval of partially multiplicative totient comparisons
desc: |
  Greedy rounding against complete smooth-orbit weights preserves finitely
  many prime multiplication laws; sparse composite rough parts protect every
  prime-power value, and a nearby target keeps all coefficients positive.
tags: []
sources:
- theory/irrationality/L220_partial_multiplicativity_interval/_index
created: 2026-10-15T21:48:35Z
updated: 2026-10-15T21:48:35Z
---

***

This is the complete author-recorded proof of
[[theory/irrationality/L220_partial_multiplicativity_interval/_index|L220]].
Fix $y,M,\varepsilon$ as in its statement. Let $\mathcal H$ consist of the
positive integers all of whose prime factors are at most $y$, including
$1$, and put $P=\prod_{p\le y}p$. Every positive integer has a unique
factorization $n=sk$ with $s\in\mathcal H$ and $\gcd(k,P)=1$.

Choose distinct primes $r_0,t_0>y$ and put $Q=r_0t_0P$. The progression
$e\equiv r_0t_0\pmod Q$ consists of integers coprime to $P$ and divisible
by both $r_0,t_0$. In particular none is $1$ or a prime power. Write
$g(e)=\lfloor\tfrac14\log_2e\rfloor$. Choose $e_1$ in this progression
sufficiently large that, for every $e\ge e_1$,

$$
g(e)\ge2Q,\qquad
\frac{3M}{2}e^{1/4}\le\varepsilon\sqrt{e/2}.
\tag{1}
$$

Set $e_{j+1}=e_j+Q\lfloor g(e_j)/Q\rfloor$ and $E=\{e_1,e_2,\ldots\}$.
All these integers remain in the progression, and their gaps satisfy
$g(e_j)/2\le e_{j+1}-e_j\le g(e_j)$. Thus

$$
E(X):=\#(E\cap[1,X])=O\bigl(X/\log(X+2)\bigr).
\tag{2}
$$

For completeness, elements up to $\sqrt X$ contribute at most $\sqrt X$;
above $\sqrt X$ their gaps are at least a fixed positive multiple of
$\log X$, once $X$ is sufficiently large. Enlarging the constant covers
the bounded range.

The entire binary weight of the orbit with rough part $e$ is

$$
A_e=\sum_{s\in\mathcal H}\varphi(s)2^{-se}.
$$

For $e\ge2$, positivity, the term $s=1$ and $\varphi(s)\le s$ give

$$
2^{-e}\le A_e\le\frac{2^{-e}}{(1-2^{-e})^2}<2^{1-e}.
\tag{3}
$$

Put $d=MA_{e_1}/2$. For any real $r$ with $|r-S|<d$, start with
$\eta_0=r-S$, and define, with nearest-integer rounding,

$$
\delta_j=M\left\lfloor\frac{\eta_{j-1}}{MA_{e_j}}\right\rceil,
\qquad
\eta_j=\eta_{j-1}-\delta_j A_{e_j}.
\tag{4}
$$

Then $\delta_1=0$, every $\delta_j$ is divisible by $M$, and
$|\eta_j|\le MA_{e_j}/2$. For $j\ge2$, (3) and the gap bound give

$$
\begin{aligned}
|\delta_j|
&\le\frac M2\left(\frac{A_{e_{j-1}}}{A_{e_j}}+1\right)\\
&\le M2^{e_j-e_{j-1}}+\frac M2
\le\frac{3M}{2}e_j^{1/4}
\le\varepsilon\sqrt{e_j/2}
\le\varepsilon\varphi(e_j).
\end{aligned}
\tag{5}
$$

The last elementary bound follows by taking the product over $p^a\Vert n$
in $\varphi(n)^2/n$: the factor $p^{a-2}(p-1)^2$ is at least one for odd
$p$, and the factor for $p=2$, when present, is at least $1/2$.

Define $h(e_j)=\varphi(e_j)+\delta_j$ and $h(k)=\varphi(k)$ at all other
integers coprime to $P$. For the unique decomposition $n=sk$ above, set

$$
f(n)=\varphi(s)h(k).
\tag{6}
$$

Equation (5), including $\delta_1=0$, proves positivity, integrality and
the asserted relative bounds. It also gives $f(n)\equiv\varphi(n)\pmod M$.
Every prime power has rough part either $1$ or a prime power, hence outside
$E$, so its value is unchanged. Multiplication by a prime $p\le y$ changes
only the smooth part $s$. The two required laws for $f(pn)$ therefore
follow from the corresponding exact laws for $\varphi(s)$.

The relative bound implies absolute convergence. The orbits with distinct
rough parts are disjoint, so absolute convergence permits regrouping:

$$
\sum_{n\ge1}(f(n)-\varphi(n))2^{-n}
=\sum_{j\ge1}\delta_j A_{e_j}
=r-S.
\tag{7}
$$

The last equality follows by telescoping (4), since (3) implies
$\eta_j\to0$. All orbit terms were included in $A_e$; there is no omitted
contribution from multiples of the changed integers.

Finally the changed set is contained in $\{se:s\in\mathcal H,e\in E\}$.
For $s\le\sqrt X$, (2) bounds its count by
$O(X\sum_{s\in\mathcal H}s^{-1}/\log X)$. For $s>\sqrt X$, the crude
bound $E(X/s)\le X/s$ gives at most

$$
X\sum_{\substack{s\in\mathcal H\\s>\sqrt X}}\frac1s
\le X^{3/4}\sum_{s\in\mathcal H}s^{-1/2}=O(X^{3/4}).
$$

Both sums over $\mathcal H$ converge, being finite Euler products
$\prod_{p\le y}(1-p^{-\alpha})^{-1}$ for $\alpha=1,1/2$. This proves the
claimed $O(X/\log X)$ bound and completes the proof. $\square$
