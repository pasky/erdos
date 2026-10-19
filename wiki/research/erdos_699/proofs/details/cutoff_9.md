---
name: research/erdos_699/proofs/details/cutoff_9
title: "Erdős 699: complete exclusion for every index at least nine"
desc: "Complete numerical source covers and finite certificates settle nine and seven. Every i>=9 and i=1,2,7 is excluded; only four fixed indices at least four remain."
created: 2026-09-22T18:43:52Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: complete exclusion for every index at least nine

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

***

**Theorem.** For every admissible triple $1\le i<j\le n/2$ with
$i\ge9$, a prime $p\ge i$ divides both $\binom ni$ and $\binom nj$.
The cases $i=1,2,7$ are also completely settled.

The [previous cutoff-ten proof](../../archive/previous_bounds/cutoff_10.md) handles
every $i\ge10$. The [new complete proof at nine](index_9_complete.md)
closes the remaining case. Independently, the
[complete proof at seven](index_7_complete.md) removes
that exceptional index as well. Both use the original prime threshold.

## How the two new complete proofs close

| Index | Numerical tail, in $h=n-i+1$ | Completed finite range |
| --- | --- | --- |
| $7$ | $h\ge10^{100000000}$ | $n\le10^{100000001}$ |
| $9$ | $h\ge10^{241547627}$ | $n\le10^{241547629}$ |

In each row the two ranges overlap after the shift from $h$ to $n$.
Every admissible row and column is therefore excluded.

The [block adjustment lemma](../../methods/details/pade_block_adjustment.md)
accounts for the smaller residual denominator cost when the Padé index
changes. Each selected approximant then certifies an interval of
logarithmic heights. Complete chains reach the numerical uniform tails,
while keeping the cofactor clauses used by the polynomial forest.

At seven, five initial alternatives and 258 joint clauses are covered.
At nine, eleven pair sources imply nineteen initial alternatives, four
ordinary product sources provide additional constraints, and all 790
joint clauses are covered. The combined checkers verify the source
bindings and exact relaxed polynomial coverage, then join the analytic
ranges to the retained finite certificates.

| Index | Initial Padé witnesses | Joint Padé witnesses | Exact Farkas leaves | Finite intervals | Residual rows | Exact column checks |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| $7$ | 122868 | 9811438 | 3388 | 18000 | 28 | 41740 |
| $9$ | 299324 | 11599987 | 24322 | 607975 | 13 | 6762 |

The proofs also use integer Newton bases for coefficient bounds and
arithmetic nonvanishing to remove the largest common-zero bounds.
The original interpolation ranks are retained. These are
computer-assisted proofs with exact integer and rational certificates
and directed analytic estimates.

The [index-seven combined checker](../../computations/erdos_699_index_7_complete.py)
and [index-nine combined checker](../../computations/erdos_699_index_9_complete.py)
have matching [seven](../../computations/erdos_699_index_7_complete.json)
and [nine](../../computations/erdos_699_index_9_complete.json) proof records.
Their notes give the individual source and finite-certificate replays.

## What remains

Any counterexample must have $i\in\{3,4,5,6,8\}$.

| Index | Status |
| --- | --- |
| $4,5,6,8$ | Finiteness is known, but no effective row bounds are established here. |
| $3$ | Global finiteness remains unproved; a bad row must exceed $10^{19}$ and have $v_2(n)\ge49$. |

The complete conjecture for $i\ge4$ is reduced to four fixed indices.
New [column restrictions at six](../../remaining/details/index_6_carry_constraints.md)
and [eight](../../remaining/details/index_8_carry_constraint.md) constrain difficult
configurations. Exact all-degree polynomial obstructions at
[six](../../remaining/details/index_6_curve_obstruction.md) and
[eight](../../remaining/details/index_8_curve_obstruction.md) show that stronger
arithmetic input is needed at the specified cofactor profiles.
