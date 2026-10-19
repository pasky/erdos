---
name: research/erdos_940/quartic_euler_majorant
title: Uniform quartic zero-local Euler-product majorant
desc: Coefficient-uniform quartic local Euler bounds from eleven nonprincipal character factors.
tags: []
sources: []
created: 2026-09-22T02:24:55Z
updated: 2026-09-23T00:37:30Z
---

# Uniform quartic zero-local Euler-product majorant

***

Let `d=(d_1,d_2,d_3,d_4)` be positive integers, write `D=d_1d_2d_3d_4`, and set


$$
 \rho_p(0;d)=p^{-3}\#\{x\in\mathbf F_p^4:\textstyle\sum_i d_i x_i^4=0\}.
$$


Assume

1. `D` is not a rational square;
2. for every ordered pair of distinct indices `a,b`, with complementary indices
   `c,d`, $d_a^3d_b d_c^2d_d^2\notin4\mathbf Q^{\times4}$.

Then, uniformly for `B>=2`,


$$
 \prod_{\substack{2<p\le B\\p\nmid D}}\rho_p(0;d)
 \ll (\log(2D))^{11}\ll_\epsilon D^\epsilon.
 \tag{1}
$$


The implied constant in the first bound is absolute. One may replace its
displayed exponent 11 by any larger fixed exponent without changing the
application.

## 1. Exact local trace expansion

For odd `p` not dividing `D`, write

$$
 \rho_p(0;d)=1+\frac{p-1}{p^2}A_p(d).
 \tag{2}
$$

If `p=3 mod4`, fourth powers and squares have identical counting measures on the
finite field, and

$$
 A_p(d)=\left(\frac Dp\right).
 \tag{3}
$$


Suppose `p=1 mod4`. Choose one prime ideal `P=(pi)` above `p` in `Z[i]`, choose
its primary generator `pi=1 mod (1+i)^3`, and let `chi=(./P)_4`. Put
`tau_j=G(chi^j)`. Additive orthogonality gives

$$
 A_p(d)=p^{-2}
 \sum_{\substack{j_1,\ldots,j_4\in\{1,2,3\}\\\sum j_i=0\pmod4}}
 \prod_i\tau_{j_i}\chi^{-j_i}(d_i).
 \tag{4}
$$

There are 21 terms, so `|A_p(d)|<=21`. The exponent patterns are

$$
 (2,2,2,2),\quad (1,1,3,3),\quad(1,3,2,2),\quad(1,1,1,1),\quad(3,3,3,3),
$$

with multiplicities 1,6,12,1,1. Using

$$
 \tau_2^2=p,\qquad \tau_1\tau_3=\chi(-1)p,
 \qquad \tau_1^4/p^2=J(\chi,\chi)^2/p=\pi^2/p,
$$

we obtain the following character decomposition.

Let `psi_R` be the quartic Kummer Hecke character of `Q(i)` corresponding to the
positive or negative rational number `R`, so $\psi_R(P)=(R/P)_4$. Let
`nu((pi))=pi^2/N(pi)` for primary generators; this is a unitary Hecke character
of infinity type 2 and modulus dividing `(1+i)^3`. Put $\eta=\nu\psi_D^{-1}$.
Then

$$
 A_p(d)=\chi_D(p)
 +\sum_{S\in\mathcal P}\sum_{P\mid p}\psi_{R_S}(P)
 +\sum_{\{a,b\}}\sum_{P\mid p}\psi_{-R_{ab}}(P)
 +\sum_{P\mid p}\eta(P),
 \tag{5}
$$

for split `p`, where:

* `chi_D` is the quadratic Dirichlet character of the squareclass of `D`;
* `P` (calligraphic) contains one representative of each of the three
  complementary pairs of 2-subsets of `{1,2,3,4}`;
* $R_S=\prod_{i\in S}d_i^3\prod_{i\notin S}d_i$;
* the second sum runs over the six unordered pairs `{a,b}`, and
  $R_{ab}=d_a^3d_b d_c^2d_d^2$, with either orientation of `{a,b}`.

Conjugate orientations give conjugate Hecke characters, explaining the traces
over the two prime ideals above `p`. At inert rational primes the Hecke prime
ideals have norm `p^2`; they do not contribute a rational-prime term of order
`1/p`.

Here is a direct verification of the needed squared Jacobi identity. Reduction
modulo `P` gives $J(\chi,\chi)\equiv\sum_x x^{(p-1)/4}(1-x)^{(p-1)/4}=0$,
because every monomial has positive degree less than `p-1`. The usual Gauss-sum
identity gives $|J|^2=p$, so `J` generates `P`. Pairing `x` and `1-x` in its
defining sum shows $J\equiv\chi(1/4)=\pm1\pmod2$. Thus `J` has odd real part and
even imaginary part. Generators of `P` with this parity are unique up to sign,
so their squares coincide. This proves `J^2=pi^2` for a primary generator and
also constructs `nu` directly as a Hecke character: choose the odd-real,
even-imaginary generator of any odd ideal and square it, dividing by its norm.
Multiplication preserves this parity and the sign disappears on squaring.

## 2. None of the eleven characters is principal

The Dirichlet character `chi_D` is nonprincipal by hypothesis 1. A rational
positive number is a fourth power in `Q(i)` precisely when it is a rational
fourth power. If `R_S` is a rational fourth power, reduction of its valuation
vector modulo 2 shows that `D` is a square, excluded here.

A negative rational number `-R`, with `R>0`, is a fourth power in `Q(i)`
precisely when `R in 4 Q^{x4}`. Indeed the fourth power of `a+bi` is real only
when `ab(a^2-b^2)=0`; the negative case has `a=+-b` and value `-4a^4`. Thus
hypothesis 2 excludes principality of the six mixed characters. Finally `eta`
has nonzero infinity type 2, and so is never principal.

All finite conductors, and a common modulus for the imprimitive versions of
these characters with every prime dividing `2D` removed, have norm bounded by a
fixed power of `2D`. This follows either from quartic reciprocity or from the
conductor-discriminant theorem applied to `Q(i,sqrt[4]{R})/Q(i)`: a
fourth-power-free representative of `R` can be chosen integral with absolute
value bounded by a fixed power of `D`, the polynomial discriminant is
`-256 R^3`, and the character conductor divides the relative discriminant. If
`x^4-R` is reducible, take the monic minimal factor of the chosen root; its
Gaussian-integral coefficients and the discriminant product formula show that
its discriminant divides the full polynomial discriminant. The field
discriminant divides that of this order. Twisting `nu` changes the conductor by
only a fixed power of `(1+i)`.

The character correspondence and the Jacobi infinity type are also stated in
[Ghidelli, Proposition 5.2](https://arxiv.org/html/1910.05070v1), whose relevant
passage has been checked. The polynomial discriminant argument gives the
polynomial conductor bound needed here, without a sharp conductor formula.

### A conductor bound in terms of the coefficient radical

Section 5 of the
[later independent record](independent/quartic_pattern_elimination_and_random_omission.md)
suggests the following sharper bound, checked here. Put
$R=\operatorname{rad}(D)$ and $\pi=1+i$. Every finite Gaussian character in (5)
has order dividing four, trivial infinity type, and conductor supported on the
prime ideals over $2D$, by the checked
[Proposition 5.2](../../../library/diophantine_problems/ghidelli_2019_arbitrarily_long_gaps_between_values_positive_definite_cubic_biquadratic_diagonal_forms/_index.md).
Since $\mathbb Z[i]$ is a PID, it is a residue-ring character. At an odd prime
ideal, the principal units in each finite quotient form an odd-primary group; an
order-dividing-four character kills them. At $\pi$, every unit
$u\equiv1\pmod{\pi^9}$ is a fourth power locally: Hensel at $1$ for $T^4-u$
applies because $v_\pi(u-1)\ge9>2v_\pi(4)=8$. Reducing the local fourth root
gives the same conclusion in every finite quotient. Thus the finite conductor
divides

$$
\pi^9\prod_{\substack{\mathfrak p\mid D\\\mathfrak p\nmid2}}
\mathfrak p.
$$

The Jacobi-square character has defining ideal dividing $(16)=\pi^8$,
so twisting it by a finite character preserves this bound. A common
imprimitive modulus, removing **all** prime ideals over $2D$, is therefore

$$
\mathfrak m=\pi^9\prod_{\substack{p\mid R\\p\text{ odd}}}(p),
\qquad N\mathfrak m\le512R^2.
\tag{5a}
$$

For the quadratic Dirichlet character, the analogous common presented
modulus is $4R$. The estimates of Sections 3–4 apply to these enlarged
moduli. Consequently (10), and hence (1), strengthen to

$$
\sum_{\substack{2<p\le B\\p\nmid D}}\frac{A_p(d)}p
\le11\log\log(3R)+O(1),\qquad
\prod_{\substack{2<p\le B\\p\nmid D}}\rho_p(0;d)
\ll(\log(3R))^{11}.
\tag{5b}
$$

No extra $\omega(R)$ loss is needed: the unwanted Euler factors are
removed in the defining moduli before applying the lattice estimate.
This refinement is not required by the original quartic proof; it is
useful in the [random omission alternative](quartic_random_omission.md).

## 3. An elementary uniform bound for the relevant Hecke L-functions

Let `psi` be a nonprincipal unitary Hecke character of `Q(i)` with fixed
infinity type `m` (here only 0 or 2) and integral modulus `f`, of norm `Q`.
Since `Z[i]` is principal, it has the form

$$
 \psi((z))=\omega(z)(z/|z|)^m,
$$

where `omega` is a Dirichlet character modulo `f`, extended by zero off the
invertible residue classes, with the appropriate compatibility on units.

For each residue class modulo `f`, a lattice Riemann-sum estimate in the disk
`|z|<=sqrt X` gives

$$
 \sum_{\substack{0<|z|\le\sqrt X\\z=a\pmod f}}
 (z/|z|)^m
 =\frac1Q\int_{|z|\le\sqrt X}(z/|z|)^m\,dz
 +O_m(\sqrt{X/Q}+1).
 \tag{6}
$$

For completeness, the boundary cells contribute `O(sqrt(X/Q)+1)`; in the
interior, the gradient of the angular factor is `O_m(1/|z|)`, whose disk
integral is `O_m(sqrt X)`, and the mesh diameter is `O(sqrt Q)`. The cell
containing zero costs `O(1)`.

Summing (6) over the `Q` residue classes, and dividing by four for units, gives

$$
 A(X):=\sum_{N(a)\le X}\psi(a)
 \ll_m \sqrt{QX}+Q.
 \tag{7}
$$

The main integral vanishes if `m != 0`. If `m=0`, it cancels because the finite
character is nonprincipal. The same proof works for any enlarged, imprimitive
modulus.

Split the Dirichlet series of `L(s,psi)` at `N(a)=Q`. The initial part is
`O(log(2Q))` because the number of Gaussian ideals of norm at most `X` is
`O(X)`. Partial summation with (7) bounds the remaining part by `O_m(1)`,
uniformly for real `s>=1`. Hence

$$
 |L(s,\psi)|\ll_m\log(2Q)\qquad(s\ge1).
 \tag{8}
$$

For nonprincipal Dirichlet characters over `Q`, the corresponding estimate
follows more simply by periodic cancellation, `|sum_{n<=X}chi(n)|<=q`, cutting
the series at its modulus `q`.

## 4. Comparison of partial Euler products with L-values

For `x>=3`, set `sigma=1+1/log x`. For any of the above unitary characters,

$$
 \sum_{N(P)\le x}\frac{\Re\psi(P)}{N(P)}
 =\log|L(\sigma,\psi)|+O(1),
 \tag{9}
$$

uniformly in the character and its modulus. Prime powers of exponent at least
two cost `O(1)`. For first powers, the absolute comparison below `x` is

$$
 \sum_{N(P)\le x}\frac{1-N(P)^{-1/\log x}}{N(P)}
 \le\frac1{\log x}\sum_{N(P)\le x}\frac{\log N(P)}{N(P)}\ll1.
$$

The tail above `x` is also bounded:

$$
 \sum_{N(P)>x}N(P)^{-1-1/\log x}\ll1.
$$

Both estimates use only the Chebyshev bound for prime ideals of `Q(i)`, which
follows immediately from the rational Chebyshev bound. The same argument applies
to Dirichlet characters over `Q`.

Use imprimitive versions of all eleven characters which vanish at every prime
dividing `2D`. Their moduli are still polynomially bounded in `D`. Equations
(5), (8), and (9), with the bounded contribution from inert prime ideals, give

$$
 \sum_{\substack{2<p\le B\\p\nmid D}}\frac{A_p(d)}p
 \le 11\log\log(2D)+O(1).
 \tag{10}
$$

Here there is one Dirichlet character and ten Gaussian Hecke characters: three
complementary 2-subset pairs, six mixed pairs, and the CM character.

Finally, from (2), `log(1+u)<=u`, and `|A_p|<=21`,

$$
 \log\prod_{\substack{2<p\le B\\p\nmid D}}\rho_p(0;d)
 \le\sum_{\substack{2<p\le B\\p\nmid D}}\frac{A_p(d)}p+O(1),
$$

which proves (1). If a factor is zero, the assertion is automatic.

## Status and scope

This proves the analytic majorant using the elementary local Gauss-sum
identities and the standard quartic Kummer character correspondence. No prime
number theorem, zero-free region, Siegel bound, or angular equidistribution is
needed for this upper bound. The argument does **not** assert convergence of the
partial Euler products; uniform boundedness is sufficient. Its application to
the full powerful-number sumset is in
[the quartic theorem](quartic_complement.md).

## Tracking principal constituents

Appendix D of
[third independent record](independent/quartic_analytic_architecture.md)
reproduces the uniform modulus, lattice cancellation and positive-factor
argument above, and adds a useful bound without the regularity hypotheses. Put
$R=\operatorname{rad}(D)$ and let $m$ count the principal constituents among the
one rational quadratic character and nine finite Gaussian characters in (5),
with multiplicity. The infinity-type-two character is never principal, so
$0\le m\le10$. Then

$$
\prod_{\substack{2<p\le Z\\p\nmid D}}\rho_p(0;d)
\ll [\log(3R)]^{11-m}[\log(2Z)]^m.
\tag{11}
$$

Each nonprincipal constituent has the previously proved upper bound
$\log\log(3R)+O(1)$ for its prime sum. For a principal constituent,
bound its $L$-function by $\zeta$ or $\zeta_{\mathbb Q(i)}$;
at $\sigma=1+1/\log Z$ its logarithm is at most
$\log\log(2Z)+O(1)$. The same smoothing proves (11).
For canonical tuples, including valuation-one targets at coefficient
primes costs at most $4^{\omega(R)}$.

Here “no principal finite characters” must include the rational
quadratic constituent, not only the nine Gaussian ones. For example,
$(2^5,3^5,5^5,30^5)$ has square product and no principal Gaussian
constituent, so $m=1$, not zero. In a complementary-pair character,
at least one of the primes $2,3,5$ has argument valuation $2\pmod4$.
For a mixed character, requiring valuations zero modulo four at both
$3$ and $5$ would require the weights assigned to each of coordinates
two and three to complement the weight at coordinate four to four;
the pattern $(2,2,1,3)$ has insufficient repeated weights for this.
Thus none of those Gaussian characters is principal.

Appendix G's additional lower-Hecke-$L$ route is not needed for (11)
or for the [universal selector](quartic_universal_selector.md): the
baseline always has positive $L$-powers, and the selector needs only
the rational quadratic two-sided estimate. No lower Gaussian
$L$-bound is being assumed in either completion.
