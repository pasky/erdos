---
name: problems/analysis/E0256
title: Problem 256
desc: |
  Asks for estimates of the largest $f(n)$ such that
  $\max_{\lvert z\rvert=1}\lvert\prod_i(1-z^{a_i})\rvert\geq f(n)$ for every
  choice of $n$ integers $1\leq a_1\leq\cdots\leq a_n$.
tags:
- Analysis
status: solved
claim: disproved
parts: [power_growth]
created: 2026-09-04T09:17:27Z
updated: 2026-10-18T10:11:14Z
---

# Problem 256

[[problems/analysis/_index|..]]

[[problems/analysis/E0256/claims/_index|claims/]]: The 1 claim page of Problem 256, one per claimant's result; the problem's standing derives from them.

***

**Statement.** Let $n\geq 1$ and $f(n)$ be maximal such that for any integers
$1\leq a_1\leq \cdots \leq a_n$ we have

$$
\max_{\lvert z\rvert=1}\left\lvert \prod_{i}(1-z^{a_i})\right\rvert\geq f(n).
$$

Estimate $f(n)$ - in particular, is it true that there exists some constant
$c>0$ such that

$$
\log f(n) \gg n^c?
$$

**Formulation.** The second question is the part `power_growth`. The first asks for an estimate with no target, so it is open-ended: it is not a part, and it never blocks the standing.

**Status.** Solved: an accepted partial claim settles the definite second part
in the negative, and the open-ended estimate does not block the standing. The
erdosproblems.com label was OPEN (page last edited 20 January 2026). The
erdosproblems.com commentary answers the specific question no. Belov and
Konyagin proved $\log f(n)\ll(\log n)^4$
([[problems/analysis/E0256/claims/1996_12_01_belov_konyagin|their 1996 paper]],
an accepted partial claim on its refereed publication). Estimating $f(n)$
remains open.

**Source.** [erdosproblems.com/256](https://www.erdosproblems.com/256), accessed
2026-09-04. Cite as: T. F. Bloom, Erdős Problem #256,
https://www.erdosproblems.com/256.

**References.**

- [At61] Atkinson, F. V., On a problem of Erdős and Szekeres. Canad. Math. Bull.
  (1961), 7-12.
- [BeKo96] Belov, A. S. and Konyagin, S. V., An estimate for the free term of a
  nonnegative trigonometric polynomial with integer coefficients. Mat. Zametki
  (1996), 627-629. The erdosproblems.com key names this short note, Mat. Zametki
  59 (1996), no. 4, 627-629 (Math. Notes 59 (1996), no. 4, 451-453), which
  bounds the least constant term of a nonnegative cosine polynomial with integer
  coefficients
  ([[../library/analysis/belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial/_index|card]]).
  The bound $\log f(n)\ll(\log n)^4$ that the erdosproblems.com commentary
  credits to [BeKo96] is in the authors' paper An estimate of the free term of a
  non-negative trigonometric polynomial with integer coefficients, Izv. Math.
  60 (1996), no. 6, 1123-1182 (Russian original Izv. Ross. Akad. Nauk Ser.
  Mat. 60 (1996), no. 6, 31-90). Tang's Proc. Amer. Math. Soc. paper cites
  that paper for the bound, and the claim page records it.
- [BoCh18] [[../library/analysis/bourgain_2018_paper_erdos_szekeres/_index|Bourgain, J. and Chang, Mei-Chu, On a paper of Erdős and Szekeres]].
  J. Anal. Math. (2018), 253-271.
- [ErSz59] Erdős, P. and Szekeres, G., On the product
  $\prod_{k=1}^n(1-z^{a_k})$. Acad. Serbe Sci. Publ. Inst. Math. (1959), 29-34.
- [Od82] Odlyzko, A. M., Minima of cosine sums and maxima of polynomials on the
  unit circle. J. London Math. Soc. (2) (1982), 412-420.
- [Ta26] Tang, Quanyu, An improved lower bound for Erdős–Szekeres products.
  Proc. Amer. Math. Soc. 154 (2026), no. 8, 3381-3388, DOI 10.1090/proc/17668;
  arXiv:2509.14182. Not an erdosproblems.com reference; added for the lower
  bound $f(n)\ge2\sqrt n$.

**Formalization.** None recorded.

## Current assessment

The erdosproblems.com formulation asks for two things: an estimate of $f(n)$,
the least over all choices of $n$ exponents $1\le a_1\le\cdots\le a_n$ of the
maximum modulus on the unit circle of $\prod_i(1-z^{a_i})$, and whether
$\log f(n)\gg n^c$ for some $c>0$. Bloom's catalog labeled the problem OPEN
(page last edited 20 January 2026), and its commentary answers the second
question no. The standing targets the question as stated.

Upper bounds. Erdős and Szekeres [ErSz59]
([[../library/analysis/erdos_1959_product/_index|card]]) proved
$\lim f(n)^{1/n}=1$, so $f(n)$ grows more slowly than any exponential, and
noted the bound $f(n)>\sqrt{2n}$. Erdős proved by probabilistic methods that
$\log f(n)\ll n^{1-c}$ for some $c>0$, as the erdosproblems.com commentary
records. Atkinson [At61]
([[../library/analysis/atkinson_1961_problem_erdos_szekeres/_index|card]])
proved $\log f(n)\ll n^{1/2}\log n$, and Odlyzko [Od82] improved this to
$\log f(n)\ll n^{1/3}(\log n)^{4/3}$. Belov and Konyagin proved
$\log f(n)\ll(\log n)^4$, in the Izvestiya paper that the References
annotate; this answers the second question no, and is recorded as an accepted
partial claim on
[[problems/analysis/E0256/claims/1996_12_01_belov_konyagin|their claim page]],
on its refereed publication alone, since the erdosproblems.com label was OPEN.
For the variant $f^*(n)$ with distinct exponents $a_1<\cdots<a_n$, Bourgain and
Chang [BoCh18]
([[../library/analysis/bourgain_2018_paper_erdos_szekeres/_index|card]])
proved in
[[../library/analysis/bourgain_2018_paper_erdos_szekeres/proposition_1_1|Proposition 1.1]]
that some set of $n$ distinct exponents in $\{1,\ldots,N\}$, with $n$
comparable to $N/2$, has product maximum at most
$\exp(c(n\log n)^{1/2}\log\log n)$. The paper states this only at the sizes its construction produces. The
[[research/erdos_256/distinct_exponent_cardinality_extension|block-dilation deduction]]
extends the same bound to every sufficiently large cardinality, with no
linear bound on the largest exponent. The deduction uses the published
dense-block theorem and is author-recorded. [BoCh18]
also recalls, as Atkinson's relation (1.9), a link between $f^*$ and the
Chowla cosine problem, [[problems/analysis/E0510/_index|Problem 510]]: with
$M_2(n)$ the infimum, over integers $a_1<\cdots<a_n$, of
$-\min_\theta\sum_j\cos(a_j\theta)$ (1.8), $\log f^*(n)\ll M_2(n)\log n$.
So if some set $A$ of $n$ distinct integers has
$\sum_{a\in A}\cos(a\theta)\ge-M$ for every $\theta$, then
$\log f^*(n)\ll M\log n$. The erdosproblems.com commentary words the hypothesis
the other way round, that every set of $n$ integers has a $\theta$ with
$\sum_{a\in A}\cos(a\theta)<-M_n$; as written that is a lower bound for
every set and gives no upper bound for $f^*(n)$, and it matches (1.9) only
when $M_n$ is the optimal constant $M_2(n)$.
Atkinson's 1961 paper [At61] states no such result: its closing remarks
(pp. 11--12) only suggest, for $f(n)$ with repeated exponents allowed, a
connection with the minimum of a sum of cosines.

Lower bounds. The bound $f(n)\ge\sqrt{2n}$ of Erdős and Szekeres stood until
Tang [Ta26] proved $f(n)\ge2\sqrt n$ in a refereed paper. The improvement
settles no instance of the problem, since it fixes neither the order of $f(n)$
nor an answer to either question, so it has no claim page.

Search scope: the erdosproblems.com page and commentary (last edited 20 January
2026), the community database (which recorded the problem as unformalized on
2026-10-07), the formal-conjectures catalog (no statement file for the problem
on that date) and the arXiv and Crossref records of Tang's paper. No proof claim
is recorded for the problem. Remaining gaps: the order of $f(n)$, between
$2\sqrt n$ and $\exp(C(\log n)^4)$; no proof has been compiled or independently
reviewed by this corpus.

**A deduction and its scope.**
[[research/erdos_256/distinct_exponent_cardinality_extension|Distinct exponent products at every cardinality]] gives the author-recorded
argument and source boundaries: integer dilations combine Bourgain–Chang dense blocks into every prescribed cardinality with the same logarithmic norm order, without a linear frequency bound.

<!-- BEGIN problem library links -->

## Linked library material

These entries are derived from explicit links on library pages. They are
navigation only and do not by themselves record mathematical progress.

- [[../library/analysis/atkinson_1961_problem_erdos_szekeres/_index|atkinson_1961_problem_erdos_szekeres]]
- [[../library/analysis/atkinson_1961_problem_erdos_szekeres/inequality_5|atkinson_1961_problem_erdos_szekeres / inequality_5]]
- [[../library/analysis/atkinson_1961_problem_erdos_szekeres/lemma_1|atkinson_1961_problem_erdos_szekeres / lemma_1]]
- [[../library/analysis/atkinson_1961_problem_erdos_szekeres/lemma_2|atkinson_1961_problem_erdos_szekeres / lemma_2]]
- [[../library/analysis/belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial/_index|belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial]]
- [[../library/analysis/belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial/corollary_1|belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial / corollary_1]]
- [[../library/analysis/belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial/corollary_2|belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial / corollary_2]]
- [[../library/analysis/belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial/theorem_1|belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial / theorem_1]]
- [[../library/analysis/belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial/theorem_2|belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial / theorem_2]]
- [[../library/analysis/belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial/theorem_3|belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial / theorem_3]]
- [[../library/analysis/belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial/theorem_4|belov_1996_estimate_free_term_nonnegative_trigonometric_polynomial / theorem_4]]
- [[../library/analysis/bourgain_2018_paper_erdos_szekeres/_index|bourgain_2018_paper_erdos_szekeres]]
- [[../library/analysis/bourgain_2018_paper_erdos_szekeres/proposition_1_1|bourgain_2018_paper_erdos_szekeres / proposition_1_1]]
- [[../library/analysis/bourgain_2018_paper_erdos_szekeres/proposition_1_2|bourgain_2018_paper_erdos_szekeres / proposition_1_2]]
- [[../library/analysis/bourgain_2018_paper_erdos_szekeres/proposition_1_3|bourgain_2018_paper_erdos_szekeres / proposition_1_3]]
- [[../library/analysis/erdos_1959_product/_index|erdos_1959_product]]
- [[../library/analysis/erdos_1959_product/theorem_1|erdos_1959_product / theorem_1]]
- [[../library/analysis/erdos_1959_product/theorem_2|erdos_1959_product / theorem_2]]
- [[../library/analysis/erdos_1959_product/theorem_3|erdos_1959_product / theorem_3]]

<!-- END problem library links -->
