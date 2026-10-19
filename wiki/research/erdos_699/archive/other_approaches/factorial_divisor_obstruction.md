---
name: research/erdos_699/archive/other_approaches/factorial_divisor_obstruction
title: "Erdős 699: why fixed factorial ratios cannot replace the Padé gcd estimate"
desc: "Every fixed product of shifted factorials that divides a Padé coefficient gcd for all sufficiently large parameters has only polynomial growth. A reflection identity for factorial valuations proves the obstruction."
created: 2026-09-22T16:42:34Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: why fixed factorial ratios cannot replace the Padé gcd estimate

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Off-diagonal Padé estimates]]

The coefficient gcd gives an exponential improvement in the Padé bounds.
It is tempting to replace its prime-interval estimate by an explicit
factorial ratio, and then use Stirling's formula to obtain a numerical
starting index. The following obstruction rules out this particular route.
It does not rule out better prime estimates or formulas involving gcds,
least common multiples, or a number of factorials that grows with the
parameter.

Let

$$G(A,B,C)=\gcd_{0\le r\le A}
 \left\{\binom{A+C-r}{C}\binom{B+r}{r}\right\}.$$

These are, up to a common sign, the coefficients of the Padé polynomial
$Q_{A,B,C}$ used in the existing proof.

**Proposition.** Fix positive integers $\lambda,\mu,\kappa$ and fixed
integer shifts $a,b,c$. Set

$$A_m=\lambda m+a,\qquad B_m=\mu m+b,\qquad
 C_m=\kappa m+c.$$

Suppose that a fixed factorial expression

$$R_m=\prod_{j=1}^s
 \bigl(\lfloor\alpha_jm+\beta_j\rfloor!\bigr)^{e_j},
 \qquad \alpha_j\in\mathbf Q_{>0},\quad
 \beta_j\in\mathbf R,\quad e_j\in\mathbf Z,$$

is an integer divisor of $G(A_m,B_m,C_m)$ for every sufficiently large
integer $m$. Then, for every distinct slope $\alpha$,

$$
\sum_{j:\alpha_j=\alpha}e_j=0.
$$

Consequently $\log R_m=O(\log m)$. In particular, such a divisor cannot
supply any positive exponential gcd rate.

The proposition applies to each of the adjacent rectangles
$(\lambda m,\mu m-1,\kappa m)$ and
$(\lambda m+1,\mu m-2,\kappa m+1)$ separately. Requiring a common
factorial divisor of both does not help.

## The exact valuation at a large prime

If $p^2>A+B+C$, write $a_0,b_0,c_0$ for the residues of $A,B,C$ modulo
$p$. Then

$$v_pG(A,B,C)=
 \begin{cases}
 1,&a_0+b_0+c_0\ge2p-1,\\
 0,&a_0+b_0+c_0\le2p-2.
 \end{cases}\tag{1}$$

Indeed each of the two binomial valuations is a single carry, since
all their factorial arguments are below $p^2$. For the second binomial
there is no carry precisely when the residue $y$ of $r$ obeys
$y\le p-b_0-1$.

If $y\le a_0$, the first binomial has no carry precisely when
$y\ge a_0+c_0-p+1$. When the residue sum is at most $2p-2$, choose

$$
r=y=\max(0,a_0+c_0-p+1).
$$

This satisfies $0\le r\le a_0\le A$ and makes both valuations zero.
When the residue sum is at least $2p-1$, the two inequalities are
incompatible. The other possibility, $y>a_0$, would require
$y\ge a_0+c_0+1$ to avoid the first carry, which is again incompatible
with $y\le p-b_0-1$. Thus every coefficient is divisible by $p$.
The coefficient at $r=0$ has valuation exactly one, proving (1).

Put $H=\lambda+\mu+\kappa$ and, away from its jump points, define

$$q(x)=\lfloor Hx\rfloor-\lfloor\lambda x\rfloor
                  -\lfloor\mu x\rfloor-\lfloor\kappa x\rfloor,
 \qquad f(x)=\mathbf1_{\{q(x)=2\}}.$$

For any fixed $x>0$ away from these jumps, take arbitrarily large primes
$p$ and integers $m$ with $m/p\to x$. Formula (1) gives

$$
v_pG(A_m,B_m,C_m)=f(x)\tag{2}
$$

for all sufficiently large $p$. All bounded shifts disappear in this
limit. This uses only the existence of arbitrarily large primes, not a
prime number estimate.

## Reflection forces the factorial expression to cancel

Stirling's formula and the bounds

$$1\le R_m\le G(A_m,B_m,C_m)
 \le\binom{A_m+C_m}{C_m}\le2^{A_m+C_m}$$

first imply the balance condition $\sum_j e_j\alpha_j=0$: otherwise
$\log R_m$ has a nonzero $m\log m$ term, contradicting one of these
bounds. Define its factorial valuation function

$$
L(x)=\sum_j e_j\lfloor\alpha_jx\rfloor.
$$

At any fixed $x>0$ away from all jump points, the same choice
$m/p\to x$ makes every factorial argument smaller than $p^2$.
Consequently $v_pR_m=L(x)$ for sufficiently large $p$. Divisibility
and (2) therefore imply

$$
0\le L(x)\le f(x).\tag{3}
$$

Choose a positive integer $T$ with $\alpha_jT\in\mathbf Z$ for all
$j$. Balance makes $L$ periodic with period $T$. At non-jump points
in $(0,T)$, the elementary floor identity gives

$$
L(x)+L(T-x)=-\sum_j e_j.\tag{4}
$$

Since $\lambda,\mu,\kappa$ are integers, the corresponding identity
for the gcd carry count is

$$
q(x)+q(T-x)=2.\tag{5}
$$

There is a nonempty interval

$$\frac1H<x<\min\left(\frac2H,
                  \frac1{\max(\lambda,\mu,\kappa)}\right)$$

on which $q(x)=1$. Choose $x$ in this interval avoiding the finitely
many jumps of $L$. Equations (3) and (5) force
$L(x)=L(T-x)=0$. Equation (4) now gives $\sum_j e_j=0$.
Applying (3) and (4) at every other non-jump point shows $L(x)=0$
throughout $(0,T)$ and hence everywhere away from jumps.

Finally combine equal slopes. If any combined coefficient remained
nonzero, let $\alpha$ be the largest such slope. At $x=1/\alpha$,
the function $\lfloor\alpha x\rfloor$ has its first jump, whereas
every smaller positive slope has no jump. Thus $L$ would have a
nonzero jump, a contradiction. Every slope therefore cancels.

For equal slopes, the factorial arguments differ by bounded integers.
Their ratios are products or reciprocals of a bounded number of
quantities of order $m$. This proves $\log R_m=O(\log m)$.

## Consequence for numerical source bounds

The obstruction is independent of the directions: it includes
$(255,58,255)$, $(35,8,35)$, and $(2,1,2)$ among the tight sources
for the remaining effective indices. A fixed factorial ratio cannot
replace their exponential prime-interval divisor. In particular,
searching for more such ratios cannot remove the need to control the
selected primes. Nonlinear constructions that select prime factors
can evade the reflection identity, but require a separate estimate.
