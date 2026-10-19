---
name: research/erdos_774/routes/moment_gaussian_coloring
title: Actual two-colorings from stable moment lattices
desc: The logarithmic-scale reverse-Minkowski argument gives actual two-colorings away from the boundary; boundary extraction is proved by a separate argument, while its arbitrary-color growth remains open.
tags: [E0774, Boolean-moments, coloring, proved, incomplete]
sources: []
created: 2026-09-18T23:14:00Z
updated: 2026-09-18T23:28:00Z
---


# Actual two-colorings from stable moment lattices

***

[Boundary extraction](moment_boundary_extraction.md) is proved by a
different, dimension-uniform exponential theta bound. This does not change
the actual two-color regime proved below or supply a boundary coloring
theorem.

## The finite theorem

For 1<=k<d, write

$$
 n=2^d,\quad r=\sum_{j=0}^k\binom dj,\quad m=n-r,
 \quad D=(d-k)\binom dk,\quad s=2^{D/(2m)}.
$$

Then the following explicit condition implies a partition of the entire
moment configuration into two fully dissociated classes:

$$
 \boxed{s\geq10(\log m+2)\sqrt{\pi/\log2}
       \quad\Longrightarrow\quad \chi_1(E_{d,k})=2.} \tag{1}
$$

Unsubscripted logarithms are natural. This is a statement about **all**
ternary relations and arbitrary support sizes, not just cube templates.
Consequently these parameter pairs also have hereditary extraction
constant at least 1/2. They cannot form the desired counterexample.

### Checked external input

[Regev--Stephens-Davidowitz, *A Reverse Minkowski Theorem*](../../../../library/discrete_geometry/regev_stephens_davidowitz_2016_reverse_minkowski_theorem/_index.md),
[full arXiv version 4, Theorem 1.2 and its definition of rho_s](https://arxiv.org/html/1611.05979v4#S1.Thm2),
states: for a rank-m Euclidean lattice K whose every sublattice has determinant
at least one,

$$
 \sum_{z\in K}\exp(-\pi t^2\|z\|^2)\leq3/2,
 \qquad t=10(\log m+2). \tag{2}
$$

The primary abstract was read first, followed by the full theorem and
the Gaussian normalization. This page uses (2), not an unproved
constant-parameter strengthening or a volume-only bound. The paper is
also published in *Annals of Mathematics* 199 (2024), 1--49.

### Proof of (1)

Let L be the integer relation lattice of E_(d,k). Multiplication by full parity
identifies it isometrically with L_(d,d-k-1). Its rank is m and determinant is
2^(D/2), by the [exact phase-lattice calculation](moment_phase_lattice.md). The
[semistability theorem](../lemmas/moment_lattice_stability.md) proves that
K=s^(-1)L satisfies every hypothesis of (2). Hence

$$
 \sum_{0\ne z\in L}
        \exp\left(-\pi(t/s)^2\|z\|^2\right)\leq1/2.
$$

Under (1), pi(t/s)^2<=log 2, so

$$
 \sum_{0\ne z\in L}2^{-\|z\|^2}\leq1/2. \tag{3}
$$

For every distinct inclusion-minimal support F of a ternary relation,
choose one relation f_F, up to its overall sign. Its squared Euclidean
norm is |F|. A uniform independent two-coloring makes F monochromatic
with probability 2^(1-|F|), precisely the sum of the two weights in
(3) contributed by f_F and -f_F. Distinct supports give distinct pairs.
The expected number of monochromatic minimal supports is therefore at
most 1/2. Some coloring has none, and then has no monochromatic ternary
relation at all. This proves chi_1<=2. Alternation on any coordinate
(k+1)-cube is a nonzero relation in the full configuration, so chi_1>=2.

This proof needs no estimate on the minimum relation support, and no
independence between different monochromatic-support events.

## A substantial excluded parameter range

For every fixed 0<a<1/2, along even d and

$$
 k=\left\lfloor d/2-a\sqrt{d\log d}\right\rfloor,
$$

condition (1) holds for all sufficiently large d. In particular

$$
 \boxed{\chi_1(E_{d,k})=2\quad\hbox{eventually}.} \tag{4}
$$

Here is the asymptotic check. Put u=d/2-k=a sqrt(d log d)+O(1).
The central-binomial estimate and the product of successive binomial
ratios give

$$
 2^{-d}\binom d{k}
 =\sqrt{\frac2{\pi d}}
        \exp(-2u^2/d+o(1))
 =\sqrt{\frac2\pi}\,d^{-1/2-2a^2}(1+o(1)).
 \tag{5}
$$

For precision, the logarithm of that ratio product is
-2u^2/d+O(u/d+u^3/d^2), whose error tends to zero in the displayed
range. The central coefficient is asymptotic to sqrt(2/(pi d));
equivalently apply the elementary Stirling estimate to the two factorials.
The geometric bound on the lower binomial tail from the
[moment entropy page](boolean_moments.md) gives r/n=o(1). Therefore

$$
 \frac Dm=\frac{1+o(1)}{\sqrt{2\pi}}
                         d^{1/2-2a^2}. \tag{6}
$$

The logarithm of s is a positive constant times the positive power
d^(1/2-2a^2), whereas log(10(log m+2)sqrt(pi/log2))=O(log d).
This proves (1) eventually.

The earlier entropy theorem excludes uniform extraction for every fixed
a>1/2. Thus neither side with a fixed strict separation from 1/2 can
supply the counterexample: one side loses extraction, and the other
has actual two-colorings.

## Exact surviving gap

The boundary a=1/2 and narrower varying-a windows are not settled.
At the exact boundary D/n tends to 1/sqrt(2 pi), so s tends to the
finite number 2^(1/(2 sqrt(2 pi))); condition (1) fails.
The existing entropy bound gives only eventual chi_1>=6 there, because
alpha/n<=1/(2 sqrt(2 pi))+o(1)<1/5. This is a fixed lower bound, not
unbounded coloring. Uniform extraction at that boundary is proved
separately on the [boundary extraction page](moment_boundary_extraction.md).

More generally, (1) excludes every sequence satisfying its exact finite
inequality; an intermediate range between positive constants and the
displayed logarithmic threshold is not decided by these estimates.
In particular, this does not include constants times log d already large
enough to meet (1). No claim is made
that failure of (1) forces chromatic growth. The original uniformly
extracting line-cover candidate and its arbitrary-color gap remain intact.

## Review and computation scope

The semistability proof and the Gaussian-to-two-color step each received
independent internal review. The external theorem was checked in its full
primary source. No numerical experiment enters (1)--(6). These results
retire a region of the new route; they do not resolve E0774.
