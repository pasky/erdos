---
name: research/leads/equilateral_two_scale/binary_transfer
title: Binary transfer for two colors and triangles
desc: |
  For two colors and three-point configurations the monochromatic indicator
  is quadratic, so OpenAI's projection onto continuous vectors preserves
  avoidance after thresholding. The algebraic-family version uses the
  release's rigidity premise; the two-scale version uses the one-parameter
  rigidity extension and applies to every real scale ratio.
created: 2026-10-16T14:00:00Z
updated: 2026-10-16T14:00:00Z
---

***

The construction and proofs are credited to Plasma AI. The
[[research/leads/equilateral_two_scale/evidence/verify/whole_conclusion/grade|graded whole-conclusion review]]
covers the stated conditional forward direction, the reverse implication
and the two-scale extension at every real ratio. The forward direction of
the algebraic-family theorem is conditional on premise (R0) of
[[research/leads/equilateral_two_scale/spectral_exclusion|the spectral
account]]. The two-scale extension below uses the separate prose rigidity
proof examined in that review. The continuous-factor and sampling arguments
are supplied here. They adapt Lemma 4.1 and Proposition 4.2 of the
[[../library/discrete_geometry/openai_2026_euclidean_plane_not_five_colorable/_index|OpenAI plane-coloring manuscript]],
read at proof depth and examined at their stated use in this argument.

## Statement

A *triangle* here is an ordered triple $(0,a,b)$ of distinct points of
$\mathbb C$, possibly collinear; its copies are $(p,\;p+ua,\;p+ub)$ with
$p\in\mathbb C$ and $|u|=1$. Let $\mathcal T=\{(0,a_j,b_j):j\in J\}$ be a
countable family. A two-coloring $c:\mathbb C\to\{-1,+1\}$ *avoids*
$\mathcal T$ if no copy of any member is monochromatic; a measurable $c$
*weakly avoids* $\mathcal T$ if for each $j$ the set of $(p,u)\in
\mathbb C\times S^1$ whose copy is monochromatic is null for area times arc
length. Equivalently its measure in $B(0,n)\times S^1$ is zero for every
positive integer $n$. Changing colors on a plane-null set preserves this
condition: for each fixed $u$, hitting that set at any of the three vertices
is a null event in $p$. Reflection is not built into this ordered-template
convention; when reflected copies are required, include the conjugate
template as well. This preserves countability and algebraic side lengths.

**Theorem.** Suppose every member of $\mathcal T$ has algebraic side
lengths.

- (a) If some two-coloring of the plane avoids $\mathcal T$, then some
  Borel two-coloring weakly avoids $\mathcal T$, granting (R0).
- (b) If some measurable two-coloring weakly avoids $\mathcal T$, then some
  two-coloring avoids $\mathcal T$. This direction needs neither (R0) nor
  algebraic sides.

**Two-scale extension.** For Problem 173, the same proof applies to
$\mathcal T$ consisting of equilateral sides $1,x$ for every real $x>0$.
Use $L=F_x(i)$, where $F_x$ is the real closure of $\mathbb Q(x)$ in
$\mathbb R$, and its unit group. Corollary 3 of the
[[research/leads/equilateral_two_scale/rigidity_extension|rigidity extension]]
provides exactly the nonzero pair-correlation identity used in the proof.
All the factor, sampling and threshold arguments below concern a countable
dense carrier and work with $L$ in place of $E$.
This yields the transfer for every real ratio. Theorem 4 of the
[[research/leads/equilateral_two_scale/circle_exclusion|circle account]]
then excludes avoidance when $x\ne1$. The graded whole-conclusion review
covers this composition. The recorded standing
of the separate algebraic Lean premise (R0) is unchanged.

## Why triangles and two colors

For $a,b,c\in[-1,1]$ put $Q(a,b,c)=1+ab+ac+bc$. Then

$$
Q(a,b,c)=\tfrac12\bigl((1+a)(1+b)(1+c)+(1-a)(1-b)(1-c)\bigr)\ge0,
$$

with equality exactly when one of $a,b,c$ equals $-1$ and one equals $+1$.
On signs, $Q/4$ is the indicator that $a,b,c$ are equal. So a $[-1,1]$-valued
field whose three pair correlations on a triangle sum to $-1$ has $Q=0$
almost surely there, and any rounding that keeps $+1$ and $-1$ produces a
nonmonochromatic triple. Only pair correlations enter. For four points, or
for three or more colors on a triangle, the monochromatic indicator has
terms of degree above two, which the projection below does not preserve.

Ordinary conditional expectation does not preserve avoidance of general
hyperedges. The uniform law on the six nonmonochromatic sign triples has all
three conditional means zero over the trivial factor, and rounding
$(0,0,0)$ gives a monochromatic triple. That projection changes each pair
correlation from $-1/3$ to $0$, so it is not of the pair-preserving kind used
here and does not test this mechanism.

## Continuous factors and measurable representatives

Let a standard probability space carry a measure-preserving action of the
countable dense additive subgroup $E\subset\mathbb C$, with Koopman
operators $T_z$. Define $H_c$ as in (R0). It is closed, since
$\|T_zv-v\|_2\le2\|v-w\|_2+\|T_zw-w\|_2$, and it contains constants.
Conjugation and Lipschitz composition preserve $H_c$. Products of two
bounded members belong to $H_c$, by the product inequality in $L^2$.

Let $\mathcal F_c$ consist of the measurable sets $A$ with
$\mathbf1_A\in H_c$, modulo completion. Complements and finite unions stay
in $\mathcal F_c$ by the preceding properties; increasing unions do by
$L^2$ convergence. Thus it is a sigma-algebra. For a real $h\in H_c$, the
Lipschitz functions $\min(1,\max(0,n(h-t)))$ converge in $L^2$ to
$\mathbf1_{\{h>t\}}$. Every real member of $H_c$ is therefore
$\mathcal F_c$-measurable, and the same follows for complex members by real
and imaginary parts. Conversely the simple $\mathcal F_c$-measurable
functions belong to $H_c$ and are dense in $L^2(\mathcal F_c)$. Hence
$H_c=L^2(\mathcal F_c)$ and its orthogonal projection is conditional
expectation. In particular it sends real functions valued in $[-1,1]$ to
functions with the same bounds.

For $y\in\mathbb C$ and $z_n\in E$ tending to $y$, the sequence $T_{z_n}h$
is Cauchy in $L^2$ for $h\in H_c$, because the norm of its difference at
$n,m$ is $\|T_{z_n-z_m}h-h\|_2$. Its limit defines $T_yh$, independently
of the approximating sequence. The group law, unitarity and strong
continuity extend by limits. Realness and interval bounds are closed
$L^2$ conditions, so $T_y$ preserves them. No pointwise action of
$\mathbb C$ on the probability space is asserted.

For a real $g\in H_c$ with $-1\le g\le1$ there is a jointly Borel field
$G(y,\eta)\in[-1,1]$ representing $T_yg$ for every fixed $y$, after choosing
a bounded Borel representative of $g$. To see this, choose Borel maps
$q_n:\mathbb C\to E$ with countable range and uniformly small
$|q_n(y)-y|$, so that
$\|T_{q_n(y)}g-T_yg\|_2\le2^{-n}$ for every $y$. Such maps exist by
density of $E$ and uniform continuity of the orbit of $g$. Realize
$G_n(y,\eta)=T_{q_n(y)}g(\eta)$ by the original countable action. The maps
$G_n$ are jointly Borel and bounded. For each fixed $y$ the sum of the
$L^1$ norms of $G_{n+1}(y,\cdot)-G_n(y,\cdot)$ is finite, so the sequence
converges almost surely. Define $G$ to be this limit where it exists and
$0$ otherwise. It is jointly Borel, and its section at every fixed $y$
represents the $L^2$ limit $T_yg$. The exceptional subset of the probability
space may depend on $y$; Tonelli, not a common pointwise action, handles it.

## Proof of (a)

Rotate each member so that $a_j>0$; with algebraic sides, $a_j,b_j\in E$,
the field of algebraic numbers, and $K$ denotes its algebraic unit vectors.
Let $\Omega\subset\{\pm1\}^E$ consist of the labelings with no monochromatic
triple $(p,p+ua_j,p+ub_j)$, $p\in E$, $u\in K$, $j\in J$. It is closed,
contains the restriction of the given coloring, and is invariant under
$\eta\mapsto\eta(k\,\cdot+z)$. Amenability of $E\rtimes K$ gives an invariant
probability $\mu$ on $\Omega$, as in the manuscript's Proposition 4.2. Define
$T_z$, $V_k$, $f(\eta)=\eta(0)$ and the projection $P$ onto the continuous
vectors $H_c$ as in the proof of Theorem 3 of the spectral account. Put
$g=Pf$.

*Bounds.* The continuous-factor argument above shows that $g$ is real with
$-1\le g\le1$, and extends the translations on $H_c$ to a strongly
continuous unitary representation of $\mathbb C$ with
$-1\le T_yg\le1$ for every $y$.

*Correlations.* As in Theorem 3, (R0) gives $\langle f,T_zf\rangle=\langle
g,T_zg\rangle$ for all nonzero $z\in E$. Let $\kappa(y)=\langle g,T_yg\rangle$,
continuous on $\mathbb C$. For $u\in K$ every $\eta\in\Omega$ satisfies
$\eta(0)\eta(ua_j)+\eta(0)\eta(ub_j)+\eta(ua_j)\eta(ub_j)=-1$, and the three
displacements $ua_j$, $ub_j$, $u(b_j-a_j)$ are nonzero. Integrating,

$$
1+\kappa(ua_j)+\kappa(ub_j)+\kappa(u(b_j-a_j))=0\qquad(u\in K),
$$

and by continuity and density of $K$ in $S^1$ this holds for every unit $u$.

*Pointwise vanishing.* For $p\in\mathbb C$ and unit $u$ the three functions
$G_1=T_pg$, $G_2=T_{p+ua_j}g$, $G_3=T_{p+ub_j}g$ take values in $[-1,1]$, and
$\int Q(G_1,G_2,G_3)\,d\mu$ is the left side above, because
$\langle T_yg,T_{y'}g\rangle=\kappa(y'-y)$. Since $Q\ge0$, $Q(G_1,G_2,G_3)=0$
$\mu$-almost surely.

*A measurable sample.* Use the jointly Borel field constructed above.
For each fixed $(p,u)$ its three sections represent the three vectors in
the preceding paragraph. Tonelli then gives, for every $j\in J$ and every
integer $n\ge1$,

$$
\int_\Omega\int_{|p|<n}\int_{S^1}
Q\bigl(G(p,\eta),G(p+ua_j,\eta),G(p+ub_j,\eta)\bigr)
\,d\sigma(u)\,dp\,d\mu(\eta)=0 .
$$

These are countably many conditions, so one $\eta_0$ makes every inner
double integral vanish. Put $c'(y)=+1$ if $G(y,\eta_0)\ge0$ and $c'(y)=-1$
otherwise; $c'$ is Borel. For almost every $(p,u)$ and every $j$ the
three values of $G(\cdot,\eta_0)$ include $+1$ and $-1$, which $c'$ keeps,
so the copy is not monochromatic. Thus $c'$ weakly avoids $\mathcal T$.
$\square$

## Proof of (b)

Let $c$ weakly avoid $\mathcal T$, and let $A^*$ and $B^*$ be the points of
density one of $\{c=1\}$ and $\{c=-1\}$. They are disjoint and their union is
conull. Suppose $p$, $p+ua_j$, $p+ub_j$ all lie in $A^*$. For small $h>0$
choose $p'$ uniformly in the disk of radius $h$ about $p$ and, independently,
$u'$ uniformly on an arc about $u$ of angular width $h/(1+|a_j|+|b_j|)$. Each
of $p'+u'a_j$ and $p'+u'b_j$ has a density at most $1/(\pi h^2)$, supported
in the disk of radius $2h$ about $p+ua_j$, respectively $p+ub_j$. Density
one at the three points makes the probability that all three random points
lie in $\{c=1\}$ tend to one. The law of $(p',u')$ is absolutely continuous,
which contradicts weak avoidance. The same holds for $B^*$. This is the
argument of the manuscript's Lemma 4.3 with three points.

Every finite set of points has a translate inside the conull set
$A^*\cup B^*$, where the density classes color it with no monochromatic copy.
Each avoidance condition is closed in $\{\pm1\}^{\mathbb C}$ and involves
three coordinates, so product compactness gives a coloring of the whole
plane avoiding $\mathcal T$. $\square$

This yields an arbitrary avoider, not a measurable completion of the density
classes on the omitted null set.
