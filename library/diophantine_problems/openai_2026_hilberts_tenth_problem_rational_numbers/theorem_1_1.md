---
name: diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/theorem_1_1
title: "Theorem 1.1: no algorithm decides whether an integer polynomial has a rational zero"
desc: |
  The manuscript's main claim: Hilbert's tenth problem over Q has a negative
  answer, by a Turing reduction of integer solvability to rational
  solvability. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

The decision problem takes as input a number of variables $n$, which is not
bounded in advance, and a polynomial $f\in\mathbb Z[X_1,\ldots,X_n]$. It
asks whether $f(\mathbf x)=0$ for some $\mathbf x\in\mathbb Q^n$, that is,
whether $f$ has a rational zero.

**Theorem 1.1.** This problem is undecidable: no algorithm gives the correct
answer on every input $(n,f)$.

The proof shows more: an algorithm for rational solvability would yield one
for integer solvability, which the Davis--Putnam--Robinson--Matiyasevich
theorem excludes.
[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/corollary_7_1|Corollary 7.1]]
records the resulting Turing degree $0'$ and the same undecidability for
polynomials of total degree at most four. The introduction says that an
existential definition of $\mathbb Z$ in $\mathbb Q$, or a Diophantine model
of integer arithmetic over $\mathbb Q$, would be a sufficient route but that
"the decision problem does not require its solution to produce either one"
(p. 3), and the proof of Corollary 7.1 says the construction "gives no
single existential definition of $\mathbb Z$ in $\mathbb Q$" (p. 57). The
reduction from integer to rational solvability is a Turing reduction; the
same passage says the argument does not establish many-one completeness of
rational solvability and supplies no bound on the number of variables.

**Source.** OpenAI, *Hilbert's tenth problem over the rational numbers*,
release folder
`preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026`;
TeX file `build/sections/01-introduction.tex`, label `thm:main` (lines
7--11), PDF p. 3; the proof closes at the end of Section 2
(`build/sections/02-reduction.tex` lines 876--887, PDF p. 17), with its
inputs proved in Sections 3--6 (pp. 18--56). Provenance and attestations are on
[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/_index|the card]].

**Read depth.** Claims checked: the statement, and the statements of
Propositions 2.1, 2.2, 2.8, 2.11 and 2.12, Lemmas 2.3, 2.7, 2.9 and 2.10,
Theorem 2.4 and Corollaries 2.5--2.6, were read clause by clause in the TeX
source. The proof was read for its structure only, as summarized below; no
step was checked. Nothing here is independently reviewed.

## Proof pointer

The argument reduces integer solvability to rational solvability. It fixes
$F=\mathbb Q(\sqrt2)$, its conjugation $\sigma$, $d=75-53\sqrt2$ and the
curve $E:y^2=x^3-d^2x$, for which $E(F)$ has rank one (Proposition 2.1, by a
two-isogeny descent in Section 5), so that $mE(F)=\mathbb ZP$ for some
$m\ge1$ and a nontorsion point $P$. A recursive first-order theory
$\mathcal T$ in an expansion of the ring language describes a domain $R$
together with points $T_a\in mE(F_R)$, $F_R=\operatorname{Frac}(R)(\sqrt2)$,
that are additive in $a$, with $T_1=P$ and $T_a$ nonzero for $a\ne0$. For
each precision $K$ it also asks that every element $A$ be a sum
$u_1/v+u_2/v+u_3/v$ whose thirteen contact values $v$ and $L_b(u_i,v)$, for
the linear forms vanishing at the four finite points of Theorem 2.4, are
each a sign times a fixed multiplier times an element $r$ with $R/rR$ a
field containing a square root of $2$. At both resulting branch ideals there
must be auxiliary $h,j_0$, fixed for all $a$, passing two tests: the ratio of
truncated formal logarithms of $T_{ha}$ and $T_h$ agrees with $a$ to order
$K$, and on the conjugate curve the ratio of the formal parameters of
$T^\sigma_{(h-4)a}$ and $T^\sigma_{j_0}$ is divisible by $r^K$ in the local
ring. The integers with $T_a=aP$ satisfy $\mathcal T$ (Lemma 2.7); the
witnesses come from the prime-pattern Lemma 6.1, proved with the
Green--Tao--Ziegler theorem on linear equations in primes and a Selberg
sieve, and the local tests from Proposition 2.2.

Given a nonconstant $f$, the method adds constants $\mathbf a$ with
$f(\mathbf a)=0$, Skolemizes, and enumerates finite tests: finitely many
ground-term values satisfying the ring and functionality constraints, the
ground instances of the axioms, and the positive existential formula $\Phi$
of Proposition 2.8 on every value. Each test reduces to finitely many
rational-solvability queries, and an integer zero makes every test succeed.
If every test succeeds, compactness (Lemma 2.9) embeds a model $R$,
containing a zero $\mathbf a$ of $f$, in the rationals ${}^*\mathbb Q$ of an
elementary extension of a many-sorted arithmetic structure, and gives an
additive injective index map $\eta:R\to{}^*\mathbb Z$ with
$\widetilde T_a=\eta(a)P$ that need not respect multiplication. At any
ambient prime $q$ of odd contact for a representing sum, the pole parity of
$\Phi$ (Lemma 2.10) attaches $q$ to one tested branch, and the two tests
then force every $\widetilde a$ to be $q$-integral and congruent to
$\eta(a)$ modulo $q^K$ (Lemma 2.3, Proposition 2.11).

Put $\delta=f(\eta(a_1),\ldots,\eta(a_n))$ and
$B=\max(1,|\eta(a_j)|)$. If $\delta=0$, elementarity gives an ordinary
integer zero. Otherwise $|\delta|\le C_fB^{\deg f}$; choosing
$K\ge c\deg f$, with $c$ the exponent of Theorem 2.4, every contact radical
of every representing sum has its $K$th power dividing $\delta$, so the
height estimate bounds all slope heights, and hence $h(\widetilde A)$ for
every $A\in R$, by $O_f(B)$ (Proposition 2.12). Applied to the coordinates of
$T_{a_j}=\eta(a_j)P$, this contradicts the quadratic growth of the canonical
height unless $B$ is bounded by an ordinary constant, in which case each
$\eta(a_j)$ is an ordinary integer, injectivity makes $\mathbf a$ an integer
zero, and $\delta=0$ after all. So when $f$ has no integer zero some finite
test fails, and running the test search alongside an enumeration of integer
tuples would decide integer solvability.

## Dependencies

The Davis--Putnam--Robinson--Matiyasevich theorem (Davis, Putnam and Robinson
1961; Matiyasevich 1970); the compactness theorem (Marker); the canonical
height (Silverman); and the manuscript's own
[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/theorem_2_4|Theorem 2.4]],
Proposition 2.8 and Lemma 6.1, whose external inputs include two other
release manuscripts, both unreviewed: Theorem 1.1 of *A pointwise 2-converse
for elliptic curves with rational two-torsion* (for Lemma 3.4, hence
Proposition 2.8) and Theorem 1.1 of *Fontaine--Mazur modularity at the prime
2* (for the modularity step of Theorem 2.4), filed at
[[number_theory/openai_2026_fontaine_mazur_modularity_prime_2/_index|the Fontaine--Mazur card]].
Lemma 6.1 rests on Green and Tao's *Linear equations in primes*, their
Möbius--nilsequences theorem and the Green--Tao--Ziegler inverse theorem
with its 2024 erratum. The fixed constants of the theory are asserted to
exist and are hardcoded; the text says that their existence suffices and
that no effective search for them is needed (p. 12). None of these inputs
was checked here.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this theorem.
