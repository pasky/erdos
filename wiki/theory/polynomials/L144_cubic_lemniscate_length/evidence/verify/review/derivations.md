---
name: theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/review/derivations
desc: Independent derivations testing equality transport, the small-parameter singular estimates, and the interval enclosure argument for the frozen cubic assertion.
created: 2026-10-15T23:40:25Z
updated: 2026-10-15T23:40:25Z
---

# theory/polynomials/L144_cubic_lemniscate_length/evidence/verify/review/derivations

***

Reading: the complete supplied statement and proof, the complete supplied
checker, and the supplied Eremenko–Hayman text through Lemma 6 and its
bibliography; text-only source inspection. These derivations examine the
mathematics frozen on 2026-10-15, preserved under `assets/subject/` beside
the [report](report.md). Original project mathematics is credited to
Plasma AI; the external deformation and extremal-existence results are due
to Eremenko and Hayman.

## 1. Does an existential extremal reduction classify every maximizer?

This is the strongest attempted refutation. Lemma 5's statement alone supplies
one suitable extremizer and cannot exclude other maximizers. The extracted
proof instead uses a property of its construction. The required local property
does follow from the supplied construction, at the external theorem boundaries
specified below.

Let $p$ be any monic cubic whose length is the global maximum $M$. Suppose its
two critical values $v,w$ are distinct and $v\notin\mathbf T$. Choose a disc
about $v$ with closure disjoint from $\mathbf T$ and $w$, and a smooth function
$\Phi$ supported in it with $\Phi(v)=1$. For sufficiently small complex
$\lambda$, $\phi_\lambda(z)=z+\lambda\Phi(z)$ is a quasiconformal
homeomorphism. The smallness condition can be strengthened to keep
$v+\lambda$ away from $w$ and $\mathbf T$.

For $q_\lambda=\phi_\lambda\circ p$, the Wirtinger chain rule gives, away
from the finitely many zeros of $p'$,

$$
\mu_{q_\lambda}(z)
=\frac{\overline{p'(z)}}{p'(z)}
  \frac{\lambda\Phi_{\bar z}(p(z))}
       {1+\lambda\Phi_z(p(z))}.
$$

Changing this coefficient at those finitely many points changes no Beltrami
equation. Its support is compact, because $p$ is proper, and it depends
holomorphically on $\lambda$ with locally uniform norm less than one. The
external input is the normalized existence and analytic-parameter dependence
theorem for the Beltrami equation invoked in the supplied source: it supplies
$\psi_\lambda(z)=z+o(1)$ at infinity with this coefficient. The usual
straightening property for equal Beltrami coefficients makes

$$
p_\lambda=\phi_\lambda\circ p\circ\psi_\lambda^{-1}
$$

entire. Near infinity $\phi_\lambda$ is the identity and
$\psi_\lambda^{-1}(z)=z+o(1)$, so $p_\lambda(z)/z^3\to1$. An entire
function with this growth is a monic cubic. Thus the normalization preserves
the precise optimization class; it does not merely preserve degree up to an
uncontrolled scale factor.

Homeomorphisms preserve local topological degree. The two simple critical
points of $p$ have local degree two, so their images are again simple critical
points of $p_\lambda$. Their values are exactly $v+\lambda$ and $w$.
In particular, this deformation cannot silently replace two simple critical
points by a double critical point.

The support of the Beltrami coefficient stays away from $E(p)$. Hence
$\psi_\lambda$ is conformal on a fixed neighborhood of $E(p)$, and
$\phi_\lambda^{-1}(\mathbf T)=\mathbf T$ gives

$$
E(p_\lambda)=\psi_\lambda(E(p)),\qquad
\ell(p_\lambda)=\int_{E(p)}|\psi_\lambda'(z)|\,|dz|.
$$

Analytic dependence on $\lambda$, together with conformality in $z$ on that
fixed neighborhood, makes $\psi_\lambda'(z)$ holomorphic in $\lambda$.
On compact parameter subdiscs its modulus is uniformly bounded for $z$ on the
compact finite-length curve. Integrating its subharmonic modulus therefore
gives a subharmonic length function. It is at most $M$ and equals $M$ at
$\lambda=0$, so the subharmonic maximum principle makes it constant. This
argument applies to **any** maximizer with the stated isolated off-circle
value, not only to the extremizer selected in Lemma 5's conclusion.

The remaining possible obstruction is failure to continue all the way to the
circle. It is important that the cubic proof uses compactness, rather than
assuming that infinitely many local moves finish. Choose a simple arc from
$v$ to $\zeta\in\mathbf T\setminus\{w\}$, lying off $\mathbf T$ until
its endpoint and avoiding $w$. Either component of the complement of the
circle remains path connected after removal of one point, so such an arc
exists. Let $S$ consist of its nonterminal points $t$ for which a monic
maximizer has critical values $t,w$. Local deformation proves that $S$ is
relatively open and contains the starting point.

To prove relative closedness, translate each such cubic to depressed form
$z^3-3u_j^2z+b_j$. Its critical-value pair gives

$$
b_j=\frac{t_j+w}{2},\qquad |u_j|^3=\frac{|w-t_j|}{4}.
$$

If $t_j\to t$, these coefficients are bounded. A convergent subsequence of
$u_j,b_j$ gives a monic cubic whose critical values are $t,w$. One can choose
the sign of $u_j$ so $4u_j^3=w-t_j$; alternatively the unordered pair is
enough. The limit values stay distinct because the arc avoids $w$. Lemma 4's
coefficient continuity preserves length $M$. Thus $S$ is relatively closed;
connectedness of the nonterminal arc yields every one of its points. The same
boundedness and continuity argument at the terminal point supplies a maximizer
with critical values $\zeta,w$.

If $w$ is off the circle, repeat with an endpoint different from $\zeta$.
The result has two distinct critical values on $\mathbf T$, hence normalizes
to the positive-$a$ family and contradicts its strict inequality. This closes
both the potential collision and coefficient-escape objections. There is no
need to choose one globally continuous branch of the cubic parameter or to
rule out monodromy separately.

If the depressed cubic has $u=0$, its length is $\Phi(|b|)$ for $|b|\le1$
and $|b|^{-2/3}\Phi(1/|b|)$ for $|b|>1$. The positive nonconstant binomial
series for $\Phi$ proves strict increase on $[0,1]$, so equality is possible
only at $|b|=1$. Finally, for $w=e^{i\varphi}$, the substitution
$z=z_0+e^{i\varphi/3}\xi$ changes $(z-z_0)^3-w$ to
$e^{i\varphi}(\xi^3-1)$ and preserves arclength. The converse equality
cases are therefore present in precisely the stated monic convention.

The source's Beltrami existence/dependence theorems are external premises,
not proved here. Their original books were not supplied. The source's local
construction and the cubic continuation above were read and checked through
those explicit boundaries. Merely citing the statement of Lemma 5 would leave
a gap, but that is not what the frozen proof does.

## 2. Can small positive parameters or a singular window escape the estimate?

Write $h=a^3$, $c=\sqrt{1-4h^2}$, and $\sigma=x+iy$. The circle in the
scaled plane is $(hx-c)^2+h^2y^2=1$. On its near branch,

$$
x=\frac{c-\sqrt{1-h^2y^2}}h
 =\frac{h(y^2-4)}{c+\sqrt{1-h^2y^2}},\qquad
\sqrt{1+(dx/dy)^2}=\frac1{\sqrt{1-h^2y^2}}.
$$

The rationalized expression is defined also at $a=0$, as $x=0$. For the
positive parameters actually used in the circle integral, the checked
inequalities $a^6Y^2<1$ and $c/a^3>Y$, with $Y=50$, ensure that this branch
covers every point of modulus less than $Y$. On the other branch $x>Y$;
outside the displayed height interval $|y|\ge Y$. Thus the complement really
is covered by the tail estimate, including the far branch at small heights.

Here is an independent derivation of the tail constant. Choose a root of
$T-1/T=\sigma$ with $|T|\ge1$, put $\varepsilon=T^{-2/3}$ using any cube
root in this expression, and set $e=|T|^{-2/3}$. With
$\omega=e^{2\pi i/3}$, the three-point average
$A=\frac13\sum_{j=0}^2|1+\varepsilon\omega^{-2j}|$ satisfies

$$
1\le A\le1+\frac{e^2}{2(1-e)}.
$$

Indeed, the real parts of the three perturbations sum to zero. For $|w|<1$,
write $x=\operatorname{Re}w$; then
$|1+w|\le1+x+|w|^2/(2(1-|w|))$, by applying
$\sqrt{r^2+t^2}\le r+t^2/(2r)$ with $r=1+x>0$.

The exact difference is

$$
g(\sigma)=e\left(\frac{A}{|1+\varepsilon^3|}
                   -|1-\varepsilon^3|^{-2/3}\right).
$$

An upper bound for the bracket is

$$
\frac{1+e^2/(2(1-e))}{1-e^3}-(1+e^3)^{-2/3}
\le e^2\left(\frac{e+1/(2(1-e))}{1-e^3}+\frac{2e}{3}\right).
$$

A lower bound for it is

$$
\frac1{1+e^3}-\frac1{1-e^3}
=-\frac{2e^3}{1-e^6}
\ge -e^2\frac{2e}{1-e^3}.
$$

Multiplying by $e$ proves the displayed $K|T|^{-2}$ bound. All terms used
for $K$ increase with $e\in(0,1)$. Also
$|\sigma|\le |T|+1$, so $|T|\ge|\sigma|-1$ and
$e\le(Y-1)^{-2/3}$. This justifies both the substitution of the endpoint
value of $e$ and the uniform bound over the tail.

Parameterize the unscaled circle by $s=c-e^{i\psi}$. If
$\psi_Y=\arcsin(hY)$, its excluded near arc has
$|\psi|\le\psi_Y$. On its complement, $|s|\ge hY$ and
$|s|^2=(1-c)^2+4c\sin^2(\psi/2)$. Consequently

$$
\begin{aligned}
\int_{\Gamma_a\setminus\mathcal A_Y}
    \frac{|d\sigma|}{(|\sigma|-1)^2}
&\le \frac{h}{(1-1/Y)^2}
       \int_{\psi_Y<|\psi|\le\pi}\frac{d\psi}{|s|^2}\\
&\le \frac{h\cot(\psi_Y/2)}{c(1-1/Y)^2}
 \le \frac{2}{cY(1-1/Y)^2}.
\end{aligned}
$$

The factor of two comes from the two tails; integrating
$\csc^2(\psi/2)$ contributes the other factor absorbed by $4c$.
This calculation checks the potentially consequential normalization constants.

The proof's numerical sentence that the tail is at most $0.03$ can also be
checked with simple rational overestimates, without relying on a sampled
tail. At the small-parameter endpoint $c>99/100$. Since
$49^{-2/3}<3/40$, the first expression for $K$ is less than
$677/1000$ and the second is smaller. One obtains

$$
K\frac{2}{c\,50(49/50)^2}
 <\frac{677}{1000}\frac{2}{(99/100)\,50(49/50)^2}
 <\frac3{100}.
$$

For example, to see the estimate for the first expression, use
$1/(2(1-e))<20/37$, $(1-e^3)^{-1}<1001/1000$, and
$2e/3<1/20$. Their resulting sum is below $677/1000$. These are
conservative rational bounds, not a new computational leg.

At the head $0\le y\le\eta$, let $X$ be a bound for $|x|$. For the actual
real parameters the weight is at least one, and $|\sigma|\le X+y$ gives

$$
\int_0^\eta |\sigma|^{-2/3}(1-a^6y^2)^{-1/2}\,dy
\ge 3\big((X+\eta)^{1/3}-X^{1/3}\big).
$$

Subtracting this lower bound has the correct direction. No value of the
singular negative power at zero is evaluated. At $a=0$ the same head formula
integrates $y^{-2/3}$; it does not assert that the scaled circle exists there.

For $|y-2|\le\delta$, the distances satisfy
$|\sigma-2i|\ge|y-2|$ and $|\sigma+2i|>0$. If $C$ bounds the numerator
times weight divided by $3|\sigma+2i|^{1/2}$, then the positive part of the
window integral is bounded by

$$
C\int_{2-\delta}^{2+\delta}|y-2|^{-1/2}\,dy
=4C\sqrt\delta.
$$

Writing $R\ge\sup|\sigma|$, the subtracted part is at least
$2\delta R^{-2/3}$, again because the weight is at least one. The code
subtracts precisely this conservative lower bound. Conjugation doubles the
head, regular pieces, and window; the tail bound above already covers both
tails. None is counted with a missing or extra symmetry factor.

All thirteen parameter boxes feed their full balls into these expressions.
The successful full run bounds $I(a)$ above by a negative number on every
box. Since $L(a)=\Phi(c)+aI(a)$ and $a>0$, this proves a strict inequality
even as $a$ tends to zero. A positive uniform lower cutoff on $a$ has not been
used.

## 3. Do branch choices, endpoint extensions, or stopping rules invalidate the balls?

For $a>0$, a root $U$ of $U^2-sU-a^6=0$ is nonzero. If $u^3=U$, expansion
of $(u-a^2/u)^3+3a^2(u-a^2/u)$ gives $U-a^6/U=s$. Multiplying $u$ by the
three cube roots of unity gives all three roots, counted with multiplicity:
their sum is zero, their pairwise-product sum is $3a^2$, and their product
is $U-a^6/U=s$, so their product polynomial is exactly $z^3+3a^2z-s$.
Away from the critical values they are distinct: the factorization

$$
(z^2+a^2)^2(z^2+4a^2)=s^2+4a^6
$$

identifies precisely the critical-value obstruction. The other quadratic
root is $-a^6/U$ and its cube roots can be chosen as $-a^2/u_j$; these
produce exactly the same $z_j$. Thus either resolvent root and any starting
cube root give the same symmetric numerator. The formula extends continuously
for that numerator at a simple critical value, even though the density is
infinite there.

The code's rotated square root $i\sqrt{-v}$ squares to $v$, and its rotated
cube root $-\sqrt[3]{-v}$ cubes to $v$. The midpoint-based selection chooses
one of two permitted resolvent roots; it is not used as an estimate of the
root. Branch discontinuity does not invalidate pointwise enclosures. The
argument needs the documented enclosing semantics of arb/acb, including
branch-cut enclosures, but never calls an analytic complex quadrature rule.
The independent prescribed-root diagnostic tests this interface using quadratic
division instead of Cardano, including real and imaginary cut crossings and
near-critical points. Its finite scope is stated in the report.

Let a routine enclose an actual integrand on a piece by $[v_-,v_+]$ and the
nonnegative exact piece width by $[d_-,d_+]$. An upper rectangle bound is
$v_+d_+$ when $v_+\ge0$, and $v_+d_-$ when $v_+<0$. A lower rectangle
bound is $v_-d_-$ when $v_-\ge0$, and $v_-d_+$ when $v_-<0$. These four
cases are exactly `piece_bound`. Ball evaluation of the products and sums
then encloses the chosen scalar bounds. Taking an upper endpoint at the end
preserves an upper inequality. For a returned lower-bound ball, its lower
endpoint is a valid scalar lower bound. The rounded lower control stated in
the proof and the conservative one in the report lie below that endpoint;
the entire displayed ball is not asserted to be a scalar lower bound.

The adaptive integration routine starts with ordered exact dyadic endpoints.
Its midpoint is representable at the working precision and lies between the
two representable endpoints; subdivision therefore preserves the interval
union. All initial endpoints have the working precision or fewer significant
bits. Even if further subdivision ceases to shorten a piece, an accepted
finite rectangle remains a bound. The tolerance and the floating number
`0.8` occur only in subdivision decisions. Acceptance at the depth cap does
not claim an error tolerance: it retains that same rectangle bound. A
nonfinite enclosure at the cap raises `ArithmeticError`. In the parameter
cover, an unresolved box narrower than $2^{-40}$ instead records a failed
obligation. Neither route turns an unresolved enclosure into success.

In the large-parameter window, write $t=\pi-\beta$. For $\theta,t$ in
$[0,\pi]$,

$$
|s-s_+|=2|\sin((\theta-t)/2)|
\ge\frac2\pi|\theta-t|.
$$

For any interval $[A,B]$ containing $t$,

$$
\int_A^B |\theta-t|^{-1/2}\,d\theta
=2\sqrt{t-A}+2\sqrt{B-t}\le2\sqrt{2(B-A)}.
$$

The code's coefficient encloses the numerator divided by
$3|s-s_-|^{1/2}$. Multiplication by
$\sqrt{\pi/2}\,2\sqrt{2(B-A)}$ is therefore an upper bound over the whole
window. The inclusion and interior tests are essential and are executed for
every accepted box.

The upper regular integral ends at $\pi_+\ge\pi$, whereas the lower
control ends at $\pi_-\le\pi$ and discards the window. Nonnegativity gives
the stated directions. The upper extension cannot inadvertently cross the
second critical angle. Indeed, the accepted test `w_hi < PI` means
$w_{\rm hi}<\pi_-$, while its construction gives
$w_{\rm hi}\ge\pi_+-\beta_{\rm lo}+\text{spread}$ with positive spread.
It follows that $\pi_+-\pi_-<\beta_{\rm lo}$, so
$\pi+\beta>\pi_+$ throughout the box. The same window tests keep
$\pi-\beta$ strictly between zero and $\pi$. This also justifies the
small auxiliary extension of the parameter cover past $\pi/2$: $\sin\beta$
stays positive, and $c=\cos\beta$ with $a^3=\sin\beta/2$ still places the
critical values on the circle. No assumption $c>0$ is imported into this
regime.

The initial parameter endpoints are increasing dyadic roundings of a linear
grid. Bisection preserves their order. A successful box is accepted only if
its enclosing upper length is strictly below the enclosed $L_0-1/100$;
successive accepted endpoints are explicitly checked to match and the final
one must be the upper endpoint. The separate overlap checks connect this
closed cover to the small-$a$ cover. The printed minimum-margin summary is
not needed for this implication: the strict comparison has already been made
on each accepted box.

### The four failed diagnostic calibration assertions

The retained diagnostic tests four endpoint identities that are stronger than
these enclosure requirements. For example, it expects the upper and lower
bounds of the ball constructed as `arb(3, 1)` to be exactly $4$ and $2$.
The supplied API documentation expressly permits upward rounding of a
constructor radius. For a radius $1+\varepsilon$ the correct interval is
$[2-\varepsilon,4+\varepsilon]$, and the rectangle code is required to
preserve these enclosing endpoints, not to replace them by $2,4$.

Similarly, if the negative test value is
$[-3-\varepsilon,-1+\varepsilon]$ and its width is
$[3/4-\delta,5/4+\delta]$, the correct upper product is
$(-1+\varepsilon)(3/4-\delta)$ and the lower product is
$(-3-\varepsilon)(5/4+\delta)$. They need not equal $-3/4,-15/4$.
The positive and sign-changing cases have the same issue. The endpoint
inequalities just proved remain valid for outward radii.

The executed diagnostic reported four failed equalities and did not print the
actual endpoint values. Therefore this record does not claim a measured value
for $\varepsilon$ or $\delta$, or a confirmed numerical diagnosis of each
failure. It identifies the logical defect in those calibration assertions and
does not use them as successful checks. Their failure alone supplies no
counterexample to an enclosing rectangle bound. The exact driver is preserved
unchanged, with its nonzero outcome. A corrected and instrumented calibration
would be a new diagnostic record; it was not run in this examination.
