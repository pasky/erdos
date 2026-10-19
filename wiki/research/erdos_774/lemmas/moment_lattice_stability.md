---
name: research/erdos_774/lemmas/moment_lattice_stability
title: Semistability of integer Boolean polynomial lattices
desc: Exact coordinate compression proves full semistability of Boolean polynomial lattices; with the weak stable-lattice Gaussian theorem it gives critical-boundary extraction.
tags: [E0774, Boolean-moments, lattice, proved]
sources: []
created: 2026-09-18T23:14:00Z
updated: 2026-09-18T23:28:00Z
---


# Semistability of integer Boolean polynomial lattices

***

The semistability theorem combines with
[a weak stable-lattice Gaussian bound](stable_lattice_free_energy.md)
to prove [critical moment extraction](../routes/moment_boundary_extraction.md).
The compression recurrence itself does not yield that bound.

## Theorem

Let X={0,1}^d, and let V_ell be the real span of Walsh functions chi_S,
|S|<=ell. Put

$$
 L_{d,\ell}=V_\ell\cap\mathbb Z^X,
 \qquad m=\sum_{s=0}^{\ell}\binom ds.
$$

For every nonzero sublattice M of L_(d,ell),

$$
 \boxed{\det(M)^{1/\operatorname{rank}M}
  \geq 2^{(d-\ell)\binom d\ell/(2m)}
  =\det(L_{d,\ell})^{1/m}.} \tag{1}
$$

Here determinant is Euclidean covolume in the real span. Thus dividing
L_(d,ell) by its normalized covolume gives a determinant-one lattice
whose every sublattice has determinant at least one: a *stable lattice*.
The proof is elementary and applies to 0<=ell<=d.

For the moment problem the relation lattice is isometric to
L_(d,d-k-1), by multiplication by the full parity character. The
[Gaussian consequence](../routes/moment_gaussian_coloring.md) of (1)
actually gives two-colorings in a substantial regime. Neither (1) nor
that consequence settles E0774.

## 1. Exact coordinate compression of spectral lattices

For any set F of subsets of [d], define

$$
 K_F=\mathbb Z^X\cap\operatorname{span}_{\mathbb R}
                       \{\chi_S:S\in F\},
 \qquad h_d(F)=\log_2\det K_F.
$$

Use det K_empty=1. Its rank is |F|. Split F by the last coordinate,
with lower-dimensional sections

$$
 A=\{S\subseteq[d-1]:S\in F\},\qquad
 B=\{S\subseteq[d-1]:S\cup\{d\}\in F\}.
$$

Downward compression replaces these sections by U=A union B and
I=A intersect B. Denote the result by C_d F. This preserves |F| and
never increases the size of a frequency set.

**Exact identity.** For the finite abelian group

$$
 Q=K_U/(K_A+K_B),
$$

one has

$$
 \boxed{\det K_F=|2Q|\,\det K_{C_dF}.} \tag{2}
$$

### Proof of the identity

Write a=|A|, b=|B|, i=|I|. Let C_A and C_B be the reductions of K_A
and K_B in the ambient binary coordinate space. Every K_F is saturated
in its ambient integer lattice, so reduction modulo two has dimension
equal to its rank. An integer function in the original spectral space
corresponds exactly to

$$
 (x,y)\in K_A\oplus K_B,\qquad x\equiv y\pmod2,
$$

under the map (x,y) -> ((x+y)/2,(x-y)/2). The parity condition has index
2^(a+b-dim(C_A intersect C_B)). The map scales all lengths by 1/sqrt(2).
Consequently

$$
 h_d(F)=h_{d-1}(A)+h_{d-1}(B)
        +\frac{a+b}{2}-\dim(C_A\cap C_B). \tag{3}
$$

In the compressed case C_I is contained in C_U, giving

$$
 h_d(C_dF)=h_{d-1}(U)+h_{d-1}(I)+\frac{a+b}{2}-i. \tag{4}
$$

The exclusive Walsh directions of the two real spans are orthogonal.
Therefore the sum/intersection determinant identity has no angle factor:

$$
 \det K_A\det K_B
       =\det K_I\det(K_A+K_B)
       =|Q|\det K_I\det K_U. \tag{5}
$$

For an elementary verification of the first equality, take a basis of
the common lattice K_I and extend it to bases of K_A and K_B.
Their images after orthogonal projection off the common real span lie
in orthogonal Walsh subspaces. The projected extended vectors form a
basis of the projected sum lattice, so their volumes multiply.

The image of K_A+K_B in K_U/2K_U has dimension
|U|-dim(Q/2Q). This follows by taking its quotient, which is
K_U/(K_A+K_B+2K_U)=Q/2Q. Saturation of K_U identifies its reduction
with its ambient reduction, namely C_A+C_B. Hence

$$
 \dim(C_A\cap C_B)=i+\dim(Q/2Q). \tag{6}
$$

Subtract (4) from (3), using (5)--(6). The difference is
log_2 |Q|-dim(Q/2Q)=log_2 |2Q|, proving (2).
In particular compression cannot increase covolume.

## 2. Downsets and mean degree

Repeat changing coordinate compressions. Each strictly lowers
sum_(S in F)|S|, a nonnegative integer. The procedure therefore ends
at a downset D of the same cardinality, with

$$
 h_d(F)\geq h_d(D). \tag{7}
$$

If F lies in the degree ball B_ell={S:|S|<=ell}, so does D.
For a downset D, the monomial evaluations x_S, S in D, form an integer
basis of K_D. Walsh expansion stays inside D, and Boolean Mobius
inversion makes all monomial coefficients of an integer-valued function
integral. The orthogonal residual at S, in an inclusion-compatible
ordering, is (-1)^|S| 2^(-|S|) chi_S. Thus

$$
 h_d(D)=\sum_{S\in D}(d/2-|S|). \tag{8}
$$

Let a_s count the members of D of size s, and put
p_s=a_s/binom(d,s), for 0<=s<=ell. Counting adjacent-level incidences
gives (s+1)a_(s+1)<=(d-s)a_s, so p_s is nonincreasing.
Under weights w_s=binom(d,s), the increasing sequence s has nonpositive
covariance with p_s: expand

$$
 \sum_{s,t=0}^{\ell}w_sw_t(s-t)(p_s-p_t)\leq0.
$$

It follows that the mean degree in a nonempty D is at most the mean
degree in B_ell. Combining this with (7)--(8) proves, for every nonempty
spectral subset F of B_ell,

$$
 \frac{h_d(F)}{|F|}
 \geq\frac{h_d(B_\ell)}{|B_\ell|}
 =\frac{(d-\ell)\binom d\ell}{2m}. \tag{9}
$$

The last identity follows by telescoping
sum_(s<=ell)(d-2s)binom(d,s)=(d-ell)binom(d,ell).

## 3. Reduction of all sublattices to spectral subspaces

Let alpha be the least normalized covolume of a nonzero sublattice of
L_(d,ell). It is attained. Indeed each squared covolume is the positive
integer determinant of an integral Gram matrix. There are only finitely
many possible such values below any fixed bound, and only m possible
ranks. Saturating a sublattice in its real span can only lower its
covolume, so every minimizer is saturated.

For saturated sublattices M,N of a Euclidean lattice one has

$$
 \det(M+N)\det(M\cap N)\leq\det M\det N, \tag{10}
$$

with determinant one for the zero lattice. To see this, extend a basis
of the intersection to bases in M and N and project off its real span.
Volume of the combined projected parallelepiped is at most the product
of the two volumes; equivalently its remaining principal-angle factor
is at most one. Here the intersection is saturated in each lattice,
because M and N are saturated in the common ambient lattice; their real
intersection is spanned by their lattice intersection.

If M and N attain alpha, their ranks add under sum and intersection.
The defining lower bound alpha^rank on each determinant and (10) force
the sum also to attain alpha. It follows that the maximal-rank minimizer
M_0 is unique: its sum with any other minimizer would otherwise have
larger rank or smaller covolume after saturation.

Every cube flip is an isometric automorphism of L_(d,ell), hence preserves
M_0 and its real span. A real subspace invariant under all cube flips
is spanned by some Walsh lines. Explicitly, the projection onto any Walsh
line is the signed average of the flip operators, and so preserves the
invariant subspace. Thus span M_0=span{chi_S:S in F} for a subset F of
B_ell. Saturation gives M_0=K_F. Applying (9) proves (1), since the
entire lattice itself is among the sublattices under consideration.

## 4. Compression also increases Gaussian and ternary enumerators

For every t>0 define Theta_F(t)=sum_(f in K_F)exp(-pi t ||f||^2).
The same frequency compression satisfies

$$
 \Theta_F(t)\leq\Theta_{C_iF}(t). \tag{11}
$$

Here is a proof retaining the coset information, not just determinants.
Use sections A,B and U,I as before, and let pi be orthogonal projection
from V_U onto E=V_(U minus I). On E let R act as +1 on V_(A minus B)
and -1 on V_(B minus A). Thus R is an orthogonal involution. In terms
of the two physical half-functions f_0,f_1, the original spectral lattice
is exactly

$$
 \{(f_0,f_1)\in K_U^2:\pi f_1=R\pi f_0\};
$$

the compressed lattice replaces R by the identity. Put Gamma=pi K_U and

$$
 w_t(p)=\sum_{z\in K_U:\pi z=p}e^{-\pi t\|z\|^2},
$$

extended by zero outside Gamma. On the R-invariant countable set
Gamma union R Gamma,

$$
 \Theta_F(t)=\sum_p w_t(p)w_t(Rp),\qquad
 \Theta_{C_iF}(t)=\sum_p w_t(p)^2.
$$

Their difference is (1/2)sum_p(w_t(p)-w_t(Rp))^2, proving (11).
All Gaussian sums converge. Replacing the Gaussian weight by
1_(z in {-1,0,1}) q^|supp z| proves, for every q>=0,

$$
 \sum_{f\in K_F\cap\{-1,0,1\}^X}q^{|\operatorname{supp}f|}
 \leq
 \sum_{f\in K_{C_iF}\cap\{-1,0,1\}^X}q^{|\operatorname{supp}f|}.
 \tag{12}
$$

This is pointwise in q, not a coefficientwise inequality. A full degree
ball is already compressed, so neither assertion supplies its missing
constant-parameter theta bound. For such balls there is the exact recurrence,
with A=L_(d-1,ell) and B=L_(d-1,ell-1),

$$
 \Theta_{d,\ell}(t)
 =\sum_{a\in A/B}
       \left(\sum_{z\in a+B}e^{-\pi t\|z\|^2}\right)^2,
 \tag{13}
$$

since L_(d,ell)={(u,v) in A^2:u-v in B}. The quotient can be infinite;
the displayed nonnegative sum is still convergent. Discarding the shifted
coset information does not yield the required boundary estimate.

## Scope and checks

The compression identity and its use in semistability are author-recorded;
separate reviewers checked each. The result is not inferred from a determinant
table. Before this proof was obtained, a finite Smith-form diagnostic tested all
53 nonempty degree unions at (d,ell)=(4,2),(6,3),(6,4); it found no violation.
Exact input matrices and output are retained in the
[Smith-form probe](../evidence/moment_band_determinants/_index.md). No further
diagnostic is needed for (1), and no external review is claimed.
