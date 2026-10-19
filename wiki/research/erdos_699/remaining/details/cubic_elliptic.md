---
name: research/erdos_699/remaining/details/cubic_elliptic
title: "Erdős 699: elliptic curves attached to the cubic"
desc: "A hypothetical cubic counterexample forces an explicit point of infinite order on one of two twists. The correct quartic transformation and varying primes of bad reduction delimit the finiteness argument."
created: 2026-09-21T23:37:17Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: elliptic curves attached to the cubic

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[[research/erdos_699/remaining/details/cubic_irreducibility|The irreducible cubic]]

***

The elliptic interpretation gives a uniform theorem: every hypothetical
bad triple forces an explicit point of infinite order on a specified
quadratic twist of the coefficient cubic. There is also an important
distinction between the two cubics in the earlier note: the rational
change between their roots does not give an isomorphism of their elliptic
curves. These observations do not prove nonexistence or global
finiteness of bad triples.

The subsequent [two-descent calculation](../../archive/other_approaches/cubic_descent.md)
identifies the marked point's square class and proves local nondivisibility
by two in a broad range. The [conductor argument](cubic_conductor.md)
removes an odd twist and bounds the conductor by a constant times
$\operatorname{Disc}P$. This makes a uniform bound on that integer a
sufficient effective finiteness target, but no such bound is established.
The [multiplication calculation](../../archive/other_approaches/cubic_multiplication.md)
also reconstructs the parameters after doubling or tripling the point:
doubling always loses row integrality, whereas tripling preserves the
valuations at two and leaves a question about odd denominators.

Two further results bear on this. The
[curve finiteness theorem](cubic_curves.md) uses the
discriminant identity over a polynomial ring to show that every fixed
algebraic curve in the $(n,j)$-plane contains only finitely many bad pairs,
even with the odd part of $n$ varying. Thus a global nondensity theorem
would suffice, but none has been proved. The
[section calculation](../../archive/other_approaches/cubic_sections.md) determines
the rational sections of the fixed-row elliptic family: the known point
generates them. This statement does not control additional points on
individual specialized curves.

## 1. Notation

Assume no odd prime divides both $\binom n3$ and $\binom nj$, where
$4\le j<n/2$. Use the established notation

$$n=2^h u,\quad c=n-j,\quad t=v_2(j)=v_2(c),\quad
m=h-t\ge2,\quad W=\frac{u(n-1)(n-2)}6.$$

Here $u$ and $W$ are odd. The preceding note proves that

$$P(z)=\frac{1}{2^tW}
\sum_{r=0}^3\binom j{3-r}\binom cr z^r
=az^3+bz^2+ez+f\in\mathbb Z[z]$$

is irreducible, has three distinct roots in $(-1,0)$, and satisfies

$$
P(1)=2^m,\qquad P'(1)\text{ odd}.\tag{1}
$$

It also supplies the monic irreducible cubic

$$H(w)=w^3-kw+2q,\qquad
k=\frac{3jc}{2^{2t}(n-1)},\quad
q=\frac{jc(c-j)}{2^{3t}(n-1)(n-2)},\tag{2}$$

with positive odd integers $k,q$.

## 2. A point of infinite order

Let $\epsilon\in\{0,1\}$ be the parity of $m$, and put $D=2^\epsilon$.
Consider

$$
E_D:\quad y^2=DP(z).
$$

Its nonsingular projective completion is an elliptic curve, with its
unique point at infinity as identity. It has the rational point

$$
Q=\left(1,2^{(m+\epsilon)/2}\right).\tag{3}
$$

**Theorem.** The point $Q$ has infinite order. In particular,
$\operatorname{rank}E_D(\mathbb Q)\ge1$. Moreover,
$E_D(\mathbb Q)[2]=0$.

**Proof.** The change $X=Da z$, $Y=Da y$ gives the integral monic model

$$
Y^2=X^3+DbX^2+D^2aeX+D^3a^2f.\tag{4}
$$

At the image of $Q$, the tangent slope is
$DP'(1)/(2y(Q))$. Therefore the doubling formula gives

$$
X(2Q)=\frac{DP'(1)^2}{4P(1)}-Db-2Da.\tag{5}
$$

The first term has two-adic valuation $\epsilon-m-2<0$, while the
remaining terms are integers. Thus

$$
v_2\bigl(X(2Q)\bigr)=\epsilon-m-2<0.\tag{6}
$$

Rational torsion points on an integral equation of the form (4) have
integer coordinates, by Nagell–Lutz. Consequently $2Q$, and hence $Q$,
cannot be torsion. A nonzero rational point of order two would give a
rational root of $P$, contrary to irreducibility. $\square$

The version of Nagell–Lutz used here is stated explicitly in
[Silverman's answer on integral coordinates of torsion points](https://mathoverflow.net/questions/392929/torsion-points-on-e-mathbbq-with-large-coordinates).

The rational point itself is not an obstruction. If $T=\binom n3$ and
$R=2^tWP$, the curve $v^2=TR(z)$ always has $(z,v)=(1,T)$, even without
badness. Under our hypotheses it is isomorphic to $E_D$: the ratio
$TR/(DP)=2^{h+t-\epsilon}W^2$ is a rational square. The theorem adds the
infinite-order conclusion using the coefficient integrality and (1).

Thus a rank-zero result for this *specified* twist of a candidate family
would exclude that family. Merely constructing the point does not settle
the original problem.

## 3. The monic substitution gives a quartic

The earlier identity is

$$P(z)=\frac{2^{2t}(1-z)^3}{un^2}
H\!\left(\frac{j+cz}{2^t(1-z)}\right).\tag{7}$$

Its multiplier depends on $z$ through an odd power. It cannot simply be
absorbed into the square of an elliptic ordinate.

Set

$$w=\frac{j+cz}{2^t(1-z)},\qquad C=\frac c{2^t},\qquad
z=\frac{2^tw-j}{2^tw+c}.$$

Substitution in (7), using $n=2^hu$, gives

$$
P(z)(2^tw+c)^4=2^{h+3t}(w+C)H(w).
$$

Since $h+3t+\epsilon$ is even, the change

$$
V=\frac{y(2^tw+c)^2}{2^{(h+3t+\epsilon)/2}}
$$

identifies $E_D$ birationally with

$$
V^2=(w+C)H(w).\tag{8}
$$

This quartic is nonsingular: $H$ has distinct roots, and

$$H(-C)=-\frac{n^2c(c-1)(c-2)}
{2^{3t}(n-1)(n-2)}\ne0.$$

The branch point $w=-C$ corresponds to the original identity at infinity.
The two rational points at infinity of the quartic correspond to $Q$ and
$-Q$. Thus (8) carries the positive-rank conclusion. The different curve
$E_H:v^2=H(w)$ does not inherit that conclusion from this argument.

For another check on the distinction, write $\mathfrak j$ for the elliptic
$j$-invariant, to distinguish it from the column index. Direct calculation
gives

$$\mathfrak j(E_D)=
\frac{1728jc^2(n-2)}{(j-1)(n-1)(c-2)^2},\tag{9}$$

whereas

$$\mathfrak j(E_H)=\frac{1728k^3}{k^3-27q^2}
=\frac{1728jc(n-2)^2}{n^2(j-1)(c-1)}.\tag{10}$$

These are different rational functions. The two curves do have isomorphic
Galois modules of two-torsion: (7) identifies their three nonzero
two-torsion points equivariantly through the corresponding cubic roots.
That is weaker than an isomorphism of elliptic curves.

## 4. What the monic elliptic curve says about bad reduction

For $E_H:v^2=w^3-kw+2q$, the standard invariants are

$$c_4=48k,\qquad c_6=-1728q,\qquad
\Delta_H=64(k^3-27q^2).$$

In our parameters this becomes

$$\Delta_H=
\frac{1728j^2c^2n^2(j-1)(c-1)}
{2^{6t}(n-1)^3(n-2)^2}.\tag{11}$$

Let $p$ be a prime not dividing $6n(n-1)(n-2)$, and suppose
$e_p=v_p(j-1)>0$. Then $j\equiv1\pmod p$ and
$c\equiv n-1\not\equiv0\pmod p$, so $v_p(k)=0$. Also
$c-1\equiv n-2\not\equiv0\pmod p$. It follows that

$$
v_p(c_4)=0,\qquad v_p(\Delta_H)=e_p.
$$

The equation is minimal at $p$, with multiplicative reduction of type
$I_{e_p}$; its conductor contains $p$ to exponent one. The same statement
holds with $j-1$ replaced by $c-1$. This uses the usual
[minimal-model reduction criterion](https://websites.umich.edu/~asnowden/teaching/2013/679/L08.html).

These primes also survive on the coefficient curve. Put $L=2^tW$. The
model (4) with $D=1$ has

$$c_4=\frac{4jc^2(c-1)(n-2)}{L^2},\qquad
\Delta=16a^2\operatorname{Disc}P.$$

At the same prime $p\mid j-1$, its $c_4$ is a unit and

$$
v_p(\Delta)=e_p+2v_p(c-2)>0.
$$

Twisting by $D\in\{1,2\}$ does not change these valuations at odd $p$.
Thus neither choice of elliptic curve removes the varying primes from
the column factors.

For an additional exact calculation at two, if $t\ge1$, then the formula
for $\operatorname{Disc}P$ in the preceding note gives

$$v_2(\operatorname{Disc}P)=0,\quad
v_2(\Delta_H)=2m+4,\quad
v_2(\mathfrak j(E_H))=8-2m.\tag{12}$$

The discriminant valuation in (12) is for the displayed equation;
minimalization can change it. These large powers of two alone are not a
contradiction.

There is an explicit minimal model illustrating this. Suppose $t\ge1$
and $m\ge4$, put $J=j/2^t$, and choose $\eta\in\{1,-1\}$ so that
$r=\eta J\equiv3\pmod4$. On the curve

$$
v^2=w^3-kw+2\eta q
$$

(either $E_H$ or its twist by $-1$), set $w=4X+r$, $v=8Y+4X$. The result is

$$Y^2+XY=X^3+\frac{3r-1}{4}X^2+
\frac{H'(J)}{16}X+\frac{\eta H(J)}{64}.\tag{13}$$

This equation is integral at two, since

$$H'(J)=\frac{3J\,2^m u(j-1)}{n-1},\qquad
H(J)=2^{2m}u^3P(0),$$

so the respective valuations are $m$ and at least $2m$.
The new $c_4$ is $3k$, an odd integer, and its discriminant valuation is
$2m-8$. Consequently it has good reduction for $m=4$, and multiplicative
reduction of type $I_{2m-8}$ for $m\ge5$. In the latter case the reduction
is $Y^2+XY=X^3+\overline{(3r-1)/4}X^2$; its node has rational tangent
lines precisely when $r\equiv3\pmod8$. Thus large $m$ is compatible with
ordinary multiplicative reduction after one of these two fixed twists.

## 5. The missing uniform step

The elliptic curves vary with $n,j$. Siegel's theorem gives finiteness of
integral points on each fixed curve, and Shafarevich's theorem gives
finiteness of curves with good reduction outside a fixed finite set.
Neither hypothesis has been established uniformly here; see, for example,
the precise statements in [Li's notes on finiteness theorems](https://www.math.columbia.edu/~chaoli/docs/HeightsAndFiniteness.html).

The existing endpoint and Lucas conditions concern primes dividing
$n(n-1)(n-2)$. We have no theorem bounding the new conductor primes from
$(j-1)(c-1)$, and no common divisibility of their discriminant exponents
that would supply a uniform level-lowering argument.

Equation (5) does give a point whose coordinate denominator is a power
of two. There is no established reason that further multiples of $Q$
retain this property, so elliptic divisibility sequences do not yet give
an infinite sequence of integral points to which Siegel could be applied.

The useful new target is therefore specific: control the rank or the
descent conditions of the marked quartic (8), together with the original
endpoint arithmetic. A rank-zero or incompatible-descent theorem for
these parameters would prove a contradiction. No such theorem is proved
in this note. The quartic transformation, doubling formula, both
$j$-invariants, and (11) were checked symbolically; no finite search was
performed.
