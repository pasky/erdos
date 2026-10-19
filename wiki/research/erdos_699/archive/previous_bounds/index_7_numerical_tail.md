---
name: research/erdos_699/archive/previous_bounds/index_7_numerical_tail
title: "Erdős 699: a numerical stopping bound for index seven"
desc: "Five numerical pair sources, 258 joint inequalities and exact relaxed polynomial coverage give n<10^3906174477003 for every bad triple at seven."
created: 2026-09-22T00:00:00Z
updated: 2026-10-14T00:26:52Z
---

# Erdős 699: a numerical stopping bound for index seven

***

This is a retained earlier research note. The [[research/erdos_699/_index|current reading guide]] gives the latest status and distinguishes completed proofs from remaining cases.

[[research/erdos_699/_index|P699 research]] ·
[[problems/factorials_binomials/E0699/_index|Erdős problem 699]] ·
[Original effective proof](../../proofs/details/index_7_effective.md)

**Theorem.** Every bad triple $(n,7,j)$ for the original threshold
$p\ge7$ satisfies

$$
\boxed{n<10^{3\,906\,174\,477\,003}.}
$$

All constants are numerical. The
[aggregate checker](../../computations/erdos_699_index_7_numerical_tail.py)
and [certificate](../../computations/erdos_699_index_7_numerical_tail.json)
combine the sources and polynomial coverage. A separate
[finite exclusion](../../proofs/details/index_7_finite.md) covers the lower
range. The subsequent interval covers join these ranges and complete the case.

**Complete result.** The [combined proof](../../proofs/details/index_7_complete.md)
excludes every admissible bad triple at seven. The source and
polynomial estimates below are retained as components of that proof.

## Initial pair alternatives

Put $h=n-6$. Choose $r_p\in\{0,\ldots,6\}$ maximizing
$v_p(n-r_p)$ for each $p\in\{2,3,5\}$, and write
$n-r_p=P_pu_p$, $e_p=\log u_p/\log h$.
The initial alternatives have the form $e_p>\alpha$ or $e_q>\beta$.
Their endpoints are smaller by $1/10000$ than in the original proof.

| $(p,q)$ | $(\alpha,\beta)$ | Sufficient exponent $K$ for $h\ge10^K$ |
| --- | --- | ---: |
| $(2,3)$ | $(.2920,.2920)$ | 1674735 |
| $(2,3)$ | $(.3295,.2915)$ | 3990256 |
| $(2,5)$ | $(.2675,.2710)$ | 922680314061 |
| $(2,5)$ | $(.2678,.2678)$ | 2790743305738 |
| $(3,5)$ | $(.2561,.3773)$ | 19729939 |

The [initial-source checker](../../computations/erdos_699_index_7_base_pairs_numerical_relaxed.py)
retains a rational upper bound for each positive-part denominator cost,
a uniform coefficient-gcd estimate, and all finite Padé constants.
Completed finite gcd certificates improve three of the starting bounds.
The symmetric $(2,5)$ source uses seed $128-125=3$ and directions
$(79,18,79)$. Its bound is the largest initial-source contribution.

## The 258 joint sources

The original clauses are

$$
\sum_p(g_p+b_pe_p)_+\ge R.
$$

Their intercepts, sign regions and block parameters $t$ are retained;
the right sides are replaced by $R-\eta$. Usually $\eta=1/10000$.
The five exceptions are stored exactly in the
[relaxed coverage certificate](../../computations/erdos_699_index_7_relaxed_sources.json).
For each of the 210 distinct direction triples, choose a rational gcd
rate $\ell$ at least the maximum of

$$
\ell_{\mathrm{old}}-\frac{3\eta}{4t}
$$

over its sources. This preserves at least $\eta/4$ of additional
analytic margin in every clause. The
[uniform gcd certificates](../../computations/erdos_699_index_7_gcd_numerical.json)
use the [sharper Chebyshev estimates](../../methods/details/sharp_theta_gcd.md)
and have numerical starting indices $m_0\le10^{12}$.

The [explicit finite-constant argument](../../methods/details/joint_numerical_thresholds.md)
then evaluates every joint source. The
[258 numerical records](../../computations/erdos_699_index_7_joint_numerical.json)
include the seed, directions, weakened target, gcd starting index,
integral prefactors and directed decay comparisons. Before adjusting the witness block, their largest
height exponent was

$$
K_{\rm original}=20219858230830.
$$

It comes from `source_361`, with directions $(10,5,11)$,
$t=6689537/311451090$, $m_0=10^{12}$, and
$\eta=6367/10^9$. Pair gaps are bounded by six and degree-two product
gaps by 36. Actual gap zero is included by the same integer argument.

## Adjusting the witness blocks

The [block adjustment lemma](../../methods/details/pade_block_adjustment.md)
reduces the residual denominator cost when a smaller Padé block is chosen.
The original intercepts and weakened thresholds stay fixed. The
[adjusted source certificates](../../computations/erdos_699_index_7_reblocked_numerical.json)
and [checker](../../computations/erdos_699_index_7_reblocked_numerical.py)
recompute all 210 uniform gcd bounds and all 258 numerical source bounds.
Seventy-five analytic margins and 180 individual stopping bounds improve.

The new common joint-source exponent is

$$
K_{\rm joint}=3906174477002.
$$

The maximum now comes from `source_039`, with directions $(20,9,20)$,
block parameter $7705356/693042767$, and $m_0=10^{11}$.
The former maximum, `source_361`, falls to exponent $4047680442$.

## Polynomial coverage and the final bound

The exact [relaxed forest](../../computations/erdos_699_index_7_relaxed_sources.py)
covers all 540 original position and minimal-cofactor cases, using
4336 nodes and 3388 rational Farkas leaves. It verifies the weaker
initial endpoints and all joint weakenings together. Its weighted
coefficient requirement is

$$
\frac{40482625000000}{404863}<99990923.
$$

The [Newton-basis coefficient bounds](../../proofs/details/index_7_polynomial_bounds.md)
and [arithmetic nonvanishing](../../proofs/details/index_7_nonvanishing.md)
therefore give the polynomial starting height $h\ge10^{99990923}$.
Coincident positions and the central column are covered by the original
reductions. Existing interpolation ranks are reused.

The joint-source exponent exceeds the initial-source and polynomial
exponents. Consequently badness implies $n-6<10^{3906174477002}$.
Adding one decimal power absorbs the shift and proves the theorem.

The aggregate names every input by basename and loads it, matches all
source identifiers and targets, checks every exact Farkas leaf, and
lists its inputs by basename in its own output as a run record, not
as a condition for running. Run

```sh
.venv/bin/python wiki/research/erdos_699/computations/erdos_699_index_7_numerical_tail.py
```

The additional `--sources` option regenerates all 210 analytic gcd
bounds, all 258 original and adjusted joint thresholds, and the five initial source thresholds.
It does not repeat interpolation ranks or enumerate binomial rows.
