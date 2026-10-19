---
name: research/erdos_699/methods/details/off_diagonal_numerical_thresholds
title: "Erdős 699: fully numerical thresholds for unequal Padé blocks"
desc: "Explicit factorial, integral, and coefficient-gcd bounds turn the twenty index-twelve pair alternatives into numerical stopping bounds."
created: 2026-09-22T08:38:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: fully numerical thresholds for unequal Padé blocks

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Unequal Padé blocks]]

***

The twenty pair alternatives in the index-twelve ramp certificate have
fully numerical starting heights. Combining the uniform coefficient-gcd
estimates with a finite prime-interval bootstrap gives

$$
\boxed{n<10^{3\,071\,170}\qquad(i=12).} \tag{1}
$$

The [completed index-twelve proof](../../proofs/details/index_12_complete.md)
excludes the entire finite range below this stopping bound.
Every constant used below is evaluated or given by an explicit rational
formula; no unevaluated asymptotic constant remains.

## Finite factorial and integral bounds

Fix positive directions $(\lambda,\mu,\kappa)$ and write
$H=\lambda+\mu+\kappa$, $L_0=\lambda+\mu$, and
$L_1=\mu+\kappa$. The two adjacent rectangles are

$$A=\lambda m+\varepsilon,\quad
B=\mu m-1-\varepsilon,\quad C=\kappa m+\varepsilon,
\qquad\varepsilon\in\{0,1\}.$$

Assume $m\ge2$. Put

$$
S=H\log H-\lambda\log\lambda-\mu\log\mu-\kappa\log\kappa,
$$

$$
F=\max\left\{\mu,\frac{(H+1)\mu^2}{\lambda\kappa}\right\}.
$$

The multinomial theorem gives

$$
\frac{(Hm)!}{(\lambda m)!(\mu m)!(\kappa m)!}\le e^{Sm}.
$$

For $\varepsilon=0$, the integral prefactor is exactly $\mu m$ times
this multinomial coefficient. For $\varepsilon=1$, its ratio to the
multinomial coefficient is

$$
\frac{(Hm+1)(\mu m)(\mu m-1)}{(\lambda m+1)(\kappa m+1)}\le Fm.
$$

Thus both prefactors are at most $Fm e^{Sm}$.

For the seed $aP-bQ=D_0>0$, put $T=aP$ and $z=D_0/T$. Define

$$
M_Q=\max_{0<u<1}u^\mu(1-u)^\kappa(1-(1-z)u)^\lambda,
$$

$$
M_E=\max_{0<u<1}u^\lambda(1-u)^\kappa(1-zu)^\mu,
$$

and $q=S+\log M_Q$, $e=S+\log M_E$. These are precisely the two
saddle-point quantities in the unequal-block lemma.

In either integral, remove the $(m-2)$-th power of the corresponding
base integrand. Every remaining exponent is nonnegative, even when
$\mu=1$ and $\varepsilon=1$. Its remaining integrand is consequently
at most one. Therefore the explicit bounds

$$|Q_{A,B,C}(z)|\le FmM_Q^{-2}e^{qm},\qquad
|E_{A,B,C}(z)|\le FmM_E^{-2}e^{em} \tag{2}$$

hold for both rectangles. No Stirling remainder or limiting argument
is needed in (2).

## A numerical coefficient-gcd starting index

The [uniform gcd checker](../../computations/erdos_699_off_diagonal_gcd_numeric.py)
uses common prime intervals for both adjacent rectangles. For each
eligible $t$, put $k_X=\lfloor Xt/H\rfloor$ for
$X\in\{\lambda,\mu,\kappa\}$. After its exact floor-stability bound,
the interval

$$
\left(
m\max\left\{\frac{\lambda+1/m_0}{k_\lambda+1},
\frac\mu{k_\mu+1},
\frac{\kappa+1/m_0}{k_\kappa+1}\right\},
\frac{Hm-1}{t}\right]
$$

is contained in both coefficient-gcd intervals for every $m\ge m_0$.
The intervals for distinct $t$ are disjoint. The retained explicit
prime bounds give a rational lower bound for their total logarithmic
prime product, divided by $m$.

With 4,000 terms, all twenty original logarithmic gcd rates $\ell$
are valid numerically: fifteen sources have $m_0=10^8$ and five have
$m_0=10^9$. The [gcd certificate](../../computations/erdos_699_off_diagonal_gcd_numeric.json)
records every exact rate comparison and names the source and ramp files.

The [finite bootstrap](../../computations/erdos_699_off_diagonal_gcd_bootstrap.py)
then reduces all twenty starting indices to at most $18795$, while
preserving every original rate $\ell$. Here is its uniform interval
argument. For $m\in[L,U]$ and a $t$ whose floors have stabilized by $L$,
use the fixed common prime interval

$$
\left(
\max\left\{\frac{\lambda U+1}{k_\lambda+1},
\frac{\mu U}{k_\mu+1},
\frac{\kappa U+1}{k_\kappa+1}\right\},
\frac{HL-1}{t}\right].
$$

Every prime in this interval divides both coefficient gcds for every
integer $m\in[L,U]$. Summing directed lower bounds for their logarithms
and comparing with $\ell U$ certifies the entire interval at once.
An exact sieve and directed fixed-point logarithm table cover endpoints
through $10^8$; the retained BFT prime bounds cover all larger endpoints,
which remain below $10^{11}$.

The bootstrap works backwards from each analytic starting index. Its
certified intervals form a contiguous partition, checked at every step.
Stopping immediately above the first unsupported singleton leaves no
gap before the analytic tail. In total, the
[certificate](../../computations/erdos_699_off_diagonal_gcd_bootstrap.json)
records $1\,356\,673$ certified intervals. The resulting $m_0$ values,
in the ramp's binding order, are

$$
14192,17247,6201,8976,14366,9130,13835,16349,10921,18795,
8140,9636,14996,11952,16697,4571,5683,7127,13737,15235.
$$

These are prime-interval certificates, not a scan of binomial rows.

## Numerical cofactor alternatives

Let $X=p^ku$, $Y=q^lv$ lie in $[h,h+R]$, with $|X-Y|\le D$.
The seed sides are powers of $p,q$, respectively. Suppose
$u\le h^{e_p}$ and $v\le h^{e_q}$. Define

$$\rho=\min\left\{\frac{1-e_p}{L_0\log P},
\frac{1-e_q}{L_1\log Q}\right\}.$$

Choose a positive rational $t<\rho$ such that $tK_0>1$, and set
$m=\lfloor t\log h\rfloor$. Then both residual prime-power blocks
are integral. The determinant supplies a nonzero integer, and (2),
the gcd bound $G\ge e^{\ell m}$, and the exact normalizations give

$$
1\le m\left(A_1e^{-C_0m}+Y A_2e^{-K_0m}\right),\tag{3}
$$

where $C_0,K_0$ are the stated unequal-block rates and

$$A_1=DTF M_Q^{-2},\qquad
A_2=\frac{D_0^3}{T}F M_E^{-2}. \tag{4}$$

The factors $T$ and $D_0^3/T$ cover both values of $\varepsilon$.
For $h>R$, put $x=\log h$ and

$$
\eta=\min\{tC_0,tK_0-1\}>0,
$$

$$
L=\log(2t)+\max\{\log A_1+C_0,\log(2A_2)+K_0\}.
$$

Since $m\le tx$, $m\ge tx-1$, and $Y<2h$, (3) implies

$$
1\le e^L x e^{-\eta x}.\tag{5}
$$

The checker finds an integer $K$ for which, at $x=K\log10$,

$$tx\ge m_0+1,\qquad x\ge\log(R+1),\qquad
\eta x>1,\qquad L+\log x-\eta x<0.\tag{6}$$

The last expression decreases for $x>1/\eta$. Thus the contradiction
holds for every $h\ge10^K$, not just at the tested endpoint.

## Index twelve

For each of the twenty exact edge bindings in
[the ramp data](../../computations/erdos_699_index_12_ramp.json), use
$h=n-11$ and $D=R=11$. The
[finite-constant checker](../../computations/erdos_699_off_diagonal_explicit_pairs.py)
certifies (6) for every source. Its
[numerical certificate](../../computations/erdos_699_off_diagonal_explicit_pairs.json)
records all prefactors, rational block parameters, directed decay margins,
and twenty individual thresholds.

Their largest exponent is $3071169$, from the $(3,5)$ alternative with
targets $(.40,.10)$ and gcd starting index $13835$. The existing $F_8$ ramp has
gain $1/10$ and algebraic bound $10^{845}$. Adding one decimal power
absorbs the row shift of eleven and proves (1).

For comparison, omitting the finite bootstrap gives the weaker but still
fully numerical cap $10^{158933576214}$. The source certificate records
both versions.

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_12_ramp.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_off_diagonal_gcd_numeric.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_off_diagonal_gcd_bootstrap.py
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_off_diagonal_explicit_pairs.py
```
