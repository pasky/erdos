---
name: research/erdos_940/quadratic_compression
title: Obstructions to polynomial and rational quadratic compression
desc: Higher-degree diagonal forms cannot be rationally represented by fixed positive quaternary quadratic forms; a stronger dimension bound holds for exponents twice odd.
tags: []
sources: []
created: 2026-09-22T03:06:14Z
updated: 2026-09-22T03:06:14Z
---


# Obstructions to polynomial and rational quadratic compression

***

## Status and relevance

These are proved limitations of a proposed transfer of the
[quartic quaternion argument](quartic_complement.md). They do **not** prove that
any additional integers are missing from $S_r$.

The quartic proof maps certain four-variable quartics to positive quaternary
quadratic forms. It is tempting to compress a higher-dimensional diagonal form
similarly, perhaps using rational functions rather than polynomials. The
proposition below excludes this for every $r\ge5$.

## Rational compression into at most four squares with fixed coefficients

**Proposition.** Let $r\ge5$ and $d_i\in\mathbb Q_{>0}$. Set


$$
F(X_1,\ldots,X_r)=\sum_{i=1}^r d_iX_i^r.
$$


There is no rational-function identity


$$
F=Q(G_1,\ldots,G_m)
\tag{1}
$$


with $m\le4$, a fixed positive-definite rational quadratic form $Q$, and
$G_i\in\mathbb Q(X_1,\ldots,X_r)$. There is no restriction on denominators.

**Proof.** If necessary pad $Q$ to dimension four by positive square terms with
zero inputs. Its determinant is positive. Over the real number field
$L=\mathbb Q(\sqrt{\det Q})$, its determinant squareclass is trivial, so $Q$ is
similar to a quaternion norm form. For completeness, after diagonalization and
division by the first coefficient, write $Q\sim\langle1,u,v,w\rangle$. The
condition $uvw\in L^{\times2}$ makes $w$ equivalent to $uv$ modulo squares,
giving $\langle1,u,v,uv\rangle$, the norm of $(-u,-v)$. Positivity at a real
embedding implies that this quaternion algebra $A$ is division.

The projective hypersurface


$$
Z=\{F=0\}\subset\mathbb P_L^{r-1}
$$


is smooth and geometrically integral, with dimension $r-2\ge3$. Indeed, its
gradient vanishes only at the zero vector, and smooth positive-degree
hypersurfaces of this dimension are geometrically integral. Standard
Brauer-group results give an isomorphism
$\operatorname{Br}(L)\to\operatorname{Br}(Z)$ and an injection
$\operatorname{Br}(Z)\to\operatorname{Br}(L(Z))$. The exact inputs are
[Colliot-Thélène--Skorobogatov, *The Brauer--Grothendieck group*, Corollary
4.4.5 and Theorem
3.5.4](https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf),
printed pages 117 and 88; their hypotheses and full passages were checked.

Consequently $A$ remains division over $L(Z)$. It remains division after
adjoining one independent transcendental variable: an isotropic
rational-function vector for its norm could be specialized at a field element
avoiding its finitely many poles and nonzero-coordinate zeros. Thus $Q$ is
anisotropic over the function field $L(Z)(t)$ of the affine cone $F=0$.

Suppose (1) held. The irreducible polynomial $F$ defines a discrete valuation
$v_F$ on $L(X_1,\ldots,X_r)$, with residue field $L(Z)(t)$. Put


$$
e=\min_{G_i\ne0}v_F(G_i),\qquad H_i=F^{-e}G_i.
$$


All $H_i$ are integral at this valuation, and at least one has nonzero
reduction. Homogeneity gives


$$
Q(H_1,\ldots,H_m)=F^{1-2e}.
$$


The left side is integral, so $1-2e\ge0$. This integer is odd and hence
positive. Reducing the identity modulo $F$ supplies a nonzero isotropic vector
of $Q$ over $L(Z)(t)$, a contradiction. $\square$

For odd $r$ the proposition also follows directly from signs over the reals. Its
additional content concerns even $r\ge6$.

## A stronger dimension obstruction for $r\equiv2\pmod4$

If $r=2k$ with $k$ odd, the same $F$ cannot be represented rationally by **any**
positive-definite rational quadratic form of dimension $m<r$.

Let $Y_i=X_i^k$ and $\varphi=\langle d_1,\ldots,d_r\rangle$. The extension


$$
\mathbb Q(X_1,\ldots,X_r)/\mathbb Q(Y_1,\ldots,Y_r)
$$


has odd degree $k^r$. A putative identity makes
$Q\perp\langle-\varphi(\mathbf Y)\rangle$ isotropic over the larger field.
Springer's theorem descends isotropy to the smaller field. Since $Q$ stays
anisotropic over a real rational-function field, the last coordinate of the
descended isotropic vector is nonzero. Thus $Q$ represents $\varphi(\mathbf Y)$
over $\mathbb Q(\mathbf Y)$. The generic representation theorem then makes
$\varphi$ a subform of $Q$, contradicting $m<r$.

The checked inputs are [Elman--Karpenko--Merkurjev, *The Algebraic and Geometric
Theory of Quadratic Forms*, Corollary 18.5 and Theorem
17.12](https://www.math.ucla.edu/~merkurev/Book/Kniga-final/Kniga.pdf), printed
pages 77 and 73.

## Two elementary polynomial limitations

More generally, a smooth homogeneous form in $r$ variables cannot be written as
$H(G_1,\ldots,G_m)$ with $m<r$, all $G_i$ homogeneous of positive degree, and
$H$ homogeneous of degree at least two. Over an algebraic closure the $G_i$ have
a common nonzero zero, by the projective dimension theorem. At this point
$H(G)=0$ and the chain rule makes every derivative vanish, contradicting
smoothness.

Also, a nondegenerate diagonal degree-$r$ form in $r\ge3$ variables is
absolutely irreducible, whereas the norm form of a degree-$r$ field or étale
algebra splits into linear factors over the algebraic closure. Hence an
invertible linear change cannot identify these forms. This rules out a linear
norm-form shortcut, not all uses of norm arithmetic.
