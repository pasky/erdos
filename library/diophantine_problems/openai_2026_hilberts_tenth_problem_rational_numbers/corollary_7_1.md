---
name: diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/corollary_7_1
title: "Corollary 7.1: rational solvability has Turing degree 0', also in total degree at most four"
desc: |
  The manuscript's consequence of Theorem 1.1: rational solvability of
  integer polynomials has the degree of the halting problem, and stays
  undecidable for total degree at most four and for sums of squares of
  quadratics. Claims checked only.
created: 2026-10-12T23:13:55Z
updated: 2026-10-12T23:13:55Z
---

***

## Statement

With the usual effective coding, let $\mathrm{H10}(\mathbb Q)$ be the set of
integral polynomials, in any number of variables (the number being part of
the input), that have a rational zero.

**Corollary 7.1.** $\mathrm{H10}(\mathbb Q)$ has Turing degree $0'$, the
degree of the halting problem. So does each of the following restricted
problems:

- (i) rational solvability for integral polynomials of total degree at most
  four;
- (ii) given a nonempty finite list
  $q_1,\ldots,q_s\in\mathbb Z[X_1,\ldots,X_N]$, each of total degree at
  most two, whether $\sum_{i=1}^sq_i^2$ has a zero in $\mathbb Q^N$.

No bound is placed on the number of variables, on the number $s$ of
summands in (ii), or on the heights of the coefficients. In particular
neither restricted problem is decidable.

The proof notes its limits (p. 57): the many-one reductions run from
$\mathrm{H10}(\mathbb Q)$ to the two restricted problems, while the reduction
from integer solvability $\mathrm{H10}(\mathbb Z)$ to
$\mathrm{H10}(\mathbb Q)$ remains a Turing reduction, and the argument "does
not establish many-one completeness" of $\mathrm{H10}(\mathbb Q)$; the list
in (ii) is part of the input; and the construction bounds neither the number
of variables nor the coefficient heights and "gives no single existential
definition of $\mathbb Z$ in $\mathbb Q$".

**Source.** OpenAI, *Hilbert's tenth problem over the rational numbers*,
release folder
`preprints/Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026`;
TeX file `build/sections/07-consequences.tex`, label
`thm:degree-normal-form` (lines 8--23), PDF p. 56; the proof follows at
lines 25--108 and closes on PDF p. 57. Read 2026-10-12. Provenance and
attestations are on
[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/_index|the card]].

**Read depth.** Claims checked: the statement and its definitions were read
clause by clause in the TeX source. The proof, which rests on
[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/theorem_1_1|Theorem 1.1]]'s
reduction, was read for its structure only; no step was checked. Nothing
here is independently reviewed.

## Proof pointer

The decision procedure in the proof of Theorem 1.1 can be run with an oracle
for $\mathrm{H10}(\mathbb Q)$ in place of a hypothetical algorithm. Its finite
tests are uniformly computable from $f$ once the fixed arithmetic data are
hardcoded, and each test makes finitely many oracle queries, so one oracle
machine gives $\mathrm{H10}(\mathbb Z)\le_{\mathrm T}\mathrm{H10}(\mathbb Q)$.
Those data are shown to exist, not computed; the text says their existence
suffices (p. 12), so the proof shows that such a machine exists without
exhibiting it.
The Davis--Putnam--Robinson--Matiyasevich theorem in Davis's form
(Theorem 8.1 of his 1973 survey), with positive-integer unknowns replaced by
$1+u_1^2+u_2^2+u_3^2+u_4^2$ through the four-square theorem, reduces the
halting set many-one to $\mathrm{H10}(\mathbb Z)$; since rational
solvability is computably enumerable, $\mathrm{H10}(\mathbb Q)$ has degree
exactly $0'$.

For the restricted forms, the proof follows the normalization of Davis's
Theorem 7.5 over $\mathbb Q$. An arithmetic circuit computing $f$ gets one new
variable per node and one equation of degree at most two per node (copy an
input or a constant, add, multiply), plus the equation setting the output to
zero. Each rational input extends uniquely to a solution of the gate
equations, so $f$ has a rational zero exactly when the list of these
quadratics has a common rational zero, which over $\mathbb Q$ happens exactly
when the sum of their squares vanishes. Expanding the sum gives an integral
polynomial of degree at most four. These are computable many-one reductions
from $\mathrm{H10}(\mathbb Q)$ to problem (ii) and from (ii) to (i); both
targets are computably enumerable, so both have degree $0'$.

## Dependencies

[[diophantine_problems/openai_2026_hilberts_tenth_problem_rational_numbers/theorem_1_1|Theorem 1.1]]
and the reduction in its proof, with all the inputs listed on that page;
Davis, *Hilbert's tenth problem is unsolvable* (1973), Theorems 7.5 and 8.1
and p. 234; Lagrange's four-square theorem. None of these inputs was
checked here.

## Bears on

The manuscript names no Erdős problem, and no problem page is identified as
using this corollary.
