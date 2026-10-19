---
name: research/erdos_699/methods/details/bft_numerical_thresholds
title: "Erdős 699: numerical thresholds for stronger prime-pair bounds"
desc: "Explicit bounds for the Padé coefficient gcd turn stronger prime-pair estimates into numerical stopping bounds, including index 11."
created: 2026-09-22T03:28:09Z
updated: 2026-09-22T03:40:04Z
---

# Erdős 699: numerical thresholds for stronger prime-pair bounds

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/small_index_effective|Small-index effectivity]]

***

The stronger prime-pair estimates need not retain an unevaluated source
constant. A finite sum of explicit prime-counting estimates supplies a
numerical lower bound for the coefficient gcd in the Padé construction of
Bennett, Filaseta and Trifonov (BFT). Their Theorem 2.4 then gives a numerical
threshold. In particular, the argument below supplies the unconditional row
bound

$$
n<10^{3\,639\,160\,902}\qquad(i=11).\tag{1}
$$

This is a very large stopping bound. Its significance is that every constant
has been evaluated. Smaller numerical prime-pair thresholds below also apply
to the weighted certificates at other indices.

The input is the BFT author preprint,
dated 26 February 2007, associated with the 2009 article
[*On the factorization of consecutive integers*](https://doi.org/10.1515/CRELLE.2009.030).
References to theorem numbers below concern that preprint.

## 1. An explicit coefficient-gcd bound

Take relatively prime integers $c>d\ge1$, put $H=c+d$, and fix positive
integers $T,m_0$ with $m_0\ge2T$. BFT's coefficient gcd is

$$G(c,d,n)=\gcd_{0\le r\le n}
 \left\{\binom{2n-r}{n}\binom{cm-n-1+r}{r}\right\},
 \qquad n=dm-\delta,\quad\delta\in\{0,1\}.$$

For each $1\le t\le T$ satisfying
$\{dt/H\}>1/2$, define

$$k_t=\lfloor dt/H\rfloor,\qquad
 v_t=\max\left\{\frac d{k_t+1},
                \frac{c-d}{t-2k_t-1}\right\}.\tag{2}$$

The denominators are positive. BFT Lemma 5.2 and the floor identities
(5.7)--(5.8) show that every prime in

$$
mv_t<p\le\frac{Hm-2}{t}\tag{3}
$$

divides $G(c,d,dm-\delta)$ for both values of $\delta$, whenever $m\ge m_0$.
Indeed, the actual lower endpoint from that lemma is at most $mv_t$, and
its actual upper endpoint is at least $(Hm-2)/t$.

These prime intervals are disjoint. The identity
$2(k_t+1)+(t-2k_t-1)=t+1$ gives $v_t\ge H/(t+1)$, so (3) lies inside
$(Hm/(t+1),Hm/t]$.

Write $\eta=213/10^6$. BFT Lemma 5.4 gives

$$
x-2.072\sqrt x<\theta(x)<x\quad(1\le x\le10^{11}),
$$
$$
|\theta(x)-x|\le\eta x\quad(x\ge10^8).\tag{4}
$$

Consequently $\theta(y)\le(1+\eta)y$ for every $y\ge1$.
Set $X_t=(Hm_0-2)/t$ and choose any rational number

$$
e_t\ge\max\left\{\eta,\frac{2.072}{\sqrt{X_t}}\right\}.
$$

Then $\theta(x)\ge(1-e_t)x$ for every $x\ge X_t$: the square-root
estimate handles $x<10^8$, and the relative estimate handles larger $x$.
The ranges in (4) overlap; there is no upper restriction on $m$.

Summing the prime products in the disjoint intervals proves

$$\boxed{
 G(c,d,dm-\delta)\ge\exp(dm\ell)
 \quad(m\ge m_0,\ \delta=0,1),
}\tag{5}$$

where any rational lower bound for

$$\ell_*=\frac1d\sum_{\substack{1\le t\le T\\\{dt/H\}>1/2}}
 \max\left\{0,
 (1-e_t)\frac{H-2/m_0}{t}-(1+\eta)v_t\right\}\tag{6}$$

can be used as $\ell$. To see this directly, the logarithm of the prime
product in (3), divided by $m$, is at least its summand in (6), before the
factor $1/d$. Terms with a negative lower bound may be discarded.

The checker uses $T=4000$ and forms $e_t$ using integer square roots:

$$w_t=\operatorname{isqrt}
 \left(\left\lfloor10^{12}(Hm_0-2)/t\right\rfloor\right),
\qquad
e_t=\max\left\{\frac{213}{10^6},\frac{259\cdot10^6}{125w_t}\right\}.$$

Thus $w_t/10^6\le\sqrt{X_t}$ exactly. Each positive normalized summand
in (6) is rounded down to a multiple of $10^{-12}$. The resulting $\ell$
is rational, with total downward rounding less than $4\cdot10^{-9}$.
No numerical prime enumeration is needed.

## 2. Applying the explicit Padé theorem

Use BFT Theorem 2.4 with $L_1(c/d)=\exp\ell$ and the $m_0$ from (5).
The three choices below use $m_0=100000$ and gap bound $D=100$.
The oriented seed is $aP-bQ=D_0>0$, where $P,Q$ are powers of the
indicated primes.

| Pair | Seed | $c/d$ | Certified exponent $w$ | $x_0<10^B$ |
| --- | --- | --- | ---: | ---: |
| $5,7$ | $2\cdot25-49=1$ | $59/39$ | $.2587$ | $B=13\,454\,096$ |
| $7,13$ | $343-2\cdot169=5$ | $51/38$ | $.1184$ | $B=14\,668\,210$ |
| $3,11$ | $243-2\cdot121=1$ | $125/92$ | $.3432$ | $B=45\,411\,830$ |

For each row, whenever $p^k u,q^l v\ge10^B$ and
$|p^k u-q^l v|\le100$, the conclusion is

$$
\max(u,v)>\min(p^ku,q^lv)^w.\tag{7}
$$

The theorem is evaluated with $\epsilon=1/20000$. The certificate verifies
$\Omega_3>1$, $\Omega_4>1$, and $\lambda_3-\epsilon>w$ by directed
interval arithmetic. The two polynomial integrals defining each
$C_{1,\delta},C_{2,\delta}$ are evaluated as exact rational numbers.
The remaining logarithms and square roots use 80-digit interval arithmetic.
For the reported integer $B$, the final check is
$\log x_0<B\log10$; a floating estimate merely proposes $B$.

The same checker instantiates fourteen further choices directly from BFT
Proposition 5.1. In particular, using $c/d=25/17$, $L_1=1.5540$,
$m_0=582$ at the pair $2,7$ yields exponent $.27346$, stronger than the
$.259 printed in BFT Theorem 2.1. All parameters, exact gcd certificates,
exponent intervals, and thresholds are retained in the output.

For the weaker improvements sufficient at index sixteen, much smaller
thresholds are possible. At $5,7$, use $c/d=79/51$, $m_0=100$, $T=50$,
and $\epsilon=1/1000$. Only three summands in (6) are positive, and the
exact certificate is

$$
\ell=\frac{159693825541}{500000000000}.
$$

It gives exponent $.23237$ with $x_0<10^{163784}$.
At $2,7$, the Proposition 5.1 choice $25/17$, $L_1=1.5540$, $m_0=582$
with $\epsilon=1/2500$ gives exponent $.27307$ and
$x_0<10^{70024}$. Both choices are retained in the `index_16_pairs`
section of the certificate. They can be combined with the original
numerical Theorem 2.1 table for all other pairs.

## 3. A fully numerical bound at index eleven

For $i=11$, use (5) with $m_0=10^7$ and these six choices:

| Pair | $c/d$ | Exponent $w$ | $x_0<10^B$ |
| --- | --- | ---: | ---: |
| $2,3$ | $132/91$ | $.2906$ | $1\,775\,929\,298$ |
| $2,5$ | $113/92$ | $.2671$ | $3\,249\,646\,235$ |
| $2,7$ | $119/81$ | $.2741$ | $1\,480\,882\,571$ |
| $3,5$ | $112/85$ | $.2227$ | $2\,062\,921\,054$ |
| $3,7$ | $145/88$ | $.0493$ | $3\,639\,160\,901$ |
| $5,7$ | $3/2$ | $.2650$ | $69\,004\,905$ |

The seed parameters are the corresponding BFT seeds, retained in the
checker; here $\epsilon=1/10000$ and again $D=100$.

The [weighted certificate for index eleven](../../proofs/details/index_11_effective.md)
applies with these exponents. Its exact minimum over the 64 choices of
witnessing endpoints is now

$$\min\left\{-7+\sum_{a=0}^3(14-a)v_{(a)}\right\}
 =\frac7{400}>0,\tag{8}$$

where $v_{(0)}\le\cdots\le v_{(3)}$ are the sorted vertex bounds.
This finite optimization is checked with integers. The argument therefore
gives, beyond the numerical prime-pair thresholds,

$$
n^{7/400}\le2(11!)^{14},\qquad n<10^{6100}.\tag{9}
$$

The second inequality is verified by an exact integer comparison.
If the selected maximal positions coincide, the earlier argument already
gives $n<10^{22}$. Finally, $n\ge10^{3\,639\,160\,902}$ implies that all
$n-r_p$ exceed the six numerical thresholds, and contradicts (9).
This proves (1), including the bounded shifts in the numerator factors.

## Reproduction

The [gcd and parameter checker](../../computations/erdos_699_bft_gcd_bounds.py)
and its [recorded output](../../computations/erdos_699_bft_gcd_bounds.json)
use the [explicit BFT threshold evaluator](../../computations/erdos_699_bft_explicit_thresholds.py).
These are finite checks of analytic parameters and small maximum-constraint
systems. They do not enumerate rows of Pascal's triangle.

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_bft_gcd_bounds.py
```
