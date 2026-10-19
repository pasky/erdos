---
name: research/erdos_699/archive/other_approaches/multipoint_minor_divisibility
title: "Erdős 699: a common prime divisor of multipoint Padé minors"
desc: "A Frobenius calculation makes normalized integral rows proportional modulo primes in explicit intervals, supplying an additional exponential divisor of all two-by-two minors."
created: 2026-09-22T08:44:00Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: a common prime divisor of multipoint Padé minors

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/off_diagonal_pade|Unequal Padé blocks]]

This lemma supplies extra divisibility for a proposed simultaneous
approximation using three nearby integers. It is an arithmetic statement
about the approximation matrices. By itself it does not establish a new
cofactor bound or make another binomial index effective.

## Integral rows

Fix distinct integers $r_0,r_1,r_2<T$, positive integers $P_i$ dividing
$T-r_i$, and nonnegative exponents $A_0,A_1,A_2,D$. Set

$$f(x)=\prod_{i=0}^2(x-r_i)^{A_i}(x-T)^D,
\quad L=A_0+A_1+A_2+D,
\quad N=\frac{(L+1)!}{A_0!A_1!A_2!D!}.$$

Define $J_i=N\int_{r_i}^{T}f(x)\,dx$ and
$b_i=A_i+D+1$. Expansion after $x=r_i+(T-r_i)u$ shows that

$$
Z_i=J_i/P_i^{b_i}\in\mathbb Z.\tag{1}
$$

Indeed, expand the two remaining factors into powers of $u$. Every
coefficient involves a beta integral with denominator dividing the
factorial normalization $N$, and an overall factor $(T-r_i)^{b_i}$.

Let $M_L=\operatorname{lcm}(1,\ldots,L+1)$ and
$G=N/\gcd(N,M_L)$. Direct integration of the integer polynomial $f$
shows that $G$ divides every $J_i$. Remove from $G$ its factors supported
on primes dividing $P_0P_1P_2$, and denote the resulting integer by
$G^*$. Then

$$
V_i=Z_i/G^*\in\mathbb Z.\tag{2}
$$

Consider several rows obtained by bounded shifts of the exponents that
preserve all three $b_i$. In particular, the shifts

$$A_i\longmapsto A_i+k\quad(i=0,1,2),\qquad D\longmapsto D-k,
\quad k=0,1,2,\tag{3}$$

have this property when $D\ge2$. Their normalizations $N,G^*$ may differ.

## The rank-one prime criterion

**Lemma.** Let $p$ be a prime not dividing $P_0P_1P_2$. Suppose that for
every row under consideration:

1. $p^2>L+1$ and $p\nmid L+1$;
2. the four integers $\lfloor A_0/p\rfloor,\lfloor A_1/p\rfloor,
   \lfloor A_2/p\rfloor,\lfloor D/p\rfloor$ are the same across rows;
3. $\lfloor L/p\rfloor-\sum_{i=0}^2\lfloor A_i/p\rfloor
   -\lfloor D/p\rfloor=1$.

Then the matrix of normalized rows $(V_0,V_1,V_2)$ has rank at most one
over $\mathbb F_p$. In particular, $p$ divides every $2\times2$ minor.

**Proof.** Write the four exponents as $p a_j+c_j$, with
$0\le c_j<p$, using $r_3=T$. The floor hypotheses imply

$$f(x)\equiv F(x)^p R(x)\pmod p,
\qquad F(x)=\prod_{j=0}^3(x-r_j)^{a_j},
\quad R(x)=\prod_{j=0}^3(x-r_j)^{c_j},$$

where $F$ is the same for every row and $p\le\deg R<2p$.
Legendre's formula gives $v_p(N)=1$, since $p^2>L+1$ and
$p\nmid L+1$. Thus $p\nmid G^*$.

In the integral of $f(x)=\sum_s f_sx^s$, terms with $p\nmid s+1$
vanish modulo $p$ after multiplication by $N$. The remaining terms give

$$J_i\equiv\frac Np\sum_{a\ge1}\frac{f_{ap-1}}a
                 (T^{ap}-r_i^{ap})\pmod p.\tag{4}$$

Here every $a<p$, by $p^2>L+1$, so division by $a$ is legitimate.
In the product $F(x)^pR(x)$ the only degree of $R$ congruent to $-1$
modulo $p$ is $p-1$. If $c$ denotes its coefficient, then

$$
\sum_{a\ge1}f_{ap-1}x^{a-1}=cF(x)\quad\text{in }\mathbb F_p[x].
$$

Fermat's identity in (4) therefore gives

$$
J_i\equiv (N/p)c\int_{r_i}^{T}F(x)\,dx\pmod p.\tag{5}
$$

The integral on the right means formal polynomial integration over
$\mathbb F_p$; its denominators are invertible because
$\deg F+1<p$. After division by $G^*P_i^{b_i}$, all rows in (5) are
scalar multiples of the same vector

$$
\left(P_i^{-b_i}\int_{r_i}^{T}F(x)\,dx\right)_{i=0}^2.
$$

Some scalars or all vector entries may be zero; this only lowers the
rank. The conclusion follows. $\square$

Dividing each row by its *full* gcd is not justified in this lemma:
that could remove an extra factor of $p$ from a zero row and destroy
the rank-one conclusion. The specified divisor $G^*$ is essential to
the argument.

## A uniform exponential contribution

Suppose the four exponents have positive integer directions
$d_0,d_1,d_2,d_3$ times $m$, plus fixed bounded shifts, and put
$H=\sum d_j$. For a normalized prime size $x=p/m$ define

$$q(x)=\left\lfloor H/x\right\rfloor-
                   \sum_{j=0}^3\left\lfloor d_j/x\right\rfloor.$$

On any closed rational interval inside an open interval on which these
floors are constant and $q=1$, all hypotheses of the lemma hold for
every sufficiently large $m$, apart from finitely many fixed primes.
The threshold is computable. For finitely many disjoint such intervals
$(a_s,b_s)$ and any rational $\eta<\sum_s(b_s-a_s)$, the retained
effective prime-number estimates consequently give

$$\boxed{\gcd(\text{all two-by-two minors})\ge e^{\eta m}}
\tag{6}$$

above a computable threshold, whenever at least one minor is nonzero.
The statement can equivalently be made as divisibility by the product of
the interval primes, including when all minors vanish.

A simple contribution always comes from

$$
\max\{H/2,d_0,d_1,d_2,d_3\}<x<H,
$$

where all four individual floors are zero and the total floor is one.
For directions $(2,2,2,1)$ this interval is $(7/2,7)$, so every rate
$\eta<7/2$ is available from this interval alone. Other $q=1$ intervals
can add to it. This is divisibility of the minors in addition to the
individual-row divisors already removed in (2).
