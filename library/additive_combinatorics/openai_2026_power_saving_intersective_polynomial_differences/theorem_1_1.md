---
name: additive_combinatorics/openai_2026_power_saving_intersective_polynomial_differences/theorem_1_1
title: "Theorem 1.1: sets avoiding nonzero values of an intersective polynomial of degree k as differences have O_h(N^(1-c_k)) elements"
desc: |
  The manuscript's main claim: for each degree k >= 2 an exponent c_k > 0,
  depending only on k, such that subsets of {1, ..., N} with no difference
  equal to a nonzero value h(n), n >= 1, of an intersective h of degree k with
  positive leading coefficient have at most C_h N^(1-c_k) elements. Claims
  checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Let $\mathbb N_+=\{1,2,\ldots\}$ and $[N]=\{1,\ldots,N\}$, and let $A-A$ be
the set of all differences $a-b$ with $a,b\in A$. In the manuscript's sense a
polynomial $h\in\mathbb Z[x]$ is intersective if it has a root modulo every
positive integer $q$, that is, $q$ divides $h(t)$ for some integer $t$
depending on $q$. Different moduli may take their roots from different
factors of $h$, so $h$ need not have a rational root (p. 2).

**Theorem 1.1.** Fix an integer $k\ge2$. There is an exponent
$c_k\in(0,1)$, determined by $k$ alone, with the following property. Let
$h\in\mathbb Z[x]$ be intersective of degree $k$ with positive leading
coefficient. Then for some constant $C_h\ge1$ and some integer $N_h\ge1$,
every set $A\subseteq[N]$ with $N\ge N_h$ and
$(A-A)\cap h(\mathbb N_+)\subseteq\{0\}$ has at most $C_hN^{1-c_k}$ elements.

The order of choice matters: $c_k$ is fixed by $k$ before $h$ is chosen,
while $C_h$ and $N_h$ are allowed to depend on all the coefficients of $h$,
and $h$ is held fixed as $N\to\infty$. The hypothesis says that no two
elements of $A$ differ by a nonzero value $h(n)$ with $n\ge1$; as $A-A$ is
symmetric, neither $h(n)$ nor $-h(n)$ is a difference, and values $h(n)=0$
impose nothing (p. 2). The proof takes $N_h=M$ and
$C_h=2^{1-c_k}M^{c_k}C_0^{1/d}$, where $M$ comes from the normalization of
Lemma 2.1 and $C_0$ from Proposition 7.2, and sets $c_k=a_0/d$ with $a_0$ and
$d$ fixed by explicit formulas in $k$ and the two prime thresholds $P_1$ and
$P$, which are chosen only as large enough in terms of $k$; no numerical
value of $c_k$ is given, and $C_0$ is not made explicit.

The manuscript sets this beside the bound
$N\exp(-c_{h,\mu}(\log N)^\mu)$, for every fixed $0<\mu<1/2$, that it
attributes to Adajar et al. (arXiv:2605.16216v2, Theorem 1.1): "Theorem 1.1
gives a fixed power of $N$ as the saving, with an exponent common to all
polynomials of each fixed degree" (p. 3).

**Source.** OpenAI, *A power saving for intersective polynomial differences
with an exponent depending only on the degree*, release folder
`preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026`;
TeX file `build/manuscript/sections/introduction.tex`, label `thm:main`
(lines 14--26), PDF p. 2; the proof closes at the end of Section 7
(`build/manuscript/sections/induction.tex`, lines 300--363, PDF pp. 45--46).
Read 2026-10-12. Provenance and attestations are on
[[additive_combinatorics/openai_2026_power_saving_intersective_polynomial_differences/_index|the card]].

**Read depth.** Claims checked: the statement, the definitions and notation
it rests on (`introduction.tex`, lines 3--12) and the remarks after it
(lines 28--31), and the statements of Condition (U), Lemmas 2.1 and 2.2,
Corollary 4.6 and Propositions 7.1 and 7.2 were read clause by clause in the
TeX source. The proof (Sections 2--7, pp. 5--46) was read for its structure
only, as summarized below; no step was checked. Nothing here is
independently reviewed.

## Proof pointer

The proof first normalizes $h$ and then bounds a multilinear density
quantity by an induction on the scale that runs over a whole family of
polynomials at once.

Normalization and the family (Section 2). Fix a compatible root
$\mathfrak z_p\in\mathbb Z_p$ of $h$ at every prime. Lemma 2.1 replaces $h$ by
$g(x)=h(r+D_0x)/M\in\mathbb Z[x]$, where $D_0$ and $M$ are built from the
finitely many primes at which the first nonzero Taylor coefficient at
$\mathfrak z_p$ is not a unit; $g$ is intersective of degree $k$, that
coefficient is a unit at every prime (Condition (U)), and $Mg(n)=h(r+D_0n)$
with $r+D_0n\ge1$. Lucier's auxiliary construction gives polynomials
$h_l=h(r_l+lx)/\lambda(l)$, $h_1=h$, with $\lambda$ completely
multiplicative and $h_l(Dx-i)=\lambda(D)h_{lD}(x)$ (Lemma 2.2), so a set
avoiding $h_l$-differences inside a progression of step $\lambda(D)$ becomes,
rescaled, a set avoiding $h_{lD}$-differences. Under (U), the local inputs,
namely complete exponential sums at large primes (Lemma 2.3), derivative
bounds and lifting at small primes (Lemmas 2.4--2.5) and zero-sum cycles of
admissible residues of one length $L$ (Lemma 2.6), hold uniformly in $l$ with
parameters depending only on $k$.

Tuple laws and the density quantity (Sections 3--4). For each prime $p\ge P$
a probability law on $\mathbb F_p^V$, $|V|=d$ even, is built as a mixture of
measures indexed by marked blocks, so that it is reflection positive across a
fixed family of cuts and, off an exceptional part of mass at most $p^{-4}$,
its increments along a designated $L$-cycle of slots are values of $h_l$ at
regular arguments; it is carried exactly to the law for $lD$ by
$z\mapsto\lambda(D)^{-1}(z-a')$ and mixes conditionally (Proposition 3.5,
Lemmas 3.6--3.7). Reflection positivity gives a signed Hölder inequality and
a seminorm (Proposition 4.1, Lemma 4.2). Integrating the product, over the
$d$ slots, of the Fourier lift of $1_A$ (its coefficients at squarefree
denominators at most $N^\beta$ with all prime factors at least $P$) gives
$Y_l(N,A)$, with
$(|A|/N)^d\le Y_l(N,A)\le C_\epsilon N^\epsilon$ (Corollary 4.6).

Cancellation and comparison (Sections 5--6). Proposition 5.1 uses avoidance
through a signed kernel supported on positive values of $h_l$ whose Fourier
transform matches, up to a negative power of $N$, that of a model kernel
built from the pair multiplier of a cycle edge (Weyl differencing on minor
arcs, local coefficients on major arcs); its
bilinear form vanishes on two ordered pieces of an avoiding set. With it,
Proposition 6.4 gives a saving $N^{-\sigma}$ for the residue assignments
modulo $M_0$ whose cycle increments are admissible, a proportion at least
$\rho_*=M_0^{1-L}$ (Lemma 6.3), when $l\le N^\zeta$. The other assignments,
and the exceptional terms once their prime labels are fixed, are instead
compared with the maximal functional $\mathcal Y_{lD}$ at the shorter scale
$\lceil N/\lambda(D)\rceil$, with a factor tending to one (Proposition 6.2).

Induction and conclusion (Section 7). These combine into the recurrence of
Proposition 7.1. Proposition 7.2 proves
$\mathcal Y_l(N)\le C_0l^{b_0}N^{-a_0}$ for all positive $l,N$ by strong
induction on $N$, simultaneously in $l$: the factor $l^{b_0}$ lets the
trivial bound of Corollary 4.6 cover $l>N^\zeta$, where the recurrence is
unavailable, and $a_0$ is chosen so that the recurrence contracts by a fixed
factor below one. Under (U), $a_0$, $b_0$ and $d$ depend only on $k$, and
$c_k=a_0/d$. Applied to $g$ at $l=1$, density domination gives
$|B|/n\le C_0^{1/d}n^{-c_k}$ for every $B\subseteq[n]$ avoiding nonzero
$g$-differences; splitting $A$ into its residue classes modulo $M$ and using
$Mg(m)=h(r+D_0m)$ transfers the bound to $h$ (pp. 45--46).

## Dependencies

External inputs, taken at statement level; none was checked here. Lucier's
auxiliary-polynomial construction (Section 8 of his Acta Arithmetica paper),
including the fact cited from it that the construction preserves the
valuation of the first nonzero coefficient; the manuscript writes out the
construction and its inheritance rule and proves that valuation fact itself
in Lemma 2.2. The release's square-difference manuscript, whose tuple laws,
signed functional, lift moments, kernel, comparison, contraction and
induction are adapted: in the released text, its Lemmas 2.1--2.2,
Section 3, Proposition 4.1, Lemmas 4.2--4.3 and 5.2--5.3, Section 6,
Propositions 7.2, 8.2 and 9.1 and Theorem 9.2. This manuscript cites the lift
lemmas as Lemmas 5.1--5.2, the contraction result as Proposition 8.1 and the
recurrence and decay results as Proposition 9.2 and Theorem 9.3, and it says
that every estimate it needs from that method is proved in the text. The
chessboard method of Fröhlich, Israel, Lieb and Simon (their Theorem 4.1),
followed for the signed Hölder inequality, with Hatami and Conlon--Lee cited
for related reflection arguments. Rice's revised version (Sections 2.4--2.5
and 4) is cited for similar restrictions on derivatives and lifting.

## Bears on

No problem page is identified as using this result; the manuscript names no
Erdős problem.
