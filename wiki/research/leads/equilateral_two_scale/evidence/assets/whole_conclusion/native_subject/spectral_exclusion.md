# wiki/research/leads/equilateral_two_scale/spectral_exclusion.md

[cut]

## Setting and the correlation identity

Identify the plane with $\mathbb C$ and put $\omega=e^{i\pi/3}$. For $r>0$,
$p\in\mathbb C$ and a unit vector $u$, write
$T_r(p,u)=(p,\;p+ru,\;p+ru\omega)$; these are all the equilateral triangles
of side $r$, each listed three times. A two-coloring is a map
$c:\mathbb C\to\{-1,+1\}$. It *avoids* side $r$ if no $T_r(p,u)$ is
monochromatic. A Lebesgue measurable $c$ *weakly avoids* side $r$ if the set
of $(p,u)\in\mathbb C\times S^1$ for which $T_r(p,u)$ is monochromatic is null
for area times arc length.

For three signs $a,b,c$ that are not all equal exactly one pair agrees, so

$$
ab+ac+bc=-1 .
$$

Every correlation argument below starts from this identity: averaged over
the copies of a triangle it gives the value $-1/3$ to each of the three
equal edge correlations. This uses two colors in an essential way.

## A Bessel lemma

Let $J_0$ be the Bessel function of order zero, let $t_0=j_{1,1}$
be the first positive zero of $J_1=-J_0'$, and put

$$
m(x)=\inf_{t\ge0}\bigl(J_0(t)+J_0(xt)\bigr)\qquad(x>0).
$$

Substituting $t\mapsto t/x$ shows $m(x)=m(1/x)$.

**Lemma 1.** $m(x)\ge-83/125>-2/3$ for every $x\ge3/2$, and hence for
every $0<x\le2/3$.

*Scalar bounds.* Write

$$
S_{\nu,N}(q)=\sum_{k=0}^{N}
 \frac{(-1)^k(q/2)^{2k+\nu}}{k!(k+\nu)!}\qquad(\nu=0,1).
$$

The [defining series for $J_\nu$](https://dlmf.nist.gov/10.2.E2) gives
$S_{\nu,21}(q)<J_\nu(q)<S_{\nu,20}(q)$ at the positive arguments below:
the omitted terms alternate and decrease, since $q\le10$. Each row records
the rational inequalities $\ell<S_{\nu,21}(q)$ and
$S_{\nu,20}(q)<u$. These are finite sums with rational inputs, so the
displayed enclosures follow by clearing positive denominators and the
alternating-series remainder bound.

| $\nu$ | $q$ | $\ell$ | $u$ |
| --- | --- | --- | --- |
| $0$ | $3$ | $-261/1000$ | $-260/1000$ |
| $0$ | $16/5$ | $-321/1000$ | $-320/1000$ |
| $0$ | $19/5$ | $-4026/10000$ | $-4025/10000$ |
| $1$ | $19/5$ | $128/10000$ | $129/10000$ |
| $1$ | $4$ | $-67/1000$ | $-66/1000$ |
| $0$ | $9/2$ | $-321/1000$ | $-320/1000$ |
| $0$ | $24/5$ | $-241/1000$ | $-240/1000$ |
| $0$ | $10$ | $-246/1000$ | $-245/1000$ |
| $1$ | $10$ | $43/1000$ | $44/1000$ |

*Zeros and monotonicity.* On $0<t\le3$, set $y=t^2/4\le9/4$. The series
for $J_1$ bounds $2J_1(t)/t$ below by
$P(y)=1-y/2+y^2/12-y^3/144$. Here
$P'(y)=-(y^2-8y+24)/48<0$ and $P(9/4)=223/1024>0$.
Thus $J_1$ has no positive zero at most $3$.

Any two successive positive zeros $a<b$ of $J_1$ satisfy $b-a>\pi$.
Indeed $v(t)=\sqrt t\,J_1(t)$ satisfies
$v''+(1-3/(4t^2))v=0$, by
[Bessel's equation](https://dlmf.nist.gov/10.2.E1). Integration by parts
and the Dirichlet Wirtinger inequality give

$$
\left(\frac{\pi}{b-a}\right)^2\int_a^b v^2
\le\int_a^b(v')^2
=\int_a^b\left(1-\frac{3}{4t^2}\right)v^2
<\int_a^b v^2.
$$

The signs in the table at $19/5$ and $4$ therefore place the first positive
zero $t_0$ in $(19/5,4)$: a preceding zero in $(3,19/5)$ would violate
this spacing. The second positive zero exceeds $19/5+\pi>24/5$, and the
third exceeds $19/5+2\pi>10$. Positive zeros are simple by uniqueness for
the differential equation. Since $J_0'=-J_1$, $J_0$ decreases up to $t_0$,
increases until the second zero, then decreases until the third. Consequently
its minimum on $[24/5,10]$ is at one of the endpoints.

*Global and tail bounds.* The derivative identities, also obtained by
differentiating the defining series, give

$$
\frac{d}{dt}\bigl(J_0(t)^2+J_1(t)^2\bigr)
=-\frac{2J_1(t)^2}{t}\le0\qquad(t>0).
$$

The energy strictly decreases between distinct positive arguments, since
$J_1$ cannot vanish identically on an interval.
At $19/5$ the energy is less than
$(4026^2+129^2)/10^8<(403/1000)^2$. Monotonicity of $J_0$ before $19/5$
and the energy bound thereafter imply $J_0(t)>-403/1000$ for all $t\ge0$.
At $10$ the energy is less than
$(246^2+44^2)/10^6<1/16$, so $J_0(t)>-1/4$ for $t\ge10$.
The endpoint bounds and preceding zero analysis also give $J_0(t)>-1/4$
on $[24/5,10]$. Finally $J_0(t)>-261/1000$ on $[0,3]$.
The same energy identity, applied from $t_0$ where $J_1(t_0)=0$, shows
that $J_0(t_0)$ is the global minimum.

*Two arguments.* Let $x\ge3/2$. If either $t$ or $xt$ is outside
$(3,24/5)$, the global and tail bounds give
$J_0(t)+J_0(xt)>-(261+403)/1000=-83/125$. Otherwise
$3<t<16/5<t_0<9/2<xt<24/5$. Monotonicity on these two intervals and the
table give $J_0(t)+J_0(xt)>-642/1000>-83/125$.
Taking the infimum proves the lemma, with the strict gap
$2/3-83/125=1/375$. $\square$



[cut]


## Measurable colorings

**Theorem 2.** Let $x>0$ satisfy $m(x)>-2/3$, in particular $x\ge3/2$ or
$x\le2/3$. No Lebesgue measurable two-coloring of the plane weakly avoids
both side $1$ and side $x$. In particular every measurable two-coloring
contains a monochromatic equilateral triangle of side $1$ or of side $x$,
and in fact a set of them of positive measure.

*Proof.* Suppose $c$ weakly avoids both sides. For $R>0$ let $B_R$ be the
disk of radius $R$ about $0$, put $c_R=c\mathbf 1_{B_R}$ and

$$
A_R(v)=\frac1{|B_R|}\int_{\mathbb C}c_R(p)\,c_R(p+v)\,dp .
$$

By Plancherel, $A_R(v)=\int e^{i\xi\cdot v}\,d\lambda_R(\xi)$ for the
probability measure $d\lambda_R=|\widehat{c_R}(\xi)|^2\,d\xi/
((2\pi)^2|B_R|)$; total mass one because $c_R^2=\mathbf 1_{B_R}$. Averaging
over rotations,

$$
\bar A_R(s)=\frac1{2\pi}\int_0^{2\pi}A_R(se^{i\theta})\,d\theta
=\int J_0(s|\xi|)\,d\lambda_R(\xi).
$$

Fix $r\in\{1,x\}$. For almost every $(p,u)$ the triangle $T_r(p,u)$ is not
monochromatic, so the identity above gives

$$
c(p)c(p+ru)+c(p)c(p+ru\omega)+c(p+ru)c(p+ru\omega)=-1 .
$$

Integrate over $p\in B_R$ and $u\in S^1$. The first two terms each give
$2\pi|B_R|\bar A_R(r)$ up to an error at most $2\pi|B_R\setminus B_{R-r}|$,
from the pairs that leave $B_R$. After the substitution $q=p+ru$ the third
term is the correlation of $q$ with $q+ru(\omega-1)$, where $|\omega-1|=1$,
and gives the same main term with an error of the same order. Hence
$\bar A_R(r)=-1/3+O(r/R)$.

Push $\lambda_R$ forward by $\xi\mapsto|\xi|$ to a probability measure
$\tau_R$ on $[0,\infty)$, regarded on the compact space $[0,\infty]$, and
take $R_n\to\infty$ with $\tau_{R_n}$ converging weak-* to $\tau$. Each
function $t\mapsto J_0(rt)$ extends continuously to $[0,\infty]$ with value
$0$ at $\infty$, by the
[large-argument asymptotic](https://dlmf.nist.gov/10.17.E3). Therefore

$$
\int_{[0,\infty)}J_0(t)\,d\tau(t)=\int_{[0,\infty)}J_0(xt)\,d\tau(t)=-\frac13,
\qquad \tau([0,\infty))\le1 .
$$

Adding, $-2/3=\int(J_0(t)+J_0(xt))\,d\tau\ge\min(m(x),0)\,\tau([0,\infty))
\ge\min(m(x),0)>-2/3$, a contradiction. $\square$



[cut]

**Premise (R0).** Let $H$ be a complex Hilbert space, $z\mapsto T_z$ a
unitary representation of the discrete additive group $E$ on $H$, and
$V_k$ $(k\in K)$ unitary operators with $V_kT_z=T_{kz}V_k$. Let $H_c$ be the
closed subspace of vectors $v$ with $T_zv\to v$ as $z\to0$ in the usual
topology of $E$. If $v\perp H_c$ and $V_kv=v$ for every $k\in K$, then
$\langle v,T_zv\rangle=0$ for every nonzero $z\in E$.



[cut]

**Theorem 3 (conditional on R0).** Let $x>0$ be algebraic with $m(x)>-2/3$,
in particular $x\ge3/2$ or $x\le2/3$. Then every two-coloring of the plane,
with no regularity assumed, contains a monochromatic equilateral triangle of
side $1$ or of side $x$.

*Proof.* Suppose $c$ avoids both sides. Let $\Omega\subset\{\pm1\}^E$ be the
set of labelings of $E$ with no monochromatic triangle $T_r(p,u)$, $p\in E$,
$u\in K$, $r\in\{1,x\}$; such triangles lie in $E$ because
$\omega,x\in E$. It is closed, contains the restriction of $c$, and is
invariant under $\eta\mapsto\eta(k\,\cdot+z)$ for $z\in E$, $k\in K$. The
countable group $E\rtimes K$ is amenable, so $\Omega$ carries an invariant
Borel probability $\mu$, exactly as in the manuscript's Proposition 4.2.

On $H=L^2(\Omega,\mu)$ put $(T_zh)(\eta)=h(\eta(\cdot+z))$ and
$(V_kh)(\eta)=h(\eta(k\,\cdot))$. These are unitary, $z\mapsto T_z$ is a
representation, and $V_kT_z=T_{kz}V_k$. Let $f(\eta)=\eta(0)$, so $\|f\|=1$
and $V_kf=f$. Let $P$ be the orthogonal projection onto $H_c$. The space
$H_c$ is invariant under every $T_z$ and every $V_k$ (for the latter,
$T_zV_kv=V_kT_{k^{-1}z}v$), and so is its orthogonal complement, the
operators being unitary with inverses of the same kind. Hence
$v=f-Pf$ satisfies $v\perp H_c$ and $V_kv=v$, and (R0) gives
$\langle v,T_zv\rangle=0$ for $z\ne0$. The cross terms
$\langle Pf,T_zv\rangle$ and $\langle v,T_zPf\rangle$ vanish, so

$$
\langle f,T_zf\rangle=\langle Pf,T_zPf\rangle\qquad(z\in E\setminus\{0\}).
$$

The right side is uniformly continuous and positive definite on $E$; it
extends to a continuous positive-definite function $\varphi$ on
$\mathbb C$, and Bochner's theorem gives $\varphi(y)=\int
e^{i\xi\cdot y}\,d\lambda(\xi)$ with $\lambda(\mathbb C)=\|Pf\|^2\le1$.
Since $V_kPf=Pf$, $\varphi(ky)=\varphi(y)$ for $k\in K$, so $\lambda$ is
invariant under the dense group $K$ of rotations and hence under all
rotations, and $\varphi(y)=\int J_0(|\xi||y|)\,d\lambda(\xi)$.

For $r\in\{1,x\}$ and $k\in K$, every $\eta\in\Omega$ gives
$\eta(0)\eta(rk)+\eta(0)\eta(rk\omega)+\eta(rk)\eta(rk\omega)=-1$.
Integrating, and using $\langle T_af,T_bf\rangle=\langle f,T_{b-a}f\rangle$
and the equality of $\langle f,T_zf\rangle$ at points of $E$ of equal
modulus (they differ by an element of $K$ and $V_kf=f$), each of the three
correlations equals $-1/3$. Thus $\varphi(1)=\varphi(x)=-1/3$, and the last
paragraph of the proof of Theorem 2, with $\lambda$ pushed to radii, gives
a contradiction. $\square$



[cut]
