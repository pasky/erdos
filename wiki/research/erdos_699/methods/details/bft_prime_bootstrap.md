---
name: research/erdos_699/methods/details/bft_prime_bootstrap
title: "Erdős 699: finite prime-interval bounds for the BFT coefficient gcd"
desc: "An exact fixed-point certificate lowers six BFT coefficient-gcd thresholds from millions of Padé parameters to between 1046 and 28602, preserving all cofactor exponents."
created: 2026-09-22T05:25:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: finite prime-interval bounds for the BFT coefficient gcd

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/asymmetric_cofactors|The asymmetric BFT argument]]

***

The six coefficient-gcd bounds needed by the index-ten cofactor argument
hold at much smaller numerical thresholds. No target cofactor exponent is
weakened.

Write $G(c,d,dm-\delta)$ for the coefficient gcd in BFT, with
$\delta\in\{0,1\}$. The following bounds are proved for every integer
$m\ge m_{\mathrm{start}}$:

$$
G(c,d,dm-\delta)\ge\exp(dm\ell). \tag{1}
$$

| Prime pair | $c,d$ | Exact $\ell$ | Previous analytic start | New $m_{\mathrm{start}}$ | Certified finite intervals |
| --- | --- | --- | ---: | ---: | ---: |
| $2,3$ | $29,20$ | $1702881759/4000000000$ | $100000000$ | $12744$ | $49436$ |
| $2,5$ | $43,35$ | $280222279237/10^{12}$ | $3000000$ | $1046$ | $13255$ |
| $2,7$ | $47,32$ | $444329464383/10^{12}$ | $100000000$ | $9825$ | $60168$ |
| $3,5$ | $55,34$ | $477383377397/10^{12}$ | $30000000$ | $4038$ | $39143$ |
| $3,7$ | $28,17$ | $120244724163/250000000000$ | $100000000$ | $13075$ | $49928$ |
| $5,7$ | $3,2$ | $7614497793/15625000000$ | $100000000$ | $28602$ | $19376$ |

The **231306 certified intervals** cover each finite range from its new
start to one less than its previous analytic start. The existing analytic
bound then covers the infinite tail. All interval margins are positive;
the smallest is greater than $2.9\cdot10^{-8}$ after dividing by $dm$.
The finite calculations concern primes and Padé parameters, not binomial
rows or columns.

The [checker](../../computations/erdos_699_bft_prime_bootstrap.py),
[input parameters](../../computations/erdos_699_bft_prime_bootstrap_parameters.json),
and [certificate](../../computations/erdos_699_bft_prime_bootstrap.json)
retain all constants, exact margins, and partition hashes.

## Prime intervals that divide the coefficient gcd

Put $h=c+d$. For an integer $t\ge1$, write

$$
dt=kh+r,\qquad 0\le r<h.
$$

Retain $t$ when $2r>h$. For $m\ge2t$, define

$$
 U_t(m)=\frac{hm-2}{t},\qquad
 V_t(m)=m\max\left\{\frac d{k+1},\frac{c-d}{t-2k-1}\right\}. \tag{2}
$$

The denominators in (2) are positive. BFT Lemma 5.2 and equations
(5.7)--(5.8) show that every prime

$$
V_t(m)<p\le U_t(m)
$$

divides both coefficient gcds in (1). The upper endpoint uses the smaller
value for $\delta=0,1$, and the lower endpoint uses upper bounds valid
for both. These prime intervals are disjoint for different $t$.

Consequently, for any finite retained set of eligible $t\le m/2$,

$$
\log G(c,d,dm-\delta)
\ge\sum_t\max\{\theta(U_t(m))-\theta(V_t(m)),0\}. \tag{3}
$$

BFT describes this finite prime-interval method and its extension across
ranges of $m$ in Section 5, following Lemma 5.4.

## Certifying a whole parameter interval

For an integer interval $L\le m\le R$, keep eligible $t\le\min(4000,L/2)$.
Both endpoints in (2) increase with $m$, so

$$
 S(L,R)=\sum_t\max\{\theta(U_t(L))-\theta(V_t(R)),0\}
 \le\log G(c,d,dm-\delta). \tag{4}
$$

The sufficient check is simply

$$
S(L,R)\ge dR\ell. \tag{5}
$$

All arguments of $\theta$ are rounded down to integers, exactly matching
its definition. The program evaluates a rigorous integer-scaled lower
bound for (4) and checks (5) by integer multiplication. It subdivides an
interval when this lower bound is insufficient.

The traversal runs from the right endpoint downwards. Once it encounters
an unsupported singleton, all larger integers have already been covered
by certified intervals. The chosen new start is one greater than that
singleton. This does not claim that (1) fails at the singleton: the
particular lower bound (4) was merely insufficient there.

## Rigorous logarithms and the sieve

The sieve retains every prime at most $10^8$, a total of $5761455$
primes. No numerical approximation is used to decide primality.

For logarithmic weights, let $Q=2^{32}$ and $M=2^{14}$. Directed interval
arithmetic gives integer lower and upper bounds for

$$
Q\log2,\qquad Q\log(k/M),\qquad M\le k\le2M.
$$

For each prime $p$, calculate exactly

$$b=\lfloor\log_2p\rfloor,\qquad
k=\left\lfloor\frac{pM}{2^b}\right\rfloor.$$

Then

$$b\log2+\log(k/M)\le\log p
\le b\log2+\log((k+1)/M). \tag{6}$$

The program obtains integer bounds for $Q\log p$ by adding the
corresponding table entries. Both prefix sums are integer arrays, with
explicit bounds preventing overflow. When both endpoints in a prime
interval lie below the sieve limit, subtracting two entries of the
*lower* prefix sums the lower weights of exactly the primes in that
interval. This avoids losing the errors from primes below its lower
endpoint.

The sieve, both logarithm tables, and both prefix sums have retained
SHA-256 hashes. The real arithmetic used to construct the logarithm
table is directed interval arithmetic; every subsequent certificate
comparison is an integer calculation.

## Larger prime arguments and the infinite parameter tail

Above the sieve limit, the checker combines

$$
x-2.072\sqrt x<\theta(x)<x\qquad(1\le x\le10^{11})
$$

from BFT Lemma 5.4 with the following retained bounds from Dusart's
Theorem 5.2:

$$
|\theta(x)-x|<\eta x/\log^k x.
$$

| $k$ | $\eta$ | Valid for $x\ge$ |
| ---: | ---: | ---: |
| $3$ | $1$ | $89967803$ |
| $2$ | $1/20$ | $122568683$ |
| $3$ | $39/50$ | $158822621$ |
| $1$ | $1/1000$ | $908994923$ |
| $2$ | $1/100$ | $7713133853$ |

The retained Dusart reading copy
records the theorem and its exact thresholds. Integer square roots and
the lower logarithmic table bounds make these inequalities rigorous at
every requested argument. All arguments used in the finite certificate
are below $10^{11}$, where the simpler upper bound $\theta(x)<x$ applies.

Finally, the checker regenerates each original infinite-tail certificate
using [the rational Dusart gcd calculation](../../computations/erdos_699_bft_dusart_gcd.py)
and checks that it supplies exactly the displayed $\ell$. Thus the finite
interval calculations and the existing analytic tail together prove (1)
for every integer $m$ at or above the new start.

To reproduce all six finite certificates:

```sh
mkdir -p tmp/erdos699
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_bft_prime_bootstrap.py \
  wiki/research/erdos_699/computations/erdos_699_bft_prime_bootstrap_parameters.json \
  --output tmp/erdos699/erdos699_prime_bootstrap.json
```

The data include elapsed times, which can differ between runs. The exact
bounds, interval counts and partition hashes are deterministic.
