---
name: integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/proposition_2_1
title: "Proposition 2.1: a conditional prime reservoir p = 4rQ+1 in a fixed progression"
desc: |
  The manuscript's prime reservoir, conditional on three inputs it takes
  from the companion Artin manuscript: many primes p in (x,2x) in a
  fixed progression with p-1 = 4rQ, Q > x^0.9 prime and r composed of
  primes in a controlled range. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

The proposition assumes Inputs 4.1, 5.1 and 5.2, three statements that the
manuscript takes from its companion, *Primitive roots for every admissible
integer base*, and does not prove. They are stated, with the marked setup
they use, on
[[integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/theorem_1_1|the page of Theorem 1.1]].

**Proposition 2.1** (a prime reservoir in a fixed progression). Suppose
Inputs 4.1, 5.1 and 5.2 hold. Fix an odd squarefree modulus $M\ge1$, the
trivial modulus $M=1$ allowed, and a class $a$ modulo $M$ such that $a$ and
$a-1$ are both prime to $M$, that is, $\gcd(a(a-1),M)=1$. Then there are
$c_{M,a}>0$ and $x_{M,a}>1$ such that, for each real $x\ge x_{M,a}$ and with
$L=\log x$, at least $c_{M,a}x/L^2$ primes $p\equiv a\pmod M$ in $(x,2x)$
have the form $p=4rQ+1$, where $Q>x^{0.9}$ is prime and $r$ is a positive
integer all of whose prime factors $\ell$ satisfy
$\exp(L^{0.1})<\ell<\exp(L^{0.3})$.

For these primes $Q$ is the largest prime factor of $p-1$ and the cofactor
$4r=(p-1)/Q$ is below $2x^{0.1}$. The statement does not exclude $r=1$, but
it does not promise that case either: the construction's marks
$\mathcal W(r)$ vanish unless $r$ has a prime factor in every group, so
$r=1$ carries no weight. For large $x$, $r$ and $Q$ are odd and every such
$p$ is $5$ modulo $8$. Nothing is claimed without the three Inputs; Input
3.1 is not used.

Read against its statement only, the companion's own Proposition 2.1, which
allows a progression modulo any positive multiple of $8$, appears to contain
this one: take there the modulus $8M$, $c=4$ and a class $u$ with
$u\equiv5\pmod8$ and $u\equiv a\pmod M$. This comparison is made on this
page and is unverified. The manuscript does not make it: it derives the
proposition from the three Inputs instead of citing the companion's, and
its introduction presents Sections 4--5 as extending the companion's
Section 12 construction to a fixed progression.

**Source.** OpenAI, *Simultaneous primitive roots: a conditional lower bound
for prime bases*, release folder
`preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026`;
TeX file `build/sections/02-reduction.tex`, label `prop:reservoir` (lines
11--28), PDF p. 2; the proof occupies Sections 4 and 5
(`build/sections/04-marked-family.tex` and
`build/sections/05-prime-reservoir.tex`, PDF pp. 6--20) and closes at
`05-prime-reservoir.tex` lines 596--610, PDF p. 20. Read 2026-10-12.
Provenance and attestations are on
[[integer_sequences/openai_2026_simultaneous_primitive_roots_conditional_lower_bound_prime_bases/_index|the card]].

**Read depth.** Claims checked: the statement, Inputs 4.1, 5.1 and 5.2 and
the marked setup and density they use (stated on the page of Theorem 1.1)
were read clause by clause in the TeX source, together with the statements
of Lemmas 4.2--4.4. The fifteen-page proof was read for its structure only
(below); no step was checked and the numerical exponent margins were not
recomputed. Nothing here is independently reviewed.

## Proof pointer

The notation ($L$, $W$, $P^-$, $V$, the group primes, the marks
$\mathcal W$ and the density $D_\gamma$) is the setup stated with the Inputs
on the page of Theorem 1.1.

Section 4 (pp. 6--12) builds a weighted family. Fix a smooth $\Psi$
supported in $(1,2)$ with $0\le\Psi\le1$, let $h_{\mathcal P}$ be the part of
$h$ composed of group primes, and let $F(h)$ be the indicator that
$h/h_{\mathcal P}=4Q$ for a prime $Q>x^{0.9}$; this $F$ is invariant under
multiplication by group primes, as Input 4.1 requires. The weight of
$d\ge2$ is $w(d)=\mathbf 1_{d\equiv a\,(M)}\Psi(d/x)F(d-1)\mathcal W(d-1)$
(4.15). A supported $d$ is uniquely $4rQ+1$ with $r$ a product of group
primes, so every supported prime has the shape the proposition asks for,
and the bound on the marks gives $0\le w\le B_K=(2/\log2)^K$. Lemma 4.3
shows by the prime number theorem modulo the fixed $M$ that the total weight
$X_0$ is of order $xJ_0/L$, where
$J_0=\sum_r\mathcal W(r)/r$ lies between $1$ and a constant depending on
$K$, and that large $r$ contribute negligibly. Lemma 4.4 bounds the sieve
remainders, on average over $r\le x^\epsilon$ and over moduli up to
$D_0=x^{1/2-\kappa/2}$, by the Bombieri--Vinogradov theorem. Lemma 4.2
twists Input 4.1 by a character $\chi_0$ modulo $M$: Input 4.1(ii) applied to
the product characters $\chi_0\chi$, of modulus at most $L^{A_0+1}$,
supplies the cancellation hypothesis of Input 4.1(i).

Section 5 (pp. 12--20) extracts primes. A lower-bound sieve (Input 5.1 at
depth $H_b=2\lfloor1/(40b)\rfloor$) removes the prime factors up to $x^b$
and leaves weight at least
$e^{-\gamma_E}b^{-1}(1-C_se^{-c_s/b})+o(1)$ in units of
$\mathfrak S_MX_0/L$, where $\mathfrak S_M>0$ is a constant fixed by $M$
(5.5). Composites whose least prime factor $n$ lies in $(x^b,x^{1/2-\kappa}]$
are removed bin by bin over a fixed partition of $[b,1/2-\kappa]$. In each
bin the weight of $d=mn$ with $P^-(m)>x^\gamma$ is replaced, at cost
$o(X_0/L)$, by a count of $W$-rough $m$ weighted by
$D_\gamma(\log m/L)/(LV(W))$; this uses Lemma 4.2 after separating
$\Psi(mn/x)$ by Fourier inversion and the progression by characters
modulo $M$ (5.8). A sieve conditioned on $n\mid d$ evaluates the replaced
count (5.6), and Input 5.2 bounds the total over the bins by
$D_b(1)-1+1/8$ in the same units (5.12)--(5.13). The remaining composites
are products of two primes above $x^{1/2-\kappa}$. For each $r$ separately,
an upper-bound sieve on pairs $(m,n)$ with $mn\equiv1\pmod{4r}$ (Input 5.1
with $H=2$) bounds their weight by $C_2(\kappa+L^{-1})X_0/L$, with $C_2$
independent of $\kappa$, $b$ and $K$ (5.20). The parameters are chosen in
the order $\kappa$, $\epsilon$, $b$, the partition, $K$, the $a_i$, and
finally $x$, so that each of the three fixed losses is at most $1/8$. The
primes then carry weight at least $\mathfrak S_MX_0/(2L)\gg x/L^2$ (5.21),
and dividing by $B_K$ counts distinct primes.

## Dependencies

Assumed and not proved in the manuscript: Inputs 4.1, 5.1 and 5.2, which it
attributes to the companion *Primitive roots for every admissible integer
base*
([[integer_sequences/openai_2026_primitive_roots_admissible_integer_base/_index|card]]):
Input 4.1 to the coefficient criterion of its Lemma 10.2 specialized to
these marks and to the cancellation verified in the proof of its
Proposition 10.3, Input 5.1 to its Lemma 11.1 and Input 5.2 to its Lemma
11.2. Proved in the manuscript: Lemmas 4.2--4.4. External results cited at
statement level and not checked here: the prime number theorem for a fixed
modulus, the Bombieri--Vinogradov theorem (Bombieri 1965, Vinogradov 1965),
Mertens' theorem and Fourier inversion.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this proposition; the card says why Problem 1065 is not listed.
