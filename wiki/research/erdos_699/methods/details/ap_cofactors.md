---
name: research/erdos_699/methods/details/ap_cofactors
title: "Erdős 699: cofactor bounds from quadratic constant-gap identities"
desc: "Composite-base Padé estimates give effective three-prime restrictions at AP positions and four-prime restrictions when two pairs have equal position sums."
created: 2026-09-22T04:53:21Z
updated: 2026-09-22T04:53:21Z
---

# Erdős 699: cofactor bounds from quadratic constant-gap identities

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/archive/previous_bounds/small_index_effective|Small-index effectivity]]

***

Three selected factors whose positions form an arithmetic progression obey
an effective cofactor restriction that does not follow from applying the
same Padé estimates to pairs of factors separately. The source identity is

$$
(n-r_-)(n-r_+)=(n-r_0)^2-h^2,
\qquad r_\pm=r_0\pm h.
\tag{1}
$$

The two sides have size comparable to $n^2$. Matching powers of a composite
base at the endpoints therefore gives a three-way alternative, with a factor
of two in the endpoint exponents.

The input is the BFT author preprint,
*On the factorization of consecutive integers*, Theorem 2.4 and especially
equation (7.6).
Theorem 2.4 permits distinct positive integer bases, including the composite
bases used here. The explicit coefficient-gcd estimate is proved in
[[research/erdos_699/methods/details/bft_numerical_thresholds|the numerical-threshold note]].

## 1. A three-way cofactor inequality

Fix a position bound $R$ and distinct primes $p_-,p_0,p_+$. Let
$0\le r_-<r_0<r_+\le R$ be in arithmetic progression, and write

$$
n-r_t=p_t^{k_t}u_t\qquad(t\in\{-,0,+\}),
\tag{2}
$$

where $k_t\ge0$ and $u_t$ are positive integers. Maximal prime-power
extraction is allowed, but is not needed for this assertion.

Choose positive integers $A,B,C$ and set

$$
M=p_0^B,\qquad E=p_-^A p_+^C.
$$

Choose either $(P,Q)=(M,E)$ or $(P,Q)=(E,M)$ as the oriented seed bases.
Suppose a BFT seed $aP-bQ=D_0>0$ and a rational parameter $s=c/d>1$
satisfy Theorem 2.4 with $\Omega_3,\Omega_4>1$. Put

$$
K=\log\max(P,Q)+\frac{\log\Omega_4}{s},
\quad
\alpha_0=1-\frac{\log M}{K},
\quad
\alpha_-=1-\frac{2A\log p_-}{K},
\quad
\alpha_+=1-\frac{2C\log p_+}{K}.
\tag{3}
$$

**Proposition.** For every choice of $\gamma_t<\alpha_t$, there is an
effectively computable $N$ such that every $n\ge N$ satisfying (2) obeys

$$
u_-\ge n^{\gamma_-}
\quad\text{or}\quad
u_0\ge n^{\gamma_0}
\quad\text{or}\quad
u_+\ge n^{\gamma_+}.
\tag{4}
$$

The threshold can be chosen uniformly for all AP positions in $[0,R]$.

**Proof.** Match all three prime-power exponents by taking

$$
m=\min\left\{
\left\lfloor\frac{2k_0}{Bc}\right\rfloor,
\left\lfloor\frac{k_-}{Ac}\right\rfloor,
\left\lfloor\frac{k_+}{Cc}\right\rfloor
\right\}.
\tag{5}
$$

Equation (1) becomes

$$
|P^{cm}U-Q^{cm}V|=h^2,
$$

with positive integers $U,V$. The sign is positive when $P=M$ and negative
when $P=E$. BFT's determinant argument leading to (7.6)
applies to these integers without any restriction on their size. Once
$m>m_0$ and $\kappa_1<\Omega_3^{dm}$, it gives

$$
V>\kappa_2\Omega_4^{dm}
       \left(\frac{P}{\min(P,Q)}\right)^{cm}.
$$

Here $\kappa_1,\kappa_2$ are the explicit constants before Theorem 2.4.
Use the gap bound $D=R^2$ in $\kappa_1$ to make them uniform in the
positions. The determinant inequality uses the absolute gap, so it holds
for either orientation. Multiplying by $Q^{cm}$ yields

$$
n^2\ge Q^{cm}V>\kappa_2\exp(cmK),
\qquad
cm<\frac{2\log n-\log\kappa_2}{K}.
\tag{6}
$$

If the middle floor attains the minimum in (5), then
$2k_0<Bc(m+1)$, and therefore, for $n\ge2R$,

$$
u_0>\frac12M^{-c/2}\kappa_2^{\log M/(2K)}n^{\alpha_0}.
\tag{7}
$$

If an endpoint floor attains the minimum, the corresponding bound is

$$
u_->\frac12p_-^{-Ac}\kappa_2^{A\log p_-/K}n^{\alpha_-},
\quad\text{or}\quad
u_+>\frac12p_+^{-Cc}\kappa_2^{C\log p_+/K}n^{\alpha_+}.
\tag{8}
$$

This also explains the factor two in (3): (6) bounds the matched block by
the logarithm of a product of two row factors, whereas an endpoint cofactor
belongs to just one row factor.

Choose an integer

$$
M>\max\left(m_0,0,\frac{\log\kappa_1}{d\log\Omega_3}\right).
$$

For $m\ge M$, equations (7)--(8) apply. If $m<M$, a floor attaining the
minimum bounds its corresponding prime-power exponent by a fixed constant;
that cofactor is at least a computable positive constant times $n$.
Since every $\alpha_t<1$, this also bounds one cofactor below by a
computable positive constant times $n^{\alpha_t}$.
Finally, the strict inequalities $\gamma_t<\alpha_t$ absorb these fixed
constants once $n$ exceeds an effective threshold. This proves (4). $\square$

## 2. Certified choices for the primes 2, 3 and 5

Set $u_p=(n-r_p)/p^{v_p(n-r_p)}$. Each row in the table means that, for all
sufficiently large $n$, at least one of the three inequalities
$u_p\ge n^{\gamma_p}$ holds. The stated middle prime must occupy the
middle position of the AP; the other two primes occupy its endpoints.

| Middle prime | Seed $aP-bQ=1$ | $s$ | $\gamma_2$ | $\gamma_3$ | $\gamma_5$ |
|---|---|---|---:|---:|---:|
| $2$ | $16-15=1$ | $11/8$ | $.348$ | $.483$ | $.243$ |
| $3$ | $81-80=1$ | $5/4$ | $.262$ | $.415$ | $.571$ |
| $3$ | $81-2\cdot40=1$ | $29/20$ | $.3299$ | $.292$ | $.4813$ |
| $5$ | $25-24=1$ | $4/3$ | $.194$ | $.574$ | $.376$ |

For example, $81-80=1$ uses $P=M=3^4$ and $Q=E=2^4\cdot5$; thus
the factor of two at the $2$-endpoint multiplies $4\log2$.

All four choices use $m_0=10^8$ and $4000$ prime intervals in the explicit
gcd estimate. The certified lower bounds for $\log L_1$ are, in table order,

$$
\frac{5899041743}{15625000000},\qquad
\frac{311676144201}{10^{12}},\qquad
\frac{423954159463}{10^{12}},\qquad
\frac{376473179729}{10^{12}}.
$$

Directed interval arithmetic verifies $\Omega_3,\Omega_4>1$ and
$\alpha_p-10^{-4}>\gamma_p$ in every case. The resulting threshold in
$n$ is effective; it has not been evaluated here.

These are additional arithmetic restrictions. For example, the cofactor
exponent vector $(e_2,e_3,e_5)=(0,.30,.28)$ satisfies the previously retained
pair bounds for these three primes, but violates the $81-80$ row when
$r_3$ is the middle AP position. This observation concerns the strength of
the inequalities, not the existence of row factors with that exponent vector.

Two further choices include the prime $7$:

| Middle prime | Endpoint primes | Oriented seed | $s$ | Certified alternative |
|---|---|---|---|---|
| $3$ | $2,7$ | $28-27=1$, $E=2^2\cdot7$, $M=3^3$ | $4/3$ | $u_2\ge n^{.483}$ or $u_3\ge n^{.385}$ or $u_7\ge n^{.274}$ |
| $3$ | $5,7$ | $245-243=2$, $E=5\cdot7^2$, $M=3^5$ | $5/4$ | $u_3\ge n^{.346}$ or $u_5\ge n^{.617}$ or $u_7\ge n^{.074}$ |

Both use the composite as $P$ and the middle prime power as $Q$. The gcd
inputs are those above for $s=4/3$ and $s=5/4$, respectively. The checker
verifies a margin of $10^{-4}$ in each exponent. For the second choice,
$K>8.40729345$ and the three unrounded exponents exceed
$.3466314,.6171329,.0741799$.

For an AP with middle prime $2$ and endpoint primes $3,7$, the additional
seed $64-63=1$, with $s=4/3$, gives the certified alternative

$$u_2\ge n^{.390}\quad\text{or}\quad
  u_3\ge n^{.356}\quad\text{or}\quad u_7\ge n^{.429}.$$

Its exact coefficient-gcd input and exponent intervals are included in
the same checker and output. The numerical-threshold note also supplies
this alternative using the published Proposition 5.1 entry at $s=9/7$.

For an AP with middle prime $7$ and endpoint primes $2,3$, the seed
$7-6=1$ gives the additional alternative

$$u_2\ge n^{.428}\quad\text{or}\quad
u_3\ge n^{.13}\quad\text{or}\quad u_7\ge n^{.198}.$$

It is included in the same certificate. The
[numerical product-threshold calculation](product_thresholds.md)
uses $s=3/2$ and the Dusart coefficient-gcd bound at $m_0=200000$, giving
a numerical height threshold $10^{329051}$ for positions in $[0,9]$.

## 3. Four factors with equal position sums

Suppose four selected positions satisfy

$$r_1+r_2=r_3+r_4,\qquad r_1r_2\ne r_3r_4,
\qquad 0\le r_t\le R.$$

Equivalently, the two unordered position pairs are different. In the
applications here all four positions are distinct.

Then

$$
(n-r_1)(n-r_2)-(n-r_3)(n-r_4)=r_1r_2-r_3r_4,
\tag{9}
$$

and the absolute gap is nonzero and at most $R^2$. Write
$n-r_t=p_t^{k_t}u_t$ for four distinct primes. Given positive integers
$a_1,a_2,a_3,a_4$, choose the oriented BFT bases from

$$
P=p_1^{a_1}p_2^{a_2},\qquad Q=p_3^{a_3}p_4^{a_4},
$$

interchanging the two bases if needed. With $K$ defined as in (3), matching

$$
m=\min_{1\le t\le4}\left\lfloor\frac{k_t}{a_tc}\right\rfloor
$$

gives the same bound (6). Consequently, for every

$$
\gamma_t<1-\frac{2a_t\log p_t}{K},
$$

at least one of $u_t\ge n^{\gamma_t}$ holds for all sufficiently large
$n$, with an effective threshold uniform in the positions. The proof of
(7)--(8), including the treatment of small $m$, applies to the four
possible minimum floors. No primeness of the BFT bases themselves is used.

For the partition $r_2+r_3=r_5+r_7$, take

$$
P=36=2^2\cdot3^2,\qquad Q=35=5\cdot7,\qquad a=b=1,\quad s=13/10.
$$

The exact gcd lower bound is

$$
\log L_1=\frac{334119934159}{10^{12}},\qquad m_0=10^8.
$$

The checker verifies $\log\Omega_3>.01868984524$,
$K>5.88707253765$, and the four unrounded exponents exceed

$$
.5290377,\quad .2535425,\quad .4532298,\quad .3389209.
$$

Thus the effective alternative

$$
u_2\ge n^{.528}\quad\text{or}\quad
u_3\ge n^{.253}\quad\text{or}\quad
u_5\ge n^{.453}\quad\text{or}\quad
u_7\ge n^{.338}
\tag{10}
$$

holds whenever $r_2+r_3=r_5+r_7$. The retained certificate again includes
a margin of $10^{-4}$.

These restrictions apply to the indicated position patterns. They require
a separate argument covering all other patterns before yielding an
effective bound for a whole index $i$.

The [checker](../../computations/erdos_699_ap_cofactors.py) and
[retained certificate](../../computations/erdos_699_ap_cofactors.json)
evaluate these seven analytic parameter choices. They enumerate no binomial
rows.
