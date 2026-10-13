---
name: additive_combinatorics/openai_2026_power_saving_polynomial_differences_prime_arguments/theorem_1_1
title: "Theorem 1.1: a subset of {1,...,N} with no difference equal to a nonzero h(p), p prime, has at most C_h N^(1-c_h) elements"
desc: |
  The manuscript's main claim: for a fixed prime-intersective integer
  polynomial h of degree at least 2 with positive leading coefficient, sets
  in {1,...,N} whose differences avoid every nonzero h(p), p prime, have at
  most C_h N^(1-c_h) elements; the proof rests on the release's claimed 7/8
  zero-free half-plane. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Write $[N]=\{1,\ldots,N\}$, $\mathbb P$ for the set of positive primes and
$A-A=\{a-b:a,b\in A\}$. The manuscript calls $h\in\mathbb Z[x]$
*prime-intersective* if every positive integer $q$ has an integer $r$ with
$(r,q)=1$ and $h(r)\equiv0\pmod q$: a root of $h$ modulo $q$ that is a unit
modulo $q$ (p. 1).

**Theorem 1.1.** Let $h\in\mathbb Z[x]$ be prime-intersective, of degree at
least $2$, with positive leading coefficient. There are constants $c_h>0$
and $C_h\ge1$ such that, for every positive integer $N$ and every
$A\subseteq[N]$, if $(A-A)\cap\{h(p):p\in\mathbb P\}\subseteq\{0\}$, that is,
if no nonzero value of $h$ at a prime is a difference of two elements of
$A$, then $|A|\le C_hN^{1-c_h}$.

The manuscript adds that the constants depend only on $h$, that $C_h$ is
enlarged to cover the finitely many small $N$, and that a prime root of $h$
is harmless: a value $h(p)=0$ restricts nothing (p. 1). No value of $c_h$ is
computed; the proof gives $c_h=a_0/d$, where $d$ is the number of slots of
the tuple laws and $a_0$ is chosen small after every structural parameter.
The manuscript does not claim that $c_h$ depends only on the degree of $h$,
as the integer-argument companion's exponent does. Read here, and not said
in the manuscript, the proof as written does not give that: $d$ and $a_0$
are fixed through the cycle length $L$ and the modulus $M_0$, which depend on
$h$ itself through its lifting exponents at small primes (Lemmas 2.3
and 2.4).

Two examples, the first from the manuscript (`introduction.tex`, lines
94--96, p. 2): $h(x)=(x-1)^2$ is prime-intersective with $r=1$, and the
theorem then forbids only the differences $(p-1)^2$, so it applies to every
set with no nonzero square difference. By contrast, observed here and not in
the manuscript, $h(x)=x^2$ is not prime-intersective, since no unit modulo
$q>1$ is a root of $x^2$ modulo $q$; the theorem says nothing about
differences $p^2$.

The statement carries no hypothesis beyond these, but its proof takes as a
theorem input the release's claimed zero-free half-plane for Dirichlet
$L$-functions (Theorem 5.1; see Dependencies), so the theorem is
established in the manuscript only given that claim.

**Source.** OpenAI, *A Power Saving for Polynomial Differences at Prime
Arguments*, release folder
`preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026`;
TeX file `build/sections/introduction.tex`, label `thm:main` (lines 19--29),
PDF p. 1, with the definition at lines 10--17 and the remark at lines
31--34; the proof closes at the end of Section 7
(`build/sections/descent.tex`, lines 473--486, PDF p. 41). Provenance and
attestations are on
[[additive_combinatorics/openai_2026_power_saving_polynomial_differences_prime_arguments/_index|the card]].

**Read depth.** Claims checked: the statement, the definition of a
prime-intersective polynomial and the remark after the theorem, and the
statements of Theorem 5.1 (`build/sections/primes.tex`, lines 27--34),
Proposition 5.2 (lines 36--47 of the same file) and Proposition 7.5
(`build/sections/descent.tex`, lines 414--420) were read clause by clause in
the TeX source. The proof (Sections 2--7, pp. 3--41) was read for its
structure only, as summarized below; no step was checked. Nothing here is
independently reviewed.

## Proof pointer

The argument is a contracting induction run over a family of auxiliary
polynomials at once, adapted from the integer-argument companion. At every
prime the manuscript fixes a root of $h$ that is a $p$-adic unit (it exists
because the unit roots modulo $p^j$ form an infinite, finitely branching
tree), records its multiplicity $m_p$ in the completely multiplicative
function $\lambda(p)=p^{m_p}$, and for each $l\ge1$ combines the roots into
an integer $r_l$ coprime to $l$, giving $T_l(x)=r_l+lx$ and
$h_l=h(T_l(x))/\lambda(l)\in\mathbb Z[x]$ (Lemma 2.1). A set avoids at $l$
if no nonzero $h_l(m)$ with $m\ge1$ and $T_l(m)$ prime lies in its
difference set; at $l=1$ this is the theorem's hypothesis. The identities
$T_l(Dx-i)=T_{lD}(x)$ and $h_l(Dx-i)=\lambda(D)h_{lD}(x)$ show that the part
of a set avoiding at $l$ in a progression of step $\lambda(D)$, rescaled,
avoids at $lD$, with the prime argument preserved.

For each large prime $p$, Section 3 builds a probability law on labels in
$\mathbb F_p$ indexed by a fixed finite slot set $V$ (Proposition 3.1). It
is reflection positive across a family of cuts, translation invariant,
covariant under $l\mapsto lD$ and conditionally mixing at rate $p^{-\gamma}$.
Off an exceptional part of mass at most $p^{-4}$, consecutive slots on a
designated cycle of length $L$ differ by residues that are values of $h_l$
at arguments $x$ with $p\nmid T_l(x)$ and $h_l'(x)\not\equiv0\pmod p$. The
product of these laws over the primes in $[P,Q]$, $Q=N^\beta$, defines a
multilinear form, and reflection positivity gives a
signed Hölder inequality and a seminorm (Proposition 4.1, Lemma 4.2). The
quantity tracked, $\mathcal Y_l(N)$, is the largest diagonal value of this
form over sets avoiding at $l$, evaluated on the Fourier lift of
$\mathbf 1_A$: its rational Fourier coefficients with squarefree denominator
at most $Q$, carried to $\prod_p\mathbb F_p$. It is at least
$(|A|/N)^d$ with $d=|V|$, and at most $N^{o(1)}$ by the lift moment bound
(Proposition 4.4).

Averaging over residues modulo a fixed modulus $M_0$ built from the small
primes, a proportion at least $M_0^{1-L}$ of residue assignments is good:
their cycle increments are admissible modulo $M_0$ (Lemma 2.4). For a good
assignment, with the exceptional parts removed, the form is $O(N^{-\sigma})$
(Proposition 7.3). Splitting $[N]$ into short intervals, some cycle edge
joins an earlier interval to a later one; after truncating and conditioning
the other inputs, what remains is a pairing of two progression-restricted
pieces of $A$ weighted by that edge's multiplier, and avoidance makes it
small (Proposition 6.1). That proposition realizes the multiplier, up to a
uniformly small error, by a signed kernel supported on the forbidden values
$h_l(m)$ with $T_l(m)$ prime (Lemma 6.2). On major arcs the comparison uses
Proposition 5.2, the count of primes in residue classes uniform in the
modulus, which is where the zero-free half-plane enters; on minor arcs it
uses Proposition 5.3, a power saving for prime-weighted polynomial
exponential sums by Vaughan's identity and Weyl differencing.

Assignments that are not good, and the exceptional terms, are bounded by the
same quantity at a shorter scale $n_B\approx N/\lambda(D_B)$ and parameter
$lD_B$ through the progression identity (Proposition 7.2). This gives the
recurrence of Proposition 7.4, whose bracket contracts because the good
proportion is bounded below and the exceptional masses sum to at most $1/4$.
The recurrence needs $l\le N^\zeta$ while its successors may leave that
range, so Proposition 7.5 proves $\mathcal Y_l(N)\le C_0l^{b_0}N^{-a_0}$ for
all $l,N\ge1$ together, by induction on $N$, with the trivial bound covering
$l>N^\zeta$. At $l=1$ this gives $(|A|/N)^d\le C_0N^{-a_0}$, hence the
theorem with $c_h=a_0/d$ and $C_h=C_0^{1/d}$. Only positive differences are
used in the cancellation, so a zero value $h(p)$ plays no role.

## Dependencies

External inputs, taken at statement level; none was checked here.
Theorem 5.1, the zero-free half-plane: every Dirichlet $L$-function, for every
modulus and every character, imprimitive ones and $\zeta$ included, has no
zero in $\operatorname{Re}s>7/8$, with the principal pole at $s=1$ allowed.
It is the Dirichlet part of Theorem 1.1 of the release's *The Quasi-Riemann
Hypothesis*, filed at
[[primes/openai_2026_quasi_riemann_hypothesis_zero_free_half_plane_7_8/theorem_1_1|the 7/8 card's Theorem 1.1]],
whose read status there is claims checked only and which nothing in this
corpus has reviewed; the manuscript says only that assertion is needed, so
the Hecke part over $\mathbb Q(\sqrt{-3})$ is not used. The release's Lean
catalog lists a comparator for this Dirichlet statement among its main
results (the catalog's review field reads unchecked); nothing was built or
audited here (see the card's Formalization paragraph). Theorem 5.1 enters
only through Proposition 5.2, and through that only in the major-arc
comparison of Lemma 6.2. The other inputs are reproved in the text or
classical: the auxiliary-polynomial construction of
Lucier in Rice's prime-intersective form (Rice 2013, Section 2.1), rebuilt in
Section 2; Vaughan's identity and Weyl differencing; the chessboard estimate
of Fröhlich, Israel, Lieb and Simon (their Theorem 4.1), with related
graph-norm arguments of Hatami and of Conlon and Lee, cited for comparison
while the needed forms are proved directly; the Borel--Carathéodory lemma,
Cauchy's estimate, the Schur product theorem and Dirichlet approximation.
The method is adapted from
[[additive_combinatorics/openai_2026_power_saving_intersective_polynomial_differences/_index|the intersective-differences companion]],
whose Fourier-lift moment estimate is reproduced with proof as
Proposition 4.4.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this theorem.
