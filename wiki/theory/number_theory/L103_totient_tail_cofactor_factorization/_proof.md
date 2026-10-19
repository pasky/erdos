---
name: theory/number_theory/L103_totient_tail_cofactor_factorization/_proof
title: Two common prefixes and the cofactor of a tail totient
desc: |
  Compare the common prefixes at the cuts H and P of one value, identify the
  tail prime tuple of every witness and the least preimage, and transfer the
  exceptional tuple count to the mass of the data and to the phase quotient.
created: 2026-10-15T04:35:23Z
updated: 2026-10-15T04:35:23Z
---

***

We prove
[[theory/number_theory/L103_totient_tail_cofactor_factorization/_index|L103]].
All manuscript results invoked below are conditional premises from the
[[../library/arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|unrefereed source]].
This proof checks their composition, not their underlying number-theoretic
proofs. Natural logarithms are used throughout.

## Notation and the two cuts

Fix $x$ and form $B=\log\log x$, $m$, $\theta=\theta(x)$, $G_m$ and the
coarse band centres $\widetilde b_i=\alpha_\theta h_i\rho^{-h_i}$,
$h_i=m-i$, as in the manuscript. For a sufficiently large cut $K$ put
$P_K=\lfloor\log\log K\rfloor$, $R_K=m-K$ and $L_K=m-P_K$. Write
$\mathcal T_K(x)$ for the tuples $(p_0,\ldots,p_{R_K},d)$ of the
manuscript's Section 3 at the cut $K$, with value map
$F(p_0,\ldots,p_{R_K},d)=d\prod_{i\le R_K}(p_i-1)$, and $E^*_K(x)$ for the
exceptional value set of its Proposition 5.3 at the cut $K$ and $t=x$. That
proposition gives

$$
|E^*_K(x)|,\ \ \#\{\tau\in\mathcal T_K(x):F(\tau)\in E^*_K(x)\}
\ \le\ \bigl(\epsilon_K+o_{x;K}(1)\bigr)\frac{xG_m}{\log x},   \tag{1}
$$

and, for every totient $v\le x$ outside $E^*_K(x)$, a unique tuple
$(p_0,\ldots,p_{R_K},d)\in\mathcal T_K(x)$ of value $v$ such that every
preimage of $v$ is $p_0\cdots p_{R_K}z$ with $\varphi(z)=d$, and

$$
\ell(v)=p_0\cdots p_{R_K}\,\ell(d).                            \tag{2}
$$

The constants $\epsilon_K$ do not depend on the phase and tend to zero.

We use two cuts: the given cut $H$, with $P=P_H$, $R=m-H$ and $L=m-P$, and
the cut $P$ itself. The cut $P$ is sufficiently large once $H$ is, and
$R_P=m-P=L$. Thus the prefix of a cut-$P$ tuple has the same length $L+1$
as the prefix of a cut-$H$ tuple followed by its retained tail primes
$Q_h=p_{m-h}$, $P\le h<H$.

Two elementary consequences of the statements are used repeatedly.

**(a) A common prefix divides exactly.** Let $v\notin E^*_K(x)$ have tuple
$(p_0,\ldots,p_{R_K},d)$, and let $n=p_0\cdots p_{R_K}z$ be a preimage
with $\varphi(z)=d$. Since
$\varphi(n)\ge\varphi(p_0\cdots p_{R_K})\varphi(z)$, with equality only for
coprime factors, and $\varphi(n)=v=d\prod_{i\le R_K}(p_i-1)$, the factors
are coprime. Hence each $p_i$ divides $n$ exactly once.

**(b) The prefix consists of the largest primes.** In the same situation,
the tuple has a basic witness with tail $w$ and $\varphi(w)=d$, and
Proposition 3.3 gives $w<p_{R_K}$, so $d<p_{R_K}$. A prime $r$ dividing $z$
satisfies $r-1\le\varphi(z)=d$, so $r\le p_{R_K}$, and $r\ne p_{R_K}$ by
(a). The prefix of a basic witness is strictly decreasing. Therefore
$p_0>p_1>\cdots>p_{R_K}$ are the $R_K+1$ largest prime factors of $n$, each
dividing $n$ exactly once.

## Witnesses of the tail totient are preimages

Let $(d,p_1,\ldots,p_R)\in\mathcal D_H(x)$ and let
$\eta=(\mathbf Q,a)\in\mathcal W_{H,\theta}(d)$ be any witness of $d$ at
the phase $\theta$; it need not be compatible with this prefix. By
Equation (2.5) at $s=\theta$,

$$
\log w(\eta)=\log a+\sum_{h=P}^{H-1}\log Q_h
\le\exp(2\alpha_\theta P\rho^{-P})
   +H\exp(1.1\alpha_\theta(H-1)\rho^{-(H-1)}).
$$

The prime $p_R$ lies in its band, so
$\log p_R\ge\exp(0.9\alpha_\theta H\rho^{-H})$. Since $1.1\rho<0.6$ by the
manuscript's bounds (3.3), we have
$1.1(H-1)\rho^{-(H-1)}<0.6H\rho^{-H}$, and for every sufficiently large
$H$, uniformly in the phase, $w(\eta)<p_R$. All primes
$p_0>\cdots>p_R$ therefore exceed every prime factor of $w(\eta)$, and for
each admissible largest prime $p_0$ the integer
$n_\eta=p_0p_1\cdots p_R\,w(\eta)$ satisfies

$$
\varphi(n_\eta)=\prod_{i=0}^R(p_i-1)\,\varphi(w(\eta))
=d\prod_{i=0}^R(p_i-1).                                       \tag{3}
$$

The primes $Q_h$ increase strictly with $h$, by the bands, and
$P^+(a)\le Q_P$. The $L+1$ largest distinct prime factors of $n_\eta$ are
therefore $p_0,\ldots,p_R,Q_{H-1},\ldots,Q_P$: there are
$(R+1)+(H-P)=L+1$ of them.

## Values outside both exceptional sets have factorized tails

Let $\tau=(p_0,\ldots,p_R,d)\in\mathcal T_H(x)$ have value
$v\notin E^*_H(x)\cup E^*_P(x)$. Let
$(p_0'',\ldots,p_L'',e)$ be the unique cut-$P$ tuple of $v$.

For every witness $\eta=(\mathbf Q,a)\in\mathcal W_{H,\theta}(d)$, the
integer $n_\eta$ is a preimage of $v$ by (3). Statement (b) at the cut $P$
says that $p_0'',\ldots,p_L''$ are the $L+1$ largest prime factors of
$n_\eta$, and the previous section identifies these as
$p_0,\ldots,p_R,Q_{H-1},\ldots,Q_P$. Hence

$$
Q_h=p''_{m-h}\qquad(P\le h<H)
$$

for **every** witness of $d$: all witnesses have the same prime tuple.
Statement (a) at the cut $P$ says that $p_L''=Q_P$ divides $n_\eta$
exactly once, so $Q_P\nmid a$. As $P^+(a)\le Q_P$ and $Q_h>Q_P$ for
$h>P$, the cofactor $a$ is coprime to $\prod_hQ_h$, and

$$
d=\varphi(w(\eta))=\varphi(a)\prod_{h=P}^{H-1}(Q_h-1).
$$

Comparing the two value identities
$v=d\prod_{i\le R}(p_i-1)=e\prod_{i\le L}(p''_i-1)$ gives
$e=d/\prod_h(Q_h-1)=\varphi(a)$ for every witness. Finally (2) at the two
cuts gives

$$
p_0\cdots p_R\,\ell(d)=\ell(v)=p_0''\cdots p_L''\,\ell(e)
=p_0\cdots p_R\prod_{h=P}^{H-1}Q_h\,\ell(e),
$$

so $\ell(d)=\ell(e)\prod_hQ_h$. Thus $d$ is factorized at the phase
$\theta(x)$.

## Counting the exceptional data

By the contrapositive, if $d$ is not factorized at phase $\theta(x)$, then
every tuple $(p_0,p_1,\ldots,p_R,d)\in\mathcal T_H(x)$ built on it has its
value in $E^*_H(x)\cup E^*_P(x)$. The tuples with value in $E^*_H(x)$ are
counted by (1) at the cut $H$. A value in $E^*_P(x)\setminus E^*_H(x)$ has
exactly one cut-$H$ tuple, so these tuples number at most $|E^*_P(x)|$,
which (1) at the cut $P$ bounds. Hence

$$
\#\{\tau\in\mathcal T_H(x):F(\tau)\in E^*_H(x)\cup E^*_P(x)\}
\le\bigl(\epsilon_H+\epsilon_P+o_{x;H}(1)\bigr)\frac{xG_m}{\log x}.
                                                               \tag{4}
$$

Now fix a datum $(d,p_1,\ldots,p_R)\in\mathcal B_H(x)$ and put
$D=d\prod_{i\le R}(p_i-1)$. By Proposition 3.3, $D\le\exp((\log x)^{0.8})$.
Every prime $p_0$ with $x^{0.9}\le p_0\le1+x/D$ completes the datum's basic
tail to a basic witness: the remaining conditions of (3.10) use the
convention $u_0=B$ and do not involve $p_0$, and $p_0>p_1$ because
$\log p_1\le(\log x)^{0.61}$. Distinct pairs of a datum and a prime $p_0$
give distinct tuples. The prime number theorem, applied as in the proof of
Proposition 6.1, gives at least

$$
\frac{x}{D\log x}\bigl(1+o_{x;H}(1)\bigr)
$$

such primes, uniformly in the data. Summing over $\mathcal B_H(x)$ and
comparing with (4),

$$
\limsup_{x\to\infty}\frac1{G_m}
\sum_{(d,p_1,\ldots,p_R)\in\mathcal B_H(x)}\frac1D
\le\epsilon_H+\epsilon_P .
$$

The bound is uniform in the phase because both $\epsilon_H$ and
$\epsilon_P$ are. This proves the first part.

## The phase quotient

Assume the premises of
[[theory/number_theory/L65_conditional_totient_ratio_coefficient/_index|L65]].
Its Equation (6) and the manuscript's Proposition 6.1 give, with
$Z(x)=xG_m/\log x$,

$$
\limsup_{x\to\infty}\left|\frac{V'(x)}{Z(x)}-\frac{M_{f_0}(x;H)}{G_m}\right|
\le\eta_H,\qquad
\limsup_{x\to\infty}\left|\frac{V(x)}{Z(x)}-\frac{M_1(x;H)}{G_m}\right|
\le\epsilon'_H,
$$

where $f_0(r)=1/r$ and $\eta_H,\epsilon'_H\to0$ do not depend on the
phase. Theorem 2.1 gives $V(x)/Z(x)=A(1;\theta(x))+o(1)$ with
$A(1;s)\ge c_->0$, and L65 gives $q(\theta(x))=V'(x)/V(x)+o(1)$. Write
$a=V'/Z$, $b=V/Z$, $a'=M_{f_0}/G_m$ and $b'=M_1/G_m$. Since $a'\le b'$,

$$
\left|\frac ab-\frac{a'}{b'}\right|
\le\frac{|a-a'|+|b-b'|}{b},
$$

so $\limsup|q(\theta(x))-M_{f_0}/M_1|\le2(\eta_H+\epsilon'_H)/c_-$. For
large $H$ also $b'\ge c_-/2$ for all large $x$.

On a factorized datum, $f_0(\ell(d)/d)=g(d)=g(e)\prod_h(1-1/Q_h)$, so

$$
0\le g(e)-g(d)\le\sum_{h=P}^{H-1}\frac1{Q_h}
\le\delta_P:=2\exp\bigl(-\exp(0.9\lambda P\rho^{-P})\bigr),
$$

by the bands $\log\log Q_h\ge0.9\alpha_\theta h\rho^{-h}$ and
$\alpha_\theta\ge\lambda$, for every sufficiently large $H$. On the
remaining data $M^*$ has no term and $f_0\le1$. Hence
$|M_{f_0}-M^*|\le M_{\mathbf 1_{\mathcal B}}+\delta_PM_1$, where
$M_{\mathbf 1_{\mathcal B}}$ is the mass of $\mathcal B_H(x)$, and the first
part gives

$$
\limsup_{x\to\infty}\left|q(\theta(x))-\frac{M^*(x;H)}{M_1(x;H)}\right|
\le c_H:=\frac{2(\eta_H+\epsilon'_H+\epsilon_H+\epsilon_P)}{c_-}
        +\delta_P .
$$

Each term tends to zero as $H\to\infty$, independently of the phase. This
proves the second part.

## What the deduction does not give

The factorized data do not form a product set: whether $d=e\prod_h(Q_h-1)$
is factorized depends on all witnesses of $d$ and, through (2), on the
global least preimage. The deduction controls the mass of the data, not the
finite coefficient's probability measure; passing to that measure needs
Lemma 6.4 and Proposition 6.5 for a weight that is not a function of
$\ell(d)/d$. It makes no comparison between two phases, and its error is
only as good as the manuscript's coverage rate at the cut $P$.
