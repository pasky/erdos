---
name: research/erdos_940/cubic_major_arcs
title: Summable rational resonances for the special cubic
desc: Growing major arcs have bounded cubic collision energy; truncated restriction still leaves the moderate-amplitude heavy-fiber correlation uncontrolled.
tags: []
sources: []
created: 2026-09-22T18:12:28Z
updated: 2026-10-14T00:26:52Z
---


# Summable rational resonances for the special cubic

***

## Status

The results below are proved. They retain and estimate the rational
resonances that obstruct the uniform contraction proposed in the
[carry-spectrum note](cubic_carry_spectrum.md). They do not bound the full
collision energy or establish positive density. In particular, the
minor-arc correlation with high-multiplicity outputs remains uncontrolled.

Put $e(t)=\exp(2\pi it)$ and

$$
S_N(\alpha)=\sum_{1\le x\le N}e(\alpha x^3),\qquad
W_N(\alpha)=S_N(\alpha)S_N(2\alpha)S_N(4\alpha).
$$

For $F(x,y,z)=x^3+2y^3+4z^3$, Parseval identifies
$\int_0^1|W_N(\alpha)|^2\,d\alpha$ with the box collision count.
Define

$$
S(q,b)=\sum_{x\bmod q}e(bx^3/q),\qquad
A(q)=q^{-6}\sum_{\substack{a\bmod q\\(a,q)=1}}
 |S(q,a)S(q,2a)S(q,4a)|^2,
$$

with $A(1)=1$.

**Theorem.** The positive series $\mathfrak S=\sum_{q\ge1}A(q)$ converges,
and

$$
\sum_{q>Q}A(q)\sim c\,Q^{-2/3}\quad(Q\longrightarrow\infty),\qquad c>0.
                                                               \tag{1}
$$

For integers $N\ge2$ and $1\le Q\le N^{1/2}$, let

$$
\mathfrak M(N,Q)=
\bigcup_{\substack{1\le q\le Q\\(a,q)=1}}
\left\{\alpha\in\mathbb R/\mathbb Z:
 \left|\alpha-\frac aq\right|\le\frac{Q}{qN^3}\right\}.
$$

Put

$$
I_j(t)=\int_0^1e(jtu^3)\,du,\qquad
\mathfrak J=\int_{\mathbb R}|I_1(t)I_2(t)I_4(t)|^2\,dt.
$$

Then $0<\mathfrak J<\infty$, and

$$
\int_{\mathfrak M(N,Q)}|W_N(\alpha)|^2\,d\alpha
=N^3\mathfrak J\mathfrak S+
 O\left(N^3Q^{-2/3}+N^2Q^2\right).                     \tag{2}
$$

For example, $Q=N^{3/8}$ gives an error $O(N^{11/4})$.

## Exact prime-power weights

CRT shows that $A$ is multiplicative. The unit frequency is reparametrized
by units when a complete sum splits over coprime moduli, compatibly for
the three coefficients.

At $2$, the proved exact uniformity of $F$ modulo every $2^k$ gives

$$
S(2^k,a)S(2^k,2a)S(2^k,4a)=0\quad(a\text{ odd}),
\qquad A(2^k)=0\quad(k\ge1).                            \tag{3}
$$

This uses uniformity of the three-variable form, not the false assertion
that cubing permutes every residue modulo $2^k$.

For $p\ge5$ and $p\nmid b$,

$$
S(p^2,b)=p,\qquad
S(p^m,b)=p^2S(p^{m-3},b)\quad(m\ge3).                  \tag{4}
$$

To prove this, write $x=y+p^{m-1}z$ and first sum over $z\bmod p$.
The sum vanishes unless $p\mid y$. For $m\ge3$, substitute $y=pu$;
the remaining summand has one redundant period. The case $m=2$ is
immediate from the same calculation. Consequently

$$
A(p^2)=(1-p^{-1})p^{-4},\quad
A(p^3)=(1-p^{-1})p^{-3},\quad
A(p^{k+3})=p^{-3}A(p^k)\quad(k\ge1).                  \tag{5}
$$

The last recurrence must not be applied at $k=0$.

At modulus $p$, the cubic-character expansion and the ordinary Gauss-sum
identity give $|S(p,b)|\le2\sqrt p$ for $p\equiv1\pmod3$. If
$p\equiv2\pmod3$, cubing is a permutation and the sum vanishes. Thus

$$
0\le A(p)\le64p^{-2}.                                 \tag{6}
$$


For the exceptional odd prime,

$$
S(3,b)=0,\qquad S(9,b)=3\bigl(1+2\cos(2\pi b/9)\bigr)
\quad(3\nmid b).
$$

The numbers $2\cos(2\pi j/9)$, $j=1,2,4$, are the roots of
$z^3-3z+1$. Their translates by one have product $-3$.
Every unit modulo $9$ permutes the classes $\{\pm1,\pm2,\pm4\}$, so

$$
S(9,a)S(9,2a)S(9,4a)=-81,\qquad A(9)=2/27.            \tag{7}
$$

Also

$$
S(3^m,b)=9S(3^{m-3},b)\quad(m\ge3,\ 3\nmid b).         \tag{8}
$$

Indeed, write $x=y+3^{m-2}z$ with $z\bmod9$. Modulo $3^m$,
$x^3\equiv y^3+3^{m-1}y^2z$. The $z$-sum is zero unless
$3\mid y$, in which case it equals nine. Substitute $y=3u$.
Thus

$$
A(3)=0,\quad A(27)=2/81,\quad
A(3^{k+3})=3^{-3}A(3^k)\quad(k\ge1).
$$

In particular the exact local factor is

$$
\sum_{k\ge0}A(3^k)
=1+\frac{2/27+2/81}{1-1/27}=\frac{43}{39}.             \tag{9}
$$


## The sharp resonance tail

For every odd prime the preceding formulas give the formal identity

$$
\sum_{k\ge0}A(p^k)t^k
=\frac{1+A(p)t+A(p^2)t^2-p^{-4}t^3}{1-p^{-3}t^3}.
                                                               \tag{10}
$$

Let $B$ be the nonnegative multiplicative function supported on odd
cube-free integers, with $B(p)=A(p)$ and $B(p^2)=A(p^2)$.
Dropping the negative numerator term coefficientwise gives

$$
A(q)\le\sum_{dm^3=q}B(d)m^{-3},                         \tag{11}
$$

where the sum may include even $m$ without harming the upper bound.
Equations (5)–(7) imply

$$
\sum_dB(d)d^{2/3}
=\prod_{p\text{ odd}}\left(1+A(p)p^{2/3}
                           +A(p^2)p^{4/3}\right)<\infty. \tag{12}
$$

Since $\sum_{m>T}m^{-3}\ll T^{-2}$ uniformly for $T>0$,

$$
\sum_{q>Q}A(q)
\le\sum_dB(d)\sum_{m>(Q/d)^{1/3}}m^{-3}
\ll Q^{-2/3}\sum_dB(d)d^{2/3}.                         \tag{13}
$$


For the matching lower bound, every odd $m$ satisfies exactly

$$
A(m^3)=\frac{\varphi(m)}{m^4}.                         \tag{14}
$$

The identity $\varphi(m)/m=\sum_{d\mid m}\mu(d)/d$ yields

$$
\sum_{\substack{m\le X\\m\text{ odd}}}\frac{\varphi(m)}m
=\frac4{\pi^2}X+O(\log(2X)).
$$

Partial summation gives

$$
\sum_{\substack{m>L\\m\text{ odd}}}\frac{\varphi(m)}{m^4}
\sim\frac2{\pi^2}L^{-2}.
$$

Retaining only $q=m^3>Q$ gives the matching lower bound in order of
magnitude. The upper bound also implies

$$
\sum_{q\le Q}qA(q)\ll Q^{1/3};                         \tag{15}
$$

integrate $\sum_{q>t}A(q)$ over $0\le t\le Q$.

For the exact asymptotic in (1), define a signed multiplicative function
$C$, supported on odd integers, by the local values

$$
C(p)=A(p),\quad C(p^2)=A(p^2),\quad C(p^3)=-p^{-4},
\quad C(p^k)=0\ (k\ge4).
$$

Equation (10) gives the exact convolution

$$
A(q)=\sum_{\substack{dm^3=q\\d,m\text{ odd}}}C(d)m^{-3}.
$$

Moreover
$\sum_d|C(d)|d^{2/3}<\infty$, by the same Euler-product comparison as
(12), with the additional summable term $p^{-2}$. Since

$$
\sum_{\substack{m>T\\m\text{ odd}}}m^{-3}\sim\tfrac14T^{-2}
$$

and this tail is $O(T^{-2})$ for every $T>0$, absolute rearrangement and
dominated convergence prove (1), with

$$
c=\frac14\prod_{p\text{ odd}}
\left(1+A(p)p^{2/3}+A(p^2)p^{4/3}-p^{-2}\right).
$$

The deviations of these factors from one are absolutely summable.
Each factor is at least $1-p^{-2}>0$, so the product is positive.

## Major-arc approximation without an epsilon loss

On $\alpha=a/q+\beta$, residue-class summation and partial summation give

$$
S_N(j\alpha)=\frac Nq S(q,ja)I_j(N^3\beta)
 +O\bigl(q(1+N^3|\beta|)\bigr)\qquad(j=1,2,4).         \tag{16}
$$

The implicit constants are absolute here. On the stated arcs the error
is $O(Q)$. Every exact factor and every main factor is at most $N$ in
absolute value, so telescoping the product yields

$$
W_N(\alpha)=M_N(\alpha)+O(QN^2),                       \tag{17}
$$

where, on the arc at $a/q$,

$$
M_N(a/q+\beta)=N^3q^{-3}S(q,a)S(q,2a)S(q,4a)
 I_1(N^3\beta)I_2(N^3\beta)I_4(N^3\beta).
$$

The arcs are disjoint for $N\ge2$: distinct reduced fractions are
separated by at least $1/(qq')$, and the sum of their radii is at most
$2Q^2/(qq'N^3)$. Their total measure is $O(Q^2/N^3)$.
Consequently

$$
\int_{\mathfrak M}|W_N-M_N|^2\ll NQ^4.                \tag{18}
$$

In particular, no factor $q^\varepsilon$ or $N^\varepsilon$ is hidden
in the approximation error.

Substitution $v=u^3$, followed by splitting at $v=|t|^{-1}$ and
integrating by parts on the remaining interval, proves
$I_j(t)\ll(1+|t|)^{-1/3}$. Hence

$$
\Phi(t):=|I_1(t)I_2(t)I_4(t)|^2\ll(1+|t|)^{-2}.
$$

This proves finiteness of $\mathfrak J$, while continuity at zero proves
positivity. Direct integration of the disjoint main terms gives

$$
N^{-3}\int_{\mathfrak M}|M_N|^2
=\sum_{q\le Q}A(q)\int_{|t|\le Q/q}\Phi(t)\,dt.
$$

The omitted denominators cost $O(Q^{-2/3})$ by (13), and the omitted
integral tails cost
$O(Q^{-1}\sum_{q\le Q}qA(q))=O(Q^{-2/3})$ by (15).
Therefore

$$
\int_{\mathfrak M}|M_N|^2
=N^3\mathfrak J\mathfrak S+O(N^3Q^{-2/3}).
$$

Cauchy–Schwarz bounds the cross term in (17) by $O(N^2Q^2)$,
using (18). The squared error $O(NQ^4)$ is no larger because
$Q\le N^{1/2}$. This proves (2).

## High-multiplicity outputs: the remaining minor-arc term

For a finite set $E$ of output integers put
$P_E(\alpha)=\sum_{n\in E}e(-n\alpha)$. Equation (2), Cauchy–Schwarz,
and $\int_0^1|P_E|^2=|E|$ imply

$$
\left|\int_{\mathfrak M(N,Q)}W_N(\alpha)P_E(\alpha)\,d\alpha\right|
\ll N^{3/2}|E|^{1/2}.                                \tag{19}
$$

If $E=\{n:R_N(n)>K\}$, then $|E|\le N^3/K$ because
$\sum_nR_N(n)=N^3$. Thus the major-arc contribution to the input mass
over these fibers is $O(N^3K^{-1/2})$, uniformly in $N$.

The exact full input mass is
$\sum_{n\in E}R_N(n)=\int_0^1W_NP_E$. The part over the complement
of $\mathfrak M$ has not been bounded sufficiently. In particular,
(19) is not a bound for this full nonnegative sum: either restricted
Fourier integral can have either sign. A small-set correlation estimate
for the minor arcs would supply a new route to tightness, but no such
estimate is established here. Bounded major-arc energy alone is
compatible with concentration on a density-zero set of outputs.

This compatibility is demonstrated by the [congruence-preserving sampling
construction](congruence_preserving_thinning.md). Its synthetic integer sequence
preserves (2), (17), and (18), as well as all fixed congruences and the joint
profinite limit, but has $O(N^2\log N)$ support and a heavy-fiber minor-arc
correlation $(1+o(1))N^3$. It need not factor into cubic Weyl sums, so a proof
using that additional structure is not excluded.

## Truncated restriction estimates leave a moderate-amplitude range

Here the degree is denoted by $k\ge3$. Put

$$
f_N(\alpha)=\sum_{x=1}^N e(\alpha x^k),\qquad
\tau=\max\{2^{1-k},1/(k(k-1))\},\qquad 0<\zeta<\tau/2.
$$

[Henriot--Hughes, Theorem 1.1 and (1.5)](https://arxiv.org/html/1610.03984)
give, for every fixed $\delta>0$,

$$
\int_{|f_N|\ge N^{1-\zeta}}|f_N|^{2k+\delta}
\ll_{k,\delta,\zeta}N^{k+\delta}.                       \tag{20}
$$

The full statement was checked: the cutoff includes the coefficient
$\ell^2$ norm, which is $\sqrt N$ here. In particular, it is not a
square-root cutoff. No uniform endpoint limit in $\delta$ is asserted.
The direct consequence at the critical moment is only

$$
\int_{|f_N|\ge N^{1-\zeta}}|f_N|^{2k}
\ll_{k,\delta,\zeta}N^{k+\zeta\delta}.                 \tag{21}
$$


One can isolate the further estimate needed even if (21) were improved.
Let $R_N$ count ordered sums of $k$ positive $k$th powers from $[1,N]$,
let $E_K=\{n:R_N(n)>K\}$, and put
$P_K(\alpha)=\sum_{n\in E_K}e(-n\alpha)$. Then

$$
|E_K|\le N^k/K,\qquad
\sum_{n\in E_K}R_N(n)=\int_0^1 f_N^kP_K.
$$

If an available moment estimate is
$\int_0^1|f_N|^{2s}\ll N^{s+\Delta_s}$, $1\le s\le k$,
Cauchy--Schwarz and the cutoff give exactly

$$
\left|\int_{|f_N|<N^{1-\zeta}}f_N^kP_K\right|
\ll \frac{N^k}{\sqrt K}
N^{\{(k-s)(1-2\zeta)+\Delta_s\}/2}.                  \tag{22}
$$

Indeed, bound $|f_N|^{2(k-s)}$ by
$N^{2(k-s)(1-\zeta)}$, and use $\|P_K\|_2=|E_K|^{1/2}$.
Even a hypothetical $O(N^k)$ bound for the high-amplitude critical
moment would control only its contribution by $O(N^k/\sqrt K)$.
For $s<k$ and $\Delta_s\ge0$, the exponent in (22) is strictly
positive. At $s=k$ it vanishes when $\Delta_k=0$, but that assumption
already supplies the sufficient full critical-moment bound. The
estimates used in this attempt leave a positive exponent and hence
do not give a fixed-$K$ heavy-fiber estimate. Improving the endpoint
only above the cutoff would not remove this loss. No new density
conclusion follows from this application of truncated restriction;
other uses of its weighted version are not ruled out.
