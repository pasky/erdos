---
name: research/erdos_699/proofs/details/index_7_initial_height_cover
title: "Erdős 699: the initial index-seven cofactor bounds from a numerical height"
desc: "Two exact boxed Padé covers lower the remaining initial pair thresholds to h=10^100000000, with all 122868 witnesses retained and independently replayed."
created: 2026-09-22T00:00:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: the initial index-seven cofactor bounds from a numerical height

[[research/erdos_699/_index|P699 research]] ·
[[research/erdos_699/methods/details/pade_block_adjustment|Choosing the Padé index]]

***

All five initial cofactor alternatives in the relaxed index-seven proof
hold for

$$
h=n-6\ge10^{100000000}.\tag{1}
$$

Three alternatives already have smaller numerical thresholds. The two
remaining alternatives are

$$
u_2>h^{.2675}\quad\text{or}\quad u_5>h^{.2710},
$$
$$
u_2>h^{.2678}\quad\text{or}\quad u_5>h^{.2678}.\tag{2}
$$

Here $p^{v_p(n-r_p)}u_p=n-r_p$, with the selected numerator factors in
$[h,h+6]$. The
[checker](../../computations/erdos_699_index_7_initial_height_cover.py)
and [full witness chains](../../computations/erdos_699_index_7_initial_height_cover.json.gz)
prove (2) throughout the interval from (1) to the previously certified
numerical tails. Those tails complete the assertion for every larger
height.

**Complete result.** The [combined proof](index_7_complete.md)
excludes every admissible bad triple at seven. The source and
polynomial estimates below are retained as components of that proof.

## The exact target box

Assume both cofactor upper bounds in one alternative hold, and write
$x=\log h$. For a fixed integer Padé index $m$, the denominator cost is
bounded by

$$
D(x)=\sum_p\bigl(\kappa_pm-b_p(1-e_p)x\bigr)_+,
$$

where $\kappa_p=L_{s(p)}a_p\log p$, $a_p$ is the seed exponent,
$b_p$ is the product multiplicity, and $e_p$ is the explicit target.
There is no requirement that $m$ be at most the source's original
block parameter times $x$.

The first term of the nonzero-integer estimate decreases with $x$.
For the second term, $d x+D(x)$ is the maximum of the affine functions

$$m\sum_{p\in J}\kappa_p+
\left(d-\sum_{p\in J}b_p(1-e_p)\right)x,$$

indexed by subsets $J$ of the prime components. There are four such
functions in each case here. Thus two rational endpoint checks for each
affine function certify the entire interval. The
[boxed sparse-witness helper](../../computations/erdos_699_off_diagonal_boxed_sparse.py)
rounds the $\kappa_p$ upwards and the intrinsic decay rates downwards,
then performs the interval checks using integer and rational arithmetic.

The Padé index is chosen near the balanced value or a point at which one
of the denominator contributions vanishes. These choices are only
proposals. Each accepted index has an independently checked pointwise
coefficient-gcd lower bound and strict interval inequalities.

## Complete interval chains

The prime-log prefix through $10^9$ is shared with the other source
calculations and loaded read-only. Proper prime powers through $10^{14}$
give additional certified logarithmic weight. Each coefficient-gcd
calculation uses 8000 disjoint BFT intervals and applies to both adjacent
Padé rectangles. No uniform estimate over untested intermediate indices
is assumed: a single tested integer $m$ proves an entire interval of
real logarithmic heights.

| Targets for $(2,5)$ | Directions | Witnesses | Numerical tail exponent |
| --- | --- | ---: | ---: |
| $(.2675,.2710)$ | $(35,8,35)$ | 75734 | 922680314061 |
| $(.2678,.2678)$ | $(79,18,79)$ | 47134 | 2790743305738 |

Both chains start at the integer 230258508, which is strictly below
$100000000\log10$. Each right endpoint is exactly the next interval's
left endpoint. Their final endpoints exceed the logarithms of the two
displayed numerical tails. The complete 122868-step certificate records
every Padé index, interval endpoint, coefficient-gcd lower bound, and
number of prime intervals used.

An independent replay recomputed every retained pointwise gcd bound and
every rational interval inequality. It used the existing prime cache;
no second prime sieve or binomial-row search was performed.

## Verification

The ordinary checker command replays the full certificate, using the
shared prime cache:

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_7_initial_height_cover.py
```

For a combined proof wrapper, `check(data, replay_gcd=False)` verifies
all source bindings, every interval inequality, and complete coverage.
Setting `replay_gcd=True` additionally recomputes the pointwise gcd
bounds. The returned summary also checks that the other three initial
alternatives have thresholds below (1).
