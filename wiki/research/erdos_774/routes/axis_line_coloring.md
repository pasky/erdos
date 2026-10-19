---
name: research/erdos_774/routes/axis_line_coloring
title: The remaining coloring problem for linear-side line families
desc: Three-direction connectivity and an entropy lower bound are proved, but unbounded dissociated coloring of L(3,4,...,t+2) remains open; full tensor products lose uniform extraction.
tags: [E0774, coloring, proved, incomplete]
sources: []
created: 2026-09-18T19:04:00Z
updated: 2026-09-18T19:51:44Z
---


# The remaining coloring problem for linear-side line families

***

Let $L_t$ be the full axis-line indicators on
$X_t=\prod_{i\le t}[i+2]$, let $N_t=|X_t|$, and put
$s_t=\sum_{i\le t}1/(i+2)$. The
[direct extraction theorem](axis_line_extraction.md) proves one uniform
full-dissociation extraction constant. The new sufficient target is
$$
\boxed{\sup_t\chi_1(L_t)=\infty.} \tag{1}
$$
It is **unproved**. This page states the actual-color consequences obtained
so far and the precise limits of transferring earlier mechanisms.

## 1. Every three-direction slice has a connectivity criterion

Fix three directions and all the other coordinates. On
$[a]\times[b]\times[c]$, identify a first-direction line with
the edge between its second and third labels, and similarly cyclically.
Thus lines correspond to the edges of $K_{a,b,c}$.

**Proposition.** A line subset $C$ is dissociated if and only if its
complementary edge graph is connected. Equivalently, dissociation and
rational independence coincide on this slice.

Indeed a line relation is exactly
$$
A(y,z)+B(x,z)+C(x,y)=0.
$$
Its solutions are exactly
$$
A(y,z)=u_y-v_z,\qquad B(x,z)=v_z-w_x,
\qquad C(x,y)=w_x-u_y.
$$
To verify completeness, fix a reference $x_0$ in the first part;
the equation at $x_0$ splits $A$ into a function of $y$
plus one of $z$, and the remaining equations determine $w_x$.
These are graph gradients with the displayed cyclic edge orientations.
A nonzero gradient supported on a given edge subset exists precisely when
its complement is disconnected. A component indicator potential gives a
supported gradient with coefficients $0,\pm1$, proving the claim.

Therefore any proper finite coloring must leave a connected complement
after deleting **each individual color** in **each** three-direction slice.
In a proper two-coloring both color graphs must be connected and spanning.
This is a simultaneous actual-color constraint, but no global contradiction
has been obtained from it.

Elementary planes alone cannot be forced for arbitrary colorings. The
two-coloring $c_i(x_{-i})=\sum_{j\ne i}x_j\pmod2$ uses both
colors among the direction-$i$ lines of every $(i,j)$-plane,
since the fixed $j$-label varies over both parities. Hence no whole
elementary plane trade is monochromatic. This is not a proper coloring of
the full relation system; the three-direction criterion supplies larger
relations that it fails to avoid.

The collapse to rational independence fails in four directions. The
[fixed exact certificate](../evidence/axis_line_circuit/_index.md), checked by
[a finite verification script](../evidence/axis_line_circuit/main.py), gives
27 lines in $[3]^4$, rank 26, with one primitive relation having one
coefficient two and all other coefficients $\pm1$. Thus that support
is a dissociated rational circuit. The finite discovery and checking bounds
are recorded on the certificate page.

## 2. A stronger fixed-height lower bound, not unbounded coloring

For general sides $d_i$, write $N=\prod_i d_i$ and
$s=\sum_i1/d_i$. If all $q$ classes are height-$h$
independent, then
$$
s\log(h+1)\leq
\frac q2\log\left(2\pi e\left[
\frac{h(h+2)t}{12q}+\frac1{12}\right]\right).
\tag{2}
$$
Here and below height bounds coefficient magnitude with unrestricted support.

For each color class independently, choose independent uniform coefficients
$U_\ell\in\{0,\ldots,h\}$. Its line sums are injective in these
coefficients, so their joint discrete entropy is
$|C|\log(h+1)$. At a point $x$, the sum has variance
$\sigma_h^2 n_C(x)$, where
$\sigma_h^2=h(h+2)/12$ and $n_C(x)$ counts its incident lines
of that color.

For an integer-valued variable $Z$, add an independent uniform variable
on $[-1/2,1/2]$. Its differential entropy equals $H(Z)$ and its
variance is $\operatorname{Var}(Z)+1/12$. Comparing its density to
the Gaussian of the same mean and variance, nonnegativity of relative
entropy gives
$$
H(Z)\le\tfrac12\log\bigl(2\pi e(\operatorname{Var}(Z)+1/12)\bigr).
$$
For completeness, that nonnegativity follows by applying
$\log u\le u-1$ to the ratio of the comparison density to the
given density and integrating. Expanding the Gaussian logarithm gives
the displayed variance bound.

Entropy subadditivity over points, followed by concavity of the logarithm
over the colors, proves (2): every point lies on exactly $t$ lines,
so $\sum_C n_C(x)=t$, and there are $N$ points.

For $d_i=i+2$, divide (2) by $\log t$ and pass to the limit.
Any fixed $q,h$ valid for all stages must satisfy
$$
q\ge2\log(h+1). \tag{3}
$$
In particular, sufficiently large stages have $\chi_2(L_t)\ge3$.
This is not infinite $\chi_2$, and (3) does not establish (1).

### Keeping the full averaged covariance has the same leading bound

Let $A$ be the full line matrix. Applying the Gaussian bound to
the whole jittered sum vector in each color, then using concavity of
$\log\det$, gives the stronger finite necessary inequality
$$
s_t\log(h+1)\le\frac q2\,
\mathbb E\log\left(2\pi e\left[
\frac{\sigma_h^2}{q}\Lambda_t+\frac1{12}\right]\right),
\qquad
\Lambda_t=\sum_{i\le t}d_i B_i,
\tag{3a}
$$
where the $B_i$ are independent Bernoulli variables of probabilities
$1/d_i$. Indeed
$AA^{\mathsf T}=\sum_i I\otimes J_{d_i}\otimes I$;
its eigenvalue $\sum_{i\in S}d_i$ has multiplicity
$\prod_{j\notin S}(d_j-1)$. Dividing the log determinant by the
row count gives precisely the expectation in (3a). The covariance of a
color's jittered sum is $\sigma_h^2 A_cA_c^{\mathsf T}+I/12$,
and averaging these positive definite matrices justifies the stated use
of concavity.

For linear sides and fixed $a,b>0$,
$\mathbb E\log(a\Lambda_t+b)/\log t\to1$. Jensen's inequality
and $\mathbb E\Lambda_t=t$ give the upper bound. For the lower
bound, some $B_i=1$ with $i\ge\varepsilon t$ occurs with
probability tending to $1-\varepsilon$: the complementary product
$\prod(1-1/(i+2))$ telescopes. On that event
$\Lambda_t\ge\varepsilon t$; elsewhere the logarithm is bounded
below by $\log b$. Let $\varepsilon\downarrow0$.
Thus this averaged full-covariance estimate still gives only (3), not
unbounded fixed-height coloring. No limitation is asserted for arguments
retaining additional color-specific information before averaging.

## 3. Why the earlier focusing theorem cannot be imported automatically

The root-family fixed-height focusing theorem uses multiplicative closure
and conductor-disjoint products. The linearly growing line family has no
proved replacement for those properties. Its full tensor products actually
lose uniform extraction.

For two stages $L_s,L_t$, the tensor family has $N_sN_t$ rows,
$N_sN_t s_s s_t$ columns, and exactly $st$ ones in each full
row. All subset sums lie in $[0,st]^{N_sN_t}$, so any dissociated
subfamily $D$ satisfies
$$
2^{|D|}\le(1+st)^{N_sN_t},\qquad
\frac{|D|}{|L_s\otimes L_t|}
\le\frac{\log_2(1+st)}{s_s s_t}. \tag{4}
$$
For the linear schedule the right side tends to zero whenever both stages
tend to infinity, even at different rates. This excludes full-product
flattening as a uniformly extracting family, not a thinner selected support.
Thus unbounded coloring at a fixed height greater than one for this new
family would itself still require a coefficient-safe transfer to (1).

Ordinary product-Ramsey trimming also needs an additional idea. If every
alphabet is replaced by a proper subset $A_i\subsetneq[d_i]$,
retain the full lines whose fixed coordinates lie in the $A_j$.
Each retained direction-$i$ line has a private point with its varying
coordinate outside $A_i$. That point belongs to no other retained line.
The retained family is therefore rationally independent. More generally,
only untrimmed directions can participate in a relation. A monochromatic
trimmed subbox alone cannot supply a line trade.

## 4. Exact actual-color extension test

Let $X$ be a fixed old box and add one coordinate $[d]$.
For a given coloring, write $C_{s,c}$ for the old direction lines
of color $c$ in layer $s$, and $P_c\subset X$ for points
whose new-axis line has color $c$. Let $\Sigma_h(C)$ denote
the sums on $C$ with integer coefficients in $[-h,h]$.
Then the coloring is height-$h$ proper if and only if every
$C_{s,c}$ is height-$h$ independent and
$$
\left(\bigcap_{s=1}^d\Sigma_h(C_{s,c})\right)
\cap\{-h,\ldots,h\}^{P_c}=\{0\}
\quad\text{for every }c. \tag{5}
$$
The last cube denotes vectors on $X$ vanishing outside $P_c$.

Indeed the new-axis coefficients give one common vector $b$ on
all layers. A monochromatic relation requires each old layer to represent
$-b$. When $b\ne0$, these representations and the new-axis
coefficients yield precisely the forbidden common vector in (5). When
$b=0$, a nontrivial relation is exactly an internal old-layer relation.
This proof assumes no uniqueness of signed representations.

The test makes the missing coupling explicit: common old-layer signed sums
must also have bounded coordinates and be supported on points carrying
the actual new-axis color. No lower bound forces such a common vector.

There is an exact nested-alphabet model for the linear schedule: take three
fixed roots numbered $0,1,2$; vertex $i+2$ chooses any smaller
number as its parent. Complete choices are recursive forests, and a line
leaves one parent choice unspecified. This is a bijective relabeling only.
No Ramsey theorem for monochromatic trades follows just from that model.

The connectivity criterion, entropy calculation, and tensor-product bound
received independent internal checks. None supplies the missing actual-color
ternary relation for every finite palette.
