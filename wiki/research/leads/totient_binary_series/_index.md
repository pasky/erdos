---
name: research/leads/totient_binary_series
title: The Binary Totient Series and Its Tail Arithmetic
desc: |
  Editable sketch for Problem 249: exact tail integers, a 2-adic valuation
  criterion and its dyadic rung, the rigidity of progression certificates,
  arithmetic progression means, and integer interpolation with an explicit
  remaining bound for the infinite binary tail.
tags: []
sources:
- problems/irrationality/E0249
problems:
- 249
research_state: ready
review_status: needs_update
created: 2026-09-17T04:06:03Z
updated: 2026-10-19T04:19:07Z
---

# The Binary Totient Series and Its Tail Arithmetic

[[research/leads/_index|..]]

[[research/leads/totient_binary_series/analytic_sources|analytic_sources]]: Non-Mahler specialization, a positive-density obstruction to fixed dyadic
filters, and transcendental sparse orbit sums with an explicit transfer gap.

[[research/leads/totient_binary_series/arithmetical_windows/_index|arithmetical_windows/]]: Isolating one totient term bounds every progression-wide valuation
certificate, including cancellation, while leaving selected arithmetic
subfamilies open.

[[research/leads/totient_binary_series/coefficient_growth_obstruction|coefficient_growth_obstruction]]: The original totient coefficients violate the mean-growth hypothesis in
Duverney–Tachiya's criterion, leaving transformed coefficients open.

[[research/leads/totient_binary_series/dilation_cube|dilation_cube]]: Exact totient dilation cubes, their common-divisor normalization and
complete averaged error bound, with a missing phase estimate, a bounded
coincidence obstruction, and a positive-tail obstruction for cofactors k.

[[research/leads/totient_binary_series/evidence/_index|evidence/]]: Exploratory recomputation of the 2-adic tail valuations through ten
million, the excess-positive indices and a coarse progression-certificate
filter, the one-large-prime windows, and a certified
continued-fraction prefix of the binary totient series, with fixed finite
expectations.

[[research/leads/totient_binary_series/integer_interpolation/_index|integer_interpolation/]]: Normalized shifted-totient vectors span the full integer lattice beyond
every cutoff, giving finite two-sided gap multipliers at every order;
a weighted coefficient bound for their complete tails remains open.

[[research/leads/totient_binary_series/progression_means|progression_means]]: Fresh-prime refinements separate nonzero absolutely summable kernels of
normalized shifted totients; fixed dilation grids have a precise
noncancellation result and explicit bounds for their full signed tails.

[[research/leads/totient_binary_series/sparse_transforms/_index|sparse_transforms/]]: Reduced-denominator obstruction for literal prime-sieve approximants,
limits of logarithmic products, and integer multipliers with explicit gaps.

[[research/leads/totient_binary_series/window_cost|window_cost]]: Modulus bounds for termwise divisibility on whole progressions, with
explicit limits on their implications for selected representatives.

***

This lead's notes that cite no source are author-recorded research, not claims.

## Target and standing

[[problems/irrationality/E0249/_index|Problem 249]], in the erdosproblems.com
formulation accessed, asks whether

$$
S=\sum_{n\ge1}\frac{\varphi(n)}{2^n}
$$

is irrational, $\varphi$ being Euler's totient. The series converges
absolutely since $\varphi(n)\le n$, and $S=1.367630801985\ldots$; the finite
observations below certify this prefix. The problem page carries the dated
status search. This page is the project's editable proof sketch. It contains
no proof or disproof of the target. Its held links are the integer tails
forced by a rational value, a sufficient 2-adic criterion, and the precisely
scoped statements below. The original research arguments are author-recorded;
their review standing is stated under Current review. The cited Duverney
extraction has separate focused statement-fidelity acceptance, as described
in its source home.
The kernel separation theorem is
filed as [[theory/irrationality/L16_totient_kernel_separation/_index|L16]]
at tier 0, which records its complete author proof without independent
acceptance. The remaining research arguments have no assigned native tier.

The
[[research/totient_binary_new_attack/proof_sketch|kernel and comparison sketch]]
uses the complete-tail criterion and distinguishes scalar cancellation from
cancellation valid for every function obeying fixed-prime totient laws.
[[theory/irrationality/L220_partial_multiplicativity_interval/_index|L220's rational comparisons]]
give an exponential lower bound for the latter class on supports of any
length, with a sufficiently large lower cutoff. They preserve every
prime-power value but not full multiplicativity. The short-support shadow
construction supplies a quantitative sufficient phase estimate for scalar
kernels; that estimate remains unproved. These are author-recorded partial
results, not an irrationality conclusion.

The route is open. A large CRT modulus does not force a large least positive
representative, and an information-counting heuristic does not bound every
possible tail argument. The earlier purported obstruction to all
single-index methods is withdrawn; the
[[research/leads/totient_binary_series/window_cost|modulus bounds]] retain only
their actual quantifiers. The next construction must either exhibit the
large valuations in Proposition 3, give a separated rational-tail
certificate, or produce a different contradiction from rationality. The
weakest rung of the criterion, that $S$ is not a dyadic rational, needs
only infinitely many indices with $2^{v_2(\Phi_N)}>N+2$. The classification
below rules out delivering such a family by eventual divisibility
assertions on entire progressions. The finite
one-large-prime window scan describes another particular construction;
it is not an exhaustive model of arithmetic information.

A constructive link exists:
[[research/leads/totient_binary_series/integer_interpolation/_index|normalized shifted-totient vectors span the full integer lattice]]
beyond every fixed cutoff. Thus a prescribed two-sided gap multiplier with
leading coefficient two and central coefficient zero exists at every order.
The proof does not bound its support or coefficients. An effective bound,
$\exp(O(k^2\log(k+2)))$ by Linnik's theorem, is on the
[[research/leads/totient_binary_series/integer_interpolation/geometry|geometry
page]]; it is too large to use. The explicit weighted
cost in that page controls its entire infinite tail; making this cost
small compared with $2^k$ remains an open quantitative question. The
[[research/leads/totient_binary_series/integer_interpolation/shadows|shadows
page]] gives a separate scalar-kernel criterion and a reverse implication
on specified growing supports; it does not prove such a reverse
implication for the original full-vector interpolation cost.
The argument and its unresolved uniformity are summarized at the end of
this sketch.

The [[research/leads/totient_binary_series/analytic_sources|analytic source tests]]
give a separate boundary and construction target. Bell--Smertnig rules out
a Mahler equation for the totient generating function, with no conclusion
about its value at one half. Kaneko--Suzuki--Tachiya applies to nonempty
finite odd-orbit subseries, but their positive omitted tails obstruct the
tested transfer to $S$. A signed sparse multiplier satisfying the exact
source hypotheses would suffice; none has been constructed.

The new [[research/leads/totient_binary_series/progression_means|progression-mean
argument]] works for infinite absolutely summable kernels, extending the
finite-support mechanism relevant to Problem 252. Thus infinite formal
support alone is no obstruction to using progression means. A missing link
remains: rationality of $S$ has not been shown to force such a nonzero
kernel to tend to zero. The same argument does rule out uniform $o(N)$
remainders for a fixed dilation grid after any fixed finite correction.
It does not address growing grids or specially selected subsequences.

## Notation and the tail integers

For $N\ge0$ put

$$
\Phi_N=\sum_{n=1}^{N}\varphi(n)\,2^{N-n}\in\mathbb Z_{\ge0},\qquad
T_N=2^NS-\Phi_N=\sum_{j\ge1}\frac{\varphi(N+j)}{2^{j}}>0 .
$$

Then $\Phi_0=0$, $T_0=S$, and for $N\ge1$

$$
\Phi_N=2\Phi_{N-1}+\varphi(N),\qquad T_{N}=2T_{N-1}-\varphi(N).
$$

Since $\varphi(n)\le n$ and $\sum_{j\ge1}j2^{-j}=2$,

$$
0<T_N\le\sum_{j\ge1}\frac{N+j}{2^j}=N+2 .
$$

**Lemma 1 (tail integers).** Suppose $S=a/b$ with integers $a$ and $b\ge1$.
Put $I_N=a2^N-b\Phi_N$. Then $I_N=bT_N$ is an integer with
$1\le I_N\le b(N+2)$, and $I_N=2I_{N-1}-b\varphi(N)$ for $N\ge1$.

*Proof.* $I_N=b(2^NS-\Phi_N)=bT_N$; the bounds are those of $T_N$ times $b$,
and $I_N\ge1$ because it is a positive integer. The recurrence is $b$ times
the recurrence of $T_N$. $\square$

Every integer combination $\sum_Nc_NI_N$ equals
$a\sum_Nc_N2^N-b\sum_Nc_N\Phi_N$, so this algebraic identity alone gives no contradiction. Arithmetic
estimates on a suitably chosen combination could still be useful.
Conversely the recurrence shows that integrality of every $I_N$
is equivalent to integrality of $I_0=bS$.

**Lemma 2 (residue formula).** For $0\le m\le N$ let
$\Phi_{N,m}=\sum_{i=0}^{m-1}2^{i}\varphi(N-i)$, so that
$\Phi_N=2^m\Phi_{N-m}+\Phi_{N,m}$. If $S=a/b$, then

$$
I_N=2^{m}I_{N-m}-b\,\Phi_{N,m},\qquad\text{hence}\qquad
I_N\equiv-b\,\Phi_{N,m}\pmod{2^{m}} .
$$

*Proof.* Induction on $m$ from $I_N=2I_{N-1}-b\varphi(N)$: if the identity
holds for $m$, substitute $I_{N-m}=2I_{N-m-1}-b\varphi(N-m)$. $\square$

So a rational value forces, for all $N$ and all $m\le N$ with
$2^m>b(N+2)$, that the residue $-b\Phi_{N,m}\bmod2^m$ lies in the short initial
interval $[1,b(N+2)]$: the last $m$ values of $\varphi$ determine $I_N$ modulo
$2^m$, while the future values determine its size.

**Proposition 3 (valuation bound under rationality).** If $S=a/b$ with
$b\ge1$, then $v_2(\Phi_N)\le\log_2\bigl(b(N+2)\bigr)$ for every $N\ge4$.
Consequently $S$ is irrational as soon as

$$
\sup_{N\ge4}\bigl(v_2(\Phi_N)-\log_2 N\bigr)=+\infty .
$$

*Proof.* For $N\ge4$ the partial sum $\Phi_N/2^N$ lies strictly between $1$
and $S$, since it equals $9/8$ at $N=4$ and increases, and $S<2$ because
$\varphi(n)\le n$ with strict inequality at $n=3$. So $2^N<\Phi_N<2^{N+1}$
and $m:=v_2(\Phi_N)\le N-1$. By $\Phi_N=2^m\Phi_{N-m}+\Phi_{N,m}$, $2^m$
divides $\Phi_{N,m}$, and Lemma 2 gives $2^m\mid I_N$. As $I_N\ge1$,
$2^m\le I_N\le b(N+2)$. For the second statement, a rational value with
denominator $b$ would bound the supremum by $\log_2(3b)$. $\square$

**Proposition 3′ (odd-part bound).** If $S=a/b$ with $b=2^{v}b'$ and $b'$
odd, then $v_2(\Phi_N)\le\log_2\bigl(b'(N+2)\bigr)$ for every $N$ with
$2^N>b(N+2)$.

*Proof.* By Lemma 1, $1\le I_N\le b(N+2)<2^N$, so
$v_2(I_N)\le\log_2(b(N+2))<N\le v_2(a2^N)$. Hence
$v_2(b\Phi_N)=v_2(a2^N-I_N)=v_2(I_N)$, that is
$v+v_2(\Phi_N)\le\log_2(b(N+2))=v+\log_2(b'(N+2))$. $\square$

The criterion therefore measures only the odd part of the denominator. One
index $N$ with $2^{v_2(\Phi_N)}>b'(N+2)$ excludes every denominator
$2^{v}b'$ with $2^{v}<2^N/(b'(N+2))$; infinitely many such indices exclude
the odd part $b'$ outright, and unbounded excess excludes every $b'$. The
natural ladder of sub-targets is $b'=1,3,5,\dots$; its first rung is the
dyadic sub-target treated after the tail certificate below.

**Carry dynamics.** For $N\ge2$ write $a_N=v_2(\Phi_N)$ and
$u_N=v_2(\varphi(N))$. If $u_N\ne1+a_{N-1}$ then
$a_N=\min(u_N,1+a_{N-1})$. If $u_N=1+a_{N-1}=u$, write
$\Phi_{N-1}=2^{u-1}x$ and $\varphi(N)=2^uy$ with $x,y$ odd. Then
$a_N=u+v_2(x+y)\ge u+1$. Large excess in this case asks for
$x\equiv-y\pmod{2^h}$, not equality of the odd parts. This exact recurrence
supplies a search criterion; it is not a distribution theorem.

In fact every $N\ge2$ with $a_N\ge\log_2N$ must be a carry tie:
$2^{u_N}\le\varphi(N)<N$, so $u_N<\log_2N\le a_N$, whereas the
non-tie case would give $a_N\le u_N$. Thus termwise clearing of the
whole window to $m\ge\log_2N$ cannot witness this criterion, even at an
exceptional representative: already its first term $\varphi(N)$ is too
small. Arithmetic cancellation remains the constructive question.

## A sufficient tail certificate and its actual limitation

For any $b\ge1$, one index $N$ with $bT_N\notin\mathbb Z$ excludes that
particular denominator. A sufficient certificate is an approximation
$B_N$ and a bound $|T_N-B_N|\le\varepsilon_N$ with
$\operatorname{dist}(bB_N,\mathbb Z)>b\varepsilon_N$. Errors can be bounded
jointly; it is not necessary to know the factorization of each term.

If one simply drops the positive tail after $H$, then, for $N\ge2$,

$$
\frac{N}{1+\log_2N}\,2^{-H}
\ \le\ \sum_{j>H}\frac{\varphi(N+j)}{2^j}
\ \le\ (N+H+2)2^{-H}.
$$

For the lower bound, order the $r=\omega(n)$ distinct prime divisors as
$p_1<\cdots<p_r$. Since $p_i\ge i+1$,
$\varphi(n)/n\ge\prod_{i=1}^r i/(i+1)=1/(r+1)$, and
$r\le\log_2n$. The function $x/(1+\log_2x)$ increases for $x\ge2$, so sum
this lower bound over $N+j$. The upper bound follows from $\varphi(n)\le n$.
Consequently this particular discarded tail can be below $1/b$ only if
$H>\log_2(bN)-\log_2(1+\log_2N)$. Cancellation, analytic tail subtraction,
and a selected growing family are not covered by that conclusion.

The [[research/leads/totient_binary_series/window_cost|window page]] proves a
lower bound on a modulus that forces termwise divisibility at every large
member of a progression. It does not bound the least representative or
establish a necessary information budget for a proof. A carry coincidence
can also make a weighted sum divisible without termwise divisibility.

## The dyadic rung and what a progression can certify

**Lemma D (dyadic reduction).** If $S=a/2^{v}$ with $a\in\mathbb Z$ and
$v\ge0$, then $2^{v_2(\Phi_N)}\le N+2$ for every $N$ with
$N-v>\log_2(N+2)$. Consequently $S\notin\mathbb Z[1/2]$ as soon as
$2^{v_2(\Phi_N)}>N+2$ for infinitely many $N$.

*Proof.* This is Proposition 3′ with $b'=1$, whose hypothesis
$2^N>2^{v}(N+2)$ is $N-v>\log_2(N+2)$. An index with
$2^{v_2(\Phi_N)}>N+2$ therefore forces $v\ge N-\log_2(N+2)$, and infinitely
many such indices exclude every $v$. $\square$

Call $N$ *excess-positive* when $2^{v_2(\Phi_N)}>N+2$. Unlike the criterion
of Proposition 3, the dyadic rung needs no growth of the excess, only
infinitely many excess-positive indices. The
[[research/leads/totient_binary_series/evidence/_index|finite evidence]] finds
$71$ of them in $16\le N\le10^7$, besides $N=3,5,10$, which are checked by
hand from $\Phi_3=8$, $\Phi_5=40$ and $\Phi_{10}=1392$; the largest record,
$N=2786632$ with $v_2(\Phi_N)=29$, excludes every $v\le2786610$. Whether
the binary expansion of $S$ terminates is thus the weakest rung of the
ladder and strictly weaker than the target. We know of no proof of it, and
none of the sources read for this page settles it; the finite exclusions
here and the Farey exclusion reported on the Plectis page cover only
bounded $v$. The evidence's valuation distribution, roughly
$P(v_2(\Phi_N)\ge k)\approx10\cdot2^{-k}$ for $k\ge6$, would predict about
five excess-positive indices in each dyadic block of $N$; the observed
blocks through $10^7$ hold between zero and ten, 71 in all. Both figures
are observations, not theorems.

One proposed construction would prove $2^m\mid\Phi_N$ for every
sufficiently large member of a progression and also establish that
divisibility at a representative $n<2^m-2$. The eventual assertion
alone does not supply divisibility at a representative below its
threshold. The following results keep both quantifiers explicit.

**Lemma R (progression certificate bounds).** Suppose $m,M\ge1$ and
$2^m\mid\Phi_N$ for every sufficiently large $N\equiv r\pmod M$.
For every positive representative $n$,

$$
2^m\le\min\{4\varphi(\gcd(n,M)),\,2\varphi(n)\}.
$$

More precisely, for $0\le i<m$ with $n-i>0$,

$$
m\le i+v_2(\varphi(n-i))+1.
$$

The [[research/leads/totient_binary_series/arithmetical_windows/_index|isolation
argument]] proves the separate forced-gcd bound in Corollary 3 and the
sharper representative bound by prime-square isolation in Theorem 4.
Its prime and semiprime construction uses Dirichlet's theorem; the
prime-square refinement additionally uses quadratic reciprocity.
Both arguments allow cancellation and apply even when $n<M$ or $n$
precedes the eventual threshold. The factor four attached to the gcd
has not been replaced by two.

The [[research/leads/totient_binary_series/arithmetical_windows/classification|exact
classification]] proves two further author-recorded results. For fixed
$n\ge m$, a containing progression with the eventual divisibility
assertion exists if and only if all the displayed position inequalities
hold. If actual $2^m\mid\Phi_n$ and excess $2^m>n+2$ are also required,
the only pair is $(n,m)=(5,3)$, realized by $5\pmod{200}$. The proof
handles arbitrary possible Fermat primes; it does not assume the known
list is complete. Thus this particular whole-progression route cannot
produce infinitely many excess-positive indices, even for the dyadic
rung.

The finite instrument retains the coarser necessary filter
$2^{v_2(\varphi(n))+2}>n+2$. Of the $71$ excess-positive indices in
$[16,10^7]$, exactly $64,204,512,1632$ meet that filter. They are
candidates only for the weaker test, and the classification rules out
every one as an excess-producing whole-progression certificate.
For example, the sharper bound at 64 is
$2^m\le2\varphi(64)=64<66$, although its actual numerator has
valuation ten. Indeed every containing class also has infinitely many
members $N=64p^2$ with valuation exactly six, by prime-square isolation.

None of these conclusions bounds the actual excess at selected indices.
Constructions using additional factorization, prime-cofactor conditions,
or other information beyond membership in a progression remain open,
as do combinations of several tails.

## Route one: Duverney's sparse product for Problem 250

[[../library/irrationality/duverney_1995_irrationalite_q_analogue_zeta_2/_index|D. Duverney,
*Irrationalité d'un q-analogue de ζ(2)*]], C. R. Acad. Sci.
Paris Sér. I Math. 321 (1995), 1287–1289, proves
[[problems/irrationality/E0250/_index|Problem 250]] for every integer base $q$ with
$|q|\ge2$. All three page images of the published note (the author's scan read
for the library card) were read; the library retains its exact unnumbered
theorem and lemma, with
[[../library/irrationality/duverney_1995_irrationalite_q_analogue_zeta_2/evidence/verify/statement_fidelity/_index|accepted independent statement-fidelity review]]
of the extraction and exact sigma-series application. Complete rewritten
proofs of that theorem and lemma are filed on their library pages and were
independently reviewed (verdict refutation-failed, with a distinct passing
grade) relative to Euler's pentagonal number theorem and Duverney 1993
Théorème 2; neither that review nor the statement-fidelity verdict covers
the following author reconstruction or any totient argument. With
$f(x)=\prod_{n\ge1}(1-x^n)$ and
Euler's pentagonal expansion, the numbers $1$, $f(1/q)$, $q^{-1}f'(1/q)$
are linearly independent over $\mathbb Q$: for fixed integers $a,b$ not
both zero, $af(1/q)+bq^{-1}f'(1/q)=\sum_na(n)q^{-n}$ has integer
coefficients supported on the generalized pentagonal numbers, with
$|a(n)|\le n^2$ eventually. At the selected upper exponent
$n_k=k(3k+1)/2$, there are $k-1$ preceding zeros and at least $k$
following zeros; the lower pentagonal exponent is $n_k-k$.
The paper invokes the sparse-series criterion of its reference [3]
(Duverney 1993, not read here) for an eventually zero scaled tail, then
deduces $q^k\mid\delta a(n_k)$ against polynomial growth. The identity
$-xf'(x)/f(x)=\sum\sigma(n)x^n$ turns a rational value of
$\sum\sigma(n)q^{-n}$ into such a relation.

The required scaled-tail implication can also be checked directly here.
If the linear combination were $\eta/\delta$, then the integer

$$
J_k=\eta q^{n_k}-\delta\sum_{n\le n_k}a(n)q^{n_k-n}
   =\delta\sum_{j>k}a(n_k+j)q^{-j}
$$

satisfies, for all sufficiently large $k$,

$$
|J_k|\le |\delta|\,|q|^{-k}
 \bigl((n_k+k)^2+4(n_k+k)+6\bigr)\longrightarrow0.
$$

This uses the whole infinite tail and the exact sums of $1,l,l^2$
against $2^{-l}$ for $l\ge1$. Hence $J_k=0$ eventually. The $k-1$
preceding zeros make every earlier summand a multiple of $q^k$, so
$q^k\mid\delta a(n_k)$. But
$a(n_k)=(-1)^k(a+bn_k)$ is eventually nonzero and polynomially bounded,
which is impossible. This direct reconstruction removes the uninspected
1993 criterion as a dependency of the comparison made here; it is not
an independent review of either source or a transfer to the totient.

Two ingredients carry the argument: the target is the logarithmic
derivative of an integer-exponent product with a lacunary expansion, and a
rational value forces a $\mathbb Q$-relation among finitely many lacunary
series with common support and polynomially bounded coefficients. Neither
is available for $\varphi$. Write $A(x)=\sum_{n\ge1}\varphi(n)x^n$ and
$L(x)=\sum_{n\ge1}\varphi(n)x^n/n$, so $A=xL'$. From
$\varphi(n)/n=\sum_{d\mid n}\mu(d)/d$,

$$
L(x)=\sum_{d\ge1}\frac{\mu(d)}{d}\,\frac{x^d}{1-x^d},\qquad
\exp L(x)=\prod_{d\ge1}(1-x^d)^{-c_d},\qquad
c_d=\frac{(\mu*\mu*\mathrm{id})(d)}{d},
$$

since $-\log\prod_d(1-x^d)^{c_d}=\sum_nx^n\,n^{-1}\sum_{d\mid n}dc_d$ and
$\sum_{d\mid n}dc_d=\varphi(n)$ by Möbius inversion. Here $c_p=(p-2)/p$
and $c_{p^2}=(p-1)^2/p^2$, so $\exp L$ is not an integer-exponent product.
The coefficients of $\exp L$ are all positive, so that particular
series has no gaps. This says nothing about gaps in $\exp(-L)$ or a
transformed product. For $\Re s>2$, the Mellin transform of $A(e^{-t})$ is
$\Gamma(s)\zeta(s-1)/\zeta(s)$; this identity by itself excludes no modular
or other functional-equation construction. The
[[research/leads/totient_binary_series/analytic_sources|analytic sources
page]] checks Bell and Smertnig's 2026 theorem: $A$ is not $k$-Mahler for
any $k\ge2$; this excludes no modular or other non-Mahler
functional-equation construction.

The three Lambert-type constants can be placed in one frame. Let
$\mathsf Uf(x)=\sum_{k\ge1}f(x^k)$ on power series without constant term;
its inverse is $\mathsf U^{-1}f(x)=\sum_{k\ge1}\mu(k)f(x^k)$. With
$R(x)=x/(1-x)^2$,

$$
\sum_nd(n)x^n=\mathsf U\Bigl(\frac{x}{1-x}\Bigr),\qquad
\sum_n\sigma(n)x^n=\mathsf U(R),\qquad
A(x)=\mathsf U^{-1}(R),\qquad
\mathsf U^{-1}\Bigl(\frac{x}{1-x}\Bigr)=x .
$$

Erdős's argument for the first controls the divisor-count coefficients.
The second has a modular interpretation as well as Duverney's sparse-product
proof. The identity $\sum_{k\ge1}A(x^k)=R(x)$ retained below is exactly
$\mathsf U(A)=R$. This comparison identifies a change from $\mathsf U$
to $\mathsf U^{-1}$; it does not prove that a useful transformed product
or modular relation for $A$ is impossible.

The [[research/leads/totient_binary_series/sparse_transforms/logarithmic_products|logarithmic-product arguments]]
give two precise obstructions beyond the displayed Euler exponents.
No $g\in1+x\mathbb Z[\![x]\!]$ makes $A+xg'/g$ a polynomial. Also, for
every fixed nonzero finite rational combination $\sum_dr_dL(x^d)$
and nonzero rational function $R$ regular at zero, the coefficients
of $R\exp(\sum_dr_dL(x^d))$ have unbounded denominators. This excludes
no unrelated integer product, growing number of dilations, or rational
correction outside those hypotheses.

The [[research/leads/totient_binary_series/sparse_transforms/prime_sieve|literal
prime-sieve family]] also has an obstruction for every squarefree $Q$.
If $P\ge5$ is its largest prime factor, let

$$
M_Q=\sum_{d\mid Q}\frac{\mu(d)2^d}{(2^d-1)^2},
\qquad D_Q=\operatorname{den}(M_Q).
$$

Then $M_Q>S$ and
$D_Q(M_Q-S)>2^{2P-9}/P^2\to\infty$ as $Q\to\infty$.
The proof isolates primitive cyclotomic factors in the actual reduced
denominator and bounds the complete positive remainder. It does not
exclude signed combinations, different sieve weights, or additional
rational corrections.

The [[research/leads/totient_binary_series/sparse_transforms/gap_multipliers|gap-multiplier
criterion]] survives these obstructions. Its finite polynomial form and
the interpolation form at the end of this sketch are exactly related
by reversing the coefficients. Euler's product supplies the required
gaps for the sigma series, with a separately proved quadratic tail bound;
the totient still needs a growing family with controlled coefficient cost.
Continued-fraction statistics cannot decide whether such an identity exists.

## Route two: Erdős's arithmetic tails

[[../library/irrationality/erdos_1948_arithmetical_properties_lambert_series/_index|Erdős (1948)]],
pp. 63-66, proves irrationality of the divisor-count Lambert series in
integer bases. His CRT block forces divisibility, an average over the
progression controls a following block of length $O(\log N)$, and a crude
bound handles the far tail. The middle-block argument controls the size of
$d(n)$; a direct substitution of $\varphi(n)$ does not give the same bound.
The displayed lower bound explains why dropping a fixed positive tail for
$\varphi$ fails. It does not rule out controlling its fractional part,
subtracting a correlated main term, or constructing an exceptional small
representative of a large modulus.

There is a sharper elementary obstruction to an unmodified forward
block. Fix integers $N\ge2$, $k\ge1$, $b\ge1$, and require
$2^j\mid b\varphi(N+j)$ for every $1\le j\le k$. Then the prefix
$b\sum_{j\le k}\varphi(N+j)2^{-j}$ is integral. To make the remaining
positive tail smaller than $1/b$ using the bound above, this construction
would require $2^k>b(N+k+2)$. But its last divisibility already gives

$$
2^k\le b\varphi(N+k)<b(N+k),
$$

which contradicts that requirement. In particular the stronger block
$2^{j+1}\mid\varphi(N+j)$ cannot supply it. Thus this specific
termwise block and crude-tail certificate cannot coexist at any selected
integer, regardless of its CRT modulus. As in the backward carry-tie
argument above, this does not exclude cancellation in the block, a sharper
tail estimate, or subtraction of a correlated main term.

**One-large-prime windows.** One possible way to evaluate a finite block
is to prescribe factorizations $N+j=s_jq_j^{a_j}$, where $s_j$ has only
prime factors at most $J$ and $q_j>J$ is prime. Then
$\varphi(N+j)=\varphi(s_j)q_j^{a_j-1}(q_j-1)$; when $a_j=1$ this is
$\varphi(s_j)((N+j)/s_j-1)$. This particular factorization pattern is not
necessary for knowing a totient: fully smooth numbers and products of
several known large primes can also be evaluated exactly.

Call a window of order $J$ a *one-large-prime window* if every integer in
$N+1,\ldots,N+J$ has exactly one distinct prime factor above $J$. The
[[research/leads/totient_binary_series/evidence/_index|finite evidence]] tests
this property with $J=J_0(N)=\lceil\log_2(N+2)\rceil$, a block length
below which the crude upper bound $(N+H+2)2^{-H}$ on the discarded tail
cannot fall below one; the displayed lower bound forces only
$H>\log_2(bN)-\log_2(1+\log_2N)$. There
are $240$ such indices $1\le N\le10^7$, the last at $N=31790$, and none
with $N\ge2^{15}-1$ in this domain. The truncated-run statistic defined
in the evidence account is $20$ in the latter range. These are finite
observations about the specified pattern, with no asymptotic conclusion.

The earlier inference from this scan to exhaustion of single-index methods
is withdrawn. Specifying which small primes divide consecutive integers
usually imposes residues modulo their product; it does not automatically
impose their prime-power least common multiple. Even a modulus larger
than the permitted interval does not exclude a specially chosen member.
No general necessity theorem has been proved for these factorization
patterns, or for the amount of prime-factor information a cancellation
construction needs. Selected prime-cofactor families and carry cancellation
therefore retain an explicit construction and tail-control obligation.

The source (p. 66) explicitly lists the totient analog as unresolved.
[[../library/irrationality/erdos_1988_irrationality_certain_series_problems_results/_index|Erdős (1988)]],
p. 102, expresses doubt about his existing methods. These historical
judgments are not impossibility theorems. The remaining construction
question is to couple divisibility or carry cancellation with a uniform
bound on the full binary remainder.

## Route three: the dilation argument for Problem 252

The source is Tokengrinder, *Erdos252*, GitHub repository
`tokengr1nder/Erdos252` at commit `dc071aafce41bbae41caf4c015499db6dafafd11`
(PROOF.tex; the sections on tails, divisor phases, the dilation grid,
cancellation and CRT indices were read), announced on 8 September 2026 in
the erdosproblems.com thread for
[[problems/irrationality/E0252/_index|Problem 252]]. Its Lean development is
accepted as a full claim on
[[problems/irrationality/E0252/claims/2026_09_08_tokengrinder|the claim page]],
after this corpus rebuilt it under its pinned Lean and Mathlib, checked its
axioms, replayed it with `leanchecker --fresh` and filed a graded blind
fidelity review of its statement. The `PROOF.tex` exposition read here is not
assessed; only the structure of its argument is used. For
$\alpha_k=\sum\sigma_k(n)/n!$ it proceeds as follows. Rationality makes the
factorial tails $T_k(n)=(n-1)!\sum_{m\ge n}\sigma_k(m)/m!$ eventually
integral. The tail $T_k(n+1)$ is the finite sum
$\sum_{j=0}^k\sigma_k(n+j+1)P_{j,k+1}(n+j+1)$ plus an error
$o(1/n)$, because the factorial makes all later terms negligible. On a
residue class $N\equiv t_e\pmod{p_e^2}$ for a grid of pairwise coprime
$p_e$, multiplicativity turns $\sigma_k(p_e)\sigma_k(n_e+j+1)$ with
$n_e=(N-t_e)/p_e$ into $\sigma_k(N+s_{e,j})$, aligning all tails to shifts
of one $N$. Binomial weights in $e$ cancel the polynomial multipliers by
finite differences of order $k+1$, leaving a finite signed sum
$\sum c_{e,j}\rho_k(N+s_{e,j})$, $\rho_k(m)=\sigma_k(m)/m^k$, that must tend
to zero along the class; progression means refined at a fresh prime show it
does not.

A fixed truncation of a binary tail has an error growing with $N$, as
the elementary bound above shows. The following computation examines one
fixed-grid imitation; it does not preclude growing grids or other
representations.

**Proposition 4.** Let $E$ be a finite set, $p_e\ge2$ pairwise distinct
integers, $0\le t_e<p_e$, and $w_e\in\mathbb Z$ not all zero. For $N$ with
$N\equiv t_e\pmod{p_e}$ for all $e$ and $N>2\max_ep_e$, put
$n_e=(N-t_e)/p_e$ and

$$
\Lambda(N)=\sum_{e\in E}w_e\,\varphi(p_e)\,T_{n_e}
=\sum_{s\ge1}A_N(s)\,\varphi(N+s),
\qquad
A_N(s)=\sum_{e:\ p_e\mid s+t_e}
 w_e\,c_{e,s}\,2^{-(s+t_e)/p_e},
$$

where $c_{e,s}=\varphi(g)/g$ with
$g=\gcd(p_e,(N+s)/p_e)$, so
$\varphi(p_e)/p_e\le c_{e,s}\le1$. Let $e^{*}$ maximize $p_e$ among the $e$
with $w_e\ne0$, and write $p=p_{e^*}$, $t=t_{e^*}$. Then there is $s_0$,
depending only on the data $(p_e,t_e,w_e)$, such that for every $s\ge s_0$
with $s\equiv-t\pmod p$,

$$
|A_N(s)|\ \ge\ \tfrac12\,\frac{\varphi(p)}{p}\,2^{-(s+t)/p}>0 ,
$$

uniformly in $N$. In particular this coefficient expansion has infinitely
many nonzero coefficients. This alone is not a claim of functional independence of the
shifted totients. If $S=a/b$ then $b\Lambda(N)\in\mathbb Z$.

*Proof.* The expansion follows from
$\varphi(p_e)\varphi(m)=\varphi(p_em)\,\varphi(g)/g$ for $g=\gcd(p_e,m)$,
applied to $m=n_e+j$ and $p_e(n_e+j)=N+jp_e-t_e$, with $s=jp_e-t_e\ge1$
because $t_e<p_e$. Fix $s\equiv-t\pmod p$. The $e^{*}$ term has absolute
value at least $(\varphi(p)/p)2^{-(s+t)/p}$. Every other contributing $e$
has $p_e\le p-1$ and contributes at most
$|w_e|2^{-s/p_e}\le|w_e|2^{-s/(p-1)}$. The ratio of the sum of these to the
$e^{*}$ term is at most $C\,2^{-s/(p(p-1))}$ with
$C=(p/\varphi(p))2^{t/p}\sum_{e\ne e^*}|w_e|$, which is below $1/2$ for
all sufficiently large $s$ (if $C=0$, there are no competing terms).
Integrality of $b\Lambda(N)$ is Lemma 1 applied
at each $n_e$. $\square$

**What follows analytically.** Restrict to a fixed compatible progression
whose modulus is divisible by every $p_e^2$. Then $A_N(s)$ is independent
of $N$ on that progression. It has an absolutely summable first moment and
infinitely many nonzero entries. The
[[research/leads/totient_binary_series/progression_means|progression-mean theorem]]
therefore proves that subtracting any fixed finite linear combination of
$\varphi(N+s)$ from $\Lambda(N)$ cannot leave $o(N)$ uniformly on that
whole progression. Its proof uses arithmetic means, not coefficient
support alone. This excludes that precise fixed-grid uniform reduction;
it leaves growing grids, arbitrary growing corrections, and selected
subsequences open.
The same page gives an explicit progression-mean error bound in the
modulus, kernel cutoff and sampling interval. It supplies a quantitative
test for proposed parameter families, while still requiring one kernel
to be held fixed throughout each sample interval.

For the particular correction that takes the first $H$ coefficients
$A_N(s)$, the same page proves an explicit bound for the entire signed
remainder. If $p$ is the largest active dilation and
$H=\lceil c\log_2N\rceil$ with fixed $c>0$, its magnitude tends to
infinity when $c<p$, whereas it tends to zero when $c>p$. The slower
decay of the largest dilation dominates all other terms in the former
case. At $c=p$, freezing the cutoff on intervals
$2^k<N\le2^{k+1/p}$ and applying the explicit progression-mean error
bound gives a positive limsup on every fixed compatible progression.
Thus $c>p$ is necessary and sufficient for this particular truncation's
remainder to tend to zero along a whole progression. Arithmetic separation
of the finite prefix from the rationality lattice, exceptional
subsequences, and other corrections remain unresolved.

For comparison, the factorial cousin $\sum_{n\ge1}\varphi(n)/n!$ is
irrational by the following elementary argument. It illustrates the
stronger tail decay supplied by factorial denominators. If it equaled
$a/b$, then for $n\ge b$ the number
$R_n=n!\sum_{m>n}\varphi(m)/m!$ would be an integer. Take $n+1=p$ an odd
prime with $p>b$: then $R_n\ge\varphi(p)/p=1-1/p$, while
$\varphi(p+1)\le(p+1)/2$ and $\varphi(m)\le m$ for $m\ge p+2$ give
$R_n\le1-1/p+1/(2p)+5/(4p(p+1))<1$. This elementary observation is
presumably classical.

## Exact identities retained for later use

The following hold for $|x|<1$ and are one-line Möbius inversions from
$\sum_{d\mid n}\varphi(d)=n$ and $\varphi=\mu*\mathrm{id}$:

$$
A(x)=\sum_{d\ge1}\mu(d)\frac{x^d}{(1-x^d)^2},\qquad
\sum_{k\ge1}A(x^k)=\frac{x}{(1-x)^2},\qquad
S=\frac12+\sum_{d\ge1}\frac{\mu(d)}{(2^d-1)^2}.
$$

At $x=1/2$ the second identity reads $\sum_{k\ge1}A(2^{-k})=2$; it is the
generating-function form of $\sum_{n}\varphi(n)/(2^n-1)=2$ and expresses
$2-S$ as the cototient series $\sum_n(n-\varphi(n))2^{-n}$. The third
identity exhibits $S$ as the Möbius twist of
$\sum_d2^d/(2^d-1)^2=\sum\sigma(n)2^{-n}$, the constant of Problem 250: the
two problems differ only by the factor $\mu(d)$.

For a prime $p$ let $A_{(p)}(x)=\sum_{p\mid n}\varphi(n)x^n$. Since
$\varphi(pn)$ equals $(p-1)\varphi(n)$ or $p\varphi(n)$ according as
$p\nmid n$ or $p\mid n$,

$$
A_{(p)}(x)=(p-1)A(x^p)+A_{(p)}(x^p)=(p-1)\sum_{k\ge1}A(x^{p^k}),
$$

so the even-indexed part of $S$ is $\sum_{k\ge1}A(2^{-2^k})$. The identity
is recorded for possible use in a dilation or sparse-transform argument; no
consequence is drawn from it here.

**Lemma 5 (Möbius form of the tail).** For $N\ge0$ write $N=dK_d+r_d$ with
$0\le r_d<d$. Then

$$
T_N=\sum_{d\ge1}\mu(d)\,2^{r_d}
 \left(\frac{K_d+1}{2^d-1}+\frac1{(2^d-1)^2}\right),
$$

the series converging absolutely.

*Proof.* $T_N=\sum_{n>N}2^{N-n}\sum_{d\mid n}\mu(d)\,n/d
=\sum_d\mu(d)\sum_{k:\,dk>N}k\,2^{N-dk}$, the rearrangement being justified
by absolute convergence of $\sum_{d,k}k2^{N-dk}$. Since $dk>N$ exactly when
$k\ge K_d+1$,

$$
\sum_{k\ge K_d+1}k\,2^{N-dk}
=2^{r_d-d}\sum_{l\ge0}(K_d+1+l)2^{-dl}
=2^{r_d}\left(\frac{K_d+1}{2^d-1}+\frac1{(2^d-1)^2}\right). \qquad\square
$$

At $N=0$ this is the third identity above. Each term has an odd
denominator, and the terms with $d>N$ sum to
$2^N\sum_{d>N}\mu(d)2^d/(2^d-1)^2$, which the elementary absolute-value
bound controls only by $O(1)$; no small-error localization has been obtained
here. The identity is recorded because it makes the dependence
of $T_N$ on the residues $N\bmod d$ explicit.

**Observation (two-adic mirror).** The rational terms
$\mu(d)2^d/(2^d-1)^2$ also converge in $\mathbb Z_2$, where
$2^d/(1-2^d)^2=\sum_{k\ge1}k2^{dk}$, so their two-adic sum is
$\sum_{n\ge1}\varphi(n)2^n$. The real and two-adic limits are different
objects; no equality between them is asserted. A crude common denominator
for the first $D$ terms has logarithm $O(D^2)$, whereas the real truncation
error is $O(2^{-D})$. Those estimates alone yield no irrationality result;
possible denominator cancellation or stronger approximants remain open.

## Finite observations

The [evidence entry point](evidence/main.py), described in
[[research/leads/totient_binary_series/evidence/_index|the evidence account]],
recomputes $v_2(\Phi_N)$ for $N\le10^7$, counts excess-positive indices
and one-large-prime windows, and certifies a prefix of the continued
fraction of $S$. It has a fixed finite domain.

- Over $16\le N\le10^7$, the excess $v_2(\Phi_N)-\log_2N$ reaches at least
  $0,1,2,3$ at $72,45,21,9$ indices respectively. Record pairs
  $(N,v_2(\Phi_N))$ are $(16,4),(28,6),(64,10),(88,12),
  (2146743,28),(2786632,29)$. Each recorded transition is a carry tie.
  These facts do not imply unbounded excess or a law for the frequency.
- There are $71$ excess-positive indices, $2^{v_2(\Phi_N)}>N+2$, in
  $16\le N\le10^7$; exactly four of them, $64,204,512,1632$, satisfy the
  necessary condition $2^{v_2(\varphi(N))+2}>N+2$ of Lemma R. The count
  does not show that there are infinitely many.
- Exactly $240$ indices $N\le10^7$ have a one-large-prime window of length
  $\lceil\log_2(N+2)\rceil$, the last being $N=31790$; the truncated-run statistic over
  $2^{15}-1\le N\le10^7$ is $20$. This concerns the range checked only.
- Any rational value $S=a/b$ has a denominator with at least $6018$
  decimal digits, subject to the author-recorded finite computation and
  its cylinder argument in the evidence account. The bounds at $M=40000$
  share $11759$ partial quotients. This is a finite exclusion; it leaves
  all larger denominators and irrationality unresolved.
- The script also prints descriptive partial-quotient statistics. No
  probabilistic conclusion or exclusion of hidden identities is drawn
  from them.

Separately, the
[[research/leads/totient_binary_series/integer_interpolation/computation|interpolation
certificates]] establish the least full-integer-image endpoint at each
of $k=3,4,8,12,16,24,32,48,64$ and retain 36 central-zero target
solutions. At $k=64$, one has cost $2433103$ and normalized full-tail
bound $2433103/2^{64}$. These are feasible costs, not certified minima
or an asymptotic estimate. They quantify the construction below without
improving the continued-fraction denominator exclusion above.

## Prior work and reading limits

The [Plectis author page](https://wcook04.github.io/plectis/maths/problems/erdos_249.html)
and [issue 5037](https://github.com/google-deepmind/formal-conjectures/issues/5037)
were inspected in the status search. They explicitly leave the target
unresolved while reporting finite exclusions, kernel-rank statements and
conditional reductions. Their complete proofs have not been examined here,
and none receives native verification standing by citation. The exact
relation of their methods to the present reductions remains a reading task.

[[../library/irrationality/kaneko_2026_refinements_erdos_s_irrationality_criterion_certain/_index|Kaneko, Suzuki and Tachiya (2026)]]
treat, among other series, one with $\varphi(n)$ in the exponent rather
than the numerator. That displayed application is a different target.
Duverney's 1995 note was read visually in full during source preparation;
its 1993 cited criterion and Nesterenko's 1996 transcendence argument have
not been read in full here. The #252 manuscript is an identified argument
source, with its checking level stated above.

## Current review

Needs update. The prime-dilation and alternating-cube paragraph and the
page it links are unreviewed; the retained review below has its stated
scope. The route was first reviewed blind as it stood on 2026-10-03; no
earlier review of it exists. The subject was an extraction of this page on that
date, with its lead fields and its review-report sentences removed, kept outside
the repository; the reviewer, an independent reviewer in a fresh context charged
to refute, also read the folder's mathematical subpages, evidence pages and
retained assets and the cited library result pages from the tree of that date,
reran the folder's evidence programs, and recomputed the valuation census, the
one-large-prime window census, the continued-fraction prefix, the classification
search, the retained certificates and witnesses and the exact identities by
structurally different routes. The review is the record
[[research/leads/totient_binary_series/evidence/verify/lead_totient_binary_series_review|the blind review]],
graded by a distinct grader in
[[research/leads/totient_binary_series/evidence/verify/lead_totient_binary_series_review_grade|the grade]],
which records pass. The graded verdicts of the statements the route rests on,
each re-derived by the grader, whose own code recomputed the same figures: the
tail integers and the residue formula; the valuation criterion with its odd-part
and dyadic forms and the carry dynamics; the sufficient tail certificate, the
two-sided bound on a dropped tail and the window page's modulus bound; Lemma D
and the finite counts of excess-positive indices; Lemma R, the isolation
theorems and the classification with its sole pair $(5,3)$; the Duverney
reconstruction, the $L$, $\exp L$ and $\mathsf U$ identities, the
logarithmic-product and prime-sieve obstructions and the gap-multiplier
criterion with its Euler calibration; the account of Erdős's 1948 method as
source fidelity, the termwise-block obstruction, the window counts and the
withdrawal of the exhaustion inference; Proposition 4, the progression-mean
separation with its explicit error bound, the fixed-grid obstruction with its
truncation thresholds and the factorial cousin; the retained identities, Lemma 5
and the two-adic mirror; every finite figure, the continued-fraction exclusion
included; and, under Remaining links and next constructions, the integer span
theorem and the complete-tail criteria in their central-zero, central-free,
aggregated, two-depth and homogeneous forms, the odd-kernel feasibility, the
shadow and flatness results, the phase transference and the short-support
localization, the one-window phase formulation, the signed sparse-multiplier
target and the geometry page's rounding and singular-value bounds are each
refutation-failed, the Kaneko--Suzuki--Tachiya and Bell--Smertnig
specializations conditional on the source statements as the library extracts
them. One sentence was refuted-as-stated, not load-bearing: the claim, in the
paragraph after the display of $\Lambda_k$, that the Dirichlet primes used to
show solvability have no retained uniform bound, which the geometry page's
Linnik bound $\exp(O(k^2\log(k+2)))$ contradicts. No statement was proof
defective; statement unresolved. Not mathematical claims: the standing
paragraph's account of what the next construction must do, the description of
the external Problem 252 manuscript, whose correctness the page does not assess,
the reading record of Prior work and reading limits, the closing account of what
remains open, and the rate sentence after Lemma D, whose constant the reviewer
and the grader found not to follow from the printed distribution. The route
consumes no native claim as a tier-bearing premise: L16, used by the
progression-mean obstruction and the geometry page, was re-derived from the
progression-means page and stays at tier 0. It consumes Dirichlet's theorem,
quadratic reciprocity, the prime number theorem in fixed progressions, Linnik's
theorem, Bertrand's postulate, Euler's pentagonal theorem and the
Kaneko--Suzuki--Tachiya and Bell--Smertnig theorems at the reading depths the
pages state. Its conclusion would rest on one of the unproved estimates the page
lists: unbounded excess $v_2(\Phi_N)-\log_2N$, or infinitely many
excess-positive indices for the dyadic rung; $\liminf_k\Gamma_k/2^k=0$ or one of
its weaker forms; $\limsup\epsilon_J2^J=\infty$ along powers of two; a signed
sparse multiplier meeting the source hypotheses; or a construction forcing a
nonzero null kernel from rationality. The grade's outcome for this lead is
reviewed and ready once its required correction lands; it accepted that
correction and three of the reviewer's four suggested corrections, one with
modified text, rejected the fourth, so the external manuscript's revision
identifier stays, and added one, and all five were applied, so the current text
differs from the reviewed text at these places: in Target and standing, the
sentence after "The proof does not bound its support or coefficients."
(suggested 1); in The dyadic rung, the rate sentence after Lemma D (suggested
2); in Route one, the Bell--Smertnig sentence after the Mellin transform
(added); in Route two, the clause describing $J_0(N)$ in the one-large-prime
window paragraph (suggested 3); and in Remaining links and next constructions,
the last sentence of the paragraph after the display of $\Lambda_k$ (required
1). The sentence of Target and standing that said the arguments have no
independent review, a standing sentence outside the extraction, was reworded in
the same change so that it does not contradict this section. Since the review,
two Route one sentences were reworded, one to record the library's independently
reviewed reconstruction of the Duverney note's theorem and lemma and one to name
the author's scan as the copy read for the library card, and the Route three
sentence on the checking level of the Problem 252 development was reworded to
record its acceptance on the Problem 252 claim page; this touches no examined
statement, proof, code or input. Only the exposition's correctness of that
development remains unassessed here. The paragraph of Remaining links and
next constructions on the prime-dilation and alternating-cube transplant
is not part of the reviewed text; it and the page it links are unreviewed.
No tier is assigned and Problem 249's
status does not
change.

## Remaining links and next constructions

The irrationality target is still unsupported. The exact tail criterion
would suffice if one could construct arbitrarily large valuation excess,
and infinitely many excess-positive indices would already settle the
dyadic rung. A different route could use a signed, uniformly small
rational-tail form. The progression-mean theorem supplies a contradiction
whenever such a construction forces a nonzero absolutely summable
normalized kernel to tend to zero on a progression; obtaining that
implication from rationality is open. The fixed-grid obstruction records
one family that cannot supply it.

There is a constructive alternative to the single-index route.
For each $k\ge3$, the
[[research/leads/totient_binary_series/integer_interpolation/_index|integer interpolation theorem]]
supplies finitely supported integers $y_n$, $n\ge k+2$, satisfying

$$
\sum_n y_n\varphi(n+s)=
\begin{cases}0&(-k<s\le0),\\-2\varphi(s)&(1\le s\le k).
\end{cases}
$$

For the same parameters,

$$
\Lambda_k=2S+\sum_ny_nT_n=uS-v,\qquad
u\equiv2\pmod{2^k},\quad v\equiv0\pmod{2^k},\qquad
|\Lambda_k|\le\frac{C_k(y)}{2^k},
$$

where $C_k(y)=2(k+2)+\sum_n|y_n|(n+k+2)$. If $S=a/b$, then
$bC_k(y)<2^k$ makes $b\Lambda_k$ a zero integer with a nonzero residue
$2a$ modulo $2^k$, a contradiction. Consequently a family with
$C_k(y)/2^k\to0$ would prove irrationality. Each finite system is
known to be integrally solvable, but this weighted estimate is unproved.
All existence quantifiers in the proof precede any limit in $k$. The
only retained quantitative version, Proposition 4 of the
[[research/leads/totient_binary_series/integer_interpolation/geometry|geometry
page]], uses Linnik's theorem to produce a solution with
$C_k(y)\le\exp(Ck^2\log(k+2))$ for an effective absolute constant $C$;
this is far above the required $o(2^k)$.

The same page also removes the central cancellation equation. If
$c_0=\sum_ny_n\varphi(n)$ is left free, then $v\equiv c_0\pmod{2^k}$.
It is even, and $1<S<2$, so under rationality the integer $2a-bc_0$
is nonzero; its magnitude is less than $bC_k(y)$. Thus the same
$bC_k(y)<2^k$ criterion works for this less constrained system. Seeking
small cost need not force the central coefficient to vanish.

This composes with the gap-multiplier criterion by
$p_{N-n}=y_n$ and $p_N=2$. Its exact error bound $E_0(P)$ is
$C_k(y)/2^k$, and its central coefficient is $c_0$. Thus the integer
span theorem settles qualitative feasibility of those affine equations
at every order, even with the stricter support cutoff $n\ge k+2$.
It supplies neither the uniform height bound $HN^2/2^k\to0$ nor the
weaker weighted-cost bound. Four of the five retained finite multipliers
also meet that stricter cutoff; the $(N,k)=(100,20)$ witness meets only
the original gap criterion. None of these finite witnesses proves a
uniform estimate.

The [[research/leads/totient_binary_series/integer_interpolation/carry_criterion|aggregated
carry criterion]] keeps only the two aggregates that the argument above
actually uses. With any nonzero leading coefficient $c$ and $y$ supported
on $n\ge k$, it requires $\sum_ny_n\Phi_n\equiv0\pmod{2^k}$ and
$c\Phi_k+\sum_ny_n(\Phi_{n+k}-2^k\Phi_n)=0$; the identical complete-tail
bound $|\Lambda|\le2^{-k}C_k(y)$ then excludes every denominator
$b<2^k/C_k(y)$. The $2k$ gap coefficients need not vanish, only cancel
as 2-adic digits with carries. At the sampled orders through $k=384$,
the best retained witnesses cost about $2k^2$. The sufficient condition
$\liminf_k\Gamma^*_k/2^k=0$ remains open. A proposed uniform Fourier
condition is refuted: the scalar character with phase
$U_k(n)/2^{k+L}$ has at most two good indices under the stated box-cost
bound, regardless of the support or rationality of $S$.

The [[research/leads/totient_binary_series/integer_interpolation/two_depth_carries|separate-depth
criterion]] leaves a less restrictive construction. With $c=1$, support
$n\ge d$, $v=\sum_n y_n\Phi_n\equiv0\pmod{2^d}$, and
$W_J=\Phi_J+\sum_n y_nU_J(n)=0$, the complete-tail bound is
$|\Lambda|\le C_J/2^J$, where
$C_J=J+2+\sum_n|y_n|(n+J+2)$. A rational denominator $b$ is excluded
when $bC_J<2^J$ and $3b\le2^{d+1}$. Thus $d\to\infty$ and
$C_J/2^J\to0$ suffice; $d$ may grow logarithmically in $J$.
The normalized integer span proves feasibility with $c=1$ for every
fixed pair of depths, but no useful coefficient bound. Conditioning
on the exact $W_J$ equation before counting residues avoids the forced
scalar character; neither the bounded slice's existence nor its
required residue cancellation is proved.
One scalar target solution and one scalar kernel vector
with odd normalized-prefix pairing suffice: a centered multiplier
modulo $2^{d-1}$ repairs the residue. The needed weighted costs of
those two vectors remain open. A repair vector with zero coefficient
of $S$ has weighted cost at least $2^{J+1}$ and cannot supply that bound.

The same page's **homogeneous scalar-kernel criterion** removes the
nonzero target and the residue repair. Take finitely supported integers
$z_n$, $n\ge B\ge4$, satisfying

$$
\sum_nz_nU_J(n)=0,\qquad
\sum_nz_n\Phi_n/2\ \hbox{odd},\qquad
C=\sum_n|z_n|(n+J+2).
$$

For $u=\sum_nz_n2^n$ and $v=\sum_nz_n\Phi_n$, the complete-tail
bound is $|uS-v|\le C/2^J$, while $2^B\mid u$ and $v_2(v)=1$.
If $S=a/b$ and $v_2(b)+1<B$, the integer $au-bv$ has valuation
exactly $v_2(b)+1$. This proves irrationality from a family with
$B\to\infty$ and $C=o(2^J)$. At $B=J\ge4$, every denominator with
$bC<2^{J+1}$ is excluded. The general version permits a scalar
remainder $W$ and requires
$B-v_2(v)\to\infty$ and
$(|W|+C)/2^{J+v_2(v)}\to0$.

An odd kernel vector is qualitatively feasible on the short interval
$[J,2J]$ for every sufficiently large $J$ with $5\nmid J$.
The proof uses two separate reduced prime classes modulo 20 and the
fixed-modulus prime number theorem at its disclosed external standing.
This settles a support choice on the subsequence $J=2^m$.
The constructed two-term vector only gives a cost bound of order
$J^2 2^J$ divided by a gcd with no useful estimate. The minimum
weighted cost in that interval is still uncontrolled. A general
positive scalar row can have full parity feasibility and many short
even relations while every odd relation costs at least $2^J$;
the page gives an explicit family. A proof for the totient row must
therefore use additional arithmetic. The Fourier phase identity under
hypothetical rationality provides a matching obstruction; the page
retains an explicit aggregate error bound, without claiming that
growing signed products cancel or yield a positive odd-vector count.

The [[research/leads/totient_binary_series/integer_interpolation/shadows|shadows page]]
gives another sufficient construction. Two exact kernel vectors whose
integer shadows $(u,v)=(\sum z_n2^n,\sum z_n\Phi_n)$ are not proportional
exclude every denominator below $2^J$ divided by their larger cost.
If an odd kernel vector exists, rounding against explicit vectors with
zero shadow also produces an odd vector at polynomial extra cost.
On $[B_J,3J]$, with $B_J=\max(4,\lfloor\log_2(J+1)\rfloor)$,
irrationality would supply such odd vectors of cost $O(J^4)$ along a
subsequence of powers of two. Conversely $B_J\to\infty$ and cost
$o(2^J)$ exclude every fixed denominator. This equivalence concerns
these supports and a subsequence, not every depth or $[J,2J]$.
Determinant-scaled realization also gives a conditional reverse
construction with $R=J+O(\log J)$ and a slowly growing lower cutoff.
Neither reverse implication constructs a family without assuming
irrationality.

The same analysis turns a flat depth into either a terminal rational
value or an exceptionally good convergent; it proves no converse to
that implication. The certified continued-fraction prefix rules out
both alternatives for $B=4$ and $33\le J\le19950$. These finite
non-flatness conclusions exhibit no vector and give weaker exclusions
than the prefix itself. They do not decide the infinite dichotomy.

The [[research/leads/totient_binary_series/integer_interpolation/phase_transference|phase
comparison]] supplies a further quantitative route. Put
$V_n=U_J(n)/2$, $A_n=\Phi_n/2$, $w_n=n+J+2$, and

$$
\epsilon_J=\inf_{\theta\in\mathbb R,\ m\in\mathbb Z^{\mathcal N}}
\max_{n\in\mathcal N}\frac{|\theta V_n-A_n/2-m_n|}{w_n}.
$$

On linearly growing supports with an odd kernel and two independent
recurrence rows, the minimum odd cost satisfies
$1/(2\epsilon_J)\le C_{\rm odd}<3/\epsilon_J+O(J^{9/2})$.
Thus $C_{\rm odd}=o(2^J)$ is equivalent to
$\epsilon_J2^J\to\infty$. On $[J,2J]$ along large powers of two,
the qualitative prime construction supplies both structural hypotheses.
The phase growth estimate remains unproved. A separate
[[research/leads/totient_binary_series/integer_interpolation/phase_localization|arithmetic
localization]] proves the exact short-support equivalence

$$
S\notin\mathbb Q
\quad\Longleftrightarrow\quad
\limsup_{J\to\infty,\ J=2^m}\epsilon_J2^J=\infty.
$$

The additional input is $\varphi(3k)=2\varphi(2k)$ for odd $k$
coprime to $3$, with two fixed-modulus prime choices supplying the
structural hypotheses. Small aligning phases then give rational
approximants with shared dyadic denominator factors. Their chaining
proves the reverse implication, which did not follow from the
wider-support shadow construction. The same proof gives a finite
exact sufficient test over positive odd $q\le26M(3J+2)$ for
$\epsilon_J>M2^{-J}$, subject to explicit size and gcd conditions.
It proves no unbounded successful family and no divergence along every
power of two. The shadow and phase
criteria preserve arithmetic, coset and cancellation methods as possible
ways to supply it; the earlier scoped obstructions retire none of these
families as a whole.

A separate one-window phase formulation is also available, but is a
reformulation rather than a bound. Fix an integer $b\ge1$ and $C\ge1$,
and let $J=J(N)$ be the least positive integer with
$2^J\ge2^Cb(N+J+2)$. If $S=a/b$, then
$bT_N\in\mathbb Z$ for every $N\ge0$, while

$$
bT_N=\frac{bU_J(N)}{2^J}+\frac{bT_{N+J}}{2^J},\qquad
U_J(N)=\sum_{j=1}^J2^{J-j}\varphi(N+j),\qquad
0<\frac{bT_{N+J}}{2^J}\le2^{-C}.
$$

Hence $bU_J(N)\bmod2^J$ lies in the top interval of relative length
$2^{-C}$. For fixed $C$ this is only a necessary condition for integrality.
With $e(t)=\exp(2\pi it)$, rationality also implies

$$
\sum_{N=1}^X e(bT_N)=X\quad(X\ge1),\qquad
\left|e(bT_N)-\prod_{j=1}^J
  e\left(\frac{b\varphi(N+j)}{2^j}\right)\right|
\le2\pi\,2^{-C}.
$$

A strict saving in the magnitude of this sum for one $b$ excludes that
denominator and every divisor of it: a rational value with reduced
denominator dividing $b$ would still have $bT_N\in\mathbb Z$. It
therefore suffices to prove exclusions on a set $\mathcal B$ such that
every positive integer divides some $b\in\mathcal B$, for example
$b=m!$ for infinitely many $m$. A sufficient estimate is, for each
$b\in\mathcal B$, a constant $\delta_b>0$ and arbitrarily large $X$
with magnitude at most $(1-\delta_b)X$. This keeps the same target
$S$ throughout. No estimate of this kind is proved here. The exact
identity $e(bT_N)=e(b2^NS)$ also shows that this is the doubling orbit of
the same unknown number. The expression using shifted totients becomes
useful only if its arithmetic yields a quantitative separation.

The [[research/leads/totient_binary_series/analytic_sources|signed sparse-multiplier
target]] uses a different consequence of hypothetical rationality. Seek a
fixed integer series $G(z)=\sum_{n\ge0}g_nz^n$ such that
$V(z)=G(z)F(z)=\sum_{n\ge1}v_nz^n$, where
$F(z)=\sum_{n\ge1}\varphi(n)z^n$, has nonnegative coefficients and
infinite support. Require fixed $C>0$ and integer $d\ge0$ with
$|g_n|,v_n\le C(n+1)^d$, and require the union of the two
positive-index supports to have counting function $o(x/\log x)$.
If $G$ has infinite positive-index support, the support of $V$ must
also meet every sufficiently large multiplicative subinterval of every
gap of that support, with the fixed constants and exact quantifiers in
[[../library/irrationality/kaneko_2026_refinements_erdos_s_irrationality_criterion_certain/theorem_1|condition (G)]].

Under $S=A/B$ with positive integers $A,B$, apply
[[../library/irrationality/kaneko_2026_refinements_erdos_s_irrationality_criterion_certain/theorem_3|KST Theorem 3]]
to $a(n)=Bv_n$ and $b(n)=-Ag_n$ for $n\ge1$, choosing
$z_j=\lceil(d+2)\log_2 x_j\rceil$ and $x_j\to\infty$.
The polynomial bounds give the required root growth and coefficient mass;
the support and gap assumptions supply the other hypotheses. The theorem
would make the following integer irrational:

$$
\sum_{n\ge1}(Bv_n-Ag_n)2^{-n}
=BG(1/2)S-A\bigl(G(1/2)-g_0\bigr)=Ag_0.
$$

No such $G$ is known here. Nonnegative coefficients of a nonzero $G$
make $GF$ eventually positive at every index, so cancellation is necessary.
For integers $N\ge1$, $h\ge0$ and $c_n=Bv_n-Ag_n$ vanishing on
$N\le n<N+h$, the research account bounds the entire scaled tail
$|\sum_{n\ge N}c_n2^{N-n}|$ by
$C(A+B)2^{-h}(N+h+1)^d\sum_{u\ge0}(u+1)^d2^{-u}$.
Any construction with changing height or degree must control these factors
with the same growing parameters and must also prove nonvanishing.
Neither the non-Mahler theorem nor the positive-orbit obstruction excludes
this signed target or the existing finite polynomial-multiplier criterion.

The [[research/leads/totient_binary_series/dilation_cube|prime-dilation
and alternating-cube construction]] adapts the initial reduction of the
base-two omega theorem. The identities are exact, and division by
$G=\gcd_\epsilon(p_\epsilon-1)$ gives integer weights on the original
tails and a smaller complete error bound. A fixed saving in the resulting
exponential average would contradict rationality. The page proves the
bound with all tails included, but supplies no such saving. In its stated
averaging regime, making the displayed absolute tail bound vanish requires
at least a logarithmic window, even after that normalization. A count using the
intersection periods of the large-prime progressions shows that
coincidences alone leave many formal coefficients; it gives no lower
bound for the phase at actual totient values. The page also rules out
Pratt's cofactors-$k$ window with a discarded positive tail below $1/b$.
These are scoped author arguments, and the remaining phase estimate and
other weighted or selected-subfamily constructions stay open.

Other open constructions include growing dilation grids, signed
combinations of sieve sums, and product transforms outside the fixed
families excluded above. Their full-tail
bounds must use the same parameters as their coefficient constructions.
Neither the finite observations nor the scoped obstruction statements
close these questions.

For the interpolation route, a
[[research/leads/totient_binary_series/integer_interpolation/geometry|projection
and integer-rounding bound]] separates two quantitative obligations:
the norm of the real solution for the prescribed target and the cost
of rounding within the integer kernel. For a prime $2k<\ell<4k$ and
every integer $X\ge\lceil4096k^2\log(k+2)\rceil$, finite progression
means give

$$
\sigma_{\min}(A)\ge\frac{X^{3/2}}{4\zeta(2)},\qquad
R=2\ell X+\ell+k-1.
$$

The corresponding real contribution to the weighted cost is less than
$512k^3$, uniformly for every such $X$. This is a finite matrix bound
uniform over all unit coefficient vectors, not an exchange of growing
limits. The qualitative integer span theorem permits increasing $X$
until integral target membership holds, but gives no useful endpoint
or rounding-cost bound. Obtaining weighted integer rounding cost
$o(2^k)$ along unbounded orders would complete this sufficient route.
The general unimodular counterexamples explain why kernel control
alone could not have supplied the now-proved real estimate. No
irrationality conclusion follows without the remaining integer bound.
