---
name: research/erdos_774/routes/anchored_phase_gluing
title: Quadratic-loss primitive-anchor gluing
desc: A phase correction gives an analytic gluing loss quadratic in the reciprocal number of blocks; diagonal padding shows that small loss does not ensure anchor propagation.
tags: [E0774, proved, construction, obstruction]
sources: []
created: 2026-09-18T00:18:00Z
updated: 2026-09-18T00:18:00Z
---


# Quadratic-loss primitive-anchor gluing

***

## Standing

The analytic lemma below is author-recorded; a separate reviewer checked it
internally, which is not a tier. It improves the available estimate for a particular gluing
operation. It does **not** supply iterated chromatic growth: a non-antipodal
example below shows that even arbitrarily inexpensive boundary gluing can
destroy every universal anchor.

## Primitive normalization

Let $B$ be a finite set of nonzero elements of a free abelian group
$\Gamma=\langle B\rangle_{\mathbb Z}$, with no antipodal pair. Suppose
$\chi(B)=q$ and a nonzero $w\in\Gamma$ belongs to
$\Sigma(C)$ for every class $C$ of every proper $q$-coloring.
Write $w=ku$, where $u$ generates the rank-one group
$\Gamma\cap\mathbb Qw$, and $k$ is a nonzero integer. Thus $u$
is primitive in $\Gamma$. Define

$$
\lambda_B(u)=\min_{\ell(u)=1}\max_{b\in B}|\ell(b)|,
\qquad \ell\in\operatorname{Hom}(\Gamma,\mathbb R).
\tag{1}
$$

The minimum exists: because $B$ spans $\Gamma\otimes\mathbb R$,
$\max_B|\ell(b)|$ is a norm, and its sublevel sets are compact.

For $m\geq3$, form the torsion-free group

$$
\Gamma_m=\Gamma^m/\mathbb Z(u_1+\cdots+u_m)
$$

and let $G_m$ be the union of the images of $B$ in its $m$ summands.
Primitivity of $u$ implies that the displayed quotient is free abelian.
The copies of $B$ remain distinct and nonzero, with no new antipodal
pairs: a relation between at most two summands cannot be a nonzero multiple
of $u_1+\cdots+u_m$.

The primitive normalization is essential. Quotienting by
$w_1+\cdots+w_m$ without saturation can leave torsion and is not the
rational-vector gluing used for positive-integer realization. In particular,
one cannot replace $\lambda_B(u)$ by $\lambda_B(w)$ in the bound below.

## Analytic gluing lemma — proved

Use the positive-real Sidon parameter $\rho$ defined in
[the tensor extraction theorem](tensor_extraction.md). Then

$$
\rho(G_m)\geq\rho(B)-
\frac{\pi^2\lambda_B(u)^2}{2m^2}. \tag{2}
$$

Indeed, the character tuples on $\Gamma_m$ are precisely
$(g_1,\ldots,g_m)\in\widehat\Gamma^m$ such that
$\prod_i u(g_i)=1$. Write an arbitrary polynomial on $G_m$ as
$\sum_i f_i(g_i)$, and independently maximize
$\operatorname{Re}f_i$ on each torus. The resulting value is at least
$\rho(B)$ times the sum of the absolute values of all coefficients.

Choose $\theta\in[-\pi,\pi]$ with
$e^{i\theta}=(\prod_i u(g_i))^{-1}$, and choose a minimizing $\ell$
in (1). Replace each $g_i$ by the character

$$
g'_i(\gamma)=g_i(\gamma)
             \exp(i\theta\ell(\gamma)/m).
$$

Their product constraint now holds because $\ell(u)=1$. At the independent
maximum of $\operatorname{Re}f_i$, its derivative in the $\ell$ direction
vanishes. Applying
$\operatorname{Re}(ze^{it})\geq\operatorname{Re}z -t\operatorname{Im}z-|z|t^2/2$
term by term therefore bounds the total loss by

$$
\frac{\theta^2}{2m^2}\sum_{i,b}|c_{i,b}|\ell(b)^2
\leq \frac{\pi^2\lambda_B(u)^2}{2m^2}
       \sum_{i,b}|c_{i,b}|.
$$

This proves (2), without a randomized lattice lift.

For $m\geq q+1$, the coloring number is exactly $q+1$. Under a
putative $q$-coloring, each block class signed-spans $w$, and their
representations sum to zero in the quotient. Conversely, use $q+1$
colors, a proper $q$-palette in every block, and arrange that every
color is absent from a block. Any proper collection of block summands embeds
as a direct sum in the quotient, so every resulting class is dissociated.

## Cheap boundary gluing need not propagate an anchor — proved

Let $A\subset\mathbb Z_{>0}$ have gcd one, maximum $M$, coloring
number $q\geq2$, and a universal anchor $a\ne0$. The punctured
Grow–Whicher example in [anchor gluing](anchor_gluing.md) supplies such an
$A$, with $q=2$, $a=3$, and $M=253$.

For an integer $r\geq2$, put

$$
B=\bigsqcup_{j=1}^r A e_j\subset\mathbb Z^r,
\qquad w=a(e_1+\cdots+e_r),\qquad u=e_1+\cdots+e_r.
$$

Direct sums preserve the coloring number and the hereditary dissociation
constant. The vector $w$ is universal: restrict any proper
$q$-coloring to each summand, represent $ae_j$ in the given color,
and add the disjoint representations. Moreover

$$
\rho(B)=\rho(A),\qquad \lambda_B(u)=M/r. \tag{3}
$$

The first equality follows by independently maximizing the polynomials on
the summands. For the second, write $\ell(e_j)=t_j$. The constraint
is $\sum_jt_j=1$, while the objective is $M\max_j|t_j|$; its
minimum $M/r$ is attained at $t_j=1/r$.

Apply the boundary gluing $m=q+1$ to $(B,w)$. Its $rm$
coordinate rays have exactly the one relation that their sum is zero.
Consequently the output is exactly

$$
G_m\cong A\otimes S_{r(q+1)}. \tag{4}
$$

It has coloring number $q+1$, and (2) has loss
$\pi^2M^2/[2r^2(q+1)^2]$, tending to zero as $r\to\infty$.
Nevertheless $r(q+1)\geq q+2$, so the proved
[large-simplex obstruction](anchor_gluing.md) says that it has **no** nonzero
universal anchor for $(q+1)$-colorings, even after any exact
ternary-relation-preserving scalar encoding.

Thus non-antipodality, hereditary extraction, and arbitrarily small analytic
loss do not imply boundary-anchor propagation. This does not rule out a
more structured scalar boundary construction; that narrower problem remains
open here.
