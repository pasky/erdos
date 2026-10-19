---
name: research/erdos_940/birational_diagonal_forms
title: Birational similitudes and direct product constructions
desc: For degree at least four every birational similitude is monomial; direct multiplicative tensoring of proper powerful subsums is subcritical.
tags: []
sources: []
created: 2026-09-23T01:11:28Z
updated: 2026-09-23T01:11:28Z
---


# Birational similitudes and direct product constructions

***

## Status and scope

The classification and counting results below are proved and independently
checked. They strengthen the
[rational-transformation limitations](rational_transformations.md), but settle
neither a density question nor a new infinitude case. In particular, excluding
composition laws is not a bound for integer fibers.

## Birational similitudes in degree at least four

The external input is de Fernex's [*Birationally rigid hypersurfaces*, Theorem
A, page 1](https://arxiv.org/pdf/math/0604213): every smooth complex degree-$r$
hypersurface in $\mathbb P^r$, for $r\ge4$, is birationally superrigid. The
theorem and its stated consequences were checked in version 6 of the full paper.
A birational map from such a hypersurface to another smooth Fano hypersurface of
Picard rank one is therefore an isomorphism.

**Theorem.** Let $K$ be finitely generated over $\mathbb Q$, let $r\ge4$,
and put $F=\sum_{i=1}^r a_i x_i^r$ with $a_i\in K^\times$.
If $T\in\operatorname{Bir}(\mathbb A^r_K)$ and

$$
F(T(\mathbf x))=mF(\mathbf x),\qquad m\in K^\times,
$$

then

$$
T_i(\mathbf x)=c_i x_{\sigma(i)},\qquad
c_i^r=m a_{\sigma(i)}/a_i,                              \tag{1}
$$

for a permutation $\sigma$ and $c_i\in K^\times$.
Positivity is not required.

**Proof.** Over $L=K(t)$, the map and its birational inverse induce a
birational map between

$$
X_t:\ F(\mathbf X)-tZ^r=0,\qquad
X_{mt}:\ F(\mathbf X)-mtZ^r=0
\quad\text{in }\mathbb P^r_L.
$$

Both are geometrically smooth: their partial derivatives vanish
simultaneously only at the zero vector. Their dimension is $r-1\ge3$,
their geometric Picard rank is one, and adjunction gives
$-K_X=\mathcal O_X(1)$.

Embed the finitely generated field $L$ into $\mathbb C$ and apply
de Fernex's theorem. The map becomes an isomorphism. This descends to
$L$: the two projections from the closure of its graph become
isomorphisms after a faithfully flat field extension, hence are already
isomorphisms. Since the isomorphism preserves the anticanonical bundle
and

$$
H^0(\mathbb P^r_L,\mathcal O(1))
\simeq H^0(X_t,\mathcal O(1)),
$$

it is induced by a projective linear map $M$ over $L$.

Let $G_t=F(\mathbf X)-tZ^r$. There is $\lambda\in L^\times$ such that
$G_{mt}(M\mathbf X)=\lambda G_t(\mathbf X)$, where here $\mathbf X$
includes $Z$. The Hessian determinant of either polynomial is a nonzero
scalar times $(X_1\cdots X_rZ)^{r-2}$. The Hessian transformation formula
therefore makes $M$ monomial. Write its rows as
$b_j(t)X_{\sigma(j)}$, indexing $Z$ by $0$.

Comparison of coefficients and then $t$-adic valuations gives

$$
r v_t(b_j)=v_t(\lambda)
 +\mathbf1_{\sigma(j)=0}-\mathbf1_{j=0}.                 \tag{2}
$$

If $\sigma$ moved $0$, the shifts on the right would include $0,1,-1$.
They cannot all be congruent modulo $r$. Thus $\sigma(0)=0$.
The $Z^r$ coefficient now gives $\lambda=mb_0^r$, and the remaining
coefficients give

$$
(b_i/b_0)^r=m a_{\sigma(i)}/a_i\in K^\times.
$$

A rational function in $t$ algebraic over $K$ belongs to $K$.
Consequently $b_i/b_0=c_i\in K^\times$. Dehomogenizing and identifying
$t$ with $F(\mathbf x)$ proves (1). $\square$

### No composition law birational in one input

For $r\ge4$ there is no rational identity

$$
F(C(\mathbf x,\mathbf y))=F(\mathbf x)F(\mathbf y)         \tag{3}
$$

whose generic $\mathbf x$-translation is birational. Apply the theorem
over $K=\mathbb Q(\mathbf y)$, with $m=F(\mathbf y)$. Equation (1) would
make a constant multiple of $F(\mathbf y)$ an $r$th power in $K$.
The valuation at the absolutely irreducible polynomial $F(\mathbf y)$
is one, which is impossible for an $r$th power. Absolute irreducibility
follows from smoothness of its projective hypersurface: distinct
positive-degree homogeneous factors would intersect and cause a
singularity.

Thus for a fixed positive rational $F$ and $r\ge4$, even arbitrarily
complicated birational self-maps preserving $F$ are only its finite
monomial symmetry group. Positivity of the image selects the positive
coordinate scalings. The fixed-complexity qualification in the earlier
[rational-map bound](rational_transformations.md) is unnecessary for this
subclass. The result does **not** exclude nonbirational rational maps,
correspondences, or positive density of the value set.

### Birational exponent descent is also excluded

Suppose a birational coordinate change identified $F$ with a positive
diagonal degree-$d$ form $H$ in the same $r$ variables, where $1\le d<r$.
Their generic projective levels would be birational: one is the
degree-$r$ hypersurface above, the other is the smooth degree-$d$
hypersurface $H(\mathbf Y)=tZ^d$ in $\mathbb P^r$.
Over $\mathbb C$, both are smooth Fano varieties of Picard rank one.
Superrigidity forces an isomorphism, but their Fano indices are $1$
and $r+1-d$, respectively. This is impossible.

This does not exclude nonbirational power substitutions, such as
$x_i\mapsto x_i^{r/d}$ when $d\mid r$; those substitutions retain
uncontrolled power restrictions on the new coordinates.

## Direct products of proper subsums

Let $A_{r,m}$ be the positive integers expressible as a sum of at most
$m$ positive $r$-powerful integers. For $1\le m\le r$, canonical
tuple counting gives

$$
\#(A_{r,m}\cap[1,X])\ll_r X^{m/r}.
$$

Suppose $k\ge2$, all $m_j\ge2$, and $\prod_{j=1}^k m_j\le r$.
Expansion of a product shows

$$
A_{r,m_1}\cdots A_{r,m_k}\subseteq S_r,
$$

because a product of powerful integers is powerful. But this construction
has the bound

$$
\#\bigl(A_{r,m_1}\cdots A_{r,m_k}\cap[1,X]\bigr)
\ll_r X^{\max_j m_j/r}(\log(2X))^{k-1}
\ll_r X^{1/2}(\log(2X))^{k-1}.                           \tag{4}
$$


To prove this, put each factor in a dyadic range
$[2^{h_j},2^{h_j+1})$. Set $\alpha_j=m_j/r$ and
$\alpha=\max_j\alpha_j>0$. The tuple count in that box is
$O_r(2^{\sum_j\alpha_jh_j})\le O_r(2^{\alpha\sum_jh_j})$.
Only $\sum h_j\le\log_2 X$ can occur. There are
$O_k((1+H)^{k-1})$ compositions with sum $H$; geometric summation
proves the first bound in (4). Finally $m_j\le r/2$, since another
factor has at least two summands. This proves the second bound.

Thus ordinary multiplicative tensoring of proper subsums cannot give
positive density, even when every powerful coefficient is allowed.
No assertion about more general composition laws follows from (4).
