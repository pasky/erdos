---
name: unit_fractions/croot_1999_unit_fractions_denominators_short_intervals/main_theorem
title: "Main Theorem: unit fractions with denominators in (N, (eʳ+o(1))N]"
desc: |
  Every positive rational r is a sum of distinct unit fractions with
  denominators between N and (e^r + O_r(log log N / log N)) N, with a
  best-possible error term.
created: 2026-09-17T11:30:00Z
updated: 2026-10-08T01:29:58Z
---

***

## Statement

**Main Theorem** (p. 100). "Suppose that $r>0$ is any given rational
number. Then, for all $N>1$, there exist integers $x_1,\ldots,x_k$, with

$$
N<x_1<\cdots<x_k\ \le\ \Bigl(e^r+O_r\Bigl(\frac{\log\log N}{\log N}\Bigr)\Bigr)N
$$

such that

$$
r=\frac{1}{x_1}+\cdots+\frac{1}{x_k}.
$$

Moreover, the error term $O_r(\log\log N/\log N)$ is best possible."

**Source.** E. S. Croot III, *On unit fractions with denominators in short
intervals*, Acta Arith. 99 (2001), no. 2, 99--114, doi:10.4064/aa99-2-1,
the held edition named on the
[[unit_fractions/croot_1999_unit_fractions_denominators_short_intervals/_index|source card]];
Main Theorem on p. 100; proof of the existence part on p. 104 from
Proposition 1 (p. 103; proof Section IV, pp. 107--110) and Proposition 2
(p. 103; proof Section V, pp. 110--112, through Lemma 5, p. 112, proved in
Section VI, pp. 112--114); proof of the sharpness on pp. 105--107. The
published introduction (pp. 99--100) states the two questions of Erdős and
Graham in a corrected form (Problem 284 uses it; for the width the paper
asks for $\sim k$ where Problem 286 keeps the monograph's $(e-1+o(1))k$) and
says that the theorem "solves these questions of Erdős and Graham for
infinitely many $k$". The arXiv preprint arXiv:math/9904181v1 (30 April
1999), which is not held, states the same Main Theorem (pp. 1--2) but
numbers its lemmas differently and proves Proposition 1 by another route;
the source card's label map relates the two.

**Read depth.** Claims checked: the Main Theorem was read clause by clause
on the page image of p. 100 and in the preprint's text layer; the statements
of Propositions 1 and 2 (p. 103) and Lemmas 1--5 were read on the page
images. The proofs were read for structure only and are summarized below,
not verified.

## Proof pointer and sketch

Let $M$ be the least integer with $r\le\sum_{N<n<M}1/n\le r+1/M$, so
$M/N=e^{r+O(1/N)}$ ((3.3), p. 104). Proposition 1 (p. 103) removes terms
$1/d_1,\ldots,1/d_l$ with $N<d_1<\cdots<d_l<M$ so that every prime power
dividing the denominator $v$ of the remaining sum $u/v$ is at most $N^{1/5}$,
the removed reciprocals summing to $\asymp\log\log N/\log N$ ((3.1)--(3.2)). Its
proof (Section IV, pp. 107--110) removes the primes $p_h>\cdots>p_1$ of
$[N^{1/5},N/\log^{10}N)$ from the denominator one at a time, each step deleting
terms $qp_{i-1}n_j$ found by Proposition 2; Lemmas 2 and 4 bound the mass of the
terms removed first, and Lemma 3 (p. 102) sets up each application of
Proposition 2. Proposition 2 (p. 103) represents a rational $A/B$ with
$\gcd(A,B)=1$, all prime power divisors of $B$ at most $M^{1/4-\varepsilon}$ and
$\log\log\log M/\log M\ll A/B\le1$, where $0<\varepsilon<1/8$, as a sum of
distinct unit fractions $1/n_i$ with $M\le n_1<\cdots<n_k\le c(M)M$, each $n_i$
having all prime power factors at most $M^{1/4-\varepsilon}$; here $c(M)$ is
chosen so that the reciprocals of such integers in $[M,c(M)M]$ sum to about
$2A/B$, and $c(M)<e^{v(\varepsilon)A/B}$ (Remark, p. 104). Its proof (Section V,
pp. 110--112) counts representations with exponential sums, the large
frequencies controlled by Lemma 5 (p. 112), whose proof (Section VI, pp.
112--114) uses de Bruijn's smooth-number estimate (Lemma 1, p. 102, for each
fixed $\varepsilon<3/5$ uniform in $y\ge2$ and
$1\le u\le\exp((\log y)^{3/5-\varepsilon})$) through (2.1). Applying Proposition
2 with $\varepsilon=1/20$ to $A/B=r-u/v\asymp\log\log N/\log N$ supplies the
missing mass with denominators below
$e^{v(1/20)A/B}M=(e^r+O_r(\log\log N/\log N))N$ (p. 104).

Sharpness (pp. 105--107): if $r=1/x_1+\cdots+1/x_k$ and $Z=\max x_i$, every
prime dividing some $x_i$ is below $Z(1+o(1))/\log Z$, and with (3.4), (3.5)
and Lemma 4 (p. 106) this forces denominators in $(N,cN)$ to have
$c\ge e^r(1+(r+o(1))\log\log N/\log N)$, an error of order
$\log\log N/\log N$.

## Relation to Problem 295

With $r=1$ the theorem gives, for every $N>1$, a representation
$1=\sum1/x_i$ with $N<x_1<\cdots<x_k\le(e+O(\log\log N/\log N))N$. Such a
representation has $k=(e-1)N+O(N\log\log N/\log N)$ terms: its
denominators are distinct integers of that interval, so
$k\le(e-1)N+O(N\log\log N/\log N)$, and since they exceed $N$,
$1\le\sum_{N<n\le N+k}1/n$ gives $k\ge(e-1)N-O(1)$. The theorem therefore
gives $k(N)\le(e-1)N+O(N\log\log N/\log N)$, weaker than the Erdős–Straus
bound $k(N)<(e-1)N+c_1N/\log N$; it gives no lower bound on $k(N)$, and it
neither proves nor refutes the divergence of $k(N)-(e-1)N$.
The preprint's introduction (p. 1) quotes the two questions of Erdős and
Graham that the theorem answers, on representations of $1$ with bounded ratio
$x_k/x_1$ and on the limit inferior $e$ of that ratio.

## Relation to Problems 284, 286 and 319

With $r=1$ the theorem gives, for every $N>1$, a representation
$1=\sum_{i=1}^k1/x_i$ with $N<x_1<\cdots<x_k\le(e+o(1))N$. Such a
representation has $k>N$ terms, since each term is below $1/N$, and at most
$(e-1+o(1))N$ terms, since its denominators are distinct integers of the
interval. So for every $k$ that occurs in this way, the largest possible
smallest denominator satisfies $f(k)\ge x_1>N\ge(1-o(1))k/(e-1)$ (the
question of Problem 284), and the denominators lie in an interval of width
below $(e-1+o(1))N<(e-1+o(1))k$ (the question of Problem 286 in the
erdosproblems.com wording); the set of such $k$ is infinite because $k>N$. The
theorem's statement does not say which $k$ occur, and the published introduction
claims the two questions "for infinitely many $k$" only. These two
deductions are written here for the problem pages; they are not in the
paper. For Problem 319 the erdosproblems.com commentary applies the theorem at
$N'=(1/e-o(1))N$ to obtain a set $B\subseteq(N',N]$ with reciprocal sum
$1$, so that $A=B\cup\{1\}$ with the sign $+1$ on $1$ and $-1$ on $B$ has
signed reciprocal sum $0$; that construction is recorded on the problem
page.

## Dependencies

Lemma 1 (de Bruijn's estimate for smooth numbers, p. 102); the prime number
theorem and Mertens' estimate for $\sum_{p\le n}1/p$, used in Lemma 4 and
Sections V--VI; Bertrand's postulate (Section IV).

## Bears on

- [[../wiki/problems/unit_fractions/E0284/_index|Problem 284]]: with $r=1$, the largest
  possible smallest denominator is $(1+o(1))k/(e-1)$ for the infinitely
  many $k$ that occur as term counts of the constructed representations;
  the published introduction (p. 100) claims the question "for infinitely
  many $k$", not for every $k$.
- [[../wiki/problems/unit_fractions/E0286/_index|Problem 286]]: the same representations
  answer erdosproblems.com's width question, with the constant $e-1$, for the
  same infinitely many $k$; the paper's own form of the question has width
  $\sim k$.
- [[../wiki/problems/unit_fractions/E0295/_index|Problem 295]]: adjacent result on the
  interval containing the denominators; the upper bound
  $k(N)-(e-1)N=O(N\log\log N/\log N)$ it implies is weaker than the
  Erdős–Straus $O(N/\log N)$, and it says nothing on the divergence.
- [[../wiki/problems/unit_fractions/E0319/_index|Problem 319]]: the source of the lower
  bound $(1-1/e+o(1))N$ in the erdosproblems.com commentary.
