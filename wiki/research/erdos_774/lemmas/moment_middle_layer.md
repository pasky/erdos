---
name: research/erdos_774/lemmas/moment_middle_layer
title: Exact moment-kernel determinant on the middle Hamming layer
desc: The exact middle-layer determinant grows at the critical boundary; hereditary extraction follows from the full moment-family theorem, not from slice stability.
tags: [E0774, Boolean-moments, lattice, proved, incomplete]
sources: []
created: 2026-09-19T00:30:00Z
updated: 2026-10-14T00:26:52Z
---


# Exact moment-kernel determinant on the middle Hamming layer

***

Uniform extraction for subsets of this slice
follows from [hereditary extraction in the whole critical moment
family](../routes/moment_boundary_extraction.md). The determinant
calculation below remains valid and does not itself supply slice
semistability or any coloring conclusion.

This tests a specific hereditary-extraction attack on the moment boundary.
If the middle layer had dissociated density tending to zero, transitivity
would rule out uniform extraction for the whole cube. The determinant
calculation below does **not** establish that assertion. Its normalized
logarithmic determinant grows, rather than vanishes. No extraction or
coloring theorem is inferred from the determinant alone.

## 1. Finite determinant formula

Let 0<=k<=min(w,d-w), N=binom(d,w), R=binom(d,k), and
a_i=binom(d,i)-binom(d,i-1), taking binom(d,-1)=0. Let K_sl be the
integer relation lattice of degree-at-most-k moments restricted to
the points of weight w. Then

$$
 \boxed{\det(K_{\rm sl})^2=
 \prod_{i=0}^{k}
 \left[\frac{\binom{d-k-i}{w-k}}
             {\binom{w-i}{k-i}}\right]^{a_i}.}
 \tag{1}
$$

Here the determinant of the rank-zero lattice is one. Let M be the
k-subset versus w-subset inclusion matrix. Every degree-j row, j<k,
is a rational combination of its rows, since the sum of the rows indexed
by k-subsets containing a fixed j-subset is binom(w-j,k-j) times that
degree-j row. Thus K_sl=ker_Z M.

The only imported integer-matrix fact is the unimodular diagonal form in
[Ghorbani et al., Corollary 3 and its proof](../../../../library/set_systems/ghorbani_et_al_2007_inclusion_matrices_chains/_index.md)
(arXiv:0709.3144v1). For this substitution of parameters, it gives image index

$$
 [\mathbb Z^R:M\mathbb Z^N]
 =\prod_{i=0}^k\binom{w-i}{k-i}^{a_i}.
 \tag{2}
$$

The author and two separate reviewers checked the primary abstract, the
theorem's range k<=w<=d-k, and its unimodular proof. A diagonal form suffices
for the index; no assertion that these entries are ordered Smith factors is
needed.

## 2. Elementary Gram spectrum

Let V_j be Euclidean space with orthonormal coordinates indexed by
j-subsets. The up map U sends a subset basis vector to the sum of its
(j+1)-element supersets, and D=U* is the down map. Direct entry counting
gives, on V_j,

$$
 DU-UD=(d-2j)I.
 \tag{3}
$$

In particular U is injective below the middle level, since
||Uf||^2=||Df||^2+(d-2j)||f||^2. Put H_i=ker(D|V_i), of dimension a_i.
Successive orthogonal decompositions V_j=UV_(j-1) plus H_j yield
V_k=directsum_(i<=k) U^(k-i)H_i. For h in H_i, induction from (3) gives

$$
 D U^a h=a(d-2i-a+1)U^{a-1}h,
 \qquad
 \|U^a h\|^2=
 \frac{a!(d-2i)!}{(d-2i-a)!}\|h\|^2.
 \tag{4}
$$

Since M^T=U^(w-k)/(w-k)!, the eigenvalues of MM^T are

$$
 \lambda_i=\binom{w-i}{k-i}\binom{d-k-i}{w-k},
 \quad\hbox{with multiplicity }a_i.
 \tag{5}
$$

For any full-row-rank integer M, the primitive-kernel volume identity is
det(ker_Z M)=sqrt(det(MM^T))/[Z^R:MZ^N]. It follows by decomposing
Euclidean volume along the kernel and the image, just as in the
[integer-graph calculation](moment_integer_graph.md). Substituting
(2) and (5) proves (1).

## 3. Critical middle-layer asymptotic

Now take even d, w=d/2, and
k=floor(d/2-(1/2)sqrt(d ln d)). Put u=w-k. Reindex i=k-j in (1).
The factor becomes

$$
 Q_u(j)=\frac{(2u+j)!\,j!}{(u+j)!^2}.
 \tag{6}
$$

Give j probability a_(k-j)/R. Its tail telescopes and satisfies

$$
 \Pr(J\ge L)=\frac{\binom d{k-L}}{\binom dk}
 \leq\left(\frac{k}{d-k+1}\right)^L.
 \tag{7}
$$

Taking L=floor(sqrt d) makes this bound tend to zero exponentially in
sqrt(ln d), while L=o(u). The factors Q_u(j) decrease with j and
Q_u(0)=binom(2u,u). For j<=L<=u,

$$
 \frac{Q_u(j)}{Q_u(0)}
 =\prod_{a=1}^j\frac{a(2u+a)}{(u+a)^2}
 \geq\frac{j!}{(2u)^j}.
$$

Thus log_2 Q_u(j)=2u-o(u) uniformly on this range: the error is at most
O(log u)+j log_2(2eu/j)=o(u). Everywhere 0<=log_2 Q_u(j)<=2u.
Equation (7) now shows that its weighted mean is (2+o(1))u. Therefore

$$
 \log_2\det K_{\rm sl}\sim u\binom dk.
 \tag{8}
$$

The exact ratio to the central binomial coefficient has logarithm
-2u^2/d+O(u^3/d^2). For the displayed rounded choice,
2u^2/d=(1/2)ln d+o(1), hence R/N~d^(-1/2). It follows that

$$
 \boxed{\frac1N\log_2\det K_{\rm sl}
       \sim\frac12\sqrt{\ln d}\longrightarrow\infty.}
 \tag{9}
$$

The precise equivalent in (9) uses u=(1/2)sqrt(d ln d)+O(1), not merely
u~(1/2)sqrt(d ln d). The weaker latter statement allows changes in the
binomial ratio too large to retain that constant.

## 4. Scope

The rank N-R is asymptotic to N, so (9) is also the logarithm of the
normalized covolume to leading order. This excludes a vanishing-determinant
argument on this slice. It supplies no short-basis estimate and no
constant-scale theta upper bound. Global semistability gives only the
old constant lower slope on slice sublattices; it does not establish
semistability at the slice's larger normalized covolume.

Even if that stronger slice semistability were supplied, the normalized covolume
2^((1/2+o(1))sqrt(ln d)) is still below the order-d threshold of the checked
reverse-Minkowski two-color criterion. Thus (9) is not being used as a coloring
theorem. The algebra and the asymptotic are author-recorded; a separate reviewer
checked them, including the rounding scope. No numerical
experiment or external review is claimed.
