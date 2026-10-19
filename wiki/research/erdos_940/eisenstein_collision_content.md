---
name: research/erdos_940/eisenstein_collision_content
title: Cubic collisions as large Eisenstein content
desc: An exact fixed-field parametrization turns cubic collision counting into a large-content problem; its critical gcd tail remains unproved.
tags: []
sources: []
created: 2026-09-22T23:49:00Z
updated: 2026-09-22T23:56:58Z
---


# Cubic collisions as large Eisenstein content

***

## Status and relation to the earlier attempt

The parametrization, height comparison, local permutation calculation, and
implication from a content-tail bound below are proved. **The required
content-tail bound is not proved, and no density case is resolved.** The
resulting parametrization revisits the [earlier Eisenstein height-counting
attempt](remaining_questions.md#an-eisenstein-height-counting-attempt); it is
not a wholly new resolution of that obstruction. The additions are the exact
integral multiplier classification, the admissible logarithmic loss in the
content-tail criterion, the complete-residue calculation, and the common-zero
geometry.

The approach uses one fixed Euclidean ring rather than the varying
quadratic fields in the [quadric-fiber approach](cubic_collision_ranges.md).

The initial observation is that every collision quadric

$$
3\sum_{i=1}^3 a_i k_i u_i^2+
\left(\sum_{i=1}^3a_i k_i^3\right)t^2=0
$$

has the point $(\mathbf u,t)=(\mathbf k,\sqrt{-3})$ over the
same quadratic field. This does not mean that every such quadric is
split over that field. Instead, a direct global change of coordinates
gives the parametrization below.

Fix positive integers $a_1,a_2,a_3$ and write
$F(\mathbf x)=\sum_i a_i x_i^3$.
Let $\omega^2+\omega+1=0$, $\operatorname{Im}\omega>0$, and put

$$
\mathcal O=\mathbb Z[\omega],\qquad
\zeta=1-\omega^2,\qquad
S(\mathbf z)=\sum_{i=1}^3a_iN(z_i)z_i.
$$

Here $N(z)=z\bar z$, and absolute values use the complex embedding.
The ring $\mathcal O$ is Euclidean: rounding the two real coordinates
in its basis $1,\omega$ approximates any complex number with squared
error at most $3/4<1$. Thus primitive vectors have a Bezout identity.

## Exact integral parametrization

For integral vectors $\mathbf x,\mathbf y$, set

$$
z_i^{\mathrm{raw}}=x_i-\omega^2y_i,\qquad
q_i=N(z_i^{\mathrm{raw}})=x_i^2+x_iy_i+y_i^2.
$$

Writing
$A=\sum_i a_i x_iq_i$ and $B=\sum_i a_i y_iq_i$, one has

$$
S(\mathbf z^{\mathrm{raw}})=A-\omega^2B,\qquad
A-B=F(\mathbf x)-F(\mathbf y).
$$

Consequently

$$
F(\mathbf x)=F(\mathbf y)
\quad\Longleftrightarrow\quad
S(\mathbf z^{\mathrm{raw}})\in\zeta\mathbb Q.            \tag{1}
$$

For integral $\mathbf z^{\mathrm{raw}}$, the rational scalar in
(1) is automatically integral.

Now let $\mathbf z\in\mathcal O^3$ be primitive over $\mathcal O$,
with $S(\mathbf z)\ne0$. Define

$$
\lambda(\mathbf z)=\zeta\overline{S(\mathbf z)},\qquad
g(\mathbf z)=\max\{d\in\mathbb N:\lambda(\mathbf z)\in d\mathcal O\},
\qquad
\delta_0(\mathbf z)=\lambda(\mathbf z)/g(\mathbf z).
$$

Equivalently, $g$ is the positive gcd of the two integral coefficients
of $\lambda$ in the basis $1,\omega$.

**Parametrization lemma.** The nonzero integral scalar multiples
$\delta\mathbf z$ which satisfy the collision equation (1) are
exactly

$$
\delta\mathbf z=\ell\,\delta_0(\mathbf z)\mathbf z,
\qquad \ell\in\mathbb Z\setminus\{0\}.                  \tag{2}
$$

The associated coordinates need not be positive; positivity is an
additional restriction.

Indeed, primitivity and Bezout show that
$\delta\mathbf z\in\mathcal O^3$ if and only if $\delta\in\mathcal O$.
Also

$$
S(\delta\mathbf z)=N(\delta)\delta S(\mathbf z).
$$

Thus a nonzero $\delta\in\mathcal O$ satisfies (1) if and only if
$\delta\in\mathbb Q\lambda$. Finally

$$
\mathcal O\cap\mathbb Q\lambda
=\mathbb Z\,\lambda/g,
$$

by the ordinary gcd of the two coefficients of $\lambda$. This
proves (2).

Conversely, divide the three raw coordinates of any integral collision
by their common Eisenstein gcd. This produces a primitive $\mathbf z$
and recovers the collision by (2). Changing the gcd by a unit produces
only the six unit associates of $\mathbf z$; it does not affect the
counting argument.

## Positivity controls the archimedean height

For a positive collision, the raw coordinates
$x_i-\omega^2y_i$ lie in the sector $0<\arg z<\pi/3$.
After division by their common Eisenstein gcd, the primitive coordinates
therefore lie in a common rotated sector of opening $\pi/3$.
Put

$$
B(\mathbf z)=\max_i|z_i|.
$$

For vectors in any such sector, projecting onto its bisector gives

$$
\frac{\sqrt3}{2}\sum_i a_i|z_i|^3
\le |S(\mathbf z)|\le\sum_i a_i|z_i|^3.
$$

In particular

$$
|S(\mathbf z)|\asymp_{\mathbf a}B^3,\qquad
1\le g(\mathbf z)\ll_{\mathbf a}B^3.                  \tag{3}
$$

There is no cancellation exception to this estimate in the positive
collision region.

Since $|\zeta|=\sqrt3$, the complex-coordinate height in (2) is

$$
\max_i|\ell\delta_0z_i|
=|\ell|\frac{\sqrt3|S(\mathbf z)|B}{g(\mathbf z)}
\asymp_{\mathbf a}|\ell|\frac{B^4}{g(\mathbf z)}.        \tag{4}
$$

The complex-coordinate height is comparable to the largest absolute
value of the associated integer root coordinates. Thus a positive
collision in $[1,N]^6$ requires

$$
B\ll_{\mathbf a}N,\qquad
g(\mathbf z)\gg_{\mathbf a}B^4/N,
$$

and each primitive parameter vector gives at most

$$
O_{\mathbf a}(Ng(\mathbf z)/B^4)
$$

allowed multipliers.

## A sufficient large-content estimate

Let $T(B,D)$ count primitive $\mathbf z\in\mathcal O^3$ with
$B/2<B(\mathbf z)\le B$, lying in some common rotated sector of
opening $\pi/3$, and with $g(\mathbf z)\ge D$.

The following is a **sufficient hypothesis, not an established bound**:
for some fixed $A\ge0$,

$$
T(B,D)\ll_{\mathbf a}
\frac{B^6}{D}\left(1+\log(2+B^3/D)\right)^A
\quad(B,D\ge1).                                      \tag{5}
$$

It would imply

$$
\#\{(\mathbf x,\mathbf y)\in[1,N]^6:
          F(\mathbf x)=F(\mathbf y)\}\ll_{\mathbf a}N^3. \tag{6}
$$

Consequently it would give positive lower density for the positive
values of $F$, and, after a fixed powerful dilation, for $S_3$.

To prove this implication, fix a dyadic shell $B$. Only contents

$$
g\ge D_0:=\max(1,c_{\mathbf a}B^4/N)
$$

can contribute, and (3) bounds them above by $C_{\mathbf a}B^3$.
In a dyadic content bin $d\le g<2d$, use (4) and (5) to bound the
number of collisions by

$$
\ll_{\mathbf a}\frac{Nd}{B^4}\frac{B^6}{d}
       \left(1+\log(2+B^3/d)\right)^A.
$$

Summing these bins gives

$$
\ll_{\mathbf a}NB^2
       \left(1+\log(2+N/B)\right)^{A+1}.               \tag{7}
$$

When $D_0=1$, the same bound holds because $B^4\ll N$ makes
$B^3\ll N/B$. Finally, the dyadic sum of (7) over $B\ll N$
is $O_{\mathbf a}(N^3)$: after $B\asymp N2^{-j}$, it is bounded
by a constant multiple of
$N^3\sum_{j\ge0}4^{-j}(j+1)^{A+1}$.

Thus logarithmic losses in the ratio $B^3/D$ would be harmless.
A logarithmic loss depending on $B$ alone at the endpoint
$D\asymp B^3$ would not give (6).

## An exact local calculation

At every prime $p\equiv2\pmod3$, one has
$\mathcal O/p\mathcal O\simeq\mathbb F_{p^2}$ and
$\bar z=z^p$. Hence the map

$$
z\longmapsto N(z)z=z^{p+2}
$$

is a permutation: its exponent is coprime to $p^2-1$, since

$$
\gcd(p+2,p^2-1)=\gcd(p+2,3)=1.
$$

If some $a_i$ is a unit modulo $p$, then for each prescribed value
of $S(\mathbf z)$ and each choice of the other two coordinates,
there is exactly one value of that coordinate. Therefore

$$
\#\{\mathbf z\bmod p:S(\mathbf z)=b\}=p^4
\qquad(b\in\mathcal O/p\mathcal O).                    \tag{8}
$$

This supports the codimension-two divisibility scale in (5), but
it concerns complete residue boxes. It does not count large
contents in the incomplete box $|\mathbf z|\le B$.

## Why this is not yet a solution

The endpoint $D\asymp B^3$ includes primitive vectors for which
$\delta_0$ is bounded. Such a fixed multiplier is itself a fixed
cubic collision equation. In particular, $\delta_0=1$ includes
the original equation. Primitivity over $\mathcal O$ does not remove
this stratum.

For an exact example, take $F=x^3+2y^3+4z^3$. Then

$$
F(3,3,26)=F(1,30,16)=70385.
$$

The norms of the three raw Eisenstein coordinates are
$13,999,1348$, whose gcd is one. The raw vector is therefore
primitive over $\mathcal O$. Direct calculation gives

$$
S(\mathbf z^{\mathrm{raw}})=\zeta\,146225,\qquad
\lambda=438675,\qquad \delta_0=1.
$$

Thus cubic-sized content can occur without a nontrivial common
Eisenstein divisor in the input.

There is also no simple factorization of the common-zero locus
of the two content polynomials. After base extension, its
projective form is

$$
\sum_i a_i z_i^2w_i=0,\qquad
\sum_i a_i z_iw_i^2=0
\quad\text{in }\mathbb P^2\times\mathbb P^2.            \tag{9}
$$

It is a smooth complete intersection of bidegrees $(2,1),(1,2)$
in characteristic zero. To check smoothness, a dependent pair
of gradients would give

$$
w_i(2\alpha z_i+\beta w_i)=0,\qquad
z_i(\alpha z_i+2\beta w_i)=0
$$

for every $i$. A nonmatching support forces $\alpha=\beta=0$;
on a matching nonzero coordinate the two equations also force
$\alpha=\beta=0$. Adjunction gives trivial canonical bundle;
the Koszul sequence gives $H^1(\mathcal O)=0$. Thus (9) is a
K3 surface, rather than a union of elementary norm-factor loci.

The missing estimate is a large-modulus gcd bound of the strength
(5), especially its endpoint. Complete congruence counts, the
Euclidean algorithm in the fixed field, and the parametrization
alone do not supply it. The route is retained as a different
arithmetic formulation, not as a completed argument or a claim
that the hard endpoint has been reduced to an easier theorem.
