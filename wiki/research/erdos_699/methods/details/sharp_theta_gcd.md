---
name: research/erdos_699/methods/details/sharp_theta_gcd
title: "Erdős 699: sharper uniform prime bounds for numerical Padé sources"
desc: "Broadbent's square-root bound through 10^19 and global theta tables remove the old Dusart error floor; verified finite-RH estimates are patched to unconditional tails."
created: 2026-09-22T16:55:37Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: sharper uniform prime bounds for numerical Padé sources

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Unequal Padé blocks]]

***

The numerical coefficient-gcd certificates improve substantially when their
prime intervals use sharper estimates for $\theta(x)$. These estimates do
not change the Padé construction or its target cofactor inequalities.
They reduce the computed starting index at which those inequalities apply.

The [uniform helper](../../computations/erdos_699_off_diagonal_gcd_sharp.py)
returns rational bounds for every $m\ge m_0$. Its public
`gcd_exponent_lower(A,B,C,terms=...,m0=...)` interface matches the existing
off-diagonal helper. `theta_errors(numerator,denominator)` supplies uniform
relative errors for every real $x$ above a rational starting point;
`theta_pointwise` supplies rational bounds at that point for finite
bootstrap calculations.

## A square-root bound through $10^{19}$

Broadbent et al., Corollary 9.1
with $c=C=.94$ and $c_0=1.03883$ gives

$$\theta(x)\ge x-1.94x^{1/2}-1.03883x^{1/3}
                    -.94x^{1/4}-1.03883x^{1/5}
\qquad(10^4\le x\le10^{19}).$$

For $x\ge10^{11}$,

$$
x^{1/6}>64,\qquad x^{1/4}>512,\qquad x^{3/10}>1024,
$$

and therefore

$$1.94+\frac{1.03883}{64}+\frac{.94}{512}
       +\frac{1.03883}{1024}
 =\frac{200610011}{102400000}<1.96.$$

Hence

$$\boxed{\theta(x)>x-1.96\sqrt x
       \qquad(10^{11}\le x\le10^{19}).}$$

Together with the previously retained BFT bound below $10^{11}$, this
extends $\theta(x)>x-2.072\sqrt x$ through $10^{19}$. This extension is
particularly useful in the interval between the finite prime lookup and
the eventual global analytic bound.

Broadbent et al., Corollary 2.1 also gives

$$
\theta(x)\le(1+1.93378\cdot10^{-8})x\qquad(x\ge0),
$$

and quotes $\theta(x)<x$ through $10^{19}$. The latter is used for
pointwise bootstrap bounds; the former is a uniform upper bound for an
unbounded tail.

## Global errors and the finite-RH range

Broadbent et al., Table 14 bounds both sides of $\theta(x)-x$ for
**all** $x>e^b$. The implementation includes its rows
$b=20,25,30,35,40,45,50,60,70,80,90,100,200$.
Every displayed error is increased by at least one final displayed unit:
the paper explicitly states that the printed tables round their last digit.
The thresholds $\lceil e^b\rceil$ are certified with directed intervals.
For example, the rounded lower errors are

$$\begin{array}{c|cccccc}
b&25&30&35&40&45&50\\\hline
\delta_-(b)&7.4367\,10^{-6}&6.0752\,10^{-7}&4.9767\,10^{-8}
&2.1483\,10^{-8}&1.1085\,10^{-8}&1.1345\,10^{-9}.
\end{array}$$

[Johnston–Yang, Lemma 2.2](../../../../../library/primes/johnston_yang_2022_some_explicit_estimates_error_term_prime_number_theorem/_index.md)
provides

$$|\theta(x)-x|<\frac{\sqrt x\log^2x}{8\pi}
       \qquad(599<x\le2.169\cdot10^{25}).$$

This is a proved finite-range bound, obtained from the verified Riemann
height; the helper does not assume the Riemann hypothesis outside that
range. Since $\log^2x/\sqrt x$ decreases for $x>e^4$, its value at $x_0$
bounds the relative error up to the end of the verified range. Above that
end, the global $b=50$ table row applies. Thus the maximum of these two
errors is valid for **every** $x\ge x_0$. The square-root bound is patched
at $10^{19}$ in the same way, using the global $b=40$ row.

The helper takes the minimum of all available valid envelopes. Square
roots are bounded by integer square roots; logarithms use a directed
16-bin binary-mantissa table. Every subsequent calculation is rational.

## The coefficient-gcd sum

Keep the intervals from the existing off-diagonal numerical argument:

$$U_t(m)=\frac{Hm-1}{t},\qquad
V_t(m)=m\max\left\{
\frac{A+1/m_0}{k_A+1},\frac B{k_B+1},\frac{C+1/m_0}{k_C+1}
\right\},$$

where $H=A+B+C$ and $k_X=\lfloor Xt/H\rfloor$. Only eligible $t$ with
$k_A+k_B+k_C=t-2$ are used. The exact floor-stability check is unchanged.
If $\epsilon_U,\epsilon_V$ are the new uniform errors above
$U_t(m_0),V_t(m_0)$, respectively, then each interval contributes at least

$$m\left[(1-\epsilon_U)\frac{U_t(m_0)}{m_0}
 -(1+\epsilon_V)\frac{V_t(m_0)}{m_0}\right]$$

to the logarithm of either coefficient gcd. Negative contributions are
replaced by zero and the others are rounded down before summing. This
proves the returned lower rate for every $m\ge m_0$.

The [sample certificates](../../computations/erdos_699_off_diagonal_gcd_sharp.json)
include directions $(17,11,26)$ with target $\ell=4.25708955$:
$m_0=10^{12}$ and 10,000 terms give a strict rate margin exceeding
$.0022149$, while the previous logarithmic Dusart helper at the same
starting index misses the target by more than $.0033907$.

The same sample record certifies the three strengthened initial
$2,7$, $3,7$, and $5,7$ sources with 100,000 terms and $m_0=10^{14}$;
their previous retained uniform starts were $10^{40}$. These are analytic
starting indices. Separate finite bootstraps may reduce them further.
