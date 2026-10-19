---
name: research/erdos_699/methods/details/asymmetric_cofactors
title: "Erdős 699: asymmetric prime-pair bounds"
desc: "Keeping the two seed prime-power logarithms separate strengthens the BFT cofactor inequalities and gives a direct numerical threshold."
created: 2026-09-22T03:53:31Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: asymmetric prime-pair bounds

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/methods/details/bft_numerical_thresholds|Numerical BFT bounds]]

***

Bennett, Filaseta and Trifonov take a symmetric maximum near the end of
their Padé argument. Retaining the two prime-power logarithms separately
gives different exponents for the two cofactors. For example, their
Proposition 5.1 parameters give the entirely numerical assertion

$$\boxed{
 \max\{5^k u,7^l v\}-\min\{5^k u,7^l v\}\le100,
 \quad x:=\min\{5^k u,7^l v\}\ge10^{913}
 \ \Longrightarrow\ u>x^{.29}\ \text{or}\ v>x^{.20}.
}\tag{1}$$

Here $u,v$ are positive integers and $k,l$ are nonnegative integers.
No coprimality assumption is required. The two inequalities in the
conclusion form a disjunction, not a simultaneous assertion.

The source is BFT, Section 7,
in the author preprint associated with
[*On the factorization of consecutive integers*](https://doi.org/10.1515/CRELLE.2009.030).
The refinement and threshold calculation below are deductions in this
repository.

## 1. The asymmetric exponents

Use any BFT Theorem 2.4 parameter choice. Write

$$
P=p^{k_0},\quad Q=q^{l_0},\quad aP-bQ=D_0>0,\quad s=c/d,
$$

and suppose its coefficient-gcd bound

$$G(c,d,dm-\delta)\ge L_1^{dm}
 \qquad(m>m_0,\ \delta=0,1)$$

has been proved. Assume $\Omega_3>1$ and $\Omega_4>1$, with the notation
of that theorem. Set

$$A=\log P,\qquad B=\log Q,\qquad
 K=\max(A,B)+\frac{\log\Omega_4}{s}.\tag{2}$$

The limiting cofactor exponents are

$$\boxed{\alpha_p=1-\frac A K,\qquad
        \alpha_q=1-\frac B K.}\tag{3}$$

Thus the larger seed prime power retains the symmetric BFT exponent;
the smaller seed prime power has a strictly larger cofactor exponent.
For every fixed bounded gap and every positive $\epsilon$, the conclusion

$$u>x^{\alpha_p-\epsilon}\quad\text{or}\quad
  v>x^{\alpha_q-\epsilon}\tag{4}$$

holds beyond an effectively computable threshold. The next section gives
a fully numerical formula when $L_1,m_0$ are explicit.

The same effective conclusion holds with the limiting coefficient bound
$L(s)$ from BFT Theorem 2.2. Its Section 7 proof supplies an effective
$m_0$ after replacing $L(s)$ by $L(s)^{1-\epsilon'}$. Choose
$\epsilon'>0$ sufficiently small to preserve any strictly smaller target
exponents in (3). This does not assert a numerical threshold until that
coefficient-gcd estimate is instantiated.

## 2. A direct numerical threshold

Fix a gap bound $D\ge1$. Let $\kappa_1,\kappa_2$ be the explicit positive
constants in BFT Theorem 2.4, for this $D$. Choose target exponents
$0<t_p<\alpha_p$ and $0<t_q<\alpha_q$, and define

$$L=\max\left\{\frac A{1-t_p},\frac B{1-t_q}\right\}<K,
\qquad
M=\max\left\{m_0,\frac{\log\kappa_1}{d\log\Omega_3}\right\}.$$

Put

$$\boxed{
H=\max\left\{
 \log D,\ cL(M+1),\
 \frac{L}{K-L}\bigl(cK+\log2-\log\kappa_2\bigr)
\right\}.
}\tag{5}$$

For positive integers $u,v$ and nonnegative integers $k,l$, suppose

$$|p^ku-q^lv|\le D,\qquad
x=\min\{p^ku,q^lv\},\qquad \log x>H.$$

Then

$$
\boxed{u>x^{t_p}\quad\text{or}\quad v>x^{t_q}.}\tag{6}
$$

**Proof.** Suppose both conclusions fail. BFT's auxiliary integer is

$$m=\min\left\{
 \left\lfloor\frac{k}{k_0c}\right\rfloor,
 \left\lfloor\frac{l}{l_0c}\right\rfloor
\right\}.$$

The assumed cofactor upper bounds imply
$p^k\ge x^{1-t_p}$ and $q^l\ge x^{1-t_q}$. Consequently

$$
m>\frac{\log x}{cL}-1>M.\tag{7}
$$

Divide the original two prime powers into their blocks of length $cm$:

$$
p^ku=P^{cm}u'',\qquad q^lv=Q^{cm}v''.
$$

The integer linear combination in BFT (7.4), together with $m>M$,
gives its estimate (7.6):

$$v''>\kappa_2\Omega_4^{dm}
       \left(\frac P{\min(P,Q)}\right)^{cm}.$$

Multiplying by $Q^{cm}$ and using (2) yields

$$
q^lv>\kappa_2\exp(cmK).\tag{8}
$$

This step only uses the absolute difference bound in the integer linear
combination. It does not require that $p^ku$ be the larger input, and it
does not use BFT (7.7) or a coprimality hypothesis on the cofactors.
The nonvanishing choice between the two Padé approximants is exactly the
determinant argument preceding (7.4).

Since $x>D$, we also have $q^lv\le x+D<2x$. Combining this with (7)
and (8) gives

$$\left(\frac K L-1\right)\log x
 <cK+\log2-\log\kappa_2,$$

contradicting the last term of (5). This proves (6).

Formula (5) uses the cofactor upper bounds directly. It does not incur the
additional estimates used to pass from BFT's auxiliary parameter to one
symmetric maximum of the two cofactors.

## 3. The pair $5,7$

Use the BFT seed and Proposition 5.1 entry

$$2\cdot25-49=1,\qquad c/d=8/5,\qquad
L_1=1.5407,\qquad m_0=53.$$

Directed interval arithmetic gives

$$
\alpha_5>.3613046269,\qquad\alpha_7>.2277777234.
$$

For $D=100$, formula (5) yields these numerical statements:

| Targets $(t_5,t_7)$ | Certified threshold |
| --- | --- |
| $(.29,.20)$ | $x\ge10^{913}$ |
| $(.35,.22)$ | $x\ge10^{1731}$ |
| $(.35,.20)$ | $x\ge10^{985}$ |

For the first row, the controlling quantity is
$cL(M+1)<2101.583$; the other nontrivial term is less than $1115.615$.
The final certificate verifies $H<913\log10$ directly.

These inequalities can be combined with all the original symmetric
prime-pair constraints: each supplies an additional disjunction whose two
endpoints now have different weights. Replacing it by the smaller of the
two weights would discard the new information.

## 4. A smaller numerical last row at index eleven

Combine (1) with the six original BFT Theorem 2.1 constraints on
$2,3,5,7$. The [index-eleven weighted argument](../../proofs/details/index_11_effective.md)
then has exact minimum gain

$$\min\left\{-7+\sum_{a=0}^3(14-a)v_{(a)}\right\}
 =\frac{13}{125},$$

where the minimum ranges over all endpoint choices for the seven
disjunctions. It is attained by $(v_2,v_3,v_5,v_7)=(.285,0,.29,.038)$
and $(.285,.038,.29,0)$. The checker verifies all $2^7$ endpoint choices
with exact rational arithmetic.

Retaining the coefficients in the weighted argument improves the numerical
comparison. For weights $m_t=14-t$, the product of the largest possible
off-maximum small-prime contributions is

$$C_*=
\prod_{p\in\{2,3,5,7\}}p^{\max_{0\le r\le10}
 \sum_{t\ne r}(14-t)v_p(|t-r|)}
=2^{86}3^{47}5^{23}7^{14}.$$

The [exact weighted estimate](weighted_ramps.md), for $n\ge945000$, is

$$n^{13/125}\le
 \frac{1000\,11^{14}C_*}{999\,2^{56}},
\qquad n<10^{711}.$$

The last comparison is checked with integers. The checker also considers
every possible collision of maximal positions using the weighted row
capacities; the minimum gain remains $13/125$.
For $n\ge10^{914}$, all $n-r_p$ exceed $10^{913}$, so the new asymmetric
constraint and the original BFT numerical constraints apply. This
contradicts the algebraic bound. Consequently

$$
\boxed{n<10^{914}\quad\text{for every bad triple with }i=11.}
$$

This replaces the exponent $3\,639\,160\,902$ obtained from the stronger
symmetric cofactor table. It is a complete numerical stopping bound,
with no unevaluated source constants.

The [checker](../../computations/erdos_699_bft_asymmetric.py) and
[recorded intervals](../../computations/erdos_699_bft_asymmetric.json)
use the existing exact polynomial-integral evaluator for
$\kappa_1,\kappa_2$, and 80-digit directed intervals for all logarithms.
No rows are enumerated.

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_bft_asymmetric.py
```

## 5. Moderate numerical bounds at indices 13, 16 and 21

The same direct threshold formula applied to the seed $8-7=1$ with
the published parameters $c/d=3/2$, $L_1=1.5395$, $m_0=138$ gives

$$u_2>x^{.24}\quad\text{or}\quad u_7>x^{.29}
\qquad(x\ge10^{497},\ |2^a u_2-7^b u_7|\le100).$$

Its limiting endpoint exponents exceed $.25923834$ and $.30680637$.
The exact interval certificate is included in the same source checker.
Combining the asymmetric alternatives with the original explicit BFT
table and the weighted polynomials gives:

| $i$ | Additional asymmetric constraints | Other added pairs | $k$ | Gain | Algebraic cap | Complete row cap |
| --- | --- | --- | ---: | ---: | --- | --- |
| $13$ | $(5,7):(.35,.20)$; $(2,7):(.24,.29)$ | None | $8$ | $.103$ | $10^{1046}$ | $10^{1046}$ |
| $16$ | $(5,7):(.29,.20)$ | None | $10$ | $.23$ | $10^{686}$ | $10^{914}$ |
| $21$ | $(5,7):(.35,.22)$ | $(2,17):.3259$; $(17,19):.1855$ | $14$ | $.6648$ | $10^{534}$ | $10^{1732}$ |

Each final cap includes all source thresholds and numerator shifts.
The two symmetric pairs in the last row have the previously certified
numerical thresholds $10^{976}$ and $10^{957}$.

The [exact weighted checker](../../computations/erdos_699_asymmetric_ramp_caps.py)
and [its output](../../computations/erdos_699_asymmetric_ramp_caps.json)
verify all minimal disjunction vectors, all collisions of maximal
positions, and the integer comparisons establishing these bounds.
In particular, index thirteen has a moderate numerical bound without
needing the interpolation coefficient estimate.
