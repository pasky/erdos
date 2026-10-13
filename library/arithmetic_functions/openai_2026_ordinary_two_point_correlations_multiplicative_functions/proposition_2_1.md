---
name: arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/proposition_2_1
title: "Proposition 2.1: the Liouville two-point saving in every fixed residue class"
desc: |
  The progression form of the quantitative claim: lambda(n)lambda(n+h)
  restricted to any fixed class b mod l, unit or not, has ordinary average
  O((log X)^(-c)) at every real cutoff, with one absolute c; Theorem 1.1
  follows from it. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

Let $\lambda(n)=(-1)^{\Omega(n)}$ be Liouville's function.

**Proposition 2.1.** One absolute exponent $c>0$ serves every shift and
every residue class. Fix integers $h,l\ge1$ and any integer $b$, with
$\gcd(b,l)$ unrestricted, and normalize by $X$ the sum of
$\lambda(n)\lambda(n+h)$ over the $n\le X$ congruent to $b$ modulo $l$:

$$
F(X)=\frac1X\sum_{1\le n\le X}\mathbf 1_{n\equiv b\ (\mathrm{mod}\ l)}\,
\lambda(n)\lambda(n+h).
$$

Then $|F(X)|\ll_{h,l}(\log X)^{-c}$ at every real cutoff $X\ge3$.

Since $b$ matters only modulo $l$, the manuscript observes (p. 7), the
implied constant may be chosen uniformly in $b$. The proof gives
$c=\delta/(6WA)$ with $\delta=1/200$, where $A\ge1000$ is fixed by the
finite-law comparison of Lemma 3.1 and $W\ge10$ by the absolute trace
constant (Section 8.4); neither is computed.

**Source.** OpenAI, *Ordinary two-point correlations of multiplicative
functions*, release folder
`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026`;
TeX file `build/quantitative/01-setup.tex`, label `q:progression` (lines
7--18), PDF p. 7. The proof occupies Sections 2--8 and closes in Section 8.4
(`build/quantitative/07-spectral.tex`, lines 279--333, PDF pp. 42--43).
Provenance and attestations are on
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/_index|the card]].

**Read depth.** Claims checked: the statement, and the statements of Lemma 3.1
(finite residue comparison), Theorem 4.3 (the imported short-interval
theorem) and Theorem 5.4 (nonbacktracking moment), were read clause by clause
in the TeX source. The proof was read for its structure only; no step was
checked. Nothing here is independently reviewed.

## Proof pointer

The proof works above a threshold for $X$ depending on $h,l$, and fixes two
absolute constants, $A$ and then $W$. With $L=(\log X)^{1/A}$ and
$J=\lfloor\delta\log L/(6W)\rfloor$ it chooses $J$ disjoint supplies of primes
$p\equiv1\pmod5$, each of reciprocal mass between $W$ and $2W$ and all above
$\exp(L^{1-\delta})$, and a disjoint set of padding primes up to $e^L$ with
weight $4^{\omega(q)}$ on their squarefree products. A label $d$ takes one
prime from each supply. Pairs $(d,q)$ are grouped into bins on which
$\log(dq)$ varies by at most $\eta=e^{-J}$, and Lemma 2.2 says the bins keep
at least half the harmonic mass $SV_*$, where $S$ is the total padding mass and
$V_*\ge W^J$ the product of the supply masses.

For each bin the centered sum $C_j$ averages the products
$\mathbf 1_{q\mid n}\prod_{p\mid d}(\mathbf 1_{p\mid n}-1/p)$ times
$\lambda(n)\lambda(n+hqd)$, with the progression condition carried along.
Expanding the product, the term with every divisibility indicator returns $F$ at
a nearby cutoff by the substitution $n=qdm$ and complete multiplicativity,
giving the total $S_0F(X)$ up to $O(SV_*(\eta+X^{-1}))$. Every other term is a
correlation averaged over shifts $hz$ with $z$ a product of large primes;
Lemma 4.4 bounds it through the short-interval theorem of Matomäki, Radziwiłł
and Tao (Theorem 4.3 here) and a fourth-moment bound for exponential sums over
rough integers (Lemma 4.2), so that the centering error over all bins is small
(Lemma 4.1).

The centered sums are then bounded by a graph argument. The manuscript first
proves that integer averages of the residue tests it uses agree with an
independent-residue model to within $e^{-L^{10}}$ (Lemma 3.1), by encoding
residues as bits, correcting their law to exact bounded independence and
applying Braverman's theorem on bounded independence for constant-depth
circuits. In that model it deletes, at small cost, sites with too many padding
or supply primes, sites where padding mass concentrates in one bin, and the
sparse set of sites where a short "prohibited" path starts (Lemmas 4.5, 4.6
and 5.3). On blocks of consecutive sites it forms weighted symmetric edge
matrices $A_d$ and the nonbacktracking operator $H$, and Theorem 5.4 bounds
$\mathbb E\|H^k\|_{\mathrm{HS}}^2$ by $[K(C_2\sqrt W)^J]^{2k}$ with
$k=\lfloor L\rfloor$ and $K=e^{4J}$. Its proof expands the trace into closed
words, integrates singleton primes exactly before taking absolute values
(Lemma 5.5), discards words with many unlit occurrences, large-rank congruences
or many singletons (Sections 5.3 and 6), and counts the remaining repetition
patterns by a forest code uniform in the padding (Lemma 7.2), the padding
weights summing to at most $K$ per step (Lemma 7.3). Each repeated prime label
is summed once, which is where $\sqrt W$ in place of $W$ comes from.

Section 8 transfers the moment bound to the projected adjacency operator
(Lemma 8.1, Proposition 8.3), tests it against $\sqrt w\,\lambda$ on
overlapping blocks (Proposition 8.4), and sums over the $O(L/\eta)$ bins. After
division by $S_0\ge SW^J/2$ the graph contribution is
$(K/\eta)(C_3/\sqrt W)^J$, and $W$ is chosen with
$e^5C_3/\sqrt W\le e^{-1}$, so every error term is at most $e^{-J}$, which is
$\ll(\log X)^{-\delta/(6WA)}$. Bounded $X$ is absorbed into the constant.

## Dependencies

External inputs, taken at statement level; none was checked here. Theorem 1.3
of Matomäki, Radziwiłł and Tao (*An averaged form of Chowla's conjecture*,
corrected arXiv version v3), restated as Theorem 4.3: for real
$10\le H\le Z$, with an absolute implied constant,

$$
\sup_{\alpha\in\mathbb R}\int_0^Z
\Bigl|\sum_{x\le n\le x+H}\lambda(n)e(\alpha n)\Bigr|\,dx
\ll HZ\Bigl(\frac{\log\log H}{\log H}+(\log Z)^{-1/700}\Bigr),
$$

where $e(t)=e^{2\pi it}$. Braverman's theorem that polylogarithmic independence
fools constant-depth circuits (Corollary 2 of his 2010 paper). The prime number
theorem for the modulus $5$ (Theorem 12.1 of Koukoulopoulos, *The Distribution
of Prime Numbers*). The almost-to-exact independence correction of Alon,
Goldreich and Mansour and the fourth-moment treatment of Pilatte's Appendix C
are cited for their form and reproved; the graph constructions of Helfgott and
Radziwiłł and of Pilatte are adapted with proofs given.

## Bears on

No problem page is identified as using this result; the manuscript names no
Erdős problem.
