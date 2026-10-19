---
name: theory/number_theory/L43_continuous_totient_phase_ratio/_proof
title: One-sided limits, unit increments and the boundary factor
desc: |
  Piecewise continuity of the finite coefficients, removal of interior jumps
  by unit increments of the two counts, and the common jump factor of G_m at
  the end of a phase period.
created: 2026-10-14T10:19:33Z
updated: 2026-10-14T10:19:33Z
---

***

We prove [[theory/number_theory/L43_continuous_totient_phase_ratio/_index|L43]].
The source results are conditional premises from the
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|unrefereed manuscript]];
[[theory/number_theory/L65_conditional_totient_ratio_coefficient/_index|L65]]
is used as stated. Natural logarithms are used throughout.

## Notation

Write $B=\log\log x$, $\psi(B)=(\log B-\log\log B)/\lambda$,
$m=\lfloor\psi(B)\rfloor$, $\theta(x)=\psi(B)-m$ and
$Z(x)=xG_m/\log x$, as in the manuscript's Equations (2.3)–(2.4). Call the
set of $x$ with $m(x)=n$ the $n$-th period. For $B>e$,

$$
\psi'(B)=\frac1{\lambda B}\Bigl(1-\frac1{\log B}\Bigr)\in
\Bigl(0,\frac1{\lambda B}\Bigr),
$$

so $\theta$ is continuous and strictly increasing on each period, and the
mean value theorem gives

$$
0<\psi(B(x+1))-\psi(B(x))\le\frac1{\lambda\,x\log x\log\log x}.  \tag{1}
$$

Let $C(x)$ be either $V(x)$ or $V'(x)$, and let $A(s)$ be correspondingly
$A(1;s)$ or $A(f_0;s)$. Theorem 2.1 of the manuscript and L65 give

$$
C(x)=Z(x)\bigl(A(\theta(x))+o(1)\bigr),\qquad
0<c_-\le A(s)\le c_+<\infty .                                   \tag{2}
$$

Each count increases by at most one from $x$ to $x+1$: the interval
$(x,x+1]$ contains one integer, which is at most one new totient and at
most one new argument of $\varphi$. Both counts tend to infinity, since
$C(x)\ge V'(x)\ge\pi(x)$. Hence

$$
\frac{C(x\pm1)}{C(x)}\longrightarrow1 .                         \tag{3}
$$

## Finite coefficients have one-sided limits

Fix a sufficiently large $H$ and $f:[1,\infty)\to[0,1]$. By the
manuscript's Lemma 6.3, the witnesses of all phases form one finite set,
and all tail totients $d$ with a witness form a finite set. In (2.5) the
phase enters only through $\alpha_s=\lambda e^{\lambda s}$, which is
continuous and strictly increasing, in two conditions:
$0.9\alpha_sh\rho^{-h}\le v_h\le1.1\alpha_sh\rho^{-h}$ for $P\le h<H$, and
$\log a\le\exp(2\alpha_sP\rho^{-P})$. Each condition holds for $s$ in an
interval: the first for
$v_h/(1.1h\rho^{-h})\le\alpha_s\le v_h/(0.9h\rho^{-h})$, the second for all
$s$ when $a\le e$ and otherwise for $\alpha_s\ge\log\log a/(2P\rho^{-P})$.
The remaining conditions of (2.5) do not involve $s$. Hence each witness is
admissible exactly on an interval of phases, and the finitely many endpoints
of these intervals cut $[0,1)$ into finitely many open intervals and points
on each of which every witness set $\mathcal W_{H,s}(d)$ is constant.

On such an open interval, Equation (2.8) is a finite sum of terms

$$
c\,\alpha_s^{-H}\exp\Bigl(-\frac\gamma{\alpha_s}S_T\Bigr),
\qquad
S_T=\sum_{h\ge H}\rho^h\max_{\eta\in T}D(h,\eta),
$$

where $c$ and the absolutely convergent $S_T$ do not depend on $s$: by
(2.6), $D(h,\eta)$ depends only on the coordinates $v_l$ of the witness.
Each term is the restriction of a continuous function of all real $s$.
Therefore $A_H(f;\cdot)$ is continuous outside finitely many points and has
a right limit at every $s\in[0,1)$ and a left limit at every $s\in(0,1]$.

Suppose $A_H\to A$ uniformly on $[0,1)$ and fix $s^*\in(0,1]$. Given
$\varepsilon>0$, choose $H$ with $\sup|A_H-A|<\varepsilon/3$, and then
$\delta>0$ such that $|A_H(t)-A_H(t')|<\varepsilon/3$ whenever
$s^*-\delta<t,t'<s^*$. Then $|A(t)-A(t')|<\varepsilon$ for those $t,t'$, so
$A$ has a left limit at $s^*$ by the Cauchy criterion. Right limits are
identical. This applies to $A(1;\cdot)$ by Theorem 2.1 and to
$A(f_0;\cdot)$ by L65.

## Interior points

Fix $s^*\in(0,1)$. As in the manuscript's Lemma 6.6, for each large $n$
there is $y_n$ with $\psi(B(y_n))=n+s^*$, so $m(y_n)=n$ and
$\theta(y_n)=s^*$. By (1), $\psi(B(y_n\pm1))=n+s^*+o(1)$, so for large $n$
the points $y_n\pm1$ lie in the $n$-th period and

$$
\theta(y_n-1)<s^*<\theta(y_n+1),\qquad
\theta(y_n\pm1)\longrightarrow s^* .
$$

Within one period $m=n$ is fixed and
$G_n(B')/G_n(B)=(B'/B)^n$. Since $n\le\psi(B)+1\ll\log B$ and, by
$dB/dx=1/(x\log x)$, $0<\log(B(x+1)/B(x))\le1/(Bx\log x)$,

$$
\frac{Z(y_n\pm1)}{Z(y_n)}\longrightarrow1 .                    \tag{4}
$$

Divide (2) at $y_n\pm1$ by (2) at $y_n$, and use (3), (4) and the bounds in
(2):

$$
A(\theta(y_n\pm1))=A(s^*)+o(1).
$$

The left side tends to the right limit $A(s^{*+})$ along $y_n+1$ and to the
left limit $A(s^{*-})$ along $y_n-1$. Hence
$A(s^{*-})=A(s^*)=A(s^{*+})$, and $A$ is continuous at $s^*$. The same
argument along $y_n+1$, with $s^*=0$, proves right continuity at $0$.

## The end of a period

For each large $n$ let $x_n$ satisfy $\psi(B_n)=n$, where
$B_n=B(x_n)$. Then $m(x_n)=n$ and $\theta(x_n)=0$, while (1) gives
$m(x_n-1)=n-1$ and $\theta(x_n-1)\to1$ from below. Moving the argument of
$G_{n-1}$ from $B(x_n-1)$ to $B_n$ as in (4),

$$
\frac{Z(x_n-1)}{Z(x_n)}
=(1+o(1))\frac{G_{n-1}(B_n)}{G_n(B_n)}
=(1+o(1))\frac{n\,g_n}{B_n}.
$$

The recurrence (2.2) gives $g_n\rho^n\to\gamma$. Here is a direct
justification. Put $F(z)=\sum_{j\ge1}a_jz^j$, analytic for $|z|<1$ since
$a_j=O(\log(j+1))$. The generating function of $g_n$ is $1/(1-F(z))$.
On $|z|\le\rho$, the triangle inequality and positivity of every $a_j$
show that $F(z)=1$ only at $z=\rho$. This zero of $1-F$ is simple.
Consequently, for some $\rho<R<1$,

$$
\frac1{1-F(z)}-\frac\gamma{1-z/\rho}
$$

is analytic on $|z|<R$: the pole cancels because
$\gamma=1/(\rho F'(\rho))$, and isolation of zeros leaves a larger
zero-free disk after that cancellation. Cauchy's coefficient bound on any
circle of radius $r$ with $\rho<r<R$ gives
$g_n=\gamma\rho^{-n}+O(r^{-n})$, proving the limit.
The equation $\psi(B_n)=n$ says
$B_n=\rho^{-n}\log B_n$ and $\log B_n=\lambda n+\log\log B_n$, so
$\log B_n/n\to\lambda$ and

$$
\frac{n\,g_n}{B_n}=\frac{n\,g_n\rho^n}{\log B_n}
\longrightarrow\frac\gamma\lambda .                             \tag{5}
$$

Now divide (2) at $x_n-1$ by (2) at $x_n$ and use (3) and (5):

$$
\frac\gamma\lambda\,
\frac{A(\theta(x_n-1))+o(1)}{A(0)+o(1)}\longrightarrow1 .
$$

Since $\theta(x_n-1)$ tends to $1$ from below and $A$ has a left limit at
$1$, that limit equals $(\lambda/\gamma)A(0)$. This holds for
$A(1;\cdot)$ and $A(f_0;\cdot)$ with the same factor.

## The quotient and the limit set

The denominator of $q=A(f_0;\cdot)/A(1;\cdot)$ is at least $c_->0$, so $q$
is continuous on $[0,1)$, and its left limit at $1$ is

$$
\frac{(\lambda/\gamma)A(f_0;0)}{(\lambda/\gamma)A(1;0)}=q(0).
$$

Thus $q$ is a continuous function on $\mathbb R/\mathbb Z$. By (10) of L65,
$V(x)/V'(x)=1/q(\theta(x))+o(1)$. Every value $1/q(s)$ is a limit along
the exact-phase sequence of $s$. Conversely, if
$V(x_k)/V'(x_k)\to L$, choose a subsequence with $\theta(x_k)$ converging
in $\mathbb R/\mathbb Z$ to some $t$; continuity gives $L=1/q(t)$. The limit
set is therefore the image of the circle under the continuous function
$1/q$, a compact interval.

By L65, $V/V'$ converges if and only if $q$ is constant. A continuous
function on the circle is the uniform limit of the Fejér means of its
Fourier series, so it is constant if and only if

$$
\hat q(n)=\int_0^1q(s)e^{-2\pi ins}\,ds=0\qquad(n\ne0).
$$

For large $H$, uniform convergence gives $A_H(1;\cdot)\ge c_-/2$, so
$q_H=A_H(f_0;\cdot)/A_H(1;\cdot)$ is defined, piecewise continuous, and
converges uniformly to $q$. Hence $\hat q(n)$ is the limit of the
corresponding integrals of $q_H$.

## The boundary factor is not one

The coefficients $a_j=\int_j^{j+1}\log t\,dt$ are strictly increasing and
grow at most logarithmically. Absolute convergence therefore permits
reindexing to give

$$
(1-\rho)\sum_{j\ge1}ja_j\rho^j-\sum_{j\ge1}a_j\rho^j
=\sum_{j\ge2}(j-1)(a_j-a_{j-1})\rho^j>0.
$$

The two sums on the left are $1/\gamma$ and $1$, respectively. Hence

$$
\gamma<1-\rho<-\log\rho=\lambda.
$$

The second inequality is strict for $0<\rho<1$. If $A(1;\cdot)$ were
constant, its left limit at $1$ would equal $A(1;0)>0$, contradicting the
factor $\lambda/\gamma>1$.
