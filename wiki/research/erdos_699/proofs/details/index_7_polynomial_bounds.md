---
name: research/erdos_699/proofs/details/index_7_polynomial_bounds
title: "Erdős 699: sharper polynomial stopping bound at seven"
desc: "A monic Newton basis, exact Farkas margins, and uniform arithmetic nonvanishing reduce the polynomial height exponent from 19813540001 to 44245906."
created: 2026-09-22T16:30:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: sharper polynomial stopping bound at seven

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[Effective index-seven proof](index_7_effective.md)

***

The polynomial part of the existing index-seven proof holds once

$$
\boxed{h=n-6\ge10^{44\,245\,906}.}
$$

This replaces the previous exponent $19\,813\,540\,001$. The analytic
source thresholds must still be included. This result alone is not a
fully numerical bound for every bad triple and does not exclude the
finite range.

The [checker](../../computations/erdos_699_index_7_polynomial_bounds.py)
and [data](../../computations/erdos_699_index_7_polynomial_bounds.json)
reuse the 49 already verified polynomial certificates. There are three
changes: smaller coefficient estimates in a monic Newton basis, the
actual contradiction margin at each of the 3356 rational leaves, and
[uniform arithmetic nonvanishing](index_7_nonvanishing.md)
for the degree-196 certificate, which then needs no resultant bound.

## Smaller coefficient bounds in an integer basis

For a degree-$d$ residual polynomial, put

$$
f_a(X)=\prod_{0\le k<a}(X-(k\bmod5)),\qquad f_0=1.
$$

Use the symmetric basis $f_a(X)f_b(Y)+f_b(X)f_a(Y)$ for $a<b$, and
$f_a(X)f_a(Y)$ on the diagonal, with $a+b\le d$. Since each $f_a$ is
monic with integer coefficients, the change from the monomial basis is
integral, triangular, and has diagonal one. It is invertible over the
integers and modulo 251. All retained rank and kernel assertions
therefore remain valid.

The Hasse coefficients are exact integers, computed by the recurrence

$$[U^r]f_{a+1}(x+U)
=(x-(a\bmod5))[U^r]f_a(x+U)+[U^{r-1}]f_a(x+U).$$

For each prescribed jet, the checker bounds the entries in its entire
row by twice the largest product of two such coefficients with combined
degree at most $d$. If this bound is $H_v$, choose the least integer
$b_v$ with

$$
rH_v^2\le10^{2b_v},
$$

where $r$ is the number of jet rows. Every maximal $r$-column minor then
has absolute value at most $10^B$, $B=\sum_vb_v$, by Hadamard's inequality.
This also bounds every Cramer replacement minor.

A Newton basis element has coefficient norm at most $2\cdot5^d$.
Consequently the earlier right-inverse and kernel-lifting estimates apply
with $r(d+6)$ replaced by

$$
B+\lceil\log_{10}(5^d)\rceil.
$$

The checker compares these bounds with the analogous row-dependent
monomial estimates and takes the smaller valid bound for each polynomial.
No new modular ranks are required for this change of basis.

For the largest certificate, `poly_coprime_last`, the calculation gives

$$d=196,\quad r=9792,\quad B=320354,\quad
\lceil\log_{10}(5^{196})\rceil=137.$$

Its full divisibility constant is at most $10^{323861}$. The Cramer lift
factor $2s(s+1)p$ is less than $10^{20}$, where $s=9801$, $p=251$.

## Removing common zeros without a height estimate

The new [arithmetic nonvanishing certificate](index_7_nonvanishing.md)
adds a third modular kernel section. The only common points of the first
two sections over $\mathbf F_{251}$ are the prescribed grid and four
additional points. The third section excludes those four points.
At each grid point, exact tangent calculations exclude any distinct
251-adic common zero reducing to it. Two diagonal points require one
further local calculation, whose determinants are 90 and 48 modulo 251.

Thus three symmetric lifts have no common integer zero outside the grid.
They may be lifted in the Newton basis above with the same individual
coefficient bound. At least one is nonzero at every admissible
$(j,n-j)$, so degree 196 is available with no common-zero height threshold.
The checker calls the new nonvanishing verifier and names its certificate
file. For comparison only, the sharpened resultant estimate would have
required exponent $125\,720\,282$.

## Use the exact margin of each contradiction

Put $L=\log_{10}h$. For polynomial certificate $k$, the necessary
inequality under badness is

$$
a_k\cdot e\le b_k+E_k/L,
$$

where $E_k$ is the new integer logarithmic coefficient bound. The old
forest replaced every $E_k/L$ by the common slack $\delta=10^{-4}$.
There is no need to make all these replacements before applying Farkas's
lemma.

At a retained leaf let $\lambda_k$ be its exact nonnegative multipliers,
and let $-\beta<0$ be the stored weighted right side with slack $\delta$.
Remove that slack and define

$$\alpha=\beta+\delta\sum_{k\text{ polynomial}}\lambda_k>0,
\qquad E=\sum_{k\text{ polynomial}}\lambda_kE_k.$$

The same weighted sum of the actual inequalities gives

$$
0\le-\alpha+E/L.
$$

It is impossible whenever $L>E/\alpha$. The checker verifies the
existing exact forest and evaluates this ratio at every leaf. Its maximum
is

$$\frac{32\,386\,100\,000\,000}{731957}
 <44\,245\,906.$$

The collision certificate needs only $L\ge822$. The displayed threshold
therefore covers the complete polynomial part. The data retain the exact
worst leaf and every polynomial's row-bound digest and coefficient
estimate. Analytic inequalities in this calculation
are unchanged from the original effective proof.
