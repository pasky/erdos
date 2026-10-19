---
name: research/erdos_132/similarity_word_sets
title: Rarity grows in dense fixed-similarity word constructions
desc: |
  A self-similar measure gives zero mass to every convex boundary;
  this excludes dense selected similarity-word sets as bounded-R families.
sources: []
research_state: closed
created: 2026-09-23T02:02:46Z
updated: 2026-09-24T22:12:56Z
---


# Rarity grows in dense fixed-similarity word constructions

***

Fix $b\ge2$ contractive planar similarities

$$f_i(x)=r_iU_ix+t_i,\qquad 0<r_i<1,$$

allowing reflections, and fix a seed $p$. Write
$f_w=f_{w_1}\circ\cdots\circ f_{w_d}$ for a word $w$ of length $d$.
Suppose

$$A_d\subseteq\{f_w(p):|w|=d\},\qquad |A_d|\ge c b^d$$

for a fixed $c>0$. Then $R(A_d)\to\infty$.

Arbitrary selection and collisions are allowed subject to the displayed
positive-density condition. The maps are fixed, not depth-dependent.
This is a restricted construction theorem, not a solution of
[Problem 132](../../problems/distance_problems/E0132/_index.md).

The later [full-orbit theorem](full_similarity_orbits.md) removes
the density assumption when $A_d$ is the entire set of word images.
The theorem below remains useful for arbitrary selected subsets
at positive formal density.

## A measure lemma

Let $K$ be the compact attractor and $\mu$ the self-similar probability
measure with uniform symbol weights. First suppose $K$ is noncollinear.
Then **every affine line and every boundary of a compact convex set
has $\mu$-measure zero**.

The measure is nonatomic. Otherwise its largest atomic mass $a>0$
is attained, and the set $M$ of atoms of mass $a$ is finite and
nonempty. For $x\in M$, stationarity gives

$$a=\frac1b\sum_i\mu(\{f_i^{-1}(x)\}).$$

Every summand is at most $a$, so every preimage belongs to $M$.
Thus each $f_i$ permutes $M$. Strict contraction of diameter makes
$M$ a singleton fixed by all the maps. Their attractor would be
that singleton, contrary to the assumption.

Let $\pi:\{1,\ldots,b\}^{\mathbb N}\to K$ be the coding map with
Bernoulli measure. Suppose a convex boundary $\Gamma$ has positive
$\mu$-measure. A planar convex boundary has at most countably many
points without a unique tangent. Choose an address $\omega$ such
that $x=\pi(\omega)\in\Gamma$ has a tangent line $L_x$, and the
conditional-probability martingale for the event $\pi(\omega)\in\Gamma$
converges to one. For the prefix $w$ of length $d$, this says

$$\mu(f_w^{-1}\Gamma)\longrightarrow1. \tag{1}$$

Let $\rho_w$ be the contraction ratio of $f_w$ and
$D=\operatorname{diam}K$. Since $x\in f_w(K)$,
$f_w(K)\subseteq B(x,D\rho_w)$. Differentiability at $x$ therefore
gives $\epsilon_d\to0$ such that

$$f_w^{-1}(\Gamma)\cap K
\subseteq\{y:\operatorname{dist}(y,L_d)\le D\epsilon_d\},
\qquad L_d=f_w^{-1}(L_x). \tag{2}$$

Each $L_d$ meets $K$ at the coded tail point. A subsequence of these
lines converges to a line $L$. By (1)--(2), every fixed neighborhood
of $L$ has full $\mu$-measure, hence $\mu(L)=1$. Full support of
$\mu$ implies $K\subseteq L$, a contradiction. When $\Gamma$ is
an affine line the same argument uses zero strip width. Degenerate
compact convex sets are contained in lines. This proves the lemma.

## Dense distinct images have negligible convex layers

Define the word and distinct-point measures

$$\eta_d=b^{-d}\sum_{|w|=d}\delta_{f_w(p)},\qquad
\nu_d=|A_d|^{-1}\sum_{a\in A_d}\delta_a.$$

Uniform contraction gives $\eta_d\Rightarrow\mu$. Every selected
point has at least one word representative, so

$$\nu_d\le\frac{b^d}{|A_d|}\eta_d\le c^{-1}\eta_d.$$

Thus every weak subsequential limit $\nu$ satisfies
$\nu\le c^{-1}\mu$.

Here is the needed convex-layer passage. Suppose finite sets $S_j$
lie in a fixed compact region, their sizes tend to infinity, and
every weak limit of their uniform measures is dominated by a fixed
multiple of $\mu$. If a positive proportion of their points lay
on their convex-hull boundaries, pass to a subsequence with empirical
limit $\nu$ and Hausdorff convex-hull limit $C$. The measure $\nu$
is supported on $C$. The measure lemma shows that $C$ has interior
and $\nu(\partial C)=0$. Boundaries of convex bodies converging in
Hausdorff distance to a body with interior converge to its boundary.
All those boundary points therefore eventually lie in any prescribed
closed $\delta$-neighborhood of $\partial C$. The portmanteau
inequality and then $\delta\downarrow0$ contradict the positive
boundary proportion.

Apply this observation to $A_d$. Its first vertex layer has $o(|A_d|)$
points. Removing that many points changes the normalized empirical
measure by $o(1)$ in total variation. Repeating the observation proves

$$|B_k(A_d)|=o(|A_d|)\quad\text{for every fixed }k,$$

where $B_k$ is the union of the first $k$ convex vertex layers.
No assertion that the post-deletion hull limit equals
$\operatorname{conv}K$ is needed.

The [rank--layer bound](layers_and_obstructions.md) now gives

$$m_{A_d}(r_k)\le2k|B_k(A_d)|=o(|A_d|)$$

for the $k$-th largest distinct distance. Each fixed rank exists
eventually by the two-anchor bound $n\le2q^2+2$. Hence any prescribed
number of largest distances are eventually rare.

## Degenerate attractors

If $K$ has at least two points and lies on a line $L$, every $f_i$
preserves $L$. In coordinates with $L=\{y=0\}$ its normal
coordinate is $y\mapsto\beta_i y$. At depth $d$ that coordinate
depends only on the symbol counts. Thus the word images are covered
by at most $\binom{d+b-1}{b-1}$ parallel lines. This is
$o(\sqrt{|A_d|})$, so even the elementary direct
[line-cover bound](line_covers.md) gives rarity growth.

If $K=\{o\}$, all maps fix $o$. A word image's radius about $o$
depends only on symbol counts. Its angle is an integer combination
of the finitely many map angles, with coefficients in $[-d,d]$,
together with a reflection parity. The number of distinct images
is therefore polynomial in $d$, contradicting $|A_d|\ge c b^d$.

A separate author proved the measure lemma and layer passage; the
author checked the martingale localization, nonatomicity, dominance,
degenerate cases, and use of the rank--layer bound. The argument is
author-recorded. This measure argument
alone does not cover arbitrary sets, nonstationary similarities, or
selected image sets of vanishing formal density. The later full-orbit
result treats all full image sets, but not arbitrary sparse selections.
