---
name: research/erdos_132/second_distance_extremality
title: Exact second-distance extremality without five concyclic points
desc: |
  Analytic even-polygon deformations attain the 3n/2 second-distance
  bound without five concyclic points, but their whole small neighborhood
  has linearly many rare distances by exact palette interlacing.
sources: []
research_state: closed
created: 2026-09-23T03:20:00Z
updated: 2026-10-14T00:26:52Z
---


# Exact second-distance extremality without five concyclic points

***

**Proposition.** For every $m\ge8$ divisible by four, there is a set of
$N=2m$ planar points such that its second-largest distance occurs exactly
$3m=3N/2$ times, yet no five of its points are concyclic.

Moreover, its strictly convex outer $m$-gon has uniform lengths in both
of its largest cyclic separation classes. Thus the parity condition in
[long_chord_rigidity](long_chord_rigidity.md) is essential. Exact or
near extremality in Vesztergombi's second-distance bound cannot by itself
force a circular fraction. This construction does not establish a small
total distance palette or bounded rarity, and is not a counterexample to
either assertion of Problem 132.

## 1. A regular initial configuration

Put $k=m/2$, $\theta=\pi/m$, $c=\cos\theta$, $s=\sin\theta$, and


$$
p_j=e^{2ij\theta},\qquad r=2c,\qquad D_0=2,
$$


where indices are modulo $m$. The regular outer polygon has $k$ diameter
pairs, $m$ pairs of length $r$ at cyclic separation $k-1$, and all other
distances strictly below $r$. Define


$$
\rho=\sqrt{5c^2-1}-c,\qquad H=\rho+c,\qquad
u_j=-\rho e^{i(2j+1)\theta}.
$$


We have $0<\rho<c$, the upper inequality following from
$\sqrt{5c^2-1}<2c$. Thus the inner points lie strictly inside the outer
polygon's incircle. The identity


$$
1+\rho^2+2\rho c=4c^2=r^2
$$


gives $|u_j-p_j|=|u_j-p_{j+1}|=r$. More generally,


$$
|u_j-p_l|^2=1+\rho^2+2\rho\cos((2l-2j-1)\theta).
$$


Its maximum occurs only for $l=j,j+1$. Also all inner--inner distances
are at most $2\rho<r$. Hence there are exactly $3m$ pairs at $r$, and
all undesignated inequalities are strict.

## 2. A full-rank analytic deformation

Set $a=k-1$. Since $k$ is even, $\gcd(a,m)=1$. In the variables
$v_0,\ldots,v_{m-1}\in\mathbb R^2$ and one additional real variable $D$,
impose


$$
|v_j-v_{j+a}|^2=r^2\quad(0\le j<m),\qquad
|v_j-v_{j+k}|^2=D^2\quad(0\le j<k). \tag{1}
$$


The differential of these $m+k$ equations has full row rank at
$(p_0,\ldots,p_{m-1},2)$. To see this, consider first a dependence on
the coordinate columns alone. Give the first family coefficients
$\alpha_j$, and the diameter edges coefficients
$\beta_j=\beta_{j+k}$. Write $\phi=\pi-2\theta$. The equilibrium
equation at $p_j$, after rotation by $p_j^{-1}$ and removal of the
common factor two, is


$$
\alpha_j(1-e^{i\phi})+
\alpha_{j-a}(1-e^{-i\phi})+2\beta_j=0.
$$


Its imaginary part gives $\alpha_j=\alpha_{j-a}$, so every $\alpha_j$
is one common $\alpha$. Its real part then gives
$\beta_j=-2c^2\alpha$. This is the entire coordinate stress space.
The additional $D$ column has pairing
$-4\sum_{j=0}^{k-1}\beta_j=-4k\beta_j$, which vanishes only when all
coefficients vanish. This proves full row rank.

The analytic implicit-function theorem gives a local solution manifold
of dimension $2m+1-(m+k)=k+1$. For every nearby outer solution,
construct $u_j(v)$ as the intersection near $u_j$ of the two radius-$r$
circles about $v_j,v_{j+1}$. The two circle gradients there are independent,
so this construction is analytic. The strict inequalities from Section 1
persist. Consequently every sufficiently nearby solution still has
exactly $k$ diameter pairs and $3m$ second-distance pairs.

## 3. Free anti-periodic radial velocities

Write an outer velocity as


$$
\dot v_j=(f_j+i g_j)p_j,\qquad f_j,g_j\in\mathbb R.
$$


The coordinate stress above, applied to the differentiated equations,
gives $\dot D=0$. The diameter equations give


$$
f_{j+k}=-f_j. \tag{2}
$$


The other equations give


$$
g_{j+a}-g_j=-\cot\theta(f_j+f_{j+a}). \tag{3}
$$


Conversely, any $k$ real values $f_0,\ldots,f_{k-1}$, extended by (2),
admit a solution of (3). Its only compatibility condition around the
single step-$a$ cycle is $\sum_j f_j=0$, already satisfied. The $g_j$
are unique up to a common rotation; choose this constant so that


$$
g_{j+k}=-g_j.
$$


Indeed, (3) makes $g_{j+k}+g_j$ constant on the step-$a$ cycle. Thus
the anti-periodic radial data are completely free and every such tangent
is realized by an analytic curve in the solution manifold.

## 4. Breaking outer five-point circles

If a fixed five-element index set $S$ remains concyclic to first order,
its radial velocities necessarily have the form


$$
f_j=A+B\cos(2j\theta)+C\sin(2j\theta),\qquad j\in S. \tag{4}
$$


These are the variations of the radius and the two center coordinates.
Condition (4) defines a proper linear subspace of the anti-periodic
data. If $S$ contains no full antipodal pair, its five values are
independent, whereas (4) has only three parameters. If it contains such
a pair, (2) forces $A=0$; five indices represent at least three different
antipodal pairs, giving at least three independent values but only two
remaining parameters.

There are finitely many five-element subsets. A tangent chosen outside
all their proper subspaces breaks every outer five-point circle along
its analytic curve, for all sufficiently small nonzero parameters.
Formally, the circle through any three of the selected points varies
analytically near the initial configuration. Failure of (4) makes one of
the other two circle equations have a nonzero first derivative.

## 5. Simultaneously breaking inner five-point circles

Put $w_j=e^{i(2j+1)\theta}$ and write
$\dot u_j=-w_j(\widehat f_j+i\widehat g_j)$, so $\widehat f_j$ is the
physical radial velocity on the inner circle. Differentiating the two
circle-intersection equations and adding them gives


$$
\widehat f_j=-\frac{(1+\rho c)(f_j+f_{j+1})
             -\rho s(g_{j+1}-g_j)}{2H}. \tag{5}
$$


This is an anti-periodic sequence. The linear map from $f$ to
$\widehat f$ is invertible on the anti-periodic space. To check this,
complexify and take its Fourier basis $f_j=z^j$, where $z^k=-1$.
Since $k$ is even, $z\ne-1$. Equations (2)--(3) give


$$
g_j=\cot\theta\frac{z-1}{z+1}z^j.
$$


Substitution into (5) gives the multiplier


$$
\widehat f_j=-\frac{(1+z)^2+4\rho c z}{2H(1+z)}z^j. \tag{6}
$$


It is nonzero: for $z=e^{i\omega}$, the numerator divided by $z$ is
$4\cos^2(\omega/2)+4\rho c>0$.

The argument of Section 4 applies to the inner circle as well, with
its angular offset. Since the radial map is invertible, each inner
five-point concyclicity condition pulls back to a proper linear subspace
of the free outer data. Choose a tangent outside the finitely many
inner and outer subspaces simultaneously.

Every mixed five-tuple is already nonconcyclic at the initial
configuration: a circle other than the two concentric circles meets
each of them in at most two points, and either original circle contains
no point of the other. These finitely many nonconcyclicity conditions
persist by continuity. Therefore a sufficiently small nonzero point of
the chosen analytic curve has no five concyclic points, while retaining
all the distance counts. This proves the proposition.

## 6. The entire local family has linearly many rare distances

The preceding construction has a stronger limitation than merely failing
to control the palette. Its regular initial configuration has exactly

$$q=3k-1=3N/4-1,\qquad R=3k-2=3N/4-2. \tag{7}$$

Moreover every sufficiently nearby $N$-point configuration, whether or
not it satisfies (1), has at least $3N/4-2$ rare distances. Thus none of
the sufficiently small deformations used above has bounded rarity.

The palette computation applies to every even $m=2k\ge6$. In the notation
of Section 1, the outer, inner, and cross palettes are respectively

$$O_j=2\sin(j\theta),\qquad I_j=\rho O_j,\qquad
C_j=\sqrt{(1-\rho)^2+4\rho\sin^2((j-1/2)\theta)}
\quad(1\le j\le k).$$

They satisfy

$$O_{j-1}<C_j<I_j<O_j\quad(1\le j\le k-1), \tag{8}$$

where $O_0=0$, and

$$I_{k-1}<I_k<O_{k-1}=C_k<O_k. \tag{9}$$

Here is an algebraic verification of the strict comparisons. We have
$\rho^2+2c\rho+1=4c^2$ and $0<\rho<c$. With $x=2j\theta$,

$$I_j^2-C_j^2
=\rho^2-1+2\rho\bigl((c-\rho)\cos x+s\sin x\bigr).$$

A function $a\cos x+b\sin x$, $a,b>0$, has no interior minimum on
$[0,\pi]$. On $[2\theta,\pi-2\theta]$ its smaller endpoint is
$\pi-2\theta$. Substitution into the preceding expression gives

$$8c(2c^2-1)(c-\rho)>0.$$

Similarly, with $y=2(j-1)\theta$,

$$C_j^2-O_{j-1}^2
=\rho^2-1+2\bigl((1-\rho c)\cos y+\rho s\sin y\bigr).$$

On $[0,\pi-4\theta]$ its minimum is at an endpoint. The endpoint
values are $C_1^2>0$ and $4\rho^2s^2>0$, respectively. This proves
(8); (9) follows from $I_k=2\rho<2c=O_{k-1}=C_k$ and monotonicity.
Thus the three $k$-element palettes have precisely one coincidence,
namely $C_k=O_{k-1}$.

Each outer or inner class has multiplicity $m$, except its antipodal
class, which has multiplicity $k$. Each cross class has $2m=N$ pairs.
Consequently only $C_k=O_{k-1}$ is rich, with multiplicity $3m$;
all the other $3k-2$ classes are rare. This proves (7).

Finally, for any fixed finite configuration, $R$ cannot decrease under
sufficiently small perturbations. Choose disjoint intervals around its
distinct positive distances, and perturb so little that each labeled
pair stays in its original interval. An initially rare class can split,
but each resulting class still contains at most its original $N$ pairs,
and cannot merge with a different original class. It therefore supplies
at least one rare distance in the perturbed set. Applied to (7), this
proves the neighborhood assertion.

The interlacing calculation, the exact multiplicities, and the
neighborhood argument were checked by the author and are
author-recorded. No floating-point
calculation is used as a certificate.

## 7. An odd-polygon caution for a possible palette bound

The even initial configuration satisfies $m(r_2)=2q+2$. That equality
does not extend to a universal upper bound. Put

$$\zeta=e^{2\pi i/5},\qquad \rho=2\sin(\pi/30),\qquad
A=\{\zeta^j,\rho\zeta^j:0\le j<5\}.$$

Let $r=2\sin(\pi/5)$, $D=2\sin(2\pi/5)$, and
$b=\sqrt{1+\rho^2-2\rho\cos(2\pi/5)}$. The exact spectrum is

$$
\begin{array}{c|rrrrrr}
\text{length}&\rho r&\rho D&1-\rho&b&r&D\\\hline
\text{multiplicity}&5&5&5&10&15&5.
\end{array}
$$

The displayed lengths are strictly increasing. For example
$0<\rho<1/4$, $\rho D<1/2<1-\rho$, and
$1-\rho<b<1<r<D$. For $b<1$ use
$\rho<1/4<2\cos(2\pi/5)$. The longest cross distance equals $r$:
writing $c=\cos(\pi/5)$, the identity
$\rho=\sqrt3\sin(\pi/5)-c$ gives
$1+\rho^2+2c\rho=4\sin^2(\pi/5)=r^2$.

Thus $q=6$ and $m_A(r_2)=15>2q+2$. This is not a counterexample
to Problem 132: it has five rare distances. Whether any bound
$m_A(r_2)\le2q(A)+C$ with an absolute constant $C$ holds is not
established here. Its relevance to a hypothetical $R=1$ sequence is
explained in [first_exceptional_distance](first_exceptional_distance.md).

## Relation to the remaining gap

The [one-rare asymptotic reduction](one_rare_asymptotics.md) forces
near-extremality of the second distance on the first two layers of a
hypothetical unbounded $R=1$ family. The proposition rules out deriving
a circular fraction from that extremality alone, even if both uniform
long-chord families can be extracted. Any successful inverse statement
must also use additional hypotheses, such as the sharp global distance
palette. Section 6 excludes the entire sufficiently small neighborhood
of this regular extremizer, but does not characterize remote portions
of the long-edge framework variety. The strengthened unrestricted
inverse statement is not proved here.

The author checked the row-rank calculation, all strict inequalities,
the anti-periodic tangent equations, the inner radial multiplier, and
the five-point transversality argument; the argument is
author-recorded. No numerical approximation is
used as a certificate.
