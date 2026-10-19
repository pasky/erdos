---
name: theory/polynomials/L186_quartic_critical_value_parameters/_proof
desc: Critical-value differences bound the roots, circumcircles parametrize the generic family, and explicit collision calculations complete the coordinate reduction.
created: 2026-10-15T17:09:48Z
updated: 2026-10-15T17:09:48Z
---

# theory/polynomials/L186_quartic_critical_value_parameters/_proof

***

Use the conventions of [[theory/polynomials/L186_quartic_critical_value_parameters/_index|L186]].
Translation centers a monic quartic. The rotation
$p(z)\mapsto e^{-4i\theta}p(e^{i\theta}z)$ preserves monicity and length,
as does conjugation of all coefficients.

## A compact parameter set

Write $p(z)=z^4+az^2+bz+c$ and let $u,v,w$ be its critical points, counted
with multiplicity. Then

$$
u+v+w=0,\qquad
p'(z)=4(z-u)(z-v)(z-w),\qquad
p(u)-p(v)=w(u-v)^3. \tag{1}
$$

For the last identity integrate $p'$ from $v$ to $u$, writing
$z=(u+v)/2+t$. The odd part vanishes, and the integral is
$-(u+v)(u-v)^3$. The identity also holds when critical points coincide.

Let $M=\max(|u|,|v|,|w|)$ and label $|u|=M$. If
$|v-w|\ge M/2$, then $|p(v)-p(w)|\ge M^4/8$. Otherwise
$|v|,|w|>M/4$ and
$|u-v|=|3u/2-(v-w)/2|>5M/4$, so
$|p(u)-p(v)|>125M^4/256$. Consequently

$$
\max_{i,j}|p(u_i)-p(u_j)|\ge M^4/8. \tag{2}
$$

If all critical values have modulus one, (2) gives $M\le2$. Comparing
coefficients in $p'$ now gives

$$
|a|\le6M^2\le24,\qquad |b|\le4M^3\le32,
\qquad |c|\le1+M^4+|a|M^2+|b|M\le177. \tag{3}
$$

The centered coefficient set with all critical values on the circle is
closed: along coefficient convergence the multiset of roots of $p'$ converges,
and their polynomial values converge. It is bounded by (3), hence compact.
More generally, critical values in $|z|\le K$ give $M^4\le16K$ and a
coefficient bound depending only on $K$. This also supplies compactness when
critical values are moved along fixed bounded arcs. No classification theorem
for the critical-value map is needed for these bounds.

## The generic two-real-parameter chart

Assume first that the critical points and the critical values are each
pairwise distinct. Choose a critical point of largest modulus, and rotate
so that it equals $s>0$. Write the other two as $st,-s(1+t)$, where

$$
|t|\le1,\qquad |1+t|\le1.
$$

Define

$$
F_t(z)=z^4-2(1+t+t^2)z^2+4t(1+t)z.
$$

Then $p(sz)=s^4F_t(z)+c$. Put
$f_1=F_t(1)$, $f_2=F_t(t)$ and $f_3=F_t(-1-t)$.
The three distinct critical values on a circle are not collinear. Thus the
$f_i$ have a unique circumcenter $C(t)$ and positive circumradius $R(t)$.
They can be obtained from the two real linear equations

$$
2\operatorname{Re}\bigl((C-f_1)\overline{(f_i-f_1)}\bigr)
=|f_i-f_1|^2,\qquad i=2,3.
$$

The unit-circle condition forces $s^4R(t)=1$ and $c=-s^4C(t)$. Conversely
these choices give unit critical values. Every member of the generic class
is therefore, up to the stated isometries, of the form

$$
p_t(z)=s^4\bigl(F_t(z/s)-C(t)\bigr),\qquad s=R(t)^{-1/4}. \tag{4}
$$

The parameter domain is the part of the closed lens
$|t|,|1+t|\le1$ where the three $f_i$ are noncollinear and the three
critical points are distinct. Relabeling critical points can give several
parameters for the same polynomial; injectivity is unnecessary for coverage.
The chart itself is singular at excluded parameters. Compactness of the
coefficient set does not give bounded derivatives of (4) there.

## The missing strata are explicit

There are three additional cases, with complex conjugation allowed to identify
the two signs below, since it preserves length.

**A double critical point.** The roots of $p'$ are $r,r,-2r$ with $r\ne0$.
Rotate so that $r>0$ and put $h=r^4$. The polynomial is

$$
p(z)=z^4-6\sqrt h\,z^2+8h^{3/4}z+
\frac{21h}{2}\ \pm i\sqrt{1-\frac{729h^2}{4}},
\qquad 0<h\le\frac2{27}. \tag{5}
$$

Indeed its critical values are $c+3h$ and $c-24h$, whose difference is
$27h$. Requiring both moduli to equal one gives (5). This family has a
double critical point and a distinct simple one throughout $h>0$.

**Distinct critical points with two equal critical values.** By (1), if
$u\ne v$ but $p(u)=p(v)$, the third critical point is zero. Thus the roots
are $r,-r,0$. Rotate so that $r>0$ and again put $h=r^4$. The family is

$$
p(z)=z^4-2\sqrt h\,z^2+\frac h2
\ \pm i\sqrt{1-\frac{h^2}{4}},\qquad 0<h\le2. \tag{6}
$$

Its critical values are $c-h,c-h,c$, so the unit-circle condition gives
(6). These are collisions of values at distinct points, and are not covered
by considering repeated roots of $p'$ alone.

**A triple critical point.** Centering forces it to be zero, so
$p(z)=z^4+c$ with $|c|=1$. Rotation makes this $z^4-1$.

These cases exhaust the complement of (4). Three distinct collinear critical
values cannot lie on the unit circle. If all critical values equal $v_0$,
each distinct critical point of multiplicity $m$ is a root of $p-v_0$ of
multiplicity $m+1$. Their total multiplicity is three plus the number of
distinct critical points, at most four. Thus there is just one critical
point, the last case above.


## Unicritical length comparison

Away from finitely many critical values, inverse branches give

$$
\ell(p)=\int_0^{2\pi}\sum_{p(z)=e^{i\theta}}\frac{d\theta}{|p'(z)|}.
$$

For $p(z)=z^4-c$ the sum is $|c+e^{i\theta}|^{-3/4}$.
At $c=1$ substitution $u=\theta/2$ gives
$\ell(z^4-1)=2^{1/4}B(1/2,1/8)$, with the usual beta integral.

For the single-critical-value class the required comparison is elementary.
Put $\Phi(c)=\ell(z^4-c)$ for real $c\ge0$. For $c<1$, expanding the two
factors of $|1+ce^{i\theta}|^{-3/4}$ and integrating gives

$$
\Phi(c)=2\pi\sum_{j\ge0}\binom{-3/8}{j}^{\!2}c^{2j}.
$$

It is strictly increasing on $[0,1)$. Dominated convergence at $c=1$ follows
from $|c+e^{i\theta}|^2=(1-c)^2+c|1+e^{i\theta}|^2$ for $c\ge1/2$.
For $c>1$, $\Phi(c)=c^{-3/4}\Phi(1/c)<\Phi(1)$. Rotating the constant
term therefore shows that $\ell(z^4+c)\le\ell(z^4-1)$, with equality
exactly when $|c|=1$.
