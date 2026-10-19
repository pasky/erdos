---
name: research/erdos_774/lemmas/moment_palette_height
title: An arbitrary-palette moment relation with palette-dependent height
desc: Congruence-sensitive entropy forces a monochromatic relation of height floor(sigma_star^q) in every fixed q-coloring at the critical boundary; no coefficient-flattening theorem is supplied.
tags: [E0774, Boolean-moments, coloring, entropy, proved, incomplete]
sources: []
created: 2026-09-19T01:30:00Z
updated: 2026-09-19T01:30:00Z
---


# An arbitrary-palette moment relation with palette-dependent height

***

This theorem concerns **every** fixed finite palette, but its coefficient
height depends on that palette. It does not establish unbounded
full-dissociation coloring, which needs height one.

## The finite entropy inequality

For $0\leq k\leq d/2$, put
$$
n=2^d,\quad r=\sum_{s=0}^k\binom ds,\quad
D=(d-k)\binom dk,\quad c_*=\tfrac12\log_2(\pi e/6).
$$
If the moment configuration admits a $q$-coloring whose classes have
no nonzero integer relation of coefficient height at most $H\geq1$, then
$$
\boxed{n\log_2(H+1)\leq
\frac{qD}{2}+q(\log_2(H+1)+c_*)r.}                 \tag{1}
$$

**Proof.** For a color class $C$ of size $M$, choose independent
uniform $\xi_x\in\{0,\ldots,H\}$. Height-$H$ independence makes the
moment-sum map injective, so its entropy is $M\log_2(H+1)$.
For Walsh sums $Y_S=\sum_{x\in C}\xi_x\chi_S(x)$, order rows by degree.
The identity
$$
Y_S=\sum_{T\subseteq S}(-2)^{|T|}
              \sum_{x\in C}\xi_x\prod_{i\in T}x_i
$$
puts each conditional $Y_S$ in one residue class modulo $2^{|S|}$.
The [integer entropy argument](../routes/boolean_moments.md), now using
$\operatorname{Var}\xi_x=H(H+2)/12$, gives
$$
M\log_2(H+1)\leq\frac12\sum_{s=0}^k\binom ds
\log_2\!\left(2\pi e
\left[\frac{H(H+2)M}{12\,4^s}+\frac1{12}\right]\right).
\tag{2}
$$
Since $M\leq2^d$ and $2^{d-2s}\geq1$, the bracket is at most
$2^{d-2s}(H+1)^2/12$. Each logarithmic contribution, including the
factor one half, is at most
$$
\frac d2-s+\log_2(H+1)+c_*.
$$
The identity
$\sum_{s\leq k}(d/2-s)\binom ds=D/2$, followed by summation over colors,
proves (1). The conditional Gaussian entropy bound in (2) follows by
adding uniform interval jitter, using Gaussian maximal entropy, then
conditional Jensen and total variance, exactly as in the linked proof.
$\square$

## Critical consequence and its exact quantifiers

At the rounded critical boundary,
$$
D/(2n)\longrightarrow c=\frac1{2\sqrt{2\pi}},
\qquad r/n\longrightarrow0,\qquad \sigma_*=2^c.
$$
For every fixed $q$, every sufficiently large stage has a nonzero
monochromatic integer relation of height at most
$$
\boxed{H(q)=\lfloor2^{cq}\rfloor=\lfloor\sigma_*^q\rfloor.} \tag{3}
$$
Indeed $\log_2(H(q)+1)>cq$, contradicting the limiting necessary
inequality (1) if every class were height-$H(q)$ independent.
Five colors force a ternary relation; six colors force a relation of
height at most two. This recovers the fixed lower bound six and adds
explicit height control for larger palettes.

The quantifiers are $\forall q\,\exists H(q)$, not the existence of
one fixed height witnessing unbounded coloring. No operation has been
proved to flatten these color-dependent relations while preserving
actual colors and the moment family's uniform extraction. Full tensor
products do not automatically preserve its total-degree moment order.

The inequality is author-recorded and was checked algebraically. No
numerical search is involved.
