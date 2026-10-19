---
name: research/prime_binary_new_attack/survivor_moments
title: Removing rough composites from rooted short-window moments
desc: |
  A fixed-dimensional sieve bounds rough-composite contamination of the
  rooted second moment by O(N_X) and of bounded local counts by O(N_X/K).
  The centered-moment input is therefore equivalent to its prime-rooted
  version. At the lower sieve cutoff, a positive base moment must be
  canceled by the signed transport. Neither missing estimate is proved.
created: 2026-10-17T06:11:46Z
updated: 2026-10-17T06:11:46Z
---

***

These are Plasma AI's author-recorded deductions supporting the
[[research/prime_binary_new_attack/short_span_sieve|shorter-span argument]]
for [[problems/irrationality/E0251/_index|Problem 251]]. They have no
independent verification warrant. The
[[research/prime_binary_new_attack/proof_sketch|canonical sketch]] retains
the full conditional contradiction. In particular, this note proves
neither its centered-moment input (VM) nor its truncated phase bound.

Use the parameters of (S1):

$$
K=\lceil12\log_2\log X\rceil,\qquad
\lambda=\frac65,\qquad
D_*=\lfloor\lambda K\log X\rfloor,\qquad
J=\lfloor D_*/2\rfloor,\qquad
z=X^{1/2-1/K^2}.
$$

Put $\mathcal I=(X,2X+D_*]$, $N_X=\pi(2X)-\pi(X)$,
$T_z=\{m\in\mathcal I:P^-(m)>z\}$ and
$\mathbb P_X=\mathbb P\cap\mathcal I$. For a finite odd set
$T\subseteq\mathcal I$, write

$$
V_T(x)=\#\{1\le a\le J:x+2a\in T\},\qquad
W(T)=\sum_{x\in T\cap(X,2X]}(V_T(x)-\lambda K)^2.
$$

All constants below are absolute once the displayed parameters are fixed.
The sieve argument uses a bounded number of linear factors, at most three.
It does not give a sieve estimate uniform in the growing number $K$ of
factors needed by the phase count.

## A uniform sieve for at most three linear factors

Write $F(n)=n/\varphi(n)$ for positive integers, with $F(1)=1$. Let
$1\le k\le3$, let $b_0=0,b_1,\ldots,b_{k-1}$ be distinct integers, and
put

$$
\Delta=\prod_{0\le i<j<k}(b_i-b_j),\qquad
\Psi_k(\Delta)=F(|\Delta|)^{k-1},
$$

with empty product $\Delta=1$ when $k=1$.

**Lemma M1.** Let $Y\to\infty$ and $w=Y^{1/10}$. Suppose $L=1$ or
$L$ is a prime greater than $w$. The number of positive integers $r\le Y$
for which none of

$$
r,\quad Lr+b_1,\quad\ldots,\quad Lr+b_{k-1}
$$

is divisible by a prime less than $w$ is

$$
\ll_k\Psi_k(\Delta)\frac{Y}{(\log Y)^k}.
\tag{M1}
$$

The constant is independent of $L$ and the offsets. If their residue
classes cover all classes at some prime below $w$, the count is zero.

*Proof.* For a prime $p<w$, multiplication by $L$ identifies the forbidden
residues with $0,-b_1,\ldots,-b_{k-1}$ modulo $p$. Let $\nu(p)$ be their
number. In the nonzero case $1\le\nu(p)<p$ for every such prime. On
squarefree numbers supported on these primes define

$$
a(d)=\prod_{p\mid d}\frac{\nu(p)}p,\qquad
h(d)=\prod_{p\mid d}\frac{a(p)}{1-a(p)},\qquad
G(w)=\sum_{d<w}\mu^2(d)h(d),\qquad
W_0(u)=\prod_{p<u}(1-a(p)).
$$

Divisor sums involving $a$ or $h$ below range over squarefree integers.

The Chinese remainder theorem counts $r\le Y$ for which $d$ divides
$r\prod_{1\le i<k}(Lr+b_i)$ as $Ya(d)+O(\nu(d))$, where
$\nu(d)=\prod_{p\mid d}\nu(p)$. Choose squarefree-supported weights

$$
\alpha_d=
\frac{\mu(d)}{G(w)\prod_{p\mid d}(1-a(p))}
\sum_{\substack{m<w/d\\(m,d)=1}}\mu^2(m)h(m)
\quad(d<w),
$$

and zero otherwise. Then $\alpha_1=1$ and
$|\alpha_d|\le W_0(w)^{-1}$. Squaring the divisor sum gives an upper
bound for the desired count. Its main quadratic form is

$$
\sum_{d,e<w}\alpha_d\alpha_e a([d,e])=\frac1{G(w)}.
\tag{M2}
$$

Indeed, $a([d,e])=a(d)a(e)\sum_{l\mid(d,e)}h(l)^{-1}$, so the form is
$\sum_l y_l^2/h(l)$, where $y_l=\sum_{l\mid d}a(d)\alpha_d$.
Möbius inversion of the displayed weights gives
$y_l=\mu(l)h(l)/G(w)$ for squarefree $l<w$, proving (M2). The remainder
has absolute value at most

$$
W_0(w)^{-2}
\left(\sum_{d<w}\mu^2(d)\nu(d)\right)^2
\ll_k w^2(1+\log w)^{4k-2}.
\tag{M3}
$$

Here $\nu(d)\le k^{\omega(d)}\le\tau_k(d)$, whose elementary divisor
sum is at most $w(1+\log w)^{k-1}$. Also
$W_0(w)\gg_k(\log w)^{-k}$: the finitely many primes $p\le k$ have
$1-a(p)\ge1/p$, and for $p>k$ the lower product
$\prod(1-k/p)$ differs from $\prod(1-1/p)^k$ by bounded positive
factors. Mertens' product estimate applies.

For completeness a short lower bound for $G$ suffices. Set
$u=w^{1/(4k)}$. The sum of $h(d)$ over divisors of
$\prod_{p<u}p$ is $W_0(u)^{-1}$. Relative to this finite positive sum,
the mean of $\log d$ is

$$
\sum_{p<u}a(p)\log p\le k\log u+O_k(1)
=\tfrac14\log w+O_k(1).
$$

Thus at least half its mass has $d<w$ for large $w$, and
$G(w)\ge1/(2W_0(u))$. This is an inequality for a finite Euler product,
with no independence assumption about the primes being counted. If
$p\nmid\Delta$, then $\nu(p)=k$ and
$(1-k/p)/(1-1/p)^k\le1$. At the other primes $\nu(p)\ge1$, so their
normalized factor is at most $(1-1/p)^{1-k}$. Consequently

$$
W_0(u)\le\Psi_k(\Delta)\prod_{p<u}(1-1/p)^k
\ll_k\frac{\Psi_k(\Delta)}{(\log w)^k}.
$$

The main term $Y/G(w)$ now has the bound (M1); (M3), with $w=Y^{1/10}$,
is smaller. This proves the lemma. $\square$

The required averages of the factor $\Psi_k$ have no growing loss. For
every fixed positive integer $m$,

$$
\sum_{n\le D}F(n)^m\ll_m D.
\tag{M4}
$$

To see this, expand $F(n)^m=\sum_{d\mid n}f_m(d)$, where $f_m$ is
nonnegative, multiplicative, squarefree-supported and
$f_m(p)=(1-1/p)^{-m}-1=O_m(1/p)$. The Euler product
$\sum_d f_m(d)/d$ converges. In particular, summing over signed offsets
$0<|b_i|\le D$ with distinct $b_i$ gives

$$
\sum_{b_1}\Psi_2(b_1)\ll D,\qquad
\sum_{b_1,b_2}\Psi_3(b_1b_2(b_1-b_2))\ll D^2.
\tag{M5}
$$

For the second inequality use
$F(|b_1b_2(b_1-b_2)|)^2
\le F(|b_1|)^2F(|b_2|)^2F(|b_1-b_2|)^2$ and Hölder's inequality.
Each of the three sums of sixth powers over the pairs is $O(D^2)$ by
(M4); every nonzero difference occurs at most $O(D)$ times. Restricting
the offsets to even integers preserves these upper bounds.

## Near-square-root composites have negligible local mass

Let $E=T_z\setminus\mathbb P_X$. For $j=0,1,2$ define $B_j$ as follows:
for each $m\in E$, count ordered, distinct, nonzero even offsets
$b_1,\ldots,b_j$, each of absolute value at most $D_*$, for which every
$m+b_i\in T_z$; then sum over $m$. Thus $B_0=|E|$.

**Proposition M2.** At the displayed parameters,

$$
B_j\ll\frac{N_X}{K^2}
       \left(\frac{D_*}{\log X}\right)^j
\quad(0\le j\le2).
\tag{M6}
$$

*Proof.* Since $z^3>3X$, every $m\in E$ has a unique expression
$m=\ell r$ with primes $z<\ell\le r$ and $\ell\le\sqrt{3X}$.
For fixed $\ell$ and offsets, take $Y=3X/\ell$. Uniformly in this
range $\log Y\asymp\log X$, $\ell>Y^{1/10}$ and $z>Y^{1/10}$.
Every counted $r$ and every $\ell r+b_i$ avoids all primes below
$Y^{1/10}$. Lemma M1 with $k=j+1$ bounds their number by

$$
\ll_j\Psi_{j+1}(\Delta)
          \frac{X}{\ell(\log X)^{j+1}}.
$$

Enlarging the range to $r\le Y$ only increases this bound, as does
discarding the restrictions $r\ge\ell$ and $m+b_i\in\mathcal I$.
Mertens' prime reciprocal estimate gives

$$
\sum_{z<\ell\le\sqrt{3X}}\frac1\ell
\ll\log\frac{\log\sqrt{3X}}{\log z}+\frac1{\log z}
\ll\frac1{K^2}.
$$

Apply (M5), or its empty-offset version when $j=0$, and use
$N_X\sim X/\log X$. This proves (M6). Squares $m=\ell^2$ are
included, and both ends of $\mathcal I$ are covered. $\square$

**Corollary M3.** Suppose $f_T(x)\in[0,1]$ depends only on
$T\cap[x,x+D_*]$ and on fixed parameters, with the same rule for each
$T$. Then

$$
\left|\sum_{x\in T_z\cap(X,2X]}f_{T_z}(x)
      -\sum_{x\in\mathbb P_X\cap(X,2X]}f_{\mathbb P_X}(x)\right|
\ll\frac{N_X}{K}.
\tag{M7}
$$

Also

$$
|W(T_z)-W(\mathbb P_X)|\ll N_X.
\tag{M8}
$$

*Proof.* A root can change a bounded summand only if it is composite,
or it is a prime with a composite of $E$ in its forward window. These
possibilities affect at most $B_0+B_1\ll N_X/K$ roots. This proves
(M7), even if $f$ is nonmonotone.

For (M8), write $A_0(T)=|T\cap(X,2X]|$,
$A_1(T)=\sum_{x\in T\cap(X,2X]}V_T(x)$ and
$A_2(T)=\sum_{x\in T\cap(X,2X]}V_T(x)(V_T(x)-1)$. Each pair or
ordered triple counted in the difference of these quantities contains a
composite $m$. All other sites are within distance $D_*$ of $m$.
Therefore, with $\Delta A_i=A_i(T_z)-A_i(\mathbb P_X)$,

$$
0\le\Delta A_0\le B_0,\qquad
0\le\Delta A_1\le2B_1,\qquad
0\le\Delta A_2\le3B_2.
$$

The exact expansion
$W(T)=A_2(T)+(1-2\lambda K)A_1(T)+\lambda^2K^2A_0(T)$ then yields
$|\Delta W|\ll B_2+KB_1+K^2B_0\ll N_X$. In particular the negative
coefficient is kept; no matching main terms have been inferred from
upper sieve bounds. $\square$

It follows that (VM) is equivalent, along the same scales, to

$$
\sum_{X<p\le2X}
\bigl(\pi(p+2J)-\pi(p)-\lambda K\bigr)^2=o(K^2N_X).
\tag{PVM}
$$

This prime-rooted centered estimate remains unproved. The monotone count
$\mathcal C_d$ and the overfull count $\mathcal D$ also satisfy (M7),
uniformly in their parameters. Thus composites can be removed from the
bounded upper event with error $o(N_X)$. This does not supply an upper
bound for that event on the primes.

The same argument does not remove composites from the required signed
phase statistic $E_d(T)$ of S6. Its summand has absolute value at most
$(5/4)^K$, since
$\binom vK(1/5)^{v-K}(4/5)^K\le1$ for $v\ge K$ and $|\kappa_d|\le1$.
The bound from affected roots is consequently
$O((5/4)^KN_X/K)$, whereas S16 needs a bound of order
$N_X5^{-(\lfloor5K/4\rfloor-K)}$. The former is much larger. Likewise
the cutoff count $\mathcal Q_d$ can be as large as
$\binom{\lfloor5K/4\rfloor}{K}$ per affected root. These statistics are
not covered by the bounded-observable conclusion (M7).

## The stopped base has a nonzero second moment

Let $y=X^{2/5}$ and $T_y=\{m\in\mathcal I:P^-(m)>y\}$. Put
$c=1+\log(3/2)$. The PNT product calculation and the near-square-root
remainder bound in
[[research/prime_binary_new_attack/consecutive_block_counts|U12 and U10]]
give

$$
|T_y\cap(X,2X]|=(c+o(1))N_X.
\tag{M9}
$$

Only this one-point census, not a correlation asymptotic, is used in the
following lower bound.

**Proposition M4.**

$$
\left(\frac{\lambda^2(c-1)^3}{3}+o(1)\right)K^2N_X
\le W(T_y)\ll K^2N_X.
\tag{M10}
$$

*Proof.* List the infinite sequence of $y$-rough positive integers as
$s_i$. For each fixed $C>0$, telescoping gives, uniformly for
$1\le m\le CK$,

$$
\sum_{X<s_i\le2X}(s_{i+m}-s_i)=(1+o(1))mX.
\tag{M11}
$$

Indeed the sum is the sum of the $m$ terms immediately after the final
root minus the first $m$ root terms. These lie respectively at
$2X+o(X)$ and $X+o(X)$, uniformly over that range of $m$: the rough
integers include every prime above $y$, and PNT supplies more than
$CK$ primes in each fixed relative neighborhood of these endpoints.
Letting the relative neighborhood tend to zero proves the uniform
statement. There are more than $CK$ roots by (M9).

For $1\le u\le c$, take $m=\lfloor u\lambda K\rfloor+1$. If
$V_{T_y}(s_i)\le u\lambda K$, then $s_{i+m}-s_i>2J$.
The window lies in $\mathcal I$, so the finite and infinite definitions
of this count agree. Markov's inequality and (M11) give, uniformly in $u$,

$$
\#\{X<s_i\le2X:V_{T_y}(s_i)\le u\lambda K\}
\le(u+o(1))N_X.
$$

Using (M9), the number with $V_{T_y}(s_i)>u\lambda K$ is at least
$(c-u-o(1))N_X$. Integration of this lower bound gives

$$
\begin{aligned}
W(T_y)
&\ge\int_{\lambda K}^{c\lambda K}
  2(v-\lambda K)\,
  \#\{x\in T_y\cap(X,2X]:V_{T_y}(x)>v\}\,dv\\
&\ge\left(2\lambda^2\int_1^c(u-1)(c-u)\,du+o(1)\right)K^2N_X\\
&=\left(\frac{\lambda^2(c-1)^3}{3}+o(1)\right)K^2N_X.
\end{aligned}
$$

For the upper bound apply M1 with $L=1$, $Y=3X$, and respectively
zero, one and two positive even offsets. Its sifting level $Y^{1/10}$
is below $y$. Averaging by (M5) gives
$A_0(T_y)\ll N_X$, $A_1(T_y)\ll KN_X$ and
$A_2(T_y)\ll K^2N_X$. The expansion used in M3 now proves the upper
bound. $\square$

In the exact Buchstab identity S13,

$$
W(T_z)=W(T_y)+\text{the signed deletion sum},
$$

the base is therefore of order $K^2N_X$. If (VM) holds, the deletion
sum must cancel a positive contribution of at least
$(\lambda^2\log(3/2)^3/3+o(1))K^2N_X$. Proposition M4 does not
compute the leading constant of the base and gives no matching
asymptotic for the signed sum. Bounding each correlation from above
still cannot supply this cancellation.

## Position in the whole contradiction

Rationality with any fixed odd denominator part $d$ forces the shorter
consecutive-block count to be at least $(1/24-o(1))N_X$. The same roots
belong to the bounded subset event $\mathcal C_d(\mathbb P_X)$ and to
$\mathcal C_d(T_z)$, whose difference is $O(N_X/K)$ by M3. To finish by
the two-cost split still requires both a bound for overfull roots and a
bound for compatible subsets at the other roots, on the same unbounded
scales for every fixed odd $d$. Neither has been proved, even for $d=1$.

The failed step is an arithmetic estimate, not removal of the rare
near-square-root composites. Reopening this route requires either the
prime-rooted estimate (PVM), or a sufficient direct overfull-root bound,
together with the truncated phase estimate; a direct estimate for the
bounded event could replace both. The fixed-dimensional sieve above has
only constant-factor upper bounds for the relevant prime correlations.
It supplies neither their signed cancellation nor the growing-order
phase information.
