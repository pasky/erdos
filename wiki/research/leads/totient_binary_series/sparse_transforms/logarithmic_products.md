---
name: research/leads/totient_binary_series/sparse_transforms/logarithmic_products
title: Precisely Scoped Limits of Logarithmic Products
desc: |
  No integer Euler product has a polynomial logarithmic defect for the
  totient series, and finite rational logarithmic transforms have unbounded denominators.
problems:
- 249
review_status: unreviewed
created: 2026-09-17T07:14:44Z
updated: 2026-09-17T07:14:44Z
---

***

Put $A(x)=\sum_{n\ge1}\varphi(n)x^n$ and
$L(x)=\sum_{n\ge1}\varphi(n)x^n/n$, so $xL'(x)=A(x)$.
The following formal-series arguments are author-recorded and unreviewed.
They concern specified transformation families, not all sparse products or
all approximants to $A(1/2)$.

## Integer products and a polynomial defect

Every $g\in1+x\mathbb Z[\![x]\!]$ has a unique formal representation

$$
g(x)=\prod_{d\ge1}(1-x^d)^{e_d},\qquad e_d\in\mathbb Z.
\tag{1}
$$

To construct it, suppose the factors with indices below $d$ have been
chosen, and their quotient into $g$ is $1+a_dx^d+O(x^{d+1})$.
Choose $e_d=-a_d$, since $(1-x^d)^{e_d}=1-e_dx^d+O(x^{2d})$.
This also proves uniqueness. Conversely, the binomial expansions have
integer coefficients and each coefficient uses only finitely many factors.
This is a formal statement; no analytic convergence is being asserted.

Logarithmic differentiation gives

$$
-\frac{xg'(x)}{g(x)}
 =\sum_{n\ge1}\psi_e(n)x^n,
\qquad \psi_e(n)=\sum_{d\mid n}d e_d.
$$

**Proposition 1.** There is no $g\in1+x\mathbb Z[\![x]\!]$ for which
$B=A+xg'/g$ is a polynomial.

*Proof.* Such a polynomial would give
$\varphi(n)=\psi_e(n)$ for all sufficiently large $n$.
At arbitrarily large primes $p$ this says $p-1=e_1+p e_p$.
Thus $p\mid e_1+1$ for arbitrarily large $p$, forcing $e_1=-1$ and
$e_p=1$ at every sufficiently large prime. Choose distinct such primes
$p,q\ge5$. At $pq$ the equality would become

$$
(p-1)(q-1)=-1+p+q+pq e_{pq},
\qquad pq(1-e_{pq})=2(p+q-1).
$$

The right side lies strictly between zero and $pq$, whereas the left is a
multiple of $pq$. This is impossible. $\square$

The exact logarithmic derivative and its repair by a polynomial defect
are therefore unavailable in this family. A rational or infinite defect,
or an unrelated product multiplier, is outside the proposition.

One can also see a precise obstruction in the defect's Lambert
coefficients. Write $B=\sum_{d\ge1}\beta_d x^d/(1-x^d)$. Möbius
inversion gives

$$
\beta_d=h(d)-d e_d,
\qquad h=\mu*\mu*\operatorname{id}.
$$

The multiplicative function $h$ satisfies
$h(p)=p-2$ and $h(p^a)=p^{a-2}(p-1)^2$ for $a\ge2$.
If $d\ge3$ and $d\not\equiv2\pmod4$, then $h(d)$ is nonzero and
$d\nmid h(d)$. Indeed, for the largest prime $p\mid d$, no factor
coming from a smaller prime contributes a $p$; the $p$-adic valuation
from $p^a\Vert d$ is zero for $a=1$ and $a-2$ for $a\ge2$.
The case of a power of two obeys the same latter formula. Hence
$\beta_d\ne0$ for every such $d$.
This is a statement about Lambert coefficients. It does not imply that
the Taylor coefficients of $gA$ have no gaps.

## Fixed powers, rational prefactors, and finitely many dilations

The rational Euler exponents for $\exp L$ alone do not prove that its
Taylor denominators cannot be cleared. The following coefficient argument
does supply that conclusion for a specified larger family.

**Theorem 2.** Let $(r_d)$ be a finitely supported nonzero sequence of
rational numbers, let $m=\min\{d:r_d\ne0\}$, and let
$R(x)\in\mathbb Q(x)$ be nonzero and regular at zero. Define

$$
E(x)=R(x)\exp\left(\sum_d r_d L(x^d)\right)
\in\mathbb Q[\![x]\!].
$$

If $h$ is the order of vanishing of $R$ at zero, then for all but finitely
many odd primes $p$,

$$
v_p\bigl([x^{mp+h}]E(x)\bigr)=-1.
\tag{2}
$$

In particular there is no nonzero integer $D$ with
$DE(x)\in\mathbb Z[\![x]\!]$.

*Proof.* Put $F(x)=\sum_d r_dL(x^d)$ and $r=r_m$.
Exclude primes dividing a numerator or denominator of $r$, any denominator
of the other $r_d$, or the finitely many denominators and nonzero leading
coefficients needed to express $R$ as a quotient of polynomials at zero.
All coefficients of $R$ are then $p$-integral, and its coefficient of
$x^h$ is a $p$-adic unit. This follows directly from the coefficient
recurrence obtained by multiplying by its denominator, whose constant
coefficient is a $p$-adic unit.

The lowest degree of $F$ is $m$, with coefficient $r$.
Every coefficient of $\exp F$ below degree $mp$ is $p$-integral:
all denominators $n$ occurring in the relevant $L$ coefficients are less
than $p$, and only factorials $j!$ with $j<p$ enter its exponential.
At degree $mp$, the only possibly nonintegral contributions are

$$
\frac{r(p-1)}p
\quad\text{and}\quad
\frac{r^p}{p!}.
$$

The first comes from $rL(x^m)$; all higher dilations use indices smaller
than $p$. The second comes from the product of $p$ lowest-degree terms
of $F$. Every other contribution is $p$-integral. After multiplying their
sum by $p!$, Wilson's and Fermat's congruences give

$$
r(p-1)(p-1)!+r^p\equiv2r\not\equiv0\pmod p.
$$

Thus this coefficient has valuation exactly $-1$. In the product with
$R$, the coefficient of degree $mp+h$ has just one summand with this
negative valuation, namely $[x^h]R\,[x^{mp}]\exp F$. All other summands
are $p$-integral. This proves (2). Choosing $p\nmid D$ disproves any
fixed common denominator. $\square$

For example, every nonzero rational power $\exp(rL)$, either sign of
$r$, fails to have bounded Taylor denominators, even after a fixed
rational prefactor. The obstruction persists for a fixed finite rational
combination of dilations in the exponent.

The nonzero residue $2r$ comes specifically from $\varphi(p)=p-1$.
For the divisor sum, $\sigma(p)=p+1$ changes that congruence to
$-r+r=0$, consistent with the integer Euler product in Duverney's
construction. This locates an arithmetic difference at the Taylor
coefficients themselves, beyond the rationality of formal Euler exponents.

This does not treat a denominator that grows with the Taylor cut-off,
a number of dilations that grows with the approximant, or an unrelated
integer product. Such families need their own height and remainder bounds.
The [[research/leads/totient_binary_series/sparse_transforms/prime_sieve|literal prime-sieve obstruction]]
is a separate result, and neither theorem asserts that every product or
Padé construction reduces to one gap criterion.
