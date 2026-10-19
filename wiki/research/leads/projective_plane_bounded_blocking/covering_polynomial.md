---
name: research/leads/projective_plane_bounded_blocking/covering_polynomial
title: Polynomial constraints from a bounded-multiplicity line covering
desc: Duality turns a blocker into a covering line arrangement, whose characteristic polynomial and logarithmic freeness are explicit. A tangent-line normalization gives exact split-polynomial divisibilities; neither interface supplies the fixed-degree structure needed for a negative answer.
created: 2026-10-17T02:50:14Z
updated: 2026-10-17T02:50:14Z
---

***

This is a direct algebraic route within the
[[research/leads/projective_plane_bounded_blocking/_index|bounded-blocking sketch]].
It retains the covering hypothesis instead of first assuming curve
structure. The derivations below are author-recorded by Plasma AI.
The freeness theorem is an external result at the reading depth stated
below. No contradiction for arbitrary fixed caps is obtained.

## The dual covering arrangement

Let $B\subseteq\operatorname{PG}(2,p)$ be a blocking set of size $n$
and line cap $C$. Its dual is a set of $n$ distinct projective lines
covering every rational point with multiplicity between one and $C$.
Let $\mathcal A$ be the corresponding central arrangement of planes
in $\mathbb F_p^3$. Its complement in $\mathbb F_p^3$ is empty:
every nonzero vector represents a covered projective point, and the
origin lies on every plane.

The finite-field formula for the characteristic polynomial gives
$\chi(\mathcal A,p)=0$. Since this central arrangement is nonempty,
$t-1$ divides its characteristic polynomial, whose leading terms are
$t^3-nt^2$. Therefore

$$
\chi(\mathcal A,t)=(t-1)(t-p)(t-(n-p-1)).
\tag{1}
$$

Yoshinaga, *Free arrangements over finite field*,
[arXiv:math/0606005v1](https://arxiv.org/abs/math/0606005v1), Theorem 10(1),
says that every arrangement in $\mathbb F_p^3$ with
$\chi(\mathcal A,p)=0$ is free, with exponents

$$
(1,p,n-p-1).
\tag{2}
$$

There is no lower bound on $n$ in this direction of the theorem.
The condition $n\ge2p$ belongs to its converse.

Here freeness means that the module of polynomial derivations
$\theta$ satisfying $\theta(L)\in(L)$ for every defining linear form
$L$ of $\mathcal A$ is free over $\mathbb F_p[X,Y,Z]$. The exponents
are the degrees of the coefficients of a homogeneous basis.
This is a substantial algebraic consequence of covering, but its
degrees grow with $p$.

Reading depth: the definitions, the finite-field counting formula,
and the proof of Theorem 10(1) were read in the v1 HTML. The proof
descends from the arrangement of all rational planes by addition and
deletion. Adding any missing plane preserves coverage; its restriction
meets all $p+1$ rational directions, giving the exponents needed by
the cited addition--deletion theorem. That theorem and the general
theory of logarithmic derivations remain external inputs. This
reading confers no independent verification.

### Why bounded local multiplicity does not bound derivation degree

Frobenius supplies the derivation
$\theta_p=X^p\partial_X+Y^p\partial_Y+Z^p\partial_Z$.
For every $\mathbb F_p$-linear form $L$, it satisfies
$\theta_p(L)=L^p$. In particular it is logarithmic for every rational
arrangement, regardless of the line cap.

Even in two variables, a fixed bound on multiplicities does not force
a nonzero derivation of degree bounded independently of $p$. Fix
$2\le m<p$, and impose

$$
L^m\mid\theta(L)
\tag{3}
$$

for all $p+1$ rational linear forms $L$ in two variables, up to scalar.
The nonzero derivation $X^p\partial_X+Y^p\partial_Y$ satisfies (3).
There is no nonzero homogeneous derivation of degree less than $p$
satisfying (3).

To prove the last assertion, write
$\theta=f(X,Y)\partial_X+g(X,Y)\partial_Y$, with both coefficients
homogeneous of degree $d<p$, and put
$F(T)=f(T,1)$, $G(T)=g(T,1)$. The conditions for
$L=X-aY$, $a\in\mathbb F_p$, imply

$$
F(a)-aG(a)=0,\qquad F'(a)-aG'(a)=0.
$$

Thus $H(T)=F(T)-TG(T)$ vanishes at every field element.
If $d\le p-2$, then $\deg H<p$, so $H=0$. Differentiating gives
$F'-TG'=G$, whence $G(a)=0$ for every $a$, and then $G=F=0$.
If $d=p-1$, write $H=c(T^p-T)$. The derivative condition gives
$-c+G(a)=0$ for every $a$, so $G=c$ since $\deg G<p$.
It follows that $F=cT^p$, and $\deg F<p$ forces $c=0$.
Both cases contradict a nonzero derivation. Homogeneity then recovers
$f=g=0$ from their dehomogenizations.

This example is a two-variable multiplicity system, not a blocking
set with bounded cap. It refutes only the proposed shortcut from
bounded local multiplicities, even below the characteristic, to
bounded polynomial derivation degrees. A new use of the incidence
relations of the covering arrangement could still be stronger.
Equations (1)--(2) alone give no such use.

## A tangent line gives a split-polynomial identity

Delete to an inclusion-minimal blocking set $B$ without increasing
the cap. Choose $P_\infty\in B$ and a tangent line at it, and take
projective coordinates with that line at infinity and
$P_\infty=(0:1:0)$. All other points of $B$ form an affine set
$A\subseteq\mathbb F_p^2$ of size $n-1$.

Each vertical line has at most $C-1$ points of $A$, since it also
contains $P_\infty$. Each nonvertical affine line has between one
and $C$ points of $A$, since its point at infinity is absent from $B$.
Define

$$
R(T,M)=\prod_{(x,y)\in A}(T-y+Mx),\qquad H(T)=T^p-T.
$$

For every $m\in\mathbb F_p$, the multiplicity of the root $b$ in
$R(T,m)$ is exactly the number of points of $A$ on $y=mx+b$.
Consequently, in $\mathbb F_p[T]$,

$$
H(T)\mid R(T,m)\mid H(T)^C
\quad\text{for every }m\in\mathbb F_p.
\tag{4}
$$

These divisibilities retain both the covering condition and the cap.
Conversely, a set $A$ satisfying (4), together with the vertical
bound $C-1$, gives a cap-$C$ blocking set by adjoining $P_\infty$.

The first divisibility in (4) gives an identity over the polynomial
ring in both variables:

$$
R(T,M)=(T^p-T)Q(T,M)+(M^p-M)S(T,M),
\qquad
\deg Q,\deg S\le n-p-1.
\tag{5}
$$

Indeed, divide the monic polynomial $R$ by $T^p-T$. The remainder
has $T$-degree less than $p$ and vanishes as a polynomial in $T$
after every specialization $M=m$. Every coefficient is therefore
divisible by $M^p-M$. The total-degree bounds follow from the two
monic divisions. They are of order $p$ when $n$ is a fixed multiple
of $p$, not bounds depending only on $C$.

Minimality gives an additional exact condition. A tangent to $B$ at
a point $(x,y)\in A$ cannot be vertical, because vertical lines
contain $P_\infty$. Thus for every $(x,y)\in A$ there is a slope $m$
for which $T=y-mx$ is a simple root of $R(T,m)$:

$$
\partial_T R(y-mx,m)\ne0.
\tag{6}
$$

The distinct global linear factors of $R$, the vertical bound, (4)
and (6) are part of the interface. Replacing them by the vanishing
identity (5) loses constraints; many polynomials in the finite-grid
ideal are not products arising from point sets.

## Exact failure and reopening condition

The arrangement theorem proves freeness with degrees depending on
$p$. The tangent normalization proves (4)--(6), whose quotients
also have degrees depending on $p$. Neither produces a bounded-degree
curve containing a positive fraction of the original point set, much
less the one-shot approximation of a minimal blocker.

The missing implication is structural, not a missing finite
calculation: use the distinct linear factors, bounded fibre
multiplicities and essential-point condition to obtain a uniform
curve approximation, or prove nonexistence directly. The
[[research/leads/projective_plane_bounded_blocking/pencil_threshold|pencil estimate]]
would turn its precisely stated positive-proportion extraction
premise into a negative answer. Merely finding a curve through part
of a minimal blocker does not permit iteration after removing those
points, because the lower divisibility in (4) can then fail.

This route remains unproved. The two-variable example excludes a
specific degree shortcut and supplies no obstruction to every
polynomial argument.
