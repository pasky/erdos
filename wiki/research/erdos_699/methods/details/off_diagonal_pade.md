---
name: research/erdos_699/methods/details/off_diagonal_pade
title: "Erdős 699: off-diagonal Padé approximants and unequal prime-power blocks"
desc: "General Padé rectangles give effective joint cofactor estimates with different block lengths on the two sides, improving several difficult small-index configurations."
created: 2026-09-22T06:30:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: off-diagonal Padé approximants and unequal prime-power blocks

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/rational_product_bounds|Joint rational-block estimates]]

***

The diagonal choice $A=C$ in BFT's application of Padé approximation is
not necessary. The general polynomials in its Lemma 3.1 give two different
prime-power block lengths. Retaining this difference improves some of the
cofactor estimates. The conclusion below is effective; it does not assume
an ineffective approximation theorem.

These are conditional source inequalities. Excluding one previously
difficult cofactor vector does not establish an entire binomial index:
every new alternative and every position assignment still needs coverage.

## The exact identity and nonvanishing

Use the integral normalizations of BFT (3.1)--(3.4), so that

$$P_{A,B,C}(z)-(1-z)^{B+C+1}Q_{A,B,C}(z)
 =z^{A+C+1}E_{A,B,C}(z).\tag{1}$$

Their degrees are respectively $C,A,B$. Let $P',Q',E'$ refer to
$(A+1,B-1,C+1)$, where $B\ge1$. The exponent $B+C+1$ in (1) is
unchanged, and subtracting the two identities gives

$$
PQ'-QP'=z^{A+C+1}(EQ'-z^2QE').
$$

The left side has degree at most $A+C+1$. Therefore

$$
\boxed{PQ'-QP'=D_{A,B,C}z^{A+C+1},\qquad D_{A,B,C}\ne0.}\tag{2}
$$

Indeed its coefficient of $z^{A+C+1}$ is $E(0)Q'(0)$, which is nonzero
by the integral formulas, or by the binomial-coefficient expansions.
This proves the required determinant statement for all rectangles, not
only $A=C$. The integral normalization fixes the signs consistently;
only absolute values are used below.

Choose a seed $aP_0-bQ_0=D_0>0$, and set $z=D_0/(aP_0)$. Let $G$ be
the gcd of the coefficients of $Q_{A,B,C}$. The identity shows that
$G$ also divides every coefficient of $P_{A,B,C}$ and $E_{A,B,C}$.
Thus the integers

$$\mathcal P=G^{-1}(aP_0)^C P(z),\quad
\mathcal Q=G^{-1}(aP_0)^A Q(z),\quad
\mathcal E=G^{-1}(aP_0)^B D_0^{A+C+1}E(z)$$

satisfy

$$\boxed{(aP_0)^{A+B+1}\mathcal P
 -(bQ_0)^{B+C+1}\mathcal Q=\mathcal E.}\tag{3}$$

Both block lengths $A+B+1$ and $B+C+1$ are preserved by the adjacent
rectangle in (2). Hence the two choices still supply a nonzero integer
linear combination after any residual denominators are cleared.

Using a common denominator power $\max(A,C)$ instead would lose this
advantage. Formula (3) is the reason unequal rectangles help.

## An effective coefficient-gcd lower bound

Fix positive integer directions $\lambda,\mu,\kappa$, and take

$$A=\lambda m,\qquad B=\mu m-1,\qquad C=\kappa m,
\qquad H=\lambda+\mu+\kappa.$$

For a finite set of positive integers $t$ satisfying

$$\left\lfloor\frac{\lambda t}{H}\right\rfloor+
\left\lfloor\frac{\mu t}{H}\right\rfloor+
\left\lfloor\frac{\kappa t}{H}\right\rfloor=t-2,$$

put

$$L_T=\sum_t\left[\frac Ht-
\max\left\{
\frac\lambda{\lfloor\lambda t/H\rfloor+1},
\frac\mu{\lfloor\mu t/H\rfloor+1},
\frac\kappa{\lfloor\kappa t/H\rfloor+1}
\right\}\right].\tag{4}$$

This is an explicit positive rational number. Every summand comes from
a disjoint prime interval in BFT Lemma 5.2. For any rational $\ell<L_T$,

$$
G\ge e^{\ell m}\tag{5}
$$

holds above an effectively computable $m_0$, for both adjacent rectangles.

Here is why the bounded shifts in $A,B,C$ cause no difficulty. For an
eligible $t$, the three fractional parts in (4) sum to $2$. None can
be zero, since the other two are strictly less than $2$ in total.
Consequently all the floors stabilize effectively under these shifts.
The corresponding interval endpoints are $m$ times the displayed constants,
up to bounded errors. The effective prime-number estimates already retained
in the [Dusart note](dusart_gcd_bounds.md) give
$\theta(x)/x\longrightarrow1$ with a computable rate. Apply them to the
finitely many interval endpoints and absorb the strict difference
$L_T-\ell$. This proves (5) with an effective threshold. No estimate
for an infinite tail of (4) is needed.

## The two exponential rates

Define

$$
S=H\log H-\lambda\log\lambda-\mu\log\mu-\kappa\log\kappa,
$$

$$q=S+\max_{0<u<1}
 \{\mu\log u+\kappa\log(1-u)
                  +\lambda\log(1-(1-z)u)\},$$

$$e=S+\max_{0<u<1}
 \{\lambda\log u+\kappa\log(1-u)
                  +\mu\log(1-zu)\}.$$

The two maxima are at unique points in $(0,1)$, determined by quadratic
equations. They can therefore be bounded with directed intervals.
The integral formulas and effective factorial estimates give the growth
rates $q,e$ for $Q,E$, with at most a polynomial factor in $m$.
Such a factor is bounded effectively by $e^{\epsilon m}$ for every
fixed $\epsilon>0$.

After division by the coefficient gcd, the decay rates needed in the
integer argument are

$$
C_0=\mu\log P_0-\lambda\log a-(\mu+\kappa)\log b-q+\ell,
$$

$$K_0=\lambda\log P_0+(\mu+\kappa)\log Q_0
 -\mu\log a-(\lambda+\kappa)\log D_0-e+\ell.\tag{6}$$

The block lengths per unit $m$ are
$L_0=\lambda+\mu$ and $L_1=\mu+\kappa$.

## The effective joint criterion

Write nearby factors as $f_p=p^{k_p}u_p\in[h,h+R]$, for distinct primes,
and form products $X,Y$ of equal degree $d$ with positive multiplicities
$b_p$. Assume $|X-Y|\le D$, with a fixed positive bound $D$.
The primes occurring in each product must
be precisely those in the corresponding seed side

$$P_0=\prod_{p\in I_0}p^{a_p},\qquad
Q_0=\prod_{p\in I_1}p^{a_p}.$$

For a proposed upper cofactor vector $e_p$ and a real $t>0$, set

$$\Delta(t)=\sum_p
 \bigl(tL_{s(p)}a_p\log p-b_p(1-e_p)\bigr)_+,$$

where $s(p)$ is the seed side. If

$$\boxed{tC_0-\Delta(t)>0,\qquad
         tK_0-\Delta(t)-d>0,}\tag{7}$$

then the simultaneous bounds $u_p\le h^{e_p}$ are impossible above an
effectively computable height.

To prove this, use $m=\lfloor t\log h\rfloor$ and clear the residual
denominators of $X/P_0^{L_0m}$ and $Y/Q_0^{L_1m}$. Their logarithmic cost
is at most $\Delta(t)\log h$. Equations (2), (3), and (6) yield, for a
computable constant $C_\epsilon$,

$$1\le C_\epsilon e^{\epsilon m}
 \left(e^{\log Z-mC_0}+Y e^{\log Z-mK_0}\right).$$

Since $Y\le2^d h^d$ for $h>R$, both terms tend effectively to zero
when $\epsilon>0$ is chosen small enough relative to the strict margins
in (7). This contradiction proves the criterion.

The actual product difference may be zero. Nonvanishing of the integer
linear combination comes from the seed determinant (2), whose seed gap
$D_0$ is positive; it does not come from $X-Y$. If $X=Y$, the term
involving $X-Y$ simply vanishes. Thus the same joint constraints apply
when two selected prime powers belong to the same numerator factor.
Their valuation and factorization hypotheses must still be checked.

The integral-block alternative is an immediate special case. Provided
$C_0>0$, every target strictly below

$$
1-\frac{dL_{s(p)}a_p\log p}{b_pK_0}\tag{8}
$$

is a valid coordinate in a cofactor disjunction. The joint criterion (7)
can be stronger than these coordinatewise limits.

The inequalities can also be replaced by rational linear alternatives
for exact subsequent computations. Fix rational $t>0$, choose rational
$g_p>tL_{s(p)}a_p\log p-b_p$, and choose a positive rational
$R<\min(tC_0,tK_0-d)$. Above an effective threshold, necessarily

$$
\sum_p(b_pe_p+g_p)_+\ge R.
$$

Otherwise both margins in (7) have a uniform positive lower bound.
The last inequality is equivalent to the finite disjunction

$$\sum_{p\in J}b_pe_p\ge R-\sum_{p\in J}g_p
\quad\text{for at least one nonempty subset }J.$$

The [rational-clause checker](../../computations/erdos_699_off_diagonal_clauses.py)
rounds the intercepts upwards and the threshold downwards, then verifies
every rounding and a strict source margin using directed intervals.
Its [example certificate](../../computations/erdos_699_off_diagonal_clauses.json)
contains only rational coefficients for the resulting linear alternatives.
This separates the analytic source verification from exact polyhedral
coverage calculations.

## A four-prime example

For $P_0=847=7\cdot11^2$, $Q_0=845=5\cdot13^2$, $a=b=1$, use
directions $(\lambda,\mu,\kappa)=(39,7,33)$. The finite sum (4) through
$t=200$ exceeds $3.0421$, so take $\ell=3$. Directed evaluation gives

$$
C_0/40>.01316,\qquad K_0/40>11.5489.
$$

Thus, for four distinct positions satisfying $r_7+r_{11}=r_5+r_{13}$,
the following alternative holds effectively:

$$u_7>h^{.612}\quad\text{or}\quad u_{11}>h^{.044}
\quad\text{or}\quad u_5>h^{.721}\quad\text{or}\quad u_{13}>h^{.111}.$$

The product gap is a fixed nonzero difference of the position products.
This strengthens the diagonal source for the same seed. Applying it in a
whole-index proof still requires covering every branch of the alternative.

The [checker](../../computations/erdos_699_off_diagonal_pade.py) and
[certificate](../../computations/erdos_699_off_diagonal_pade.json)
record the finite rational gcd sum, the two saddle points, directed bounds
for both rates, and a strict margin for each listed exponent. The same
checker exports the general growth calculation for other seeds and rectangles.

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_off_diagonal_pade.py
```
