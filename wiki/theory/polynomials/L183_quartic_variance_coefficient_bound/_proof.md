---
name: theory/polynomials/L183_quartic_variance_coefficient_bound/_proof
title: Laurent modes and the residual Cauchy--Schwarz inequality
desc: |
  The exterior inverse identifies arclength with a Hardy norm. Polynomial
  division fixes five modes of the variation, and orthogonality to the
  constant observable bounds the remaining modes. Their nonproportionality
  gives strict loss at a unicritical polynomial.
created: 2026-10-15T23:06:58Z
updated: 2026-10-15T23:06:58Z
---

***

Use the notation of the
[[theory/polynomials/L183_quartic_variance_coefficient_bound/_index|claim]].
The inner product below is linear in its first argument and uses the
measure $d\theta/(2\pi)$ on the unit circle.

## The exterior inverse and its boundary norm

There is a univalent exterior inverse $\Psi$, normalized by
$\Psi(w)=w+O(w^{-1})$, such that

$$
p(\Psi(w))=w^4,\qquad |w|>1. \tag{1}
$$

One can construct it directly by continuing the root asymptotic to $w$
near infinity. All finite critical values have modulus one, so no roots
collide for $|w|>1$. A circuit in the $w$-plane winds the target $w^4$
four times around all finite critical values; the root monodromy around
them is the four-cycle seen at infinity, so this continuation is
single-valued. The four roots are $\Psi(w),\Psi(iw),\Psi(-w),\Psi(-iw)$.
They are distinct and account for every inverse root. This also proves
univalence: two arguments with the same image must differ by a fourth
root of unity, and the four listed roots never coincide.

The nonvanishing derivative has winding number zero around infinity.
Consequently it has an analytic square root

$$
g(w)=\sqrt{\Psi'(w)}=1+\sum_{k\ge2}g_k w^{-k},\qquad |w|>1. \tag{2}
$$

At a critical point of multiplicity $r$ in $p'$, the derivative of an
inverse branch has singular order $r/(r+1)\le3/4$. Its modulus is
integrable. The finitely many such boundary expansions show that $g$ has
square-integrable boundary values and that the radial boundary norms
converge. The boundary parameterization by $\Psi$ counts each regular
arc of $|p|=1$ once: $w\mapsto w^4$ runs through the four inverse sheets.
Thus Parseval's identity gives

$$
S=\frac{\ell(p)}{2\pi}=\|g\|^2=1+\sum_{k\ge2}|g_k|^2. \tag{3}
$$

If $S=1$, every $g_k$ vanishes, so $\Psi'=1$ and its normalization gives
$\Psi(w)=w$. Then $p=z^4$, whose critical value is zero, contrary to the
hypothesis. Hence $S>1$.

## The modes fixed by polynomial division

Solving (1) at infinity and taking the square root gives

$$
g_2=\frac a8,\qquad g_3=\frac b4,\qquad
g_4=\frac{3c}{8}-\frac{7a^2}{128},\qquad
g_5=-\frac{ab}{32}. \tag{4}
$$

For example, the inverse begins
$\Psi=w-a/(4w)-b/(4w^2)+(a^2/32-c/4)w^{-3}+0w^{-4}+O(w^{-5})$,
which verifies all four coefficients in (4).

Let $V$ be the polynomial quotient of $p^2$ by $p'$, so $V'=Q$, and put
$R=p^2-p'V$, of degree at most two. Differentiating (1) yields
$p'(\Psi)\Psi'=4w^3$, whence

$$
V(\Psi(w))=\frac{w^5\Psi'(w)}4-U(w),\qquad
U(w)=\frac{R(\Psi(w))}{p'(\Psi(w))}=O(w^{-1}).
$$

For $f(w)=Q(\Psi(w))g(w)$, differentiation gives

$$
f(w)=\frac54w^4g(w)+\frac12w^5g'(w)-\frac{U'(w)}{g(w)}. \tag{5}
$$

The last term starts at $w^{-2}$. The coefficients of $w^4,w^3,w^2,w,1,w^{-1}$
in $f$ are therefore, respectively,

$$
\frac54,\quad0,\quad\frac a{32},\quad-\frac b{16},\quad
A=\frac{21a^2}{512}-\frac{9c}{32},\quad\frac{5ab}{128}. \tag{6}
$$

Since $Q$ stays bounded on the compact lemniscate, $f$ has
square-integrable boundary values as well. With arclength transferred by
$\Psi$, the moment identities are

$$
\langle f,g\rangle=Sm,\qquad
\|f-mg\|^2=S\operatorname{Var}_\mu(Q). \tag{7}
$$

## The projection bound

Set $h=f-mg$. It is orthogonal to $g$. Because $g$ has no positive modes
and no $w^{-1}$ mode, (6) fixes the squared norm in the four modes
$w^4,w^2,w,w^{-1}$ of $h$ to be

$$
D=\frac{25}{16}+\frac{|a|^2}{1024}+\frac{|b|^2}{256}
                       +\frac{25|ab|^2}{16384}. \tag{8}
$$

Its constant coefficient is $h_0=A-m$. Write $h_{-k}$ for its coefficient
of $w^{-k}$. Orthogonality to $g$, with $g_0=1$ and $g_1=0$, says

$$
h_0+\sum_{k\ge2}h_{-k}\overline{g_k}=0.
$$

By Cauchy--Schwarz and (3),

$$
\sum_{k\ge2}|h_{-k}|^2\ge\frac{|h_0|^2}{S-1}.
$$

Adding these disjoint modes and using (7) gives

$$
S\operatorname{Var}_\mu(Q)
 \ge D+|A-m|^2+\frac{|A-m|^2}{S-1}
 =D+\frac{S|A-m|^2}{S-1},
$$

which is the asserted inequality.

## Strict loss at the unicritical limit

For $p=z^4+c$ with $|c|=1$, one has

$$
\Psi(w)=(w^4-c)^{1/4},\quad
g(w)=(1-cw^{-4})^{-3/8},\quad
Q(\Psi(w))=\frac54w^4-\frac34c. \tag{9}
$$

The pushforward of normalized arclength by $p$ has density proportional
to $|\zeta-c|^{-3/4}$ on the unit circle. Writing $\zeta=ce^{i\theta}$,
the beta-integral recurrence gives
$\mathbb E\sin^2(\theta/2)=1/5$, hence
$\mathbb E\zeta=3c/5$. It follows that $m=0$ and
$\operatorname{Var}(Q)=(25/16)(1-9/25)=1$.

The Cauchy--Schwarz step above is strict here. In fact
$g_{4j}=(3/8)_j c^j/j!$ and all other nonconstant modes vanish.
For $j\ge1$, (9) gives

$$
\frac{f_{-4j}}{g_{4j}}
 =c\left(\frac54\frac{j+3/8}{j+1}-\frac34\right)
 =c\,\frac{j/2-9/32}{j+1}. \tag{10}
$$

These ratios differ already at $j=1,2$, and both corresponding
$g_{4j}$ are nonzero. The two tail vectors are not proportional, so
equality in Cauchy--Schwarz is impossible. The stated lower bound is
therefore strictly less than one at (9). Its exact value there is

$$
\frac{25}{16S_0}+\frac{81}{1024(S_0-1)},\qquad
S_0=\frac{\ell(z^4-1)}{2\pi}.
$$

This strict loss concerns the finite projection used in the proof, not
the unproved variance inequality for regular quartics.
