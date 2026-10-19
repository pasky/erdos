---
name: research/smooth_successor_estimates/classical_inputs
title: Section 2 inputs consumed by the successor extraction
desc: |
  The exact Section 2 consumption of the successor extraction and the signed
  Type II estimate: the classical theorems used in standard form (prime number
  theorem, Mertens, Siegel-Walfisz, the multiplicative large sieve), the
  derived divisor moments and Fourier separation, and the Type I
  large-sieve application written out with its parameter order.
created: 2026-10-15T15:28:45Z
updated: 2026-10-15T15:28:45Z
---

# Section 2 inputs consumed by the successor extraction

***

This page records which estimates of Section 2 of the
[[../library/arithmetic_functions/openai_2026_weighted_dilation_graphs_smooth_shifted_primes_totient_fibers/_index|weighted-dilation manuscript]]
the [[research/smooth_successor_primes/signed_type_ii|signed Type II estimate]]
and the
[[research/smooth_successor_primes/successor_prime_extraction|extraction of primes 2u-1]]
consume, at which parameters, and how each is supplied. It belongs to the
[[research/smooth_successor_estimates/_index|elementary estimates of the smooth-successor route]].
The estimates are the manuscript's or classical; the inventory and the
derivations are Plasma AI's. The
[[research/smooth_successor_estimates/evidence/verify/elementary_estimates/_index|E5 examination]]
records **refutation-failed** relative to the stated classical premises, whose
original proofs were unread. Its [distinct whole-contract grade](evidence/verify/elementary_estimates/grade.md),
examined on 2026-10-16 UTC, is **PASS** at those exact scopes and reading
boundaries.
The [[research/erdos_824_uniformity/shift_cancellation_reconstruction|reconstruction of premise P]]
checked the Section 2 inputs used inside P's own proof; that coverage is not
relied on here, and the inputs of the extraction are listed separately.

## Classical theorems used in standard form

These are classical theorems, used as stated and not re-derived. Their
displayed statements in the cited sources supply the classical boundary;
the derived inputs and applications below do not assume the rest of the
weighted-dilation manuscript.

- **The prime number theorem**, in the form
  $\pi(y)=\mathrm{Li}(y)+O_A(y(\log y)^{-A})$ for every fixed $A>0$;
  see Terence Tao, [254A, Notes 2, Corollary 39 and Exercise 40](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/).
  It is used for prime counts in cells of relative length
  $L^{-S}$ with $A=S+2$, chosen after $S$; for last-prime counts in the
  rough-integer densities; for the free slot of the candidate; and for the
  harmonic masses of bands and groups.
- **Mertens' estimates**, $\sum_{p\le y}1/p=\log\log y+M+O(1/\log y)$ and
  $\prod_{p\le y}(1-1/p)\sim e^{-\gamma_E}/\log y$;
  see Tao, [254A, Notes 1, Theorems 15 and 26](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/).
  The **Chebyshev bound** $\sum_{y<p\le2y}1/p\ll1/\log y$, for $y\ge2$,
  follows already from $\pi(2y)/y\ll1/\log y$.
- **The Siegel–Walfisz theorem** (the manuscript's Theorem 2.2): for fixed
  $A,C$, uniformly for $(a,r)=1$ and $r\le(\log y)^C$,
  $\pi(y;r,a)=\mathrm{Li}(y)/\varphi(r)+O_{A,C}(y(\log y)^{-A})$, with
  ineffective constants. Tao's Notes 2, Exercise 64, states its
  von Mangoldt form; removing prime powers and partial summation give this
  form, with arbitrarily large fixed logarithmic accuracy.
- **The multiplicative large sieve** (the manuscript's Theorem 2.3): for
  coefficients on an interval of length $H$,
  $\sum_{f\le R}\frac f{\varphi(f)}\sum^*_{\chi\bmod f}|\sum a_n\chi(n)|^2
  \ll(H+1+R^2)\sum|a_n|^2$. This is Montgomery and Vaughan,
  [Multiplicative Number Theory II, Theorem 19.16](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf),
  enlarging a real interval to consecutive integers, at a cost of at most
  one in its length.
- **Decay of Fourier transforms** of smooth compactly supported functions,
  by integration by parts.

## Derived inputs

**Harmonic character sums** (the manuscript's Corollary 2.4) are derived from
the Siegel–Walfisz theorem on the
[[research/smooth_successor_estimates/proxy_discrepancy|proxy-discrepancy page]],
uniformly for every interval in $[\exp(L^c),x^{C_0}]$, every nonprincipal
character of modulus at most $L^B$, primitive or not, and every twist up to
$L^B$.

**The block sieve** (the manuscript's Lemma 2.9) is derived on the
[[research/smooth_successor_estimates/block_sieve|block-sieve page]], with its
five consumed instances checked.

**Divisor moments** (the manuscript's Lemma 2.5). For fixed $k\ge0$,

$$
\sum_{n\le Y}\frac{\tau(n)^k}n\le\prod_{p\le Y}\sum_{a\ge0}\frac{(a+1)^k}{p^a}
\le\prod_{p\le Y}\Bigl(1+\frac{2^k}p+\frac{c_k}{p^2}\Bigr)\ll_k(\log2Y)^{2^k},
$$

by unique factorization and Mertens, and
$\sum_{n\le Y}\tau(n)^k\le Y\sum_{n\le Y}\tau(n)^k/n$. The consumed forms follow
by Cauchy's inequality: $\sum_{u\le2x}\tau(u)\tau(2u-1)\ll xL^{O(1)}$ in the
Type II absolute bound, $\sum_{v\ll x}\tau(v)\tau(v+1)^3\ll xL^{O(1)}$ in its
diagonal, the endpoint square sums with $\tau(z_*)^4$ in its separation step,
and $\sum_{r\asymp U}b(r)^2\ll UL^{O(1)}$ for the Type I coefficients
$0\le b(r)\le L^{O(1)}\tau(r)$. The exponents depend only on $k$ and the fixed
coefficient bounds, never on later precisions.

**Fourier separation** (the manuscript's Lemma 2.8). Let $F$ be smooth on
$\mathbb R^b$, $b$ fixed, supported in a fixed box, with $j$-th derivatives
$O_j(L^{C(j+1)})$, with $C\ge1$ after enlargement if necessary.
Integrating by parts $j$ times,
$|\widehat F(\xi)|\ll_jL^{C(j+1)}(1+|\xi|)^{-j}$. With $j=b+1$ this gives
$\int|\widehat F|\ll L^{C(b+2)}$, and for $C'=2C$,

$$
\int_{|\xi|>L^{C'}}|\widehat F(\xi)|\,d\xi\ll_jL^{C(j+1)-C'(j-b)}
=L^{-Cj+C(2b+1)},
$$

which is at most $L^{-A}$ once $j\ge2b+1+A/C$. So $C'$ is fixed before the
desired saving $A$, as the Type II page requires. For a fixed smooth $\Psi$ on
$[1,2]$, Mellin inversion $\Psi(y)=\frac1{2\pi}\int\widetilde\Psi(\tau)
y^{i\tau}d\tau$ with $\widetilde\Psi$ the Fourier transform of $\Psi\circ\exp$
has $\int|\widetilde\Psi|<\infty$; this is the bounded integrated cost used in
Type I.

**Elementary sums.** Positivity and the squarefree Euler product give
$\sum_{d\le y}\mu^2(d)/\varphi(d)\le\prod_{p\le y}(1-1/p)^{-1}
\ll\log(2y)$, used for the principal character in Type I and for the
squarefree $h$-sum below. For the balanced-box remainders let
$d_3(n)=\#\{(a,b,c)\in\mathbb N^3:abc=n\}$. At each prime power
$d_3(p^a)=\binom{a+2}{2}\ge3$ for $a\ge1$, hence
$3^{\omega(n)}\le d_3(n)$ and

$$
\sum_{n\le D}3^{\omega(n)}\le\sum_{ab\le D}\left\lfloor\frac D{ab}\right\rfloor
\le D\left(\sum_{a\le D}\frac1a\right)^2
\le D(1+\log D)^2.
$$

In particular both $\sum_{d\le D}\nu(d)/d$ and
$D^{-1}\sum_{d\le D}\nu(d)$ are $O(D(1+\log D)^2)$ whenever
$0\le\nu(d)\le d\,3^{\omega(d)}$, as in the balanced box.

## The large sieve in Type I

The Type I proposition on the extraction page is the only consumer of the
large sieve, which P does not use. Its application is checked here at the
exact parameters. Fix $\vartheta<1/2$ and $D>0$. After extracting the first
slot $p\in\mathcal Q_0$ of band $0$, $A(u)=\sum_{pr=u}b(r)$ with
$0\le b(r)\le L^{c_b}\tau(r)$, $c_b$ depending only on the candidate. As
$\mathcal Q_0\subset[x^{c_1s'},x^{c_2s'}]$ and $c_2s'<1/4$, every contributing
dyad pair $p\asymp P$, $r\asymp U$ has $PU\asymp x$ and
$x^{a_0}\ll P,U\ll x^{1-a_0}$ with $a_0=c_1s'$. A nonprincipal character
modulo squarefree odd $d=hf$ is the primitive $\chi^*\bmod f>1$ together with
coprimality to $h$, and $\varphi(d)=\varphi(h)\varphi(f)$.

Fix $c'$ large enough, in terms of the early candidate choices, that the
divisor moments give both $\sum_{r\asymp U}b(r)\ll UL^{c'}$ and
$\sum_{r\asymp U}b(r)^2\ll UL^{c'}$. The parameter $c'$ precedes $D,C'$
and all proxy choices.

*Large conductors.* For $R/2<f\le R$ with $R>L^{C'}$, separate $\Psi(pr/x)$ by
Mellin inversion. For each $\tau$ put $a_p=\mathbf 1_{(p,h)=1}p^{i\tau}$ on the
dyad and $b'_r=b(r)\mathbf 1_{(r,h)=1}r^{i\tau}$. Since
$1/\varphi(f)\le(2/R)f/\varphi(f)$, Cauchy's inequality and the large sieve give

$$
\sum_{R/2<f\le R}\frac1{\varphi(f)}\sum^*_{\chi\bmod f}
\Bigl|\sum_pa_p\chi(p)\Bigr|\Bigl|\sum_rb'_r\chi(r)\Bigr|
\ll\frac1R\bigl((P+1+R^2)P\cdot(U+1+R^2)UL^{c'}\bigr)^{1/2},
$$

with $c'$ from the divisor moments. With $PU\asymp x$ this is
$\ll xL^{c'/2}(R^{-1}+P^{-1/2}+U^{-1/2}+R/\sqrt x)$. Summing over the
$O(L)$ dyadic $R\in(L^{C'},x^\vartheta]$, over squarefree $h\le x^\vartheta$
with weight $1/\varphi(h)$ (total $O(L)$), over the $O(L^2)$ dyad pairs and over $\tau$
against $|\widetilde\Psi|$ gives
$xL^{c'/2+4}(L^{-C'}+x^{-a_0/2}+x^{\vartheta-1/2})$. Choose
$C'\ge D+c'/2+4$; the restrictions $(f,h)=1$ and squarefreeness of $f$ were
dropped only to enlarge a sum of absolute values. Keeping $h$ squarefree
makes its $O(L)$ mass precisely the elementary sum proved above.

*Small conductors.* For $1<f\le L^{C'}$, fix $h$, $\chi^*$ and $r$. The primes
$p\mid h$ in $\mathcal Q_0$ are at most $\vartheta/a_0+1$ in number and cost
$\sum_rb(r)\ll x^{1-a_0}L^{c'}$ per dyad pair. For the rest, partial summation
against $y\mapsto\Psi(yr/x)$ on the dyad, whose total variation is $O(1)$
including the two cutoffs, and the bound
$\sum_{p\le y}\chi^*(p)\ll_KyL^{-K}$ give $O_K(PL^{-K})$.
For completeness, $\log y\asymp L$ at these endpoints, so
$f\le L^{C'}\le(\log y)^{2C'+1}$ eventually. Apply Siegel–Walfisz with
accuracy $K+C'+2$ and sum over at most $f\le L^{C'}$ reduced classes;
the nonprincipal main terms cancel and the resulting bound is stronger
than $O_K(yL^{-K})$. Thus the loss from residue classes is included.
Summing over $r$, the $\varphi(f)$ characters with weight $1/\varphi(f)$,
$f\le L^{C'}$, $h$ and dyads gives $\ll xL^{c'+C'+3-K}+x^{1-a_0}L^{c'+C'+3}$.
Choose $K\ge D+c'+C'+3$ after $C'$.

For the principal character, replacing its coprimality-restricted mass by
$X_A$ costs at most

$$
X_A\max_{u\le2x,\ A(u)>0}
\sum_{l\mid u}\frac1{l-1}
\sum_{d'\le x}\frac{\mu^2(d')}{\varphi(d')}
\ll X_A\frac{L}{\log L}L^{-20}L
\ll X_AL^{-18}.
$$

Here $l$ is prime, every such $l$ is at least $L^{20}$, and the divisor
sum over $d'$ bounds the original sum with $(d',l)=1$ dropped. With the
nonprincipal estimates this proves the Type I bound
$\sum_{d\le x^\vartheta}|r(d)|\ll xL^{-D}+X_AL^{-18}$ for odd squarefree $d$.
The order is $D$, then $C'$, then the Siegel–Walfisz exponent $K$; none
depends on $\kappa$ beyond $\vartheta=1/2-\kappa/2<1/2$, and none on $S$.

## Consumption by step

| Step | Inputs | Parameters |
| --- | --- | --- |
| Type II, absolute bounds and diagonal | divisor moments | $k\le6$ |
| Type II, splitting and separation | Fourier separation | $b\le3$, frequencies $L^{O(1)}$ |
| Type I | Mertens, Mellin, large sieve, divisor moments, Siegel–Walfisz | $\vartheta<1/2$, $R\le x^\vartheta$ |
| Preliminary sieve | block sieve, Type I, Mertens | $z=x^{b_1}$, $h=2\lfloor1/(40b_1)\rfloor$ |
| Proxy discrepancy | block sieve, Siegel–Walfisz | $z=W$, $h=2\lceil T^2\rceil$, $r,\lvert t\rvert\le L^B$ |
| Densities and (7.19) | prime number theorem, Mertens, block sieve | $A=S+2$; $z=x^{b_1}$ |
| Composite subtraction | Type II, (7.17), block sieve, Type I | $z=W$, products below $x^{1/2-\kappa+o(1)}$ |
| Balanced box | (7.16), block sieve, lattice counts, candidate mass | $h=2$, $z=x^\theta$ |
| Candidate and final count | prime number theorem, Mertens, Chebyshev | band and group masses |

No step consumes the mean-square lemma (Lemma 2.6), the derivative tests
(Lemma 2.7) or the rough-integer polynomial (Corollary 2.10); those enter only
P's own proof.
