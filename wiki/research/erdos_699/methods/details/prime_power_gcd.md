---
name: research/erdos_699/methods/details/prime_power_gcd
title: "Erdős 699: prime powers in the Padé coefficient gcd"
desc: "The coefficient-divisibility argument holds for each Legendre summand, so the numerical gcd estimate can use Chebyshev psi instead of theta. The common interval construction does not require floor stability."
created: 2026-09-22T16:59:03Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: prime powers in the Padé coefficient gcd

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Off-diagonal Padé estimates]]

***

The prime-interval divisor in the existing Padé argument extends to
prime powers. Consequently its logarithm can be bounded by differences
of

$$
\psi(x)=\sum_{p^k\le x}\log p
$$

instead of $\theta(x)$. Each prime power contributes $\log p$, not
$\log(p^k)$. There is no restriction such as $p^2>A+B+C$ in the
following lower bound.

## A carry at each prime power

Fix nonnegative integers $A,B,C$, a prime power $q=p^k$, and write
$a,b,c$ for the residues of $A,B,C$ modulo $q$. Suppose

$$
a+b+c\ge2q-1.\tag{1}
$$

The $k$th Legendre summand of every coefficient of each polynomial
$P_{A,B,C}$, $Q_{A,B,C}$, and $E_{A,B,C}$ is at least one. Thus, if
$\mathcal Q$ is any set of distinct prime powers satisfying (1), then

$$\boxed{\prod_{p^k\in\mathcal Q}p
 \ \text{divides every coefficient of }P,Q,E.}\tag{2}$$

To prove this, recall that the contribution at modulus $q$ to
$v_p\binom nk$ is

$$\left\lfloor\frac nq\right\rfloor
 -\left\lfloor\frac kq\right\rfloor
 -\left\lfloor\frac{n-k}q\right\rfloor\in\{0,1\}.$$

The coefficient products for $P,Q,E$ therefore have nonnegative
contributions at every prime power. It remains to prove a contribution
of at least one when (1) holds.

For the coefficient of $z^r$ in $Q$, ignore its sign and use

$$
\binom{A+C-r}{C}\binom{B+r}{r}.
$$

Let $y$ be the residue of $r$ modulo $q$, and $z$ the residue of
$A-r$ modulo $q$. If both contributions were zero, then
$z+c\le q-1$ and $b+y\le q-1$. Since $a\le y+z$, this would give
$a+b+c\le2q-2$, contradicting (1).

For $E$ the coefficient product is

$$
\binom{A+r}{r}\binom{A+B+C+1}{A+C+r+1}.
$$

Put $s=a+b+c$ and again write $y$ for the residue of $r$. Condition
(1) gives $\lfloor(s+1)/q\rfloor=2$. The contribution is

$$2+\left\lfloor\frac{a+y}{q}\right\rfloor
 -\left\lfloor\frac{a+c+y+1}{q}\right\rfloor
 -\left\lfloor\frac{b-y}{q}\right\rfloor\ge1,$$

because $c+1\le q$ and $\lfloor(b-y)/q\rfloor\le0$.

For $P$ the coefficient product is

$$
\binom{A+B+C+1}{r}\binom{A+C-r}{A}.
$$

Its contribution is

$$2-\left\lfloor\frac{s+1-y}{q}\right\rfloor
 +\left\lfloor\frac{a+c-y}{q}\right\rfloor
 -\left\lfloor\frac{c-y}{q}\right\rfloor\ge1,$$

because $b+1\le q$ and $\lfloor(c-y)/q\rfloor\le0$.
Summing these lower bounds over the powers of each prime proves (2).

## Eligible intervals without floor stability

Let $t\ge2$ and let $k_A,k_B,k_C$ be any nonnegative integers with

$$
k_A+k_B+k_C=t-2.
$$

Define

$$V=\max\left\{\frac{A}{k_A+1},
                  \frac{B}{k_B+1},
                  \frac{C}{k_C+1}\right\},
 \qquad U=\frac{A+B+C}{t}.$$

Every prime power $q\in(V,U]$ satisfies (1). Indeed

$$\left\lfloor\frac Aq\right\rfloor+
  \left\lfloor\frac Bq\right\rfloor+
  \left\lfloor\frac Cq\right\rfloor\le t-2,
 \qquad \frac{A+B+C}{q}\ge t,$$

so its residue sum is at least $2q$, which is slightly stronger than
(1). Moreover $q>V$ gives

$$
A+B+C<q\bigl((k_A+1)+(k_B+1)+(k_C+1)\bigr)=q(t+1).
$$

Thus the interval lies in
$((A+B+C)/(t+1),(A+B+C)/t]$. Intervals constructed for distinct $t$
are disjoint. The usual choices
$k_A=\lfloor At/(A+B+C)\rfloor$, and similarly for $B,C$, are
therefore sufficient but not necessary. This observation removes a
floor-stability requirement from the numerical common-interval proof.

For any finite family of such intervals, their prime-power product
is a common coefficient divisor, whose logarithm is exactly

$$
\boxed{\sum_t\bigl(\psi(U_t)-\psi(V_t)\bigr).}\tag{3}
$$

Empty intervals are omitted.

## One divisor for both adjacent rectangles

Let $\lambda,\mu,\kappa$ be positive integers, $H=\lambda+\mu+\kappa$,
and consider

$$A_\epsilon=\lambda m+\epsilon,\quad
 B_\epsilon=\mu m-1-\epsilon,\quad
 C_\epsilon=\kappa m+\epsilon,
 \qquad\epsilon\in\{0,1\}.$$

Require $m\ge m_0\ge1$ and $\mu m_0\ge2$. For every selected $t$
choose nonnegative $k_\lambda,k_\mu,k_\kappa$ with sum $t-2$. In
particular, one may retain the existing choices
$k_\lambda=\lfloor\lambda t/H\rfloor$, and similarly for the other
directions, whenever their sum is $t-2$. Set

$$
U_t(m)=\frac{Hm-1}{t},
$$

$$V_t(m)=m\max\left\{
 \frac{\lambda+1/m_0}{k_\lambda+1},
 \frac{\mu}{k_\mu+1},
 \frac{\kappa+1/m_0}{k_\kappa+1}\right\}.$$

For both values of $\epsilon$, these satisfy

$$V_t(m)\ge
 \max\left\{\frac{A_\epsilon}{k_\lambda+1},
             \frac{B_\epsilon}{k_\mu+1},
             \frac{C_\epsilon}{k_\kappa+1}\right\},
 \qquad
 U_t(m)\le\frac{A_\epsilon+B_\epsilon+C_\epsilon}{t}.$$

Hence every prime power in $(V_t(m),U_t(m)]$ contributes one factor
of its underlying prime to a common coefficient divisor of all six
polynomials, for both rectangles. The intervals are disjoint because
each is contained in the interval from the preceding section for
$\epsilon=0$. Therefore both coefficient gcds satisfy

$$\boxed{\log G_\epsilon\ge
 \sum_{t:V_t(m)<U_t(m)}
 \bigl(\psi(U_t(m))-\psi(V_t(m))\bigr),\qquad\epsilon=0,1.}\tag{4}$$

This is valid for every $m\ge m_0$ under the stated conditions. There
is no additional requirement that the floors of the shifted
rectangles agree with the directional floors. The new numerical
estimate can therefore use direct explicit bounds for $\psi$, and
can omit the old floor-stability threshold.
