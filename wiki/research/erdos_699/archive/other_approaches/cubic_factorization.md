---
name: research/erdos_699/archive/other_approaches/cubic_factorization
title: "Erdős 699: an integer factorization of the cubic discriminant"
desc: "A uniform factorization, including the canceled factor of three, identifies the odd conductor exactly away from 6. The resulting equations have no positive integral descent by the displayed coordinate Vieta mutations."
created: 2026-09-22T00:15:05Z
updated: 2026-09-22T00:15:05Z
---

# Erdős 699: an integer factorization of the cubic discriminant

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/remaining/details/cubic_conductor|The conductor normalization]] ·
[[research/erdos_699/remaining/details/cubic_irreducibility|The integer cubics]]

The endpoint conditions give a factorization of the cubic discriminant
into a square and one additional integer. It applies to every hypothetical
bad triple, including the cases with a canceled factor of three. In the
hard subcase $n=2^h$, $j$ odd, the equations resemble equations suited to
Vieta descent, but their natural coordinate mutations fail to give a
smaller positive integral solution. No global finiteness result follows.

## 1. The factorization for all hypothetical bad triples

Use the established notation

$$n=2^h u,\quad c=n-j,\quad d=n-2j,\quad
t=v_2(j)=v_2(c),\quad m=h-t\ge2,$$

where $u$ is odd, $4\le j<n/2$, and $d^2>3n-2$. Put

$$K=\frac{jc}{n-1},\quad M=\frac{n-2}{2},\quad
g=\gcd(u,3),\quad v=u/g.$$

Since $3K=2^{2t}k$ is an integer, the reduced denominator $\lambda$ of
$K$ belongs to $\{1,3\}$. Write $\kappa=\lambda K$. If $\lambda=3$,
then $3\mid n-1$, so $3\nmid uM$ and $3\nmid\kappa$. Consequently

$$
\gcd(\kappa,\kappa-\lambda)=1,\qquad \gcd(\lambda,M)=1.
$$

**Lemma.** There are unique coprime positive integers $A,B$ such that

$$
M=AB,\qquad A\mid\kappa,\qquad B^2\mid\kappa-\lambda,
$$

where $A$ contains exactly the prime-power factors of $M$ whose primes
divide $\kappa$.

**Proof.** For every $p^a\Vert M$, the endpoint conditions give
$j\bmod p^a\in\{0,1,2\}$. The only possibly inactive prime is $p=3,a=1$;
the same assertion then holds without a restriction. If $j\equiv0$ or
$2\pmod{p^a}$, then $p^a\mid jc$, hence $p^a\mid\kappa$. If
$j\equiv1\pmod{p^a}$, both $j-1$ and $c-1$ are divisible by $p^a$.
Using

$$
K-1=\frac{(j-1)(c-1)}{n-1}
$$

gives $p^{2a}\mid\kappa-\lambda$. Here $p\nmid\lambda(n-1)$.
Coprimality of $\kappa$ and $\kappa-\lambda$ makes the alternatives
disjoint and proves the assertion. $\square$

Write $\kappa=A R$, $\kappa-\lambda=B^2s$, and $e=d/2$. Both
$A,B$ are odd, $v_2(R)=2t$, and $v_2(e)=t$. The identity

$$
q=\frac{\kappa e}{\lambda2^{3t}M}
$$

and $\gcd(B,R)=1$ imply $B\mid e$. Also $v\mid j,c,e$ and
$\gcd(v,M)=1$. The denominators in $K$ are coprime to $v$, so
$v^2\mid R$. Thus positive odd integers $r,f$ are defined by

$$
R=2^{2t}v^2r,\qquad e=2^tBvf.
$$

The resulting exact equations are

$$\begin{aligned}
AB+1&=2^{h-1}u,\\
2^{2t}v^2Ar-B^2s&=\lambda,\\
\lambda2^{2t}v^2f^2&=\lambda A^2-s(2AB+1).
\end{aligned}\tag{1}$$

For the last equation, use $e^2=(M+1)^2-K(2M+1)$.
Eliminating $B^2s$ from (1) gives

$$
A^3r-\lambda f^2=2^{2m-2}g^2s.\tag{2}
$$

The normalized curve from the conductor note therefore has

$$k_0=\frac{3Ar}{\lambda},\qquad q_0=\frac{rf}{\lambda},\qquad
E_0:\ y^2=x^3-k_0x+2q_0.\tag{3}$$

These coefficients are integers. In particular, when $\lambda=3$,
one has $3\nmid Ar$ and $3\mid f$.

The exact cubic discriminant factorization is

$$
\boxed{\operatorname{Disc}P=\frac{27r^2s}{\lambda^3g^4}.}\tag{4}
$$

Indeed, the earlier discriminant formula is
$\operatorname{Disc}P=27K^2(K-1)/(2^{4t}u^4M^2)$, and substitution
gives (4). The only denominator in (4) is a power of three; its
integrality is already supplied by $P\in\mathbb Z[z]$.

The same equations give
$\gcd(Ar,s)=\gcd(B,r)=\gcd(A,f)=\gcd(s,f)=1$.
Equation (2) shows that every common prime divisor of $r,f$ divides
$3$: any such prime must divide $g$ or $\lambda$, and $\lambda=3$
excludes $3\mid r$. Finally, $d^2>3n-2$ gives $K<M/2$, hence

$$
r<\frac{\lambda B}{2^{2t+1}v^2}.\tag{5}
$$

## 2. The odd conductor away from six

For $p\ge5$ dividing $s$, (2)--(3) give
$v_p(c_4)=0$ and $v_p(\Delta)=v_p(s)$: the reduction is multiplicative,
with conductor exponent one.

For $p\ge5$ dividing $r$, put $a=v_p(r)$. The coprimalities above give

$$v_p(c_4)=a+v_p(A),\qquad v_p(c_6)=a,\qquad
v_p(\Delta)=2a.$$

Write $a=6b+d$ with $0\le d<6$. Scaling the Weierstrass coordinates
by $p^{2b},p^{3b}$ gives valuations $2b+d+v_p(A),d,2d$.
This model is minimal, since its constant coefficient has valuation
$d<6$. It has good reduction for $d=0$ and additive reduction otherwise.
At $p\ge5$ the latter has conductor exponent two. Thus, exactly,

$$N(E_0)_{\{2,3\}'}
=\prod_{\substack{p\ge5\\p\mid s}}p
\cdot\prod_{\substack{p\ge5\\p\mid r\\6\nmid v_p(r)}}p^2.\tag{6}$$

The subscript removes the prime factors two and three. These are the standard local conductor
rules used in the [conductor note](../../remaining/details/cubic_conductor.md).
In particular, if $r,s$ are squarefree away from six, their contribution
has the full size $r^2s$ away from six. The endpoint equations alone have
not forced repeated prime factors that would improve this bound.

## 3. Coordinate Vieta mutations in the hard subcase

Now assume $u=1,t=0$. Thus $g=v=1$, $h\ge4$, and (1) simplifies to

$$AB+1=2^{h-1},\quad Ar-B^2s=\lambda,\quad
\lambda f^2=\lambda A^2-s(2AB+1),\qquad r<\lambda B/2.\tag{7}$$

This includes both $\lambda=1$ and the canceled case $\lambda=3$.
All of $A,B,r,f$ are odd. Reduction modulo eight shows
$8\mid s$ and $r\equiv-\lambda B\pmod8$. These conditions and
$r<\lambda B/2$ exclude $B=1$. Also $A>2Bs/\lambda$.

Eliminating $s$ gives the quadratic in $A$

$$B(\lambda B-2r)A^2+(2\lambda B-r)A
+\lambda-\lambda B^2f^2=0.\tag{8}$$

The second root is

$$
A'=-A-\frac{2\lambda B-r}{B(\lambda B-2r)}.
$$

It is never integral: $\gcd(B,r)=1$ makes the fraction's numerator
coprime to $B>1$. Holding $A,r,f$ fixed instead gives the quadratic

$$
\lambda(A^2-f^2)B^2-2A(Ar-\lambda)B-(Ar-\lambda)=0,
$$

whose second root is $B'=-B/(2AB+1)\in(-1,0)$, also nonintegral.

The other two coordinate choices do not give positive solutions.
Eliminating $A$ and regarding the result as a quadratic in $r$ gives
the second root

$$
r'=-\frac{\lambda Ar}{\lambda A-2Bs}<0.
$$

Regarding it as a quadratic in $s$ gives

$$s'=\frac{\lambda(\lambda^2-r^2f^2)}
{B^3(\lambda B-2r)s}\le0,$$

because $rf/\lambda=q_0$ is a positive integer. Changing the sign of
$f$ exchanges $j,c$. Thus these coordinate root exchanges do not give
a descent among positive admissible tuples. This does not exclude
other transformations or an argument using higher Lucas digits.

The factorization and the conductor formula are uniform necessary
conditions. They do not prove that arbitrary positive solutions of
(1) satisfy all the original Lucas conditions, nor do they bound
$r^2s$. A restriction on these factors beyond (1)--(5) is still needed
to obtain a contradiction or global finiteness.

## 4. Splitting the two outer residue groups

The [residue-group proof](../../remaining/details/cubic_residue_groups.md)
excludes an empty outer group by a small square identity. Here is its
extension when both outer groups are present. Write
$U=C_0$, $V=C_2$, $B=C_1$, so $A=UV$, and use the unnormalized
$R$ from Section 1:

$$
UVR-B^2s=\lambda.
$$

Set $j=Ua$, $c=Ub+2$, where $a,b>0$ and $a+b=2BV$. The same
elimination as in the empty-group proof gives

$$
D=2BV^2R-\lambda ab,\qquad UD=2\lambda a-VR>0,
$$

and

$$
[VR-\lambda(a-BV)]^2=B^2(\lambda^2V^2-Ds).
$$

Positivity follows from $VR=\lambda ac/(n-1)<\lambda a$. Since
a rational square root of an integer is integral, there is an integer
$z$ with

$$
Ds=\lambda^2V^2-z^2,\qquad |z|<\lambda V.
$$

When $V=1$, this restricts $Ds$ to the short list used in the proof.
For variable $V$, the list grows with $V^2$. Thus this extension of
the identity does not give a uniform bound when all three groups grow.
