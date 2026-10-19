---
name: arithmetic_functions/leanmeanbean_2026_explicit_bound_erdos_problem_417
title: "LeanMeanBean: An explicit bound for Erdős problem 417"
desc: |
  A two-page note of October 2026, with no author line and hosted on GitHub,
  claiming limsup V(x)/V'(x) <= e^{M_*} < 2.195202 for the two totient counts
  of Problem 417 by bounding how often primes divide least preimages and
  applying Jensen's inequality; it takes two inputs from an unrefereed
  manuscript and settles neither question.
license: unstated
created: 2026-10-14T22:07:06Z
updated: 2026-10-19T04:19:04Z
---

# LeanMeanBean: An explicit bound for Erdős problem 417

[[arithmetic_functions/_index|..]]

[[arithmetic_functions/leanmeanbean_2026_explicit_bound_erdos_problem_417/theorem_1|theorem_1]]: Claims limsup V(x)/V'(x) <= e^{M_*} < 2.195202 for the two totient counts of
Problem 417, where M_* = (log 2)/2 + sum over primes p >= 3 of
p/(p-1)^2 log(p/(p-1)); unreviewed, and resting on Proposition 5.3 of an
unrefereed manuscript.

***

*An explicit bound for Erdős problem 417*, a two-page note (2026) that prints
no author, affiliation or date, hosted in the public GitHub repository
`LeanMeanBean/417` (<https://github.com/LeanMeanBean/417>) as `417.pdf`; the
account name LeanMeanBean is its only attribution. Unrefereed; no arXiv version
is recorded.

**Version.** The copy read for this card is `417.pdf` at the repository's
commit `3620821345595c5e2b60de4f86561e1872c81840`. Provenance: fetched from
<https://raw.githubusercontent.com/LeanMeanBean/417/3620821345595c5e2b60de4f86561e1872c81840/417.pdf>,
259,570 bytes. The PDF's metadata has empty title and author
fields and gives the creation date 10 October 2026 (UTC). No notice is printed
in the file, and the hosting repository (https://github.com/LeanMeanBean/417,
read 2026-10-14) has no license file; the term is unstated.

**Claim.** Theorem 1 (p. 1) states, without hypotheses, that the two counts of
[[../wiki/problems/arithmetic_functions/E0417/_index|Problem 417]], $V(x)$ for
the totients up to $x$ and $V'(x)$ for the distinct values $\varphi(n)$ with
$n\le x$, satisfy

$$
\limsup_{x\to\infty}\frac{V(x)}{V'(x)}\le e^{M_*}<2.195202,
\qquad
M_*=\frac{\log2}{2}+\sum_{p\ge3\text{ prime}}\frac{p}{(p-1)^2}\log\frac p{p-1}.
$$

Its proof (pp. 1--2) compares $V'(x)$ with the sum $W(x)$ of $v/\ell(v)$ over
the totients $v\le x$, where $\ell(v)$ is the least preimage, deriving
$W(x)=V'(x)+o(V(x))$ from the common-prefix estimates of Proposition 5.3 of its
only reference, OpenAI's manuscript *An asymptotic formula for the number of
totients* (filed as
[[arithmetic_functions/openai_2026_asymptotic_formula_number_totients/_index|openai_2026_asymptotic_formula_number_totients]]).
It bounds the proportion of totients whose least preimage is divisible by a
prime $p$ by deleting the power of $p$, using the manuscript's fixed-scale
limit $V(cx)/V(x)\to c$ from its Theorem 2.1, so that the mean of
$\log(\ell(v)/v)$ has limit superior at most $M_*$; Jensen's inequality then
gives $\liminf V'(x)/V(x)\ge e^{-M_*}$. The numerical part (p. 2) bounds
$M_*<0.786274052$ by an exact rational sum over the primes up to $999990$ and
an integral bound for the larger primes.
Standing here: **claimed, unreviewed**.

**Disclosures.** The note prints no acknowledgement and no statement on the use
of AI or other software. Its numerical step reports the outcome of an "exact
rational summation" over primes (p. 2) without naming a program or giving code.

**Read status.** Claims checked: Theorem 1 and the definitions it uses (p. 1)
were read clause by clause on the page images of the PDF. The proof (pp. 1--2)
was read for its structure only and is not verified here; the exact rational
prime sum was not recomputed, and the two results the note imports from the
manuscript stand as the manuscript's card records them. Nothing here is
independently reviewed. Result page:
[[arithmetic_functions/leanmeanbean_2026_explicit_bound_erdos_problem_417/theorem_1|theorem_1]].

**In the corpus.** The project's conditional claim
[[../wiki/theory/number_theory/L44_finite_prime_totient_phase/_index|L44]]
(tier 0, author-recorded) proves its own versions of the note's displays
(1)--(4), in the uniform form that claim needs and from premises taken from the
same manuscript; it does not use the note's numerical bound and is not a review
of the note. The
[[../wiki/research/leads/distinct_totient_preimage_ratio/_index|distinct totient preimage ratio lead]]
records the note's claim beside that reduction.

**Bears on.**
[[../wiki/problems/arithmetic_functions/E0417/_index|Problem 417]]: Theorem 1
claims an explicit constant, $e^{M_*}<2.195202$, for the boundedness of
$V(x)/V'(x)$ recorded on the problem page, resting on the manuscript's
unrefereed Proposition 5.3. It does not show that the limit exists, so it
settles neither question.

No file of this source is held: no license on record permits its redistribution,
and the card cites the edition it names above.
