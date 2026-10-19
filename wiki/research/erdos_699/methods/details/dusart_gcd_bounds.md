---
name: research/erdos_699/methods/details/dusart_gcd_bounds
title: "Erdős 699: sharper numerical coefficient-gcd estimates"
desc: "Two retained Dusart bounds improve the uniform prime-interval calculation used to instantiate BFT cofactor estimates."
created: 2026-09-22T05:10:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: sharper numerical coefficient-gcd estimates

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/asymmetric_cofactors|Asymmetric cofactor estimates]]

***

The finite prime-interval argument for the BFT coefficient gcd can use
substantially smaller uniform errors than the original implementation.
This matters when an interpolation certificate needs a cofactor exponent
close to the limiting BFT value. All source inputs below are already
retained in the repository.

Write $\vartheta(x)=\sum_{p\le x}\log p$. Dusart's retained
2010 paper,
Proposition 5.1, gives

$$
\vartheta(x)<\left(1+\frac1{36260}\right)x\qquad(x>0). \tag{1}
$$

Its Theorem 5.2 gives

$$|\vartheta(x)-x|<\frac{x}{100\log^2x}
\qquad(x\ge7\,713\,133\,853). \tag{2}$$

For $x\ge10^{11}$, the relative error in (2) is less than $1/60000$:
$\log10>9/4$ and $(11\cdot9/4)^2>600$ suffice. On
$1\le x\le10^{11}$, BFT Lemma 5.4 gives
$\vartheta(x)>x-2.072\sqrt{x}$. Consequently the following bounds
hold simultaneously for every $x\ge1$:

$$
x\left(1-\max\left\{\frac{2.072}{\sqrt{x}},\frac1{60000}\right\}\right)
<\vartheta(x)<\left(1+\frac1{36260}\right)x. \tag{3}
$$

Thus neither error must retain the previous floor $0.000213$.
The lower error still decreases explicitly with $x$ until it reaches
the new floor.

## A rational coefficient-gcd certificate

Let $c>d\ge1$ be coprime, $h=c+d$, and retain $1\le t\le T$ with
$m_0\ge2T$. Put

$$k=\left\lfloor\frac{dt}{h}\right\rfloor,\qquad
r=dt-hk.$$

For each $2r>h$, the same common subintervals of BFT Lemma 5.2 used in
the [earlier numerical calculation](bft_numerical_thresholds.md)
have endpoints

$$
U_t(m)=\frac{hm-2}{t},\qquad
V_t(m)=m\max\left\{\frac d{k+1},
                  \frac{c-d}{t-2k-1}\right\}.
$$

They give disjoint prime contributions to both
$\mathcal G(c,d,dm)$ and $\mathcal G(c,d,dm-1)$. Applying (3), discarding
negative contributions, and dividing by $dm$ gives the lower bound

$$
\sum_{\substack{1\le t\le T\\2r>h}}
\frac1{dm}\max\left\{
(1-\epsilon_t(m))U_t(m)
-\frac{36261}{36260}V_t(m),\ 0\right\}, \tag{4}
$$

where $\epsilon_t(m)=\max\{2.072/\sqrt{U_t(m)},1/60000\}$.
Each summand is nondecreasing for $m\ge m_0$:
$U_t(m)/m$ increases, $\epsilon_t(m)$ decreases, and $V_t(m)/m$ is
constant. It therefore suffices to evaluate (4) at $m_0$.

The [integer checker](../../computations/erdos_699_bft_dusart_gcd.py)
bounds each square root from below by an integer square root divided by
a fixed scale, and rounds every positive summand downward. Its rational
output $\ell$ proves

$$\mathcal G(c,d,dm-\delta)\ge\exp(dm\ell)
\qquad(m\ge m_0,\ \delta\in\{0,1\}). \tag{5}$$

This output can be passed directly to the existing asymmetric and
product cofactor evaluators. The original coefficient-gcd checker and
its previously retained certificates are unchanged.

For example, $(c,d)=(132,91)$, $m_0=10^6$, and $T=4000$ give the exact
certificate

$$
\ell=\frac{105451178659}{250000000000}.
$$

This is a uniform analytic bound on all $m\ge m_0$, not a test of a
bounded set of binomial rows.
