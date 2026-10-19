---
name: theory/number_theory/L44_finite_prime_totient_phase/_proof
title: Divisibility profiles and a uniform prime truncation
desc: |
  Encode fixed prime divisibility as a least-preimage-ratio weight, count it
  using the common prefix, and transfer prime-deletion bounds to all phases
  and to the finite coefficient.
created: 2026-10-14T10:49:15Z
updated: 2026-10-14T10:49:15Z
---

***

We prove
[[theory/number_theory/L44_finite_prime_totient_phase/_index|L44]]. All
manuscript results below are explicit conditional premises from the
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|September 2026 unrefereed manuscript]].
We use the notation and conclusions of
[[theory/number_theory/L65_conditional_totient_ratio_coefficient/_index|L65]]:
$Z(x)=xG_m/\log x$, $q(s)=A(f_0;s)/A(1;s)$ and $f_0(r)=1/r$.
The measure $\mu_{H,s}$ always uses the union probability for each distinct
tail totient and the least preimage among all preimages.

## Encoding a fixed set of primes

The map from a finite set of primes $S$ to
$r(S)=\prod_{p\in S}p/(p-1)$ is injective. Indeed, cancel the primes common
to two sets with equal products and take the largest prime $p$ remaining.
After cross multiplication, $p$ divides the side containing its numerator
and cannot divide the other side: every remaining prime and every factor
of the form $q-1$ there is smaller than $p$. This is a contradiction.

For a squarefree integer $k$, define $h_k(r(S))$ to be $1$ if every prime
dividing $k$ belongs to $S$, and $0$ otherwise. Extend $h_k$ arbitrarily
with values in $[0,1]$ off these arguments. For every totient $d$,

$$
h_k(\ell(d)/d)=\mathbf 1_{k\mid\ell(d)}.                 \tag{1}
$$

This uses $d=\varphi(\ell(d))$, not the prime factors of a chosen
witness. In particular
$b_{H,k}(s)=A_H(h_k;s)/A_H(1;s)$ for all sufficiently large $H$.

## Counting the divisibility condition

Fix $k$, and choose $H$ large enough that the lower bound for every prefix
prime in the manuscript is greater than every prime dividing $k$. This
choice is possible because that lower bound tends to infinity with $H$,
uniformly in phase. Keep $H$ fixed while $x\to\infty$.

Outside the exceptional sets of Proposition 5.3, a value has a unique tuple
and

$$
v=d\prod_{i=0}^R(p_i-1),\qquad
\ell(v)=\ell(d)\prod_{i=0}^Rp_i.
$$

Thus $k\mid\ell(v)$ if and only if $k\mid\ell(d)$. For fixed remaining
data, counting $p_0$ as in Proposition 6.1 gives

$$
\limsup_{x\to\infty}
\left|\frac{C_k(x)}{Z(x)}-\frac{M_{h_k}(x;H)}{G_m}\right|
\le e_H,\qquad e_H\longrightarrow0.                       \tag{2}
$$

The count for each datum is its unweighted largest-prime count multiplied
by (1). Its weight lies in $[0,1]$, so the errors from exceptional values
and tuples are at most those in Proposition 5.3, and the prime-sum error is
controlled by $M_1\ll K_HG_m$. No independence of prime divisibility and
phase is used. The restriction on $H$ depends on $k$; once it holds, the
error bounds do not.

Apply Proposition 6.5 and Lemma 6.6 to the comparison quantity $C_k/Z$ in
(2). They give uniform convergence to $B_k(s)=A(h_k;s)$ and
$C_k(x)/Z(x)=B_k(\theta(x))+o(1)$. Since $A(1;s)$ is bounded away from
zero, division gives

$$
b_{H,k}\longrightarrow b_k:=\frac{B_k}{A(1;\cdot)}
\quad\hbox{uniformly},\qquad
\frac{C_k(x)}{V(x)}=b_k(\theta(x))+o(1).                    \tag{3}
$$

The bounds $0\le b_k\le1$ and $b_1=1$ follow directly.

By the finite-coefficient argument of
[[theory/number_theory/L43_continuous_totient_phase_ratio/_index|L43]],
$B_k$ has one-sided limits; the positive denominator gives the same for
$b_k$. The count $C_k$ changes by at most one on an interval of length one.
Since $0\le C_k\le V$,

$$
\left|\frac{C_k(x+1)}{V(x+1)}-\frac{C_k(x)}{V(x)}\right|
\le\frac2{V(x)}\longrightarrow0.                          \tag{4}
$$

Use (4) and (3) at the exact-phase arguments and their neighbors in L43's
proof. At an interior phase both one-sided limits equal the value at that
phase; at the period boundary the limit from $1$ equals the value at $0$.
This proves continuity on $\mathbb R/\mathbb Z$ without a positive lower
bound for $B_k$.

## Prime deletion, uniformly in the prime

We give the estimates used in the unrefereed, non-arXiv October note
[*An explicit bound for Erdős problem 417*](https://github.com/LeanMeanBean/417/blob/3620821345595c5e2b60de4f86561e1872c81840/417.pdf),
Equations (2)–(4), at the uniformity needed here. The note's numerical
evaluation is not used.

Fixed dilation of $V$ implies that for some absolute constant $D$,

$$
\frac{V(x/t)}{V(x)}\le Dt^{-1/2}\qquad(t\ge1, x\ge x_0). \tag{5}
$$

To see the uniformity, choose $x_0$ so that
$V(y/2)/V(y)\le2^{-1/2}$ for $y\ge x_0$. Iterate down dyadic scales
while the arguments remain above $x_0$, and use monotonicity for an
intermediate $t$. The same iteration gives $V(x)\gg\sqrt{x}$; below
$x_0$ the numerator is bounded, and when $x/t\ge1$ one has $t\le x$.
When $x/t<1$ the numerator vanishes. These cases prove (5) after increasing
$D$.

If $p^a\Vert\ell(v)$, deleting the full $p$-part leaves an integer with
totient $v/[p^{a-1}(p-1)]$. For each fixed $a$ this is an injection on
the values $v$. Therefore

$$
\frac{C_p(x)}{V(x)}
\le\sum_{a\ge1}\frac{V(x/[p^{a-1}(p-1)])}{V(x)}
\le\frac{D}{\sqrt{p-1}(1-p^{-1/2})}
\le Kp^{-1/2},                                             \tag{6}
$$

where $K$ is independent of $p$ and $x\ge x_0$. For fixed $p$, (5)
dominates the series in $a$, so fixed dilation also gives
$\limsup C_p(x)/V(x)\le p/(p-1)^2$. If $2\mid\ell(v)$, minimality
forces $4\mid\ell(v)$, since an integer with exactly one factor of $2$
has the same totient after that factor is removed. Consequently $v/2$ is
a totient and $C_2(x)\le V(x/2)$. Taking the exact-phase sequences in
(3) proves the bounds for $b_p$ and $b_2$ on the card.

## Truncating the single weighted expectation

For a totient $v$ put $g(v)=v/\ell(v)$ and
$w_Y(v)=\prod_{p\le Y,\ p\mid\ell(v)}(1-1/p)$. Elementary finite-product
inequalities give

$$
0\le w_Y(v)-g(v)
\le\sum_{p>Y,\ p\mid\ell(v)}\frac1p.
$$

Summing and applying (6) proves

$$
0\le\frac1{V(x)}\sum_{v\le x,\ v\in\mathcal V}
          (w_Y(v)-g(v))
\le K\sum_{p>Y}p^{-3/2}\le\frac{2K}{\sqrt Y}.               \tag{7}
$$

The last bound compares the sum over primes with
$\sum_{n=Y+1}^\infty n^{-3/2}\le\int_Y^\infty t^{-3/2}\,dt$.

We also need the comparison

$$
\frac1{V(x)}\sum_{v\le x,\ v\in\mathcal V}g(v)
=\frac{V'(x)}{V(x)}+o(1)=q(\theta(x))+o(1).                 \tag{8}
$$

This is Equation (1) of the October note. It follows directly from the
same premises as L65: on a good tuple,
$g(v)=f_0(\ell(d)/d)\prod_{i=0}^R(1-1/p_i)$, and the prefix product
is $1+o_H(1)+o_{x;H}(1)$ uniformly by the prime-band bounds. Counting the
largest prime over its full range therefore gives
$(x/\log x)M_{f_0}$ for the sum in (8), with normalized error tending to
zero as $H\to\infty$. The discarded values and tuples have weights at
most one. L65's asymptotic for $V'$ has the same limiting coefficient,
which proves (8). This argument retains the full minimum in $\ell(v)$.

Expand the finite product $w_Y$ and use (3):

$$
\frac1{V(x)}\sum_{v\le x,\ v\in\mathcal V}w_Y(v)
=\sum_{k\mid P_Y}\frac{\operatorname{mobius}(k)}k
                   \frac{C_k(x)}{V(x)}
=Q_Y(\theta(x))+o_Y(1).                                  \tag{9}
$$

Keep $Y$ fixed and take an exact-phase sequence in (7)–(9). The bound in
(7) is independent of phase and of $Y$, so

$$
0\le Q_Y(s)-q(s)\le K\sum_{p>Y}p^{-3/2}\quad(0\le s<1).    \tag{10}
$$

There is no exchange of the limits in $x$ and $Y$. In particular $Q_Y\to q$
uniformly. This initial bound can now be sharpened to one with an explicit
constant. For fixed integers $Z>Y\ge2$, the product inequality gives
$w_Y-w_Z\le\sum_{Y<p\le Z,\ p\mid\ell(v)}1/p$. Take an exact-phase
sequence and use (3), (9) and the bound for $b_p$ to obtain

$$
0\le Q_Y(s)-Q_Z(s)
\le\sum_{Y<p\le Z}\frac{b_p(s)}p
\le\sum_{Y<p\le Z}\frac1{(p-1)^2}.
$$

Let $Z\to\infty$ using (10). This proves the stronger bound

$$
0\le Q_Y(s)-q(s)\le T_Y:=\sum_{p>Y}\frac1{(p-1)^2}
\le\sum_{n=Y}^\infty\frac1{n^2}
\le\frac1{Y-1}.                                           \tag{11}
$$

For fixed $Y$, the finite product expansion also gives

$$
\sum_d\mu_{H,s}(d)w_Y(d)
=\sum_{k\mid P_Y}\frac{\operatorname{mobius}(k)}k b_{H,k}(s)
\longrightarrow Q_Y(s)
$$

uniformly in $s$. Subtract L65's uniformly convergent $q_H$ and use (11)
to obtain the claimed finite-coefficient truncation bound. Here $Y$ is
fixed before $H\to\infty$; no error uniform over arbitrary $Y=Y(H)$ is
claimed.

Finally (11) implies uniform convergence $Q_Y\to q$ as $Y\to\infty$.
The oscillation of two continuous functions on the circle differs by at
most twice their uniform distance. Thus
$\operatorname{osc} Q_Y\to\operatorname{osc} q$, which is zero precisely
when $q$ is constant. L65 makes this equivalent to the existence of the
limit in Problem 417. No constancy of any $b_k$ or $Q_Y$ has been assumed
or proved.
