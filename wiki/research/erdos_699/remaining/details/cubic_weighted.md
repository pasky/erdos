---
name: research/erdos_699/remaining/details/cubic_weighted
title: "Erdős 699: the critical certificate after removing the power of two"
desc: "The degree-2m polynomial through the five remaining congruence points is unique. This explains why discounting powers of n alone cannot repair the cubic fat-point argument."
created: 2026-09-21T21:51:33Z
updated: 2026-09-21T21:51:33Z
---

# Erdős 699: the critical certificate after removing the power of two

[[research/erdos_699/remaining/details/cubic_uniform|Uniform cubic proof attempt]] ·
[[research/erdos_699/remaining/details/cubic_followup|Earlier cubic reductions]]

***

For a hypothetical bad cubic triple, write

$$
n=2^h u,\qquad u\text{ odd},\qquad c=n-j.
$$

At an active odd prime-power component of $n-t$, the pair $(j,c)$
reduces to one of the integer points $(r,t-r)$, with $0\le r\le t$.
The six relevant points, for $t=0,1,2$, are therefore

$$
(0,0),\ (1,0),\ (0,1),\ (2,0),\ (1,1),\ (0,2).
$$

A possible improvement to the polynomial argument is to use a large power
of $X+Y$. At $(j,c)$ this factor is $n$, and its power of two can be
removed exactly. The following elementary result describes the critical
degree after doing so. It rules out a strict improvement by this particular
construction; it does **not** rule out a different proof of the cubic case.

## 1. The polynomial through the other five points is unique

Put

$$
L_1=X+Y-1,\qquad L_2=X+Y-2.
$$

**Lemma.** Let $m\ge1$, and let $H\in\mathbb Q[X,Y]$ be nonzero.
Suppose that $H$ vanishes to order at least $m$ at each of

$$
(1,0),\ (0,1),\ (2,0),\ (1,1),\ (0,2).
$$

Then $\deg H\ge2m$. If $\deg H=2m$, then

$$
H=\lambda(L_1L_2)^m\qquad(\lambda\in\mathbb Q\setminus\{0\}).
$$

**Proof.** Suppose $D=\deg H\le2m$. Remove the maximal powers of the two
line factors:

$$
H=L_1^aL_2^bG.
$$

Here $a,b\ge0$, neither $L_1$ nor $L_2$ divides $G$, and
$\deg G=D-a-b$. Restriction of $G$ to $L_1=0$ is a nonzero univariate
polynomial. Its two marked points have multiplicity at least
$\max(m-a,0)$, since $L_2$ is nonzero there. Restriction to $L_2=0$
similarly gives three points of multiplicity at least $\max(m-b,0)$.
Consequently

$$\begin{aligned}
D-a-b&\ge2\max(m-a,0),\\
D-a-b&\ge3\max(m-b,0).
\end{aligned}\tag{1}$$

If $a\ge m$ and $b<m$, the degree on the left is at most $m-b$, whereas
the second inequality requires at least $3(m-b)$, a contradiction.
Thus $a\ge m$ implies $b\ge m$. Since $a+b\le D\le2m$, this forces
$a=b=m$ and $D=2m$.

Likewise, if $b\ge m$ and $a<m$, the degree is at most $m-a$, contradicting
the first inequality. So $b\ge m$ gives the same conclusion.

In the remaining case $a,b<m$, inequalities (1) give

$$
a-b\ge2m-D\ge0,\qquad 2b-a\ge3m-D\ge m.
$$

The first says $a\ge b$, and the second therefore implies $b\ge m$,
contradicting the case assumption. The only possibility is
$a=b=m$, $D=2m$, and $G$ constant. This also proves that $D<2m$ is
impossible. $\square$

## 2. What removing the power of two achieves

Let $F$ vanish to order at least $m$ at all six points. Write

$$
F=(X+Y)^aH,
$$

where $a$ is maximal. The factor $X+Y$ is nonzero at the other five
points, so $H$ satisfies the lemma. At evaluation,

$$
\frac{F(j,c)}{2^{ha}}=u^aH(j,c).\tag{2}
$$

Thus, when the factor $2^{ha}$ is removed in this way, the remaining
degree in $n$ is at least $2m$. At the critical degree $\deg H=2m$,
the lemma forces

$$
F=\lambda(X+Y)^a\bigl((X+Y-1)(X+Y-2)\bigr)^m.
$$

Since $H(0,0)=\lambda2^m\ne0$, the multiplicity at the origin also
forces $a\ge m$. Formula (2) becomes

$$\frac{F(j,c)}{2^{ha}}
=\lambda u^a(n-1)^m(n-2)^m.\tag{3}$$

There is no dependence on $j$. For the minimal choice $a=m$, this is a
scalar multiple of the very odd part whose divisibility the argument is
using:

$$u^m(n-1)^m(n-2)^m=(6W)^m,
\qquad W=\frac{u(n-1)(n-2)}6.$$

For example, normalizing $F$ by $6^{-m}$ gives exactly $W^m$ after
removing $2^{hm}$. It gives an identity, with no strict inequality to
contradict integrality. Additional powers $a>m$ only insert the factor
$u^{a-m}$ into this identity.

The conclusion is specific: uniform multiplicity $m$ at these six points,
with only powers of $X+Y$ discounted by their known power of two, cannot
produce a remaining degree below $2m$. At degree $2m$, the certificate is
forced to be independent of the column. This does not address constructions
using different local conditions, cancellation beyond that explicit factor,
or the higher Lucas digits. It supplies no finiteness theorem for bad
cubic triples.
