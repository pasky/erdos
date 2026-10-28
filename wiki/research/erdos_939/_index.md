---
name: research/erdos_939
title: Sums of coprime r-powerful numbers
desc: "Reconstruction of the binomial construction of r-powerful sums of r-2 coprime r-powerful numbers for r at least 6; r=4 and finiteness at r=5 remain open."
tags: []
sources: []
created: 2026-09-28T04:32:26Z
updated: 2026-10-28T16:29:39Z
---

# Sums of coprime r-powerful numbers

[[research/_index|..]]

[[research/erdos_939/connections|connections]]: Assesses, as mathematics, what the reconstructed binomial construction gives
for the open cases of Problem 939 and for Problems 940, 1107 and 937: a
proved transfer lemma for monomial substitution, a proved Mason-Stothers
obstruction to every polynomial family with two summands for r at least 3,
a four-term quintic identity over the cube roots of unity that is not real,
and the precise reasons the other transfers fail.

[[research/erdos_939/evidence/_index|evidence/]]: Independent focused review and distinct grade of the Theorem 1
reconstruction page, with no executable evidence and no tier.

[[research/erdos_939/theorem_1_reconstruction|theorem_1_reconstruction]]: Reconstructs the binomial construction of infinitely many r-powerful
numbers that are sums of r-2 distinct, positive, jointly coprime
r-powerful numbers for every r at least 6, with the distinctness step
supplied.

***

## What this folder holds

Research on [[problems/diophantine_problems/E0939/_index|Problem 939]], which asks,
for $r\ge4$, whether a sum of $r-2$ coprime $r$-powerful numbers can be
$r$-powerful and whether there are at most finitely many such sums, and,
for $r=3$, whether there are infinitely many coprime $3$-powerful triples
$a+b=c$. The folder holds the author-recorded reconstruction of Theorem 1
of the manuscript held by the
[[../library/diophantine_problems/price_2026_infinite_r_powerful_sums/_index|Price (2026)]]
card, whose statement and proof sketch are on the card's
[[../library/diophantine_problems/price_2026_infinite_r_powerful_sums/theorem|result page]],
the [[research/erdos_939/connections|connections page]], and the review
records under [[research/erdos_939/evidence/verify/_index|evidence/verify/]].
The problem page carries the mathematical status; nothing here changes it.

## Where things stand

**Reviewed.** Each reconstruction page was independently reviewed as it
stood on 2026-09-28T05:03:27Z by a focused review filed under
[[research/erdos_939/evidence/verify/_index|evidence/verify/]], with a distinct
grade of the one report. As
[[research/erdos_939/evidence/verify/grade|the grade]] records it, the verdict
is: Theorem 1, fidelity faithful with correction C1 in the Boundary prose
outside the statement and the proof, and argument sound. The report was graded
pass, not void. The one correction, C1, was applied, so the current text differs
from the reviewed text at the one place the grade names, the "Formal
counterpart" paragraph of the Boundary section. No tier is assigned and the
problem's status is unchanged. After the review, line wrapping was normalized on
the reconstruction pages; no formula or sentence changed. The
[[research/erdos_939/connections|connections page]] and its lead were then
independently reviewed as they stood on 2026-09-28T13:50:48Z by eight focused
reviews and
[[research/erdos_939/evidence/verify/connections_grade|a distinct grade]],
whose outcome is that all eight reviews pass, sixteen corrections (C1 to C16)
are accepted and applied, every claim on them is refutation-failed
once the corrections are in, the lead counts as reviewed, and no tier is
assigned. After both reviews, the sentences on the reconstruction and
connections pages that cited Lean proofs of the Problem 940 arguments were
removed, leaving links to the arguments themselves, and the remarks on the
summand convention of those Lean statements were removed; no step of any
argument changed.

**Reconstructed.** The manuscript's Theorem 1, that for every $r\ge6$ there
are infinitely many $r$-powerful $N$ which are sums of exactly $r-2$
distinct, positive, jointly coprime $r$-powerful numbers, is written out
step by step in
[[research/erdos_939/theorem_1_reconstruction|the reconstruction page]],
with the distinctness of the summands, which the manuscript asserts but
does not argue, supplied and labeled. The same statement is kernel-checked
in Lean as `infinite_rpowerful_sums` inside the file that the
[[../library/diophantine_problems/conjectures_io_2026_erdos_939_lean_r_powerful_sums/_index|Conjectures.io card]]
records, by Conjectures.io's kernel and not built here; it is not a native claim
of this repository.

**Not reconstructed.** The $r=3$ part of the problem is resolved in the
refereed literature by
[[../library/diophantine_problems/nitaj_1995_conjecture_erdos_3_powerful_numbers/_index|Nitaj (1995)]]
and
[[../library/diophantine_problems/cohn_1998_conjecture_erdos_3_powerful_numbers/_index|Cohn (1998)]];
the corpus holds only bibliographic cards for both, their texts are not
held, so their constructions cannot be reconstructed against an artifact.
The held
[[../library/diophantine_problems/walsh_2024_question_erdos_powerful_numbers_elliptic_curve/_index|Walsh (2024)]]
preprint gives a further $3$-powerful construction and is not treated here.

**Open.** The exponents $r=4$ (no example known) and $r=5$ (examples known,
finiteness open). The binomial mechanism cannot reach them: the identity has
$\lceil r/2\rceil+1$ summands before any splitting, which exceeds $r-2$ for
$r\le5$, and splitting only adds summands. A different identity with fewer
monomials, or a construction of a different kind, would be needed.

**Mechanism and leads.** The mechanism is the polynomial identity
$(X+Y)^r-(X-Y)^r=\sum_{j\ \mathrm{odd}}2\binom rjX^{r-j}Y^j$, in which
every right-hand term is a monomial divisible by $Y$; evaluating at
$X=q^r$ and $Y=B^r$, with $B$ carrying every coefficient prime and $q>B$
prime, makes each monomial and both $r$-th powers $r$-powerful, and the term
$(X-Y)^r$, coprime to $XY$, gives the joint coprimality. The same
substitution turns any integer identity among monomials into an identity
among $r$-powerful numbers, at the cost of the number of terms. The
positive-lower-density arguments for the complement in the sibling
[[problems/diophantine_problems/E0940/_index|Problem 940]] rest on sieve
arguments unrelated to this identity and are not affected by it. The
[[problems/diophantine_problems/E0940/claims/2026_07_26_beyer_de_ryke|cubic claim of Beyer de Ryke]]
and the
[[problems/diophantine_problems/E0940/claims/2026_10_28_plasma_ai|quartic claim of Plasma AI]]
are accepted on the
[[../library/diophantine_problems/plasma_ai_2026_powerful_sum_complements/_index|separate Lean formalization]].
The [[research/erdos_940/quartic_complement|quartic prose argument]] retains its
own author-recorded standing.

**Connections.** [[research/erdos_939/connections|The connections page]]
transports the mechanism to the problems it touches. It separates the
substitution into a transfer lemma, proves by the Mason–Stothers inequality
that no polynomial family of coprime $r$-powerful solutions of $a+b=c$
exists for $r\ge3$, so that the $r=4$ case of this problem and three-term
progressions of $r$-powerful numbers for $r\ge3$ lie beyond every identity
of this kind, exhibits a four-term identity of fifth powers of quadratic
forms over the cube roots of unity that has no real form, and records why
[[problems/diophantine_problems/E0940/_index|Problem 940]] and
[[problems/diophantine_problems/E1107/_index|Problem 1107]] receive no transfer and
why [[problems/diophantine_problems/E0937/_index|Problem 937]] needs none. The one
route it opens, a rational four-term identity of $5$-powerful forms that
would refute finiteness at $r=5$, is the lead
[[research/leads/quintic_powerful_identity_route/_index|quintic_powerful_identity_route]].
