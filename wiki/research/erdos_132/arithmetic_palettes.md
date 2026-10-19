---
name: research/erdos_132/arithmetic_palettes
title: Arithmetic-progression palettes and a uniform ellipse bound
desc: |
  Uniform lattice counts on ellipses force bounded-rarity palettes to need
  at least n^(1/10-o(1)) polynomial-length arithmetic progressions.
sources: []
research_state: closed
created: 2026-09-23T07:03:23Z
updated: 2026-09-24T22:12:56Z
---


# Arithmetic-progression palettes and a uniform ellipse bound

***

The squared-distance palette here includes zero. Arithmetic progressions
may have different real starting points and steps; negative steps can be
reversed, and singletons can be assigned a positive step.

**Theorem.** Fix $K,B>0$ and $\eta>0$. Suppose $A$ has $n$ points,
$R(A)\le K$, and its squared-distance palette is covered by $r$
arithmetic progressions, each of at most $n^B$ terms. Then, for large
enough $n$ depending on these parameters,

$$r\ge c_{K,B,\eta}n^{1/10-\eta}. \tag{1}$$

In particular an unbounded bounded-rarity family cannot have its
squared-distance palettes covered by $n^{o(1)}$ polynomial-length
progressions. This excludes a restricted palette structure, not
arbitrary real palettes or rational palettes of uncontrolled height.

## Uniform lattice points on an ellipse

**Lemma.** For every $\varepsilon>0$, every nondegenerate real ellipse
contains $O_\varepsilon(Q^\varepsilon)$ integer points in $[-Q,Q]^2$,
uniformly in the ellipse, for $Q\ge1$.

If there are at most four points there is nothing to prove. Choose
five otherwise. No three are collinear. Their evaluation matrix on
$x^2,xy,y^2,x,y,1$ has rank five: for each selected point, the product
of the two lines pairing the other four vanishes at those four but
not at the selected point. Its one-dimensional kernel is therefore
spanned by the coefficient vector of the ellipse.

The signed $5$-by-$5$ minors give an integer coefficient vector of
height $O(Q^{10})$. After dividing by its common divisor and choosing
the sign, write the equation as

$$Ax^2+Bxy+Cy^2+Dx+Ey+F=0,
\qquad A>0,\quad\Delta=4AC-B^2>0.$$

Put

$$T=2AE-BD,\qquad U=2Ax+By+D,\qquad V=\Delta y+T.$$

The map $(x,y)\mapsto(U,V)$ is injective, and every point on the
ellipse satisfies

$$V^2+\Delta U^2=M:=T^2+\Delta(D^2-4AF). \tag{2}$$

Here $M$ is a positive integer of size $O(Q^{40})$. Positivity follows
also directly from (2): $M=0$ would allow only one point.

In the imaginary quadratic field $F_0=\mathbb Q(\sqrt{-\Delta})$,
the element $V+U\sqrt{-\Delta}$ is an algebraic integer of norm $M$.
Use ideals in the maximal ring of integers of $F_0$, not in a possibly
nonmaximal quadratic order. Unique prime-ideal factorization bounds
the number of ideals of norm $M$ by the divisor function $\tau(M)$:
at a rational prime power $p^a$ there are $a+1$ choices when $p$
splits, at most one when it is inert, and one when it ramifies.
Each principal ideal has at most six generators, since an imaginary
quadratic field has at most six units. Thus there are at most
$6\tau(M)$ possible pairs $(U,V)$.

The elementary bound $\tau(M)=O_\delta(M^\delta)$ for every
$\delta>0$, used with $\delta=\varepsilon/40$, proves the lemma.
The implied constant is independent of the quadratic field and hence
of the ellipse. In particular, arbitrarily eccentric ellipses cause
no loss of uniformity.

## Three anchors and progression covers

Let $T_0=\{t_1,t_2,t_3\}$ be any noncollinear triangle, and let
$S\subset\mathbb R_{\ge0}$ have $q_0$ elements covered by $r$
progressions of at most $Q$ terms. Define

$$X=\{x\in\mathbb R^2:|x-t_i|^2\in S\text{ for }i=1,2,3\}.$$

For every $\varepsilon>0$,

$$\max_{\Gamma\text{ circle}}|X\cap\Gamma|
\ll_\varepsilon r^2Q^\varepsilon,
\qquad |X|\ll_\varepsilon q_0r^2Q^\varepsilon. \tag{3}$$

Fix a positive-radius circle $\Gamma$ with center $c$. Some two of
$t_1-c,t_2-c,t_3-c$ are linearly independent, since the anchors are
noncollinear. On this circle the squared-distance functions are
affine linear:

$$|x-t_i|^2=2(c-t_i)\cdot x+|t_i|^2+\rho^2-|c|^2,$$

where $\rho$ is the circle's radius. The selected pair therefore
defines an invertible affine map. Choose one of the covering
progressions for each selected squared distance, and use their integer
indices as coordinates. The image of $\Gamma$ is an ellipse, and
its eligible points have integer coordinates in $[0,Q-1]^2$.
The ellipse lemma bounds their number by $O_\varepsilon(Q^\varepsilon)$.
Sum over the $r^2$ progression choices. Overlaps between progressions
only overcount. Radius-zero circles are singletons.

Finally, $X$ is covered by the $q_0$ circles centered at $t_1$ with
squared radii in $S$. This proves both bounds in (3). Their constants
do not depend on the anchor shape, the progression offsets, or their
steps. In particular they remain valid for triangles approaching
collinearity, as long as each triangle is noncollinear.

## Application to the moving-frame reduction

Assume $R(A)\le K$ along an unbounded sequence. The established
[moving-frame argument](moving_frames.md) gives a noncollinear triangle
$T_n$, linearly many motions $g$ with $gT_n\subset A$ and distinct
roots, and a strictly convex $C\subset A$ of linear size. Put

$$U=\bigcup_g g^{-1}C,\qquad N=|U|,\qquad
M(A)=\max_\Gamma|A\cap\Gamma|.$$

Its energy inequality is

$$N^2(\sqrt N+M(A))\gg_K n^3/\log(2n). \tag{4}$$

All squared distances from $U$ to $T_n$ lie in the squared-distance
palette $S$ of $A$. Apply (3) to this triangle. Apply its circle
bound also to any congruent copy $gT_n\subset A$, so that it controls
$M(A)$. Since pair counting gives $|S|=q(A)+1=O_K(n)$, with
$Z=r^2Q^\varepsilon$ we obtain

$$N\ll_{K,\varepsilon}nZ,\qquad
M(A)\ll_\varepsilon Z.$$

Substitution into (4) gives

$$\frac{n^3}{\log(2n)}
\ll_{K,\varepsilon}n^{5/2}Z^{5/2}+n^2Z^3.$$

At least one of these two terms supplies half the lower bound. Thus

$$r^2Q^\varepsilon=Z
\gg_{K,\varepsilon}\frac{n^{1/5}}{(\log(2n))^{2/5}}. \tag{5}$$

Equivalently, after renaming $\varepsilon$,

$$r\gg_{K,\varepsilon}
\frac{n^{1/10}}{Q^\varepsilon(\log(2n))^{1/5}}.$$

For $Q\le n^B$, choosing $\varepsilon$ sufficiently small and
absorbing the logarithm proves (1).

This argument uses the entire palette rather than merely three-anchor
cardinality. No comparable ellipse or progression cover is supplied
by bounded rarity alone. The author checked the conic coefficient
bound, norm identity, ideal counting, affine maps, and exponent
calculation; the argument is author-recorded.
