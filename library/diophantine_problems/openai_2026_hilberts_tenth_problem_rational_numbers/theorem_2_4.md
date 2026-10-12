---
name: diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/theorem_2_4
title: "Theorem 2.4: five-point height estimate, h(s) <= H M_S(s)^c for the primes of odd contact with five fixed points of P^1"
desc: |
  The manuscript's five-point height estimate: the Weil height of a rational
  point of P^1 off five fixed rational points is at most H M^c, where M is the
  product of the primes outside a fixed finite set at which the point meets
  one of the five to odd order. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Write $h$ for the absolute logarithmic Weil height on
$\mathbf P^1(\mathbb Q)$ and $v_q$ for the $q$-adic valuation, with
$v_q(q)=1$ and $v_q(0)=+\infty$.

**Theorem 2.4** (five-point height estimate). There exist five distinct
points $\mathcal C\subset\mathbf P^1(\mathbb Q)$, one of them $\infty$, a
finite set $S$ of primes and constants $H,c>0$ with the following property.
For each $b\in\mathcal C$ choose a primitive integral linear form
$L_b(U,V)$ vanishing at $b$, with $L_\infty(U,V)=V$. For
$s=(u:v)\in\mathbf P^1(\mathbb Q)\setminus\mathcal C$, the contact order of
$s$ with $b$ at a prime $q$ is
$v_q(L_b(u,v))-\min\{v_q(u),v_q(v)\}$, and $M_S(s)$ is the product, each
prime taken once, of the primes $q\notin S$ at which at least one of the
five contact orders is odd. Then
$$
h(s)\le H\,M_S(s)^c .
$$

The contact orders do not depend on the homogeneous coordinates chosen for
$s$, they are nonnegative, and $M_S(s)$ is a finite product (p. 10). The
choice of each $L_b$ is fixed up to sign. For a positive integer $K$ and a
nonzero integer $e$ with $M_S(s)^K\mid e$, the theorem gives
$h(s)\le H|e|^{c/K}$ (p. 10), the form in which the reduction uses it.
**Corollary 2.5** (p. 10): for any fixed finite $S'\supset S$,
$h(s)\le H\bigl(\prod_{q\in S'\setminus S}q\bigr)^cM_{S'}(s)^c$, so
enlarging the exceptional set changes the constant and not the exponent.

The theorem asserts existence. Section 4 constructs $\mathcal C$ as the five
branch values of the Atkin--Lehner quotient of the Shimura curve attached to
a maximal order in the indefinite quaternion algebra of discriminant
$210=2\cdot3\cdot5\cdot7$, identified over $\mathbb Q$ with $\mathbf P^1$ so
that one branch value is $\infty$; the manuscript does not print their
coordinates or values for $S$, $H$ and $c$, and says the precise value of $c$
is not needed (p. 10). It does not claim the constants are effective: the
proof bounds the fibers with complex multiplication through the finiteness
of CM $j$-invariants of bounded degree, a finiteness that, in the text's
words, "need not be effective" (p. 36), and the proof's $H$ absorbs that
bound. The proof of Lemma 4.7 allows the level bound $N\le CM^2$, but no
value of $c$ is stated.

**Source.** OpenAI, *Hilbert's tenth problem over the rational numbers*,
release folder
`preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026`;
TeX file `build/sections/02-reduction.tex`, label `hei:height` (lines
232--248), PDF p. 9, with Corollary 2.5, label `hei:enlarge-exceptions`
(lines 270--279), PDF p. 10; the proof occupies Section 4
(`build/sections/04-height.tex`, PDF pp. 26--44) and closes at lines
1299--1309, PDF p. 44. Read 2026-10-12. Provenance and attestations are on
[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/_index|the card]].

**Read depth.** Claims checked: the statement, the definition of the contact
orders and of $M_S(s)$, and Corollary 2.5 were read clause by clause in the
TeX source. The proof in Section 4 was read for its structure only, as
summarized below; no step was checked. Nothing here is independently
reviewed.

## Proof pointer

The construction (Section 4.1) takes the maximal-level Shimura curve $X$ of
the discriminant-$210$ quaternion algebra, a proper curve of genus $5$ with
no elliptic points, and its quotient by the Atkin--Lehner group
$\mathcal W\cong(\mathbb Z/2)^4$. Riemann--Hurwitz bounds the number of branch
values by five, five fixed points labelled by $m=30,42,70,105,210$ (from
embeddings of $\mathbb Q(\sqrt{-m})$) give at least five, and so the quotient
is a genus-zero curve over $\mathbb Q$ with five individually rational branch
values, hence $\mathbf P^1$; the text says this agrees with the tables of
Long, Maclachlan and Reid and of Nualart Riera. A finite étale level cover
$Y\to X$ carries a principally polarized abelian surface family
$\mathcal A\to Y$ with quaternionic multiplication, built through a
symplectic representation into a Siegel datum. The composite
$\pi:Y\to\mathbf P^1$ has ramification index exactly two over $\mathcal C$,
and fibers over a common base point are geometrically isogenous.

For a rational $s\notin\mathcal C$ with $M=M_S(s)$, the local equation
$t=z^2$ at the branch sections shows that the splitting field $K_0$ of
$\pi^{-1}(s)$ has bounded degree and is unramified outside $S$ and the
primes dividing $M$, and that every fiber over $s$ has good reduction
outside $S$ (Lemma 4.1). Lemma 4.2 bounds the base height by
$C(1+\max\{0,h_{\mathrm F}(\mathcal A_y)\})$, through a theta-null map and
Pazuki's comparison of theta and Faltings heights, so it remains to bound
the Faltings height of a fiber $A$ polynomially in $M$. Lemma 4.4 gives a
Galois field $L$ of bounded degree, unramified outside $S$ and the primes
of $M$, over which all homomorphisms between the Galois conjugates of $A$
are defined. If the centralizer of the quaternion action is an imaginary
quadratic field, $A$ is isogenous over $L$ to the square of a CM elliptic
curve whose $j$-invariant has degree at most $[L:\mathbb Q]$; only finitely
many such $j$-invariants exist (by Siegel's class-number theorem, a
finiteness the text says need not be effective), and the Gaudron--Rémond
isogeny theorem then bounds $h_{\mathrm F}(A)$ uniformly. Otherwise
$\operatorname{End}^0(A)$ is the quaternion algebra, conjugate isogenies
compatible with it define a sign cocycle, and Lemma 4.5 splits that cocycle
by a cochain whose square is a Dirichlet character of order $O(M)$, tame at
odd primes and unramified outside $S$ and the primes of $M$. The corrected
Galois action is two copies of a two-dimensional, odd, irreducible
representation that is de Rham with cyclotomic exponents $0$ and $1$, so
with distinct Hodge--Tate weights; the Fontaine--Mazur theorem at $2$ of the
cited release manuscript makes the $2$-adic one the representation of a
weight-two newform $f$, and Lemma 4.6 matches the $3$-adic one with the same
form.
Carayol's local-global compatibility, with tameness at large primes and a
uniform ramification cut at the small fixed ones, gives a level
$N\le CM^a$ (Lemma 4.7). Faltings' theorems then make $A$ an isogeny factor
of $J_1(N)$ over a field of degree at most $CM$ (Lemma 4.8). Javanpeykar's
bound for Jacobians of Belyi curves gives $h_{\mathrm F}(J_1(N))\le CN^{12}$;
Zarhin's trick, the Gaudron--Rémond isogeny theorem with its explicit
dependence on dimension, and Bost's lower bound for the complement then give
$h_{\mathrm F}(A)\le CM^C$, and Lemma 4.2 converts this into
$h(s)\le HM^c$.

## Dependencies

Deligne's canonical models of Shimura varieties; Voight's *Quaternion
Algebras* (the Eichler area formula and conjugacy of maximal orders); Long,
Maclachlan and Reid, and Nualart Riera, for comparison of the quotient;
Mumford's *Abelian Varieties* and Guitart and Molina for the family; Pazuki's
theta-height comparison, Bombieri and Gubler's height machine and Gaudron and
Rémond's normalization of the Faltings height for Lemma 4.2; Siegel's
class-number theorem and Cox for the CM case (not effective); Ribet, Pyle
and Quer on $\mathbb Q$-curves and building blocks; local class
field theory and the Brauer group (Serre, Milne); Scholze's de Rham
comparison and Fontaine for the Hodge--Tate data; Theorem 1.1 and Section 2.1
of the release manuscript *Fontaine--Mazur modularity at the prime 2*,
unreviewed, filed at
[[number_theory/openai_2026_fontaine_mazur_modularity_prime_2/_index|the Fontaine--Mazur card]];
Deligne's Galois representations of modular forms, Carayol's local-global
compatibility (Theorem A), Silverberg and Zarhin's semistable reduction
criterion and Ribet's Eichler--Shimura realization for the level and the
modular factor; Faltings 1983; Javanpeykar's height bound for Belyi curves
(Theorem 1.1.1); Zarhin's quaternion trick; the Gaudron--Rémond isogeny
theorem (*Polarisations et isogénies*, Theorem 1.4) and Bost's lower bound
in the form of Gaudron and Rémond (Corollary 8.4). The text names
Murty--Pasten, von Känel and Alpöge as precedents for the modular height
strategy. None of these inputs was checked here.

## Bears on

No problem page is identified as using this estimate; the five points are
fixed by the Shimura curve and are not the configuration of any problem
page's question.
