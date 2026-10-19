---
name: research/erdos_774/routes/moment_phase_lattice
title: A projected-lattice criterion for Boolean moment extraction
desc: The exact phase-basis criterion remains valid; its basis premise is still open, but a separate weak stable-lattice theta argument proves critical moment extraction.
tags: [E0774, Boolean-moments, lattice, proved, conditional, incomplete]
sources: []
created: 2026-09-18T22:52:00Z
updated: 2026-09-18T23:28:00Z
---


# A projected-lattice criterion for Boolean moment extraction

***

## Standing

The lattice descriptions and rounding criterion below are proved. **The
required bounded-energy basis has not been constructed.** Extraction at
the critical moment boundary is nevertheless proved by the separate
[weak stable-lattice theta argument](moment_boundary_extraction.md), which
does not use this basis; arbitrary-color growth still requires a separate
proof. No counterexample is asserted.

The [semistability theorem](../lemmas/moment_lattice_stability.md)
verifies every sublattice normalized-covolume inequality, but does not
construct the basis required here. Its
[Gaussian consequence](moment_gaussian_coloring.md) gives actual
two-colorings away from the critical boundary and narrows the candidate
range.

## 1. The exact phase lattice

Write X={0,1}^d, n=2^d, and let V_k be the real span of the Walsh functions
chi_S(x)=product_(i in S)(1-2x_i), |S|<=k. Put

$$
 W=V_k^\perp,\quad r=\sum_{s=0}^k\binom ds,\quad m=n-r,
 \quad L=W\cap\mathbb Z^X,\quad \Lambda=P_W\mathbb Z^X.
 \tag{1}
$$

The moment-character torus is exactly exp(2 pi i V_k). The space is
rational, so Lambda is a full lattice in W; for example the rational
projection matrix has a common denominator. With duality inside W,

$$
 \Lambda^*=L. \tag{2}
$$

Indeed, for y in W, the numbers <y,P_W e_x>=y_x are all integers exactly
when y belongs to L.

Put ell=d-k-1 and epsilon=chi_[d]. Multiplication by epsilon sends W
isometrically to V_ell. Every integer-valued function in V_ell has integer
monomial coefficients: its coefficient at A is the integer Mobius sum
sum_(B subset A)(-1)^(|A|-|B|) f(1_B). Thus

$$
 b_A(x)=\epsilon(x)\prod_{i\in A}x_i,
 \qquad |A|\leq\ell,
 \tag{3}
$$

is a Z-basis of L. In increasing cardinality order its orthogonal
Gram--Schmidt residuals are

$$
 u_A=(-1)^{|A|}2^{-|A|}\chi_{[d]\setminus A},
 \qquad \|u_A\|^2=2^{d-2|A|}.
 \tag{4}
$$

To check (4), expand b_A in Walsh functions. All terms except the displayed
one are indexed by proper subsets of A in (3), hence already lie in the
preceding span. The surviving Walsh vectors are mutually orthogonal.
Telescoping binomial coefficients gives

$$
 \sum_{s=0}^j(d-2s)\binom ds=(d-j)\binom dj.
$$

Using j=ell and duality therefore gives the exact covolume

$$
 \det\Lambda=2^{-D/2},\qquad
 D=(d-k)\binom dk. \tag{5}
$$

The reversed dual basis of (3) is a rational basis of Lambda. Its
Gram--Schmidt residuals, up to signs and reversed order, are

$$
 \widetilde u_A=2^{|A|-d}\chi_{[d]\setminus A},\qquad
 T_{\rm mon}:=\sum_A\|\widetilde u_A\|^2
       =2^{-d}\sum_{s=0}^{\ell}\binom ds4^s.
 \tag{6}
$$

For any basis, reversing the dual basis reciprocates the Gram--Schmidt
lengths: in an orthogonal Gram--Schmidt coordinate system, the basis change
is triangular; the dual change is its inverse transpose. This also checks
the scaling in (6).

## 2. Why covolume alone does not prove the original rounding proposal

For an arbitrary lattice basis with Gram--Schmidt residuals u_1,...,u_m,
write T=sum_i ||u_i||^2. Adjacent stochastic rounding, followed by a uniform
cube flip of the basis, gives the familiar coordinate second-moment
certificate T/(4n). The quadratic phase estimate would consequently give

$$
 \rho(E_{d,k})\geq1-\frac{\pi^2T}{2n}. \tag{7}
$$

Here rho is the positive-real Sidon parameter defined on the
[tensor extraction page](tensor_extraction.md). On the other hand,
the product of the squared Gram--Schmidt lengths is 2^(-D). Arithmetic--
geometric mean gives, for **every** basis,

$$
 \frac Tn\geq\frac mn\,2^{-D/m}. \tag{8}
$$

Thus (7) cannot be positive whenever the right side of (8) is at least
2/pi^2. This is a limitation of that worst-case second-moment certificate,
**not** a lower bound on actual rounding errors, the covering radius, or
the Sidon parameter. Section 3 gives a different, positive certificate.

## 3. Root rounding gives a stronger positive criterion

**Theorem.** Suppose a rational basis of Lambda has Gram--Schmidt residuals
u_i satisfying

$$
 |u_i(x)|\leq\tfrac14\quad\hbox{for all }i,x.
 \tag{9}
$$

Then

$$
 \boxed{\rho(E_{d,k})\geq
       \exp\left(-2\pi^2 T/n\right).} \tag{10}
$$

In particular, a sequence of such bases with T<=C n for one C would give one
positive Sidon bound and hence uniform full-dissociation extraction. The
application of
[Pisier's Theorem 2](../../../../library/analysis/pisier_1983_arithmetic_characterizations_sidon_sets/_index.md)
required for that last implication is the one already checked on the
[moment route's parent construction](tensor_extraction.md); no extraction
conclusion is being drawn without the uniform basis premise.

### A finite root distribution

Let D and R be positive integers with D>=4R. Put J=D-R-1,
alpha_j=sin((j+1)pi/(J+2)), 0<=j<=J, and Q=sum alpha_j^2.
For any prescribed z on the unit circle, assign each D-th root y of z
probability

$$
 \frac{1}{DQ}\left|\sum_{j=0}^{J}\alpha_j y^j\right|^2.
$$

These probabilities sum to one. For |a|<=R their moments are the
target-independent positive real numbers

$$
 c_{|a|}=\mathbb E Y^a
  =\frac{\sum_{j=0}^{J-|a|}\alpha_j\alpha_{j+|a|}}Q
  \geq\exp(-2\pi^2a^2/D^2).
 \tag{11}
$$

The sums over D-th roots have no nonzero exponent divisible by D:
J+R=D-1. This proves normalization and the moment identity, also for
negative a by conjugation. To verify the estimate, extend alpha by zero
and let S be the bilateral shift. The sine eigenvector identity gives
c_1=cos(pi/(D-R+1)). Therefore

$$
 1-c_a=\frac{\|(S^a-I)\alpha\|_2^2}{2Q}
 \leq a^2(1-c_1)
 \leq\frac{\pi^2a^2}{2(D-R+1)^2}=:v.
$$

Since D>=4R and |a|<=R, v<5/9 and D-R+1>=3D/4. Thus
-log c_a<=v/(1-v)<=(9/4)v<=2 pi^2 a^2/D^2.
This proves (11). It is the same elementary finite distribution used in
[covered extraction](incidence_cover_extraction.md), now applied to
orthogonal lattice residuals.

### Backward basis rounding

For each i choose an integer denominator D_i such that
u_i(x)=a_(i,x)/D_i for integers a_(i,x), and put
R_i=max_x |a_(i,x)|. Nonzero u_i implies R_i>=1; (9) gives D_i>=4R_i.

Start from an arbitrary w in W, and process the basis vectors b_i in
decreasing order. If the current residual's coefficient along u_i is
alpha_i, select an integer j_i from 0,...,D_i-1 by applying (11) to

$$
 Y_i=\exp(2\pi i(\alpha_i-j_i)/D_i),\qquad
 Y_i^{D_i}=\exp(2\pi i\alpha_i).
$$

Subtract j_i b_i. At the end z=sum_i j_i b_i belongs to Lambda and

$$
 e=w-z=\sum_i\eta_i u_i,\qquad \eta_i=\alpha_i-j_i.
$$

Conditional on the previously chosen larger-index coefficients,

$$
 \mathbb E\exp(2\pi i\eta_i u_i(x))
       =c^{(i)}_{|a_{i,x}|}.
$$

The right side is independent of every earlier random choice. Integrate
first over the last choice (index 1), then over index 2, and so on. This
is an exact conditional-expectation calculation, not an independence
assertion about the eta_i. It gives

$$
 \mathbb E e^{2\pi i e_x}
  =\prod_i c^{(i)}_{|a_{i,x}|}
  \geq\exp\left(-2\pi^2\sum_i u_i(x)^2\right)>0.
 \tag{12}
$$

All choices have finite support. No unbiasedness or small real error is
needed: the assertion is about the exact character expectation.

### Symmetry and phase interpolation

Coordinate flips of the binary cube preserve V_k, W, and Lambda and act
transitively on X. Randomize the basis by one uniform such flip before
rounding, keeping w fixed. The bound (12) holds for every target w and
every flipped basis. Jensen's inequality gives for every x

$$
 \mathbb E e^{2\pi i e_x}
 \geq\exp(-2\pi^2 T/n),
$$

with the expectation real. To apply this to arbitrary complex coefficients
c_x, choose real theta_x with c_x exp(2 pi i theta_x)=|c_x|, arbitrarily
when c_x=0, and set w=P_W theta. If z=P_W a for a in Z^X, then

$$
 \theta-e=\theta-P_W\theta+P_Wa
          =P_{V_k}(\theta-a)+a.
$$

Hence exp(2 pi i(theta-e)) lies in the allowed moment-character torus.
Its expected polynomial has real part at least
exp(-2 pi^2 T/n) sum_x |c_x|, by the positive real character expectation
and conjugation. Some outcome attains this expectation. This proves (10).

## 4. The still missing basis estimate

For k>=1 the explicit residuals (6) do satisfy (9), since their largest
coordinate is 2^(-k-1). The theorem consequently gives the unconditional
finite bound

$$
 \rho(E_{d,k})\geq
 \exp\left(-\frac{2\pi^2}{4^d}
              \sum_{s=0}^{d-k-1}\binom ds4^s\right).
 \tag{13}
$$

This bound does **not** stay positive uniformly in the proposed window
k=floor(d/2-(1/2)sqrt(d ln d)): its displayed exponent grows in magnitude.
The determinant (5) neither constructs a better basis nor rules one out
for (10). The exact sufficient target of this route is a rational basis
with (9) and T=O(n), or another target-independent phase procedure with
the same uniform consequence. Its existence remains unproved; extraction
at the boundary is proved by the separate
[stable-lattice bridge](moment_boundary_extraction.md).

The arbitrary-color obligation is entirely separate and remains open.
No numerical search or theorem-prover computation is used on this page.

### Coordinate generators cannot be repaired just by reordering

Let R_0 consist of the cube points of weight at most k. The monomial
evaluation matrix on R_0 is unimodular, so those integer monomials together
with e_x, x outside R_0, form a basis of Z^X. Projecting to W gives
a lattice basis {P_W e_x:x outside R_0}, each vector of norm at most one.
Its Gram--Schmidt energy satisfies T<=m. Thus bounded energy alone is easy.

For any ordering of any coordinate-projection basis, the residual is
u_i=P_(V_k+span{e_(x_j):j<i})^perpendicular e_(x_i). Orthogonal projection
therefore gives u_i(x_i)=||u_i||^2. If every residual coordinate had
magnitude at most 1/4, then

$$
 2^{-D}=\det(\Lambda)^2=\prod_i\|u_i\|^2\leq4^{-m},
$$

which requires D/m>=2. At the exact critical boundary D/m tends to
1/sqrt(2 pi)<2. No reordering of these coordinate generators can satisfy
the cap there. This does not exclude mixed integer generators or a
different rounding procedure.

### Alternative finite extraction criterion

The [phase-entropy route](moment_phase_entropy.md) gives a second exact
sufficient condition, using a checked single-set Gaussian-width extraction
theorem. It needs a constant-parameter theta bound controlling the actual
wrapped torus, not merely its period covolume; that bound is supplied at
the boundary by the [stable-lattice bridge](moment_boundary_extraction.md).
These are alternative extraction targets; neither supplies arbitrary-color
growth.
