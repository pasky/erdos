---
name: research/erdos_940/quintic_first_moment_barrier
title: Every quintic progression first moment exceeds two
desc: The uniform unordered quintic progression mean exceeds 2.468; a fifth-moment gap criterion is proved but its arithmetic hypotheses are not.
tags: []
sources: []
created: 2026-09-22T02:48:33Z
updated: 2026-09-22T21:53:34Z
---


# Every quintic progression first moment exceeds two

***

## Status and scope

The argument below is proved, including its finite exact comparisons. The
[preserved certificate](evidence/util/r5_first_moment.py) uses integer
convolution and rational arithmetic. The combined file runs and passes
under the evidence entry point. The local
formulas, tail estimates, and certificate logic have been checked in writing.

The subsequent
[four-unit extension](evidence/util/quintic_four_unit_extension.py) uses only 70
new coefficient profiles modulo 25. Its executed exact certificate and the
argument in Section 6 strengthen (1) to

$$
\liminf_{X\to\infty}\frac M X U_5(X;a,M)
>\frac{385732347}{156250000}=2.4686870208.                 \tag{0}
$$

Section 7 explains why even exact first-three Poisson factorial moments
at these means would not, by themselves, force an unrepresented target.
Neither statement resolves the infinitude or density questions.

Let $U_5(X;a,M)$ count unordered multisets of five positive $5$-powerful
integers whose sum is at most $X$ and congruent to $a\pmod M$.

**Theorem.** For every fixed modulus and residue,


$$
\liminf_{X\to\infty}\frac M X U_5(X;a,M)>\frac{429}{400}>1.
\tag{1}
$$


Thus the full unordered representation first moment cannot be reduced below one
by choosing a fixed progression. This rules out that particular route to a
density deficit for $S_5$. It proves neither positive density of distinct
represented values nor finiteness of the complement. An argument that removes
redundant representations would not be covered by this obstruction.

## 1. A finite canonical family and its weighted mass

Let


$$
\mathcal E=\{p\le1000:p\text{ prime},\ p\ne5,\ p\not\equiv1\pmod5\},
$$


and let $\mathcal C$ consist of canonical fifth-power cores supported on
$\mathcal E$: at each of these primes the exponent is one of $0,6,7,8,9$. This
is a finite set.

For a core tuple $\mathbf d=(d_1,\ldots,d_5)$, let $t_p$ be the number of its
coefficients prime to $p$. Put


$$
z_p=\sum_{s=1}^4p^{-1-s/5},\qquad
h_p(t)=\begin{cases}1-p^{1-t},&t\ge2,\\0,&t\le1.\end{cases}
$$


Independent choices of canonical prime exponents give the identity


$$
\sum_{\mathbf d\in\mathcal C^5}(d_1\cdots d_5)^{-1/5}
\prod_{p\in\mathcal E}h_p(t_p)
=\prod_{p\in\mathcal E}\sum_{t=2}^5\binom5t z_p^{5-t}(1-p^{1-t})=:H.
\tag{2}
$$


The exact certificate proves


$$
H>25000.
\tag{3}
$$


Specifically, with $R=10000$, replace $p^{-1/5}$ by $v/R$, where $v$ is the
largest integer satisfying $pv^5\le R^5$. Every polynomial factor in (2) is
increasing in $z_p$, so this produces a rational lower bound. The floor of that
rational lower bound is $26380$.

## 2. The local factors on the supporting primes

For $F_{\mathbf d}=\sum_i d_ix_i^5$, use the normalization


$$
\rho_{p^k}(a;\mathbf d)=p^{-4k}\#\{\mathbf x\bmod p^k:F_{\mathbf d}(\mathbf x)\equiv a\pmod{p^k}\}.
$$


If $p\ne5$ and $p\not\equiv1\pmod5$, fifth powering permutes $\mathbb F_p$. If
there are $t\ge1$ unit coefficients, there are exactly $p^4$ roots modulo $p$
for each target. For a zero target, the singular roots have all $t$
unit-coefficient variables zero, and number $p^{5-t}$; nonzero targets have no
singular roots. Nonsingular lifting therefore proves


$$
\rho_{p^k}(a;\mathbf d)\ge1-p^{1-t}=h_p(t)\qquad(t\ge2).
\tag{4}
$$


For $t\le1$, use the lower bound zero. This argument does not assert that fifth
powering permutes nonunits modulo higher prime powers.

For primes of this class greater than $1000$, all the selected coefficients are
units, so (4) supplies $1-p^{-4}$. Their product exceeds $99/100$, since


$$
\prod_{p>1000}(1-p^{-4})\ge1-\sum_{n>1000}n^{-4}
>1-\frac1{3\cdot1000^3}>\frac{99}{100}.
\tag{5}
$$


## 3. Exact small-prime factors

All coefficients are units at $5$ and at primes $p\equiv1\pmod5$. Unit
coefficients have five classes modulo fifth powers. Up to permutation of the
five variables, there are $\binom95=126$ coefficient multisets to consider.

For $p\equiv1\pmod5$, choose a primitive root $g$ modulo $p$ and form


$$
A_j(y)=\#\{x\bmod p:g^j x^5\equiv y\pmod p\},\qquad 0\le j<5.
$$


For each coefficient multiset, its cyclic convolution of five arrays is the
exact count for each target. Subtract one from the zero-target count to remove
the singular zero vector. The least count, divided by $p^4$, is a lower bound
for all targets at every power of $p$, by nonsingular lifting.

At $p=5$, instead take arrays modulo $25$, with $g=2$, while allowing the input
$x$ to range modulo $5$. A primitive input pattern modulo $5$ has local density
$1/125$ on its output class modulo $25$. Indeed, fix the other four coordinates
in their prescribed residue classes; the unit-coordinate fifth-power map is
five-to-one from a specified class modulo $5$ onto a specified fifth-power class
modulo $25$. Expanding $((u+5t)^5-u^5)/25$ proves the map property: its
reduction has nonzero linear coefficient and its derivative is a unit modulo
$5$, so the bijection lifts to all higher powers. The normalized density modulo
$5$ itself is $1$.

The exact primitive minima are as follows. The denominator is $p^4$, except at
$p=5$, where it is $125$.

| $p$ | Least primitive count |
|---:|---:|
| 5 | 65 |
| 11 | 3125 |
| 31 | 595650 |
| 41 | 2127000 |
| 61 | 11833800 |
| 71 | 20697250 |
| 101 | 89442500 |
| 131 | 280075900 |
| 151 | 511836000 |
| 181 | 1038852900 |
| 191 | 1291278950 |
| 211 | 1964362050 |
| 241 | 3326737200 |
| 251 | 3937876250 |
| 271 | 5292527850 |
| 281 | 6184725400 |
| 311 | 9120099250 |
| 331 | 11850879150 |
| 401 | 25624970000 |
| 421 | 31243739100 |
| 431 | 34259951150 |
| 461 | 44977169300 |
| 491 | 57804285700 |

The exact rational product of these factors is greater than $3/125$; its
approximate value is $0.02496026410022227$. The certificate uses NumPy integer
convolution, not floating-point FFT. Every intermediate coefficient is bounded
by $491^5<2^{63}$, so the integer arithmetic cannot overflow.

## 4. Bounds for the remaining primes

For $p\equiv1\pmod5$, expand the five complete exponential sums using an
order-five character. Of the $4^5=1024$ character exponent vectors, exactly
$(4^5-4)/5=204$ have exponent sum zero; the other $820$ have nonzero exponent
sum. Gauss-sum magnitudes and additive orthogonality give


$$
|\rho_p(0;\mathbf d)-1|\le204(1-p^{-1})p^{-3/2},
$$


and, for $a\ne0\pmod p$,


$$
|\rho_p(a;\mathbf d)-1|\le204p^{-5/2}+820p^{-2}.
$$


For $p>500$, the latter is at most $204p^{-3/2}$. Removing the zero vector and
using nonsingular lifting gives the uniform lower bound


$$
\rho_{p^k}(a;\mathbf d)\ge\gamma_p:=1-204p^{-3/2}-p^{-4}.
\tag{6}
$$


For $500<p\le5000$ in this prime class, the certificate uses
$k=\lfloor10000\sqrt p\rfloor$ and multiplies the rational lower bounds


$$
1-\frac{204\cdot10000}{pk}-p^{-4}.
$$


Their product is greater than $13/20$; its approximate value is
$0.6519469312995785$.

For $p>5000$, this prime class is contained in $p\equiv1,11\pmod{30}$. Write
$c_p=1-\gamma_p<1/1000$. A decreasing function $f$ has sum at most
$f(B)+\frac1{30}\int_B^\infty f(t)\,dt$ on either such progression above $B$.
Taking $B=5000$ and using $\sqrt{5000}>70$ gives


$$
\sum c_p<S:=2\left[204\left(\frac1{350000}+\frac1{1050}\right)
+\frac1{5000^4}+\frac1{90\cdot5000^3}\right].
$$


The rational inequality $\frac{1000}{999}S<2/5$, included in the certificate,
and $-\log(1-c)\le c/(1-c)$ imply


$$
\prod_{\substack{p>5000\\p\equiv1\ (5)}}\gamma_p>e^{-2/5}>\frac23.
\tag{7}
$$


For the last inequality, $\log(3/2)>2/5$ follows from the strict midpoint lower
bound for the integral of the convex function $1/t$ over $[1,3/2]$.

## 5. Archimedean factor and conclusion

Euler's product gives $\Gamma(1+z)\ge e^{-\gamma_E z}$ for $z>0$. Also
$\gamma_E<H_5-\log5<\log2$. For an elementary numerical-free check of the second
inequality, $H_5=137/60$ and the positive-term series for the logarithm gives


$$
\log10=3\log2+\log(5/4)
>3\left(\frac23+\frac2{81}\right)+\frac29
=\frac{62}{27}>\frac{137}{60}.
$$


Consequently $\Gamma(6/5)^5>1/2$.

For every fixed modulus and fixed core tuple, positive lattice-point counting
gives normalized progression mean


$$
\Gamma(6/5)^5(d_1\cdots d_5)^{-1/5}\rho_M(a;\mathbf d).
$$


Sum over the finite family $\mathcal C^5$. Factors corresponding to primes not
dividing $M$ can be inserted into the lower bound, because each lies in $[0,1]$.
CRT, (2), and the uniform bounds above therefore give ordered mean greater than


$$
\frac12\,H\,\frac3{125}\,\frac{13}{20}\,\frac23\,\frac{99}{100}.
$$


Canonical uniqueness prevents double counting of ordered summand tuples. Every
unordered multiset has at most $5!=120$ orderings, so


$$
\liminf_{X\to\infty}\frac M X U_5(X;a,M)
>\frac{25000}{120}\cdot\frac12\cdot\frac3{125}\cdot\frac{13}{20}
\cdot\frac23\cdot\frac{99}{100}
=\frac{429}{400}.
$$


This proves (1). The strict lower bound concerns representation counts, not the
number of distinct represented targets.

## 6. Extending the finite core family at five

Enlarge the old family to

$$
\mathcal C'=\{5^e d:d\in\mathcal C,\ e\in\{0,6,7,8,9\}\},
\qquad z_5=\sum_{s=1}^4 5^{-1-s/5}.
$$

These are distinct canonical cores. If exactly $t$ of five coefficients
are units at five, use the local lower bound

$$
\ell_5(t)=
\begin{cases}13/25,&t=5,\\9/25,&t=4,\\0,&t\le3.\end{cases}
$$

The five-unit bound was proved in Section 3. For four unit coefficients,
the additional certificate convolves the length-25 arrays
$\#\{x\bmod5:2^j x^5=y\pmod{25}\}$ over the 70 coefficient
multisets $0\le j_1\le\cdots\le j_4<5$. Removing the all-zero input
at target zero, the least primitive count is exactly nine; it occurs
for $(j_1,j_2,j_3,j_4)=(0,0,0,0)$ at target three.

Each primitive pattern in the four active coordinates has five choices
for the inactive coordinate modulo five. Each resulting full pattern
contributes normalized density $1/125$ at every $5^k$, $k\ge2$, by the
unit-coordinate lifting argument in Section 3. This gives $9/25$.
The inactive term is divisible by $5^6$, so it vanishes modulo 25;
even for $k>6$, its arbitrary higher digits can be compensated by the
chosen unit coordinate. Modulo five the density is one. Thus the
stated lower bound holds uniformly at all powers and targets.

At every other prime, multiplying a coefficient by $5^e$ preserves
the old hypotheses. At the supporting primes the bound depends only
on the number of unit coefficients; elsewhere the old coefficient-unit
estimates were uniform over all classes. Summing the new canonical
five-parts with their weights therefore replaces $13/25$ by

$$
\ell_5(5)+\binom54 z_5\ell_5(4)=\frac{13+45z_5}{25}.
$$

The terms with fewer unit coefficients are simply discarded. Local
factors for primes absent from $M$ can still be inserted because all
lie in $[0,1]$. All the other factors of the old proof, including the
division by $120$, remain unchanged. The resulting lower bound is

$$
\frac{429}{400}\left(1+\frac{45}{13}z_5\right).
$$

Finally $5(18/25)^5<1$, whence

$$
z_5>\frac15\sum_{j=1}^4(18/25)^j=\frac{734526}{1953125}.
$$

Exact rational arithmetic yields (0). The argument uses only a fixed
finite family and therefore has the same quantifier order as (1).

## 7. The third-moment gap inequality and its limitation

For any nonnegative integer-valued random variable $R$ with finite third
moment, put $\mu_j=\mathbb E(R)_j$. For every nonzero real $a$,

$$
\frac{(1-R)(R-a)^2}{a^2}\le\mathbf1_{R=0}.
$$

Taking expectations gives

$$
\Pr(R=0)\ge1-\mu_1+\frac{2\mu_2}{a}
 -\frac{2\mu_2+\mu_3}{a^2}.
$$

When $\mu_2>0$, choose $a=(2\mu_2+\mu_3)/\mu_2$ to obtain

$$
\Pr(R=0)\ge1-\mu_1+
\frac{\mu_2^2}{2\mu_2+\mu_3}.                            \tag{8}
$$

Thus suitable pair/triple collision estimates, not currently proved,
could give a gap through this inequality.

For Poisson factorial moments $\mu_j=\lambda^j$, the right side is
$(2-\lambda)/(2+\lambda)$. The threshold two cannot be improved by
any argument using just these three moments. Indeed let $Y=1$ with
probability $2/3$ and $Y=4$ with probability $1/3$. Then
$\mathbb E(Y)_j=2^j$ for $j=1,2,3$, although $Y$ never vanishes.
For every $\lambda\ge2$, adding an independent Poisson variable of
mean $\lambda-2$ gives a positive-supported law with the first three
factorial moments of Poisson$(\lambda)$, by the factorial binomial
identity. The strengthened floor (0) puts every fixed quintic
progression beyond this threshold.

No Poisson moment theorem is claimed for the actual representation
function. Nor does this calculation exclude a non-Poisson collision
inequality making (8) positive, or a successful higher-order argument.

## 8. A fifth-moment gap certificate

The preceding obstruction is specific to three moments. For any
nonnegative integer-valued $R$ with finite fifth moment, one has

$$
\Pr(R=0)\ge
1-\mu_1+\frac{51}{112}\mu_2-\frac{41}{336}\mu_3
+\frac{13}{672}\mu_4-\frac1{672}\mu_5.                 \tag{9}
$$

To prove this, set

$$
H(k)=(k-1)(k-3)(k-4)(k-7)(k-8).
$$

For integer $k\ge1$, the factor $k-1$ and each of the two
consecutive-root products are nonnegative. Since $H(0)=-672$,
$-H(k)/672\le\mathbf1_{k=0}$. Expanding gives the exact identity

$$
H(k)=(k)_5-13(k)_4+82(k)_3-306(k)_2+672k-672,
$$

and expectations prove (9).

Under the additional hypotheses $\mu_j=\lambda^j$ for $1\le j\le5$,
the right side equals $-f(\lambda)/672$, where

$$
f(\lambda)=\lambda^5-13\lambda^4+82\lambda^3
-306\lambda^2+672\lambda-672.
$$

Here

$$
f''(\lambda)=4(\lambda-3)(5\lambda^2-24\lambda+51),
\qquad f'(3)=51.
$$

The quadratic factor is positive everywhere, so $f'$ has global
minimum $51$. Also $f(31/10)=-88379/100000$. Consequently,
for every $0\le\lambda\le31/10$,

$$
\Pr(R=0)\ge\frac{88379}{67200000}>0.                  \tag{10}
$$

The identities above were checked by exact symbolic expansion.
The same bound holds as a liminf if five factorial moments converge
to these Poisson moments.

For the full unordered quintic representation function on a fixed
progression, such moment convergence with mean at most $31/10$
would prove a positive relative density of missing targets; the
shorter representations have density zero. **Neither that mean
upper bound nor the moment convergence is proved.** In particular,
the established mean lower bound $2.4686870208$ does not supply the
missing upper bound. This certificate is a conditional implication,
not an infinitude result for $S_5$.
