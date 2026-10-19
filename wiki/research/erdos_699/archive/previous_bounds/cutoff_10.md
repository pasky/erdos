---
name: research/erdos_699/archive/previous_bounds/cutoff_10
title: "Erdős 699: complete exclusion for every index at least ten"
desc: "Fully numerical Padé bounds and completed finite certificates settle indices 12 and 14, lowering the complete cutoff to 10."
created: 2026-09-22T09:10:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: complete exclusion for every index at least ten

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]]

**Theorem.** For every admissible triple $1\le i<j\le n/2$ with
$i\ge10$, a prime $p\ge i$ divides both $\binom ni$ and $\binom nj$.
The cases $i=1,2$ and the [new complete case $i=7$](../../proofs/details/index_7_complete.md) are also settled.

The new complete cases are **$i=12$ and $i=14$**. The
[previous complete proof](cutoff_15.md) already covered
$i=10,11,13$ and every $i\ge15$, so these two cases fill every remaining
gap above nine. The prime threshold remains the original $p\ge i$.

| Remaining index | Current status |
| --- | --- |
| $4,5,6,8$ | Finiteness is known, but no effective row bounds are established here. |
| $3$ | Global finiteness remains unproved. A bad row must exceed $10^{19}$ and have $v_2(n)\ge49$. |

**Subsequent complete cutoff.** The [proof at nine](../../proofs/details/cutoff_9.md)
excludes every $i\ge9$. Seven is also complete. The preceding
proof and its source calculations are retained below.

## The two new complete cases

| Index | Numerical tail bound | Reduced finite cap | Certified intervals | Exact residual rows | Exact column checks |
| --- | --- | --- | ---: | ---: | ---: |
| $12$ | $n<10^{3\,071\,170}$ | $10^{43}$ | $149926$ | $15$ | $1610$ |
| $14$ | $n<10^{8\,516\,269}$ | $10^{41}$ | $400818$ | $0$ | $0$ |

Both bounds are fully numerical. Neither depends on an unevaluated
effective constant. The finite ranges are also completely excluded,
rather than left as possible exceptional sets.

At twelve, [explicit integral and factorial estimates](../../methods/details/off_diagonal_numerical_thresholds.md)
make the twenty unequal-block Padé sources numerical. Finite prime-interval
certificates reduce their coefficient-gcd starting indices to at most
$18795$. The degree-72 ramp then gives the numerical tail in the table.

At fourteen, the [numerical tail proof](../../proofs/details/index_14_numerical_tail.md)
uses 64 selected pair alternatives. Exact coverage of 543 minimal vectors
and 13002 collision-capacity lists gives positive gain $7/625$. The
previously verified $831\times841$ interpolation matrix is retained.
A sharper coefficient estimate supplies the algebraic bound
$10^{6255983}$; the largest source threshold, with the row shift included,
gives $10^{8516269}$.

Both tails lie within the range $10^{15170264}$ of the existing
six-prime strip certificate. Its exponent-$1/3$ pair estimates, combined
with explicit weighted ramps, reduce the finite caps to those in the
table. New exponent-$2/5$ certificates then strengthen every pair on these
smaller ranges. Their exceptional solutions are kept individually and
disable an estimate only on the exact row windows where it could fail.

The completed interval partitions have **550744 certified intervals** in
total. The fifteen residual rows at twelve are all at most 736, and every
admissible column in them is excluded by exact binomial gcd arithmetic.
Fourteen has no residual rows. Every part of each finite range is covered.

The complete proof records are:

- **Twelve:** [proof](../../proofs/details/index_12_complete.md),
  [checker](../../computations/erdos_699_index_12_complete.py), and
  [certificate](../../computations/erdos_699_index_12_complete.json).
- **Fourteen:** [numerical tail](../../proofs/details/index_14_numerical_tail.md),
  [finite proof](../../proofs/details/index_14_finite.md), and the
  [combined checker](../../computations/erdos_699_index_14_complete.py)
  with its [certificate](../../computations/erdos_699_index_14_complete.json).

These are computer-assisted mathematical proofs, with exact integer and
rational certificates and directed analytic bounds. They are not Lean
formalizations. The linked notes give the reproduction commands and
source provenance; the numerical dependencies are
[pinned in the repository](../../evidence/assets/erdos_699_interpolation_requirements.txt).

## Complete exclusion at seven

The [index-seven proof](../../proofs/details/index_7_complete.md) now joins
all five initial and 258 joint numerical source bounds at
$h=n-6\ge10^{100000000}$ to the finite exclusion
$n\le10^{100000001}$. No exceptional set remains at seven.
The block adjustment lemma and exact interval covers supply the missing
analytic bridge.

## Further progress on the remaining indices

The [new quintic cofactor bound](../../remaining/details/index_5_cofactor_range.md)
shows that every sufficiently large bad index-five triple must have
$\{r_2,r_3\}=\{0,1\}$ and

$$
\boxed{(n-4)^{1/100}<u_2,u_3<(n-4)^{57/100}.}
$$

The threshold is effective, but this does not exclude intermediate
cofactor sizes or settle index five.

A new simultaneous-approximation construction has an
[exact three-factor determinant](../other_approaches/multipoint_moments.md),
[additional prime divisibility of its minors](../other_approaches/multipoint_minor_divisibility.md),
and [extra powers of two for the seed $10,9,8$](../other_approaches/multipoint_two_adic.md).
These are proved auxiliary lemmas. They have not yet supplied cofactor
inequalities strong enough to settle six or eight. The complete conjecture
for all $i\ge4$, and the separate cubic finiteness question, remain open.
