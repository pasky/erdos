---
name: arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/theorem_1_2
title: "Theorem 1.2: the binary corrected Elliott conjecture for ordinary averages"
desc: |
  The manuscript's qualitative claim: for multiplicative f_1, f_2 with values
  in the closed unit disk, one of them uniformly nonpretentious, and distinct
  shifts, the ordinary average of f_1(n+h_1)f_2(n+h_2) tends to zero, with no
  rate. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-14T07:41:33Z
---

***

## Statement

Write $\mathbb D=\{z\in\mathbb C:|z|\le1\}$ for the closed unit disk. The
manuscript's functions (p. 4) map the positive integers into $\mathbb D$ and
are multiplicative only in the weak sense: $f(mn)=f(m)f(n)$ is required just
for coprime $m,n$. Its measure of how closely $f$ imitates a twisted character
$\chi(n)n^{it}$, for a Dirichlet character $\chi$ and real $t$, using the
primes up to $X\ge2$, is the pretentious distance $D(f,\chi n^{it};X)\ge0$,
whose square is

$$
D(f,\chi n^{it};X)^2=\sum_{p\le X}
\frac{1-\operatorname{Re}\bigl(f(p)\overline{\chi(p)p^{it}}\bigr)}{p}
\qquad\text{(1.1)},
$$

the sum running over primes. Uniform nonpretentiousness asks that this
distance grow without bound even after minimizing over heights $|t|\le N$,
with the primes cut off at the same $N$: $f$ is uniformly nonpretentious
when, for each fixed Dirichlet character $\chi$,

$$
\inf_{|t|\le N}D(f,\chi n^{it};N)\to\infty\qquad(N\to\infty)
\qquad\text{(1.2)}.
$$

**Theorem 1.2.** Suppose $f_1,f_2:\mathbb N\to\mathbb D$ are multiplicative
and $f_1$ or $f_2$ is uniformly nonpretentious. Then for any two fixed
distinct shifts $h_1\ne h_2$, both nonnegative integers, the ordinary average
of the shifted product vanishes in the limit:

$$
\frac1N\sum_{n=1}^Nf_1(n+h_1)f_2(n+h_2)\to0
\qquad(N\to\infty,\ N\in\mathbb N).
$$

On p. 4 the manuscript stresses the generality: complex values are allowed,
$|f_i|$ may fall below $1$, and only multiplicativity on coprime arguments is
used. The product is taken without complex conjugation; the conjugated
product follows from the theorem itself, because conjugating $f$ leaves (1.2)
intact. No rate of decay is claimed for this class. The manuscript identifies
(1.2) with the corrected condition of Matomäki, Radziwiłł and Tao (their
Section 1.1 and Appendix B) and presents the theorem as the binary corrected
Elliott conjecture for ordinary averages. For $\lambda$, Lemma 18.5 (p. 85)
gives (1.2) in quantitative form,
$\inf_{|t|\le X}D(\lambda,\chi n^{it};X)\ge\frac14\sqrt{\log\log X}-O_\chi(1)$
for $X\ge100$, and the closing paragraph of Section 18 (p. 86) observes that
$\mu$ has the same distances as $\lambda$, so any pair drawn from
$\{\lambda,\mu\}$ qualifies.

**Formalization.** The release's Lean page for the family describes a
formalization of this statement, in two comparator theorems, each named
`binary_corrected_elliott`. In words, each says: if complex functions
$f_1,f_2$ on the natural numbers are multiplicative on coprime positive
arguments and bounded by one, and one of them is uniformly nonpretentious,
then $N^{-1}\sum_{n=1}^Nf_1(n+h_1)f_2(n+h_2)\to0$ for all natural numbers
$h_1\ne h_2$. The one in `OrdinaryTwoPointCorrelations.lean` bounds the
functions at positive arguments and writes (1.2) as: for each modulus
$q\ge1$, character $\chi$ modulo $q$ and real $K$, once $N$ is large the
squared distance up to $N$ is at least $K$ for every $|t|\le N$. The one in
`OrdinaryElliott.lean` bounds them at every argument and writes (1.2) as the
infimum above. Both were read statically and not built or audited here, and
the release's catalog lists no entry for either at this revision (see the card).

**Source.** OpenAI, *Ordinary two-point correlations of multiplicative
functions*, release folder
`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026`;
TeX file `build/introduction.tex`, label `thm:elliott` (lines 64--72), with
`eq:distance` (lines 51--55) and `eq:unp` (lines 58--61), PDF p. 4. The proof is
Part II: the reduction is in `build/qualitative/analytic-transfer.tex` (lines
251--275, PDF p. 49), and the deferred graph estimate closes at the end of
Section 17 (`build/qualitative/localization.tex`, lines 144--167, PDF p. 81).
Provenance and attestations are on
[[arithmetic_functions/openai_2026_ordinary_two_point_correlations_multiplicative_functions/_index|the card]].

**Read depth.** Claims checked: the statement, the definitions (1.1) and (1.2),
and the statements of Proposition 10.1 (divisor graph estimate),
Proposition 11.4 (analytic centering), Theorem 12.2 (the imported short-interval
theorem), Theorem 13.3 (high trace) and Lemma 18.5 were read clause by clause in
the TeX source. The proof, about 37 pages, was read for its structure only; no
step was checked. Nothing here is independently reviewed.

## Proof pointer

The argument is by contradiction, with the graph fixed before the long average
is taken. A multiplicative function with $f(1)=0$ vanishes, so both functions
may be normalized by $f(1)=1$. If $\sum_p(1-|f_i(p)|)/p$ diverges for either
function, its mean modulus tends to zero by a periodic majorant (Lemma 11.1). A
translation reduces the shifts to $0$ and $h\ge1$. Suppose
$|\sum_{m\le N_j}f_1(m)f_2(m+h)|\ge\gamma N_j$ along integers $N_j\to\infty$.

At an auxiliary scale $B$ the manuscript takes a core band of primes with
$B^{1-\varepsilon/100}<\log p\le B$, each weighted by a large constant $A$, and
a center band with $B^{1-\varepsilon}<\log p\le B^{1-\varepsilon/100}$, weighted
$1$, where $\varepsilon=10^{-4}$; $L_0$ is the total weighted reciprocal mass of
the squarefree band products. Lemma 11.2 finds one short multiplicative interval
$(H,\tau H]$ of such products $d$, with at most $C_0\log B$ prime factors and
$|f_1(d)f_2(d)|\ge1/2$, carrying weighted mass $\gg L_0/B$. Restricting to
$x=dm$ and using multiplicativity, Lemma 11.3 turns the bias into a raw sum with
divisibility indicators and residue cutoffs on the core primes whose average up
to $X_j=HN_j$ is at least $c_\gamma L_0/B$ in the limit. Proposition 11.4
replaces each center-band indicator by $\mathbf 1_{p\mid x}-\theta/p$ with
$\theta=1/4$ at a cost $O(L_0(B^{-1-\varepsilon}+J/P_0))$: the expanded terms
are correlations averaged over shifts by rough integers, handled by Fourier
inversion of the cutoffs (which keeps the twisted functions uniformly
nonpretentious, Lemma 12.1), the short exponential-sum theorem of Matomäki,
Radziwiłł and Tao for general multiplicative functions (Theorem 12.2) and sup
and fourth-moment bounds for the rough-number multiplier (Lemma 12.3).
Proposition 10.1 bounds the centered sum by $O(L_0B^{-1-c_*/2})$ with
$c_*=\varepsilon/100$, for arbitrary bounded test functions. Dividing by
$L_0/B$ gives
$c_\gamma\le C(B^{-c_*/2}+B^{-\varepsilon}+BJe^{-B^{1-\varepsilon}})$, which
fails for large $B$.

Proposition 10.1 rests on the high-trace bound, Theorem 13.3. Vertices where a
short primitive path specification qualifies are deleted; they have density at
most $P_0^{-1+o(1)}$ with $P_0=\exp(B^{1-\varepsilon})$. The sum over closed
lines of length $\ell=2\lfloor B\rfloor$ of the absolute residue averages of the
normalized edge products is at most $B^{-(1+c_*)\ell}$. The proof keeps lines
with connected activity on the first-visit tree (Proposition 14.1), replaces the
deletion by short lists of qualifying specifications through a truncated sieve
on an intersection poset (Proposition 15.3), and sums the trace with a
weighted-subtree identity (Section 16). There a center prime occurring on a
single good edge cancels because $\theta=1/4$ is the square of the center-band
vertex factor $\beta_Z=1/2$, the core band supplies pivot savings, and
exceptional configurations are removed by triangular arithmetic constraints
(Lemma 13.7). Section 17 passes to long intervals: block matrices on intervals
of length about $B^{10}H$, a singular-value moment averaged over residues, a
negligible set of exceptional blocks and a Cauchy--Schwarz bilinear bound.

## Dependencies

External inputs, taken at statement level; none was checked here. Theorem 1.7
of Matomäki, Radziwiłł and Tao in its corrected version (arXiv v3), restated as
Theorem 12.2: for $X\ge D\ge10$ and a $1$-bounded multiplicative $b$, with
$Q=\min((\log X)^{1/125},(\log D)^5)$ and $\mathcal M(b;X,Q)$ the infimum of
$D(b,\chi n^{it};X)^2$ over $|t|\le X$ and characters $\chi$ of modulus at
most $Q$, with an absolute implied constant,

$$
\sup_{\alpha}\int_0^X
\Bigl|\sum_{y<m\le y+D}b(m)e(\alpha m)\Bigr|\,dy
\ll DX\Bigl(e^{-\mathcal M(b;X,Q)/20}+\frac{\log\log D}{\log D}+
(\log X)^{-1/700}\Bigr),
$$

where $e(t)=e^{2\pi it}$. Mertens' estimates for the band masses. Rota's Möbius
function of a finite poset (his 1964 paper, Section 3 and Proposition 6) for the
sieve truncation, and the Erdős--Szekeres monotone-subsequence theorem in
Lemma 14.4. The constructions of Helfgott and Radziwiłł and of Pilatte
(prohibited paths, intersection rank, triangular constraints) are adapted with
proofs given. Lemma 18.5 uses Lemma C.1 of Matomäki, Radziwiłł and Tao and the
prime number theorem in progressions.

## Bears on

No problem page is identified as using this result; the manuscript names no
Erdős problem.
