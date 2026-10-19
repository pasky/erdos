---
name: research/erdos_774/lemmas/moment_integer_graph
title: Integer graph and hard-kernel reductions for moment theta mass
desc: The exact graph-kernel and puncturing reductions remain valid; a separate weak stable-lattice theorem supplies the critical fixed-scale cancellation needed for extraction.
tags: [E0774, Boolean-moments, lattice, proved, incomplete]
sources: []
created: 2026-09-18T23:43:00Z
updated: 2026-09-19T00:48:35Z
---


# Integer graph and hard-kernel reductions for moment theta mass

***

The fixed-scale extraction/cancellation target
below is obtained from [full semistability and the weak Gaussian
bound](../routes/moment_boundary_extraction.md). The graph and puncturing
identities and their countermodel retain their exact scopes. The
[growing-modulus reduction](moment_modular_depth.md) is an additional
equivalent formulation, not an unresolved extraction prerequisite.

This page proves an exact version of the low-rank reduction. It does
**not** itself prove the constant-scale theta estimate required by the
[finite extraction criterion](../routes/moment_phase_entropy.md); that
estimate comes from the stable-lattice bridge.

## 1. The explicit integer graph

Let 0<=k<d, n=2^d, r=sum_(j<=k)binom(d,j), m=n-r. Identify cube points
with subsets of [d]. Let P={B:|B|<=k} and S={T:|T|>k}.
The moment matrix A has entries A_(R,T)=1_(R subset T), |R|<=k.
Its square submatrix U on P is the Boolean zeta matrix, with determinant
one in cardinality order and inverse

$$
 (U^{-1})_{B,R}=(-1)^{|R|-|B|}1_{B\subseteq R}.
$$

Put C=-U^{-1}A_S, an integer r-by-m matrix. The relation lattice K,
in coordinate order (S,P), is exactly

$$
 K=\{(z,Cz):z\in\mathbb Z^m\}.
 \tag{1}
$$

Truncated binomial inversion gives its explicit entries:

$$
 C_{B,T}=
 \begin{cases}
 (-1)^{k-|B|+1}\binom{|T|-|B|-1}{k-|B|},&B\subseteq T,\\
 0,&B\not\subseteq T.
 \end{cases}
 \tag{2}
$$

Indeed, the relevant sum in -U^{-1}A_S is
-sum_(j=0)^(k-|B|)(-1)^j binom(|T|-|B|,j), giving (2).

The graph basis has Gram matrix Q=I_m+C^T C. The projected coordinate
basis {P_W e_T:T in S} of Lambda=P_W Z^n is dual to it: its pairing
with (e_U,C_U) is delta_(T,U). Therefore its Gram matrix is exactly

$$
 G=Q^{-1}=I_m-C^T(I_r+CC^T)^{-1}C.
 \tag{3}
$$

Thus the low-rank contraction is an identity, not a heuristic model.
For theta_L(s)=sum_(z in L)exp(-pi s^2||z||^2), (1) also gives

$$
 \vartheta_K(s)=\vartheta_{\mathbb Z}(s)^m
       \mathbb E e^{-\pi s^2\|CZ\|^2},
 \tag{4}
$$

where the coordinates of Z are independent with probabilities
P(Z_i=j)=exp(-pi s^2 j^2)/theta_Z(s).
The missing extraction estimate is a genuinely exponential suppression
in (4); dropping the expectation gives no such conclusion.

## 2. Remove the graph penalty without changing limiting free energy

Let H=ker_Z C, viewed in R^m. For every fixed s>0,

$$
 \boxed{\vartheta_H(s)\leq\vartheta_K(s)
       \leq\vartheta_{\mathbb Z}(s)^r\vartheta_H(s).}
 \tag{5}
$$

The lower bound uses (z,0) for z in H. For the upper bound, group (1)
by y=Cz. Any nonempty fiber is z_y+H. Decompose z_y into its orthogonal
components parallel and perpendicular to span H. The perpendicular
component only decreases Gaussian mass. The Gaussian mass of a translate
of H within its span is at most theta_H(s): the Fourier expansion of its
periodization has nonnegative Gaussian coefficients, each multiplied by
a unit phase under translation, so the real sum is largest at zero.
Consequently each fiber has mass at most theta_H(s). Summing the
remaining factor exp(-pi s^2||y||^2) over y in im C, and then over all
Z^r, proves (5). This argument also covers the zero-rank kernel.

In particular, whenever r=o(n),

$$
 0\leq\frac1n\log\vartheta_K(s)
       -\frac1n\log\vartheta_H(s)
 \leq\frac rn\log\vartheta_{\mathbb Z}(s)=o(1).
 \tag{6}
$$

The sufficient strict fixed-scale extraction inequality transfers between
K and H with an arbitrarily small loss in its positive constant. This
reduces the analytic target; it does not establish it.

## 3. Surjectivity and determinant retention

Assume 2k<d. The high-weight set P'={T:|T|>=d-k} has r points and is
disjoint from P. Complementing all variables acts on the degree-at-most-k
monomials by an integral triangular matrix with diagonal entries plus or
minus one, and maps P to P'. Hence A_(P') is unimodular, as is the
corresponding square submatrix -U^{-1}A_(P') of C. In particular C maps
Z^m onto Z^r, and rank H=m-r=n-2r.

The primitive-kernel determinant formula gives

$$
 \det H=\sqrt{\det(CC^T)},\qquad
 \det K=\sqrt{\det(I_r+CC^T)}.
 \tag{7}
$$

For completeness, extend an integer basis of H by integer lifts of the
standard basis of Z^r under C. They form a unimodular basis of Z^m.
Projecting its last r vectors orthogonally off span H gives a volume of
1/det H. The map C on this perpendicular space has volume factor
sqrt(det(CC^T)) and sends those projected vectors to the standard basis.
This proves the first identity; the second follows from the graph Gram
matrix and det(I+C^TC)=det(I+CC^T).

Put D=(d-k)binom(d,k) and s_0=2^(D/(2m)), so det K=s_0^m.
The previously proved [full semistability](moment_lattice_stability.md)
applies to H embedded as (H,0) in K, and (7) gives the upper bound:

$$
 s_0^{m-r}\leq\det H\leq s_0^m.
 \tag{8}
$$

Equivalently,

$$
 0\leq\log\det K-\log\det H\leq r\log s_0,
 \qquad
 \det(I_r+(CC^T)^{-1})\leq s_0^{2r}.
 \tag{9}
$$

At the critical boundary r=o(n) and s_0 converges to a constant greater
than one. Thus K and the hard kernel H have the same limiting normalized
logarithmic determinant as well as the same fixed-scale theta free energy.
The operation preserves the exponential determinant scale. It leaves an
analytic theta estimate to be supplied separately, rather than reducing it
to rank alone.

## 4. General coordinate-puncturing theorem

The preservation phenomenon is not specific to a unimodular pivot choice.
Let L<=Z^N be any lattice of rank M, let J be a coordinate set, and put
L_0={x in L:x_J=0} and q=rank(proj_J L). Then

$$
 \vartheta_{L_0}(s)\leq\vartheta_L(s)
 \leq\vartheta_{\mathbb Z}(s)^q\vartheta_{L_0}(s),
 \qquad \det L_0\leq\det L.
 \tag{10}
$$

For theta, the same Gaussian fiber proof first gives a factor
theta_(proj_J L)(s). Choose q coordinate positions giving an injective
projection on span(proj_J L). Projecting onto them decreases norms and
maps lattice points injectively into Z^q, proving the displayed factor.

For determinants, L_0 is primitive in L. Its orthogonal quotient has
covolume det L/det L_0 and maps injectively and contractively under proj_J
onto the integral lattice proj_J L. The latter has covolume at least one,
because its squared covolume is a positive integer Gram determinant.
Thus det L/det L_0>=1, as required.

If L is semistable and det L=s_0^M, its nonzero-rank sublattice L_0 also
satisfies det L_0>=s_0^(M-q); the same inequality holds with determinant
one at rank zero. In particular, for q=o(N), M=N-o(N), and bounded
log s_0, any such puncturing preserves normalized log-theta and logdet
up to o(1). It subsumes any number of successive puncturings whose
total rank loss is o(N).

This also identifies a limitation precisely. When s_0 tends to a fixed
constant, the normalized covolume of the surviving lattice lies between
s_0 and s_0^(M/(M-q)), hence still tends to that same constant. Puncturing
alone cannot raise it to the growing determinant scale of the existing
reverse-Minkowski coloring test. Any useful further argument must exploit
additional structure of the surviving lattice.

No finite computation or external theorem is needed for (1)--(10).
The graph formulas, affine-class theorem and puncturing argument are
author-recorded; separate reviewers checked the first two. No external
review is claimed.

## 5. Why full sublattice stability still matters

There is an explicit countermodel to dropping that hypothesis from the
remaining analytic problem. Fix 0<c<log(sqrt 2), let m>=3 and
M_m=max(1,floor(exp(cm)/sqrt m)), and take the one-row integer matrix
C_m=(1,M_m,...,M_m). Its graph lattice has normalized determinant tending
to exp(c)>1, and C_m is surjective. The Gram contraction has rank one
and largest diagonal contraction at most 1/(m-1) for all sufficiently
large m. Nevertheless, for every fixed s>0,

$$
 \frac1m\log\vartheta_{\operatorname{graph}C_m}(s)
 \longrightarrow\log\vartheta_{\mathbb Z}(s).
 \tag{11}
$$

The upper bound drops the graph penalty. For the lower bound use its
hard-kernel vectors with first coordinate zero and the other m-1
coordinates summing to zero. Their Gaussian mass is
theta_Z(s)^(m-1) times P(Z_1+...+Z_(m-1)=0), for the fixed-scale integer
Gaussians in (4). This probability is at least c_s/sqrt m. For an even
number of terms, split into equal halves and apply Cauchy--Schwarz to
the convolution at zero, restricting the half-sum to an interval of
length O_s(sqrt m) whose probability is at least 3/4 by Chebyshev.
For an odd number, additionally prescribe one Gaussian to be zero.
The polynomial loss proves (11).

Thus the extraction target's limiting left side would be
log(s theta_Z(s))=log theta_Z(1/s)>0, by one-dimensional Gaussian
Poisson summation. Low rank, surjectivity, and small individual diagonal
contractions do not establish the needed negative value.

This is **not** a counterexample to a full-semistability bridge. The same hard
kernel contains a rank-(m-2) root lattice of determinant sqrt(m-1), whose
normalized covolume tends to one. It violates full semistability while the
graph's shortest nonzero vector has length sqrt 2>exp(c). In particular,
checking only short single vectors would also miss the obstruction. The actual
moment lattice does have full semistability; the
[stable-lattice bridge](../routes/moment_boundary_extraction.md) is how it
enters the fixed-scale bound.
