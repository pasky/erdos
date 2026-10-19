---
name: theory/integer_sequences/L253_exponent_pair_smooth_blocks/_proof
title: Proof of the exponent-pair smooth-block bound
desc: |
  Match the reciprocal square-root phase to Bourgain's exponent pair,
  use Vaaler's inequality to bound the multiplier discrepancy, and show
  that its error is uniformly smaller than the pair-count main term for
  m <= K^(97/38-delta).
tags: []
sources:
- theory/integer_sequences/L253_exponent_pair_smooth_blocks/_index
created: 2026-10-15T22:54:40Z
updated: 2026-10-15T22:54:40Z
---

***

This proves the whole statement of
[[theory/integer_sequences/L253_exponent_pair_smooth_blocks/_index|L253]].
Write $e(u)=\exp(2\pi iu)$,
$\psi(u)=u-\lfloor u\rfloor-\frac12$, and

$$
S_C(X)=\sum_{C<c\le2C}\psi\bigl(\sqrt{X/c}\bigr),\qquad
Y_X=\sqrt{X/C}.
$$

All implied constants below are uniform in $m,K,C,X,r$. They may depend
on the fixed positive parameter $\eta$, and eventually on $\delta$.

## The analytic input and its specialization

Theorem 6 of Bourgain, *Decoupling, exponential sums and the Riemann zeta
function*, J. Amer. Math. Soc. 30 (2017), 205--224, in
[arXiv:1408.5794v2](https://arxiv.org/abs/1408.5794v2), Section 5,
states that

$$
(\kappa,\lambda)=(13/84+\eta,55/84+\eta)
$$

is an exponent pair for every fixed $0<\eta<1/100$.
In the normalization used there,
an admissible phase of size $T$ on an interval of length comparable to
$M$, with $T\ge M$, has exponential sum
$\ll_\eta (T/M)^\kappa M^\lambda$.
The phase class consists of functions whose derivatives approximate those
of a monomial with first derivative $yu^{-s}$, $s>0$; the constants are
uniform for fixed $s$ and fixed derivative tolerances. Section 5 explains
both the extension to $M>\sqrt T$ and the allowance of subintervals. These
qualifications matter here, since the first few frequencies can have
$C>\sqrt{rY_X}$.

For $X>0$ and $r\ge1$, take

$$
f(u)=-r\sqrt X\,u^{-1/2}\quad(C\le u\le2C).
$$

Its first derivative is exactly
$f'(u)=(r\sqrt X/2)u^{-3/2}$: this is the source's monomial with
$s=3/2$, with zero approximation error at every derivative order.
Equivalently, its normalized phase is $-v^{-1/2}$ on $1\le v\le2$,
independent of $r,X,C$, and its size is $T=rY_X$.
The positive-phase sum is the conjugate of the sum for $f$, so the same
bound applies. Thus, whenever $rY_X\ge2C$,

$$
T_r(X):=\sum_{C<c\le2C}e\bigl(r\sqrt{X/c}\bigr),\qquad
|T_r(X)|\ll_\eta (rY_X/C)^\kappa C^\lambda
=C^{1/2}(rY_X)^\kappa .
\tag{1}
$$

The equality uses $\lambda-\kappa=1/2$. The fixed change from the source's
interval $[M/2,M]$ to $[C,2C]$ changes only constants. No almost-all
qualification occurs in this estimate.

## Discrepancy estimate

Assume $Y_X\ge2C$ and $C^{1/2}Y_X^{-\kappa}\ge1$. Put

$$
V=(C^{1/2}Y_X^{-\kappa})^{1/(1+\kappa)},\qquad
R=\lceil V\rceil,
$$

so $V\le R\le2V$. Equation (1) of
[[theory/integer_sequences/L251_averaged_near_square_smooth_blocks/_proof|the proof of L251, derived from Vaaler's inequality for this exact convention of psi]],
gives

$$
|S_C(X)|\le\frac{C}{2R+2}
+\Bigl(1+\frac1\pi\Bigr)\sum_{r=1}^R\frac{|T_r(X)|}{r}.
$$

Since $Y_X\ge2C$, (1) applies to every positive frequency, and
$\sum_{r=1}^Rr^{\kappa-1}\ll_\eta R^\kappa$. Consequently

$$
|S_C(X)|\ll_\eta \frac CR+C^{1/2}Y_X^\kappa R^\kappa
\ll_\eta C^aY_X^b,
\qquad
a=\frac{\kappa+1/2}{1+\kappa},\quad
b=\frac{\kappa}{1+\kappa}.
\tag{2}
$$

Both terms have exactly these exponents after substituting $V$.
In particular

$$
1+a=\frac{3/2+2\kappa}{1+\kappa},\qquad
1-b=\frac1{1+\kappa}.
\tag{3}
$$

## Uniform construction

Fix $0<\delta<1/20$, set $\eta=\delta/10$ and
$\nu=21/38-\delta$. Then
$1/2<\nu<21/38$ and $0<\kappa<1/4$. All inequalities that follow hold
for every $K$ beyond a single threshold depending only on $\delta$.

Let $K\ge64$ and $0\le m\le K^{2+\nu}$ be integers. If
$m\le K^{5/2}/128$, apply
[[theory/integer_sequences/L250_explicit_near_square_smooth_blocks/_index|L250's explicit construction]].
Otherwise put

$$
C=\left\lceil\frac{16m}{K^2}\right\rceil,\qquad
E=\left\lfloor\frac{K^2}{128C}\right\rfloor .
$$

The following bounds are uniform throughout the remaining range:

$$
\frac{\sqrt K}{8}<C\le32K^\nu=o(K),\qquad
\frac{K^2}{256C}\le E\le\frac{K^2}{128C}\le m,
\tag{4}
$$

and, for $X=m$ and $X=m+E$,

$$
\frac{K}{4\sqrt2}<Y_X\le\frac{K}{2\sqrt2}.
\tag{5}
$$

Indeed $16m/K^2>\sqrt K/8\ge1$, so $C\le32m/K^2\le32K^\nu$,
while $C\ge16m/K^2$ bounds $Y_m$ above by $K/4$ and
$C<16m/K^2+1\le32m/K^2$ bounds it below by $K/(4\sqrt2)$.
For large $K$, $C\le K^2/256$, giving the lower bound for $E$ after
rounding down. Also $C>\sqrt K/8$ gives $E<K^{3/2}/16\le m$ for
$K\ge64$. This proves (4), and $m+E\le2m$ proves (5).

In particular, $Y_X\ge2C$ for all sufficiently large $K$, because
$\nu<1$. Furthermore

$$
C^{1/2}Y_X^{-\kappa}
>\frac{K^{1/4-\kappa}}{\sqrt8}\longrightarrow\infty .
$$

Thus (2) applies to both endpoints, giving

$$
|S_C(m)|+|S_C(m+E)|\ll_\delta C^aK^b.
\tag{6}
$$

By Lemma 2 of the proof of L251, the number of pairs of positive integers
$(c,q)$ with $C<c\le2C$ and $m<cq^2\le m+E$ is

$$
\sum_{C<c\le2C}
\left(\sqrt{(m+E)/c}-\sqrt{m/c}\right)-S_C(m+E)+S_C(m).
$$

The elementary estimate (3) in that proof uses only (4), (5) and
$Y_m\le K/4$, and gives the lower bound $K/(219C)$ for this sum's
main term. To compare (6) with it, (3) and $C\le32K^\nu$ yield

$$
\frac{C^aK^b}{K/C}
\ll_\delta
K^{\{\nu(3/2+2\kappa)-1\}/(1+\kappa)}.
\tag{7}
$$

Here the exponent is strictly negative. More precisely,

$$
\nu(3/2+2\kappa)-1
=\left(\frac{21}{38}-\delta\right)
\left(\frac{38}{21}+\frac\delta5\right)-1
=\delta\left(\frac{21}{190}-\frac{38}{21}\right)
-\frac{\delta^2}{5}< -\delta .
$$

It follows that the pair count is positive for every sufficiently large
$K$, uniformly for all the integers $m$ in the specified range. Choose
such a pair and let $t$ be the largest nonnegative integer satisfying
$ct^2<cq^2-m$. The adjustment lemma in L251 gives

$$
0<N-m<2\sqrt{cE}+c\le K/4+2C\le K,
\qquad N=c(q-t)(q+t).
$$

Also $1\le c\le2C\le K$, $q-t\ge1$, and

$$
q\le\sqrt{(m+E)/c}\le\frac{K}{2\sqrt2},\qquad
t<\sqrt{E/c}\le\frac{K}{8\sqrt2 C}.
$$

Since $C\ge1$, these two bounds give $q+t<K$. All three factors are
positive integers at most $K$. This proves the first sentence after
choosing an integer $K_0(\delta)$ large enough for the finitely many
uniform threshold requirements above. Since $2+\nu=97/38-\delta$, its
exponent is exactly the one stated.

## Translation to k(n)

Fix $\varepsilon>0$. Choose $0<\delta<1/20$ so small that
$1/(97/38-\delta)<38/97+\varepsilon$, and write $d=97/38-\delta$.
For every integer $n\ge1$, set

$$
K=\max\bigl(K_0(\delta),\lceil n^{1/d}\rceil\bigr).
$$

Then $n\le K^d$, and the first sentence supplies a $K$-smooth member of
every block $(m,m+K]$ with $0\le m\le n$. If a longer block witnessed
$k(n)\ge K$, its first $K$ terms would have no such member. Hence

$$
k(n)\le K-1<\max\bigl(K_0(\delta),n^{1/d}\bigr)
\le K_0(\delta)n^{38/97+\varepsilon}.
$$

This gives the stated bound with $A_\varepsilon=K_0(\delta)$.
Every construction included $m=0$, so requiring $m$ to be positive
preserves all conclusions. $\square$
