---
name: research/erdos_699/archive/other_approaches/cubic_descent
title: "Erdős 699: the two-descent class of the marked elliptic point"
desc: "An explicit Kummer class and a uniform local obstruction to halving the marked point. This does not exclude bad triples or prove global finiteness."
created: 2026-09-21T23:49:43Z
updated: 2026-09-22T19:12:28Z
---

# Erdős 699: the two-descent class of the marked elliptic point

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/remaining/details/cubic_elliptic|The elliptic curves]] ·
[[research/erdos_699/remaining/details/cubic_irreducibility|The irreducible cubic]]

The marked point arising from a hypothetical bad triple has an explicit
two-descent class. In many cases this class is already nontrivial over
$\mathbb Q_2$. This prevents halving the point; it does not prevent the
point, or the hypothetical triple, from existing. Global nonexistence and
global finiteness remain unproved.

## 1. The class in the cubic field

Retain the notation from the elliptic note:

$$P(z)=az^3+bz^2+ez+f,\qquad P(1)=2^m,\qquad
m=h-t,\quad \epsilon\equiv m\pmod2,\quad D=2^\epsilon.$$

Here $a,b,e,f$ are positive integers, $P$ is irreducible, and
$P'(1)$ is odd. On $E_D:y^2=DP(z)$ the marked point is

$$
Q=(1,2^{(m+\epsilon)/2}).
$$

Let $\alpha$ be a root of $P$ and $K=\mathbb Q(\alpha)$. The integral
monic model obtained by $X=Da z$, $Y=Da y$ is

$$
Y^2=X^3+DbX^2+D^2aeX+D^3a^2f.
$$

Its corresponding cubic root is $\theta=Da\alpha$. The usual Kummer
map has kernel $2E_D(\mathbb Q)$ and sends $(X,Y)$ to the square class
of $X-\theta$. Consequently

$$
\delta(Q)=[Da(1-\alpha)]\in K^\times/K^{\times2}.\tag{1}
$$

This description of the descent map is given in
[Michael Stoll's explanation of explicit two-descent](https://mathoverflow.net/questions/222538/explicit-2-descent-on-elliptic-curves).

We can express (1) in the field defined by
$H(w)=w^3-kw+2q$. Put $C=c/2^t$ and let $\beta$ be the root corresponding
to $\alpha$. The earlier change of variable gives

$$\alpha=\frac{2^t\beta-j}{2^t\beta+c},\qquad
1-\alpha=\frac{2^m u}{\beta+C}.$$

Since $D2^m$ is a rational square, (1) becomes

$$
\boxed{\delta(Q)=[au(\beta+C)].}\tag{2}
$$

Indeed, it first becomes $[au/(\beta+C)]$, and the two representatives
differ by the square $(\beta+C)^2$. The leading coefficient is

$$
a=\frac{c(c-1)(c-2)}{2^t u(n-1)(n-2)},
$$

so the identity for $H(-C)$ gives

$$
N_{K/\mathbb Q}(\beta+C)=-H(-C)=2^{2m}u^3a.
$$

In particular,

$$N_{K/\mathbb Q}\bigl(au(\beta+C)\bigr)
=2^{2m}a^4u^6.\tag{3}$$

Thus the square-norm condition in two-descent is automatic.

## 2. A local obstruction to halving

**Theorem.** Suppose either $t\ge3$, or $t\ge2$ and $m$ is odd.
Then $Q\notin2E_D(\mathbb Q_2)$, and hence
$Q\notin2E_D(\mathbb Q)$.

**Proof.** For $t\ge2$, the exact coefficient valuations give $a,f$ odd
and $b,e$ even. Thus

$$
P(z)\equiv z^3+1=(z+1)(z^2+z+1)\pmod2.
$$

These factors are separable and coprime. It follows that
$K\otimes\mathbb Q_2\cong\mathbb Q_2\times L$, where
$L/\mathbb Q_2$ is the unramified quadratic extension. Let $\alpha$ now
denote the root belonging to $L$. Both $\alpha$ and $1-\alpha$ are units.

If $m$ is odd, then $D=2$ and $Da(1-\alpha)$ has valuation one in $L$.
It is not a square, so (1) obstructs halving.

Suppose instead that $m$ is even and $t\ge3$. Put $J=j/2^t$, so
$J+C=2^m u$. Direct reduction of the coefficient formulas modulo four
gives

$$
a\equiv C/u,\qquad f\equiv J/u,\qquad b\equiv e\equiv0\pmod4.
$$

Since $m\ge2$, this yields $P(z)\equiv a(z^3-1)\pmod4$.
The element $\alpha-1$ is a unit in $L$, so

$$
\alpha^2+\alpha+1\equiv0\pmod4.
$$

If $a(1-\alpha)$ were a square, a square root would reduce to
$\alpha$ modulo two: in the residue field $\mathbb F_4$,
$1-\alpha=\alpha^2$, and squaring is bijective. Its square modulo four
would therefore be $\alpha^2$. However,

$$a(1-\alpha)-\alpha^2
\equiv(a+1)+(1-a)\alpha
\equiv\begin{cases}2,&a\equiv1\pmod4,\\
2\alpha,&a\equiv3\pmod4.
\end{cases}$$

Both are nonzero modulo four. Thus the class in (1) is nontrivial over
$L$, proving the theorem. $\square$

This theorem identifies a nonzero class in the Mordell--Weil group modulo
two. It supplies no upper bound on the rank or on $n$. No assertion about
halving is made here for the remaining cases.

## 3. Why the transported class is not an obstruction

The same class has a rational-point representative on a twist of the
monic cubic. Namely,

$$
E':y^2=-auH(w)
$$

has the point $Q'=(-C,2^m a u^2)$, because
$H(-C)=-2^{2m}u^3a$. If $B=-au$, the monic coordinates for this curve
are $X=Bw$, $Y=By$, with cubic root $B\beta$. Its Kummer class at $Q'$
is exactly

$$
[B(-C-\beta)]=[au(\beta+C)].
$$

Thus transporting (2) through the shared two-torsion does not produce
a class lacking a rational-point representative. The twist factor $au$
varies with the original parameters. Neither (3) nor the local theorem
controls the remaining Selmer classes or the varying cubic fields.
An additional uniform restriction is needed to turn this descent into
nonexistence or a globally finite exceptional set.
