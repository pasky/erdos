---
name: research/leads/quintic_powerful_identity_route
title: A Polynomial-Identity Route to Infinitely Many Solutions at r = 5
desc: |
  Reduces the finiteness question of Problem 939 at r = 5 to the existence of
  a rational four-term identity of 5-powerful binary forms of the shape the
  monomial-substitution transfer needs, with the transfer proved, the
  three-term case excluded by Mason-Stothers, a complex four-term identity
  of fifth powers of quadratics that has no real form, and bounded numerical
  searches that found no rational identity in degrees 10 and 15.
problems:
- 939
research_state: candidate
review_status: reviewed
created: 2026-09-28T07:04:05Z
updated: 2026-10-19T04:19:07Z
---

# A Polynomial-Identity Route to Infinitely Many Solutions at r = 5

[[research/leads/_index|..]]

[[research/leads/quintic_powerful_identity_route/evidence/_index|evidence/]]: Two exploratory scripts searching numerically for four-term identities of
fifth powers of binary forms; no entry point, no checks, and no evidence
for any claim.

***

This lead's notes that cite no source are author-recorded research, not claims.

## Target and status evidence

The second question of [[problems/diophantine_problems/E0939/_index|Problem 939]]
at $r=5$: a $5$-powerful number is a positive integer divisible by the fifth
power of each of its prime factors; are there at most finitely many sums of
three jointly coprime $5$-powerful numbers that are themselves $5$-powerful?
The problem page records this as open: two solutions are known, both recomputed
on the problem page, and a
forum-reported search found no further solution with sum below $10^{16}$
except possibly ones in which every pair of summands shares a factor. The
same question is answered negatively for every $r\ge6$ by the binomial
construction reconstructed in
[[research/erdos_939/theorem_1_reconstruction|the Problem 939 research folder]],
and its $r=4$ case is excluded from the polynomial-identity route of
Corollary 3.1 of the connections page, one-parameter families and
polynomially parametrized parameter curves, by the theorem recalled below.
This lead concerns $r=5$ only and the exact erdosproblems.com question, with
"coprime" read as joint coprimality, as the problem page records
erdosproblems.com and the formal-conjectures catalog read it.

## Route

The route is the mechanism of the $r\ge6$ construction with the binomial
identity replaced by an unknown identity with the right number of terms.
Every link is proved on
[[research/erdos_939/connections|the Problem 939 connections page]]; this
page states the chain and its standing.

**Established inputs, at their actual scope.**

- *The transfer (Lemma 1 of the connections page; author-recorded, with
  proof).* Let $A_1+A_2+A_3=A_4$ be an identity in $\mathbb Z[U,V]$ in which
  each $A_i$ is an integer constant $c_i$ times a product of polynomials
  raised to powers at least $5$, $V^5$ divides every $A_i$ with $|c_i|>1$,
  $A_1=K^5$ with $K(U,0)=\pm U^{d}$ and $K(0,V)=\pm V^{d'}$, and $A_2$ is a
  monomial. Then for every $B$ divisible by the primes of the $c_i$ and every
  $m$ coprime to $B$ at which all $A_i(m,B)$ are positive, the three values
  $A_1(m,B),A_2(m,B),A_3(m,B)$ are jointly coprime $5$-powerful integers with
  $5$-powerful sum $A_4(m,B)$; positivity holds for all large $m$ when the
  leading coefficients in $U$ are positive, and then infinitely many distinct
  sums arise.
- *The three-term obstruction (Theorem 3 and Corollary 3.1 there;
  author-recorded, with proof from the Mason–Stothers inequality).* No
  identity $a+b=c$ of pairwise coprime $r$-powerful polynomials, not all
  constant, with $r\ge3$ exists, so the three summands of the premise cannot
  include two proportional polynomials: the identity must have four
  genuinely distinct terms, and the four-summand Brownawell–Masser bound
  recalled on
  [[../library/diophantine_problems/corvaja_zannier_2011_abcd_function_fields/recalled_abc_abcd_bounds|the Corvaja–Zannier source page]],
  $\max\deg\le3(n_0-1)$ with $n_0$ the number of distinct linear factors of
  the product, permits such identities in every degree at least $3$.
- *A complex identity in the least possible degree (Proposition 4 and
  Corollary 4.1 there; author-recorded, with proof).* For a primitive cube
  root of unity $\omega$ and $Q_k=\omega^{2k}U^2+UV-2\omega^kV^2$, one has
  $Q_0^5+Q_1^5+Q_2^5=(3UV)^5$, a four-term identity of fifth powers of
  quadratic forms over $\mathbb Q(\omega)$ with no vanishing proper subsum
  and no common factor. No projective linear change of variables and
  rescaling makes all four forms real, so it yields no identity with four
  rational terms.

**Provisional premise.** *(P)* There is an identity $A_1+A_2+A_3=A_4$ in
$\mathbb Z[U,V]$ satisfying the hypotheses of the transfer with $r=5$, with
positive leading coefficients in $U$ and $A_4(U,B)$ nonconstant for some
admissible $B$.

**Deduction.** Under (P) the transfer produces infinitely many jointly
coprime triples of $5$-powerful integers with $5$-powerful sum, answering the
second question of Problem 939 at $r=5$ in the negative. Whether the
summands are also pairwise distinct, which the formal-conjectures catalog's
finite-set formulation requires and the erdosproblems.com question does not,
follows for all but finitely many $m$ whenever $A_i(U,B)\ne A_j(U,B)$ as
polynomials in $U$.

## What is known about the premise

Over $\mathbb C$ a four-term identity of $5$-powerful forms with one
fifth-power term and one monomial term exists: the complex identity above
has degree $10$, the least possible degree, since degree $5$ would need four
fifth powers of linear forms with zero sum, which the Vandermonde
determinant of their roots excludes except with vanishing subsums; and it is
the only nondegenerate identity of fifth powers of quadratic forms that the
search below found. Over $\mathbb R$, and hence over $\mathbb Q$, no
identity of degree $10$ was found, and the degree-$15$ search restricted to
fifth powers of cubic forms found none either. The shapes $L^6M^9$ and
$L^7M^8$ of degree $15$ ($L,M$ linear), identities mixing shapes among the
four terms, and every degree above $15$ were not searched; $L^5M^{10}=(LM^2)^5$
lies inside the searched shape. The two known solutions at $r=5$ are not
values of any identity found here, and the forum-reported search bound is
mild evidence against a rational identity of small degree and small
coefficients.

## Exploratory computation

Two scripts are retained under this lead's evidence folder as exploratory
computations, not as evidence for any claim; their environment and run
commands are in [the evidence index](evidence/_index.md).

The script `quintic_identity_search.py` searches for identities
$Q_1^5+Q_2^5+Q_3^5+Q_4^5=0$ among binary forms of one degree $d\in\{2,3\}$
over $\mathbb C$ or $\mathbb R$. Every $5$-powerful binary form of degree
$10$ is a constant times the fifth power of a quadratic form, and over
$\mathbb C$ constants are fifth powers while over $\mathbb R$ they are signs
times fifth powers of positive reals, so at $d=2$ the search covers every
four-term identity of $5$-powerful binary forms of degree $10$; at $d=3$ it
covers the shape "fifth power of a cubic" only. It fixes $Q_4$ to one
representative of each orbit of the projective linear group over the field
($UV$ and $U^2$ over $\mathbb C$, with $U^2+V^2$ added over $\mathbb R$ for
$d=2$; $UV(U-V)$, $U^2V$, $U^3$ and, over $\mathbb R$, $V(U^2+V^2)$ for
$d=3$), takes the coefficients of $Q_1,Q_2,Q_3$ as unknowns, and solves the
$5d+1$ coefficient equations by Levenberg–Marquardt from random starts. A
converged point is kept as clean when its residual is below $10^{-13}$
relative to the size of the fifth powers, no form is smaller than a tenth of
the largest, no proper subsum $Q_i^5+Q_j^5$ is below a hundredth of the
largest fifth power, the four forms are not nearly proportional, and they
have no common root; the iteration approaches the degenerate configurations
(a vanishing subsum, or all four forms proportional) without reaching them,
and those limits are the bulk of the converged points. Usage:

```sh
uv run --no-sync --with numpy python wiki/research/leads/quintic_powerful_identity_route/evidence/util/quintic_identity_search.py complex 2 2000
```

with the field, the degree and the number of starts as arguments, and an
optional seed. The runs recorded here, with the printed counts of clean
classes after grouping by gauge-invariant quantities:

| field | degree | starts per gauge | clean classes |
| --- | --- | --- | --- |
| complex | 2 | 2000 | 1 (the identity above) |
| real | 2 | 2000 | 0 |
| complex | 3 | 2000 | 0 |
| real | 3 | 3000 | 0 |

The script `trace_search.py` searches the cyclic shape
$\sum_{k=0}^{2}(Q\circ M^k)^5=I^5$, with $M(U,V)=(-V,U-V)$ the rational
substitution of order three and $I$ an $M$-invariant form of the same
degree as $Q$; the identity above has this shape, since $M$ is the
diagonal substitution of the proposition written in rational coordinates.
For quadratics over $\mathbb C$ it reproduces that family ($300$ starts);
for quadratics over $\mathbb R$ it found only the degenerate case in which
$Q$ is itself invariant ($300$ starts); for cubics over either field none of
$600$ starts converged, which its cruder finite-difference Jacobian may
explain. A finite number of random starts leaves the universal question open
in every case; the runs distinguish an identity that a few thousand starts
would find from one that is absent or hard to reach, and prove nothing.

## Consequential gap

The premise (P) is not established, and the evidence points against its
simplest forms: the only degree-$10$ identity is not real, the degree-$15$
pure-power shape gave nothing over $\mathbb R$, and the abc-type polynomial
bounds neither supply nor exclude an identity in higher degree. A proof that
no four-term identity of $5$-powerful binary forms with real terms exists
would close the homogeneous case of this route; the transfer does not need
homogeneity, and inhomogeneous identities satisfying its hypotheses are a
separate possibility that nothing here examines. Closing the route would
leave $r=5$ to constructions of the kind that settled $r=3$ (recurrences on
a cubic curve, or multiples of a point on an elliptic curve), which this
lead does not attempt.

## Next step

Two bounded computations would decide the low-degree cases. First, extend
the search over $\mathbb R$ to the mixed shapes of degree $15$ and to fifth
powers of quartics (degree $20$), with $Q_4$ fixed in each shape; the script's
gauge and classification code extends to these by listing the shapes'
representatives. Second, decide the degree-$10$ case exactly, by a Gröbner
basis or a resultant computation on the eleven coefficient equations with
$Q_4=UV$, $U^2$ and $U^2+V^2$ and with the degenerate loci saturated out;
this would turn the numerical absence of a real degree-$10$ identity into a
proof. A rational identity found by either computation, checked against the
hypotheses of the transfer, would refute finiteness at $r=5$ and change the
status of the second question; a proof of nonexistence in all degrees would
close the homogeneous case of the route; a negative result in bounded degree
establishes nothing about the target and only narrows where an identity
could live.

## Current review

Reviewed. The route was independently reviewed on 2026-09-28 in the review
records
[[research/erdos_939/evidence/verify/connections_problem_939_at_r_5_three_summands_review|the Problem 939 at r = 5 review]]
(which covers this lead sentence by sentence and re-derives the transfer at
$r=5$, the bridge to Theorem 3 and the search coverage) and
[[research/erdos_939/evidence/verify/connections_shared_results_review|the shared results review]]
(which covers Lemma 1, Theorem 3, Corollary 3.1, Proposition 4 and
Corollary 4.1 of the connections page), and graded in
[[research/erdos_939/evidence/verify/connections_grade|the grade]]. The
graded verdicts of the statements the route rests on are these. Lemma 1,
the transfer: refutation-failed. Its application at $r=5$: the value
statement refutation-failed; the infinitude was proof defective as written,
for want of the nonconstancy hypothesis on $A_4(U,B)$, and is
refutation-failed after C6 under the joint-coprimality reading. Theorem 3
with its sharpness: refutation-failed; Corollary 3.1: refutation-failed,
standing at the author-recorded standing of the Problem 940 proposition it
adapts; the restatement of the obstruction on this page was
refuted-as-stated by $1+1=2$ before C15, and the shape constraint that no two
summands are proportional is refutation-failed with its justification supplied
by C7 on the connections page. Proposition 4 and Corollary 4.1, the complex
identity in the least degree and its non-reality: refutation-failed. The
premise (P) is a provisional premise that nothing establishes, not a claim;
the deduction under (P) was proof defective as written and is
refutation-failed after C6, and its distinctness clause is
refutation-failed. The gap and the closing implications were proof
defective as written, since the transfer does not need homogeneity and
nothing here examines inhomogeneous identities, and are refutation-failed
after C8; the degree-$15$ coverage sentence was refuted-as-stated and is
corrected by C9; the phrase "every polynomial route" in the target
paragraph was unsupported and is refutation-failed after C16. The
corrections the grade accepted were applied, so the current text differs
from the reviewed text at the places the grade names: on this page C6 (the
nonconstancy of $A_4(U,B)$ in (P)), C8 (the homogeneous-case scoping in
"What is known about the premise", "Consequential gap" and "Next step"), C9
(the degree-$15$ coverage) with its counterpart in the docstring of the
retained script, C15 ("not all constant" in the obstruction) and C16 (the
scope of the $r=4$ exclusion); on the connections page C1 to C14, of which
C6, C7, C8 and C9 touch the $r=5$ section this page restates. The searches
remain exploratory, and the grade notes that the degree-$10$ plan of the
Next step needs a real-algebraic step after the Gröbner or resultant
computation, to be named when that computation is run. Since the review, "Target
and status evidence" was restated against the current problem page without a
date; this touches no examined statement, proof, code or input. No tier is
assigned and the status of Problem 939 is unchanged.
