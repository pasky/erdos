---
name: theory/polynomials/L144_cubic_lemniscate_length/_proof
title: Explicit length integrals and their ball-arithmetic bounds
desc: Root identities give exact length integrals; a comparison with z^3-c and box-uniform ball bounds over two parameter regimes prove the family inequality.
created: 2026-10-15T11:10:00Z
updated: 2026-10-15T11:10:00Z
---

***

Use the notation of
[[theory/polynomials/L144_cubic_lemniscate_length/_index|L144]]. Throughout,
$0\le a\le2^{-1/3}$, $c=\sqrt{1-4a^6}$, and

$$
P(z)=z^3+3a^2z,\qquad q_a=P-c,\qquad L(a)=\ell(q_a),\qquad
L_0=L(0)=\ell(z^3-1).
$$

Put $\beta=\arcsin(2a^3)\in[0,\pi/2]$, so that $c=\cos\beta$.

## 1. Reduction of all cubics to the family

By Lemmas 4 and 5 of Eremenko and Hayman, some monic cubic $p^*$ maximizes
$\ell$ and has all its critical points on its lemniscate, so its critical
values have modulus one. A translation and the rotation
$p(z)\mapsto e^{-3i\theta}p(e^{i\theta}z)$ preserve monicity and length, so
we may take $p^*(z)=z^3-3u^2z+b$ with $b\le0$. Its critical values are
$b\mp2u^3$, and $|b-2u^3|=|b+2u^3|=1$ gives $\operatorname{Re}(b\bar u^3)=0$
and $b^2+4|u|^6=1$. If $b<0$, then $u^3$ is purely imaginary, and a rotation
by a multiple of $2\pi/3$, which fixes $b$, makes $u=\pm ia$ with $a=|u|$.
If $b=0$, an arbitrary rotation achieves the same normalization. Thus
$p^*=q_a$. This is the normalization of the
[[research/erdos_114/cubic_extremizer_reduction|research sketch]]. Hence every
monic cubic $p$ has $\ell(p)\le\ell(p^*)=L(a)$ for some $a$, and the
inequality for every cubic follows from the family inequality.

## 2. The length integral

The lemniscate of $q_a$ is $P^{-1}(C)$, where $C=\{s:|s-c|=1\}$. The critical
points of $P$ are $\pm ia$, with critical values $s_\pm=\pm2ia^3$, and both
lie on $C$ since $4a^6+c^2=1$. Away from these two values, $P$ restricted to
$P^{-1}(C)$ is a three-sheeted covering by analytic arcs, and on each arc
$|dz|=|ds|/|P'(z)|$. Therefore

$$
L(a)=\int_0^{2\pi}G_a(c+e^{i\theta})\,d\theta,\qquad
G_a(s)=\sum_{P(z)=s}\frac1{|P'(z)|},
$$

and the conjugation symmetry $G_a(\bar s)=G_a(s)$ gives
$L(a)=2\int_0^\pi G_a(c+e^{i\theta})\,d\theta$. On $C$ the critical values sit
at $\theta_\pm=\pi\mp\beta$. For $a=0$ the roots of $z^3=s$ give
$G_0(s)=|s|^{-2/3}$.

## 3. Root identities

If $P(z)=s$, expansion gives

$$
(z^2+a^2)^2(z^2+4a^2)=z^6+6a^2z^4+9a^4z^2+4a^6=s^2+4a^6.
$$

Since $P'(z)=3(z^2+a^2)$, for $s\ne s_\pm$,

$$
\frac1{|P'(z)|}=\frac{|z^2+4a^2|^{1/2}}{3|s^2+4a^6|^{1/2}}.
$$

Let $U$ be either root of $U-a^6/U=s$ and let $u_1,u_2,u_3$ be the cube roots
of $U$. Then $(u-a^2/u)^3+3a^2(u-a^2/u)=u^3-a^6/u^3=s$, the roots of $P(z)=s$
are $u_j-a^2/u_j$ (the other choice of $U$ is $-a^6/U$, whose cube roots are
$-a^2/u_j$, giving the same roots), and $z^2+4a^2=(u+a^2/u)^2$. Hence

$$
G_a(s)=\frac{\sum_j|u_j+a^2/u_j|}{3|s^2+4a^6|^{1/2}}. \tag{1}
$$

For $a>0$ put $\sigma=s/a^3$. Then $G_a(s)=a^{-2}G_1(\sigma)$, where $G_1$ is
(1) with $a=1$.

## 4. The comparison with $z^3-c$

Let $\Phi(c)=\int_0^{2\pi}|c+e^{i\theta}|^{-2/3}\,d\theta$, the length of
$\{|z^3-c|=1\}$. For $0\le c<1$,
$(1+ce^{i\theta})^{-1/3}=\sum_kb_kc^ke^{ik\theta}$
with $b_k=\binom{-1/3}k$, and Parseval gives
$\Phi(c)=2\pi\sum_kb_k^2c^{2k}$, strictly increasing for $c>0$. To pass to
$c=1$, use $|c+e^{i\theta}|^2=(1-c)^2+c|1+e^{i\theta}|^2$ for $c\ge1/2$
and dominated convergence; the limiting singularity has exponent $-2/3$.
Monotone convergence of the series and the beta integral at $c=1$ give

$$
\Phi(c)\le\Phi(1)=L_0=2\pi\,{}_2F_1\!\left(\tfrac13,\tfrac13;1;1\right)
=\frac{2\pi\,\Gamma(1/3)}{\Gamma(2/3)^2}
=2^{1/3}B\!\left(\tfrac12,\tfrac16\right)\approx9.1797.
$$

Indeed $|1+e^{i\theta}|=2|\cos(\theta/2)|$ evaluates the integral as the beta
value displayed, and the gamma duplication formula gives the gamma quotient.

For $a>0$ write $g(\sigma)=G_1(\sigma)-|\sigma|^{-2/3}$ and let $\Gamma_a$ be
the circle $|a^3\sigma-c|=1$, the image of $C$. Since $G_a(s)=a^{-2}G_1(\sigma)$,
$|s|^{-2/3}=a^{-2}|\sigma|^{-2/3}$ and $|ds|=a^3|d\sigma|$,

$$
L(a)=\Phi(c)+a\,I(a),\qquad I(a)=\int_{\Gamma_a}g(\sigma)\,|d\sigma|,
\qquad\text{so}\qquad L(a)\le L_0+a\,I(a). \tag{2}
$$

## 5. Small parameters: $0<a\le13/64$

Here it suffices that $I(a)<0$. The circle $\Gamma_a$ has center $c/a^3$ and
radius $a^{-3}$ and passes through $\pm2i$. For $a\le13/64$ one has
$a^6\cdot50^2<1$ and $c/a^3>50$. Hence the arc of $\Gamma_a$ near the origin is
the graph

$$
x=x_a(y)=\frac{a^3(y^2-4)}{c+\sqrt{1-a^6y^2}},\qquad |y|\le50,\qquad
|d\sigma|=\frac{dy}{\sqrt{1-a^6y^2}},
$$

and every other point of $\Gamma_a$ has $|\sigma|\ge50$. The integrand and the
arc are symmetric under conjugation.

*Tail.* Let $|\sigma|\ge Y>2$, let $T$ be the root of $T-1/T=\sigma$ with
$|T|\ge1$, so $|T|\ge|\sigma|-1$, let $\tau$ be a cube root of $T$,
$\varepsilon=\tau^{-2}$ and $e=|\varepsilon|=|T|^{-2/3}\le(Y-1)^{-2/3}$. From
(1) with $a=1$,

$$
g(\sigma)=|T|^{-2/3}\left(\frac{A(\varepsilon)}{|1+\varepsilon^3|}
-|1-\varepsilon^3|^{-2/3}\right),\qquad
A(\varepsilon)=\frac13\sum_{j=0}^2|1+\varepsilon\omega^{-2j}|,
$$

with $\omega=e^{2\pi i/3}$. The real parts of the three terms of $A$ sum to
three, and $|1+w|\le1+\operatorname{Re}w+|w|^2/(2(1-|w|))$, so
$1\le A\le1+e^2/(2(1-e))$. With $(1+e^3)^{-2/3}\ge1-\tfrac23e^3$ and
$(1-e^3)^{-2/3}\le(1-e^3)^{-1}$ this gives $|g(\sigma)|\le K|T|^{-2}\le
K(|\sigma|-1)^{-2}$, where

$$
K=\max\left\{\frac{e+1/(2(1-e))}{1-e^3}+\frac{2e}3,\ \frac{2e}{1-e^3}\right\},
\qquad e=(Y-1)^{-2/3}.
$$

Parametrize $C$ by $s=c-e^{i\psi}$. Denote the near arc by $\mathcal A_Y$;
it is $|\psi|\le\psi_Y$
with $\sin\psi_Y=a^3Y$, and on the rest $|s|\ge a^3Y$ and
$|s|^2\ge4c\sin^2(\psi/2)$. Hence

$$
\int_{\Gamma_a\setminus\mathcal A_Y}\frac{|d\sigma|}{(|\sigma|-1)^2}
\le\frac{a^3}{(1-1/Y)^2}\int_{\psi_Y<|\psi|\le\pi}\frac{d\psi}{|s|^2}
\le\frac{a^3\cot(\psi_Y/2)}{c(1-1/Y)^2}\le\frac{2}{cY(1-1/Y)^2}.
$$

With $Y=50$ this tail is at most $0.03$ in absolute value.

*Near arc.* For each box $a\in[k/64,(k+1)/64]$, $0\le k\le12$, the program
bounds $2\int_0^{50}g(x_a(y)+iy)(1-a^6y^2)^{-1/2}dy$ from above, uniformly
for $a$ in the box. On $[0,2^{-10}]$ it uses $|\sigma|\le X+y$, with $X$ the
largest $|x_a|$ there, so the subtracted term is at least
$3[(X+2^{-10})^{1/3}-X^{1/3}]$. On $[2-2^{-13},2+2^{-13}]$ it uses
$G_1(\sigma)=N_1(\sigma)/(3|\sigma-2i|^{1/2}|\sigma+2i|^{1/2})$ with a ball
enclosure of the numerator and $|\sigma-2i|\ge|y-2|$, so that the window
contributes at most the enclosure times $4\cdot2^{-13/2}$. Elsewhere it sums
the supremum of a ball enclosure of the integrand over each piece times the
piece width. Every box gives $I(a)<0$; the largest bound is about $-0.216$.
By (2), $L(a)<L_0$ for $0<a\le13/64$.

The first parameter box includes $a=0$ only as an enclosure of the continuous
formula for $x_a(y)$ and its weight. The circle $\Gamma_a$ and (2) are used
only for $a>0$; at $a=0$ the target equality is exact. The head estimate
integrates the $|y|^{-2/3}$ singularity rather than evaluating it at zero,
and the window estimate integrates the $|y-2|^{-1/2}$ singularity. Thus no
positive lower cutoff on $a$ or on distance to either singularity is assumed.

## 6. Larger parameters: $7/512\le\beta\le\pi/2$

Here the program bounds $L(a)=2\int_0^\pi G_a(c+e^{i\theta})d\theta$ itself,
uniformly for $\beta$ in each box, with $c=\cos\beta$ and $a^3=\sin\beta/2$.
A window $W$ contains $\theta_+=\pi-\beta$ for every $\beta$ in the box. On it,
$G_a(s)=N_a(s)/(3|s-s_+|^{1/2}|s-s_-|^{1/2})$ by (1), with
$|s-s_+|=2|\sin((\theta-\theta_+)/2)|\ge(2/\pi)|\theta-\theta_+|$ and
$\int_W|\theta-\theta_+|^{-1/2}d\theta\le2\sqrt{2|W|}$; so the window is
bounded by the supremum of $N_a/(3|s-s_-|^{1/2})$ over $W$ times
$(\pi/2)^{1/2}\,2\sqrt{2|W|}$. The point $\theta_-=\pi+\beta$ lies outside
$[0,\pi]$. Off the window the program sums piece suprema of ball enclosures
of (1). Starting from 300 equal boxes and bisecting any box whose bound is not
below $L_0-1/100$, it covers $[7/512,\pi/2]$ by 591 consecutive boxes, each
with $L(a)<L_0-1/100$.

The program checks $0<\inf W<\sup W<\pi$ and inclusion of every possible
$\theta_+$ before accepting a window. It integrates the nonnegative density
up to an upper dyadic enclosure $\pi_+\ge\pi$ for an upper bound. The
parameter cover likewise ends at a dyadic enclosure of $\pi/2$ from above,
so it includes $c=0$ without assuming $c>0$. The density formula remains
valid in this small extension by taking $c=\cos\beta$ and
$a^3=\sin\beta/2$.

## 7. Coverage and conclusion

The program checks $7/512<\arcsin(2(13/64)^3)$, so the two regimes overlap and
together cover $0<a\le2^{-1/3}$. Hence $L(a)<L_0$ for every $a$ in that range.
With Section 1, every monic cubic $p$ satisfies $\ell(p)\le L_0$.

On the nonsingular pieces, every bound in Sections 5 and 6 is a finite sum
of exact piece widths times enclosing endpoints of arb balls. The explicit
head, window and tail estimates bound all omitted pieces. All formulas take
the whole parameter box as their input, so the bound holds at every
parameter in that box, rather than only at sampled values. Stopping an
integration subdivision at its depth limit retains the same certified
rectangle bound; a nonfinite enclosure fails. The adaptive tolerances affect
only sharpness.

The square-root and cube-root choices in (1) cause no loss of coverage:
either quadratic root and any cube root give the same multiset of three
roots of $P(z)=s$. A fixed branch is enclosed on each input ball; the code
rotates its cut when convenient. No holomorphic integration assumption is
used. As a control, the program also computes a lower bound at $\beta=1/2$
using lower ends on the regular pieces, omitting the singular window, and
stopping at a lower dyadic enclosure $\pi_-\le\pi$. Nonnegativity makes
these omissions valid. The two bounds are $8.1746\le L\le8.1830$.

## 8. Uniqueness of the maximizer

Let $p$ be a monic cubic of maximal length; then $\ell(p)\ge L_0$. Translate so
that $p(z)=z^3-3u^2z+b$.

If $u=0$, Section 2 with $G_0(s)=|s|^{-2/3}$ on the circle $|s+b|=1$ gives
$\ell(p)=\Phi(|b|)$ when $|b|\le1$ and $\ell(p)=|b|^{-2/3}\Phi(1/|b|)$ when
$|b|>1$. Since $b_1=-1/3\ne0$, $\Phi$ is strictly increasing, so
$\ell(p)<L_0$ unless $|b|=1$.

If $u\ne0$, the critical points $\pm u$ are simple and the critical values
$b\mp2u^3$ are distinct. If both lie on the unit circle $\mathbf T$, Section 1
makes $p$ a rotation and translation of $q_{|u|}$, and Sections 5 to 7 give
$\ell(p)<L_0$, a contradiction. Otherwise use the deformation in the proof of
Eremenko and Hayman's Lemma 5, which applies to every extremal polynomial: for
a critical value $v\notin\mathbf T$ and an open disc $U\ni v$ missing
$\mathbf T$ and the other critical values, it gives monic polynomials
$p_\lambda=\phi_\lambda\circ p\circ\psi_\lambda^{-1}$, $|\lambda|<\epsilon$,
with $\phi_\lambda,\psi_\lambda$ homeomorphisms, the critical value $v$ moved
to $v+\lambda$, the other critical value fixed, and $\ell(p_\lambda)=\ell(p)$.
Each $p_\lambda$ again has two simple critical points.

Let $v\notin\mathbf T$ be a critical value of $p$ and $w$ the other one.
Choose a simple arc $\gamma$ from $v$ to a point $\zeta\in\mathbf T$,
$\zeta\ne w$, avoiding $w$ and meeting $\mathbf T$ only at $\zeta$. Such an
arc exists in either component of $\mathbb C\setminus\mathbf T$, with one
point removed if necessary. The set of $t\in\gamma\setminus\{\zeta\}$ for
which some maximizer has critical values $t$ and $w$ contains $v$ and is
relatively open by the deformation.

It is also relatively closed. Center each maximizer by translation, writing
it as $z^3-3u_j^2z+b_j$. If its critical values are $t_j\to t$ and $w$, then
$b_j=(t_j+w)/2$ and $|u_j|^3=|w-t_j|/4$ are bounded. A subsequence converges
to a monic cubic with critical values $t$ and $w$, and its length is maximal
by Lemma 4. The connectedness of $\gamma\setminus\{\zeta\}$ therefore gives
every $t$ on that arc. The same compactness argument at $\zeta$ gives a
maximizer with the two distinct critical values $\zeta$ and $w$.

If $w\notin\mathbf T$, repeat with an arc from $w$ to a point of
$\mathbf T\setminus\{\zeta\}$ avoiding $\zeta$. This produces a maximizer
with two distinct critical values on $\mathbf T$, which the strict family
inequality excludes.

Therefore every maximizer is $(z-z_0)^3-w$ with $|w|=1$. Conversely each such
polynomial is a rotation and translation of $z^3-1$ and has length $L_0$.
