---
name: research/erdos_774/routes/boolean_moments
title: The Boolean moment route
desc: Critical Boolean moments have uniform hereditary full-dissociation extraction; entropy and restricted-color results do not yet prove unbounded actual coloring.
tags: [E0774, new-route, proved, incomplete]
sources: []
created: 2026-09-18T22:38:00Z
updated: 2026-09-18T23:28:00Z
---


# The Boolean moment route

***

## Standing

[Uniform full-dissociation extraction at the rounded critical
boundary](moment_boundary_extraction.md) is proved. The entropy exclusions
and non-affine circuits below are unchanged. Only the arbitrary-color
obligation remains for that critical family.

The [projected-lattice page](moment_phase_lattice.md) proves an exact phase
rounding criterion: bounded normalized Gram--Schmidt energy together with
coordinate magnitudes at most 1/4 would give uniform extraction. Its
required basis is unproved. This replaces the previous unchecked lattice
suggestion by a precise sufficient target, not by an extraction theorem.
Separately, [semistability](../lemmas/moment_lattice_stability.md) and
[Gaussian counting](moment_gaussian_coloring.md) prove actual
two-colorability for every fixed 0<a<1/2 in the square-root-logarithmic
scale below. The exact a=1/2 boundary retains the coloring obligation, and
the larger-degree regime proved two-colorable cannot supply the required
unbounded coloring.

This family is not an incidence cover, a root-of-unity grid, or a
difference tower. Its integer columns record low-order joint moments of
binary points. The arguments below prove several exact structural facts
and identify a parameter window. **Uniform proportional dissociation is
proved at the rounded boundary; unbounded dissociated coloring is not. This
is not a counterexample.**

## 1. The configuration and its signed relations

For 1<=k<d, let

$$
 v_{d,k}(x)=\left(\prod_{i\in S}x_i\right)_{S\subseteq[d],\ |S|\leq k},
 \qquad x\in\{0,1\}^d,
 \qquad E_{d,k}=\{v_{d,k}(x):x\in\{0,1\}^d\}.
 \tag{1}
$$

The empty monomial is one. Thus all columns are nonzero and there are no
antipodal pairs. Degree-one rows distinguish the 2^d columns. Write

$$
 n=2^d,\qquad r=\sum_{s=0}^k\binom ds.
$$

The r columns indexed by points with at most k ones form a square inclusion
matrix: its entry at (S,T) is 1_{S subset T}. Ordering by cardinality gives
a triangular matrix with diagonal one. Consequently rank_Q(E_{d,k})=r.

A ternary relation is a pair of disjoint sets of binary points having the
same cardinality and the same joint moments through degree k. Call this a
*flat moment trade*. Unlike fixed-order h-freeness, every possible support
size is forbidden in the dissociation condition.

One may equivalently use Walsh rows

$$
 \chi_S(x)=\prod_{i\in S}(1-2x_i),\qquad |S|\leq k.
 \tag{2}
$$

Expanding (2) is an invertible triangular rational change of rows, so it
preserves every integer relation among columns. It is not generally a
unimodular change; the powers of two in it are central to Section 3.

## 2. Hereditary extraction is exactly a maximum-size question

Let alpha(d,k) be the largest size of a dissociated subset of E_{d,k}, and
let eta(d,k) be its hereditary full-dissociation extraction constant. Then

$$
 \boxed{\eta(d,k)=\alpha(d,k)/2^d.}
 \tag{3}
$$

Indeed, a coordinate flip x_i -> 1-x_i induces an invertible integer change
of the moment rows; it preserves degree and is its own inverse. The group
of all flips acts transitively on the columns and preserves dissociation.
Fix a maximum dissociated subset D. For any F subset E, the expected size
of F intersect a uniform translate of D is |F||D|/2^d. Every such intersection
is dissociated. Some translate gives the lower bound in (3), and the full
set F=E gives the reverse inequality.

Thus a single positive-density dissociated subset at each chosen parameter
pair would suffice for the entire hereditary extraction requirement. This
is a concrete advantage of the new family, not a construction of that subset.

## 3. An entropy bound that uses the integral congruences

**Theorem.** If D is dissociated and |D|=m, then

$$
 m\leq\frac12\sum_{s=0}^k\binom ds
       \log_2\left(2\pi e\left[\frac{m}{4^{s+1}}+
                                      \frac1{12}\right]\right).
 \tag{4}
$$

**Proof.** Independently select every x in D with Bernoulli probability one
half, writing its indicator as xi_x. For |S|<=k put

$$
 Y_S=\sum_{x\in D}\xi_x\chi_S(x),\qquad
 Z_S=\sum_{x\in D}\xi_x\prod_{i\in S}x_i.
$$

Dissociation makes the subset-sum map injective, so the joint entropy of
all Y_S is m bits. Order the rows by increasing degree. The identity

$$
 Y_S=\sum_{T\subseteq S}(-2)^{|T|}Z_T
$$

shows that, conditional on earlier rows, Y_S lies in one fixed residue
class modulo 2^{|S|}. The smaller Z_T are already determined by the earlier
Walsh rows. Therefore its conditional entropy is that of an integer random
variable with conditional variance Var(Y_S | earlier)/4^{|S|}.

For any integer variable W, adding an independent uniform variable on
[-1/2,1/2] gives differential entropy H(W) and variance Var(W)+1/12.
The Gaussian maximizes entropy at fixed variance (by nonnegativity of
relative entropy), giving

$$
 H(W)\leq\tfrac12\log_2(2\pi e[\operatorname{Var}(W)+1/12]).
$$

Apply this conditionally, average, and use concavity of logarithm and the
law of total variance. Since Var(Y_S)=m/4, the contribution of row S is
at most one half log_2(2 pi e[m/4^{|S|+1}+1/12]). Sum the chain rule for
entropy. This proves (4). QED.

### 3.1 A simple exact corollary

For k<=d/2 put c_0=(1/2)log_2(2 pi e/3). Since m<=2^d,

$$
 \boxed{\alpha(d,k)\leq
       \frac{d-k}{2}\binom dk+c_0\sum_{s=0}^k\binom ds.}
 \tag{5}
$$

For each s<=k, the bracket in (4) is at most 2^{d-2s}/3. Thus the row's
contribution is at most (d/2-s)+c_0. The identity

$$
 \sum_{s=0}^k(d-2s)\binom ds=(d-k)\binom dk
$$

follows by telescoping
(d-2s)binom(d,s)=d[binom(d-1,s)-binom(d-1,s-1)]. It proves (5).

Ignoring the congruences in this entropy argument would charge roughly
(1/2)log_2 m+O(1) bits per row. Equation (4) accounts for the mesh
2^{|S|}, saving approximately |S| bits while the rescaled variance is
large. This difference
rules out the first proposed parameter scale.

### 3.2 Elementary quantitative exclusion

For d=2m and k=m-u, 1<=u<m, the following finite inequalities suffice:

$$
 \frac{\binom{2m}{m-u}}{2^{2m}}
 \leq\frac{1}{\sqrt{3m+1}}
                 \exp\left(-\frac{u^2}{m+u}\right),
 \qquad
 r\leq\frac{m+u+1}{2u+1}\binom{2m}{m-u}.
 \tag{6}
$$

For the first, induction gives binom(2m,m)/4^m<=1/sqrt(3m+1): the induction
step is the elementary inequality
((2m+1)/(2m+2))^2<=(3m+1)/(3m+4). The ratio to the central binomial
coefficient is the product of (m-j+1)/(m+j), j=1,...,u. Applying
log(1-z)<=-z bounds its logarithm by -u^2/(m+u). For the second, successive
lower terms have ratio at most (m-u)/(m+u+1), so sum a geometric series.

Equations (3), (5), and (6) give an explicit finite upper bound for eta.
In particular, along even d,

$$
 k=\left\lfloor\frac d2-a\sqrt{d\ln d}\right\rfloor,
 \quad a>\tfrac12
 \quad\Longrightarrow\quad \eta(d,k)\longrightarrow0.
 \tag{7}
$$

Indeed the leading bound is O(sqrt(d) exp(-u^2/(d/2+u))), which is
 d^{1/2-2a^2+o(1)}. Therefore this range cannot furnish the required
uniform extraction constant.

A specific surviving candidate scale is

$$
 \boxed{k_d=\left\lfloor\frac d2-
                         \frac12\sqrt{d\ln d}\right\rfloor.}
 \tag{8}
$$

Equation (5) does not force the density to zero there. It also does not
prove positive density. The new route remains conditional at this point.

## 4. Affine cubes do not capture the relation system

### 4.1 Minimum relation support

Every nonzero ternary relation in E_{d,k} has at least 2^{k+1} points in
its support. Reduce it modulo two, giving a nonzero binary function f
whose moments through degree k vanish. The bound follows inductively.
Write f_0,f_1 for its restrictions to the last coordinate. The function
f_0+f_1 has zero moments through degree k in d-1 variables, and f_1 has
zero moments through degree k-1. If f_0+f_1 is nonzero, its support already
has size at least 2^{k+1}, no larger than that of f. If it is zero, then
f_0=f_1 is nonzero and its doubled support has size at least
2 times 2^k. The base k=0 is even nonzero support, of size at least two;
when all monomial rows are present their inclusion matrix has full rank.
This also handles the endpoint cases in the induction.

There are at most 2^{d^2+d} affine subspaces of F_2^d: choose an origin and
an ordered d-tuple of generators. A random two-coloring therefore has
probability at most

$$
 2^{d^2+d+1-2^{k+1}}
 \tag{9}
$$

of a monochromatic affine subspace of dimension at least k+1. Whenever
the exponent is negative, some two-coloring avoids every such subspace,
and hence every relation whose support is an affine subspace. This applies
in (8) for sufficiently large d. It is **not** a proper coloring of all
moment trades.

### 4.2 Explicit non-affine flat circuits at every order

In four binary coordinates take

$$
\begin{aligned}
 P&=\{1000,0101,0011\},\\
 M&=\{0001,1101,0010\},\qquad S=P\cup M.
\end{aligned}
$$

The three points in P and those in M have the same coordinate sums and
the same cardinality. More strongly, the degree-one moment matrix on S
has exactly the one-dimensional kernel generated by
(1,1,1,-1,-1,-1), in the displayed order.

For an elementary check, call its coefficients a,b,c,d,e,f. The four
coordinate equations give e=-a, b=a, f=-c, d=-c; the constant row then
gives c=a. The row x_1 x_2 evaluates this kernel to -a, so degree-two
moments have zero kernel on S. Every five-column subset is independent.

The XOR of all six points is zero. A four-point affine plane in S would
have XOR zero, forcing the complementary two distinct points also to
have XOR zero, which is impossible. Thus S contains no affine plane.

For k>=1 put ell=k-1 and take S times {0,1}^ell in k+3 coordinates.
Give its point (x,y) coefficient f_0(x)(-1)^{|y|}, where f_0 is +1 on P
and -1 on M. This is a flat moment relation through degree k.
It is in fact the unique relation up to scale on that support.

To see uniqueness, expand any coefficient array in Walsh frequencies T
of the ell new coordinates. The coefficient function on S at frequency T
must annihilate the old moments through degree k-|T|. If |T|<ell, this
includes degree two and the coefficient function is zero. If T is the
whole ell-set, it must be a scalar multiple of f_0. This proves uniqueness,
including ell=0, and hence proves that the support is a rational circuit
with all primitive coefficients +1 or -1.

Its size is 6 times 2^{k-1}. It contains no affine subspace of dimension
k+1: the projection of any contained affine subspace to the old four
coordinates is contained in S and has dimension at most one, while its
projection kernel has dimension at most ell. Extra coordinates may be
fixed at zero to embed the same circuit in any E_{d,k} with d>=k+3.

These are genuine non-affine circuits, not just sums of smaller supported
cube relations. Their existence does not force a monochromatic copy in
an arbitrary coloring.

## 5. A limitation of a prospective extraction proof

A plain first-moment deletion argument would be the wrong positive certificate
for this particular family. Let H be the family of distinct inclusion-minimal
supports of nonzero ternary relations, and put T_{d,k}(z)=sum_{F in H} z^{|F|}.
Suppose, for one fixed 0<p<1, one proved T_{d,k}(p)=O(n) along (8). For any
fixed integer q with pq>=2,

$$
 \mathbb E(\text{monochromatic minimal supports in a random }q\text{-coloring})
 =q T_{d,k}(1/q)
 \leq q\,2^{-2^{k+1}}T_{d,k}(p)=o(1).
 \tag{10}
$$

The inequality uses the minimum support from Section 4.1 and
2^{k+1} much larger than log n. Thus such a relation-count bound would
actually give a bounded proper coloring, not the desired counterexample.
This excludes only that particular counting/alteration certificate, not
structural extraction proofs or the family itself.

## 6. Exact tasks before this becomes a counterexample

For some sequence in or above the surviving window, both of the following
are needed; sequences covered by the exact finite two-coloring criterion of
[the Gaussian coloring theorem](moment_gaussian_coloring.md) are excluded.

1. alpha(d,k)>=delta 2^d with one delta>0. By (3), this is enough for
   hereditary full-dissociation extraction. At the rounded critical
   boundary this is proved on the
   [boundary extraction page](moment_boundary_extraction.md).
2. chi_1(E_{d,k}) is unbounded, against arbitrary actual colorings and
   using all flat moment trades, not only affine-cube templates. This is
   unproved.

If both were established, final exact integer encoding and separated-block
assembly from the main argument would give the required infinite integer
set.

## Check record

One prescribed finite certificate was checked computationally, without a
search: the six four-bit points in Section 4.2. Exact rational elimination
checked the 5-by-6 degree-one matrix, each of its six five-column deletions,
and the matrix after adjoining x_1 x_2. The respective ranks were 5, six
copies of 5, and 6. The stated signed sum was zero, and its x_1 x_2 sum
was -1. All fifteen four-point subsets were checked for zero XOR; none
was found. The direct proof above makes the theorem independent of that
calculation. Nine even-parity-restriction Smith-form diagnostics for
3<=d<=7, 1<=k<d/2, are recorded with the
[Smith-form probe](../evidence/moment_band_determinants/_index.md); they
supply no theorem on this page.

The entropy argument and non-affine-circuit construction are
author-recorded; a separate reviewer checked each. No external review or
E0774 solution is claimed.
