---
name: research/sidon_extremal_error/evidence
title: Evidence
desc: Exact finite checks of degree-two moments, lattice capacities, Singer arc discrepancy, and the genuine block law's short-count covariance, with separately scoped exploratory computations.
tags: []
sources: []
created: 2026-10-15T18:08:57Z
updated: 2026-10-15T18:08:57Z
---

# Evidence

[[research/sidon_extremal_error/_index|..]]

***

The [entry point](main.py) checks the finite statements behind the notes of
this folder. It verifies the explicit degree-two family of the
[[research/sidon_extremal_error/linear_capacity_barrier|linear-capacity note]]
in exact rational arithmetic at sample sizes, every constraint included, with
a floating-point eigenvalue control and a negative control just beyond the
family's limit. It checks the integer parameter conditions of the proof on the
whole closed-form range for $48\le N\le 200000$, and the window inequality at
the sample points. For the rotated perturbed lattice it computes the exact
expected difference counts of the unconditioned process at two sample sizes
and checks them, with the conditioning factor of the proof, against the
capacities. For the
[[research/sidon_extremal_error/perfect_difference_cuts|perfect-difference note]]
it builds Singer sets for $q\in\{5,7,11,13,17\}$, checks the perfect difference
property and checks every arc of every unit dilate against the ceiling. The
full run also brackets an auxiliary circulant linear-program threshold at
$N=1000$ between the coefficients $0.583$ and $0.596$. This program omits sum
capacities; its floating-point solver reports are uncertified and do not
establish feasibility of the full relaxation. The lattice convolution
uses exact integer autocorrelation counts and a second-difference recurrence,
checked against direct enumeration on a small input. Its capacity comparisons
are rational. The parameter-range scan likewise uses integer inequalities.

The
[[research/sidon_extremal_error/short_count_covariance|short-count covariance formulas]]
are checked against every outcome of the unrotated block law at
$(s,W)=(2,4),(3,4),(3,6),(4,6)$. All means, covariance entries and the
two-kernel decomposition are compared in exact rational arithmetic. Both
run modes include these four complete sample spaces, the largest of which
has $\binom{6}{4}^4=50625$ outcomes. This finite check supports the exposed
counting formulas; it is not a positivity certificate for a Sidon repair.

The fixed-seed short-pair simulation is exploratory: it permits coincident
labeled positions and does not certify a repaired moment functional. The
precise quartic obstruction has its own
[[theory/additive_bases/L217_sidon_block_quartic_obstruction/evidence/_index|exact finite witness and direct-enumeration control]].

Run from the repository root with
`uv run --no-sync python wiki/research/sidon_extremal_error/evidence/main.py`;
the full run takes about a minute and uses under 3 GiB, with one thread;
`--quick` uses smaller samples and takes a few seconds. These are finite
checks of stated samples. The statements for all $N$ rest on the written
proofs.
