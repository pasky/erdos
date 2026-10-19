---
name: research/erdos_774/lemmas/galois_color_slices
title: Sign-coherent Galois differences and actual-color slices
desc: Orbitwise sign coherence makes differences of equal-value root supports ternary after all collisions; actual-color slice counting needs no monochromatic whole support, but a generating-function ceiling excludes its coordinatewise counting test for linearly growing axis lines.
tags: [E0774, proved, algebra, coloring, conditional, incomplete]
sources: []
created: 2026-09-18T19:02:16Z
updated: 2026-09-18T19:02:16Z
---


# Sign-coherent Galois differences and actual-color slices

***

## Standing

This is a coefficient-safe alternative to the mixed products in
[Galois squaring](galois_squaring.md). Equal evaluated sums can be
subtracted without coefficients exceeding one when their formal signs
agree on overlaps. An actual-color slice version does not require whole
supports to be monochromatic.

These are proved conditional mechanisms, not unbounded coloring theorems.
No arbitrary coloring has been shown to supply the required equal slice
values or a family violating the counting criterion. Section 6 proves
that the coordinatewise cardinality criterion cannot itself give an
unbounded coloring conclusion for the new linearly growing axis-line
family, even with nonconstant target sums.

## 1. A sign-coherent Galois difference

Let $N$ be odd, let $B\subset\mu_N$, and suppose
$$
U=\sum_{b\in B}\epsilon_b[b],\qquad
\sum_{b\in B}\epsilon_b b=h,
\qquad \epsilon_b\in\{\pm1\},\quad h\in\mathbb Z.
\tag{1}
$$
Here brackets denote the formal basis of $\mathbb Z[\mu_N]$.
Let $H$ be a subgroup of the cyclotomic Galois group. Assume the
signs extend to an $H$-invariant function
$$
\eta:HB\longrightarrow\{\pm1\}.
\tag{2}
$$
Equivalently, no $H$-orbit meets both a positive and a negative
leaf of $U$.

**Lemma.** For $\sigma,\tau\in H$, the difference
$$
R_{\sigma,\tau}=\sigma U-\tau U
\tag{3}
$$
evaluates to zero and has coefficients in $\{0,\pm1\}$.
It is nonzero precisely when its two formal summands differ.

**Proof.** Every conjugate evaluates to the same rational integer $h$.
A root in both supports has coefficient $\eta(g)$ in both and
cancels. A root in exactly one support has coefficient $\pm1$.
This accounts for every collision. The nontriviality assertion is the
definition of formal inequality. $\square$

Thus two distinct conjugate leaf supports, individually monochromatic
in the same actual color, give a nonzero monochromatic ternary relation.
Neither the color of the pivot $1$ nor the magnitude of $h$
enters this conclusion.

For a relation $\sum\epsilon_b b=hw$, first divide by $w$
and pull the coloring back under multiplication by $w$. Equivalently,
use the centered permutations $b\mapsto w\sigma(b/w)$.
This is a valid change of coloring because multiplication by a nonzero
root preserves all signed additive relations.

### A finite refinement consequence

Suppose $q+1$ chosen automorphisms $\sigma_0,\ldots,\sigma_q$
give distinct formal conjugates of $U$. Under a proper dissociated
$q$-coloring $f$, the leaf set $B$ cannot be monochromatic
for the refinement
$$
b\longmapsto
\bigl(f(\sigma_0b),\ldots,f(\sigma_qb)\bigr).
\tag{4}
$$
Otherwise each conjugate leaf support has one actual color. Two have
the same color, contradicting the lemma. For odd $N$, powers of
squaring may be used when they produce sufficiently many distinct images.

This is independent of $h$, but does not force a support satisfying
(1)--(2) to be monochromatic for (4).

## 2. Exact verification on the twenty-point root circuit

Use the labels and coefficients in the
[twenty-point circuit](prime_tensor_circuit.md). Its pivot is
$w=(0,0,1)$ in $C_3\times C_5\times C_7$, with coefficient
$-2$. Divide by $w$, that is, subtract this exponent tuple.
Put $J=\{0,3,4,5,6\}$, $K=\{2,3,4\}$. The nineteen
leaves and their right-hand-side signs become:

| Normalized leaves | Sign | Number of nonzero coordinates |
|---|---:|---:|
| $(0,0,z-1)$, $z\in J$ | $-1$ | 1 |
| $(0,1,1)$ | $+1$ | 2 |
| $(0,y,0)$, $y\in K$ | $-1$ | 1 |
| $(1,0,1)$ | $+1$ | 2 |
| $(1,1,z-1)$, $z\in J$ | $-1$ | 3 |
| $(2,1,0)$ | $+1$ | 2 |
| $(2,y,1)$, $y\in K$ | $-1$ | 3 |

All exponents are reduced in their displayed cyclic groups. In particular
$z-1\ne0\pmod7$. Since these conductors are distinct primes,
$$
\epsilon_b=\mu(\operatorname{ord}b),\qquad
\sum_{b\in B}\mu(\operatorname{ord}b)b=2.
\tag{5}
$$
The sign is therefore invariant under the full Galois group.

The formal Galois orbit has exactly $48=\varphi(105)$ members.
Indeed the pure order-five leaves are all nonidentity fifth roots except
$\zeta_5$, and the pure order-seven leaves are all nonidentity seventh
roots except $\zeta_7$. A stabilizer fixes both coordinates. The
unique order-21 leaf, $(1,0,1)$, then forces it to fix the third-order
coordinate as well. The stabilizer is trivial. The squaring orbit has
length $\operatorname{lcm}(2,4,3)=12$.

Thus at most $q$ of these 48 distinct leaf supports can be individually
monochromatic under a proper $q$-coloring. This is an upper bound on
good conjugates, not a lower bound ensuring any exist.

## 3. Actual-color slices without monochromatic whole supports

Fix a proper dissociated $q$-coloring $f$. For a conjugate in
Section 1 and a color $c$, put
$$
U_{\sigma,c}
=\sum_{\substack{g\in\sigma B\\f(g)=c}}\eta(g)[g].
\tag{6}
$$

**Slice injectivity.** Equal evaluations of two color-$c$ slices imply
their formal equality.

Indeed their difference has coefficients in $\{0,\pm1\}$, because
the common sign function agrees on overlaps, and every surviving root has
actual color $c$. A nonzero difference would violate properness.

Consequently the first $q-1$ evaluated slices determine the whole
formal conjugate: equality of those slices gives equality of the last
evaluated slice because each total is $h$; slice injectivity then
identifies all formal slices. For $q=1$, this says that at most one
distinct conjugate can occur under a proper one-coloring.

The same argument works for any family of distinct supports having the
same evaluated signed sum and using one common sign function. A Galois
action is not necessary for this version.

## 4. A same-conductor positive counting criterion

Assume now that $N$ is squarefree and odd, and put
$D=\varphi(N)$. Let $\mathcal F$ be a family of distinct subsets
$B\subset\mu_N$ satisfying
$$
\sum_{b\in B}\mu(\operatorname{ord}b)b=h,
\qquad h\in\mathbb Z_{\ge0}.
\tag{7}
$$
Then any proper dissociated $q$-coloring satisfies
$$
\boxed{\displaystyle
|\mathcal F|\le
\binom{h+q-1}{q-1}^{D}.}
\tag{8}
$$
In particular a strict violation forces an actual-color ternary relation,
without monochromatic whole supports or monochromatic product blocks.

### Proof with all basis signs explicit

Fix primitive roots $\zeta_p$, for $p\mid N$, and use the basis
$$
e_a=\prod_{p\mid N}(-\zeta_p^{a_p}),
\qquad 1\le a_p<p.
\tag{9}
$$
In each prime factor the nonidentity roots form a rational basis;
the cyclotomic degree formula makes their tensor products a basis for
$\mathbb Q(\zeta_N)$. The minus sign in every factor of (9) is
intentional.

Write $b=\prod_{p\mid N}\zeta_p^{b_p}$, with $0\le b_p<p$.
Using $1=\sum_{a=1}^{p-1}(-\zeta_p^a)$ at the zero coordinates,
$$
\mu(\operatorname{ord}b)b
=\sum_{\substack{a:\ a_p=b_p\ \text{whenever }b_p\ne0}}e_a.
\tag{10}
$$
Thus each signed root in (7) is a nonempty $0/1$ cylinder indicator
in this basis, and $1=\sum_a e_a$. Equation (7) says that these
cylinders cover every basis coordinate exactly $h$ times.

For each $B$ and color, its slice coordinates are nonnegative integers.
At any one basis coordinate the $q$ slice values sum to $h$,
allowing $\binom{h+q-1}{q-1}$ possibilities. Slice injectivity makes
the entire array of these values injective on $\mathcal F$. Multiplying
over the $D$ coordinates proves (8). If $h=0$, positivity forces
$B=\varnothing$, consistent with the bound. $\square$

### General incidence-vector form

For any finite indexed $0/1$ column configuration on a row set $X$,
let $\mathcal F_v$ be a family of subsets of column labels having
one common sum $v\in\mathbb Z_{\ge0}^{X}$. A proper dissociated
$q$-coloring of the labels necessarily gives
$$
|\mathcal F_v|
\le\prod_{x\in X}\binom{v_x+q-1}{q-1}.
\tag{11}
$$
This is the same slice-injectivity proof with all column signs positive.
In particular it applies directly to the axis-line indicators. The count
is of subsets of labels, with no repeated use of a column.

## 5. General circuits need not have coherent full-Galois signs

Normalization at the unique heavy column does not automatically supply
the hypothesis of Section 1 for the full Galois group. In the graph-cut
circuit from [the prime staircase](prime_staircase_obstruction.md), take
$p\ge5$ and normalize the heavy pivot
$(u_2,v_2,\text{layer }0)$ to $1$. The layer-one leaves
$$
(u_4,v_1,\text{layer }1),\qquad
(u_3,v_3,\text{layer }1)
\tag{12}
$$
have right-hand-side signs $+1,-1$, respectively. For the cut used
there, $u_4$ is inside and $v_1$ outside; $u_3$ is outside
and $v_3$ inside, giving these opposite cut signs. The right-hand-side
leaf signs in layer one equal the cut signs.

Both leaves differ from the pivot in all three coordinates, so both have
relative order $pqr$. They therefore belong to one full Galois orbit
but have opposite signs. Further Galois conjugation cannot repair this
shared-order conflict. Smaller subgroups can still have coherent signs;
no assertion excludes such a choice.

## 6. A ceiling for all positive target-cover counts of linear axis lines

Let $X=\prod_{i=1}^t[d_i]$, where $d_i=i+2$, and let $L$
be all full axis-line indicators. For
$v\in\mathbb Z_{\ge0}^{X}$, write
$$
\mathcal C_v={A\subseteq L:\ \sum_{\ell\in A}\ell=v\}.
$$
The following ceiling concerns the cardinality test (11) alone. It is
**not** a proper two-coloring, and does not bound $\chi_1(L)$.

**Proposition.** For $v\ne0$, putting $S=\{x:v_x>0\}$,
$$
\boxed{\displaystyle
|\mathcal C_v|
\le e^{-|S|/32}\prod_{x\in S}(v_x+1)
<\prod_{x\in X}(v_x+1).}
\tag{13}
$$
Also $|\mathcal C_0|=1$. In particular, no target $v$, uniform
or nonuniform, violates even the $q=2$ instance of (11).

### Generating-function proof

Every line selected by a cover of $v$ must lie in $S$. Assign
$0<z_x<1$ to $x\in S$. The coefficient generating function gives
$$
|\mathcal C_v|
\le \prod_{x\in S}z_x^{-v_x}
\prod_{\substack{\ell\in L\\\ell\subseteq S}}
\left(1+\prod_{x\in\ell}z_x\right).
\tag{14}
$$
For a line in direction $i$, arithmetic--geometric mean gives
$$
\prod_{x\in\ell}z_x
\le\frac1{d_i}\sum_{x\in\ell}z_x^{d_i}.
$$
Lines in one direction are disjoint, so using $\log(1+u)\le u$
in (14) yields
$$
\begin{aligned}
\log|\mathcal C_v|
&\le\sum_{x\in S}
\left[-v_x\log z_x+\sum_{i=1}^t\frac{z_x^{d_i}}{d_i}\right]\\
&\le\sum_{x\in S}
\left[-v_x\log z_x-\log(1-z_x)-z_x-\frac{z_x^2}{2}\right].
\tag{15}
\end{aligned}
$$
The empty-cover-family case is immediate and need not take a logarithm.

For an integer $a=v_x\ge3$, choose $z_x=a/(a+1)$. Then
$$
-a\log z_x=a\log(1+1/a)<1,
\qquad z_x+z_x^2/2\ge33/32,
$$
so the summand in (15) is less than $\log(a+1)-1/32$.
For $a=1,2$, choose $z_x=2/3$. In both cases the difference
from $\log(a+1)$ is
$$
2\log(3/2)-8/9<-1/18<-1/32.
$$
For example convexity of $1/u$ gives
$\log(3/2)<5/12$, proving the displayed estimate. Summing proves
(13).

For a uniform target $v=h\mathbf1$, $h\ge1$, this specializes to
$$
|\mathcal C_{h\mathbf1}|
< (h+1)^{|X|},
$$
which already lies below the two-color slice capacity. A new argument
would have to exploit additional constraints on the attainable color-slice
functions, not merely their coordinatewise nonnegative counts.

No numerical experiment or external source theorem was used in this page.
The signs, orbit sizes, color-slice arguments, and all-target generating
bound passed independent internal review. They do not establish the
required counterexample.
