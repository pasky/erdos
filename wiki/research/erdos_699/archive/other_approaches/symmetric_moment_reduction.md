---
name: research/erdos_699/archive/other_approaches/symmetric_moment_reduction
title: "Erdős 699: symmetric moments reduce to the 81/80 singular points"
desc: "An exact arithmetic-progression moment construction has only three singular points after a quadratic substitution; the calculation identifies its stronger prime-power blocks and the normalization issue."
created: 2026-09-22T09:12:51Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: symmetric moments reduce to the 81/80 singular points

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

The following exact reduction explains a proposed simultaneous treatment of
$n,n-1,n-2$. It gives a valid construction and stronger divisibility than a
first inspection suggests. No new effective index bound follows here.

For nonnegative integers $a,b,d$, with $a,b$ even, put

$$
W(x)=x^a(x-2)^a(x-1)^b(10-x)^d(x+8)^d,
$$

$$J_i=\int_i^{10}W(x)\,dx\quad(i=0,1,2),\qquad
I=\int_0^1W(x)\,dx.$$

A common integer normalization may be applied throughout. Since
$W(2-x)=W(x)$,

$$
J_0-J_1=J_1-J_2=I.
$$

Consequently, if $X_i=n-i$, then

$$
X_0J_1-X_1J_0=X_1J_2-X_2J_1=J_0-nI.\tag{1}
$$

If the integer-normalized $X_i,J_i$ both have the appropriate three
pairwise coprime prime-power block divisors, (1) is divisible by their
product. This uses one moment row. Its size bound involves $J_0+nI$,
rather than products of two moment sizes.

Nonvanishing also has an exact proof. Replace $W$ by $(x-1)^2W$ to obtain
$I',J_i'$. Write $H=\int_2^{10}W$. The multiplier is strictly below 1 on
$(0,1)$ and strictly above 1 on $(2,10)$, so

$$
H'/I'>H/I.
$$

Since $J_0/I=2+H/I$, the two numbers $J_0-nI$ and $J_0'-nI'$ cannot both
vanish. The extra factor changes the degrees by a fixed amount and leaves
the original block divisors available.

## The quadratic reduction

Set $u=x-1$. Then

$$
W(x)=(u^2-1)^a u^b(81-u^2)^d.
$$

For the odd antiderivative

$$
F(v)=\int_0^v u^b(u^2-1)^a(81-u^2)^d\,du,
$$

we have exactly

$$J_0=F(9)+F(1),\qquad J_1=F(9),\qquad J_2=F(9)-F(1),
\qquad I=F(1).$$

A second substitution, $y=u^2$, gives

$$\boxed{F(v)=\frac12\int_0^{v^2}
 y^{(b-1)/2}(y-1)^a(81-y)^d\,dy.}\tag{2}$$

Thus the five-root integrand reduces to three singular points $0,1,81$.
These are the same singular points as the $81-80=1$ Padé seed. Because
$b$ is even, the first exponent in (2) is a half-integer. The reduction
alone does not justify importing the integer-parameter coefficient-gcd
formula: its denominator normalization must be established separately.
Nor does identifying the same singular points prove that every resulting
cofactor inequality is already implied by an existing source.

## The full block exponents

Let $L=2a+b+2d$. Integration of an integer polynomial can lose at most
$v_p(\operatorname{lcm}(1,\ldots,L+1))=O(\log L)$ powers of a fixed prime.
The following substitutions therefore identify the exponential parts of
the block divisors, before any common normalization.

For $J_0$, put $x=10t$: the integrand and differential contain
$10^{a+d+1}$. Hence its 5-adic valuation is at least

$$
a+d+1-\lfloor\log_5(L+1)\rfloor.
$$

For $J_1=F(9)$, put $u=9t$. The factors $u^b$, $(81-u^2)^d$, and $du$
contain $9^{b+2d+1}$. Its 3-adic valuation is therefore at least

$$
2b+4d+2-\lfloor\log_3(L+1)\rfloor.
$$

Finally, in $J_2$ put $x=2+8t$. The factors $x^a$, $(x-2)^a$,
$(10-x)^d$, $(x+8)^d$, and $dx$ contribute, respectively,
$2^a,2^{3a},2^{3d},2^d,2^3$. Thus its 2-adic valuation is at least

$$
4(a+d)+3-\lfloor\log_2(L+1)\rfloor.
$$

In directions $(a,b,d)=(Am,Bm,Dm)$, the block rates are consequently

$$\boxed{5^{(A+D)m},\quad
3^{(2B+4D)m},\quad 2^{4(A+D)m},}$$

up to factors of polynomial size. The middle and 2-adic blocks are
stronger than $9^{(B+D)m}$ and $8^{(A+D)m}$ obtained by looking only at
the integration endpoints. The endpoint ratio is exactly the $2^4\cdot5$
factorization of $80$; the middle block has the $3^4$ factorization of $81$.

The direct five-factor multinomial normalization is expensive. Small exact
computations confirm that its evaluated common divisor removes a substantial
part of that expense, so its generic coefficient-gcd lower bound should not
be mistaken for a sharp bound. The exploratory computations did not yield a
strict inequality excluding the remaining balanced index-six profile.
