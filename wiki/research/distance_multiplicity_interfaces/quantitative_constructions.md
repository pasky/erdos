---
name: research/distance_multiplicity_interfaces/quantitative_constructions
title: "Quantitative distance constructions"
desc: "Clearance controls measurable area, generic subset sums control the second distance multiplicity, and residual packing fills preserve a boundary coefficient."
created: 2026-10-14T15:30:27Z
updated: 2026-10-14T15:30:27Z
---

***

The deductions and obstructions here are author-recorded by Plasma AI.
Source-dependent conclusions retain the named premises and reading limits. No
independent review, novelty claim or complete solution of the linked problems
follows from this account.

The relevant questions are [[problems/distance_problems/E0953/_index|E0953]],
[[problems/distance_problems/E0959/_index|E0959]],
[[problems/distance_problems/E1084/_index|E1084]].

## Quantitative construction interfaces

## E0953: the finite clearance objective must retain area

Write $N(r,\delta)$ for the largest size of a finite set in the radius-$r$ disk
whose distinct-center lengths are all at distance at least $\delta$ from every
integer, including zero. Let $0<\delta<1/10$. Around a set $P\subset B_{r-1}$
with this clearance, put open disks of radius $\delta/4$. They are disjoint
because distinct centers are at least $\delta$ apart. They lie inside $B_r$.
Within each small disk all distances are below one. Between two disks the change
from the center distance is less than $\delta/2$, so every positive integer is
still avoided. The area is exactly
$$
 \frac{\pi}{16}\delta^2|P|.
$$

Conversely, take a compact subset $K$ of any admissible measurable set in $B_r$.
Its distance image is compact and avoids the finitely many positive integers in
its range, hence has a positive clearance $\eta$. For
$0<\delta<\min(\eta,1/10)$, a maximal $\delta$-separated net $P\subset K$ is
finite, covers $K$ by radius-$\delta$ disks, and satisfies the clearance
condition also at zero. Thus
$|K|\le\pi\delta^2|P|\le\pi\sup_\delta\delta^2N(r,\delta)$. Inner regularity of
Lebesgue measure gives the same upper bound for the area supremum. This is the
robust reduction in the inspected proof of Chojecki's Lemma 2, with an explicit
lower-bound constant and radius shift.

To prove the requested $M(r)\gg\sqrt r$, a finite construction must achieve
$\delta^2|P|\gg\sqrt r$. A finite set with noninteger distances always has some
positive clearance, but that clearance can be too small for the desired area.
The next test must quantify it. The source's kernel construction and stronger
quantitative claims were not re-audited; the exponent-level result is not
mistaken for the missing constant-factor result.

## E0959: a fully controlled $n\log n$ gap

Choose $t\ge2$ unit vectors $v_1,\ldots,v_t$ in generic planar directions and
form all subset sums $p_\varepsilon=\sum_i\varepsilon_i v_i$,
$\varepsilon\in\{0,1\}^t$. There are $n=2^t$ distinct points for generic
directions. A nonzero difference has coefficient vector $c\in\{-1,0,1\}^t$, with
squared norm
$$
 \sum_i c_i^2+2\sum_{i<j}c_ic_j\cos(\theta_i-\theta_j).
$$
The distinct nonconstant Fourier characters and the constant term are linearly
independent. Consequently two such norm polynomials are identical only if both
supports are singletons, or if the support has at least two entries and the
vectors agree up to an overall sign. Indeed the off-diagonal products $c_ic_j$,
together with support size, determine the support and all relative signs. All
other equalities, and all collisions, are nonzero analytic equations in the
angles. Their finite union has empty interior, so they can all be avoided
simultaneously.

A signed difference with support size $s$ then occurs in $2^{t-s}$ unordered
pairs: the coordinates outside the support may be chosen freely, and reversing
the pair supplies the negative difference rather than an additional unordered
pair. All $t$ singleton supports merge into the unit class, giving multiplicity
$t2^{t-1}=tn/2$. Every other class has multiplicity at most $2^{t-2}=n/4$, and
support two attains that bound. Hence
$$
 M(n)\ge \frac n2\log_2 n-\frac n4\qquad(n=2^t,\ t\ge2).
$$
Generic padding to any larger order below $2n$ adds only singleton new lengths:
choose each new point off the finitely many old-distance circles and
perpendicular bisectors. This proves an $\Omega(n\log n)$ gap for all
sufficiently large orders.

This direct specialization is consistent with the inspected proof of
Clemen--Dumitrescu--Liu Theorem 1.9 and Corollary 1.10 in Section 4. It is not a
new matching upper bound or an acceptance of stronger pending claims. A
construction with many unit pairs does not by itself bound its second-richest
distance. Any attempted improvement must inspect that competitor explicitly.

## E1084: extend the special-size packing coefficient to all sizes

Normalize minimum center distance to one, and let $f(n)=f_3(n)$ count unordered
contacts. The inspected statement recalled on page 2 of Bezdek--Reid gives, with
$$
 c=486^{1/3}=6(3/2)^{2/3},\qquad n_k=(2k^3+k)/3,
$$
the strict inequality $f(n_k)>6n_k-cn_k^{2/3}$ for $k\ge2$. Their
unit-radius-ball convention has contact distance two; scaling the centers by one
half gives this normalization with the contact count unchanged. The earlier
construction proof cited there was not inspected. The following interpolation is
conditional only on that displayed source statement.

Distant union gives $f(a+b)\ge f(a)+f(b)$, and adding distant isolated points
gives monotonicity. For $n\ge6$, take the largest $k$ with $n_k\le n$, and set
$r=n-n_k$. Then
$$
 r<n_{k+1}-n_k=2k^2+2k+1\le4k^2
       \le4(3n/2)^{2/3}.
$$
Monotonicity first yields
$$
 f(n)>6n-6r-cn^{2/3}\ge6n-5cn^{2/3}.
$$
The weak inequality $f(n)\ge6n-5cn^{2/3}$ holds also for $0\le n\le5$, because
the right side is nonpositive; put $f(0)=0$. Fill the residual with this uniform
construction, instead of isolated points. Superadditivity now gives
$$
\begin{split}
 f(n)&>6n-cn_k^{2/3}-5cr^{2/3}\\
     &\ge6n-cn^{2/3}-C n^{4/9},\\
 C&=5c\,4^{2/3}(3/2)^{4/9},\qquad n\ge6.
\end{split}
$$
Thus the coefficient $c$ in the construction's $n^{2/3}$ deficit extends
asymptotically to every size. This is a completed conditional deduction with an
explicit error term, not a claim of novelty. The inspected upper theorem is
$f(n)<6n-0.926n^{2/3}$, so the boundary constant remains between 0.926 and
$c=7.862\ldots$. Neither the exact function in dimension three nor the
higher-dimensional question is settled. The theorem and recalled lower bound
were checked against PDF page 2; no transcription correction was needed.

## Source interfaces

These source locators identify the uses in this account. Statement and account
reading do not certify a source proof; proof reading here is author inspection
and confers no independent standing.

- [[../library/distance_problems/bezdek_2013_contact_graphs_unit_sphere_packings_revisited/_index|bezdek
  2013 contact graphs unit sphere packings revisited]]: Section 1, Theorem 1 and
  immediately following recalled lower bound, PDF p.2 (statement reading).
- [[../library/distance_problems/chojecki_2026_order_growth_planar_sets_avoiding_integer/_index|chojecki
  2026 order growth planar sets avoiding integer]]: Section 1, Lemma 2 and its
  proof (proof reading). Section 1, Theorems 1 and 3 (statement reading).
- [[../library/distance_problems/clemen_2025_multiplicities_interpoint_distances/_index|clemen
  2025 multiplicities interpoint distances]]: Section 4, proof of Theorem 1.9
  and deduction of Corollary 1.10 (proof reading). Theorem 1.9; Corollary 1.10;
  Problem 1.11 (statement reading).
