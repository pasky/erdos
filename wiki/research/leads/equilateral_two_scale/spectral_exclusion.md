---
name: research/leads/equilateral_two_scale/spectral_exclusion
title: Bessel exclusion of two equilateral scales
desc: |
  Avoiding equilateral triangles of side r forces the rotation-averaged pair
  correlation -1/3 at distance r. A Bessel bound then excludes sides 1 and x
  for x >= 3/2 or x <= 2/3: for measurable colorings outright, and for every
  coloring when x is algebraic, granting the Lean rigidity theorem of
  OpenAI's plane-coloring release.
created: 2026-10-16T14:00:00Z
updated: 2026-10-16T14:00:00Z
---

***

The arguments are credited to Plasma AI. Lemma 1 and Theorem 2 are covered
by the [[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/grade|graded whole-conclusion review]].
Theorem 3 is outside that grade's standalone acceptance scope and remains
author-recorded, conditional on the external premise
named in its statement; Lemma 1 and Theorem 2 use no premise beyond standard
analysis. The scalar bounds in Lemma 1 are given by rational partial sums,
not assumed from floating-point evaluations.

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

The constant $3/2$ is not sharp: splitting the range of $t$ further with
more values of $J_0$ improves it. Near its minimum
$J_0(t)\approx J_0(t_0)+\tfrac12|J_0(t_0)|(t-t_0)^2$, because
$J_0''(t_0)=-J_0(t_0)$; this second-order estimate suggests that the
criterion $m(x)>-2/3$ holds from about $x\approx1.37$. That figure is a
heuristic, not a certified bound.

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

**Comparison with Shkredov's criterion.** Shkredov's Theorem 1
([[../library/discrete_geometry/shkredov_2015_problems_euclidean_ramsey_theory/theorem_1|Shkredov 2015, Theorem 1]])
gives, for a triangle with two sides in ratio $\omega'$, a monochromatic copy
in every measurable two-coloring when $m(\omega')\ge-0.5972406$, with the
constant exactly as printed in that theorem.
Applied to the isosceles triangle with sides $1,1,x$, or $x,x,1$ when
$x\ge2$, and combined with
[[../library/discrete_geometry/jelinek_2009_monochromatic_triangles_two_colored_plane/corollary_1_4|Lemma 1.3 of Jelínek et al.]],
which turns a monochromatic triangle with sides in $\{1,x\}$ into a
monochromatic equilateral triangle of side $1$ or $x$, it excludes two scales
when $m(x)\ge-0.5972406$. Theorem 2 uses the stronger hypothesis that both
equilateral scales are avoided, which fixes both correlations at exactly
$-1/3$, and needs only $m(x)>-2/3$. For an exact comparison take
$x=10/t_0>5/2$. The bounds in Lemma 1 give
$m(x)\le J_0(t_0)+J_0(10)<-6475/10000<-0.5972406$.
Thus Shkredov's criterion fails while Lemma 1
applies. Shkredov's proofs are also
Fourier-analytic and use two colors essentially; what is added here is that
missing both equilateral scales fixes both correlations exactly. A web
search on 2026-10-16 for the two-scale equilateral form of this argument
found no earlier statement; the search was brief and does not certify
novelty.

## Arbitrary colorings at algebraic ratios

Let $E\subset\mathbb C$ be the field of algebraic numbers and $K$ its group
of algebraic unit vectors, as in Definition 2.1 of the
[[../library/discrete_geometry/openai_2026_euclidean_plane_not_five_colorable/_index|OpenAI plane-coloring manuscript]].

**Premise (R0).** Let $H$ be a complex Hilbert space, $z\mapsto T_z$ a
unitary representation of the discrete additive group $E$ on $H$, and
$V_k$ $(k\in K)$ unitary operators with $V_kT_z=T_{kz}V_k$. Let $H_c$ be the
closed subspace of vectors $v$ with $T_zv\to v$ as $z\to0$ in the usual
topology of $E$. If $v\perp H_c$ and $V_kv=v$ for every $k\in K$, then
$\langle v,T_zv\rangle=0$ for every nonzero $z\in E$.

This is the Fourier form of the manuscript's Theorem 2.3 (Haar rigidity of
wild character laws). It is the Lean theorem
`OAI.PlaneFiveColor.Spectral.residual_fourier` of the release's Lean
development, file `lean/OAI/Analysis/PlaneSpectrum/Ergodicity.lean` at the
card's revision adc7f1241, which derives it from `finite_wild_fourier`, the
Lean form of Theorem 2.3. In that development $E$ is
`algebraicClosure ℚ ℂ`, $K$ the algebraic points of the unit circle, and
$H_c$ the vectors whose orbit map is continuous at $0$. The theorem lies in
the proof of `OAI.EuclideanFiveColor.no_proper_five_coloring`, through
`proper_to_borel_weak`, `exists_label_field`, `fieldVector_unit_correlation`
and `projected_unit_correlation`, and that declaration was built with only
the standard axioms in the verification recorded on the
[[problems/discrete_geometry/E0508/claims/2026_09_23_openai|Problem 508
claim page]].
The statement and this dependency chain were read here in the Lean source of
the release; the five files involved are identical at revision adc7f1241 and
at the release's later commit of 2026-10-12. No review has checked that the
Lean statement matches (R0) as used below, so (R0) is carried as a
premise.

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

The proof uses neither a measurable sample nor the factor structure of the
manuscript's Lemma 4.1: only the orthogonal decomposition and (R0). With the
reduction of
[[../library/discrete_geometry/jelinek_2009_monochromatic_triangles_two_colored_plane/corollary_1_4|Corollary 1.4 of Jelínek et al.]],
Theorem 3 says that a two-coloring of the plane with two exceptional
triangles must miss equilateral triangles of two sides $a<b$ whose ratio
$b/a$ is transcendental or lies in $(1,3/2)$, granting (R0).

## Scope and the remaining window

Theorem 3 is limited to algebraic $x$ because (R0) concerns the additive
group of algebraic numbers: no equilateral triangle of transcendental side
has all its vertices in $E$. What is known about other carriers is recorded
in [[research/leads/equilateral_two_scale/transcendental_scales|the
transcendental-scale account]].

The separately reviewed
[[research/leads/equilateral_two_scale/rigidity_extension|rigidity
extension]] supplies the corresponding correlation identity over the
algebraic closure of $\mathbb Q(x)$ for every real ratio. Together with
binary transfer and the circle account, it forms the reviewed full proof
on the canonical lead. Theorem 3 as stated here retains its narrower
conditional scope and does not inherit independent verification from that
whole-conclusion grade.

For $2/3<x<3/2$ the correlation identities alone may be consistent, and the
window is closed by a different mechanism: Theorem 4 of the
[[research/leads/equilateral_two_scale/circle_exclusion|circle account]]
excludes it for measurable colorings by the structure of unit circles about
boundary points, without pair correlations. The remarks below record what
the correlation method alone gives there. The exact
condition they impose is that $(-\tfrac13,-\tfrac13)$ lie in the convex hull
of the origin and the curve $t\mapsto(J_0(t),J_0(xt))$, $t\ge0$; Lemma 1
uses only the diagonal functional of this two-moment condition. For $x$ near
$1$ the condition holds. For $x>1$ close to $1$, the function
$J_0(xt)-J_0(t)$ has opposite signs on either side of the strict minimum
$t_0$, giving a crossing $t^*$ close to $t_0$. At this crossing,
$J_0(t^*)=J_0(xt^*)<-1/3$, and the measure $\lambda$ concentrated on the circle
of radius $t^*$ with mass $1/(3|J_0(t^*)|)<1$ meets both identities.
The case $x<1$ follows by reciprocal scaling. This constructs a feasible
spectral measure for these two equations, not an avoiding coloring.

Further linear constraints on the same correlation function are available.
Any three signs satisfy $ab+ac+bc\ge-1$. Averaging over equilateral
triangles of any side $d$, without assuming avoidance at that side, gives

$$
K(d)=\int J_0(dt)\,d\tau(t)\ge-\frac13\qquad(d>0),
$$

in the setting of Theorem 2, and the same for the function $\varphi$ of
Theorem 3: first obtain the inequality at algebraic $d$, then use
continuity for all real $d>0$. In the measurable case the disk-cutoff
boundary errors vanish for each fixed $d$, and the same weak limit $\tau$
applies. Thus $K$ attains its global minimum at both $d=1$ and $d=x$.
A single circle of frequencies cannot do this for $x\ne1$, because
$J_0(dt^*)$ has a unique global minimum in $d$. No feasible mixture meeting
these global inequalities at two distinct minimum radii is supplied here.
These are the first constraints of a linear-programming hierarchy in
which every finite configuration of points imposes the constraints of its
avoiding colorings on the pair correlations. Their feasibility or
infeasibility in the window is not settled here, and Theorem 4 makes it
unnecessary for the route. For
algebraic $x$ the [[research/leads/equilateral_two_scale/binary_transfer|binary
transfer]] reduces the question to weakly avoiding measurable colorings,
granting (R0), and Theorem 4 then excludes every algebraic $x\ne1$.
