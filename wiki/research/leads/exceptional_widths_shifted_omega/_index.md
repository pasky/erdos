---
name: research/leads/exceptional_widths_shifted_omega
title: Density-one widths and shifted prime-divisor counts
desc: An explicit exceptional-width construction answers the modified omega subquestion negatively while leaving uniform-width formulations and the full classification separate.
problems: [122]
research_state: candidate
review_status: reviewed
last_reviewed: 2026-10-14
created: 2026-10-14T18:42:37Z
updated: 2026-10-15T02:28:16Z
---

# Density-one widths and shifted prime-divisor counts

[[research/leads/_index|..]]

[[research/leads/exceptional_widths_shifted_omega/evidence/_index|evidence/]]: Exact mathematical snapshots and independently graded scrutiny of the density-one width construction for omega.

***

[[theory/number_theory/L34_exceptional_widths_for_omega/_index|L34]]
constructs widths $F(x)\to\infty$ with $F(n)/\omega(n)\to0$ on a
set of natural density one, while

$$
\frac{\#\{n\ge1:x<n+\omega(n)<x+F(x)\}}{F(x)}\le7
$$

for every sufficiently large real $x$. The
[[research/leads/exceptional_widths_shifted_omega/evidence/verify/width_counterexample/_index|independent examination and separate passing grade]]
of 2026-10-14 accept this complete argument for the $\omega$ subquestion
under the literal modified statement of
[[problems/arithmetic_functions/E0122/_index|Problem 122]]. They do not
classify all $f$; their source and formulation limits remain explicit.

The source input is the modulus-one specialization of
[[../library/arithmetic_functions/erdos_1997_locally_repeated_values_arithmetic_functions_iv/lemma_1|the published second-moment inequality]].
It makes atypical inputs sparse. Counting how often their images enter
short intervals makes atypical interval locations sparse as well.
The proof permits short widths elsewhere and widths of order $x$
at exceptional locations. Density-one smallness allows this definition.
The argument establishes neither infinitude of the exceptional set nor
failure of an everywhere-small condition for this particular $F$.
No conclusion is claimed about the different formulation requiring
$F(n)=o(\log\log n)$ everywhere or about monotone widths.

The construction is compatible with
[[../library/arithmetic_functions/erdos_1997_locally_repeated_values_arithmetic_functions_iv/theorem_1|large point multiplicities in the published paper]]:
the widths may be enlarged at those exceptional images. The
[[problems/arithmetic_functions/E0122/claims/1997_01_01_erdos_pomerance_sarkozy|unpublished affirmative report]]
is retained at its recorded standing. Its original passages and any
unpublished proof have not been inspected for their width convention.
Reconciling that historical formulation is a separate source obligation;
it is not an extra premise of L34. The divisor-function case and the
whole classification remain outside this result.
