---
name: theory/analysis/L165_consecutive_gap_growth_conjunction
title: The three mean-normalized consecutive-gap divergences
desc: "The three mean-normalized consecutive-gap divergences over all circle sequences and the distinct-point subclass, with a passing independent whole-conclusion grade at tier 1; catalog acceptance remains pending."
id: L165
statement: |
  Let A be the family of all infinite sequences on R/Z, allowing repetitions,
  and D its subfamily with distinct terms. For n >= r, sort the first n
  labels by position, breaking ties by arrival index, extend real lifts by
  y_(i+n) = y_i + 1, and let M_n^(r), m_n^(r) be the largest and smallest
  y_(i+r)-y_i over 1 <= i <= n. Interpret M/0 as positive infinity.
  There are absolute c > 0 and integer r0 such that, for every integer
  r >= r0 and every X in A, the two separate limsups of n M_n^(r)-r and
  r-n m_n^(r) are at least c sqrt(log r), and
  limsup_n M_n^(r)/m_n^(r) >= 1 + log(r)/(200r), with natural logarithms.
  For either F = A or F = D, define Lambda_r^F = inf_(X in F) limsup_n
  n M_n^(r), lambda_r^F = sup_(X in F) liminf_n n m_n^(r), and
  mu_r^F = inf_(X in F) limsup_n M_n^(r)/m_n^(r).
  Then Lambda_r^F-r and r-lambda_r^F are at least c sqrt(log r), and
  r(mu_r^F-1) is at least log(r)/200, for all integer r >= r0.
  All three expressions tend to positive infinity through the integers.
status: proved
tier: 1
depends_on:
- L163
- L164
created: 2026-10-15T20:39:29Z
updated: 2026-10-20T17:29:46Z
---

# The three mean-normalized consecutive-gap divergences

[[theory/analysis/_index|..]]

[[theory/analysis/L165_consecutive_gap_growth_conjunction/_proof|_proof]]: Checks the common sequence model, absolute quantifiers, separate limits and extremum directions, then restricts to the distinct-point subclass.

[[theory/analysis/L165_consecutive_gap_growth_conjunction/evidence/_index|evidence/]]: Exact subjects, whole-conclusion examination and independent passing grade for the mean-normalized consecutive-gap conjunction.

***

The [proof](_proof.md) composes
[[theory/analysis/L163_all_sequence_span_ratio/_index|L163's universal ratio bound]]
and [[theory/analysis/L164_all_sequence_span_deviations/_index|L164's two separate one-sided bounds]].
Both inputs have their own whole-statement examinations and distinct passing
grades. Their conjunction, its subclass consequence and its exact match to
the modified Statement of [[problems/analysis/E1221/_index|Problem 1221]]
are recorded here by Plasma AI at **tier 1**. The [whole-conclusion examination](evidence/verify/whole_statement/report.md)
has verdict **refutation-failed**, including the match to the supplied
modified Statement. Its [independent whole-contract grade](evidence/verify/whole_statement/grade.md)
is **PASS**, examined on 2026-10-16 UTC. This is the warrant for the
conjunction and its stated consequences; catalog acceptance remains pending.

## Conventions and scope

Spans are forward arcs through $r$ consecutive gaps on the circle of
circumference one. Labels preserve multiplicity and cyclic starting positions;
real lifts distinguish a full turn from a zero span. The $n$ spans sum to
$r$, so $M_n^{(r)}>0$. The two one-sided deviations need not occur at the
same times. The sequence may depend on $r$; $c$ and $r_0$ may not.
The extrema are taken after the limits, separately for each nonempty family.
No equality of extrema between the two families is assumed or established.

The all-sequence conclusion answers the mean-normalized modified Statement,
whose quantities are $\Lambda_r-r$, $r-\lambda_r$ and $r(\mu_r-1)$.
It does not replace the literal erdosproblems.com first two expressions by
an unannounced convention. The problem page records the printed normalization
issue and its source evidence. No optimal constant or attained extremum is
claimed.

## Attribution and standing

The span-to-count mechanism and closing comparisons come from S. Korsky's
unrefereed arXiv:2609.07196v2. Larcher's range splitting supplies the method
of the finite-list input; Halász's planar theorem, as presented by Bilyk,
supplies the other method. The complete local proofs with constants,
coincident-point extension and composition are credited to Plasma AI as a
technical completion of
[[problems/analysis/E1221/claims/2026_09_08_korsky|Korsky's full problem claim]].
The input grades examine the supplied local proofs, not the original
publications. Their source and independence qualifications remain visible on
L163 and L164. The conjunction has its own whole-statement examination and distinct
passing grade; its warrant is separate from the two premise grades.

The current statement, conventions and proof are the examined mathematics.
The grade accepts the complete conjunction, both families' extremal and
divergence consequences, and the exact supplied mean-normalized formulation.
At its final dependency reading on 2026-10-16 UTC, L163 and L164 were proved
at tier 1 without stale standing and matched the frozen interfaces; filing
confirmed those conditions. The grade supplies no original-publication
fidelity, stronger coefficient $1/100$, optimality, attainment, equality of
the two families' extrema, Lean credit or catalog acceptance. The independent
records and their operating disclosures are retained with the evidence. The
[[research/erdos_1221/all_sequence_composition|research argument]]
keeps the complete chain and the unexamined stronger-constant alternatives.
