---
name: research/erdos_699/archive/previous_bounds/seven_nine_bounds
title: "Erdős 699: complete exclusion at seven and nine"
desc: "Both seven and nine are completely excluded. The complete cutoff is nine; four fixed indices at least four still lack effective bounds."
created: 2026-09-22T17:12:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: complete exclusion at seven and nine

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[Complete cutoff nine](../../proofs/details/cutoff_9.md)

**Seven and nine are completely excluded**, for the original threshold
$p\ge i$. Their [seven](../../proofs/details/index_7_complete.md) and
[nine](../../proofs/details/index_9_complete.md) combined proofs join fully
numerical infinite tails to completed finite ranges. Neither index has a
remaining exceptional set.

The current classification is:

| Index | Result |
| --- | --- |
| $1,2,7$ and every $i\ge9$ | No bad triples. |
| $4,5,6,8$ | Finiteness is known; effective row bounds remain missing here. |
| $3$ | Global finiteness remains unproved. |

Only four fixed indices remain among $i\ge4$. Their finiteness is known;
effective row bounds are still missing here.

## How the two ranges at seven meet

Put $h=n-6$. All five initial cofactor alternatives and all 258 joint
inequalities now hold for $h\ge10^{100000000}$. The exact relaxed
polynomial forest needs only $h\ge10^{99990923}$. The completed finite
proof covers $n\le10^{100000001}$, so every row is excluded.

The main additional step is the
[block adjustment lemma](../../methods/details/pade_block_adjustment.md).
When the Padé index is chosen below its nominal value, the residual
prime-power denominator cost decreases. Quantifying that saving lets
one approximant certify a whole interval of logarithmic heights.
Chains of such intervals reach the already numerical uniform tails.
The source clauses and their exact polynomial coverage are retained.

The [initial-source chains](../../proofs/details/index_7_initial_height_cover.md)
contain 122868 witnesses. Among the joint sources, 43 hold directly by
uniform estimates and 215 are covered by 9811438 exact witnesses in
187 direction groups. Every direction is covered without a gap.

The [finite proof](../../proofs/details/index_7_finite.md) has 18000 certified
intervals, 28 residual rows, and 41740 exact column checks. Its extension
to $10^{100000001}$ reuses the lower stages and adds eight exponent
anchors for each of the three prime pairs. No interpolation rank is
recomputed by the combined checker.

## How the two ranges at nine meet

Put $h=n-8$. All initial and joint sources, and the exact polynomial
coverage, apply for $h\ge10^{241547627}$. The
[finite proof](../../proofs/details/index_9_finite.md) covers
$n\le10^{241547629}$, so the ranges overlap and all rows are excluded.

The [initial-source covers](../../proofs/details/index_9_initial_height_cover.md)
contain 299324 retained witnesses. Eleven pair sources imply the nineteen
initial pair alternatives; four ordinary product sources provide the other
initial constraints. Among the 790 joint clauses, 440 hold directly at
the target height and 350 are covered by 11599987 exact witnesses in
321 direction groups. Every direction is covered without a gap.

The relaxed polynomial proof checks all 104976 labeled position and
cofactor cases with 24322 exact rational Farkas leaves. The finite proof
retains 607975 certified intervals, thirteen residual rows, and 6762 exact
column checks. The six extended prime-pair certificates add no exceptions.
All pieces are bound by the [combined checker](../../computations/erdos_699_index_9_complete.py)
and [proof record](../../computations/erdos_699_index_9_complete.json).

## Improvements shared by the two calculations

The numerical proofs use several complementary changes:

- [Explicit Padé constants](../../methods/details/joint_numerical_thresholds.md)
  account for the integral prefactors and residual denominators.
- [Sharper Chebyshev estimates](../../methods/details/sharp_theta_gcd.md)
  improve the uniform coefficient-gcd estimates.
- The initial endpoints are weakened by $10^{-4}$ and joint thresholds
  by individually certified amounts; exact replacement forests check all
  these changes together.
- Integer Newton bases and actual Farkas margins reduce the polynomial
  coefficient requirements.
- [Arithmetic nonvanishing at seven](../../proofs/details/index_7_nonvanishing.md)
  and [nine](../../proofs/details/index_9_nonvanishing.md) removes the largest
  common-zero height bounds.
- The [prime-power gcd lemma](../../methods/details/prime_power_gcd.md) includes
  powers of primes in the approximation divisor and removes an unnecessary
  floor-stability restriction.

For comparison, the original index-seven polynomial exponent was
$19813540001$. The sharper coefficient and nonvanishing argument lowers
it to $44245906$ for the original clauses, or $99990923$ for the relaxed
clauses used in the complete proof. At nine, the corresponding final
polynomial exponent is $241547627$, replacing $5109634000001$.

## The four indices still lacking effective bounds

At six, [a degree-twelve product and a column valuation identity](../../remaining/details/index_6_carry_constraints.md)
force all three selected primes into their high-residue branches in a
specified cofactor box, for $n-5\ge10^{425}$. At eight, an
[exact column valuation argument](../../remaining/details/index_8_carry_constraint.md)
excludes one Lucas residue branch in a difficult configuration. These
are conditional restrictions, not whole-index effectivity results.

Exact line coverings at [six](../../remaining/details/index_6_curve_obstruction.md)
and [eight](../../remaining/details/index_8_curve_obstruction.md) prove that no
polynomial of any degree can give the required strict weighted degree
gain at the specified hard profiles. Controlling common curve zeros alone
cannot remove that obstruction; stronger arithmetic input is needed.

The [Runge criterion](../../methods/details/runge_curve_criterion.md)
makes bad pairs on a fixed curve effectively determinable when enough
numerator fibers contribute poles. For four and five, three finite pole
fibers suffice. It does not put all bad pairs on finitely many such curves.
The cubic results remain unchanged.
