---
name: additive_combinatorics/openai_2026_power_saving_square_difference_free_sets/theorem_1_1
title: "Theorem 1.1: every subset of {1,...,N} with no positive square difference has at most C N^(1-c) elements"
desc: |
  The manuscript's main claim: absolute constants c > 0 and C such that every
  subset of {1,...,N} in which no difference is a positive square has at
  most C N^(1-c) elements, for every N >= 1. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

For a positive integer $N$ write $[N]=\{1,\ldots,N\}$. The manuscript calls
$A\subseteq[N]$ *square-difference-free* when no difference of two of its
elements is the square of a positive integer, that is,
$(A-A)\cap\{m^2:m\ge1\}=\varnothing$; the condition concerns differences of
integers, not residues. It writes $s(N)$ for the largest size of a
square-difference-free subset of $[N]$ (p. 2).

**Theorem 1.1.** There are constants $c>0$ and $C<\infty$, depending on
nothing, such that for every integer $N\ge1$ every square-difference-free
$A\subseteq[N]$ has $|A|\le CN^{1-c}$. Equivalently, $s(N)\le CN^{1-c}$: any
subset of $[N]$ with more than $CN^{1-c}$ elements has two distinct elements
whose difference, in absolute value, is the square of a positive integer.

The manuscript calls the exponent positive and absolute "but extremely
small" and says the argument gives no useful numerical value and no optimal
exponent (p. 2). Its proof takes $c=a_0/d$, where $d=(24!)^{161}$ is the size
of its slot set and $a_0\le\sigma_0/2$ with
$\sigma_0=\beta\gamma^2/(4000(d+1))$, $\beta=10^{-5}$, $\gamma=1/64$; so
$c<d^{-2}$ (this page's arithmetic from the stated parameter choices, not a
statement of the manuscript). It reads the theorem as an affirmative answer
to the fixed-power question posed by Green and Sawhney (their Section 1.1),
whose own bound is $s(N)\ll N\exp(-c_1\sqrt{\log N})$. The best lower bound
it cites is Krachun's $\liminf_{N\to\infty}\log s(N)/\log N\ge0.7527\ldots$.

Remark 1.2 (p. 2) states the coloring form. Shrink $c$ if needed so that
$0<c<1$; then for integers $r,N\ge1$ with $N>(Cr)^{1/c}$, every coloring of
$[N]$ with $r$ colors has elements $a$ and $a+d^2$, $d\ge1$, of one color,
since some color class has more than $CN^{1-c}$ elements. Equivalently, the
graph $G_N$ on $[N]$ joining two integers whose difference is a square has
chromatic number $\chi(G_N)\ge N/s(N)\ge C^{-1}N^c$.

**Formalization.** The release's Lean page for the family describes a
formalization of this statement, with the comparator theorem
`OAI.SquareDifference.power_saving`; it was read statically and not built
or audited here, and the catalog lists no entry for it at this revision (see
the card).

**Source.** OpenAI, *A power saving for square-difference-free sets*, release
folder
`preprints/A-power-saving-for-square-difference-free-sets-September-24-2026`;
TeX file `build/sections/introduction.tex`, label `thm:main` (lines 15--25), PDF
p. 2, with the definitions at lines 4--12 and Remark 1.2 at lines 32--46 (p. 2);
the proof closes in `build/sections/induction.tex`, where Theorem 9.2 (lines
201--301, PDF pp. 46--47) is followed by the proof of Theorem 1.1 (lines
303--318, PDF p. 47). Provenance and attestations are on
[[additive_combinatorics/openai_2026_power_saving_square_difference_free_sets/_index|the card]].

**Read depth.** Claims checked: the statement, the definitions it rests on,
Remark 1.2, and the statements of Lemma 4.2 (seminorm properties),
Proposition 9.1 (the recurrence) and Theorem 9.2 (decay of the functional)
were read clause by clause in the TeX source, with the statements of the
propositions the proof pointer names. The proof, Sections 2--9 (pp. 6--47),
was read for its structure only, as summarized below; no step was checked.
Nothing here is independently reviewed.

## Proof pointer

The proof replaces the density by a nonnegative multilinear quantity and
shows that this quantity decays like a power of $N$. Section 3 fixes a slot
set $V$ of $d=(24!)^{161}$ elements (tuples of $161$ permutation words on
$24$ symbols) with a designated directed cycle of $24$ slots, and, for every
prime $p$ at least an absolute threshold $P$, builds a probability law $\mu_p$
on labelings $V\to\mathbb F_p$ (Proposition 3.1). The law is reflection
positive for symbol swaps within a block, invariant under $z\mapsto qz+a$
with $q$ a nonzero square, has uniform single labels and mixes conditionally
(Lemma 3.6). Outside an exceptional part $\varepsilon_p$ of mass at most
$p^{-4}$, every designated cycle edge has a nonzero square difference, with
each edge pair uniform among such pairs. The finite-field counts of Section
2 (Lemmas 2.1--2.2) control the constraint systems used to build it. Taking
the product over the primes in $[P,N^\beta]$, $\beta=10^{-5}$, the functional
$Z(g)=\mathbb E\prod_{v\in V}g(z_v)$ obeys a signed Hölder inequality
(Proposition 4.1), so $Z(g)^{1/d}$ is a seminorm bounding $|\mathbb E g|$
(Lemma 4.2). The Fourier lift $G$ of $1_A$ keeps the rational Fourier
coefficients of $1_A$ at squarefree denominators up to $N^\beta$ from those
primes, read as a real function on $\prod_p\mathbb F_p$ with mean $|A|/N$
that may take negative values. Hence $(|A|/N)^d\le Y(N,A):=Z(G)$, and it
suffices to prove $Y(N,A)\le C_0N^{-a_0}$ (Theorem 9.2), which gives
$c=a_0/d$ and $C=C_0^{1/d}$ (p. 47).

Three estimates feed a recurrence for the largest value $\mathcal Y(N)$ of
$Y(N,A)$. First, every fixed moment of a lift, or of any part of it made of
complete denominator classes, is $N^{o(1)}$ (Lemma 5.2), fixing coordinates
costs an explicit power (Lemma 5.3), and an input with only large conductors
contributes a power saving (Lemma 4.3); together these justify the Fourier
truncations. Second, the scale comparison (Proposition 7.2): fixing the
coordinates at a set $B$ of primes with product $q_B\le N^\tau$ makes the low
coefficients exact averages over one residue class modulo $D=M_0q_B$, where
$M_0$ is $8$ times the product of the odd primes below $P$. Splitting that
class into progressions of step $D^2$ and rescaling gives
square-difference-free subsets of $[\lceil N/D^2\rceil]$, since a square
difference $m^2$ there would give the square difference $(Dm)^2$ in $A$.
Square-affine invariance and the triangle inequality then bound the
specialized functional by $\mathcal Y$ at that length, up to a factor tending
to $1$ and an error $O(N^{-\sigma_0})$.
Third, the cancellation (Proposition 8.2): write $1_A$ as an average over
residues $s$ modulo $M_0$ and call a tuple of residues good when every
designated cycle difference is $1$ modulo $8$ and a nonzero square at each
odd prime of $M_0$; good tuples have proportion $\rho\ge M_0^{-23}$ (Lemma
8.1). For a good tuple, the integral against the nonexceptional parts is
$O(N^{-\sigma_0})$. One cuts $[N]$ into about $N^\tau$ consecutive intervals.
Unless all $24$ cycle slots choose the same interval (probability
$O(N^{-23\tau})$), some cycle edge runs from an earlier interval to a later
one. Truncating and expanding the other slots and conditioning on their
primes leaves a bilinear sum for that edge weighted by the unit-square
multiplier $\mathfrak g$, which Proposition 6.1 bounds by $O(H^{-1/3})$,
$H=N^{\beta/2}$: a signed kernel supported on the actual squares $m^2$
vanishes between two ordered supports with no square difference.

Proposition 9.1 assembles these estimates. Expanding the product of the
full laws as the product of the nonexceptional parts plus an
inclusion--exclusion over nonempty sets $B$ of exceptional primes, the terms
with $q_B>N^\tau$ are bounded by moments and the summability
$\sum_Bq_B\eta_B\le1/4$, those with $q_B\le N^\tau$ by the scale comparison
at length $n_B=\lceil N/(M_0q_B)^2\rceil$, and non-good residue tuples by the
scale comparison with $B$ empty. The result is, with $u_N\to0$ and the sum
over nonempty $B$ with $q_B\le N^\tau$,

$$
\mathcal Y(N)\le KN^{-\sigma_0}+(1+u_N)\Bigl((1-\rho)\,
\mathcal Y(n_\varnothing)+\rho\sum_B\eta_B\,\mathcal Y(n_B)\Bigr).
$$

Theorem 9.2 closes it by strong induction, with
$a_0=\min\{1/4,\sigma_0/2,\log(1/r)/(4\log M_0)\}$ and $r=1-3\rho/4$, chosen so
that the loss $M_0^{2a_0}$ from passing to the shorter length is outweighed
by the factor $r<1$.

## Dependencies

Proved inside the manuscript: Lemmas 2.1--2.2, Proposition 3.1 with Lemmas
3.2--3.6, Proposition 4.1 and Lemmas 4.2--4.3, Lemmas 5.2--5.3, Proposition
6.1, Lemma 7.1 and Proposition 7.2, Lemma 8.1 and Proposition 8.2,
Proposition 9.1 and Theorem 9.2. Standard facts used and derived in the
text: the modulus of quadratic Gauss sums modulo prime powers, Dirichlet
approximation, Weyl differencing, the Chinese remainder theorem and the
convergence of $\prod_p(1+p^{-3})$. Cited as precedents, not imported: the
chessboard estimates of Fröhlich and Lieb (Theorem 2.2) and of Fröhlich,
Israel, Lieb and Simon (Theorem 4.1), whose inequality the manuscript proves
directly for its law; the large sieve of Montgomery and Vaughan (Theorem 1),
replaced by an elementary Gram-matrix bound; the decoupling of de la Peña and
Montgomery-Smith (Section 4); Green and Sawhney (Sections 3 and 5, Lemma
6.2), Bloom and Maynard (Theorem 2) and the Main Lemma of Pintz, Steiger and
Szemerédi as methodological antecedents. None was checked here.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this result; the card's Bears on section records the pages read and
why none qualifies.
