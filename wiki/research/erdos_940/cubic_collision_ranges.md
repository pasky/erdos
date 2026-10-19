---
name: research/erdos_940/cubic_collision_ranges
title: Controlled ranges in the cubic collision count
desc: Coordinate-sharing collisions and bounded secant, binary-norm, and binary-trace ratio strata are controlled; their unrestricted tails remain open.
tags: []
sources: []
created: 2026-09-22T03:46:38Z
updated: 2026-09-22T23:09:46Z
---


# Controlled ranges in the cubic collision count

***

## Status

The estimates below are proved. They remove several ranges at the desired
$O(N^3)$ scale from the [cubic energy route](energy_and_multiplicity.md). They
do not bound the full energy or establish positive density.

Fix positive integers $a_1,a_2,a_3$, and count pairs
$\mathbf x,\mathbf y\in[1,N]^3\cap\mathbb Z^3$ with


$$
F(\mathbf x)=F(\mathbf y),\qquad F(\mathbf x)=\sum_i a_i x_i^3.
$$


Write $\mathbf h=\mathbf x-\mathbf y$. For $\mathbf h\ne0$, write
$\mathbf h=t\mathbf k$, where $t>0$ and $\mathbf k$ is primitive. For every
fixed $0<\eta<1/2$, the union of the following three ranges contributes
$O_{\mathbf a,\eta}(N^3)$:


$$
h_1h_2h_3=0,
\qquad
0<\|\mathbf h\|_\infty\le N^{2/3-\eta},
\qquad
\|\mathbf k\|_\infty\le N^{1/2-\eta}.
\tag{1}
$$


The last two ranges have power-saving bounds after coordinate-zero differences
are removed.

For the special coefficients $(1,2,4)$, the later argument in
[Coordinate-zero differences](#coordinate-zero-differences-have-a-power-saving-for-distinct-cube-classes)
also gives a power saving in the first range. It removes those inputs from the
logarithmic-multiplicity problem at a cost of $o(N^3)$.

## A uniform binary quadratic bound

Fix $L>0$ and $\varepsilon>0$. If $A,B,m$ are nonzero integers of absolute value
at most $N^L$, with $N\ge2$, then


$$
\#\{(u,v)\in[-N,N]^2\cap\mathbb Z^2:Au^2+Bv^2=m\}
\ll_{L,\varepsilon}N^\varepsilon.
\tag{2}
$$


Set $D=-AB$ and $n=Am$. Multiplication by $A$ gives $(Au)^2-Dv^2=n$. If $D=d^2$
is a square, factorization into $(Au-dv)(Au+dv)=n$ bounds the count by
$2\tau(|n|)$.

Otherwise put $K=\mathbb Q(\sqrt D)$. Each solution determines a distinct
algebraic integer


$$
\alpha=Au+v\sqrt D\in\mathcal O_K,
\qquad N_{K/\mathbb Q}(\alpha)=n.
$$


There are at most $\tau(|n|)$ integral ideals of norm $|n|$, uniformly in $K$.
At a split prime the number of ideals of norm $p^e$ is $e+1$; at a ramified
prime it is one; at an inert prime it is at most one. Multiply these bounds over
primes.

The relevant generators of any one principal ideal are uniformly controlled.
Both embeddings of $\alpha$ have absolute value at most


$$
U=N(|A|+\sqrt{|AB|})\le2N^{L+1}.
$$


In an imaginary quadratic field each ideal has at most six generators of a
prescribed norm. In a real quadratic field generators differ by units, while
their first absolute embedding lies between $|n|/U$ and $U$. A fundamental unit
whose first absolute embedding exceeds one has that embedding at least
$\varphi=(1+\sqrt5)/2$. Indeed, after adjusting its sign, a norm-one unit $z>1$
satisfies $z+z^{-1}\in\mathbb Z_{\ge3}$, and a norm-minus-one unit satisfies
$z-z^{-1}\in\mathbb Z_{\ge1}$. Thus only $O_L(\log N)$ units can occur in the
indicated interval, independently of the field.

We obtain $O_L(\tau(|Am|)\log N)$ solutions. The divisor bound, with its
exponent chosen in terms of $L,\varepsilon$, proves (2).

## A uniform ternary quadratic bound

If $ABC\ne0$ and $|A|,|B|,|C|,|M|\le N^L$, then


$$
\#\{(u,v,w)\in[-N,N]^3\cap\mathbb Z^3:
Au^2+Bv^2+Cw^2=M\}
\ll_{L,\varepsilon}N^{1+\varepsilon}.
\tag{3}
$$


For fixed $w$, apply (2) to $m=M-Cw^2$ when it is nonzero, increasing the fixed
height exponent as necessary. The exceptional equation $M-Cw^2=0$ has at most
two integral solutions $w$. For each, the homogeneous binary equation has $O(N)$
solutions, since fixing $v$ permits at most two values of $u$. This proves (3),
without a primitivity or nonsquare-discriminant hypothesis. Fixed constant
multiples of $N$ in the coordinate bounds cause no change.

## Applying the bound to cubic differences

Put $u_i=x_i+y_i$. The identity $4(x_i^3-y_i^3)=h_i(3u_i^2+h_i^2)$ gives


$$
3\sum_i a_i h_i u_i^2=-\sum_i a_i h_i^3.
\tag{4}
$$


When $h_1h_2h_3\ne0$, equation (3) applies uniformly for each $\mathbf h$; its
coefficients and target have polynomial height in $N$. Ignoring parity and
positivity restrictions only enlarges the count. Consequently, for
$1\le H\le N$,


$$
E_{\mathrm{short}}(N,H)
\ll_{\mathbf a,\varepsilon}N^{1+\varepsilon}H^3.
\tag{5}
$$


Taking $H=N^{2/3-\eta}$ and $\varepsilon<3\eta$ gives a power saving over $N^3$.

Alternatively, after $\mathbf h=t\mathbf k$ and division by $t$, equation (4)
becomes


$$
3\sum_i a_i k_i u_i^2=-t^2C(\mathbf k),\qquad
C(\mathbf k)=\sum_i a_i k_i^3.
\tag{6}
$$


For $K=\|\mathbf k\|_\infty$ one has $t\le N/K$, and the target is
$O_{\mathbf a}(N^2K)$, so (3) is uniform here too. Since $O(m^2)$ primitive
vectors have maximum norm $m$,


$$
E_{\mathrm{direction}}(N,K_0)
\ll_{\mathbf a,\varepsilon}
N^{1+\varepsilon}\sum_{\substack{\mathbf k\text{ primitive}\\
0<\|\mathbf k\|_\infty\le K_0}}
\frac{N}{\|\mathbf k\|_\infty}
\ll_{\mathbf a,\varepsilon}N^{2+\varepsilon}K_0^2.
\tag{7}
$$


Coordinate-zero directions are excluded here and handled next. Taking
$K_0=N^{1/2-\eta}$ and $\varepsilon<2\eta$ gives a power saving.

## Coordinate-zero differences

Let $f(\alpha)=\sum_{n\le N}e(\alpha n^3)$. The number of collisions with
$x_3=y_3$ is


$$
N\int_0^1|f(a_1\alpha)f(a_2\alpha)|^2\,d\alpha
\le N\int_0^1|f(\alpha)|^4\,d\alpha
\ll N^3.
\tag{8}
$$


The inequality uses Cauchy--Schwarz and invariance of the integral under
multiplication of $\alpha$ by a positive integer. The log-free fourth moment
follows from [Heath-Brown, *The density of rational points on cubic surfaces*,
Theorem
1](https://ora.ox.ac.uk/objects/uuid%3A04b73804-727f-43e4-bb2d-b99e175903e6/files/m9ec4d87761c586cdadad7b977f9b3bb8).
Its statement was checked in the indexed primary text: for a nonsingular cubic
surface with three rational coplanar lines, integer points off the rational
lines have count $O_\varepsilon(N^{4/3+\varepsilon})$. The Fermat cubic surface
meets these hypotheses; its finitely many lines contribute $O(N^2)$. Applying
(8) to each coordinate proves the first bound in (1).

## The remaining range and unsuccessful analytic transfers

For $(a_1,a_2,a_3)=(1,2,4)$, $C(\mathbf k)$ never vanishes at a nonzero rational
vector: the nonzero summands have distinct $2$-adic valuations modulo three.
Thus all remaining fibers are nonsingular. The part of the energy route not
controlled by (1) is confined to


$$
k_1k_2k_3\ne0,\qquad
N^{1/2-\eta}<K\le N,\qquad
tK>N^{2/3-\eta}.
\tag{9}
$$


This still contains the critical shell $K\asymp N$, $t=1$. Its expected $O(1)$
count per direction has not been proved on average. The weaker bounded-fiber
criterion in the [energy note](energy_and_multiplicity.md) could bypass a full
energy bound; it is not established either.

Direct use of [Browning--Heath-Brown, *Counting rational points on quadric
surfaces*, Theorem 1.1](https://arxiv.org/pdf/1801.00979) does not close this
range. Even when its hypothesis on the squarefull part of the determinant holds,
its bound contains $(\|Q\|^4/|\det Q|)^{5/8}$. For generic directions of size
$K$, our four-variable $Q_{\mathbf k}$ has height of order $K^3$ and determinant
of order $K^6$, giving a factor $K^{15/4}$. The resulting estimate is too large
to sum. Replacing $t$ by $t'=Kt$ balances the real coefficients but introduces
the sublattice $K\mid t'$ and rational coefficients; no estimate preserving the
necessary arithmetic saving under this operation was established. This rejects
the direct substitution into that theorem, not a sharper anisotropic average.

Fixing one coordinate in (6) gives another attempted transfer, through binary
quadratic norm equations. After choosing two same-sign coefficients, the
primitive diagonal positive binary form $[A,0,B]$ represents an ambiguous ideal
class: its inverse $[A,-0,B]$ is the same class. Varying diagonal factorizations
therefore does not average over the whole class group, and dividing an
unrestricted ideal count by the class number is unjustified. The target values
are also linked to $\mathbf k$, rather than running through a complete norm
interval.

The unconditional result inspected in [Browning--Munshi--Wang, *Beyond the
square-root barrier: cubic forms of Perazzo type*, Theorem
1.1](https://arxiv.org/html/2604.19045v1) concerns the singular fourfold
$\sum_i x_i y_i^2=0$. The diagonal collision fourfold is smooth, so it is not
linearly equivalent to that example. In difference coordinates the additional
term $C(\mathbf h)$ has the same cubic scale as $3\sum_i a_i h_i u_i^2$ in the
outstanding range; simply omitting it is not a valid application of the theorem.
No perturbation or averaged estimate bridging this difference was proved.

## The precise complete-sum change in the Perazzo transfer

A subsequent check identified the arithmetic step, rather than merely the
geometric distinction, that prevents the direct transfer. The calculation
below is self-contained. It supplies no new global energy estimate.

Let $p\nmid6a_1a_2a_3$, let $\chi$ be the quadratic character modulo $p$,
extended by zero, and let $\tau_p=\sum_v\chi(v)e_p(v)$. Put

$$
H(\mathbf h,\mathbf u)=C(\mathbf h)+3\sum_i a_i h_i u_i^2,
\qquad C(\mathbf h)=\sum_i a_i h_i^3.
$$

For frequencies $\boldsymbol\ell,\mathbf s\in\mathbb F_p^3$ with
$s_1s_2s_3\ne0$, define

$$
T_p=\sum_{\lambda\ne0}\sum_{\mathbf h,\mathbf u}
 e_p\bigl(\lambda H+\boldsymbol\ell\cdot\mathbf h+
 \mathbf s\cdot\mathbf u\bigr).
$$

Terms with some $h_i=0$ vanish on summing over $u_i$. Completing the three
quadratic squares in the other terms gives exactly

$$
T_p=\tau_p^3\chi(27a_1a_2a_3)
\sum_{h_1h_2h_3\ne0}\chi(h_1h_2h_3)e_p(\boldsymbol\ell\cdot\mathbf h)
\sum_{\lambda\ne0}\chi(\lambda)
e_p\bigl(\lambda C(\mathbf h)-D(\mathbf h)/\lambda\bigr),       \tag{10}
$$

where

$$
D(\mathbf h)=\sum_i\frac{s_i^2}{12a_i h_i},\qquad
L(\mathbf h)=h_1h_2h_3D(\mathbf h).
$$


If the cubic term is **identically removed**, the inner sum is
$\tau_p\chi(-D)$, so (10) reduces to

$$
T_p^{(0)}=p^2\chi(27a_1a_2a_3)
\sum_{h_1h_2h_3\ne0}\chi(-L(\mathbf h))
 e_p(\boldsymbol\ell\cdot\mathbf h).                       \tag{11}
$$

Here $L$ is a nondegenerate ternary quadratic form: its three nonzero mixed-term
coefficients are $s_i^2/(12a_i)$. For any nondegenerate ternary quadratic form
$Q(\mathbf h)=\mathbf h^TM\mathbf h$, expansion of $\chi$ by its Gauss sum,
followed by completing squares, gives

$$
\sum_{\mathbf h}\chi(Q(\mathbf h))e_p(\boldsymbol\ell\cdot\mathbf h)
=p\chi(-\det M)
\begin{cases}
p-1,&\boldsymbol\ell^TM^{-1}\boldsymbol\ell=0,\\
-1,&\boldsymbol\ell^TM^{-1}\boldsymbol\ell\ne0.
\end{cases}                                                \tag{12}
$$

On each coordinate plane, $L$ is a nonzero constant times the product
of the other two coordinates; its character Fourier sum has magnitude
at most $p$. Intersections of two coordinate planes contribute zero.
Thus (11) has magnitude at most $4p^3$ outside the dual quadratic
condition in (12). This is the special finite-field cancellation behind
the unperturbed calculation.

For $C(\mathbf h)\ne0$, the inner sum of (10) instead has the Salié identity

$$
\sum_{\lambda\ne0}\chi(\lambda)e_p(C\lambda-D/\lambda)
=\tau_p\chi(C)\sum_{v^2=-4CD}e_p(v).                       \tag{13}
$$

For completeness, sum both sides against $e_p(tD)$ over $D$. At
$t\ne0$, each sum is $p\chi(t)e_p(C/t)$; at $t=0$, each is zero.
On the right this follows by one quadratic Gauss sum. This proves (13),
including $D=0$.

Accordingly the part of $T_p$ with $C(\mathbf h)\ne0$ is

$$
p^2\chi(27a_1a_2a_3)
\sum_{\substack{h_1h_2h_3\ne0\\C(\mathbf h)\ne0}}
\chi(h_1h_2h_3C(\mathbf h))e_p(\boldsymbol\ell\cdot\mathbf h)
\sum_{v^2=-4C(\mathbf h)D(\mathbf h)}e_p(v).                \tag{14}
$$

Directions with $C=0$ give the corresponding restricted part of (11).
Recovering a $p^3$ estimate now requires an $O(p)$ bound for the combined
sum after its $p^2$ prefactor is removed. Formula (12) does not supply
that bound: the cubic term remains in the phase and in the square-root
condition of (14). No needed cancellation estimate or subsequent modulus
average was proved. This rules out the direct substitution into the
unperturbed proof, not every possible treatment of the perturbed sum.

## Coordinate-zero differences have a power saving for distinct cube classes

The following strengthens the first range of (1). The external input is
[Salberger, *Counting rational points on projective varieties* (2023), Corollary
0.7, pp.
1094–1095](https://research.chalmers.se/publication/535246/file/535246_Fulltext.pdf).
The theorem and its projective-height convention were checked in the full paper.
For a diagonal degree-$d$ surface in $\mathbb P^3$ with nonzero rational
coefficients, its rational points of height at most $B$ outside all
two-term-zero-subsum loci number $O_d(B^{3/\sqrt d}(\log B)^4+1)$, uniformly in
the coefficients.

Let $a,b>0$ be rational, with $a/b\notin\mathbb Q^{\times3}$. Then

$$
\#\{(x,y,u,v)\in[1,N]^4\cap\mathbb Z^4:
 ax^3+by^3=au^3+bv^3,\ (x,y)\ne(u,v)\}
\ll N^{\sqrt3}(1+\log N)^4.                         \tag{15}
$$

Indeed, a same-sign two-term subsum cannot vanish. A subsum
$ax^3-au^3=0$ forces $x=u$ and then $y=v$, and likewise for the
other matching pair. A crossed subsum, such as $ax^3-bv^3=0$,
would make $a/b$ a rational cube. Thus every primitive nontrivial
positive solution lies in Salberger's open subset. Splitting a general
solution by its coordinate gcd gives

$$
\sum_{g\le N}O\bigl((N/g)^{\sqrt3}(1+\log(N/g))^4+1\bigr)
\ll N^{\sqrt3}(1+\log N)^4,
$$

since $\sqrt3>1$. This proves (15).

Consequently, if the three coefficients of $F$ have distinct rational
cube classes, the number $E_0(N)$ of off-diagonal collisions having at
least one equal coordinate satisfies

$$
E_0(N)\ll N^{1+\sqrt3}(1+\log N)^4=o(N^3).           \tag{16}
$$

For each choice of the common coordinate, sum (15) over its $N$ possible
values. In particular, (16) applies to $F=x^3+2y^3+4z^3$.

### Removal from the logarithmic moment

For this special form, let $Z_N$ be the inputs in $[1,N]^3$ having a
distinct equal-output partner with some equal coordinate. Let $g_N(n)$
count the representations remaining after deleting $Z_N$. Then
$|Z_N|\le E_0(N)$, and each remaining fiber is coordinatewise injective;
in particular $g_N(n)\le N$.

Writing $R_N(n)=g_N(n)+b_N(n)$, use $R_N(n)\le N^2$ and
$\log(1+t)\le t$ to obtain, also when $g_N(n)=0$,

$$
0\le R_N(n)\log R_N(n)-g_N(n)\log g_N(n)
\le b_N(n)(2\log N+1).
$$

Here $0\log0=0$. Since $\sum_n b_N(n)=|Z_N|$, (16) implies

$$
\sum_n\bigl(R_N(n)\log R_N(n)-g_N(n)\log g_N(n)\bigr)
\ll N^{1+\sqrt3}(1+\log N)^5=o(N^3).                 \tag{17}
$$

Thus deleting these inputs preserves the bounded-logarithmic-moment
question, including the effect on their surviving fiber-mates. The
remaining fibers, whose representations differ in all three coordinates,
are not bounded by this argument. No density conclusion follows from
(15)–(17) alone.

### Near neighbors for arbitrary positive coefficients

There is also a useful conclusion without the distinct-cube-class
hypothesis. Let $B_N^{(0)}(\varepsilon)$ count inputs having a distinct
equal-output partner within Euclidean distance $\varepsilon N$, with at
least one equal coordinate. Then for every positive ternary diagonal
cubic,

$$
B_N^{(0)}(\varepsilon)
\le6\varepsilon N^3+3N^2
 +O\bigl(N^{1+\sqrt3}(1+\log N)^4\bigr).                \tag{18}
$$

The bound remains valid in a fixed interior box.

To prove this, fix the common coordinate $i$ and write $j,k$ for the
other two. Salberger's open subset contributes the power-saving term
as above, even if the coefficient ratio is a cube. The only remaining
off-diagonal positive solutions have

$$
y_j=cx_k,\qquad y_k=x_j/c,\qquad
c=(a_k/a_j)^{1/3}\in\mathbb Q.
$$

Indeed, the same-sign two-term subsums cannot vanish, the same-coordinate
subsum forces the diagonal, and either crossed subsum forces this weighted
swap. The distance condition implies $|x_j-cx_k|\le\varepsilon N$.
Fixing $x_i,x_k$ leaves at most $2\varepsilon N+1$ possibilities for
$x_j$. Sum over the three choices of $i$ to prove (18).

It follows that

$$
\lim_{\varepsilon\downarrow0}\limsup_{N\to\infty}
 B_N^{(0)}(\varepsilon)/N^3=0.
$$

Thus the [near-neighbor criterion](energy_and_multiplicity.md) may now
restrict entirely to partners differing in all three coordinates, for
every positive coefficient tuple. That remaining existence estimate,
at distance $\varepsilon N$ with fixed $\varepsilon$, is still unproved.

## A uniform bound on each secant-ratio slice

The following additional estimates are proved. They control a new
arithmetic stratum of the near-neighbor count, but not all its inputs.

Write an ordered nontrivial collision as

$$
F(x)=F(x+tk),\qquad t\ge1,\quad k\in\mathbb Z^3\text{ primitive},
$$

and put

$$
K=\|k\|_\infty,\quad C=F(k),\quad
B=\sum_i a_i x_i k_i^2,\quad A=\sum_i a_i x_i^2k_i.
$$

Throughout this section assume $k_1k_2k_3C\ne0$. For the special
form $x^3+2y^3+4z^3$, the condition $C\ne0$ is automatic.

**Slice lemma.** For every $q\in\mathbb Q$, the number of
$x\in[1,N]^3\cap\mathbb Z^3$ satisfying

$$
B=qC,\qquad F(x+tk)=F(x)
$$

is

$$
O_{\mathbf a}(1+N/K),                                    \tag{19}
$$

uniformly in $q,k,t,N$. Requiring $x+tk\in[1,N]^3$ can only decrease
this count.

**Proof.** The collision equation is $3A+3tB+t^2C=0$. Set $z=x-qk$.
The two equations become

$$
\sum_i a_i k_i^2z_i=0,\qquad
\sum_i a_i k_i z_i^2
=-\left(q^2+tq+\frac{t^2}{3}\right)C.                    \tag{20}
$$

The scalar in parentheses is $(q+t/2)^2+t^2/12>0$.

Let $n=(a_i k_i^2)_i$, $M=\operatorname{diag}(a_i k_i)$, and
$W=n^\perp$. The quadratic form $z^TMz$ is nondegenerate on $W$.
Indeed, a vector $z$ in the radical of its restriction has
$Mz\in\mathbb Rn$, so $z\in\mathbb Rk$. Membership in $W$ and
$n\cdot k=C\ne0$ then force $z=0$. Its nonzero level in (20) is
therefore a nonsingular affine conic and contains no line. Equivalently,
the homogeneous ternary matrix of that conic has rank three.

If the affine plane $B=qC$ has an integral point, its integral points
are a coset of the rank-two lattice

$$
\Lambda=\{v\in\mathbb Z^3:n\cdot v=0\},\qquad
\det\Lambda=\frac{\|n\|_2}{\gcd(a_1k_1^2,a_2k_2^2,a_3k_3^2)}
\asymp_{\mathbf a}K^2.                                  \tag{21}
$$

For each prime, some $k_i$ is a unit; hence the denominator in (21)
divides $\operatorname{lcm}(a_1,a_2,a_3)$.

Choose a shortest nonzero lattice vector $v$. It is primitive in
$\Lambda$, and the two-dimensional lattice bound gives
$\|v\|\ll\sqrt{\det\Lambda}$. Extend it to a lattice basis.
The parallel lattice lines in direction $v$ are spaced
$\det\Lambda/\|v\|\gg\sqrt{\det\Lambda}\asymp_{\mathbf a}K$.
Only $O_{\mathbf a}(1+N/K)$ such lines meet the box. Each meets the
conic at most twice, proving (19). $\square$

## Fixed normalized ratios and bounded denominators

Define the normalized secant ratio

$$
\rho=\frac{B}{tC}.
$$

It determines the third intersection of the secant with the cubic:
its parameter on the line $x+s(tk)$ is $s=-1-3\rho$.

For a prescribed rational $\rho$, let $E_\rho(N,H)$ count ordered
collisions in $[1,N]^3$ with $0<tK\le H$ and $k_1k_2k_3C\ne0$.
For $1\le H\le N$,

$$
E_\rho(N,H)\ll_{\mathbf a}H^3+NH^2
\ll_{\mathbf a}NH^2,                                    \tag{22}
$$

with a constant independent of $\rho$. For each $k,t$, apply (19)
with $q=t\rho$. There are $O(m^2)$ primitive directions of height $m$,
so the resulting sum is bounded by

$$
\sum_{m\le H}m^2\frac Hm\left(1+\frac Nm\right)
\ll H^3+NH^2.
$$


There is also a bound allowing infinitely many normalized ratios as
$N$ varies. Fix $D\ge1$ and $0<\eta\le A_0:=\sum_i a_i$. Let
$E_{D,\eta}(N,H)$ count the same pairs, restricted by

$$
|F(k)|\ge\eta K^3,
\qquad \operatorname{den}\!\left(\frac{B}{tC}\right)\le D,
$$

where $\operatorname{den}$ means the reduced positive denominator. Then

$$
E_{D,\eta}(N,H)\ll_{\mathbf a}
\frac{D^2}{\eta}N^2H.                                   \tag{23}
$$


To prove this, partition the displacements into dyadic shells
$J/2<tK\le J$. Since $B\le A_0NK^2$, a contributing ratio satisfies

$$
|\rho|\le\frac{2A_0N}{\eta J}=:L.
$$

There are at most
$\sum_{d\le D}(2Ld+1)\ll_{\mathbf a}D^2N/(\eta J)$ such rationals
of denominator at most $D$. Apply (22), with $H=J$, to each. This
bounds the shell by $O_{\mathbf a}(D^2N^2J/\eta)$. The upper endpoints
of the shells up to $H$ sum to at most $2H$, proving (23).

For fixed $D,\eta$, the full collision energy on this stratum is
$O_{\mathbf a,D,\eta}(N^3)$. Its near-neighbor **existence** count at
Euclidean distance at most $\varepsilon N$ is at most

$$
O_{\mathbf a}\!\left(D^2\varepsilon N^3/\eta\right),        \tag{24}
$$

because every such input participates in an ordered pair counted by
(23). Thus this stratum satisfies the vanishing near-neighbor limit
required in the [density criterion](energy_and_multiplicity.md).

**Remaining gap.** No uniform tail estimate permits $D\to\infty$ or
$\eta\downarrow0$ while retaining almost all relevant input mass.
Ratios can have reduced denominators growing with $N$, and directions
can have $|F(k)|/K^3$ arbitrarily small. The denominator in (23) is that
of $B/(tC)$, not the denominator $C/\gcd(C,3B)$ of the third secant
point in primitive projective coordinates. The bounds do not imply
the full near-neighbor estimate, bounded typical multiplicity, or
positive density.

## Binary norm ratios of small height

This estimate concerns $F=x^3+y^3+cz^3$ with fixed $c\in\mathbb N$,
not the distinct-coefficient form $x^3+2y^3+4z^3$. Put
$Q(x,y)=x^2-xy+y^2$. Let $E_D(N)$ count ordered collisions

$$
F(x,y,z)=F(u,v,w),\qquad x,y,z,u,v,w\in[1,N]\cap\mathbb Z,
$$

such that $Q(u,v)/Q(x,y)=p/q$ in lowest terms with
$\max(p,q)\le D$, excluding the identical triple and the swap
$(u,v,w)=(y,x,z)$. For all $N\ge2$, $D\ge1$, and $\varepsilon>0$,

$$
E_D(N)\ll_{c,\varepsilon}D N^{2+\varepsilon}.
\tag{25}
$$


Write $m=Q(x,y)$, $m'=Q(u,v)$ and
$H=x^3+y^3-u^3-v^3$. First suppose $H\ne0$. Fix $(x,y)$.
Since $q\mid m$, at most $D\tau(m)$ pairs $(p,q)$ can occur,
and each determines $m'=pm/q$. All contributing norms are at most
$N^2$. The elementary norm bound

$$
\#\{(u,v)\in\mathbb Z^2:Q(u,v)=m'\}\le6\tau(m')
$$

follows in the Eisenstein integers: there are at most $\tau(m')$
integral ideals of norm $m'$, and each principal ideal has six
generators. For each resulting binary quadruple, the equation

$$
(w-z)(w^2+wz+z^2)=H/c\ne0
$$

has no solutions unless $c\mid H$, and otherwise at most
$2\tau(|H/c|)$ solutions. Fixing the nonzero difference $w-z$
leaves a quadratic equation. Since $|H|\le2N^3$, the divisor bound,
with its exponents chosen sufficiently small, proves (25) for $H\ne0$.

If $H=0$, then $z=w$. Write
$s=x+y$, $t=u+v$, $d=x-y$, $e=u-v$.
From $sm=tm'$ and $m'/m=p/q$, we obtain

$$
s=p\ell,\qquad t=q\ell,\qquad
1\le\ell\le\frac{2N}{\max(p,q)}.
$$

The identities $4m=s^2+3d^2$ and $4m'=t^2+3e^2$ give

$$
3q e^2-3p d^2=(p^3-q^3)\ell^2.
\tag{26}
$$

If $p=q$, then $p=q=1$ and equal trace and norm force only the excluded
identical pair and swap. Otherwise the right side of (26) is nonzero. The
coefficients and target have polynomial height in $N$, since $p,q\le2N$ here.
The [uniform binary quadratic bound](#a-uniform-binary-quadratic-bound) gives
$O_\varepsilon(N^\varepsilon)$ choices of $(d,e)$ per $(p,q,\ell)$. Thus the
binary quadruples number at most

$$
\ll_\varepsilon N^\varepsilon
\sum_{k\le\min(D,2N)}2k\left\lfloor\frac{2N}{k}\right\rfloor
\ll_\varepsilon D N^{1+\varepsilon}.
$$

The $N$ choices $z=w$ complete the proof of (25).

For any fixed $0<\eta<1$, take $D=N^{1-\eta}$ and $\varepsilon<\eta$. Removing
all endpoints of these nontrivial collisions costs $o(N^3)$ inputs, and also
$o(N^3)$ in the logarithmic moment, since $R_N(n)\le N^2$. The unrestricted norm
ratios can have height of order $N^2$, however. No bound for their complementary
input mass has been proved. In particular (25) does not bound the
[cross-coordinate correlation or conditional
entropy](energy_and_multiplicity.md#the-cross-coordinate-correlation-still-needed).

## Nearly vanishing directions near a balanced positive ray

The following geometric observation is checked. It does not extend the
exact coordinate-sharing count to nearby directions.

For $F=\sum_{i=1}^3 a_i x_i^3$, $a_i>0$, put
$X_i=a_i^{1/3}x_i$, $H_i=a_i^{1/3}h_i$ and
$R=\max_i|H_i|>0$. Assume

$$
|X_i-M|\le\delta M,\qquad R\le\varepsilon M,\qquad
F(\mathbf x+\mathbf h)=F(\mathbf x),
$$

where $\delta+\varepsilon$ is sufficiently small. Expanding the
collision identity gives

$$
S:=H_1+H_2+H_3=O((\delta+\varepsilon)R).
$$

Indeed the linear term is $3M^2S+O(\delta M^2R)$, while the
quadratic and cubic terms are $O(MR^2+R^3)$.
Using

$$
\sum_iH_i^3=3H_1H_2H_3+
S\left(\sum_iH_i^2-\sum_{i<j}H_iH_j\right),
$$

we conclude that

$$
|F(\mathbf h)|\le\eta R^3
\quad\Longrightarrow\quad
\min_i|H_i|\ll(\eta+\delta+\varepsilon)R.
\tag{27}
$$

For the last implication, $|S|\le R/2$ makes the largest two
$|H_i|$ comparable, and the product is
$O((\eta+\delta+\varepsilon)R^3)$.

Thus nearly vanishing directions in this cone approach weighted
coordinate-swap directions. But for nonzero integer differences with
$\|h\|_\infty\le H$ and one coordinate at most $L$, the available
ternary quadratic bound gives only
$O_{\mathbf a,\nu}(N^{1+\nu}H^2L)$. At $H$ proportional to $N$
and $L$ a fixed small fraction of $H$, this is not $o(N^3)$.
Continuity of the real geometry therefore does not justify replacing
the uncontrolled thin sector by the already controlled exact
coordinate-zero locus. No near-neighbor existence estimate follows.

## Binary trace ratios, uniformly in the prescribed ratio

Fix $c\in\mathbb N$ and put $F(x,y,z)=x^3+y^3+cz^3$. Exclude
the collisions $(u,v,w)=(x,y,z)$ and $(y,x,z)$. For every reduced
positive rational $p/q$, the remaining collisions in $[1,N]^6$ with

$$
\frac{u+v}{x+y}=\frac pq
$$

number

$$
O_{c,\varepsilon}(N^{2+\varepsilon}),                    \tag{28}
$$

uniformly in $p,q$, even when their height grows with $N$.

Only $p,q\le2N$ can contribute. Write

$$
x+y=q\ell,\quad u+v=p\ell,\quad d=x-y,\quad e=u-v.
$$

Then

$$
H:=4c(w^3-z^3)
=\ell\bigl((q^3-p^3)\ell^2+3qd^2-3pe^2\bigr).          \tag{29}
$$

Suppose first that $z\ne w$. Fixing $(z,w)$ fixes a nonzero
$H=O_c(N^3)$, and $\ell\mid H$. Unless

$$
H/\ell-(q^3-p^3)\ell^2=0,                              \tag{30}
$$

the uniform binary quadratic bound (2) gives
$O_{c,\varepsilon}(N^\varepsilon)$ choices of $(d,e)$ for each
divisor $\ell$. All coefficients and targets have polynomial height
in $N$. The divisor bound, with smaller intermediate exponents,
proves (28) for this part.

Under (30), one has $qd^2=pe^2$. If $p/q$ is not a rational
square, then $d=e=0$. Enumerate $\ell\le2N/\max(p,q)$ instead.
Equation (29) prescribes a nonzero difference of cubes, which has
$O_{c,\varepsilon}(N^\varepsilon)$ solutions $(z,w)$: factor
$w^3-z^3=(w-z)(w^2+wz+z^2)$ and fix its first factor.

If $p=a^2,q=b^2$ with $(a,b)=1$, set $A=\max(a,b)$. The
homogeneous solutions are

$$
d=at,\qquad e=\pm bt,\qquad
\ell\le2N/A^2,\quad |t|\le N/A.
$$

Here $A\le\sqrt{2N}$ whenever $\ell$ exists. Thus there are
$O(N^2/A^3)$ pairs $(\ell,t)$. Each again prescribes a nonzero
difference of cubes, giving $O_{c,\varepsilon}(N^{2+\varepsilon})$
collisions. The case $p=q=1$ cannot satisfy (30) when $H\ne0$.

Finally let $z=w$. If $p=q$, then $p=q=1$, and equal binary
trace and cubic sum give only the excluded identical pair and swap.
Otherwise, for each $\ell\le2N/\max(p,q)$, (29) is a binary
quadratic equation with nonzero target. Apply (2) and then allow
the $N$ choices of $z=w$. This completes the proof.

There are $O(D^2)$ positive rational ratios of height at most $D$,
so their nontrivial collisions number

$$
O_{c,\varepsilon}(D^2N^{2+\varepsilon}).                 \tag{31}
$$

For every fixed $0<\eta<1/2$, taking
$D=N^{1/2-\eta}$ and $\varepsilon<2\eta$ permits removal of
all endpoints of these collisions at cost $o(N^3)$. The same is
true for their contribution to the logarithmic moment, by the
deletion inequality (17) and $R_N(n)\le N^2$.

Unlike the small-direction range, (28) permits unrestricted
displacements. Unlike (25), it imposes no small-height condition on
the binary norm ratio. Neither observation controls its complementary
trace-ratio tail. A fiber can have many distinct traces of size
comparable to $N$ with pairwise small gcd, so ordinary pigeonhole
arguments do not supply a ratio of height at most $N^{1/2-\eta}$.
No typical-multiplicity estimate or density conclusion follows.
