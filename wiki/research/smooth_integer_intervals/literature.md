---
name: research/smooth_integer_intervals/literature
title: Every-interval smooth-number theorems matched at the diagonal
desc: |
  Each located theorem on smooth integers in every short interval, read at
  its exact interval length and smoothness, with the diagonal exponent it
  gives for k(n) in Problem 962, including the classical 2/5 exponent,
  the parameter mismatch in recent results, and Bourgain's analytic
  input for the project bound 38/97+epsilon.
tags: [E0962, literature]
sources:
- problems/integer_sequences/E0962
created: 2026-10-15T22:27:51Z
updated: 2026-10-15T22:27:51Z
---

# Every-interval smooth-number theorems matched at the diagonal

***

This page supports the
[[research/smooth_integer_intervals/proof_sketch|proof sketch for upper bounds on k(n)]].
Problem 962 needs, for every block $(m,m+K]$ with $m\le n$, a member whose
prime factors are all at most $K$: the interval length and the smoothness
bound are the same number. The comparison here applies a theorem with
interval length $x^\beta$ and smoothness $x^\alpha$ by scaling with a
multiplier. The sketch shows that this application never goes below
$\beta$ and gives $\alpha/(1+\alpha-\beta)$ when $\beta\le\alpha$.
This limits that application, not every possible use of the theorem.
Each entry records what was read and how deeply.

## Theorems that bear on the diagonal

**Erdős and Sárközy (1979).** P. Erdős and A. Sárközy, On the prime factors
of $\binom nk$ and of consecutive integers, Utilitas Math. 16 (1979),
197--215; public scan in
[the Rényi Institute's Erdős archive](https://static.renyi.hu/~p_erdos/1979-15.pdf).
Theorem 2 (printed p. 198): $n_k>k^{5/2}/16$ for $k>k_0$, with $n_k$ the
smallest $n$ such that $P(n+i)>k$ for $1\le i\le k$ (printed p. 197). The
definition and the statement were checked on page images of the scan; the
proof in section 3 was read in the scan's text layer. The construction
is the one-multiplier near-square adjustment, and the theorem gives the
exponent $2/5$ for $k(n)$; L250 restates it with explicit constants.

**Friedlander and Lagarias (1987).** J. B. Friedlander and J. C. Lagarias,
On the distribution in short intervals of integers having no large prime
factor, J. Number Theory 25 (1987), 249--273. Read in the
[authors' manuscript](https://websites.umich.edu/~lagarias/doc/short.pdf):
the definition of $f(\alpha)$, the infimum of the $\beta$ such that, for
every $\alpha_1>\alpha$, every interval $(x-x^\beta,x]$ with sufficiently
large $x$ contains an $x^{\alpha_1}$-smooth integer; Theorem 3,
$f(\lambda\alpha)\le\lambda f(\alpha)+1-\lambda$; Theorem 4,
$f(1/r)\le1-2/r+1/(r2^{r-1})$, with the case $r=2$ credited also to Balog
and Sárközy. Statements, with the proof of Theorem 3 and the start of the
proof of Theorem 4. Diagonal: $f(1/2)\le1/4$ gives $2/5$ (with an
$\varepsilon$ of slack); $f(1/3)\le5/12$ gives $5/12$; for $r\ge4$ the
bound of Theorem 4 exceeds $1/2$. Translating the endpoint and allowing
arbitrarily small power slack gives the forward-interval form used for
the comparison.

**Harman (1999).** G. Harman, Integers without large prime factors in short
intervals and arithmetic progressions, Acta Arith. 91 (1999), 279--289.
Theorem 2 (printed p. 280), read on the public archive scan at statement
level: for $y=x^\gamma$ with $3/7<\gamma<1/2$, with $\theta(\gamma)$ an
infimum over known exponent pairs, if $\theta(\gamma)<\gamma$ then
$\Psi(x+y,u)-\Psi(x,u)\gg y$ for $u\ge x^{\varrho\theta+\varepsilon}$,
$\varrho=e^{-1/2}$. The value $\theta=(3-5\gamma)/2$ on
$3/7<\gamma\le1/2$ is conditional on the exponent pair conjecture; with the
pairs known in 1999 the author remarks that the result holds down to some
$\gamma$ between $0.45$ and $0.46$. Since the smoothness exponent
$\varrho\theta(\gamma)$ is below $\gamma$, scaling gives a diagonal
exponent of at least $\gamma$: above $0.45$ unconditionally, above $3/7$
under the conjecture. The $0.45$ comparison uses the pairs in the author's
1999 discussion; the theorem's restriction $\gamma>3/7$ itself already
prevents an improvement of $2/5$ through scaling. For a concrete further
match, inserting Bourgain's pair from L253 into Harman's formula (1.2)
makes $\theta(\gamma)<\gamma$ whenever
$\gamma>(139+84\eta)/(307+84\eta)$, so it supplies every fixed interval
exponent above $139/307\approx0.4528$ by taking $\eta$ small enough.
This is an application calculated here, not a claim that the infimum over
all available pairs equals that value. Granville's survey
(2008, section 4.1, printed p. 295)
reports the range $1/2\ge\beta\ge3/7$ with $\alpha>(3-5\beta)/(2\sqrt e)$
without stating this condition; the original's hypotheses govern.

**Weingartner (2023).** *Somewhat smooth numbers in short intervals*,
Ramanujan J. 60 (2023), 447--453, read as
[arXiv:2105.13568v2](https://arxiv.org/abs/2105.13568v2), Theorem 1,
Corollaries 1--3 and Table 1 at statement depth, with the opening divisor
count in the proof of Theorem 1. This is a uniform result with smoothness
$y\ge\sqrt{2x}$ and length

$$
z\ge A\min\left(x^{\vartheta},
x^{\ell/(1+\kappa)}y^{(\kappa-\ell)/(1+\kappa)}\right),
$$

where $(\kappa,\ell)$ is an exponent pair and the reported value of
$\vartheta$ is $517/1648+\varepsilon>1/4$. At $y=x^\alpha$ with
$\alpha\ge1/2$, the second interval exponent is
$\beta=((1-\alpha)\ell+\alpha\kappa)/(1+\kappa)$.
Since $\ell\ge1/2$ and $\kappa\ge0$, it obeys
$\beta\ge(1-\alpha)/2$; the first exponent $\vartheta$ also obeys that
inequality. Scaling therefore gives a diagonal exponent at least
$2\alpha/(1+3\alpha)\ge2/5$. This comparison covers the whole stated
exponent-pair family, even its conjectured limit. The paper also states
the near-square single-witness bound with smoothness $\sqrt{2x}$ and
length $3x^{1/4}$, which scales to the classical $2/5$.

**[[../library/number_theory/bourgain_2017_decoupling_exponential_sums_riemann_zeta/theorem_6|Bourgain (2017), an analytic input]].** *Decoupling, exponential sums and
the Riemann zeta function*, J. Amer. Math. Soc. 30 (2017), 205--224;
[arXiv:1408.5794v2](https://arxiv.org/abs/1408.5794v2), Section 5,
Theorem 6 and its proof discussion read in the primary text. It proves
that $(13/84+\eta,55/84+\eta)$ is an exponent pair for every $\eta>0$,
including the monomial phase and parameter range used in
[[theory/integer_sequences/L253_exponent_pair_smooth_blocks/_proof|L253's derivation of the diagonal bound 38/97+epsilon]].
This is a project application of the source theorem, not a smooth-block
theorem stated by Bourgain. The full decoupling proof is an external
dependency and was not independently verified here.

## Results at the square-root scale or longer

These give no exponent below $1/2$ by scaling, because their interval
exponent is at least $1/2$.

- Balog, On the distribution of integers having no large prime factor,
  Astérisque 147--148 (1987), 27--31: the statement and its deduction on
  printed pp. 27--28 (text layer, partly garbled): smoothness $x^\alpha$ for
  every fixed $\alpha>0$ in intervals of length $x^{1/2+\varepsilon}$.
- Harman (1999), Theorem 1 (printed p. 279): intervals $[x,x+x^{1/2}]$,
  smoothness $x^{\varrho/4+\varepsilon}$.
- Croot, Smooth numbers in short intervals (author manuscript, 2006),
  Theorem 1: intervals of length $c(\varepsilon)\sqrt x$, smoothness
  $x^{47/(190\sqrt e)+\varepsilon}$; statement only. Granville cites a
  different version with a different constant.
- Matomäki and Radziwiłł (2016), filed in the library:
  [[../library/primes/matomaki_2016_multiplicative_functions_short_intervals/corollary_1|its Corollary 1 gives X^epsilon-smooth numbers in every interval of length C(epsilon) sqrt(X)]],
  at the square-root scale, and
  [[../library/primes/matomaki_2016_multiplicative_functions_short_intervals/corollary_6|its Corollary 6 counts smooth numbers only in almost all short intervals]],
  so it cannot control an exceptional block.
- Jain, Smooth numbers in short intervals, arXiv:2502.10530v1, Theorems
  1.1 and 1.2 (statements): Theorem 1.2 holds in every interval but needs
  length at least $\sqrt x\,e^{(1+\varepsilon)W}$, where
  $W=\frac{11}{16}u\log u+2\log\log x$ and $u=\log x/\log y$; Theorem
  1.1 is an almost-all result. A 2026 journal version (Quart. J. Math.
  77, 397--422) exists; its final statements were not read.
- Younis, Asymptotics for smooth numbers in short intervals,
  arXiv:2409.05761v1, Theorem 1.1 (statement): lengths $x^\theta$ with
  $\theta>17/30$.

Almost-all theorems (Friedlander and Lagarias's Theorem 6,
Hildebrand--Tenenbaum, Jain's Theorem 1.1, Matomäki and Radziwiłł's
Corollary 6) do not apply to $k(n)$ at all: the one bad block may lie in the
exceptional set.

## Related methods and different problems

- Rivat and Shparlinski, Multiples of squares in short intervals, Funct.
  Approx. Comment. Math. 54 (2016), 57--63: by its abstract, exponent pairs
  and Vaaler polynomials give a multiple $m^2r$ of a square in every
  interval $[x,x+x^{1/2}]$ with $m>x^{0.281286}$. It is the closest method
  precedent for the multiplier sum of L251, in a different range: there the
  interval has length $x^{1/2}$ and the square root $m$ should be large,
  while L251 needs $cq^2$ in windows of length about $x^{4/7}$ with
  $q\asymp x^{11/28}$ capped by $K$ and the multiplier in a dyadic range.
  The full text was not accessible; only the abstract was read.
- van Doorn and Tang, Consecutive integers free of certain prime factors,
  arXiv:2606.19863 (abstract): their $n_k$ is the least $n>2k$ such that
  $(n-k)\cdots(n-1)$ has no prime factor in $(k,2k)$, a different function;
  their superpolynomial lower bound says nothing about $k(n)$ of Problem
  962.
- An author report on Problem 962 at
  [erdosproblemaday.com/report/962](https://www.erdosproblemaday.com/report/962)
  (accessed 2026-10-15) claims $k(n)<n^{0.46}$ through a theorem of Laishram
  and Murty, Grimm's conjecture and smooth numbers, Michigan Math. J. 61
  (2012), 151--160. Their abstract (arXiv:1306.0765) proves $g(n)=O(n^\alpha)$
  with $0.45<\alpha<0.46$ for Grimm's function $g(n)$, the same range that
  Harman's Theorem 2 reaches with known exponent pairs; the paper itself was
  not read, and the exponent is weaker than $2/5$ in any case.

## Search record

A search on 2026-10-15 for every-interval results with a diagonal exponent
below $2/5$, or for improvements of $n_k>k^{5/2}/16$, found none. It covered
web searches on the phrases "every interval" smooth exponent below $2/5$,
"maximal gaps between smooth numbers", "Erdős problem 962" with $n^{2/5}$,
"$n_k$" with $k^{5/2}$ and with "prime factor greater than $k$", and
multiples of squares or almost squares in short intervals with the
exponents $11/28$ and $38/97$; the zbMATH review of the 1979 paper (Zbl
0419.10040); a
zbMATH query for documents whose reference lists contain that paper (no
records returned, which is weak evidence since older reference lists are
often incomplete); the arXiv listing API; and the EuDML record of Harman's
paper. The sources above were then read at the depths stated. This is a
bounded search, not a novelty certificate: MathSciNet and Google Scholar
were not searched, and Balog and Sárközy's papers on sums of integers with
small prime factors (Studia Sci. Math. Hungar. 19 (1984), 35--47 and
81--88), which Friedlander and Lagarias credit for the case $r=2$, were not
read.
