---
name: research/erdos_774/routes/moment_phase_entropy
title: A finite Gaussian-width route to moment extraction
desc: A finite Gaussian-width extraction criterion, satisfied at the critical moment boundary by the weak stable-lattice Gaussian theorem.
tags: [E0774, Boolean-moments, extraction, conditional, incomplete]
sources: []
created: 2026-09-18T23:20:00Z
updated: 2026-09-18T23:28:00Z
---


# A finite Gaussian-width route to moment extraction

***

## Standing

This is a sufficient extraction criterion at the Boolean-moment boundary.
It avoids requiring a basis with simultaneously small Gram--Schmidt
coordinates and bounded energy. **The theta estimate (4) below is proved
at the rounded critical boundary by the
[stable-lattice bridge](moment_boundary_extraction.md)**, so the criterion
supplies the extraction constant there. Arbitrary-color growth remains
open; nothing here proves unbounded coloring or completes E0774.

## 1. A checked single-set extraction theorem

For a finite set A of n nonzero distinct characters of a compact abelian
group, let alpha(A) be its maximum dissociated cardinality and put

$$
 W(A)=\mathbb E\left\|\sum_{\gamma\in A}Z_\gamma\gamma\right\|_\infty,
$$

where the Z_gamma are independent complex Gaussians. There is an absolute
C such that

$$
 \alpha(A)\geq W(A)^2/(Cn). \tag{1}
$$

This is Rodriguez-Piazza's finite theorem, stated as Theorem 3.4, equation
(3.3), printed page 10 of
[Lefevre--Li--Queffelec--Rodriguez-Piazza](../../../../library/analysis/lefevre_et_al_2009_thin_sets_integers_harmonic_analysis_p_stable_random_fourier_series/_index.md)
(arXiv:0902.2625). The author checked the primary abstract, then the definitions
of the Gaussian norm on printed page 5 and of alpha and W on page 10, and the
theorem itself. Gaussian normalization only changes C. The statement is for
**one finite set**, not a conclusion inferred from a hypothesis on all subsets.

For moment configurations, flip transitivity gives eta=alpha/n, as already
proved. Thus W(E_(d,k))>=c n for one c>0 would settle hereditary extraction
along a parameter sequence. At the rounded critical boundary that width
lower bound follows from (2) and (4) below with the stable-lattice bridge.

## 2. Fixed-scale phase packing implies linear width

Let T={(gamma(t))_(gamma in A):t in G}, a subset of (S^1)^n. Suppose T
contains at least exp(a n) points separated by epsilon in the coordinate
maximum metric, for fixed a>0 and 0<epsilon<=1. Then

$$
 W(A)\geq c(a,\epsilon)n,\qquad
 \alpha(A)\geq c'(a,\epsilon)n. \tag{2}
$$

Here is the finite metric argument. Put M=ceil(8 pi/epsilon), and choose
0<beta<1/2 with h(beta)+beta log M<=a/2, where h is binary entropy using
natural logarithms. Set r=epsilon sqrt(beta)/4. In any Euclidean ball
of radius r sqrt(n), a point has at most beta n coordinates differing
from its center by at least epsilon/4. Specify those coordinates and
their labels in an M-arc partition of the circle with arc diameter at
most epsilon/4. Two packing points with the same specification are less
than epsilon apart everywhere, and so must coincide. The ball therefore
contains at most

$$
 \sum_{j\leq\beta n}\binom njM^j
 \leq\exp(n[h(\beta)+\beta\log M])\leq e^{an/2}
$$

packing points. Greedy deletion leaves Q>=exp(a n/2) points at pairwise
Euclidean distance greater than r sqrt(n).

For independent standard real Gaussians g_j,h_j, their evaluation
process X_t=sum_j(g_j Re t_j+h_j Im t_j) has increment variance
||t-s||^2. Compare it on these Q points to independent Gaussians Y_i of
variance r^2 n/2. The Gaussian comparison needed here follows directly
by differentiating the expected soft maximum
F_b(z)=b^(-1)log sum_i exp(b z_i) along
sqrt(u)X+sqrt(1-u)Y. Gaussian integration by parts makes the derivative

$$
 \frac b4\mathbb E\sum_{i,j}p_ip_j
  [\mathbb E(X_i-X_j)^2-\mathbb E(Y_i-Y_j)^2]\geq0,
$$

where the p_i are the positive soft-max weights. Let b tend to infinity.
The elementary Gaussian tail bound gives E max_(i<=Q)Y_i>=c r sqrt(n log Q).
It follows that W(A)>=c epsilon sqrt(a beta) n, up to the immaterial
complex-Gaussian normalization. Applying (1) proves (2).

## 3. A theta bound controlling the actual wrapped torus

Let V be a rational subspace of R^n, let T=exp(2 pi i V), and let
K=V perpendicular intersect Z^n. For s>0 define

$$
 \vartheta_K(s)=\sum_{z\in K}e^{-\pi s^2\|z\|^2}.
$$

For 0<epsilon<=1/2 let B_epsilon be the normalized-angle neighborhood
of the identity in T: every coordinate has distance at most epsilon
from an integer. Its Haar probability satisfies

$$
 \boxed{\mu_T(B_\epsilon)
 \leq e^{\pi n\epsilon^2/s^2}\,s^n\vartheta_K(s).} \tag{3}
$$

Indeed, the one-dimensional periodic Gaussian
g_s(t)=sum_(a in Z)exp(-pi(t-a)^2/s^2) has absolutely convergent Fourier
series s sum_(j in Z)exp(-pi s^2 j^2)exp(2 pi i jt). This follows by
integrating its Fourier coefficients and evaluating the Gaussian Fourier
transform. Integrating the product of n such series over T retains
exactly frequencies in K, giving s^n vartheta_K(s). On B_epsilon each
factor is at least exp(-pi epsilon^2/s^2), proving (3).

Consequently, the following fixed-parameter estimate would suffice:
there exist s>0 and b>0, independent of d, such that

$$
 \boxed{\log s+\frac1n\log\vartheta_K(s)\leq-b.} \tag{4}
$$

Choose fixed epsilon>0 small enough that pi epsilon^2/s^2<=b/2.
Then (3) is at most exp(-bn/2). A maximal epsilon-separated set in the
normalized-angle metric covers T by its translated B_epsilon balls,
and so has at least exp(bn/2) points. On this range angular separation
epsilon gives a fixed positive chordal separation. Equation (2) applies.

For moments, K is exactly the integer relation lattice already proved
semistable. The reverse-Minkowski theorem alone controls it at a parameter
depending on log n and the normalized determinant; it does **not** give (4) with
fixed s,b at the critical boundary. The
[weak stable-lattice free-energy theorem](../lemmas/stable_lattice_free_energy.md)
does, and the [boundary extraction page](moment_boundary_extraction.md) applies
it. The [compression identities](../lemmas/moment_lattice_stability.md) by
themselves do not bound the theta function of the already compressed degree
ball.

## 4. Why phase-period covolume cannot replace (3)

The covolume of V intersect Z^n alone is insufficient. For
A_N={N+1,...,N+n}, that covolume is
sqrt(sum_(j=1)^n(N+j)^2), since these consecutive integers are primitive.
It can be arbitrarily large while n is fixed. Nevertheless any dissociated
m-subset satisfies

$$
 2^m\leq(m+1)(mn+1).
$$

For each subset cardinality j, subtract jN from its sum; at most mn+1
values remain, and there are m+1 cardinalities. Thus alpha(A_N)=O(log n)
uniformly in N. Multiplication by exp(2 pi i Nt) also shows that the
Gaussian sup norm is independent of N. These phase curves all lie on
the two-parameter surface (exp(2 pi i(a+jb)))_j, whose fixed-scale
coordinate covering number is O(n epsilon^(-2)).

For n>=3 this example does not refute a stronger use of semistability: its
kernel contains {z:sum z_j=sum jz_j=0}, of rank n-2 and covolume n
sqrt((n^2-1)/12), independent of N. The whole kernel's normalized covolume grows
with N, so it is not semistable for sufficiently large N. The remaining bridge
is therefore a genuine estimate such as (4), not another unqualified
volume-to-packing inference.

All new finite arguments here were checked internally. No computation,
external review, boundary extraction theorem, or counterexample is claimed.
