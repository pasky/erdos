---
name: research/erdos_774/lemmas/moment_flattening_limits
title: Exact limits of three moment flattening mechanisms
desc: Critical full moment tensors lose extraction, low-degree height-two functions need not have ternary substitutes on their support, and recoverable pointwise ternarization incurs full original degree.
tags: [E0774, Boolean-moments, proved, scoped-obstruction]
sources: []
created: 2026-09-19T01:50:00Z
updated: 2026-09-19T01:50:00Z
---


# Exact limits of three moment flattening mechanisms

***

The [critical moment family](../routes/moment_boundary_extraction.md) has
uniform hereditary full-dissociation extraction. Every fixed palette also
forces a [palette-dependent-height relation](moment_palette_height.md).
The missing conclusion remains an **actual monochromatic ternary** relation.
The three results here delimit particular ways of connecting these facts;
they do not exclude color-adaptive, nonpointwise constructions.

## 1. Full tensors of critical moment configurations lose extraction

Let $E_i=E_{d_i,k_i}$, where $1\leq k_i\leq d_i/2$, and put

$$
n_i=2^{d_i},\quad r_i=\sum_{j\leq k_i}\binom{d_i}j,\quad
D_i=(d_i-k_i)\binom{d_i}{k_i},\quad N=\prod_i n_i,\quad R=\prod_i r_i.
$$

For the full tensor $A=\bigotimes_{i=1}^s E_i$, its largest dissociated
subset satisfies the exact finite bound

$$
\boxed{\alpha(A)\leq
 \frac12\sum_{i=1}^s D_i\prod_{j\ne i}r_j+c_0R,\qquad
c_0=\tfrac12\log_2(2\pi e/3).}                    \tag{1}
$$

In particular its hereditary extraction constant is at most the right
side divided by $N$.

**Proof.** Identify the columns with points of a Boolean cube of dimension
$d=\sum_i d_i$. The retained Walsh rows have indices $S=(S_i)$ with
$|S_i|\leq k_i$; this is a downset, though not a total-degree ball. The monomial
and Walsh rows are related by an invertible triangular change, preserving
dissociation. For a dissociated subset $F$ of size $M$, take independent fair
bits $\xi_x$, $x\in F$, and form

$$
Y_S=\sum_{x\in F}\xi_x\chi_S(x).
$$

The vector $Y$ has entropy $M$ bits, because subset sums are distinct.
Order rows by total degree. Expanding each Walsh character into
squarefree monomials shows that, conditional on earlier rows, $Y_S$
lies in one residue class modulo $2^{|S|}$. All proper subindices
occur earlier in this downset; their Walsh sums determine the needed
monomial sums by the triangular expansion.

For an integer variable on a mesh of step $h$, add independent uniform
interval jitter after dividing by $h$. Gaussian maximal entropy gives
the bound $\frac12\log_2(2\pi e[\operatorname{Var}/h^2+1/12])$.
Apply this conditionally, use concavity of logarithm, and use total
variance to bound the averaged conditional variance by
$\operatorname{Var}Y_S=M/4$. Thus

$$
H(Y_S\mid\text{earlier rows})
\leq\tfrac12\log_2\!\left(2\pi e
 [M/4^{|S|+1}+1/12]\right).
$$

Since $M\leq2^d$ and $2|S|\leq d$, the bracket is at most

$$
2^{d-2|S|}/4+1/12\leq2^{d-2|S|}/3.
$$

The contribution is consequently at most $d/2-|S|+c_0$.
Summing and using

$$
\sum_{j\leq k_i}(d_i/2-j)\binom{d_i}j=D_i/2
$$

proves (1). The full family itself suffices for the claimed upper bound
on hereditary extraction. Cube-flip transitivity also gives
$\eta(A)=\alpha(A)/N$, but is not needed for the exclusion. $\square$

For two critical factors with both dimensions tending to infinity,

$$
\eta(E_1\otimes E_2)
\leq\frac{D_1}{2n_1}\frac{r_2}{n_2}
    +\frac{D_2}{2n_2}\frac{r_1}{n_1}
    +c_0\frac{r_1r_2}{n_1n_2}\longrightarrow0.     \tag{2}
$$

Indeed $D_i/(2n_i)\to1/(2\sqrt{2\pi})$ and $r_i/n_i\to0$.
No comparison of the two dimension-growth rates is required. For $s$
identical factors,

$$
\eta(E_{d,k}^{\otimes s})\leq
s\frac D{2n}(r/n)^{s-1}+c_0(r/n)^s.              \tag{3}
$$

Thus every fixed $s\geq2$ loses uniform extraction along the critical
sequence. This is an actual exclusion, not merely the observation that
rectangular tensors differ from total-degree moments. It does not apply
to sparse tensor subsets or to the distinct family $E_{\sum d_i,k_{\sum d_i}}$.

### The analogous simplicial and mixed full tensors

These two additional bounds are author-recorded. For simplicial blocks
$S_{n_i,k_i}$,
write $N_i=\binom{n_i}{k_i}$, $M_i=\binom{n_i}{k_i-1}$, and
$L_i=n_i-k_i+1$. Every row in their full tensor has $L_1L_2$
nonzero entries, of magnitude one. Fair subset-sum entropy and the
one-coordinate integer Gaussian bound give

$$
\eta(S_1\otimes S_2)\leq
\frac{k_1k_2}{2L_1L_2}
 \log_2\!\left(2\pi e[L_1L_2/4+1/12]\right).     \tag{3a}
$$

Indeed each row variance is at most $L_1L_2/4$; sum the entropy
bounds over its $M_1M_2$ rows and divide by $N_1N_2$.
No row independence is assumed. At fixed critical constants
$n_i/k_i\sim C_i\log n_i$, (3a) tends to zero when both $n_i$
grow, of order $1/\log n_1+1/\log n_2$.

For a moment block $E_{d,k}$, write $n,r,D$ as above. For a
simplicial block write $L_s=n_s-k_s+1$. The same proof, now
conditioning the moment rows at each simplicial row, gives

$$
\eta(E_{d,k}\otimes S_{n_s,k_s})\leq
\frac{k_s}{L_s}\left\{\frac D{2n}
 +\frac rn\left[\tfrac12\log_2 L_s+c_0\right]\right\}. \tag{3b}
$$

The conditional mesh is $2^{|S|}$, and the unconditional row variance
is at most $nL_s/4$; the derivation of (1) thus adds
$\frac12\log_2L_s$ to each moment-row entropy charge. At the two
critical scales, the first term in (3b) vanishes with $n_s$, and
the second vanishes with $d$, since
$(k_s/L_s)\log_2L_s$ stays bounded. Thus this mixed full tensor also
loses extraction whenever both critical indices tend to infinity.

## 2. A one-dimensional height-two space with no ternary vector

For $1\leq\ell\leq d-2$, put $a=\ell-1$, $b=d-\ell-2$, and

$$
C=\{u\in\{0,1\}^3:|u|\ne2\}\times\{0\}^{a}\times\{0,1\}^{b}.
$$

The real multilinear polynomials of degree at most $\ell$ supported
on $C$ form exactly the line generated by

$$
P(u,z,w)=(2-u_1-u_2-u_3)\prod_{j=1}^{a}(1-z_j).   \tag{4}
$$

To see this, support on $z=0$ forces any function to equal
$\prod_j(1-z_j)Q(u,w)$, by uniqueness of multilinear interpolation.
The degree of this product is $a+\deg Q$, so $Q$ is affine.
Vanishing at every weight-two $u$, for all $w$, first kills all
free-coordinate coefficients. The three remaining equations on the
affine coefficients force $Q$ to be a multiple of $2-u_1-u_2-u_3$.

The values of $P$ include $2,1,-1$. Thus it has integer height two,
but no nonzero scalar multiple takes only the values $0,\pm1$.
Parity multiplication identifies degree-$\ell$ functions with relations
for moment order $d-\ell-1$, as in the existing moment construction.
Consequently a real annihilator, even an integer one of height two,
does not automatically give a ternary annihilator on the same support.

This applies at the exact critical degree $\ell=d-k_d-1$, eventually.
The support density is $5/2^{\ell+2}$, tending to zero. It does not
construct a bounded proper palette or contradict an arbitrary-color
theorem for large color classes.

## 3. Recoverable pointwise ternarization incurs full original degree

Let $d/2\leq\ell<d$, and choose proper subsets $A,B\subset[d]$
with $|A|=|B|=\ell$ and $A\cup B=[d]$. Put

$$
p(x)=x_A+x_B\in\{0,1,2\}.
$$

Suppose $Y$ is finite and an encoder
$\Phi:\{0,1,2\}\times Y\to\{0,\pm1\}$ obeys

$$
\Phi(0,y)=0,\qquad \sum_{y\in Y}w_y\Phi(h,y)=h
\quad(h=0,1,2)                                    \tag{5}
$$

for fixed real weights $w_y$. For some $y$,

$$
b_y:=\Phi(2,y)-2\Phi(1,y)\ne0.
$$

Otherwise ternarity would force both $\Phi(1,y)$ and $\Phi(2,y)$
to vanish for every $y$, contradicting (5). On the Boolean cube,

$$
\Phi(p(x),y)=\Phi(1,y)(x_A+x_B)+b_yx_{[d]}.        \tag{6}
$$

Thus some fiber has degree exactly $d$. If $Y=\{0,1\}^t$, the
total multilinear degree of $F(x,y)=\Phi(p(x),y)$ is at least $d$,
since restriction cannot increase degree. For unweighted recovery,
$\sum_y b_y=0$, so its nonzero coefficient function $b(y)$ is
nonconstant and the total degree is at least $d+1$.

In particular $t=o(d)$ ancillary coordinates cannot give a universal
encoder of this form within a critical half-degree bound on $d+t$
variables. The theorem concerns pointwise, zero-preserving, linearly
recoverable encoders. It does not prohibit palette-dependent or
nonpointwise operations.

## Checks

All three proofs are finite algebra and entropy arguments, with no
computational search, and are author-recorded. Statements (4)--(6) were
checked against a separate derivation, and a separate reviewer checked the
rectangular tensor calculation, including its mesh conditioning,
constants, distinct columns, and asymptotic quantifiers. These are
internal reviews only.
