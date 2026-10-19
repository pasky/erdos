---
name: research/erdos_644/independent
title: Independent
desc: Unverified independent inputs, preserved separately from checked topical arguments.
tags: [unverified, research-input]
sources: []
created: 2026-09-22T23:43:04Z
updated: 2026-10-13T05:28:09Z
---

# Independent

[[research/erdos_644/_index|..]]

[[research/erdos_644/independent/complete_family_limit_and_seven_edge_obstruction|complete_family_limit_and_seven_edge_obstruction]]: Unverified independent input; checked certificates, a corrected finite example, and stronger existing results are recorded in topical notes.

[[research/erdos_644/independent/fano_ground_set_and_coding_constructions|fano_ground_set_and_coding_constructions]]: Unverified independent input; selected claims were checked, corrected, or superseded in the topical research notes.

[[research/erdos_644/independent/fractional_reductions_and_good_triples|fractional_reductions_and_good_triples]]: Unverified independent record; checked overlaps, stronger parity-union failure, and qualifications are documented in topical notes.

***

The inputs retain their original mathematical text, including claims needing
qualification. Checked topical notes, not this archive, record the verified
statements and their precise scope. None of these reviews resolved either
assertion of Problem 644.

The review of the first record is incorporated into
[Certificates and obstructions](../certificates_and_obstructions.md),
[Complete families](../complete_families.md),
[Structural reductions](../structural_reductions.md),
[Convex-profile amplification](../convex_profile_amplification.md),
[Exterior transversal model](../exterior_transversal_model.md),
[Coding refinement](../coding_refinement.md), and
[Random thinning obstruction](../random_thinning_obstruction.md).

## Review of the second record

The fractional inequalities and complete-family limit agree with the established
arguments.
[Complete families](../complete_families.md#equivalent-fractional-formulations)
identifies its $M_r$ with $1/\lambda_r$ and relates the sufficient fractional
threshold to the existing weighted obstruction. That page also retains the
correction to the survey's reported floor formulas; the discrepancy is not
explained by small-family vacuity.

[Certificates and obstructions](../certificates_and_obstructions.md#checking-the-independent-hub-construction)
verifies the hub threshold but proves it is dominated by the existing adaptive
certificate. It retains the disjoint-edge rectangle formulation as a
necessary-condition reduction, not a complete characterization, and
distinguishes the explicit $33/40$ upper allocation from the unverified solver
optima.
[Convex-profile amplification](../convex_profile_amplification.md#uniform-upward-shadows-of-disjoint-parity-copies)
checks the proposed three-block parity failure and strengthens it to every
number of copies $m\ge2$.

Several proposed directions are already more sharply restricted:
[Coding refinement](../coding_refinement.md) fills the Fano-classification gap
only for $4n-7k<k/17$ and excludes the stated distance criteria;
[Helly and chromatic reduction](../helly_and_chromatic_reduction.md) gives a
logarithmic bound for the proposed graph construction;
[Boolean reductions](../boolean_reductions.md) gives the weaker, exact
$(r-1)$-wise inner-intersection condition for universal substitution;
[Structural reductions](../structural_reductions.md) compares its core and
criticality claims with explicit obstructions and the later moment deletion
theorem.

The convergence inequalities in §7.3 remain sufficient but unproved for
unrestricted families. Existing
[block-profile convergence](../block_profile_convergence.md) and
[matroid-base bounds](../matroid_base_families.md) are stronger restricted
results, not a way to remove that gap. The independent upward-shadow operation
is not a [join layer](../join_layer_families.md), so the local-template theorems
do not by themselves prove its failure; the explicit seven-row witness does.

## Review of the third record

The input was compared with the linked topical notes, not treated as
an established proof. Its named auxiliary files
complete_family_model.md, scaling_and_shifting.md,
static_avoidance_analysis.md, two_profile_analysis.md, and
fractional_cover_analysis.md are absent from this research folder.
Claims retained below were checked from their displayed arguments
or proved in the existing notes.

[Complete families](../complete_families.md#the-independent-row-normalized-linear-programs)
identifies its $d_r$ with $\rho_r=1/(1-\lambda_r)$ and verifies the
private-padding argument. Its complete-family convergence is not a new
unrestricted convergence theorem. The finite compactness and fractional bounds
reproduce
[Structural reductions](../structural_reductions.md#fractional-restrictions).
For rank at most $k$, the incidence probability sum is at most $k$, not
necessarily equal to it. Its projective examples are correct: hyperplanes of
$\mathrm{PG}(s,q)$, $s=\lceil r/2\rceil$, have $\tau^*=q+(q-1)/(q^s-1)$ and
$\tau=q+1$, and satisfy $P_{2s}$. These match the general examples in
[Incidence moments](../incidence_moment_rounding.md). The complement
reformulation presumes $|V|\ge2$ and $0\le t\le|V|$ to avoid vacuous subset
quantifiers.

[Static certificates](../certificates_and_obstructions.md#review-of-the-independent-static-certificates)
verify §7 but already give a stronger asymmetric criterion. The claimed solver
optima remain uncertified.
[Block-profile families](../block_profile_families.md#a-checked-six-spectrum-certificate-from-the-independent-input)
retain the useful six-spectrum realization and show that the proposed
two-profile theorem is subsumed by the bound $3k/4+16$ for all full two-block
profile families. The numerical endpoint candidate has
[$\tau=95$, not $93$](../certificates_and_obstructions.md#endpoint-two-profile-candidate-a-finite-correction);
the explicit seven-edge failure of $P_7$ remains valid.

[Clone substitution](../convex_profile_amplification.md#exact-universal-condition-for-complete-clone-classes)
sharpens the input's sufficient condition to the exact universal criterion
$(r-1)(N-s)<N$, with asymptotic multiplier $1/(r-2)$. This still loses ratio for
$r\ge4$; it is not a necessity statement for a fixed special seed. The shift
example is a relabeling of the existing rank-three example, but its
[shared-padding extension](../compression_obstructions.md#the-same-failure-at-every-uniformity)
validly extends the failure to every $k\ge3$, retaining $\tau=3$. The Cartesian
union product still has the minimum, not the sum, of the factor transversal
numbers. Tuza completion is not merely unverified as a locality-preserving
operation: [Exterior transversal model](../exterior_transversal_model.md)
already gives an explicit failure.

[Coding refinement](../coding_refinement.md) records where existing
Fano classification and XOR obstructions go beyond §9, while keeping
their different ranges separate. The suggested structural core or
dense/sublinear dichotomy remains unproved in the needed form:
exact critical traces, low-influence normalization, and safe
[guard projection](../nonuniform_guard_fibres.md) still do not give a
rank-sensitive, $P_7$-preserving reduction with controlled loss.
